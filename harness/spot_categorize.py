#!/usr/bin/env python3
"""
SPOT error-type categorization + text-detectable subset preparation.

Outputs (under data/spot/):
  text_detectable/<safe_doi>/paper.txt          - text-only paper content
  text_detectable/<safe_doi>/ground_truth.json  - SPOT annotations for this paper
  text_detectable/index.csv                     - one row per text-detectable paper
  text_detectable/SUBSET_REPORT.md              - human-readable summary
  scoring/spot_classification.csv               - all 91 errors with detectability label
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
META_FILE = REPO / "data" / "spot" / "metadata" / "spot_metadata_train.parquet"
PARSED_FILE = REPO / "data" / "spot" / "parsed" / "spot_parsed_train.parquet"
OUT_DIR = REPO / "data" / "spot" / "text_detectable"
SCORING_DIR = REPO / "data" / "spot" / "scoring"

# Mapping from SPOT error_category -> our detectability bucket.
# - text:    fully detectable from prose alone
# - partial: text side may be detectable if the contradiction surfaces in prose
# - figure:  requires vision (image comparison)
DETECTABILITY = {
    "Equation / proof":                    "text",
    "Statistical reporting":               "text",
    "Experiment setup":                    "text",
    "Reagent identity":                    "text",
    "Data inconsistency":                  "text",       # generic; treat as text-detectable
    "Data Inconsistency (text-text)":      "text",
    "Data Inconsistency (figure-text)":    "partial",
    "Data Inconsistency (figure-figure)":  "figure",
    "Figure duplication":                  "figure",
}


def safe_doi(doi: str) -> str:
    """Filesystem-safe DOI/arxiv id."""
    return re.sub(r"[^A-Za-z0-9._-]", "_", doi or "unknown")


def extract_text(paper_content) -> str:
    """
    paper_content is a list of dicts of the form
        {'type': 'text', 'text': '...'} or {'type': 'image_url', 'image_url': '...'}
    Return only the text segments concatenated with double newlines.
    """
    parts: list[str] = []
    if paper_content is None:
        return ""
    for entry in paper_content:
        if not isinstance(entry, dict):
            continue
        t = entry.get("text")
        if t:
            parts.append(str(t))
    return "\n\n".join(parts).strip()


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    SCORING_DIR.mkdir(parents=True, exist_ok=True)

    meta = pd.read_parquet(META_FILE)
    parsed = pd.read_parquet(PARSED_FILE)

    # Per-error detectability classification on full metadata (91 rows)
    meta = meta.copy()
    meta["detectability"] = meta["error_category"].map(DETECTABILITY).fillna("unknown")

    # Save per-error classification
    classification_path = SCORING_DIR / "spot_classification.csv"
    meta.to_csv(classification_path, index=False)

    # Aggregate detectability per paper
    paper_detectability = (
        meta.groupby("title")["detectability"]
        .agg(lambda s: ",".join(sorted(set(s))))
        .to_dict()
    )

    # Papers with at least one text or partial error
    text_detectable_titles = {
        t for t, d in paper_detectability.items()
        if "text" in d or "partial" in d
    }

    # Subset of parsed papers that are text-detectable AND have parsed content
    parsed_titles = set(parsed["title"].unique())
    runnable_titles = text_detectable_titles & parsed_titles

    # Build per-paper records (collapse multi-error rows into lists)
    rows = []
    for title in sorted(runnable_titles):
        paper_rows = parsed[parsed["title"] == title]
        meta_rows = meta[meta["title"] == title]
        # Each row in `parsed` corresponds to ONE annotated error for that paper,
        # so multiple parsed rows per title may exist if a paper has multiple errors.
        # Take the paper_content from the first row (it's identical across rows).
        first = paper_rows.iloc[0]
        doi = first["doi/arxiv_id"]
        safe = safe_doi(doi)
        paper_dir = OUT_DIR / safe
        paper_dir.mkdir(parents=True, exist_ok=True)

        # Paper text
        paper_text = extract_text(first["paper_content"])
        (paper_dir / "paper.txt").write_text(paper_text, encoding="utf-8")

        # Ground truth: list of {location, description, category, severity, detectability}
        gt = []
        for _, mrow in meta_rows.iterrows():
            gt.append({
                "location": mrow["error_location"],
                "description": mrow["error_annotation"],
                "category": mrow["error_category"],
                "severity": mrow["error_severity"],
                "detectability": mrow["detectability"],
            })
        ground_truth = {
            "title": title,
            "doi": doi,
            "paper_category": first["paper_category"],
            "errors": gt,
        }
        (paper_dir / "ground_truth.json").write_text(
            json.dumps(ground_truth, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        # Detectability summary for this paper
        text_errors = sum(1 for e in gt if e["detectability"] == "text")
        partial_errors = sum(1 for e in gt if e["detectability"] == "partial")
        figure_errors = sum(1 for e in gt if e["detectability"] == "figure")

        rows.append({
            "doi": doi,
            "safe_doi": safe,
            "title": title,
            "paper_category": first["paper_category"],
            "n_errors_total": len(gt),
            "n_text": text_errors,
            "n_partial": partial_errors,
            "n_figure_only": figure_errors,
            "paper_text_chars": len(paper_text),
            "primary_severity": meta_rows["error_severity"].mode().iloc[0]
                                 if len(meta_rows) else "",
        })

    index_df = pd.DataFrame(rows).sort_values(["paper_category", "doi"])
    index_df.to_csv(OUT_DIR / "index.csv", index=False)

    # ── Summary report ─────────────────────────────────────────
    total_errors = len(meta)
    text_errors = (meta["detectability"] == "text").sum()
    partial_errors = (meta["detectability"] == "partial").sum()
    figure_errors = (meta["detectability"] == "figure").sum()
    total_papers = meta["title"].nunique()
    text_papers = len(text_detectable_titles)
    runnable_papers = len(runnable_titles)
    parsed_papers = len(parsed_titles)
    parsed_text_runnable = len(runnable_titles)

    by_cat = (
        meta.groupby(["error_category", "detectability"])
        .size()
        .reset_index(name="n")
        .sort_values(["detectability", "n"], ascending=[True, False])
    )

    runnable_by_paper_cat = (
        index_df.groupby("paper_category")["doi"].count().sort_values(ascending=False)
    )

    report_lines = [
        "# SPOT Subset Report",
        "",
        "_Generated by `harness/spot_categorize.py` — do not edit by hand._",
        "",
        "## Totals",
        "",
        f"| Quantity | Count |",
        f"|---|---|",
        f"| Total annotated errors (metadata split) | **{total_errors}** |",
        f"| ↳ Text-detectable | **{text_errors}** |",
        f"| ↳ Partially text-detectable (figure-text contradictions) | **{partial_errors}** |",
        f"| ↳ Figure-only (vision required) | **{figure_errors}** |",
        f"| Total unique papers (metadata) | **{total_papers}** |",
        f"| Papers with parsed content available | **{parsed_papers}** |",
        f"| Papers with ≥1 text-detectable error | **{text_papers}** |",
        f"| **Runnable papers (parsed AND text-detectable)** | **{runnable_papers}** |",
        "",
        "## Errors by category and detectability",
        "",
        "| Error category | Detectability | Count |",
        "|---|---|---|",
    ]
    for _, r in by_cat.iterrows():
        report_lines.append(f"| {r['error_category']} | {r['detectability']} | {r['n']} |")

    report_lines += [
        "",
        "## Runnable papers by paper category",
        "",
        "| Paper category | Runnable papers |",
        "|---|---|",
    ]
    for cat, n in runnable_by_paper_cat.items():
        report_lines.append(f"| {cat} | {n} |")

    report_lines += [
        "",
        "## Per-paper index",
        "",
        f"See [`index.csv`](index.csv) for the full list of {runnable_papers} runnable papers, "
        "with safe DOIs, error counts, and paper text lengths.",
        "",
        "## Notes",
        "",
        "- **Detectability** is a *category-level* heuristic: 'text' means the SPOT category "
        "describes errors that surface in prose (equations, statistics, experiment setup, "
        "reagent identity, text-text inconsistencies); 'partial' means figure-text "
        "inconsistencies where the text side may be visible but the figure side is required "
        "for full verification; 'figure' means image-only errors (figure duplication, "
        "figure-figure inconsistencies) which our text-only pipeline cannot detect by design.",
        "",
        "- The 'partial' bucket is included in the runnable subset because the error "
        "*description* still names a textual claim that can be evaluated even without "
        "seeing the figure. We will be transparent about this in the paper's results section.",
        "",
        "- Papers with multiple errors (some text, some figure) are run as long as at least one "
        "error is text-detectable. Our scoring credits text-detectable errors only.",
    ]

    (OUT_DIR / "SUBSET_REPORT.md").write_text("\n".join(report_lines), encoding="utf-8")

    # ── Console summary ────────────────────────────────────────
    print(f"\nWrote {classification_path.relative_to(REPO)}")
    print(f"Wrote {(OUT_DIR / 'index.csv').relative_to(REPO)} ({runnable_papers} papers)")
    print(f"Wrote {(OUT_DIR / 'SUBSET_REPORT.md').relative_to(REPO)}")
    print(f"Per-paper artifacts under {OUT_DIR.relative_to(REPO)}/<safe_doi>/")
    print()
    print(f"Total errors: {total_errors}  |  text: {text_errors}  partial: {partial_errors}  figure: {figure_errors}")
    print(f"Runnable papers (parsed AND ≥1 text-detectable error): {runnable_papers} of {parsed_papers} parsed / {total_papers} total")


if __name__ == "__main__":
    main()
