#!/usr/bin/env python3
"""
Build a BLINDED, shuffled audit sheet pooling all unmatched RW findings
across GD / B3 / B3++ into one stream. The reviewer does not see which
condition produced which finding, and the cover page does not telegraph
what the experiment is testing.

Outputs:
  analysis/rw_false_positive_audit/blinded/audit_blinded.{md,csv,pdf}
  analysis/rw_false_positive_audit/blinded/decoding_key.csv  (DO NOT OPEN
    until you finish auditing — maps finding_id -> condition)

The decoding key is kept in the same directory but in a separate file so
the reviewer can keep it closed during the audit.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import markdown
import weasyprint

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "analysis" / "rw_false_positive_audit" / "blinded"

SOURCES = [
    ("audit_sheet_gd.csv", "GD"),
    ("audit_sheet_b3.csv", "B3"),
    ("audit_sheet_b3pp.csv", "B3PP"),
]


def stable_shuffle_key(paper_id: str, finding_idx: str, condition: str) -> str:
    """Deterministic, reproducible per-entry sort key. Salt prevents
    accidental ordering correlation with paper_id alphabetical."""
    raw = f"BLIND:{paper_id}::{finding_idx}::{condition}".encode()
    return hashlib.sha256(raw).hexdigest()


def load_all_findings() -> list[dict]:
    audit_dir = REPO / "analysis" / "rw_false_positive_audit"
    rows = []
    for filename, cond in SOURCES:
        with (audit_dir / filename).open() as f:
            for r in csv.DictReader(f):
                rows.append({
                    "_condition": cond,        # decoder-only
                    "_paper_id": r["paper_id"],
                    "_finding_idx": r["finding_idx"],
                    "paper_title": r["paper_title"],
                    "paper_category": r["paper_category"],
                    "spot_error_category": r["spot_error_category"],
                    "spot_error_severity": r["spot_error_severity"],
                    "spot_annotation": r["spot_annotation"],
                    "finding_location": r["gd_finding_location"],
                    "finding": r["gd_finding"],
                    "arbiter_justification": r["arbiter_justification"],
                })
    rows.sort(key=lambda r: stable_shuffle_key(r["_paper_id"],
                                                  r["_finding_idx"],
                                                  r["_condition"]))
    # Assign blinded IDs in shuffled order
    for i, r in enumerate(rows, start=1):
        r["finding_id"] = f"F{i:03d}"
    return rows


COVER_HTML = """
<div class="cover">
  <h1>Blinded peer-review audit</h1>
  <p class="subtitle">{n} candidate findings to evaluate</p>

  <div class="box">
    <h2>Task</h2>
    <p>Below are {n} machine-generated review findings, each labelled
    <em>retraction-worthy</em> by an automated reviewer. Each is paired
    with the SPOT benchmark's documented retraction/correction cause for
    the same paper (shown for context only — it is NOT the standard for
    judging this finding).</p>
    <p>For each finding, judge:</p>
    <ul>
      <li><strong>VALID</strong> — if this finding's claim were true,
      it would warrant retraction of the paper.</li>
      <li><strong>RELATED</strong> — the finding identifies a real
      methodological issue, but the severity rating is too high. Should
      have been MAJOR-REVISION.</li>
      <li><strong>FALSE</strong> — the finding does not describe a real
      severe error (misreads the paper, generic complaint, routine
      limitation framed as catastrophic, etc).</li>
    </ul>
  </div>

  <div class="box warn">
    <h2>Calibration</h2>
    <ul>
      <li>Be strict on VALID. "Could be a problem" is RELATED; only
      mark VALID when the described error, if confirmed, plainly
      invalidates the paper's central conclusions.</li>
      <li>If you cannot independently verify a technical claim (math
      proof, materials chemistry, specific theorem), default to
      RELATED rather than guessing.</li>
      <li>The SPOT annotation shown for each paper is ONE annotated
      error per paper. A finding being different from the SPOT
      annotation does not make it wrong — papers have multiple
      issues.</li>
      <li>Findings are presented in randomized order. No two consecutive
      entries are necessarily from the same paper.</li>
    </ul>
  </div>

  <h2>Recording verdicts</h2>
  <p>This PDF is read-only. Record your judgments in the CSV file:</p>
  <p class="code">analysis/rw_false_positive_audit/blinded/audit_blinded.csv</p>
  <p>Use exactly <code>VALID</code>, <code>RELATED</code>, or
  <code>FALSE</code> in the <code>verdict</code> column. The
  <code>notes</code> column is for free-form comments.</p>

  <h2>Time</h2>
  <p>Aim for 1–3 minutes per finding. The full audit is ≈ {hours_lo}–{hours_hi}
  hours. You can stop and resume — the CSV holds your progress.</p>

  <p class="footnote">Findings are referenced by opaque IDs (F001, F002, …).
  The mapping from each ID to its source condition is in a separate file
  (<code>decoding_key.csv</code>) that should remain closed until you
  finish auditing.</p>
</div>
<div class="pagebreak"></div>
"""

CSS = """
@page {
  size: Letter;
  margin: 0.75in 0.85in 0.9in 0.85in;
  @bottom-center {
    content: "Page " counter(page) " of " counter(pages);
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 8pt;
    color: #777;
  }
}
body {
  font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
  font-size: 10pt;
  line-height: 1.35;
  color: #222;
}
.cover h1 { font-size: 22pt; margin: 0 0 4pt; }
.cover .subtitle { font-size: 11pt; color: #666; margin: 0 0 18pt; }
.cover h2 { font-size: 13pt; margin: 16pt 0 6pt;
  border-bottom: 1px solid #999; padding-bottom: 2pt; }
.box { background: #f4f4f4; border-left: 3px solid #888;
  padding: 8pt 12pt; margin: 12pt 0; page-break-inside: avoid; }
.box h2 { border-bottom: none; margin-top: 0; }
.box.warn { background: #fff7e6; border-left-color: #c80; }
p.code, code { font-family: "SF Mono", Menlo, monospace; font-size: 9pt; }
p.code { background: #eaeaea; padding: 4pt 6pt; border-radius: 3pt; }
.footnote { font-size: 9pt; color: #666; font-style: italic; }
.pagebreak { page-break-after: always; }
h1, h2, h3 { font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
h3 { font-size: 11pt; margin: 14pt 0 4pt;
  background: #e0e0ec; padding: 4pt 6pt; border-left: 3px solid #557;
  page-break-after: avoid; }
hr { border: 0; border-top: 1px dashed #bbb; margin: 10pt 0; }
blockquote { margin: 4pt 0 4pt 6pt; padding: 4pt 8pt;
  border-left: 2px solid #99a; background: #f7f7fb;
  font-size: 9.5pt; page-break-inside: avoid; }
.finding-block { page-break-inside: avoid; }
.meta { color: #555; font-size: 9pt; }
.verdict-line { font-size: 9.5pt; margin-top: 4pt;
  border-top: 1px dotted #ccc; padding-top: 3pt; }
"""


def render_finding_html(row: dict) -> str:
    paper_title = (row["paper_title"] or row["_paper_id"])
    paper_title_esc = paper_title.replace("&", "&amp;").replace("<", "&lt;")
    spot_ann = (row["spot_annotation"] or "").replace("&", "&amp;").replace("<", "&lt;")
    finding = (row["finding"] or "").replace("&", "&amp;").replace("<", "&lt;")
    arbiter = (row["arbiter_justification"] or "").replace("&", "&amp;").replace("<", "&lt;")
    loc = (row["finding_location"] or "").strip()
    loc_html = f"  <em>Location:</em> {loc}<br>" if loc else ""

    return f"""
<div class="finding-block">
<h3>{row['finding_id']}</h3>
<p class="meta">Paper: <em>{paper_title_esc}</em>
  &nbsp;·&nbsp; Field: {row['paper_category'] or '—'}
  &nbsp;·&nbsp; SPOT severity tier: <code>{row['spot_error_severity']}</code>
</p>

<p><strong>SPOT-annotated error in this paper (context only):</strong></p>
<blockquote>{spot_ann}</blockquote>

<p><strong>Candidate finding (rated retraction-worthy):</strong></p>
{loc_html}
<blockquote>{finding}</blockquote>

<p><strong>Arbiter's justification for the retraction-worthy rating:</strong></p>
<blockquote>{arbiter}</blockquote>

<p class="verdict-line">
  Verdict (record in audit_blinded.csv):
  &nbsp;&nbsp;[ ] VALID &nbsp;&nbsp;[ ] RELATED &nbsp;&nbsp;[ ] FALSE
</p>
</div>
<hr>
"""


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = load_all_findings()
    n = len(rows)
    hours_lo = n * 1 // 60
    hours_hi = n * 3 // 60

    # --- Decoding key (kept separate) ---
    dec_path = OUT_DIR / "decoding_key.csv"
    with dec_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=[
            "finding_id", "condition", "paper_id", "finding_idx",
            "paper_title",
        ])
        w.writeheader()
        for r in rows:
            w.writerow({
                "finding_id": r["finding_id"],
                "condition": r["_condition"],
                "paper_id": r["_paper_id"],
                "finding_idx": r["_finding_idx"],
                "paper_title": r["paper_title"],
            })
    print(f"  decoding key: {dec_path}")

    # --- Blinded CSV for entering verdicts ---
    csv_path = OUT_DIR / "audit_blinded.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=[
            "finding_id", "paper_title", "paper_category",
            "spot_error_severity", "spot_annotation",
            "finding_location", "finding", "arbiter_justification",
            "verdict", "notes",
        ])
        w.writeheader()
        for r in rows:
            w.writerow({
                "finding_id": r["finding_id"],
                "paper_title": r["paper_title"],
                "paper_category": r["paper_category"],
                "spot_error_severity": r["spot_error_severity"],
                "spot_annotation": r["spot_annotation"],
                "finding_location": r["finding_location"],
                "finding": r["finding"],
                "arbiter_justification": r["arbiter_justification"],
                "verdict": "",
                "notes": "",
            })
    print(f"  blinded csv:  {csv_path}")

    # --- Blinded markdown (and PDF via weasyprint) ---
    md_path = OUT_DIR / "audit_blinded.md"
    md_lines = ["# Blinded peer-review audit\n\n",
                 f"{n} candidate findings, randomly shuffled.\n\n",
                 "See the cover page of the PDF for instructions, or the "
                 "README for context. Record verdicts in "
                 "`audit_blinded.csv`.\n\n", "---\n\n"]
    for r in rows:
        md_lines.append(f"### {r['finding_id']}\n\n")
        md_lines.append(f"- Paper: *{r['paper_title']}*\n")
        md_lines.append(f"- Field: {r['paper_category']}\n")
        md_lines.append(f"- SPOT severity tier: `{r['spot_error_severity']}`\n\n")
        md_lines.append(f"**SPOT-annotated error in this paper (context only):**\n")
        md_lines.append(f"> {r['spot_annotation']}\n\n")
        md_lines.append(f"**Candidate finding (rated retraction-worthy):**\n")
        if r["finding_location"]:
            md_lines.append(f"*Location: {r['finding_location']}*\n\n")
        md_lines.append(f"> {r['finding']}\n\n")
        md_lines.append(f"**Arbiter's justification:**\n")
        md_lines.append(f"> {r['arbiter_justification']}\n\n")
        md_lines.append("Verdict (record in `audit_blinded.csv`): "
                         "[ ] VALID  [ ] RELATED  [ ] FALSE\n\n")
        md_lines.append("---\n\n")
    md_path.write_text("".join(md_lines), encoding="utf-8")
    print(f"  blinded md:   {md_path}")

    # PDF
    pdf_path = OUT_DIR / "audit_blinded.pdf"
    cover = COVER_HTML.format(n=n, hours_lo=hours_lo, hours_hi=hours_hi)
    body_html = "".join(render_finding_html(r) for r in rows)
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>{CSS}</style></head><body>{cover}{body_html}</body></html>"""
    weasyprint.HTML(string=html, base_url=str(OUT_DIR)).write_pdf(str(pdf_path))
    print(f"  blinded pdf:  {pdf_path}  ({pdf_path.stat().st_size//1024} KB)")

    # README
    (OUT_DIR / "README.md").write_text(_render_readme(n), encoding="utf-8")
    print(f"  README:       {OUT_DIR / 'README.md'}")


def _render_readme(n: int) -> str:
    return f"""# Blinded RW false-positive audit

This directory contains a single audit sheet pooling all {n} unmatched
retraction-worthy findings across the three conditions (GD, B3, B3++).
Findings are shuffled by a deterministic hash so neither the reviewer
nor the order can reveal which condition produced which finding.

## Files

- `audit_blinded.pdf` — print-ready, randomized order, with cover-page
  instructions. Read this to do the audit.
- `audit_blinded.md` — same content, markdown form.
- `audit_blinded.csv` — for recording verdicts (`verdict` and `notes`
  columns blank). Open in a spreadsheet.
- `decoding_key.csv` — maps each `finding_id` to its source condition
  (GD / B3 / B3PP) and paper. **Do not open until you finish auditing.**

## Procedure

1. Read each finding in `audit_blinded.pdf`.
2. Decide VALID / RELATED / FALSE per the cover page instructions.
3. Record verdicts in `audit_blinded.csv`.
4. When done, run `python harness/decode_blinded_audit.py` to compute
   per-condition statistics (it joins the verdicts CSV with the
   decoding key).

## What this controls for

The per-condition audit sheets (`audit_sheet_{{gd,b3,b3pp}}.{{md,pdf}}`)
explicitly told the reviewer which condition produced each finding and
which condition was hoped to "win." That biases verdicts. This blinded
sheet removes both signals.
"""


if __name__ == "__main__":
    main()
