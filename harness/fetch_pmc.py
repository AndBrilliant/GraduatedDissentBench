#!/usr/bin/env python3
"""
Fetch open-access full text for retracted papers via PubMed Central.

Given a PubMed ID for the original (retracted) paper, look up its PMC ID
via elink, then efetch the JATS-XML full text from PMC. Strip XML, keep
prose. The output is plaintext suitable for downstream anonymization.

Returns None if the paper isn't in PMC's open-access subset.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
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


def pmc_id_for_pmid(pmid: str) -> str | None:
    """elink from pubmed -> pmc; return PMC id (e.g. 'PMC123456')."""
    url = (f"{EUTILS}/elink.fcgi?dbfrom=pubmed&db=pmc&id={pmid}&retmode=json")
    try:
        data = json.loads(http_get(url))
    except Exception:
        return None
    linksets = data.get("linksets", [])
    for ls in linksets:
        for db in ls.get("linksetdbs", []):
            if db.get("dbto") == "pmc":
                ids = db.get("links", [])
                if ids:
                    return f"PMC{ids[0]}"
    return None


def fetch_pmc_xml(pmcid: str) -> ET.Element | None:
    """efetch JATS XML for a PMC ID."""
    pmc_num = pmcid.replace("PMC", "")
    url = f"{EUTILS}/efetch.fcgi?db=pmc&id={pmc_num}&rettype=full&retmode=xml"
    try:
        return ET.fromstring(http_get(url))
    except Exception:
        return None


def jats_to_text(root: ET.Element) -> str:
    """Crude JATS-XML -> plain-text. Preserves section order; drops tables/figures."""
    out_parts: list[str] = []

    # Title
    for ti in root.iter("article-title"):
        if ti.text:
            out_parts.append(ti.text.strip())
        out_parts.append("")
        break

    # Abstract
    for ab in root.iter("abstract"):
        out_parts.append("ABSTRACT")
        for p in ab.iter("p"):
            txt = "".join(p.itertext()).strip()
            if txt:
                out_parts.append(txt)
        out_parts.append("")
        break

    # Body sections
    for body in root.iter("body"):
        for sec in body.findall(".//sec"):
            title_node = sec.find("title")
            if title_node is not None:
                tt = "".join(title_node.itertext()).strip()
                if tt:
                    out_parts.append(tt.upper())
            for p in sec.findall("./p"):
                txt = "".join(p.itertext()).strip()
                # Collapse whitespace
                txt = re.sub(r"\s+", " ", txt)
                if txt:
                    out_parts.append(txt)
            out_parts.append("")
        break

    return "\n".join(out_parts).strip()


def fetch_full_text(pmid: str) -> str | None:
    pmcid = pmc_id_for_pmid(pmid)
    if not pmcid:
        return None
    xml_root = fetch_pmc_xml(pmcid)
    if xml_root is None:
        return None
    txt = jats_to_text(xml_root)
    if len(txt) < 500:
        return None
    return txt


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--pmid", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()
    txt = fetch_full_text(args.pmid)
    if txt is None:
        print(f"No PMC full text for PMID {args.pmid}", file=sys.stderr)
        sys.exit(1)
    Path(args.out).write_text(txt, encoding="utf-8")
    print(f"Wrote {len(txt)} chars to {args.out}")


if __name__ == "__main__":
    main()
