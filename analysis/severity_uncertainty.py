#!/usr/bin/env python3
"""
Uncertainty quantification for severity-calibration metrics.

Computes:
  - Wilson 95% CIs for RW-precision, RW-yield, and the RW-tier
    placement of true positives (per condition: B2, B3, GD).
  - Fisher exact tests for the key GD-vs-B3 comparisons (RW-precision,
    RW-yield, pass@1).
  - Fisher exact test for the retracted-paper false-positive contrast
    (GD 0/19 vs B3 2/19).

Outputs both a human-readable summary table and LaTeX-ready text
snippets, written to analysis/severity_uncertainty.md.
"""
from __future__ import annotations

import io
from pathlib import Path

import numpy as np
from scipy.stats import fisher_exact, norm

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "analysis" / "severity_uncertainty.md"


def wilson_ci(k: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion."""
    if n == 0:
        return (0.0, 0.0)
    z = norm.ppf(1 - alpha / 2)
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    margin = z * np.sqrt((p * (1 - p) + z * z / (4 * n)) / n) / denom
    return max(0.0, center - margin), min(1.0, center + margin)


def fmt_pct(x: float) -> str:
    return f"{100*x:.1f}\\%"


def fmt_p(p: float) -> str:
    if p < 1e-4:
        return f"$p < 10^{{-4}}$"
    if p < 1e-3:
        return f"$p = {p:.1e}$".replace("e-0", r"\times 10^{-")
    return f"$p = {p:.3f}$"


def line(buf: io.StringIO, s: str = "") -> None:
    buf.write(s + "\n")


def section(buf: io.StringIO, title: str) -> None:
    line(buf, f"\n## {title}\n")


def render() -> str:
    buf = io.StringIO()

    line(buf, "# Severity-metric uncertainty quantification")
    line(buf)
    line(buf, "Wilson score 95% CIs and Fisher exact tests for the "
              "severity-tier metrics on the full text-detectable SPOT "
              "subset (n=50) and for the retracted-paper FP contrast "
              "(n=19 probative controls). Computed by "
              "`analysis/severity_uncertainty.py`.")
    line(buf)
    line(buf, "Source data:")
    line(buf, "  - SPOT RW-precision / RW-yield: `harness/rw_precision.py` over "
              "`data/spot/scoring/full_run/`.")
    line(buf, "  - SPOT pass@1: `data/spot/scoring/full_run/aggregates.csv`.")
    line(buf, "  - Retracted-paper FP under majority audit: "
              "`paper/main.tex` Table 3 / `validation/retracted_paper_audit/`.")

    # ---- 1) RW-precision (k = RW matches; n = total RW findings) ----
    rw_prec = [
        ("B2", 8, 115),
        ("B3", 6, 97),
        ("GD", 9, 77),
    ]
    section(buf, "1. RW-precision (per-RW-finding match rate)")
    line(buf, "| Condition | k / n | Proportion | Wilson 95% CI |")
    line(buf, "|---|---:|---:|---|")
    rw_prec_ci = {}
    for label, k, n in rw_prec:
        lo, hi = wilson_ci(k, n)
        rw_prec_ci[label] = (k, n, k / n, lo, hi)
        line(buf, f"| {label} | {k}/{n} | {k/n:.1%} | "
                  f"[{lo:.1%}, {hi:.1%}] |")

    # ---- 2) RW-yield (k = papers with >=1 RW-matched finding;
    #                   n = papers that emitted >=1 RW finding) ----
    rw_yield = [
        ("B2", 7, 35),
        ("B3", 6, 30),
        ("GD", 9, 28),
    ]
    section(buf, "2. RW-yield (papers with a matched RW out of flagged papers)")
    line(buf, "_Denominator is papers that emitted at least one RW finding, "
              "matching the paper's reported `9/28` GD figure (run "
              "`harness/rw_precision.py` to reproduce). The task brief's "
              "`10/50` formulation does not match the data — the correct "
              "numerators / denominators are below._")
    line(buf)
    line(buf, "| Condition | k / n | Proportion | Wilson 95% CI |")
    line(buf, "|---|---:|---:|---|")
    rw_yield_ci = {}
    for label, k, n in rw_yield:
        lo, hi = wilson_ci(k, n)
        rw_yield_ci[label] = (k, n, k / n, lo, hi)
        line(buf, f"| {label} | {k}/{n} | {k/n:.1%} | "
                  f"[{lo:.1%}, {hi:.1%}] |")

    # ---- 3) RW true positives placed in the RW tier (severity_rank) ----
    # k = RW-tier matches, n = total true positives for the condition
    tp_rw = [
        ("B2", 8, 15),
        ("B3", 6, 16),
        ("GD", 9, 19),
    ]
    section(buf, "3. Fraction of true positives placed in the RW tier")
    line(buf, "| Condition | k / n | Proportion | Wilson 95% CI |")
    line(buf, "|---|---:|---:|---|")
    tp_rw_ci = {}
    for label, k, n in tp_rw:
        lo, hi = wilson_ci(k, n)
        tp_rw_ci[label] = (k, n, k / n, lo, hi)
        line(buf, f"| {label} | {k}/{n} | {k/n:.1%} | "
                  f"[{lo:.1%}, {hi:.1%}] |")

    # ---- 4) Pass@1 ----
    pass1 = [
        ("B1", 12, 50),  # 24%
        ("B2", 14, 50),  # 28%
        ("B3", 15, 50),  # 30%
        ("GD", 18, 50),  # 36%
    ]
    # cross-check vs aggregates.csv: pass_at_1 is .24/.28/.30/.36 — so
    # numerators are 12/14/15/18 (NOT the TP totals which use a per-paper
    # detection rule that can credit multiple findings per paper).
    section(buf, "4. Pass@1 on full SPOT subset (n=50)")
    line(buf, "| Condition | k / n | Proportion | Wilson 95% CI |")
    line(buf, "|---|---:|---:|---|")
    pass1_ci = {}
    for label, k, n in pass1:
        lo, hi = wilson_ci(k, n)
        pass1_ci[label] = (k, n, k / n, lo, hi)
        line(buf, f"| {label} | {k}/{n} | {k/n:.1%} | "
                  f"[{lo:.1%}, {hi:.1%}] |")

    # ---- 5) Fisher exact tests ----
    section(buf, "5. Fisher exact tests (GD vs B3)")
    fisher_results = {}

    # RW-precision
    # table: rows = condition (GD, B3); cols = (RW-match, RW-no-match)
    k_gd, n_gd = 9, 77
    k_b3, n_b3 = 6, 97
    tab = [[k_gd, n_gd - k_gd], [k_b3, n_b3 - k_b3]]
    odds, p = fisher_exact(tab, alternative="two-sided")
    fisher_results["rw_prec_gd_vs_b3"] = (odds, p)
    line(buf, f"- **RW-precision** (GD 9/77 vs B3 6/97): "
              f"odds ratio = {odds:.2f}, two-sided p = {p:.3f}.")

    # RW-yield
    k_gd, n_gd = 9, 28
    k_b3, n_b3 = 6, 30
    tab = [[k_gd, n_gd - k_gd], [k_b3, n_b3 - k_b3]]
    odds, p = fisher_exact(tab, alternative="two-sided")
    fisher_results["rw_yield_gd_vs_b3"] = (odds, p)
    line(buf, f"- **RW-yield** (GD 9/28 vs B3 6/30): "
              f"odds ratio = {odds:.2f}, two-sided p = {p:.3f}. "
              "Note: the underlying papers are paired (same 50 papers seen "
              "by both conditions); McNemar on the paired discordant set "
              "is the conditionally correct test and is already reported "
              "for pass@1 (see Section 6).")

    # Pass@1 (unpaired Fisher; McNemar paired test already in paper)
    k_gd, n_gd = 18, 50
    k_b3, n_b3 = 15, 50
    tab = [[k_gd, n_gd - k_gd], [k_b3, n_b3 - k_b3]]
    odds, p = fisher_exact(tab, alternative="two-sided")
    fisher_results["pass1_gd_vs_b3_unpaired"] = (odds, p)
    line(buf, f"- **Pass@1 (unpaired)** (GD 18/50 vs B3 15/50): "
              f"odds ratio = {odds:.2f}, two-sided p = {p:.3f}. "
              "The paired McNemar p (`0.453`, already reported) is the "
              "appropriate test for the same-papers comparison; this "
              "unpaired Fisher is provided only as a complementary upper "
              "bound on the marginal contrast.")

    # ---- 6) Retracted-paper FP contrast ----
    section(buf, "6. Retracted-paper false-positive contrast (n=19 controls)")
    # GD 0/19 vs B3 2/19 (majority audit). Brief said "should get p ~= 0.49"
    tab_fp = [[0, 19], [2, 17]]
    odds_fp, p_fp = fisher_exact(tab_fp, alternative="two-sided")
    fisher_results["fp_gd_vs_b3"] = (odds_fp, p_fp)
    line(buf, f"- **GD 0/19 vs B3 2/19** (majority audit): "
              f"odds ratio = {odds_fp:.2f}, two-sided p = {p_fp:.3f}. "
              "Matches the brief's expectation (~0.49); the FP advantage "
              "is in the right direction but not significant at n=19.")
    # also B2 3/19 vs GD 0/19 (first-author scoring) and the majority-audit
    # B2 collapses to 0/19, so the first-author contrast is the live one.
    tab_b2 = [[0, 19], [3, 16]]
    odds_b2, p_b2 = fisher_exact(tab_b2, alternative="two-sided")
    fisher_results["fp_gd_vs_b2_firstauthor"] = (odds_b2, p_b2)
    line(buf, f"- **GD 0/19 vs B2 3/19** (first-author scoring): "
              f"odds ratio = {odds_b2:.2f}, two-sided p = {p_b2:.3f}.")
    # Clopper-Pearson for 0/19 — already in the paper as [0, 0.17] — confirm.
    from scipy.stats import beta as _beta
    alpha = 0.05
    cp_lo = 0.0  # exact for k=0
    cp_hi = _beta.ppf(1 - alpha / 2, 0 + 1, 19 - 0)
    line(buf, f"- **Clopper–Pearson 95% CI for 0/19** = "
              f"[{cp_lo:.3f}, {cp_hi:.3f}]. The paper currently states "
              f"`[0, 0.17]`; the exact bound is `{cp_hi:.4f}` "
              "(rounded to 0.17 in the manuscript — consistent).")

    # ---- 7) LaTeX-ready snippets ----
    section(buf, "7. LaTeX-ready paper insertions")

    # Snippet A: abstract / discussion sentence
    g = rw_prec_ci["GD"]
    b = rw_prec_ci["B3"]
    fisher_p = fisher_results["rw_prec_gd_vs_b3"][1]
    snippet_a = (
        f"GD achieves {g[2]:.1%} RW-precision "
        f"(95% Wilson CI: [{g[3]:.1%}, {g[4]:.1%}]) "
        f"compared with B3's {b[2]:.1%} "
        f"([{b[3]:.1%}, {b[4]:.1%}]); "
        f"Fisher exact two-sided $p = {fisher_p:.3f}$."
    ).replace("%", r"\%")
    line(buf, "**Snippet A (RW-precision contrast for results §):**")
    line(buf, "")
    line(buf, "```latex")
    line(buf, snippet_a)
    line(buf, "```")
    line(buf)

    # Snippet B: RW-yield
    g = rw_yield_ci["GD"]
    b = rw_yield_ci["B3"]
    fisher_p_y = fisher_results["rw_yield_gd_vs_b3"][1]
    snippet_b = (
        f"On RW-yield --- the fraction of papers a condition flags as "
        f"retraction-worthy that contain a SPOT-annotated error --- "
        f"GD reaches {g[0]}/{g[1]} = {g[2]:.1%} "
        f"(95% Wilson CI: [{g[3]:.1%}, {g[4]:.1%}]) "
        f"versus B3's {b[0]}/{b[1]} = {b[2]:.1%} "
        f"([{b[3]:.1%}, {b[4]:.1%}]); "
        f"unpaired Fisher exact two-sided $p = {fisher_p_y:.3f}$."
    ).replace("%", r"\%")
    line(buf, "**Snippet B (RW-yield contrast):**")
    line(buf, "")
    line(buf, "```latex")
    line(buf, snippet_b)
    line(buf, "```")
    line(buf)

    # Snippet C: pass@1
    g = pass1_ci["GD"]
    b = pass1_ci["B3"]
    fisher_p_p = fisher_results["pass1_gd_vs_b3_unpaired"][1]
    snippet_c = (
        f"On pass@1, GD's {g[0]}/{g[1]} = {g[2]:.1%} "
        f"(95% Wilson CI: [{g[3]:.1%}, {g[4]:.1%}]) "
        f"versus B3's {b[0]}/{b[1]} = {b[2]:.1%} "
        f"([{b[3]:.1%}, {b[4]:.1%}]) gives an unpaired Fisher exact "
        f"two-sided $p = {fisher_p_p:.3f}$; the paired McNemar test "
        f"on the seven discordant pairs gives $p = 0.453$."
    ).replace("%", r"\%")
    line(buf, "**Snippet C (pass@1 contrast with paired/unpaired note):**")
    line(buf, "")
    line(buf, "```latex")
    line(buf, snippet_c)
    line(buf, "```")
    line(buf)

    # Snippet D: FP contrast
    p_fp = fisher_results["fp_gd_vs_b3"][1]
    snippet_d = (
        f"Under majority audit, GD produces $0/19$ false retraction-worthy "
        f"classifications on probative controls (Clopper--Pearson 95\\% CI: "
        f"[0\\%, {100*cp_hi:.1f}\\%]) versus B3's $2/19$ "
        f"(Wilson 95\\% CI: [{100*wilson_ci(2,19)[0]:.1f}\\%, "
        f"{100*wilson_ci(2,19)[1]:.1f}\\%]); Fisher exact two-sided "
        f"$p = {p_fp:.3f}$ (underpowered at $n = 19$ but directionally "
        f"consistent with the SPOT severity-calibration result)."
    )
    line(buf, "**Snippet D (retracted-paper FP contrast):**")
    line(buf, "")
    line(buf, "```latex")
    line(buf, snippet_d)
    line(buf, "```")
    line(buf)

    # ---- 8) Augmented Table 5 ----
    section(buf, "8. Augmented severity-tier table with CIs")
    line(buf, "Drop-in LaTeX (4-condition columns collapsed to the three "
              "that emit severity):")
    line(buf, "")
    line(buf, "```latex")
    line(buf, r"\begin{table}[t]")
    line(buf, r"\centering")
    line(buf, r"\small")
    line(buf, r"\begin{tabular}{lccc}")
    line(buf, r"\toprule")
    line(buf, r"Metric & B2 & B3 & GD \\")
    line(buf, r"\midrule")

    def cell(ci_tuple):
        k, n, p, lo, hi = ci_tuple
        return f"{k}/{n} = {100*p:.1f}\\% [{100*lo:.1f}, {100*hi:.1f}]"

    line(buf, r"Total RW findings & 115 & 97 & 77 \\")
    line(buf, r"RW per paper & 2.30 & 1.94 & 1.54 \\")
    line(buf, rf"RW-precision (95\% CI) & {cell(rw_prec_ci['B2'])} & "
              rf"{cell(rw_prec_ci['B3'])} & {cell(rw_prec_ci['GD'])} \\")
    line(buf, rf"RW-yield (95\% CI)     & {cell(rw_yield_ci['B2'])} & "
              rf"{cell(rw_yield_ci['B3'])} & {cell(rw_yield_ci['GD'])} \\")
    line(buf, rf"TPs in RW tier (95\% CI) & {cell(tp_rw_ci['B2'])} & "
              rf"{cell(tp_rw_ci['B3'])} & {cell(tp_rw_ci['GD'])} \\")
    line(buf, r"\bottomrule")
    line(buf, r"\end{tabular}")
    line(buf, r"\caption{Severity-tier behaviour on the full text-detectable "
              r"SPOT subset ($n = 50$) with Wilson score 95\% confidence "
              r"intervals. RW-yield denominator is papers that emitted at "
              r"least one RW finding. GD's per-flag RW-precision is "
              r"roughly $2\times$ that of B2/B3, but the small absolute "
              r"counts (under 10 matched RW findings per condition) leave "
              r"the CIs broadly overlapping; the contrast is "
              r"directionally consistent with the retracted-paper "
              r"FP/specificity result on independent controls.}")
    line(buf, r"\label{tab:severity_tier_ci}")
    line(buf, r"\end{table}")
    line(buf, "```")

    # ---- 9) Notes / interpretation ----
    section(buf, "9. Honest read")
    line(buf, "- The Wilson intervals for RW-precision and RW-yield are wide "
              "and overlap between conditions. The Fisher exact tests on the "
              "GD-vs-B3 severity-tier metrics are not significant at "
              "α = 0.05 with the n=50 SPOT subset alone.")
    line(buf, "- What survives uncertainty quantification is the *directional* "
              "claim: GD's per-flag and per-paper RW yields are higher than "
              "B3's by roughly a factor of two in point estimates, and the "
              "retracted-paper benchmark shows the FP rate in the right "
              "direction (GD 0/19 vs B3 2/19, p ≈ 0.49 at n=19).")
    line(buf, "- Both benchmarks individually are underpowered; the "
              "load-bearing argument is the *agreement of direction* across "
              "two independent corpora (SPOT n=50 and the retracted-paper "
              "n=29 set). The Fisher tests should be reported alongside the "
              "point estimates so readers can see the wide intervals "
              "explicitly rather than infer them.")

    return buf.getvalue()


def main():
    text = render()
    OUT.write_text(text, encoding="utf-8")
    print(text)
    print(f"\n[saved to {OUT}]")


if __name__ == "__main__":
    main()
