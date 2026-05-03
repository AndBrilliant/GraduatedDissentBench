# SPOT comparison

| condition           | label                                                        |   N | precision_micro   | recall_micro   | PPR   | pass_at_1   | detection_rate   | notes                                      |
|:--------------------|:-------------------------------------------------------------|----:|:------------------|:---------------|:------|:------------|:-----------------|:-------------------------------------------|
| B1                  | B1: Single GPT-5.4 (text-only) — apples-to-apples vs SPOT o3 |  20 | 0.0087            | 0.2381         | 0.0   | 0.25        | 0.25             |                                            |
| B2                  | B2: Single GPT-5.4 + severity rubric                         |  20 | 0.0169            | 0.2381         | 0.0   | 0.2         | 0.2              |                                            |
| B3                  | B3: Multi-model ensemble, no steelman                        |  20 | 0.0197            | 0.2381         | 0.0   | 0.25        | 0.25             |                                            |
| GD                  | Graduated dissent (this work)                                |  20 | 0.0252            | 0.3333         | 0.0   | 0.35        | 0.35             |                                            |
| SPOT_o3_pass1       | SPOT (Son et al.) — o3 single-model, vision, full benchmark  |  83 | 0.061             | 0.211          | —     | 0.184       | —                | Vision-capable; pass@4 = 37.8\%.           |
| SPOT_human_baseline | SPOT human-annotator agreement (reference)                   |  91 | —                 | —              | —     | —           | —                | Cross-validated by independent annotators. |
