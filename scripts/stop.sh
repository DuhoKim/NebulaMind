#!/usr/bin/env bash
# NebulaMind — stop all services

PROJECT_DIR="$HOME/NebulaMind"
LOGS_DIR="$PROJECT_DIR/logs"

echo "🛑 Stopping NebulaMind services..."

stop_pid() {
  local name="$1"
  local pidfile="$LOGS_DIR/$2.pid"
  if [ -f "$pidfile" ]; then
    local pid=$(cat "$pidfile")
    if kill -0 "$pid" 2>/dev/null; then
      kill "$pid" && echo "  ✓ $name stopped (PID $pid)"
    else
      echo "  - $name was not running"
    fi
    rm -f "$pidfile"
  else
    echo "  - $name: no PID file found"
  fi
}

stop_pid "Cloudflare Tunnel"  "cloudflared"
stop_pid "Next.js frontend"   "frontend"
stop_pid "Celery beat"        "celery_beat"
stop_pid "Celery worker"      "celery_worker"
stop_pid "FastAPI backend"    "backend"

echo "  Stopping Docker services..."
cd "$PROJECT_DIR"
docker compose down
echo "  ✓ PostgreSQL + Redis stopped"

echo ""
echo "✅ All NebulaMind services stopped."
