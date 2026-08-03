# GORU BRIEF — Commit the frontier scheduler lane (Kun audit action #4)

Task ID: `goru-frontier-scheduler-commit-20260803T1200Z`
Lane: **Goru on Codex gpt-5.5** (first Codex task since the 2026-08-03 reassignment — Codex Kun retired, Codex is now Goru's engine).
Coordinator: Hwao/Fable. Authorized by Duho: "brief Goru on #4".
Context: Kun architecture audit R5/action #4 — the production daily job `com.nebulamind.frontier-daily` runs `backend/app/agent_loop/frontier_ranking.py`, which is UNTRACKED in git, as are its tests. Production must not run untracked code.

## Objective

Get these three files properly tracked in a commit on a dedicated branch, tests green or formally quarantined:

1. `backend/app/agent_loop/frontier_ranking.py`  (the daily/weekly scheduler module — launchd runs it)
2. `backend/tests/test_frontier_ranking_scheduler.py`
3. `backend/tests/test_arxiv_daily_intake.py`  (WARNING per Yui's plan: imports symbols absent from committed `arxiv_fetch.py` — it may not pass as-is)

## Method (exact)

1. Create an isolated worktree INSIDE the repo (existing convention):
   `git worktree add /Users/duhokim/NebulaMind/NebulaMind/.claude/worktrees/frontier-scheduler-lane -b frontier-scheduler-lane-20260803 origin/main`
2. Copy the three files from the dev worktree (`/Users/duhokim/NebulaMind/NebulaMind`) into the same relative paths in the new worktree. Copy — do NOT move or modify the dev worktree's copies.
3. Run the two test files against the NEW worktree using the dev venv:
   `cd <new-worktree>/backend && /Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python -m pytest tests/test_frontier_ranking_scheduler.py tests/test_arxiv_daily_intake.py -q`
4. If `test_arxiv_daily_intake.py` fails on imports/symbols: FIRST try the minimal honest fix ONLY if it is trivially import-plumbing; otherwise quarantine formally — module-level `pytest.skip("quarantined 2026-08-03: imports symbols absent from committed arxiv_fetch.py — see Kun audit R5", allow_module_level=True)` at the top, keeping the test body intact. Do not delete or gut tests. `test_frontier_ranking_scheduler.py` must PASS for real.
5. Commit IN THE NEW WORKTREE, exactly these files (plus the quarantine edit if made). Never `git add -A`, never add anything else. Commit message:
   `feat(backend): track the frontier scheduler lane — daily/weekly frontier_ranking module + tests`
   with a body noting Kun audit R5/action #4 and the quarantine status of the intake test, ending with:
   `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`
6. Verify: `git show --stat HEAD` lists ONLY the intended files. If anything else appears, `git reset --soft` and redo the add.
7. Do NOT push. Do NOT open a PR. No network. Hwao pushes after inspection.

## Hard constraints

- Write only inside the new worktree and this lane dir (`.hermes/handoffs/goru-frontier-scheduler-commit-20260803T1200Z/`; temp files `_tmp_*` here).
- Never touch `.env*` contents; never delete anything; never modify the dev worktree, the live worktree (`NebulaMind-origin-main-live`), or any launchd plist.
- No `git push`, no `gh`, no network calls.

## Deliverable (a FILE, not stdout)

`.hermes/handoffs/goru-frontier-scheduler-commit-20260803T1200Z/GORU_REPORT.md` containing: commit sha, `git show --stat HEAD` output, full pytest output, what you did with the intake test (fix vs quarantine and why), and any anomalies. End with marker:
`GORU_CODEX_FRONTIER_SCHEDULER_COMMIT_COMPLETE_20260803T1200Z`
