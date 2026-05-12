#!/usr/bin/env python3
"""
Retry the Gemini calls that 429'd during the OOF audit run.

Walks `validation/retracted_paper_audit_oof/raw_responses.jsonl`, finds every
(paper_id, condition, finding_idx, event) where the Gemini response is an
error, reconstructs the prompt (using the original audit prompt set + the
finding text from github/outputs/raw/), and re-calls Gemini with low
concurrency. Writes to `raw_responses_gemini_fillin.jsonl` in the same
directory; the aggregator merges this in like the in-family opus fillin.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "harness"))

from api_client import call_model, configure_tracker, parse_json  # noqa: E402
from audit_retracted import (  # noqa: E402
    MATCH_PROMPT_RETRACTED, MATCH_PROMPT_CONTROL, SEVERITY_PROMPT,
    load_ground_truth, load_findings_for_paper, is_retracted,
)

OOF_DIR = REPO / "validation" / "retracted_paper_audit_oof"
RAW = OOF_DIR / "raw_responses.jsonl"
FILLIN = OOF_DIR / "raw_responses_gemini_fillin.jsonl"


def build_prompt(paper_id: str, condition: str, finding_idx: int,
                 event: str, gt: dict) -> str | None:
    findings, _ = load_findings_for_paper(paper_id, condition)
    if finding_idx >= len(findings):
        return None
    f = findings[finding_idx]
    if not isinstance(f, dict):
        return None
    ftext = f.get("finding", "") or f.get("description", "")
    if not ftext:
        return None
    if event == "severity":
        return SEVERITY_PROMPT.format(finding_text=ftext)
    retracted = is_retracted(paper_id, gt)
    if retracted:
        cause = gt[paper_id]["retraction_cause"]
        return MATCH_PROMPT_RETRACTED.format(
            ground_truth=cause, finding_text=ftext,
        )
    return MATCH_PROMPT_CONTROL.format(finding_text=ftext)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--workers", type=int, default=2,
                   help="Concurrent gemini calls (default 2; quota-sensitive)")
    p.add_argument("--gap", type=float, default=0.5,
                   help="Sleep between calls (default 0.5s)")
    p.add_argument("--cap", type=float, default=5.0)
    args = p.parse_args()

    configure_tracker(args.cap)
    gt = load_ground_truth()

    # Find all (key, event) where gemini failed
    failed: list[tuple] = []
    with RAW.open() as f:
        for line in f:
            r = json.loads(line)
            for resp in r["responses"]:
                if resp["model"] != "gemini":
                    continue
                rr = resp.get("response", {})
                if isinstance(rr, dict) and (rr.get("error") or rr.get("parse_error")):
                    failed.append((r["paper_id"], r["condition"],
                                     r["finding_idx"], r["event"]))
                    break
    print(f"Gemini calls to retry: {len(failed)}")
    if not failed:
        print("Nothing to retry.")
        return

    # Build prompts
    tasks = []
    for (pid, cond, fi, event) in failed:
        prompt = build_prompt(pid, cond, fi, event, gt)
        if prompt is None:
            continue
        tasks.append({"paper_id": pid, "condition": cond,
                       "finding_idx": fi, "event": event, "prompt": prompt})
    print(f"Tasks built: {len(tasks)}")

    fh = FILLIN.open("a", encoding="utf-8")  # append in case of multiple runs
    last_call = [0.0]
    import threading
    lock = threading.Lock()
    n_done = 0
    n_ok = 0
    n_err = 0
    progress_lock = threading.Lock()
    t0 = time.time()
    last_print = t0

    def call(task):
        nonlocal n_done, n_ok, n_err, last_print
        with lock:
            now = time.time()
            gap = now - last_call[0]
            if gap < args.gap:
                time.sleep(args.gap - gap)
            last_call[0] = time.time()
        # Retry within this call for transient
        resp = None
        for attempt in range(6):
            try:
                raw = call_model("gemini", task["prompt"], temperature=0,
                                  label=f"gemini_fillin/{task['event']}")
                resp = parse_json(raw)
                break
            except Exception as e:
                msg = str(e).lower()
                if attempt < 5 and any(s in msg for s in
                                         ("429", "rate", "quota", "timeout",
                                          "connection", "unavailable")):
                    delay = min(60, 5 * (2 ** attempt))
                    time.sleep(delay)
                    continue
                resp = {"error": f"{type(e).__name__}: {e}"}
                break
        # Write
        with lock:
            fh.write(json.dumps({
                "event": task["event"],
                "paper_id": task["paper_id"],
                "condition": task["condition"],
                "finding_idx": task["finding_idx"],
                "responses": [{"model": "gemini", "response": resp}],
            }) + "\n")
            fh.flush()
        with progress_lock:
            n_done += 1
            if isinstance(resp, dict) and not resp.get("error"):
                n_ok += 1
            else:
                n_err += 1
            now = time.time()
            if now - last_print >= 30 or n_done == len(tasks):
                elapsed = now - t0
                rate = n_done / max(1, elapsed)
                eta = (len(tasks) - n_done) / max(0.01, rate)
                print(f"  [{n_done}/{len(tasks)} ({n_ok} ok, {n_err} err), "
                      f"{elapsed:.0f}s elapsed, ETA {eta:.0f}s]")
                last_print = now

    print(f"Retrying with workers={args.workers}, gap={args.gap}s")
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        list(ex.map(call, tasks))

    fh.close()
    print(f"\nDONE. {n_ok} OK, {n_err} errors, {time.time()-t0:.0f}s")
    print(f"  output: {FILLIN}")


if __name__ == "__main__":
    main()
