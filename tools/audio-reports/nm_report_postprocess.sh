#!/bin/zsh
# nm_report_postprocess.sh <reading.mp3> — everything that happens AFTER a
# reading is published, in dependency order, off the critical path.
#   1. forced alignment  (needs the venv python — system python3 has no faster_whisper)
#   2. slide deck derivation (needs the alignment)
#   3. archive index rebuild (picks up transcript + deck)
# Slides must never block archiving: every step is best-effort and the index
# rebuild runs regardless.
S=/Users/duhokim/HermesOps/scripts
VENV_PY=/Users/duhokim/.hermes/hermes-agent/venv/bin/python
mp3="${1:?mp3 required}"
stem="${mp3:r}"
log=/Users/duhokim/HermesOps/reports/status-audio/postprocess.log
{
  echo "--- $(date '+%Y-%m-%d %H:%M:%S %Z') $(basename $mp3) ---"
  [[ -f "$stem.txt" ]] && "$VENV_PY" "$S/nm_audio_align.py" "$(basename $stem)" 2>&1
  if [[ -n "${NM_DECK:-}" && -f "${NM_DECK}" ]]; then
    # Speaker-authored deck (they know their own report); we only resolve
    # graphics and enforce the restate-only rules.
    python3 "$S/nm_deck_build.py" "$mp3" "${NM_DECK}" 2>&1
  else
    [[ -f "$stem.txt" ]] && python3 "$S/nm_deck_derive.py" "$mp3" 2>&1
  fi
  python3 "$S/nm_audio_index.py" 2>&1 | tail -1
} >> "$log" 2>&1
