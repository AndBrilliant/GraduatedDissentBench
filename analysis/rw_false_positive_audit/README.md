# RW false-positive audit

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
