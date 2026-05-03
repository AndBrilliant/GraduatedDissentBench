#!/usr/bin/env python3
"""
v6 Graduated Dissent Benchmark Runner
Three models, three families, three roles.

Primary: GPT-5.4 (Prover A) + DeepSeek V3.2 (Prover B + Judge) + Opus 4.6 (Arbiter)
Baseline: DeepSeek V3.2 in all roles

Severity integrated from the start. No old models. No shared code with v4.
"""

import json
import os
import sys
import time
import argparse
from pathlib import Path

# ── Model Registry ───────────────────────────────────────────────────────────

MODELS = {
    "gpt-5.4": {
        "provider": "openai",
        "model_id": "gpt-5.4",
    },
    "deepseek": {
        "provider": "deepseek",
        "model_id": "deepseek-chat",
    },
    "opus": {
        "provider": "anthropic",
        "model_id": "claude-opus-4-6",
    },
    "sonnet": {
        "provider": "anthropic",
        "model_id": "claude-sonnet-4-6",
    },
}

# ── API Callers ──────────────────────────────────────────────────────────────

def call_anthropic(model_id, prompt):
    import anthropic
    client = anthropic.Anthropic()
    message = client.messages.create(
        model=model_id,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def call_openai(model_id, prompt, base_url=None, api_key_env="OPENAI_API_KEY"):
    import openai
    kwargs = {}
    if base_url:
        kwargs["base_url"] = base_url
    kwargs["api_key"] = os.environ.get(api_key_env, "")
    client = openai.OpenAI(**kwargs)
    response = client.chat.completions.create(
        model=model_id,
        max_completion_tokens=4096,  # GPT-5.4 requires this instead of max_tokens
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def call_model(model_name, prompt):
    spec = MODELS[model_name]
    model_id = spec["model_id"]
    provider = spec["provider"]

    if provider == "anthropic":
        return call_anthropic(model_id, prompt)
    elif provider == "openai":
        return call_openai(model_id, prompt)
    elif provider == "deepseek":
        return call_openai(
            model_id, prompt,
            base_url="https://api.deepseek.com",
            api_key_env="DEEPSEEK_API_KEY"
        )
    else:
        raise ValueError(f"Unknown provider: {provider}")


def parse_json(raw):
    """Parse JSON from model output, handling markdown fences."""
    text = raw.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        text = "\n".join(lines[1:])
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try to find JSON object in the text
        start = text.find("{")
        end = text.rfind("}") + 1
        if start >= 0 and end > start:
            try:
                return json.loads(text[start:end])
            except:
                pass
        return {"raw": raw, "parse_error": True}


# ── Severity Rubric ──────────────────────────────────────────────────────────

SEVERITY_RUBRIC = """
SEVERITY CLASSIFICATION (required for every finding):

RETRACTION-WORTHY: The error means the paper's central conclusions CANNOT be
supported by the data as presented. Not "could be improved" — "fundamentally broken."
Examples: data coding errors that change the primary outcome, impossible statistical
values, applying tests that don't match the study design rendering all inferences invalid.

MAJOR-REVISION: A real methodological concern that could change conclusions if
addressed differently, but does NOT definitively invalidate them.
Examples: missing controls, underpowered secondary analyses, questionable but
defensible statistical choices.

MINOR: Valid criticism applicable to most published papers. Would not change conclusions.
Examples: no robustness checks, limited generalizability, minor reporting gaps.

KEY TEST: If confirmed, would this need RETRACTION, REVISION, or just NOTING?
"""

# ── Prompts ──────────────────────────────────────────────────────────────────

PROVER_PROMPT = """You are an independent scientific reviewer. Review this manuscript for
methodological correctness. For each error or concern, classify its severity.

""" + SEVERITY_RUBRIC + """
Manuscript:
{paper_text}

Respond in JSON:
{{"verdict": "flagged"|"not_flagged",
  "confidence": 0.0-1.0,
  "reasoning": "overall assessment",
  "findings": [
    {{"finding": "description",
      "severity": "RETRACTION-WORTHY|MAJOR-REVISION|MINOR",
      "justification": "what breaks if confirmed?"}}
  ]}}"""

JUDGE_PROMPT = """Compare two independent reviews of the same manuscript.

REVIEW A:
{review_a}

REVIEW B:
{review_b}

Rate semantic agreement 0.0-1.0. Identify where they disagree on severity.

Respond in JSON:
{{"agreement_score": 0.0-1.0,
  "severity_agreement": "do they agree on which findings are retraction-worthy?",
  "shared_findings": ["findings both identify"],
  "severity_disputes": ["findings where severity differs"],
  "unique_to_a": ["only in A"],
  "unique_to_b": ["only in B"]}}"""

STEELMAN_PROMPT = """You previously reviewed a manuscript.

YOUR REVIEW:
{own_review}

A DIFFERENT REVIEWER reached different conclusions:
{other_review}

TASKS:
1. Build the STRONGEST CASE for the other reviewer's position, especially on severity.
2. For findings you rated RETRACTION-WORTHY: could they be MAJOR-REVISION instead?
3. Which of your severity ratings might be wrong?

""" + SEVERITY_RUBRIC + """
Respond in JSON:
{{"steelman_for_other": "strongest case for their position",
  "severity_i_now_upgrade": ["findings I think are MORE severe"],
  "severity_i_now_downgrade": ["findings I think are LESS severe"],
  "findings_i_still_defend": ["findings + severity I stand by"],
  "new_errors_noticed": ["errors from fresh perspective"]}}"""

ARBITER_PROMPT = """You are the Arbiter. You have the complete deliberation.

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
- Findings where a prover downgraded own severity = probably overstated
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
      "source": "both|prover_a|prover_b|emergent",
      "survived_steelman": true|false}}
  ]}}"""

# ── Thresholds ───────────────────────────────────────────────────────────────

THETA_ACCEPT = 0.90
THETA_NOISE = 0.15


# ── Protocol ─────────────────────────────────────────────────────────────────

def run_graduated_dissent(paper_text, paper_id,
                          prover_a="gpt-5.4", prover_b="deepseek",
                          judge="deepseek", arbiter="opus",
                          results_dir="results", dry_run=False):
    """Full v6 graduated dissent protocol."""

    print(f"\n{'='*60}")
    print(f"v6 Graduated Dissent: {paper_id}")
    print(f"Prover A: {prover_a} | Prover B: {prover_b} | Arbiter: {arbiter}")
    print(f"{'='*60}")

    if dry_run:
        print("[DRY RUN]")
        return None

    # Step 1: Independent reviews
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

    # Step 4: Steelman
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

    # Step 5: Arbiter
    print("\n[5] Arbiter...")
    raw_arb = call_model(arbiter, ARBITER_PROMPT.format(
        review_a=json.dumps(review_a, indent=2),
        review_b=json.dumps(review_b, indent=2),
        judge_analysis=json.dumps(judge_analysis, indent=2),
        steelman_a=json.dumps(steelman_a, indent=2),
        steelman_b=json.dumps(steelman_b, indent=2)))
    final = parse_json(raw_arb)

    # Count severities
    final_findings = final.get("findings", [])
    sev = {"RETRACTION-WORTHY": 0, "MAJOR-REVISION": 0, "MINOR": 0}
    for f in final_findings:
        s = f.get("severity", "MINOR") if isinstance(f, dict) else "MINOR"
        if s in sev:
            sev[s] += 1

    print(f"\n  FINAL: {sev['RETRACTION-WORTHY']} RW, {sev['MAJOR-REVISION']} MajR, {sev['MINOR']} Minor")

    # Save
    result = {
        "paper_id": paper_id,
        "prover_a": prover_a,
        "prover_b": prover_b,
        "judge": judge,
        "arbiter": arbiter,
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
        "timestamp": int(time.time()),
    }

    os.makedirs(results_dir, exist_ok=True)
    ts = int(time.time())
    fn = f"{paper_id}_{prover_a}+{prover_b}_{arbiter}_{ts}.json"
    fp = os.path.join(results_dir, fn)
    with open(fp, "w") as f:
        json.dump(result, f, indent=2)
    print(f"  Saved: {fp}")
    return result


def main():
    parser = argparse.ArgumentParser(description="v6 Graduated Dissent Benchmark")
    parser.add_argument("--paper", required=True, help="Path to anonymized paper")
    parser.add_argument("--paper-id", required=True, help="Paper identifier")
    parser.add_argument("--prover-a", default="gpt-5.4", choices=["gpt-5.4", "deepseek", "opus", "sonnet"])
    parser.add_argument("--prover-b", default="deepseek", choices=["gpt-5.4", "deepseek", "opus", "sonnet"])
    parser.add_argument("--judge", default="deepseek", choices=["gpt-5.4", "deepseek", "opus", "sonnet"])
    parser.add_argument("--arbiter", default="opus", choices=["gpt-5.4", "deepseek", "opus", "sonnet"])
    parser.add_argument("--results-dir", default="results")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    paper_text = Path(args.paper).read_text()
    print(f"Paper: {args.paper} ({len(paper_text)} chars)")

    run_graduated_dissent(
        paper_text, args.paper_id,
        prover_a=args.prover_a, prover_b=args.prover_b,
        judge=args.judge, arbiter=args.arbiter,
        results_dir=args.results_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
