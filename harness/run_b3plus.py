#!/usr/bin/env python3
"""
Budget-matched non-adversarial control conditions for the SPOT benchmark.

  B3+   : 5-call pipeline matching GD's compute, but with NEUTRAL reflection
          instead of adversarial steelman exchange.
          Calls: prover_a (gpt-5.4), prover_b (deepseek),
                 reflection_a (gpt-5.4), reflection_b (deepseek),
                 arbiter (opus).

  B3++  : 5-call pipeline matching GD's compute, with ANTI-steelman reflection
          (each prover defends their own severity ratings rather than arguing
          against them). Same call shape, different reflection prompt.

These conditions isolate whether the GD result is driven by *adversarial*
re-engagement specifically, or by any second pass at the prover stage.

Usage:
    python harness/run_b3plus.py --paper-id 2405.01133v3 \
        --paper data/spot/text_detectable/2405.01133v3/paper.txt \
        --condition b3plus  --out-dir data/spot/outputs/budget_matched/
    python harness/run_b3plus.py --paper-id 2405.01133v3 \
        --paper data/spot/text_detectable/2405.01133v3/paper.txt \
        --condition b3plusplus  --out-dir data/spot/outputs/budget_matched/

The sweep script `harness/sweep_b3plus.py` walks all 50 SPOT papers.
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
    ANTI_STEELMAN_PROMPT, ARBITER_REFLECT_PROMPT, PROVER_PROMPT,
    REFLECTION_PROMPT,
)


def jdump(obj) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)


def _run_with_reflection(paper_text: str, paper_id: str, *,
                          condition_label: str,
                          reflection_prompt: str) -> dict:
    """Common 5-call pipeline: 2 provers, 2 reflections, 1 arbiter."""
    raw_a = call_model("gpt-5.4",
                        PROVER_PROMPT.format(paper_text=paper_text),
                        label=f"{paper_id}/{condition_label}/prover_a")
    review_a = parse_json(raw_a)

    raw_b = call_model("deepseek",
                        PROVER_PROMPT.format(paper_text=paper_text),
                        label=f"{paper_id}/{condition_label}/prover_b")
    review_b = parse_json(raw_b)

    raw_ra = call_model("gpt-5.4", reflection_prompt.format(
        own_review=jdump(review_a),
        other_review=jdump(review_b),
    ), label=f"{paper_id}/{condition_label}/reflection_a")
    reflection_a = parse_json(raw_ra)

    raw_rb = call_model("deepseek", reflection_prompt.format(
        own_review=jdump(review_b),
        other_review=jdump(review_a),
    ), label=f"{paper_id}/{condition_label}/reflection_b")
    reflection_b = parse_json(raw_rb)

    raw_arb = call_model("opus", ARBITER_REFLECT_PROMPT.format(
        review_a=jdump(review_a),
        review_b=jdump(review_b),
        reflection_a=jdump(reflection_a),
        reflection_b=jdump(reflection_b),
    ), label=f"{paper_id}/{condition_label}/arbiter")
    final = parse_json(raw_arb)
    findings = final.get("findings", []) or []

    return {
        "condition": condition_label.upper(),
        "paper_id": paper_id,
        "verdict": final.get("verdict", "unknown"),
        "confidence": final.get("confidence", 0.0),
        "reasoning": final.get("reasoning", ""),
        "findings": findings,
        "severity_counts": severity_count(findings),
        "review_a": review_a,
        "review_b": review_b,
        "reflection_a": reflection_a,
        "reflection_b": reflection_b,
        "arbiter_raw": final,
    }


def run_b3plus(paper_text: str, paper_id: str) -> dict:
    return _run_with_reflection(paper_text, paper_id,
                                  condition_label="b3plus",
                                  reflection_prompt=REFLECTION_PROMPT)


def run_b3plusplus(paper_text: str, paper_id: str) -> dict:
    return _run_with_reflection(paper_text, paper_id,
                                  condition_label="b3plusplus",
                                  reflection_prompt=ANTI_STEELMAN_PROMPT)


CONDITION_FNS = {
    "b3plus": run_b3plus,
    "b3plusplus": run_b3plusplus,
}


def run_one(paper_path: Path, paper_id: str, condition: str,
             out_dir: Path) -> dict:
    paper_text = paper_path.read_text(encoding="utf-8")
    fn = CONDITION_FNS[condition.lower()]
    t0 = time.time()
    pre_calls = len(get_tracker().calls)
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
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False),
                          encoding="utf-8")
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--paper", required=True)
    p.add_argument("--paper-id", required=True)
    p.add_argument("--condition", required=True,
                   choices=list(CONDITION_FNS))
    p.add_argument("--out-dir", required=True)
    p.add_argument("--cap", type=float, default=25.0)
    args = p.parse_args()

    configure_tracker(args.cap)
    try:
        result = run_one(Path(args.paper), args.paper_id,
                          args.condition, Path(args.out_dir))
    except BudgetExceeded as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)

    sev = result.get("severity_counts") or {}
    rw = sev.get("RETRACTION-WORTHY", 0)
    print(f"{args.paper_id} {args.condition}: "
          f"verdict={result['verdict']} RW={rw} | "
          f"cost=${result['meta']['cost_usd']:.4f} "
          f"({result['meta']['n_api_calls']} calls, "
          f"{result['meta']['duration_s']}s)")


if __name__ == "__main__":
    main()
