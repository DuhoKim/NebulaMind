# §6 R11 REFEREE REPORT — CODEX

Verdict: **NOT CLEAR**. The intended relocation of the ordinary Stage-C power decision to Row J is directionally correct, and the named no-rerun passages agree. But applying Clause 10 in both directions exposes two still-open Stage-C branches plus stale contradictory repair claims: R11 deleted the R10B protocol-deviation `VOID` branch rather than reseating it pre-unblinding, and Row J does not terminate the frozen Stage-C implementation's independent self-verification failure path.

## Artifact identity — verified first

- File opened: `SECTION6_DRAFT_AGY_R11.md`
- Independently computed sha256: `5daae51e7a195be46ec9e4bd6269fa0035dc1f7ca34af9edac2fcc72dfda17f0`
- Digest recorded at `runner_s6rev11_round.log:2`: `5daae51e7a195be46ec9e4bd6269fa0035dc1f7ca34af9edac2fcc72dfda17f0`
- Result: **MATCH**. Content review proceeded.

## Numbered findings

1. **HIGH — Row J / Row P / Clause 10: the R10B protocol-deviation `VOID` branch was deleted, not reseated.**

   **Why it fails:** The brief says the substantively correct R10B power-inapplicability repair is unchanged. R10B made any deviation from the pinned 1,000-trial protocol or frozen Stage-C implementation terminate `VOID`. R11 removes that condition from both Row P (`SECTION6_DRAFT_AGY_R11.md:53`) and Part 2 item 4 (`:106`). Row P merely binds a protocol digest and verifier result; it states no consequence if either verification fails. Thus a protocol/implementation deviation is a reachable input condition with no stated outcome, violating Clause 10 in the forward direction. In the reverse direction, Part 5 still states twice that the outcome exists: line 137 says Row P makes any deviation `VOID`, and line 145 says Row P and Part 2 item 4 do so. Those stated branches are unreachable because the normative row and conforming edit no longer contain them.

   **Smallest sufficient repair:** Put the protocol check where it can execute before BS-5f is accepted: Row J must verify exactly `N_TRIALS = 1_000` and the frozen Stage-C implementation/protocol digest before running or issuing BS-5f, with any deviation terminating `VOID`. Make BS-5f bind that verification. Keep Row P limited to binding the already-verified PASS and protocol digest. Conform Part 2 item 4 and Part 5 items 8 and 16 to that Row-J seating; do not restore an unreachable post-unblinding Stage-C FAIL branch in Row P.

2. **HIGH — Row J / Clause 10: `< 962` is seated there, but it is not the only executable Stage-C FAIL path.**

   **Why it fails:** Row J (`:47`) gives `INCONCLUSIVE-BY-POWER` only when the locked run yields fewer than 962 passing trials. The frozen implementation has an independent fail-closed branch at `../ref/successor_ref_v9.py:1275–1276`: any `refuted` or `nonconservative` result returns `False` regardless of the passing-trial count. V15 `:421–425` assigns every Stage-C FAIL the same pre-unblinding consequence: `INCONCLUSIVE-BY-POWER` and halt. R11's Row J void column forbids continuing after a Stage-C FAIL, but it never states the outcome for a self-verification FAIL at 962 or more passing trials. That reachable path is therefore unterminated under Clause 10. The numeric threshold itself is correct (`N_TRIALS = 1_000`, `CP_PASS_X = 962` at reference lines 77–78); the missing branch is semantic, not numeric.

   **Smallest sufficient repair:** After the protocol-deviation check in finding 1, state in Row J that **any** locked Stage-C FAIL emits `INCONCLUSIVE-BY-POWER` and halts, explicitly including (a) fewer than 962/1,000 passing trials and (b) the self-verification `refuted` or `nonconservative` fail-closed return at reference lines 1275–1276. State the complementary PASS branch as the sole route to BS-5f → BS-L. Conform Part 3 C2 and Part 5 item 17 to describe the complete PASS/FAIL partition rather than only the count threshold.

3. **MEDIUM — Part 5 findings 8 and 16 contradict R11's normative relocation.**

   **Why it fails:** Part 5 line 137 says “Row P deterministically applies” the `< 962` rule; line 145 says Row P and Part 2 item 4 retain the deviation-to-`VOID` rule and that Part 3 explains it. R11 lines 47, 53, 106, 116, and 147 instead place the count decision in Row J and delete those Row-P/Part-2 branches. This is not merely historical wording: Part 5 labels both assertions `REPAIR`, so the document simultaneously claims incompatible current mechanisms. It also defeats the requested whole-document reachability audit by advertising outcomes absent from the normative text.

   **Smallest sufficient repair:** Rewrite Part 5 items 8 and 16 to say: the ordinary Stage-C PASS/FAIL decision executes at Row J; a verified PASS is required for BS-L and therefore inherited by Row P; protocol or frozen-implementation deviation terminates `VOID` at Row J before an acceptable BS-5f exists. Update the referenced locations accordingly.

## Clause 10 bidirectional audit

- **Path → exactly one outcome:** Row P's eight ordered accounting states, attrition-first calibration failure, calibration-accuracy failure, and no-removal/pass continuation are stated without restoring the unreachable Stage-C FAIL branch. The open paths are the protocol/implementation-deviation condition (finding 1) and Stage-C self-verification FAIL at a count of at least 962 (finding 2).
- **Stated outcome → reachable path:** Row J's `< 962/1,000 → INCONCLUSIVE-BY-POWER` outcome is reachable before BS-L. Row P cannot lawfully see a Stage-C FAIL because `verify_lock()` requires BS-5f PASS; deleting that Row-P branch was correct. The stale Row-P `VOID` and Row-P `< 962` claims in Part 5 have no corresponding branch (findings 1 and 3).

## Required focused checks and failed attacks

- **Digest attack:** held; live sha256 equals the post-exit pinned digest exactly.
- **Ordinary `< 962` relocation:** held in the narrow sense requested. Row J contains `< 962/1,000 → INCONCLUSIVE-BY-POWER` and halt; reference constants at lines 77–78 are exactly 1,000 and 962; V15 lines 421–425 require pre-unblinding halt on Stage-C FAIL. Removing the duplicate Row-P power branch did not remove the ordinary count decision from the study.
- **No-rerun sweep:** held across Row P (`:53`), Part 2 items 2 and 4 (`:104`, `:106`), Part 3 C1 (`:115`), Part 5 finding 5 (`:134`), and R3 (`:124`). They consistently bind the locked BS-5f result and perform no post-attrition Stage-C rerun.
- **Number sweep:** threshold literals checked clean: 1,000 and 962 match reference lines 77–78; `a_LB_b < 0.85` matches V15 lines 566–567 and reference line 81; the post-first-real-χ void citation matches V15 lines 570–573; 208,405 matches V15 lines 35 and 546. Mechanical recount found twenty lifecycle rows (A–S including C2) and ten numbered clauses. No numeric transcription error found.
- **Unreachable-branch attack on Row P:** held for the intended repair. A verified BS-L requires BS-5f PASS, so a Row-P Stage-C FAIL outcome would indeed be dead code.

## Testimony

No assertion requiring a real-data fetch was used. `/Users/duhokim/NebulaMindData/` was not read, and nothing was fetched. The retrospective-custody state and the future BS-2a mechanism were not independently verified; they remain declared residual/blocking matters rather than evidence for this verdict.

§6 is not yet sound as prose because the Stage-C branch partition and its repair map remain incomplete/inconsistent. Apart from these bounded Stage-C custody/termination repairs, the remaining declared blocker is genuinely the refused BS-2a mechanism; BS-6 and the first image byte remain blocked.

**NOT CLEAR**