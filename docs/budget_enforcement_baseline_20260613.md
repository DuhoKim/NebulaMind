# Budget Enforcement Baseline Marker (Audit D4)

**Baseline start:** 2026-06-13
**Enforcement flip date:** 2026-06-20
**Approved by:** Papa (2026-06-13, via HwaO dispatch)
**Spec:** `docs/nebulamind_state_audit_20260612.md` §1.2 / §8 D4

## What this is

`llm_calls` has been populating cleanly since 2026-06-12 (~1,008 calls/24h with
per-role success tracking). Budget caps are currently **log-only**:
`REGISTRY_ENFORCE_BUDGETS: bool = False` (`backend/app/config.py`). This file
marks the start of the 7-day baseline window before enforcement flips on.

## Flip procedure (2026-06-20)

1. Review the 7-day baseline: per-role call volume and success rates in
   `llm_calls` (2026-06-13 → 2026-06-20). Confirm per-lane caps in the page
   registry are sane against observed volume.
2. Set `REGISTRY_ENFORCE_BUDGETS=true` in `backend/.env` (env var overrides the
   config.py default via pydantic settings).
3. Restart services:
   `launchctl kickstart -k gui/$UID/com.nebulamind.backend`
   `launchctl kickstart -k gui/$UID/com.nebulamind.celery`
   `launchctl kickstart -k gui/$UID/com.nebulamind.celery-autowiki`
4. Verify enforcement: `[page_registry] budget check ... enforce=True` lines in
   celery logs; lanes that hit cap should stop dispatching instead of logging.
5. Watch the first 24h for over-aggressive blocking (compare against the
   baseline week); alert HwaO with any lane that gets starved.

A one-shot OpenClaw cron reminder is scheduled for 2026-06-20 09:00 KST in
Tori's session to trigger this procedure.
