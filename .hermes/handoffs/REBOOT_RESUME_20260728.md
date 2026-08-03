# Reboot resume runbook — Mac Studio · prepared 2026-07-28 14:25 KST (Hwao)

Context: Duho is updating macOS on all Macs. This host was prepped; nothing was mid-write
(autopilot idle, all agent panes idle, Tori's v9 re-verify finished 14:02, no DB writes in flight).

## Comes back AUTOMATICALLY at login (launchd)

backend :8000 (uvicorn) · frontend (next) · cloudflared tunnel · celery + celery-autowiki +
celery-beat · labworker · hermes gateway · hermesops static :8093 · static :8091 (dev frontend/public
→ tailnet /agent-reports + /human-cal; added as launchd `ai.hermesops.static8091` 2026-07-28 16:25,
previously ad-hoc and lost on reboot) · openwebui · usage monitors ·
docker-init → **now also launches Docker.app itself** → `docker compose up -d` (postgres:16, redis:7).

**Fix applied today:** `scripts/docker_compose_init.sh` used to only WAIT for the Docker daemon;
Docker Desktop doesn't auto-start at login, so after this morning's boot Postgres never came up and
the backend served health=500 from 12:41 until repaired at ~14:20. The script now runs
`open -g -a Docker` first and waits up to 300 s. Verified end-to-end today: containers up,
`/api/health` 200, nebulamind.net 200.

## Needs MANUAL relaunch (tmux panes; cwd = ~/NebulaMind/NebulaMind unless noted)

- `ge-mastermind` — pane 0: Claude session (`claude --resume` picks up Hwao's session);
  pane 1 Tori: `~/.hermes/hermes-agent/venv/bin/hermes -p default`
- `ge-autopilot`: `python3 tools/galaxy_evolution_autopilot.py watch --auto-approve-safe --print-ticks --interval 20.0`
- `ge-autopilot-dashboard-renderer`: `python3 tools/render_ge_autopilot_dashboard_v2.py --watch`
- `ge-pipeline-board-renderer`: `while true; do python3 tools/render_pipeline_board.py; sleep 60; done`
- `ge-provider-usage-monitor`: `python3 tools/live_provider_usage_monitor.py --watch` (without `--watch` it runs once and exits, killing the pane)
- `goru-agy`: `agy`

## Post-reboot verification (2 min)

1. `docker ps` → nebulamind-postgres-1 + nebulamind-redis-1 Up (if not: `tail ~/NebulaMind/logs/docker_init.log`)
2. `curl -s -o /dev/null -w '%{http_code}' http://localhost:8000/api/health` → 200
3. https://nebulamind.net and https://lab.nebulamind.net → 200
4. Cockpit pages refresh once the renderer panes are relaunched.

## Known-benign / notes

- `logs/labworker.err.log` contains a STALE h5py ModuleNotFoundError from an old interpreter config;
  current labworker (homebrew py3.11) imports fine — ignore unless it recurs with fresh timestamps.
- celerybeat-schedule*.db regenerate on start; no backup needed.
- Backend DB is Postgres in Docker (config.py default URL); app.db/nebula.db in backend/ are empty
  decoys — real data lives in the Docker volume, which survives reboot.
- DESI aa60182-26: v9 package is GO (Tori 8/8, 14:02 KST), sits on disk at
  `~/work/desi2/revision_aa60182/aa60182-26_revised_submission_v9.zip` — upload to nestor.aanda.org
  is Duho's pending action; nothing running, fully reboot-safe.
- This runbook covers the Mac Studio only. Mac Pro / other hosts and their lanes (e.g., Kun/Codex)
  need their own prep from those machines.
- Mac Pro (checked post-reboot 2026-07-28 15:40 KST): fully self-recovers via launchd — no tmux on
  that host, nothing manual. Ollama + ollama-proxy + backup.db + openclaw node all came back.
  Its flapping `ai.openclaw.gateway` job (start-blocked by mode=remote since ~May) was disabled;
  the node keeps retrying by design (self-heals if the Studio's deliberately-disabled openclaw
  gateway is ever re-enabled).
- MacBook Pro (checked 2026-07-28 15:50 KST): also fully self-recovers via launchd (own local
  openclaw gateway on loopback :18789 + node); no tmux lanes. Known-broken since May, not
  reboot-related: Discord bot @openaihwao 4014 "Disallowed intent(s)" (portal fix), and both
  Mac Pro + MacBook node spokes dial wss://gateway.nebulamind.net (CF tunnel) whose origin is
  the disabled Studio openclaw gateway → endless 502 retries (harmless, self-healing).
