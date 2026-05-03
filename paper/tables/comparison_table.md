# Comparison with recent algorithms

## Our conditions

| Approach | Method | Ground truth | Detection | False positive / precision |
|---|---|---|---|---|
| B1: Single model, no rubric (Liang 2024 baseline) | Single GPT-5.4 | 10 retracted papers | 3/10 (30%) | — |
| B2: Single model + severity rubric | Single GPT-5.4 + severity rubric | 10 retracted, 19 controls | 4/10 (40%) | 3/19 (16%) |
| B3: Multi-model ensemble, no steelman (Wang 2023 / Du 2024 family) | GPT-5.4 + DeepSeek pooled to Opus arbiter | 10 retracted, 19 controls | 3/10 (30%) | 1/19 (5%) |
| Graduated dissent (this work) | GPT-5.4 + DeepSeek + steelman + Opus arbiter | 10 retracted, 19 controls | 7/10 (70%) | 0/19 (0%) |

## Published comparators

| Approach | Method | Ground truth | Detection | False positive / precision |
|---|---|---|---|---|
| SPOT 2025 (Son et al.) | Single-model LLM review (vision) | 83 papers, 91 human-annotated errors | o3 18.4% pass@1; 37.8% pass@4 | Precision 6.1%, recall 21.1% |
| FLAWS 2025 (Xi et al.) | Single-model error localization | 713 papers with LLM-inserted errors | GPT-5: 39.1% identification at k=10 | Holistic review weaker than targeted |
| Pub-Guard-LLM 2025 (Chen et al.) | Fine-tuned LLM + RAG + debate | 11K PubMed articles (retraction status) | ~91% retraction classification | — |
| "To Err Is Human" 2025 | GPT-5-based correctness checker | 316 expert-validated mistakes (ML) | — | Precision 83.2% (human-validated) |
| Liang 2024 (NEJM AI) | Single GPT-4 review | Human reviewer comments (not GT) | 30.85% (Nature) / 39.23% (ICLR) overlap | Positivity bias noted |
| MARG 2024 (Darcy et al.) | Multi-agent review generation | User-rated comments | 3.7 good comments/paper | Generic-comment rate 60%→29% |