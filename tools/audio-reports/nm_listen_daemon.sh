#!/bin/zsh
# nm_listen_daemon.sh v2 — queue-aware native auto-player (2026-08-20).
# Polls queue.json on the Studio; plays EVERY unplayed non-quiet reading in
# order (the old latest.txt latch dropped all but the last of a burst).
# Quiet-hours readings (quiet=true) are skipped for playback by design.
# Falls back to the latest.txt latch if queue.json is unreachable.
# Stop now: killall afplay. Stop for good:
#   launchctl bootout gui/$UID/net.nebulamind.status-listener
BASE="https://duho-macstudio.taila27502.ts.net/reports/status-audio"
STATE="$HOME/.nm_status_listener_seq"
LEGACY_STATE="$HOME/.nm_status_listener_last"
mkdir -p /tmp/nm_readings
while true; do
  q=$(curl -fsS --max-time 8 "$BASE/queue.json" 2>/dev/null)
  if [[ -n "$q" ]]; then
    last=$(cat "$STATE" 2>/dev/null)
    if [[ -z "$last" ]]; then
      # first poll only arms — never replay history on startup
      print -r -- "$q" | python3 -c 'import json,sys; print(json.load(sys.stdin)["seq"])' > "$STATE" 2>/dev/null
    else
      plays=$(print -r -- "$q" | python3 -c "
import json,sys
q=json.load(sys.stdin)
for e in q['entries']:
    if e['seq'] > int('$last') and not e.get('quiet'):
        print(e['seq'], e['file'])")
      maxseq=$(print -r -- "$q" | python3 -c 'import json,sys; print(json.load(sys.stdin)["seq"])')
      if [[ -n "$plays" ]]; then
        print -r -- "$plays" | while read -r seq file; do
          f="/tmp/nm_readings/$file"
          curl -fsS --max-time 60 "$BASE/$file" -o "$f" && afplay "$f"
          rm -f "$f"
          print -r -- "$seq" > "$STATE"
        done
      fi
      # advance past quiet entries too, so they are never back-played
      [[ -n "$maxseq" ]] && print -r -- "$maxseq" > "$STATE"
    fi
  else
    # legacy fallback: latest.txt latch
    stamp=$(curl -fsS --max-time 8 "$BASE/latest.txt" 2>/dev/null)
    if [[ -n "$stamp" && "$stamp" != "$(cat "$LEGACY_STATE" 2>/dev/null)" ]]; then
      if [[ -f "$LEGACY_STATE" ]]; then
        f=$(mktemp /tmp/nm_reading_XXXX).mp3
        curl -fsS --max-time 60 "$BASE/latest.mp3" -o "$f" && afplay "$f"
        rm -f "$f"
      fi
      print -r -- "$stamp" > "$LEGACY_STATE"
    fi
  fi
  sleep 8
done
