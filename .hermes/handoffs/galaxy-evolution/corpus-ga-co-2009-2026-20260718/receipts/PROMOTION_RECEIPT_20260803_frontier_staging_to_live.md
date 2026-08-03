# Promotion receipt — frontier staging → live frontend, 2026-08-03

Backfilled 2026-08-03 ~20:2x KST by the actor, in response to Kun audit finding R1 / action #2
(`.hermes/handoffs/kun-architecture-audit-20260803T1010Z/KUN_NEBULAMIND_ARCHITECTURE_AUDIT_20260803.md`).
All times KST.

## Actor and authorization

- Actor for every step below: **Hwao/Fable** (Claude Code session, this repo's coordinator seat).
- Authorization: **Duho, live in-session**, stepwise:
  1. "apply the fix and run the catch-up" — ingest retry patch + plist reschedule + limit-500 catch-up.
  2. "run the weekly rerank too" — weekly rerank (staging only).
  3. "promote the staging to live" — the promotion + rebuild + restart recorded here.

## Timeline of operator actions (2026-08-03)

| Time (KST) | Action | Evidence |
|---|---|---|
| ~18:20 | Retry/backoff patch (`fetch_bytes`, 429/5xx + Retry-After ≤300s, attempts 4) added to `ingest_incremental.py`; verified by `py_compile` + 5-paper `--dry-run` | patch in file; dry-run output `window_saturated: true` |
| ~18:25 | `com.nebulamind.frontier-daily` rescheduled 10:45→**14:00 KST**, then `--limit 100→300`; a stray plutil-inserted arg caught and removed; job re-bootstrapped | plist now `daily --limit 300`, StartCalendarInterval 14:00 |
| 18:38 | Manual audited catch-up `daily --limit 500`: **+41 papers, 953→994, coverage → 2026-07-31** | `daily_frontier_ingest_20260803T093855Z.json` |
| 18:40 | Smoke test of the exact launchd invocation (`--limit 300`): finished, added 0 | `daily_frontier_ingest_20260803T094048Z.json` |
| 18:42 | Manual weekly rerank post-catch-up: 57 clusters, 31 movements, staging regenerated; `live_frontend_updated: false` (correct — promotion is a separate act) | `weekly_frontier_rerank_20260803T094257Z.json` |
| ~18:48 | Pre-promotion backup of the in-tree live data file → `frontiersData.live.backup-20260803T1850K.ts` (sha256 `08ec69b7…`). NOTE (per Kun): this captured the already-dirty in-tree state, NOT committed HEAD (`4d07f80d…`); the last committed version remains recoverable via `git show HEAD:frontend/src/app/lab/frontiersData.ts` in either checkout | backup file in engine dir |
| ~18:50 | Promotion: `frontiersData.v3.staging.ts` copied byte-identical over `frontend/src/app/lab/frontiersData.ts` in BOTH checkouts (dev + `NebulaMind-origin-main-live`) | sha256 `b3b0f6d5613de75d…` in all three locations, == staging sha pinned in the 18:42 rerank receipt |
| 18:57 | Production `next build` in the live checkout | `.next/BUILD_ID` = `Pja97kcysgU-pDNO6Ufik`, mtime 18:57:29 |
| ~19:00 | `launchctl kickstart -k gui/501/com.nebulamind.frontend`; end-to-end verify: `https://nebulamind.net/lab` HTTP 200, HTML references new chunk `page-3609d8a748976e0c.js`, chunk carries new value (`size:1317` present, old `size:1316` absent) | curl + chunk grep, this session |

## Clarifications for open audit uncertainties (§9 of the Kun report)

- The 12:30 KST `weekly_frontier_rerank_20260803T033006Z.json` was the **scheduled launchd** weekly run (pre-catch-up, nothing new at that time). The 18:42 rerank and both 18:3x/18:40 daily receipts were **manual** runs by the actor above.
- The `logs/frontier.daily.error.log` 429 tail predates the retry patch (last failed scheduled run was 10:45 this morning, pre-patch). First unattended test of the patched 14:00/limit-300 job: 2026-08-04 14:00 KST.
- The promotion was executed as uncommitted working-tree changes in both checkouts, following the standing pattern — committing this state to main is Kun action #1 and awaits Duho's git gate.

## Addendum — merge + traceable rebuild, 2026-08-03 ~22:2x KST

- Duho merged PR #129 (squash `636f118`) and PR #130 (squash `eee27d6`); Kun pre-merge review: both MERGE_OK, 0 blocking (`.hermes/handoffs/kun-pr-review-20260803T1230Z/`).
- Live worktree `main` reset --hard to `origin/main` = `eee27d6` (pre-reset diff verified: only the 3 backend scheduler files; frontend byte-identical). Status clean, 0 ahead/behind.
- Per Kun advisory #129-1: production rebuilt FROM the merged commit — new `.next` BUILD_ID `t-4cjL-dL-rFMEM4WMxlC` (supersedes `Pja97kcysgU-pDNO6Ufik`), service kickstarted, `https://nebulamind.net/lab` HTTP 200 first try, lab chunk carries promoted data (`size:1317`). Post-rebuild served chunk: `page-dd7fb6189c351d9f.js` (supersedes 19:0x `page-3609d8a748976e0c.js`; hash recorded per Kun delta re-audit N1). The served artifact is now end-to-end git-traceable: eee27d6 → build → serve.
- Dev worktree `studio-dev` fast-forwarded to `eee27d6`; redundant untracked copies of the 3 scheduler files removed after byte-verification (intake test's committed version = dev copy + quarantine block); `frontiersData.ts` absorbed. Remaining dev dirt: `scripts/docker_compose_init.sh`, `wiki_schema.md` only.
- Cleanup: stale local branch `live-state-capture-20260803` deleted; Goru's clone `.claude/worktrees/frontier-scheduler-lane` removed (commit merged); remote PR branches auto-deleted.
- Actor: Hwao/Fable. Authorization: Duho — "merge both PRs".
