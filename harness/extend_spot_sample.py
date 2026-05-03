#!/usr/bin/env python3
"""
Pick the next batch of SPOT papers to add to the pilot, stratified across
paper categories, and merge them into the existing sample.csv. Then
anonymize each new paper.txt in place (saving the original as
paper.raw.txt for traceability).

Usage:
    python harness/extend_spot_sample.py --add 10 --seed 43 --out-name pilot_n10
"""
from __future__ import annotations

import argparse
import random
import shutil
import sys
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "OLD" / "scripts"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--add", type=int, default=10, help="How many papers to add")
    p.add_argument("--seed", type=int, default=43,
                   help="Different from the previous pilot's seed (42) so we avoid re-picking")
    p.add_argument("--out-name", default="pilot_n10")
    p.add_argument("--max-paper-chars", type=int, default=120_000)
    args = p.parse_args()

    index_csv = REPO / "data" / "spot" / "text_detectable" / "index.csv"
    out_dir = REPO / "data" / "spot" / "outputs" / args.out_name
    sample_csv = out_dir / "sample.csv"

    index = pd.read_csv(index_csv)
    existing = pd.read_csv(sample_csv)
    eligible = index[
        (index["paper_text_chars"] <= args.max_paper_chars)
        & (~index["safe_doi"].isin(existing["safe_doi"]))
    ].reset_index(drop=True)

    print(f"Already in sample: {len(existing)} papers")
    print(f"Eligible (not yet sampled, under {args.max_paper_chars} chars): {len(eligible)}")

    # Stratified-by-category random sample using the new seed
    rng = random.Random(args.seed)
    by_cat: dict[str, list[int]] = {}
    for i, row in eligible.iterrows():
        by_cat.setdefault(row["paper_category"], []).append(i)
    cats = sorted(by_cat.keys())
    for cat in cats:
        rng.shuffle(by_cat[cat])
    picked: list[int] = []
    while len(picked) < args.add:
        progressed = False
        for cat in cats:
            if len(picked) >= args.add:
                break
            if by_cat[cat]:
                picked.append(by_cat[cat].pop())
                progressed = True
        if not progressed:
            break

    new = eligible.loc[picked].sort_values(["paper_category", "doi"]).reset_index(drop=True)
    print(f"\nNewly picked {len(new)} papers:")
    print(new[["doi", "safe_doi", "paper_category", "n_errors_total",
                "n_text", "n_partial", "n_figure_only", "paper_text_chars"]]
          .to_string(index=False))

    # Anonymize each new paper.txt in place (back up as paper.raw.txt).
    paper_root = REPO / "data" / "spot" / "text_detectable"
    from anonymize_paper import anonymize  # type: ignore

    anon_count = 0
    for _, row in new.iterrows():
        d = paper_root / row["safe_doi"]
        ptxt = d / "paper.txt"
        praw = d / "paper.raw.txt"
        if not ptxt.exists():
            print(f"!! missing paper.txt for {row['safe_doi']}")
            continue
        if not praw.exists():
            shutil.copy2(ptxt, praw)
        original = praw.read_text(encoding="utf-8")
        cleaned = anonymize(original)
        ptxt.write_text(cleaned, encoding="utf-8")
        anon_count += 1
    print(f"\nAnonymized {anon_count} papers in place (originals saved as paper.raw.txt).")

    combined = pd.concat([existing, new], ignore_index=True)
    sample_csv.write_text(combined.to_csv(index=False), encoding="utf-8")
    print(f"\nUpdated sample: {len(combined)} papers total -> {sample_csv.relative_to(REPO)}")


if __name__ == "__main__":
    raise SystemExit(main() or 0)
