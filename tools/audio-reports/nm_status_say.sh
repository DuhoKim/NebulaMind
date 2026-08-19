#!/bin/zsh
# Stamp with real `date` (never estimated), timestamp-FIRST so lexical order == chronological order,
# then refresh a stable latest.mp3 so Chrome has one URL that is always the newest reading.
R=/Users/duhokim/HermesOps/reports/status-audio
slug="${1:?slug required}"; shift
text="$*"
TS=$(date '+%Y%m%dT%H%M%S')
out="$R/${TS}-${slug}.mp3"
# NM_SAY_VOICE picks the speaker (default alloy); NM_SAY_NO_PLAY=1 skips afplay.
python3 /Users/duhokim/HermesOps/scripts/nm_say.py "$text" --voice "${NM_SAY_VOICE:-alloy}" -o "$out" >/dev/null || exit 1
cp "$out" "$R/latest.mp3"
printf '%s  %s\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')" "$(basename "$out")" > "$R/latest.txt"
[[ -z "${NM_SAY_NO_PLAY:-}" ]] && afplay "$out" >/dev/null 2>&1 &
# Keep archive.html in step with every reading — it went stale for 3 days once
# (2026-08-16..19) because nothing in the pipeline rebuilt it.
python3 /Users/duhokim/HermesOps/scripts/nm_audio_index.py >/dev/null 2>&1
echo "$out"
echo "https://duho-macstudio.taila27502.ts.net/reports/status-audio/latest.mp3"
