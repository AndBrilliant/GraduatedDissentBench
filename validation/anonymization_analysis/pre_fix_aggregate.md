# Pre-fix aggregate (mixed anonymization)

| Condition | Anonymized | n | TPs | pass@1 |
|---|---|---:|---:|---:|
| B1 | yes | 10 | 4 | 40.00% |
| B1 | no | 10 | 1 | 10.00% |
| B2 | yes | 10 | 3 | 30.00% |
| B2 | no | 10 | 1 | 10.00% |
| B3 | yes | 10 | 3 | 30.00% |
| B3 | no | 10 | 2 | 20.00% |
| GD | yes | 10 | 5 | 50.00% |
| GD | no | 10 | 2 | 20.00% |

**Per-condition deltas (anonymized − un-anonymized):**

| Condition | pass@1 (anon) | pass@1 (un-anon) | Δ (pp) |
|---|---:|---:|---:|
| B1 | 40.00% | 10.00% | +30.0 |
| B2 | 30.00% | 10.00% | +20.0 |
| B3 | 30.00% | 20.00% | +10.0 |
| GD | 50.00% | 20.00% | +30.0 |

## Context

This snapshot was taken with 10 papers anonymized via the same text-anonymization pipeline used for an earlier retracted-paper benchmark, and 10 papers run on the original parsed text from the public SPOT release. The anonymization status was a function of two batches drawn with different random seeds, not an intentional control. The deltas above motivated re-anonymizing the second batch and re-running it for consistency. The post-fix comparison is in `anonymization_effect.md`.
