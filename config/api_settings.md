# API Settings

All results collected April 4-6, 2026.

## Models

| Model | API ID | Provider | Endpoint |
|-------|--------|----------|----------|
| GPT-5.4 | `gpt-5.4` | OpenAI | `https://api.openai.com/v1/chat/completions` |
| DeepSeek V3.2 | `deepseek-chat` | DeepSeek | `https://api.deepseek.com/chat/completions` |
| Claude Opus 4.6 | `claude-opus-4-6` | Anthropic | `https://api.anthropic.com/v1/messages` |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | Anthropic | `https://api.anthropic.com/v1/messages` |

## Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Temperature | 1.0 (default) | Not explicitly set; all providers default to 1.0 |
| Max tokens | 4096 | GPT-5.4 uses `max_completion_tokens`; others use `max_tokens` |
| Top-p | Default | Not explicitly set |
| System prompt | None | All instructions in user message |

## Cost Estimates

| Condition | Papers | API calls/paper | Est. cost |
|-----------|--------|----------------|-----------|
| B1 (single, no rubric) | 34 | 1 (GPT-5.4) | ~$5 |
| B2 (single + rubric) | 34 | 1 (GPT-5.4) | ~$5 |
| B3 (multi, no steelman) | 34 | 3 (GPT-5.4 + DeepSeek + Opus) | ~$8 |
| Graduated Dissent | 34 | 5-6 (2 provers + judge + 2 steelman + arbiter) | ~$15 |
| Prompted retraction | 30 | 1 per model × 3 models | ~$8 |
| viXra GUT | 5 | 5-6 (same as GD) | ~$3 |
| **Total** | | | **~$44** |
