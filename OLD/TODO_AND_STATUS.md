# Graduated Dissent Benchmark v6 — Complete Status & TODO
## Updated: April 6, 2026 ~12:00 JST

---

## COMPLETED BENCHMARKS (all on photek in results/)

### Primary Results (all 34 papers)
- **B1 baseline** (single model GPT-5.4, no rubric): 34/34 ✅ → results/baseline_B1/*_B1_*.json
- **B2 baseline** (single model GPT-5.4 + severity rubric): 34/34 ✅ → results/baseline_B1/*_B2_*.json
- **Graduated Dissent** (GPT-5.4 prover + DeepSeek prover + Opus arbiter): 34/34 ✅ → results/primary/*.json
- **Prompted retraction** (told "this was retracted, find why" — 3 models × 10 papers): 30/30 ✅ → results/prompted/*.json

### Private tests (NOT in benchmark, NOT in paper)
- **UFT crackpot** (viXra unified field theory): 10 RW, 9 MajR, 2 Minor → results/crackpot_test/
- **Cousins severity paper** (legitimate published): 0 RW, 0 MajR, 6 Minor → results/crackpot_test/

### HEADLINE RESULTS
| Condition | Ground Truth Detection | False Positive Rate |
|-----------|----------------------|---------------------|
| B1 (no rubric) | 3/10 (30%) | N/A (no severity) |
| B2 (+ rubric) | 4/10 (40%) | 3/24 (12%) |
| **Graduated Dissent** | **7/10 (70%)** | **0/24 (0%)** |

### Severity Averages
| Category | n | Avg RW | Avg MajR | Avg Minor | Avg Score |
|----------|---|--------|----------|-----------|-----------|
| Retracted | 10 | 0.5 | 8.3 | 4.9 | 23.0 |
| Controls | 10 | 0.0 | 7.9 | 5.1 | 20.9 |
| Hard-neg | 9 | 0.0 | 6.2 | 5.6 | 18.0 |
| Wildcards | 5 | 0.0 | 6.6 | 5.8 | 19.0 |

### B2 False Positives (eliminated by GD)
- C04 (matched control): B2=1 RW, GD=0
- C10 (matched control): B2=2 RW, GD=0
- HN10 (hard negative): B2=1 RW, GD=0

---

## BENCHMARKS STILL NEEDED

### 1. viXra GUT Theory Papers (control group)
- **What:** 5 most recent "Grand Unified Theory" or "Theory of Everything" papers from viXra.org
- **Why:** Show the protocol correctly identifies fundamentally flawed papers (high RW)
- **Criteria:** Post-cutoff (2025-2026), no hand-picking, just "most recent"
- **Must be anonymized** same as all other papers
- **DO NOT include the Muñoz UFT paper** — use only viXra papers with no identifiable author
- **Run through:** Graduated Dissent primary config (GPT-5.4 + DeepSeek + Opus)
- **Expected result:** High RW counts (5-10+), demonstrating full severity spectrum

### 2. LLM Co-Authored Papers (control group)
- **What:** 2-3 papers with LLM listed as co-author or acknowledged as primary writer
- **Why:** Test if protocol catches AI-generated content quality issues
- **Source:** Search for papers where ChatGPT/Claude/LLM is listed as author
- **Must be post-cutoff, anonymized**
- **Run through:** Same primary config

### 3. Prompted Retraction Analysis (needs proper scoring)
- **Data exists:** results/prompted/ — 30 JSON files (10 papers × 3 models)
- **Problem:** Keyword matcher returned 0/10 due to format mismatch
- **Fix needed:** The prompted format uses "identified_error" field not "findings"
- **Manual review shows:** Models DO find real errors when told it's retracted (R04 all 3 nailed it, R19 all 3 nailed it)
- **Key finding:** Telling model it's retracted doesn't magically unlock detection — models predict plausible retraction causes, not always the actual one
- **Integration:** Needs proper write-up in paper with correct detection rates

### 4. Arbiter Threshold Sweep (ROC curve)
- **What:** Rerun ONLY the arbiter at different severity thresholds on same prover/steelman material
- **Why:** Shows sensitivity-specificity tradeoff as a tunable slider
- **How:** 3 threshold settings × 34 papers × 1 arbiter call each = 102 calls (~$5)
  - Aggressive: "Flag as RW if error COULD invalidate"
  - Moderate: "Flag as RW if error LIKELY invalidates" 
  - Conservative: "Flag ONLY if definitively invalidates" (current)
- **Output:** ROC-like curve showing operating points
- **Paper already has placeholder for this in Section slider**

---

## FIGURES NEEDED (generate with Python/matplotlib)

### Style inspiration:
- Radar/spider charts for model strengths per role
- Bullet graphs (like the sales chart) for severity thresholds
- Clean bar comparisons (like LLM benchmark charts)
- Heatmaps for paper × condition matrices

### Specific figures:

1. **Ground Truth Detection Comparison** (THE money figure)
   - Grouped bar: B1 (30%) vs B2 (40%) vs GD (70%)
   - Add false positive bars: B2 (12%) vs GD (0%)
   - Two-panel or stacked showing both metrics

2. **Severity Spectrum** 
   - Stacked bar or violin showing RW/MajR/Minor distribution
   - By category: Retracted | Controls | Hard-Neg | Wildcards
   - Show that discrimination is in the RW tier only

3. **False Positive Elimination Detail**
   - Show the 3 specific B2 false positives (C04, C10, HN10)
   - Show they become 0 RW under GD
   - Annotate with steelman exchange mechanism

4. **Protocol Flowchart** (updated for v6)
   - GPT-5.4 → DeepSeek → Judge → Steelman → Opus Arbiter
   - Show severity at each stage

5. **Bullet Graph: Severity Slider Concept**
   - Show conservative/moderate/aggressive threshold zones
   - Mark current operating point
   - Placeholder until ROC data available

6. **Per-Paper Ground Truth Match** 
   - 10 retracted papers, which conditions found the real error
   - Checkmarks/X for B1/B2/GD per paper

7. **Crackpot Spectrum** (if viXra data collected)
   - Full range: viXra (10+ RW) → Retracted (0-2 RW) → Controls (0 RW)

---

## PAPER STATUS

### File: ~/Desktop/Academic/graduated_dissent_bench_v6/manuscripts/main.tex
### Also on photek at same path

### What's updated:
- ✅ Abstract — v6 numbers (70% GT detection, 0% FP, 34 papers)
- ✅ Dataset section — 34 papers in 4 categories with CI calculation
- ✅ Controls section — matched + hard-neg + wildcards described
- ✅ Models — GPT-5.4, DeepSeek V3.2, Opus 4.6
- ✅ Baselines B1/B2 methodology
- ✅ Results: Ground truth detection table
- ✅ Results: False positive elimination table
- ✅ Results: Severity spectrum table
- ✅ Results: Qualitative validation (crackpot + legitimate)
- ✅ Discussion: "Protocol's contribution is specificity"
- ✅ Discussion: "Why single-model produces false positives"
- ✅ Discussion: Role separation
- ✅ Discussion: Severity slider concept
- ✅ Discussion: Implications for manuscript generation
- ✅ Anonymization paragraph (formatting bias documented)
- ✅ Conclusion — three findings

### What still needs updating:
- ⚠️ Old figure references (fig1-fig5) point to v4 images that don't match v6 data
- ⚠️ Some old figure \includegraphics may fail on compile (files don't exist in v6)
- ⚠️ Prompted retraction results not yet in paper
- ⚠️ viXra/LLM control groups not yet in paper (placeholders exist)
- ⚠️ ROC/slider analysis not yet done (placeholder in discussion)

---

## KEY FILES ON PHOTEK

### Scripts
- scripts/run_v6.py — main graduated dissent protocol (GPT-5.4, DeepSeek, Opus, Sonnet)
- scripts/run_baseline.py — B1/B2 baselines
- scripts/run_prompted_retraction.py — prompted "this was retracted" test
- scripts/match_ground_truth.py — keyword-based GT matching
- scripts/full_results.py — complete results summary
- scripts/check_ground_truth.py — detailed per-paper GT comparison
- scripts/extract_science.py — paper anonymizer/extractor
- scripts/run_v6_complete.sh — master run script (B1 + B2 + Primary)

### Data
- dataset/retracted/ — 10 raw retracted papers
- dataset/controls/ — 10 raw control papers
- dataset/hard_negatives/ — 9 raw hard-negative papers
- dataset/wildcards/ — 5 raw wildcard papers
- dataset/anonymized/ — R01-R25, C01-C25, HN02-HN10, W01-W05 anonymized
- ground_truth/ — R01-R25 ground truth error documentation

### Results
- results/baseline_B1/ — B1 and B2 results (34 each)
- results/primary/ — Graduated dissent results (34)
- results/prompted/ — Prompted retraction (30)
- results/crackpot_test/ — UFT and Cousins (private, not in benchmark)
- results/authors_choice/ — Partial Sonnet run (9 papers, incomplete)

### API Keys
- ~/.keys/anthropic, ~/.keys/openai, ~/.keys/deepseek

### Models Used
- GPT-5.4 (gpt-5.4) — Prover A, baselines
- DeepSeek V3.2 (deepseek-chat) — Prover B, Judge
- Claude Opus 4.6 (claude-opus-4-6) — Arbiter
- Claude Sonnet 4.6 (claude-sonnet-4-6) — available but not in primary results

---

## IMPORTANT NOTES FOR FUTURE SESSIONS

1. **v4 pilot data exists** in ~/Desktop/Academic/graduated_dissent_bench/ but is SEPARATE from v6. v4 had broken anonymization and old models. Do not mix.

2. **The Cousins and UFT tests are PRIVATE** — not in the published benchmark. Cousins is a colleague's paper, UFT has an identifiable author.

3. **Anonymization is critical.** Papers must have NO author names, NO journal names, NO retraction mentions, NO publisher templates. Country names kept if scientifically relevant (documented in dataset/anonymized/METHODOLOGY_NOTE.md).

4. **The paper's narrative:** Graduated dissent's contribution is SPECIFICITY (0% FP) not sensitivity. It finds the same errors as single models but eliminates false alarms through steelman exchange.

5. **Ground truth detection (70%)** is measured by keyword matching against documented retraction causes. This is approximate — some matches may be missed by keywords. Manual verification of a subset was done for R01-R05.

6. **The severity slider concept** is discussed but NOT yet empirically validated. The ROC curve analysis (threshold sweep) is planned but not run.

7. **Session transcript** saved at ~/claude/session_transcript_2026-04-02_to_2026-04-05.jsonl
