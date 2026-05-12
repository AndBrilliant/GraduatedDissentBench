# Out-of-family audit: comparison with in-family audit
Audit models:
- **In-family**: GPT-5.4, Claude Opus 4.6, DeepSeek V3.2
- **Out-of-family**: Gemini 2.5 Pro, xAI Grok 4 Fast Reasoning, Mistral Large 2

## Finding-level concordance
- Findings cross-compared: **1318**
- Both audits ⇒ match: 127 (9.6%)
- Both audits ⇒ no-match: 923 (70.0%)
- In-family yes, OOF no: 7
- OOF yes, in-family no: 261
- **Raw agreement: 79.7%**
- **Cohen's kappa (majority vs majority): 0.395**
- Cohen's kappa (in-family majority vs OOF unanimous): 0.587

## Paper-level audit-match aggregates (match-majority only)
Each cell: detection on retracted papers / false positives on probative controls.

| Condition | In-family det | In-family FP | OOF (2/3 maj) det | OOF (2/3 maj) FP | OOF (3/3 unan) det | OOF (3/3 unan) FP |
|---|---:|---:|---:|---:|---:|---:|
| B1 | 6/10 | 4/19 | 6/10 | 9/19 | 6/10 | 4/19 |
| B2 | 8/10 | 8/19 | 9/10 | 17/19 | 9/10 | 7/19 |
| B3 | 7/10 | 14/19 | 7/10 | 18/19 | 7/10 | 16/19 |
| GD | 7/10 | 13/19 | 10/10 | 17/19 | 10/10 | 15/19 |

## Paper-level RW-severity aggregates (severity-majority = RETRACTION-WORTHY)

In-family uses Opus + GPT-5.4 + DeepSeek (3-model). OOF-3m uses Gemini + Grok + Mistral (Gemini failed on ~55% of calls; this column reflects only the 768 findings where Gemini did complete). OOF-2m uses Grok + Mistral both-agree on the full 1318 findings.

| Condition | In-family det | In-family FP | OOF-3m det | OOF-3m FP | OOF-2m det | OOF-2m FP |
|---|---:|---:|---:|---:|---:|---:|
| B1 | 0/10 | 0/19 | 1/10 | 0/19 | 1/10 | 0/19 |
| B2 | 0/10 | 0/19 | 0/10 | 0/19 | 0/10 | 0/19 |
| B3 | 0/10 | 2/19 | 3/10 | 3/19 | 3/10 | 3/19 |
| GD | 0/10 | 0/19 | 1/10 | 2/19 | 1/10 | 2/19 |

## Headline question

> Does the OOF audit support the paper's specificity claim (GD has the fewest false-positive RW classifications)?

Read off the table above. If GD's OOF-FP column is ≤ B3's and ≤ B2's, the claim holds under the independent audit.
