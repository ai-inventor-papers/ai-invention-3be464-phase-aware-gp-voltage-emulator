#!/bin/bash
# Batch of aii-web-tools searches for literature grounding.
export SKILL_DIR="$(realpath /ai-inventor/.claude/skills/aii-web-tools)"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
OUT="../results/search_log.txt"
: > "$OUT"
run () {
  echo "=== QUERY: $1 [mode=$2] $(date -u +%FT%TZ) ===" >> "$OUT"
  "$PY" "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "$1" --mode "$2" --max-results 10 >> "$OUT" 2>&1
  echo "" >> "$OUT"
}
run "Gaussian process surrogate power flow distribution network voltage prediction" scholarly
run "Gaussian process emulator unbalanced three-phase distribution network voltages" scholarly
run "graph kernel Laplacian Kirchhoff kernel Gaussian process power system" scholarly
run "LinDistFlow linearised distribution flow three-phase unbalanced quadratic correction" scholarly
run "pandapower IEEE PES European low voltage test feeder 55 loads three-phase" general
run "phase-aware kernel unbalanced three-phase distribution graph Gaussian process" scholarly
run "probabilistic power flow Gaussian process uncertainty voltage magnitude" scholarly
run "graph Laplacian kernel power grid Kirchhoff effective resistance kernel" scholarly
run "surrogate model power system operation physics-informed Gaussian process" scholarly
run "distribution feeder voltage sensitivity matrix impedance-based machine learning surrogate" scholarly
run "Gaussian process multi-output regression shared kernel bus voltage prediction" scholarly
run "negative log predictive density Gaussian process regression power system" scholarly
echo "ALL DONE $(date -u +%FT%TZ)" >> "$OUT"
