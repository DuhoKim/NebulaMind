# KUN NEBULAMIND ARCHITECTURE AUDIT — 2026-08-03

Task ID: `kun-architecture-audit-20260803T1010Z`
Coordinator: Hwao/Fable. Requested by Duho.
Reviewer: Kun on Hermes via Nous Portal route `moonshotai/kimi-k3`
Date: 2026-08-03 (~19:10-20:10 KST / 10:10-11:10 UTC)
Prior pass: `.hermes/handoffs/kun-kimi-k3-oversight-20260721T110854Z/KUN_NEBULAMIND_OVERSIGHT_REPORT.md`

---

## 1. Executive verdict

`HEALTHY_WITH_ESCALATED_RISKS`

The product is up and serving (localhost:3000 HTTP 200, nebulamind.net HTTP 200, lab. 308 to canonical), the frontier-ranking loop is genuinely producing receipts (994 papers, coverage to 2026-07-31, hash-pinned staging), and focused tests executed in this pass are all green (5/5 trust-cap + canary, frontier-scope smoke, surveys-IA smoke). But the two risks I flagged 13 days ago have mutated into a sharper shape: the dev checkout now sits on a DETACHED HEAD at `origin/main` with 5 modified and 341 untracked files, and — worse — the previously clean live serving checkout `NebulaMind-origin-main-live` is now DIRTY with 8 modified + 2 untracked files and is one commit BEHIND origin/main (#127 not landed), while serving a production build (BUILD_ID mtime 18:57 today) that no commit anywhere describes. The frontier-data promotion executed today is byte-verifiable and receipt-anchored (staging sha256 `b3b0f6d5…` == in-tree live file in BOTH checkouts), but the promotion itself — and the 18:57 rebuild of the live frontend — has no handoff receipt I can find: what is serving right now is not reconstructible from git alone.

## 2. Delta vs 2026-07-21 — status of the 7 prior prioritized actions

1. **Fate of `feat/surveys-atlas-ia-p1-20260627` (rebase/merge or shelve).** Status: PARTIAL / SUPERSEDED. The 6-ahead/66-behind divergence is gone because the branch situation was resolved sideways: dev checkout is now detached at `origin/main` (`4a9d628`), and local `main` (`6553874`, #126) is exactly one commit behind. Evidence: `git branch --show-current` = "(HEAD detached at origin/main)"; `git rev-list --count HEAD..origin/main` = 0; `git log main..origin/main` = only #127. The surveys branch commits were either landed via PRs (#119–#126 are all lab-surface) or abandoned — I did not diff the old branch tip. Detached HEAD is itself a hazard (see §4).
2. **Worktree hygiene sweep (~360 untracked).** Status: UNTOUCHED. 341 untracked in dev (was ~360). Root-level junk improved slightly (only 6 untracked root files now: 5 `*.applescript` + `.hermes.md`; the old `click.js`/`test_*.applescript` litter is mostly gone), but `docs/` untracked ballooned to 278 entries and `tools/` holds 44 untracked incl. 8+ `.bak` files (`live_provider_usage_monitor.py.bak-*` x3, `gemini_app_usage*.bak-*` x3). `backend/celerybeat-schedule-v2.db.db` (double extension) sits untracked.
3. **Baseline Claim Ledger Contract v1.** Status: DONE (contract stage). Board updated 2026-07-21T13:43Z: `CLAIM_LEDGER_CONTRACT_V1_AGN_COMPLETE_20260703T0830Z` now marked complete, status/debate map is "next", execution phrase `NO ACTIVE EXECUTION PHRASE`, G6/apply gates still held. Caveat: the board's own updated timestamp (07-21) is two weeks stale relative to today, and no status/debate-map design proposal artifact surfaced in `.hermes/plans/` newer than 2026-07-28 (paper-board plans, not Baseline).
4. **Reconcile Lab frontend divergence (which tree is authoritative).** Status: PARTIAL — inverted. The old divergence (live-tree files missing in dev) is resolved: dev now contains the lab surface. But a NEW divergence exists in the opposite direction: live checkout carries uncommitted hand-patches (`frontierScope.ts` + `test-galaxy-frontier-scope.mjs` untracked; `DraftBoard.tsx`, `stageData.ts`, `subnavVideos.ts`, `package.json`, `LabStages.tsx` modified) — I checked dev for `frontierScope.ts`: dev tree also has `frontend/src/app/lab/frontierScope.ts` untracked (per `git status` cluster listing, `frontend` has 3 untracked entries). So the same WIP scope feature sits uncommitted in both trees. No recorded decision about authority found.
5. **Test-teardown FK cycle + test-DB litter.** Status: PARTIAL. Root-level `test*.db` litter is gone from `git status` (only `backend/celerybeat-schedule-v2.db.db` remains, which is a runtime artifact, not a test DB). I did not re-run the broader suites that showed the SAWarning, so the FK-cycle fix is unverified.
6. **5 known pre-existing tool-test failures.** Status: NOT VERIFIED. Not re-run this pass (time-boxed to focused suites).
7. **`backend/.env.redacted-before-disable-gemini-20260708_174609`.** Status: UNTOUCHED. Still untracked in dev tree (name listed only; never opened).

Net: 1 done, 3 partial, 2 untouched, 1 unverified. The hygiene/secret-adjacent items are the same as 13 days ago.

## 3. Architecture map as-built today

**Product runtime (dev checkout `/Users/duhokim/NebulaMind/NebulaMind`):** FastAPI backend (`backend/app`, port 8000 via launchd `com.nebulamind.backend`), PostgreSQL+Redis via Docker (`scripts/docker_compose_init.sh` — locally patched uncommitted to auto-launch Docker.app and wait 300s), Celery workers + beat (`com.nebulamind.celery*`), Next.js 15 frontend source in `frontend/src/app`.

**Serving topology (the two-checkout reality):**
- DEV: detached HEAD at `origin/main` tip `4a9d628` (#127); 5 modified / 341 untracked.
- LIVE: `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live`, branch `main` at `6553874` (#126) = one commit behind origin/main; 8 modified / 2 untracked; `next start -p 3000` via launchd `com.nebulamind.frontend` (state=running, pid 6985, KeepAlive, RunAtLoad).
- Production build `.next/` rebuilt today 18:57 KST — AFTER the 18:46 frontiersData.ts promotion — so the served build includes the uncommitted promotion.
- Cloudflare tunnel: `cloudflared tunnel run` process alive (`com.nebulamind.cloudflared`); nebulamind.net 200 in 0.93s; lab.nebulamind.net 308 → `https://nebulamind.net/` (canonical redirect working).
- Backend API + celery on same host; logs under `/Users/duhokim/NebulaMind/logs/`.

**Research pipelines:**
- Frontier-ranking engine: `.hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718/` — immutable base `corpus_ga_co_2009_2026.jsonl` (120,676 rows, sha256 verified == Yui plan pin `e5a91e5f…`), frozen map `frontier_map_v3.json` (sha verified), incremental delta now 994 papers / 860 assigned / 134 novel-or-noise, coverage 2026-07-03→2026-07-31 (receipt `daily_frontier_ingest_20260803T093855Z.json`).
- Retry/backoff patch present in `ingest_incremental.py` (429/5xx with Retry-After honor, cap 300s).
- Weekly rerank receipt `weekly_frontier_rerank_20260803T094257Z.json`: 57 clusters reranked over base+860, constants frozen, staging `frontiersData.v3.staging.ts` sha `b3b0f6d5…` pinned IN the receipt, `live_frontend_updated: false` at receipt time.
- Promotion (later same day, ~18:46 KST): staging file copied byte-identical into BOTH checkouts' `frontend/src/app/lab/frontiersData.ts` (verified by sha256 match in all three locations); pre-promotion backup `frontiersData.live.backup-20260803T1850K.ts` exists but does NOT match committed HEAD version (sha `08ec69b7…` vs HEAD `4d07f80d…`) — i.e. the backup captured the already-dirty in-tree file, not the last committed one. The last committed frontiersData is recoverable only from git objects.
- Lab runner: `tools/lab_runner_worker.py` modified uncommitted — new `alpha-knee-age-radius` method branch importing untracked `tools/nm_alpha_knee.py` (APOGEE 3-table join); `tools/overnight_loop.py` modified — non-circularity gate extended to knee results.

**Trust stack:** `backend/app/services/trust_calculation.py` — `_apply_debate_stance_semantic_cap` now COMMITTED (in HEAD; was working-tree-only on 07-21); tests `test_trust_debate_stance_caps.py` + `test_model_canary.py` committed and passing (5/5 this pass).

**Automation (launchd, 22 nebulamind plists):** frontier-daily 14:00 KST `--limit 300` (moved from 10:45; brief confirmed), frontier-weekly Mon 12:30, evidence_boost_retry 09:00, gen-debates 10:00, gen-hero 09:30, regenerate 03:00, security-scan 17:00, plus backend/celery x4/cloudflared/docker-init/frontend/gemini-usage-autofetch/labworker/services/tunnel-health and `net.nebulamind.kun-tui`. Two stale plist backups (`celery.plist.before-arxiv-repair`, `.pre-reform-validation.bak`, `backend.plist.bak-pre-main-cutover-20260722`) linger in LaunchAgents dir.

**Doctrine/gates:** `.hermes/plans/2026-07-01_205807-paper-prose-distillation-roadmap.md` canonical; board P0 apply gate HELD, `NO ACTIVE EXECUTION PHRASE`. Yui's overnight arXiv preview plan `docs/plans/2026-07-31_223011-…md` remains PLAN ONLY awaiting user approval phrase — and its predicted failure mode (arXiv 429 → fail-closed guard) is exactly what `logs/frontier.daily.error.log` still shows (HTTP 429 tracebacks), though today's manual catch-up succeeded around it.

## 4. Ranked risks/blockers (adversarial)

**R1 (HIGH) — The live product is no longer reconstructible from git.**
Failure scenario: `NebulaMind-origin-main-live` serves a build whose inputs are: main@#126 + 8 uncommitted hand-patches + 2 untracked files + one data-file promotion. If the frontend process dies and the box reboots after a disk event, or if anyone runs `git checkout -- .` / `git clean` in that checkout out of habit, the exact served state is unrecoverable — `frontierScope.ts` and the DraftBoard scope-filter logic exist nowhere in any commit. Yesterday's clean-mirror property (my 07-21 anchor) is gone. There is no receipt recording WHO promoted frontiersData.ts at 18:46 or WHO rebuilt at 18:57 and under what authorization — the engine receipts explicitly say `live_frontend_updated: false`, so the actual promotion step happened outside the receipted pipeline. This is precisely the "promotion-without-commit" pattern: the artifact chain (receipt → staging sha → live sha) is verifiable, but the ACTOR and GATE for the final copy+rebuild are not recorded anywhere I could find.

**R2 (HIGH) — Detached HEAD dev checkout with live-writing automation.**
`com.nebulamind.frontier-daily` and the engine scripts run with WorkingDirectory inside the dev checkout while HEAD is detached. Any accidental `git checkout <branch>` by a human or agent instantly changes what the daily 14:00 job executes. Detached HEAD also means any accidental commit created now is orphaned (only reachable via reflog). 34 local branches + 2 stashes (`live-deploy local WIP pre-main-sync 20260719`, parked WIP from 06-21) compound the entropy.

**R3 (MEDIUM-HIGH) — Receipt-less state transitions in the lab surface.**
Beyond the frontend promotion: `subnavVideos.ts` in the live tree has a NEW uncommitted video ID swap (`embedding: Ruk9fTgn5_E → piNaIKTedHQ`) auto-written by `tools/watch_subnav_videos.py` (itself untracked in dev) — an automated writer mutating the serving tree with no receipt in `.hermes/handoffs/` that I could locate. The `z9-10-unlensed-metallicity-deficit.pdf` and its `_history.json` in `frontend/public/studies/` are also modified uncommitted in the live tree — public-served study artifacts changed outside git. Pattern: the live checkout is drifting into a hand-maintained server directory, the exact failure mode the clean-mirror discipline existed to prevent.

**R4 (MEDIUM) — frontier-daily still fails on arXiv 429; retry patch is in the engine script but the launchd path may not exercise it.**
`logs/frontier.daily.error.log` ends in a raw `urllib.error.HTTPError: 429` traceback (pre-patch timestamp ordering unclear; receipts show successful runs 08-01/02/03). The 07-25→08-01 daily receipts show gaps (no receipts 07-28→07-31), then a 4-day catch-up (+41 covering through 07-31) run manually this morning. The loop is recovering, but coverage is being maintained by operator intervention, not by the schedule. Yui's plan documents "last exit code 1" and zero weekly runs as of 07-31 — the weekly rerank receipt from 08-03 12:30 KST (Monday) suggests the weekly job DID fire today (12:30 receipt exists, generated by schedule or manually — receipt doesn't say).

**R5 (MEDIUM) — WIP scheduler code in the daily job's import path.**
`backend/app/agent_loop/frontier_ranking.py` (the module launchd runs daily) is UNTRACKED, and Yui's plan explicitly labels it a prototype that "must be treated as work-in-progress, not canonical production code" — yet it is the production daily job. `backend/tests/test_frontier_ranking_scheduler.py` and `test_arxiv_daily_intake.py` are also untracked; the latter imports symbols absent from committed `arxiv_fetch.py` (per Yui's plan) so it cannot pass as-is.

**R6 (LOW-MEDIUM) — Hygiene/secret-adjacent items unchanged.** `.env.redacted…` file still in tree; 8+ `.bak` files in tools/; `celerybeat-schedule-v2.db.db` runtime artifact in repo root of backend; 3 stale plist backups in LaunchAgents.

**R7 (LOW) — Baseline board timestamp drift.** Board last updated 07-21; claim-ledger-complete status is 4 weeks old relative to the 07-03 contract marker; status/debate map "next" has no dated design artifact. During DESI-paper crunch this is understandable, but the flagship mission's visible state is stale.

## 5. Evidence/trust assessment — doctrine vs enforcement

Machine-checked TODAY:
- Immutable corpus + frozen map: sha256 verified against Yui plan pins (base `e5a91e5f…` ✓, frozen map `620a7e46…` ✓). Delta artifacts' shas changed since the plan (expected — 720→994 papers growth is receipted).
- Rerank receipt pins staging sha256; staging == live-in-tree file byte-identical in both checkouts (I verified independently). This is a genuinely auditable artifact chain for the DATA.
- Trust-cap: debate-stance semantic cap is committed code with committed tests, 5/5 pass in this pass.
- frontierScope logic has a smoke test in the LIVE tree (`test-galaxy-frontier-scope.mjs` → `galaxy_frontier_scope_ok`, run this pass) — but that test file itself is uncommitted.
- Fail-closed ingest guard (window-saturation → audited catch-up) fired as designed during the 429 storm, per Yui's plan + error log.

Aspirational / NOT machine-checked:
- Baseline "every prose sentence binds to a ledger entry" — still no production ledger artifact; claim ledger is a validated contract-stage artifact (07-03), not wired to prose rendering.
- The promotion gate itself (staging → both checkouts + rebuild): no machine check, no receipt, no recorded authorization phrase. The strongest trust culture in the project (receipts) stops one step short of the actual public mutation.
- `wiki_schema.md` coverage block (33/33 topics, 49 pages) is a doc edit, uncommitted — freshness unverified against the live DB.

## 6. Engineering/reproducibility

Commands run and results (all in this pass, read-only except this report):
- `pytest tests/test_trust_debate_stance_caps.py tests/test_model_canary.py -q` (backend/.venv) → 5 passed in 0.70s. No test-DB litter observed in `git status` afterward.
- `node scripts/test-galaxy-frontier-scope.mjs` (live frontend) → `galaxy_frontier_scope_ok`.
- `node scripts/test-surveys-atlas-ia.mjs` (dev frontend) → passed.
- HTTP probes: localhost:3000 200 (24ms); nebulamind.net 200 (0.93s); lab.nebulamind.net 308 → nebulamind.net.
- sha256 verification of corpus base, frozen map, staging ts, in-tree live ts (both checkouts), backup ts, HEAD-version ts (see §3).
- launchd state: `launchctl print gui/$UID/com.nebulamind.frontend` (running, pid 6985), `com.nebulamind.frontier-daily` (not running, scheduled 14:00).
- NOT run: full backend suite, `next build`, migrations, DB queries (no DB access attempted).

Reconstructibility verdict: DEV checkout behavior is reconstructible from origin/main + 5 visible diffs + 341 untracked files (mostly docs/tools, but including the DAILY JOB's module and the lab runner's new dependency `nm_alpha_knee.py`). LIVE served product is NOT reconstructible from git alone — requires the current dirty live checkout plus the engine-dir staging file. The only committed anchor for the live lab surface is main@#126, which is not what is serving.

## 7. Prioritized next actions (owner / action / expected evidence / gate)

1. **Hwao + user — Commit or intentionally snapshot the live checkout state.** Land `frontierScope.ts` + DraftBoard/stageData/subnavVideos/package.json patches + frontiersData.ts promotion as a reviewed PR to main, then fast-forward live. Evidence: live `git status` clean, `git log` shows the promotion commit, BUILD_ID newer than commit. Gate: user approval for git writes (per standing gate).
2. **Hwao — Backfill a promotion receipt for the 2026-08-03 18:46/18:57 KST promotion+rebuild.** One markdown file naming actor, authorization, sha chain (staging b3b0f6d5… → live), build ID. Evidence: receipt file in engine dir. Gate: none (docs only).
3. **Hwao/Tori — Attach HEAD in dev checkout** (create/switch to a branch at `4a9d628` or fast-forward local main to origin/main). Evidence: `git branch --show-current` non-empty. Gate: user approval (git write).
4. **Goru — Commit the frontier scheduler lane properly:** `backend/app/agent_loop/frontier_ranking.py` + its test + either fix or formally quarantine `test_arxiv_daily_intake.py`. The daily production job must not run untracked code. Evidence: tracked files in a PR, focused tests green. Gate: normal review.
5. **Hwao — Decide authority for lab-surface WIP shared by both trees** (frontierScope feature): single source, one commit, promoted via the receipted path. Evidence: recorded decision + PR. Gate: Hwao decision + user git gate.
6. **Tori — Extend engine receipts to cover the promotion step** (`live_frontend_updated` currently always false; make the copy+rebuild a receipted action with actor field). Evidence: next promotion receipt shows true + shas. Gate: none for tooling change; user approval if it touches the live tree.
7. **Goru — Hygiene sweep, same scope as 07-21 action #2 plus:** move/delete `backend/.env.redacted-…`, `celerybeat-schedule-v2.db.db`, tools/*.bak (8+), 3 stale LaunchAgents plist backups, 278 untracked docs/ entries triaged. Evidence: inventory + reduced `git status` count. Gate: user approval before any deletion.
8. **Lana/Hwao — Date-stamp the Baseline status/debate-map design proposal** (board "next" since 07-21). Evidence: artifact under `.hermes/plans/`. Gate: existing docs-only gate.

## 8. Evidence ledger

Commands executed (read-only; cwd dev checkout unless noted):
- `git status --short` (wc 346; 5 modified / 341 untracked), `git rev-parse HEAD`, `git log --oneline -8`, `git branch -a`, `git describe --all`, `git stash list`, `git diff --stat`, `git diff` (5 modified files), `git rev-list --count HEAD..origin/main` / `origin/main..HEAD` (0/0), `git log main..origin/main` (#127 only), `git rev-parse main` vs `origin/main`, untracked-cluster awk counts.
- Live checkout: `git log --oneline -8` (tip 6553874 #126), `git status --short` (10), `git diff --stat` + `git diff` (DraftBoard/stageData/subnavVideos/package.json), `git rev-list --count main..origin/main` (1).
- sha256: `shasum -a 256` on frontiersData.ts (dev, live, staging, backup, `git show HEAD:` version), corpus base, frontier_map_v3.json, delta artifacts, reranked map.
- Receipts read (content): `daily_frontier_ingest_20260803T093855Z.json`, `weekly_frontier_rerank_20260803T094257Z.json`; receipts dir listing (14 files 07-23→08-03).
- `grep -n retry/backoff` in `ingest_incremental.py`; `ls -lt` engine dir; `find .hermes -newer board…` for recent artifacts; `ls .hermes/handoffs | grep` for claim/baseline/deploy/promote receipts.
- launchd: `launchctl print gui/$UID/com.nebulamind.frontend` + `…frontier-daily`; `plutil -p` on all 22 `com.nebulamind.*` plists + `net.nebulamind.kun-tui`; `ps aux | grep cloudflared`.
- HTTP GET probes: `curl` localhost:3000, nebulamind.net, lab.nebulamind.net (status/timing only).
- Logs: `tail` of `logs/frontier.daily.error.log` (429 traceback), `logs/frontier.daily.log` (receipt JSONL).
- Tests: `pytest tests/test_trust_debate_stance_caps.py tests/test_model_canary.py -q` → 5 passed; `node scripts/test-galaxy-frontier-scope.mjs` (live) → ok; `node scripts/test-surveys-atlas-ia.mjs` (dev) → passed.
- `.next/BUILD_ID` mtime (stat) + content read; source file mtimes for promoted/patched lab files.

Files read (content): prior Kun report (full); KUN_BRIEF.md; `.hermes/board/paper-prose-distillation-board.md` (lines 1-120 of 143); `docs/plans/2026-07-31_223011-nebulamind-overnight-arxiv-corpus-ranking-preview.md` (first ~60 lines + section 2 head); dev `git diff` full text of 5 modified files; live `git diff` of 4 lab files + package.json; `ingest_incremental.py` (grep excerpts only).

Names-listed only (never opened): `backend/.env`, `backend/.env.example`, `backend/.env.redacted-before-disable-gemini-20260708_174609`, `.claude/` untracked entry, LaunchAgents plist contents beyond plutil keys shown.

## 9. Uncertainties + deliberately not inspected

- NOT inspected: any `.env*`/credential content (per constraint); production DB contents/queries; running Celery workers' actual task state; MCP server behavior; `fulltext_cache` (25k entries) content; tmux panes; Docker container state; the public cockpit HTML/JSON; `autowiki/`; the 278 untracked docs/ files individually (names sampled only); whether the 08-03 12:30 weekly rerank was launchd-fired or manual (receipt doesn't record the trigger); who executed the 18:46 promotion and 18:57 rebuild (no receipt found — this is a finding, R1/R2, not an oversight).
- NOT run: full backend pytest suite, `next build`/lint, migration checks, any write anywhere except this report file.
- Fact vs inference: "live product not reconstructible from git" is FACT (dirty live tree + untracked files + build newer than any commit). "Promotion lacked authorization" is INFERENCE — no receipt/record found, but an out-of-band approval I cannot see may exist; the finding is that the record is absent, not that the act was unauthorized. "frontier-daily still 429-prone" is FACT for the error-log tail; whether the retry patch has since run clean under launchd is UNKNOWN (today's success receipts were from a manual catch-up context per the brief; schedule fires 14:00 KST and receipts at 09:38/09:40 UTC = 18:38/18:40 KST suggest manual runs). "The backup file not matching HEAD" is FACT; its implication (backup captured dirty state) is arithmetic, not speculation.

---

KUN_KIMI_K3_ARCHITECTURE_AUDIT_COMPLETE_20260803T1010Z
