#!/bin/zsh
# K1S2_claude_driver.sh -- K1 stage-2 step 2, seat "claude" (BLIND of the codex seat).
# Generates every COMPAS command line for the pinned grid + controls, runs them through
# `xargs -P 10`, and writes <runs>/DONE when every job has finished cleanly.
#
# Pins used (K1S2_PIN_GATE_agy.md, MASTER PIN SHEET + "Driver Settings Needed"; brief _K1S2_DRIVER_BRIEF.md):
#   row 1  binary  : _tmp_k1s2_codex/COMPAS/src/COMPAS, COMPAS v03.29.05, commit e728869cef4fc21d22e7db6e6645a8f878ada2b2
#   row 2  options : --remnant-mass-prescription FRYER2012 (explicit), --fryer-supernova-engine {DELAYED,RAPID},
#                    --maximum-neutron-star-mass <cap> (explicit at every point)
#   row 3  caps    : {1.97, 2.50, 3.50} Msun
#   metallicity    : prereg Zsun = 0.02 -> --metallicity 0.02 (=Zsun) and 0.0002 (=0.01 Zsun); passed explicitly, so the
#                    code's own ZSOL=0.0142 never enters.
#   row 6  MC      : 3 batches x 10^6 binaries per grid point; pinned batch seeds 104729, 130363, 155921.
#                    DECLARED DEVIATION (flagged for the RESULT): COMPAS uses `--random-seed + <system index>` per system
#                    (src/main.cpp L663, `RandomSeedCmdLine() + index`), so batches of 10^6 started at the pinned values
#                    verbatim would overlap in >97% of their per-system seeds and the across-batch dispersion would be
#                    meaningless. Each batch therefore starts at (pinned seed x 1000): 104729000, 130363000, 155921000 --
#                    blocks of 10^6 that never overlap. The same three seeds are used at every grid point (common random
#                    numbers across caps, so the cap derivative is a paired difference per batch).
#   row 7  CE/kick : "default" = code defaults (LAMBDA_NANJING, MULLERMANDEL kicks); "alt" = LAMBDA_FIXED lambda=0.1,
#                    alpha=1.0, MAXWELLIAN sigma_CCSN(NS,BH)=265 km/s, BH kicks FALLBACK (the COMPAS-paper fiducial).
#   IMF slope      : NOT rerun; reweighted from Mass@ZAMS(1) in K1S2_claude_post.py (Kroupa alpha3=2.3 sampled).
#   C3             : --mode SSE, same seeds, 10^6 stars, cap grid x engine x metallicity (CE/kick axis has no meaning in SSE).
#   C4             : centre configuration (cap grid x DELAYED x Z=0.02 x default) with three extra batch seeds
#                    200003000, 300007000, 400009000 (declared here; 6 x 10^6 per cap in total).
# Output hygiene   : --rlof-printing FALSE (the RLOF log is not used by the post-processing and is the bulk of the file),
#                    --quiet (the per-system stdout narration would be ~10^8 bytes per run), --logfile-type HDF5.
# Resumable        : a job is skipped when <jobdir>/DONE exists; re-running the driver only runs what is missing.
set -u
L=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828
C=$L/_tmp_k1s2_codex/COMPAS/src/COMPAS
RUNS=$L/_tmp_k1s2_claude/runs
NSYS=1000000
NPAR=10
NICE=5
mkdir -p "$RUNS"
JOBS=$RUNS/jobs.txt
MANIFEST=$RUNS/manifest.csv
RUNNER=$RUNS/run_one.zsh

echo "K1S2 claude driver start: $(date '+%Y-%m-%d %H:%M:%S %Z')  host=$(hostname)  cores=$(getconf _NPROCESSORS_ONLN 2>/dev/null)"
echo "binary: $C"
echo "binary sha256: $(shasum -a 256 "$C" | cut -d' ' -f1)"
echo "checkout HEAD: $(git -C "$L/_tmp_k1s2_codex/COMPAS" rev-parse HEAD 2>/dev/null)"
"$C" --version 2>&1 | head -1

typeset -a CAPS ENGINES ZS CEKS SEEDS_PINNED SEEDS_EXTRA
CAPS=(1.97 2.50 3.50)
ENGINES=(DELAYED RAPID)
ZS=(0.02 0.0002)
CEKS=(default alt)
SEEDS_PINNED=(104729 130363 155921)
SEEDS_EXTRA=(200003 300007 400009)

COMMON="--remnant-mass-prescription FRYER2012 --logfile-type HDF5 --quiet --rlof-printing FALSE --output-container out"
ALT="--common-envelope-alpha 1.0 --common-envelope-lambda-prescription LAMBDA_FIXED --common-envelope-lambda 0.1 --kick-magnitude-distribution MAXWELLIAN --kick-magnitude-sigma-CCSN-NS 265 --kick-magnitude-sigma-CCSN-BH 265 --black-hole-kicks-mode FALLBACK"

: > "$JOBS"
echo "mode,cap,engine,Z,cek,batch,seed_pinned,random_seed,dir" > "$MANIFEST"

# emit MODE CAP ENGINE Z CEK BATCH SEED_PINNED
emit() {
  local mode=$1 cap=$2 eng=$3 Z=$4 cek=$5 b=$6 sp=$7
  local rseed=$(( sp * 1000 ))
  local dir="$RUNS/${mode}_cap${cap}_${eng}_Z${Z}_${cek}/b${b}_s${sp}"
  local args="--mode $mode --number-of-systems $NSYS --random-seed $rseed --metallicity $Z --fryer-supernova-engine $eng --maximum-neutron-star-mass $cap $COMMON"
  [[ $cek == alt ]] && args="$args $ALT"
  print -r -- "$dir $args" >> "$JOBS"
  echo "$mode,$cap,$eng,$Z,$cek,$b,$sp,$rseed,$dir" >> "$MANIFEST"
}

# ---- queue order: science-critical first ----
# 1. BSE centre configuration (DELAYED, Z=0.02, default) over the cap grid, 3 pinned batches  -> 9 jobs
for cap in $CAPS; do for i in 1 2 3; do emit BSE $cap DELAYED 0.02 default $i ${SEEDS_PINNED[$i]}; done; done
# 2. BSE remaining 21 configurations x 3 batches                                              -> 63 jobs
for eng in $ENGINES; do for Z in $ZS; do for cek in $CEKS; do
  [[ $eng == DELAYED && $Z == 0.02 && $cek == default ]] && continue
  for cap in $CAPS; do for i in 1 2 3; do emit BSE $cap $eng $Z $cek $i ${SEEDS_PINNED[$i]}; done; done
done; done; done
# 3. C3: SSE centre (DELAYED, Z=0.02) cap grid, 3 batches                                     -> 9 jobs
for cap in $CAPS; do for i in 1 2 3; do emit SSE $cap DELAYED 0.02 default $i ${SEEDS_PINNED[$i]}; done; done
# 4. C4: BSE centre configuration, three extra batches (4,5,6)                                -> 9 jobs
for cap in $CAPS; do for i in 1 2 3; do emit BSE $cap DELAYED 0.02 default $(( i + 3 )) ${SEEDS_EXTRA[$i]}; done; done
# 5. C3 extended: SSE at the other engine/metallicity box points, 3 batches                   -> 27 jobs
for eng in $ENGINES; do for Z in $ZS; do
  [[ $eng == DELAYED && $Z == 0.02 ]] && continue
  for cap in $CAPS; do for i in 1 2 3; do emit SSE $cap $eng $Z default $i ${SEEDS_PINNED[$i]}; done; done
done; done

NJOBS=$(wc -l < "$JOBS" | tr -d ' ')
echo "jobs queued: $NJOBS  (concurrency $NPAR, nice $NICE, $NSYS systems each)"
echo "jobs file: $JOBS"

cat > "$RUNNER" <<'RUNNER_EOF'
#!/bin/zsh
# run_one.zsh <jobdir> <COMPAS args...>   (invoked by xargs -L 1)
C=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/_tmp_k1s2_codex/COMPAS/src/COMPAS
dir=$1; shift
if [[ -f "$dir/DONE" ]]; then echo "skip (DONE) $dir"; exit 0; fi
mkdir -p "$dir"
rm -rf "$dir/out"
start=$(date +%s)
echo "start $(date '+%Y-%m-%d %H:%M:%S %Z') $dir" 
echo "cmd: $C $* --output-path $dir" > "$dir/job.log"
nice -n 5 "$C" "$@" --output-path "$dir" >> "$dir/job.log" 2>&1
rc=$?
secs=$(( $(date +%s) - start ))
echo "rc=$rc wall_secs=$secs" >> "$dir/job.log"
if [[ $rc -eq 0 && -f "$dir/out/COMPAS_Output.h5" ]]; then
  echo "rc=$rc wall_secs=$secs $(date '+%Y-%m-%d %H:%M:%S %Z')" > "$dir/DONE"
  echo "done  $(date '+%Y-%m-%d %H:%M:%S %Z') rc=$rc wall=${secs}s $dir"
else
  echo "FAIL  $(date '+%Y-%m-%d %H:%M:%S %Z') rc=$rc wall=${secs}s $dir"
fi
exit 0
RUNNER_EOF

xargs -P $NPAR -L 1 zsh "$RUNNER" < "$JOBS"

# ---- completion accounting ----
ndone=0; missing=()
while read -r line; do
  d=${line%% *}
  if [[ -f "$d/DONE" ]]; then (( ndone++ )); else missing+=("$d"); fi
done < "$JOBS"
echo "finished: $ndone / $NJOBS jobs DONE at $(date '+%Y-%m-%d %H:%M:%S %Z')"
if (( ndone == NJOBS )); then
  { echo "ALL $NJOBS jobs DONE $(date '+%Y-%m-%d %H:%M:%S %Z')"; echo "binary sha256: $(shasum -a 256 "$C" | cut -d' ' -f1)"; } > "$RUNS/DONE"
  echo "wrote $RUNS/DONE"
else
  printf '%s\n' "${missing[@]}" > "$RUNS/FAILED"
  echo "NOT complete; missing jobs listed in $RUNS/FAILED (re-run the driver to retry only those)"
fi
