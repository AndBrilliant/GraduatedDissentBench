#!/usr/bin/env python3
"""
Run a single condition (B1, B2, B3, or GD) on a single paper.

Designed to be importable from sweep scripts AND runnable directly:

    python harness/run_pipeline.py \
        --paper data/spot/text_detectable/2405.01133v3/paper.txt \
        --paper-id 2405.01133v3 \
        --condition gd \
        --out-dir data/spot/outputs/pilot/

Outputs JSON to <out-dir>/<paper_id>/<condition>.json with the full protocol
trace (prover reviews, judge, steelman if any, arbiter), plus token/cost stats.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "harness"))

from api_client import (  # noqa: E402
    BudgetExceeded, call_model, configure_tracker, get_tracker,
    parse_json, severity_count,
)
from prompts import (  # noqa: E402
    ARBITER_B3_PROMPT, ARBITER_PROMPT, B1_PROMPT, B2_PROMPT,
    JUDGE_PROMPT, PROVER_PROMPT, STEELMAN_PROMPT,
    THETA_ACCEPT, THETA_NOISE,
)


def jdump(obj) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)


def run_b1(paper_text: str, paper_id: str) -> dict:
    raw = call_model("gpt-5.4", B1_PROMPT.format(paper_text=paper_text),
                     label=f"{paper_id}/b1/review")
    review = parse_json(raw)
    findings = review.get("findings", [])
    sev = severity_count(findings) if findings and isinstance(findings[0], dict) and "severity" in findings[0] else None
    return {
        "condition": "B1",
        "paper_id": paper_id,
        "verdict": review.get("verdict", "unknown"),
        "confidence": review.get("confidence", 0.0),
        "reasoning": review.get("reasoning", ""),
        "findings": findings,
        "severity_counts": sev,
        "raw_review": review,
    }


def run_b2(paper_text: str, paper_id: str) -> dict:
    raw = call_model("gpt-5.4", B2_PROMPT.format(paper_text=paper_text),
                     label=f"{paper_id}/b2/review")
    review = parse_json(raw)
    findings = review.get("findings", [])
    return {
        "condition": "B2",
        "paper_id": paper_id,
        "verdict": review.get("verdict", "unknown"),
        "confidence": review.get("confidence", 0.0),
        "reasoning": review.get("reasoning", ""),
        "findings": findings,
        "severity_counts": severity_count(findings),
        "raw_review": review,
    }


def run_b3(paper_text: str, paper_id: str) -> dict:
    # Two provers in parallel logically (sequential here for cost-cap safety).
    raw_a = call_model("gpt-5.4", PROVER_PROMPT.format(paper_text=paper_text),
                       label=f"{paper_id}/b3/prover_a")
    review_a = parse_json(raw_a)

    raw_b = call_model("deepseek", PROVER_PROMPT.format(paper_text=paper_text),
                       label=f"{paper_id}/b3/prover_b")
    review_b = parse_json(raw_b)

    raw_arb = call_model("opus", ARBITER_B3_PROMPT.format(
        review_a=jdump(review_a), review_b=jdump(review_b),
    ), label=f"{paper_id}/b3/arbiter")
    final = parse_json(raw_arb)
    findings = final.get("findings", [])
    return {
        "condition": "B3",
        "paper_id": paper_id,
        "verdict": final.get("verdict", "unknown"),
        "confidence": final.get("confidence", 0.0),
        "reasoning": final.get("reasoning", ""),
        "findings": findings,
        "severity_counts": severity_count(findings),
        "review_a": review_a,
        "review_b": review_b,
        "arbiter_raw": final,
    }


def run_gd(paper_text: str, paper_id: str) -> dict:
    raw_a = call_model("gpt-5.4", PROVER_PROMPT.format(paper_text=paper_text),
                       label=f"{paper_id}/gd/prover_a")
    review_a = parse_json(raw_a)

    raw_b = call_model("deepseek", PROVER_PROMPT.format(paper_text=paper_text),
                       label=f"{paper_id}/gd/prover_b")
    review_b = parse_json(raw_b)

    raw_judge = call_model("deepseek", JUDGE_PROMPT.format(
        review_a=jdump(review_a), review_b=jdump(review_b),
    ), label=f"{paper_id}/gd/judge")
    judge_analysis = parse_json(raw_judge)
    agreement = float(judge_analysis.get("agreement_score", 0.5) or 0.5)

    if agreement >= THETA_ACCEPT:
        level = "L0"
        snr = None
    else:
        snr = (1.0 - agreement) / THETA_NOISE
        level = "L1" if snr < 1.0 else "L2"

    if level == "L2":
        raw_sa = call_model("gpt-5.4", STEELMAN_PROMPT.format(
            own_review=jdump(review_a), other_review=jdump(review_b),
        ), label=f"{paper_id}/gd/steelman_a")
        steelman_a = parse_json(raw_sa)

        raw_sb = call_model("deepseek", STEELMAN_PROMPT.format(
            own_review=jdump(review_b), other_review=jdump(review_a),
        ), label=f"{paper_id}/gd/steelman_b")
        steelman_b = parse_json(raw_sb)
    else:
        steelman_a = {"steelman_for_other": "N/A — escalation level " + level}
        steelman_b = {"steelman_for_other": "N/A — escalation level " + level}

    raw_arb = call_model("opus", ARBITER_PROMPT.format(
        review_a=jdump(review_a),
        review_b=jdump(review_b),
        judge_analysis=jdump(judge_analysis),
        steelman_a=jdump(steelman_a),
        steelman_b=jdump(steelman_b),
    ), label=f"{paper_id}/gd/arbiter")
    final = parse_json(raw_arb)
    findings = final.get("findings", [])

    return {
        "condition": "GD",
        "paper_id": paper_id,
        "verdict": final.get("verdict", "unknown"),
        "confidence": final.get("confidence", 0.0),
        "reasoning": final.get("reasoning", ""),
        "findings": findings,
        "severity_counts": severity_count(findings),
        "protocol": {
            "level": level,
            "agreement": agreement,
            "snr": snr,
            "theta_accept": THETA_ACCEPT,
            "theta_noise": THETA_NOISE,
        },
        "review_a": review_a,
        "review_b": review_b,
        "judge": judge_analysis,
        "steelman_a": steelman_a,
        "steelman_b": steelman_b,
        "arbiter_raw": final,
    }


CONDITION_FNS = {
    "b1": run_b1,
    "b2": run_b2,
    "b3": run_b3,
    "gd": run_gd,
}


def run_one(paper_path: Path, paper_id: str, condition: str, out_dir: Path) -> dict:
    paper_text = paper_path.read_text(encoding="utf-8")
    fn = CONDITION_FNS[condition.lower()]
    t0 = time.time()
    pre_calls = len(get_tracker().calls)
    pre_cost = get_tracker().total
    result = fn(paper_text, paper_id)
    duration = round(time.time() - t0, 2)
    new_calls = get_tracker().calls[pre_calls:]
    result["meta"] = {
        "paper_chars": len(paper_text),
        "duration_s": duration,
        "n_api_calls": len(new_calls),
        "cost_usd": round(sum(c.cost_usd for c in new_calls), 4),
        "total_input_tokens": sum(c.input_tokens for c in new_calls),
        "total_output_tokens": sum(c.output_tokens for c in new_calls),
        "calls": [vars(c) for c in new_calls],
    }

    paper_out_dir = out_dir / paper_id
    paper_out_dir.mkdir(parents=True, exist_ok=True)
    out_path = paper_out_dir / f"{condition.lower()}.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--paper", required=True, help="Path to paper.txt")
    p.add_argument("--paper-id", required=True)
    p.add_argument("--condition", required=True, choices=list(CONDITION_FNS))
    p.add_argument("--out-dir", required=True)
    p.add_argument("--cap", type=float, default=25.0, help="Cost cap in USD")
    args = p.parse_args()

    configure_tracker(args.cap)
    try:
        result = run_one(Path(args.paper), args.paper_id,
                         args.condition, Path(args.out_dir))
    except BudgetExceeded as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)

    sev = result.get("severity_counts") or {"RETRACTION-WORTHY": 0, "MAJOR-REVISION": 0, "MINOR": 0}
    rw = sev.get("RETRACTION-WORTHY", 0) if sev else 0
    print(f"{args.paper_id} {args.condition.upper()}: verdict={result['verdict']} "
          f"RW={rw} | cost=${result['meta']['cost_usd']:.4f} "
          f"({result['meta']['n_api_calls']} calls, {result['meta']['duration_s']}s)")


if __name__ == "__main__":
    main()
