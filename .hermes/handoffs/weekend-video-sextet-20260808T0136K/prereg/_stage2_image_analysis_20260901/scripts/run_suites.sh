#!/bin/zsh
# run_suites.sh — aggregate runner v2 (Blanc 2026-09-07 07:33 KST: the v1 runner `_tmp_v33_aggregate_all.sh` piped each child through grep|cut, so the
# subshell's status was cut's and a suite could exit non-zero unseen; its DONE marker shared the '== ' suite-header prefix).
# Usage: run_suites.sh <spec.tsv> <out_dir> <log>
#   spec.tsv lines:  <module path relative to _optionA_dev, e.g. track13/test_track13_nsd_table><TAB><env assignments, space-separated, may be empty>
#                    or  cmd:<shell command run inside the suite's out dir>   (for gate fixtures)
# For each suite: the child's stdout and stderr go UNFILTERED to <out_dir>/<NN>_<name>/stdout.txt and stderr.txt; its REAL exit code is captured
# directly (no pipe between the child and $?); the log gets '== <module>  [<env>]', 'EXIT <rc>' and a display extract (display only);
# <out_dir>/status.tsv gets: idx, module, rc, sha256(stdout), sha256(stderr), dir RELATIVE to the status file (v2.1). Completion marker: '## DONE <time>' — NOT in the '== ' namespace.
set -u
spec=$1; out=$2; log=$3
L=${RUN_SUITES_ROOT:-$(cd "$(dirname "$0")/.." && pwd -P)}   # v2.1 (Blanc 07:49): the lane root comes from THIS script's own location (or RUN_SUITES_ROOT), never a hardcoded live path — a staged copy tests the staged code
PYI=${PYI:-/Library/Developer/CommandLineTools/usr/bin/python3}; export PYTHONPATH="$L/_optionA_dev/_venv_bls/lib/python3.9/site-packages"; export PYTHONDONTWRITEBYTECODE=1
mkdir -p "$out"; out=$(cd "$out" && pwd -P); : > "$out/status.tsv"; : > "$log"   # absolute: the gate resolves the suite dirs from any cwd
{ echo "# run_suites.sh v2.1 $(date '+%Y-%m-%d %H:%M:%S %Z') spec=$spec out=$out"; echo "# interpreter: $("$PYI" -c 'import sys; print(sys.executable, sys.version.split()[0])')"; } >> "$log"
i=0
while IFS=$'\t' read -r m envs || [[ -n "$m" ]]; do
  [[ -z "$m" || "$m" == \#* ]] && continue
  i=$((i+1)); name=${m//\//_}; name=${name#cmd:}; name=${name//[^A-Za-z0-9_.-]/_}; d="$out/$(printf '%02d' $i)_${name:0:60}"; mkdir -p "$d"
  echo "== $m  [${envs:-}]" >> "$log"
  if [[ "$m" == cmd:* ]]; then
    ( cd "$d" && zsh -c "${m#cmd:}" ) > "$d/stdout.txt" 2> "$d/stderr.txt"; rc=$?
  else
    ( cd "$L/_optionA_dev/$(dirname "$m")" && env ${=envs} "$PYI" -W error::ResourceWarning -m unittest "$(basename "$m")" ) > "$d/stdout.txt" 2> "$d/stderr.txt"; rc=$?
  fi
  echo "EXIT $rc" >> "$log"
  grep -hE "^Ran [0-9]+ tests? in|^OK$|^OK \(|^FAILED" "$d/stderr.txt" "$d/stdout.txt" >> "$log" 2>/dev/null   # display only; the gate reads status.tsv and the full files
  printf '%d\t%s\t%d\t%s\t%s\t%s\n' "$i" "$m" "$rc" "$(shasum -a 256 "$d/stdout.txt" | cut -c1-64)" "$(shasum -a 256 "$d/stderr.txt" | cut -c1-64)" "$(basename "$d")" >> "$out/status.tsv"   # v2.1: RELATIVE to the status file (Blanc 07:49) — a relocated copy can never point at live evidence
done < "$spec"
echo "## DONE $(date '+%Y-%m-%d %H:%M:%S %Z') suites=$i" >> "$log"
