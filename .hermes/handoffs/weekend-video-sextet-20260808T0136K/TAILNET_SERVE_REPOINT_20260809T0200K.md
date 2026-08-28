# Tailnet 8765 repointed — predecessor `40804f86…` → accepted cut `c5e7deed…`

Acted 2026-08-09 02:00 KST by the **Claude-macbook** seat (Directors board, pane %30), on Duho's
direct instruction in that pane: *"repoint 8765 at the accepted cut"*.

Supersedes `TAILNET_SERVE_REPOINT_20260808T1414K.md`.

## What changed

| | Before | After |
|---|---|---|
| PID | 33243 | 13053 |
| Served directory | `…/spin-method-overhaul-canary-20260808T1312K` | `…/spin-method-overhaul-canary-20260808T1959K` |
| Bind | `100.84.12.101:8765` | `100.84.12.101:8765` (unchanged) |
| Artifact | `40804f86…` (ACCEPTED WITH INCIDENT, superseded) | `c5e7deed…` (**ACCEPTED**) |

## Watch URL

`http://100.84.12.101:8765/spin-method-overhaul-canary-20260808T1959K.mp4`

## Served-bytes verification

Hashing what the socket returns, not what is on disk:

- served: `c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240`
- on disk: `c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240`
- `POST_ENCODE_FREEZE_V3.json` / `HWAO_FINAL_VERDICT_c5e7deed.md`: same
- `Content-Length: 16065978`, `Content-type: video/mp4`, listing `HTTP 200`

Four-way match.

## Note — two live routes now serve this candidate

Tori's packet records a separate listener on **8766** (PID 38142) rooted at `integrator/canaries`,
so the same bytes are reachable two ways:

- `:8765/spin-method-overhaul-canary-20260808T1959K.mp4` — short form, this server
- `:8766/spin-method-overhaul-canary-20260808T1959K/spin-method-overhaul-canary-20260808T1959K.mp4`
  — candidate-qualified; the bare filename under 8766 returns 404 because its root is the parent

Both serve in place with no copies. Duplication is not a gate problem, but one of them should be
retired to avoid a stale-route repeat of the confusion that made this repoint necessary. Retiring
8766 is Tori's call since it owns that listener; retiring 8765 is mine.

## Gates

Route only — no copy into `cockpit/videos`, `frontend/public`, or any protected root; no upload, no
publication, no Git write, no deletion. `100.84.12.101` is inside the non-global CGNAT range
`100.64.0.0/10`. Stopping PID 33243 ended a process; the `1312K` predecessor remains preserved on
disk with its ACCEPTED WITH INCIDENT record, and is simply no longer exposed on this port.

`video_reportable_now` remains `false`. This authorizes private viewing only.
