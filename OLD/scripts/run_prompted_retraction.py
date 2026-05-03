#!/usr/bin/env python3
"""
Run single models with the prompt: "This paper was retracted. Identify the methodological
error that caused the retraction."

Tests whether knowing retraction status unlocks detection that blind review misses.
"""
import json, os, sys, time, argparse
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from run_v6 import call_model, parse_json, MODELS

PROMPTED_PROMPT = """This paper was retracted due to a methodological error. Your task is to
identify the specific error that caused the retraction.

Read the manuscript carefully and identify:
1. The specific methodological, statistical, or conceptual error
2. Why this error invalidates the paper's conclusions
3. What the correct approach should have been

Manuscript:
{paper_text}

Respond in JSON:
{{"identified_error": "description of the specific error you believe caused retraction",
  "why_fatal": "why this error invalidates the conclusions",
  "correct_approach": "what should have been done instead",
  "confidence": 0.0-1.0,
  "additional_errors": ["list of other methodological concerns"]}}"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", required=True)
    parser.add_argument("--paper-id", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--results-dir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    paper_text = Path(args.paper).read_text()
    prompt = PROMPTED_PROMPT.format(paper_text=paper_text)

    print(f"  Prompted retraction | {args.model} | {args.paper_id}")

    if args.dry_run:
        print("  [DRY RUN]")
        return

    raw = call_model(args.model, prompt)
    result = parse_json(raw)
    result["paper_id"] = args.paper_id
    result["model"] = args.model
    result["condition"] = "prompted_retraction"
    result["timestamp"] = int(time.time())

    os.makedirs(args.results_dir, exist_ok=True)
    ts = int(time.time())
    fn = f"{args.paper_id}_prompted_{args.model}_{ts}.json"
    fp = os.path.join(args.results_dir, fn)
    with open(fp, "w") as f:
        json.dump(result, f, indent=2)

    error = str(result.get("identified_error", ""))[:120]
    conf = result.get("confidence", "?")
    print(f"  -> {error}")
    print(f"  -> confidence: {conf}")


if __name__ == "__main__":
    main()
