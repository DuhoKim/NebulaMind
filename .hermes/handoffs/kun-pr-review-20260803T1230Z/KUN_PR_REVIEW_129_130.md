# KUN ADVERSARIAL PR REVIEW — #129 and #130

Task ID: `kun-pr-review-20260803T1230Z`
Reviewer: Kun on Hermes via Nous Portal route `moonshotai/kimi-k3`
Date: 2026-08-03 (~21:30-22:00 KST / 12:30-13:00 UTC)
Context: same session as the 2026-08-03 architecture audit; these PRs close my R1 and R5/action-#4.

---

## PR #129 — `live-state-capture-20260803` (commit `e4b4ac5`, base `9c7941c`)

**Verdict: MERGE_OK** (with one advisory note, not a nit on the diff itself)

### Content check — all 10 files justified, nothing smuggled

| File | Verdict | Evidence |
|---|---|---|
| `frontend/src/app/lab/frontiersData.ts` (+321/−221) | Justified | Committed blob sha256 = `b3b0f6d5…` — byte-identical to the rerank-receipt-pinned staging file. Exact match to claim. |
| `frontend/src/app/lab/frontierScope.ts` (new, 43 lines) | Justified | Scope policy module. Independently verified: 57 IDs, 57 unique, zero dupes, covers 0–56 completely; unknown IDs fail closed to `out_of_scope`. No abs paths/secrets. |
| `frontend/scripts/test-galaxy-frontier-scope.mjs` (new, 142 lines) | Justified, substantive | 24 assert calls; loads the real TS via transpile+vm, checks ID coverage against actual `frontiersData.ts` FRONTIERS, fail-closed on 999, scope wiring in DraftBoard/LabStages/stageData/package.json. Not vacuous. |
| `DraftBoard.tsx` (+11/−10), `LabStages.tsx` (+17/−13), `stageData.ts`, `subnavVideos.ts`, `package.json` | Justified | Diffs reviewed in full; all are the scope-wiring + copy updates + embedding video swap + one script entry, exactly as described. |
| `z9-10-…-deficit.pdf` (binary) | Justified | 104,031 bytes in commit == live-tree file exactly; ~104KB is sane for a compiled study PDF. |
| `z9-10-…_history.json` (+44/−20) | Justified | Well-formed JSON (parsed: 6 top-level keys). Note: much of the +/- churn is Unicode-escaping normalization (`–` → `–` etc.), but it is NOT purely cosmetic — new `humanFeedback` entries exist (COMMISSIONED / FRAMING items). Semantic comparison old vs new: NOT equal — real content added, consistent with "history refresh". |

### Cross-verification against the live tree (the PR's whole reason to exist)

All 10 files: `git show e4b4ac5:<file>` sha256 == live-tree file sha256 — **10/10 MATCH**. The claim "captures the exact working-tree state serving nebulamind.net" is TRUE at file level.

Additional confirmations:
- Base `9c7941c` (#128) is the current origin/main tip and DOES contain the alpha-knee trio (`tools/nm_alpha_knee.py`, `lab_runner_worker.py`, `overnight_loop.py` — 3 files, 415 insertions) — so the "missing lab-runner branch" issue from my audit morning state is handled on the base, not smuggled into this PR. Correct layering.
- The referenced `receipts/PROMOTION_RECEIPT_20260803_frontier_staging_to_live.md` EXISTS (backfilled ~20:2x KST, names Hwao/Fable as actor, stepwise in-session user authorizations, timeline matching my audit's independent mtime observations: 18:38 catch-up +41→994, 18:50 promotion, 18:57 build `Pja97kcysgU-pDNO6Ufik`, ~19:00 kickstart + chunk-verify). It answers my §9 uncertainties (12:30 weekly was scheduled; 18:3x/18:4x runs were manual; 429 log tail predates the retry patch).
- GitHub PR file list == local commit file list (diff empty).
- Secret/abs-path scan of the full diff: zero hits for tokens/keys/`/Users/`/passwords/Bearer.
- The live checkout has since been checked out ONTO `e4b4ac5` and is clean (`git status` empty), tip = e4b4ac5 — the capture is already the serving commit.

### Advisory (non-blocking)

1. The PR body says "The live worktree's git status is clean as of this commit" — verified true NOW, but note the served `.next` build (18:57) still predates the commit (19:38): the build was produced from identical content, so no rebuild is strictly required, but the first rebuild after merge is what makes the served artifact git-traceable end-to-end. Recommend (not require) a rebuild + restart receipt after merge.
2. `_history.json` Unicode-escaping churn will make future human diffs noisier; harmless.

## PR #130 — `frontier-scheduler-lane-20260803` (commit `78c2949`, base `9c7941c`)

**Verdict: MERGE_OK**

### Correctness

1. **Matches launchd invocation.** CLI exposes exactly `daily --limit N` and `weekly` subcommands (argparse, lines 418–430); plist invokes `-m app.agent_loop.frontier_ranking daily --limit 300` (14:00 KST) and weekly (Mon 12:30). Module path, subcommands, and flag all align. Limit validation 1–500 matches the audited catch-up guard bound.
2. **Receipts match reality.** Module-written receipt keys vs the real receipt files in the engine dir:
   - daily: module emits exactly the 10 keys of the real `daily_frontier_ingest_20260803T093855Z.json` (status/lane/generated_at/before/after/added_papers/automatic_wiki_integration/live_frontend_updated/stdout_tail/receipt). MATCH.
   - weekly finished: module emits exactly the 14 keys of the real `weekly_frontier_rerank_20260803T094257Z.json`. MATCH.
   - weekly skipped path: `skipped_no_new_papers` + 12 keys == real scheduled 12:30 receipt `…033006Z.json`. MATCH.
   - Receipt filename pattern `{lane}_{ts}Z.json` matches the on-disk naming. `live_frontend_updated: False` always, with a hard invariant that raises if the live file's sha changes during weekly — the fail-closed staging-only discipline is enforced in code, not just promised.
3. **Quarantine is honest.** `test_arxiv_daily_intake.py`: module-level `pytest.skip(..., allow_module_level=True)` with accurate reason; I verified NONE of the 6 imported symbols (`build_intake_fields`, `canonical_arxiv_id`, `collect_daily_rss_candidates`, `persist_daily_rss_intake`, `query_arxiv_rss`, `select_unseen_papers`) exist in committed `app/agent_loop/arxiv_fetch.py`. Body preserved intact below the skip (312 lines vs dev's 307 untracked — the 5 extra lines are the skip itself).
4. **Tests are substantive, not vacuous.** 5 tests: CLI wiring (both lanes, monkeypatched, asserts exact call sequence + JSON stdout), daily ingest with real tmp engine + store invariants + receipt write, refusal on misaligned embedding store, weekly snapshot-never-writes-live (asserts live sha unchanged), weekly skip path preserving staging. Verified run in the PR's own clone: **5 passed, 1 skipped in 0.11s** — matches the PR description exactly.
5. **Secret/abs-path scan** of the full commit: zero hits. Module resolves the engine dir relative to `__file__` with a `NEBULAMIND_FRONTIER_ENGINE_DIR` env override — no hardcoded user paths.

### Rebase integrity

- `git diff 9c7941c 78c2949` and `git diff e4b4ac5 644a52e` are **byte-identical diffs** (diff-of-diffs empty; patch-ids equal: `bc964b59…`). The rebase is pure: Goru's 3-file addition atop e4b4ac5 was transplanted onto origin/main `9c7941c` with zero content change.
- Base correctness: `78c2949` sits directly on `9c7941c` (clone `git log` confirms `78c2949 → 9c7941c → 4a9d628`). Since #128 landed between Goru's authoring and the rebase, the rebase was necessary and done right.

### Content independence of #129 and #130

Zero shared files (`comm` on name lists: none); #130's 3 files do not exist in `e4b4ac5`'s tree. Either merge order works; no hidden ordering constraint. (Trivially, both target disjoint paths: frontend vs backend/tests.)

### Message/description accuracy

Every verifiable claim in both PR bodies checked out: file lists, test counts/timings, sha pins, BUILD_ID, receipt references, quarantine reason, authorship/rebase narrative. One soft spot: #130's body says tests were "re-checked" by Hwao before push — I cannot see that session, but my own independent run in the clone reproduces 5 passed / 1 skipped, so the outcome claim is confirmed regardless.

### Nits (non-blocking, for the record)

1. `frontier_ranking.py` CLI default `--limit 100` vs the launchd plist's explicit `--limit 300` — harmless (plist is explicit), but if anyone runs the module bare they get the old default. Consider syncing the default to 300 in a future commit.
2. The quarantined test file's skip message cites "Kun audit R5" — fine, but a link to the future unquarantine condition (the daily-RSS intake lane landing in `arxiv_fetch.py`) would make the quarantine self-service. Body preservation makes this recoverable anyway.
3. `WEEKLY_TIMEOUT_SECONDS = 300` for rerank + generator over a 994-paper delta is adequate today (observed runs complete in seconds), but the delta grows ~40/day; the timeout will eventually need raising or the weekly job will start failing closed. Not a merge blocker — failing closed is the designed behavior.

## Ranked findings summary

None blocking. Advisory items: (#129) post-merge rebuild+restart receipt to make the served artifact end-to-end git-traceable; (#130) CLI default/plist drift, weekly timeout growth curve, quarantine unskip-condition pointer.

## Evidence ledger

Commands (read-only):
- `gh pr view 129|130 --repo DuhoKim/NebulaMind --json …` (metadata, files, bodies); `gh pr diff 129|130 --name-only` cross-checked against local commit name-lists (identical both PRs).
- Dev repo: `git show e4b4ac5` (+ per-file, full diff read of LabStages/DraftBoard/stageData/subnavVideos/package.json/_history.json/frontierScope.ts/smoke test); `git show e4b4ac5~1:…_history.json` for semantic compare; `git merge-base e4b4ac5 origin/main` → `9c7941c`; `git show 9c7941c --stat`; `git ls-files tools/nm_alpha_knee.py` (tracked); sha256 comparison of all 10 PR-129 files vs live-tree files (10/10 match); frontiersData committed blob sha == `b3b0f6d5…`; scope-ID coverage/dupe arithmetic; secret-pattern grep of both commits (zero hits).
- Live checkout: `git log -2` (tip e4b4ac5), `git status` (clean), `.next/BUILD_ID` mtime/content.
- Worktree clone `.claude/worktrees/frontier-scheduler-lane`: `git log -3` (78c2949 → 9c7941c → 4a9d628); `git rev-parse HEAD`; patch-id + diff-of-diffs rebase-integrity check (identical); PR-independence `comm` check (no shared files); full read of `backend/app/agent_loop/frontier_ranking.py` (434 lines); reads of both test files; symbol-existence grep against committed `app/agent_loop/arxiv_fetch.py` (0/6 present — quarantine accurate).
- Receipts read (content): `PROMOTION_RECEIPT_20260803_frontier_staging_to_live.md` (full); key-set comparison of real daily/weekly/skipped receipts vs module-emitted keys (exact matches).
- Tests executed: `pytest tests/test_frontier_ranking_scheduler.py tests/test_arxiv_daily_intake.py -q` from the worktree clone using dev venv → **5 passed, 1 skipped in 0.11s** (no repo litter: tmp_path fixtures).
- launchd plist re-read (`com.nebulamind.frontier-daily`: `daily --limit 300`, 14:00) for invocation match.

Files read (content): as enumerated above; names-only listing of nothing sensitive; no `.env*` touched; no GitHub mutations; no git writes.

## Uncertainties

- Hwao's pre-push verification session itself (out of band for me) — outcome independently reproduced, so immaterial.
- Whether the PDF's internal content corresponds to the `_history.json` narrative — I verified sizes/hashes/JSON validity, not PDF text (binary; content review was the crew's gate, and the history narrative is internally consistent).
- The `_history.json` Unicode-escaping change's producer (likely the writer tool's JSON serializer) — cosmetic, not investigated further.

---

KUN_PR_REVIEW_COMPLETE_20260803T1230Z
