#!/bin/bash
# Run B3 ablation on all 34 primary papers
# Same provers as GD (GPT-5.4 + DeepSeek), same arbiter (Opus)
# NO steelman exchange — findings pooled directly

BASE=~/Desktop/Academic/graduated_dissent_bench_v6
ANON=$BASE/dataset/anonymized
RESULTS=$BASE/results/baseline_B3

# Load API keys
export OPENAI_API_KEY=$(cat ~/.keys/openai)
export ANTHROPIC_API_KEY=$(cat ~/.keys/anthropic)
export DEEPSEEK_API_KEY=$(cat ~/.keys/deepseek)

mkdir -p $RESULTS

# All 34 primary papers
for PAPER_FILE in $ANON/R{01,02,03,04,05,10,11,19,24,25}_anon.txt \
                  $ANON/C{01,02,03,04,05,10,11,19,24,25}_anon.txt \
                  $ANON/HN{02,03,04,05,06,07,08,09,10}_anon.txt \
                  $ANON/W{01,02,03,04,05}_anon.txt; do

    PID=$(basename $PAPER_FILE _anon.txt)

    if [ ! -f "$PAPER_FILE" ]; then
        echo "SKIP: $PAPER_FILE not found"
        continue
    fi

    # Check if already done
    if ls $RESULTS/${PID}_B3_*.json 1>/dev/null 2>&1; then
        echo "SKIP: $PID already has B3 results"
        continue
    fi

    echo "$(date): B3 running $PID..."
    python3 $BASE/scripts/run_b3_ablation.py \
        --paper "$PAPER_FILE" \
        --paper-id "$PID" \
        --results-dir "$RESULTS" \
        2>&1 | tee -a $RESULTS/run_log.txt

    echo "$(date): Done $PID"
    echo "---" >> $RESULTS/run_log.txt
done

echo "$(date): All B3 ablation papers complete."
