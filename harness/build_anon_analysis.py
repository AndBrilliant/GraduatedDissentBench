#!/usr/bin/env python3
"""
Build validation/anonymization_analysis/ artifacts.

Two phases:
  --phase pre   : write pre_fix_anon_split.csv + pre_fix_aggregate.md from the
                  current validation/scoring/per_paper_scores.csv. Run this
                  BEFORE the re-anonymized 10 are re-scored.
  --phase post  : write post_fix_results.csv from a freshly-rescored
                  per_paper_scores.csv, then write anonymization_effect.md
                  comparing before/after and computing per-paper flips.

Both phases also write a per-paper summary that includes paper category and
SPOT error category for downstream discussion.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
VALID = REPO / "validation"
ANON = VALID / "anonymization_analysis"
META = VALID / "config" / "paper_metadata.csv"
GT = VALID / "ground_truth" / "spot_ground_truth.csv"


def per_paper_split(per_paper_csv: Path) -> pd.DataFrame:
    """Reshape per_paper_scores.csv into one row per paper with B1/B2/B3/GD pass flags."""
    df = pd.read_csv(per_paper_csv)
    pivot = df.pivot_table(
        index="paper_id", columns="condition", values="TP_i",
        aggfunc="first", fill_value=0
    ).astype(int)
    pivot = (pivot > 0).astype(int)
    pivot.columns = [f"{c}_pass" for c in pivot.columns]
    pivot = pivot.reset_index()

    meta = pd.read_csv(META)[["paper_id", "anonymized", "paper_category"]]
    pivot = pivot.merge(meta, on="paper_id", how="left")

    # Add SPOT error_category (first annotation per paper)
    gt = pd.read_csv(GT)
    first_err = gt.sort_values("annotation_index").drop_duplicates("paper_id")[
        ["paper_id", "error_category"]
    ]
    pivot = pivot.merge(first_err, on="paper_id", how="left")

    cols = ["paper_id", "anonymized", "paper_category", "error_category",
            "B1_pass", "B2_pass", "B3_pass", "GD_pass"]
    cols = [c for c in cols if c in pivot.columns]
    return pivot[cols].sort_values("paper_id")


def aggregate_table(per_paper: pd.DataFrame) -> pd.DataFrame:
    """Pass@1 by condition × anonymization status."""
    rows = []
    for cond in ["B1", "B2", "B3", "GD"]:
        col = f"{cond}_pass"
        if col not in per_paper.columns:
            continue
        for status in ["yes", "no"]:
            sub = per_paper[per_paper["anonymized"] == status]
            n = len(sub)
            tp = int(sub[col].sum())
            rate = tp / n if n else 0.0
            rows.append({"condition": cond, "anonymized": status,
                         "n": n, "tp": tp, "pass_at_1": round(rate, 4)})
    return pd.DataFrame(rows)


def md_aggregate(table: pd.DataFrame, header: str) -> str:
    out = [f"# {header}", ""]
    out.append("| Condition | Anonymized | n | TPs | pass@1 |")
    out.append("|---|---|---:|---:|---:|")
    for _, r in table.iterrows():
        out.append(f"| {r['condition']} | {r['anonymized']} | {r['n']} | "
                   f"{r['tp']} | {r['pass_at_1']:.2%} |")
    out.append("")
    out.append("**Per-condition deltas (anonymized − un-anonymized):**")
    out.append("")
    out.append("| Condition | pass@1 (anon) | pass@1 (un-anon) | Δ (pp) |")
    out.append("|---|---:|---:|---:|")
    for cond in ["B1", "B2", "B3", "GD"]:
        sub = table[table["condition"] == cond]
        if len(sub) != 2:
            continue
        a = sub[sub["anonymized"] == "yes"]["pass_at_1"].iloc[0]
        u = sub[sub["anonymized"] == "no"]["pass_at_1"].iloc[0]
        out.append(f"| {cond} | {a:.2%} | {u:.2%} | {(a - u) * 100:+.1f} |")
    out.append("")
    return "\n".join(out)


def write_pre(per_paper_csv: Path):
    ANON.mkdir(parents=True, exist_ok=True)
    per_paper = per_paper_split(per_paper_csv)
    per_paper.to_csv(ANON / "pre_fix_anon_split.csv", index=False)

    table = aggregate_table(per_paper)
    md = md_aggregate(table, "Pre-fix aggregate (mixed anonymization)")
    md += "\n## Context\n\n"
    md += ("This snapshot was taken with 10 papers anonymized via the same "
           "text-anonymization pipeline used for an earlier retracted-paper "
           "benchmark, and 10 papers run on the original parsed text from "
           "the public SPOT release. The anonymization status was a function "
           "of two batches drawn with different random seeds, not an "
           "intentional control. The deltas above motivated re-anonymizing "
           "the second batch and re-running it for consistency. The "
           "post-fix comparison is in `anonymization_effect.md`.\n")
    (ANON / "pre_fix_aggregate.md").write_text(md, encoding="utf-8")
    print(f"Wrote {ANON.relative_to(REPO)}/pre_fix_anon_split.csv")
    print(f"Wrote {ANON.relative_to(REPO)}/pre_fix_aggregate.md")


def write_post(per_paper_csv: Path):
    ANON.mkdir(parents=True, exist_ok=True)
    per_paper_post = per_paper_split(per_paper_csv)
    per_paper_post.to_csv(ANON / "post_fix_results.csv", index=False)
    print(f"Wrote {ANON.relative_to(REPO)}/post_fix_results.csv")

    pre_csv = ANON / "pre_fix_anon_split.csv"
    if not pre_csv.exists():
        print("!! no pre-fix snapshot found; run --phase pre first")
        return
    pre = pd.read_csv(pre_csv)
    post = per_paper_post.copy()

    # Identify the originally-unanonymized 10 papers (anonymized="no" in pre).
    target_ids = set(pre[pre["anonymized"] == "no"]["paper_id"])
    pre_t = pre[pre["paper_id"].isin(target_ids)].set_index("paper_id")
    post_t = post[post["paper_id"].isin(target_ids)].set_index("paper_id")

    # Per-paper flips
    flip_rows = []
    for pid in sorted(target_ids):
        if pid not in pre_t.index or pid not in post_t.index:
            continue
        pre_row = pre_t.loc[pid]
        post_row = post_t.loc[pid]
        rec = {"paper_id": pid,
               "paper_category": pre_row.get("paper_category", ""),
               "error_category": pre_row.get("error_category", "")}
        for cond in ["B1", "B2", "B3", "GD"]:
            col = f"{cond}_pass"
            if col in pre_row and col in post_row:
                pre_v = int(pre_row[col])
                post_v = int(post_row[col])
                rec[f"{cond}_pre"] = pre_v
                rec[f"{cond}_post"] = post_v
                if pre_v == 0 and post_v == 1:
                    rec[f"{cond}_flip"] = "→TP"
                elif pre_v == 1 and post_v == 0:
                    rec[f"{cond}_flip"] = "→miss"
                else:
                    rec[f"{cond}_flip"] = ""
        flip_rows.append(rec)
    flips = pd.DataFrame(flip_rows)
    flips.to_csv(ANON / "per_paper_flips.csv", index=False)

    # Aggregate-level before/after on the 10 affected papers
    md = ["# Anonymization effect: before vs after re-anonymization", ""]
    md.append("## Setup")
    md.append("")
    md.append("Of the n=20 SPOT pilot papers, 10 were originally run on un-")
    md.append("anonymized text (the parsed content as published by the SPOT")
    md.append("dataset, including author bylines, journal headers, dates, and")
    md.append("affiliations). The other 10 were run on text passed through the")
    md.append("anonymization pipeline used in an earlier retracted-paper")
    md.append("benchmark.")
    md.append("")
    md.append("This document compares model performance on the *same 10 papers*")
    md.append("under the two conditions:")
    md.append("- **Pre-fix**: original parsed text (un-anonymized)")
    md.append("- **Post-fix**: same 10 papers re-run on anonymized text")
    md.append("")
    md.append("All other inputs (prompts, model versions, parameters, judge)")
    md.append("are identical between the two runs.")
    md.append("")

    md.append("## Aggregate pass@1 on the 10 affected papers")
    md.append("")
    md.append("| Condition | Pre-fix (un-anon) | Post-fix (anon) | Δ (pp) |")
    md.append("|---|---:|---:|---:|")
    for cond in ["B1", "B2", "B3", "GD"]:
        col = f"{cond}_pass"
        if col not in pre_t.columns or col not in post_t.columns:
            continue
        pre_rate = pre_t[col].mean()
        post_rate = post_t[col].mean()
        md.append(f"| {cond} | {pre_rate:.2%} | {post_rate:.2%} | "
                  f"{(post_rate - pre_rate) * 100:+.1f} |")
    md.append("")

    md.append("## Per-paper detection-flip table")
    md.append("")
    md.append("Rows are the 10 originally-unanonymized papers. Each cell shows")
    md.append("`pre→post` per condition, with markers for flips: `→TP` means")
    md.append("the paper was missed pre-fix and detected post-fix; `→miss`")
    md.append("means it was detected pre-fix and missed post-fix. Blank means")
    md.append("no change.")
    md.append("")
    md.append("| Paper | Category | SPOT error type | B1 | B2 | B3 | GD |")
    md.append("|---|---|---|---|---|---|---|")
    for _, r in flips.iterrows():
        md.append(
            f"| {r['paper_id']} | {r.get('paper_category','')[:18]} "
            f"| {r.get('error_category','')[:24]} "
            f"| {r.get('B1_pre',0)}→{r.get('B1_post',0)} {r.get('B1_flip','')} "
            f"| {r.get('B2_pre',0)}→{r.get('B2_post',0)} {r.get('B2_flip','')} "
            f"| {r.get('B3_pre',0)}→{r.get('B3_post',0)} {r.get('B3_flip','')} "
            f"| {r.get('GD_pre',0)}→{r.get('GD_post',0)} {r.get('GD_flip','')} |"
        )
    md.append("")

    md.append("## Reading these results")
    md.append("")
    md.append("**If anonymization itself is doing the work**, the post-fix")
    md.append("pass@1 on these 10 papers should rise toward the level seen")
    md.append("for the originally-anonymized 10. We saw `B1=40, B2=30, B3=30,")
    md.append("GD=50` on those 10 in the pre-fix snapshot.")
    md.append("")
    md.append("**If the gap was paper-category mix or sampling noise**, the")
    md.append("post-fix pass@1 on these 10 will stay close to the pre-fix")
    md.append("rates: `B1=10, B2=10, B3=20, GD=20`.")
    md.append("")
    md.append("Per-paper flips show *which specific papers* changed status.")
    md.append("If the same papers consistently flip across multiple conditions,")
    md.append("that's evidence anonymization affects model behavior on those")
    md.append("particular papers (e.g., by removing distracting bylines).")
    md.append("")
    md.append("## Related: pre/post-cutoff null result")
    md.append("")
    md.append("In the parallel retracted-paper benchmark, papers were stratified")
    md.append("by training-cutoff status (whether the retraction occurred before")
    md.append("or after the model's training-data cutoff). Detection rates on")
    md.append("post-cutoff retractions were comparable to pre-cutoff retractions,")
    md.append("supporting that memorization of retraction status is not the")
    md.append("primary driver of detection in those results.")
    md.append("")
    md.append("Two confounds were therefore tested:")
    md.append("- **Memorization (pre/post training cutoff)**: null effect.")
    md.append("- **Anonymization (raw vs scrubbed text)**: see table above.")
    md.append("")
    md.append("If anonymization shows a real signal here, prestige and")
    md.append("formatting cues may be a larger confound than memorization in")
    md.append("LLM-based scientific evaluation.")

    (ANON / "anonymization_effect.md").write_text("\n".join(md), encoding="utf-8")
    print(f"Wrote {ANON.relative_to(REPO)}/per_paper_flips.csv")
    print(f"Wrote {ANON.relative_to(REPO)}/anonymization_effect.md")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--phase", choices=["pre", "post"], required=True)
    p.add_argument("--per-paper", default=str(VALID / "scoring" / "per_paper_scores.csv"))
    args = p.parse_args()
    if args.phase == "pre":
        write_pre(Path(args.per_paper))
    else:
        write_post(Path(args.per_paper))


if __name__ == "__main__":
    main()
