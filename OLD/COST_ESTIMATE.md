# v6 Benchmark — Cost Estimate
## Three models, three families, three roles

---

## Models

| Role | Model | API ID | Input $/M | Output $/M |
|------|-------|--------|----------|-----------|
| **Prover A** | GPT-5.4 | gpt-5.4 | $2.50 | $15.00 |
| **Prover B** | DeepSeek V3.2 | deepseek-chat | $0.14 | $0.28 |
| **Arbiter** | Opus 4.6 | claude-opus-4-6 | $5.00 | $25.00 |

**Baseline** (cheap iteration): DeepSeek V3.2 in all roles.

---

## Per-Paper Cost: Primary Configuration

| Call | Model | Cost |
|------|-------|------|
| Prover A | GPT-5.4 | $0.050 |
| Prover B | DeepSeek | $0.002 |
| Judge | DeepSeek | $0.003 |
| Steelman A | GPT-5.4 | $0.070 |
| Steelman B | DeepSeek | $0.003 |
| Arbiter | Opus 4.6 | $0.210 |
| **Per paper** | | **$0.34** |

Opus arbiter = 62% of cost. The arbiter IS the product.

## Per-Paper Cost: DeepSeek Baseline

All 6 calls DeepSeek: **$0.02 per paper**

---

## Run Plan & Costs

| Phase | What | Papers | Cost |
|-------|------|--------|------|
| 1 | DeepSeek baseline | 60 | **$1** |
| 2 | Primary (GPT-5.4 + DS + Opus arb) | 60 | **$20** |
| 3 | Arbiter comparison (4 arbiters) | 10 | **$6** |
| 4 | Scoring (Opus) | ~600 findings | **$21** |
| 5 | Buffer | — | **$10** |
| **Total** | | | **~$58** |

### By provider:
- Anthropic (Opus): ~$35
- OpenAI (GPT-5.4): ~$15
- DeepSeek: ~$3

### With batch API (50% off): ~$30

---

## Decision: Scorer model

Opus as scorer = $21. DeepSeek as scorer = $3.
Pilot showed scorer quality matters. **Recommend Opus.**
Total with DeepSeek scorer: ~$40.
