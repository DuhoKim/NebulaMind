#!/bin/zsh
# One-line installer for the NebulaMind status listener (MacBook).
set -e
B="https://duho-macstudio.taila27502.ts.net/reports/status-audio"
mkdir -p ~/.local/bin ~/Library/LaunchAgents
curl -fsS "$B/nm_listen_daemon.sh" -o ~/.local/bin/nm_listen_daemon.sh
chmod +x ~/.local/bin/nm_listen_daemon.sh
curl -fsS "$B/net.nebulamind.status-listener.plist" -o ~/Library/LaunchAgents/net.nebulamind.status-listener.plist
launchctl bootout gui/$UID/net.nebulamind.status-listener 2>/dev/null || true
launchctl bootstrap gui/$UID ~/Library/LaunchAgents/net.nebulamind.status-listener.plist
echo "installed and running — new readings will play aloud here."
