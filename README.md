# Graduated Dissent Benchmark

Benchmark and supplementary materials for:

> **Detecting Retraction-Worthy Errors with Graduated Dissent**  
> Andrew M. Brilliant, Joe Reid  
> April 2026

## Overview

This repository contains the complete dataset, prompts, raw model outputs, and scoring materials for the graduated dissent benchmark. The benchmark evaluates whether multi-model adversarial architectures can identify documented methodological errors in retracted scientific papers while avoiding false positives on non-retracted controls.

### Key Results

| Condition | GT Detection | FP Rate (n=24) |
|-----------|-------------|-----------------|
| B1: Single model, no rubric | 3/10 (30%) | N/A |
| B2: Single model + rubric | 4/10 (40%) | 3/24 (12%) |
| B3: Multi-model, no steelman | 3/10 (30%) | 1/24 (4%) |
| Prompted (told retracted) | 7/30 (23%) | N/A |
| **Graduated Dissent** | **7/10 (70%)** | **0/24 (0%)** |

## Repository Structure

```
data/papers/          Anonymized manuscripts (txt)
prompts/              Exact prompts used for all conditions
config/               API settings, thresholds, scoring rubric
outputs/raw/          Raw JSON model outputs per paper per condition
outputs/scored/       Scoring audit table
analysis/             Results analysis scripts
replication/          Replication instructions
```

## Dataset

- **10 retracted papers** (R01-R25): Peer-reviewed papers retracted for documented methodological errors
- **10 matched controls** (C01-C25): Non-retracted papers from same journals/fields
- **9 hard-negative controls** (HN02-HN10): Controversial but non-retracted papers
- **5 wildcard controls** (W01-W05): Papers from unrelated fields
- **5 viXra papers** (V01-V05): Unrestricted preprint server submissions (informal validation)

All papers are anonymized: author names, journal names, dates, affiliations, references, and publisher templates removed.

## Replication

See [replication/REPLICATION.md](replication/REPLICATION.md) for full instructions.

**Requirements:**
- API access: OpenAI (GPT-5.4), DeepSeek (V3.2), Anthropic (Opus 4.6)
- Python 3.9+
- Estimated cost: ~$50 for full replication of all conditions

## Models

| Model | API ID | Role |
|-------|--------|------|
| GPT-5.4 | `gpt-5.4` | Prover A, Baselines |
| DeepSeek V3.2 | `deepseek-chat` | Prover B, Judge |
| Claude Opus 4.6 | `claude-opus-4-6` | Arbiter |

All results collected April 2026. Default temperature (1.0) for all providers.

## License

MIT License. See [LICENSE](LICENSE).

## Citation

```bibtex
@article{brilliant2026graduated_bench,
  title={Detecting Retraction-Worthy Errors with Graduated Dissent},
  author={Brilliant, Andrew M. and Reid, Joe},
  year={2026},
  note={Preprint}
}
```
