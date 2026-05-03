#!/usr/bin/env python3
"""
Severity rank analysis: when a condition emits findings, what severity
tier does it use, and which tier does the SPOT-annotated true positive
end up in?

Outputs:
  - A table per condition: count by severity × matched-to-ground-truth.
  - A horizontal stacked-bar PNG: matched (green) vs unmatched (gray)
    portions for each severity tier, side by side per condition.

The protocol's claim is that GD concentrates true positives at higher
severity tiers and emits less low-severity noise than B2 / B3. This
script measures that claim directly.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parent.parent

SEVERITIES = ("RETRACTION-WORTHY", "MAJOR-REVISION", "MINOR")


def main():
    sweep = sys.argv[1] if len(sys.argv) > 1 else "full_run"
    sweep_dir = REPO / "data" / "spot" / "outputs" / sweep
    traces = REPO / "data" / "spot" / "scoring" / sweep / "judge_traces.jsonl"

    by_pc: dict[tuple[str, str], dict] = {}
    if traces.exists():
        with traces.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                r = json.loads(line)
                by_pc[(r["paper_id"], r["condition"])] = r

    # counts[cond][severity] = (total, matched)
    counts: dict[str, dict[str, dict[str, int]]] = {
        c: {s: {"total": 0, "matched": 0} for s in SEVERITIES + ("(no severity)",)}
        for c in ("B2", "B3", "GD")
    }
    # Track which severity each TP landed in
    tp_severity: dict[str, list[str]] = defaultdict(list)

    n_papers = {c: 0 for c in ("B2", "B3", "GD")}

    for pdir in sorted(sweep_dir.iterdir()):
        if not pdir.is_dir():
            continue
        for cond in ("B2", "B3", "GD"):
            jpath = pdir / f"{cond.lower()}.json"
            if not jpath.exists():
                continue
            n_papers[cond] += 1
            blob = json.loads(jpath.read_text(encoding="utf-8"))
            findings = blob.get("findings", []) or []
            rec = by_pc.get((pdir.name, cond), {})
            matched_pred_indices = {m.get("prediction_index") for m in rec.get("matches", []) or []
                                    if isinstance(m.get("prediction_index"), int)}
            for i, f in enumerate(findings):
                if not isinstance(f, dict):
                    continue
                sev = f.get("severity", "(no severity)") or "(no severity)"
                if sev not in counts[cond]:
                    sev = "(no severity)"
                counts[cond][sev]["total"] += 1
                if i in matched_pred_indices:
                    counts[cond][sev]["matched"] += 1
                    tp_severity[cond].append(sev)

    # Print table
    print(f"Sweep: {sweep}\n")
    print("| Condition | Severity tier | Total findings | Matched GT | Match-rate within tier |")
    print("|---|---|---:|---:|---:|")
    for cond in ("B2", "B3", "GD"):
        for sev in SEVERITIES:
            t = counts[cond][sev]["total"]
            m = counts[cond][sev]["matched"]
            rate = (m / t) if t else 0.0
            print(f"| {cond} | {sev} | {t} | {m} | {rate:.1%} |")
        # Also show no-severity row only if non-zero
        if counts[cond]["(no severity)"]["total"]:
            t = counts[cond]["(no severity)"]["total"]
            m = counts[cond]["(no severity)"]["matched"]
            rate = (m / t) if t else 0.0
            print(f"| {cond} | (no severity) | {t} | {m} | {rate:.1%} |")
    print()
    print(f"N papers per condition: B2={n_papers['B2']}, B3={n_papers['B3']}, GD={n_papers['GD']}")
    print()
    print("Where do the true-positive matches land?")
    for cond in ("B2", "B3", "GD"):
        if not tp_severity[cond]:
            print(f"  {cond}: 0 TPs")
            continue
        from collections import Counter
        c = Counter(tp_severity[cond])
        bits = ", ".join(f"{k}={v}" for k, v in sorted(c.items()))
        print(f"  {cond}: {len(tp_severity[cond])} TPs -> {bits}")

    # Plot
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np

        matplotlib.rcParams.update({
            "font.family": "serif",
            "font.size": 10,
            "axes.titlesize": 11,
            "savefig.dpi": 200,
            "savefig.bbox": "tight",
            "axes.spines.top": False,
            "axes.spines.right": False,
        })
        fig, ax = plt.subplots(figsize=(8, 4.5))
        conds = ("B2", "B3", "GD")
        x = np.arange(len(conds))
        width = 0.25

        # For each severity tier, plot a stacked bar with matched (color) + unmatched (gray)
        offsets = [-1, 0, 1]  # RW, MajR, Minor positions
        tier_colors = {
            "RETRACTION-WORTHY": "#D55E00",
            "MAJOR-REVISION":    "#E69F00",
            "MINOR":             "#56B4E9",
        }
        for sev_idx, sev in enumerate(SEVERITIES):
            xs = x + offsets[sev_idx] * width
            totals = [counts[c][sev]["total"] for c in conds]
            matched = [counts[c][sev]["matched"] for c in conds]
            unmatched = [t - m for t, m in zip(totals, matched)]
            color = tier_colors[sev]
            ax.bar(xs, matched, width, color=color, edgecolor="white", linewidth=0.5,
                   label=f"{sev} (matched GT)" if sev_idx == 0 else None)
            ax.bar(xs, unmatched, width, bottom=matched, color=color, alpha=0.35,
                   edgecolor="white", linewidth=0.5,
                   label=f"{sev} (unmatched)" if sev_idx == 0 else None)
            for xi, ti, mi in zip(xs, totals, matched):
                if ti:
                    ax.text(xi, ti + 1, f"{mi}/{ti}", ha="center", fontsize=8)

        ax.set_xticks(x)
        ax.set_xticklabels(conds)
        ax.set_ylabel("Findings (total per condition)")
        ax.set_title("Findings by severity tier — matched (solid) vs unmatched (light) GT")

        from matplotlib.patches import Patch
        handles = [
            Patch(facecolor=tier_colors[s], label=s) for s in SEVERITIES
        ]
        handles.append(Patch(facecolor="#999999", label="solid = matched GT, light = unmatched"))
        ax.legend(handles=handles, loc="upper right", fontsize=8)
        ax.yaxis.grid(True, color="#e0e0e0", linewidth=0.5)
        ax.set_axisbelow(True)
        plt.tight_layout()
        out = REPO / "paper" / "figures" / "fig_severity_rank.png"
        out.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out)
        plt.close(fig)
        print(f"\nWrote {out.relative_to(REPO)}")
    except ImportError:
        print("(matplotlib not available; skipping plot)")


if __name__ == "__main__":
    raise SystemExit(main() or 0)
