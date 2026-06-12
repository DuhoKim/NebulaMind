#!/usr/bin/env bash
# Wait for Docker socket, then bring up NebulaMind containers.
# Called by com.nebulamind.docker-init LaunchAgent at login.

COMPOSE_DIR="$HOME/NebulaMind/NebulaMind"
DOCKER="/usr/local/bin/docker"
SOCKET="/var/run/docker.sock"
LOG="$HOME/NebulaMind/logs/docker_init.log"
MAX_WAIT=120   # seconds to wait for Docker to be ready
INTERVAL=5

mkdir -p "$(dirname "$LOG")"
echo "[$(date)] docker_compose_init.sh starting" >> "$LOG"

# Poll until Docker socket is ready
elapsed=0
while ! "$DOCKER" info >/dev/null 2>&1; do
    if [ "$elapsed" -ge "$MAX_WAIT" ]; then
        echo "[$(date)] Timed out waiting for Docker after ${MAX_WAIT}s" >> "$LOG"
        exit 1
    fi
    echo "[$(date)] Waiting for Docker... (${elapsed}s elapsed)" >> "$LOG"
    sleep "$INTERVAL"
    elapsed=$((elapsed + INTERVAL))
done

echo "[$(date)] Docker ready. Running docker compose up -d" >> "$LOG"
cd "$COMPOSE_DIR" && "$DOCKER" compose up -d >> "$LOG" 2>&1
echo "[$(date)] docker compose up -d finished (exit $?)" >> "$LOG"
