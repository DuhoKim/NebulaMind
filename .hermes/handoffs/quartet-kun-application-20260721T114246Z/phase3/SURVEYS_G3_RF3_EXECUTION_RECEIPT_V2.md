# G3 Surveys RF-3 execution receipt — V2

Run: `quartet-kun-application-20260721T114246Z` · Phase 3 follow-on, G3 Surveys
Executor: Tori/Hermes — bounded tool executor and receipt verifier
Issued: 2026-07-22T13:51:33+0900 KST

Authority chain:

1. `SURVEYS_G3_REREVIEW_FAIL_RF2_RESCOPE_GATE_RECEIPT.md`
2. User line `UNFREEZE G3 SURVEYS RF-2 PLOTA 20260722` and `HWAO_G3_SURVEYS_RF2_ACTIVATED_20260722`
3. `SURVEYS_G3_RF2_MIRROR_REPIN_STOP_DECISION_RECEIPT.md`
4. `SURVEYS_G3_RF2_CENSUS_STOP_RF3_RESCOPE_RECEIPT.md`
5. User line `UNFREEZE G3 SURVEYS RF-3 CONTROLBAR 20260722` and `HWAO_G3_SURVEYS_RF3_ACTIVATED_20260722`
6. `SURVEYS_G3_RF3_MIRROR_REPIN_STOP_DECISION_RECEIPT.md` — `HWAO_G3_SURVEYS_RF3_MIRROR_REPIN_AUTHORIZED_20260722`

This receipt records RF-3 execution and V2 preservation only. It does not authorize wrap-up, Git/index changes, runtime, deployment, publication, cockpit updates, DB/SQL, network, cleanup, or worktree disposition.

## 1. Final closed-world scope

Disposable worktree: `/Users/duhokim/NebulaMind/agent-worktrees/g3-surveys-rework-20260722`

Immutable base: detached `28e873570f1c479fffd18a5106e5afa91d46e3e9`

Exactly seven unstaged tracked paths at completion:

1. `frontend/scripts/test-surveys-atlas-ia.mjs`
2. `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`
3. `frontend/src/components/surveys/ChartView.tsx`
4. `frontend/src/components/surveys/ControlBar.tsx`
5. `frontend/src/components/surveys/PlotA.tsx`
6. `frontend/src/components/surveys/PlotB.tsx`
7. `frontend/src/components/surveys/SurveysView.tsx`

Final index: empty. `FilterSheet.tsx` remained clean and read-only at index blob `e61f9e760400cc1e7d8c8cf06f7341097a45bdc3`. The four RF-1-corrected production files remained edit-frozen during RF-3. No new source file or dependency was added.

## 2. Required defect-class census

The RF-2 pre-edit census examined directly rendered Surveys components for:

- flattening semantics such as `role="img"` around focusable/interactive descendants; and
- `aria-controls` references whose targets are absent in the trigger's current state.

Findings:

- Expected PlotA findings: SVG `role="img"` over focusable `role="button"` points; inline missing-data target conditionally unmounted.
- Additional finding: ControlBar always exposed `aria-controls="surveys-filter-sheet"`, while FilterSheet returned `null` when closed.
- Clean for those two classes: SurveyCard, SurveyPeek, BandSpectrumStrip, SurveyLogo, repaired PlotB, and repaired DatasetCard.

The additional hit triggered the required STOP before any edit. Hwao locked the standards-sound E5 relationship:

- FilterSheet remains a conditionally mounted modal dialog with its mount-scoped behavior and animations.
- ControlBar exposes `aria-controls` only while `filterSheetOpen` is true.
- FilterSheet remains read-only.

## 3. RF-3 RED → GREEN evidence

### R8 — remove PlotA defect-enforcing assertions

Test-only change:

- Removed PlotA `role="img"` enforcement.
- Removed token-only PlotA `aria-controls` and target-`id` assertions that passed despite conditional unmounting.
- Retained benign accessible-label, `aria-expanded`, density, missing-data, and zero-plottable-row checks.

Post-excision baseline: `node scripts/test-surveys-atlas-ia.mjs` → `surveys atlas IA smoke checks passed`.

### R6 / E1 — PlotA interactive SVG semantics

RED:

- Added a TSX-tree inspector that finds the labelled PlotA SVG and the focusable `g` point descendants in that same SVG.
- Required container `role="group"`, retained ``aria-labelledby={`${titleId} ${descId}`}``, point `role="button"`, and `tabIndex={0}`.
- Observed failure: actual `containerRole: "img"`; all other fields matched.

GREEN:

- Changed only PlotA SVG `role="img"` to `role="group"`.
- Focus, Enter/Space activation, pointer behavior, title, description, and point labeling remained intact.
- Focused smoke passed.

### R7 / E2 — PlotA inline disclosure target

RED:

- Generalized the proven PlotB TSX disclosure inspector and applied it to PlotA.
- Required the panel to remain mounted, use `hidden={!missingExpanded}`, and retain the matching `missingListId` relationship.
- Observed failure: `panelConditionallyMounted: true`, `panelHidden: null`.

GREEN:

- Removed only the `missingExpanded &&` conditional wrapper.
- Added `hidden={!missingExpanded}` to the existing region.
- Focused smoke passed.

### R10 / E5 — ControlBar and FilterSheet locked dialog relationship

RED:

- Replaced the unconditional-attribute source regex with a paired ControlBar/FilterSheet AST inspection.
- Required ControlBar `aria-haspopup="dialog"`, `aria-expanded={filterSheetOpen}`, and `aria-controls={filterSheetOpen ? "surveys-filter-sheet" : undefined}`.
- Read-only FilterSheet lock required matching `id="surveys-filter-sheet"`, `role="dialog"`, and `aria-modal="true"` in the open branch.
- Observed failure: actual trigger controls were unconditional `surveys-filter-sheet`; every FilterSheet-side lock passed.

GREEN:

- Applied the single authorized ControlBar line: `aria-controls={filterSheetOpen ? "surveys-filter-sheet" : undefined}`.
- FilterSheet was not edited.
- Focused smoke passed.

### R9 / E4 — B1 initializer pin with self-tested teeth

Test-only AST checker:

- Rejects `const searchStatusOpSurveys = statusOpSurveys;`.
- Rejects a band-filtered first argument to `filterSurveysBySearch`.
- Accepts the exact direct-call fixture.
- Accepts the live memoized implementation only when its body is `filterSurveysBySearch(statusOpSurveys, state.search)` and dependencies are exactly `[statusOpSurveys, state.search]`.

The first checker version correctly rejected both bad fixtures but failed to recognize live `useMemo`; no production edit was made. The checker was strengthened to unwrap and validate the exact memoized form. Final focused smoke passed.

## 4. Final verification

All commands ran in the disposable worktree only.

1. `npm run test:surveys-atlas-ia` — PASS; final line `surveys atlas IA smoke checks passed`.
2. `npx --no-install tsc --noEmit` — PASS, no output.
3. `NEXT_TELEMETRY_DISABLED=1 npm run build` — PASS; compiled, type-checked, generated 44/44 static pages, and completed optimization/traces.
4. Build routes — `/surveys` at 17 kB / 129 kB first load; `/surveys/[slug]` at 6.68 kB / 103 kB first load.
5. Manifest/chunk probe — PASS for both route manifests, PlotA title marker, filter-dialog target, truthful filter-empty copy, PlotB filter-count copy, stale Mima absence, and Dataset Data link.
6. `git diff --check HEAD --` — PASS.
7. Scope — PASS: exactly seven ` M` paths, cached diff empty.
8. FilterSheet lock — PASS: clean/read-only, blob unchanged.
9. Added-line scan — no hardcoded secret assignment, process/eval execution, or unsafe HTML injection.
10. Primary integrity — PASS at `826e73381cb7870954bbd7f041a618408385a80a`, 20 modified / 360 untracked / 0 deleted, 4/4 dirty-intent patches reverse-apply.

## 5. Content-aware mirror ledger

Hwao's `SURVEYS_G3_RF3_MIRROR_REPIN_STOP_DECISION_RECEIPT.md` re-pinned linked mirror `main` and shared `origin/main` to `4bbb1160f0e93bd6c2e557cbc49254e76738347f`, with divergence context 6 ahead / 69 behind, while keeping RF-3's immutable base at `28e87357`.

The re-pin range from `ed207087` contained exactly two external Lab commits:

- `68c92c2` — `feat(lab): refresh Draft-board card text for A/B integrated results (#103)`
- `4bbb116` — `feat(lab): add 2026-07-22 work to Paper A revision log (#104)`

Changed paths were only two Lab study records and `frontend/src/app/lab/FlagshipStudies.tsx` / `FrontierDrafts.tsx`; zero protected Surveys/package overlap.

After the disjoint-fast-forward rule took effect, both the pre-verification and final-custody checkpoints observed no further advance: linked mirror and shared `origin/main` remained clean at `4bbb116` on `main`. Therefore the cumulative post-rule advance list is empty.

## 6. Preserved V2 artifact

Replacement patch:

`phase3/SURVEYS_G3_REVIEW_FIX_FINAL_V2.patch`

- Bytes: `53,521`
- SHA-256: `ecb095c1dbe6607db8a7570c8e4103bb6a64ed556b1fade404017757d42366bf`
- Exact source: `git -C <worktree> diff HEAD`
- Preservation verification: saved byte count and SHA-256 match the final live diff exactly.

The first V2 preservation attempt aborted before writing because the Hermes terminal stream capped stdout below this diff's size. The successful retry read the local Git byte stream directly, wrote through the file-write tool, and independently verified the saved file.

Frozen prior evidence remains untouched:

- V1 `SURVEYS_G3_REVIEW_FIX_FINAL.patch`: 39,513 bytes, SHA-256 `b39215c3c31763689d764fcb297600e946f2a2c253ffed21291427a3877bd75a`.
- `/tmp/g3-surveys-rework-20260722.diff`: SHA-256 `cae4cde97f35cbd0bb78ec8d20a33189fcfdb737675ac7264c50c1fac570154e`.

## 7. Safety ledger

RF-3 source/test writes: exactly PlotA, ControlBar, and the smoke script · FilterSheet writes 0 · other production writes 0 · new source files 0 · dependencies 0 · installs 0 · lane network/fetch 0 · Git index writes 0 · add/stage/commit/PR/push/merge 0 · stash/reset 0 · branch/checkout/worktree operations 0 · primary source writes 0 · mirror writes 0 · runtime/dev-server/port/deploy 0 · cockpit/publication 0 · DB/SQL 0 · `.env*` content access 0 · file moves/deletes 0 · V1/`/tmp` overwrites 0.

Artifact writes: V2 patch 1 · V2 execution receipt 1.

## 8. Remaining gate

A third fresh independent fail-closed review must verify V2 custody and judge B1–B5 plus E1–E4 and E5 against the locked conditional-IDREF design. PASS requires `passed: true`, `security_concerns: []`, exact scope, and exact hash. The verdict returns to Hwao either way. No source edit is authorized during review.

`TORI_G3_SURVEYS_RF3_EXECUTION_COMPLETE_V2_20260722`
