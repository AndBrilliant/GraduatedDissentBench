#!/usr/bin/env python3
"""
Download the SPOT benchmark from HuggingFace.

Saves:
- data/spot/metadata/spot_metadata.parquet  (annotations: title, paper_category,
  error_category, error_location, error_severity, error_annotation, ...)
- data/spot/parsed/spot_parsed.parquet      (parsed paper contents)

Both datasets live at:
  https://huggingface.co/datasets/amphora/SPOT-MetaData
  https://huggingface.co/datasets/amphora/SPOT
"""
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
META_DIR = REPO / "data" / "spot" / "metadata"
PARSED_DIR = REPO / "data" / "spot" / "parsed"
META_DIR.mkdir(parents=True, exist_ok=True)
PARSED_DIR.mkdir(parents=True, exist_ok=True)


def main():
    from datasets import load_dataset

    print("Loading amphora/SPOT-MetaData ...")
    meta = load_dataset("amphora/SPOT-MetaData")
    for split, ds in meta.items():
        out = META_DIR / f"spot_metadata_{split}.parquet"
        ds.to_parquet(str(out))
        print(f"  {split}: {len(ds)} rows -> {out.relative_to(REPO)}")
        print(f"    columns: {list(ds.features.keys())}")

    print("\nLoading amphora/SPOT (parsed contents) ...")
    try:
        parsed = load_dataset("amphora/SPOT")
        for split, ds in parsed.items():
            out = PARSED_DIR / f"spot_parsed_{split}.parquet"
            ds.to_parquet(str(out))
            print(f"  {split}: {len(ds)} rows -> {out.relative_to(REPO)}")
            print(f"    columns: {list(ds.features.keys())}")
    except Exception as e:
        # SPOT papers may be PDFs/files instead of a tabular dataset; fall back to snapshot_download
        print(f"  load_dataset failed: {e}")
        print("  falling back to snapshot_download ...")
        from huggingface_hub import snapshot_download
        path = snapshot_download(
            repo_id="amphora/SPOT",
            repo_type="dataset",
            local_dir=str(PARSED_DIR / "raw"),
        )
        print(f"  downloaded snapshot to {path}")


if __name__ == "__main__":
    sys.exit(main() or 0)
