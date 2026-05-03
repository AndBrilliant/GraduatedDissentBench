#!/usr/bin/env python3
"""
Compare our SPOT pilot results to SPOT's published numbers.

After scoring_spot.py emits aggregates.csv, this script:
  - Reads the aggregates per condition (B1/B2/B3/GD).
  - Joins them with the published SPOT numbers from Son et al. (2025).
  - Emits a paper/tables/spot_comparison.* triplet (CSV/MD/TeX).

The SPOT published numbers we compare against are the o3 result on the
*full multimodal* benchmark; our text-only B1 is the apples-to-apples
single-model baseline against which the architecture contribution should
be judged.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd

REPO = Path(__file__).resolve().parent.parent

# Published SPOT numbers (Son et al., 2025) — best-case figures.
SPOT_PUBLISHED = pd.DataFrame([
    {"condition": "SPOT_o3_pass1",
     "label": "SPOT (Son et al.) — o3 single-model, vision, full benchmark",
     "N": 83,
     "TP_total": "—", "FP_total": "—", "FN_total": "—",
     "precision_micro": 0.061, "recall_micro": 0.211,
     "precision_macro": "—", "recall_macro": "—",
     "PPR": "—",
     "pass_at_1": 0.184,
     "detection_rate": "—",
     "notes": "Vision-capable; pass@4 = 37.8\\%."},
    {"condition": "SPOT_human_baseline",
     "label": "SPOT human-annotator agreement (reference)",
     "N": 91,
     "TP_total": "—", "FP_total": "—", "FN_total": "—",
     "precision_micro": "—", "recall_micro": "—",
     "precision_macro": "—", "recall_macro": "—",
     "PPR": "—",
     "pass_at_1": "—",
     "detection_rate": "—",
     "notes": "Cross-validated by independent annotators."},
])


def to_md(combined: pd.DataFrame) -> str:
    cols = ["condition", "label", "N", "precision_micro", "recall_micro",
            "PPR", "pass_at_1", "detection_rate", "notes"]
    df = combined[cols].copy()
    return "# SPOT comparison\n\n" + df.to_markdown(index=False) + "\n"


def to_latex(combined: pd.DataFrame) -> str:
    """Render a clean LaTeX longtable. Escape % only — values stay numeric."""
    def esc(s: object) -> str:
        s = str(s)
        s = s.replace("\\", r"\textbackslash{}")
        s = s.replace("&", r"\&")
        s = s.replace("%", r"\%")
        s = s.replace("_", r"\_")
        return s

    header = (r"\begin{table}[ht]" "\n"
              r"\centering" "\n"
              r"\caption{SPOT benchmark comparison. Top block: our four conditions on the "
              r"text-detectable subset (50 papers, 62 errors). Bottom block: published SPOT "
              r"numbers from \citet{son2025spot} for reference.}" "\n"
              r"\label{tab:spot_comparison}" "\n"
              r"\small" "\n"
              r"\begin{tabular}{lcccccc}" "\n"
              r"\toprule" "\n"
              r"\textbf{Condition} & \textbf{N} & \textbf{Precision} & \textbf{Recall} & "
              r"\textbf{PPR} & \textbf{pass@1} & \textbf{Detection} \\" "\n"
              r"\midrule" "\n")

    rows = []
    n_ours = sum(1 for _, r in combined.iterrows()
                 if not str(r["condition"]).startswith("SPOT_"))
    for i, r in combined.iterrows():
        if str(r["condition"]).startswith("SPOT_"):
            label = r["label"]
        else:
            label = r["condition"]
        row = " & ".join([
            esc(label),
            esc(r["N"]),
            esc(r["precision_micro"]),
            esc(r["recall_micro"]),
            esc(r["PPR"]),
            esc(r["pass_at_1"]),
            esc(r["detection_rate"]),
        ])
        rows.append(row + r" \\")
        if i == n_ours - 1:
            rows.append(r"\midrule")

    footer = (r"\bottomrule" "\n"
              r"\end{tabular}" "\n"
              r"\end{table}" "\n")
    return header + "\n".join(rows) + "\n" + footer


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--aggregates", default="data/spot/scoring/pilot_n10/aggregates.csv",
                   help="Path to aggregates.csv emitted by scoring_spot.py")
    p.add_argument("--out-stem", default="paper/tables/spot_comparison",
                   help="Output stem (writes .csv .md .tex)")
    args = p.parse_args()

    agg_path = REPO / args.aggregates
    if not agg_path.exists():
        print(f"!! aggregates not found: {agg_path}")
        print("   Run harness/sweep_pilot.py and harness/scoring_spot.py first.")
        return 1

    ours = pd.read_csv(agg_path)
    ours["label"] = ours["condition"].map({
        "B1": "B1: Single GPT-5.4 (text-only) — apples-to-apples vs SPOT o3",
        "B2": "B2: Single GPT-5.4 + severity rubric",
        "B3": "B3: Multi-model ensemble, no steelman",
        "GD": "Graduated dissent (this work)",
    }).fillna(ours["condition"])
    ours["notes"] = ""
    cols = ["condition", "label", "N", "TP_total", "FP_total", "FN_total",
            "precision_micro", "recall_micro", "precision_macro", "recall_macro",
            "PPR", "pass_at_1", "detection_rate", "notes"]
    ours_clean = ours[[c for c in cols if c in ours.columns]]
    combined = pd.concat([ours_clean, SPOT_PUBLISHED], ignore_index=True)

    out_dir = REPO / Path(args.out_stem).parent
    out_dir.mkdir(parents=True, exist_ok=True)
    base = REPO / args.out_stem
    combined.to_csv(base.with_suffix(".csv"), index=False)
    base.with_suffix(".md").write_text(to_md(combined), encoding="utf-8")
    base.with_suffix(".tex").write_text(to_latex(combined), encoding="utf-8")

    print(f"Wrote {base.with_suffix('.csv').relative_to(REPO)}")
    print(f"Wrote {base.with_suffix('.md').relative_to(REPO)}")
    print(f"Wrote {base.with_suffix('.tex').relative_to(REPO)}")
    print()
    print(combined[["condition", "N", "precision_micro", "recall_micro",
                    "PPR", "pass_at_1", "detection_rate"]].to_string(index=False))


if __name__ == "__main__":
    raise SystemExit(main() or 0)
