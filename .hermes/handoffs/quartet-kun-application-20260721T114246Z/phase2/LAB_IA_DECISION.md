# Lab IA decision — Phase 2 (Lana)

Task ID: `quartet-kun-application-20260721T114246Z-phase2`
Authority: Phase 1 ratified (`HWAO_PHASE1_CLASSIFICATION_RATIFIED_20260721`); Phase 2 released. Read-only decision phase. No git or product mutation authorized. Canonical plan: `.hermes/plans/2026-07-21_205603-kun-report-quartet-application-plan.md`.

## Snapshot verification (hard-stop gate cleared)

The six-commit history and the 6/66 relationship were re-verified read-only before deciding. **No drift** — this decision is made on the exact snapshot the brief describes:

| Check | Brief | Observed | Match |
|---|---|---|---|
| Branch | `feat/surveys-atlas-ia-p1-20260627` | same | ✅ |
| HEAD | `826e733` | `826e73381cb7870954bbd7f041a618408385a80a` | ✅ |
| Ahead / behind `origin/main` (cached) | 6 / 66 | 6 / 66 | ✅ |
| Merge-base | — | `63f7b305` (parent of `ac0608c`) | ✅ |
| Six commits (old→new) | `ac0608c,e5ceda8,fd15e8e,01e8afa,586fef1,826e733` | identical, in order | ✅ |
| Branch diff vs merge-base | 20 files / +2,190 / −111 | 20 files / +2,190 / −111 | ✅ |
| Dirty worktree | 20 modified / 360 untracked | 20 / 360 | ✅ |
| Phase 1 buckets | 222/130/18/10 | 222/130/18/10 (`GORU_PHASE1_WORKTREE_CLASSIFICATION_COMPLETE_20260721`) | ✅ |

`origin/main` HEAD used for comparison: `28e87357` (locally cached; **no fetch performed**).

---

## 1. Decision

**`REWORK PIECEMEAL`** — rebuild the small set of still-valuable ideas as independent, topical units on a fresh `origin/main` base. Do **not** rebase the branch as a whole, do **not** cherry-pick the commits verbatim, and do **not** abandon the work wholesale.

*(Decision only. No action is taken here. Every git write remains behind gate G3, which is Held.)*

---

## 2. Plain-English rationale

The branch is six commits ahead but **66 commits behind**, and — critically — upstream already went where most of this branch was trying to go, only further:

- **The Lab work (four of the six commits, ~1,900 of the 2,190 added lines) is superseded.** `origin/main` independently grew a **richer** Lab that already contains the branch's *own* final filenames — `LabStages.tsx`, `frontiersData.ts`, `LabTopTabs.tsx`, `labTabStore.ts`, `page.tsx` — plus a whole family the branch never had (`DraftBoard`, `FlagshipStudies`, `FrontierDrafts`, `PipelineBoard`, `stageData`, `subnavVideos`, `researchCatalog`, `methodLinks`, `clusterScatter`, `dataLandscape`, `DesktopCompanion`, `rawStyle`). Those same-named files diverge massively from the branch's versions (`LabStages.tsx` 1,917 diff-lines across 9 upstream commits; `frontiersData.ts` 1,936 diff-lines). Rebasing or cherry-picking the branch's Lab commits onto main is an **add/add conflict wall against superior upstream code** — you would be hand-merging line-by-line to *re-derive* something main already ships better.

- **The branch's Lab commits also fight themselves.** `826e733` (HEAD) deletes `LabConfigurator.tsx` and `RecentRuns.tsx` — the exact files `fd15e8e` created and `01e8afa`/`586fef1` then edited. So commits 4–5 are pure intermediate churn whose code contribution to the final tree is essentially zero. Replaying them (rebase/cherry-pick) resurrects and re-deletes dead UI for no benefit.

- **What is *not* superseded is small and specific**, and it is exactly the work worth reworking on a clean base:
  1. **Surveys Atlas IA** (`ac0608c`) — but its intent now lives across three layers: the commit, *uncommitted extensions* to four of its files, and *six additional modified tracked* surveys components outside that commit. No cherry-pick captures all three.
  2. **Wiki claim-source fix** (`e5ceda8`) — a tiny, self-contained idea, but its one real file drifted 4 upstream commits, so it needs a re-apply against today's file, not a blind pick.
  3. **Backend autonomous research runner** (`fd15e8e`'s backend half + `tools/lab_runner_worker.py`) — the *only* piece genuinely absent from main (`backend/app/main.py` has **0** upstream drift; no runner router/worker on main). It is conflict-free to reintroduce, but `826e733` orphaned it (no UI reaches it), so reviving it is a fresh product decision, not a salvage reflex.

Rework-piecemeal preserves each of those on its own merits, discards the stale Lab-frontend churn that main already beat, and reconciles every unit against current main rather than pretending 66 upstream commits didn't happen. It is also what the canonical plan already mandates: *"A single all-or-nothing branch rebase is not the default"* and *"reimplement against main… salvage product work topically… never one 'save the dirty tree' commit"* (plan §3 #1, §9 P3.2, N4).

---

## 3. Six-commit disposition table

Fates below are the *proposed* per-unit outcome **under REWORK PIECEMEAL**. None is executed here.

| # | Commit | Conceptual unit | Depends on | Conflict / staleness risk | Proposed fate |
|---|---|---|---|---|---|
| 1 | `ac0608c` feat(surveys): polish Atlas IA | **Surveys Atlas IA** | none (branch root) | **Medium.** Touches `PlotA`(drift 1), `ChartView`(1), `SurveysView`(3), `ControlBar`(3), `surveys/page`(1), and *creates* `plotting.ts` which **main created independently** (drift 1 → add/add). Also **superseded by uncommitted dirty edits** on 4 of its 8 files (see §4). | **REWORK** as a Surveys unit reconciling committed **+** dirty **+** main. Do **not** cherry-pick (stale subset, guaranteed conflicts). |
| 2 | `e5ceda8` fix: show claim sources on wiki sources page | **Wiki claim-source fix** | none | **Low–Medium.** Only 2 files, but `WikiSourcesClient.tsx` drifted **4** upstream commits. Self-contained idea. | **REWORK (re-apply)** the fix onto current `WikiSourcesClient.tsx`; re-run the smoke test. Closest to a clean reapply, but still verify against drift. |
| 3 | `fd15e8e` feat(lab): autonomous research runner (AASTeX + review-revise) | **Autonomous Lab runner** — *split unit*: (a) backend API + worker; (b) first frontend configurator | none | **Split.** (a) Backend `main.py`(drift **0**), `lab_runner.py` & `lab_runner_worker.py` **branch-only, absent on main** → **conflict-free but ORPHANED** by #6. (b) Frontend `LabConfigurator`/`RecentRuns`/`page`/`layout`/`middleware` → **superseded** by main's richer Lab. | **REWORK, split:** (a) backend runner+worker = **separate product decision** — revive as its own backend unit *only if* an autonomous runner is still wanted (plan Phase 5 #8). (b) frontend configurator = **ABANDON** (superseded; already deleted by #6). |
| 4 | `01e8afa` feat(lab): stage tabs in sticky banner | **Lab Topic/config IA evolution (1/3)** | #3 | **High / moot.** Edits `LabConfigurator` (deleted by #6). Creates `LabTopTabs`/`labTabStore`, which **exist on main**, heavily divergent (88 / 127 diff-lines; drift 1 / 4). | **ABANDON.** Intermediate churn; endpoint superseded on main. |
| 5 | `586fef1` feat(lab): lineate each topic's derivation | **Lab Topic/config IA evolution (2/3)** | #3, #4 | **High / moot.** Only edits `LabConfigurator.tsx` (+73), which #6 **deletes** → **net-zero** in the tree. The topic-derivation *idea* already lives on main (`frontiersData`/`LabStages`). | **ABANDON** the code; the derivation idea is already realized upstream. |
| 6 | `826e733` refactor(lab): explanatory pipeline — dissolve frontier map into Topic tab **(HEAD)** | **Lab Topic/config IA evolution (3/3) — the endpoint** | #3, #4, #5 | **Superseded.** Creates `LabStages.tsx`/`frontiersData.ts` — **same names exist on main** but diverge **1,917 / 1,936** diff-lines; main has **9** commits on `LabStages` since the merge-base. | **ABANDON.** Main independently built a richer version of this exact concept; keep only as historical reference. |

**Net:** 1 unit reworked (Surveys), 1 reworked/re-applied (Wiki fix), 1 split (backend runner = deferred product decision / frontend configurator = abandon), 3 Lab-IA commits abandoned as superseded churn.

---

## 4. Dirty-worktree interaction

All **20** modified tracked paths are Phase 1 **`KEEP-COMMIT`** (`evidence_basis: filename-only`, `future_gate: G3 held`). Nothing here is moved, staged, stashed, or reset — this is a read-only overlap map.

**A. Five paths overlap the branch commits, and the uncommitted edits *extend / supersede* the committed version** (working-tree-vs-HEAD deltas shown):

| Modified path | Origin commit | Uncommitted Δ vs HEAD | Effect |
|---|---|---|---|
| `frontend/src/components/surveys/SurveysView.tsx` | `ac0608c` | +26 / small | Dirty tree **supersedes** the committed surveys view. |
| `frontend/src/components/surveys/ChartView.tsx` | `ac0608c` | +18 | Dirty tree **supersedes**. |
| `frontend/scripts/test-surveys-atlas-ia.mjs` | `ac0608c` | +45 | Dirty tree **extends** the smoke test. |
| `frontend/package.json` | `ac0608c` | +2 | Dirty tree extends. |
| `tools/lab_runner_worker.py` | `fd15e8e` | +85 | Dirty tree **substantially extends** the runner worker. |

Consequence: for the Surveys unit and the backend worker, **the working-tree state is the latest intent** — cherry-picking the committed `ac0608c`/`fd15e8e` would freeze a *stale subset* and drop these extensions. This is a primary reason the disposition is REWORK, not CHERRY-PICK.

**B. Fifteen paths are disjoint from the branch commits** — independent dirty units that belong to the plan's Phase 5 salvage tracks, **not** to the branch-fate decision. Listed with upstream drift (uncommitted edits sit on the stale HEAD, 66 behind, so each must be diffed against *current* main before reuse — several may already be superseded):

| Modified path | Upstream drift | Maps to plan unit |
|---|---|---|
| `backend/app/services/trust_calculation.py` | 0 | P.A trust semantics (test `test_trust_debate_stance_caps.py` untracked) |
| `backend/app/services/model_canary.py` | 1 | P.D model-canary reliability (test `test_model_canary.py` untracked) |
| `backend/app/routers/pages.py` | 6 | Phase 5 #3 pages/source APIs |
| `frontend/src/app/wiki/[slug]/WikiPageClient.tsx` | **14** | Phase 5 #4 wiki presentation (heavy drift — recheck before reuse) |
| `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx` | 0 | Surveys unit (new-ish, not in branch commits) |
| `frontend/src/components/surveys/BandSpectrumStrip.tsx` | 1 | Surveys unit (uncommitted build-out) |
| `frontend/src/components/surveys/FilterSheet.tsx` | 1 | Surveys unit |
| `frontend/src/components/surveys/PlotB.tsx` | 0 | Surveys unit |
| `frontend/src/components/surveys/SurveyCard.tsx` | 1 | Surveys unit |
| `frontend/src/components/surveys/SurveyPeek.tsx` | 1 | Surveys unit |
| `frontend/src/app/ideas/IdeasIndexClient.tsx` | 1 | Phase 5 #6 ideas/home/nav |
| `frontend/src/app/ideas/page.tsx` | 1 | ideas/home/nav |
| `frontend/src/app/page.tsx` | 2 | ideas/home/nav |
| `frontend/src/app/components/NavBar.tsx` | 1 | ideas/home/nav |
| `wiki_schema.md` | 0 | docs |

**Note on scope for the Surveys rework:** the Surveys IA unit must reconcile *committed* `ac0608c` **+** the dirty extensions to `ChartView`/`SurveysView`/test/package.json (group A) **+** the six additional modified tracked surveys components in group B (`SurveyDetailClient`, `BandSpectrumStrip`, `FilterSheet`, `PlotB`, `SurveyCard`, `SurveyPeek`) — all against main's modest surveys drift. That committed+uncommitted spread across additional paths is impossible to capture with any cherry-pick and confirms rework.

---

## 5. Clean-base target (recommendation only — G3 Held)

**Recommend: yes — cut fresh from `origin/main` (`28e87357`), one topical branch per unit, in isolated `git worktree`s so the stale dirty checkout is never disturbed.** This is a recommendation; no branch/worktree is created here.

Suggested topical branches (each from `origin/main`, each its own PR):

- `salvage/surveys-atlas-ia` — the reconciled Surveys unit (committed `ac0608c` + dirty extensions + 6 additional modified components).
- `salvage/wiki-sources-fix` — re-applied `e5ceda8` onto current `WikiSourcesClient.tsx`.
- `salvage/lab-runner-backend` — backend runner + worker **only if** the product decision to revive an autonomous runner is made; otherwise this branch is not cut.
- (Out of Phase 2 scope, listed for completeness only:) the 15 disjoint dirty units flow into their own plan Phase 5 branches (trust, model-canary, pages APIs, wiki presentation, ideas/nav).

**Why worktrees, not in-place work:** the primary checkout holds 20 uncommitted KEEP-COMMIT edits + 360 untracked entries (incl. the immutable Contract v1 packet). A fresh `origin/main` worktree keeps every salvage build physically separate from that unpreserved state, so no rework can accidentally reset or stash it. **Why not rebase-in-place:** covered in §2 — the Lab endpoint is superseded, so an in-place rebase converges on conflicts, not on main.

---

## 6. Future execution packet (G5 — **HELD**, nothing executed)

> The brief's "G5 execution packet" = the *future gated action sequence* proposed for later approval. It maps to the plan's **G3** git gate (branch/commit/cherry-pick/rebase/PR/merge), which is **Held**. Listed here for design review only. **No step below runs in Phase 2.**

**Preservation prerequisites (must all be true before any G3 step):**
- P0 preservation receipt exists: Contract v1 validated + SHA-256 manifest + out-of-repo backup (plan Phase 0). ✅ prerequisite, not done here.
- Phase 1 classification ratified (already `HWAO_PHASE1_CLASSIFICATION_RATIFIED_20260721`). ✅
- **Capture the dirty work before any checkout that could touch it:** produce read-only patch snapshots of the 5 overlap files' uncommitted deltas **and** the 6 additional modified tracked surveys components **and** the 15 disjoint dirty units, stored under `phase2/`/`phase3/` handoff dirs. (Snapshot only — no `stash`, no `reset`.)
- Live mirror on `main` stays read-only throughout.

**Bounded action sequence (per unit, each independently gated):**

1. **Surveys Atlas IA** → `git worktree add` from `origin/main`; port the reconciled surveys intent (commit + dirty changes across additional tracked components); file scope = `frontend/src/app/surveys/**`, `frontend/src/components/surveys/**`, `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`, `frontend/scripts/test-surveys-atlas-ia.mjs`, `frontend/package.json`. **No** Lab/backend/ideas hunks.
2. **Wiki sources fix** → separate worktree; re-apply onto current `WikiSourcesClient.tsx`; file scope = that file + `frontend/scripts/test-wiki-sources-page.mjs`.
3. **Backend autonomous runner** → **only after** a product decision to revive it; separate worktree; file scope = `backend/app/routers/lab_runner.py`, `backend/app/main.py` (2-line router registration), `tools/lab_runner_worker.py` (with the +85 dirty extension). Frontend configurator **not** included (abandoned).
4. Lab-IA frontend commits (`01e8afa`,`586fef1`,`826e733` frontend, `fd15e8e` frontend half) → **no action**; recorded as abandoned/superseded; left in branch history for reference.

**Conflict stop rules:**
- **Any add/add conflict in a Lab file** (`LabStages.tsx`, `frontiersData.ts`, `LabTopTabs.tsx`, `labTabStore.ts`, `lab/page.tsx`) → **STOP**; it confirms the abandon call — do not hand-merge to re-derive superseded upstream code.
- A surveys or wiki hunk that **drags unrelated upstream lines** → STOP and re-scope (plan stop-rule: "a topical change drags unrelated hunks").
- Backend runner reintroduction that would touch **any DB/migration/model metadata** → STOP (that is G5 DB gate, Closed).
- Any recount that differs from 6/66 / 20 / 360 without explanation → STOP and re-inventory.

**Tests / acceptance a later packet must run (disposable paths, no prod services):**
- Surveys: `cd frontend && node scripts/test-surveys-atlas-ia.mjs` → `surveys atlas IA smoke checks passed`.
- Wiki: `cd frontend && node scripts/test-wiki-sources-page.mjs` (the smoke test shipped in `e5ceda8`).
- Frontend build/type check on each salvage branch (`next build` / `tsc`) to prove no orphaned imports after abandoning `LabConfigurator`/`RecentRuns`.
- Backend runner (if revived): import/health of `backend/app/routers/lab_runner.py`; `lab_runner_worker.py` dry-run guard; confirm `GET /api/lab/runs` shape; **no** repo-local DB created (ties to plan Phase 4 hygiene). Do **not** run mutating research jobs or create repo-local DBs.
- Regression guard: confirm shipped live fixes **#97–#101** remain intact wherever a salvage branch touches Lab-adjacent surfaces.

**Rollback:** every salvage build lives in a disposable `git worktree`; discard = `git worktree remove` — the primary checkout and its 380 uncommitted entries are never mutated. No `reset`/`stash` of the primary tree. `git reflog` covers any branch-local mistake. No live-mirror write at any point.

**Gate status: G3 Held, G5 (DB) Closed, G7 (runtime/publication) Closed.** This packet is a proposal; approval is a separate explicit user line.

---

## 7. Rejected alternatives

- **`KEEP/REBASE` the branch as a whole — rejected.** Rebasing 6 commits across 66 upstream commits converges on an **add/add conflict wall**: main already owns `LabStages.tsx`/`frontiersData.ts`/`LabTopTabs.tsx`/`labTabStore.ts`/`page.tsx` in divergent, richer form (1,917 / 1,936 diff-lines; 9 upstream commits on `LabStages`). It would also resurrect the `LabConfigurator`/`RecentRuns` churn that HEAD deletes, and inherit surveys drift + main's independent `plotting.ts`. The plan bars this explicitly: *"A single all-or-nothing branch rebase is not the default"* and *"'rebase and see' is prohibited before this decision."*
- **`CHERRY-PICK` selected commits — rejected.** (a) `ac0608c` freezes a **stale subset** — it predates the uncommitted surveys extensions across 6 additional tracked components (§4), and collides with main's surveys drift + independently-created `plotting.ts`. (b) The Lab commits replay deleted intermediate code and hit main's divergent same-named files. (c) Even the tiny `e5ceda8` drifted 4 upstream commits. Cherry-pick preserves commit boundaries that **no longer match the desired end state**. (The wiki fix's near-verbatim reapply is handled as a rework sub-case, not a raw pick.)
- **`ABANDON` the whole branch — rejected.** It discards genuinely useful, **not-yet-on-main** intent: the Surveys Atlas IA polish **plus** substantial uncommitted surveys build-out across six additional tracked components, the wiki claim-source fix, and the **branch-only backend autonomous runner** (`main.py` 0 drift; absent from main). Wholesale abandon forfeits real value. (The Lab *frontend* commits are individually abandoned-in-place because main supersedes them — but that is a per-unit fate inside REWORK, not a whole-branch abandon.)

---

## 8. Safety ledger

Phase 2 was read-only. Only one file was written: this decision markdown.

| Action | Count |
|---|---|
| Branch creation | 0 |
| Branch switch / checkout | 0 |
| Worktree creation | 0 |
| Rebase | 0 |
| Cherry-pick | 0 |
| Commit | 0 |
| Stash | 0 |
| Reset | 0 |
| Move (file) | 0 |
| Delete | 0 |
| Product / source / test edit | 0 |
| DB / SQL / migration action | 0 |
| Runtime / deploy / restart action | 0 |
| Network / fetch | 0 |
| Publication | 0 |
| `.env*` content access | 0 |
| Files written | 1 (this `LAB_IA_DECISION.md`) |

Methods used: `git rev-parse`, `rev-list --count`, `merge-base`, `log`, `show --stat`, `diff --stat`/`diff … | wc -l`, `ls-tree`, `status --short`, and read-only file reads (`.hermes.md`, canonical plan, Phase 1 classification). No fetch. `origin/main` used from local cache only (`28e87357`). No `.env*` file opened.

---

`LANA_PHASE2_LAB_IA_DECISION_COMPLETE_20260721`
