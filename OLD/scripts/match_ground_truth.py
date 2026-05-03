#!/usr/bin/env python3
"""
Match model findings against documented retraction causes.
For each paper × condition, score whether the actual error was identified.

Uses keyword matching against ground truth, then human review.
Outputs a scoring table.
"""
import json, glob, os, re

BASE = os.path.expanduser("~/Desktop/Academic/graduated_dissent_bench_v6")

# Ground truth: keywords that indicate the real error was found
# Each paper has a list of key phrases — if ANY finding contains these, it's a match
GROUND_TRUTH_KEYWORDS = {
    "R01": [
        ["HR", "0.00", "hazard"],  # impossible hazard ratios
        ["missing data", "asymptomatic"],  # coding error
        ["age", "range", "8", "13"],  # age range violation
        ["denominator", "271", "0.4"],  # incorrect incidence
    ],
    "R02": [
        ["extrapolat", "out-of-sample", "beyond"],  # extrapolation issue
        ["spatial", "autocorrelation", "correlation"],  # spatial autocorrelation
        ["data", "quality", "GDP", "implausible"],  # data quality (Uzbekistan)
    ],
    "R03": [
        ["preregistr", "post-hoc", "post hoc"],  # false preregistration
        ["selection", "outcome", "knowledge", "data"],  # selected with knowledge
        ["exploratory", "confirmatory"],  # exploratory presented as confirmatory
    ],
    "R04": [
        ["t-test", "repeated measure", "ANOVA", "longitudinal"],  # wrong test
        ["implausible", "height", "SD", "standard deviation"],  # implausible values
        ["replicat", "reproduc"],  # not replicable
    ],
    "R05": [
        ["randomiz", "allocation", "ratio", "1:2", "group size"],  # randomization failure
        ["741", "991", "1:1.3", "deviat"],  # specific group size mismatch
    ],
    "R10": [
        ["selection bias", "restrict", "prior", "vitamin D test"],  # selection bias
        ["14", "730", "day", "measurement", "gap", "delay"],  # measurement timing
    ],
    "R11": [
        ["mediation", "circular", "causal", "related construct"],  # circular mediation
        ["cortisol", "emotional exhaustion", "depersonaliz"],  # same construct
        ["cross-sectional", "causal", "design"],  # design flaw
    ],
    "R19": [
        ["reproduc", "replicat", "not reproduc"],  # not reproducible
        ["unclear", "analysis", "comprehend", "method"],  # unclear methodology
        ["time-zero", "misalign", "immortal"],  # time alignment issue
        ["hazard ratio", "continuous", "weight"],  # wrong use of HR
    ],
    "R24": [
        ["outcome event", "incorrect", "number"],  # wrong event count
        ["denominator", "population", "error"],  # population error
        ["non-independence", "procedures", "patients"],  # counting error
    ],
    "R25": [
        ["ICD", "code", "OR", "AND", "logic"],  # ICD code logic
        ["dementia", "false", "case", "misclassif"],  # false dementia cases
        ["Parkinson", "secondary", "dementia"],  # specific coding issue
    ],
}


def check_finding_matches(finding_text, keywords_list):
    """Check if a finding matches any of the keyword groups."""
    finding_lower = finding_text.lower()
    for keyword_group in keywords_list:
        if all(kw.lower() in finding_lower for kw in keyword_group):
            return True
    return False


def _prompted_match(d, pid):
    """Check if a prompted result dict matches ground truth for a paper."""
    kw = GROUND_TRUTH_KEYWORDS.get(pid, [])
    for finding in d.get("findings", []):
        text = str(finding.get("finding", "")) if isinstance(finding, dict) else str(finding)
        if check_finding_matches(text, kw):
            return True
    for field in ["identified_error", "why_fatal", "correct_approach"]:
        text = d.get(field, "")
        if text and isinstance(text, str) and check_finding_matches(text, kw):
            return True
    for err in d.get("additional_errors", []):
        if err and check_finding_matches(str(err), kw):
            return True
    return False


def analyze_condition(results_pattern, condition_name, is_baseline=False):
    """Analyze a set of results against ground truth."""
    print(f"\n{'='*70}")
    print(f"{condition_name}")
    print(f"{'='*70}")

    results = {}
    for f in sorted(glob.glob(os.path.join(BASE, results_pattern))):
        with open(f) as fh:
            d = json.load(fh)
        pid = d.get("paper_id", "?")
        if not pid.startswith("R"):
            continue
        results[pid] = d

    found_count = 0
    total = 0

    for pid in sorted(GROUND_TRUTH_KEYWORDS.keys()):
        if pid not in results:
            continue
        total += 1
        d = results[pid]

        # Get findings text
        if is_baseline:
            findings = d.get("findings", d.get("specific_errors_found", []))
        else:
            findings = d.get("findings", [])

        # Check each finding against ground truth
        matched = False
        matched_findings = []
        for finding in findings:
            if isinstance(finding, dict):
                text = str(finding.get("finding", ""))
                sev = finding.get("severity", "?")
            else:
                text = str(finding)
                sev = "N/A"

            if check_finding_matches(text, GROUND_TRUTH_KEYWORDS[pid]):
                matched = True
                matched_findings.append((sev, text[:100]))

        # Also check prompted retraction fields (identified_error, why_fatal, etc.)
        for field in ["identified_error", "why_fatal", "correct_approach"]:
            text = d.get(field, "")
            if text and isinstance(text, str):
                if check_finding_matches(text, GROUND_TRUTH_KEYWORDS[pid]):
                    matched = True
                    matched_findings.append((field, text[:100]))

        additional = d.get("additional_errors", [])
        if isinstance(additional, list):
            for err in additional:
                text = str(err) if err else ""
                if text and check_finding_matches(text, GROUND_TRUTH_KEYWORDS[pid]):
                    matched = True
                    matched_findings.append(("additional", text[:100]))

        if matched:
            found_count += 1
            tag = "FOUND"
        else:
            tag = "MISSED"

        print(f"\n  {pid}: {tag}")
        if matched_findings:
            for sev, desc in matched_findings[:3]:
                print(f"    [{sev}] {desc}...")
        else:
            print(f"    (no findings matched ground truth keywords)")

    print(f"\n  Ground truth detection: {found_count}/{total} = {100*found_count/total:.0f}%")
    return found_count, total


# Run analysis
print("GROUND TRUTH MATCHING")
print("Does each condition identify the actual retraction-causing error?")

b1_f, b1_t = analyze_condition("results/baseline_B1/*_B1_*.json", "B1: Single model, no rubric", is_baseline=True)
b2_f, b2_t = analyze_condition("results/baseline_B1/*_B2_*.json", "B2: Single model + rubric", is_baseline=True)
gd_f, gd_t = analyze_condition("results/primary/*.json", "GRADUATED DISSENT")

# Check if prompted results exist and analyze per-model
prompted_pattern = "results/prompted/*.json"
prompted_files = glob.glob(os.path.join(BASE, prompted_pattern))
pr_f, pr_t = 0, 0
prompted_by_model = {}
if prompted_files:
    # Group prompted results by model
    for f in sorted(prompted_files):
        with open(f) as fh:
            d = json.load(fh)
        model = d.get("model", "unknown")
        if model not in prompted_by_model:
            prompted_by_model[model] = {}
        pid = d.get("paper_id", "?")
        if pid.startswith("R"):
            prompted_by_model[model][pid] = d

    print(f"\n{'='*70}")
    print("PROMPTED (told it was retracted) — per model")
    print(f"{'='*70}")

    pr_total_f, pr_total_t = 0, 0
    for model in sorted(prompted_by_model.keys()):
        model_found = 0
        model_total = 0
        print(f"\n  --- {model} ---")
        for pid in sorted(GROUND_TRUTH_KEYWORDS.keys()):
            if pid not in prompted_by_model[model]:
                continue
            model_total += 1
            d = prompted_by_model[model][pid]

            # Check all text fields against ground truth
            matched = False
            matched_findings = []

            # Check findings list (if present)
            for finding in d.get("findings", []):
                if isinstance(finding, dict):
                    text = str(finding.get("finding", ""))
                else:
                    text = str(finding)
                if check_finding_matches(text, GROUND_TRUTH_KEYWORDS[pid]):
                    matched = True
                    matched_findings.append(text[:80])

            # Check prompted retraction fields
            for field in ["identified_error", "why_fatal", "correct_approach"]:
                text = d.get(field, "")
                if text and isinstance(text, str):
                    if check_finding_matches(text, GROUND_TRUTH_KEYWORDS[pid]):
                        matched = True
                        matched_findings.append(f"[{field}] {text[:80]}")

            for err in d.get("additional_errors", []):
                text = str(err) if err else ""
                if text and check_finding_matches(text, GROUND_TRUTH_KEYWORDS[pid]):
                    matched = True
                    matched_findings.append(f"[additional] {text[:80]}")

            if matched:
                model_found += 1
                print(f"    {pid}: FOUND")
            else:
                print(f"    {pid}: MISSED")

        if model_total:
            print(f"    => {model}: {model_found}/{model_total} = {100*model_found/model_total:.0f}%")
        pr_total_f += model_found
        pr_total_t += model_total

    pr_f, pr_t = pr_total_f, pr_total_t

print("\n" + "=" * 70)
print("SUMMARY: Ground Truth Detection Rate")
print("=" * 70)
if b1_t: print(f"  B1 (no rubric):        {b1_f}/{b1_t} = {100*b1_f/b1_t:.0f}%")
if b2_t: print(f"  B2 (+ rubric):         {b2_f}/{b2_t} = {100*b2_f/b2_t:.0f}%")
if gd_t: print(f"  Graduated dissent:     {gd_f}/{gd_t} = {100*gd_f/gd_t:.0f}%")
if pr_t:
    print(f"  Prompted (overall):    {pr_f}/{pr_t} = {100*pr_f/pr_t:.0f}%")
    for model in sorted(prompted_by_model.keys()):
        mdata = prompted_by_model[model]
        mf = sum(1 for pid in GROUND_TRUTH_KEYWORDS if pid in mdata and _prompted_match(mdata[pid], pid))
        mt = sum(1 for pid in GROUND_TRUTH_KEYWORDS if pid in mdata)
        if mt:
            print(f"    {model:>12s}:        {mf}/{mt} = {100*mf/mt:.0f}%")
