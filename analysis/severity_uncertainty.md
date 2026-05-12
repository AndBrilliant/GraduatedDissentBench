# Severity-metric uncertainty quantification

Wilson score 95% CIs and Fisher exact tests for the severity-tier metrics on the full text-detectable SPOT subset (n=50) and for the retracted-paper FP contrast (n=19 probative controls). Computed by `analysis/severity_uncertainty.py`.

Source data:
  - SPOT RW-precision / RW-yield: `harness/rw_precision.py` over `data/spot/scoring/full_run/`.
  - SPOT pass@1: `data/spot/scoring/full_run/aggregates.csv`.
  - Retracted-paper FP under majority audit: `paper/main.tex` Table 3 / `validation/retracted_paper_audit/`.

## 1. RW-precision (per-RW-finding match rate)

| Condition | k / n | Proportion | Wilson 95% CI |
|---|---:|---:|---|
| B2 | 8/115 | 7.0% | [3.6%, 13.1%] |
| B3 | 6/97 | 6.2% | [2.9%, 12.8%] |
| GD | 9/77 | 11.7% | [6.3%, 20.7%] |

## 2. RW-yield (papers with a matched RW out of flagged papers)

_Denominator is papers that emitted at least one RW finding, matching the paper's reported `9/28` GD figure (run `harness/rw_precision.py` to reproduce). The task brief's `10/50` formulation does not match the data — the correct numerators / denominators are below._

| Condition | k / n | Proportion | Wilson 95% CI |
|---|---:|---:|---|
| B2 | 7/35 | 20.0% | [10.0%, 35.9%] |
| B3 | 6/30 | 20.0% | [9.5%, 37.3%] |
| GD | 9/28 | 32.1% | [17.9%, 50.7%] |

## 3. Fraction of true positives placed in the RW tier

| Condition | k / n | Proportion | Wilson 95% CI |
|---|---:|---:|---|
| B2 | 8/15 | 53.3% | [30.1%, 75.2%] |
| B3 | 6/16 | 37.5% | [18.5%, 61.4%] |
| GD | 9/19 | 47.4% | [27.3%, 68.3%] |

## 4. Pass@1 on full SPOT subset (n=50)

| Condition | k / n | Proportion | Wilson 95% CI |
|---|---:|---:|---|
| B1 | 12/50 | 24.0% | [14.3%, 37.4%] |
| B2 | 14/50 | 28.0% | [17.5%, 41.7%] |
| B3 | 15/50 | 30.0% | [19.1%, 43.8%] |
| GD | 18/50 | 36.0% | [24.1%, 49.9%] |

## 5. Fisher exact tests (GD vs B3)

- **RW-precision** (GD 9/77 vs B3 6/97): odds ratio = 2.01, two-sided p = 0.277.
- **RW-yield** (GD 9/28 vs B3 6/30): odds ratio = 1.89, two-sided p = 0.373. Note: the underlying papers are paired (same 50 papers seen by both conditions); McNemar on the paired discordant set is the conditionally correct test and is already reported for pass@1 (see Section 6).
- **Pass@1 (unpaired)** (GD 18/50 vs B3 15/50): odds ratio = 1.31, two-sided p = 0.671. The paired McNemar p (`0.453`, already reported) is the appropriate test for the same-papers comparison; this unpaired Fisher is provided only as a complementary upper bound on the marginal contrast.

## 6. Retracted-paper false-positive contrast (n=19 controls)

- **GD 0/19 vs B3 2/19** (majority audit): odds ratio = 0.00, two-sided p = 0.486. Matches the brief's expectation (~0.49); the FP advantage is in the right direction but not significant at n=19.
- **GD 0/19 vs B2 3/19** (first-author scoring): odds ratio = 0.00, two-sided p = 0.230.
- **Clopper–Pearson 95% CI for 0/19** = [0.000, 0.176]. The paper currently states `[0, 0.17]`; the exact bound is `0.1765` (rounded to 0.17 in the manuscript — consistent).

## 7. LaTeX-ready paper insertions

**Snippet A (RW-precision contrast for results §):**

```latex
GD achieves 11.7\% RW-precision (95\% Wilson CI: [6.3\%, 20.7\%]) compared with B3's 6.2\% ([2.9\%, 12.8\%]); Fisher exact two-sided $p = 0.277$.
```

**Snippet B (RW-yield contrast):**

```latex
On RW-yield --- the fraction of papers a condition flags as retraction-worthy that contain a SPOT-annotated error --- GD reaches 9/28 = 32.1\% (95\% Wilson CI: [17.9\%, 50.7\%]) versus B3's 6/30 = 20.0\% ([9.5\%, 37.3\%]); unpaired Fisher exact two-sided $p = 0.373$.
```

**Snippet C (pass@1 contrast with paired/unpaired note):**

```latex
On pass@1, GD's 18/50 = 36.0\% (95\% Wilson CI: [24.1\%, 49.9\%]) versus B3's 15/50 = 30.0\% ([19.1\%, 43.8\%]) gives an unpaired Fisher exact two-sided $p = 0.671$; the paired McNemar test on the seven discordant pairs gives $p = 0.453$.
```

**Snippet D (retracted-paper FP contrast):**

```latex
Under majority audit, GD produces $0/19$ false retraction-worthy classifications on probative controls (Clopper--Pearson 95\% CI: [0\%, 17.6\%]) versus B3's $2/19$ (Wilson 95\% CI: [2.9\%, 31.4\%]); Fisher exact two-sided $p = 0.486$ (underpowered at $n = 19$ but directionally consistent with the SPOT severity-calibration result).
```


## 8. Augmented severity-tier table with CIs

Drop-in LaTeX (4-condition columns collapsed to the three that emit severity):

```latex
\begin{table}[t]
\centering
\small
\begin{tabular}{lccc}
\toprule
Metric & B2 & B3 & GD \\
\midrule
Total RW findings & 115 & 97 & 77 \\
RW per paper & 2.30 & 1.94 & 1.54 \\
RW-precision (95\% CI) & 8/115 = 7.0\% [3.6, 13.1] & 6/97 = 6.2\% [2.9, 12.8] & 9/77 = 11.7\% [6.3, 20.7] \\
RW-yield (95\% CI)     & 7/35 = 20.0\% [10.0, 35.9] & 6/30 = 20.0\% [9.5, 37.3] & 9/28 = 32.1\% [17.9, 50.7] \\
TPs in RW tier (95\% CI) & 8/15 = 53.3\% [30.1, 75.2] & 6/16 = 37.5\% [18.5, 61.4] & 9/19 = 47.4\% [27.3, 68.3] \\
\bottomrule
\end{tabular}
\caption{Severity-tier behaviour on the full text-detectable SPOT subset ($n = 50$) with Wilson score 95\% confidence intervals. RW-yield denominator is papers that emitted at least one RW finding. GD's per-flag RW-precision is roughly $2\times$ that of B2/B3, but the small absolute counts (under 10 matched RW findings per condition) leave the CIs broadly overlapping; the contrast is directionally consistent with the retracted-paper FP/specificity result on independent controls.}
\label{tab:severity_tier_ci}
\end{table}
```

## 9. Honest read

- The Wilson intervals for RW-precision and RW-yield are wide and overlap between conditions. The Fisher exact tests on the GD-vs-B3 severity-tier metrics are not significant at α = 0.05 with the n=50 SPOT subset alone.
- What survives uncertainty quantification is the *directional* claim: GD's per-flag and per-paper RW yields are higher than B3's by roughly a factor of two in point estimates, and the retracted-paper benchmark shows the FP rate in the right direction (GD 0/19 vs B3 2/19, p ≈ 0.49 at n=19).
- Both benchmarks individually are underpowered; the load-bearing argument is the *agreement of direction* across two independent corpora (SPOT n=50 and the retracted-paper n=29 set). The Fisher tests should be reported alongside the point estimates so readers can see the wide intervals explicitly rather than infer them.
