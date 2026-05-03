# SPOT comparison

| condition           | label                                                        |   N | precision_micro   | recall_micro   | PPR   | pass_at_1   | detection_rate   | notes                                      |
|:--------------------|:-------------------------------------------------------------|----:|:------------------|:---------------|:------|:------------|:-----------------|:-------------------------------------------|
| B1                  | B1: Single GPT-5.4 (text-only) — apples-to-apples vs SPOT o3 |   5 | 0.0061            | 0.2            | 0.0   | 0.2         | 0.2              |                                            |
| B2                  | B2: Single GPT-5.4 + severity rubric                         |   5 | 0.0               | 0.0            | 0.0   | 0.0         | 0.0              |                                            |
| B3                  | B3: Multi-model ensemble, no steelman                        |   4 | 0.0               | 0.0            | 0.0   | 0.0         | 0.0              |                                            |
| GD                  | Graduated dissent (this work)                                |   4 | 0.0169            | 0.25           | 0.0   | 0.25        | 0.25             |                                            |
| SPOT_o3_pass1       | SPOT (Son et al.) — o3 single-model, vision, full benchmark  |  83 | 0.061             | 0.211          | —     | 0.184       | —                | Vision-capable; pass@4 = 37.8\%.           |
| SPOT_human_baseline | SPOT human-annotator agreement (reference)                   |  91 | —                 | —              | —     | —           | —                | Cross-validated by independent annotators. |
