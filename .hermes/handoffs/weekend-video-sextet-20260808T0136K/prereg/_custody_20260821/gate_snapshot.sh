#!/bin/zsh
# Tamper-EVIDENT snapshot of deliverables at gate dispatch. NOT immutability: on this host the
# owner can always undo chflags. A codex gate demonstrated both original defects on 2026-08-21 —
# a 0444 copy was reverted and rewritten, and the ledger was truncated — so this script now:
#   (a) verifies an existing destination's FULL digest instead of trusting a 12-hex prefix,
#   (b) sets chflags uchg to raise the bar past an accidental write,
#   (c) hash-chains the ledger so a truncation or edit is DETECTABLE after the fact.
# It gives evidence of tampering. It does not prevent it. Say it that way.
set -e
OUT="${0:A:h}/_gated"; mkdir -p "$OUT"
LEDGER="$OUT/GATED_SNAPSHOTS.jsonl"
STAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
for f in "$@"; do
  [[ -f "$f" ]] || { echo "missing: $f" >&2; exit 1; }
  H=$(shasum -a 256 "$f" | cut -d' ' -f1)
  B=$(basename "$f")
  DST="$OUT/${B%.md}.${H:0:12}.md"
  if [[ -f "$DST" ]]; then
    EXIST=$(shasum -a 256 "$DST" | cut -d' ' -f1)
    if [[ "$EXIST" != "$H" ]]; then
      echo "REFUSING: $DST exists with digest $EXIST, source is $H — destination was replaced" >&2
      exit 2
    fi
  else
    cp "$f" "$DST"; chmod 444 "$DST"; chflags uchg "$DST" 2>/dev/null || true
  fi
  PREV=$([[ -s "$LEDGER" ]] && shasum -a 256 "$LEDGER" | cut -d' ' -f1 || echo "GENESIS")
  print -r -- "{\"utc\":\"$STAMP\",\"file\":\"$B\",\"sha256\":\"$H\",\"snapshot\":\"$(basename $DST)\",\"prev_ledger_sha256\":\"$PREV\"}" >> "$LEDGER"
  echo "snapshot $B sha ${H:0:16} -> $(basename $DST)  (chain prev ${PREV:0:12})"
done
