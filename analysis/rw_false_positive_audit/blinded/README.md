# Blinded RW false-positive audit

This directory contains a single audit sheet pooling all 264 unmatched
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

The per-condition audit sheets (`audit_sheet_{gd,b3,b3pp}.{md,pdf}`)
explicitly told the reviewer which condition produced each finding and
which condition was hoped to "win." That biases verdicts. This blinded
sheet removes both signals.
