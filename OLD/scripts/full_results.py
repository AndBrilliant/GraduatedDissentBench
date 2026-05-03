#!/usr/bin/env python3
"""Complete v6 results analysis."""
import json, glob, os, statistics

BASE = os.path.expanduser("~/Desktop/Academic/graduated_dissent_bench_v6")

def load_results(pattern):
    results = {}
    for f in sorted(glob.glob(os.path.join(BASE, pattern))):
        with open(f) as fh:
            d = json.load(fh)
        pid = d.get("paper_id", "?")
        results[pid] = d
    return results

b1 = load_results("results/baseline_B1/*_B1_*.json")
b2 = load_results("results/baseline_B1/*_B2_*.json")
gd = load_results("results/primary/*.json")

def cat(pid):
    if pid.startswith("R"): return "Retracted"
    if pid.startswith("C"): return "Control"
    if pid.startswith("HN"): return "Hard-Neg"
    if pid.startswith("W"): return "Wildcard"
    return "?"

def get_rw(d, baseline=False):
    if baseline:
        findings = d.get("findings", d.get("specific_errors_found", []))
        return sum(1 for f in findings if isinstance(f, dict) and f.get("severity") == "RETRACTION-WORTHY")
    else:
        return d.get("severity_counts", {}).get("RETRACTION-WORTHY", 0)

# === B2 FALSE POSITIVES ===
print("=" * 70)
print("B2 (SINGLE MODEL + RUBRIC) — FALSE POSITIVES ON NON-RETRACTED")
print("=" * 70)
b2_fp = 0
b2_non = 0
for pid in sorted(b2):
    if pid.startswith("R"): continue
    rw = get_rw(b2[pid], baseline=True)
    b2_non += 1
    if rw > 0:
        b2_fp += 1
        print(f"  FALSE POSITIVE: {pid} ({cat(pid)}) — {rw} RW")
if b2_fp == 0:
    print("  NONE")
print(f"\n  B2 false positive rate: {b2_fp}/{b2_non} = {100*b2_fp/b2_non:.0f}%")

# === GD FALSE POSITIVES ===
print("\n" + "=" * 70)
print("GRADUATED DISSENT — FALSE POSITIVES ON NON-RETRACTED")
print("=" * 70)
gd_fp = 0
gd_non = 0
for pid in sorted(gd):
    if pid.startswith("R"): continue
    rw = get_rw(gd[pid])
    gd_non += 1
    if rw > 0:
        gd_fp += 1
        print(f"  FALSE POSITIVE: {pid} ({cat(pid)}) — {rw} RW")
if gd_fp == 0:
    print("  NONE")
print(f"\n  GD false positive rate: {gd_fp}/{gd_non} = {100*gd_fp/gd_non:.0f}%")

# === SENSITIVITY ===
print("\n" + "=" * 70)
print("SENSITIVITY ON RETRACTED PAPERS (>=1 RW finding)")
print("=" * 70)
header = f"  {'Paper':6s}  {'B2':>4s}  {'GD':>4s}"
print(header)
print("  " + "-" * 20)
b2_det = gd_det = n_ret = 0
for pid in sorted(gd):
    if not pid.startswith("R"): continue
    n_ret += 1
    b2_rw = get_rw(b2.get(pid, {}), baseline=True)
    gd_rw = get_rw(gd[pid])
    if b2_rw > 0: b2_det += 1
    if gd_rw > 0: gd_det += 1
    b2_tag = str(b2_rw) if b2_rw > 0 else "-"
    gd_tag = str(gd_rw) if gd_rw > 0 else "-"
    print(f"  {pid:6s}  {b2_tag:>4s}  {gd_tag:>4s}")

print(f"\n  B2 sensitivity: {b2_det}/{n_ret} = {100*b2_det/n_ret:.0f}%")
print(f"  GD sensitivity: {gd_det}/{n_ret} = {100*gd_det/n_ret:.0f}%")

# === FULL TABLE ===
print("\n" + "=" * 70)
print("GRADUATED DISSENT — ALL 34 PAPERS")
print("=" * 70)
header = f"  {'Paper':6s}  {'Category':10s}  {'RW':>3s}  {'MR':>3s}  {'Mi':>3s}  {'Score':>5s}"
print(header)
print("  " + "-" * 40)

by_cat = {}
for pid in sorted(gd):
    sc = gd[pid].get("severity_counts", {})
    rw = sc.get("RETRACTION-WORTHY", 0)
    mr = sc.get("MAJOR-REVISION", 0)
    mi = sc.get("MINOR", 0)
    score = rw * 3 + mr * 2 + mi
    c = cat(pid)
    print(f"  {pid:6s}  {c:10s}  {rw:3d}  {mr:3d}  {mi:3d}  {score:5d}")
    by_cat.setdefault(c, []).append({"rw": rw, "mr": mr, "mi": mi, "score": score})

print("\n  " + "-" * 40)
for c in ["Retracted", "Control", "Hard-Neg", "Wildcard"]:
    if c not in by_cat: continue
    items = by_cat[c]
    print(f"  {'AVG ' + c:15s}  {statistics.mean([i['rw'] for i in items]):3.1f}  "
          f"{statistics.mean([i['mr'] for i in items]):3.1f}  "
          f"{statistics.mean([i['mi'] for i in items]):3.1f}  "
          f"{statistics.mean([i['score'] for i in items]):5.1f}")

# === HEADLINE ===
print("\n" + "=" * 70)
print("HEADLINE COMPARISON")
print("=" * 70)
print(f"  B2 (single model + rubric):  sensitivity {b2_det}/{n_ret}, FP {b2_fp}/{b2_non}")
print(f"  GD (graduated dissent):      sensitivity {gd_det}/{n_ret}, FP {gd_fp}/{gd_non}")
if b2_fp > gd_fp:
    print(f"\n  Graduated dissent eliminates {b2_fp - gd_fp} false positive(s)")
