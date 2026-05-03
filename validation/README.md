# Validation Package — SPOT n=20 Multi-Model Evaluation Pilot

This directory is a self-contained verification package for a four-condition
multi-model evaluation pipeline tested on 20 papers from the
[SPOT scientific error detection benchmark](https://huggingface.co/datasets/amphora/SPOT-MetaData)
(Son et al., 2025). It includes all raw model outputs, ground truth, scoring
code, prompts, and configuration. **An evaluator who has never seen this
project before should be able to verify the reported results from this
directory alone.**

You are being asked to **be adversarial.** Your job is to find errors, not
to confirm results.

## What was tested

Four conditions on the same 20 SPOT papers:

| Condition | Description |
|---|---|
| **B1** | Single-model review (GPT-5.4), no severity rubric |
| **B2** | Single-model review (GPT-5.4) with a three-tier severity rubric |
| **B3** | Two provers (GPT-5.4 + DeepSeek V3.2) pooled to a Claude Opus 4.6 arbiter — **no steelman exchange** |
| **GD** | Same as B3, plus an adversarial **steelman exchange** between provers before the arbiter sees their reviews |

The exact prompts for each stage are in `prompts/`. Models, endpoints, and
parameters are in `config/models_used.json`.

## Reported aggregate results to verify

Strict pass@1 = "did the model identify the specific error annotated by the
SPOT team for that paper?" Lenient detection = "did the model classify the
paper as containing any retraction-worthy issue, regardless of whether it
matched the specific SPOT annotation?" (B1 has no severity classification,
so lenient is N/A.)

| Condition | N | Strict pass@1 | Recall (micro) | Precision (micro) | Lenient detection |
|---|---|---|---|---|---|
| B1 | 20 | 25.0% (5/20) | 23.81% | 0.87% | n/a |
| B2 | 20 | 20.0% (4/20) | 23.81% | 1.69% | 70.0% |
| B3 | 20 | 25.0% (5/20) | 23.81% | 1.97% | 70.0% |
| GD | 20 | 35.0% (7/20) | 33.33% | 2.52% | 75.0% |

For external context, SPOT (Son et al., 2025) reports o3 with vision access
attaining 18.4% pass@1 on the full 83-paper SPOT benchmark (precision 6.1%,
recall 21.1%). Our subset is the text-detectable papers only (categories:
equation/proof, statistical reporting, experiment setup, reagent identity,
text-text inconsistencies, and figure-text inconsistencies where the text
side may surface in prose).

## What you need to verify

1. **Every true positive is genuine.** For each paper × condition with TP_i ≥ 1,
   does the model finding actually describe the same scientific error as the
   SPOT annotation? Look at `raw_outputs/<paper_id>/<COND>.json` and
   `ground_truth/spot_ground_truth.csv`. Document any TPs you think are
   spurious.
2. **Every B3-vs-GD discordant pair is genuine.** Specifically: there are
   3 papers where GD detected and B3 did not (and 1 where the reverse).
   For each of the 3 GD-only detections, is the additional finding real?
3. **The scoring pipeline reproduces the reported aggregates.**
   `scoring/score_outputs.py` runs without API calls and replays the saved
   judge decisions in `scoring/judge_traces.jsonl`. It must produce
   `aggregate_results.csv` matching the table above.
4. **The four conditions are correctly differentiated by their prompts.** B1
   has no severity rubric, B2 has the rubric, B3 has no steelman material in
   the arbiter prompt, GD includes steelman exchange before the arbiter.
   Compare `prompts/B1_prompt.txt`, `B2_prompt.txt`, `B3_prompt.txt`,
   `GD_prompt.txt`. Flag any contamination between conditions.
5. **The ground truth mapping is correct.** Compare `ground_truth/spot_ground_truth.csv`
   to the canonical SPOT annotations at https://huggingface.co/datasets/amphora/SPOT-MetaData
   and confirm we did not alter or paraphrase the annotated errors.

## Known asymmetries to investigate

These are flagged for you because they may be confounds. **Investigate
whether they drive the results.**

### Anonymization status is split 10/10
Of the 20 papers, 10 were processed through a text-anonymizer that strips
author names, journal headers, dates, and affiliations before model review;
10 were not. See the `anonymized` column in `config/paper_metadata.csv`.
The auto-stratification in `scoring/score_outputs.py` reports:

```
B1  | anonymized=yes | n=10 | pass@1 = 40.00%
B1  | anonymized=no  | n=10 | pass@1 = 10.00%
B2  | anonymized=yes | n=10 | pass@1 = 30.00%
B2  | anonymized=no  | n=10 | pass@1 = 10.00%
B3  | anonymized=yes | n=10 | pass@1 = 30.00%
B3  | anonymized=no  | n=10 | pass@1 = 20.00%
GD  | anonymized=yes | n=10 | pass@1 = 50.00%
GD  | anonymized=no  | n=10 | pass@1 = 20.00%
```

**All four conditions perform substantially better on the anonymized subset.**
The anonymized subset and the un-anonymized subset were drawn with different
random seeds and may differ in paper-category composition. Investigate:
- Is the difference attributable to paper-category distribution? (compare
  `paper_category` distributions in the two subsets)
- Is anonymization itself making detection easier (e.g., by removing
  distractor text)?
- Or is it a sampling artifact?

Report your finding. If anonymization is doing real work here, the
aggregated numbers are confounded and need either (a) re-running all
20 on consistent input or (b) explicit acknowledgment with disaggregated
reporting.

### Sample size
n=20 is below the threshold where most paired comparisons reach
conventional significance. The B3-vs-GD McNemar's exact test gives
p = 0.625 at this n (3 of 4 discordant pairs favor GD). Aggregate
differences may not survive expansion to a larger sample.

### Single LLM-as-judge for matching
TP/FP/FN counts depend on a single GPT-5.4 LLM-as-judge run at
temperature=0 to decide whether each model finding semantically matches
each SPOT annotation. The prompt mirrors SPOT's published judge prompt.
The full judge transcript per paper × condition is in
`scoring/judge_traces.jsonl`. Spot-check whether the judge's match
decisions are reasonable.

## How to run the scoring

```bash
cd validation/scoring
pip install -r requirements.txt
python score_outputs.py
```

This reads `raw_outputs/`, `ground_truth/spot_ground_truth.csv`,
`config/paper_metadata.csv`, and `judge_traces.jsonl`, and writes
`per_paper_scores.csv` + `aggregate_results.csv` + a stratification
report. **It must reproduce the reported aggregates table above.**

To re-run the LLM judge from scratch (requires `OPENAI_API_KEY`, costs
~$0.50 in API calls):

```bash
export OPENAI_API_KEY=sk-...
python score_outputs.py --rerun-judge
```

The re-run mode writes a new `judge_traces_rerun.jsonl` and uses it for
scoring. Compare the matches it produces against the saved
`judge_traces.jsonl`.

## How to report findings

Create a Markdown file in `reports/` named `<your_name_or_handle>_report.md`
containing the sections below. Be specific — cite paper IDs, condition,
and quote the relevant passages from the model finding and the SPOT
annotation.

```markdown
# Validation report — <your_name_or_handle>

## 1. True positive audit
For each (paper_id, condition) with TP_i ≥ 1: is the match genuine?
List each TP. Mark each as GENUINE / SPURIOUS / AMBIGUOUS with reasoning.

## 2. Discordant pair audit (B3 vs GD)
For each paper where GD detected but B3 did not: is the GD detection real?
For the one paper where B3 detected but GD did not: anything notable?

## 3. Scoring reproduction
Did `python score_outputs.py` produce the reported aggregates? If you
ran `--rerun-judge`, did the new matches agree with the saved ones?

## 4. Prompt verification
Are the four conditions correctly differentiated? Any contamination?

## 5. Ground truth verification
Spot-check 5+ rows of `spot_ground_truth.csv` against the SPOT
HuggingFace dataset. Any altered/paraphrased annotations?

## 6. Anonymization confound
Examine the per-paper, per-condition results stratified by anonymization
status. Is the gap (anonymized > un-anonymized for all conditions)
driven by:
  - paper-category distribution differences between the two subsets?
  - anonymization itself simplifying the input?
  - sampling noise?
Provide your assessment.

## 7. Other flags
Anything else suspicious — inconsistent file structures, malformed JSON,
suspicious model outputs, prompts that contradict the README, etc.

## 8. Final verdict
One of:
  - CONFIRMED — results reproduce, no significant issues
  - ISSUES FOUND — results reproduce but with caveats (list)
  - CRITICAL PROBLEM — a result is wrong or a confound is decisive (explain)
```

## Directory map

```
validation/
├── README.md                    this file
├── VALIDATION.md                detailed step-by-step protocol
├── raw_outputs/                 80 JSON files: 20 papers × 4 conditions
│   └── paper_001/  ...  paper_020/
│       ├── B1.json
│       ├── B2.json
│       ├── B3.json
│       └── GD.json
├── ground_truth/
│   └── spot_ground_truth.csv    SPOT annotations for our 20 papers
├── scoring/
│   ├── score_outputs.py         standalone scorer (no API by default)
│   ├── requirements.txt         pandas (+ optional openai for --rerun-judge)
│   ├── judge_traces.jsonl       saved per-(paper, condition) judge decisions
│   ├── per_paper_scores.csv     replay output
│   └── aggregate_results.csv    replay output
├── prompts/
│   ├── B1_prompt.txt
│   ├── B2_prompt.txt
│   ├── B3_prompt.txt            includes BOTH the prover and arbiter prompts
│   └── GD_prompt.txt            includes prover, judge, steelman, arbiter
├── config/
│   ├── models_used.json         model IDs, providers, parameters, thresholds
│   ├── paper_metadata.csv       per paper: anonymized?, category, sizes
│   └── id_mapping.csv           paper_NNN ↔ original SPOT identifier
├── reports/                     drop your audit report here
└── evaluator_prompts/           ready-to-paste prompts for three tools
    ├── claude_chat.txt
    ├── claude_code.txt
    └── chatgpt.txt
```
