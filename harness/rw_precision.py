#!/usr/bin/env python3
"""
RW-precision: of all findings classified RETRACTION-WORTHY by a condition,
how many match a SPOT ground-truth annotation?

For each condition that emits severity (B2, B3, GD):
  - total_rw       = sum of RW findings across all scored papers
  - rw_per_paper   = total_rw / N
  - rw_matching_gt = count of RW findings whose finding-index appears in
                     the saved judge match list for that (paper, condition)
  - rw_precision   = rw_matching_gt / total_rw
  - rw_yield       = (papers where >=1 RW finding matched GT) / (papers
                     where >=1 RW finding was emitted)
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parent.parent


def extract_predictions(blob: dict) -> list[dict]:
    """Same shape as scoring_spot.py: {location, description, severity, _orig_index}."""
    out = []
    for i, f in enumerate(blob.get("findings", []) or []):
        if not isinstance(f, dict):
            continue
        out.append({
            "_orig_index": i,
            "location": f.get("location") or "(not provided)",
            "description": f.get("finding", "") or f.get("description", ""),
            "severity": f.get("severity", ""),
        })
    return out


def main():
    if len(sys.argv) > 1:
        sweep = sys.argv[1]
    else:
        sweep = "full_run"
    sweep_dir = REPO / "data" / "spot" / "outputs" / sweep
    traces = REPO / "data" / "spot" / "scoring" / sweep / "judge_traces.jsonl"
    if not traces.exists():
        print(f"!! no judge traces yet at {traces}")
        return 1

    # Index judge_traces by (paper, condition)
    by_pc: dict[tuple[str, str], dict] = {}
    with traces.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            by_pc[(r["paper_id"], r["condition"])] = r

    # Walk raw outputs and compute per-condition stats
    rows: dict[str, dict] = {c: {"papers": 0, "total_rw": 0, "rw_matched": 0,
                                    "papers_with_rw": 0, "papers_with_rw_match": 0}
                              for c in ("B2", "B3", "GD")}

    for pdir in sorted(sweep_dir.iterdir()):
        if not pdir.is_dir():
            continue
        for cond in ("B2", "B3", "GD"):
            cond_lower = cond.lower()
            jpath = pdir / f"{cond_lower}.json"
            if not jpath.exists():
                continue
            blob = json.loads(jpath.read_text(encoding="utf-8"))
            preds = extract_predictions(blob)
            rw_indices = [p["_orig_index"] for p in preds
                          if p.get("severity") == "RETRACTION-WORTHY"]
            n_rw = len(rw_indices)
            paper_id = pdir.name
            rec = by_pc.get((paper_id, cond))
            matched_pred_indices: set[int] = set()
            if rec is not None:
                for m in rec.get("matches", []) or []:
                    pi = m.get("prediction_index")
                    if isinstance(pi, int):
                        matched_pred_indices.add(pi)
            # The judge's prediction_index is into the SAME list of predictions
            # that we just rebuilt — so a prediction's _orig_index equals its
            # position in preds. matched_pred_indices index into preds (positionally).
            # So we map back: a position in preds whose _orig_index is in
            # rw_indices and which is also in matched_pred_indices is an
            # RW finding that matched ground truth.
            n_rw_matched = sum(
                1 for pos, p in enumerate(preds)
                if p.get("severity") == "RETRACTION-WORTHY" and pos in matched_pred_indices
            )
            r = rows[cond]
            r["papers"] += 1
            r["total_rw"] += n_rw
            r["rw_matched"] += n_rw_matched
            if n_rw > 0:
                r["papers_with_rw"] += 1
                if n_rw_matched > 0:
                    r["papers_with_rw_match"] += 1

    print(f"Sweep: {sweep}\n")
    print("| Condition | Total RW findings | RW per paper | RW matching GT | RW-precision | RW-yield |")
    print("|---|---:|---:|---:|---:|---:|")
    for cond in ("B2", "B3", "GD"):
        r = rows[cond]
        N = r["papers"]
        total = r["total_rw"]
        rwpp = total / N if N else 0.0
        matched = r["rw_matched"]
        prec = matched / total if total else 0.0
        yield_ = r["papers_with_rw_match"] / r["papers_with_rw"] if r["papers_with_rw"] else 0.0
        print(f"| {cond} | {total} | {rwpp:.2f} | {matched} | {prec:.2%} | "
              f"{yield_:.2%} ({r['papers_with_rw_match']}/{r['papers_with_rw']}) |")
    print()
    print(f"N papers per condition: {rows['B2']['papers']}, {rows['B3']['papers']}, {rows['GD']['papers']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
