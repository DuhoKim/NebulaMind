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
RECEIPTS="$HOME/.nm_played.jsonl"      # playback receipts, collected by the Studio
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
      # Entries newer than our state, in order, quiet-flag included. State only
      # advances THROUGH successes: a failed download/play stops the walk so the
      # reading is retried next poll instead of being skipped forever (review
      # finding 2026-08-20). Quiet entries advance without playing.
      todo=$(print -r -- "$q" | python3 -c "
import json,sys
q=json.load(sys.stdin)
for e in q['entries']:
    if e['seq'] > int('$last'):
        print(e['seq'], 1 if e.get('quiet') else 0, e['file'])")
      if [[ -n "$todo" ]]; then
        print -r -- "$todo" | while read -r seq isquiet file; do
          if [[ "$isquiet" == "1" ]]; then
            print -r -- "$seq" > "$STATE"
            continue
          fi
          f="/tmp/nm_readings/$file"
          if curl -fsS --max-time 60 "$BASE/$file" -o "$f"; then
            # PLAYBACK RECEIPT (2026-08-21, Hwao's request): written when sound
            # actually starts on THIS host, never on enqueue. A missing receipt
            # must keep meaning "nobody heard it" — that is the whole point.
            print -r -- "{\"seq\":$seq,\"file\":\"$file\",\"host\":\"$(hostname -s)\",\"event\":\"STARTED\",\"local_time\":\"$(date '+%Y-%m-%dT%H:%M:%S%z')\"}" >> "$RECEIPTS"
            if afplay "$f"; then ev=COMPLETED; else ev=INTERRUPTED; fi
            print -r -- "{\"seq\":$seq,\"file\":\"$file\",\"host\":\"$(hostname -s)\",\"event\":\"$ev\",\"local_time\":\"$(date '+%Y-%m-%dT%H:%M:%S%z')\"}" >> "$RECEIPTS"
            rm -f "$f"
            print -r -- "$seq" > "$STATE"
          else
            rm -f "$f"
            break   # retry this entry on the next poll
          fi
        done
      fi
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
