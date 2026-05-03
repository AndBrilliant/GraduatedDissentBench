#!/bin/bash
# Permissive arbiter run: 29 papers (10 retracted + 10 matched + 9 hard-neg)
# Skip 5 wildcards — won't flip under any threshold

BASE=~/Desktop/Academic/graduated_dissent_bench_v6
ANON=$BASE/dataset/anonymized
RESULTS=$BASE/results/permissive

export OPENAI_API_KEY=$(cat ~/.keys/openai)
export ANTHROPIC_API_KEY=$(cat ~/.keys/anthropic)
export DEEPSEEK_API_KEY=$(cat ~/.keys/deepseek)

mkdir -p $RESULTS

for PID in R01 R02 R03 R04 R05 R10 R11 R19 R24 R25 \
           C01 C02 C03 C04 C05 C10 C11 C19 C24 C25 \
           HN02 HN03 HN04 HN05 HN06 HN07 HN08 HN09 HN10; do

    PAPER="$ANON/${PID}_anon.txt"

    if [ ! -f "$PAPER" ]; then
        echo "SKIP: $PAPER not found"
        continue
    fi

    if ls $RESULTS/${PID}_permissive_*.json 1>/dev/null 2>&1; then
        echo "SKIP: $PID already has permissive results"
        continue
    fi

    echo "$(date): Permissive running $PID..."
    python3 $BASE/scripts/run_permissive.py \
        --paper "$PAPER" \
        --paper-id "$PID" \
        --results-dir "$RESULTS" \
        2>&1 | tee -a $RESULTS/run_log.txt

    echo "$(date): Done $PID"
    echo "---" >> $RESULTS/run_log.txt
done

echo "$(date): All permissive runs complete."
