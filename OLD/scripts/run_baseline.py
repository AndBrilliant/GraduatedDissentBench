#!/usr/bin/env python3
"""
Baseline runner for v6 benchmark.
B1: Single model, plain review prompt, no severity rubric.
B2: Single model, WITH severity rubric.
"""
import json, os, sys, time, argparse
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from run_v6 import call_model, parse_json, SEVERITY_RUBRIC

B1_PROMPT = """Review this manuscript for methodological correctness. Identify any statistical errors, methodological flaws, unsupported claims, or logical inconsistencies. Be specific.

Manuscript:
{paper_text}

Respond in JSON:
{{"verdict": "flagged"|"not_flagged",
  "confidence": 0.0-1.0,
  "reasoning": "overall assessment",
  "specific_errors_found": ["list of errors"]}}"""

B2_PROMPT = """Review this manuscript for methodological correctness. For each error or concern, classify its severity.

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


def run_baseline(paper_text, paper_id, model, baseline, results_dir, dry_run=False):
    prompt_template = B1_PROMPT if baseline == "B1" else B2_PROMPT
    prompt = prompt_template.format(paper_text=paper_text)

    print(f"  {baseline} | {model} | {paper_id}")

    if dry_run:
        print("  [DRY RUN]")
        return None

    raw = call_model(model, prompt)
    result = parse_json(raw)
    result["paper_id"] = paper_id
    result["model"] = model
    result["baseline"] = baseline
    result["timestamp"] = int(time.time())

    # Count RW findings for B2
    if baseline == "B2":
        findings = result.get("findings", [])
        rw = sum(1 for f in findings if isinstance(f, dict) and f.get("severity") == "RETRACTION-WORTHY")
        result["rw_count"] = rw
    else:
        result["rw_count"] = 0  # B1 doesn't have severity

    os.makedirs(results_dir, exist_ok=True)
    ts = int(time.time())
    fn = f"{paper_id}_{baseline}_{model}_{ts}.json"
    fp = os.path.join(results_dir, fn)
    with open(fp, "w") as f:
        json.dump(result, f, indent=2)

    n_findings = len(result.get("specific_errors_found", result.get("findings", [])))
    print(f"  -> {result.get('verdict','?')} | {n_findings} findings | RW: {result.get('rw_count', '?')}")
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", required=True)
    parser.add_argument("--paper-id", required=True)
    parser.add_argument("--model", default="gpt-5.4")
    parser.add_argument("--baseline", required=True, choices=["B1", "B2"])
    parser.add_argument("--results-dir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    paper_text = Path(args.paper).read_text()
    run_baseline(paper_text, args.paper_id, args.model, args.baseline,
                 args.results_dir, args.dry_run)


if __name__ == "__main__":
    main()
