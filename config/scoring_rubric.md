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

## Limitations

- Keyword matching is approximate; some true matches may be missed
- Scorer override rates were not systematically recorded
- Inter-rater reliability has not been formally measured
- The first author verified all matches and non-matches against retraction notices
