# Scoring Rubric

## Ground Truth Matching

Each retracted paper has a documented retraction cause decomposed into keyword groups. A finding is scored as matching ground truth if it contains ALL keywords in ANY keyword group for that paper.

### Example: Paper R01

Keyword groups:
- ["HR", "0.00", "hazard"] — impossible hazard ratios
- ["missing data", "asymptomatic"] — coding error
- ["age", "range", "8", "13"] — age range violation
- ["denominator", "271", "0.4"] — incorrect incidence

A finding matching any one of these groups counts as detecting the retraction cause.

### Scoring Categories

| Category | Definition |
|----------|-----------|
| True positive | Finding matches documented retraction cause |
| Severity-correct TP | TP rated RETRACTION-WORTHY or MAJOR-REVISION |
| False positive (RW on control) | RETRACTION-WORTHY finding on a non-retracted paper |
| Noise | Generic, unfounded, or hallucinated findings |

## Severity Classification

Severity is assigned by the arbiter during protocol execution and is NOT modified during scoring. The three levels:

- **RETRACTION-WORTHY**: Central conclusions cannot be supported
- **MAJOR-REVISION**: Could change conclusions if addressed differently
- **MINOR**: Valid criticism, would not change conclusions

## Two-Stage Scoring Process

1. **Automated keyword matching** (described above): Identifies findings containing documented retraction-cause keywords. This is the primary, reproducible scoring mechanism.

2. **Manual review**: The first author reviewed all keyword matches and non-matches against the original retraction notices. A finding could also be scored as a true positive if it identified "a substantively related problem that would independently undermine the paper's conclusions" even without exact keyword matches. In practice, all true positives in the reported results were identified by keyword matching; no additional matches were added during manual review.

No separate LLM scorer was used for ground-truth matching. The manuscript's reference to an "external scorer" describes the keyword-matching script, not a Sonnet-based scoring pass.

## Limitations

- Keyword matching is approximate; some true matches may be missed by keywords
- Scorer override rates were not systematically recorded
- Inter-rater reliability has not been formally measured
- The first author verified all matches and non-matches against retraction notices
