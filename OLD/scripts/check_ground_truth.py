#!/usr/bin/env python3
"""Check if model findings match ground truth retraction causes."""
import json, glob, os

BASE = os.path.expanduser("~/Desktop/Academic/graduated_dissent_bench_v6")

ground_truth = {
    "R01": "Coding errors: missing data coded as asymptomatic, incorrect date cutoffs, age range violations, impossible HRs of 0.00",
    "R02": "Flawed Uzbekistan GDP data, results insignificant when corrected for spatial autocorrelation",
    "R03": "Post-hoc analysis presented as preregistered, selection of outcomes with knowledge of data",
    "R04": "Unreplicable analyses, wrong stats tests (t-test not repeated measures), implausible baseline values",
    "R05": "Randomization failed - group sizes dont match stated 1:2 ratio (3900 each instead of 2:1)",
    "R10": "Selection bias - only included patients with prior vitamin D testing, 14-730 day measurement gap",
    "R11": "Mediation analysis between causally related stress constructs is conceptually circular",
    "R19": "Results not reproducible from raw data, unclear what analysis was performed",
    "R24": "Incorrect number of primary outcome events reported, errors in population denominator",
    "R25": "ICD code logic error OR vs AND for Parkinson+dementia, added 5413 false cases",
}

for results_dir in ["results/primary", "results/authors_choice"]:
    full_dir = os.path.join(BASE, results_dir)
    if not os.path.exists(full_dir):
        continue

    print(f"\n{'#'*70}")
    print(f"# {results_dir}")
    print(f"{'#'*70}")

    for f in sorted(glob.glob(os.path.join(full_dir, "R*.json"))):
        with open(f) as fh:
            d = json.load(fh)
        pid = d.get("paper_id")
        if pid not in ground_truth:
            continue

        print(f"\n{'='*70}")
        print(f"{pid} | GROUND TRUTH: {ground_truth[pid]}")
        print(f"{'='*70}")

        findings = d.get("findings", [])
        for finding in findings:
            if isinstance(finding, dict):
                sev = finding.get("severity", "?")
                desc = str(finding.get("finding", ""))[:140]
                marker = ">>>" if sev == "RETRACTION-WORTHY" else "   "
                print(f"  {marker} [{sev}] {desc}")

        print(f"  --- {len(findings)} findings total ---")
