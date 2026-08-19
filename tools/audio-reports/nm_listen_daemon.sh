#!/bin/zsh
# nm_listen_daemon.sh — native auto-player for NebulaMind status readings.
# Polls latest.txt on the Studio; when it changes, plays latest.mp3 aloud.
# No browser, no click. Stop for now: killall afplay. Stop for good:
#   launchctl bootout gui/$UID/net.nebulamind.status-listener
BASE="https://duho-macstudio.taila27502.ts.net/reports/status-audio"
STATE="$HOME/.nm_status_listener_last"
while true; do
  stamp=$(curl -fsS --max-time 8 "$BASE/latest.txt" 2>/dev/null)
  if [[ -n "$stamp" && "$stamp" != "$(cat "$STATE" 2>/dev/null)" ]]; then
    if [[ -f "$STATE" ]]; then   # first poll only arms; don't replay an old reading
      f=$(mktemp /tmp/nm_reading_XXXX).mp3
      curl -fsS --max-time 30 "$BASE/latest.mp3" -o "$f" && afplay "$f"
      rm -f "$f"
    fi
    print -r -- "$stamp" > "$STATE"
  fi
  sleep 8
done
