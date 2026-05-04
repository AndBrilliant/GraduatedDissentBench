#!/usr/bin/env python3
"""
Fill in Opus votes for audit batches where Opus was BudgetExceeded.

Re-uses the same prompts as audit_retracted.py but only calls Opus, and
only on the (paper, condition, finding) batches where Opus's stored
response carries 'BudgetExceeded'. The result is appended to the
existing raw_responses.jsonl with a marker.

After this script, run audit_aggregate.py — but it needs to be told
to use the fill-in Opus votes. Simpler: rebuild per_paper.csv from
scratch by combining the original GPT-5.4/DeepSeek votes with the
filled-in Opus votes.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "harness"))

from api_client import call_model, configure_tracker, parse_json  # noqa: E402

GH = REPO / "github"
GT_CSV = GH / "data" / "ground_truth.csv"
OUT_RAW = GH / "outputs" / "raw"
AUDIT = REPO / "validation" / "retracted_paper_audit"

CONDITION_DIRS = {
    "B1": "baseline_B1",
    "B2": "baseline_B2",
    "B3": "baseline_B3",
    "GD": "graduated_dissent",
}

MATCH_PROMPT_RETRACTED = """You are auditing a single candidate finding from a manuscript review against a documented ground-truth flaw. The audit is blinded: you do not know which review system produced the finding or which paper it concerns.

DOCUMENTED RETRACTION CAUSE (ground truth):
{ground_truth}

CANDIDATE FINDING:
{finding_text}

QUESTION: Does the candidate finding substantially identify the same methodological error as the documented retraction cause? Allow for paraphrase or different framing of the same underlying problem; reject matches that are merely topically adjacent or describe a different flaw.

Respond with JSON only:
{{"match": true|false, "reasoning": "one sentence"}}
"""

MATCH_PROMPT_CONTROL = """You are auditing a single candidate finding from a manuscript review. The audit is blinded: you do not know which review system produced the finding or which paper it concerns.

CANDIDATE FINDING:
{finding_text}

QUESTION: Based solely on the evidence in this finding (treat the finding's claims as if they were established), does it describe a methodological flaw severe enough that, if confirmed, would warrant retracting the manuscript? Be strict: most papers have routine limitations; the threshold is "fundamentally broken in a way that invalidates central conclusions," not "could be improved."

Respond with JSON only:
{{"match": true|false, "reasoning": "one sentence"}}
"""

SEVERITY_PROMPT = """You are auditing the severity of a single candidate finding from a manuscript review.

CANDIDATE FINDING:
{finding_text}

QUESTION: Based solely on the evidence in the finding, what severity tier is justified?
- RETRACTION-WORTHY: central conclusions cannot be supported as presented; fundamentally broken
- MAJOR-REVISION: real concern that could change conclusions if addressed differently, but does not definitively invalidate
- MINOR: valid criticism applicable to most papers; would not change conclusions

Respond with JSON only:
{{"severity": "RETRACTION-WORTHY|MAJOR-REVISION|MINOR", "reasoning": "one sentence"}}
"""


def load_ground_truth() -> dict[str, dict]:
    gt = {}
    with GT_CSV.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            gt[row["paper_id"]] = row
    return gt


def load_findings(paper_id: str, condition: str) -> list[dict]:
    cond_dir = OUT_RAW / CONDITION_DIRS[condition]
    matches = list(cond_dir.glob(f"{paper_id}_*.json"))
    if not matches:
        return []
    blob = json.loads(matches[0].read_text(encoding="utf-8"))
    return blob.get("findings", []) or []


def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--cap", type=float, default=20.0,
                   help="USD cost cap for Opus fill-in")
    args = p.parse_args()

    raw_log = AUDIT / "raw_responses.jsonl"
    out_log = AUDIT / "raw_responses_opus_fillin.jsonl"
    fh_out = out_log.open("w", encoding="utf-8")

    gt = load_ground_truth()
    configure_tracker(args.cap)

    n_done = 0
    n_skipped = 0
    with raw_log.open(encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            event = rec.get("event")
            if event not in ("match", "severity"):
                continue
            # Find Opus response in this batch
            opus_resp = None
            for resp in rec.get("responses", []):
                if resp.get("model") == "opus":
                    opus_resp = resp
                    break
            if opus_resp is None:
                continue
            ans = opus_resp.get("response", {})
            if isinstance(ans, dict) and "error" in ans and "BudgetExceeded" in ans.get("error", ""):
                # Need to refire Opus
                pid = rec["paper_id"]
                cond = rec["condition"]
                fi = rec["finding_idx"]
                findings = load_findings(pid, cond)
                if fi >= len(findings):
                    n_skipped += 1
                    continue
                f_obj = findings[fi]
                if not isinstance(f_obj, dict):
                    n_skipped += 1
                    continue
                ftext = f_obj.get("finding", "") or f_obj.get("description", "")
                if not ftext:
                    n_skipped += 1
                    continue

                if event == "match":
                    is_retracted = gt.get(pid, {}).get("category") == "retracted"
                    if is_retracted:
                        cause = gt[pid]["retraction_cause"]
                        prompt = MATCH_PROMPT_RETRACTED.format(ground_truth=cause, finding_text=ftext)
                    else:
                        prompt = MATCH_PROMPT_CONTROL.format(finding_text=ftext)
                else:  # severity
                    prompt = SEVERITY_PROMPT.format(finding_text=ftext)

                try:
                    raw = call_model("opus", prompt, temperature=0,
                                     label=f"opus_fillin/{pid}/{cond}/{fi}/{event}")
                    parsed = parse_json(raw)
                    new_resp = {"model": "opus", "response": parsed}
                except Exception as e:
                    new_resp = {"model": "opus", "response": {"error": f"{type(e).__name__}: {e}"}}

                fh_out.write(json.dumps({
                    "event": event,
                    "paper_id": pid,
                    "condition": cond,
                    "finding_idx": fi,
                    "responses": [new_resp],
                }) + "\n")
                fh_out.flush()
                n_done += 1
                if n_done % 25 == 0:
                    print(f"  filled in {n_done} Opus calls (skipped {n_skipped})")

    fh_out.close()
    print(f"\nFilled in Opus on {n_done} batches; skipped {n_skipped}.")
    print(f"Wrote {out_log}")


if __name__ == "__main__":
    raise SystemExit(main() or 0)
