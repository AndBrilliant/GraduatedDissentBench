#!/usr/bin/env python3
"""
LLM-screen the candidate retracted papers from candidates_<batch>.csv.

For each candidate: send the retraction-notice abstract to a cheap model
(DeepSeek) and ask: is this a methodological error (vs misconduct), is the
specific error described, would it be text-detectable from the manuscript?

Outputs data/retracted/candidates/screened_<batch>.csv with verdict columns
and a one-paragraph rationale per candidate.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "harness"))

from api_client import call_model, configure_tracker, parse_json  # noqa: E402

SCREEN_PROMPT = """You are screening a retraction notice to decide if the original paper meets these inclusion criteria:

(A) METHODOLOGICAL ERROR — was the paper retracted because of a methodological mistake (statistical error, coding error, design flaw, calculation error, data-processing error, reproducibility failure)? NOT for misconduct (plagiarism, fabrication, image manipulation, paper mill, fraud, authorship dispute, ethics breach).

(B) SPECIFIC ERROR DOCUMENTED — does the retraction notice describe the specific error in enough detail that someone re-reading the manuscript could check for it?

(C) TEXT-DETECTABLE — would the error be inferable from the manuscript's text (rather than requiring inspection of unpublished code, hardware, raw data, or images)?

JOURNAL: {journal}
ORIGINAL TITLE: {title}
RETRACTION NOTICE ABSTRACT: {notice}

Respond in JSON with exactly these keys:
{{"methodological": true|false,
  "specific_error_documented": true|false,
  "text_detectable": true|false,
  "include": true|false,
  "summary": "one-sentence summary of the documented error",
  "rationale": "two-sentence rationale for the include/exclude decision"}}

Set "include" true only if all three criteria above hold. Be strict: if the notice only says 'paper mill', 'commercial entity', 'compromised peer review', 'AI-generated', 'duplicate publication', or 'integrity concerns' without describing a specific methodological error, return include=false.
"""


def screen_one(row: dict) -> dict:
    notice = row.get("retraction_abstract") or ""
    notice = notice[:3000]  # keep prompt small
    prompt = SCREEN_PROMPT.format(
        journal=row.get("container_title", ""),
        title=row.get("original_title", ""),
        notice=notice,
    )
    try:
        raw = call_model("deepseek", prompt, temperature=0,
                         label=f"screen/{row.get('original_doi', '')}")
        verdict = parse_json(raw)
    except Exception as e:
        verdict = {"include": False, "summary": "(screen error)",
                   "rationale": f"{type(e).__name__}: {e}"}
    return verdict


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--in-csv", default="data/retracted/candidates/candidates_v1.csv")
    p.add_argument("--out-csv", default="data/retracted/candidates/screened_v1.csv")
    p.add_argument("--cap", type=float, default=2.0,
                   help="USD cap for screening API calls")
    p.add_argument("--max", type=int, default=None,
                   help="Cap number of candidates screened (for testing)")
    args = p.parse_args()

    in_path = REPO / args.in_csv
    out_path = REPO / args.out_csv

    df = pd.read_csv(in_path)
    if args.max:
        df = df.head(args.max)
    print(f"Screening {len(df)} candidates (cap ${args.cap}) ...")

    configure_tracker(args.cap)

    rows = []
    for i, row in df.iterrows():
        # Skip rows with empty notice abstracts — can't screen them.
        if not isinstance(row.get("retraction_abstract"), str) or len(row["retraction_abstract"]) < 50:
            continue
        v = screen_one(row.to_dict())
        out = dict(row)
        out["screen_methodological"] = bool(v.get("methodological", False))
        out["screen_specific"] = bool(v.get("specific_error_documented", False))
        out["screen_text_detectable"] = bool(v.get("text_detectable", False))
        out["screen_include"] = bool(v.get("include", False))
        out["screen_summary"] = v.get("summary", "")
        out["screen_rationale"] = v.get("rationale", "")
        rows.append(out)
        if (len(rows) % 10) == 0:
            n_keep = sum(1 for r in rows if r["screen_include"])
            print(f"  screened {len(rows)} ... included so far: {n_keep}")

    out_df = pd.DataFrame(rows)
    out_df.to_csv(out_path, index=False)

    n_keep = (out_df["screen_include"] == True).sum()
    print(f"\nWrote {out_path.relative_to(REPO)}")
    print(f"Of {len(out_df)} screened, {n_keep} marked include=True")
    print()
    if n_keep:
        print("Included candidates:")
        keep = out_df[out_df["screen_include"] == True]
        for _, r in keep.head(30).iterrows():
            print(f"  - {r['original_doi']:<35} | {r['screen_summary'][:100]}")


if __name__ == "__main__":
    raise SystemExit(main() or 0)
