#!/usr/bin/env python3
"""
Compare B3 / B3+ / B3++ / GD on the n=49 SPOT intersection.

  - pass@1, recall (from existing aggregates)
  - RW-precision (RW findings matching SPOT GT / total RW)
  - RW-yield   (papers with >=1 RW match / papers with >=1 RW)
  - RW per paper

Uses judge_traces.jsonl for both sweeps to identify matched findings.

Paper 10.1038_s41598-025-91235-1 is excluded — OpenAI safety filter blocks
it for B3+/B3++ (newly tightened biology restrictions); the n=49 intersection
is the apples-to-apples comparison set.

Outputs:
  analysis/budget_matched_comparison.md
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "harness"))

FULL_RUN_DIR = REPO / "data" / "spot" / "outputs" / "full_run"
BUDGET_DIR = REPO / "data" / "spot" / "outputs" / "budget_matched"
FULL_SCORE = REPO / "data" / "spot" / "scoring" / "full_run"
BUDGET_SCORE = REPO / "data" / "spot" / "scoring" / "budget_matched"

EXCLUDED_PAPER = "10.1038_s41598-025-91235-1"
OUT_MD = REPO / "analysis" / "budget_matched_comparison.md"


def load_matched_indices(traces_path: Path) -> dict:
    """Returns {(paper_id, condition): set(prediction_index)}."""
    out: dict = {}
    if not traces_path.exists():
        return out
    with traces_path.open() as f:
        for line in f:
            r = json.loads(line)
            key = (r["paper_id"], r["condition"])
            out[key] = {m["prediction_index"] for m in r.get("matches", [])
                        if isinstance(m.get("prediction_index"), int)}
    return out


def load_findings(out_dir: Path, paper_id: str,
                   condition_filename: str) -> list[dict]:
    p = out_dir / paper_id / f"{condition_filename}.json"
    if not p.exists():
        return []
    blob = json.loads(p.read_text())
    return blob.get("findings", []) or []


def compute_stats(out_dir: Path, score_dir: Path,
                   condition: str, condition_filename: str,
                   paper_set: set[str]) -> dict:
    """For each paper in paper_set, walk findings and compute RW stats."""
    matched_by_pc = load_matched_indices(score_dir / "judge_traces.jsonl")
    total_rw = 0
    rw_matched = 0
    papers_with_rw = 0
    papers_with_rw_match = 0
    total_papers = 0
    tp_total = 0
    pass_at_1 = 0  # papers where at least one finding matched any GT error

    for pid in sorted(paper_set):
        findings = load_findings(out_dir, pid, condition_filename)
        if not findings:
            continue
        total_papers += 1
        matched = matched_by_pc.get((pid, condition.upper()), set())
        # RW counts
        rw_positions = [i for i, f in enumerate(findings)
                         if isinstance(f, dict)
                         and f.get("severity") == "RETRACTION-WORTHY"]
        n_rw = len(rw_positions)
        n_rw_matched = sum(1 for pos in rw_positions if pos in matched)
        total_rw += n_rw
        rw_matched += n_rw_matched
        if n_rw > 0:
            papers_with_rw += 1
            if n_rw_matched > 0:
                papers_with_rw_match += 1
        tp_total += len(matched)
        if matched:
            pass_at_1 += 1

    return {
        "N": total_papers,
        "TP_total": tp_total,
        "pass_at_1": pass_at_1,
        "total_rw": total_rw,
        "rw_matched": rw_matched,
        "rw_per_paper": total_rw / max(1, total_papers),
        "rw_precision": rw_matched / max(1, total_rw),
        "papers_with_rw": papers_with_rw,
        "papers_with_rw_match": papers_with_rw_match,
        "rw_yield": papers_with_rw_match / max(1, papers_with_rw),
    }


def wilson_ci(k: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    if n == 0:
        return 0.0, 0.0
    import math
    z = 1.959963984540054  # 0.975 quantile of N(0,1)
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    margin = z * math.sqrt((p * (1 - p) + z * z / (4 * n)) / n) / denom
    return max(0.0, center - margin), min(1.0, center + margin)


def main():
    # Build the n=49 intersection: papers present in both sweeps, excluding
    # the OpenAI-safety-blocked paper.
    full_papers = {p.name for p in FULL_RUN_DIR.iterdir() if p.is_dir()}
    budget_papers = {p.name for p in BUDGET_DIR.iterdir() if p.is_dir()}
    intersection = (full_papers & budget_papers) - {EXCLUDED_PAPER}
    print(f"n=49 intersection: {len(intersection)} papers")
    if len(intersection) != 49:
        print(f"  WARN: expected 49, got {len(intersection)}")

    # Compute stats per condition
    rows = []
    rows.append(("B3", compute_stats(FULL_RUN_DIR, FULL_SCORE,
                                       "B3", "b3", intersection)))
    rows.append(("B3+", compute_stats(BUDGET_DIR, BUDGET_SCORE,
                                        "B3PLUS", "b3plus", intersection)))
    rows.append(("B3++", compute_stats(BUDGET_DIR, BUDGET_SCORE,
                                         "B3PLUSPLUS", "b3plusplus",
                                         intersection)))
    rows.append(("GD", compute_stats(FULL_RUN_DIR, FULL_SCORE,
                                       "GD", "gd", intersection)))

    # Print and format markdown
    print()
    print(f"{'Cond':<6} {'N':>3} {'pass@1':>8} {'TPs':>5} {'RW total':>9} "
          f"{'RW/paper':>9} {'RW-prec':>8} {'RW-yield':>10}")
    print("-" * 70)
    for name, s in rows:
        rwp = f"{s['rw_matched']}/{s['total_rw']}={100*s['rw_precision']:.1f}%"
        rwy = f"{s['papers_with_rw_match']}/{s['papers_with_rw']}={100*s['rw_yield']:.1f}%"
        p1 = f"{s['pass_at_1']}/{s['N']}={100*s['pass_at_1']/max(1,s['N']):.1f}%"
        print(f"{name:<6} {s['N']:>3} {p1:>16} {s['TP_total']:>5} "
              f"{s['total_rw']:>9} {s['rw_per_paper']:>9.2f} "
              f"{rwp:>16} {rwy:>20}")

    # Build markdown
    md = []
    md.append("# Budget-matched comparison: B3 / B3+ / B3++ / GD on n=49 SPOT\n\n")
    md.append("Paper excluded from comparison: "
              f"`{EXCLUDED_PAPER}` — OpenAI's safety filter (biology "
              "restriction) blocks GPT-5.4 from accepting the prover prompt "
              "for B3+/B3++ runs, even though the same prompt succeeded for "
              "the original B1/B2/B3/GD sweep. The n=49 intersection is the "
              "apples-to-apples comparison set.\n\n")

    md.append("## Pipeline shapes\n\n")
    md.append("| Condition | Calls/paper | Reflection prompt |\n")
    md.append("|---|---:|---|\n")
    md.append("| B3 | 3 | (none — pool both reviews directly) |\n")
    md.append("| B3+ | 5 | Neutral: 'Re-examine your findings, "
              "reconsider whether severity is right.' |\n")
    md.append("| B3++ | 5 | Anti-steelman: 'Build the strongest case "
              "FOR your severity ratings.' |\n")
    md.append("| GD | 5-6 | Steelman: 'Build the strongest case for the "
              "OTHER reviewer's position.' |\n\n")

    md.append("## Headline numbers (n=49)\n\n")
    md.append("| Condition | pass@1 | pass@1 95% Wilson CI | RW per paper | "
              "RW-precision | RW-yield |\n")
    md.append("|---|---:|---|---:|---:|---:|\n")
    for name, s in rows:
        lo, hi = wilson_ci(s["pass_at_1"], s["N"])
        ci = f"[{100*lo:.1f}%, {100*hi:.1f}%]"
        rwp = f"{s['rw_matched']}/{s['total_rw']} = {100*s['rw_precision']:.1f}%"
        rwy = (f"{s['papers_with_rw_match']}/{s['papers_with_rw']} = "
                f"{100*s['rw_yield']:.1f}%")
        md.append(f"| {name} | {s['pass_at_1']}/{s['N']} = "
                   f"{100*s['pass_at_1']/max(1,s['N']):.1f}% | {ci} | "
                   f"{s['rw_per_paper']:.2f} | {rwp} | {rwy} |\n")

    md.append("\n## What the table shows\n\n")
    # Auto-generate a short narrative based on the numbers
    b3 = next(s for n, s in rows if n == "B3")
    b3p = next(s for n, s in rows if n == "B3+")
    b3pp = next(s for n, s in rows if n == "B3++")
    gd = next(s for n, s in rows if n == "GD")

    md.append("**Same-compute, different reflection prompt — pass@1:**\n\n")
    md.append(f"- B3 (no reflection, 3 calls): {b3['pass_at_1']}/{b3['N']} "
              f"= {100*b3['pass_at_1']/b3['N']:.1f}%\n")
    md.append(f"- B3+ (neutral reflection, 5 calls): {b3p['pass_at_1']}/{b3p['N']} "
              f"= {100*b3p['pass_at_1']/b3p['N']:.1f}%\n")
    md.append(f"- B3++ (anti-steelman, 5 calls): {b3pp['pass_at_1']}/{b3pp['N']} "
              f"= {100*b3pp['pass_at_1']/b3pp['N']:.1f}%\n")
    md.append(f"- GD (steelman, 5-6 calls): {gd['pass_at_1']}/{gd['N']} "
              f"= {100*gd['pass_at_1']/gd['N']:.1f}%\n\n")

    md.append("**Same-compute, different reflection prompt — RW-precision:**\n\n")
    for name, s in rows:
        md.append(f"- {name}: {s['rw_matched']}/{s['total_rw']} = "
                   f"{100*s['rw_precision']:.1f}%\n")
    md.append("\n")

    md.append("## Interpretation hooks\n\n")
    md.append("- B3+ tests whether *any* re-engagement helps. "
              "If B3+ ≈ B3, the second pass alone doesn't carry signal.\n")
    md.append("- B3++ tests whether *adversarial* framing is necessary. "
              "If B3++ ≈ B3, only adversarial works. "
              "If B3++ ≈ GD, the second pass itself matters but not its direction.\n")
    md.append("- GD vs B3++ separates 'self-defense' from 'steelman the other side'.\n")

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("".join(md), encoding="utf-8")
    print(f"\n[saved to {OUT_MD}]")


if __name__ == "__main__":
    main()
