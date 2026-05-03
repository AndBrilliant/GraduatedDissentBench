#!/usr/bin/env python3
"""Compare B1/B2 baseline findings to graduated dissent findings."""
import json, glob, os

BASE = os.path.expanduser("~/Desktop/Academic/graduated_dissent_bench_v6")

ground_truth = {
    "R01": "HRs of 0.00, coding errors, age range violations",
    "R04": "Wrong stats test (t-test not repeated measures), implausible values",
    "C01": "(control - should have no retraction-worthy errors)",
    "C04": "(control - should have no retraction-worthy errors)",
}

for pid in ["R01", "R04", "C01", "C04"]:
    print("\n" + "=" * 70)
    print(f"{pid} | Ground truth: {ground_truth.get(pid, '?')}")
    print("=" * 70)

    # B1 — no rubric
    b1_files = glob.glob(f"{BASE}/results/baseline_B1/{pid}_B1_*.json")
    if b1_files:
        with open(b1_files[0]) as f:
            d = json.load(f)
        findings = d.get("specific_errors_found", [])
        print(f"\n  B1 (single model, no rubric): {len(findings)} findings")
        for finding in findings[:6]:
            desc = str(finding)[:130]
            print(f"    - {desc}")
        if len(findings) > 6:
            print(f"    ... ({len(findings)} total)")

    # B2 — with rubric
    b2_files = glob.glob(f"{BASE}/results/baseline_B1/{pid}_B2_*.json")
    if b2_files:
        with open(b2_files[0]) as f:
            d = json.load(f)
        findings = d.get("findings", d.get("specific_errors_found", []))
        rw = sum(1 for f in findings if isinstance(f, dict) and f.get("severity") == "RETRACTION-WORTHY")
        print(f"\n  B2 (single model + rubric): {len(findings)} findings, {rw} retraction-worthy")
        for finding in findings[:6]:
            if isinstance(finding, dict):
                sev = finding.get("severity", "?")
                desc = str(finding.get("finding", ""))[:110]
                print(f"    [{sev}] {desc}")

    # Graduated dissent
    gd_files = glob.glob(f"{BASE}/results/primary/{pid}_gpt*.json")
    if gd_files:
        with open(gd_files[0]) as f:
            d = json.load(f)
        sc = d.get("severity_counts", {})
        rw = sc.get("RETRACTION-WORTHY", 0)
        mr = sc.get("MAJOR-REVISION", 0)
        mi = sc.get("MINOR", 0)
        findings = d.get("findings", [])
        print(f"\n  GRADUATED DISSENT: {len(findings)} findings (RW={rw} MR={mr} Mi={mi})")
