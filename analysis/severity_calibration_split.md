# Severity calibration: retract-tier vs errata-tier placement

SPOT annotates each paper's error with one of two severity levels:

- `retract` — error caused the paper to be retracted (genuinely retraction-worthy).
- `errata` — error caused a published correction (major-revision-tier, NOT retraction-worthy).

A severity-calibrated reviewer places true-positives matched to `retract`-tier annotations in its own RETRACTION-WORTHY (RW) severity tier, and TPs matched to `errata`-tier annotations in MAJOR-REVISION. An uncalibrated reviewer treats them identically.

**Calibration score** = P(RW | retract-TP) − P(RW | errata-TP). Range [−1, 1]; perfect calibration = 1, no calibration ≈ 0.

## Headline table

| Condition | Retract TPs | RW on retract [95% Wilson CI] | Errata TPs | RW on errata [95% Wilson CI] | Calibration | Within-cond Fisher p |
|---|---:|---|---:|---|---:|---:|
| B2 | 14 | 7/14 = 50.0% [26.8%, 73.2%] | 1 | 1/1 = 100.0% [20.7%, 100.0%] | -50.0 pp | 1.000 |
| B3 | 14 | 5/14 = 35.7% [16.3%, 61.2%] | 2 | 1/2 = 50.0% [9.5%, 90.5%] | -14.3 pp | 1.000 |
| B3+ | 10 | 5/10 = 50.0% [23.7%, 76.3%] | 2 | 1/2 = 50.0% [9.5%, 90.5%] | 0.0 pp | 1.000 |
| B3++ | 14 | 6/14 = 42.9% [21.4%, 67.4%] | 5 | 1/5 = 20.0% [3.6%, 62.4%] | 22.9 pp | 0.603 |
| GD | 16 | 8/16 = 50.0% [28.0%, 72.0%] | 3 | 1/3 = 33.3% [6.1%, 79.2%] | 16.7 pp | 1.000 |

## Paper-level detection by ground-truth severity

Corpus split: 27 retract papers + 23 errata papers in the n=50 SPOT text-detectable subset (B2/B3/GD evaluated). B3+/B3++ evaluated on n=49 intersection (27 retract + 22 errata).

| Condition | Retract papers detected | Errata papers detected | Detection gap |
|---|---:|---:|---:|
| B2 | 13/27 = 48% | 1/23 = 4% | 44 pp |
| B3 | 13/27 = 48% | 2/23 = 9% | 39 pp |
| B3+ | 9/27 = 33% | 2/22 = 9% | 24 pp |
| B3++ | 13/27 = 48% | 5/22 = 23% | 25 pp |
| GD | 15/27 = 56% | 3/23 = 13% | 43 pp |

**This is the real signal**: errata-tier errors are much harder to detect than retract-tier errors across ALL conditions. The detection gap is roughly 30-50 percentage points. This is consistent with the intuition that genuinely retraction-worthy errors are blunter and more visible than correctable errata-level issues.

## Severity-tier distribution of matched TPs

(Reading: when the TP matched a `retract` annotation, where did the condition place it severity-wise? And on errata?)

| Condition | retract-TP severity dist | errata-TP severity dist |
|---|---|---|
| B2 | {'MAJOR-REVISION': 6, 'RETRACTION-WORTHY': 7, 'MINOR': 1} | {'RETRACTION-WORTHY': 1} |
| B3 | {'MAJOR-REVISION': 9, 'RETRACTION-WORTHY': 5} | {'RETRACTION-WORTHY': 1, 'MAJOR-REVISION': 1} |
| B3+ | {'MAJOR-REVISION': 5, 'RETRACTION-WORTHY': 5} | {'RETRACTION-WORTHY': 1, 'MAJOR-REVISION': 1} |
| B3++ | {'MAJOR-REVISION': 8, 'RETRACTION-WORTHY': 6} | {'MAJOR-REVISION': 4, 'RETRACTION-WORTHY': 1} |
| GD | {'MAJOR-REVISION': 8, 'RETRACTION-WORTHY': 8} | {'MAJOR-REVISION': 2, 'RETRACTION-WORTHY': 1} |

## Cross-condition Fisher tests

Test: does the chosen condition's RW-on-retract (or RW-on-errata) rate differ from a comparator?

| Comparison | OR (retract) | p (retract) | OR (errata) | p (errata) |
|---|---:|---:|---:|---:|
| GD vs B3 | 1.80 | 0.484 | 0.50 | 1.000 |
| GD vs B3+ | 1.00 | 1.000 | 0.50 | 1.000 |
| GD vs B3++ | 1.33 | 0.730 | 2.00 | 1.000 |
| GD vs B2 | 1.00 | 1.000 | 0.00 | 1.000 |

## Honest read

Things to look for:

- **A high calibration score for GD** with low scores for B3 / B3+ / B3++ would support the paper's claim that the steelman exchange uniquely produces severity calibration.
- If all conditions have similar calibration, the SPOT split is consistent with 'severity calibration is not different 'from any of these protocols.'
- **Sample-size caveat**: errata annotations dominate (59/91 SPOT-classification rows), and most TPs at n=49/50 may be of one severity. If a cell is <5 TPs, Fisher tests are underpowered.
- The annotation-level severity is from the SPOT authors (human-validated), and is independent of the audit chain in this study. This is a stronger test of calibration than the LLM-rejudging used in the retracted-paper benchmark.

## Auto-narrative

- Pooled non-adversarial baseline (B3 + B3+ + B3++): P(RW|retract) = 16/38 = 42.1%; P(RW|errata) = 3/9 = 33.3%; calibration = 8.8 pp.
- GD vs pooled non-adversarial:
    - P(RW|retract): GD 8/16 = 50.0% vs pooled 42.1%, OR=1.38, p=0.765
    - P(RW|errata): GD 1/3 = 33.3% vs pooled 33.3%, OR=1.00, p=1.000
