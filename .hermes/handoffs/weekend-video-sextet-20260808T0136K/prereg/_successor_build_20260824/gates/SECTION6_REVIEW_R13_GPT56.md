# §6 R13 REFEREE REPORT — GPT56

Subject: `SECTION6_DRAFT_AGY_R13.md`
Brief: `BRIEF_SECTION6_REVIEW_R13.md`

## Verdict

No blocking finding. R13 moves the frozen calibration-floor decision onto Row J after BS-8f exists and before Stage C, BS-5f, BS-L, or unblinding; gives its failure the required `INCONCLUSIVE-BY-CALIBRATION` pre-unblinding halt; binds the complementary PASS through BS-5f and `verify_lock()`; and leaves Row P's distinct post-unblinding removal/applicability branch intact. The corrected lines-1275–1277 attribution is accurate. The bidirectional Clause 10 sweep and the value/phase/failure-effect threshold sweep found no new orphan, overlap, or executable gap.

## Digest verification — performed first

- Pinned SHA-256 in `runner_s6r13_round.log` line 5: `385228543d178052ed27f62bd8df90c11168628a7120bd9127c707ca54eec1da`.
- Independently computed SHA-256 of `SECTION6_DRAFT_AGY_R13.md`: `385228543d178052ed27f62bd8df90c11168628a7120bd9127c707ca54eec1da`.
- Result: **MATCH**. The bytes reviewed are the pinned bytes.

## Numbered findings

None.

## Required repair checks

### 1. Calibration decision executes before BS-L

- The phase line places BS-8f at P4, BS-5f at P5, BS-L at P6, and unblinding at P7 (draft line 31).
- Row I emits BS-8f at P4 (line 46). Thus the per-bin `a_LB_b` aggregate exists before Row J consumes it.
- Row J (line 47) evaluates any `a_LB_b < 0.85` before Stage C, emits `INCONCLUSIVE-BY-CALIBRATION`, and halts pre-unblinding. Only the complementary calibration PASS proceeds to protocol verification, Stage C, and BS-5f.
- BS-5f binds the calibration PASS. Clause 3(c) (line 67) requires `verify_lock()` to check BS-5f's complementary calibration PASS and Stage-C PASS; verifier failure refuses both unblinding and the verdict path. Row O additionally requires a passing `verify_lock()` before unsealing.
- This matches V15 lines 566–567: any per-bin lower bound below `0.85` is `INCONCLUSIVE-BY-CALIBRATION, pre-unblinding halt`.

### 2. Row P's distinct applicability branch survives

Row P (line 53) no longer re-evaluates the calibration-floor failure after unblinding. It binds the already-verified pre-unblinding PASS. Its separate post-unblinding applicability rule remains reachable and unchanged in substance: absent, non-finite, or low-confidence terminal states cause removal; any removal immediately emits `INCONCLUSIVE-BY-CALIBRATION`; no Stage-C rerun occurs. The same rule is conformed in Part 2 item 4, Part 3 C1/C2, and residual risk R3.

### 3. Corrected source citation

The cited source was read directly:

- `successor_ref_v9.py` lines 1275–1276: nonempty `refuted` or `nonconservative` returns `(succ, False, audit)`.
- Line 1277: otherwise returns `succ >= CP_PASS_X` only when `n_trials == N_TRIALS`, and `None` when the count differs.
- The draft now correctly attributes the no-deviation legality rule to Row J's pre-run verification and uses lines 1275–1277 only for the self-verification/count-return partition (Part 5 item 16, line 145).

## Clause 10 — both directions

I checked both (a) every branch has exactly one stated consequence and (b) every stated consequence has a structural witness. The currently refused BS-2a intentionally blocks execution before BS-6; conditional downstream reachability means “reachable once the named prerequisite is filled,” not that the present blocked draft can execute.

| Row | Forward termination | Reverse reachability | Result |
|---|---|---|---|
| A | Conforming provisioning emits BS-2k; each listed custody/read breach voids. | Provisioning and each listed breach witness the outcomes. | Complete |
| B | Authorized touches log one event; premature D touch is refused and logged; delivery/log failures void. | Authorized, refused, and breach paths each have witnesses. | Complete |
| C | Conforming production emits the sealed completion receipt; export/view breaches void. | Normal production and each listed breach are constructible. | Complete |
| C2 | With a replacement BS-2a, conforming work emits projections and exact-parent completion; classifier/schema/attestation breaches void. | Present BS-2a refusal blocks execution; all post-repair outcomes remain structurally reachable. | Complete, blocked |
| D | Post-C2 inference emits sealed measurements; external χ emission voids. | Normal and breach witnesses exist, conditional on C2. | Complete, blocked |
| E | One verified projection per parent yields ledger and realised partition; out-of-schema read voids. | Normal and breach witnesses exist, conditional on replacement BS-2a. | Complete, blocked |
| F | Conforming χ-free inputs emit boundaries/allocation; χ-bearing input voids. | Both paths have witnesses. | Complete |
| G | Allocated-sample interface use emits co-signatures; role/view/export/log violations void. | Normal use and each violation are constructible. | Complete |
| H | Conforming ingestion emits the sealed label-set receipt; alternate persistence/schema/export paths void. | Both normal and listed breach paths are reachable. | Complete |
| I | Any allocated missing/non-finite output fails and aborts before BS-8f; all usable finite outputs permit BS-8f; failure to abort or forbidden export/schema behavior voids. | Missing/non-finite and all-finite samples witness the ordinary branches; listed violations witness VOID. | Complete |
| J | Calibration FAIL halts `INCONCLUSIVE-BY-CALIBRATION`; calibration PASS advances to protocol verification. Protocol/count/digest deviation terminates VOID. Lawful Stage-C FAIL halts `INCONCLUSIVE-BY-POWER`; only both PASSes emit BS-5f. | Low calibration bound, protocol deviation, `<962`, self-verification failure, and clean `>=962` runs witness all stated consequences. | Complete |
| K | Proper custody emits nothing; a pre-unblinding holder read voids. | No-touch custody and forbidden read witness both states. | Complete |
| L | Authorized signatures emit their named artifacts; early access/opening or wrong-body signing voids. | Every ceremony and breach path has a witness. | Complete |
| M | Authorized non-χ receipt work emits assigned receipts; pre-unblinding χ access voids. | Normal and breach paths exist. | Complete |
| N | Conforming ceremony emits BS-L; incomplete, unsigned, or mis-signed lock voids. | Both normal and malformed paths exist. | Complete |
| O | Verified lock plus fresh canonical authorization emits the unblinding receipt; early, replayed, or out-of-destination use voids. | Authorized opening and every listed breach witness the outcomes. | Complete |
| P | Exact-parent precedence gives each attempt one terminal state. Missing/duplicate/orphan/malformed states refuse under one named outcome. Absence/non-finiteness/low confidence remove; any removal yields calibration inconclusiveness. No removal binds the already-verified calibration and Stage-C PASSes and emits the adequacy chain. | Every record-state label is constructible; any removal witnesses the applicability failure; a no-removal partition witnesses the successful adequacy/verdict path. Silent loss, retry, or premature execution witness VOID. | Complete |
| Q | Metadata-only checking emits the seal-state receipt; content read voids. | Both paths have witnesses. | Complete |
| R | Any otherwise-unlisted pre-unblinding χ access voids; no access emits nothing. | The default breach supplies the VOID witness. | Complete |
| S | BS-V-authorized P9 export publishes; earlier export voids. | Authorized and premature exports witness both outcomes. | Complete |

The moved decision did not orphan a later dependency: Row P now consumes the locked PASS rather than the raw low-bound decision, while its removal/applicability decision remains independent and reachable. In the reverse direction, both calibration outcomes retain witnesses: low bound before Stage C and post-unblinding removal, respectively.

## Three-part threshold sweep: value, phase, failure effect

| Threshold/gate | Value | Binding phase | Failure effect | Result |
|---|---|---|---|---|
| Calibration accuracy floor | Any per-bin `a_LB_b < 0.85` fails; complement is every bin `>= 0.85`. Source: V15 566–567 and `A_FLOOR = 0.85` at code line 81. | Row J after BS-8f/P4 and before Stage C/BS-5f/P5, BS-L/P6, and unblinding/P7. | `INCONCLUSIVE-BY-CALIBRATION`, immediate pre-unblinding halt. PASS is bound into BS-5f and checked by `verify_lock()`. | Complete |
| Stage-C trial count/protocol | Exactly `N_TRIALS = 1_000` (code line 77). | Row J after calibration PASS but before Stage-C execution or BS-5f issuance. | Any count/protocol/frozen-implementation deviation is VOID and cannot issue acceptable BS-5f. | Complete |
| Stage-C power count | FAIL below `CP_PASS_X = 962`; complement PASS at `>= 962`, subject to self-verification (code lines 78 and 1275–1277). | Row J during locked Stage C, pre-BS-5f and pre-unblinding. | `<962` emits `INCONCLUSIVE-BY-POWER` and halts; clean `>=962` is the sole count-side PASS route to BS-5f. | Complete |
| Stage-C self-verification | Any nonempty `refuted` or `nonconservative`; complement is both empty. | Row J at locked Stage-C return, before BS-5f. | Failure emits `INCONCLUSIVE-BY-POWER` regardless of success count; clean complement proceeds to the 962 cut. | Complete |
| Calibration path spread | `max_b |â_b − â| <= 0.03` selects scalar; spread failure selects profile (V15 566–567; code 1492–1496). | `adjudicate_path()` after BS-8f and before the Stage-C path consumes scalar/profile calibration inputs. | No halt: failure of spread alone deterministically selects PROFILE; it does not weaken the separate `0.85` halt. The frozen implementation/protocol digest remains mandatory in Row J. | Complete |
| Post-unblinding attrition/applicability | Zero removals passes applicability; any one or more removals fails. | Row P/P8, after exact-parent terminal-state assignment and before any statistic/verdict. | `INCONCLUSIVE-BY-CALIBRATION`; no Stage-C rerun. | Complete |
| Confidence exclusion | Numeric value and authority must be frozen in replacement BS-2a before BS-6; BS-2a is presently REFUSED/UNFILLED. Application is the already-declared below-threshold test. | Value/design at P0 before first image byte; application at Row P/P8 after unblinding. | Below threshold yields `EXCLUDED-BY-CONFIDENCE`; that removal immediately yields `INCONCLUSIVE-BY-CALIBRATION`. No executable gap exists while the value is absent because BS-2a blocks BS-6. | Complete but intentionally blocked under the brief's named unresolved BS-2a work |
| Allocated-sample output usability | Every allocated object must have a usable finite output. | Row I before BS-8f. | Any missing/non-finite allocated output fails and aborts before BS-8f; failure to abort voids. | Complete |

No competing values or phase/effect contradictions were found for `0.85`, `1,000`, `962`, the zero-versus-any-removal cut, or the deferred confidence cut. The `208,405` archive number is a count, not a decision threshold; it is consistent at draft lines 17 and 87 but remains testimony because the prohibited data tree was not inspected.

## Failed attacks

- I tried to continue from `a_LB_b < 0.85` into Stage C, BS-5f, BS-L, or unblinding. Row J's halt plus BS-5f/`verify_lock()` PASS binding closes every route.
- I tried to construct a Row-P calibration-floor FAIL after the branch was removed. A verified BS-L requires the complementary PASS, so such a Row-P branch would be unreachable and is correctly absent.
- I tried to make the removal/applicability branch disappear with the adjacent low-bound deletion. It remains explicit in Row P and all conforming prose.
- I tried to orphan calibration PASS. It is emitted/bound by BS-5f, checked by `verify_lock()`, inherited by Row P, and recorded in the adequacy receipt.
- I tried the equality boundaries: `a_LB_b = 0.85` is PASS, 962 of 1,000 is Stage-C count PASS, and 961 is FAIL, matching the frozen source.
- I tried to revive the R11 Stage-C FAIL branch in Row P. BS-L excludes Stage-C FAIL, and Row P binds rather than re-runs the locked PASS.
- I tried to recover the R12 citation error. Lines 1275–1277 are now described accurately, and Row J—not those code lines—is identified as the no-deviation legality rule.
- I diffed R12→R13. The substantive changes are confined to Row J, Row P, `verify_lock()`, and their conforming status/Part 2/Part 3/Part 5 prose; no adjacent terminal-state or void consequence was deleted.

## Testimony and limits

- BS-2a's `REFUSED / UNFILLED` status, the consequent C2/E/BS-6 block, and the unresolved channel-design findings are stated by the draft and brief. I did not independently execute external gates.
- The predecessor archive count of 208,405 remains testimony. I did not read `/Users/duhokim/NebulaMindData/`.
- I reviewed the prose, its exact R12→R13 delta, and the named local frozen-source lines. I did not execute Stage C, inspect χ-bearing data, or fetch anything.

## Evidence ledger

Content read:

- `BRIEF_SECTION6_REVIEW_R13.md`
- `runner_s6r13_round.log`
- `SECTION6_DRAFT_AGY_R13.md`
- `BRIEF_DRAFT_SECTION6_R13.md`
- `SECTION6_DRAFT_AGY_R12.md` through an exact no-index R12→R13 diff
- `SECTION6_REVIEW_R12_CODEX.md`
- `SECTION6_REVIEW_R12_GPT56.md`
- `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md`, including lines 306–342, 421–425, 557–573, and 603–628
- `../ref/successor_ref_v9.py`, including lines 72–84, 1268–1277, and 1446–1496

Checks run:

- `shasum -a 256 SECTION6_DRAFT_AGY_R13.md`
- `git diff --no-index -- SECTION6_DRAFT_AGY_R12.md SECTION6_DRAFT_AGY_R13.md`
- Whole-document comparator/threshold and branch-token searches
- Exact extraction of full Rows J and P
- Independent boundary re-derivation from `N_TRIALS`, `CP_PASS_X`, `A_FLOOR`, `adjudicate_path()`, and the lines-1275–1277 return partition

No content under `/Users/duhokim/NebulaMindData/` was read, and no network fetch was performed.

**CLEAR**