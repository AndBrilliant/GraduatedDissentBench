#!/usr/bin/env python3
"""
Anonymize the remaining 30 text-detectable SPOT papers and add them to
the sweep sample. Output goes to data/spot/outputs/full_run/<safe_doi>/
to keep the n=20 pilot outputs untouched.

Each new paper:
  - paper.txt is overwritten with the anonymized text (paper.raw.txt
    saved for traceability)
  - the sample.csv at data/spot/outputs/full_run/sample.csv lists ALL
    50 papers so sweep_serial.sh resume keeps picking up where we left
    off and avoids re-running anything
  - the existing 20 papers' outputs are PRE-COPIED into the full_run/
    directory so resume properly skips them
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
TEXT = REPO / "data" / "spot" / "text_detectable"
OLD_DIR = REPO / "data" / "spot" / "outputs" / "pilot_n10"
NEW_DIR = REPO / "data" / "spot" / "outputs" / "full_run"
INDEX = TEXT / "index.csv"

sys.path.insert(0, str(REPO / "OLD" / "scripts"))


def main():
    NEW_DIR.mkdir(parents=True, exist_ok=True)

    # Read the existing pilot sample (the n=20 already done) and the full text-detectable index
    pilot = pd.read_csv(OLD_DIR / "sample.csv")
    idx = pd.read_csv(INDEX)
    eligible = idx[idx["paper_text_chars"] <= 120_000].copy()
    already_done = set(pilot["safe_doi"])
    new_rows = eligible[~eligible["safe_doi"].isin(already_done)].copy()
    print(f"Already done: {len(pilot)} papers")
    print(f"Remaining text-detectable: {len(new_rows)} papers")

    from anonymize_paper import anonymize  # type: ignore

    anon_count = 0
    for _, row in new_rows.iterrows():
        d = TEXT / row["safe_doi"]
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
    print(f"Anonymized {anon_count} new papers (originals saved as paper.raw.txt).")

    # Pre-copy the existing 20 outputs into full_run/<safe_doi>/ so resume skips them
    pre_copied = 0
    for _, row in pilot.iterrows():
        src = OLD_DIR / row["safe_doi"]
        dst = NEW_DIR / row["safe_doi"]
        if not src.exists():
            print(f"!! missing pilot output dir for {row['safe_doi']}")
            continue
        dst.mkdir(parents=True, exist_ok=True)
        for f in src.glob("*.json"):
            target = dst / f.name
            if not target.exists():
                shutil.copy2(f, target)
                pre_copied += 1
    print(f"Pre-copied {pre_copied} existing output files into full_run/")

    # Combined sample = all 50 papers
    combined = pd.concat([pilot, new_rows], ignore_index=True).drop_duplicates("safe_doi")
    sample_path = NEW_DIR / "sample.csv"
    combined.to_csv(sample_path, index=False)
    print(f"Wrote {sample_path.relative_to(REPO)} ({len(combined)} papers total)")

    # Sanity: count expected outputs and existing
    n_total = len(combined) * 4
    n_existing = sum(1 for _ in NEW_DIR.glob("*/*.json"))
    print(f"Expected total tasks: {n_total} | Existing outputs in full_run/: {n_existing}")
    print(f"Tasks left to run: {n_total - n_existing}")


if __name__ == "__main__":
    main()
