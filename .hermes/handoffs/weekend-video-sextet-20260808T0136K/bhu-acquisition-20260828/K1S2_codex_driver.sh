#!/bin/zsh
set -euo pipefail

LANE=${0:A:h}
ROOT="$LANE/_tmp_k1s2_codex"
RUNS="$ROOT/runs"
COMPAS="$ROOT/COMPAS/src/COMPAS"
COMMANDS="$ROOT/commands.txt"
N=1000000
SEEDS=(104729 130363 155921)
EXTRA_SEEDS=(181081 196613 216091)
CAPS=(1.97 2.50 3.50)
ENGINES=(DELAYED RAPID)
METALS=(0.02 0.0002)
CEKICKS=(default alternative)

mkdir -p "$RUNS"
rm -f "$RUNS/DONE"
: > "$COMMANDS"

emit() {
  local tag=$1 mode=$2 cap=$3 engine=$4 metal=$5 cekick=$6 seed=$7
  local out="$RUNS/$tag"
  local extra=""
  if [[ "$cekick" == alternative ]]; then
    extra="--common-envelope-lambda-prescription LAMBDA_FIXED --common-envelope-lambda 0.1 --kick-magnitude-distribution MAXWELLIAN --kick-magnitude-sigma-CCSN-NS 265 --kick-magnitude-sigma-CCSN-BH 265"
  fi
  print -r -- "mkdir -p '$out'; '$COMPAS' --mode '$mode' --number-of-systems '$N' --random-seed '$seed' --output-path '$out' --output-container COMPAS_Output --remnant-mass-prescription FRYER2012 --fryer-supernova-engine '$engine' --maximum-neutron-star-mass '$cap' --metallicity '$metal' $extra > '$out/compas.log' 2>&1"
}

# Main 24 configurations x three independent master-sheet seeds.
for cap in $CAPS; do
  for engine in $ENGINES; do
    for metal in $METALS; do
      for cekick in $CEKICKS; do
        for seed in $SEEDS; do
          emit "bse_cap${cap}_eng${engine}_z${metal}_ce${cekick}_seed${seed}" BSE "$cap" "$engine" "$metal" "$cekick" "$seed" >> "$COMMANDS"
        done
      done
    done
  done
done

# C3: fiducial nuisance setting, full three-cap grid, same three seeds, SSE.
for cap in $CAPS; do
  for seed in $SEEDS; do
    emit "sse_cap${cap}_engDELAYED_z0.02_cedefault_seed${seed}" SSE "$cap" DELAYED 0.02 default "$seed" >> "$COMMANDS"
  done
done

# C4: three additional independent batches at every cap of the centre/fiducial
# configuration, giving 6e6 systems per cap when combined with the main batches.
for cap in $CAPS; do
  for seed in $EXTRA_SEEDS; do
    emit "c4_cap${cap}_engDELAYED_z0.02_cedefault_seed${seed}" BSE "$cap" DELAYED 0.02 default "$seed" >> "$COMMANDS"
  done
done

# Validation mode generates all command lines but evolves nothing.
[[ "${1:-}" == "--commands-only" ]] && exit 0

# Each line is a complete, independently logged command.  Do not exceed 10.
if ! jot - 1 "$(wc -l < "$COMMANDS")" | xargs -P 10 -n 1 zsh -c \
  'set -o pipefail; sed -n "${2}p" "$1" | zsh' worker "$COMMANDS"; then
  print -u2 -- "At least one COMPAS batch failed; DONE not written."
  exit 1
fi
touch "$RUNS/DONE"
