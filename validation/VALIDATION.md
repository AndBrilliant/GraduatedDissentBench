# VALIDATION PROTOCOL — Step by step

This is the operational protocol. Follow it in order. **Be adversarial:
your job is to find errors, not to confirm the reported results.**

## Step 0 — Set up

```bash
cd validation/scoring
pip install -r requirements.txt
```

If you also want to re-run the LLM judge:
```bash
export OPENAI_API_KEY=sk-...
```

## Step 1 — Reproduce the aggregate scoring

```bash
python score_outputs.py
```

Compare the printed `aggregate_results.csv` table against the README's
"Reported aggregate results" table. **They must match exactly.** If not,
flag it — that means either the scoring code, the judge transcript, or
the ground truth has drifted from what was reported.

Also note the printed anonymization stratification.

Optional integrity check:
```bash
python score_outputs.py --rerun-judge
```
This costs ~$0.50 and writes `judge_traces_rerun.jsonl`. Compare its
match counts against the saved `judge_traces.jsonl` row by row.

## Step 2 — True positive audit

For each `(paper_id, condition)` row in `per_paper_scores.csv` where
`TP_i ≥ 1`, do the following:

1. Open `raw_outputs/<paper_id>/<COND>.json` — find the matched
   prediction in the `findings` list.
2. Open `ground_truth/spot_ground_truth.csv` — find the matched
   annotation row by `paper_id`.
3. Open `scoring/judge_traces.jsonl` — find the entry for this
   `(paper_id, COND)` and look at the matched `(annotation_index,
   prediction_index, explanation)`.
4. Decide: does the model finding actually describe the same scientific
   error as the SPOT annotation?

Categorize each as:
- **GENUINE** — clear semantic match
- **SPURIOUS** — the judge accepted a match that does not describe the
  same error
- **AMBIGUOUS** — partial overlap; reasonable people could disagree

Total TPs across the four conditions: 5 + 4 + 5 + 7 = 21 to audit.
If any are spurious, recompute the affected aggregate.

## Step 3 — Discordant pair audit (B3 vs GD)

```bash
python -c "
import pandas as pd
df = pd.read_csv('per_paper_scores.csv')
b3 = df[df['condition']=='B3'].set_index('paper_id')['TP_i']
gd = df[df['condition']=='GD'].set_index('paper_id')['TP_i']
both = pd.DataFrame({'b3': b3, 'gd': gd})
print('GD-only:', list(both[(both['b3']==0)&(both['gd']>0)].index))
print('B3-only:', list(both[(both['b3']>0)&(both['gd']==0)].index))
"
```

For each GD-only paper: open `raw_outputs/<paper_id>/B3.json` and
`raw_outputs/<paper_id>/GD.json` side by side. Confirm the GD findings
include a clear hit on the SPOT annotation that is absent from B3's
findings. Document.

## Step 4 — Prompt verification

Diff the four prompt files. Confirm:

- `B1_prompt.txt` does **not** contain "RETRACTION-WORTHY" or any severity
  vocabulary.
- `B2_prompt.txt` does contain the severity rubric.
- `B3_prompt.txt` includes the prover prompt AND a separate arbiter
  prompt. The arbiter prompt does **not** mention "steelman" or any
  steelman exchange material.
- `GD_prompt.txt` includes prover, judge, steelman, and arbiter prompts.
  The arbiter prompt **does** include the steelman material as input.

Also spot-check a `raw_outputs/<paper_id>/<COND>.json` to confirm the
stored prover/arbiter outputs are consistent with the prompt that should
have produced them (e.g., GD outputs should reference the steelman
exchange in their `arbiter_raw.reasoning` field).

## Step 5 — Ground truth verification

Pick at least 5 random rows from `ground_truth/spot_ground_truth.csv`.
For each, look up the corresponding paper in
`config/id_mapping.csv` to find the original SPOT identifier
(`doi/arxiv_id`), then verify against
https://huggingface.co/datasets/amphora/SPOT-MetaData that the
`error_category`, `error_location`, and `error_annotation` columns are
unaltered.

## Step 6 — Anonymization confound investigation

The README documents that all four conditions perform substantially
better on the 10 anonymized papers than the 10 un-anonymized. This is a
real risk to the reported results. Your task here:

```bash
python -c "
import pandas as pd
meta = pd.read_csv('../config/paper_metadata.csv')
print(meta.groupby('anonymized')['paper_category'].value_counts().unstack(fill_value=0))
"
```

Then make an assessment:
1. Is the paper-category distribution different between the two subsets?
2. If yes, could that drive the detection-rate gap (e.g., math/CS
   papers are easier text-only than biology/chemistry)?
3. If no, is the anonymizer itself making detection easier (e.g., by
   removing distractor text near the abstract)?
4. Could it be sampling noise at n=10 per arm?

Report your conclusion. This is the most important methodological
question to settle before any larger run is launched.

## Step 7 — Anything else suspicious

Look for:
- Malformed JSON
- Findings that are nearly identical across conditions for the same
  paper (suggests prompt contamination or shared context)
- Judge match `explanation` fields that don't actually justify the match
- A `paper_id` with substantially different findings between the
  un-anonymized batch and what we'd expect

## Step 8 — Write the report

Save as `reports/<your_name_or_handle>_report.md` using the template in
the README. End with a single-line verdict: CONFIRMED / ISSUES FOUND /
CRITICAL PROBLEM.

## Out of scope

- You do **not** need to evaluate whether the underlying protocol or its
  theoretical motivation is sound. You are verifying that the reported
  numbers were generated honestly from the stored data.
- You do **not** need to evaluate whether SPOT itself is a good
  benchmark; treat its annotations as ground truth for this exercise.
