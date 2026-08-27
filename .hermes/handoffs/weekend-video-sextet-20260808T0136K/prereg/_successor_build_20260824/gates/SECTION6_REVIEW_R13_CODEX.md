# SECTION 6 REVIEW R13 — CODEX

## Verdict

R13 places the calibration lower-bound decision at the correct nominal phase and gives its failure the correct pre-unblinding consequence. It does not, however, make that repair executable or receiptable: the pinned `SLOT_SCHEMA` still gives BS-5f only the Stage-C fields, no pinned `verify_lock()` exists in the frozen implementation, and Part 2's exhaustive conforming/code-side edit list does not add either mechanism. The draft therefore describes an earlier check but does not yet make BS-L/unblinding mechanically depend on an authenticated complementary calibration PASS.

## Digest verification — performed before opening the subject

- Pinned digest in `runner_s6r13_round.log` line 5: `385228543d178052ed27f62bd8df90c11168628a7120bd9127c707ca54eec1da`.
- Independently computed SHA-256 before opening `SECTION6_DRAFT_AGY_R13.md`: `385228543d178052ed27f62bd8df90c11168628a7120bd9127c707ca54eec1da`.
- Result: **MATCH**. The bytes reviewed are the pinned bytes.

## Numbered findings

1. **BLOCKING — Row J / Clause 3(c) / permitted aggregate surface / Part 2 item 7: the calibration halt and complementary PASS are prose assertions with no conforming executable or receipt-schema repair.**
   - **Evidence:** Row J (line 47) now says it evaluates `a_LB_b < 0.85` before Stage C, that BS-5f binds the complementary PASS, and that only the PASS branches reach BS-5f. Clause 3(c) (line 67) says `verify_lock()` checks “BS-5f's complementary calibration PASS.” But the draft's exhaustive permitted aggregate surface (line 17) still defines BS-5f only as the “Stage-C receipt (PASS/FAIL and the permitted Stage-C scalar output).” The currently pinned `../ref/successor_ref_v9.py` `SLOT_SCHEMA` at lines 185–193 defines BS-5f as exactly `("successes", "n_trials", "passed", "mask_digest")`; it has no calibration result, BS-8f digest, minimum `a_LB_b`, or other authenticated field from which BS-5f can bind the claimed PASS. A content search of the pinned implementation found no `verify_lock()` definition. Finally, Part 2 says it lists every conforming edit required by the replacement (line 5), but its only code-side item (line 109) adds Row B/C2 mechanisms and omits the new Row-J calibration guard, the BS-5f binding/schema change, and `verify_lock()` enforcement.
   - **Why it fails:** The review brief requires checking that the decision “actually execute[s]” before BS-L and that `verify_lock()` genuinely cannot pass without the calibration PASS, not merely that the prose places it earlier. Under the bytes and conforming edits R13 names, the authenticated BS-5f `passed` bit remains a Stage-C result. Neither its schema nor an implemented lock verifier proves `min(a_LB_b) >= 0.85`. Clause 3(c)'s assertion cannot authenticate a field that the closed schema does not carry, and Part 2 supplies no code change that instead re-evaluates the BS-8f record. Consequently, a Stage-C-passing BS-5f has no specified machine-verifiable calibration-PASS binding, so the intended guard from BS-8f → BS-5f → BS-L is not yet a receiptable dependency.
   - **Smallest sufficient repair:** Add one explicit conforming code/schema route to Part 2 and to the closed permitted surface. Either (a) extend authenticated BS-5f to bind the exact BS-8f digest plus a canonical calibration-PASS field/minimum, with Row J refusing BS-5f on `min(a_LB_b) < 0.85`, or (b) keep BS-5f's Stage-C schema unchanged but require the pinned `verify_lock()` to resolve the BS-L-bound BS-8f bytes and independently recompute `all(a_LB_b >= 0.85)`. In either route, pin the implementation/schema digest, add a negative fixture showing that low-bound BS-8f cannot produce a passing lock, and list the edit in Part 2's atomic code-side work.

## Clause 10 — both directions

### Forward: every branch must terminate once

- **Row J calibration:** `min(a_LB_b) < 0.85` is assigned `INCONCLUSIVE-BY-CALIBRATION` and a pre-unblinding halt; its mathematical complement is all per-bin lower bounds `>= 0.85`. The prose partition is single-valued and correctly seated at P5 after BS-8f/P4 and before Stage C, BS-5f, BS-L/P6, and unblinding/P7.
- **Row J protocol:** `N_TRIALS != 1_000` or an implementation/protocol-digest deviation is checked before execution/BS-5f and terminates `VOID` through Row J's void column.
- **Row J Stage C:** with calibration and protocol verified, `(successes < 962) OR refuted OR nonconservative` emits `INCONCLUSIVE-BY-POWER` and halts. Its complement—`successes >= 962`, no `refuted`, and no `nonconservative`—is PASS and the sole lawful route to BS-5f.
- **Row P:** the eight-state exact-parent precedence remains intact. Missing, duplicate, extra, and malformed states have one named unconditional `INCONCLUSIVE-BY-*` refusal each. Absence, non-finiteness, or low confidence causes removal; any one removal then emits `INCONCLUSIVE-BY-CALIBRATION` with no Stage-C rerun. The accepted-finite/no-removal path binds the already-verified pre-unblinding PASS rather than re-evaluating the low-bound threshold.
- **Other rows:** their normal emissions/refusals and listed void conditions remain as in R12; I found no R13-created double outcome.

The forward prose partition is complete. Finding 1 is the execution/receipt seam beneath that prose: the calibration branch is not yet implemented by the atomic conforming edits.

### Reverse: every stated outcome must have a reachable, authenticated witness

- `INCONCLUSIVE-BY-CALIBRATION` is structurally reachable from a low BS-8f bound pre-unblinding and from any Row-P post-unblinding removal.
- `VOID` is reachable from protocol/count/digest deviation and from the table's other void conditions.
- `INCONCLUSIVE-BY-POWER` is reachable from fewer than 962 successes or either self-verification failure.
- Row P's four accounting refusals and three exclusions each have the corresponding record-state witness.
- The successful disclosure path is intended to require calibration PASS, protocol PASS, Stage-C PASS, BS-5f, verified BS-L, unblinding, no-removal exact-parent closure, BS-7f, and BS-V.

The reverse test fails at the authenticated calibration-PASS witness. Current BS-5f bytes can witness Stage-C PASS, but the closed schema and named implementation cannot witness the additional calibration PASS that Clause 3(c) tells `verify_lock()` to require. That orphan is Finding 1.

## Three-part threshold sweep — value, phase, failure effect

1. **Calibration accuracy:** value `0.85`; evaluated from BS-8f after P4 and before Stage C/BS-5f/BS-L; any per-bin lower bound `< 0.85` must emit `INCONCLUSIVE-BY-CALIBRATION` and halt pre-unblinding, while all `>= 0.85` is PASS. The value, phase, and prose failure effect match V15 lines 566–567 and code line 81/`adjudicate_path()`. The missing authenticated implementation/binding is Finding 1.
2. **Stage-C trial count:** exactly `1_000`; verified in Row J before Stage-C execution or BS-5f; mismatch is protocol deviation and `VOID`. This matches code line 77 and the line-1277 `None` branch.
3. **Stage-C success count:** FAIL for `< 962` of 1,000 and PASS for `>= 962`, evaluated at P5 before BS-L; FAIL emits `INCONCLUSIVE-BY-POWER` and halts. This matches code lines 77–78 and 1277.
4. **Stage-C self-verification:** any `refuted` or `nonconservative` result at P5 is a fail-closed Stage-C FAIL, hence `INCONCLUSIVE-BY-POWER`; neither is required for PASS. Code lines 1275–1277 support the corrected citation and partition exactly.
5. **Post-unblinding attrition:** threshold is one removal (`>= 1`) at Row P/P8; any removal emits `INCONCLUSIVE-BY-CALIBRATION` with no Stage-C rerun. The zero-removal complement proceeds. This is the principal-held design and was not weakened.
6. **Confidence exclusion:** the numeric value is deliberately not yet supplied because it belongs to the refused BS-2a DESIGN slot and must be frozen before BS-6; application is post-unblinding at Row P, where a below-threshold row becomes `EXCLUDED-BY-CONFIDENCE`, and the resulting removal immediately yields `INCONCLUSIVE-BY-CALIBRATION`. Because BS-2a is REFUSED/UNFILLED and blocks the first image byte, the absent value does not create post-data discretion in an executable run; it remains an expressly blocked prerequisite.
7. **Exact-parent cardinality boundaries:** zero records, more than one record, extra records, and malformed records are evaluated at P8 with their four fixed `INCONCLUSIVE-BY-*` effects; exactly one usable record continues through absence/non-finite/confidence/accepted-finite precedence.
8. **Allocated-sample finiteness:** any allocated missing/non-finite output is tested by Row I before BS-8f and fails/halts the run; the all-usable-finite complement can emit BS-8f.
9. **One-use opening authorization:** exactly one P7 invocation is allowed; replay voids. No threshold phase or failure effect is deferred.

I found no competing value or boundary contradiction among the thresholds stated in R13. The blocker is not a wrong number; it is the missing executable and authenticated carrier for the calibration threshold's phase/effect.

## Corrected citation check

`../ref/successor_ref_v9.py` lines 1275–1277 read:

- nonempty `refuted` or `nonconservative` → `return succ, False, audit`;
- otherwise `succ >= CP_PASS_X` only when `n_trials == N_TRIALS`, else `None`.

Part 5 item 16 now correctly attributes the no-deviation legality rule to Row J and cites lines 1275–1277 only for the self-verification and count-return partition. This repair holds.

## Failed attacks

- I tried to recreate R12's late calibration branch. It is gone: Row J now evaluates the low bound at P5, before Stage C and BS-L, and Row P only binds the inherited PASS.
- I tried to delete or bypass Row P's distinct removal/applicability branch. It remains reachable and intact: any absence, non-finiteness, or low-confidence removal yields `INCONCLUSIVE-BY-CALIBRATION` without a rerun.
- I tried to find an uncovered lawful Stage-C FAIL. With exactly 1,000 trials, `< 962`, `refuted`, and `nonconservative` exhaust FAIL; the complement is PASS.
- I tried to route a calibration or Stage-C FAIL into Row P. The prose makes BS-5f/BS-L PASS prerequisites, so those post-unblinding FAIL branches remain correctly absent. The attack that did land is narrower: the calibration PASS prerequisite is not yet authenticated by the schema/code R13 names.
- I checked the repaired 1275–1277 citation directly; it is accurate.

## Testimony

- The draft states that BS-2a is `REFUSED / UNFILLED`, Rows C2 and E cannot run, and BS-6/the first image byte remain blocked. I did not independently adjudicate the external BS-2a gate reports; those state assertions remain testimony for this prose review.
- The stated predecessor count of 208,405 was not checked against data. I did not read `/Users/duhokim/NebulaMindData/` and performed no fetch.
- I did not execute Stage C or touch χ-bearing inputs. The source checks were limited to the local preregistration, draft history, and pinned reference implementation.

## Evidence ledger

Content read:

- `BRIEF_SECTION6_REVIEW_R13.md`
- `BRIEF_DRAFT_SECTION6_R13.md`
- `runner_s6r13_round.log`
- `SECTION6_DRAFT_AGY_R13.md`
- `SECTION6_DRAFT_AGY_R12.md` through the R12→R13 unified diff
- `SECTION6_REVIEW_R12_CODEX.md`
- `SECTION6_REVIEW_R12_GPT56.md`
- `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` relevant acceptance, Stage-C, calibration, void-rule, and slot passages
- `../ref/successor_ref_v9.py` constants, `SLOT_SCHEMA`, Stage-C return partition, and located calibration/receipt passages

Checks run:

- `shasum -a 256 SECTION6_DRAFT_AGY_R13.md`
- R12→R13 unified diff
- Full Row P extraction
- Whole-document numeric/threshold and branch-token sweeps
- Repository searches for `verify_lock`, BS-5f schema/bindings, confidence thresholds, calibration PASS, and `a_lb_b`

No content under `/Users/duhokim/NebulaMindData/` was read, no network fetch was performed, and no source/preregistration/code artifact was modified. The only write was this required referee report.

**NOT CLEAR**