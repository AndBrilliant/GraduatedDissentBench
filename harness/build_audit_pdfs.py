#!/usr/bin/env python3
"""
Convert the markdown audit sheets to PDFs with a clear instructions cover.

For each of GD / B3 / B3++ audit sheets, produce a PDF with:
  1. Cover page with reviewer instructions
  2. The audit content rendered cleanly with one finding per entry
  3. Print-friendly styling

The user reads the PDF in Preview, then enters their verdicts in the
.csv file (which the audit_sheet_<cond>.csv already has prepared with
empty `human_verdict` and `notes` columns).
"""
from __future__ import annotations

import sys
from pathlib import Path

import markdown
import weasyprint

REPO = Path(__file__).resolve().parent.parent
AUDIT_DIR = REPO / "analysis" / "rw_false_positive_audit"

INSTRUCTIONS_HTML = """
<div class="cover">
  <h1>RW False-Positive Audit — {cond} condition</h1>
  <p class="subtitle">{n_findings} findings to review · {n_papers} papers</p>

  <div class="box">
    <h2>What you're doing</h2>
    <p>SPOT annotates exactly <em>one</em> error per paper — the one that
    caused the retraction or correction. But papers usually have more than
    one severe issue.</p>
    <p>The aggregate metric "RW-precision = matched / total" counts every
    RW finding outside the single SPOT annotation as a false positive.
    Some of those are <strong>genuine severe errors that SPOT just didn't
    annotate</strong>. This audit identifies them.</p>
  </div>

  <h2>For each finding, choose one verdict:</h2>
  <ul class="verdicts">
    <li><strong>VALID SEVERE</strong> — genuine severe methodological
    error that, if confirmed, would warrant retraction. The arbiter's
    RW classification is correct; SPOT just didn't annotate this one.</li>

    <li><strong>RELATED</strong> — the finding identifies a real issue,
    but the severity rating is too high. Should have been MAJOR-REVISION.
    Use this when you're uncertain — it's the conservative choice.</li>

    <li><strong>FALSE ALARM</strong> — not a genuine severe error, or
    the model misread the paper.</li>
  </ul>

  <div class="box warn">
    <h2>Calibration guidance</h2>
    <ul>
      <li><strong>VALID</strong> means: <em>"if true, this paper should
      be retracted, independent of SPOT's annotation."</em> Be strict.</li>
      <li>If you can't verify the technical claim (math proof, materials
      chemistry, specific theorem), mark <strong>RELATED</strong> rather
      than guessing.</li>
      <li>The SPOT-annotated error is shown above each finding for
      context only — it is NOT the standard. The standard is whether
      <em>this specific finding</em> describes a retraction-worthy
      error in the paper.</li>
    </ul>
  </div>

  <h2>How to record your verdict</h2>
  <p>This PDF is read-only. After reading each finding here, open the
  matching CSV file in a spreadsheet (Excel, Numbers, or VS Code) and
  fill in the <code>human_verdict</code> and <code>notes</code> columns:</p>
  <p class="code">analysis/rw_false_positive_audit/audit_sheet_{slug}.csv</p>

  <p>Use exactly <code>VALID</code>, <code>RELATED</code>, or
  <code>FALSE</code> in the <code>human_verdict</code> column.</p>

  <h2>Time estimate</h2>
  <p>2–5 minutes per finding. Full audit ≈ {time_lo}–{time_hi} hours.
  You can stop and resume — the CSV holds your progress.</p>

  <h2>What we're looking for</h2>
  <p>Whether GD has a higher rate of VALID findings (among its unmatched
  RW pool) than B3 or B3++. If yes, the steelman exchange is selecting
  for real severe errors at a higher rate than alternative reflection
  protocols — and the original RW-precision metric was understating GD's
  advantage.</p>

  <p class="footnote">If the rates are similar, the calibration advantage
  is exactly as the aggregate metric showed (2× directional, not
  significant at this n). If GD's rate is lower, the aggregate metric
  was overstating GD. The honest answer is whatever the data says.</p>
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
.cover h1 {
  font-size: 22pt;
  margin: 0 0 4pt;
  color: #1a1a1a;
}
.cover .subtitle {
  font-size: 11pt;
  color: #666;
  margin: 0 0 18pt;
}
.cover h2 {
  font-size: 13pt;
  margin: 16pt 0 6pt;
  border-bottom: 1px solid #999;
  padding-bottom: 2pt;
}
.cover p { margin: 4pt 0; }
.cover ul.verdicts li {
  margin: 6pt 0;
  padding-left: 6pt;
}
.box {
  background: #f4f4f4;
  border-left: 3px solid #888;
  padding: 8pt 12pt;
  margin: 12pt 0;
  page-break-inside: avoid;
}
.box h2 { border-bottom: none; margin-top: 0; }
.box.warn { background: #fff7e6; border-left-color: #c80; }
p.code, code {
  font-family: "SF Mono", Menlo, monospace;
  font-size: 9pt;
}
p.code {
  background: #eaeaea;
  padding: 4pt 6pt;
  border-radius: 3pt;
}
.footnote { font-size: 9pt; color: #666; font-style: italic; }
.pagebreak { page-break-after: always; }

h1, h2, h3 {
  font-family: -apple-system, BlinkMacSystemFont, sans-serif;
}
h1 { font-size: 16pt; margin: 18pt 0 6pt; }
h2 { font-size: 12pt; margin: 14pt 0 4pt; color: #333; }
h3 {
  font-size: 11pt; margin: 14pt 0 4pt;
  background: #e0e0ec; padding: 4pt 6pt; border-left: 3px solid #557;
  page-break-after: avoid;
}
hr {
  border: 0;
  border-top: 1px dashed #bbb;
  margin: 10pt 0;
}
blockquote {
  margin: 4pt 0 4pt 6pt;
  padding: 4pt 8pt;
  border-left: 2px solid #99a;
  background: #f7f7fb;
  font-size: 9.5pt;
  page-break-inside: avoid;
}
ul, ol { margin: 4pt 0 4pt 18pt; }
li { margin: 2pt 0; }
.finding-block { page-break-inside: avoid; }
"""


def md_to_finding_html(md_text: str) -> str:
    """Convert the audit markdown to HTML, then wrap each finding entry in
    a 'finding-block' div to encourage page-break-inside: avoid."""
    # Strip the top header sections (we replace with our cover)
    # The first '### ' heading marks the start of finding entries.
    cut_idx = md_text.find("\n### ")
    if cut_idx > 0:
        md_text = md_text[cut_idx + 1:]
    html = markdown.markdown(md_text, extensions=["extra", "sane_lists"])
    # Wrap each finding entry: split on <h3 ...> markers
    parts = html.split("<h3>")
    if len(parts) <= 1:
        return html
    wrapped = parts[0]  # any preamble
    for chunk in parts[1:]:
        wrapped += '<div class="finding-block"><h3>' + chunk + "</div>"
    return wrapped


def build_one(cond_label: str, slug: str) -> Path:
    md_path = AUDIT_DIR / f"audit_sheet_{slug}.md"
    csv_path = AUDIT_DIR / f"audit_sheet_{slug}.csv"
    out_path = AUDIT_DIR / f"audit_sheet_{slug}.pdf"
    md_text = md_path.read_text(encoding="utf-8")

    # Pull counts from the markdown for the cover
    n_findings = md_text.count("\n### ")
    # Count distinct papers
    import re
    paper_ids = set(re.findall(r"### (\S+) —", md_text))
    n_papers = len(paper_ids)
    time_lo = n_findings * 2 // 60
    time_hi = n_findings * 5 // 60

    cover_html = INSTRUCTIONS_HTML.format(
        cond=cond_label, n_findings=n_findings, n_papers=n_papers,
        slug=slug, time_lo=time_lo, time_hi=time_hi,
    )
    body_html = md_to_finding_html(md_text)

    full = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>{CSS}</style></head><body>
{cover_html}
{body_html}
</body></html>"""

    weasyprint.HTML(string=full, base_url=str(AUDIT_DIR)).write_pdf(str(out_path))
    return out_path


def main():
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    pdfs = []
    for label, slug in [("GD", "gd"), ("B3", "b3"), ("B3++", "b3pp")]:
        p = build_one(label, slug)
        print(f"  wrote {p}  ({p.stat().st_size//1024} KB)")
        pdfs.append(p)
    print()
    for p in pdfs:
        print(p)


if __name__ == "__main__":
    sys.exit(main() or 0)
