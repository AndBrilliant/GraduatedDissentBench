#!/bin/bash
# Variance spot-check: rerun GD on 3 papers to check run-to-run stability
# R01 (detected), R04 (missed), C01 (control)

BASE=~/Desktop/Academic/graduated_dissent_bench_v6
ANON=$BASE/dataset/anonymized
RESULTS=$BASE/results/variance_check

export OPENAI_API_KEY=$(cat ~/.keys/openai)
export ANTHROPIC_API_KEY=$(cat ~/.keys/anthropic)
export DEEPSEEK_API_KEY=$(cat ~/.keys/deepseek)

mkdir -p $RESULTS

for PID in R01 R04 C01; do
    PAPER="$ANON/${PID}_anon.txt"
    echo "$(date): Variance check $PID..."
    python3 $BASE/scripts/run_v6.py \
        --paper "$PAPER" \
        --paper-id "${PID}_v2" \
        --results-dir "$RESULTS" \
        2>&1 | tee -a $RESULTS/run_log.txt
    echo "$(date): Done $PID"
    echo "---" >> $RESULTS/run_log.txt
done

echo "$(date): Variance check complete."
