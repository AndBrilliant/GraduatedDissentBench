# Graduated Dissent — Combined Paper Workspace

Working directory for the combined theory + empirical paper:

> **Decorrelated Multi-Model Evaluation for Error Detection in Scientific Manuscripts: Information-Theoretic Bounds and Empirical Validation**
> Andrew Michael Brilliant. 2026.

This repo consolidates three lines of work for resubmission to IJPRAI:

1. **Theory** — information-theoretic bounds on LLM self-correction (preprint DOI: 10.20944/preprints202601.0892.v3).
2. **Protocol** — Graduated Dissent multi-model architecture (preprint DOI: 10.20944/preprints202603.1830.v1).
3. **Benchmark** — paired-ablation evaluation on retracted scientific papers, plus a head-to-head comparison against the SPOT benchmark (Son et al., 2025).

## Layout

```
paper/                  Combined paper LaTeX, figures, tables, bibliography
data/
  retracted/            Retracted-paper benchmark (expanded from n=10 → target n=100)
  spot/                 SPOT integration: metadata, parsed papers, our outputs, scoring
  controls/             Control papers
harness/                Pipeline: graduated dissent + baselines + scoring
analysis/               Comparison tables, statistical tests, figure generation
github/                 Published benchmark repo (separate .git, gitignored here)
gui/                    Replication GUI server + accumulated runs
OLD/                    Earlier scripts, manuscripts, and curation logs
test_paper.tex          Standalone theory paper (rejected from IJPRAI; rewritten into paper/main.tex)
```

## Running the pipeline

API keys are auto-loaded from `~/.keys/{openai,deepseek,anthropic}` (see `gui/server.py`).

Models:

| Role | Model | API ID |
|------|-------|--------|
| Prover A, Baselines | GPT-5.4 | `gpt-5.4` |
| Prover B, Judge | DeepSeek V3.2 | `deepseek-chat` |
| Arbiter | Claude Opus 4.6 | `claude-opus-4-6` |

Conditions:

- **B1** — single model, no severity rubric (Liang 2024 baseline)
- **B2** — single model, severity rubric
- **B3** — multi-model ensemble pooled to arbiter, no steelman exchange
- **GD** — full graduated dissent with adversarial steelman exchange

## Status

Current results on the original n=10 retracted papers + 19 controls:

| Condition | Detection | False positives |
|-----------|-----------|-----------------|
| B1 | 3/10 (30%) | n/a |
| B2 | 4/10 (40%) | 3/19 (16%) |
| B3 | 3/10 (30%) | 1/19 (5%) |
| **GD** | **7/10 (70%)** | **0/19 (0%)** |

Paired ablation (B3 vs GD): 4/4 discordant pairs favor GD (McNemar exact p = 0.125 at n=10).
