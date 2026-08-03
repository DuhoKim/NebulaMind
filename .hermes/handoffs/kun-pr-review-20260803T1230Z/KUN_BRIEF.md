# KUN BRIEF — Adversarial review of PR #129 and PR #130

Task ID: `kun-pr-review-20260803T1230Z`
Seat: Kun on Hermes / Nous `moonshotai/kimi-k3` (same session as the 2026-08-03 architecture audit — your audit context applies).
Coordinator: Hwao/Fable. Authorized by Duho: "have Kun review PR #129 and #130".

## Context

Both PRs exist because of your audit:
- **PR #129** `live-state-capture-20260803` — closes your R1. One commit `e4b4ac5`: captures the exact working-tree state serving nebulamind.net (frontiersData promotion, frontierScope WIP + smoke test, subnavVideos swap, z9-10 study PDF+history refresh, package.json script line). Commit is in the dev repo's object store; branch exists locally and on GitHub.
- **PR #130** `frontier-scheduler-lane-20260803` — closes your R5 / action #4. One commit `78c2949` (Goru-authored `644a52e` REBASED by Hwao from atop e4b4ac5 onto origin/main `9c7941c`): adds `backend/app/agent_loop/frontier_ranking.py` + `backend/tests/test_frontier_ranking_scheduler.py` (5 passed) + `backend/tests/test_arxiv_daily_intake.py` (module-level quarantine skip). The rebased commit lives in the clone at `/Users/duhokim/NebulaMind/NebulaMind/.claude/worktrees/frontier-scheduler-lane` (its `git show HEAD`), and on GitHub.

Access paths: local git (`git show e4b4ac5`, clone's HEAD) and read-only `gh` (`gh pr view/diff 129|130 --repo DuhoKim/NebulaMind`). gh is authed as DuhoKim.

## Review mandate (adversarial — hunt for what Hwao and Goru missed)

For EACH PR:
1. Exact content check — every file in the diff justified by the PR description? Anything smuggled (secrets, tokens, absolute paths, junk, oversized binaries)? #129 contains a binary PDF — sanity-check its size and that `_history.json` is well-formed JSON.
2. Correctness — #130: does `frontier_ranking.py` match what the launchd jobs actually invoke (`daily --limit 300`, `weekly`)? Do the receipts it writes match the real receipt files in the engine dir? Is the quarantine of `test_arxiv_daily_intake.py` honest (skip reason accurate, body intact) — and is `test_frontier_ranking_scheduler.py` actually testing behavior, not vacuous?
3. Rebase integrity — #130: confirm `78c2949`'s tree relative to `9c7941c` equals `644a52e`'s tree relative to `e4b4ac5` (pure-addition claim). Confirm #129 and #130 are content-independent (no hidden ordering constraint).
4. Message/description accuracy — no overclaims. Flag any claim you cannot verify.

## Hard constraints

- FINDINGS ONLY. No git writes, no GitHub mutations of any kind (no comments, reviews, approvals, labels — `gh pr view/diff` read-only is allowed). No `.env*` contents. No process actions. Temps only in this lane dir as `_tmp_*`.

## Deliverable (a FILE)

`.hermes/handoffs/kun-pr-review-20260803T1230Z/KUN_PR_REVIEW_129_130.md`:
- Per-PR verdict: `MERGE_OK` / `MERGE_WITH_NITS` / `BLOCK` + ranked findings with evidence.
- Evidence ledger (commands run, files read).
- End with marker: `KUN_PR_REVIEW_COMPLETE_20260803T1230Z`
