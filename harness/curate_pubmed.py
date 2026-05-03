#!/usr/bin/env python3
"""
Curate candidate retracted papers from PubMed E-utilities.

PubMed retraction records have richer metadata than Crossref's abstract
field. The "Retraction notice" PMID is linked to the original PMID via
RetractionIn / RetractionOf pointers, and the notice text is often more
substantive than Crossref's abstract.

Pipeline:
  1. esearch retracted publications since cutoff -> PMID list
  2. efetch in chunks -> XML records with abstract, title, journal, links
  3. extract original-paper PMIDs from RetractionOf links
  4. emit one row per retracted-original pair
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "data" / "retracted" / "candidates"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def http_get(url: str, retries: int = 3) -> bytes:
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return r.read()
        except Exception:
            if attempt == retries:
                raise
            time.sleep(1.5 * (attempt + 1))
    return b""


def esearch_retractions(from_date: str, retmax: int = 1000) -> list[str]:
    """Return PMIDs of items typed Retraction Notice or Retraction of Publication."""
    # Use [PT]=Retraction of Publication (i.e., the retraction-notice records).
    term = urllib.parse.quote(
        f'retracted publication[pt] AND "{from_date}"[PDAT]:"3000"[PDAT]'
    )
    url = f"{EUTILS}/esearch.fcgi?db=pubmed&term={term}&retmax={retmax}&retmode=json"
    import json
    data = json.loads(http_get(url))
    return data.get("esearchresult", {}).get("idlist", [])


def efetch_records(pmids: list[str]) -> ET.Element:
    """Fetch XML for up to ~200 PMIDs at once."""
    ids = ",".join(pmids)
    url = f"{EUTILS}/efetch.fcgi?db=pubmed&id={ids}&retmode=xml"
    raw = http_get(url)
    return ET.fromstring(raw)


def text_or_empty(node, *path) -> str:
    for tag in path:
        if node is None:
            return ""
        node = node.find(tag)
    return (node.text or "").strip() if node is not None else ""


def all_text(node) -> str:
    if node is None:
        return ""
    return "".join(node.itertext()).strip()


def extract_record(article: ET.Element) -> dict | None:
    """Pull metadata from a single PubmedArticle XML element."""
    pmid = text_or_empty(article, "MedlineCitation", "PMID")
    journal = text_or_empty(article, "MedlineCitation", "Article", "Journal", "Title")
    title_node = article.find("./MedlineCitation/Article/ArticleTitle")
    title = all_text(title_node)
    abstract_nodes = article.findall("./MedlineCitation/Article/Abstract/AbstractText")
    abstract = " ".join(all_text(n) for n in abstract_nodes)

    # Year
    year = text_or_empty(article, "MedlineCitation", "Article", "Journal", "JournalIssue", "PubDate", "Year")
    if not year:
        year = text_or_empty(article, "MedlineCitation", "Article", "Journal", "JournalIssue", "PubDate", "MedlineDate")

    # DOI from elocation IDs
    doi = ""
    for el in article.findall("./MedlineCitation/Article/ELocationID"):
        if el.get("EIdType") == "doi":
            doi = (el.text or "").strip()
            break
    if not doi:
        for el in article.findall("./PubmedData/ArticleIdList/ArticleId"):
            if el.get("IdType") == "doi":
                doi = (el.text or "").strip()
                break

    # Reference to original (the paper this notice retracts)
    original_pmid = ""
    original_doi = ""
    for cs in article.findall(".//CommentsCorrectionsList/CommentsCorrections"):
        if cs.get("RefType") == "RetractionOf":
            opmid_node = cs.find("PMID")
            if opmid_node is not None:
                original_pmid = (opmid_node.text or "").strip()

    # Some XML packages encode PT (publication type) we want to verify
    pubtypes = [all_text(pt) for pt in article.findall("./MedlineCitation/Article/PublicationTypeList/PublicationType")]

    return {
        "notice_pmid": pmid,
        "notice_doi": doi,
        "notice_title": title,
        "notice_abstract": abstract,
        "journal": journal,
        "year": year,
        "publication_types": "; ".join(pubtypes),
        "original_pmid": original_pmid,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--from-date", default="2024/04/01")
    p.add_argument("--retmax", type=int, default=600)
    p.add_argument("--batch", default="pm_v1")
    args = p.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"esearch retractions since {args.from_date} (retmax={args.retmax}) ...")
    pmids = esearch_retractions(args.from_date.replace("-", "/"), retmax=args.retmax)
    print(f"  got {len(pmids)} PMIDs")

    if not pmids:
        return

    rows: list[dict] = []
    chunk = 200
    for i in range(0, len(pmids), chunk):
        batch = pmids[i:i + chunk]
        print(f"efetch {i}..{i+len(batch)} of {len(pmids)} ...")
        try:
            root = efetch_records(batch)
        except Exception as e:
            print(f"  !! efetch failed: {e}")
            continue
        for article in root.findall(".//PubmedArticle"):
            row = extract_record(article)
            if row:
                rows.append(row)
        time.sleep(0.5)  # be nice to NCBI

    print(f"\nParsed {len(rows)} retraction notices")

    # Filter for substantive notices
    rows = [r for r in rows if len(r["notice_abstract"]) > 100]
    print(f"With substantive abstracts (>100 chars): {len(rows)}")

    # Add a quick keyword-based misconduct flag (LLM screen happens later)
    misconduct_terms = re.compile(
        r"plagiari|fabricat|image manipulat|image duplica|duplicate publi|"
        r"paper mill|created.{0,30}sold|integrity concerns|fals(?:e|if)|"
        r"compromised peer review|forged|stolen", re.I)
    for r in rows:
        r["likely_misconduct"] = bool(misconduct_terms.search(r["notice_abstract"]))

    out = OUT_DIR / f"candidates_{args.batch}.csv"
    cols = list(rows[0].keys())
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {out.relative_to(REPO)}")
    print(f"Likely-misconduct: {sum(1 for r in rows if r['likely_misconduct'])}")
    print(f"Likely-methodological (or unclear): {sum(1 for r in rows if not r['likely_misconduct'])}")


if __name__ == "__main__":
    raise SystemExit(main() or 0)
