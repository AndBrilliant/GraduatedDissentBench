#!/usr/bin/env python3
"""
Generate the literature comparison table for the paper.

Combines:
  1. Our four conditions (B1, B2, B3, GD) with their detection / FP numbers.
  2. Six published comparator studies' headline numbers (from the handoff).

Outputs:
  - paper/tables/comparison_table.tex   (LaTeX, drop-in for paper)
  - paper/tables/comparison_table.csv   (CSV, easy machine read)
  - paper/tables/comparison_table.md    (Markdown, easy human read)
"""
from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent

import pandas as pd

REPO = Path(__file__).resolve().parent.parent

# ── Our results ────────────────────────────────────────────────────────
# Headline numbers from the original n=10 retracted papers + 19 controls.
# Will be regenerated with expanded n later; this is the seed table.
OUR_RESULTS = pd.DataFrame([
    {"row": "B1: Single model, no rubric (Liang 2024 baseline)",
     "approach": "Single GPT-5.4",
     "ground_truth": "10 retracted papers",
     "detection": "3/10 (30%)",
     "false_positive": "—",
     "notes": "No severity classification"},
    {"row": "B2: Single model + severity rubric",
     "approach": "Single GPT-5.4 + severity rubric",
     "ground_truth": "10 retracted, 19 controls",
     "detection": "4/10 (40%)",
     "false_positive": "3/19 (16%)",
     "notes": "Adds RW/Major/Minor labels"},
    {"row": "B3: Multi-model ensemble, no steelman (Wang 2023 / Du 2024 family)",
     "approach": "GPT-5.4 + DeepSeek pooled to Opus arbiter",
     "ground_truth": "10 retracted, 19 controls",
     "detection": "3/10 (30%)",
     "false_positive": "1/19 (5%)",
     "notes": "Self-consistency-style pooling"},
    {"row": "Graduated dissent (this work)",
     "approach": "GPT-5.4 + DeepSeek + steelman + Opus arbiter",
     "ground_truth": "10 retracted, 19 controls",
     "detection": "7/10 (70%)",
     "false_positive": "0/19 (0%)",
     "notes": "Adversarial steelman exchange"},
])

# ── Published comparator studies ───────────────────────────────────────
# Numbers from the handoff (Task 5). Update this dict if better numbers arrive
# from a re-read of the source papers.
LITERATURE = pd.DataFrame([
    {"row": "SPOT 2025 (Son et al.)",
     "approach": "Single-model LLM review (vision)",
     "ground_truth": "83 papers, 91 human-annotated errors",
     "detection": "o3 18.4% pass@1; 37.8% pass@4",
     "false_positive": "Precision 6.1%, recall 21.1%",
     "notes": "Models rarely find same errors across runs"},

    {"row": "FLAWS 2025 (Xi et al.)",
     "approach": "Single-model error localization",
     "ground_truth": "713 papers with LLM-inserted errors",
     "detection": "GPT-5: 39.1% identification at k=10",
     "false_positive": "Holistic review weaker than targeted",
     "notes": "LLM-inserted (not real) errors"},

    {"row": "Pub-Guard-LLM 2025 (Chen et al.)",
     "approach": "Fine-tuned LLM + RAG + debate",
     "ground_truth": "11K PubMed articles (retraction status)",
     "detection": "~91% retraction classification",
     "false_positive": "—",
     "notes": "Binary classification, not specific error ID"},

    {"row": '"To Err Is Human" 2025',
     "approach": "GPT-5-based correctness checker",
     "ground_truth": "316 expert-validated mistakes (ML)",
     "detection": "—",
     "false_positive": "Precision 83.2% (human-validated)",
     "notes": "Restricted to objective errors"},

    {"row": "Liang 2024 (NEJM AI)",
     "approach": "Single GPT-4 review",
     "ground_truth": "Human reviewer comments (not GT)",
     "detection": "30.85% (Nature) / 39.23% (ICLR) overlap",
     "false_positive": "Positivity bias noted",
     "notes": "Overlap metric, not detection rate"},

    {"row": "MARG 2024 (Darcy et al.)",
     "approach": "Multi-agent review generation",
     "ground_truth": "User-rated comments",
     "detection": "3.7 good comments/paper",
     "false_positive": "Generic-comment rate 60%→29%",
     "notes": "Not tested against ground truth"},
])


def to_latex(combined: pd.DataFrame) -> str:
    """Render a clean LaTeX longtable. Any LaTeX special chars are escaped."""
    def esc(s: str) -> str:
        s = str(s)
        # Escape % and & inside cells; LaTeX needs them as \% \&.
        s = s.replace("\\", r"\textbackslash{}")
        s = s.replace("&", r"\&")
        s = s.replace("%", r"\%")
        s = s.replace("_", r"\_")
        s = s.replace("#", r"\#")
        s = s.replace("$", r"\$")
        s = s.replace("→", r"$\rightarrow$")
        s = s.replace("—", r"---")
        s = s.replace("~", r"$\sim$")
        return s

    header = (r"\begin{longtable}{p{4.5cm} p{4cm} p{2.5cm} p{2.5cm} p{2.5cm}}" "\n"
              r"\caption{Comparison with recent algorithms on scientific-error detection. "
              r"Our four conditions appear in the top block; published comparators in the bottom block. "
              r"Ground truth and metrics differ across studies; numbers are best-result figures from each paper.}"
              r"\label{tab:comparison} \\" "\n"
              r"\toprule" "\n"
              r"\textbf{Approach} & \textbf{Method} & \textbf{Ground truth} & \textbf{Detection} & \textbf{False positive / precision} \\" "\n"
              r"\midrule" "\n"
              r"\endfirsthead" "\n"
              r"\toprule" "\n"
              r"\textbf{Approach} & \textbf{Method} & \textbf{Ground truth} & \textbf{Detection} & \textbf{False positive / precision} \\" "\n"
              r"\midrule" "\n"
              r"\endhead" "\n")

    rows = []
    n_ours = len(OUR_RESULTS)
    for i, r in combined.iterrows():
        row = " & ".join([esc(r["row"]), esc(r["approach"]),
                          esc(r["ground_truth"]),
                          esc(r["detection"]),
                          esc(r["false_positive"])])
        rows.append(row + r" \\")
        if i == n_ours - 1:
            rows.append(r"\midrule")

    footer = (r"\bottomrule" "\n"
              r"\end{longtable}" "\n")
    return header + "\n".join(rows) + "\n" + footer


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--from-csv", default=None,
                   help="Optional: pull our results from a sweep aggregates.csv "
                        "instead of the hardcoded values.")
    args = p.parse_args()

    if args.from_csv:
        sweep = pd.read_csv(args.from_csv)
        # TODO: expand this once the SPOT pilot finishes — replace OUR_RESULTS
        # rows with computed numbers including SPOT detection.
        print(f"(loaded sweep from {args.from_csv}; not yet wired in)")

    out_dir = REPO / "paper" / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)

    combined = pd.concat([OUR_RESULTS, LITERATURE], ignore_index=True)
    combined.to_csv(out_dir / "comparison_table.csv", index=False)

    md_lines = ["# Comparison with recent algorithms",
                "",
                "## Our conditions",
                "",
                "| Approach | Method | Ground truth | Detection | False positive / precision |",
                "|---|---|---|---|---|"]
    for _, r in OUR_RESULTS.iterrows():
        md_lines.append(f"| {r['row']} | {r['approach']} | {r['ground_truth']} | "
                        f"{r['detection']} | {r['false_positive']} |")
    md_lines += ["", "## Published comparators",
                 "",
                 "| Approach | Method | Ground truth | Detection | False positive / precision |",
                 "|---|---|---|---|---|"]
    for _, r in LITERATURE.iterrows():
        md_lines.append(f"| {r['row']} | {r['approach']} | {r['ground_truth']} | "
                        f"{r['detection']} | {r['false_positive']} |")
    (out_dir / "comparison_table.md").write_text("\n".join(md_lines), encoding="utf-8")

    (out_dir / "comparison_table.tex").write_text(to_latex(combined), encoding="utf-8")

    print(f"Wrote {(out_dir / 'comparison_table.csv').relative_to(REPO)}")
    print(f"Wrote {(out_dir / 'comparison_table.md').relative_to(REPO)}")
    print(f"Wrote {(out_dir / 'comparison_table.tex').relative_to(REPO)}")


if __name__ == "__main__":
    main()
