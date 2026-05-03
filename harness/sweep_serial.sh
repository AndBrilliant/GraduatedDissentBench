#!/usr/bin/env bash
# Bulletproof serial sweep: one fresh Python process per (paper, condition).
# Avoids the threading hang we saw with sweep_pilot.py.
#
# Usage:
#   bash harness/sweep_serial.sh [pilot_n10] [conditions]
#
# Defaults: out_name=pilot_n10, conditions=b1,b2,b3,gd
set -uo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

OUT_NAME="${1:-pilot_n10}"
CONDS_CSV="${2:-b1,b2,b3,gd}"
IFS=',' read -r -a CONDS <<< "$CONDS_CSV"

OUT_DIR="$REPO/data/spot/outputs/$OUT_NAME"
SAMPLE="$OUT_DIR/sample.csv"

if [ ! -f "$SAMPLE" ]; then
  echo "!! sample.csv missing: $SAMPLE — run sweep_pilot.py once to generate it"
  exit 1
fi

PAPER_DIR="$REPO/data/spot/text_detectable"
PY="$REPO/.venv/bin/python"

# Get paper ids from sample.csv (skip header, take safe_doi column)
SAFE_DOIS=()
while IFS= read -r line; do
  SAFE_DOIS+=("$line")
done < <(tail -n +2 "$SAMPLE" | awk -F, '{print $2}')

total=$(( ${#SAFE_DOIS[@]} * ${#CONDS[@]} ))
done=0
for safe_doi in "${SAFE_DOIS[@]}"; do
  for cond in "${CONDS[@]}"; do
    out_file="$OUT_DIR/$safe_doi/$cond.json"
    if [ -f "$out_file" ]; then
      done=$((done + 1))
      echo "[skip] $safe_doi/$cond (already done)"
      continue
    fi
    paper_path="$PAPER_DIR/$safe_doi/paper.txt"
    if [ ! -f "$paper_path" ]; then
      echo "[miss] $safe_doi (no paper.txt at $paper_path)"
      continue
    fi
    done=$((done + 1))
    t0=$(date +%s)
    echo "[$done/$total] $safe_doi/$cond starting at $(date '+%H:%M:%S') ..."
    "$PY" "$REPO/harness/run_pipeline.py" \
      --paper "$paper_path" \
      --paper-id "$safe_doi" \
      --condition "$cond" \
      --out-dir "$OUT_DIR" \
      --cap 25.0
    rc=$?
    t1=$(date +%s)
    echo "  -> rc=$rc dt=$((t1 - t0))s"
  done
done

echo ""
echo "Sweep complete."
