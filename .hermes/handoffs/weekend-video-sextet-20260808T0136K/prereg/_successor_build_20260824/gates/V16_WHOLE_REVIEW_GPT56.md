# V16 WHOLE-DOCUMENT REFEREE REPORT — GPT56

Verdict: **NOT CLEAR**. The pinned V16 bytes match, the R15 Part-1 §6 body landed byte-for-byte, the new unblinding-receipt contract closes my R15 schema-list blocker at document-contract level, and the core `0.85` / `1,000` / `962` / decision-threshold values agree with the pinned v9 code. The whole-document fold nevertheless exposes four blocking seams: §7's asserted execution-gate count does not close over its own table; the required §4 conforming edit was not applied although §10 says it was; §2.7 retains a dangling reason-(d) threshold contract with two different producer slots; and the folded §6.3 deleted the operative whole-document change/void clauses while Row P still cites the deleted V15 text. The document-wide Clause-10/outcome registry is consequently not closed.

## Digest-first identity check

- Subject: `../PREREG_SUCCESSOR_DRAFT_V16_20260827.md`.
- Brief-pinned sha256: `1b9b9486736bf734c8cb4ac8cedf54870fd179587e3e1455273ec4724132a0da`.
- Independently computed before opening: `1b9b9486736bf734c8cb4ac8cedf54870fd179587e3e1455273ec4724132a0da`.
- Result: **MATCH**.
- Independently computed R15 source sha256: `d2c388a451d076f880c879e888ee7901331adc62142245a285b8ff932d67f01a` — **MATCH** to V16 lines 3–4 and the fold record.
- Exact extraction check: R14 Part 1, R15 Part 1, and V16 `## §6 Conduct` through the line before `### The fold record` are byte-identical (23,774 bytes; independently normalized extraction sha256 `7472acd61f0661f13102bdeb6c165f214777a716ade08f8a8b66f4a0b05d368f`).
- Pinned code shas independently match V16 §0: `successor_ref_v9.py` = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` = `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.

## Numbered findings

### 1. HIGH / BLOCKING — §7's “7 class-E slots” assertion fails count closure against the table as applied

- **Section / lines:** §7 lines 628–666, especially line 636 and table lines 655–666.
- **Evidence:** I parsed the tables directly. Class P contains 14 data rows, agreeing with line 636. Under the `Class E — execution gates` heading, however, the table contains **eight** data rows: BS-6, BS-2f, BS-8f, BS-5f, BS-L, Unblinding receipt, BS-7f, and BS-V. Line 636 says “There are 7 class-E slots” and immediately asserts that lint makes the prose count equal the parsed table count. It does not. BS-2f itself is correctly in Class E; the brief's requested BS-2f check holds. The defect is the unseparated unblinding-receipt row under the Class-E slot table.
- **Why it fails:** R15 Part 2 required seven class-E slots and also required the unblinding receipt to be added as a named post-unblinding artifact. V16 applied the latter by making the artifact an eighth row in the class-E slot table. A reader/parser has no textual basis to exclude that row from the table count: the column is literally named `slot`, and no separator marks the row as non-slot. This reproduces the exact §7 count seam the fold claims closed.
- **Smallest sufficient repair:** Either (a) move the unblinding receipt out of the class-E slot table into a separately headed post-unblinding-artifact table/list and retain the count seven, or (b) expressly classify it as the eighth Class-E row and change the prose/lint contract to eight. Do not leave a row under the table while asking a parser not to count it.

### 2. HIGH / BLOCKING — the required §4 conforming edit was not applied, but §10 says it was

- **Section / lines:** §4 lines 412–452; §10 line 736; fold brief Part 2 item 3; R15 Part 2 item 3 (source lines 107–109).
- **Evidence:** The V15→V16 diff changes §2.5, §2.7, §5, §6, §7, §10 and adds §11; it contains **no change in §4**. R15 Part 2 item 3 explicitly names “§2.7(4) and §4 Stage C exclusions” and requires §4 to state that BS-5f certifies only the locked pre-attrition BS-2f mask, post-unblinding removal terminates `INCONCLUSIVE-BY-CALIBRATION`, and no post-attrition Stage-C reevaluation occurs. V16 §4 still ends Stage C at the pre-unblinding FAIL rule (lines 448–452) and contains none of those final-mask/post-attrition statements. Nevertheless §10 line 736 says the conforming edits were applied to “§2.5, §2.7, §4, §5, and §7.”
- **Why it fails:** This is exactly the review brief's “check edits as applied” seam. The missing §4 text leaves the power-gate section appearing to certify the accepted mask without stating its restricted pre-attrition scope; readers must leave §4 and infer the restriction from §2.7/§5/§6. The repair trace then falsely records an edit that did not land.
- **Smallest sufficient repair:** Apply R15 Part 2 item 3 literally in §4: state BS-5f's pre-attrition-only scope, the one-removal calibration-inconclusive consequence, and the prohibition on post-attrition Stage-C reevaluation. Keep the existing thresholds and P5 seating unchanged. Then retain the §10 claim; otherwise remove §4 from the applied-edit claim and mark the seam open.

### 3. HIGH / BLOCKING — §2.7's confidence threshold is left attached to nonexistent reason (d) and assigned to two different pre-image slots

- **Section / lines:** §2.7 lines 335–375, especially 358–372; §7 line 642.
- **Evidence:** The applied edit narrows the pre-lock exclusion list to reasons (a) and (b) at lines 335–342 and defers confidence to Row P post-unblinding. But paragraph 5 still begins “Reason (d)” (line 358), and paragraph 7 still says “The thresholds in (d)” are pinned in **BS-3** before any image byte (lines 371–372). In the same section, paragraph 6 assigns “The numeric confidence threshold” to **BS-2a** (lines 365–370), and §7's BS-2a row repeats that assignment (line 642). The pinned v9 `SLOT_SCHEMA` confirms BS-3 currently contains only `weights_sha256`, `tau`, and `antisymmetry_receipt` (code lines 185–205); it has no confidence-threshold field. BS-2a is presently absent from that schema and explicitly unresolved.
- **Why it fails:** The conforming edit removed reason (d) from the live pre-lock reason enumeration but did not conform the paragraphs that define and seat its threshold. A future operator is told both BS-3 and BS-2a own the same threshold. The value is intentionally unresolved, but its **phase and producer slot** must still be single-valued before data. This fails the requested value/phase/failure-effect audit even before a numeric value exists.
- **Smallest sufficient repair:** Rewrite paragraphs 5 and 7 around Row P state (7), not nonexistent reason (d), and name exactly one producer slot. The surrounding design consistently makes the confidence value/authority part of the refused BS-2a design, frozen before BS-6 and applied only at P8; if that is intended, delete the BS-3 assignment and conform §7. Keep below-threshold → `EXCLUDED-BY-CONFIDENCE` → any removal → `INCONCLUSIVE-BY-CALIBRATION` explicit.

### 4. HIGH / BLOCKING — the fold deleted the operative whole-document void/change clauses, leaving Clause 10 and Row P dependent on superseded V15 text

- **Section / lines:** §6.3 lines 568–576; Row P line 532; Clause 10 line 562; §5 lines 456–473.
- **Evidence:** V15 contained full bodies for “No strata,” calibration/admissibility, the post-first-real-χ void rule, one-change-per-iteration, no-claim-stronger-than-check, custody, and blind-double scope. Folded V16 §6.3 contains only seven bare bullet titles with no operative text. Row P nevertheless says its consequences are fixed by “V15 lines 570–573 which void any post-first-real-χ change to a decision threshold” (line 532). V16 supersedes V15; the cited rule is not present in V16. The only remaining threshold-change void sentence is §2.7 line 372, itself attached to the dangling reason-(d) contract in Finding 3, and it does not govern every rule/algorithm/schema as V15's deleted clause did.
- **Why it fails:** A clause title is not a clause. Whole-document Clause 10 cannot terminate a forbidden post-data change branch through a superseded document whose operative text was deleted from the folded promise. This is also an overclaim: line 532 says the consequences “are fixed” by text that V16 no longer carries. Separately, §5 says the production path emits “exactly one of four outcomes” (line 464), but its bullets name REPRODUCED, REJECTED, INCONCLUSIVE, INCONCLUSIVE-BY-POWER and INCONCLUSIVE-BY-CALIBRATION, while Row P additionally names four `INCONCLUSIVE-BY-{MISSING-RECORD,DUPLICATE,ORPHAN,MALFORMED}` run-level refusals. Without a canonical whole-document outcome/refusal registry, the reverse Clause-10 audit cannot reconcile the asserted exhaustive set.
- **Smallest sufficient repair:** Restore complete, V16-conformed bodies under §6.3, including the universal post-first-real-χ change/void rule and its exemptions, rather than citing V15. Add one canonical outcome/refusal registry that distinguishes numeric verdicts, pre-statistic inconclusive halts, accounting refusals, per-attempt exclusions, and VOID; make §5's count and guard wording agree with it. Then rerun Clause 10 forward (every branch → exactly one category) and backward (every category → a reachable antecedent) across §§0–11, not only Rows A–S.

## Whole-document Clause 10 audit — both directions

### Forward: branch → stated outcome

The principal decision partitions that held are: Branch A/B at BS-1; Row J's `<0.85` versus all-bins `>=0.85`; exact `N_TRIALS = 1,000`; Stage-C `<962`/self-verification FAIL versus the complementary PASS; Row P's ordered eight record states; and zero versus one-or-more post-unblinding removals. Their local inequalities are single-valued.

The whole-document forward audit does **not** clear because Findings 3–4 leave two governing branches without one current V16 contract: the confidence threshold has two producer slots and a dangling reason identifier, and post-first-real-χ rule/schema/threshold changes depend on deleted V15 prose rather than a V16 consequence. §5's asserted exhaustive outcome count also does not close over Row P.

### Reverse: stated outcome → reachable antecedent

The main antecedents are present: low calibration bound → pre-lock calibration inconclusive; Stage-C failure → power inconclusive; Row-P absence/nonfinite/low confidence → removal → calibration inconclusive; the four accounting defects → their named refusals; clean adequacy plus numeric regions → the three numeric verdicts. But V16 has no single authoritative set that tells a production guard whether the four accounting labels are members of generic `INCONCLUSIVE`, unconditional refusals outside the four-outcome claim, or separate verdict outcomes. The reverse audit therefore cannot validate the document's “exactly four” exhaustiveness assertion.

## Threshold sweep — value, phase, failure effect

### Values/phases/effects that held against pinned v9

- `A_LONGO = +0.0408`, published sign `−0.0408`, `SIGMA_PUB = 0.011` — document and code lines 73–75 agree.
- Production `N_PERM = 100,000` — §3/§5 and code line 76 agree; p is plus-one and one-sided as stated.
- `P_REPRODUCED = 0.001`, strict `<`; `P_REJECT_MIN = 0.05`, strict `>`; equality falls to INCONCLUSIVE — §5 and code lines 79–80 / 1579–1584 agree.
- `A_FLOOR = 0.85`, failure `<`, equality PASS; phase Row J/P5 after BS-8f and before Stage C/BS-5f/BS-L/unblinding; failure `INCONCLUSIVE-BY-CALIBRATION` — prose and code lines 81 / 1492–1496 agree at contract level. Implementation of the moved Row-J/lock path remains unresolved.
- `N_TRIALS = 1,000`, `CP_PASS_X = 962`; 961 FAIL, 962 PASS subject to no `refuted`/`nonconservative` — §4/Row J and code lines 77–78 / 1275–1277 agree.
- `RETENTION_LB = 0.8572`, `L_PLAN_MARGIN = 1.2`, `NEQ_MIN = 100,000`, `N_EXACT = 16` — §§2.3/2.6 and code lines 82, 84–86 agree.
- Detection floor multiplier `3.09`; three-sigma reproduction/rejection bands — §5 and code lines 83 / 1577–1584 agree.
- Calibration-path spread `0.03`: code line 1496 fixes scalar at `<=0.03`, profile otherwise. V16 no longer states this threshold because the §6.3 calibration body was deleted; that absence is part of Finding 4, not a competing value.
- One-or-more post-unblinding removals versus zero: effect is calibration inconclusive versus continued adequacy; no Stage-C rerun. This partition is locally consistent in §§2.7, 5 and 6.
- One-use P7 opening: replay is refused/void; the new §11 schema item correctly binds identity and replay state, but implementation remains unresolved.

### Threshold defect

- Confidence: numeric value intentionally absent while BS-2a is refused, which is acceptable only because BS-2a blocks BS-6. Its application effect is stated, but its producer/phase contract is contradictory between BS-3 and BS-2a and references deleted reason (d): Finding 3.

The §2.2 galaxy-cut values are present in the document, but the named predecessor source files were not present in the authorized build tree I inspected, and the pinned v9 code does not contain those SQL predicates. I therefore do not restate their provenance as independently verified; they remain under Testimony below rather than being silently credited.

## Fold-record accuracy

- **Held:** the folded filename and sha; R14/R15/V16 Part-1 byte identity; R12 GPT56 CLEAR; R13 GPT56 CLEAR; CODEX's R13 concurrence on the prose partition while separately blocking the executable carrier; both R14 reports crediting route (b) at document-contract level; R15 report verdicts and report-file mtimes (`CODEX 21:52:33 KST`, `GPT56 21:53:46 KST`); the R15 GPT56 schema blocker; and §11's literal adoption of its minimum repair.
- **Held:** BS-2f is in Class E, not Class P.
- **Not accurate:** §10 line 736 says the §4 conforming edit was applied; it was not (Finding 2).
- **Not closed as claimed:** the §7 count/DESIGN seam is not closed because the applied class-E table has eight rows under a prose count of seven (Finding 1).
- **Testimony only:** the underlying raw Duho instruction at 21:48 KST and dispatch-before-verdict event were not available as an independent instruction/dispatch receipt in the reviewed artifact set. `BRIEF_V16_FOLD_BANNER.md` states them, and report mtimes are later, but I do not elevate that supplied chronology to independently verified authority.
- **Testimony only:** “V16 lints clean.” No `prereg_lint.py` was present in the authorized build tree found by filename search, so I could not reproduce the lint run. My independent table parse contradicts the embedded count-lint assertion even though the specific BS-2f class finding was indeed a false positive.

## Overclaim check

V16 prominently says it is a draft, states nothing is in force, keeps BS-2a refused, blocks Rows C2/E, BS-6 and the first image byte, marks `verify_lock()` and the unblinding mechanisms unimplemented, and discloses the Stage-P code conflict. Those limitations are sufficiently prominent and held under attack.

The overclaims that do not hold are narrower but material: §10 claims an unapplied §4 edit; §7 claims parsed-count lint closure that fails direct parsing; Row P claims a deleted V15 rule fixes V16 consequences; and §5 claims an exhaustive four-outcome surface that does not close over its own labels and Row P's named refusals.

## Failed attacks / credited repairs

1. Tried to reopen my R15 unblinding-receipt schema blocker: §11 line 748 now enumerates the BS-L identity/checkpoint, complete extending chain segment, terminal unsealing events, final checkpoint, destination, ceremony identity and replay state; binds schema bytes into the implementation/schema digest; and requires exact authentication. This closes the document-contract list defect while honestly leaving implementation unresolved.
2. Tried to find drift in the folded §6 body: exact extraction was byte-identical R14 → R15 → V16.
3. Tried the core equality boundaries: `a_LB_b == 0.85`, 962/1,000, p == 0.001, and p == 0.05 are consistently seated by the strict/complementary inequalities.
4. Tried to put BS-2f back in Class P: the live §7 table correctly seats it in Class E and labels it value-only.
5. Tried to route a Stage-C/calibration FAIL through BS-L: the prose PASS-only chain blocks it; the missing implementation is disclosed rather than claimed delivered.
6. Tried to find an undisclosed claim that the first image byte is authorized: the banner and §7 consistently block it.

## Testimony / limits

- BS-2a's three-seat refusal, findings 1/2/2b/3 status, predecessor counts, real-geometry measurements, Stage-P receipt values, source-citation verification, and archive seal state were not independently re-executed here.
- The future Row-J guard, `verify_lock()`, new slot schemas, `verify_unblinding_receipt()`, `verify_archive_seal()`, mediator, C2 worker, replay guard, adequacy verifier, and fixtures do not exist in pinned v9. AST inspection found zero definitions for `verify_lock`, `verify_unblinding_receipt`, `verify_archive_seal`, and `recompute_acceptance_ledger`; I credit them only as required unresolved work.
- The raw 21:48 principal instruction and dispatch event were not independently available; only the later briefs/fold text and report mtimes were available.
- The named predecessor cut-threshold source files and the claimed corrected `prereg_lint.py` were not found in the authorized build tree. Their claims remain unverified, not disproved.
- I did not read `/Users/duhokim/NebulaMindData/`, fetch anything, inspect secrets, or touch χ-bearing material.

## Evidence ledger and custody

Content read included: `BRIEF_V16_WHOLE_REVIEW.md`; the complete V16 subject; V15 through the full V15→V16 diff; `SECTION6_DRAFT_AGY_R15.md`; R12–R15 GPT56/CODEX referee reports needed to check the fold record; `BRIEF_FOLD_V16.md`; `BRIEF_V16_FOLD_BANNER.md`; `BRIEF_V16_CLOSE_BLOCKER.md`; and the pinned v9 code regions for constants, `SLOT_SCHEMA`, Stage C, calibration, decisions and the production runner.

Independent checks included: subject/source/code sha256; exact section extraction and byte comparison; direct §7 table parsing; full applied diff inspection; AST definition/schema search; threshold-token sweep; pinned-code value/boundary comparison; Row-P full-line extraction; and forward/reverse branch review across §§0–11.

No source, code, preregistration draft, data artifact, gate brief, or prior report was modified. This report is the sole intended write by this seat.

**NOT CLEAR**