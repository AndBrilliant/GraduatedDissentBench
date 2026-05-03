#!/usr/bin/env python3
"""Quick on-disk status of the SPOT pilot. Runs in <1s, no API calls."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sweep", default="pilot_n10")
    args = p.parse_args()

    sweep_dir = REPO / "data" / "spot" / "outputs" / args.sweep
    if not sweep_dir.exists():
        print(f"No sweep dir at {sweep_dir}")
        return

    paper_dirs = [d for d in sweep_dir.iterdir() if d.is_dir()]
    paper_dirs.sort()
    n_papers = len(paper_dirs)
    expected_per_paper = 4
    n_expected = n_papers * expected_per_paper
    files = []
    for pd_ in paper_dirs:
        files.extend(sorted(pd_.glob("*.json")))

    n_done = len(files)
    by_cond: dict[str, int] = {"b1": 0, "b2": 0, "b3": 0, "gd": 0}
    seen_calls: set[tuple] = set()
    all_calls: list[dict] = []
    detections = {"b1": [], "b2": [], "b3": [], "gd": []}
    for f in files:
        data = json.loads(f.read_text(encoding="utf-8"))
        cond_low = f.stem.lower()
        if cond_low in by_cond:
            by_cond[cond_low] += 1
        for c in data.get("meta", {}).get("calls", []):
            cid = (c.get("label", ""), c.get("input_tokens"), c.get("output_tokens"))
            if cid not in seen_calls:
                seen_calls.add(cid)
                all_calls.append(c)
        # Detection-flag heuristic: a paper is "detected" if any finding contains
        # the ground-truth annotation description's first noun phrase. Without
        # the LLM judge we can't compute a real match here — this is just a
        # rough verdict-flag count.
        verdict = data.get("verdict", "")
        sev = data.get("severity_counts") or {}
        rw_count = sev.get("RETRACTION-WORTHY", 0) if sev else 0
        cond_low = f.stem.lower()
        if cond_low in detections:
            detections[cond_low].append({
                "paper_id": f.parent.name,
                "verdict": verdict,
                "rw_count": rw_count,
            })

    total_cost = sum(c.get("cost_usd", 0) for c in all_calls)

    print(f"Sweep: {args.sweep}")
    print(f"Papers in sample: {n_papers}")
    print(f"Tasks done: {n_done} of {n_expected}")
    for cond, n in by_cond.items():
        print(f"  {cond}: {n}/{n_papers}")
    print(f"True total cost (deduped {len(all_calls)} unique calls): ${total_cost:.4f}")
    print()
    print("Per-condition verdict + RW counts:")
    for cond in ["b1", "b2", "b3", "gd"]:
        flagged = sum(1 for d in detections[cond] if d["verdict"] == "flagged")
        rw_sum = sum(d["rw_count"] for d in detections[cond])
        n = len(detections[cond])
        if n:
            print(f"  {cond.upper()}: {flagged}/{n} flagged, total RW findings = {rw_sum}")


if __name__ == "__main__":
    main()
