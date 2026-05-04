#!/usr/bin/env python3
"""
Aggregate the multi-model audit on the retracted-paper benchmark into the
table the paper expects, plus a report listing disagreement cases.

Reads validation/retracted_paper_audit/raw_responses.jsonl AND any
raw_responses_opus_fillin.jsonl that exists; merges them so Opus
budget-failed calls are replaced with the fill-in vote. Then re-derives
per-finding and per-paper rows from the merged responses, applies the
keyword-based first-author scoring, and produces:
  - per_paper_merged.csv  — paper-level outcomes under each regime
  - aggregate_table.md    — the four-row scoring-regime comparison
  - aggregate_table.csv
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
import pandas as pd

REPO = Path(__file__).resolve().parent.parent
AUDIT = REPO / "validation" / "retracted_paper_audit"
GT_CSV = REPO / "github" / "data" / "ground_truth.csv"
OUT_RAW = REPO / "github" / "outputs" / "raw"
COND_DIRS = {
    "B1": "baseline_B1", "B2": "baseline_B2",
    "B3": "baseline_B3", "GD": "graduated_dissent",
}


def load_ground_truth():
    gt = {}
    with GT_CSV.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            gt[row["paper_id"]] = row
    return gt


def load_findings(paper_id, condition):
    cond_dir = OUT_RAW / COND_DIRS[condition]
    matches = list(cond_dir.glob(f"{paper_id}_*.json"))
    if not matches:
        return []
    blob = json.loads(matches[0].read_text(encoding="utf-8"))
    return blob.get("findings", []) or []


def vote_extract(rec, model):
    """Return (match_or_severity_value, parse_error_bool) for a model in this batch."""
    for resp in rec.get("responses", []):
        if resp.get("model") != model:
            continue
        ans = resp.get("response", {})
        if not isinstance(ans, dict):
            return None, True
        if "error" in ans:
            return None, True
        if rec.get("event") == "match":
            return bool(ans.get("match", False)), bool(ans.get("parse_error", False))
        elif rec.get("event") == "severity":
            return ans.get("severity", "?"), bool(ans.get("parse_error", False))
    return None, True


def merge_opus_fillin(primary, fillin):
    """Build merged_records[(pid, cond, fi, event)] = {primary_responses + opus_override}."""
    merged = {}
    for rec in primary:
        key = (rec["paper_id"], rec["condition"], rec["finding_idx"], rec["event"])
        merged[key] = {
            "paper_id": rec["paper_id"],
            "condition": rec["condition"],
            "finding_idx": rec["finding_idx"],
            "event": rec["event"],
            "responses": list(rec.get("responses", [])),
        }
    # Replace Opus response with fill-in if present
    for rec in fillin:
        key = (rec["paper_id"], rec["condition"], rec["finding_idx"], rec["event"])
        if key not in merged:
            merged[key] = {
                "paper_id": rec["paper_id"],
                "condition": rec["condition"],
                "finding_idx": rec["finding_idx"],
                "event": rec["event"],
                "responses": list(rec.get("responses", [])),
            }
            continue
        # Replace any opus response in the merged record
        new_responses = [r for r in merged[key]["responses"] if r.get("model") != "opus"]
        for r in rec.get("responses", []):
            if r.get("model") == "opus":
                new_responses.append(r)
        merged[key]["responses"] = new_responses
    return merged


def main():
    primary_path = AUDIT / "raw_responses.jsonl"
    fillin_path = AUDIT / "raw_responses_opus_fillin.jsonl"
    primary = [json.loads(l) for l in primary_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    fillin = []
    if fillin_path.exists():
        fillin = [json.loads(l) for l in fillin_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    print(f"primary records: {len(primary)} | fill-in records: {len(fillin)}")
    merged = merge_opus_fillin(primary, fillin)
    print(f"merged records: {len(merged)}")

    gt = load_ground_truth()
    # First-author keyword matching (replicate the original scoring)
    def kw_match_per_paper(pid, findings):
        kw_csv = gt.get(pid, {}).get("keyword_groups", "")
        if not kw_csv or kw_csv == "N/A":
            return False
        groups = []
        for grp in kw_csv.split("|"):
            grp = grp.strip()
            if grp:
                groups.append([k.strip().lower() for k in grp.split("+") if k.strip()])
        for f in findings:
            if not isinstance(f, dict):
                continue
            text = (f.get("finding", "") or f.get("description", "") or "").lower()
            if any(all(k in text for k in g) for g in groups):
                return True
        return False

    # Per-paper-condition assembly
    pp_rows = []
    paper_conds = sorted({(rec["paper_id"], rec["condition"]) for rec in merged.values()})
    for pid, cond in paper_conds:
        is_retracted = gt.get(pid, {}).get("category") == "retracted"
        is_control = gt.get(pid, {}).get("category") in ("matched_control", "hard_negative")
        if not is_retracted and not is_control:
            continue
        findings = load_findings(pid, cond)
        n_findings = len(findings)
        first_author_match = kw_match_per_paper(pid, findings) if is_retracted else False
        first_author_RW = any(
            isinstance(f, dict) and f.get("severity") == "RETRACTION-WORTHY"
            for f in findings
        )

        # Walk match events for this paper×condition
        any_majority = False
        any_unanimous = False
        any_RW_maj = False
        any_RW_unan = False
        # Track per-model votes for disagreement reporting
        model_votes_match = {"gpt-5.4": [], "opus": [], "deepseek": []}
        for fi in range(n_findings):
            mkey = (pid, cond, fi, "match")
            if mkey not in merged:
                continue
            rec = merged[mkey]
            votes = []
            for m in ("gpt-5.4", "opus", "deepseek"):
                v, _ = vote_extract(rec, m)
                votes.append(v)
                model_votes_match[m].append(v if v is not None else False)
            valid = [v for v in votes if v is not None]
            true_count = sum(1 for v in valid if v is True)
            if true_count >= 2:
                any_majority = True
            if len(valid) >= 3 and true_count == 3:
                any_unanimous = True

            # Severity event (only fires when majority match was True at run time)
            skey = (pid, cond, fi, "severity")
            if skey in merged:
                srec = merged[skey]
                sev_votes = []
                for m in ("gpt-5.4", "opus", "deepseek"):
                    v, _ = vote_extract(srec, m)
                    sev_votes.append(v)
                rw_count = sum(1 for v in sev_votes if v == "RETRACTION-WORTHY")
                if rw_count >= 2:
                    any_RW_maj = True
                if len(sev_votes) >= 3 and all(v == "RETRACTION-WORTHY" for v in sev_votes if v is not None):
                    if sum(1 for v in sev_votes if v is not None) == 3 and rw_count == 3:
                        any_RW_unan = True

        pp_rows.append({
            "paper_id": pid,
            "condition": cond,
            "is_retracted": is_retracted,
            "is_control": is_control,
            "n_findings": n_findings,
            "first_author_match": first_author_match,
            "first_author_RW_present": first_author_RW,
            "audit_match_majority": any_majority,
            "audit_match_unanimous": any_unanimous,
            "audit_RW_majority": any_RW_maj,
            "audit_RW_unanimous": any_RW_unan,
        })
    pp = pd.DataFrame(pp_rows)
    pp.to_csv(AUDIT / "per_paper_merged.csv", index=False)
    print(f"Wrote {AUDIT / 'per_paper_merged.csv'} ({len(pp)} rows)")

    retracted = pp[pp["is_retracted"] == True].copy()
    controls = pp[pp.get("is_control", ~pp["is_retracted"]) == True].copy() if "is_control" in pp.columns else pp[pp["is_retracted"] == False].copy()

    n_retracted = retracted["paper_id"].nunique()
    n_controls = controls["paper_id"].nunique()

    rows = []
    for cond in ("B1", "B2", "B3", "GD"):
        r = retracted[retracted["condition"] == cond]
        c = controls[controls["condition"] == cond]
        # Detection on retracted papers (regime-by-regime)
        det_first = r["first_author_match"].astype(bool).sum()
        det_maj = r["audit_match_majority"].astype(bool).sum()
        det_unan = r["audit_match_unanimous"].astype(bool).sum()
        # FP on probative controls (regime-by-regime)
        fp_first = c["first_author_RW_present"].astype(bool).sum()
        fp_maj = c["audit_RW_majority"].astype(bool).sum()
        fp_unan = c["audit_RW_unanimous"].astype(bool).sum()
        rows.append({
            "condition": cond,
            "n_retracted": n_retracted,
            "n_controls": n_controls,
            "det_first_author": int(det_first),
            "det_audit_majority": int(det_maj),
            "det_audit_unanimous": int(det_unan),
            "fp_first_author": int(fp_first),
            "fp_audit_majority": int(fp_maj),
            "fp_audit_unanimous": int(fp_unan),
        })
    table = pd.DataFrame(rows)

    # The paper's table format (B3 + GD focus)
    def pct(x: int, n: int) -> str:
        return f"{(100*x/n):.0f}%" if n else "-"

    md = ["# Retracted-paper benchmark — multi-model rescoring", ""]
    md.append("## Comparison table (B3 vs GD)")
    md.append("")
    md.append("| Scoring regime | B3 det. | GD det. | B3 FP | GD FP |")
    md.append("|---|---:|---:|---:|---:|")
    b3 = table[table["condition"] == "B3"].iloc[0]
    gd = table[table["condition"] == "GD"].iloc[0]
    md.append(f"| First-author scoring | {pct(b3['det_first_author'], n_retracted)} ({b3['det_first_author']}/{n_retracted}) | {pct(gd['det_first_author'], n_retracted)} ({gd['det_first_author']}/{n_retracted}) | {pct(b3['fp_first_author'], n_controls)} ({b3['fp_first_author']}/{n_controls}) | {pct(gd['fp_first_author'], n_controls)} ({gd['fp_first_author']}/{n_controls}) |")
    md.append(f"| Majority audit (2/3) | {pct(b3['det_audit_majority'], n_retracted)} ({b3['det_audit_majority']}/{n_retracted}) | {pct(gd['det_audit_majority'], n_retracted)} ({gd['det_audit_majority']}/{n_retracted}) | {pct(b3['fp_audit_majority'], n_controls)} ({b3['fp_audit_majority']}/{n_controls}) | {pct(gd['fp_audit_majority'], n_controls)} ({gd['fp_audit_majority']}/{n_controls}) |")
    md.append(f"| Unanimous strict (3/3) | {pct(b3['det_audit_unanimous'], n_retracted)} ({b3['det_audit_unanimous']}/{n_retracted}) | {pct(gd['det_audit_unanimous'], n_retracted)} ({gd['det_audit_unanimous']}/{n_retracted}) | {pct(b3['fp_audit_unanimous'], n_controls)} ({b3['fp_audit_unanimous']}/{n_controls}) | {pct(gd['fp_audit_unanimous'], n_controls)} ({gd['fp_audit_unanimous']}/{n_controls}) |")
    md.append("")
    md.append("## All conditions")
    md.append("")
    md.append("| Condition | First-author det. | Majority det. | Unanimous det. | First-author FP | Majority FP | Unanimous FP |")
    md.append("|---|---:|---:|---:|---:|---:|---:|")
    for _, r in table.iterrows():
        md.append(
            f"| {r['condition']} | "
            f"{pct(r['det_first_author'], n_retracted)} | "
            f"{pct(r['det_audit_majority'], n_retracted)} | "
            f"{pct(r['det_audit_unanimous'], n_retracted)} | "
            f"{pct(r['fp_first_author'], n_controls)} | "
            f"{pct(r['fp_audit_majority'], n_controls)} | "
            f"{pct(r['fp_audit_unanimous'], n_controls)} |"
        )
    md.append("")

    # Disagreements: per-paper-per-condition cells where first-author and
    # majority audit differ
    dis = []
    for cond in ("B1", "B2", "B3", "GD"):
        sub = pp[pp["condition"] == cond]
        for _, row in sub.iterrows():
            cat = "retracted" if row["is_retracted"] else "control"
            if row["is_retracted"]:
                fa = bool(row["first_author_match"])
                ma = bool(row["audit_match_majority"])
                if fa != ma:
                    dis.append({
                        "paper_id": row["paper_id"],
                        "category": cat,
                        "condition": cond,
                        "metric": "detection",
                        "first_author": fa,
                        "audit_majority": ma,
                    })
            else:
                fa = bool(row["first_author_RW_present"])
                ma = bool(row["audit_RW_majority"])
                if fa != ma:
                    dis.append({
                        "paper_id": row["paper_id"],
                        "category": cat,
                        "condition": cond,
                        "metric": "false_positive",
                        "first_author": fa,
                        "audit_majority": ma,
                    })
    dis_md = ["", "## Disagreements (first-author vs majority audit)", ""]
    if dis:
        dis_md.append("| Paper | Category | Cond | Metric | First-author | Majority audit |")
        dis_md.append("|---|---|---|---|---|---|")
        for d in dis:
            dis_md.append(
                f"| {d['paper_id']} | {d['category']} | {d['condition']} | "
                f"{d['metric']} | {d['first_author']} | {d['audit_majority']} |"
            )
    else:
        dis_md.append("(no disagreements between first-author and majority audit)")
    md.extend(dis_md)
    md.append("")

    (AUDIT / "aggregate_table.md").write_text("\n".join(md), encoding="utf-8")
    table.to_csv(AUDIT / "aggregate_table.csv", index=False)

    print(f"Wrote {(AUDIT / 'aggregate_table.md').resolve()}")
    print(f"Wrote {(AUDIT / 'aggregate_table.csv').resolve()}")
    print()
    print("=== Headline B3 vs GD comparison ===")
    print(f"  retracted papers: n={n_retracted}; controls: n={n_controls}")
    print(f"  First-author:           B3 det {b3['det_first_author']}/{n_retracted}, GD det {gd['det_first_author']}/{n_retracted}; B3 FP {b3['fp_first_author']}/{n_controls}, GD FP {gd['fp_first_author']}/{n_controls}")
    print(f"  Majority audit (2/3):   B3 det {b3['det_audit_majority']}/{n_retracted}, GD det {gd['det_audit_majority']}/{n_retracted}; B3 FP {b3['fp_audit_majority']}/{n_controls}, GD FP {gd['fp_audit_majority']}/{n_controls}")
    print(f"  Unanimous strict (3/3): B3 det {b3['det_audit_unanimous']}/{n_retracted}, GD det {gd['det_audit_unanimous']}/{n_retracted}; B3 FP {b3['fp_audit_unanimous']}/{n_controls}, GD FP {gd['fp_audit_unanimous']}/{n_controls}")


if __name__ == "__main__":
    main()
