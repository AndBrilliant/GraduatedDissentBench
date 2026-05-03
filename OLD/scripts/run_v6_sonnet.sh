#!/bin/bash
# v6 Author's Choice: Sonnet 4.6 (Prover A) + DeepSeek V3.2 (Prover B) + Opus 4.6 (Arbiter)
# Pre-registered "author's choice" config based on v4 pilot experience

set -e
export PATH=/opt/homebrew/bin:$PATH
export ANTHROPIC_API_KEY="$(cat ~/.keys/anthropic)"
export OPENAI_API_KEY="$(cat ~/.keys/openai)"
export DEEPSEEK_API_KEY="$(cat ~/.keys/deepseek)"

BASE=~/Desktop/Academic/graduated_dissent_bench_v6
ANON="$BASE/dataset/anonymized"
SCRIPTS="$BASE/scripts"
LOG="$BASE/results/authors_choice_run.log"

mkdir -p "$BASE/results/authors_choice"

echo "=== AUTHOR'S CHOICE at $(date) ===" | tee "$LOG"
echo "Prover A: Sonnet 4.6 | Prover B: DeepSeek V3.2 | Arbiter: Opus 4.6" | tee -a "$LOG"

for paper in "$ANON"/R??_anon.txt "$ANON"/C??_anon.txt "$ANON"/HN??_anon.txt "$ANON"/W0?_anon.txt; do
    [ -f "$paper" ] || continue
    pid=$(basename "$paper" _anon.txt)

    existing=$(ls "$BASE/results/authors_choice/${pid}_"*.json 2>/dev/null | head -1)
    if [ -n "$existing" ]; then
        echo "SKIP: $pid" | tee -a "$LOG"
        continue
    fi

    echo "$(date): $pid" | tee -a "$LOG"
    python3 "$SCRIPTS/run_v6.py" \
        --paper "$paper" --paper-id "$pid" \
        --prover-a sonnet --prover-b deepseek \
        --judge deepseek --arbiter opus \
        --results-dir "$BASE/results/authors_choice" 2>&1 | tee -a "$LOG"
done

echo "" | tee -a "$LOG"
echo "=== COMPLETE at $(date) ===" | tee -a "$LOG"
echo "Files: $(ls "$BASE"/results/authors_choice/*.json 2>/dev/null | wc -l)" | tee -a "$LOG"
