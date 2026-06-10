#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/duhokim/NebulaMind/NebulaMind"
FRONTEND="$ROOT/frontend"
NODE_PATH="/Users/duhokim/.nvm/versions/node/v24.13.0/bin:$PATH"

cd "$FRONTEND"
PATH="$NODE_PATH" npx tsc --noEmit
PATH="$NODE_PATH" npm run build
rm -rf .next/cache/fetch-cache

pkill -f "node_modules/.bin/next start -p 3000" || true
sleep 2
nohup /opt/homebrew/bin/node node_modules/.bin/next start -p 3000 >/tmp/nebulamind-next.log 2>&1 &
sleep 2
curl -fsS -o /dev/null http://localhost:3000/wiki/galaxy-evolution
