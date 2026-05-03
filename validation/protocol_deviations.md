# Protocol deviations and clarifications

This document records the actual protocol behavior on the n=20 pilot,
focusing on points the evaluator audit flagged for review.

## Escalation gate behavior

The graduated-dissent protocol has three levels:
- **L0**: agreement ≥ θ_accept (0.90) → accept without steelman
- **L1**: SNR < 1.0 (where SNR = (1 − agreement) / θ_noise, θ_noise = 0.15) → accept; disagreement is below noise floor
- **L2**: SNR ≥ 1.0 → run steelman exchange before arbitration

### Observed behavior on n=20

All 20 papers' GD outputs include a `protocol` block recording the
agreement score and the level the gate selected. Inspection of those
blocks gives:

| Paper | Agreement | Level | Steelman ran? |
|---|---:|---|---|
| paper_001 | 0.82 | L2 | yes |
| paper_002 | 0.75 | L2 | yes |
| paper_003 | 0.75 | L2 | yes |
| paper_004 | 0.75 | L2 | yes |
| paper_005 | 0.92 | **L0** | **no** |
| paper_006 | 0.84 | L2 | yes |
| paper_007 | 0.85 | L2 | yes |
| paper_008 | 0.15 | L2 | yes |
| paper_009 | 0.92 | **L0** | **no** |
| paper_010 | 0.72 | L2 | yes |
| paper_011 | 0.85 | L2 | yes |
| paper_012 | 0.75 | L2 | yes |
| paper_013 | 0.75 | L2 | yes |
| paper_014 | 0.62 | L2 | yes |
| paper_015 | 0.72 | L2 | yes |
| paper_016 | 0.85 | L2 | yes |
| paper_017 | 0.85 | L2 | yes |
| paper_018 | 0.95 | **L0** | **no** |
| paper_019 | 0.40 | L2 | yes |
| paper_020 | 0.85 | L2 | yes |

Three papers (005, 009, 018) hit L0 and skipped the steelman exchange.
Seventeen papers escalated to L2 and ran the full exchange. **No paper
hit L1**, because the bandgap between θ_accept = 0.90 and the noise
floor at SNR = 1 (agreement = 0.85) leaves L1 only triggered when
agreement is in (0.85, 0.90), which did not happen on any paper.

The L0-skipped papers are visible in the saved JSON: their
`steelman_a.steelman_for_other` and `steelman_b.steelman_for_other`
fields contain the literal placeholder string `"N/A — escalation level
L0"` (vs. real steelman content for L2 papers), and the arbiter's
final reasoning does not reference any steelman material.

### Why an evaluator might report "the gate was non-functional"

The `ARBITER_PROMPT` template that the protocol uses at the L2 →
arbitration step is the same template used at L0; the template includes
placeholder positions for the steelman exchange. At L0, those positions
are filled with the `"N/A — escalation level L0"` markers above rather
than skipped from the prompt entirely. A reader scanning only the
arbiter prompt without inspecting the contents could see "the prompt
mentions steelman" and conclude the gate was bypassed, even though
operationally no steelman API calls were made and the arbiter saw
explicit "N/A" markers.

### Effect on the B3-vs-GD comparison

None of the three L0 papers (005, 009, 018) appear in the B3-vs-GD
discordant pair set. Specifically:
- paper_005, 009, 018: B3 and GD give the same TP outcome.

So even if one were to attribute the GD detection on these papers to
the L0 path (which is structurally identical to B3 — both papers see
two prover reviews and an arbiter), the B3-vs-GD comparison is
unaffected.

## Always-steelman vs. graduated framing

The protocol can be described two ways depending on what the reader
needs:

- **"Graduated dissent with conditional escalation"**: accurate for the
  protocol *as designed* (and as it ran here at the gate level).
- **"Multi-model with steelman exchange"**: accurate for the *17 of 20*
  papers that hit L2. For those papers, what discriminates GD from B3
  is the steelman exchange.

The manuscript should describe the protocol as graduated with
conditional escalation, but report empirical numbers with explicit
disclosure that 3/20 papers in this pilot hit L0.

## Disputed TPs flagged in audit

The independent evaluator audit flagged paper_014 GD as a borderline
match (`scoring/per_paper_scores.csv` `disputed = yes`). The aggregate
`scoring/aggregate_results.csv` reports two GD rows:
- `GD_strict` excludes the disputed TP (pass@1 = 25%).
- `GD_standard` honors the judge's decision (pass@1 = 30%).
