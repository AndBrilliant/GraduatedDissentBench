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

## Validation Experiments (May 2026)

Two follow-up experiments addressing reviewer concerns. Total cost ~$44 of
API spend; commit `0c30822`.

### Out-of-family audit

All 1,318 retracted-paper findings rescored by models disjoint from the
GPT-5.4 / Opus / DeepSeek evaluation pipeline: **Grok 4 Fast Reasoning** and
**Mistral Large 2** (Gemini 2.5 Pro attempted but hit daily quota partway
through; 768/1706 calls completed, used as a 3-model cross-check on that
subset). Final aggregation uses Grok + Mistral both-agree on the full 1318
findings.

Match-majority detection on 10 retracted papers rises under OOF:
GD 10/10 (in-fam 7/10), B3 7/10 (unchanged). RW-severity-majority FP on
19 probative controls: GD 2/19 (in-fam 0/19), B3 3/19 (in-fam 2/19). The
GD > B3 specificity direction holds; the absolute "0/19 false positives"
claim does not survive independent audit. Cohen κ in-fam vs OOF: 0.40.

Raw data and per-finding tables in `validation/retracted_paper_audit_oof/`.
Aggregator: `harness/aggregate_oof_audit.py`.

### Budget-matched ablation

Three 5-call conditions matched to GD's compute, run on n=49 SPOT papers:

- **B3+** — neutral reflection ("re-examine your severity ratings")
- **B3++** — anti-steelman ("defend your severity ratings")
- **GD** — steelman (existing — argue against own ratings)

Pass@1: B3 28.6% · B3+ 22.4% · B3++ 36.7% · GD 34.7%.
RW-precision: B3 5.2% · B3+ 7.2% · B3++ 6.2% · **GD 10.5%**.

Detection (pass@1) reproduces with any 5-call re-engagement (B3++ matches
or exceeds GD). Severity calibration (RW-precision, RW-yield) is uniquely
produced by adversarial self-challenge — neither B3+ nor B3++ approaches
GD's 10.5% RW-precision.

Pipeline: `harness/run_b3plus.py`, `harness/sweep_b3plus.py`.
Outputs: `data/spot/outputs/budget_matched/`.
Comparison: `analysis/budget_matched_comparison.md`.

One SPOT paper (`10.1038_s41598-025-91235-1`) excluded — OpenAI's newly
tightened biology safety filter blocks GPT-5.4 from accepting the prover
prompt for B3+/B3++ runs, even though the same prompt succeeded in the
original B1/B2/B3/GD sweep.
