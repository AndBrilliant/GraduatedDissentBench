#!/usr/bin/env python3
"""
Re-parse pilot outputs that originally hit a truncated-arbiter parse error.

Walks data/spot/outputs/<sweep>/<paper>/{b3,gd}.json (and optionally b1/b2),
looks at the stored arbiter_raw / raw_review, re-runs the improved parse_json
from api_client, and if recovery yields better data (more findings, valid
verdict), updates the file in place.

No API calls — uses only stored raw responses.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "harness"))

from api_client import parse_json, severity_count  # noqa: E402


def reparse_one(path: Path) -> dict:
    """Return a summary of what changed (or empty dict if no change)."""
    data = json.loads(path.read_text(encoding="utf-8"))
    cond = data.get("condition", "")
    changed = False
    notes = []

    # Identify the "raw" arbiter or single-model response we want to re-parse.
    # Schema (per run_pipeline.py):
    #   B1/B2: raw_review
    #   B3:    arbiter_raw
    #   GD:    arbiter_raw
    candidate_keys = ["arbiter_raw", "raw_review"]
    for key in candidate_keys:
        if key not in data:
            continue
        block = data[key]
        if not isinstance(block, dict):
            continue
        # Block has 'raw' string only when the original parse failed.
        raw = block.get("raw")
        if not raw:
            continue
        recovered = parse_json(raw)
        if recovered.get("parse_error"):
            notes.append(f"{key}: still parse_error after recovery")
            continue
        old_findings = block.get("findings", []) if isinstance(block, dict) else []
        new_findings = recovered.get("findings", [])
        old_verdict = data.get("verdict")
        new_verdict = recovered.get("verdict")
        # Only count it as improved if we got more findings or a different verdict.
        improved = (len(new_findings) > len(old_findings)) or (
            old_verdict in ("unknown", None, "") and new_verdict
        )
        if improved:
            data[key] = recovered
            data["verdict"] = recovered.get("verdict", data.get("verdict"))
            data["confidence"] = recovered.get("confidence", data.get("confidence"))
            data["reasoning"] = recovered.get("reasoning", data.get("reasoning"))
            data["findings"] = new_findings
            data["severity_counts"] = severity_count(new_findings)
            data.setdefault("reparse", []).append({
                "key": key,
                "verdict_before": old_verdict,
                "verdict_after": data["verdict"],
                "n_findings_before": len(old_findings),
                "n_findings_after": len(new_findings),
                "truncated": recovered.get("truncated", False),
            })
            changed = True

    if changed:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        return {"path": str(path), "condition": cond, "changes": data["reparse"][-1]}
    return {}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sweep", default="pilot_n10")
    p.add_argument("--root", default=None,
                   help="Override default data/spot/outputs/<sweep>/")
    args = p.parse_args()

    root = Path(args.root) if args.root else (
        REPO / "data" / "spot" / "outputs" / args.sweep
    )
    if not root.exists():
        print(f"!! sweep dir not found: {root}")
        return 1

    files = sorted(root.glob("*/*.json"))
    print(f"Scanning {len(files)} files in {root.relative_to(REPO)} ...")

    changed = []
    for f in files:
        res = reparse_one(f)
        if res:
            changed.append(res)
            ch = res["changes"]
            print(f"  RECOVERED {f.parent.name}/{f.name}: "
                  f"verdict {ch['verdict_before']} -> {ch['verdict_after']}, "
                  f"findings {ch['n_findings_before']} -> {ch['n_findings_after']}"
                  f"{' (truncated)' if ch['truncated'] else ''}")

    print(f"\n{len(changed)} files recovered.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
