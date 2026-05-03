# Paper Curation Guide
## For human review of benchmark candidates

Each paper below needs a human check. Mark your decision in the Status column.

### How to review:
1. Open the retraction notice link
2. Confirm the error is **methodology, not misconduct**
3. Confirm full text is accessible
4. Check: could a reviewer spot this error from the manuscript alone?
5. Mark: INCLUDE / EXCLUDE / UNSURE

### Quick reference:
- **INCLUDE if:** Statistical error, coding error, design flaw, conceptual error, reproducibility failure
- **EXCLUDE if:** Plagiarism, fabrication, image manipulation, "data integrity concerns" without specifics
- **UNSURE if:** Borderline — flag for discussion

---

## Retracted Papers

| ID | Field | Error Summary | RW Link | Status | Notes |
|----|-------|--------------|---------|--------|-------|
| R01 | Pediatrics | Coding errors, incidence underestimated 3x | [RW](https://retractionwatch.com/2024/08/20/coding-errors-prompt-retraction-of-paper-on-long-covid-in-kids/) | INCLUDE | Confirmed, PMC available |
| R02 | Economics | Flawed GDP data, results insignificant when corrected | [RW](https://retractionwatch.com/2025/12/03/authors-retract-nature-paper-projecting-high-costs-of-climate-change/) | INCLUDE | Authors self-retracted |
| R03 | Psychology | Post-hoc presented as preregistered | [Nature](https://www.nature.com/articles/s41562-024-01997-3) | INCLUDE | PMC available |
| R04 | Nutrition | Unreplicable analyses, implausible values | [RW](https://retractionwatch.com/2025/09/23/apple-cider-vinegar-weight-loss-study-retracted-bmj/) | INCLUDE | "Honest mistakes" acknowledged |
| R05 | Emergency Med | Randomization discrepancies | [RW](https://retractionwatch.com/2025/12/29/bmj-retraction-clinical-trial-discrepancies-randomization/) | INCLUDE | "Unintentional procedural errors" |
| R07 | Clin Epi | Misunderstood "treatment effect" | NEEDS LINK | _____ | Need to identify specific paper |
| R10 | Medicine | Vitamin D/COVID selection bias | [RW](https://retractionwatch.com/2025/09/25/authors-defend-retracted-paper-on-vitamin-d-and-covid-19-critic-called-deeply-bizarre/) | INCLUDE | "No obvious signs of fakery" |
| R11 | Psychology | Mediation between related constructs | [RW](https://retractionwatch.com/2025/07/11/retraction-for-unsound-analysis-was-disproportionate-and-discouraging-author-says/) | INCLUDE | Author disputes proportionality |
| R19 | Obesity | GLP-1 combo, results not reproducible | [RW](https://retractionwatch.com/2026/02/23/glp-1-study-retracted-ozempic-saxenda-contrave-statistics/) | INCLUDE | Reanalysis found "not substantiated" |
| R24 | Medicine | Metformin/COVID outcome errors | [RW](https://retractionwatch.com/2025/11/20/lancet-journal-retracts-covid-19-metformin-paper-nearly-2-years-after-authors-request-correction/) | INCLUDE | Authors self-reported errors |
| R25 | Neurology | ICD code logic error (OR vs AND) | [JAMA](https://jamanetwork.com/journals/jamaneurology/fullarticle/2835757) | INCLUDE | Classic coding error, quantified |

### Papers needing more candidates (gap to 25):
We have 11 confirmed. Need ~14 more. See `retracted_candidates.md` for moderate candidates needing verification.

---

## How to add a new paper:

1. Find it on Retraction Watch
2. Fill in the row above
3. Download the full text to `dataset/retracted/`
4. Write ground truth in `ground_truth/` (see template below)

### Ground truth template:
```
Paper: R[XX]
Title: [paper title]
Retraction cause: [1-2 sentences]
Specific errors (for scoring):
- [Error 1: specific, scorable description]
- [Error 2: if multiple]
Text-detectable signals:
- [What should a reviewer notice in the manuscript?]
```
