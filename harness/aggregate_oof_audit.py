#!/usr/bin/env python3
"""
Aggregate the OOF audit and compare against the in-family audit.

Reads:
  - validation/retracted_paper_audit_oof/raw_responses.jsonl  (this run)
  - validation/retracted_paper_audit/raw_responses.jsonl       (in-family)
  - validation/retracted_paper_audit/raw_responses_opus_fillin.jsonl
    (in-family Opus follow-ups for findings where the original missed)

Computes:
  1. Per-finding match-majority votes for each audit (in-family vs OOF)
  2. Cohen's kappa between in-family and OOF majority verdicts
  3. Paper-level detection (retracted papers) and FP (controls) under
     both majority and unanimous OOF scoring
  4. Comparison table mirroring paper Table 3 with OOF columns added

Usage:
    python harness/aggregate_oof_audit.py [--partial]
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OOF_DIR = REPO / "validation" / "retracted_paper_audit_oof"
INF_DIR = REPO / "validation" / "retracted_paper_audit"
GT_CSV = REPO / "github" / "data" / "ground_truth.csv"


def load_responses(path: Path) -> dict:
    """Returns {(paper, cond, fi, event): [{model: ..., response: ...}]}"""
    out = {}
    if not path.exists():
        return out
    with path.open() as f:
        for line in f:
            r = json.loads(line)
            key = (r["paper_id"], r["condition"], r["finding_idx"], r["event"])
            out[key] = r["responses"]
    return out


def vote_match(responses: list[dict]) -> dict[str, bool | None]:
    """Per-model match vote. None for failed/parse-error responses."""
    votes = {}
    for r in responses:
        m = r["model"]
        resp = r.get("response", {})
        if isinstance(resp, dict) and not resp.get("error") \
                and not resp.get("parse_error"):
            votes[m] = bool(resp.get("match", False))
        else:
            votes[m] = None
    return votes


def two_model_majority(votes: dict[str, bool | None],
                        models: tuple[str, str] = ("grok", "mistral")
                        ) -> tuple[bool, bool]:
    """Returns (both_agree, either_agrees) for the chosen two models.
    None votes count as no-match."""
    vals = [bool(votes.get(m)) if votes.get(m) is not None else False
            for m in models]
    return (all(vals) and len(vals) == 2), any(vals)


def vote_severity(responses: list[dict]) -> dict[str, str | None]:
    votes = {}
    for r in responses:
        m = r["model"]
        resp = r.get("response", {})
        if isinstance(resp, dict) and not resp.get("error") \
                and not resp.get("parse_error"):
            votes[m] = resp.get("severity", None)
        else:
            votes[m] = None
    return votes


def majority_match(votes: dict[str, bool | None]) -> bool:
    return sum(1 for v in votes.values() if v is True) >= 2


def unanimous_match(votes: dict[str, bool | None]) -> bool:
    """All non-None votes are True, and we have ≥2 valid votes."""
    valid = [v for v in votes.values() if v is not None]
    return len(valid) >= 2 and all(valid)


def cohen_kappa(a: list[bool], b: list[bool]) -> float:
    """Cohen's kappa for two binary raters over the same items."""
    n = len(a)
    if n == 0:
        return 0.0
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pa1 = sum(1 for x in a if x) / n
    pb1 = sum(1 for x in b if x) / n
    pe = pa1 * pb1 + (1 - pa1) * (1 - pb1)
    if pe == 1.0:
        return 1.0
    return (po - pe) / (1 - pe)


def load_gt() -> dict[str, dict]:
    out = {}
    with GT_CSV.open() as f:
        for row in csv.DictReader(f):
            out[row["paper_id"]] = row
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--partial", action="store_true",
                   help="Allow incomplete Phase 2 (severity) data")
    p.add_argument("--out", default=str(OOF_DIR / "comparison.md"))
    args = p.parse_args()

    gt = load_gt()

    # Load OOF responses
    oof = load_responses(OOF_DIR / "raw_responses.jsonl")

    # Load in-family responses (raw + opus fillin)
    inf = load_responses(INF_DIR / "raw_responses.jsonl")
    inf_fill = load_responses(INF_DIR / "raw_responses_opus_fillin.jsonl")
    # Merge fillin into inf, but only filling missing or error responses
    for key, resps in inf_fill.items():
        if key in inf:
            # Replace any in-family Opus response that was a parse error
            existing = inf[key]
            for r in existing:
                if r["model"] == "opus":
                    resp = r.get("response", {})
                    if isinstance(resp, dict) and resp.get("error"):
                        # use fillin's opus instead
                        for fr in resps:
                            if fr["model"] == "opus":
                                r["response"] = fr["response"]
        else:
            inf[key] = resps

    # ─── Build per-finding match table for both audits ──────────────
    # Key: (paper, cond, fi). Each row has both audit majorities.
    rows = []
    all_keys = sorted(set((k[0], k[1], k[2]) for k in oof.keys()
                          if k[3] == "match"))
    n_inf_missing = 0
    for (pid, cond, fi) in all_keys:
        oof_resps = oof.get((pid, cond, fi, "match"), [])
        inf_resps = inf.get((pid, cond, fi, "match"), [])
        if not inf_resps:
            n_inf_missing += 1
            continue
        oof_votes = vote_match(oof_resps)
        inf_votes = vote_match(inf_resps)
        # 2-model OOF (Grok + Mistral): both-agree and either-agrees
        gm_both, gm_either = two_model_majority(oof_votes, ("grok", "mistral"))
        rows.append({
            "paper_id": pid,
            "condition": cond,
            "finding_idx": fi,
            "inf_votes": inf_votes,
            "oof_votes": oof_votes,
            "inf_maj": majority_match(inf_votes),
            "oof_maj": majority_match(oof_votes),  # 2/3 if all 3 voted
            "oof_unan": unanimous_match(oof_votes),
            "oof_2m_both": gm_both,
            "oof_2m_either": gm_either,
        })
    print(f"Findings cross-compared: {len(rows)}")
    print(f"Findings missing in-family data: {n_inf_missing}")

    # ─── Cohen's kappa (majority verdicts) ─────────────────────────
    a = [r["inf_maj"] for r in rows]
    b = [r["oof_maj"] for r in rows]
    kappa_maj = cohen_kappa(a, b)
    # Also kappa vs OOF-unanimous (stricter)
    c = [r["oof_unan"] for r in rows]
    kappa_unan = cohen_kappa(a, c)

    # Agreement breakdown
    both_t = sum(1 for r in rows if r["inf_maj"] and r["oof_maj"])
    both_f = sum(1 for r in rows if not r["inf_maj"] and not r["oof_maj"])
    inf_only = sum(1 for r in rows if r["inf_maj"] and not r["oof_maj"])
    oof_only = sum(1 for r in rows if not r["inf_maj"] and r["oof_maj"])
    n = len(rows)
    print(f"\nMajority agreement (n={n}):")
    print(f"  both match:       {both_t} ({both_t/n:.1%})")
    print(f"  both no-match:    {both_f} ({both_f/n:.1%})")
    print(f"  inf yes, oof no:  {inf_only}")
    print(f"  oof yes, inf no:  {oof_only}")
    print(f"  raw agreement:    {(both_t+both_f)/n:.1%}")
    print(f"  Cohen's kappa (majority vs majority): {kappa_maj:.3f}")
    print(f"  Cohen's kappa (in-family majority vs OOF unanimous): {kappa_unan:.3f}")

    # ─── Paper-level detection / FP (match-majority only) ──────────
    # For each (paper, condition), did any finding pass match-majority?
    by_pc_inf = defaultdict(bool)
    by_pc_oof_maj = defaultdict(bool)
    by_pc_oof_unan = defaultdict(bool)
    by_pc_oof_2m_both = defaultdict(bool)
    by_pc_oof_2m_either = defaultdict(bool)
    for r in rows:
        pc = (r["paper_id"], r["condition"])
        if r["inf_maj"]:
            by_pc_inf[pc] = True
        if r["oof_maj"]:
            by_pc_oof_maj[pc] = True
        if r["oof_unan"]:
            by_pc_oof_unan[pc] = True
        if r["oof_2m_both"]:
            by_pc_oof_2m_both[pc] = True
        if r["oof_2m_either"]:
            by_pc_oof_2m_either[pc] = True

    def status(pid: str) -> str:
        cat = gt.get(pid, {}).get("category", "")
        return "retracted" if cat == "retracted" else \
               ("control" if cat in ("matched_control", "hard_negative")
                else "other")

    # Paper-level table — match-majority on retracted papers (detection),
    # but separately track 2-model OOF scoring (Grok + Mistral) since Gemini
    # failed on ~55% of calls.
    print("\n── Paper-level match aggregates (any finding match-confirmed) ──")
    print("                IN-FAM   OOF-3m-maj   OOF-3m-unan   OOF-2m-both   OOF-2m-either")
    print("                det/FP    det/FP        det/FP         det/FP         det/FP")
    table_rows = []
    for cond in ("B1", "B2", "B3", "GD"):
        det_inf = sum(1 for pid in gt
                      if status(pid) == "retracted"
                      and by_pc_inf.get((pid, cond), False))
        fp_inf = sum(1 for pid in gt
                     if status(pid) == "control"
                     and by_pc_inf.get((pid, cond), False))
        det_oof = sum(1 for pid in gt
                      if status(pid) == "retracted"
                      and by_pc_oof_maj.get((pid, cond), False))
        fp_oof = sum(1 for pid in gt
                     if status(pid) == "control"
                     and by_pc_oof_maj.get((pid, cond), False))
        det_uno = sum(1 for pid in gt
                      if status(pid) == "retracted"
                      and by_pc_oof_unan.get((pid, cond), False))
        fp_uno = sum(1 for pid in gt
                     if status(pid) == "control"
                     and by_pc_oof_unan.get((pid, cond), False))
        det_2b = sum(1 for pid in gt
                     if status(pid) == "retracted"
                     and by_pc_oof_2m_both.get((pid, cond), False))
        fp_2b = sum(1 for pid in gt
                    if status(pid) == "control"
                    and by_pc_oof_2m_both.get((pid, cond), False))
        det_2e = sum(1 for pid in gt
                     if status(pid) == "retracted"
                     and by_pc_oof_2m_either.get((pid, cond), False))
        fp_2e = sum(1 for pid in gt
                    if status(pid) == "control"
                    and by_pc_oof_2m_either.get((pid, cond), False))
        line = (f"  {cond:3s}           "
                f"{det_inf:>2d}/{fp_inf:>2d}    "
                f"{det_oof:>2d}/{fp_oof:>2d}        "
                f"{det_uno:>2d}/{fp_uno:>2d}         "
                f"{det_2b:>2d}/{fp_2b:>2d}         "
                f"{det_2e:>2d}/{fp_2e:>2d}")
        print(line)
        table_rows.append({
            "condition": cond,
            "det_inf": det_inf, "fp_inf": fp_inf,
            "det_oof_maj": det_oof, "fp_oof_maj": fp_oof,
            "det_oof_unan": det_uno, "fp_oof_unan": fp_uno,
            "det_oof_2m_both": det_2b, "fp_oof_2m_both": fp_2b,
            "det_oof_2m_either": det_2e, "fp_oof_2m_either": fp_2e,
        })

    # ─── Severity-level (RW-justified) if Phase 2 data present ─────
    sev_keys = [k for k in oof.keys() if k[3] == "severity"]
    n_sev = len(sev_keys)
    print(f"\nPhase 2 severity events present: {n_sev}")

    sev_complete = True
    rw_section = ""
    if not args.partial and n_sev < 388 * 0.95:
        sev_complete = False
        print("(Phase 2 still running; skipping RW-severity table.)")
    else:
        # For OOF 2-model severity: we need both Grok and Mistral to agree
        # match=True AND both vote RW. (Sequential gate: match-2m-both then
        # severity-2m-both.) Also report 3-model OOF-majority severity for
        # findings where Gemini happened to complete.
        rw_2m_by_pc_oof = defaultdict(bool)   # Grok+Mistral both
        rw_3m_by_pc_oof = defaultdict(bool)   # 3-model majority
        rw_by_pc_inf = defaultdict(bool)
        for r in rows:
            sev_resps = oof.get((r["paper_id"], r["condition"],
                                  r["finding_idx"], "severity"), [])
            sv = vote_severity(sev_resps)
            # 2-model OOF rule: Grok and Mistral both said match (in match
            # phase), AND both vote RW in severity phase
            if r["oof_2m_both"]:
                grok_rw = sv.get("grok") == "RETRACTION-WORTHY"
                mistral_rw = sv.get("mistral") == "RETRACTION-WORTHY"
                if grok_rw and mistral_rw:
                    rw_2m_by_pc_oof[(r["paper_id"], r["condition"])] = True
            # 3-model OOF rule: 3/3 majority match, then 2/3 vote RW
            if r["oof_maj"]:
                rw_count = sum(1 for v in sv.values()
                                if v == "RETRACTION-WORTHY")
                if rw_count >= 2:
                    rw_3m_by_pc_oof[(r["paper_id"], r["condition"])] = True
        for r in rows:
            if not r["inf_maj"]:
                continue
            sev_resps = inf.get((r["paper_id"], r["condition"],
                                  r["finding_idx"], "severity"), [])
            sv = vote_severity(sev_resps)
            rw_count = sum(1 for v in sv.values() if v == "RETRACTION-WORTHY")
            if rw_count >= 2:
                rw_by_pc_inf[(r["paper_id"], r["condition"])] = True

        print("\n── Paper-level RW-severity aggregates (severity confirmed = RW) ──")
        print("                IN-FAM   OOF-3m-maj   OOF-2m-both")
        print("                det/FP    det/FP        det/FP")
        rw_table_rows = []
        for cond in ("B1", "B2", "B3", "GD"):
            det_inf_rw = sum(1 for pid in gt
                              if status(pid) == "retracted"
                              and rw_by_pc_inf.get((pid, cond), False))
            fp_inf_rw = sum(1 for pid in gt
                             if status(pid) == "control"
                             and rw_by_pc_inf.get((pid, cond), False))
            det_3m_rw = sum(1 for pid in gt
                             if status(pid) == "retracted"
                             and rw_3m_by_pc_oof.get((pid, cond), False))
            fp_3m_rw = sum(1 for pid in gt
                            if status(pid) == "control"
                            and rw_3m_by_pc_oof.get((pid, cond), False))
            det_2m_rw = sum(1 for pid in gt
                             if status(pid) == "retracted"
                             and rw_2m_by_pc_oof.get((pid, cond), False))
            fp_2m_rw = sum(1 for pid in gt
                            if status(pid) == "control"
                            and rw_2m_by_pc_oof.get((pid, cond), False))
            line = (f"  {cond:3s}           "
                    f"{det_inf_rw:>2d}/{fp_inf_rw:>2d}    "
                    f"{det_3m_rw:>2d}/{fp_3m_rw:>2d}        "
                    f"{det_2m_rw:>2d}/{fp_2m_rw:>2d}")
            print(line)
            rw_table_rows.append({
                "condition": cond,
                "det_inf_rw": det_inf_rw, "fp_inf_rw": fp_inf_rw,
                "det_oof_3m_rw": det_3m_rw, "fp_oof_3m_rw": fp_3m_rw,
                "det_oof_2m_rw": det_2m_rw, "fp_oof_2m_rw": fp_2m_rw,
            })

        rw_section = "\n## Paper-level RW-severity aggregates (severity-majority = RETRACTION-WORTHY)\n\n"
        rw_section += ("In-family uses Opus + GPT-5.4 + DeepSeek (3-model). "
                        "OOF-3m uses Gemini + Grok + Mistral (Gemini failed on "
                        "~55% of calls; this column reflects only the 768 "
                        "findings where Gemini did complete). OOF-2m uses "
                        "Grok + Mistral both-agree on the full 1318 findings.\n\n")
        rw_section += ("| Condition | In-family det | In-family FP | "
                        "OOF-3m det | OOF-3m FP | OOF-2m det | OOF-2m FP |\n")
        rw_section += "|---|---:|---:|---:|---:|---:|---:|\n"
        for r in rw_table_rows:
            rw_section += (f"| {r['condition']} | "
                            f"{r['det_inf_rw']}/10 | {r['fp_inf_rw']}/19 | "
                            f"{r['det_oof_3m_rw']}/10 | {r['fp_oof_3m_rw']}/19 | "
                            f"{r['det_oof_2m_rw']}/10 | {r['fp_oof_2m_rw']}/19 |\n")

    # ─── Markdown output ───────────────────────────────────────────
    md = []
    md.append("# Out-of-family audit: comparison with in-family audit\n")
    md.append("Audit models:\n")
    md.append("- **In-family**: GPT-5.4, Claude Opus 4.6, DeepSeek V3.2\n")
    md.append("- **Out-of-family**: Gemini 2.5 Pro, xAI Grok 4 Fast Reasoning, "
              "Mistral Large 2\n\n")
    if not sev_complete:
        md.append(f"_⚠ Partial: Phase 2 severity audit is still running "
                  f"({n_sev}/388 done). The match-majority section below is "
                  f"complete; the RW-severity section will populate once "
                  f"Phase 2 finishes._\n\n")

    md.append("## Finding-level concordance\n")
    md.append(f"- Findings cross-compared: **{n}**\n")
    md.append(f"- Both audits ⇒ match: {both_t} ({both_t/n:.1%})\n")
    md.append(f"- Both audits ⇒ no-match: {both_f} ({both_f/n:.1%})\n")
    md.append(f"- In-family yes, OOF no: {inf_only}\n")
    md.append(f"- OOF yes, in-family no: {oof_only}\n")
    md.append(f"- **Raw agreement: {(both_t+both_f)/n:.1%}**\n")
    md.append(f"- **Cohen's kappa (majority vs majority): {kappa_maj:.3f}**\n")
    md.append(f"- Cohen's kappa (in-family majority vs OOF unanimous): {kappa_unan:.3f}\n\n")

    md.append("## Paper-level audit-match aggregates (match-majority only)\n")
    md.append("Each cell: detection on retracted papers / false positives on probative controls.\n\n")
    md.append("| Condition | In-family det | In-family FP | "
              "OOF (2/3 maj) det | OOF (2/3 maj) FP | "
              "OOF (3/3 unan) det | OOF (3/3 unan) FP |\n")
    md.append("|---|---:|---:|---:|---:|---:|---:|\n")
    for r in table_rows:
        md.append(f"| {r['condition']} | "
                   f"{r['det_inf']}/10 | {r['fp_inf']}/19 | "
                   f"{r['det_oof_maj']}/10 | {r['fp_oof_maj']}/19 | "
                   f"{r['det_oof_unan']}/10 | {r['fp_oof_unan']}/19 |\n")

    if sev_complete:
        md.append(rw_section)

    md.append("\n## Headline question\n\n")
    md.append("> Does the OOF audit support the paper's specificity claim "
              "(GD has the fewest false-positive RW classifications)?\n\n")
    md.append("Read off the table above. If GD's OOF-FP column is ≤ B3's "
              "and ≤ B2's, the claim holds under the independent audit.\n")

    out_path = Path(args.out)
    out_path.write_text("".join(md), encoding="utf-8")
    print(f"\n[saved to {out_path}]")


if __name__ == "__main__":
    main()
