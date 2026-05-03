#!/usr/bin/env python3
"""
Build the validation/ package: stable paper IDs (paper_001..paper_020),
copied raw outputs, ground-truth + metadata CSVs, and a sanitized
schema (no internal labels in the per-output JSONs).

The output is a self-contained tree that can be evaluated independently
without reading the rest of the repo.
"""
from __future__ import annotations

import csv
import json
import re
import shutil
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
SWEEP = REPO / "data" / "spot" / "outputs" / "pilot_n10"
TEXT_DETECT = REPO / "data" / "spot" / "text_detectable"
SAMPLE = SWEEP / "sample.csv"
VALID = REPO / "validation"
META_PARQUET = REPO / "data" / "spot" / "metadata" / "spot_metadata_train.parquet"

OUT_RAW = VALID / "raw_outputs"
OUT_GT = VALID / "ground_truth"
OUT_CONFIG = VALID / "config"


def safe_to_id(safe_doi_list: list[str]) -> dict[str, str]:
    """Map safe_doi -> paper_001..paper_020 in alphabetic order."""
    sorted_dois = sorted(safe_doi_list)
    return {doi: f"paper_{i+1:03d}" for i, doi in enumerate(sorted_dois)}


def sanitize_output(blob: dict, paper_id: str) -> dict:
    """Strip internal labels (which embed safe_doi) from a stored output."""
    blob = json.loads(json.dumps(blob))  # deep copy
    blob["paper_id"] = paper_id
    # Scrub label fields in meta.calls (they embed the original safe_doi)
    meta = blob.get("meta") or {}
    for c in meta.get("calls", []) or []:
        lbl = c.get("label", "")
        # labels look like "<safe_doi>/<cond>/<role>" — replace prefix
        if "/" in lbl:
            c["label"] = paper_id + "/" + lbl.split("/", 1)[1]
    return blob


def main():
    sample = pd.read_csv(SAMPLE)
    safe_dois = sample["safe_doi"].tolist()
    if len(safe_dois) != 20:
        print(f"warning: expected 20 papers in sample, got {len(safe_dois)}")

    id_map = safe_to_id(safe_dois)

    # 1) Copy raw outputs into stable paper_NNN directories
    for safe_doi in safe_dois:
        new_id = id_map[safe_doi]
        new_dir = OUT_RAW / new_id
        new_dir.mkdir(parents=True, exist_ok=True)
        for cond_lower in ("b1", "b2", "b3", "gd"):
            src = SWEEP / safe_doi / f"{cond_lower}.json"
            if not src.exists():
                print(f"!! missing {src}")
                continue
            blob = json.loads(src.read_text(encoding="utf-8"))
            blob = sanitize_output(blob, paper_id=new_id)
            dst = new_dir / f"{cond_lower.upper()}.json"
            dst.write_text(json.dumps(blob, indent=2, ensure_ascii=False), encoding="utf-8")

    # 2) Build ground_truth/spot_ground_truth.csv
    # Pull SPOT annotations for the 20 papers from spot_metadata_train.parquet
    meta = pd.read_parquet(META_PARQUET)
    gt_rows = []
    for safe_doi in safe_dois:
        new_id = id_map[safe_doi]
        gt_path = TEXT_DETECT / safe_doi / "ground_truth.json"
        if not gt_path.exists():
            print(f"!! missing ground_truth.json for {safe_doi}")
            continue
        gt = json.loads(gt_path.read_text(encoding="utf-8"))
        for i, err in enumerate(gt.get("errors", []), start=1):
            gt_rows.append({
                "paper_id": new_id,
                "annotation_index": i,
                "error_category": err.get("category", ""),
                "error_severity": err.get("severity", ""),
                "error_location": err.get("location", ""),
                "error_annotation": err.get("description", ""),
                "detectability": err.get("detectability", ""),
            })

    OUT_GT.mkdir(parents=True, exist_ok=True)
    gt_df = pd.DataFrame(gt_rows)
    gt_df.to_csv(OUT_GT / "spot_ground_truth.csv", index=False)
    print(f"Wrote ground_truth.csv: {len(gt_df)} rows across {gt_df['paper_id'].nunique()} papers")

    # 3) Build config/paper_metadata.csv
    meta_rows = []
    for safe_doi in safe_dois:
        new_id = id_map[safe_doi]
        paper_dir = TEXT_DETECT / safe_doi
        # Anonymization status: paper.raw.txt exists iff paper was anonymized
        # (we backed up the original before overwriting paper.txt with anon).
        anonymized = (paper_dir / "paper.raw.txt").exists()
        # Pull row from sample.csv
        s = sample[sample["safe_doi"] == safe_doi].iloc[0]
        meta_rows.append({
            "paper_id": new_id,
            "anonymized": "yes" if anonymized else "no",
            "paper_category": s["paper_category"],
            "n_errors_total": int(s["n_errors_total"]),
            "n_text_detectable": int(s["n_text"]),
            "n_partial_detectable": int(s["n_partial"]),
            "n_figure_only_excluded": int(s["n_figure_only"]),
            "paper_text_chars": int(s["paper_text_chars"]),
            "primary_severity": s["primary_severity"],
        })
    OUT_CONFIG.mkdir(parents=True, exist_ok=True)
    meta_df = pd.DataFrame(meta_rows)
    meta_df.to_csv(OUT_CONFIG / "paper_metadata.csv", index=False)
    print(f"Wrote paper_metadata.csv: {len(meta_df)} rows")
    n_anon = (meta_df["anonymized"] == "yes").sum()
    n_raw = (meta_df["anonymized"] == "no").sum()
    print(f"  anonymized: {n_anon}, un-anonymized: {n_raw}")

    # 4) Build config/models_used.json
    models_cfg = {
        "models": {
            "GPT-5.4": {
                "api_id": "gpt-5.4",
                "provider": "OpenAI",
                "endpoint": "https://api.openai.com/v1/chat/completions",
                "max_completion_tokens": 4096,
                "temperature": "provider default (1.0)",
                "role": "Prover A; sole reviewer for B1 and B2",
            },
            "DeepSeek V3.2": {
                "api_id": "deepseek-chat",
                "provider": "DeepSeek",
                "endpoint": "https://api.deepseek.com/chat/completions",
                "max_tokens": 4096,
                "temperature": "provider default (1.0)",
                "role": "Prover B; judge in graduated dissent",
            },
            "Claude Opus 4.6": {
                "api_id": "claude-opus-4-6",
                "provider": "Anthropic",
                "endpoint": "https://api.anthropic.com/v1/messages",
                "max_tokens": 4096,
                "temperature": "provider default (1.0)",
                "role": "Arbiter in B3 and GD",
            },
            "GPT-5.4 (judge in scoring)": {
                "api_id": "gpt-5.4",
                "provider": "OpenAI",
                "max_completion_tokens": 4096,
                "temperature": 0,
                "role": "LLM-as-judge for matching predictions to SPOT annotations",
            },
        },
        "thresholds": {
            "theta_accept": 0.90,
            "theta_noise": 0.15,
            "comment": "Graduated dissent escalation: L0 if agreement>=0.90, L1 if SNR=(1-agreement)/theta_noise<1, L2 otherwise (steelman exchange triggered).",
        },
        "data_sources": {
            "spot_metadata": "https://huggingface.co/datasets/amphora/SPOT-MetaData",
            "spot_parsed": "https://huggingface.co/datasets/amphora/SPOT",
            "spot_evaluation_code": "https://github.com/guijinSON/SPOT",
        },
        "id_mapping_note": "Original SPOT DOIs were renamed paper_001..paper_020 (alphabetic order) for this validation package; the mapping is in config/id_mapping.csv.",
    }
    (OUT_CONFIG / "models_used.json").write_text(
        json.dumps(models_cfg, indent=2), encoding="utf-8"
    )

    # 5) id_mapping.csv (visible — evaluators may want to look up the original)
    mapping_df = pd.DataFrame(
        [{"paper_id": v, "original_safe_doi": k} for k, v in id_map.items()]
    ).sort_values("paper_id")
    mapping_df.to_csv(OUT_CONFIG / "id_mapping.csv", index=False)

    print("\nValidation package built. Counts:")
    print(f"  paper directories: {len(list(OUT_RAW.iterdir()))}")
    print(f"  output files: {sum(1 for _ in OUT_RAW.glob('*/*.json'))}")
    print(f"  ground truth rows: {len(gt_df)}")
    print(f"  metadata rows: {len(meta_df)}")


if __name__ == "__main__":
    main()
