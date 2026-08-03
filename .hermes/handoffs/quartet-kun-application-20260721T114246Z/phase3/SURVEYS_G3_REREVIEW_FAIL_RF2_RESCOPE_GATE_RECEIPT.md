# G3 Surveys fresh re-review FAIL — re-adjudication and RF-2 rescope gate — Hwao decision receipt

Run: `quartet-kun-application-20260721T114246Z` · Phase 3 follow-on, G3 Surveys unit, after RF-1 + MC-1
Authority chain: `SURVEYS_G3_APPROVAL_PACKET.md` → `SURVEYS_G3_REVIEW_FAIL_FIX_GATE_RECEIPT.md` (RF-1) → user line `UNFREEZE G3 SURVEYS REVIEW-FIX R1-R5 20260722` → `SURVEYS_G3_RF1_MIRROR_DRIFT_STOP_DECISION_RECEIPT.md` (MC-1) → `SURVEYS_G3_RF1_EXECUTION_RECEIPT.md` (`TORI_G3_SURVEYS_RF1_EXECUTION_COMPLETE_20260722`) → this receipt
Author: Hwao/Fable — packet issuer and final ratifier per `.hermes.md`
Issued: 2026-07-22T11:54 KST (2026-07-22T02:54 UTC)
Record type: **re-review FAIL adjudication + RF-2 rescope-gate definition. This document executes nothing.** One file written (this receipt); no source/test edit, no git/index/worktree mutation, no runtime/cockpit/DB/network action, no `.env*` content access. Worktree and all sources stay frozen.

---

## Decision

1. **The fresh re-review verdict `passed: false` is adopted fail-closed.** Acceptance B1, B2, B4: PASS. B3 and B5: FAIL — residual defects sit in `PlotA.tsx` (outside RF-1's writable set) and in the smoke suite. There is no fix→review ping-pong: this receipt is the mandated Hwao re-adjudication between rounds.
2. **RF-1 execution was COMPLIANT; the gap is a scoping defect, owned by Hwao.** PlotA could not lawfully be edited under RF-1, and excising the smoke's PlotA `role="img"` assertion would have made the suite fail against a file the executor was forbidden to fix. Lesson recorded (§4): the acceptance surface (what the modified code renders) is larger than the diff file set; future fix packets must census directly-rendered child components before scoping.
3. **RF-2 is WARRANTED and defined (§5) as the smallest rescope: `frontend/src/components/surveys/PlotA.tsx` is added as the sixth authorized path.** Writable files in RF-2 are exactly TWO — PlotA.tsx (production) and the smoke script (tests). The four already-fixed production files are EDIT-FROZEN (their passing B1/B2/B4 + PlotB-B3 fixes must not be reopened).
4. **RF-2 is NOT activated by this receipt.** Scope expansion requires a NEW explicit user approval line (§7). Until it arrives: no source/test edit anywhere, freeze persists.

## 1. Reviewer verdict — verbatim evidence of record

Delegation `deleg_c833f280`, completed 2026-07-22 after 415.61 s. **This completion exposed no saved summary filepath; the verbatim JSON below, quoted from the relay, is therefore the durable evidence record — no file path is to be invented for it.**

```json
{"passed":false,"security_concerns":[],"logic_errors":["frontend/src/components/surveys/PlotA.tsx:186-288 remains an interactive SVG with role=\"img\" around focusable role=\"button\" descendants, so the modified ChartView still exposes a directly affected accessibility path whose point semantics may be flattened.","frontend/src/components/surveys/PlotA.tsx:123-168 keeps its aria-controls target conditionally unmounted while the missing-data disclosure is collapsed, leaving a dangling IDREF in the default state.","frontend/scripts/test-surveys-atlas-ia.mjs:271-275 still asserts PlotA role=\"img\" and uses token-only aria-controls/id checks that pass the two accessibility defects above, contrary to the requirement to remove defect-enforcing coverage.","frontend/scripts/test-surveys-atlas-ia.mjs:240-269 executes the search helper and checks downstream prop names, but never AST-checks that searchStatusOpSurveys is initialized by filterSurveysBySearch(statusOpSurveys, state.search), so restoring the original search bypass under the same variable name would still pass."],"suggestions":[],"scope_findings":["The preserved patch is exactly 39,513 bytes with SHA-256 b39215c3c31763689d764fcb297600e946f2a2c253ffed21291427a3877bd75a and is byte-identical to the live git diff HEAD.","HEAD is 28e873570f1c479fffd18a5106e5afa91d46e3e9; the index is clean and the worktree contains exactly the five allowed modified tracked paths with no untracked or out-of-scope drift.","Correcting the directly affected PlotA accessibility defects would require an explicit scope expansion because PlotA.tsx is not one of the five allowed paths."],"acceptance":{"B1":"pass","B2":"pass","B3":"fail","B4":"pass","B5":"fail"},"summary":"Fail-closed review fails despite exact custody and correct PlotB/DatasetCard production fixes because a directly affected interactive SVG remains inaccessible and the smoke suite still locks or misses the relevant regressions."}
```

## 2. Independent grounding by Hwao (read-only, 11:53 KST)

| Point | Observed | Verdict-claim match |
|---|---|---|
| Preserved patch custody | `phase3/SURVEYS_G3_REVIEW_FIX_FINAL.patch` = 39,513 bytes, SHA-256 `b39215c3…7bd75a`; live `git -C <worktree> diff HEAD` hashes identically | ✅ exact |
| Worktree | detached `28e87357`; exactly five `␣M` paths; cached diff empty | ✅ |
| PlotA is a genuine sixth path | `git status -- PlotA.tsx` empty (unmodified); index blob = `efe9d5d4bb43407e8429a40acf41987e640d5e0d` (= HEAD state, pinned here as the RF-2 pre-fix baseline) — the defects are pre-existing upstream code of the same classes as B3/B4 | ✅ |
| Smoke still enforces PlotA defects (reviewer error 3) | Read directly at smoke ~271-276: `assert.match(plotA, /role="img"/, 'Plot SVG should expose image semantics.')` plus token-only `aria-controls={missingListId}` / `id={missingListId}` presence checks that cannot detect a conditionally-unmounted panel | ✅ confirmed by direct read |
| Missing B1 initialization pin (reviewer error 4) | Read directly at smoke 240-269: behavioral fixture for `filterSurveysBySearch` + JSX wiring checks (`ChartView plotBSurveys=searchStatusOpSurveys`, `PlotB surveys=plotBSurveys`) exist, but **no assertion that `searchStatusOpSurveys` is initialized by `filterSurveysBySearch(statusOpSurveys, state.search)`** — re-aliasing `searchStatusOpSurveys = statusOpSurveys` would pass every current check | ✅ confirmed by direct read |
| PlotA production defects (reviewer errors 1-2) | Proven present by the PASSING defect-enforcing assertion (`/role="img"/` matched PlotA source in Tori's green run) plus reviewer line-level inspection at 186-288 and 123-168; PlotA untouched since base | ✅ accepted |
| Primary | `826e733`, 20 modified / 360 untracked / 0 deleted; (4/4 reverse-apply re-verified at 11:36 KST this session) | ✅ |
| Mirror pin | `1a8da92e` on `chore/lab-refresh-paper-pdfs-20260722`, clean — unchanged vs the MC-1 pin | ✅ |
| MC-1 artifacts | V1 patch (11:40) + execution receipt (11:41) present in phase3 | ✅ |

## 3. What stands and what fails

- **Stand (do not reopen):** the RF-1 production fixes in `SurveysView.tsx`, `ChartView.tsx`, `PlotB.tsx`, `SurveyDetailClient.tsx` — B1 (search+status+operator, no band, consistent counts), B2 (truthful filtered-empty copy), B4 (mounted+hidden DatasetCard panel, sibling link/button), and PlotB's own B3 fix (`role="group"`). Custody and closed-world discipline: exact.
- **Fail:** B3 at the rendered-surface level (PlotA, drawn by the modified ChartView, keeps `role="img"` over focusable `role="button"` points, and its missing-data panel unmounts while collapsed) and B5 (smoke retains PlotA defect-enforcing assertions and lacks the B1 initialization pin).
- The `/tmp` artifact (`cae4…`, first FAIL) and the V1 patch (`b392…`, second FAIL) are both frozen review evidence. **Neither is ever overwritten, moved, or deleted under this unit's authorities.**

## 4. Scoping lesson (binding on future packets in this run)

RF-1's writable set was inherited from the failed diff's file list, while its acceptance criteria (B1–B5) implicitly ranged over the whole rendered Surveys surface. Components rendered by modified files (here: PlotA via ChartView) sat in the gap. **Rule going forward: a fix packet's scope census must enumerate directly-rendered child components of every modified file for the defect classes under acceptance, before the writable set is frozen.** RF-2 §5.2 applies this rule.

## 5. RF-2 — smallest rescope packet (defined, NOT activated)

**Objective:** resolve exactly the four re-review findings (E1 PlotA container semantics; E2 PlotA mounted-hidden panel; E3 smoke de-enforcement; E4 smoke B1 initialization pin). Nothing else.

### 5.1 Scope

- Authorized paths: the RF-1 five **plus** `frontend/src/components/surveys/PlotA.tsx` (sixth). 
- **Writable in RF-2: exactly two files** — `PlotA.tsx` (production) and `frontend/scripts/test-surveys-atlas-ia.mjs` (tests). The other four modified files are **edit-frozen**; a genuine need to touch any of them → STOP back to Hwao (their acceptance-passing fixes must not be reopened).
- Same frozen worktree, same detached base `28e87357`. No new files, no dependencies, no network/install (parent §10). Primary checkout and live mirror read-only. `.env*` never touched.

### 5.2 Activation preflight (read-only; any mismatch → STOP)

1. Worktree: exactly five `␣M` paths; cached diff empty; `git diff HEAD` = 39,513 bytes, SHA-256 `b392…7bd75a`; `PlotA.tsx` clean with index blob `efe9d5d4bb43407e8429a40acf41987e640d5e0d`.
2. Primary: `826e733`, 20/360/0, 4/4 dirty-intent reverse-apply OK. Mirror: `1a8da92e` on `chore/lab-refresh-paper-pdfs-20260722`, clean.
3. phase3: V1 patch present at `b392…`/39,513; `SURVEYS_G3_REVIEW_FIX_FINAL_V2.patch` absent.
4. **Defect-class census (read-only, anti-ping-pong):** scan the components directly rendered by the five modified files (at minimum `PlotA.tsx`, `SurveyCard.tsx`, `SurveyPeek.tsx`, `BandSpectrumStrip.tsx`, `FilterSheet.tsx`) for the two defect classes — `role="img"` (or any flattening role) wrapping focusable/interactive descendants, and `aria-controls` targets conditionally unmounted. Census results go in the RF-2 execution receipt. **If any hit exists beyond PlotA → STOP before any edit** and return to Hwao for rescope; if clean apart from PlotA, proceed.

### 5.3 Method — strict RED-first, in this order

1. **R8 (E3, test-only):** excise the PlotA defect-enforcing assertions (the `role="img"` enforcement and token-only `aria-controls`/`id` presence checks at smoke ~271-275). Benign neighbors (aria-labelledby presence, `aria-expanded` state check, label-density check) may stay. Record the post-excision baseline. Defect-enforcing assertions may never return.
2. **R6 (E1):** add NEW AST assertions — PlotA's SVG container uses interactive-compatible semantics (`role="group"`, retaining `aria-labelledby`), with focusable `role="button"` + `tabIndex={0}` point descendants preserved, and no `role="img"` wrapping interactive content → **observe FAIL against current PlotA** → minimal fix in `PlotA.tsx:186-288` (role change mirroring the proven PlotB R3 pattern; titles/descriptions/keyboard/pointer behavior intact) → GREEN.
3. **R7 (E2):** add NEW AST assertions — PlotA's missing-data controlled region is always mounted with `hidden={!missingExpanded}`; no conditional unmount; `aria-controls` IDREF resolvable in the collapsed default → **observe FAIL** → minimal fix in `PlotA.tsx:123-168` (mirroring the PlotB R5b disclosure pattern) → GREEN.
4. **R9 (E4, test-only):** add the AST initialization pin — `searchStatusOpSurveys` in `SurveysView.tsx` must be initialized by `filterSurveysBySearch(statusOpSurveys, state.search)`. Current production is already correct, so RED-by-fix is impossible; **teeth are proven by fixture self-test instead:** the checker must REJECT a synthetic defective fixture (e.g. `const searchStatusOpSurveys = statusOpSurveys;` and a band-filtered variant) and ACCEPT the live source. If the self-test cannot demonstrate rejection → STOP.

**RED rule unchanged:** each production correction (R6, R7) requires its new assertion observed failing first; an assertion passing pre-fix is a STOP to re-derive, never permission to edit.

### 5.4 Completion requirements

1. Full focused smoke → final line `surveys atlas IA smoke checks passed`.
2. `npx --no-install tsc --noEmit` → clean.
3. `NEXT_TELEMETRY_DISABLED=1 npm run build` → completes.
4. `/surveys` and `/surveys/[slug]` manifest/chunk markers present. No server start, no port, no deploy — G7 Closed.
5. **Replacement final patch:** capture `git -C <worktree> diff HEAD` to `phase3/SURVEYS_G3_REVIEW_FIX_FINAL_V2.patch` with byte count and SHA-256 recorded in a V2 execution receipt. Expected post-RF-2 scope: **exactly six `␣M` paths** (the five + PlotA), cached diff empty. **V1 patch and `/tmp` artifact remain untouched as review evidence.**
6. **Third independent review:** new fail-closed reviewer; inputs = V2 patch path + its SHA-256, base `28e87357`, six-path scope law, acceptance = original B1–B5 **plus E1–E4**. PASS = `passed:true` AND `security_concerns:[]` AND exact custody. Verdict (JSON verbatim if no file is exposed) returns to Hwao either way — PASS → fresh wrap-up receipt pipeline; FAIL → re-adjudication. No fix→review ping-pong without Hwao between rounds.

### 5.5 Stop rules and rollback

All parent + RF-1 stops carry forward, plus: any edit outside {`PlotA.tsx`, smoke} → STOP; census hit beyond PlotA (§5.2.4) → STOP; RED unachievable for R6/R7 → STOP; R9 self-test unable to reject the defective fixture → STOP; any pin drift (worktree hash, PlotA blob, primary, mirror) → STOP; any attempt to overwrite V1/`/tmp` evidence → STOP. Rollback unchanged (parent §12): lossless preservation before any worktree removal; never stash/reset the primary.

## 6. Exact approval wording Tori should request

Tori presents: "The second independent review failed the Surveys unit on residual defects outside RF-1's authority: PlotA — rendered inside the fixed chart area but not one of the five authorized files — still has an image-role SVG over interactive points and a disclosure panel that unmounts while collapsed; and the smoke suite still asserts the PlotA defects and lacks an AST pin of the search fix. The correct PlotB/DatasetCard fixes all passed and stay. Hwao defined a smallest rescope RF-2: add PlotA.tsx as the sixth file, failing-AST-test-first fixes there, strengthen the smoke, everything else edit-frozen, then a replacement patch and a third independent review. Still no commit, push, merge, network, or runtime. To proceed, please reply exactly:"

> **`UNFREEZE G3 SURVEYS RF-2 PLOTA 20260722`**

- That verbatim line (or an unambiguous equivalent naming "RF-2" / "PlotA") activates RF-2 as defined in §5, one-shot; Hwao will acknowledge with `HWAO_G3_SURVEYS_RF2_ACTIVATED_20260722`.
- Alternatives: **`KEEP FROZEN`** (unit persists as-is for inspection) or **`DISCARD WITH PRESERVATION`** (parent §12 flow; both frozen evidence patches already sit in phase3).

## 7. Gate ledger after this receipt

G1 Completed · G2 Completed · **G3 Surveys unit: RF-1 fixes verified for B1/B2/B4 + PlotB-B3; second review FAILED on PlotA (B3) and smoke (B5); freeze maintained; RF-2 defined and awaiting the §6 user line** · G3 all other units Held · G4a/G4b/G4c Held separately · G5 Closed · G6 Held · G7 Closed — no cockpit/status write accompanies this receipt.

## 8. Safety ledger for this adjudication pass

Source/test edits 0 · git/index/worktree writes 0 · stage/commit/PR/push/merge 0 · stash/reset 0 · file moves/deletes 0 · patch/evidence overwrites 0 · DB/SQL 0 · runtime/deploy/cockpit/publication 0 · network/fetch 0 · `.env*` content access 0 · fixes executed 0 · **files written 1 (this receipt)**.

Methods: read-only reads of the RF-1 fix-gate receipt, MC-1 drift decision, RF-1 execution receipt, and the relayed verdict JSON; read-only git in worktree/primary/mirror (`rev-parse`, `status --porcelain=v1`, `diff --cached --name-only`, `diff HEAD` piped to `shasum`/`wc -c` only, `rev-parse :path`); `shasum -a 256` on the preserved V1 patch; direct read of smoke lines 240-276; `ls`/`date`. No state changed anywhere.

---

`HWAO_G3_SURVEYS_REREVIEW_FAIL_DECIDED_20260722`
