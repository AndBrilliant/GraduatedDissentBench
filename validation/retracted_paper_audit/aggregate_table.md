# Retracted-paper benchmark — multi-model rescoring

## Comparison table (B3 vs GD)

| Scoring regime | B3 det. | GD det. | B3 FP | GD FP |
|---|---:|---:|---:|---:|
| First-author scoring | 30% (3/10) | 70% (7/10) | 5% (1/19) | 0% (0/19) |
| Majority audit (2/3) | 70% (7/10) | 70% (7/10) | 11% (2/19) | 0% (0/19) |
| Unanimous strict (3/3) | 0% (0/10) | 0% (0/10) | 5% (1/19) | 0% (0/19) |

## All conditions

| Condition | First-author det. | Majority det. | Unanimous det. | First-author FP | Majority FP | Unanimous FP |
|---|---:|---:|---:|---:|---:|---:|
| B1 | 30% | 60% | 10% | 5% | 0% | 0% |
| B2 | 40% | 80% | 10% | 16% | 0% | 0% |
| B3 | 30% | 70% | 0% | 5% | 11% | 5% |
| GD | 70% | 70% | 0% | 0% | 0% | 0% |


## Disagreements (first-author vs majority audit)

| Paper | Category | Cond | Metric | First-author | Majority audit |
|---|---|---|---|---|---|
| C04 | control | B1 | false_positive | True | False |
| R04 | retracted | B1 | detection | False | True |
| R10 | retracted | B1 | detection | False | True |
| R19 | retracted | B1 | detection | False | True |
| C04 | control | B2 | false_positive | True | False |
| C10 | control | B2 | false_positive | True | False |
| HN10 | control | B2 | false_positive | True | False |
| R04 | retracted | B2 | detection | False | True |
| R05 | retracted | B2 | detection | False | True |
| R10 | retracted | B2 | detection | False | True |
| R19 | retracted | B2 | detection | False | True |
| HN03 | control | B3 | false_positive | False | True |
| R04 | retracted | B3 | detection | False | True |
| R05 | retracted | B3 | detection | False | True |
| R10 | retracted | B3 | detection | False | True |
| R24 | retracted | B3 | detection | False | True |
| R01 | retracted | GD | detection | True | False |
| R02 | retracted | GD | detection | True | False |
| R04 | retracted | GD | detection | False | True |
| R10 | retracted | GD | detection | False | True |
