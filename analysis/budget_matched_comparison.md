# Budget-matched comparison: B3 / B3+ / B3++ / GD on n=49 SPOT

Paper excluded from comparison: `10.1038_s41598-025-91235-1` — OpenAI's safety filter (biology restriction) blocks GPT-5.4 from accepting the prover prompt for B3+/B3++ runs, even though the same prompt succeeded for the original B1/B2/B3/GD sweep. The n=49 intersection is the apples-to-apples comparison set.

## Pipeline shapes

| Condition | Calls/paper | Reflection prompt |
|---|---:|---|
| B3 | 3 | (none — pool both reviews directly) |
| B3+ | 5 | Neutral: 'Re-examine your findings, reconsider whether severity is right.' |
| B3++ | 5 | Anti-steelman: 'Build the strongest case FOR your severity ratings.' |
| GD | 5-6 | Steelman: 'Build the strongest case for the OTHER reviewer's position.' |

## Headline numbers (n=49)

| Condition | pass@1 | pass@1 95% Wilson CI | RW per paper | RW-precision | RW-yield |
|---|---:|---|---:|---:|---:|
| B3 | 14/49 = 28.6% | [17.8%, 42.4%] | 1.96 | 5/96 = 5.2% | 5/29 = 17.2% |
| B3+ | 11/49 = 22.4% | [13.0%, 35.9%] | 1.69 | 6/83 = 7.2% | 6/31 = 19.4% |
| B3++ | 18/49 = 36.7% | [24.7%, 50.7%] | 2.29 | 7/112 = 6.2% | 7/36 = 19.4% |
| GD | 17/49 = 34.7% | [22.9%, 48.7%] | 1.55 | 8/76 = 10.5% | 8/27 = 29.6% |

## What the table shows

**Same-compute, different reflection prompt — pass@1:**

- B3 (no reflection, 3 calls): 14/49 = 28.6%
- B3+ (neutral reflection, 5 calls): 11/49 = 22.4%
- B3++ (anti-steelman, 5 calls): 18/49 = 36.7%
- GD (steelman, 5-6 calls): 17/49 = 34.7%

**Same-compute, different reflection prompt — RW-precision:**

- B3: 5/96 = 5.2%
- B3+: 6/83 = 7.2%
- B3++: 7/112 = 6.2%
- GD: 8/76 = 10.5%

## Interpretation hooks

- B3+ tests whether *any* re-engagement helps. If B3+ ≈ B3, the second pass alone doesn't carry signal.
- B3++ tests whether *adversarial* framing is necessary. If B3++ ≈ B3, only adversarial works. If B3++ ≈ GD, the second pass itself matters but not its direction.
- GD vs B3++ separates 'self-defense' from 'steelman the other side'.
