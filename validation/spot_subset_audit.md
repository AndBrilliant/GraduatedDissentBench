# SPOT subset audit — what n=50 is and is not

## Definitions

The SPOT benchmark \citep{son2025spot} is distributed as two HuggingFace
datasets:
- `amphora/SPOT-MetaData` — 91 human-annotated errors across 83
  scientific papers, with `error_category` tagging (Equation/proof,
  Statistical reporting, Figure duplication, etc.).
- `amphora/SPOT` — 68 of those error annotations with parsed paper
  content attached, suitable for downstream LLM evaluation.

Our pipeline operates on **text-detectable** errors only — categories
where the error surfaces in prose rather than requiring figure
inspection:

  Text-detectable  : Equation/proof, Statistical reporting,
                     Experiment setup, Reagent identity,
                     Data inconsistency, Data Inconsistency (text-text)
  Partially text   : Data Inconsistency (figure-text)  — text side
                                                         may surface
                                                         in prose
  Figure-only      : Data Inconsistency (figure-figure),
                     Figure duplication                — excluded

## How we get to n = 50

```
Total annotated errors (SPOT-MetaData):              91
   Text-detectable (incl. partial figure-text):      62
   Figure-only (excluded by design — vision-only):   29

Total unique papers:                                  83
   With ≥1 text-detectable error:                    56
   With figure-only errors only (excluded):          27

Papers with parsed content (amphora/SPOT):            62
   With ≥1 text-detectable error AND parsed content: 50  ← our n=50
   With text-detectable error but NO parsed content:  6  (excluded — no input text)
```

**n = 50 is the complete intersection of (text-detectable) and (parsed
content available).** It is not a stopping point — every paper meeting
both criteria was run.

## The six text-detectable papers we did not run

These six papers have text-detectable annotations in
`amphora/SPOT-MetaData` but no parsed content in `amphora/SPOT`. They
were therefore excluded from our runnable subset. We list them
explicitly:

| Paper category | Error category | Severity | Title |
|---|---|---|---|
| Environmental Science | Data inconsistency | errata | Assessment of clean production level in phosphate mining enterprises... |
| Biology | Reagent identity | retract | Glycerol-silica/chitosan conjugated self-assembled nano-flower framework... |
| Materials Science | Data inconsistency | errata | In-situ acid catalysis strategy to achieve rapid ambient pressure drying... |
| Materials Science | Data inconsistency | errata | Innovative fabrication of highly efficient CeO2 ceramic nanomaterials... |
| Chemistry | Data Inconsistency (figure-text) | errata | Screening High-Performance Hybrid Halides Scintillators... |
| Chemistry | Data Inconsistency (figure-text), (figure-figure) | errata | Superacid In Situ Protected Synthesis of Covalent Organic Frameworks |

We could not include these in the run because the SPOT distribution
does not provide the parsed manuscript text. Re-parsing the original
papers from publisher PDFs would deviate from SPOT's pipeline and
introduce a comparison confound; we elected to leave them excluded
and document the exclusion rather than fold them in non-comparably.

## What this implies for the comparison with SPOT-published o3

SPOT (Son et al., 2025) reports o3 with vision access on the **full
83-paper benchmark including figure-only errors**: pass@1 18.4%,
recall 21.1%, precision 6.1%.

Our n = 50 is a subset:
- Excludes 27 papers whose annotations are figure-only.
- Excludes 6 papers that lack parsed content in the public release.

The text-detectable-subset comparison is therefore not strictly
apples-to-apples with SPOT's published headline number; the relevant
direct comparison on our subset is our own single-model GPT-5.4
baseline (B1, pass@1 = 24%), which sits at the same constraint
(text-only, no figure access, same papers as our other conditions).

## Reproduction note

`harness/spot_categorize.py` regenerates the runnable index from the
two HuggingFace datasets. Re-running it should yield 50 papers; if a
future SPOT release adds parsed content for any of the six excluded
papers above, the index would expand correspondingly.
