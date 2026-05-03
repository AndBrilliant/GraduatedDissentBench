#!/usr/bin/env python3
"""
Score graduated-dissent / baseline outputs against SPOT ground truth.

Mirrors SPOT's evaluation approach (LLM-as-judge matching predictions to
annotations, then per-paper TP/FP/FN to compute precision/recall/PPR) so we
can publish numbers directly comparable to SPOT (Son et al., 2025).

Inputs:
  - data/spot/text_detectable/<safe_doi>/ground_truth.json   (annotations)
  - data/spot/outputs/<sweep>/<safe_doi>/<condition>.json    (predictions)

Outputs (per sweep):
  - data/spot/scoring/<sweep>/per_paper.csv     (one row per paper×condition)
  - data/spot/scoring/<sweep>/aggregates.csv    (precision/recall/PPR per condition)
  - data/spot/scoring/<sweep>/judge_traces.jsonl
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "harness"))

from api_client import call_model, configure_tracker, parse_json  # noqa: E402

JUDGE_MODEL = "gpt-5.4"  # SPOT used gpt-4.1; gpt-5.4 is our closest analogue

# SPOT's judge prompt verbatim — using their wording so our scoring is the
# same protocol as the published numbers we're comparing against.
SPOT_JUDGE_PROMPT = """You are an expert LLM-as-a-Judge. You will receive a JSON object with two arrays:

1. "annotations": the ground-truth errors (each has "location" and "description").
2. "predictions": the model's reported errors (same format).

**Task**
1. Compare each prediction against each annotation.
2. A match occurs **only** when both "location" and "description" are identical (semantically — slightly different wording is OK as long as the underlying error is the same).
3. Your output should be generated in the following format:

<analysis>
Analysis and comparison of each prediction and annotation.
</analysis>

<response>
{{
  "matches": [
    {{
      "annotation_index": <index into annotations array>,
      "prediction_index": <index into predictions array>,
      "explanation": "why this is a match"
    }}
  ]
}}
</response>

Be rigorous: location may be slightly differently named, but the description must overall describe the same scientific flaw. Do not record duplicates — each annotation should match at most ONE prediction (the best one).

INPUT:
{payload}
"""


def extract_predictions(condition_output: dict) -> list[dict[str, str]]:
    """Map our findings list to {location, description} dicts SPOT-style."""
    findings = condition_output.get("findings") or []
    out = []
    for f in findings:
        if not isinstance(f, dict):
            continue
        # Our schema: finding (text), justification (text), severity (label).
        # SPOT schema: location, description.
        out.append({
            "location": f.get("location") or "(not provided)",
            "description": f.get("finding", "") or f.get("description", ""),
        })
    return out


def extract_annotations(ground_truth: dict, *, only_text_detectable: bool = True) -> list[dict[str, str]]:
    """Pull annotations into SPOT scoring shape, optionally filtering by detectability."""
    out = []
    for e in ground_truth.get("errors", []):
        if only_text_detectable and e.get("detectability") == "figure":
            continue
        out.append({
            "location": e.get("location", ""),
            "description": e.get("description", ""),
            "category": e.get("category", ""),
            "severity": e.get("severity", ""),
            "detectability": e.get("detectability", ""),
        })
    return out


def parse_judge_response(raw: str) -> dict:
    """Pull the <response>{...}</response> block, falling back to raw JSON."""
    import re
    m = re.search(r"<response>\s*(\{.*?\})\s*</response>", raw, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass
    return parse_json(raw)


def judge_pair(annotations: list[dict], predictions: list[dict],
               *, paper_id: str, condition: str) -> dict:
    """Run the LLM judge and return {matches, raw_response, judge_dict}."""
    if not predictions:
        return {"matches": [], "judge_dict": {"matches": []}, "raw_response": ""}
    if not annotations:
        return {"matches": [], "judge_dict": {"matches": []}, "raw_response": ""}

    payload = json.dumps({
        "annotations": annotations,
        "predictions": predictions,
    }, ensure_ascii=False, indent=2)

    raw = call_model(JUDGE_MODEL, SPOT_JUDGE_PROMPT.format(payload=payload),
                     label=f"{paper_id}/{condition}/judge")
    judge_dict = parse_judge_response(raw)
    matches_raw = judge_dict.get("matches", []) if isinstance(judge_dict, dict) else []

    # Validate matches: each annotation_index/prediction_index must be in range,
    # and each annotation can be matched at most once (deduplicate).
    seen_anno: set[int] = set()
    matches: list[dict] = []
    for m in matches_raw:
        if not isinstance(m, dict):
            continue
        ai = m.get("annotation_index")
        pi = m.get("prediction_index")
        if not isinstance(ai, int) or not isinstance(pi, int):
            continue
        if ai < 0 or ai >= len(annotations) or pi < 0 or pi >= len(predictions):
            continue
        if ai in seen_anno:
            continue
        seen_anno.add(ai)
        matches.append({
            "annotation_index": ai,
            "prediction_index": pi,
            "annotation": annotations[ai],
            "prediction": predictions[pi],
            "explanation": m.get("explanation", ""),
        })
    return {"matches": matches, "judge_dict": judge_dict, "raw_response": raw}


def per_paper_metrics(annotations: list[dict], predictions: list[dict],
                      matches: list[dict]) -> dict:
    k_i = len(annotations)
    TP_i = len(matches)
    FP_i = max(0, len(predictions) - TP_i)
    FN_i = k_i - TP_i
    precision = TP_i / (TP_i + FP_i) if (TP_i + FP_i) else 0.0
    recall = TP_i / k_i if k_i else 0.0
    perfect = (TP_i == k_i) and (FP_i == 0)
    return {
        "k_i": k_i, "TP_i": TP_i, "FP_i": FP_i, "FN_i": FN_i,
        "precision_i": precision, "recall_i": recall, "perfect_i": int(perfect),
        "n_predictions": len(predictions),
    }


def score_sweep(sweep_dir: Path, gt_dir: Path, scoring_dir: Path,
                conditions: list[str], cap_usd: float) -> None:
    sweep_name = sweep_dir.name
    out_dir = scoring_dir / sweep_name
    out_dir.mkdir(parents=True, exist_ok=True)

    configure_tracker(cap_usd)

    rows = []
    judge_log_path = out_dir / "judge_traces.jsonl"
    judge_log = judge_log_path.open("w", encoding="utf-8")

    paper_ids = sorted([p.name for p in sweep_dir.iterdir() if p.is_dir()])
    for paper_id in paper_ids:
        gt_path = gt_dir / paper_id / "ground_truth.json"
        if not gt_path.exists():
            print(f"  skip {paper_id}: no ground truth")
            continue
        ground_truth = json.loads(gt_path.read_text(encoding="utf-8"))
        annotations = extract_annotations(ground_truth, only_text_detectable=True)

        for condition in conditions:
            cond_path = sweep_dir / paper_id / f"{condition.lower()}.json"
            if not cond_path.exists():
                continue
            cond_output = json.loads(cond_path.read_text(encoding="utf-8"))
            predictions = extract_predictions(cond_output)

            judge = judge_pair(annotations, predictions,
                               paper_id=paper_id, condition=condition.upper())
            metrics = per_paper_metrics(annotations, predictions, judge["matches"])
            metrics.update({
                "paper_id": paper_id,
                "condition": condition.upper(),
                "title": ground_truth.get("title", ""),
                "paper_category": ground_truth.get("paper_category", ""),
                "verdict": cond_output.get("verdict", "unknown"),
                "n_annotations_text": len(annotations),
                "n_annotations_total": len(ground_truth.get("errors", [])),
                "rw_count": (cond_output.get("severity_counts") or {}).get("RETRACTION-WORTHY", 0)
                             if cond_output.get("severity_counts") else None,
            })
            rows.append(metrics)

            judge_log.write(json.dumps({
                "paper_id": paper_id, "condition": condition.upper(),
                "annotations": annotations, "predictions": predictions,
                "matches": judge["matches"],
                "raw_judge_response": judge["raw_response"],
            }, ensure_ascii=False) + "\n")

    judge_log.close()

    if not rows:
        print("No outputs scored.")
        return

    per_paper = pd.DataFrame(rows)
    per_paper.to_csv(out_dir / "per_paper.csv", index=False)

    # Aggregates per condition
    agg_rows = []
    for cond, grp in per_paper.groupby("condition"):
        TP = grp["TP_i"].sum()
        FP = grp["FP_i"].sum()
        FN = grp["FN_i"].sum()
        N = len(grp)
        precision_micro = TP / (TP + FP) if (TP + FP) else 0.0
        recall_micro = TP / (TP + FN) if (TP + FN) else 0.0
        precision_macro = grp["precision_i"].mean()
        recall_macro = grp["recall_i"].mean()
        ppr = grp["perfect_i"].mean()  # perfect-paper rate
        # SPOT's pass@1: papers where the model identified at least one true error
        # (recall_i > 0). We report it for compatibility.
        pass_at_1 = (grp["TP_i"] > 0).mean()
        # Detection rate (our binary metric): paper has any TP at all.
        detection_rate = (grp["TP_i"] > 0).mean()

        agg_rows.append({
            "condition": cond,
            "N": N,
            "TP_total": int(TP), "FP_total": int(FP), "FN_total": int(FN),
            "precision_micro": round(precision_micro, 4),
            "recall_micro": round(recall_micro, 4),
            "precision_macro": round(precision_macro, 4),
            "recall_macro": round(recall_macro, 4),
            "PPR": round(ppr, 4),
            "pass_at_1": round(pass_at_1, 4),
            "detection_rate": round(detection_rate, 4),
        })

    agg = pd.DataFrame(agg_rows).sort_values("condition")
    agg.to_csv(out_dir / "aggregates.csv", index=False)

    def rel(p: Path) -> str:
        try:
            return str(p.resolve().relative_to(REPO))
        except ValueError:
            return str(p)
    print(f"\nWrote {rel(out_dir / 'per_paper.csv')}")
    print(f"Wrote {rel(out_dir / 'aggregates.csv')}")
    print(f"Wrote {rel(judge_log_path)}")
    print()
    print("Aggregates:")
    print(agg.to_string(index=False))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sweep-dir", required=True,
                   help="data/spot/outputs/<sweep>/")
    p.add_argument("--gt-dir", default="data/spot/text_detectable",
                   help="Directory with ground_truth.json per paper")
    p.add_argument("--scoring-dir", default="data/spot/scoring")
    p.add_argument("--conditions", default="b1,b2,b3,gd")
    p.add_argument("--cap", type=float, default=5.0,
                   help="Cost cap for the judge runs")
    args = p.parse_args()
    score_sweep(
        Path(args.sweep_dir), Path(args.gt_dir), Path(args.scoring_dir),
        [c.strip() for c in args.conditions.split(",")],
        args.cap,
    )


if __name__ == "__main__":
    main()
