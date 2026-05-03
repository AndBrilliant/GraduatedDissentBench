#!/usr/bin/env python3
"""
Standalone scoring script for the SPOT n=20 validation package.

Two modes:

  default — recompute aggregate metrics from the saved LLM-as-judge
            decisions in judge_traces.jsonl (no API calls; deterministic).
            This is the path independent evaluators should use first.

  --rerun-judge — call the LLM judge from scratch using your own
            OPENAI_API_KEY. Verifies the saved judge decisions are
            reproducible. Costs ~$0.50.

Outputs:
  per_paper_scores.csv     one row per (paper_id, condition) with TP/FP/FN
  aggregate_results.csv    one row per condition with pass@1, recall,
                           precision (micro and macro), PPR, lenient

Usage:
  pip install -r requirements.txt
  python score_outputs.py --outputs ../raw_outputs \
                          --ground-truth ../ground_truth/spot_ground_truth.csv \
                          --metadata ../config/paper_metadata.csv

The default mode does NOT make API calls. It reproduces the reported
aggregates exactly from the stored judge_traces.jsonl. To audit the
underlying judge decisions yourself, inspect judge_traces.jsonl directly.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent

# ── ID mapping (built once from id_mapping.csv) ───────────────────────

def load_id_map(metadata_csv: Path) -> dict[str, str]:
    """Load the safe_doi -> paper_NNN mapping from validation/config/id_mapping.csv."""
    config_dir = metadata_csv.parent
    id_csv = config_dir / "id_mapping.csv"
    if not id_csv.exists():
        return {}
    df = pd.read_csv(id_csv)
    return dict(zip(df["original_safe_doi"], df["paper_id"]))


# ── Default mode: replay saved judge decisions ────────────────────────

def replay_judge_traces(
    traces_path: Path,
    ground_truth: pd.DataFrame,
    id_map: dict[str, str],
    raw_outputs_dir: Path,
) -> pd.DataFrame:
    """Walk judge_traces.jsonl and assemble per-paper TP/FP/FN per condition."""
    rows = []
    with traces_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            old_id = rec.get("paper_id", "")
            paper_id = id_map.get(old_id, old_id)
            cond = rec.get("condition", "").upper()
            annotations = rec.get("annotations", []) or []
            predictions = rec.get("predictions", []) or []
            matches = rec.get("matches", []) or []

            # Sanity: the judge already validated each match's annotation_index
            # is in range. We still defensively dedupe by annotation index.
            seen = set()
            tp = 0
            for m in matches:
                ai = m.get("annotation_index")
                if isinstance(ai, int) and 0 <= ai < len(annotations) and ai not in seen:
                    seen.add(ai)
                    tp += 1
            k_i = len(annotations)
            fp_i = max(0, len(predictions) - tp)
            fn_i = k_i - tp

            # Pull severity counts from the per-paper output JSON (under raw_outputs)
            cond_lower = cond.lower()
            output_path = raw_outputs_dir / paper_id / f"{cond}.json"
            rw_count = None
            verdict = None
            if output_path.exists():
                try:
                    blob = json.loads(output_path.read_text(encoding="utf-8"))
                    sev = blob.get("severity_counts") or {}
                    rw_count = sev.get("RETRACTION-WORTHY") if sev else None
                    verdict = blob.get("verdict")
                except Exception:
                    pass

            rows.append({
                "paper_id": paper_id,
                "condition": cond,
                "n_annotations": k_i,
                "n_predictions": len(predictions),
                "TP_i": tp,
                "FP_i": fp_i,
                "FN_i": fn_i,
                "precision_i": tp / (tp + fp_i) if (tp + fp_i) else 0.0,
                "recall_i": tp / k_i if k_i else 0.0,
                "perfect_i": int(tp == k_i and fp_i == 0),
                "verdict": verdict,
                "rw_count": rw_count,
            })

    df = pd.DataFrame(rows)
    return df


# ── Disputed-TP list (editorial — set by evaluator audit, not the judge) ──

# Each entry is (paper_id, condition) for a TP that an external audit
# flagged as borderline. The aggregate emits both GD_strict (excludes
# disputed) and GD_standard (includes) when GD has any disputed TP.
DISPUTED_TPS: set[tuple[str, str]] = {
    ("paper_014", "GD"),  # ChatGPT/Claude evaluators split on this match
}


# ── Aggregate metrics ─────────────────────────────────────────────────

def _condition_metrics(grp: pd.DataFrame, label: str) -> dict:
    N = len(grp)
    TP = int(grp["TP_i"].sum())
    FP = int(grp["FP_i"].sum())
    FN = int(grp["FN_i"].sum())
    precision_micro = TP / (TP + FP) if (TP + FP) else 0.0
    recall_micro = TP / (TP + FN) if (TP + FN) else 0.0
    precision_macro = grp["precision_i"].mean()
    recall_macro = grp["recall_i"].mean()
    pass_at_1 = (grp["TP_i"] > 0).mean()
    ppr = grp["perfect_i"].mean()
    if "rw_count" in grp.columns and grp["rw_count"].notna().any():
        lenient = (grp["rw_count"].fillna(0).astype(int) > 0).mean()
    else:
        lenient = float("nan")
    return {
        "condition": label,
        "N": N,
        "TP_total": TP,
        "FP_total": FP,
        "FN_total": FN,
        "precision_micro": round(precision_micro, 4),
        "recall_micro": round(recall_micro, 4),
        "precision_macro": round(precision_macro, 4),
        "recall_macro": round(recall_macro, 4),
        "PPR": round(ppr, 4),
        "pass_at_1": round(pass_at_1, 4),
        "lenient_RW_detection": round(lenient, 4) if lenient == lenient else None,
    }


def aggregate(per_paper: pd.DataFrame) -> pd.DataFrame:
    """Per-condition pass@1, precision, recall, PPR, lenient detection.

    For any condition that has a disputed TP, emit BOTH a `<COND>_strict`
    row (disputed TPs reclassified as misses) and a `<COND>_standard` row
    (judge decision honored). Conditions with zero disputed TPs emit a
    single row.
    """
    pp = per_paper.copy()
    # Strict view: any (paper_id, condition) in DISPUTED_TPS has TP -> 0.
    pp["disputed"] = pp.apply(
        lambda r: "yes" if (r["paper_id"], r["condition"]) in DISPUTED_TPS else "no",
        axis=1,
    )

    rows = []
    for cond, grp in pp.groupby("condition"):
        any_disputed = (grp["disputed"] == "yes").any()
        if not any_disputed:
            rows.append(_condition_metrics(grp, cond))
            continue
        # Standard
        rows.append(_condition_metrics(grp, f"{cond}_standard"))
        # Strict: zero out the disputed rows' TPs and increment FN
        strict = grp.copy()
        mask = strict["disputed"] == "yes"
        strict.loc[mask, "TP_i"] = 0
        strict.loc[mask, "FN_i"] = strict.loc[mask, "FN_i"] + (grp.loc[mask, "TP_i"].values)
        strict["precision_i"] = strict.apply(
            lambda r: (r["TP_i"] / (r["TP_i"] + r["FP_i"])) if (r["TP_i"] + r["FP_i"]) else 0.0,
            axis=1,
        )
        strict["recall_i"] = strict.apply(
            lambda r: (r["TP_i"] / (r["TP_i"] + r["FN_i"])) if (r["TP_i"] + r["FN_i"]) else 0.0,
            axis=1,
        )
        strict["perfect_i"] = ((strict["TP_i"] == strict["n_annotations"]) & (strict["FP_i"] == 0)).astype(int)
        rows.append(_condition_metrics(strict, f"{cond}_strict"))

    return pd.DataFrame(rows).sort_values("condition").reset_index(drop=True)


# ── Optional: re-run LLM judge ────────────────────────────────────────

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


def rerun_judge(traces_path: Path, out_path: Path, model: str = "gpt-5.4") -> None:
    """Re-run the LLM judge from scratch. Requires OPENAI_API_KEY."""
    import os
    import re
    try:
        import openai  # type: ignore
    except ImportError:
        sys.exit("openai package not installed; run 'pip install openai'")

    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        sys.exit("OPENAI_API_KEY env var not set")
    client = openai.OpenAI(api_key=api_key, timeout=180.0, max_retries=2)

    new_lines = []
    n = 0
    with traces_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            payload = json.dumps({
                "annotations": rec.get("annotations", []),
                "predictions": rec.get("predictions", []),
            }, ensure_ascii=False, indent=2)
            try:
                resp = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": SPOT_JUDGE_PROMPT.format(payload=payload)}],
                    max_completion_tokens=4096,
                    temperature=0,
                )
                raw = resp.choices[0].message.content or ""
            except Exception as e:
                raw = f"(API error: {e})"
            m = re.search(r"<response>\s*(\{.*?\})\s*</response>", raw, re.DOTALL)
            new_matches = []
            if m:
                try:
                    new_matches = json.loads(m.group(1)).get("matches", [])
                except json.JSONDecodeError:
                    pass
            new_rec = dict(rec)
            new_rec["matches"] = new_matches
            new_rec["raw_judge_response"] = raw
            new_lines.append(json.dumps(new_rec, ensure_ascii=False))
            n += 1
            if n % 10 == 0:
                print(f"  judged {n} ...")
    out_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    print(f"Wrote re-run judge traces to {out_path} ({n} entries)")


# ── Main ──────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--outputs", default="../raw_outputs",
                   help="Path to validation/raw_outputs/")
    p.add_argument("--ground-truth", default="../ground_truth/spot_ground_truth.csv",
                   help="Path to spot_ground_truth.csv")
    p.add_argument("--metadata", default="../config/paper_metadata.csv",
                   help="Path to paper_metadata.csv (anonymization status)")
    p.add_argument("--judge-traces", default="judge_traces.jsonl",
                   help="Path to judge_traces.jsonl")
    p.add_argument("--per-paper-out", default="per_paper_scores.csv")
    p.add_argument("--aggregate-out", default="aggregate_results.csv")
    p.add_argument("--rerun-judge", action="store_true",
                   help="Call OpenAI to re-run the judge from scratch")
    p.add_argument("--rerun-judge-out", default="judge_traces_rerun.jsonl")
    args = p.parse_args()

    raw_outputs = Path(args.outputs).resolve()
    gt_path = Path(args.ground_truth).resolve()
    meta_path = Path(args.metadata).resolve()
    traces_path = Path(args.judge_traces).resolve()

    if not raw_outputs.exists():
        sys.exit(f"!! raw outputs dir not found: {raw_outputs}")
    if not gt_path.exists():
        sys.exit(f"!! ground truth csv not found: {gt_path}")
    if not traces_path.exists():
        sys.exit(f"!! judge traces not found: {traces_path}")

    if args.rerun_judge:
        rerun_judge(traces_path, Path(args.rerun_judge_out))
        traces_path = Path(args.rerun_judge_out).resolve()

    ground_truth = pd.read_csv(gt_path)
    id_map = load_id_map(meta_path) if meta_path.exists() else {}
    if not id_map:
        # Fallback: identity (judge_traces already use the new IDs).
        id_map = {}

    per_paper = replay_judge_traces(traces_path, ground_truth, id_map, raw_outputs)
    # Annotate the per-paper output with the disputed flag
    per_paper["disputed"] = per_paper.apply(
        lambda r: "yes" if (r["paper_id"], r["condition"]) in DISPUTED_TPS else "no",
        axis=1,
    )
    per_paper.to_csv(args.per_paper_out, index=False)
    agg = aggregate(per_paper)
    agg.to_csv(args.aggregate_out, index=False)

    print()
    print("Per-condition aggregates:")
    print(agg.to_string(index=False))
    print()
    print(f"Wrote {args.per_paper_out}")
    print(f"Wrote {args.aggregate_out}")

    # Anonymization stratification
    if meta_path.exists():
        meta = pd.read_csv(meta_path)
        merged = per_paper.merge(meta[["paper_id", "anonymized"]], on="paper_id", how="left")
        print("\nAnonymization stratification (pass@1 by condition):")
        for cond in ["B1", "B2", "B3", "GD"]:
            grp = merged[merged["condition"] == cond]
            for status in ["yes", "no"]:
                sub = grp[grp["anonymized"] == status]
                if len(sub):
                    rate = (sub["TP_i"] > 0).mean()
                    print(f"  {cond:<3} | anonymized={status} | n={len(sub):>2} | pass@1 = {rate:.2%}")


if __name__ == "__main__":
    main()
