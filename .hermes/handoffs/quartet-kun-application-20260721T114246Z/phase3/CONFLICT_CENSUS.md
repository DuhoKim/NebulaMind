# KUN PHASE 3.1 — READ-ONLY CONFLICT CENSUS

Task: quartet-kun-application-20260721T114246Z-phase3-census. Authority: Hwao Phase 2 ratified (`HWAO_PHASE2_LAB_IA_DECISION_RATIFIED_20260721`); disposition REWORK PIECEMEAL. Methods: read-only `rev-parse`, `rev-list`, `merge-base`, `diff-tree`, `merge-tree` legacy three-tree form only, `status`, `cat-file`, `rev-parse HEAD:<path>` blob compares. No `--write-tree`; no index/ref/object/worktree mutation; temp outputs in /tmp only (not removed by Kun after a guarded-cleanup denial; no repo impact).

## 1. Snapshot verification (all match brief; no drift)

Branch `feat/surveys-atlas-ia-p1-20260627`; HEAD `826e733`; cached `origin/main` `28e87357`; merge-base `63f7b305`; 6 ahead / 66 behind; 20 modified + 360 untracked (Tori independently re-verified 2026-07-21 with zero deleted entries). Proceed authorized.

## 2. Textual vs semantic distinction (governing rule)

Legacy `merge-tree` measures only textual mergeability of a delta against current `origin/main`. A zero-marker result is NOT semantic safety: 586fef1 is textually clean yet net-zero (its only file is deleted by HEAD 826e733); fd15e8e's backend half is textually clean yet orphaned (no UI reaches it after 826e733). Conversely add/add markers on Lab files confirm supersession, not salvage value. Conceptual supersession is treated as a blocker even where a mechanical merge looks possible.

## 3. Six-commit census table

Per-commit legacy `merge-tree <parent> <commit> origin/main`; "markers" = conflict-marker sections touching that commit's own paths. Dirty-overlap = tracked-modified paths touching the commit's files (all KEEP-COMMIT/G3-held per Phase 1).

| Commit | Parent | Paths changed | Also changed on main since 63f7b305 | merge-tree indicators | Class | Dirty overlap | Phase 2 fate |
|---|---|---|---|---|---|---|---|
| ac0608c surveys polish | 63f7b30 | 8 (M package.json, surveys/page, ChartView, ControlBar, PlotA, SurveysView; A test-surveys-atlas-ia.mjs, plotting.ts) | package.json(21), test script(4), page(1), ChartView(1), ControlBar(3), PlotA(1), SurveysView(3), plotting.ts(1) | content: package.json(1), SurveysView(1); add/add: test script(5) | content + add/add | SurveysView +26, ChartView +18, test +45, package.json +2 | REWORK (no cherry-pick) |
| e5ceda8 wiki sources fix | ac0608c | 2 (A test-wiki-sources-page.mjs; M WikiSourcesClient.tsx) | WikiSourcesClient.tsx(4); test script(0, absent on main) | content: WikiSourcesClient.tsx(1) | content (small; 16-line file delta vs 4 upstream commits) | none | REWORK (re-apply) |
| fd15e8e lab runner | e5ceda8 | 8 (M backend main.py, frontend layout; A lab_runner.py router, lab_runner_worker.py, LabConfigurator, RecentRuns, lab/page, middleware.ts) | backend/main.py(0), lab_runner.py(0 absent), worker(0 absent), layout(1), middleware(1), lab/page(3); configurator/RecentRuns absent on main | add/add: lab/page(3), middleware(2); content: layout(1). Backend half: ZERO markers | backend = clean but conceptually orphaned; frontend = superseded | tools/lab_runner_worker.py +85 | SPLIT: backend = deferred product decision; frontend = ABANDON |
| 01e8afa stage tabs | fd15e8e | 4 (M LabConfigurator; A LabTopTabs, labTabStore; M lab/page) | LabTopTabs(1), labTabStore(4), lab/page(3); LabConfigurator absent on main | add/add: LabTopTabs(1), labTabStore(3); content: lab/page(3) | add/add + content; intermediate churn (file later deleted by HEAD) | none | ABANDON |
| 586fef1 lineate topics | 01e8afa | 1 (M LabConfigurator +73) | LabConfigurator absent on main | ZERO markers | textually clean, semantically net-zero (deleted by 826e733) | none | ABANDON |
| 826e733 dissolve frontier map (HEAD) | 586fef1 | 7 (D LabConfigurator, RecentRuns; A LabStages, frontiersData; M LabTopTabs, labTabStore, lab/page) | LabStages(9), frontiersData(2), LabTopTabs(1), labTabStore(4), lab/page(3) | add/add: LabStages(11), frontiersData(29); content: LabTopTabs(2), labTabStore(2), lab/page(3) | add/add + content; conceptually superseded (main's same-name files richer) | none | ABANDON |

Same-name divergence scale (HEAD vs origin/main diff lines): LabStages.tsx 1917, frontiersData.ts 1936, labTabStore.ts 127, LabTopTabs.tsx 88, lab/page.tsx 172. Whole-branch merge-tree totals: 61 conflict markers across 11 sections; the Lab add/add wall accounts for 51 of 61.

## 4. Per-unit census

### 4.1 Surveys Atlas IA (ac0608c + dirty changes across additional tracked components)

- Textual: content conflicts in package.json (upstream 21 commits; branch adds a dependency block) and SurveysView (1 marker among 14 hunks); add/add on the smoke script (5 markers — main rewrote it 4 times, dirty tree extends it +45). ControlBar (upstream drift 3) merges textually clean at commit level but the intent differs.
- plotting.ts add/add resolved as NOT a conflict: blob compare `rev-parse HEAD:` vs `origin/main:` = identical object `ecfcec98…`; main merged the same change as PR #29 (`8921c95 feat(surveys): polish Atlas IA (#29)`). Likewise ChartView, PlotA, surveys/page.tsx are blob-identical HEAD vs main. True surviving deltas: SurveysView, ControlBar, test script, package.json.
- Additional dirty components outside `ac0608c` (all tracked, modified, exist on main): SurveyDetailClient.tsx (drift 0), PlotB (0), BandSpectrumStrip (1), FilterSheet (1), SurveyCard (1), SurveyPeek (1).
- Census conclusion: rework must reconcile committed ac0608c + dirty extensions (SurveysView/ChartView/test/package.json) + 6 additional modified tracked components against main; three of the commit's eight paths are already upstream-verbatim, so the real rework surface is ~5 files. Cherry-pick rejected (stale subset + guaranteed add/add on the test script).

### 4.2 Wiki sources fix (e5ceda8)

- Only real file `WikiSourcesClient.tsx` drifted 4 upstream commits; merge-tree shows exactly 1 content marker (small, near the import/source-list region); the companion smoke script is absent on main (clean add). A raw pick would conflict textually and stale-semantically; re-apply the 16-line idea onto current file and re-run `node scripts/test-wiki-sources-page.mjs`.

### 4.3 Backend autonomous runner (fd15e8e backend half)

- Branch-only clean additions: `backend/app/routers/lab_runner.py`, `tools/lab_runner_worker.py` (both absent on main, 0 upstream drift), plus `backend/app/main.py` router registration (main.py has 0 upstream drift since merge-base — registration would apply cleanly).
- Separation: these three are textually conflict-free. The frontend half (LabConfigurator/RecentRuns/lab-page/middleware/layout) is superseded/abandoned. Dirty worker extension +85 lines (lit grounding via nm_fulltext_layer) is the latest intent and must be carried into any revival. Blocker is conceptual, not textual: 826e733 orphaned the runner (no UI), so revival = product decision per plan Phase 5 #8, with acceptance exposing when fail-open lit-grounding did not run.

### 4.4 Lab frontend IA (fd15e8e frontend half, 01e8afa, 586fef1, 826e733)

- Add/add wall confirmed: LabStages (11 markers), frontiersData (29), labTabStore (3+2), LabTopTabs (1+2), lab/page (3+3), middleware (2). Main independently built the same-named files richer (LabStages 9 upstream commits; 1917/1936 diff-lines) plus a family the branch never had (stageData, subnavVideos, DraftBoard, FlagshipStudies, FrontierDrafts, PipelineBoard, methodLinks, researchCatalog, clusterScatter, dataLandscape, DesktopCompanion, rawStyle).
- Intermediate-deletion chain: fd15e8e creates LabConfigurator/RecentRuns; 01e8afa and 586fef1 edit LabConfigurator; 826e733 deletes both. Commits 4–5 contribute net-zero to the final tree; replaying them resurrects dead UI.
- Conceptual supersession is a hard blocker regardless of mechanical mergeability. No Lab frontend replay.

## 5. Dirty-overlap map (20 modified tracked files)

Overlap with branch commits (5): SurveysView.tsx(+26), ChartView.tsx(+18), test-surveys-atlas-ia.mjs(+45), package.json(+2) → Surveys unit; tools/lab_runner_worker.py(+85) → runner unit. Disjoint dirty units (15), upstream drift in parentheses: trust_calculation.py(0)→P.A; model_canary.py(1)→P.D; pages.py(6)→Phase5#3; WikiPageClient.tsx(14)→Phase5#4 recheck-before-reuse; SurveyDetailClient(0)/BandSpectrumStrip(1)/FilterSheet(1)/PlotB(0)/SurveyCard(1)/SurveyPeek(1)→Surveys unit; IdeasIndexClient(1)/ideas/page(1)/app/page(2)/NavBar(1)→Phase5#6; wiki_schema.md(0)→docs. All KEEP-COMMIT, G3 held; working-tree state is latest intent for Surveys and worker — never frozen by cherry-pick.

## 6. Execution-shape recommendation (restatement only; nothing executed)

Base: fresh cached `origin/main` (`28e87357`); no fetch performed or assumed. Shape: isolated topical worktrees only after G3 approval — `salvage/surveys-atlas-ia` (rework: commit + dirty changes across additional tracked components), `salvage/wiki-sources-fix` (re-apply), `salvage/lab-runner-backend` (only after product decision to revive; backend scope only). No Lab frontend replay; commits 01e8afa/586fef1/826e733 remain in branch history as reference. Stop rules (from Phase 2, restated): any add/add in a Lab file → STOP (confirms abandon); hunk dragging unrelated upstream lines → STOP and re-scope; runner reintroduction touching DB/migration/model metadata → STOP (G5 closed); recount drift from 6/66/20/360 → STOP and re-inventory. Tests the future packet must run: `node scripts/test-surveys-atlas-ia.mjs`; `node scripts/test-wiki-sources-page.mjs`; per-branch `next build`/`tsc` for orphaned imports after abandoning LabConfigurator/RecentRuns; runner import/health + dry-run guard with no repo-local DB; confirm #97–#101 intact on Lab-adjacent surfaces.

## 7. Future G3 approval packet checklist

1. Fresh recount evidence (6/66, 20/360, merge-base 63f7b305) at approval time.
2. Read-only patch snapshots of the 5 overlap files' uncommitted deltas + 6 additional modified tracked surveys components + 15 disjoint dirty units, stored under handoff dirs (no stash/reset).
3. Per-unit exact file scopes (Surveys: surveys/**, components/surveys/**, SurveyDetailClient, test script, package.json; Wiki: WikiSourcesClient.tsx + its test; Runner: lab_runner.py, main.py 2-line registration, lab_runner_worker.py incl. +85).
4. P0 preservation receipt (Contract v1 manifest + backup) confirmed in place.
5. Named base commit `28e87357`, one worktree per unit, live mirror read-only.
6. Stop rules and test commands from §6 pasted verbatim into the approval request.
7. Rollback statement: discard = `git worktree remove`; primary checkout never mutated.
8. Product decision record for the backend runner (revive or not) before its branch is cut.

## 8. Safety ledger (all zero)

Branch creation 0; branch switch/checkout 0; worktree creation 0; index writes 0; ref writes 0; object writes (no hash-object/commit-tree/mktree/merge-tree --write-tree) 0; rebase 0; cherry-pick 0; commit 0; stash 0; reset 0; file moves 0; deletes 0; product/source/test edits 0; DB/SQL/migration 0; runtime/deploy/restart 0; network/fetch 0; publication 0; `.env*` content reads 0. Files written: 1 (this CONFLICT_CENSUS.md). Note: one guarded multi-file /tmp cleanup loop was denied by the operator and NOT retried; /tmp scratch outputs (mt_*.txt) remain harmlessly outside the repo. Tori's independent re-verification (HEAD 826e733, 20 modified, 360 untracked, zero deleted) was accepted as steering input.

G3 remains HELD; G5 (DB) CLOSED; G7 (runtime/publication) CLOSED. This census authorizes no action.

KUN_PHASE3_CONFLICT_CENSUS_COMPLETE_20260721
