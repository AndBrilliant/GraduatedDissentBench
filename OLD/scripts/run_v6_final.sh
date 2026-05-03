#!/bin/bash
# v6 FINAL RUN — all conditions, all 34 papers
# 1. B1 baseline (single model, no rubric) — all papers
# 2. B2 baseline (single model + rubric) — all papers
# 3. Primary: GPT-5.4 + DeepSeek + Opus arbiter — resume remaining
# 4. Author's choice: Sonnet + DeepSeek + Opus arbiter — all papers

set -e
export PATH=/opt/homebrew/bin:$PATH
export ANTHROPIC_API_KEY="$(cat ~/.keys/anthropic)"
export OPENAI_API_KEY="$(cat ~/.keys/openai)"
export DEEPSEEK_API_KEY="$(cat ~/.keys/deepseek)"

BASE=~/Desktop/Academic/graduated_dissent_bench_v6
ANON="$BASE/dataset/anonymized"
SCRIPTS="$BASE/scripts"
LOG="$BASE/results/final_run.log"

mkdir -p "$BASE/results/baseline_B1" "$BASE/results/primary" "$BASE/results/authors_choice"

echo "=== v6 FINAL RUN at $(date) ===" | tee "$LOG"

# Papers list
PAPERS=$(ls "$ANON"/R??_anon.txt "$ANON"/C??_anon.txt "$ANON"/HN??_anon.txt "$ANON"/W0?_anon.txt 2>/dev/null)
echo "Total papers: $(echo "$PAPERS" | wc -l)" | tee -a "$LOG"

# === B1: Single model, no rubric ===
echo "" | tee -a "$LOG"
echo "=== B1 BASELINE ===" | tee -a "$LOG"
for paper in $PAPERS; do
    pid=$(basename "$paper" _anon.txt)
    existing=$(ls "$BASE/results/baseline_B1/${pid}_B1_"*.json 2>/dev/null | head -1)
    [ -n "$existing" ] && continue
    echo "$(date): B1 $pid" | tee -a "$LOG"
    python3 "$SCRIPTS/run_baseline.py" --paper "$paper" --paper-id "$pid" --model gpt-5.4 --baseline B1 --results-dir "$BASE/results/baseline_B1" 2>&1 | tee -a "$LOG"
done

# === B2: Single model + severity rubric ===
echo "" | tee -a "$LOG"
echo "=== B2 BASELINE ===" | tee -a "$LOG"
for paper in $PAPERS; do
    pid=$(basename "$paper" _anon.txt)
    existing=$(ls "$BASE/results/baseline_B1/${pid}_B2_"*.json 2>/dev/null | head -1)
    [ -n "$existing" ] && continue
    echo "$(date): B2 $pid" | tee -a "$LOG"
    python3 "$SCRIPTS/run_baseline.py" --paper "$paper" --paper-id "$pid" --model gpt-5.4 --baseline B2 --results-dir "$BASE/results/baseline_B1" 2>&1 | tee -a "$LOG"
done

# === PRIMARY: GPT-5.4 + DeepSeek + Opus (resume) ===
echo "" | tee -a "$LOG"
echo "=== PRIMARY (GPT-5.4) ===" | tee -a "$LOG"
for paper in $PAPERS; do
    pid=$(basename "$paper" _anon.txt)
    existing=$(ls "$BASE/results/primary/${pid}_gpt"*.json 2>/dev/null | head -1)
    [ -n "$existing" ] && continue
    echo "$(date): PRIMARY $pid" | tee -a "$LOG"
    python3 "$SCRIPTS/run_v6.py" --paper "$paper" --paper-id "$pid" --prover-a gpt-5.4 --prover-b deepseek --judge deepseek --arbiter opus --results-dir "$BASE/results/primary" 2>&1 | tee -a "$LOG"
done

# === AUTHOR'S CHOICE: Sonnet + DeepSeek + Opus ===
echo "" | tee -a "$LOG"
echo "=== AUTHOR'S CHOICE (Sonnet) ===" | tee -a "$LOG"
for paper in $PAPERS; do
    pid=$(basename "$paper" _anon.txt)
    existing=$(ls "$BASE/results/authors_choice/${pid}_"*.json 2>/dev/null | head -1)
    [ -n "$existing" ] && continue
    echo "$(date): SONNET $pid" | tee -a "$LOG"
    python3 "$SCRIPTS/run_v6.py" --paper "$paper" --paper-id "$pid" --prover-a sonnet --prover-b deepseek --judge deepseek --arbiter opus --results-dir "$BASE/results/authors_choice" 2>&1 | tee -a "$LOG"
done

echo "" | tee -a "$LOG"
echo "=== ALL COMPLETE at $(date) ===" | tee -a "$LOG"
echo "B1: $(ls "$BASE"/results/baseline_B1/*_B1_*.json 2>/dev/null | wc -l)" | tee -a "$LOG"
echo "B2: $(ls "$BASE"/results/baseline_B1/*_B2_*.json 2>/dev/null | wc -l)" | tee -a "$LOG"
echo "Primary: $(ls "$BASE"/results/primary/*.json 2>/dev/null | wc -l)" | tee -a "$LOG"
echo "Authors choice: $(ls "$BASE"/results/authors_choice/*.json 2>/dev/null | wc -l)" | tee -a "$LOG"
