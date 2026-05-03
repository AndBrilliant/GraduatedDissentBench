#!/usr/bin/env python3
"""Inspect SPOT metadata + parsed splits to understand structure."""
import json
from pathlib import Path
import pandas as pd

REPO = Path(__file__).resolve().parent.parent
META = REPO / "data" / "spot" / "metadata" / "spot_metadata_train.parquet"
PARSED = REPO / "data" / "spot" / "parsed" / "spot_parsed_train.parquet"


def main():
    meta = pd.read_parquet(META)
    parsed = pd.read_parquet(PARSED)

    print(f"=== METADATA ({len(meta)} rows) ===")
    print(f"columns: {list(meta.columns)}")
    print(f"\nunique titles in metadata: {meta['title'].nunique()}")
    print(f"unique titles in parsed:   {parsed['title'].nunique()}")
    print(f"\nerror_category value counts (metadata, all 91 errors):")
    print(meta["error_category"].value_counts().to_string())
    print(f"\npaper_category value counts:")
    print(meta["paper_category"].value_counts().to_string())
    print(f"\nerror_severity distribution:")
    print(meta["error_severity"].value_counts().to_string())
    print(f"\nerrors per paper distribution (metadata):")
    print(meta.groupby("title").size().value_counts().sort_index().to_string())

    print(f"\n=== PARSED ({len(parsed)} rows) ===")
    print(f"columns: {list(parsed.columns)}")
    print(f"\nerror_category in parsed (subset):")
    print(parsed["error_category"].value_counts().to_string())
    print(f"\npaper_content length stats (chars):")
    print(parsed["paper_content"].str.len().describe().to_string())
    print(f"error_local_content length stats (chars):")
    print(parsed["error_local_content"].str.len().describe().to_string())

    # Which papers in metadata have parsed content?
    titles_meta = set(meta["title"].unique())
    titles_parsed = set(parsed["title"].unique())
    missing = titles_meta - titles_parsed
    print(f"\npapers in metadata but NOT in parsed: {len(missing)}")
    for t in list(missing)[:10]:
        print(f"  - {t[:80]}")

    # Sample one row
    print("\n=== SAMPLE METADATA ROW 0 ===")
    row = meta.iloc[0]
    for col in meta.columns:
        val = str(row[col])
        if len(val) > 200:
            val = val[:200] + " ...[truncated]"
        print(f"  {col}: {val}")

    print("\n=== SAMPLE PARSED ROW 0 (paper_content truncated) ===")
    row = parsed.iloc[0]
    for col in parsed.columns:
        val = str(row[col])
        if col in ("paper_content", "error_local_content"):
            val = f"[{len(val)} chars] " + val[:200].replace("\n", " ") + " ..."
        elif len(val) > 200:
            val = val[:200] + " ...[truncated]"
        print(f"  {col}: {val}")


if __name__ == "__main__":
    main()
