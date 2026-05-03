# SPOT comparison

| condition           | label                                                        |   N | precision_micro   | recall_micro   | PPR   | pass_at_1   | detection_rate   | notes                                      |
|:--------------------|:-------------------------------------------------------------|----:|:------------------|:---------------|:------|:------------|:-----------------|:-------------------------------------------|
| B1                  | B1: Single GPT-5.4 (text-only) — apples-to-apples vs SPOT o3 |  50 | 0.0103            | 0.2364         | 0.0   | 0.24        | 0.24             |                                            |
| B2                  | B2: Single GPT-5.4 + severity rubric                         |  50 | 0.0241            | 0.2727         | 0.0   | 0.28        | 0.28             |                                            |
| B3                  | B3: Multi-model ensemble, no steelman                        |  50 | 0.0277            | 0.2909         | 0.0   | 0.3         | 0.3              |                                            |
| GD                  | Graduated dissent (this work)                                |  50 | 0.0291            | 0.3455         | 0.0   | 0.36        | 0.36             |                                            |
| SPOT_o3_pass1       | SPOT (Son et al.) — o3 single-model, vision, full benchmark  |  83 | 0.061             | 0.211          | —     | 0.184       | —                | Vision-capable; pass@4 = 37.8\%.           |
| SPOT_human_baseline | SPOT human-annotator agreement (reference)                   |  91 | —                 | —              | —     | —           | —                | Cross-validated by independent annotators. |
