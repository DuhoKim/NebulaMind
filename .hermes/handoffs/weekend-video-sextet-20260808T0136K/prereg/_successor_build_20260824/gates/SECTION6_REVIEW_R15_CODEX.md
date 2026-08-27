# SECTION 6 REVIEW R15 — CODEX

## Verdict

R15 is clear at the document-contract level. Its Part 2 now names the outside-§6 edits omitted in R14, preserves route (b), and keeps every not-yet-written mechanism explicitly UNRESOLVED rather than presenting it as implemented. I found no new asserted-versus-executable seam in the conforming-edit instruction. The implementation remains blocked and unexecuted; this verdict does not clear BS-2a, code, the first image byte, or any run.

## Digest verification — performed first

- Required SHA-256: `d2c388a451d076f880c879e888ee7901331adc62142245a285b8ff932d67f01a`.
- Independently computed SHA-256 for `SECTION6_DRAFT_AGY_R15.md`: `d2c388a451d076f880c879e888ee7901331adc62142245a285b8ff932d67f01a`.
- Result: **MATCH**. The bytes reviewed are the pinned bytes.
- Mechanical R14/R15 Part-1 check: both replacement-§6 bodies hash to `48f0090a56d85e2741832da7df7a62f9d43f7f445e3f0275a717eac439a9f893`; result **BYTE-IDENTICAL**. The substantive R15 delta is Part 2.

## Numbered findings

1. **NO BLOCKING FINDING — Part 2 completeness now holds at fold-instruction level.**

   **Evidence.** The top-to-bottom dependency walk closes the outside-§6 work Part 1 creates: BS-2a refusal/BS-6 block (item 1); §2.5 checksum narrowing (item 2); §2.7/§4 exclusion and Stage-C conformance (item 3); §5/production guard conformance (item 4); Row-P exact-parent closure, adequacy receipt and consequence tree (item 5); §7 table moves and named unblinding artifact (item 6); §7 counts/DESIGN inventory plus lint (item 7); §10 trace (item 8); and the schema, lock verifier, Row-J guard, mediation, C2/recompute and Row-O/Q verifier implementations (item 9). Part 2 line 103 explicitly says these are required unresolved work, not implemented mechanisms.

   **Why it holds.** A literal application of Part 2 now has an instruction for each R14 outside seam and for the exact schema entries named by GPT56. It no longer relies on Part 1's normative prose alone to imply the required edits.

   **Smallest sufficient repair.** None required for clearance.

2. **LOW / NON-BLOCKING — Part 5 line 159 uses a stale status label for the R14 completeness finding.**

   **Evidence.** It labels “R14 Defect 1 — Omitted edits” as `UNRESOLVED` and immediately says the omitted items were added. The implementation is indeed unresolved, but the R14 finding was that Part 2 failed to name required work; R15 repairs that document defect.

   **Why it does not fail this gate.** Part 2 line 103 and the item-9 heading clearly distinguish required work from implemented work, so the operative fold instruction is not ambiguous. The stale repair-map label does not remove or weaken any required edit.

   **Smallest sufficient repair.** In a future metadata-only cleanup, label the R14 document-completeness defect `REPAIR` and state separately that the listed code remains `UNRESOLVED`. This is not required before folding Part 2.

## Each R14 seam — individual disposition

1. **§7 count and DESIGN inventory — CLOSED.** Part 2 item 7 requires “One of fourteen class-P slots is filled,” `7 class-E`, a regenerated DESIGN inventory including BS-2a and BS-2k and excluding value-only BS-2f, plus lint against parsed tables/classifications. I independently parsed current V15 as 14 class-P and 6 class-E rows; removing class-P BS-L, adding class-P BS-2k, and adding class-E BS-L yields 14 class-P and 7 class-E, exactly as R15 states.

2. **Canonical receipt/schema seam behind `SLOT_SCHEMA` — CLOSED at document-contract level.** Part 2 item 9 explicitly requires exact pinned `SLOT_SCHEMA` entries and canonical fields for BS-L and BS-2k, names BS-2a schema work as deferred with the refused design, binds the schema bytes into the implementation/schema digest, and requires BS-2f/BS-L checkpoint and archive-seal-state schema updates. Items 4–6 and 9 additionally name the adequacy and unblinding artifacts and their verification dependencies. The pinned v9 code still lacks BS-2a, BS-2k and BS-L entries and still has the old BS-2f fields; R15 correctly records the changes as required work rather than claiming they exist.

3. **§5 guard seam — CLOSED.** Part 2 item 4 now explicitly conforms both §5 and the pinned production symbol to require and verify canonical BS-L, the one-use unblinding receipt, exact final-mask binding and post-unblinding ledger recomputation, with refusal before any statistic on an inconclusive adequacy result.

4. **§2.5 checksum narrowing and Clause-10/§10 trace implications — CLOSED.** Item 2 narrows the producer checksum list to source-image transport at BS-6. Item 8 requires the §10 repair-trace entry. The broader implementation implications are enumerated in item 9 rather than left implicit.

## GPT56’s R14 schema seam — disposition

**CLOSED at document-contract level.** Part 2 item 9 individually names exact pinned schema entries/canonical receipt fields for BS-2a, BS-2k and BS-L: BS-2a is explicitly deferred with its refused design; BS-2k and BS-L are required in the next atomic revision. None is falsely claimed implemented.

## Route (b) adjudication

R15 unambiguously takes **route (b)**: BS-5f remains unchanged; pinned `verify_lock()` must resolve the BS-L-bound authenticated BS-8f bytes and independently recompute `all(a_LB_b >= 0.85)`; the implementation/schema digest is pinned; and a low-bound negative fixture must show that no passing lock can result. This closes the R13 asserted-versus-executable finding at document-contract level rather than relocating it. Route (a) is not better: adding a producer-authored calibration field to BS-5f enlarges a Stage-C receipt and still requires independent authentication of the authoritative BS-8f source. Route (b) checks that source directly at the lock verifier.

## Clause 10 — both directions over the whole table

### Forward: each branch has one consequence

- Row I: allocated missing/non-finite output halts before BS-8f; the usable-finite complement emits BS-8f.
- Row J calibration: any bin `< 0.85` emits `INCONCLUSIVE-BY-CALIBRATION` and halts; all bins `>= 0.85` proceed.
- Row J protocol: trial-count or frozen implementation/protocol deviation terminates through the row’s `VOID` rule before Stage C/BS-5f.
- Row J Stage C: `< 962` successes, `refuted`, or `nonconservative` emits `INCONCLUSIVE-BY-POWER`; the exact complement is the sole route to BS-5f and BS-L.
- Row O: the authorized one-use P7 invocation emits the unblinding receipt; pre-lock invocation, replay, or out-of-destination decryption has the stated void consequence.
- Row P: the ordered eight-state exact-parent partition gives one fixed consequence to every record state. Any absence/non-finite/low-confidence removal then emits `INCONCLUSIVE-BY-CALIBRATION`; zero removal binds the already verified calibration and Stage-C PASS. There is no post-unblinding Stage-C rerun.
- Clause 8: unresolved retrospective custody at freeze refuses the run.
- Other rows retain one named normal emission and one stated forbidden-surface consequence. Part 1 is byte-identical to the R14 body already checked, and the R15 Part-2 additions create no new branch or outcome.

### Reverse: each stated outcome has a defined witness

- Pre-lock `INCONCLUSIVE-BY-CALIBRATION`: authenticated BS-8f with any `a_LB_b < 0.85`; route (b) requires the independent lock-verifier check and negative fixture.
- `INCONCLUSIVE-BY-POWER`: fewer than 962 successes or either fail-closed self-verification condition after protocol admission.
- `VOID`: protocol/count/digest deviation or a table-defined forbidden act.
- Row-P accounting refusals/exclusions: the corresponding exact-parent terminal state; any exclusion witnesses the post-unblinding calibration-applicability halt.
- Success: authenticated BS-8f calibration PASS, BS-5f Stage-C PASS, verified BS-L, one-use unblinding receipt, zero-removal exact-parent closure, BS-7f, BS-V, then disclosure.

No branch is double-valued, deferred to later judgement, or orphaned by the R15 Part-2 edits.

## Threshold sweep — value, phase, failure effect

1. **Calibration floor:** `0.85`; Row J/P5 after BS-8f and before Stage C, BS-5f, BS-L and unblinding; any bin `< 0.85` → `INCONCLUSIVE-BY-CALIBRATION`, equality passes. This matches V15 lines 566–567 and v9 `A_FLOOR`/`adjudicate_path()` lines 81 and 1492–1496.
2. **Trial count:** exactly `1_000`; verified before Stage C/BS-5f; mismatch is protocol deviation → `VOID`. This matches v9 lines 77 and 1277.
3. **Stage-C success threshold:** `< 962` FAIL, `>= 962` PASS out of 1,000; evaluated pre-unblinding at P5; FAIL → `INCONCLUSIVE-BY-POWER`. This matches v9 lines 78 and 1277.
4. **Stage-C self-verification:** any `refuted` or `nonconservative` result fails closed at P5 → `INCONCLUSIVE-BY-POWER`; neither is required for PASS. This matches v9 lines 1275–1277.
5. **Post-unblinding removal:** one or more removals at Row P/P8 → `INCONCLUSIVE-BY-CALIBRATION`; zero is the complement; no Stage-C rerun.
6. **Exact-parent accounting:** zero, duplicate, extra and malformed records have the four fixed post-unblinding `INCONCLUSIVE-BY-*` refusals; exactly one valid record proceeds through absence, finiteness and confidence.
7. **Opening cardinality:** exactly one authorized P7 opening; replay has the stated void effect.

I found no value, phase or failure-effect conflict.

## Asserted-versus-executable sweep

I found no additional document-level seam. Every mechanism not present in pinned v9 that Part 1 requires is either enumerated in Part 2 as next-atomic-revision work or explicitly deferred with refused BS-2a. The code remains non-executable for this redesign; the document no longer disguises that fact as completion.

## Failed attacks

- I tried to re-create the R14 false §7 arithmetic and DESIGN list after a literal fold. Item 7 now gives the correct post-edit counts and classification constraints and adds lint.
- I tried to reach Row P through the old §5 surface without BS-L or a one-use unblinding receipt. Item 4 now explicitly closes both guards in §5 and the pinned production symbol.
- I tried to leave BS-2a, BS-2k or BS-L outside the pinned schema work. Item 9 names all three and keeps BS-2a honestly deferred.
- I tried to preserve the broad producer-checksum scope or omit the repair trace. Items 2 and 8 close both.
- I tried the equality boundaries: `a_LB_b == 0.85` passes, `successes == 962` passes, and `n_trials` must equal 1,000. Draft, V15 and pinned v9 agree.
- I tried to make route (b) trust BS-5f’s producer-authored PASS. The required verifier instead resolves BS-L’s bound BS-8f bytes and recomputes the predicate independently.

## Testimony

- The future Row-J guard, `verify_lock()`, new/changed schemas, mediator, C2 worker, recompute path, opening/replay verifier, archive verifier and negative fixtures were not executed because they do not exist in pinned v9. Their future behavior remains **Testimony / UNRESOLVED** until implemented, pinned, tested and gated.
- BS-2a REFUSED/UNFILLED, Rows C2/E blocked, and first-image-byte blockage are brief/draft state assertions. I did not independently re-adjudicate the external BS-2a reports.
- I did not inspect the predecessor archive or verify the stated 208,405 count. I did not read `/Users/duhokim/NebulaMindData/`, fetch anything, inspect secrets, or touch χ-bearing inputs.

## Evidence ledger

Content read:

- `BRIEF_SECTION6_REVIEW_R15.md`
- `SECTION6_DRAFT_AGY_R15.md`
- `SECTION6_REVIEW_R14_CODEX.md`
- `SECTION6_DRAFT_AGY_R14.md` through the R14→R15 diff
- `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` relevant §4, §5, §6.3, §7 and §10 passages
- `../ref/successor_ref_v9.py` constants, `SLOT_SCHEMA`, Stage-C return partition and calibration adjudicator

Checks run:

- `shasum -a 256 SECTION6_DRAFT_AGY_R15.md`
- R14/R15 Part-1 SHA comparison and full R14→R15 unified diff
- Independent current-V15 §7 table parse and post-edit arithmetic
- Search of pinned v9 for lock/unblinding/archive/recompute mechanisms
- Whole-table Clause-10 forward/reverse audit
- Threshold value/phase/effect comparison against V15 and pinned v9

No source, preregistration, code, draft-under-review, or data artifact was modified. The only write was this required referee report.

**CLEAR**