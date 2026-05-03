#!/usr/bin/env python3
"""
Run the SPOT pilot: stratified sample of 10 papers × 4 conditions, with a
hard cost cap and per-paper progress reporting.

After the inference sweep, runs scoring_spot.py over the outputs.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "harness"))

import pandas as pd  # noqa: E402

from api_client import (  # noqa: E402
    BudgetExceeded, configure_tracker, get_tracker,
)
from run_pipeline import run_one  # noqa: E402

INDEX_CSV = REPO / "data" / "spot" / "text_detectable" / "index.csv"
PAPER_DIR = REPO / "data" / "spot" / "text_detectable"


def stratified_sample(index: pd.DataFrame, n: int, seed: int) -> pd.DataFrame:
    """One paper per category until we hit n; fill the rest by random pick."""
    rng = random.Random(seed)
    picked: list[int] = []
    by_cat: dict[str, list[int]] = {}
    for i, row in index.iterrows():
        by_cat.setdefault(row["paper_category"], []).append(i)
    # Round-robin one per category until n reached
    cats = sorted(by_cat.keys())
    for cat in cats:
        rng.shuffle(by_cat[cat])
    while len(picked) < n:
        progress_made = False
        for cat in cats:
            if len(picked) >= n:
                break
            if by_cat[cat]:
                picked.append(by_cat[cat].pop())
                progress_made = True
        if not progress_made:
            break
    return index.loc[picked].sort_values(["paper_category", "doi"]).reset_index(drop=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=10, help="Pilot size")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--cap", type=float, default=25.0)
    p.add_argument("--conditions", default="b1,b2,b3,gd")
    p.add_argument("--out-name", default="pilot_n10",
                   help="Subdir under data/spot/outputs/")
    p.add_argument("--max-paper-chars", type=int, default=120_000,
                   help="Skip papers with text longer than this")
    p.add_argument("--no-score", action="store_true",
                   help="Skip scoring after inference")
    args = p.parse_args()

    index = pd.read_csv(INDEX_CSV)
    # Drop papers that exceed the safe length budget (saves API cost).
    too_big = index["paper_text_chars"] > args.max_paper_chars
    if too_big.any():
        print(f"Dropping {too_big.sum()} papers > {args.max_paper_chars} chars from sampling pool")
    eligible = index[~too_big].reset_index(drop=True)

    sample = stratified_sample(eligible, n=args.n, seed=args.seed)
    print(f"\nStratified sample of {len(sample)} papers:")
    print(sample[["doi", "safe_doi", "title", "paper_category", "n_errors_total",
                  "n_text", "n_partial", "n_figure_only", "paper_text_chars"]]
          .to_string(index=False))

    out_dir = REPO / "data" / "spot" / "outputs" / args.out_name
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "sample.csv").write_text(sample.to_csv(index=False), encoding="utf-8")

    tracker = configure_tracker(args.cap)
    print(f"\nCost cap: ${args.cap:.2f}")
    print(f"Conditions: {args.conditions}")
    print(f"Output dir: {out_dir.relative_to(REPO)}")
    print()

    conditions = [c.strip() for c in args.conditions.split(",")]
    n_total = len(sample) * len(conditions)
    done = 0
    failures: list[dict] = []
    started = time.time()

    for _, row in sample.iterrows():
        paper_id = row["safe_doi"]
        paper_path = PAPER_DIR / paper_id / "paper.txt"
        if not paper_path.exists():
            print(f"!! missing paper.txt for {paper_id}")
            continue
        for cond in conditions:
            done += 1
            try:
                t0 = time.time()
                result = run_one(paper_path, paper_id, cond, out_dir)
                dur = time.time() - t0
                sev = result.get("severity_counts") or {}
                rw = sev.get("RETRACTION-WORTHY", 0)
                print(f"[{done:>2}/{n_total}] {paper_id[:32]:<32} {cond.upper():<3} "
                      f"verdict={result['verdict']:<10} RW={rw} "
                      f"cost=${result['meta']['cost_usd']:.4f} "
                      f"running=${tracker.total:.2f} ({dur:.1f}s)")
            except BudgetExceeded as e:
                print(f"!! BUDGET EXCEEDED at {paper_id}/{cond}: {e}")
                failures.append({"paper_id": paper_id, "condition": cond, "error": str(e)})
                # Stop entirely.
                break
            except Exception as e:
                print(f"!! ERROR {paper_id}/{cond}: {type(e).__name__}: {e}")
                failures.append({"paper_id": paper_id, "condition": cond, "error": str(e)})
                # Continue with remaining work.
        else:
            continue
        break

    duration = time.time() - started
    summary = tracker.summary()
    summary["sweep"] = args.out_name
    summary["n_papers"] = len(sample)
    summary["conditions"] = conditions
    summary["wall_clock_s"] = round(duration, 1)
    summary["failures"] = failures
    (out_dir / "cost_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print()
    print(f"Total cost: ${tracker.total:.4f} of ${args.cap:.2f} cap")
    print(f"Total calls: {summary['total_calls']}")
    print(f"Wall clock:  {duration:.1f}s")
    print(f"Failures:    {len(failures)}")
    print()
    if failures:
        print("Failures detail:")
        for f in failures:
            print(f"  {f['paper_id']}/{f['condition']}: {f['error'][:120]}")
    print(f"\nCost summary written to {out_dir.relative_to(REPO)}/cost_summary.json")

    if args.no_score or failures:
        print("\nSkipping scoring (use harness/scoring_spot.py to score later).")
        return

    print("\n" + "=" * 60)
    print("Scoring against SPOT ground truth ...")
    print("=" * 60)
    from scoring_spot import score_sweep
    score_sweep(out_dir, PAPER_DIR, REPO / "data" / "spot" / "scoring",
                conditions, cap_usd=max(args.cap - tracker.total, 1.0))


if __name__ == "__main__":
    main()
