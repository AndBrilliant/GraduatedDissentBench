#!/usr/bin/env python3
"""
Build human-reviewable audit sheets for RETRACTION-WORTHY findings that did
NOT match a SPOT annotation, per condition.

Many of these "false positives" may be genuine severe errors that SPOT did
not annotate (SPOT lists ONE error per paper; a paper can have more). A
human reviewer who reads each finding can label it:
  VALID  — genuine severe error, SPOT missed it
  RELATED — identifies a real issue but overstates severity
  FALSE  — not a genuine severe error

Adjusted RW-precision = (matched_RW + valid_unmatched_RW) / total_RW.

Inputs (no API calls):
  data/spot/outputs/<sweep>/<paper_id>/<cond>.json    (raw findings)
  data/spot/scoring/<sweep>/judge_traces.jsonl        (SPOT matches)
  data/spot/parsed/spot_parsed_train.parquet          (paper titles + GT)

Outputs:
  analysis/rw_false_positive_audit/audit_sheet_<cond>.md
  analysis/rw_false_positive_audit/audit_sheet_<cond>.csv
  analysis/rw_false_positive_audit/README.md
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "analysis" / "rw_false_positive_audit"

CONDITIONS = [
    # (label, condition_key, sweep, file_base)
    ("GD",   "GD",         "full_run",       "gd"),
    ("B3",   "B3",         "full_run",       "b3"),
    ("B3++", "B3PLUSPLUS", "budget_matched", "b3plusplus"),
]


def load_spot_meta():
    """Returns dict: safe_paper_id -> {title, error_category, error_severity,
    annotation, paper_category}."""
    try:
        import pandas as pd
    except ImportError:
        return {}
    p = REPO / "data" / "spot" / "parsed" / "spot_parsed_train.parquet"
    if not p.exists():
        return {}
    df = pd.read_parquet(p)
    out = {}
    for _, row in df.iterrows():
        safe = row["doi/arxiv_id"].replace("/", "_")
        out[safe] = {
            "title": row["title"],
            "paper_category": row["paper_category"],
            "error_category": row["error_category"],
            "error_location": row["error_location"],
            "error_severity": row["error_severity"],
            "annotation": row["error_annotation"],
        }
    return out


def load_matches(sweep: str, cond_key: str) -> dict[str, set]:
    """Returns {paper_id: set(prediction_index)}"""
    out: dict[str, set] = {}
    path = REPO / "data" / "spot" / "scoring" / sweep / "judge_traces.jsonl"
    with path.open() as f:
        for line in f:
            r = json.loads(line)
            if r["condition"] != cond_key:
                continue
            out[r["paper_id"]] = {m["prediction_index"]
                                   for m in r.get("matches", [])
                                   if isinstance(m.get("prediction_index"), int)}
    return out


def collect_unmatched_rw(cond_key: str, sweep: str, file_base: str,
                          meta: dict) -> list[dict]:
    """Walk all papers; return rows for RW findings that did NOT match."""
    matched_by_paper = load_matches(sweep, cond_key)
    sweep_dir = REPO / "data" / "spot" / "outputs" / sweep
    rows = []
    for pdir in sorted(sweep_dir.iterdir()):
        if not pdir.is_dir():
            continue
        cond_path = pdir / f"{file_base}.json"
        if not cond_path.exists():
            continue
        blob = json.loads(cond_path.read_text())
        matched_idx = matched_by_paper.get(pdir.name, set())
        m = meta.get(pdir.name, {})
        for i, fobj in enumerate(blob.get("findings", []) or []):
            if not isinstance(fobj, dict):
                continue
            if fobj.get("severity") != "RETRACTION-WORTHY":
                continue
            if i in matched_idx:
                continue  # this RW DID match a SPOT annotation
            rows.append({
                "paper_id": pdir.name,
                "paper_title": m.get("title", ""),
                "paper_category": m.get("paper_category", ""),
                "spot_error_category": m.get("error_category", ""),
                "spot_error_severity": m.get("error_severity", ""),
                "spot_annotation": (m.get("annotation") or "").strip(),
                "finding_idx": i,
                "gd_finding_location": (fobj.get("location") or "").strip(),
                "gd_finding": (fobj.get("finding") or fobj.get("description") or "").strip(),
                "arbiter_justification": (fobj.get("justification") or "").strip(),
                "source": fobj.get("source", ""),
                "survived_steelman": fobj.get("survived_steelman", ""),
                "human_verdict": "",   # leave blank for manual entry
                "notes": "",
            })
    return rows


def write_md(label: str, rows: list[dict], matched_count: int,
             total_rw: int, out_path: Path) -> None:
    md = []
    md.append(f"# {label} — RW false-positive audit sheet\n\n")
    md.append(f"**Total RW findings:** {total_rw}  \n")
    md.append(f"**Matched SPOT annotation:** {matched_count}  \n")
    md.append(f"**Unmatched (this audit):** {len(rows)}  \n\n")

    md.append("## Summary (fill in after manual review)\n\n")
    md.append("```\n")
    md.append(f"Total non-matching RW findings: {len(rows)}\n")
    md.append("Valid severe (SPOT missed): ___\n")
    md.append("Related (real but overstated): ___\n")
    md.append("False alarm: ___\n\n")
    md.append(f"Original RW-precision: {matched_count}/{total_rw} = "
              f"{100*matched_count/max(1,total_rw):.1f}%\n")
    md.append(f"Adjusted RW-precision: "
              f"({matched_count} + valid_severe) / {total_rw} = ___%\n")
    md.append("```\n\n")

    md.append("## How to fill in `human_verdict`\n\n")
    md.append("- **VALID**: Reading the finding alongside the paper, this is a "
              "genuine severe methodological error that, if confirmed, would "
              "warrant retraction. SPOT didn't annotate it because SPOT lists "
              "only the single retraction-causing error per paper.\n")
    md.append("- **RELATED**: The finding identifies a real issue, but the "
              "severity rating is too high (should have been MAJOR-REVISION).\n")
    md.append("- **FALSE**: Not a real error, or an error that does not rise "
              "to retraction-worthy severity.\n\n")

    md.append("---\n\n")

    for row in rows:
        title = row["paper_title"] or row["paper_id"]
        md.append(f"### {row['paper_id']} — {title}\n\n")
        md.append(f"- **Paper category:** {row['paper_category']}\n")
        md.append(f"- **SPOT error category:** {row['spot_error_category']} "
                  f"(severity tier: `{row['spot_error_severity']}`)\n")
        md.append(f"- **SPOT annotation (the one annotated error):** "
                  f"{row['spot_annotation']}\n\n")
        md.append(f"- **{label} finding (rated RETRACTION-WORTHY, "
                  f"finding #{row['finding_idx']}):**  \n")
        md.append(f"  Location: {row['gd_finding_location']}  \n")
        md.append(f"  > {row['gd_finding']}\n\n")
        if row['arbiter_justification']:
            md.append(f"- **Arbiter justification for RW classification:**  \n")
            md.append(f"  > {row['arbiter_justification']}\n\n")
        md.append(f"- **Human verdict** (mark one):  \n")
        md.append(f"  - [ ] VALID SEVERE — genuine error, SPOT missed it  \n")
        md.append(f"  - [ ] RELATED — real issue but severity overstated  \n")
        md.append(f"  - [ ] FALSE ALARM — not a genuine severe error  \n\n")
        md.append(f"- **Notes:** _______________________________________________\n\n")
        md.append("---\n\n")

    out_path.write_text("".join(md), encoding="utf-8")


def write_csv(rows: list[dict], out_path: Path) -> None:
    if not rows:
        return
    cols = ["paper_id", "paper_title", "paper_category",
            "spot_error_category", "spot_error_severity", "spot_annotation",
            "finding_idx", "gd_finding_location", "gd_finding",
            "arbiter_justification", "source", "survived_steelman",
            "human_verdict", "notes"]
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in cols})


def count_rw_total(cond_key: str, sweep: str, file_base: str) -> tuple[int, int]:
    """Returns (total_rw, matched_rw)."""
    matched_by_paper = load_matches(sweep, cond_key)
    sweep_dir = REPO / "data" / "spot" / "outputs" / sweep
    total = 0
    matched = 0
    for pdir in sorted(sweep_dir.iterdir()):
        if not pdir.is_dir():
            continue
        cond_path = pdir / f"{file_base}.json"
        if not cond_path.exists():
            continue
        blob = json.loads(cond_path.read_text())
        matched_idx = matched_by_paper.get(pdir.name, set())
        for i, fobj in enumerate(blob.get("findings", []) or []):
            if not isinstance(fobj, dict):
                continue
            if fobj.get("severity") == "RETRACTION-WORTHY":
                total += 1
                if i in matched_idx:
                    matched += 1
    return total, matched


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    meta = load_spot_meta()

    for label, cond_key, sweep, file_base in CONDITIONS:
        total, matched = count_rw_total(cond_key, sweep, file_base)
        rows = collect_unmatched_rw(cond_key, sweep, file_base, meta)
        slug = label.replace("+", "p").replace("/", "_").lower()
        md_path = OUT_DIR / f"audit_sheet_{slug}.md"
        csv_path = OUT_DIR / f"audit_sheet_{slug}.csv"
        write_md(label, rows, matched, total, md_path)
        write_csv(rows, csv_path)
        print(f"{label}: total_RW={total}, matched={matched}, "
              f"unmatched={len(rows)} → {md_path.name}, {csv_path.name}")

    # README
    readme = OUT_DIR / "README.md"
    readme.write_text(_render_readme(), encoding="utf-8")
    print(f"\nwrote {readme}")


def _render_readme() -> str:
    return """# RW false-positive audit

## Purpose

Each condition (GD, B3, B3++) produces many findings classified as
RETRACTION-WORTHY by its arbiter. Only a small number match the SPOT
ground-truth annotation, because SPOT annotates only ONE error per paper —
the one that *caused* the retraction or correction. Papers usually have more
than one severe issue.

The aggregate metric `RW-precision = matched_RW / total_RW` therefore
underestimates the true precision of each condition: it counts as a false
positive any RW finding that SPOT didn't happen to flag.

This audit asks a human reviewer to read each unmatched RW finding and judge:

- **VALID SEVERE** — genuine severe error, SPOT missed it
- **RELATED** — identifies a real issue but the severity is overstated
- **FALSE ALARM** — not a genuine severe error

The adjusted metric is then:

  adjusted_RW_precision = (matched + valid_severe) / total_RW

If GD's adjusted score is meaningfully above B3's and B3++'s, that supports
the paper's calibration claim more cleanly than the raw `matched / total`
metric, which underestimates all conditions equally but may underestimate
GD differently because GD emits fewer, more carefully placed RW flags.

## Files

| File | Purpose |
|---|---|
| `audit_sheet_gd.md` | GD's 68 unmatched RW findings — primary audit |
| `audit_sheet_b3.md` | B3's 91 unmatched RW findings — comparison |
| `audit_sheet_b3pp.md` | B3++'s 105 unmatched RW findings — comparison |
| `audit_sheet_<cond>.csv` | Same content as .md but structured |

Each row contains the paper title, the SPOT-annotated error (for context),
and the model's flagged finding + arbiter justification. The reviewer fills
in `human_verdict` and `notes` columns.

## Procedure

1. Read each finding alongside the SPOT annotation (which is the
   retraction/errata cause for that paper).
2. Decide whether the finding is:
   - a genuine severe error that, if confirmed, would warrant retraction
     (VALID),
   - a real but lower-severity issue rated too high (RELATED),
   - not a real severe error (FALSE).
3. Optionally consult the original paper if needed; SPOT papers are
   identified by DOI/arXiv ID and the paper category is included.
4. Fill in the `human_verdict` column.
5. Aggregate: count VALID per condition, compute adjusted RW-precision.

## What we're looking for

If GD's VALID count is ≥ B3's or B3++'s VALID counts as a fraction of its
unmatched RW pool, that's evidence the steelman exchange is selecting for
real severe errors at a higher rate than alternative reflection protocols.

If GD's VALID rate ≈ B3 / B3++'s, the calibration advantage was real but is
not larger than what the raw `matched / total` metric showed (so the
contribution remains the small 2× point estimate we already have).

If GD's VALID rate is *lower* than alternatives, GD is fewer-but-not-better
in the unmatched pool — the raw metric was if anything overstating GD's
advantage. (Unlikely but the audit will reveal it.)

## Reviewer guidance

- Be strict on VALID. "Could be a problem" is RELATED; "fundamentally
  invalidates central conclusions" is VALID.
- Match the SPOT severity tier rubric (RW = fundamentally broken; MR =
  serious but addressable).
- It's fine to mark items as RELATED if you're unsure — the conservative
  read for GD's purposes.
- Time per finding: aim for 2-5 minutes. The full GD audit (68 items)
  should take ~3-5 hours.
"""


if __name__ == "__main__":
    main()
