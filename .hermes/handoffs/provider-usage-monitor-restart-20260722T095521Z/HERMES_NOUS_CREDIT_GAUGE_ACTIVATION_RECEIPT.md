# Hermes / Nous credit quota activation receipt

Marker: `HERMES_NOUS_CREDIT_GAUGE_ACTIVATED_V1`
Completed at: `2026-07-22T10:21:32Z`

## Operator approvals

- `restart usage monitor` authorized replacement of provider monitor PID 80096 only.
- `restart private renderer` separately authorized replacement of private renderer PID 70437 only.

## Result

The `Hermes / Nous credits` card is active in the stable public status feed and the tailnet-private dashboard status feed.

Current read-only account snapshot:

- Total usable: `$43.12`
- Monthly Plus allowance: `$22.00`
- Monthly remaining: `$0.00`
- Purchased/top-up remaining: `$43.12`
- Monthly plan used: `100%`
- Renewal shown by provider: `Jul 24, 2026`

The purchased/top-up and total-usable sub-gauges intentionally have no percentage because the provider exposes no fixed denominator for purchased balance.

Source: normalized read-only `GET /api/oauth/account`; no token or credential value was emitted.

## Process receipt

- Old provider monitor PID 80096: gone.
- Active provider monitor PID 4900: one process, tmux `ge-provider-usage-monitor`, cadence `60s` local / `300s` slash.
- Old private renderer PID 70437: gone.
- Active private renderer PID 9602: one process, tmux `ge-autopilot-dashboard-renderer`, cadence `20s`.
- Renderer pane reported no new traceback/error after restart.

No duplicate monitor or renderer writer was present.

## Repeated-cycle verification

- Initial post-restart public/private usage observation: `2026-07-22T10:18:17Z`.
- Next full monitor cycle: public advanced to `2026-07-22T10:19:18Z`.
- Next renderer tick: private mirrored the same `2026-07-22T10:19:18Z` observation at `2026-07-22T10:19:34Z`.
- Public status: HTTP 200 with one `Hermes / Nous credits` card.
- Private tailnet status: HTTP 200 with one matching card and all three sub-gauges.
- Final stable cockpit guard: `PASS`; local rich checks pass, public rich check passes, HTTP 200, no stale writer, all protected files `uchg`.
- Public protected marker/layout was preserved.
- Static private HTML is the existing JavaScript shell and does not embed live balance literals; its served JSON feed was verified. Hydrated-browser DOM inspection was not run because browser automation was outside the approved scope.

## Test receipt

- Changed-path focused suite: `90 passed`.
- Python compile checks: passed.
- `git diff --check`: passed.
- Full private-renderer file plus monitor tests: `99 passed, 1 pre-existing unrelated failure`; the stale test expects overnight marker `GE_AUTOPILOT_OVERNIGHT_REPORT_20260712`, while current renderer source uses `GE_AUTOPILOT_OVERNIGHT_20260719_CORPUS_GATES_DONE`. That unrelated marker behavior was not changed.

## Backup

Pre-activation backup directory:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/provider-usage-monitor-restart-20260722T095521Z`

Manifest: `backup-manifest.json`

- 17 active artifacts copied from both public roots and the private status set.
- `all_hashes_match: true`.
- Backups were stored outside served roots.

## Source changes

- `tools/nous_credits_usage.py`
- `tools/live_provider_usage_monitor.py`
- `tools/render_ge_autopilot_dashboard_v2.py`
- `tools/stable_cockpit_guard.py`
- `tools/tests/test_nous_credits_usage.py`
- `tools/tests/test_provider_usage_quota_parsing.py`
- `tools/tests/test_stable_cockpit_guard.py`
- `tests/test_render_ge_autopilot_dashboard_v2.py`

These paths remain untracked in the already-dirty worktree. No Git action was taken.

## Explicit negatives

No purchase, top-up, billing/payment mutation, browser/account-page automation, DB write, SQL/apply, product deploy/restart, public route redesign, Git commit/push/merge, cron job, cloud/GCP change, or unrelated process restart occurred.
