#!/bin/bash
# Run graduated dissent on 5 viXra GUT papers
# Uses same primary config: GPT-5.4 + DeepSeek + Opus

BASE=~/Desktop/Academic/graduated_dissent_bench_v6
ANON=$BASE/dataset/anonymized
RESULTS=$BASE/results/vixra_gut

# Load API keys
export OPENAI_API_KEY=$(cat ~/.keys/openai)
export ANTHROPIC_API_KEY=$(cat ~/.keys/anthropic)
export DEEPSEEK_API_KEY=$(cat ~/.keys/deepseek)

mkdir -p $RESULTS

for V in V01 V02 V03 V04 V05; do
    PAPER="$ANON/${V}_anon.txt"
    if [ ! -f "$PAPER" ]; then
        echo "SKIP: $PAPER not found"
        continue
    fi

    # Check if already done
    if ls $RESULTS/${V}_*.json 1>/dev/null 2>&1; then
        echo "SKIP: $V already has results"
        continue
    fi

    echo "$(date): Running $V..."
    python3 $BASE/scripts/run_v6.py \
        --paper "$PAPER" \
        --paper-id "$V" \
        --results-dir "$RESULTS" \
        2>&1 | tee -a $RESULTS/run_log.txt

    echo "$(date): Done $V"
    echo "---" >> $RESULTS/run_log.txt
done

echo "$(date): All viXra GUT papers complete."
