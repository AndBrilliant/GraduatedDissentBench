#!/usr/bin/env python3
"""
McNemar's exact test for paired ablation (B3 vs Graduated Dissent on the
same papers).

Inputs: a CSV with columns paper_id, condition_b3, condition_gd, where each
condition column holds 0/1 detection flags. Computes the discordant pair
counts and the exact p-value.

Usage:
    python analysis/mcnemar_test.py --csv data/paired_table.csv \
        --col-a condition_b3 --col-b condition_gd
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path
from typing import Tuple

import pandas as pd


def mcnemar_exact(b: int, c: int) -> float:
    """
    Two-sided exact McNemar test on discordant pair counts (b, c).
    Returns the two-sided p-value: P(|X - n/2| >= |b - n/2|) for X ~ Bin(n, 0.5),
    n = b + c.
    """
    n = b + c
    if n == 0:
        return 1.0
    # Binomial PMF under H0: X ~ Bin(n, 0.5)
    def pmf(k):
        return math.comb(n, k) / (2 ** n)

    # Two-sided p-value: sum of probabilities at points at least as extreme as min(b,c).
    k0 = min(b, c)
    tail = sum(pmf(k) for k in range(0, k0 + 1))
    p = 2 * tail
    if p > 1.0:
        p = 1.0
    return p


def from_paired_table(df: pd.DataFrame, col_a: str, col_b: str) -> Tuple[int, int, int, int, float]:
    """
    Compute (b: A=1,B=0  c: A=0,B=1  agree_yes  agree_no  p_value).
    'A' is taken as the baseline; 'B' is the comparison.
    """
    a = df[col_a].astype(int).to_numpy()
    b_col = df[col_b].astype(int).to_numpy()

    b = int(((a == 1) & (b_col == 0)).sum())  # A only
    c = int(((a == 0) & (b_col == 1)).sum())  # B only
    agree_yes = int(((a == 1) & (b_col == 1)).sum())
    agree_no = int(((a == 0) & (b_col == 0)).sum())
    p = mcnemar_exact(b, c)
    return b, c, agree_yes, agree_no, p


def main():
    p_arg = argparse.ArgumentParser()
    p_arg.add_argument("--csv", required=True, help="CSV with paper_id, condition_a, condition_b columns")
    p_arg.add_argument("--col-a", required=True, help="Baseline column (e.g. b3)")
    p_arg.add_argument("--col-b", required=True, help="Comparison column (e.g. gd)")
    args = p_arg.parse_args()

    df = pd.read_csv(args.csv)
    b, c, ay, an, p = from_paired_table(df, args.col_a, args.col_b)
    n = len(df)

    print(f"Paired McNemar exact test: {args.col_a} vs {args.col_b}")
    print(f"N papers: {n}")
    print(f"           {args.col_b}=1   {args.col_b}=0")
    print(f"  {args.col_a}=1   {ay:>5}     {b:>5}")
    print(f"  {args.col_a}=0   {c:>5}     {an:>5}")
    print()
    print(f"Discordant pairs: b={b} ({args.col_a} only), c={c} ({args.col_b} only)")
    print(f"Two-sided exact p-value: {p:.6f}")
    if b + c > 0:
        print(f"Direction: {c}/{b+c} discordant pairs favor {args.col_b}")


if __name__ == "__main__":
    main()
