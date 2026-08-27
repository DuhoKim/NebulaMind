# CODEX referee report — preregistration text V12, round 3

Subject independently read as fresh: `PREREG_SUCCESSOR_DRAFT_V12_20260827.md`, sha256 `7633bc7a6b49da8277dd018228a4bfb51102eb22bbff8f84add2b7f8f58e63d3`.

## Findings

1. **BLOCKING — the primary-lock receipt is required both before and after unblinding, so the repaired event order still cannot be executed.**

   **Section / sentence.** §6.1(1) says the primary lock “is sealed by a signed BS-V receipt”; §6.1(2) requires “BS-5f's confirmatory power receipt exists, then the primary lock is sealed, then unblinding occurs.” But §7 defines BS-V as “verdict + primary lock” and requires its content to include the `decide()` output and evaluated floor. §5 says the production verdict is formed only after `run_production_verdict()` receives the real signed mask and creates the production permutation record; §7 separately places BS-7f before the verdict.

   **Why this fails as a promise.** At the sentence level, V12 correctly repairs the order to BS-5f → lock → unblinding. At the receipt level, however, the lock cannot be sealed until BS-V contains a verdict, and the verdict cannot exist until the real signs have been unblinded and evaluated. Thus the document simultaneously requires BS-V before unblinding and makes BS-V depend on work after unblinding. A future operator cannot comply with both; choosing which clause to relax is an outcome-adjacent discretion. The same cycle also makes §6.1(2)'s claim that key holders are recorded in “BS-V's schema before any image byte” non-receiptable: the only named BS-V artifact is the later verdict receipt.

   **Smallest sufficient repair.** Split the pre-unblinding lock from the post-unblinding verdict. Add a distinct pre-unblinding lock/key-holder receipt (with roster, accepted-mask digest, calibration digest, decision-input digests, and access-log digest), make BS-5f block that receipt, make it block unblinding, and reserve BS-V for the later verdict. Update §6.1(1)–(3) and §7 to name that same sequence and receipt.

2. **BLOCKING — BS-2a is called a class-P design prerequisite in §2.7 but is placed in Class E in §7, allowing the preregistration to freeze before its acceptance rule exists.**

   **Section / sentence.** §2.7(6) says acceptance design “is its own class-P slot” and describes BS-2a as the threshold, retry/failure semantics, evidence and ledger schemas, recomputation code, and fixtures. §7 instead lists BS-2a under **Class E — execution gates**. §7's class-P preamble still says there are twelve class-P slots, that one is filled, and names the design slots without BS-2a. The header says the text becomes a preregistration once every class-P slot holds a receipt, the gates pass, and Duho signs the freeze.

   **Why this fails as a promise.** The accepted set changes both signs and geometry and therefore can change the answer. Under the literal slot table, all twelve class-P slots can be filled and the text can be signed and frozen while BS-2a remains undesigned. The operator may then choose the confidence definition, threshold, retry policy, failure semantics, evidence schema, and recomputation implementation as an execution-stage item. “Before any image byte” prevents choosing after inference but does not repair the document's claim that the analysis promise was complete at freeze. It also understates incompleteness: once BS-2a is correctly treated as class P, the draft has thirteen class-P slots, twelve unfilled, not twelve total and eleven unfilled.

   **Smallest sufficient repair.** Move BS-2a into the Class-P table; make it block freeze as well as BS-2f and BS-6; update the count to thirteen class-P slots / twelve unfilled; and add BS-2a to the §7 DESIGN-slot list. Keep BS-2f as the later value-only realised partition.

3. **BLOCKING — Stage P remains dual-valued under the document's own precedence law. Open disclosure is honest draft posture, but it is not a freezeable promise.**

   **Section / sentence.** §0 says every operational mechanism is defined by pinned code and “the code is the definition.” §2.6 openly says the pinned v9 code implements the shared-null route while the preferred prose promises an exact per-trial null. §4 still specifies the shared reference-null mechanism. The v9 code independently inspected at lines 1218–1263 constructs one `ref_z` and uses it across trials, with only sampled own-null checks. The exact receipt instead records 995/1000 under 20,000 permutations per trial, but identifies a measurement harness and is not the code §0 pins.

   **Why this fails as a promise.** Stating the conflict openly is the correct posture for an unfinished draft, and it is materially better than concealing it. It is not sufficient for a preregistration declared sound enough to freeze once slots are filled: the operator still has two operative tests and can cite either §0/§4 or the preferred prose. Moreover, BS-5p is explicitly unfillable while the conflict remains. This is not merely an empty value slot; it is an unresolved answer-determining mechanism.

   **Smallest sufficient repair.** Before any freeze, either (preferably) implement the exact per-trial test in the code §0 pins, pin all of its permutation/addressing/serialization details, add fixtures, gate the new bytes, and make §4 describe exactly that code; or amend §0's precedence law and delete the conflicting shared-null mechanism from the binding promise. Then re-run the text gate.

4. **MINOR — §2.7 has two item 5s.**

   **Section / sentence.** The acceptance list numbers the confidence-definition clause as 5, the BS-2a clause as 6, and the threshold-before-image clause again as 5.

   **Why this matters as a promise.** A future receipt or amendment referring to “§2.7(5)” would be ambiguous between the confidence definition and the threshold timing rule. The substance is present, so this is not independently blocking.

   **Smallest sufficient repair.** Renumber the final clause as 7 and update any references.

## Promise audit and failed attacks

- **Can it fail?** Yes. §5 gives a narrow positive result (`REPRODUCED-LONGO`), a narrow negative result (`REJECTED-AT-LONGO-AMPLITUDE`), and an explicit residual `INCONCLUSIVE` region. A null p-value alone cannot be promoted to rejection; the three-sigma upper bound must also fall below 0.0408. The text cannot absorb every numeric outcome into reproduction.
- **Researcher degrees of freedom.** The DR11/DR10.1 fork is date- and availability-bound in §2.1. Selection thresholds and decision boundaries are code- or slot-bound. The still-open answer-determining choices are candidly represented as DESIGN work (Stage P, BS-2a acceptance, BS-8p calibration plan, BS-9 input path), but Finding 2 shows BS-2a is on the wrong side of freeze. The Stage-P choice in Finding 3 remains genuinely dual rather than merely empty.
- **Circularity.** I did not find a data-adaptive primary decision boundary in §5. The fixed `x >= 962`, p thresholds, 0.0408 target, and N_eq floor do not depend on the realised sky result. Calibration values affect the predeclared scalar/profile/halt route, but the stated route is fixed before unblinding. Acceptance remains contingent on the not-yet-designed BS-2a mechanism rather than safely closed now.
- **Numbers and artifacts independently checked.** The two §0 code hashes match exactly: `successor_ref_v9.py` = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` = `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`. The fixture output ends `ALL FIXTURES PASS` and its digest matches the freeze record (`fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`). The exact Stage-P receipt gives 995/1000, n=53,005, Var(c)=0.7546638985, N_eq=120002.8798. The closure freeze records 65,060 objects → 6,445 selected bricks → 12,117 required bricks and plan digest `aaeaa9f3…`. Independent arithmetic gives 12,117 / 6,445 = 1.880062 and 12,117 × 12.2 MB = 147.8274 GB, matching §2.6's 1.880× and ≈147.8 GB. I found no additional stale quoted figure in the checked pins/receipts.
- **Predecessor input language.** The header now distinguishes the 60,308-brick sample (successor input) from the 208,405 sealed measurements (not an input), and §6.2 repeats that no predecessor χ enters the analysis. The nearby 208,407 figure is explicitly the declined parent-object count, not a third claim that 208,407 measurements enter this study.
- **Blinding.** §6.1 now forbids conflicted roles from access, requires logging of every read/refusal, makes unauthorized access void the run, and states a checkable no-external-artifact condition. The redesign record is described as geometry-only and any outcome-derived quantity in that path voids the licence. I did not find a remaining prose permission to unblind before BS-5f; the remaining failure is the receipt cycle in Finding 1.
- **Incompleteness and overclaim.** V12 is candid that the selection lacks a producer receipt, the exact power calculation is outside the pinned code, the mechanism panel had one seat, and most slots are empty. It also says the test is not a test of isotropy or A≈0.02 and names rejection only at Longo's amplitude. Finding 2 requires correcting the slot count and freeze boundary; otherwise the draft reads one decisive design slot closer to completion than it is.

## Testimony

Not independently verified in this pass: the Longo abstract quotation and sign-convention mapping; Duho's historical drafting/catalog-only authorizations; the claim that no fetch was needed in the 2026-08-25 geometry run; the provenance and exact count of the predecessor's sealed χ archive; provider refusal reasons for the two missing closure-referee seats; producer checksum provenance; and the claim that the footprint redesign path never saw an outcome-derived quantity. These remain testimony here, not findings asserted as independently established.

Blocking findings: (1) BS-V makes the repaired lock order cyclic; (2) BS-2a is misclassified as Class E and can remain open at freeze; (3) Stage P remains dual-valued under §0.

**NOT CLEAR**