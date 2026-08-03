# G3 Surveys RF-2 census STOP — ControlBar/FilterSheet adjudication and RF-3 rescope gate — Hwao decision receipt

Run: `quartet-kun-application-20260721T114246Z` · Phase 3 follow-on, G3 Surveys unit, RF-2 census stage
Authority chain: `SURVEYS_G3_REREVIEW_FAIL_RF2_RESCOPE_GATE_RECEIPT.md` (RF-2) → user line `UNFREEZE G3 SURVEYS RF-2 PLOTA 20260722` → `HWAO_G3_SURVEYS_RF2_ACTIVATED_20260722` → `SURVEYS_G3_RF2_MIRROR_REPIN_STOP_DECISION_RECEIPT.md` (`HWAO_G3_SURVEYS_RF2_MIRROR_REPIN_AUTHORIZED_20260722`) → §5.2.4 census STOP → this receipt
Author: Hwao/Fable — packet issuer and final ratifier per `.hermes.md`
Issued: 2026-07-22T13:32 KST (2026-07-22T04:32 UTC)
Record type: **census-STOP adjudication + design ruling + RF-3 rescope-gate definition. This document executes nothing.** One file written (this receipt); no source/test edit, no git/index/worktree mutation, no runtime/cockpit/DB/network action, no `.env*` content access, no evidence overwrite. V1 and `/tmp` evidence preserved; V2 remains absent.

---

## Decision

1. **The census STOP was correct and the anti-ping-pong gate did exactly its job:** a real defect beyond PlotA was found BEFORE any edit, instead of by a fourth review round. No R8/R6/R7/R9 work started; the worktree freeze is verified intact.
2. **The extra hit is CONFIRMED as defect E5:** `ControlBar.tsx` renders its filter trigger with an unconditional `aria-controls="surveys-filter-sheet"` while `FilterSheet.tsx` returns `null` when closed — a dangling IDREF in the collapsed default state.
3. **Design ruling (§2): the standards-sound smallest fix is a conditional `aria-controls` on ControlBar alone. Mounted-hidden FilterSheet is REJECTED** — FilterSheet is a true modal dialog, where conditional mounting is the correct pattern; its lifecycle stays untouched. The chosen relationship is LOCKED (§2.3) and binds the next review's E5 acceptance.
4. **RF-3 is defined (§3) as the smallest next packet: ControlBar.tsx becomes the seventh authorized path; writable files are exactly three** (PlotA.tsx, smoke, ControlBar.tsx). FilterSheet.tsx remains read-only. All RF-2 work items carry over unchanged.
5. **RF-3 is NOT activated.** The scope expansion requires a NEW explicit user line (§5). Until it arrives, freeze persists; nothing may be edited.

## 1. Census reconciled and independently verified (Hwao, read-only, 13:30 KST)

- **Pins at census start and now:** exactly the five `␣M` paths; live diff hashes `b39215c3…7bd75a`; cached diff empty; V2 absent; mirror/origin-main pins per the re-pin receipt held. ✅
- **PlotA expected hits:** confirmed (role="img" over focusable `role="button"` points; missing-data `aria-controls` target conditional on `missingExpanded`) — already covered by RF-2's R6/R7. ✅
- **E5 grounded by direct code read (both files clean at base; blobs pinned below):**
  - `ControlBar.tsx:185-196` — the trigger has `aria-label="Open survey filters"`, **`aria-haspopup="dialog"`, `aria-expanded={filterSheetOpen}`, and unconditional `aria-controls="surveys-filter-sheet"`**.
  - `FilterSheet.tsx:43` — `if (!open) return null`; the target `id="surveys-filter-sheet"` exists only in the open branch (~line 94) on a container with **`role="dialog"` + `aria-modal="true"` + `aria-labelledby`**, under a fixed full-screen backdrop with click-to-close, an Escape handler bound only while open, and mount-scoped entrance animations.
- **Defect-class sweep co-signed:** across the surveys components, `aria-controls`/`role="img"` occur only in ControlBar:190 (E5), PlotB:116 (the repaired R5b disclosure — mounted-hidden, correct), and PlotA (known E1/E2). `SurveyCard.tsx`, `SurveyPeek.tsx`, `BandSpectrumStrip.tsx`, `SurveyLogo.tsx`: clean. ControlBar's `role="group"` wraps native buttons — non-flattening, compatible; not a defect. ✅ The census requirement of §5.2.4 is SATISFIED and recorded here (RF-3 does not re-run it).
- **Baseline blob pins for RF-3 preflight:** `PlotA.tsx` = `efe9d5d4bb43407e8429a40acf41987e640d5e0d` · `ControlBar.tsx` = `a72e9186f4887ce9831aabbdaa45f65ec93af063` · `FilterSheet.tsx` = `e61f9e760400cc1e7d8c8cf06f7341097a45bdc3`.

## 2. Design adjudication E5 — conditional IDREF, not mounted-hidden

### 2.1 Why mounted-hidden is wrong here

FilterSheet is a **modal dialog** (`role="dialog"`, `aria-modal="true"`, full-screen backdrop, Escape/click-outside dismissal, mount-scoped slide/fade/scale entrance animations). For modal dialogs, conditional rendering is the established, correct pattern; ARIA does not require dialog targets to persist while closed. Forcing mounted-hidden would: break the entrance animations (they run on mount; a `hidden` toggle never replays them), require restructuring the mount-scoped Escape/backdrop wiring, and keep an `aria-modal` container permanently in the DOM — real regression risk, zero assistive-technology gain.

### 2.2 Why this differs from DatasetCard and PlotA

DatasetCard (B4) and PlotA's missing-data region (E2) are **inline disclosure regions** — content blocks toggled in place by a disclosure button. There, mounted+`hidden` is the canonical APG relationship and cheap. FilterSheet is not a disclosure; it is a dialog. Same IDREF rule (references must resolve), different sound remedy per pattern.

### 2.3 LOCKED RELATIONSHIP (binds implementation, tests, and the third review's E5 acceptance)

- **Trigger (ControlBar):** `aria-haspopup="dialog"` and `aria-expanded={filterSheetOpen}` always present; **`aria-controls` present with value `"surveys-filter-sheet"` when `filterSheetOpen` is true, absent (`undefined`) otherwise** — e.g. `aria-controls={filterSheetOpen ? "surveys-filter-sheet" : undefined}`.
- **Dialog (FilterSheet, untouched):** keeps `if (!open) return null`; its open branch keeps `id="surveys-filter-sheet"`, `role="dialog"`, `aria-modal="true"`, `aria-labelledby`.
- **Result:** the IDREF exists exactly when its target exists — no dangling reference in any state.
- The third review judges E5 **against this locked relationship**, not against a mounted-hidden preference; this receipt is the documented rationale.

## 3. RF-3 — smallest rescope packet (defined, NOT activated)

**Objective:** RF-2's four items (E1–E4) unchanged, plus E5 under the locked relationship. Nothing else.

### 3.1 Scope

- Authorized-path universe for this unit becomes: the parent packet's ten + `PlotA.tsx` (RF-2) + **`ControlBar.tsx` (RF-3, new — outside even the original ten)**.
- **Writable in RF-3: exactly three files** — `frontend/src/components/surveys/PlotA.tsx`, `frontend/scripts/test-surveys-atlas-ia.mjs`, `frontend/src/components/surveys/ControlBar.tsx`.
- **`FilterSheet.tsx` is read-only.** Tests may READ its source for lock assertions; if any step appears to require editing it → STOP back to Hwao. The four RF-1-fixed production files remain edit-frozen. No new files, no dependencies, no network/install. Primary and mirror read-only. `.env*` never touched.

### 3.2 Activation preflight (read-only; any mismatch → STOP)

1. Worktree: five `␣M` exactly; cached diff empty; `git diff HEAD` = 39,513 B / `b392…7bd75a`; blobs match §1 pins (PlotA `efe9d5d4…`, ControlBar `a72e9186…`, FilterSheet `e61f9e76…`).
2. Primary `826e733` + 20/360/0 + 4/4 reverse-apply; mirror `main @ ed207087` clean; shared `origin/main` = `ed207087` (divergence context 6/67 per the re-pin receipt).
3. phase3: V1 patch exact (`b392…`/39,513); V2 absent. `/tmp` artifact untouched (`cae4…`).
4. Census: already satisfied and recorded in §1 — do NOT re-run; any NEW defect-class sighting during work is still a STOP.

### 3.3 Method — strict RED-first, in this order

1. **R8 (test-only):** excise the PlotA defect-enforcing smoke assertions (~271-275); benign neighbors may stay; record post-excision baseline; excised assertions never return.
2. **R6:** PlotA container semantics — new AST assertions (role="group" + aria-labelledby retained; focusable `role="button"` + `tabIndex={0}` points; no `role="img"` over interactive content) → observe FAIL → minimal fix `PlotA.tsx:186-288` → GREEN.
3. **R7:** PlotA missing-data region — new AST assertions (always mounted, `hidden={!missingExpanded}`, IDREF resolvable collapsed) → observe FAIL → minimal fix `PlotA.tsx:123-168` → GREEN.
4. **R10 (E5):** new AST assertions for the §2.3 locked relationship — ControlBar side: `aria-controls` is the conditional expression gated on `filterSheetOpen` with value `"surveys-filter-sheet"`, alongside `aria-haspopup="dialog"` and `aria-expanded={filterSheetOpen}` → **observe FAIL against current unconditional code** → minimal fix in `ControlBar.tsx:185-196` → GREEN. FilterSheet side (read-only lock, passing from the start): open branch contains matching `id="surveys-filter-sheet"` with `role="dialog"` + `aria-modal` — a regression pin, not a RED pair.
5. **R9 (test-only):** the B1 initialization pin (`searchStatusOpSurveys` = `filterSurveysBySearch(statusOpSurveys, state.search)`), teeth proven by fixture self-test (must REJECT the synthetic `const searchStatusOpSurveys = statusOpSurveys;` bypass and a band-filtered variant; ACCEPT live source). Self-test unable to reject → STOP.

**RED rule unchanged:** every production correction (R6, R7, R10) requires its new assertion observed failing first; passing pre-fix → STOP and re-derive.

### 3.4 Completion requirements

1. Full smoke → final line `surveys atlas IA smoke checks passed`; 2. `npx --no-install tsc --noEmit` clean; 3. `NEXT_TELEMETRY_DISABLED=1 npm run build` completes; 4. `/surveys` + `/surveys/[slug]` manifest/chunk markers (no server, no port, no deploy — G7 Closed).
5. **Replacement final patch:** `git -C <worktree> diff HEAD` → `phase3/SURVEYS_G3_REVIEW_FIX_FINAL_V2.patch`, byte count + SHA-256 recorded in a V2 execution receipt. Expected scope: **exactly SEVEN `␣M` paths** (the five + PlotA + ControlBar), cached diff empty. V1 and `/tmp` evidence never overwritten.
6. **Third independent review:** new fail-closed reviewer; inputs = V2 patch + hash, base `28e87357`, the seven-path scope law, acceptance = **B1–B5 + E1–E4 + E5-as-locked (§2.3, rationale included)**. PASS = `passed:true` AND `security_concerns:[]` AND exact custody. Verdict returns to Hwao either way (verbatim JSON embedded in the next receipt if no file is exposed). No fix→review ping-pong without Hwao between rounds.

### 3.5 Stop rules and rollback

All parent + RF-1 + RF-2 stops carry forward, plus: any edit outside the three writable files → STOP; FilterSheet edit need → STOP; any new defect-class sighting → STOP; RED unachievable (R6/R7/R10) → STOP; R9 self-test unable to reject → STOP; any pin drift (worktree hash, three blobs, primary, mirror, shared origin/main) → STOP; evidence overwrite attempt → STOP. Rollback unchanged (parent §12): lossless preservation before any worktree removal; never stash/reset the primary.

## 4. Exact approval wording Tori should request

Tori presents: "RF-2's mandatory pre-edit census caught one more defect outside the approved files, before anything was touched: the Filters button in ControlBar always advertises `aria-controls` for the filter sheet, but the sheet only exists in the DOM while open — a dangling reference in the default state. Everything else censused clean. Hwao adjudicated the sheet's close-on-unmount behavior as correct modal-dialog design, so the smallest fix is to make the button's `aria-controls` conditional — one line in ControlBar — rather than restructuring FilterSheet. RF-3 = RF-2's PlotA and smoke work unchanged, plus ControlBar as a third writable file, failing-test-first throughout, then the replacement patch and a third independent review judging against this locked design. Still no commit, push, merge, network, or runtime. To proceed, please reply exactly:"

> **`UNFREEZE G3 SURVEYS RF-3 CONTROLBAR 20260722`**

- That verbatim line (or an unambiguous equivalent naming "RF-3" / "ControlBar") activates RF-3 as defined in §3, one-shot; Hwao will acknowledge with `HWAO_G3_SURVEYS_RF3_ACTIVATED_20260722`.
- Alternatives: **`KEEP FROZEN`** or **`DISCARD WITH PRESERVATION`** (parent §12 flow).

## 5. Gate ledger after this receipt

G1 Completed · G2 Completed · **G3 Surveys unit: RF-2 census STOP adjudicated; E5 confirmed; design locked (conditional IDREF); RF-3 defined and awaiting the §4 user line; freeze maintained** · G3 all other units Held · G4a/G4b/G4c Held separately · G5 Closed · G6 Held · G7 Closed — no cockpit/status write accompanies this receipt.

## 6. Safety ledger for this adjudication pass

Source/test edits 0 · git/index/worktree writes 0 · stage/commit/PR/push/merge 0 · stash/reset 0 · file moves/deletes 0 · evidence overwrites 0 · DB/SQL 0 · runtime/deploy/cockpit/publication 0 · network/fetch 0 · `.env*` content access 0 · fixes executed 0 · **files written 1 (this receipt)**.

Methods: read-only reads of the RF-2 rescope gate and mirror re-pin receipts; direct reads of `ControlBar.tsx:175-200` and `FilterSheet.tsx:30-100` plus lifecycle grep in the frozen worktree; defect-class grep across the surveys components; read-only git (`status --porcelain=v1`, `diff HEAD` piped to `shasum` only, `rev-parse :path` ×3); `ls`/`date`. No state changed anywhere.

---

`HWAO_G3_SURVEYS_RF2_CENSUS_STOP_DECIDED_20260722`
