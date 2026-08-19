#!/bin/zsh
# Stamp with real `date` (never estimated), timestamp-FIRST so lexical order == chronological order.
# 2026-08-20 overhaul: publishing goes through nm_audio_publish.py — monotonic
# queue.json (no more dropped bursts), transcript sidecar, quiet hours
# (22:30-08:00 KST render-but-don't-play, NM_QUIET_OFF=1 or NM_FORCE_LIVE=1 to
# override), speaker identity from voices.json via NM_SPEAKER.
# NM_SAY_VOICE picks the TTS voice (default alloy); NM_SAY_NO_PLAY=1 skips afplay.
R=/Users/duhokim/HermesOps/reports/status-audio
S=/Users/duhokim/HermesOps/scripts
slug="${1:?slug required}"; shift
text="$*"
TS=$(date '+%Y%m%dT%H%M%S')
out="$R/${TS}-${slug}.mp3"
python3 "$S/nm_say.py" "$text" --voice "${NM_SAY_VOICE:-alloy}" -o "$out" >/dev/null || exit 1
pub_args=("$out" --slug "$slug" --speaker "${NM_SPEAKER:-system}" --text "$text")
[[ -n "${NM_FORCE_LIVE:-}" ]] && pub_args+=(--force-live)
pub=$(python3 "$S/nm_audio_publish.py" "${pub_args[@]}") || exit 1
quiet=$(print -r -- "$pub" | python3 -c 'import json,sys; print("1" if json.load(sys.stdin)["quiet"] else "0")')
if [[ "$quiet" != "1" && -z "${NM_SAY_NO_PLAY:-}" ]]; then
  afplay "$out" >/dev/null 2>&1 &
fi
# archive index in the background, logged (it rotted silently for 3 days once)
( python3 "$S/nm_audio_index.py" >> "$R/index.log" 2>&1 ) &
echo "$out"
[[ "$quiet" == "1" ]] && echo "(quiet hours — queued, will not auto-play)"
echo "https://duho-macstudio.taila27502.ts.net/reports/status-audio/latest.mp3"
