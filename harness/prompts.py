"""Centralized prompt strings — single source of truth for all conditions.

Mirrors the prompts used in the original benchmark (see github/prompts/) but
defined inline so the harness has no path-resolution surprises. Any prompt
change here must be reflected upstream when the published repo is updated.
"""

SEVERITY_RUBRIC = """
SEVERITY CLASSIFICATION (required for every finding):

RETRACTION-WORTHY: The error means the paper's central conclusions CANNOT be
supported by the data as presented. Not "could be improved" — "fundamentally broken."
Examples: data coding errors that change the primary outcome, impossible statistical
values, applying tests that don't match the study design rendering all inferences invalid.

MAJOR-REVISION: A real methodological concern that could change conclusions if
addressed differently, but does NOT definitively invalidate them.
Examples: missing controls, underpowered secondary analyses, questionable but
defensible statistical choices.

MINOR: Valid criticism applicable to most published papers. Would not change conclusions.
Examples: no robustness checks, limited generalizability, minor reporting gaps.

KEY TEST: If confirmed, would this need RETRACTION, REVISION, or just NOTING?
"""

PROVER_PROMPT = """You are an independent scientific reviewer. Review this manuscript for
methodological correctness. For each error or concern, classify its severity.

""" + SEVERITY_RUBRIC + """
Manuscript:
{paper_text}

Respond in JSON:
{{"verdict": "flagged"|"not_flagged",
  "confidence": 0.0-1.0,
  "reasoning": "overall assessment",
  "findings": [
    {{"finding": "description",
      "severity": "RETRACTION-WORTHY|MAJOR-REVISION|MINOR",
      "justification": "what breaks if confirmed?"}}
  ]}}"""

JUDGE_PROMPT = """Compare two independent reviews of the same manuscript.

REVIEW A:
{review_a}

REVIEW B:
{review_b}

Rate semantic agreement 0.0-1.0. Identify where they disagree on severity.

Respond in JSON:
{{"agreement_score": 0.0-1.0,
  "severity_agreement": "do they agree on which findings are retraction-worthy?",
  "shared_findings": ["findings both identify"],
  "severity_disputes": ["findings where severity differs"],
  "unique_to_a": ["only in A"],
  "unique_to_b": ["only in B"]}}"""

STEELMAN_PROMPT = """You previously reviewed a manuscript.

YOUR REVIEW:
{own_review}

A DIFFERENT REVIEWER reached different conclusions:
{other_review}

TASKS:
1. Build the STRONGEST CASE for the other reviewer's position, especially on severity.
2. For findings you rated RETRACTION-WORTHY: could they be MAJOR-REVISION instead?
3. Which of your severity ratings might be wrong?

""" + SEVERITY_RUBRIC + """
Respond in JSON:
{{"steelman_for_other": "strongest case for their position",
  "severity_i_now_upgrade": ["findings I think are MORE severe"],
  "severity_i_now_downgrade": ["findings I think are LESS severe"],
  "findings_i_still_defend": ["findings + severity I stand by"],
  "new_errors_noticed": ["errors from fresh perspective"]}}"""

ARBITER_PROMPT = """You are the Arbiter. You have the complete deliberation.

""" + SEVERITY_RUBRIC + """
REVIEW A:
{review_a}

REVIEW B:
{review_b}

JUDGE:
{judge_analysis}

STEELMAN EXCHANGE:
A's steelman of B: {steelman_a}
B's steelman of A: {steelman_b}

TASK: Final severity-ranked assessment.
- Findings surviving steelman with consistent severity = high confidence
- Findings where a prover downgraded own severity = probably overstated
- ONLY classify as RETRACTION-WORTHY if fundamentally broken.
  When in doubt, MAJOR-REVISION.

Respond in JSON:
{{"verdict": "flagged"|"not_flagged",
  "confidence": 0.0-1.0,
  "reasoning": "synthesis",
  "findings": [
    {{"finding": "description",
      "severity": "RETRACTION-WORTHY|MAJOR-REVISION|MINOR",
      "confidence_in_severity": 0.0-1.0,
      "justification": "why this level",
      "source": "both|prover_a|prover_b|emergent",
      "survived_steelman": true|false}}
  ]}}"""

# B3 arbiter (no steelman material).
ARBITER_B3_PROMPT = """You are the Arbiter. Two independent reviewers evaluated this manuscript.

""" + SEVERITY_RUBRIC + """
REVIEW A:
{review_a}

REVIEW B:
{review_b}

TASK: Final severity-ranked assessment.
- Consider both reviews and produce a unified assessment.
- ONLY classify as RETRACTION-WORTHY if fundamentally broken.
  When in doubt, MAJOR-REVISION.

Respond in JSON:
{{"verdict": "flagged"|"not_flagged",
  "confidence": 0.0-1.0,
  "reasoning": "synthesis",
  "findings": [
    {{"finding": "description",
      "severity": "RETRACTION-WORTHY|MAJOR-REVISION|MINOR",
      "confidence_in_severity": 0.0-1.0,
      "justification": "why this level",
      "source": "both|prover_a|prover_b"}}
  ]}}"""

# B1 — single model, no severity rubric.
B1_PROMPT = """Review this manuscript. Identify methodological strengths and weaknesses.

Manuscript:
{paper_text}

Respond in JSON:
{{"verdict": "flagged"|"not_flagged",
  "confidence": 0.0-1.0,
  "reasoning": "overall assessment",
  "findings": [
    {{"finding": "description"}}
  ]}}"""

# B2 — single model + severity rubric (same as PROVER_PROMPT, kept separate
# in case B2 phrasing diverges in future).
B2_PROMPT = PROVER_PROMPT

# Thresholds (graduated dissent escalation logic).
THETA_ACCEPT = 0.90
THETA_NOISE = 0.15
