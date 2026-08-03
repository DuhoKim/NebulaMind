# Hygiene inventory — dev worktree, 2026-08-03 ~21:05 KST

Read-only census per Kun audit action #7 (R6). Actor: Hwao/Fable, authorized by Duho ("run the hygiene inventory").
Source: `git status --porcelain` on `/Users/duhokim/NebulaMind/NebulaMind` (branch `studio-dev` @ 9c7941c).
**Nothing was deleted, moved, or committed by this inventory.** Every disposition below is a RECOMMENDATION awaiting Duho's approval.

Totals: 3 modified tracked files, ~341 untracked (278 docs/, 44 tools/, 6 backend/, 3 frontend/, 5 root applescripts, crew dirs).

## Class A — COMMIT candidates (real code running or referenced in production)

| Path | Note |
|---|---|
| `backend/app/agent_loop/frontier_ranking.py` + `backend/tests/test_frontier_ranking_scheduler.py` + `backend/tests/test_arxiv_daily_intake.py` | Kun action #4 — Goru brief ready (`goru-frontier-scheduler-commit-20260803T1200Z/`), BLOCKED on Codex re-login |
| `tools/watch_subnav_videos.py` | The receipt-less live-tree writer (Kun R3) — must be tracked AND governed |
| `tools/` 26 more non-bak scripts (autopilot, dashboards ×4, cockpit guard/renderer, nm_* science modules ×5, gemini-usage suite ×6, tmux board tools, `templates/`, `tests/`) | Working crew tooling; recommend one or two "ops tooling" PRs |
| `backend/scripts/generate_video_gemini.py` | Video-gen tooling |
| `frontend/src/app/lab/rankMovement.ts` + `frontend/scripts/test-topic-rank-movement.mjs` + `frontend/public/human-cal/` | Rank-movement feature WIP in DEV (distinct from live's frontierScope WIP) — consumer for the FRONTIER_RANK_MOVEMENT export |
| Modified tracked: `scripts/docker_compose_init.sh` (Docker auto-launch patch), `wiki_schema.md` (33/33 coverage block) | Commit-worthy small diffs |
| Modified tracked: `frontend/src/app/lab/frontiersData.ts` | Do NOT commit separately — reconciles automatically when PR #129 merges and dev syncs |

## Class B — CREW RECORDS, keep as-is (recommend .gitignore entries, not commits)

- `.hermes/` (board/handoffs/plans — durable crew store), `.hermes.md`, `.claude/` (worktrees, session state)
- `docs/` untracked: 278 files — campaign packets and reports (24× paper_prose_readiness_pilot, ~30× page58 audit packets, galaxy_v2 workspaces, surveys packets, agent progress reports). Referenced by handoffs; recommend leaving in place now, optionally archiving families >30 days old into a dated tarball outside the repo later.
- Recommend a small PR adding `.gitignore` lines: `.hermes/`, `.hermes.md`, `.claude/`, `*.bak-*`, `celerybeat-schedule*`.

## Class C — DELETE candidates (await approval; nothing deleted)

1. **15 `tools/*.bak-*` files** — 10 timestamped `.bak` variants of `render_ge_autopilot_dashboard_v2.py` + 3 of the usage-monitor suite + 2 others (all Jul 9–18; live originals exist alongside).
2. **`tools/nm_alpha_knee.py.local-pre128-20260803`** — verified byte-identical (399/399 lines, empty numstat) to committed #128 `tools/nm_alpha_knee.py`; pure redundancy. (Earlier "differs" note in-session was an artifact of comparing against a not-yet-materialized file — corrected here.)
3. **5 root applescripts** — `click_textarea`, `click_via_js`, `open_new_gemini`, `paste_submit`, `run_js` (July Gemini-driving experiments, superseded).
4. **4 `docs/*backup*` dirs** — cockpit/dashboard backups from Jul 7 + Jul 21 (originals live in git or current docs).
5. ~~**`backend/celerybeat-schedule-v2.db.db`**~~ — **WITHDRAWN 2026-08-03 ~21:4x KST after the check (Duho-ordered): this is the LIVE celery-beat schedule DB, not an orphan.** Beat (pid 2548, `com.nebulamind.celery-beat`) runs with `--schedule=…/celerybeat-schedule-v2.db`; macOS shelve/ndbm appends `.db`, producing the double extension. File is 16.4 MB, mtime 20:03 today; no single-`.db` file exists. DO NOT DELETE. Covered by the proposed `.gitignore` line `celerybeat-schedule*` instead.
6. **LaunchAgents backups (outside repo)** — `com.nebulamind.celery.plist.before-arxiv-repair`, `com.nebulamind.celery.plist.pre-reform-validation.bak`, `com.nebulamind.backend.plist.bak-pre-main-cutover-20260722`. All non-`.plist` suffixes → launchd-inert; safe deletes.

## Class D — SECRET-ADJACENT (move out of tree, do not commit; Duho decision)

- `backend/.env.redacted-before-disable-gemini-20260708_174609` — **DONE 2026-08-03 ~21:5x KST (Duho-ordered):** moved to `~/HermesOps/secure/` (dir 700, file 600), contents never opened. Repo untracked count 317→316. Kun's twice-flagged item closed.

## Class E — inspect-later (unclassified small items)

- `playwright_test/`, top-level `tests/`, `tools/R15_prompt.txt`, `tools/build_hwao_2929_trust_recompute_stage_packet_20260705T122901Z.py`, `tools/gemini_burn_plan_patch.py` — one-off packet builders / experiment dirs; likely archive-or-delete, listed for a second look before any action.

## Proposed execution order (all gated on Duho's word)

1. C1–C4 + C6 deletions (mechanical, zero risk) — one approval covers them.
2. C5 after the celery-beat schedule_filename check.
3. D move-out (name the destination).
4. A commits as 2–3 PRs (scheduler lane via Goru once Codex re-auths; ops-tools; rank-movement WIP when its author is ready).
5. B .gitignore PR.
