#!/usr/bin/env python3
"""
Permissive arbiter run — same protocol, different arbiter instructions.
"Flag as RW if the error COULD invalidate conclusions."
"""
import json, os, sys, time, argparse
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from run_v6 import (call_model, parse_json, PROVER_PROMPT, JUDGE_PROMPT,
                     STEELMAN_PROMPT, SEVERITY_RUBRIC, THETA_ACCEPT, THETA_NOISE)

PERMISSIVE_ARBITER_PROMPT = """You are the Arbiter. You have the complete deliberation.

""" + SEVERITY_RUBRIC + """
REVIEW A:
{review_a}

REVIEW B:
{review_b}

JUDGE:
{judge_analysis}

STEELMAN EXCHANGE:
A's steelman of B: {steelman_a}
B's steelman of A: {steelman_b}

TASK: Final severity-ranked assessment.
- Findings surviving steelman with consistent severity = high confidence
- Findings where a prover downgraded own severity = consider carefully but do not automatically dismiss
- Classify as RETRACTION-WORTHY if the error COULD invalidate the paper's central conclusions, even if alternative interpretations exist.
  Be thorough: it is better to flag a potential fatal flaw for human review than to miss one.

Respond in JSON:
{{"verdict": "flagged"|"not_flagged",
  "confidence": 0.0-1.0,
  "reasoning": "synthesis",
  "findings": [
    {{"finding": "description",
      "severity": "RETRACTION-WORTHY|MAJOR-REVISION|MINOR",
      "confidence_in_severity": 0.0-1.0,
      "justification": "why this level",
      "source": "both|prover_a|prover_b|emergent",
      "survived_steelman": true|false}}
  ]}}"""


def run_permissive_gd(paper_text, paper_id,
                      prover_a="gpt-5.4", prover_b="deepseek",
                      judge="deepseek", arbiter="opus",
                      results_dir="results"):

    print(f"\n{'='*60}")
    print(f"PERMISSIVE Graduated Dissent: {paper_id}")
    print(f"{'='*60}")

    # Step 1: Independent reviews (identical to conservative)
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

    # Step 2: Judge
    print("\n[2] Judge comparison...")
    raw_judge = call_model(judge, JUDGE_PROMPT.format(
        review_a=json.dumps(review_a, indent=2),
        review_b=json.dumps(review_b, indent=2)))
    judge_analysis = parse_json(raw_judge)
    agreement = judge_analysis.get("agreement_score", 0.5)
    print(f"  Agreement: {agreement}")

    # Step 3: Escalation
    if agreement >= THETA_ACCEPT:
        level = "L0"
        print(f"  [L0] Agreement >= {THETA_ACCEPT}")
    else:
        snr = (1.0 - agreement) / THETA_NOISE
        if snr < 1.0:
            level = "L1"
            print(f"  [L1] SNR {snr:.2f} < 1.0")
        else:
            level = "L2"
            print(f"  [L2] SNR {snr:.2f} — steelman exchange")

    # Step 4: Steelman (identical to conservative)
    if level == "L2":
        print("\n[4] Steelman exchange...")
        raw_sa = call_model(prover_a, STEELMAN_PROMPT.format(
            own_review=json.dumps(review_a, indent=2),
            other_review=json.dumps(review_b, indent=2)))
        steelman_a = parse_json(raw_sa)

        raw_sb = call_model(prover_b, STEELMAN_PROMPT.format(
            own_review=json.dumps(review_b, indent=2),
            other_review=json.dumps(review_a, indent=2)))
        steelman_b = parse_json(raw_sb)

        up_a = len(steelman_a.get("severity_i_now_upgrade", []))
        dn_a = len(steelman_a.get("severity_i_now_downgrade", []))
        up_b = len(steelman_b.get("severity_i_now_upgrade", []))
        dn_b = len(steelman_b.get("severity_i_now_downgrade", []))
        print(f"  A: {up_a} up, {dn_a} down | B: {up_b} up, {dn_b} down")
    else:
        steelman_a = {"steelman_for_other": "N/A"}
        steelman_b = {"steelman_for_other": "N/A"}

    # Step 5: PERMISSIVE Arbiter
    print("\n[5] PERMISSIVE Arbiter...")
    raw_arb = call_model(arbiter, PERMISSIVE_ARBITER_PROMPT.format(
        review_a=json.dumps(review_a, indent=2),
        review_b=json.dumps(review_b, indent=2),
        judge_analysis=json.dumps(judge_analysis, indent=2),
        steelman_a=json.dumps(steelman_a, indent=2),
        steelman_b=json.dumps(steelman_b, indent=2)))
    final = parse_json(raw_arb)

    final_findings = final.get("findings", [])
    sev = {"RETRACTION-WORTHY": 0, "MAJOR-REVISION": 0, "MINOR": 0}
    for f in final_findings:
        s = f.get("severity", "MINOR") if isinstance(f, dict) else "MINOR"
        if s in sev:
            sev[s] += 1

    print(f"\n  FINAL: {sev['RETRACTION-WORTHY']} RW, {sev['MAJOR-REVISION']} MajR, {sev['MINOR']} Minor")

    result = {
        "paper_id": paper_id,
        "condition": "permissive_arbiter",
        "prover_a": prover_a,
        "prover_b": prover_b,
        "judge": judge,
        "arbiter": arbiter,
        "arbiter_mode": "permissive",
        "verdict": final.get("verdict", "unknown"),
        "confidence": final.get("confidence", 0),
        "reasoning": final.get("reasoning", ""),
        "findings": final_findings,
        "severity_counts": sev,
        "protocol": {
            "level": level,
            "agreement": agreement,
            "prover_a_findings": len(findings_a),
            "prover_a_rw": rw_a,
            "prover_b_findings": len(findings_b),
            "prover_b_rw": rw_b,
        },
        "raw_intermediate": {
            "review_a": review_a,
            "review_b": review_b,
            "judge_analysis": judge_analysis,
            "steelman_a": steelman_a if level == "L2" else None,
            "steelman_b": steelman_b if level == "L2" else None,
            "arbiter_output": final,
        },
        "timestamp": int(time.time()),
    }

    os.makedirs(results_dir, exist_ok=True)
    ts = int(time.time())
    fn = f"{paper_id}_permissive_{ts}.json"
    fp = os.path.join(results_dir, fn)
    with open(fp, "w") as f:
        json.dump(result, f, indent=2)
    print(f"  Saved: {fp}")
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", required=True)
    parser.add_argument("--paper-id", required=True)
    parser.add_argument("--results-dir", default="results/permissive")
    args = parser.parse_args()

    paper_text = Path(args.paper).read_text()
    print(f"Paper: {args.paper} ({len(paper_text)} chars)")
    run_permissive_gd(paper_text, args.paper_id, results_dir=args.results_dir)


if __name__ == "__main__":
    main()
