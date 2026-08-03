# Kun Phase 3.1 — read-only conflict census brief

Task ID: `quartet-kun-application-20260721T114246Z-phase3-census`

## Authority

Hwao ratified Phase 2 with `HWAO_PHASE2_LAB_IA_DECISION_RATIFIED_20260721` and recommended the read-only P3.1 conflict census. This brief authorizes only analysis plus one receipt file. Every git action gate remains held.

Canonical plan: `.hermes/plans/2026-07-21_205603-kun-report-quartet-application-plan.md`
Phase 2 decision: `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase2/LAB_IA_DECISION.md`

## Verified snapshot

- Branch `feat/surveys-atlas-ia-p1-20260627`
- HEAD `826e733`
- Cached `origin/main` `28e87357`
- Merge base `63f7b305`
- 6 ahead / 66 behind
- 20 modified + 360 top-level untracked
- Chosen disposition: `REWORK PIECEMEAL`

If any of those values drift, stop and report; do not create the output.

## Goal

Precompute a read-only conflict census for each conceptual unit and each of the six commits without changing the index, worktree, refs, object database, or branch. The census must distinguish textual merge conflict from conceptual supersession and dirty-worktree overlap.

## Allowed read-only methods

- `git merge-base`, `rev-parse`, `rev-list`, `log`, `show`, `diff`, `diff-tree`, `ls-tree`, `status`, `check-ignore`
- Legacy three-tree output form only: `git merge-tree <base-treeish> <branch1-treeish> <branch2-treeish>`
- Read-only Python/shell processing of command output
- Read existing Phase 1/2 receipts and relevant source files

## Forbidden methods

- Never use `git merge-tree --write-tree` (it writes objects).
- No `git hash-object -w`, `commit-tree`, `mktree`, or any command that writes objects/refs/index.
- No branch/worktree creation or switch, checkout, reset, stash, rebase, cherry-pick, commit, add, restore, clean, fetch, push, PR, or merge.
- No product/source/test edit; no moves/deletes/archives/quarantine.
- No `.env*` content access, DB/SQL/migration, runtime, deploy, restart, network, browser, cloud, cockpit, or publication.

## Required census

### A. Six-commit table

For each commit `ac0608c`, `e5ceda8`, `fd15e8e`, `01e8afa`, `586fef1`, `826e733`, record:

- parent/base commit;
- paths changed;
- paths also changed on `origin/main` since the merge base;
- legacy `merge-tree` conflict indicators when applying that commit's delta against current `origin/main`;
- conflict classes (`clean`, `content`, `add/add`, `delete/modify`, `dependency-only`, `conceptually superseded`);
- dirty-worktree overlap paths;
- Phase 2 proposed fate.

Do not treat a zero textual-conflict count as semantic safety.

### B. Per-unit census

1. **Surveys Atlas IA** — committed `ac0608c` plus current dirty extensions and six new survey components. Name same-path upstream changes, add/add risks such as independently-created `plotting.ts`, and the five/other dirty overlaps relevant to the unit.
2. **Wiki sources fix** — `e5ceda8`; identify the four upstream touches to `WikiSourcesClient.tsx` and whether a raw pick would conflict or merely be stale.
3. **Backend autonomous runner** — backend/worker subset of `fd15e8e`; separate branch-only clean additions from `backend/app/main.py` router registration and from the abandoned frontend configurator half. Record the +85 dirty worker extension.
4. **Lab frontend IA** — `fd15e8e` frontend half plus `01e8afa`, `586fef1`, `826e733`; identify add/add/same-name divergence and intermediate files later deleted by HEAD. Treat conceptual supersession as a blocker even if a mechanical merge looks possible.

### C. Execution-shape recommendation

Restate, without executing, the bounded Phase 3 recommendation:

- fresh cached `origin/main` base;
- isolated topical worktrees only after G3 approval;
- rework surveys, re-apply wiki fix, hold backend runner for product decision, no Lab frontend replay;
- exact conflict stop rules and tests from Phase 2;
- list what a future G3 approval packet must include.

## Required output

Write only:

`.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase3/CONFLICT_CENSUS.md`

The receipt must include:

- snapshot verification;
- six-commit census table;
- four per-unit sections;
- explicit textual-vs-semantic conflict distinction;
- dirty-overlap map;
- future G3 packet checklist;
- safety ledger with zero branch creation/switch, worktree creation, index/ref/object writes, rebase, cherry-pick, commit, stash, reset, move, delete, product edit, DB/runtime/network/publication action, and `.env*` content reads;
- a statement that G3/G5/G7 remain held/closed and no action is authorized;
- final standalone marker `KUN_PHASE3_CONFLICT_CENSUS_COMPLETE_20260721`.
