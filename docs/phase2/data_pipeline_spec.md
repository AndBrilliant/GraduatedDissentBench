# Graduated Dissent Benchmark: Data Pipeline Tool Spec

## Phase 2 Initial Build

**Authors:** Andrew Brilliant, Joe Reid

---

## Goals

A single tool that handles all stages of the benchmark pipeline from candidate extraction through inter-rater scoring, such that growing the benchmark from n=10 to n=50 is a matter of steady workflow execution rather than ad-hoc scripting. Designed for Drew + Joe as the initial users, architected so it can scale to outside contributors in phase 3 without a rewrite. Every decision creates an audit trail that can be reconstructed later. No API keys stored server-side, ever.

## Non-goals

Not a real-time collaboration tool for phase 2 (single user at a time is fine). Not a general retraction database (only tracks what is in the benchmark). Not a model serving platform (calls external APIs, does not host models). Not a replacement for git (git still holds the canonical dataset).

## Users and roles (phase 2)

**Maintainer** (Drew): full access, can lock schemas and ground truth, can override automated decisions.

**Contributor** (Joe): full access within assigned domains, can propose changes to locked items for maintainer approval.

Phase 3 adds an **external contributor** role with write access only to their own submissions pending review.

## Data model

Core entities. Every record has standard audit fields: `created_at`, `created_by`, `updated_at`, `updated_by`.

- **Paper**: record_id, retraction_watch_id, title_hash, pub_date, retraction_date, reason_raw, reason_structured, class (A/B/C), status (candidate/accepted/excluded/routed), exclusion_reason
- **RetractionNotice**: paper_id, notice_text, notice_url, parsed_fields (JSON)
- **Control**: control_id, paired_paper_id, journal, topic, pub_date, verification_notes
- **GroundTruthKeywords**: paper_id, keyword_groups (JSON), locked (bool), locked_by, locked_at
- **AnonymizedManuscript**: paper_id, file_path, anonymization_log
- **ProtocolRun**: run_id, paper_id, config_snapshot, model_versions, timestamp
- **Finding**: run_id, stage, severity, text, source_model
- **ScoringResult**: run_id, paper_id, gt_match (bool), matched_findings, overrides
- **Contributor**: user_id, name, domains, papers_added, inter_rater_subset

## User flows

Each stage describes: trigger, what user sees, what user does, what system does, what gets stored.

### Stage 1: Candidate ingestion from Retraction Watch

Trigger: Maintainer clicks "Update candidates".
System: Pulls latest CSV from Crossref mirror via `git pull`. Diffs against existing records. Applies pre-filter (post-cutoff, excludes misconduct categories, excludes paper mills).
User sees: Table of new candidates with filters for date, journal, reason category.
User does: Selects which candidates go into the pool, or accepts the pre-filter default.
Stored: Paper records with status=candidate.

### Stage 2: Notice enrichment

Trigger: Automatic after new candidates added.
System: Fetches retraction notice text and full-text availability (Unpaywall API). LLM parses notice into structured fields.
User sees: List of parsed results with confidence markers. Low-confidence parses highlighted.
User does: Spot-checks a sample (default 20%, minimum 5). Approves, edits, or flags.
Stored: RetractionNotice records with parsed_fields and audit trail of which entries were verified.

### Stage 3: Triage (Class A/B/C)

Trigger: User opens triage queue.
System: Shows unreviewed candidates with notice text, LLM-suggested class, pre-specified criteria reminder.
User does: Reads notice, assigns class, records decision reasoning.
Stored: class decision, reasoning, LLM suggestion (for drift analysis), agreement flag.

### Stage 4: Domain routing and expert review

Trigger: Triage assigns a paper to a domain outside the maintainer's expertise.
System: Routes to contributor whose declared domains match, or to queue if no match.
Contributor sees: Notice, abstract, methodology section, relevant figures.
Contributor does: Confirms the error is text-detectable and matches the notice, or rejects with reason.
Stored: Verification record with contributor ID and reasoning.

### Stage 5: Anonymization

Trigger: Paper reaches accepted status.
System: Runs anonymization script (strips author names, affiliations, journal, dates, acknowledgments, references). LLM scans for remaining identifying markers.
User sees: Before/after diff plus LLM-flagged items.
User does: Approves each flag or marks as false positive.
Stored: AnonymizedManuscript file plus anonymization log.

### Stage 6: Control matching

Trigger: User opens control matching interface.
System: Suggests candidate controls from same journal, similar date, topic overlap. LLM ranks by similarity.
User does: Reviews top 5, selects match or rejects all.
Stored: Control record paired to retracted paper with verification notes.

### Stage 7: Ground truth keyword extraction

Trigger: User opens GT editor for a paper.
System: Shows notice text and current keyword groups (may be empty or LLM-suggested).
User does: Edits groups, adds, removes. Clicks "Lock" when satisfied.
Stored: Keyword groups as JSON, lock status, lock timestamp. Post-lock changes require explicit unlock with audit reason.

### Stage 8: Protocol execution

Trigger: User selects paper(s) and clicks "Run protocol".
System: Prompts for API keys (session-scoped, never stored). Runs provers, judge, steelman, arbiter. Saves all outputs.
User sees: Progress indicator, cancel option, final output with all stage artifacts.
Stored: ProtocolRun, Finding records, raw output files.

### Stage 9: Automated scoring

Trigger: Automatic after protocol run.
System: Runs keyword matching against locked GT. Produces audit table.
User sees: Paper-by-paper matches with finding text and which keyword group matched (or did not).
User does: Reviews audit, optionally overrides with reason.
Stored: ScoringResult record, override log.

### Stage 10: Inter-rater check

Trigger: Second user opens an already-scored paper.
System: Hides first user's decisions, shows only findings.
Second user does: Scores independently.
System: Compares, computes agreement metric, surfaces discrepancies.
Stored: Second rater decisions, agreement stats.

## Technical architecture

**Backend**: Python with FastAPI. Single process, SQLite database file. SQL queries with a thin helper layer rather than a full ORM. Keeps the code readable for someone learning Python.

**Frontend**: Server-rendered HTML with htmx for interactivity. No build step, no JavaScript framework. Anyone with basic web knowledge can contribute to the UI.

**File storage**: Local filesystem for phase 2. Organized by paper record_id. Directory layout mirrored in git so the full dataset is versioned alongside the code.

**LLM integration**: Single abstract interface that wraps provider APIs. User provides keys at runtime. Keys never logged, never persisted, never sent to the backend beyond the scope of the request that needs them.

**Auth**: Phase 2 is single-user local deployment with no login. Phase 3 adds password-hashed user accounts. Phase 4 could add OAuth.

**Deployment**: Phase 2 runs as `python -m benchmark_tool` locally, or in a Docker container. Database is a SQLite file the maintainer keeps on their machine and commits to the repo on every session. Phase 3 deploys to a modest VPS.

## Phase boundaries

**Phase 2 (now)**: Drew + Joe, local deployment. Goal: grow benchmark to n=25-50 with the tool handling the pipeline. Prove the workflow before scaling.

**Phase 3 (after phase 2 paper posted)**: Small group of contributors, hosted deployment, proper auth, review queue for external submissions. Same data model, bigger user base.

**Phase 4 (if phase 3 gets traction)**: Open contribution, rate limiting, moderation, attribution on releases.

## What to build first

Minimum viable for phase 2, in priority order:

1. **Stage 1** (candidate ingestion from CSV). This is the highest-leverage single piece of work because it unlocks the whole pipeline and replaces the LLM-guessing selection method that produced only 10 papers last time.
2. **Stage 3** (triage UI). The place where human judgment gets applied consistently.
3. **Stage 7** (ground truth editor). Must exist before scoring can be trusted.
4. **Stage 9** (automated scoring). Already mostly works as a script; needs to be integrated so the audit table lives in the tool rather than in CSVs.

Stages 2, 5, 6, 8, and 10 can remain scripted or manual in the short term and get wrapped into the tool as Joe and Drew need them.

## Suggested division of labor

Drew: database schema, stage 9 integration, overall architecture decisions, spec enforcement.

Joe: stages 1, 3, and 7 UIs. These are good learning projects because they exercise SQL, FastAPI basics, git integration, API clients, simple prompt engineering, and htmx. They give Joe real ownership of pieces that matter rather than fetch-tasks.

Both: stage 4 workflow, because domain routing affects everyone.

## Open questions

- Database choice: SQLite is right for phase 2, but the migration path to Postgres in phase 3 should be checked early so the SQL is portable.
- Git integration: should the tool auto-commit changes, or should the user commit manually? Auto-commit is safer but noisier.
- LLM provider abstraction: support just one provider initially (probably Anthropic since Drew has it) or support multiple from the start? Multiple adds complexity but matches the paper's multi-model philosophy.
- Anonymization automation: how much can be scripted reliably? Requires a test set to evaluate.

These are worth discussing Friday.
