# Backend cutover to main — executed by the Lab session

By: Claude Code (Lab session) on Duho's authorization ("get the backend onto main"). 2026-07-22 ~22:05 KST.

## Discovery
The live uvicorn API server was NOT running off the feat branch — it ran from a PINNED runtime-candidate
worktree `runtime-candidates/origin-main-cc4ced2-20260629T132728/backend` at cc4ced2 (29 commits behind main).
Celery + celery-autowiki already ran from the primary checkout. Split/stale setup.

## What was done
- Confirmed low risk: cc4ced2 -> main = 0 migrations, 0 dependency changes, 8 backend files (runner + draft_provenance + config/tasks + tests).
- Moved the primary checkout to main content (detached @ 0674910) — reworked runner present.
- Repointed com.nebulamind.backend plist WorkingDirectory: runtime-candidate(cc4ced2) -> /Users/duhokim/NebulaMind/NebulaMind/backend (primary @ main). Backup: com.nebulamind.backend.plist.bak-pre-main-cutover-20260722.
- Reloaded backend (bootout+bootstrap) + restarted celery/celery-autowiki/labworker.

## Result — VERIFIED
- API healthy: nebulamind.net/api/lab/runs = 200; /api/pages = 200.
- REWORKED runner LIVE: GET /api/lab/runs now returns lit_grounded (honest grounding status) — the field the rework added.
- Backend + celery now BOTH run from the primary checkout at main = consistent, no longer stale cc4ced2.
- Closes Kun's "backend runs off an un-merged/stale checkout" finding.

## Rollback (if ever needed)
Restore com.nebulamind.backend.plist.bak-pre-main-cutover-20260722, bootout+bootstrap com.nebulamind.backend.
Note: the primary checkout is on DETACHED main (0674910); it won't auto-advance if main moves — re-checkout origin/main to update.
