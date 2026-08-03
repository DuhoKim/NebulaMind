# Lana Phase 2 — Lab IA decision brief

Task ID: `quartet-kun-application-20260721T114246Z-phase2`

## Authority

The user directed the canonical plan to proceed. Hwao closed Phase 1 with `HWAO_PHASE1_CLASSIFICATION_RATIFIED_20260721` and released Phase 2. This is a read-only decision phase. No git or product mutation is authorized.

Canonical plan: `.hermes/plans/2026-07-21_205603-kun-report-quartet-application-plan.md`

## Current verified state

- Branch: `feat/surveys-atlas-ia-p1-20260627`
- HEAD: `826e733`
- Compared with locally cached `origin/main`: 6 ahead / 66 behind
- Dirty worktree: 20 modified + 360 top-level untracked entries
- Phase 1 classification: 222 KEEP-COMMIT, 130 ARCHIVE, 18 DELETE-CANDIDATE, 10 UNKNOWN; all later dispositions remain gated
- Contract v1 preservation and board reconciliation are complete and separate from this product decision

Six branch-only commits, oldest to newest:

1. `ac0608c feat(surveys): polish Atlas IA`
2. `e5ceda8 fix: show claim sources on wiki sources page`
3. `fd15e8e feat(lab): autonomous research runner with AASTeX + review-revise loop`
4. `01e8afa feat(lab): move configurator stage tabs into the sticky top banner`
5. `586fef1 feat(lab): lineate each topic's derivation in the Topic tab`
6. `826e733 refactor(lab): explanatory pipeline — dissolve frontier map into Topic tab`

Branch diff against its merge base with `origin/main`: 20 tracked files, 2,190 insertions, 111 deletions. Major areas include backend Lab runner, `tools/lab_runner_worker.py`, new `frontend/src/app/lab/**`, survey Atlas changes, wiki sources, middleware/layout, and tests.

## Goal

Inspect the six commits and the current Lab/Survey/Wiki implementation read-only, then choose exactly one disposition for the stale branch:

1. keep/rebase the branch as a whole;
2. cherry-pick selected commits;
3. rework selected ideas piecemeal on a clean base;
4. abandon the Lab IA work.

Do not take the action. Produce only the decision artifact.

## Required analysis

- Read `.hermes.md` and the canonical plan.
- Use read-only git history/diff/show/status commands only; no fetch.
- Inspect commit boundaries and relevant source/test files.
- Separate four conceptual units rather than treating the branch as one blob:
  - Atlas IA survey polish (`ac0608c`);
  - wiki claim-source fix (`e5ceda8`);
  - autonomous Lab runner (`fd15e8e`);
  - three-step Lab Topic/configurator IA evolution (`01e8afa`, `586fef1`, `826e733`).
- Account for 66 commits of upstream drift and current dirty worktree overlap.
- Assess whether each commit is self-contained, conflicts with current main architecture, depends on earlier branch commits, or encodes an idea worth reimplementing.
- Name tests/acceptance checks that a later G5 packet would need. Do not run mutating tests or create repo-local DBs.
- Do not open or read any `.env*` file.

## Required output

Write only:

`.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase2/LAB_IA_DECISION.md`

It must contain:

1. **Decision** — exactly one of `KEEP/REBASE`, `CHERRY-PICK`, `REWORK PIECEMEAL`, or `ABANDON`.
2. **Plain-English rationale** — why this option best preserves useful work while minimizing stale-branch risk.
3. **Six-commit disposition table** — one row per commit with conceptual unit, dependencies, conflict/staleness risk, and proposed fate under the chosen decision.
4. **Dirty-worktree interaction** — which of the 20 modified paths overlap or supersede the branch work, using Phase 1 classification without moving anything.
5. **Clean-base target** — recommend a fresh `origin/main`-based branch/worktree or explain why not; this is recommendation only.
6. **Future G5 execution packet** — exact bounded action sequence that would be proposed later, including preservation prerequisites, commit/file scope, conflict stop rules, tests, and rollback. Clearly state G5 is held.
7. **Rejected alternatives** — concise rejection of the other three options.
8. **Safety ledger** — zeros for branch creation/switch, rebase, cherry-pick, commit, stash, reset, move, delete, product edit, DB action, runtime action, network, and publication.
9. Final standalone marker: `LANA_PHASE2_LAB_IA_DECISION_COMPLETE_20260721`.

## Hard stops

- No branch creation, switch, checkout, worktree creation, rebase, cherry-pick, reset, stash, commit, add, push, PR, merge, or fetch.
- No source/product/test edits; only the one decision markdown file may be written.
- No moves, deletes, archives, quarantines, cleanup, DB/SQL/migration, runtime, deploy, restart, browser, cloud, cron, cockpit, or publication action.
- No `.env*` content access.
- If the six-commit history or 6/66 relationship has drifted, stop and report rather than deciding on a different snapshot.
