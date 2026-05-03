#!/usr/bin/env python3
"""
Run the SPOT pilot: stratified sample of 10 papers × 4 conditions, with a
hard cost cap. Uses a thread pool to run (paper × condition) tasks
concurrently.

After inference, runs scoring_spot.py over the outputs.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
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

PRINT_LOCK = threading.Lock()


def safe_print(*args, **kwargs):
    with PRINT_LOCK:
        print(*args, **kwargs, flush=True)


def stratified_sample(index: pd.DataFrame, n: int, seed: int) -> pd.DataFrame:
    """One paper per category until n reached; then random fill."""
    rng = random.Random(seed)
    by_cat: dict[str, list[int]] = {}
    for i, row in index.iterrows():
        by_cat.setdefault(row["paper_category"], []).append(i)
    cats = sorted(by_cat.keys())
    for cat in cats:
        rng.shuffle(by_cat[cat])
    picked: list[int] = []
    while len(picked) < n:
        progress = False
        for cat in cats:
            if len(picked) >= n:
                break
            if by_cat[cat]:
                picked.append(by_cat[cat].pop())
                progress = True
        if not progress:
            break
    return index.loc[picked].sort_values(["paper_category", "doi"]).reset_index(drop=True)


def task_fn(paper_id: str, paper_path: Path, condition: str,
            out_dir: Path, total_n: int, counter: list[int]) -> dict:
    try:
        t0 = time.time()
        result = run_one(paper_path, paper_id, condition, out_dir)
        dur = time.time() - t0
        sev = result.get("severity_counts") or {}
        rw = sev.get("RETRACTION-WORTHY", 0) if sev else 0
        running = get_tracker().total
        with PRINT_LOCK:
            counter[0] += 1
            done = counter[0]
            safe_print(
                f"[{done:>2}/{total_n}] {paper_id[:32]:<32} {condition.upper():<3} "
                f"verdict={result['verdict']:<10} RW={rw} "
                f"cost=${result['meta']['cost_usd']:.4f} "
                f"running=${running:.2f} ({dur:.0f}s)"
            )
        return {"paper_id": paper_id, "condition": condition, "ok": True,
                "duration_s": dur, "cost_usd": result["meta"]["cost_usd"]}
    except BudgetExceeded as e:
        safe_print(f"!! BUDGET {paper_id}/{condition}: {e}")
        return {"paper_id": paper_id, "condition": condition, "ok": False, "error": str(e), "fatal": True}
    except Exception as e:
        safe_print(f"!! ERROR  {paper_id}/{condition}: {type(e).__name__}: {e}")
        return {"paper_id": paper_id, "condition": condition, "ok": False, "error": str(e), "fatal": False}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=10, help="Pilot size")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--cap", type=float, default=25.0)
    p.add_argument("--conditions", default="b1,b2,b3,gd")
    p.add_argument("--out-name", default="pilot_n10")
    p.add_argument("--max-paper-chars", type=int, default=120_000)
    p.add_argument("--workers", type=int, default=6,
                   help="Concurrent (paper × condition) tasks")
    p.add_argument("--no-score", action="store_true")
    args = p.parse_args()

    index = pd.read_csv(INDEX_CSV)
    too_big = index["paper_text_chars"] > args.max_paper_chars
    if too_big.any():
        safe_print(f"Dropping {too_big.sum()} papers > {args.max_paper_chars} chars")
    eligible = index[~too_big].reset_index(drop=True)

    sample = stratified_sample(eligible, n=args.n, seed=args.seed)
    safe_print(f"\nStratified sample of {len(sample)} papers:")
    safe_print(sample[["doi", "safe_doi", "title", "paper_category",
                        "n_errors_total", "n_text", "n_partial",
                        "n_figure_only", "paper_text_chars"]]
                .to_string(index=False))

    out_dir = REPO / "data" / "spot" / "outputs" / args.out_name
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "sample.csv").write_text(sample.to_csv(index=False), encoding="utf-8")

    tracker = configure_tracker(args.cap)
    safe_print(f"\nCost cap: ${args.cap:.2f}")
    safe_print(f"Conditions: {args.conditions}")
    safe_print(f"Workers: {args.workers}")
    safe_print(f"Output dir: {out_dir.relative_to(REPO)}")
    safe_print("")

    conditions = [c.strip() for c in args.conditions.split(",")]
    work: list[tuple[str, Path, str]] = []
    for _, row in sample.iterrows():
        paper_id = row["safe_doi"]
        paper_path = PAPER_DIR / paper_id / "paper.txt"
        if not paper_path.exists():
            safe_print(f"!! missing paper.txt for {paper_id}")
            continue
        for cond in conditions:
            # Skip if already done (resume support)
            existing = out_dir / paper_id / f"{cond.lower()}.json"
            if existing.exists():
                safe_print(f"   resume: {paper_id}/{cond} already done")
                continue
            work.append((paper_id, paper_path, cond))

    n_total = len(work)
    counter = [0]
    results: list[dict] = []
    started = time.time()

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [
            pool.submit(task_fn, paper_id, paper_path, cond,
                        out_dir, n_total, counter)
            for paper_id, paper_path, cond in work
        ]
        for fut in as_completed(futures):
            r = fut.result()
            results.append(r)
            if r.get("fatal"):
                safe_print("Cancelling remaining work due to budget overage.")
                for f2 in futures:
                    f2.cancel()
                break

    duration = time.time() - started
    summary = tracker.summary()
    summary["sweep"] = args.out_name
    summary["n_papers"] = len(sample)
    summary["conditions"] = conditions
    summary["wall_clock_s"] = round(duration, 1)
    summary["task_results"] = results
    failures = [r for r in results if not r.get("ok")]
    summary["n_failures"] = len(failures)
    (out_dir / "cost_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    safe_print(f"\nTotal cost: ${tracker.total:.4f} of ${args.cap:.2f} cap")
    safe_print(f"Total calls: {summary['total_calls']}")
    safe_print(f"Wall clock:  {duration:.1f}s")
    safe_print(f"Failures:    {len(failures)}")
    if failures:
        safe_print("Failure detail:")
        for f in failures[:10]:
            safe_print(f"  {f.get('paper_id')}/{f.get('condition')}: {f.get('error','')[:100]}")
    safe_print(f"\nCost summary written to {out_dir.relative_to(REPO)}/cost_summary.json")

    if args.no_score or any(r.get("fatal") for r in results):
        safe_print("\nSkipping scoring (use harness/scoring_spot.py to score later).")
        return

    safe_print("\n" + "=" * 60)
    safe_print("Scoring against SPOT ground truth ...")
    safe_print("=" * 60)
    from scoring_spot import score_sweep
    remaining_budget = max(args.cap - tracker.total, 1.0)
    score_sweep(out_dir, PAPER_DIR, REPO / "data" / "spot" / "scoring",
                conditions, cap_usd=remaining_budget)


if __name__ == "__main__":
    main()
