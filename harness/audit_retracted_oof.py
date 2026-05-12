#!/usr/bin/env python3
"""
Out-of-family rescoring of the retracted-paper benchmark.

Mirrors `harness/audit_retracted.py` but uses three models from training
distributions disjoint from the in-pipeline {OpenAI, Anthropic, DeepSeek}
set:

    AUDIT_MODELS_OOF = ("gemini", "grok", "mistral")

Same MATCH and SEVERITY prompts as the in-family audit. Comparison
between in-family and out-of-family majority votes is exact at prompt
level.

Outputs to validation/retracted_paper_audit_oof/:
  - raw_responses.jsonl  — one row per (paper, condition, finding, question)
  - per_finding.csv      — finding-level votes
  - per_paper.csv        — paper-level detection / FP outcomes
  - cost_summary.json    — per-model token + USD accounting

Run:
    python harness/audit_retracted_oof.py --smoke            # 5 findings
    python harness/audit_retracted_oof.py --workers 4        # full
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import csv
import json
import os
import sys
import threading
import time
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "harness"))

from api_client import (  # noqa: E402
    call_model, configure_tracker, get_tracker, parse_json,
)
from audit_retracted import (  # noqa: E402
    MATCH_PROMPT_RETRACTED, MATCH_PROMPT_CONTROL, SEVERITY_PROMPT,
    load_ground_truth, load_findings_for_paper,
    is_retracted, is_probative_control, majority, unanimous,
)

AUDIT_MODELS_OOF = ("gemini", "grok", "mistral")
OUT_DIR = REPO / "validation" / "retracted_paper_audit_oof"

# Per-provider concurrency caps. Mistral paid tier handles 6+ concurrent
# easily; free tier needs Semaphore(1) and ~2.5s pacing. Override via env.
_PROVIDER_SEMAPHORES = {
    "mistral": threading.Semaphore(int(os.environ.get("MISTRAL_CONCURRENCY", "6"))),
    "gemini": threading.Semaphore(int(os.environ.get("GEMINI_CONCURRENCY", "8"))),
    "grok": threading.Semaphore(int(os.environ.get("GROK_CONCURRENCY", "8"))),
}
# Per-model minimum gap between calls. 0 on paid Mistral; 2.5s on free.
_MISTRAL_MIN_GAP = float(os.environ.get("MISTRAL_MIN_GAP", "0"))
_mistral_last_call_t = [0.0]
_mistral_call_lock = threading.Lock()


def _call_with_pacing(model: str, prompt: str) -> str:
    sem = _PROVIDER_SEMAPHORES.get(model)
    if sem is not None:
        sem.acquire()
        try:
            if model == "mistral":
                with _mistral_call_lock:
                    now = time.time()
                    gap = now - _mistral_last_call_t[0]
                    if gap < _MISTRAL_MIN_GAP:
                        time.sleep(_MISTRAL_MIN_GAP - gap)
                    _mistral_last_call_t[0] = time.time()
            return call_model(model, prompt, temperature=0,
                              label=f"audit_oof/{model}")
        finally:
            sem.release()
    return call_model(model, prompt, temperature=0,
                      label=f"audit_oof/{model}")


def call_one_model_with_retry(prompt: str, model: str) -> dict:
    """Single (prompt, model) call with rate-limit backoff. Returns the
    standard `{model, response}` record."""
    for attempt in range(8):
        try:
            raw = _call_with_pacing(model, prompt)
            ans = parse_json(raw)
            return {"model": model, "response": ans}
        except Exception as e:
            msg = str(e).lower()
            if attempt < 7 and any(s in msg for s in
                                    ("429", "rate", "timeout",
                                     "temporarily", "connection",
                                     "overloaded")):
                delay = min(60, (2 ** attempt) + 1)
                time.sleep(delay)
                continue
            return {"model": model,
                     "response": {"error": f"{type(e).__name__}: {e}"}}
    return {"model": model, "response": {"error": "exhausted retries"}}


def audit_one_finding_parallel(prompt: str,
                               models: tuple[str, ...] = AUDIT_MODELS_OOF
                               ) -> list[dict]:
    """Fire all three models in parallel for a single prompt. Per-provider
    semaphores serialize/pace where required."""
    out: list[dict] = [None] * len(models)  # type: ignore
    with cf.ThreadPoolExecutor(max_workers=len(models)) as ex:
        futures = {ex.submit(call_one_model_with_retry, prompt, m): i
                   for i, m in enumerate(models)}
        for fut in cf.as_completed(futures):
            idx = futures[fut]
            out[idx] = fut.result()
    return out


def votes_from_responses(responses: list[dict]) -> list[bool]:
    votes = []
    for r in responses:
        resp = r.get("response", {})
        if isinstance(resp, dict) and not resp.get("parse_error") \
                and not resp.get("error"):
            votes.append(bool(resp.get("match", False)))
        else:
            votes.append(False)
    return votes


def sev_votes_from_responses(responses: list[dict]) -> list[str]:
    votes = []
    for r in responses:
        resp = r.get("response", {})
        if isinstance(resp, dict) and not resp.get("parse_error") \
                and not resp.get("error"):
            votes.append(resp.get("severity", "?"))
        else:
            votes.append("?")
    return votes


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--cap", type=float, default=20.0,
                   help="USD cost cap")
    p.add_argument("--limit", type=int, default=None,
                   help="Limit findings per paper × condition (testing)")
    p.add_argument("--smoke", action="store_true",
                   help="Smoke test: stop after 5 findings")
    p.add_argument("--skip-severity", action="store_true",
                   help="Match-only, skip severity follow-ups")
    p.add_argument("--workers", type=int, default=4,
                   help="Concurrent findings (default 4)")
    p.add_argument("--out-dir", default=str(OUT_DIR))
    args = p.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    raw_log = out_dir / "raw_responses.jsonl"

    configure_tracker(args.cap)
    gt = load_ground_truth()

    paper_ids = sorted(
        pid for pid in gt
        if is_retracted(pid, gt) or is_probative_control(pid, gt)
    )

    # Build the full match-task list up front.
    match_tasks: list[dict] = []
    for pid in paper_ids:
        retracted = is_retracted(pid, gt)
        cause = gt[pid]["retraction_cause"] if retracted \
            else "(none — control)"
        for cond in ("B1", "B2", "B3", "GD"):
            findings, _blob = load_findings_for_paper(pid, cond)
            if not findings:
                continue
            limit = args.limit if args.limit else len(findings)
            for fi, f in enumerate(findings[:limit]):
                if not isinstance(f, dict):
                    continue
                ftext = f.get("finding", "") or f.get("description", "")
                if not ftext:
                    continue
                if retracted:
                    prompt = MATCH_PROMPT_RETRACTED.format(
                        ground_truth=cause, finding_text=ftext,
                    )
                else:
                    prompt = MATCH_PROMPT_CONTROL.format(finding_text=ftext)
                match_tasks.append({
                    "paper_id": pid,
                    "is_retracted": retracted,
                    "condition": cond,
                    "finding_idx": fi,
                    "finding_text": ftext,
                    "first_author_severity": f.get("severity", ""),
                    "prompt": prompt,
                })

    if args.smoke:
        match_tasks = match_tasks[:5]
    n_findings = len(match_tasks)
    print(f"OOF audit: {n_findings} findings × "
          f"{len(AUDIT_MODELS_OOF)} models ({', '.join(AUDIT_MODELS_OOF)})")
    print(f"Workers: {args.workers}, Cost cap: ${args.cap}")
    if args.smoke:
        print("SMOKE MODE: 5 findings only")

    # ─── PHASE 1: match calls (parallel over findings) ───────────────
    raw_fh = raw_log.open("w", encoding="utf-8")
    raw_lock = threading.Lock()
    per_finding_rows: list[dict] = []
    pf_lock = threading.Lock()
    n_completed = 0
    progress_lock = threading.Lock()

    t0 = time.time()
    last_progress_t = t0

    def process_match(task: dict) -> dict:
        nonlocal n_completed, last_progress_t
        responses = audit_one_finding_parallel(task["prompt"])
        votes = votes_from_responses(responses)
        row = {
            "paper_id": task["paper_id"],
            "is_retracted": task["is_retracted"],
            "condition": task["condition"],
            "finding_idx": task["finding_idx"],
            "finding_text": task["finding_text"][:300],
            "first_author_severity": task["first_author_severity"],
            "audit_match_votes": votes,
            "audit_match_majority": majority(votes),
            "audit_match_unanimous": unanimous(votes),
            "audit_match_any": any(votes),
            # filled in phase 2 if applicable
            "audit_severity_votes": [],
            "audit_severity_majority_RW": False,
        }
        with raw_lock:
            raw_fh.write(json.dumps({
                "event": "match",
                "paper_id": task["paper_id"],
                "condition": task["condition"],
                "finding_idx": task["finding_idx"],
                "responses": responses,
            }) + "\n")
            raw_fh.flush()
        with pf_lock:
            per_finding_rows.append(row)
        with progress_lock:
            n_completed += 1
            now = time.time()
            if now - last_progress_t >= 60 or n_completed == n_findings:
                elapsed = now - t0
                rate = n_completed / max(1, elapsed)
                eta = (n_findings - n_completed) / max(0.01, rate)
                print(f"  [{n_completed}/{n_findings} findings, "
                      f"${get_tracker().total:.3f}, "
                      f"{elapsed:.0f}s elapsed, ETA {eta:.0f}s]")
                last_progress_t = now
        return row

    print(f"Phase 1: match calls ({n_findings} findings)...")
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        list(ex.map(process_match, match_tasks))

    n_match_calls = n_findings * len(AUDIT_MODELS_OOF)
    print(f"Phase 1 done: {n_match_calls} match calls, "
          f"${get_tracker().total:.4f}, {time.time()-t0:.0f}s")

    # ─── PHASE 2: severity calls (only on match-majority findings) ──
    sev_tasks = [r for r in per_finding_rows if r["audit_match_majority"]] \
        if not args.skip_severity else []

    if sev_tasks:
        print(f"Phase 2: severity calls ({len(sev_tasks)} findings)...")
        t1 = time.time()

        def process_sev(row: dict) -> None:
            sev_prompt = SEVERITY_PROMPT.format(finding_text=row["finding_text"])
            responses = audit_one_finding_parallel(sev_prompt)
            sv = sev_votes_from_responses(responses)
            row["audit_severity_votes"] = sv
            row["audit_severity_majority_RW"] = (
                sum(1 for s in sv if s == "RETRACTION-WORTHY") >= 2
            )
            with raw_lock:
                raw_fh.write(json.dumps({
                    "event": "severity",
                    "paper_id": row["paper_id"],
                    "condition": row["condition"],
                    "finding_idx": row["finding_idx"],
                    "responses": responses,
                }) + "\n")
                raw_fh.flush()

        with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
            list(ex.map(process_sev, sev_tasks))

        n_sev_calls = len(sev_tasks) * len(AUDIT_MODELS_OOF)
        print(f"Phase 2 done: {n_sev_calls} severity calls, "
              f"{time.time()-t1:.0f}s")
    else:
        n_sev_calls = 0

    raw_fh.close()

    # ─── Aggregate per paper × condition ─────────────────────────────
    per_paper_rows: list[dict] = []
    by_pc: dict[tuple[str, str], list[dict]] = {}
    for r in per_finding_rows:
        by_pc.setdefault((r["paper_id"], r["condition"]), []).append(r)
    for pid in paper_ids:
        retracted = is_retracted(pid, gt)
        for cond in ("B1", "B2", "B3", "GD"):
            rows = by_pc.get((pid, cond), [])
            audit_match_majority = any(r["audit_match_majority"] for r in rows)
            audit_match_unanimous = any(r["audit_match_unanimous"] for r in rows)
            audit_match_any = any(r["audit_match_any"] for r in rows)
            audit_RW_majority = any(r["audit_severity_majority_RW"] for r in rows)
            audit_RW_unanimous = any(
                len(r["audit_severity_votes"]) >= 3 and
                all(s == "RETRACTION-WORTHY" for s in r["audit_severity_votes"])
                for r in rows
            )
            per_paper_rows.append({
                "paper_id": pid,
                "condition": cond,
                "is_retracted": retracted,
                "n_findings": len(rows),
                "audit_match_majority": audit_match_majority,
                "audit_match_unanimous": audit_match_unanimous,
                "audit_match_any": audit_match_any,
                "audit_RW_majority": audit_RW_majority,
                "audit_RW_unanimous": audit_RW_unanimous,
            })

    # ─── Write CSVs ─────────────────────────────────────────────────
    if per_finding_rows:
        with (out_dir / "per_finding.csv").open("w", newline="",
                                                  encoding="utf-8") as f:
            cols = list(per_finding_rows[0].keys())
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            for r in per_finding_rows:
                r2 = {k: (json.dumps(v) if isinstance(v, list) else v)
                      for k, v in r.items()}
                w.writerow(r2)
    if per_paper_rows:
        with (out_dir / "per_paper.csv").open("w", newline="",
                                                 encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(per_paper_rows[0].keys()))
            w.writeheader()
            for r in per_paper_rows:
                w.writerow(r)

    summary = get_tracker().summary()
    (out_dir / "cost_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8")
    elapsed = time.time() - t0
    print(f"\nDONE. total cost ${summary['total_cost_usd']:.4f}, "
          f"{elapsed:.0f}s ({elapsed/60:.1f}m)")
    print(f"  match calls: {n_match_calls}, severity calls: {n_sev_calls}")
    print(f"  per-model breakdown:")
    for m, d in summary.get("by_model", {}).items():
        print(f"    {m}: n={d['n_calls']}, "
              f"in={d['input_tokens']}, out={d['output_tokens']}, "
              f"${d['cost_usd']:.4f}")
    print(f"  outputs: {out_dir}")


if __name__ == "__main__":
    sys.exit(main() or 0)
