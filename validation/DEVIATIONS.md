# Protocol deviations register

This document records every place where the final paper differs from the
original protocol specification, the as-pre-registered hypothesis
framing, or earlier reported numbers. Each entry covers what was
planned, what happened, what changed, and where the supporting data
lives. A reviewer or replicator should be able to read this register
and reconstruct the experimental record without surprises.

Status as of 2026-05-04. All deviations described here are reflected in
the paper's body text and limitations section.

---

## Deviation 1 — Escalation gate not invoked under tested conditions

**Specification.** The graduated dissent (GD) protocol is specified
with three escalation levels. With agreement threshold
$\theta_{\text{accept}} = 0.90$ and noise floor $\theta_{\text{noise}} =
0.15$, a paper is supposed to resolve at L0 (skip steelman) when
inter-prover agreement is at least $0.90$, at L1 when SNR
$=(1-\text{agreement})/\theta_{\text{noise}}<1$ (accept; noise),
otherwise at L2 (run steelman exchange before arbiter).

**What happened.** The gate fired correctly at the protocol level — 3
of the 20 SPOT pilot papers hit L0 — but the arbiter prompt template
was passed steelman placeholders at all escalation levels, with the
literal string `"N/A — escalation level L0"` substituted when the
gate was not triggered. Initial fresh-Claude adversarial review of the
n=20 raw outputs flagged this as evidence the gate was non-functional.
Inspection of the per-paper protocol logs disconfirmed the
non-functional reading: paper_005 (agreement 0.92), paper_009
(agreement 0.92), and paper_018 (agreement 0.95) all correctly hit L0
and skipped the steelman API calls. The remaining 17 of 20 escalated
to L2; no paper hit L1 (the noise-floor band between agreement 0.85
and 0.90 was empty in this sample).

**Papers affected.** paper_005, paper_009, paper_018 in the validated
n=20 core. None are in the B3-vs-GD discordant pair set — when GD's
arbitration runs without steelman material, the result is
indistinguishable from B3 on detection for those papers.

**Impact on aggregates.** None on the headline B3-vs-GD comparison.
The L0 papers contribute equal-and-aligned detections to both
conditions.

**Resolution.** The GD condition is described in the paper as
"multi-model with conditional steelman exchange" with an explicit
note that 3 of 20 papers in the validated core skipped the exchange.
Future work should test the protocol on an adversarial sample where
the L1 band is occupied to characterize the gate empirically.

**Discovered.** 2026-05-03, by fresh Claude Opus adversarial audit of
the n=20 validation package.

**Data.** [`validation/protocol_deviations.md`](protocol_deviations.md)
contains the per-paper protocol log table.

---

## Deviation 2 — Anonymization inconsistency between SPOT batches

**Plan.** All SPOT papers were to be anonymized through the same
text-anonymization pipeline used for the retracted-paper benchmark
before being submitted to the four conditions.

**What happened.** The first 10 SPOT papers (drawn with seed=42 in the
initial pilot) were run on the original parsed content from the SPOT
public release — including author bylines, journal headers, dates, and
affiliations. The next 10 papers (drawn with seed=43) were
anonymized in place via `extend_spot_sample.py`. The asymmetry was
introduced when the second batch was added without retroactively
re-anonymizing the first.

**Observed effect.** Across all four conditions, pass@1 was 20–30 pp
higher on the anonymized batch than on the un-anonymized batch (B1:
+30 pp, B2: +20 pp, B3: +10 pp, GD: +30 pp).

**Initial concern.** A 30 pp gap on GD between batches looked like a
serious confound: either anonymization was helping (improbable on
mechanism but possible) or the anonymizer was leaking GT-correlated
signal.

**Root cause investigation.** The originally-unanonymized 10 papers
were re-anonymized through the same pipeline and re-run with all
prompts/models/parameters held constant. On the same 10 papers, B1
was unchanged (10 % → 10 %), B2 unchanged (10 % → 10 %), B3 dropped
(20 % → 10 %), GD dropped (20 % → 10 %); two specific
paper-condition cells flipped from detected to missed (paper_013 B3
and paper_020 GD). **Anonymization did not inflate detection. If
anything it slightly reduced it.** The 30 pp pre-fix gap was sample
composition: the seed-43 batch had more equation/proof papers
(for which the strict pass@1 metric is more often met) than the
seed-42 batch.

**Resolution.** All 50 papers in the final full text-detectable SPOT
run were anonymized through the same pipeline. The pre-fix
mixed-anonymization snapshot is preserved as a finding worth
reporting in its own right, alongside the orthogonal pre/post-cutoff
null result from the retracted-paper benchmark.

**Discovered.** 2026-05-03, in the validation package's
auto-stratification report; flagged before push.

**Data.** [`validation/anonymization_analysis/`](anonymization_analysis/)
contains the pre-fix snapshot, post-fix snapshot, and per-paper flips.

---

## Deviation 3 — Keyword scoring artifact on retracted-paper benchmark

**Original claim.** On the n=10 retracted + 19 probative-control
benchmark, GD was reported to detect $7/10$ retracted papers' errors
versus B3's $3/10$ — a 4-paper gap with all 4 discordant pairs
favoring GD (McNemar's exact two-sided $p = 0.125$).

**What happened.** Detection scoring used a keyword-matching pipeline:
each retracted paper had a set of keyword groups derived from the
documented retraction notice; a finding was scored as a match if it
contained all keywords in any keyword group for that paper. To reduce
dependence on first-author scoring decisions, every finding produced
by every condition on every paper was put through a blinded
three-model audit (GPT-5.4, Claude Opus 4.6, DeepSeek V3.2 at
temperature $0$). The audit asked, blinded to condition and paper
identity: "does the candidate finding substantially identify the same
methodological error as the documented retraction cause?"

**Impact.** Under blinded majority audit (2 of 3 models agreeing),
B3 detects $7/10$ retracted papers — the same as GD — and the
discordant pair set for B3-vs-GD detection is empty. The 4-paper gap
under first-author scoring was a scoring artifact: the keyword
pipeline missed B3's paraphrased findings that did not happen to
contain the registered keyword tokens. The McNemar $4/4$ direction
claim from the first-author scoring is also a scoring artifact.

**What survived.** GD's $0/19$ false retraction-worthy classifications
on probative controls is robust across all three scoring regimes
(first-author, majority audit, unanimous strict). B3's FP rate
*increased* under majority audit ($1/19 \to 2/19$): one additional
control (HN03) had a B3 RW classification that the audit majority
deemed retraction-justified. B2's first-author $3/19$ FP collapsed
to $0/19$ under audit — the auditors did not agree that B2's RW
classifications on controls actually warranted retraction.

**Resolution.** The paper now leads with the regime-robust claim
(``$0/19$ FP under every scoring regime tested'') and reports the
detection comparison with the audit table inlined. The original
``$70\%$ vs $30\%$ on detection'' framing has been retracted in the
paper body as a scoring-artifact result.

**Discovered.** 2026-05-04, by the multi-model rescoring run we
ourselves designed to test the original claim.

**Data.** [`validation/retracted_paper_audit/`](retracted_paper_audit/)
contains the raw audit responses, per-finding votes, per-paper
aggregates, and the four-row regime-comparison table. The Opus
fill-in run (`raw_responses_opus_fillin.jsonl`) covers the 598
audit batches that hit the initial budget cap on Anthropic.

---

## Deviation 4 — Disputed true positive: paper_014 (SPOT)

**Specification.** The SPOT n=20 pass@1 score depends on a binary
match decision: for each paper, did the model's findings semantically
identify the SPOT-annotated error?

**What happened.** Two of the three blinded adversarial evaluators
disagreed on exactly one paper (paper_014, GD condition). The SPOT
annotation describes a specific runtime-analysis omission; GD's
matching finding identified a related-but-distinct concern in the
same section. ChatGPT: "BORDERLINE/INCORRECT — B3 made a similar
critique that was rejected by the SPOT-style judge." Fresh Claude
Opus: "GENUINE — GD's finding is semantically closer to the
annotation than B3's."

**Impact.** Of the $19$ true positives across all four conditions at
n=20, exactly one is contested. GD pass@1 at n=20 is therefore
$25\%$ (5/20, strict; excludes the disputed TP) or $30\%$ (6/20,
standard; honors the original judge decision). At the full n=50
the same single paper is diluted: GD pass@1 is $34\%$ ($17/50$)
strict or $36\%$ ($18/50$) standard.

**Resolution.** paper_014 GD is flagged with `disputed=yes` in
[`scoring/per_paper_scores.csv`](scoring/per_paper_scores.csv). The
aggregate emits two GD rows (`GD_strict`, `GD_standard`) so the
strict-vs-standard difference is visible to readers. The paper's
abstract uses the standard value; limitations explicitly note the
strict alternative.

**Discovered.** 2026-05-03, in the cross-evaluator comparison of the
adversarial audit.

**Data.** [`scoring/score_outputs.py`](scoring/score_outputs.py) hosts
the `DISPUTED_TPS` set; future audit decisions can be added without
touching the rest of the code.

---

## Deviation 5 — Framing shift from detection to severity calibration

**Original framing (pre-data, pre-audit).** Earlier preprint and
draft material framed graduated dissent as primarily an *error
detection* method: a multi-model pipeline that finds methodological
errors single models miss. The retracted-paper benchmark's $70\%$
vs $30\%$ headline supported this framing under the original
keyword scoring.

**What the data showed.**
- On SPOT (n=50), GD pass@1 ($36\%$) leads single-model B1 ($24\%$)
  and B2 ($28\%$). It also leads multi-model-without-steelman B3
  ($30\%$), but by 6 pp — a single-paper gap on the discordant axis
  ($5/7$ pairs favor GD, McNemar $p=0.453$).
- Where GD separates clearly from both B2 and B3 on SPOT is the
  retraction-worthy severity tier: GD emits 33–56 % fewer RW flags
  per paper, at $11.7\%$ per-flag tier-precision versus B2's $7.0\%$
  and B3's $6.2\%$. RW-yield (papers correctly flagged retraction-
  worthy out of papers flagged at all) is $32\%$ for GD vs $20\%$
  for B2 and B3.
- On the retracted-paper benchmark, the keyword detection gap
  collapsed under blinded multi-model audit (Deviation 3). The
  surviving result on that benchmark is $0/19$ false retraction-worthy
  classifications under every scoring regime tested.

**Resolution.** The paper has been reframed around severity
calibration — the protocol's empirically observed contribution at
the load-bearing precision and false-positive level — with detection
treated as a secondary, regime-dependent comparison. The title was
changed from ``Information-Theoretic Bounds and Empirical
Validation'' to ``Information-Theoretic Bounds and Empirical
Evidence'' to reflect that the empirical results refine rather than
confirm the originally hypothesized contribution.

**Status.** This is not an error in the experimental record; it is
the research process working as intended. Pre-registering the
detection-headline framing made it harder for the data to lead us to
the calibration-headline framing, but the audit and the SPOT n=50
RW-precision metric independently surfaced the calibration story
from two directions, and the framing in the final paper follows the
data.

**Discovered.** 2026-05-04, in aggregate across the audit run, the
SPOT severity-rank analysis, and the user-prompted RW-precision
metric.

---

## Cross-references

- Paper limitations section now points at this register
  (single-line reference).
- Paper §SPOT comparison documents Deviation 4 (disputed TP) inline
  with strict/standard reporting.
- Paper §Retracted-paper benchmark documents Deviation 3 (keyword
  artifact) with the audit table inlined.
- Paper §Limitations documents Deviation 1 (always-steelman framing)
  and Deviation 2 (anonymization noted as resolved by uniform
  re-anonymization).
- Paper title and abstract reflect Deviation 5 (framing shift).

## Reproduction note

Every deviation listed here can be reproduced from the data in this
repository. The audit pipelines (`harness/audit_retracted.py`,
`harness/audit_aggregate.py`, `harness/audit_opus_fillin.py`) are
deterministic at temperature $0$. The SPOT subset analysis
(`harness/spot_categorize.py`) regenerates the $n = 50$ runnable
subset from the public HuggingFace datasets. The protocol logs
referenced in Deviation 1 are stored verbatim in each per-paper GD
output JSON.
