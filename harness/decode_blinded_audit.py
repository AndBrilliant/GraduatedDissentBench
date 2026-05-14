#!/usr/bin/env python3
"""
Decode a completed blinded audit by joining the verdicts CSV with the
decoding key, then computing per-condition statistics.

Inputs:
  analysis/rw_false_positive_audit/blinded/audit_blinded.csv  (filled in)
  analysis/rw_false_positive_audit/blinded/decoding_key.csv

Outputs to stdout + a small markdown report:
  analysis/rw_false_positive_audit/blinded/audit_results.md

Run AFTER finishing the audit, not during.
"""
from __future__ import annotations

import csv
import math
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DIR = REPO / "analysis" / "rw_false_positive_audit" / "blinded"


def wilson_ci(k: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    if n == 0:
        return 0.0, 0.0
    z = 1.959963984540054
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    margin = z * math.sqrt((p * (1 - p) + z * z / (4 * n)) / n) / denom
    return max(0.0, center - margin), min(1.0, center + margin)


def main():
    verdicts_path = DIR / "audit_blinded.csv"
    key_path = DIR / "decoding_key.csv"
    if not verdicts_path.exists():
        print(f"missing: {verdicts_path}", file=sys.stderr); return 1
    if not key_path.exists():
        print(f"missing: {key_path}", file=sys.stderr); return 1

    # Load decoding
    cond_by_id = {}
    paper_by_id = {}
    with key_path.open() as f:
        for r in csv.DictReader(f):
            cond_by_id[r["finding_id"]] = r["condition"]
            paper_by_id[r["finding_id"]] = r["paper_id"]

    # Load verdicts
    counts = defaultdict(lambda: defaultdict(int))   # cond -> verdict -> n
    unrated = 0
    total_by_cond = defaultdict(int)
    valid_papers_by_cond = defaultdict(set)
    with verdicts_path.open() as f:
        for r in csv.DictReader(f):
            fid = r["finding_id"]
            cond = cond_by_id.get(fid, "?")
            total_by_cond[cond] += 1
            v = (r.get("verdict") or "").strip().upper()
            if v not in ("VALID", "RELATED", "FALSE"):
                unrated += 1
                continue
            counts[cond][v] += 1
            if v == "VALID":
                valid_papers_by_cond[cond].add(paper_by_id.get(fid, ""))

    # Original aggregate (matched / total RW):
    # GD 9/77, B3 6/97, B3PP 7/112
    original = {"GD": (9, 77), "B3": (6, 97), "B3PP": (7, 112)}

    # Adjusted RW-precision = (matched + valid) / total_RW
    lines = []
    lines.append("# Blinded audit — results\n\n")
    lines.append("## Per-condition verdict distribution (unmatched RW only)\n\n")
    lines.append("| Condition | Unmatched n | VALID | RELATED | FALSE | Unrated |\n")
    lines.append("|---|---:|---:|---:|---:|---:|\n")
    for c in ("GD", "B3", "B3PP"):
        n = total_by_cond.get(c, 0)
        v = counts[c].get("VALID", 0)
        r = counts[c].get("RELATED", 0)
        fa = counts[c].get("FALSE", 0)
        u = n - (v + r + fa)
        lines.append(f"| {c} | {n} | {v} | {r} | {fa} | {u} |\n")

    lines.append("\n## Adjusted RW-precision\n\n")
    lines.append("Original metric counts only SPOT-annotation matches as TPs. "
                  "Adjusted metric also counts VALID unmatched RW findings.\n\n")
    lines.append("| Condition | Matched (SPOT) | VALID unmatched | Total RW | "
                  "Original RW-prec | Adjusted RW-prec (Wilson 95% CI) |\n")
    lines.append("|---|---:|---:|---:|---:|---|\n")
    for c in ("GD", "B3", "B3PP"):
        matched, total_rw = original[c]
        valid = counts[c].get("VALID", 0)
        adj = (matched + valid) / total_rw if total_rw else 0
        lo, hi = wilson_ci(matched + valid, total_rw)
        orig = matched / total_rw if total_rw else 0
        lines.append(f"| {c} | {matched} | {valid} | {total_rw} | "
                      f"{100*orig:.1f}% | "
                      f"{matched + valid}/{total_rw} = {100*adj:.1f}% "
                      f"[{100*lo:.1f}, {100*hi:.1f}] |\n")

    lines.append("\n## Per-paper RW yield (papers with >=1 VALID RW)\n\n")
    for c in ("GD", "B3", "B3PP"):
        pset = valid_papers_by_cond[c]
        lines.append(f"- {c}: {len(pset)} papers have at least one VALID RW "
                      f"finding\n")

    if unrated:
        lines.append(f"\n_Note: {unrated} findings unrated. Re-run after "
                      "completing audit for final numbers._\n")

    out = "".join(lines)
    print(out)
    (DIR / "audit_results.md").write_text(out, encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main() or 0)
