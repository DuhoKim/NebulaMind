#!/usr/bin/env bash
set -euo pipefail

# Deploy the PRODUCTION frontend (2026-08-20 overhaul).
#
# Production serves from the git WORKTREE at NebulaMind-origin-main-live, not
# from the dev checkout — the previous version of this script built and
# restarted the dev tree while cloudflared kept pointing at the live one, so
# "deploys" silently deployed nothing. Pass an explicit ref to serve;
# rollback = rerun with the previous ref (printed below at every deploy).
#
#   scripts/deploy_frontend.sh [git-ref]     # default: current worktree HEAD
#
LIVE="/Users/duhokim/NebulaMind/NebulaMind-origin-main-live"
FRONTEND="$LIVE/frontend"
NODE_PATH="/Users/duhokim/.nvm/versions/node/v24.13.0/bin:$PATH"
REF="${1:-}"

cd "$LIVE"
PREV=$(git rev-parse --short HEAD)
echo "live worktree at $PREV (rollback: scripts/deploy_frontend.sh $PREV)"
if [[ -n "$REF" ]]; then
  git fetch origin --quiet || true
  git checkout --quiet "$REF"
  echo "checked out $REF -> $(git rev-parse --short HEAD)"
fi

cd "$FRONTEND"
rm -rf .next/types   # stale generated types for deleted routes fail tsc
PATH="$NODE_PATH" npx tsc --noEmit
PATH="$NODE_PATH" npm run build
rm -rf .next/cache/fetch-cache

pkill -f "node_modules/.bin/next start" || true
sleep 2
nohup /opt/homebrew/bin/node node_modules/.bin/next start -p 3000 >/tmp/nebulamind-next.log 2>&1 &
sleep 4
# Smoke the surfaces that matter (the old script asserted a deprecated wiki page)
curl -fsS -o /dev/null http://localhost:3000/ && echo "smoke / ok"
curl -fsS -o /dev/null http://localhost:3000/lab && echo "smoke /lab ok"
curl -fsS -o /dev/null http://localhost:3000/surveys && echo "smoke /surveys ok"
echo "deployed $(git -C "$LIVE" rev-parse --short HEAD)"
