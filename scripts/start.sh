#!/usr/bin/env bash
# NebulaMind — start all services
set -e

PROJECT_DIR="$HOME/NebulaMind/NebulaMind"
BACKEND_DIR="$PROJECT_DIR/backend"
FRONTEND_DIR="$PROJECT_DIR/frontend"
LOGS_DIR="$HOME/NebulaMind/logs"
VENV="$BACKEND_DIR/.venv/bin"

mkdir -p "$LOGS_DIR"

echo "🚀 Starting NebulaMind services..."

# 1. Docker (postgres + redis)
echo "  [1/6] Starting Docker services..."
cd "$PROJECT_DIR"
docker compose up -d
echo "       PostgreSQL + Redis started"

# Wait for DB to be ready
sleep 3

# 2. FastAPI backend
echo "  [2/6] Starting FastAPI backend..."
cd "$BACKEND_DIR"
nohup "$VENV/uvicorn" app.main:app --host 0.0.0.0 --port 8000 \
  > "$LOGS_DIR/backend.log" 2>&1 &
echo $! > "$LOGS_DIR/backend.pid"
echo "       Backend started (PID $(cat $LOGS_DIR/backend.pid))"

# 3. Celery worker
echo "  [3/6] Starting Celery worker..."
cd "$BACKEND_DIR"
nohup "$VENV/celery" -A app.agent_loop.worker worker \
  --pool=threads --concurrency=4 --loglevel=info \
  > "$LOGS_DIR/celery_worker.log" 2>&1 &
echo $! > "$LOGS_DIR/celery_worker.pid"
echo "       Celery worker started (PID $(cat $LOGS_DIR/celery_worker.pid))"

# 4. Celery beat
echo "  [4/6] Starting Celery beat..."
cd "$BACKEND_DIR"
nohup "$VENV/celery" -A app.agent_loop.worker beat \
  --loglevel=info \
  > "$LOGS_DIR/celery_beat.log" 2>&1 &
echo $! > "$LOGS_DIR/celery_beat.pid"
echo "       Celery beat started (PID $(cat $LOGS_DIR/celery_beat.pid))"

# 5. Next.js frontend
echo "  [5/6] Starting Next.js frontend..."
cd "$FRONTEND_DIR"
nohup npm run dev \
  > "$LOGS_DIR/frontend.log" 2>&1 &
echo $! > "$LOGS_DIR/frontend.pid"
echo "       Frontend started (PID $(cat $LOGS_DIR/frontend.pid))"

# 6. Cloudflare Tunnel
echo "  [6/6] Starting Cloudflare Tunnel..."
if command -v cloudflared &> /dev/null; then
  nohup cloudflared tunnel run nebulamind \
    > "$LOGS_DIR/cloudflared.log" 2>&1 &
  echo $! > "$LOGS_DIR/cloudflared.pid"
  echo "       Cloudflare Tunnel started (PID $(cat $LOGS_DIR/cloudflared.pid))"
else
  echo "       ⚠️  cloudflared not found — skipping"
fi

# 7. MCP Server
echo "  [7/7] Starting MCP Server..."
MCP_DIR="$HOME/NebulaMind/NebulaMind/mcp"
if [ -f "$MCP_DIR/.venv/bin/python3" ]; then
  cd "$MCP_DIR"
  nohup .venv/bin/python3 server.py --transport sse --host 0.0.0.0 --port 8001 \
    > "$LOGS_DIR/mcp.log" 2>&1 &
  echo $! > "$LOGS_DIR/mcp.pid"
  echo "       MCP Server started (PID $(cat $LOGS_DIR/mcp.pid))"
else
  echo "       ⚠️  MCP venv not found — skipping"
fi

echo ""
echo "✅ All NebulaMind services started!"
echo "   API docs:  http://localhost:8000/docs"
echo "   Frontend:  http://localhost:3000"
echo "   MCP:       http://localhost:8001/sse"
echo "   Logs:      $LOGS_DIR/"
