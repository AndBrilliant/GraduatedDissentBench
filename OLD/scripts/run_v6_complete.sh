#!/bin/bash
# v6 Complete Benchmark
# 1. Quick B1 baseline on 4 papers (illustrative)
# 2. Primary graduated dissent on all 34 papers
# Runs independently on photek overnight.

set -e
export PATH=/opt/homebrew/bin:$PATH
export ANTHROPIC_API_KEY="$(cat ~/.keys/anthropic)"
export OPENAI_API_KEY="$(cat ~/.keys/openai)"
export DEEPSEEK_API_KEY="$(cat ~/.keys/deepseek)"

BASE=~/Desktop/Academic/graduated_dissent_bench_v6
ANON="$BASE/dataset/anonymized"
SCRIPTS="$BASE/scripts"
LOG="$BASE/results/complete_run.log"

mkdir -p "$BASE/results/baseline_B1" "$BASE/results/primary"

echo "=== v6 BENCHMARK START at $(date) ===" | tee "$LOG"

# ══════════════════════════════════════════════════════════════
# B1: Illustrative baseline — 4 papers only
# Shows that single-model review doesn't discriminate
# ══════════════════════════════════════════════════════════════
echo "" | tee -a "$LOG"
echo "=== B1: Single model baseline (4 papers) ===" | tee -a "$LOG"

for pid in R01 R04 C01 C04; do
    paper="$ANON/${pid}_anon.txt"
    [ -f "$paper" ] || continue
    echo "$(date): B1 $pid" | tee -a "$LOG"
    python3 "$SCRIPTS/run_baseline.py" \
        --paper "$paper" --paper-id "$pid" \
        --model gpt-5.4 --baseline B1 \
        --results-dir "$BASE/results/baseline_B1" 2>&1 | tee -a "$LOG"
done

echo "" | tee -a "$LOG"
echo "=== B2: Single model + severity rubric (4 papers) ===" | tee -a "$LOG"

for pid in R01 R04 C01 C04; do
    paper="$ANON/${pid}_anon.txt"
    [ -f "$paper" ] || continue
    echo "$(date): B2 $pid" | tee -a "$LOG"
    python3 "$SCRIPTS/run_baseline.py" \
        --paper "$paper" --paper-id "$pid" \
        --model gpt-5.4 --baseline B2 \
        --results-dir "$BASE/results/baseline_B1" 2>&1 | tee -a "$LOG"
done

# ══════════════════════════════════════════════════════════════
# PRIMARY: Full graduated dissent on ALL 34 papers
# GPT-5.4 (Prover A) + DeepSeek (Prover B + Judge) + Opus (Arbiter)
# ══════════════════════════════════════════════════════════════
echo "" | tee -a "$LOG"
echo "=== PRIMARY: Graduated Dissent (all 34 papers) ===" | tee -a "$LOG"

for paper in "$ANON"/R??_anon.txt "$ANON"/C??_anon.txt "$ANON"/HN??_anon.txt "$ANON"/W0?_anon.txt; do
    [ -f "$paper" ] || continue
    pid=$(basename "$paper" _anon.txt)

    # Skip if already done
    existing=$(ls "$BASE/results/primary/${pid}_gpt-5.4+deepseek_opus_"*.json 2>/dev/null | head -1)
    if [ -n "$existing" ]; then
        echo "SKIP (exists): $pid" | tee -a "$LOG"
        continue
    fi

    echo "$(date): PRIMARY $pid" | tee -a "$LOG"
    python3 "$SCRIPTS/run_v6.py" \
        --paper "$paper" --paper-id "$pid" \
        --prover-a gpt-5.4 --prover-b deepseek \
        --judge deepseek --arbiter opus \
        --results-dir "$BASE/results/primary" 2>&1 | tee -a "$LOG"
done

# ══════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════
echo "" | tee -a "$LOG"
echo "=== COMPLETE at $(date) ===" | tee -a "$LOG"
echo "B1 baseline: $(ls "$BASE"/results/baseline_B1/*.json 2>/dev/null | wc -l) files" | tee -a "$LOG"
echo "Primary: $(ls "$BASE"/results/primary/*.json 2>/dev/null | wc -l) files" | tee -a "$LOG"
