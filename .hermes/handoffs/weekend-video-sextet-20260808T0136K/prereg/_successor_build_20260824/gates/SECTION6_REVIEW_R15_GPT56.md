# §6 R15 REFEREE REPORT — GPT56

Verdict: **NOT CLEAR**. R15 closes my R14 `SLOT_SCHEMA` seam and most of CODEX's named R14 seams, without disturbing the credited Part 1 contract. One receipt-schema seam remains open: Part 2 requires use and verification of the one-use unblinding receipt but never lists the required canonical unblinding-receipt schema addition. A future `verify_unblinding_receipt()` with no enumerated schema is again a named verifier without the complete receipt contract it must authenticate, so Part 2's asserted completeness is still false.

## Digest-first identity check

- Opened subject: `SECTION6_DRAFT_AGY_R15.md`.
- Independently computed sha256: `d2c388a451d076f880c879e888ee7901331adc62142245a285b8ff932d67f01a`.
- Brief-pinned sha256: `d2c388a451d076f880c879e888ee7901331adc62142245a285b8ff932d67f01a`.
- Result: **MATCH**.
- Mechanical Part-1 comparison: the text between the Part 1 and Part 2 headings is byte-identical in R14 and R15; both extracted regions hash to `06f6e98915e9e5e120c82ccb131c3124d3ee23c892a2122dc93b34ca058b6964`.

## Numbered findings

1. **HIGH / BLOCKING — the canonical unblinding-receipt schema is still absent from the asserted-complete Part 2 list.**
   - **Row/clause:** Row O; Row P; Clauses 3(e), 4 and 6; Part 2 items 4, 6 and 9.
   - **Evidence:** Row O emits the unblinding receipt; Row P requires it; Clause 3(e) requires canonical receipts to carry and authenticate decoded fields; Clause 4 requires the genuinely final post-unblinding access-log checkpoint to be carried in it. Part 2 item 4 requires §5 and the pinned production symbol to verify the one-use unblinding receipt, item 6 merely adds it as a named artifact, and item 9 requires `verify_unblinding_receipt`. But no Part 2 item says to add/freeze the canonical unblinding-receipt schema or enumerates the fields that verifier must authenticate. The code-side schema bullet names BS-L, BS-2k, deferred BS-2a, and BS-2f/BS-L checkpoint/archive fields only. This omission is directly visible against R5 Part 2 line 188, which explicitly required “Add unblinding receipt schema”; that required outside edit has again disappeared.
   - **Why it fails:** A verifier name does not define its accepted bytes. Without a frozen canonical schema, later code retains freedom over whether the receipt binds the BS-L digest/checkpoint, complete extending chain segment, terminal unsealing events, final checkpoint, ceremony identity, destination, and one-use/replay state. This does not reopen Part 1 or the route-(b) calibration repair; it means the fold instruction still omits one outside-§6 edit that its own mechanisms require.
   - **Smallest sufficient repair:** Add one explicit Part 2 code/schema item requiring the canonical unblinding-receipt schema and its exact authenticated fields, including at minimum the BS-L identity/checkpoint, complete extending chain segment, terminal unsealing events, final post-unblinding checkpoint, destination and one-use ceremony identity/replay state; bind those schema bytes into the pinned implementation/schema digest and make `verify_unblinding_receipt()` authenticate exactly them. Keep implementation marked UNRESOLVED until delivered.

## R14 seams — individual closure status

1. **CODEX: §7 count and DESIGN inventory — CLOSED.** Part 2 item 7 explicitly changes the prose to one of fourteen class-P slots filled and seven class-E slots, includes BS-2a and BS-2k, excludes value-only BS-2f, and requires count/classification linting.
2. **CODEX: canonical receipt/schema seams — STILL OPEN, but narrowed.** The slot-schema portion is closed: Part 2 item 9 explicitly requires exact pinned entries/canonical fields for BS-L and BS-2k, defers the BS-2a entry with the refused design, and requires the BS-2f/BS-L checkpoint/archive updates. Row P plus item 5 state the adequacy-receipt bindings. The canonical unblinding-receipt schema itself is still omitted, producing Finding 1.
3. **CODEX: §5 guard seam — CLOSED.** Item 4 now expressly requires canonical BS-L, the one-use unblinding receipt, exact final-mask binding, post-unblinding recomputation, and refusal before any statistic on an inconclusive adequacy result.
4. **CODEX: §2.5 producer-checksum narrowing — CLOSED.** Item 2 limits the list to source-image transport at BS-6.
5. **CODEX: Clause 10 / V15 §6.3 and §10 repair-trace seam — CLOSED.** Item 8 requires the replacement to be recorded in the repair trace.
6. **CODEX: remaining named implementation seams — CLOSED as inventory, not implementation.** Item 9 lists Row-B mediation, the C2 hermetic worker and fixtures, `recompute_acceptance_ledger`, `verify_unblinding_receipt`, `verify_archive_seal`, and opening-authorization/replay verification. Their future behavior remains Testimony, as the draft correctly says.
7. **GPT56: exact pinned `SLOT_SCHEMA` entries and canonical fields for BS-2a, BS-2k and BS-L — CLOSED.** Item 9 adopts the smallest repair from my R14 report: exact BS-L/BS-2k entries and fields, BS-2a schema work deferred with the refused BS-2a design, and schema bytes bound into the implementation/schema digest. A fresh AST comparison confirms that the current v9 schema is missing exactly `BS-2a`, `BS-2k`, and `BS-L`, so the new edit item is accurately scoped.

## Part 2 completeness walk

R15 lists the following outside-§6 edits required by Part 1: BS-2a refusal/BS-6 block; §2.5 checksum narrowing; §2.7(4)/§4 exclusion timing and no post-attrition Stage-C rerun; §5 lock/unblinding/adequacy guards; Row-P exact-parent closure and adequacy consequence; §7 P/E table moves and the named unblinding artifact; §7 counts/DESIGN inventory/lints; §10 repair trace; new slot schemas; route-(b) lock verification; the Row-J guard; Row-B mediation; C2 integrity and recomputation; archive, opening and unblinding verifiers.

That walk closes every R14 seam except the schema half of the unblinding-receipt requirement. The unblinding receipt is named three times but its canonical schema addition is not in the list. Therefore the “complete list” assertion at Part 2 line 103 still does not hold.

## Route adjudication

R15 retains **route (b)**. BS-5f remains unchanged; pinned `verify_lock()` must resolve authenticated BS-L-bound BS-8f bytes and independently recompute `all(a_LB_b >= 0.85)`, with the implementation/schema digest pinned and a low-bound negative fixture required. This closes the R13 asserted-versus-executable calibration-carrier finding at document-contract level rather than relocating it.

Route (a) is **not better**. Adding a producer-authored calibration field to BS-5f would enlarge the Stage-C receipt and still require independent authentication of its source. Route (b) checks the authoritative BS-8f bytes at the lock verifier.

## Clause 10 audit in both directions

- **Branch → outcome:** Rows A–S retain the R14 partition. Row I halts before BS-8f on an allocated unusable output. Row J maps any `a_LB_b < 0.85` to pre-unblinding `INCONCLUSIVE-BY-CALIBRATION`; protocol/count/digest deviation to pre-BS-5f void; Stage-C power/self-verification failure to `INCONCLUSIVE-BY-POWER`; and only the exact complementary PASS reaches BS-5f and BS-L. Row P's ordered exact-parent states are single-valued, and any removal terminates `INCONCLUSIVE-BY-CALIBRATION` before any Stage-C reconsideration. Clause 8 refuses unresolved retrospective custody before freeze.
- **Outcome → branch:** Each Row-J and Row-P terminal outcome has a stated antecedent. No calibration or Stage-C FAIL can enter the PASS-only BS-L path; no named post-unblinding FAIL is orphaned; and the successful path has the complementary predicates.
- **Result:** no new overlap, orphan outcome, or deferred judgement. Finding 1 is a receipt-contract completeness defect, not a reopened partition defect.

## Threshold sweep: value, phase and failure effect

- **Calibration floor:** `0.85`, matching V15 lines 566–567 and `A_FLOOR = 0.85`. It is evaluated from BS-8f in Row J/P5 before Stage C, BS-5f, BS-L and unblinding. Any bin `< 0.85` emits `INCONCLUSIVE-BY-CALIBRATION`; equality passes. The lock verifier independently recomputes the complementary all-bins `>= 0.85` predicate.
- **Trial count:** exactly `1_000`, matching `N_TRIALS = 1_000`. Row J verifies it before Stage C/BS-5f; deviation voids before a passing receipt exists.
- **Stage-C power:** fewer than `962` successes out of 1,000 fails; `962` passes, matching `CP_PASS_X = 962` and reference line 1277. Failure at P5 emits `INCONCLUSIVE-BY-POWER` and cannot reach lock.
- **Self-verification:** `refuted` or `nonconservative` fails closed at reference lines 1275–1277, at Row J before BS-5f, with `INCONCLUSIVE-BY-POWER` and no lock route.
- **Post-unblinding attrition:** one or more removals emits `INCONCLUSIVE-BY-CALIBRATION`; zero is the complement; no Stage-C rerun occurs.

No value, phase, boundary or failure-effect mismatch was found.

## Asserted-versus-executable sweep

The calibration mechanism is now a checkable future dependency: producer guard, independent verifier recomputation from authenticated BS-8f bytes, schema/implementation pin, and negative fixture are all enumerated and honestly UNRESOLVED. The current pinned implementation contains no `verify_lock`, `verify_unblinding_receipt`, `verify_archive_seal`, or `recompute_acceptance_ledger` definition; I therefore credit these only as contract requirements, not executed protections. Finding 1 is the remaining named-versus-defined seam: the future unblinding verifier is named but its receipt schema is not included in the supposedly complete edit inventory.

## Failed attacks

1. Tried to reopen the low-bound route to BS-5f: Row J blocks it and route (b) independently recomputes the PASS at lock verification.
2. Tried to route Stage-C/calibration FAIL through verified BS-L into Row P: the PASS-only lock path excludes it.
3. Tested equality boundaries at `0.85` and `962/1,000`: draft, V15 and v9 constants/returns agree.
4. Re-ran Clause 10 forward and backward over the whole table: the credited single-valued partition held.
5. Recompared the closed-list slots with current `SLOT_SCHEMA`: only BS-2a, BS-2k and BS-L are missing, and R15 now explicitly inventories all three.
6. Checked each other R14 outside seam: §7 arithmetic/classification, §5 guards, §2.5, §10 and named mechanisms are now present.

## Testimony / unverified assertions

- The future Row-J guard, `verify_lock()`, canonical slot/schema edits, unblinding verifier/schema, mediator, C2 worker, replay guard and fixtures do not exist in pinned v9 and were not executed.
- BS-2a findings 1, 2, 2b and 3 remain UNRESOLVED; Rows C2/E and BS-6 remain blocked. I did not treat these declarations as implemented repairs.
- I did not inspect `/Users/duhokim/NebulaMindData/`, fetch anything, inspect secrets, or read χ-bearing material.

## Evidence ledger and custody

Files read for content:

- `BRIEF_SECTION6_REVIEW_R15.md`
- `SECTION6_DRAFT_AGY_R15.md`
- `SECTION6_REVIEW_R14_GPT56.md`
- `SECTION6_REVIEW_R14_CODEX.md`
- `SECTION6_DRAFT_AGY_R5.md` (Part 2 and related schema history)
- `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` (current §2.5, §5, calibration, §7 and §10 seams)
- `../ref/successor_ref_v9.py` (`SLOT_SCHEMA`, constants, Stage-C partition and calibration adjudicator)

Independent checks performed:

- Subject sha256 before review: MATCH.
- R14/R15 Part-1 byte comparison and extracted-region sha256: identical.
- Current implementation sha256: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- AST extraction/set comparison of the §6 closed slot list against `SLOT_SCHEMA`: missing exactly BS-2a, BS-2k and BS-L.
- Definition counts for `verify_lock`, `verify_unblinding_receipt`, `verify_archive_seal` and `recompute_acceptance_ledger`: zero each.
- Threshold/source checks for `A_FLOOR`, `N_TRIALS`, `CP_PASS_X`, and Stage-C fail-closed returns.

The only file written by this seat is this report.

**NOT CLEAR**