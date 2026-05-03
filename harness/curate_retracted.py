#!/usr/bin/env python3
"""
Curate candidate retracted papers from Crossref.

Pipeline:
  1. Query Crossref REST API for retraction-typed updates after a cutoff.
  2. For each candidate, follow the `update-to` relation back to the
     original retracted work and pull title, DOI, journal, abstract,
     license info.
  3. Heuristic screen: open access? has abstract? title looks
     methodological (not "Retraction Note: …")?
  4. Save candidate list to data/retracted/candidates_<batch>.csv for
     downstream LLM-based screening + manual review.

Run:
    python harness/curate_retracted.py --batch v1 --target 30
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "data" / "retracted" / "candidates"
USER_AGENT = "graduated-dissent-bench (mailto:ab@ad-research.org)"


def crossref_get(url: str) -> dict:
    """GET a Crossref endpoint with retry and a courtesy User-Agent."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:
            if attempt == 3:
                raise
            time.sleep(1.5 * (attempt + 1))
    return {}


def fetch_retraction_notices(from_date: str, n: int, cursor: str | None = None) -> tuple[list[dict], str | None]:
    """Page through Crossref retractions; returns items + next cursor."""
    base = "https://api.crossref.org/works"
    params = {
        "filter": f"update-type:retraction,from-update-date:{from_date}",
        "rows": str(min(n, 1000)),
        "select": "DOI,title,issued,update-to,relation,member,container-title,abstract,subject,publisher,type,license,URL",
        "cursor": cursor or "*",
    }
    url = base + "?" + urllib.parse.urlencode(params)
    data = crossref_get(url)
    msg = data.get("message", {})
    items = msg.get("items", [])
    next_cursor = msg.get("next-cursor")
    return items, next_cursor


def looks_misconduct(title: str, notice_text: str | None = None) -> bool:
    """Cheap keyword screen for terms that suggest misconduct / fraud."""
    blob = (title or "") + " " + (notice_text or "")
    blob = blob.lower()
    misconduct_terms = [
        "plagiari", "fabricat", "image manipulat", "image duplica",
        "fraud", "ghost author", "authorship dispute", "paper mill",
        "data fabrication", "duplicate publication", "falsif",
        "copy", "stolen", "ethical violation", "ethics breach",
        "informed consent", "irb violation",
    ]
    return any(t in blob for t in misconduct_terms)


def looks_methodological(notice_text: str) -> bool:
    """Lightweight positive signal for documented methodological errors."""
    blob = (notice_text or "").lower()
    method_terms = [
        "calculation error", "computation", "statistic", "regression",
        "spreadsheet", "formula", "coding error", "code error",
        "data process", "data preparation", "data cleaning",
        "wrong test", "incorrect test", "incorrect analysis",
        "study design", "design flaw", "selection bias",
        "underestimate", "overestimate", "inconsistent",
        "implausible", "impossible", "out of range",
        "denominator", "sample size", "underpowered",
        "unit conversion", "decimal", "log",
    ]
    return any(t in blob for t in method_terms)


def best_title(item: dict) -> str:
    titles = item.get("title") or []
    return titles[0] if titles else ""


def issued_year(item: dict) -> int | None:
    issued = (item.get("issued") or {}).get("date-parts") or []
    if issued and issued[0]:
        try:
            return int(issued[0][0])
        except Exception:
            return None
    return None


def has_open_license(item: dict) -> bool:
    licenses = item.get("license") or []
    for lic in licenses:
        url = (lic.get("URL") or "").lower()
        if any(t in url for t in ["creativecommons", "cc-by", "open"]):
            return True
    return False


def fetch_original_via_update_to(item: dict) -> dict | None:
    """The retraction work's `update-to` array points to the retracted DOI."""
    for u in item.get("update-to", []) or []:
        doi = u.get("DOI")
        if not doi:
            continue
        url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='/')}"
        try:
            data = crossref_get(url)
            return data.get("message")
        except Exception:
            continue
    # Fallback: inspect relations field
    for kind, rels in (item.get("relation") or {}).items():
        if "is-retraction-of" in kind or "retracts" in kind:
            for r in rels:
                doi = r.get("id")
                if doi:
                    try:
                        data = crossref_get(f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='/')}")
                        return data.get("message")
                    except Exception:
                        pass
    return None


def screen_one(retraction: dict) -> dict | None:
    """Return a candidate row, or None to drop."""
    notice_title = best_title(retraction)
    if looks_misconduct(notice_title):
        return None

    # Drop pure "Retraction Note: ..." titles where the notice describes
    # nothing about the actual error.
    abstract = (retraction.get("abstract") or "").strip()
    if not abstract and not notice_title:
        return None

    # Get original paper metadata (preferred for licensing + abstract).
    original = fetch_original_via_update_to(retraction)
    if not original:
        return None

    orig_title = best_title(original)
    if looks_misconduct(orig_title, abstract):
        return None

    notice_year = issued_year(retraction)
    orig_year = issued_year(original)

    open_license_orig = has_open_license(original)
    open_license_notice = has_open_license(retraction)

    return {
        "retraction_doi": retraction.get("DOI", ""),
        "retraction_title": notice_title,
        "retraction_year": notice_year or "",
        "retraction_abstract": abstract.replace("\n", " ")[:1500],
        "original_doi": original.get("DOI", ""),
        "original_title": orig_title,
        "original_year": orig_year or "",
        "container_title": (original.get("container-title") or [""])[0],
        "publisher": original.get("publisher", ""),
        "subject": "; ".join(original.get("subject") or [])[:300],
        "open_access_original": open_license_orig,
        "open_access_notice": open_license_notice,
        "method_signal": looks_methodological(abstract or ""),
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--from-date", default="2024-04-01",
                   help="Earliest retraction-update date (post training cutoff)")
    p.add_argument("--target", type=int, default=200,
                   help="Number of candidates to surface")
    p.add_argument("--batch", default="v1",
                   help="Output batch label, written to candidates_<batch>.csv")
    p.add_argument("--max-pages", type=int, default=20,
                   help="Maximum Crossref pages to walk")
    args = p.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_csv = OUT_DIR / f"candidates_{args.batch}.csv"

    print(f"Querying Crossref retractions from {args.from_date} ...")
    cursor: str | None = None
    keep: list[dict] = []
    total_seen = 0

    for page in range(args.max_pages):
        items, cursor = fetch_retraction_notices(args.from_date, n=200, cursor=cursor)
        if not items:
            break
        for it in items:
            total_seen += 1
            row = screen_one(it)
            if row is None:
                continue
            keep.append(row)
            if len(keep) % 10 == 0:
                print(f"  kept {len(keep)} candidates (seen {total_seen}) ...")
            if len(keep) >= args.target:
                break
        if len(keep) >= args.target or cursor is None:
            break

    print(f"\nKept {len(keep)} candidates of {total_seen} retractions seen.")
    if not keep:
        print("(no candidates passed screening)")
        return

    cols = list(keep[0].keys())
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(keep)
    print(f"Wrote {out_csv.relative_to(REPO)}")


if __name__ == "__main__":
    sys.exit(main() or 0)
