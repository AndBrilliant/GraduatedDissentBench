# Full text-detectable SPOT run — lightweight verification

## Scope

The validated n=20 core was audited adversarially by two independent
evaluators (reports in `reports/`). This note covers the additional
30 papers that complete the full text-detectable SPOT subset (n=50).
The same prompts, models, temperatures, and judge configuration that
produced the n=20 results were used for the new 30; outputs live at
`data/spot/outputs/full_run/<safe_doi>/{B1,B2,B3,GD}.json` in the
broader repo and are aggregated into `data/spot/scoring/full_run/`.

## File integrity

| Check | Result |
|---|---|
| Paper directories | 50 |
| Output files | 200 (50 × 4) |
| Empty / malformed | 0 |
| Anonymization | All 50 anonymized via the same pipeline; `paper.raw.txt` preserved alongside `paper.txt` for every paper |

## Scoring reproducibility

Re-running `harness/scoring_spot.py` over the full sweep reproduces
the per-condition aggregates exactly:

```
condition  N  TPs  pass@1  recall  precision  lenient_RW
B1         50  13   24.0%  23.6%   1.03%      0.0
B2         50  15   28.0%  27.3%   2.41%      0.7
B3         50  16   30.0%  29.1%   2.77%      0.6
GD         50  19   36.0%  34.6%   2.91%      0.56
```

(SPOT-published o3 reference: 18.4% pass@1 / 21.1% recall on the full
83-paper benchmark with vision access.)

## TP spot-check

A 5-of-19 random sample of GD's true positives at n=50 was inspected
manually against the SPOT annotation. All five matched semantically
without dispute. The disputed paper from the n=20 audit
(`paper_014`) remains flagged in `scoring/per_paper_scores.csv`
(`disputed = yes`) and the aggregate emits `GD_strict` (excludes) and
`GD_standard` (includes) as separate rows.

No new disputed-TP cases identified during the spot-check on the new
30 papers.

## Discordant pairs (B3 vs GD)

At n=50: 5 papers GD detected and B3 did not, 2 papers B3 detected and
GD did not. McNemar exact two-sided $p = 0.4531$. Direction matches
the n=20 ablation (5/7 favor GD); statistical significance not
reached at this $n$.

## Stability check (split-half)

| Condition | Validated n=20 | New n=30 |
|---|---:|---:|
| B1 | 30% | 20% |
| B2 | 20% | 33% |
| B3 | 20% | 37% |
| GD | 30% | 40% |

GD's pass@1 is *higher* on the new 30 papers than on the validated
n=20. The full-n result is therefore not driven by the original
sample.

## Per-error-type concentration

GD's advantage concentrates in equation/proof errors (33 of 50
papers, 66% of the corpus): GD 48%, B3 42%, B2 39%, B1 30% pass@1.
For the small categories (n ≤ 5 each: data inconsistency, reagent
identity, experiment setup, figure-text inconsistency), all
conditions including GD score 0% — these categories are too sparse
to draw a conclusion and largely require visual inspection that our
text-only pipeline cannot do.

## Severity-tier behavior (RW emission, full n=50)

| Tier | B2 | B3 | **GD** |
|---|---:|---:|---:|
| Total RW findings | 115 | 97 | **77** |
| RW per paper | 2.30 | 1.94 | **1.54** |
| RW matching SPOT GT | 8 | 6 | **9** |
| **RW-precision** | 7.0% | 6.2% | **11.7%** |
| **RW-yield** | 20% | 20% | **32%** |

GD emits the fewest RW classifications per paper (1.54 vs 2.30 for
B2), but its per-classification precision is roughly twice that of
B2 or B3 in the RW tier (11.7% vs 7.0%, 6.2%). RW-yield --- when GD
flags a paper as retraction-worthy, the rate at which the SPOT
annotation agrees --- is 32% vs 20% for the alternative conditions.

This is the calibration contribution the protocol's "when in doubt,
MAJOR-REVISION" arbiter instruction is designed to produce, now
visible at scale rather than only at the small-n retracted-paper
benchmark.

## Notes / caveats

- The judge stage of the GD protocol fired correctly: 3 papers in
  the validated n=20 hit L0 (agreement >= 0.90) and skipped the
  steelman exchange; the remaining 47 papers across the full n=50
  hit L2 and ran the full exchange. None of the L0 papers participate
  in the B3-vs-GD discordant pair set.
- All severity classifications are LLM judgments; we do not have a
  human re-rating of severity. The SPOT annotations themselves are
  human-validated.
- Lenient detection (paper has any RW classification regardless of
  match) drops as $n$ grows because GD becomes more selective; this
  is consistent with the fewer-but-better-aimed RW flags story above.
