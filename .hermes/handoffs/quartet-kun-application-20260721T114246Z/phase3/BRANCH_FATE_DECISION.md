# Branch fate decision — Phase 3.2 (Hwao authority record)

Task ID: `quartet-kun-application-20260721T114246Z-phase3.2`
Authority: canonical plan §9 Phase 3 — "Hwao decides; Goru runs mechanics; Kun verifies; Tori verifies receipts." Phase 3.1 census and Phase 3.2 dirty-intent snapshots are complete; this is Hwao's ratified branch-fate record.
Canonical plan: `.hermes/plans/2026-07-21_205603-kun-report-quartet-application-plan.md` (embedded verbatim in `QUARTET_KUN_REPORT_APPLICATION_PLAN.html`, marker `QUARTET_KUN_REPORT_APPLICATION_PLAN_COMPLETE_20260721T114246Z`).
Completed: 2026-07-22 00:00 KST (2026-07-21 15:00 UTC).
Nature: **decision record only.** Nothing is executed by this document. Every git write remains behind gate G3, which stays Held.

---

## 1. Snapshot (re-verified read-only at decision time — zero drift)

| Check | Expected (brief / census) | Observed at decision time | Match |
|---|---|---|---|
| Branch | `feat/surveys-atlas-ia-p1-20260627` | same | ✅ |
| HEAD | `826e733` | `826e73381cb7870954bbd7f041a618408385a80a` | ✅ |
| `origin/main` (locally cached, **no fetch**) | `28e87357` | `28e873570f1c479fffd18a5106e5afa91d46e3e9` | ✅ |
| Merge-base | `63f7b305` | `63f7b305c0560f06402ac71858630864e5e6d494` | ✅ |
| Ahead / behind | 6 / 66 | 6 / 66 | ✅ |
| Modified / untracked / deleted | 20 / 360 / 0 (380 entries) | 20 / 360 / 0 (380) | ✅ |
| Six commits (old→new) | `ac0608c, e5ceda8, fd15e8e, 01e8afa, 586fef1, 826e733` | identical (per Phase 3.1 census; HEAD re-confirmed) | ✅ |

Methods: `git branch --show-current`, `rev-parse`, `merge-base`, `rev-list --count`, `status --porcelain`. Read-only throughout; no fetch; no `.env*` content touched.

## 2. Prerequisite chain (all receipts verified in place)

1. **P0 preservation** — `phase0/PHASE0_PRESERVATION_RECEIPT.md`: Contract v1 validated `PASS` (16/45/45, 26/26, 16/16, 0 errors, safety counters all 0); 36-row SHA-256 manifest (`phase0/CONTRACT_V1_SHA256_MANIFEST.txt`, manifest SHA-256 `b7f0de4df74929d7c0aeaad20ec796b7795ac1c5132dfe8ddb3c54c13f443abd`); out-of-repo backup at `/Users/duhokim/HermesOps/backups/claim-ledger-contract-v1-20260721T114246Z/` verified 36/36 paths, digests, and mtimes; Tori and Kun independently computed identical manifests. Marker: `PHASE0_CONTRACT_V1_PRESERVATION_COMPLETE_20260721T114246Z`.
2. **P1 classification** — 380 entries bucketed 222/130/18/10, no moves. Markers: `GORU_PHASE1_WORKTREE_CLASSIFICATION_COMPLETE_20260721`, ratified `HWAO_PHASE1_CLASSIFICATION_RATIFIED_20260721`.
3. **P2 Lab IA decision** — `REWORK PIECEMEAL` on a fresh `origin/main` base; no whole-branch rebase, no verbatim cherry-pick, no wholesale abandon. Markers: `LANA_PHASE2_LAB_IA_DECISION_COMPLETE_20260721`, ratified `HWAO_PHASE2_LAB_IA_DECISION_RATIFIED_20260721`.
4. **P3.1 conflict census** — read-only legacy `merge-tree` census of all six commits; textual-vs-semantic governing rule established. Marker: `KUN_PHASE3_CONFLICT_CENSUS_COMPLETE_20260721`.
5. **P3.2 dirty-intent snapshots** — 4 read-only patch snapshots covering all 20 modified tracked paths, manifest `phase3/PATCH_SNAPSHOT_MANIFEST.json`. Marker: `TORI_PHASE3_DIRTY_INTENT_SNAPSHOTS_COMPLETE_20260721`.

The critical path required by the plan — preservation → Lab IA decision → branch fate — is satisfied in order. This record is the final link.

## 3. Gate-ledger correction: G2 is COMPLETED, not Held

The canonical plan's approval ledger (§13) and its HTML gate panel record **G2 · HELD**. That was true at planning time and is now **stale**. The correction, binding for every later packet that restates the ledger:

> **G2 (Contract hash manifest and out-of-repo backup writes) is COMPLETED — approved, executed, and receipted on 2026-07-21 22:40 KST.** Evidence: the Phase 0 receipt records `Gate: G2 APPROVED`, the 36-row SHA-256 manifest, and the verified 36/36 backup (paths, byte digests, mtimes all matching; source unchanged after copy). It is not an open approval awaiting grant; it is discharged.

Corrected ledger as of this record (G1 and G2 discharged):

| Gate | Scope | State |
|---|---|---|
| G1 | Baseline board docs-only reconciliation | **COMPLETED 2026-07-21 in Phase 0 (Hwao-verified `HWAO_G1_BOARD_RECONCILIATION_VERIFIED_20260721`)** |
| **G2** | Contract manifest + out-of-repo backup | **COMPLETED 2026-07-21 (receipt `PHASE0_CONTRACT_V1_PRESERVATION_COMPLETE_20260721T114246Z`)** |
| G3 | Any branch, commit, rebase, cherry-pick, PR, push, merge | Held |
| G4a / G4b / G4c | Archive moves / deletion / secret-adjacent handling | Held, each separately |
| G5 | DB / SQL / migration / production data | Closed |
| G6 | Status/debate-map docs run | Held |
| G7 | Runtime / deploy / restart / publication / cockpit | Closed |

## 4. Ratified fate — all six ahead commits

Adopting Lana's Phase 2 disposition table as confirmed by Kun's Phase 3.1 census, Hwao rules each unit independently. Exact fates:

| # | Commit | Unit | **Fate (ratified)** | Basis |
|---|---|---|---|---|
| 1 | `ac0608c` feat(surveys): polish Atlas IA | Surveys Atlas IA | **REWORK** — fold into the Surveys unit; cherry-pick prohibited | Census 4.1: three of its eight paths are already upstream-verbatim (PR #29 `8921c95`; `plotting.ts`/`ChartView`/`PlotA`/`surveys/page` blob-identical); real surviving surface ≈ 5 files; dirty tree supersedes 4 of its files; add/add on the smoke script. A pick freezes a stale subset. |
| 2 | `e5ceda8` fix: show claim sources on wiki sources page | Wiki claim-source fix | **RE-APPLY** — port the 16-line idea onto current `WikiSourcesClient.tsx`; raw pick prohibited | Census 4.2: the one real file drifted 4 upstream commits (1 content marker); companion smoke test is a clean add. Re-apply then rerun `node scripts/test-wiki-sources-page.mjs`. |
| 3 | `fd15e8e` feat(lab): autonomous research runner | Split unit | **SPLIT — backend half HOLD; frontend half ABANDON** | Census 4.3: backend `lab_runner.py` + `tools/lab_runner_worker.py` are branch-only with 0 upstream drift and `backend/app/main.py` has 0 drift (registration applies cleanly) — textually conflict-free but conceptually **orphaned** by `826e733` (no UI reaches it). Frontend half (`LabConfigurator`, `RecentRuns`, `lab/page`, `middleware`, `layout`) is superseded. |
| 4 | `01e8afa` feat(lab): stage tabs in sticky banner | Lab IA churn 1/3 | **ABANDON** | Intermediate churn: edits a file HEAD deletes; its adds (`LabTopTabs`, `labTabStore`) exist on main in divergent, richer form. |
| 5 | `586fef1` feat(lab): lineate topic derivation | Lab IA churn 2/3 | **ABANDON** | Textually clean but semantically net-zero: its only file (`LabConfigurator.tsx` +73) is deleted by `826e733`; the derivation idea already lives on main. |
| 6 | `826e733` refactor(lab): dissolve frontier map into Topic tab (HEAD) | Lab IA endpoint | **ABANDON** | Superseded: main independently built the same-named files richer (`LabStages.tsx` 1,917 / `frontiersData.ts` 1,936 diff-lines; 9 upstream commits on `LabStages`) plus a family the branch never had. Add/add wall = 51 of the branch's 61 conflict markers. |

**Branch container:** `feat/surveys-atlas-ia-p1-20260627` is never rebased, merged, or cherry-picked wholesale. It stays frozen as read-only historical reference. Its eventual retirement/deletion is a separate future G3 decision after the salvage units land — not decided here.

## 5. Unit fates (ratified)

- **Surveys Atlas IA → REWORK.** One topical unit reconciling committed `ac0608c` + the dirty extensions (`SurveysView` +26, `ChartView` +18, smoke test +45, `package.json` +2) + the six additional modified tracked survey components — all against main's surveys drift. No cherry-pick can capture that three-layer spread.
- **Wiki claim-source fix → RE-APPLY.** Reimplement `e5ceda8`'s intent onto today's `WikiSourcesClient.tsx`; verify with its smoke test. (Distinct from the dirty `WikiPageClient.tsx`, which is Phase 5 #4 wiki presentation, drift 14 — outside branch fate.)
- **Backend autonomous runner → HOLD pending an explicit revive-or-not product decision.** The backend half (`backend/app/routers/lab_runner.py`, `backend/app/main.py` 2-line registration, `tools/lab_runner_worker.py` including the +85 lit-grounding extension) is conflict-free but orphaned. It is **not** salvaged by reflex and **not** abandoned: no `salvage/lab-runner-backend` branch may be cut until a recorded product decision (plan Phase 5 #8) says revive; if the decision is "do not revive," the unit closes as retained-in-history with no branch. Acceptance on revival must expose when fail-open literature grounding did not run.
- **Lab frontend → ABANDON as superseded.** `fd15e8e`'s frontend half plus `01e8afa`, `586fef1`, `826e733`. Main's Lab is richer and shipped (#97–#101); conceptual supersession is a hard blocker regardless of mechanical mergeability. No replay, no hand-merge to re-derive superseded upstream code; commits remain in branch history as reference only.

Net: 1 unit reworked, 1 re-applied, 1 held for a product decision, 3.5 commits' worth of Lab frontend abandoned as superseded.

## 6. Dirty-intent snapshot evidence (Phase 3.2 manifest, re-verified at decision time)

`phase3/PATCH_SNAPSHOT_MANIFEST.json` (`TORI_PHASE3_DIRTY_INTENT_SNAPSHOTS_COMPLETE_20260721`): **4 read-only patches, 20 exact tracked-modified paths, partition 5 overlap + 15 disjoint, total unique 20.** Baseline HEAD `826e73381cb7870954bbd7f041a618408385a80a`.

| Patch | Paths | SHA-256 (manifest = on-disk) | Reverse-apply check |
|---|---|---|---|
| `SURVEYS_DIRTY_INTENT.patch` | 10 | `f083c5d388567a24ca4c69c77140a563e2bcbe39e2c9c4a7f12435c7972a927b` ✅ | ✅ OK |
| `LAB_RUNNER_WORKER_DIRTY_INTENT.patch` | 1 | `6669c584c0ee1e34cb5a943fcbf5c056c1a9d780eef4eb6b674b4e8a8f8a1bb4` ✅ | ✅ OK |
| `BACKEND_WIKI_DIRTY_INTENT.patch` | 5 | `4e1da5b582f4c70cbb4fa709fbf7c033931de1102ee2e3da6ab1211a6d814128` ✅ | ✅ OK |
| `IDEAS_NAV_DIRTY_INTENT.patch` | 4 | `a696975d0760a649a6ba8e8629225391b3b180bfff19baa690f3b9da5ebd39ce` ✅ | ✅ OK |

The 20 exact paths:

1. `frontend/package.json`
2. `frontend/scripts/test-surveys-atlas-ia.mjs`
3. `frontend/src/components/surveys/ChartView.tsx`
4. `frontend/src/components/surveys/SurveysView.tsx`
5. `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`
6. `frontend/src/components/surveys/BandSpectrumStrip.tsx`
7. `frontend/src/components/surveys/FilterSheet.tsx`
8. `frontend/src/components/surveys/PlotB.tsx`
9. `frontend/src/components/surveys/SurveyCard.tsx`
10. `frontend/src/components/surveys/SurveyPeek.tsx`
11. `tools/lab_runner_worker.py`
12. `backend/app/routers/pages.py`
13. `backend/app/services/model_canary.py`
14. `backend/app/services/trust_calculation.py`
15. `frontend/src/app/wiki/[slug]/WikiPageClient.tsx`
16. `wiki_schema.md`
17. `frontend/src/app/components/NavBar.tsx`
18. `frontend/src/app/ideas/IdeasIndexClient.tsx`
19. `frontend/src/app/ideas/page.tsx`
20. `frontend/src/app/page.tsx`

Verification performed for this record (read-only): **SHA-256 recomputed for all four patch files — 4/4 match the manifest; `git apply --reverse --check` passes 4/4** (the working tree still exactly equals the snapshots — the latest intent is captured, nothing has drifted since Tori's snapshot); **patch path union diffed against `git diff --name-only` — exact 20/20 set match, no extras, no gaps.**

**Subset clarification (binding):** the six additional survey components (`SurveyDetailClient.tsx`, `BandSpectrumStrip.tsx`, `FilterSheet.tsx`, `PlotB.tsx`, `SurveyCard.tsx`, `SurveyPeek.tsx`) are **tracked, modified files inside the 15 disjoint paths — a subset, not new untracked files** (`additional_modified_survey_components_inside_disjoint_set: 6`). They belong to the Surveys rework scope; the remaining 9 disjoint paths (trust, model-canary, pages API, wiki presentation, ideas/nav, `wiki_schema.md`) belong to plan Phase 5 / parallel-track units and are **outside branch fate**.

Consequence reaffirmed: for Surveys and the runner worker, the working-tree state is the latest intent; cherry-picking `ac0608c`/`fd15e8e` would freeze a stale subset and drop these captured extensions. The snapshots make the rework losslessly reconstructible even if the dirty checkout is later disturbed.

## 7. Future G3 requirements — per-topical packet only

Each future git action requires its **own** approval packet covering **exactly one** topical unit. Every packet must contain, verbatim where indicated:

1. **Fresh recount at approval time:** branch, HEAD `826e733`, cached `origin/main` `28e87357`, merge-base `63f7b305`, 6 ahead / 66 behind, 20 modified + 360 untracked + 0 deleted. Any unexplained drift → STOP and re-inventory before requesting approval.
2. **Snapshot integrity re-check:** the four Phase 3.2 patches present with matching SHA-256 and passing `git apply --reverse --check`. If reverse-apply fails, the dirty tree has moved — re-snapshot under a new receipt before any checkout-adjacent action.
3. **Exact file scope for the unit, closed-world (no unrelated hunks):**
   - *Surveys:* `frontend/src/app/surveys/**` (incl. `[slug]/SurveyDetailClient.tsx`), `frontend/src/components/surveys/**`, `frontend/scripts/test-surveys-atlas-ia.mjs`, `frontend/package.json`. No Lab, backend, or ideas/nav hunks.
   - *Wiki:* `frontend/src/app/wiki/[slug]/WikiSourcesClient.tsx` + `frontend/scripts/test-wiki-sources-page.mjs` only.
   - *Runner (only if revived):* `backend/app/routers/lab_runner.py`, `backend/app/main.py` (2-line registration), `tools/lab_runner_worker.py` (incl. the +85 extension). Frontend configurator excluded (abandoned).
4. **P0 preservation receipt cited and confirmed in place** (manifest + out-of-repo backup), per §2 item 1.
5. **Named base commit `28e87357`** (cached `origin/main`); **one disposable `git worktree` per unit**; the primary dirty checkout and the clean live mirror are never written. Advancing the base via fetch is a separate explicit approval (network stays gated).
6. **Stop rules pasted verbatim:** any add/add conflict in a Lab file (`LabStages.tsx`, `frontiersData.ts`, `LabTopTabs.tsx`, `labTabStore.ts`, `lab/page.tsx`) → STOP (confirms abandon; never hand-merge to re-derive superseded upstream code); a hunk dragging unrelated upstream lines → STOP and re-scope; runner reintroduction touching any DB/migration/model metadata → STOP (G5 Closed); recount drift from 6/66/20/360 → STOP and re-inventory.
7. **Test commands pasted verbatim:** `cd frontend && node scripts/test-surveys-atlas-ia.mjs` → `surveys atlas IA smoke checks passed`; `cd frontend && node scripts/test-wiki-sources-page.mjs`; per-branch `next build`/`tsc` proving no orphaned imports after abandoning `LabConfigurator`/`RecentRuns`; runner (if revived): import/health of the router, worker dry-run guard, `GET /api/lab/runs` shape, zero repo-local DB files; confirm shipped fixes #97–#101 intact wherever a salvage branch nears Lab-adjacent surfaces.
8. **Rollback statement:** discard = `git worktree remove`; no `stash`/`reset` of the primary checkout at any point; `git reflog` covers branch-local mistakes; no live-mirror write.
9. **Runner precondition:** the explicit revive-or-not product decision record must exist **before** `salvage/lab-runner-backend` is cut. No decision record → no branch.
10. **One explicit user approval line per packet.** No packet inherits approval from this record, from another packet, or from any prior phase.

## 8. No blanket G3; no action now

This record grants **no gate and executes nothing**. There is no blanket G3 for the branch, for the REWORK PIECEMEAL disposition as a whole, or for any subset of units. Deciding a fate is not performing it: no branch, worktree, rebase, cherry-pick, add, commit, PR, push, merge, move, delete, stash, or reset occurs now, and none is authorized by this document. G3 remains **Held** for every unit until its own packet (per §7) receives its own explicit user approval line.

## 9. Gates that remain separate and untouched

- **G4a / G4b / G4c** (archive moves; deletion after quarantine/dwell; secret-adjacent `.env.redacted-*` handling) — Held, each separately; nothing here disposes of any file; the secret-adjacent file's contents remain unread.
- **G5** (DB / SQL / migration / production data) — Closed; nothing proposed; runner revival touching DB/migration/metadata is an explicit STOP.
- **G7** (runtime / deploy / restart / publication / cockpit) — Closed; nothing proposed; tests in future packets are not deployments and must use disposable paths.
- **Network fetch** — none performed and none authorized; `origin/main` was used strictly from local cache (`28e87357`). Any future fetch/pull is its own explicit approval, separate from G3 packet approval.
- **G1** (board reconciliation) — **COMPLETED** in Phase 0; Hwao-verified `HWAO_G1_BOARD_RECONCILIATION_VERIFIED_20260721`. Not an open gate; unaffected by this record.
- **G6** (status/debate-map docs run) — Held, unaffected by this record.

## 10. Safety ledger (this Phase 3.2 decision pass — all zero)

| Action | Count |
|---|---|
| Branch creation / switch / checkout | 0 |
| Worktree creation | 0 |
| Rebase / cherry-pick | 0 |
| Add / stage / commit / PR / push / merge | 0 |
| Stash / reset | 0 |
| File move / delete | 0 |
| Product / source / test edit | 0 |
| DB / SQL / migration action | 0 |
| Runtime / deploy / restart action | 0 |
| Network / fetch | 0 |
| Publication / cockpit change | 0 |
| `.env*` content access | 0 |
| Files written | 1 (this `BRANCH_FATE_DECISION.md`) |

Methods used: read-only file reads (`.hermes.md`, canonical plan, Phase 0 receipt, Phase 2 decision, Phase 3.1 census, Phase 3.2 manifest); read-only git (`branch --show-current`, `rev-parse`, `merge-base`, `rev-list --count`, `status --porcelain`, `diff --name-only`, `apply --reverse --check`); `shasum -a 256` on the four patch files. No fetch; no `.env*` opened; no /tmp or scratchpad files written.

---

`HWAO_PHASE3_BRANCH_FATE_DECISION_COMPLETE_20260721`
