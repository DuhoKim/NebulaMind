#!/usr/bin/env bash
# NebulaMind — check service status

PROJECT_DIR="$HOME/NebulaMind"
LOGS_DIR="$PROJECT_DIR/logs"

echo "📊 NebulaMind Service Status"
echo "══════════════════════════════"

check_pid() {
  local name="$1"
  local pidfile="$LOGS_DIR/$2.pid"
  printf "  %-22s" "$name"
  if [ -f "$pidfile" ]; then
    local pid=$(cat "$pidfile")
    if kill -0 "$pid" 2>/dev/null; then
      echo "✅ running  (PID $pid)"
    else
      echo "❌ stopped  (stale PID $pid)"
    fi
  else
    echo "❌ stopped  (no PID file)"
  fi
}

check_pid "FastAPI backend"    "backend"
check_pid "Celery worker"      "celery_worker"
check_pid "Celery beat"        "celery_beat"
check_pid "Next.js frontend"   "frontend"
check_pid "Cloudflare Tunnel"  "cloudflared"

echo ""
echo "  Docker containers:"
docker compose -f "$PROJECT_DIR/docker-compose.yml" ps --format "    {{.Name}}: {{.Status}}" 2>/dev/null || echo "    (docker compose not available)"

echo ""
echo "  Endpoints:"
curl -sf http://localhost:8000/health > /dev/null && echo "  ✅ API  http://localhost:8000/docs" || echo "  ❌ API  http://localhost:8000 (not responding)"
curl -sf http://localhost:3000 > /dev/null && echo "  ✅ UI   http://localhost:3000"          || echo "  ❌ UI   http://localhost:3000 (not responding)"
