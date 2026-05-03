#!/usr/bin/env python3
"""
B3 Ablation: Multi-model ensemble WITHOUT steelman exchange.
Same provers (GPT-5.4 + DeepSeek), same arbiter (Opus), but findings are
pooled directly — no judge, no steelman, no adversarial severity challenge.

This isolates the steelman exchange as the active ingredient.
"""
import json, os, sys, time, argparse
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from run_v6 import (call_model, parse_json, PROVER_PROMPT,
                     SEVERITY_RUBRIC)

B3_ARBITER_PROMPT = """You are the Arbiter. Two independent reviewers evaluated this manuscript.

""" + SEVERITY_RUBRIC + """
REVIEW A:
{review_a}

REVIEW B:
{review_b}

TASK: Final severity-ranked assessment.
- Consider both reviews and produce a unified assessment.
- ONLY classify as RETRACTION-WORTHY if fundamentally broken.
  When in doubt, MAJOR-REVISION.

Respond in JSON:
{{"verdict": "flagged"|"not_flagged",
  "confidence": 0.0-1.0,
  "reasoning": "synthesis",
  "findings": [
    {{"finding": "description",
      "severity": "RETRACTION-WORTHY|MAJOR-REVISION|MINOR",
      "confidence_in_severity": 0.0-1.0,
      "justification": "why this level",
      "source": "both|prover_a|prover_b"}}
  ]}}"""


def run_b3(paper_text, paper_id,
           prover_a="gpt-5.4", prover_b="deepseek", arbiter="opus",
           results_dir="results"):
    """B3: Multi-model ensemble, no steelman exchange."""

    print(f"\n{'='*60}")
    print(f"B3 Ablation: {paper_id}")
    print(f"Prover A: {prover_a} | Prover B: {prover_b} | Arbiter: {arbiter}")
    print(f"NO steelman exchange")
    print(f"{'='*60}")

    # Step 1: Independent reviews (same as graduated dissent)
    print("\n[1] Independent reviews...")
    raw_a = call_model(prover_a, PROVER_PROMPT.format(paper_text=paper_text))
    review_a = parse_json(raw_a)
    findings_a = review_a.get("findings", [])
    rw_a = sum(1 for f in findings_a if isinstance(f, dict) and f.get("severity") == "RETRACTION-WORTHY")
    print(f"  Prover A ({prover_a}): {len(findings_a)} findings ({rw_a} RW)")

    raw_b = call_model(prover_b, PROVER_PROMPT.format(paper_text=paper_text))
    review_b = parse_json(raw_b)
    findings_b = review_b.get("findings", [])
    rw_b = sum(1 for f in findings_b if isinstance(f, dict) and f.get("severity") == "RETRACTION-WORTHY")
    print(f"  Prover B ({prover_b}): {len(findings_b)} findings ({rw_b} RW)")

    # Step 2: Send DIRECTLY to arbiter (no judge, no steelman)
    print("\n[2] Arbiter (no steelman)...")
    raw_arb = call_model(arbiter, B3_ARBITER_PROMPT.format(
        review_a=json.dumps(review_a, indent=2),
        review_b=json.dumps(review_b, indent=2)))
    final = parse_json(raw_arb)

    # Count severities
    final_findings = final.get("findings", [])
    sev = {"RETRACTION-WORTHY": 0, "MAJOR-REVISION": 0, "MINOR": 0}
    for f in final_findings:
        s = f.get("severity", "MINOR") if isinstance(f, dict) else "MINOR"
        if s in sev:
            sev[s] += 1

    print(f"\n  FINAL: {sev['RETRACTION-WORTHY']} RW, {sev['MAJOR-REVISION']} MajR, {sev['MINOR']} Minor")

    result = {
        "paper_id": paper_id,
        "condition": "B3_no_steelman",
        "prover_a": prover_a,
        "prover_b": prover_b,
        "arbiter": arbiter,
        "verdict": final.get("verdict", "unknown"),
        "confidence": final.get("confidence", 0),
        "reasoning": final.get("reasoning", ""),
        "findings": final_findings,
        "severity_counts": sev,
        "protocol": {
            "level": "B3",
            "prover_a_findings": len(findings_a),
            "prover_a_rw": rw_a,
            "prover_b_findings": len(findings_b),
            "prover_b_rw": rw_b,
        },
        "timestamp": int(time.time()),
    }

    os.makedirs(results_dir, exist_ok=True)
    ts = int(time.time())
    fn = f"{paper_id}_B3_{prover_a}+{prover_b}_{arbiter}_{ts}.json"
    fp = os.path.join(results_dir, fn)
    with open(fp, "w") as f:
        json.dump(result, f, indent=2)
    print(f"  Saved: {fp}")
    return result


def main():
    parser = argparse.ArgumentParser(description="B3 Ablation: No Steelman Exchange")
    parser.add_argument("--paper", required=True)
    parser.add_argument("--paper-id", required=True)
    parser.add_argument("--results-dir", default="results/baseline_B3")
    args = parser.parse_args()

    paper_text = Path(args.paper).read_text()
    print(f"Paper: {args.paper} ({len(paper_text)} chars)")
    run_b3(paper_text, args.paper_id, results_dir=args.results_dir)


if __name__ == "__main__":
    main()
