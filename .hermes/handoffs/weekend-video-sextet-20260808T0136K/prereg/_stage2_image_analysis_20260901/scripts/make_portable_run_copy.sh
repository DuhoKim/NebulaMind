#!/bin/zsh
# make_portable_run_copy.sh <original_run_dir> <portable_run_dir> — a SEPARATELY NAMED portable verification copy (Blanc 07:49): copies every suite dir,
# verifies each stdout/stderr digest against the ORIGINAL status.tsv at copy time, writes a status.tsv whose dir column is RELATIVE to the copy, and a
# RELOCATION_MAP.txt (original absolute dir -> relative dir, digests verified). The original run dir and its status.tsv are NOT modified (historical evidence).
set -u; src=$1; dst=$2; [[ -f "$src/status.tsv" ]] || { echo "STOP: no status.tsv in $src"; exit 2; }
mkdir -p "$dst"; dst=$(cd "$dst" && pwd -P); : > "$dst/status.tsv"; { echo "# RELOCATION MAP $(date '+%Y-%m-%d %H:%M:%S %Z') original=$src copy=$dst"; echo "# every stdout/stderr digest re-computed on the copy and compared with the ORIGINAL status.tsv"; } > "$dst/RELOCATION_MAP.txt"; bad=0
while IFS=$'\t' read -r i m rc so se d; do
  [[ -z "$i" || "$i" == \#* ]] && continue
  rel=$(basename "$d"); mkdir -p "$dst/$rel"; cp -p "$d/stdout.txt" "$d/stderr.txt" "$dst/$rel/"
  cso=$(shasum -a 256 "$dst/$rel/stdout.txt" | cut -c1-64); cse=$(shasum -a 256 "$dst/$rel/stderr.txt" | cut -c1-64)
  if [[ "$cso" == "$so" && "$cse" == "$se" ]]; then v=VERIFIED; else v=MISMATCH; bad=$((bad+1)); fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$i" "$m" "$rc" "$so" "$se" "$rel" >> "$dst/status.tsv"; printf '%s -> %s  %s\n' "$d" "$rel" "$v" >> "$dst/RELOCATION_MAP.txt"
done < "$src/status.tsv"
echo "## $(wc -l < "$dst/status.tsv" | tr -d ' ') suites copied; mismatches=$bad" >> "$dst/RELOCATION_MAP.txt"; cat "$dst/RELOCATION_MAP.txt" | tail -1; [[ $bad -eq 0 ]] || { echo "STOP: $bad digest mismatches"; exit 2; }
