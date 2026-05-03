# Replication Guide

## Requirements

- Python 3.9+
- API keys for: OpenAI, DeepSeek, Anthropic
- Estimated cost: ~$50 for full replication

## Environment Setup

```bash
pip install openai anthropic
export OPENAI_API_KEY=<your key>
export ANTHROPIC_API_KEY=<your key>
export DEEPSEEK_API_KEY=<your key>
```

## Running the Benchmark

### 1. Graduated Dissent (Primary)

For each paper in `data/papers/`:
1. Run Prover A (GPT-5.4) with `prompts/prover_prompt.txt`
2. Run Prover B (DeepSeek) with `prompts/prover_prompt.txt`
3. Run Judge (DeepSeek) with `prompts/judge_prompt.txt`
4. If SNR ≥ 1.0: Run steelman exchange with `prompts/steelman_prompt.txt`
5. Run Arbiter (Opus) with `prompts/arbiter_prompt.txt`

See `config/thresholds.md` for escalation logic.

### 2. Baselines

- **B1**: Run GPT-5.4 with `prompts/baseline_b1_prompt.txt` (no severity rubric)
- **B2**: Run GPT-5.4 with `prompts/baseline_b2_prompt.txt` (severity rubric, single model; note: slightly different framing from prover prompt)
- **B3**: Run Prover A + Prover B, pool findings, send to Arbiter (no steelman). See `prompts/baseline_b3_prompt.txt`

### 3. Prompted Retraction

Run each of 3 models (GPT-5.4, DeepSeek, Opus) on retracted papers only, with `prompts/prompted_retraction.txt`.

## Scoring

Compare findings against `data/ground_truth.csv` using keyword matching. A finding matches if it contains ALL keywords in ANY keyword group for that paper.

## Expected Results

Your results should be approximately consistent with ours, though exact numbers will vary due to temperature=1.0 (non-deterministic outputs). The key patterns should hold:
- GD detection rate substantially higher than baselines
- GD false positive rate at or near zero
- B3 false positive rate higher than GD (steelman exchange is the active ingredient)

## Notes

- All API calls used default parameters (temperature=1.0)
- GPT-5.4 requires `max_completion_tokens` not `max_tokens`
- Results may vary between runs; see variance analysis in the paper
