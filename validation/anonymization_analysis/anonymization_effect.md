# Anonymization effect: before vs after re-anonymization

## Setup

Of the n=20 SPOT pilot papers, 10 were originally run on un-
anonymized text (the parsed content as published by the SPOT
dataset, including author bylines, journal headers, dates, and
affiliations). The other 10 were run on text passed through the
anonymization pipeline used in an earlier retracted-paper
benchmark.

This document compares model performance on the *same 10 papers*
under the two conditions:
- **Pre-fix**: original parsed text (un-anonymized)
- **Post-fix**: same 10 papers re-run on anonymized text

All other inputs (prompts, model versions, parameters, judge)
are identical between the two runs.

## Aggregate pass@1 on the 10 affected papers

| Condition | Pre-fix (un-anon) | Post-fix (anon) | Δ (pp) |
|---|---:|---:|---:|
| B1 | 10.00% | 10.00% | +0.0 |
| B2 | 10.00% | 10.00% | +0.0 |
| B3 | 20.00% | 10.00% | -10.0 |
| GD | 20.00% | 10.00% | -10.0 |

## Per-paper detection-flip table

Rows are the 10 originally-unanonymized papers. Each cell shows
`pre→post` per condition, with markers for flips: `→TP` means
the paper was missed pre-fix and detected post-fix; `→miss`
means it was detected pre-fix and missed post-fix. Blank means
no change.

| Paper | Category | SPOT error type | B1 | B2 | B3 | GD |
|---|---|---|---|---|---|---|
| paper_001 | Materials Science | Data Inconsistency (figu | 0→0  | 0→0  | 0→0  | 0→0  |
| paper_003 | Environmental Scie | Data Inconsistency (figu | 0→0  | 0→0  | 0→0  | 0→0  |
| paper_006 | Multidisciplinary | Data inconsistency | 0→0  | 0→0  | 0→0  | 0→0  |
| paper_007 | Biology | Reagent identity | 0→0  | 0→0  | 0→0  | 0→0  |
| paper_008 | Medicine | Reagent identity | 0→0  | 0→0  | 0→0  | 0→0  |
| paper_009 | Environmental Scie | Equation / proof | 0→0  | 0→0  | 0→0  | 0→0  |
| paper_010 | Mathematics | Equation / proof | 0→0  | 0→0  | 0→0  | 0→0  |
| paper_013 | Computer Science | Equation / proof | 0→0  | 0→0  | 1→0 →miss | 0→0  |
| paper_016 | Physics | Equation / proof | 1→1  | 1→1  | 1→1  | 1→1  |
| paper_020 | Computer Science | Experiment setup | 0→0  | 0→0  | 0→0  | 1→0 →miss |

## Reading these results

**If anonymization itself is doing the work**, the post-fix
pass@1 on these 10 papers should rise toward the level seen
for the originally-anonymized 10. We saw `B1=40, B2=30, B3=30,
GD=50` on those 10 in the pre-fix snapshot.

**If the gap was paper-category mix or sampling noise**, the
post-fix pass@1 on these 10 will stay close to the pre-fix
rates: `B1=10, B2=10, B3=20, GD=20`.

Per-paper flips show *which specific papers* changed status.
If the same papers consistently flip across multiple conditions,
that's evidence anonymization affects model behavior on those
particular papers (e.g., by removing distracting bylines).

## Related: pre/post-cutoff null result

In the parallel retracted-paper benchmark, papers were stratified
by training-cutoff status (whether the retraction occurred before
or after the model's training-data cutoff). Detection rates on
post-cutoff retractions were comparable to pre-cutoff retractions,
supporting that memorization of retraction status is not the
primary driver of detection in those results.

Two confounds were therefore tested:
- **Memorization (pre/post training cutoff)**: null effect.
- **Anonymization (raw vs scrubbed text)**: see table above.

If anonymization shows a real signal here, prestige and
formatting cues may be a larger confound than memorization in
LLM-based scientific evaluation.