# SPOT comparison

| condition           | label                                                       |   N | precision_micro   | recall_micro   | PPR   | pass_at_1   | detection_rate   | notes                                      |
|:--------------------|:------------------------------------------------------------|----:|:------------------|:---------------|:------|:------------|:-----------------|:-------------------------------------------|
| GD                  | Graduated dissent (this work)                               |   3 | 0.0238            | 0.3333         | 0.0   | 0.3333      | 0.3333           |                                            |
| SPOT_o3_pass1       | SPOT (Son et al.) — o3 single-model, vision, full benchmark |  83 | 0.061             | 0.211          | —     | 0.184       | —                | Vision-capable; pass@4 = 37.8\%.           |
| SPOT_human_baseline | SPOT human-annotator agreement (reference)                  |  91 | —                 | —              | —     | —           | —                | Cross-validated by independent annotators. |
