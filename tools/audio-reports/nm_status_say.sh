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
[[ "${NM_FORCE_LIVE:-}" == "1" ]] && pub_args+=(--force-live)
pub=$(python3 "$S/nm_audio_publish.py" "${pub_args[@]}") || exit 1
quiet=$(print -r -- "$pub" | python3 -c 'import json,sys; print("1" if json.load(sys.stdin)["quiet"] else "0")')
if [[ "$quiet" != "1" && -z "${NM_SAY_NO_PLAY:-}" ]]; then
  # Playback receipt for THIS host, written when sound starts (2026-08-21).
  seqno=$(print -r -- "$pub" | python3 -c 'import json,sys; print(json.load(sys.stdin)["seq"])')
  print -r -- "{\"seq\":$seqno,\"file\":\"$(basename $out)\",\"host\":\"$(hostname -s)\",\"event\":\"STARTED\",\"local_time\":\"$(date '+%Y-%m-%dT%H:%M:%S%z')\"}" >> "$R/played.jsonl"
  ( if afplay "$out" >/dev/null 2>&1; then ev=COMPLETED; else ev=INTERRUPTED; fi
    print -r -- "{\"seq\":$seqno,\"file\":\"$(basename $out)\",\"host\":\"$(hostname -s)\",\"event\":\"$ev\",\"local_time\":\"$(date '+%Y-%m-%dT%H:%M:%S%z')\"}" >> "$R/played.jsonl" ) &
fi
# Archive index + alignment + slide deck are rebuilt by nm_report_postprocess.sh,
# which the publisher spawns (it must run AFTER the transcript exists).
# Readings with no transcript still get an index refresh here.
[[ -z "$text" ]] && ( python3 "$S/nm_audio_index.py" >> "$R/index.log" 2>&1 ) &
echo "$out"
[[ "$quiet" == "1" ]] && echo "(quiet hours — queued, will not auto-play)"
# Stable per-reading link. (A lane added deck.html?f=<stem> for this at 23:35 on
# 08-20 — right diagnosis, and it now points at the fuller status-report page,
# which postprocess renders for every reading.) latest.mp3 is a
# single shared slot and now races — with three Fables publishing into one dir it
# resolves to whoever wrote last (2026-08-20: Hwao overwrote Tori's by 48s and the
# wrong reading played). Keep latest.mp3 for the self-polling listen page, which
# is *meant* to track the newest; link the stable URL for "play that reading".
echo "https://duho-macstudio.taila27502.ts.net/reports/status-audio/report-${TS}-${slug}.html"
echo "https://duho-macstudio.taila27502.ts.net/reports/status-audio/latest.mp3"
