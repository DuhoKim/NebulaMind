# G3 Surveys independent-review FAIL — reconciliation and review-fix gate — Hwao decision receipt

Run: `quartet-kun-application-20260721T114246Z` · Phase 3 follow-on, G3 Surveys unit
Authority chain: `SURVEYS_G3_APPROVAL_PACKET.md` (`HWAO_G3_SURVEYS_ONLY_APPROVED_20260722`) → `SURVEYS_G3_STAGE_STOP_DECISION_RECEIPT.md` (`HWAO_G3_SURVEYS_STAGE_STOP_DECIDED_20260722`) → this receipt
Author: Hwao/Fable — packet issuer and final ratifier per `.hermes.md`
Issued: 2026-07-22T09:38 KST (2026-07-22T00:38 UTC)
Record type: **decision + fix-gate definition. This document executes nothing.** One file written (this receipt); no source/test edit, no git/index write, no runtime/cockpit/DB/network action, no `.env*` content access.

---

## Decision

1. **The independent review verdict `passed: false` is adopted fail-closed.** The unit is NOT acceptance-complete. Five blocking defects (B1–B5, §2) stand.
2. **The wrap-up recommendation is WITHDRAWN.** `SURVEYS_G3_STAGE_STOP_DECISION_RECEIPT.md` §5 option 1 ("unfreeze for wrap-up — recommended") is superseded by this receipt. Keep-frozen is the standing default.
3. **The worktree remains FROZEN.** No user unfreeze line has arrived in this chat. Nothing in this receipt unfreezes it.
4. **The smallest review-fix packet RF-1 is DEFINED (§4) but NOT ACTIVATED.** Execution of any fix requires a new explicit user approval line (§5–§6). No self-granted continuation.

## 1. Reviewer verdict reconciled (custody exact)

- Verdict source: `/Users/duhokim/.hermes/cache/delegation/subagent-summary-0-20260722_092217_595513.txt` — fresh independent reviewer, fail-closed protocol.
- `passed`: **false** · `security_concerns`: **[] (empty — no security escalation; failure is correctness/accessibility/test-adequacy)** · `suggestions`: [].
- Reviewer scope finding (quoted): live diff **21,029 bytes**, SHA-256 `cae4cde97f35cbd0bb78ec8d20a33189fcfdb737675ac7264c50c1fac570154e`, "exactly matching the supplied artifact; its five modified tracked files are within Hwao's ten-path allowlist, status showed no untracked or out-of-scope files."
- **Hwao custody re-verification at 2026-07-22T09:37:35 KST:** `shasum -a 256 /tmp/g3-surveys-rework-20260722.diff` = `cae4cde97f35cbd0bb78ec8d20a33189fcfdb737675ac7264c50c1fac570154e` — byte-identical to the hash pinned in the stage-stop receipt §2 and to the reviewer's artifact. The reviewed artifact IS the frozen worktree state.
- Lana's final pane (%276) was not consulted: the reviewer JSON plus the frozen artifact fully specify the blockers; no additional evidence was required.

## 2. Blocking defects B1–B5 (normative for RF-1)

- **B1 — PlotB bypasses global search.** `SurveysView.tsx:152-183,267-270` and `ChartView.tsx:72-102` feed PlotB a `statusOpSurveys` dataset filtered by status+operator while omitting the global search filter. PlotB can render surveys the search excluded while the shared header reports a smaller "matching filters" count, and PlotB's SVG description calls its larger set "matching surveys." **Required semantics: PlotB's dataset is search+status+operator filtered with NO band filter** (band exclusion is the intentional preserve-out-of-band behavior; search bypass is not).
- **B2 — Untruthful empty-state copy.** `PlotB.tsx:148-160` shows "No data yet — populated by Mima" whenever the filtered input is empty, but that state can arise purely from filter selections. **Required: truthful filtered-empty copy** for the filters-yield-zero case; ingestion-status claims may not be emitted for filter-caused emptiness.
- **B3 — SVG role conflict.** `PlotB.tsx:169-179,220-236` sets `role="img"` on the SVG while nesting focusable `role="button"` point groups inside it; an image role flattens descendants to presentational, making the interactive semantics structurally unreliable. **Required: compatible interactive SVG container semantics** (group/document-appropriate semantics with an accessible name; interactive points remain genuinely focusable and exposed — no `role="img"` wrapping interactive descendants).
- **B4 — DatasetCard disclosure defects.** `SurveyDetailClient.tsx:347-398`: `aria-controls` points to a panel that is unmounted while collapsed (dangling IDREF in the default state), and the interactive Data anchor (lines 377-393) nests inside the disclosure button (invalid nested interactive content). **Required: the controlled region remains mounted and hidden when collapsed** (IDREF always resolvable) **and the link and button are siblings**, never nested.
- **B5 — Smoke test enforces the defects.** `test-surveys-atlas-ia.mjs:104-158` uses source-text regex assertions that lock in the faulty `statusOpSurveys` flow and pass the incompatible `role="img"`/`role="button"` structure and conditionally-missing `aria-controls` targets; there is no behavioral/AST structural coverage of search combinations, filtered-empty copy, log-axis fixtures, disclosure relationships, or the accessibility tree. **Required: the defect-enforcing assertions are removed and replaced with behavioral/AST structural coverage (§4.4).**

## 3. Effect on prior records

- Stage-stop receipt §5.1 (wrap-up recommended): **withdrawn** (this receipt, Decision 2). §5.2 (keep frozen) is the operative default until the user's new line.
- The executor-lane verification PASS (smoke/tsc/build/route) is **no longer acceptance evidence**: the smoke itself is part of the defect set (B5). `tsc`/`build`/route markers remain necessary but insufficient.
- The original one-shot G3 authority re-latched at the STOP and confers nothing further. **No live record currently authorizes any production edit.**
- The parent approval packet's discipline (§6 scope law, §10 no-network/no-install, §11 stops, §12 rollback, §13 prohibitions) carries forward unchanged into RF-1.

## 4. Review-fix packet RF-1 — defined, awaiting activation

**Objective:** fix exactly B1–B5, nothing else. Smallest possible diff on top of the frozen state.

### 4.1 Where and what scope

- **Same frozen worktree** `/Users/duhokim/NebulaMind/agent-worktrees/g3-surveys-rework-20260722`, detached HEAD `28e873570f1c479fffd18a5106e5afa91d46e3e9`. No new worktree, no base advance, no fetch.
- **Writable tracked paths: exactly the same five already-modified files, no others:**
  1. `frontend/scripts/test-surveys-atlas-ia.mjs`
  2. `frontend/src/components/surveys/SurveysView.tsx`
  3. `frontend/src/components/surveys/ChartView.tsx`
  4. `frontend/src/components/surveys/PlotB.tsx`
  5. `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`
- The other five packet paths are NOT writable in RF-1. A fix that genuinely needs a sixth file is a STOP → fresh rescope packet, not an inline widening. No new source files; generated build/test outputs remain disposable per parent §6. Primary checkout and live mirror stay read-only.

### 4.2 Activation preflight (read-only, before any edit)

- Worktree status shows exactly the five `␣M` unstaged entries; `git diff --cached --name-only` empty (index pristine).
- `git -C <worktree> diff HEAD | shasum -a 256` still equals `cae4cde9…154e`.
- Primary recount: `feat/surveys-atlas-ia-p1-20260627` @ `826e733`, 20/360/0, 4/4 dirty-intent patches reverse-apply OK. Mirror at `28e8735 [main]`. No fetch.
- Any drift → STOP and re-inventory; RF-1 does not proceed.

### 4.3 Method — strict RED-first, per correction

Order and rules (binding):

1. **R5a — excise the defect-enforcing assertions** from `test-surveys-atlas-ia.mjs:104-158` (test-only edit; no production file touched). Record the post-excision smoke baseline. Regex assertions that enforce B1/B3/B4 structures may never return.
2. **R1 (fixes B1):** add NEW behavioral/AST assertions that the PlotB dataset derivation applies search+status+operator and omits band, and that PlotB's rendered description/header counts are consistent with that set → **observe FAIL against the frozen code** → minimal production fix in `SurveysView.tsx` + `ChartView.tsx` (and PlotB description if implicated) → GREEN.
3. **R2 (fixes B2):** NEW failing assertion with a filters-yield-zero fixture requiring truthful filtered-empty copy and forbidding ingestion-claim copy in that state → observe FAIL → fix `PlotB.tsx` empty-state branch → GREEN.
4. **R3 (fixes B3):** NEW failing assertions on the SVG container semantics (no `role="img"` with focusable descendants; container exposes an accessible name; point interactivity preserved) → observe FAIL → fix `PlotB.tsx` → GREEN.
5. **R4 (fixes B4):** NEW failing assertions that the controlled panel exists mounted+hidden while collapsed, `aria-controls` resolves in the default state, and the Data link is a sibling of (not nested in) the disclosure button → observe FAIL → fix `SurveyDetailClient.tsx` → GREEN.
6. **R5b — coverage completion:** add the remaining reviewer-named coverage (search-combination behavior, log-axis fixtures, disclosure relationship, accessibility structure) so the smoke is behavioral/AST-structural, not regex-only.

**RED rule (parent §7 sharpened):** each production correction R1–R4 is preceded by its own NEW assertion observed to FAIL against the then-current code. If a proposed RED assertion passes before the fix, STOP and re-derive the assertion — that is never permission to edit production code.

**Harness constraint:** parent §10 stands — no network, no installs, no new dependencies. AST assertions use the already-on-disk `typescript` compiler API; behavioral assertions use plain Node against importable/extractable logic. If adequate coverage is impossible without a new dependency → STOP and report; no offline-install workaround.

### 4.4 Completion requirements (all mandatory, in the worktree only)

1. Focused smoke: `cd frontend && node scripts/test-surveys-atlas-ia.mjs` → final line `surveys atlas IA smoke checks passed`, now backed by the B1–B5 behavioral/AST assertions.
2. `cd frontend && npx --no-install tsc --noEmit` → clean.
3. `cd frontend && npm run build` → completes.
4. Route markers: `/surveys` and `/surveys/[slug]` present in build output/route manifest. **No `next start`/`next dev`, no port bound, no deploy — G7 Closed.**
5. **Regenerated final patch:** `git -C <worktree> diff HEAD` captured to `phase3/SURVEYS_G3_REVIEW_FIX_FINAL.patch` with its SHA-256 recorded in the execution receipt (`/tmp` copies are reboot-fragile; phase3 is the preserved home).
6. **Fresh independent re-review:** a new fail-closed reviewer instance, given the regenerated patch hash and B1–B5 as acceptance criteria, must return `passed: true` with `security_concerns: []` and exact scope/hash match. **Only after that PASS may a wrap-up recommendation be re-issued, via a fresh Hwao receipt.** A second FAIL returns here for re-adjudication; no fix-review ping-pong without Hwao between rounds.

### 4.5 Stop rules and rollback

Parent §11 stops all apply, plus: out-of-five-path need → STOP; RED unachievable → STOP; new-dependency need → STOP; recount/hash drift at preflight or any checkpoint → STOP. On STOP: freeze, write a stop receipt, report via Tori. Rollback unchanged from parent §12 — worktree removal only after lossless preservation into phase3; never stash/reset the primary.

## 5. Execution gate — a NEW explicit user line is required

Nothing in this receipt executes or pre-authorizes execution. RF-1 activates **only** upon a new explicit user approval line in chat, relayed by Tori, that names the review-fix. **Generic continuation phrases ("go ahead", "continue", "next step") are INSUFFICIENT for this gate** — an outstanding recommendation (wrap-up) was just withdrawn, so an unnamed continuation would be ambiguous between wrap-up, keep-frozen, and fix. The line must unambiguously reference the review-fix packet.

## 6. Exact approval wording Tori should request

Tori presents: "Independent review FAILED the frozen Surveys unit on five blockers (search-bypass in PlotB, untruthful empty-state copy, SVG role conflict, disclosure aria-controls/nesting, defect-enforcing smoke test). Hwao withdrew the wrap-up recommendation and defined a smallest fix packet: same frozen worktree, same five files, failing-test-first fixes, then a regenerated patch and a fresh independent review. Still no commit, push, merge, network, or runtime. To proceed, please reply exactly:"

> **`UNFREEZE G3 SURVEYS REVIEW-FIX R1-R5 20260722`**

- That verbatim line (or an unambiguous equivalent naming "review-fix" / "R1-R5") activates RF-1 as defined in §4, one-shot.
- Alternatives the user may give instead: **`KEEP FROZEN`** (state persists for direct inspection) or **`DISCARD WITH PRESERVATION`** (parent §12 flow: preserve patch+receipt into phase3, then worktree removal — itself requiring its own confirmation at execution).

## 7. Gate ledger after this receipt

G1 Completed · G2 Completed · **G3 Surveys unit: independent review FAILED; freeze maintained; wrap-up recommendation withdrawn; RF-1 defined and awaiting the §6 user line** · G3 all other units Held · G4a/G4b/G4c Held separately (`HWAO_PHASE4_DISPOSITION_PACKETS_RATIFIED_20260722`) · G5 Closed · G6 Held · G7 Closed — no cockpit/status write accompanies this receipt.

## 8. Safety ledger for this adjudication pass

Source/test edits 0 · git/index writes 0 · worktree writes 0 · stage/commit/PR/push/merge 0 · stash/reset 0 · file moves/deletes 0 · DB/SQL 0 · runtime/deploy/cockpit/publication 0 · network/fetch 0 · `.env*` content access 0 · fixes executed 0 · **files written 1 (this receipt)**.

Methods: read-only reads of `.hermes.md`, the reviewer verdict JSON, the two prior Surveys G3 records; `shasum -a 256` on the preserved `/tmp` artifact; `ls`/`date`. The frozen worktree itself was not touched in this pass.

---

`HWAO_G3_SURVEYS_REVIEW_FAIL_DECIDED_20260722`
