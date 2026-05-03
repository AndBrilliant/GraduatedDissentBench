#!/bin/bash
# v6 Master Run Script — runs independently on photek
# Three models: GPT-5.4, DeepSeek V3.2, Opus 4.6
# No dependency on SSH or other machines

export PATH=/opt/homebrew/bin:$PATH
export ANTHROPIC_API_KEY="$(cat ~/.keys/anthropic)"
export OPENAI_API_KEY="$(cat ~/.keys/openai)"
export DEEPSEEK_API_KEY="$(cat ~/.keys/deepseek)"

BASE=~/Desktop/Academic/graduated_dissent_bench_v6
cd "$BASE"

mkdir -p "$BASE/results/baseline" "$BASE/results/primary"
LOG="$BASE/results/run_log.txt"

echo "=== v6 BENCHMARK RUN at $(date) ===" | tee -a "$LOG"
echo "Papers found:" | tee -a "$LOG"
ls "$BASE"/dataset/anonymized/*.txt | wc -l | tee -a "$LOG"

# Phase 1: DeepSeek baseline
echo "" | tee -a "$LOG"
echo "=== PHASE 1: DeepSeek Baseline ===" | tee -a "$LOG"
for paper in "$BASE"/dataset/anonymized/*_anon.txt; do
    pid=$(basename "$paper" _anon.txt)
    if [ -f "$BASE/results/baseline/${pid}_deepseek+deepseek_deepseek_"*.json ] 2>/dev/null; then
        echo "SKIP (exists): $pid" | tee -a "$LOG"
        continue
    fi
    echo "$(date): $pid (baseline)" | tee -a "$LOG"
    python3 "$BASE/scripts/run_v6.py" \
        --paper "$paper" --paper-id "$pid" \
        --prover-a deepseek --prover-b deepseek \
        --judge deepseek --arbiter deepseek \
        --results-dir "$BASE/results/baseline" 2>&1 | tee -a "$LOG"
done

# Phase 2: Primary configuration
echo "" | tee -a "$LOG"
echo "=== PHASE 2: Primary (GPT-5.4 + DeepSeek + Opus arbiter) ===" | tee -a "$LOG"
for paper in "$BASE"/dataset/anonymized/*_anon.txt; do
    pid=$(basename "$paper" _anon.txt)
    if [ -f "$BASE/results/primary/${pid}_gpt-5.4+deepseek_opus_"*.json ] 2>/dev/null; then
        echo "SKIP (exists): $pid" | tee -a "$LOG"
        continue
    fi
    echo "$(date): $pid (primary)" | tee -a "$LOG"
    python3 "$BASE/scripts/run_v6.py" \
        --paper "$paper" --paper-id "$pid" \
        --prover-a gpt-5.4 --prover-b deepseek \
        --judge deepseek --arbiter opus \
        --results-dir "$BASE/results/primary" 2>&1 | tee -a "$LOG"
done

echo "" | tee -a "$LOG"
echo "=== v6 BENCHMARK COMPLETE at $(date) ===" | tee -a "$LOG"
echo "Results:" | tee -a "$LOG"
echo "  Baseline: $(ls "$BASE"/results/baseline/*.json 2>/dev/null | wc -l) files" | tee -a "$LOG"
echo "  Primary: $(ls "$BASE"/results/primary/*.json 2>/dev/null | wc -l) files" | tee -a "$LOG"
