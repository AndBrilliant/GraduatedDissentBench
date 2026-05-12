#!/usr/bin/env python3
"""
Sweep B3+ and/or B3++ across all 50 text-detectable SPOT papers.

Parallelizes papers across a thread pool. Each paper's pipeline is 5 sequential
API calls so the bottleneck is per-paper wall clock (~60-90s on past runs);
running 4-8 papers concurrently brings the full sweep to ~10-20 min.

Outputs:
  data/spot/outputs/budget_matched/<paper_id>/{b3plus,b3plusplus}.json

Resumable: if a paper's output JSON already exists, it is skipped.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import sys
import threading
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "harness"))

from api_client import (  # noqa: E402
    BudgetExceeded, configure_tracker, get_tracker,
)
from run_b3plus import run_one  # noqa: E402

SOURCE_DIR = REPO / "data" / "spot" / "text_detectable"
OUT_DIR = REPO / "data" / "spot" / "outputs" / "budget_matched"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--conditions", nargs="+",
                   choices=["b3plus", "b3plusplus"],
                   default=["b3plus", "b3plusplus"])
    p.add_argument("--workers", type=int, default=4,
                   help="Concurrent papers (default 4)")
    p.add_argument("--cap", type=float, default=50.0)
    p.add_argument("--limit", type=int, default=None,
                   help="Limit number of papers (testing)")
    p.add_argument("--paper-ids", nargs="+", default=None,
                   help="Run only these paper IDs")
    p.add_argument("--out-dir", default=str(OUT_DIR))
    args = p.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    configure_tracker(args.cap)

    paper_dirs = sorted(d for d in SOURCE_DIR.iterdir()
                        if d.is_dir() and (d / "paper.txt").exists())
    if args.paper_ids:
        wanted = set(args.paper_ids)
        paper_dirs = [d for d in paper_dirs if d.name in wanted]
    if args.limit:
        paper_dirs = paper_dirs[:args.limit]

    n_total = len(paper_dirs) * len(args.conditions)
    print(f"Sweep: {len(paper_dirs)} papers × {len(args.conditions)} "
          f"conditions = {n_total} runs")
    print(f"Workers: {args.workers}, cost cap: ${args.cap}")
    print(f"Output: {out_dir}")

    tasks: list[tuple[Path, str, str]] = []  # (paper_path, paper_id, condition)
    for d in paper_dirs:
        for cond in args.conditions:
            existing = out_dir / d.name / f"{cond}.json"
            if existing.exists():
                continue
            tasks.append((d / "paper.txt", d.name, cond))
    n_skip = n_total - len(tasks)
    print(f"To run: {len(tasks)} (skipping {n_skip} existing)")

    n_done = 0
    n_err = 0
    progress_lock = threading.Lock()
    t0 = time.time()

    def run_task(task):
        nonlocal n_done, n_err
        paper_path, paper_id, cond = task
        try:
            result = run_one(paper_path, paper_id, cond, out_dir)
            sev = result.get("severity_counts") or {}
            rw = sev.get("RETRACTION-WORTHY", 0)
            mc = result["meta"]["cost_usd"]
            ds = result["meta"]["duration_s"]
            msg = (f"{paper_id} {cond}: verdict={result['verdict']} "
                   f"RW={rw} | ${mc:.4f} ({ds}s)")
            with progress_lock:
                n_done += 1
                running = get_tracker().total
                eta_s = (running / max(1, n_done)) * (len(tasks) - n_done) \
                        * 0  # rate-based ETA hard to estimate w/ workers
                elapsed = time.time() - t0
                rate = n_done / max(1, elapsed)
                eta = (len(tasks) - n_done) / max(0.01, rate)
                print(f"  [{n_done}/{len(tasks)} done, "
                      f"${running:.3f}, {elapsed:.0f}s, ETA {eta:.0f}s] "
                      f"{msg}")
        except BudgetExceeded as e:
            print(f"!! BUDGET EXCEEDED on {paper_id} {cond}: {e}",
                  file=sys.stderr)
            with progress_lock:
                n_err += 1
            raise
        except Exception as e:
            with progress_lock:
                n_err += 1
                print(f"  ERR on {paper_id} {cond}: "
                      f"{type(e).__name__}: {e}")

    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        try:
            list(ex.map(run_task, tasks))
        except BudgetExceeded:
            ex.shutdown(wait=False, cancel_futures=True)

    summary = get_tracker().summary()
    summary_path = out_dir / "sweep_cost_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2),
                              encoding="utf-8")
    elapsed = time.time() - t0
    print(f"\nDONE. {n_done} runs, {n_err} errors, "
          f"${summary['total_cost_usd']:.4f}, "
          f"{elapsed:.0f}s ({elapsed/60:.1f}m)")
    print(f"  cost_summary: {summary_path}")


if __name__ == "__main__":
    main()
