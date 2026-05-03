#!/usr/bin/env python3
"""
Run after the SPOT pilot finishes (or partially completes). Walks through the
output directory, reparses any truncated arbiter responses, scores the surviving
results against SPOT ground truth, generates the paper's spot_comparison table,
and updates fig3_spot_comparison.png.

Idempotent — safe to run multiple times.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def run(cmd: list[str], cwd: Path = REPO) -> int:
    print(f"\n$ {' '.join(cmd)}")
    r = subprocess.run(cmd, cwd=str(cwd))
    return r.returncode


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sweep", default="pilot_n10")
    p.add_argument("--cap", type=float, default=5.0,
                   help="Cost cap for the scoring (judge) calls")
    p.add_argument("--skip-score", action="store_true")
    p.add_argument("--skip-figs", action="store_true")
    args = p.parse_args()

    sweep_dir = REPO / "data" / "spot" / "outputs" / args.sweep
    if not sweep_dir.exists():
        print(f"!! sweep dir not found: {sweep_dir}")
        return 1

    py = str(REPO / ".venv" / "bin" / "python")

    # Step 1 — recover any truncated arbiter outputs.
    rc = run([py, "harness/reparse_outputs.py", "--sweep", args.sweep])
    if rc != 0:
        print(f"reparse step failed (rc={rc}); continuing")

    # Step 2 — run scoring (LLM judge against SPOT ground truth).
    if args.skip_score:
        print("Skipping scoring (--skip-score)")
    else:
        rc = run([
            py, "harness/scoring_spot.py",
            "--sweep-dir", str(sweep_dir),
            "--gt-dir", "data/spot/text_detectable",
            "--scoring-dir", "data/spot/scoring",
            "--cap", str(args.cap),
        ])
        if rc != 0:
            print(f"scoring step failed (rc={rc}); continuing")

    # Step 3 — generate the SPOT comparison table for the paper.
    aggregates = REPO / "data" / "spot" / "scoring" / args.sweep / "aggregates.csv"
    if aggregates.exists():
        rc = run([
            py, "analysis/spot_comparison.py",
            "--aggregates", str(aggregates.relative_to(REPO)),
            "--out-stem", "paper/tables/spot_comparison",
        ])
        if rc != 0:
            print(f"spot_comparison step failed (rc={rc})")
    else:
        print(f"(no aggregates at {aggregates}; skipping spot_comparison table)")

    # Step 4 — regenerate paper figures with live SPOT data.
    if args.skip_figs:
        print("Skipping figures (--skip-figs)")
    elif aggregates.exists():
        rc = run([
            py, "analysis/figures/generate_paper_figures.py",
            "--spot-aggregates", str(aggregates.relative_to(REPO)),
        ])
        if rc != 0:
            print(f"figure generation failed (rc={rc})")
    else:
        print("(no aggregates yet; skipping figure refresh)")

    # Step 5 — recompile main.tex.
    paper_dir = REPO / "paper"
    if (paper_dir / "main.tex").exists():
        run(["pdflatex", "-interaction=nonstopmode", "-draftmode", "main.tex"], cwd=paper_dir)
        run(["bibtex", "main"], cwd=paper_dir)
        run(["pdflatex", "-interaction=nonstopmode", "-draftmode", "main.tex"], cwd=paper_dir)
        run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=paper_dir)
        # Clean tex artifacts
        for ext in ["aux", "bbl", "blg", "log", "out"]:
            (paper_dir / f"main.{ext}").unlink(missing_ok=True)

    print("\n=== finalize complete ===")
    if aggregates.exists():
        import pandas as pd
        agg = pd.read_csv(aggregates)
        print("\nSPOT pilot aggregates:")
        cols_show = [c for c in ["condition", "N", "TP_total", "FP_total", "FN_total",
                                  "precision_micro", "recall_micro", "PPR",
                                  "pass_at_1", "detection_rate"]
                     if c in agg.columns]
        print(agg[cols_show].to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
