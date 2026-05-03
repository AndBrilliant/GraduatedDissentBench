# LaTeX Updates Needed — After v6 Benchmark Completes

## New Narrative
The paper's story has shifted from "detects retraction-worthy errors" to:
**"Graduated dissent eliminates false retraction-worthy classifications 
that single-model review produces, while maintaining error detection."**

The contribution is SPECIFICITY (precision), not sensitivity (recall).

## Abstract
- Rewrite to reflect: "all configurations detect methodological errors in 
  retracted papers, but single-model review produces false retraction-worthy 
  classifications on control papers that graduated dissent eliminates"
- Update numbers from actual results
- Drop "100% sensitivity" claims — actual is ~40% for RW binary
- Emphasize: protocol finds real errors in 10/10 retracted papers at 
  major-revision level; the question is severity calibration, not detection

## Results Section — Major Restructure

### New Table: Error Detection (did it find the ground truth error?)
Show that ALL conditions find the real errors:
| Paper | B1 found GT? | B2 found GT? | GD found GT? |
This should show ~10/10 or close for all conditions.
The protocol doesn't find MORE errors — everyone finds them.

### New Table: False Positive Rate (RW findings on controls)
| Condition | Controls with >=1 RW | False positive rate |
| B1 (no rubric) | N/A (no severity) | N/A |
| B2 (+ rubric) | X/24 | X% |
| Graduated dissent | 0/24 | 0% |
THIS is the headline result.

### New Table: Full Severity Spectrum 
Show the full range from crackpot to clean:
| Category | Avg RW | Avg MajR | Avg Minor |
| viXra/crackpot | ~10 | ~9 | ~2 |
| Retracted | ~0.5 | ~8 | ~5 |
| Controls | 0 | ~8 | ~5 |
| Wildcards | 0 | ~5 | ~3 |
(If we include the viXra papers)

### Keep: Arbiter comparison table (from pilot data)

## Discussion Section Updates

### "The Protocol's Contribution is Specificity"
New subsection. Key points:
- All approaches find methodological errors — LLMs are good at this
- Single-model review finds errors BUT also generates false RW flags
- Graduated dissent's steelman exchange causes provers to back off 
  overblown criticisms (cite Cousins private test: Prover A downgraded 
  5/9 findings during steelman)
- The arbiter's conservative threshold eliminates remaining false positives
- This means: when the protocol says "retraction-worthy," trust it

### "Detection vs Classification"
- Protocol detects retraction-causing errors in all 10 retracted papers
- But classifies only 4/10 as retraction-worthy (rest as major-revision)
- This is conservative calibration, not detection failure
- The same conservatism that produces 0% false positives limits sensitivity
- This tradeoff is a design choice, not a bug

### "Implications for Manuscript Generation" — already added, keep

### Drop or soften: "Why Model-Role Assignment Matters" 
- We only tested one config in v6, so the v4 arbiter comparison is 
  from different data. Could keep as pilot finding but not primary claim.

## Figures
- fig1 (bar chart): regenerate with v6 data
- fig2 (heatmap): regenerate
- fig3 (arbiter comparison): keep from v4 or drop
- fig5 (severity scores): regenerate — show overlap is the point now
- NEW fig: B1 vs B2 vs GD false positive comparison
- NEW fig: full spectrum from crackpot → retracted → control → wildcard

## Limitations — Update
- "40% sensitivity for retraction-worthy classification" — honest
- "100% detection at major-revision level" — also honest
- These are different metrics measuring different things

## Models Table
- GPT-5.4: confirmed
- DeepSeek V3.2: confirmed  
- Opus 4.6: confirmed
- (No Sonnet in primary results)

## Baseline Section
- B1 and B2 are now central to the paper, not illustrative
- Need full results tables for both
- The C04 false positive in B2 is a key finding

## Bibliography
- May need to add references for specificity/precision distinction
- Mayo (2018) already cited — severity framing supports this
