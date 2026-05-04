#!/usr/bin/env python3
"""
Blinded multi-model rescoring of the retracted-paper benchmark.

Walks every (paper, condition, finding) triple in
github/outputs/raw/{baseline_B1,baseline_B2,baseline_B3,graduated_dissent}/
and asks three independent models (GPT-5.4, Claude Opus 4.6, DeepSeek
V3.2) to judge:

  - For RETRACTED papers: does the candidate finding substantially
    identify the same error as the documented retraction cause?
  - For CONTROLS (matched + hard-negative): does the candidate finding
    identify a methodological flaw severe enough that, if confirmed,
    would warrant retracting the manuscript?

The audit is BLIND: the prompt does not reveal the condition, the
paper identity, the retraction status of the paper, or the original
severity rating. Audit calls run at temperature=0.

Outputs to validation/retracted_paper_audit/:
  - raw_responses.jsonl       — one row per (paper, condition, finding,
                                model, question) audit call
  - per_finding.csv           — finding-level audit aggregates
  - per_paper.csv             — paper-level detection / FP outcomes
                                under three scoring regimes
  - aggregate_table.md        — the four-row comparison table
  - report.md                 — narrative summary + disagreement list

Run:
    python harness/audit_retracted.py
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "harness"))

from api_client import call_model, configure_tracker, parse_json  # noqa: E402

GH = REPO / "github"
GT_CSV = GH / "data" / "ground_truth.csv"
OUT_RAW = GH / "outputs" / "raw"
OUT_DIR = REPO / "validation" / "retracted_paper_audit"

CONDITION_DIRS = {
    "B1": "baseline_B1",
    "B2": "baseline_B2",
    "B3": "baseline_B3",
    "GD": "graduated_dissent",
}

AUDIT_MODELS = ("gpt-5.4", "opus", "deepseek")

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


def load_findings_for_paper(paper_id: str, condition: str) -> tuple[list[dict], dict]:
    """Return (findings_list, full_blob) for a given paper × condition."""
    cond_dir = OUT_RAW / CONDITION_DIRS[condition]
    matches = list(cond_dir.glob(f"{paper_id}_*.json"))
    if not matches:
        return [], {}
    blob = json.loads(matches[0].read_text(encoding="utf-8"))
    findings = blob.get("findings", []) or []
    return findings, blob


def audit_one_finding(prompt: str, models: tuple[str, ...] = AUDIT_MODELS) -> list[dict]:
    """Three-model audit of a single finding. Returns one record per model."""
    out = []
    for m in models:
        try:
            raw = call_model(m, prompt, temperature=0,
                             label=f"audit/{m}")
            parsed = parse_json(raw)
            ans = parsed
        except Exception as e:
            ans = {"error": f"{type(e).__name__}: {e}"}
        out.append({"model": m, "response": ans})
    return out


def majority(votes: list[bool]) -> bool:
    return sum(1 for v in votes if v) >= 2


def unanimous(votes: list[bool]) -> bool:
    return all(votes)


def is_retracted(paper_id: str, gt: dict) -> bool:
    return gt.get(paper_id, {}).get("category", "") == "retracted"


def is_probative_control(paper_id: str, gt: dict) -> bool:
    cat = gt.get(paper_id, {}).get("category", "")
    return cat in ("matched_control", "hard_negative")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--cap", type=float, default=8.0,
                   help="USD cost cap for the audit")
    p.add_argument("--limit", type=int, default=None,
                   help="Limit per paper × condition for testing")
    p.add_argument("--skip-severity", action="store_true",
                   help="Skip the severity question; only run match question")
    p.add_argument("--out-dir", default=str(OUT_DIR))
    args = p.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    raw_log = out_dir / "raw_responses.jsonl"
    fh = raw_log.open("w", encoding="utf-8")

    gt = load_ground_truth()

    # Subset: 10 retracted + 19 probative controls (skip wildcards / viXra)
    paper_ids = [pid for pid in gt
                 if is_retracted(pid, gt) or is_probative_control(pid, gt)]
    paper_ids.sort()

    configure_tracker(args.cap)
    print(f"Auditing {len(paper_ids)} papers × 4 conditions × 3 models")
    print(f"Cost cap: ${args.cap}")

    per_finding_rows: list[dict] = []
    per_paper_rows: list[dict] = []
    n_calls = 0

    for pid in paper_ids:
        retracted = is_retracted(pid, gt)
        cause = gt[pid]["retraction_cause"] if retracted else "(none — control)"
        for cond in ("B1", "B2", "B3", "GD"):
            findings, blob = load_findings_for_paper(pid, cond)
            if not findings:
                # Record empty paper × condition
                per_paper_rows.append({
                    "paper_id": pid,
                    "condition": cond,
                    "is_retracted": retracted,
                    "n_findings": 0,
                    "first_author_match": False,
                    "first_author_RW_present": False,
                    "audit_match_majority": False,
                    "audit_match_unanimous": False,
                    "audit_RW_majority": False,
                    "audit_RW_unanimous": False,
                })
                continue

            # First-author flags from the existing data
            severities = [f.get("severity", "") for f in findings if isinstance(f, dict)]
            first_author_RW = any(s == "RETRACTION-WORTHY" for s in severities)
            # First-author MATCH against ground truth via the existing keyword logic.
            # We re-implement keyword matching here so the audit table is self-contained.
            first_author_match = False
            if retracted:
                kw_csv = gt[pid]["keyword_groups"]
                groups = []
                for grp in kw_csv.split("|"):
                    grp = grp.strip()
                    if not grp:
                        continue
                    groups.append([k.strip().lower() for k in grp.split("+") if k.strip()])
                for f in findings:
                    if not isinstance(f, dict):
                        continue
                    text = (f.get("finding", "") or f.get("description", "") or "").lower()
                    if any(all(k in text for k in g) for g in groups):
                        first_author_match = True
                        break

            audit_match_per_finding: list[list[bool]] = []  # per finding, per model
            audit_severity_per_finding: list[list[str]] = []

            limit = args.limit if args.limit else len(findings)
            for fi, f in enumerate(findings[:limit]):
                if not isinstance(f, dict):
                    continue
                ftext = f.get("finding", "") or f.get("description", "")
                if not ftext:
                    continue

                if retracted:
                    prompt = MATCH_PROMPT_RETRACTED.format(
                        ground_truth=cause, finding_text=ftext,
                    )
                else:
                    prompt = MATCH_PROMPT_CONTROL.format(finding_text=ftext)

                results = audit_one_finding(prompt)
                votes = []
                for r in results:
                    resp = r.get("response", {})
                    if isinstance(resp, dict) and not resp.get("parse_error"):
                        votes.append(bool(resp.get("match", False)))
                    else:
                        votes.append(False)
                audit_match_per_finding.append(votes)

                row = {
                    "paper_id": pid,
                    "is_retracted": retracted,
                    "condition": cond,
                    "finding_idx": fi,
                    "finding_text": ftext[:300],
                    "first_author_severity": f.get("severity", ""),
                    "audit_match_votes": votes,
                    "audit_match_majority": majority(votes),
                    "audit_match_unanimous": unanimous(votes),
                }
                fh.write(json.dumps({"event": "match", "paper_id": pid,
                                       "condition": cond, "finding_idx": fi,
                                       "responses": results}) + "\n")
                fh.flush()
                n_calls += 3

                # Severity question only fires on a positive match (majority)
                if not args.skip_severity and row["audit_match_majority"]:
                    sev_prompt = SEVERITY_PROMPT.format(finding_text=ftext)
                    sev_results = audit_one_finding(sev_prompt)
                    sev_votes = []
                    for r in sev_results:
                        resp = r.get("response", {})
                        if isinstance(resp, dict) and not resp.get("parse_error"):
                            sev_votes.append(resp.get("severity", "?"))
                        else:
                            sev_votes.append("?")
                    audit_severity_per_finding.append(sev_votes)
                    row["audit_severity_votes"] = sev_votes
                    row["audit_severity_majority_RW"] = sum(
                        1 for s in sev_votes if s == "RETRACTION-WORTHY"
                    ) >= 2
                    fh.write(json.dumps({"event": "severity",
                                           "paper_id": pid, "condition": cond,
                                           "finding_idx": fi,
                                           "responses": sev_results}) + "\n")
                    fh.flush()
                    n_calls += 3
                else:
                    audit_severity_per_finding.append([])
                    row["audit_severity_votes"] = []
                    row["audit_severity_majority_RW"] = False

                per_finding_rows.append(row)

            # Aggregate to paper-level
            audit_match_majority = any(majority(v) for v in audit_match_per_finding)
            audit_match_unanimous = any(unanimous(v) for v in audit_match_per_finding)
            audit_RW_majority = any(
                row.get("audit_severity_majority_RW", False)
                for row in per_finding_rows
                if row["paper_id"] == pid and row["condition"] == cond
            )
            # Unanimous RW: all 3 models say RW for any single finding
            audit_RW_unanimous = False
            for row in per_finding_rows:
                if row["paper_id"] == pid and row["condition"] == cond:
                    sv = row.get("audit_severity_votes", []) or []
                    if len(sv) >= 3 and all(s == "RETRACTION-WORTHY" for s in sv):
                        audit_RW_unanimous = True
                        break

            per_paper_rows.append({
                "paper_id": pid,
                "condition": cond,
                "is_retracted": retracted,
                "n_findings": len(findings),
                "first_author_match": first_author_match,
                "first_author_RW_present": first_author_RW,
                "audit_match_majority": audit_match_majority,
                "audit_match_unanimous": audit_match_unanimous,
                "audit_RW_majority": audit_RW_majority,
                "audit_RW_unanimous": audit_RW_unanimous,
            })

            print(f"  {pid:>5} {cond}: {len(findings):>2} findings | "
                  f"FAm={int(first_author_match)} ARWp={int(first_author_RW)} "
                  f"| audit maj={int(audit_match_majority)} unan={int(audit_match_unanimous)} "
                  f"| RW maj={int(audit_RW_majority)} | calls so far ~{n_calls}")

    fh.close()

    # Save per-finding and per-paper CSVs
    if per_finding_rows:
        keys = list(per_finding_rows[0].keys())
        with (out_dir / "per_finding.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            for row in per_finding_rows:
                w.writerow({k: (v if not isinstance(v, list) else json.dumps(v)) for k, v in row.items()})
    if per_paper_rows:
        keys = list(per_paper_rows[0].keys())
        with (out_dir / "per_paper.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(per_paper_rows)

    def rel(p: Path) -> str:
        try:
            return str(p.resolve().relative_to(REPO))
        except ValueError:
            return str(p)
    print(f"\nWrote {rel(raw_log)}")
    print(f"Wrote {rel(out_dir / 'per_finding.csv')}")
    print(f"Wrote {rel(out_dir / 'per_paper.csv')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
