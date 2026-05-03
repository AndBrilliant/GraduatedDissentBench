#!/usr/bin/env python3
"""
Re-anonymize the originally-unanonymized SPOT papers.

A paper counts as "originally unanonymized" iff its directory under
data/spot/text_detectable/<safe_doi>/ does NOT contain paper.raw.txt
(we save paper.raw.txt as a backup before overwriting paper.txt with
the anonymized version).

For each such paper:
  1. Save current paper.txt as paper.raw.txt (now the unanonymized backup).
  2. Anonymize paper.txt in place using OLD/scripts/anonymize_paper.py.
  3. Archive the existing protocol outputs under
     data/spot/outputs/pilot_n10_unanon_archive/<safe_doi>/, then delete
     them from data/spot/outputs/pilot_n10/<safe_doi>/ so the sweep will
     re-run them.

The sweep is launched separately by sweep_serial.sh.
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
TEXT_DETECT = REPO / "data" / "spot" / "text_detectable"
OUTPUTS = REPO / "data" / "spot" / "outputs" / "pilot_n10"
ARCHIVE = REPO / "data" / "spot" / "outputs" / "pilot_n10_unanon_archive"
SAMPLE = OUTPUTS / "sample.csv"

sys.path.insert(0, str(REPO / "OLD" / "scripts"))


def main():
    sample = pd.read_csv(SAMPLE)
    safe_dois = sample["safe_doi"].tolist()

    from anonymize_paper import anonymize  # type: ignore

    targets: list[str] = []
    for safe_doi in safe_dois:
        d = TEXT_DETECT / safe_doi
        if (d / "paper.raw.txt").exists():
            continue  # already anonymized in a previous batch
        targets.append(safe_doi)

    print(f"Originally-unanonymized papers to re-anonymize: {len(targets)}")
    for t in targets:
        print(f"  - {t}")

    if not targets:
        print("\nNothing to do.")
        return

    ARCHIVE.mkdir(parents=True, exist_ok=True)

    for safe_doi in targets:
        d = TEXT_DETECT / safe_doi
        ptxt = d / "paper.txt"
        praw = d / "paper.raw.txt"
        if not ptxt.exists():
            print(f"!! missing paper.txt for {safe_doi}")
            continue

        # 1) Back up the unanonymized original as paper.raw.txt
        shutil.copy2(ptxt, praw)

        # 2) Anonymize in place
        original = praw.read_text(encoding="utf-8")
        cleaned = anonymize(original)
        ptxt.write_text(cleaned, encoding="utf-8")

        # 3) Archive existing outputs and remove originals so the sweep re-runs
        out_dir = OUTPUTS / safe_doi
        if out_dir.exists():
            arc = ARCHIVE / safe_doi
            arc.mkdir(parents=True, exist_ok=True)
            for f in out_dir.glob("*.json"):
                shutil.move(str(f), str(arc / f.name))

        print(f"  re-anonymized + archived outputs: {safe_doi}")

    print(f"\nDone. {len(targets)} papers re-anonymized; their old outputs archived to "
          f"{ARCHIVE.relative_to(REPO)}/")


if __name__ == "__main__":
    main()
