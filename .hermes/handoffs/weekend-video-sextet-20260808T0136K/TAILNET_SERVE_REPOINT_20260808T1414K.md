# Tailnet serve repointed — 0204 (rejected) → 1312K (current candidate)

Acted 2026-08-08 14:14 KST by the **Claude-macbook** seat (Directors board, pane %30), on Duho's
direct instruction in that pane: *"repoint the tailnet server at the 1312K directory"*.

## What changed

| | Before | After |
|---|---|---|
| PID | 97462 (started 12:54 KST, PPID 66392 = `hermes -p yui`, pane s007) | 33243 |
| Served directory | `integrator/canaries/spin-method-canary-20260808T0204` | `integrator/canaries/spin-method-overhaul-canary-20260808T1312K` |
| Bind | `100.84.12.101:8765` | `100.84.12.101:8765` (unchanged) |

**Why:** the 12:54 server was still exposing the canary Duho **rejected**. It survived the 14:05
gate containment, which only removed the `_weekend-canaries` copy from `cockpit/videos`. Anyone
opening the tailnet link would have watched the rejected cut.

## Watch URL

`http://100.84.12.101:8765/spin-method-overhaul-canary-20260808T1312K.mp4`

Contact sheet and SRT are in the same listing.

## Served-bytes verification

Done the way Tori verified 0204 — hash what the socket actually returns, not what is on disk:

- served: `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`
- on disk: `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`
- `POST_ENCODE_FREEZE.json`: `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`
- `Content-Length: 13697038`, `Content-type: video/mp4`, listing `HTTP 200`

Three-way match. Tori's *"re-verify the served bytes by hash if the file is exposed for Duho's
watch"* row can be closed against this, or independently re-run.

## Gate position

This is the route `HWAO_GATE_BREACH_CONTAINMENT.md` explicitly sanctions — *"serve the canary
directory directly — it is a handoff path, not a gated public location"* — rather than staging
copies into `cockpit/videos`. Tailnet-only; nothing uploaded, published, or made publicly
reachable.

No closed gate was touched: no file written into `cockpit/`, `frontend/public/`, or the integrator
canary tree; no Git write; **no deletion** — stopping PID 97462 ends a process, and every byte of
the 0204 attempt remains on disk. The 0204 directory is simply no longer exposed.

## Note for the yui seat on pane s007

PID 97462 was your child process. It was stopped, not crashed, and it is not supervised — it will
not come back on its own. If you need 0204 exposed again for a diagnostic comparison, use a
different port so the current candidate stays on 8765.
