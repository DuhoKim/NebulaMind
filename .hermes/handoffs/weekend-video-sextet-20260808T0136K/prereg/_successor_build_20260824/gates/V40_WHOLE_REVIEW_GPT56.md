# V40 whole-document referee — GPT56

## Verdict

**NOT CLEAR.** The dispatched bytes match the required SHA-256. V40 correctly keeps forbidden acts and protocol/digest deviation at `Any`, and the historical evidence supports `Post-first-real-χ` as the §2.7 instant. But the new computation route is not a terminated, enforceable procedure: it emits a terminal run outcome and then permits the same run to continue; Row J still says every Stage-C failure halts as `INCONCLUSIVE-BY-POWER` and that continuing voids; the frozen random-address contract has no attempt dimension; the claimed attempt log has no authenticated schema or producer; and the acknowledged attempt cap has no dependency edge to BS-6. Independently, BS-3g remains omitted from the exhaustive receiptable-schema surface, so its apparent BS-6 edge is not actually gateable. These are preregistration defects, not implementation complaints about an otherwise complete contract.

## Findings

### 1. HIGH / REPAIR-REQUIRED — `INCONCLUSIVE-BY-COMPUTATION` is both a terminal run outcome and a retryable attempt state

Section 5 first states that the lifecycle registry emits **exactly one outcome per run** (line 488), classifies `INCONCLUSIVE-BY-COMPUTATION` among the pre-statistic inconclusive **halts** (line 491), and says the code is **emitted** when the computation fails (lines 492–493). It then permits another Stage-C attempt in the same procedure (lines 494–497).

That leaves both ends unterminated. If a later attempt is finite and Stage C passes, the same run can acquire BS-5f and ultimately a numeric verdict after already emitting `INCONCLUSIVE-BY-COMPUTATION`. If all allowed attempts fail, the text does not say whether the run-level code was emitted on the first failure, on every failure, or only after exhaustion. There is no provisional/superseded state and no new-run rule.

The normative conduct table directly conflicts with the new route. Row J says **any locked Stage-C FAIL emits `INCONCLUSIVE-BY-POWER` and halts**, that continuing after a Stage-C FAIL voids, and that PASS is the sole route to BS-5f (line 568; corresponding antecedent at line 792). A non-finite or degenerate Stage-C computation is not excluded from “any ... FAIL.” Thus the same event is assigned `INCONCLUSIVE-BY-POWER`, `INCONCLUSIVE-BY-COMPUTATION`, and—if rerun—VOID. This violates clause 10's requirement that every branch terminate in one stated outcome (line 604).

A complete repair must distinguish per-attempt failure from the single terminal run outcome, define when the terminal code is emitted, and add an explicit Row-J branch excluded from ordinary power FAIL and `VOID-6.1J-CONTINUE-FAIL`.

### 2. HIGH / REPAIR-REQUIRED — the rerun allowance is neither reproducible nor enforceably result-blind

Line 494 permits a rerun only under the same frozen implementation and protocol digests. The pinned normative code says randomness is addressed by `SeedSequence((MASTER, stage, prefix, trial, role))` (`ref/successor_ref_v9.py` lines 30–33 and 160–161). There is no attempt index. With the same inputs and frozen addresses, a numerical rerun is bit-repetition and will reproduce the same failure; changing a seed, prefix, address, or trial stream to seek recovery creates a different random path not specified by the frozen protocol. The draft therefore does not answer the brief's forking question: the allowed repeat is either futile or an unbound fork.

The asserted safeguard is not receiptably enforceable. Line 495 says every attempt, trigger, and outcome is appended “to the §6 log on the same receipted path as any other conduct record.” The exhaustive non-χ-bearing list defines only Row B's access-log schema—timestamp, actor, table row, operation, object identity, success/refusal, refusal reason, and chain digest (lines 540–546). It has no attempt index, numerical trigger, RNG-address identity, Stage-C outcome, or protocol digest. Row B logs sealed-store touches (line 559); Row J emits only BS-5f (line 568). Section 11 adds no attempt-log schema, verifier, chain binding, or negative fixture (lines 908–920). Line 502 admits “per-attempt emission” is unimplemented but does not supply the missing contract.

Consequently an operator can label a finite result “non-finite” to claim rerun eligibility, or change the random path, without a defined verifier that recomputes and rejects the claim. A repair needs a pre-frozen attempt-indexed address schedule plus a canonical authenticated attempt schema, named producer/verifier, chain binding into terminal BS-5f/BS-L, and adversarial fixtures.

### 3. HIGH / REPAIR-REQUIRED — the acknowledged attempt cap has no BS-6 dependency edge

Line 497 correctly calls the maximum attempt count an answer-changing researcher degree of freedom and says it **must be bound before BS-6**. But none of the sixteen Class-P rows binds that parameter or its Stage-C rerun semantics (lines 708–727), and BS-6 remains only the image-transport approval (line 733). BS-2a's “retry and failure semantics” concern the acceptance/confidence mechanism, while BS-7p names randomness/serialization and fixtures but not the new attempt budget. Section 11 also omits the cap.

Thus all enumerated Class-P prerequisites can be receipted and BS-6 issued while the parameter remains unbound. Merely declaring the omission is insufficient: this recreates the exact defect the BS-3g repair was meant to cure—an asserted precondition with no dependency enforcing it. Assign the cap and full rerun contract to an explicit DESIGN Class-P slot (new or amended) that blocks BS-6, and include its schema and verifier in §11.

### 4. HIGH / REPAIR-REQUIRED — BS-3g still cannot supply a gate-readable receipt, so its BS-6 edge only appears to exist

The §7 repair now correctly names BS-3g among the DESIGN slots and makes its row Class P / UNFILLED / blocks BS-6 (lines 708 and 723). But §6.1 declares its non-χ-bearing receipt list **closed and exhaustive** and enumerates SLOT_SCHEMA receipts without BS-3g (lines 540–542). It then makes everything else χ-bearing by default (line 548), while gates and referees may inspect only the closed non-χ-bearing classes and fixtures (line 550). Section 11's SLOT_SCHEMA work likewise names BS-L, BS-2k, and deferred BS-2a, but not BS-3g (line 910).

Therefore a BS-3g receipt is, by the document's own default, χ-bearing and unavailable to the gate that must verify it before BS-6. The row exists, but the promised receipt/gate edge is not receiptable. This directly fails the brief's question whether BS-3g actually makes §1's sentence true. Add BS-3g's exact authenticated schema to the closed non-χ-bearing list and to the implementation/schema inventory, with fields sufficient to verify all seven required control elements without χ-bearing payloads.

### 5. MEDIUM / REPAIR-REQUIRED — calibration failures overlap the new computation category

Line 491 assigns aggregate non-finite/degenerate failures (apart from Row I's missing-output case) to `INCONCLUSIVE-BY-CALIBRATION`. Lines 492–493 assign any pre-unblinding “permutation, statistic or protocol computation” returning non-finite/degenerate to `INCONCLUSIVE-BY-COMPUTATION`. Calibration-aggregate validation is itself a pre-unblinding statistical/protocol computation, and the second rule does not exclude it. The same aggregate failure can therefore satisfy two run-level categories, contrary to line 488's one-outcome registry.

Define ordered, disjoint scope—for example: missing allocated output → missing-output code; invalid calibration aggregate → calibration code; only Row-J/Stage-C numerical failure → computation code.

### 6. LOW / REPAIR-REQUIRED — the repaired §2.7 evidence paragraph still points to the wrong bytes

Line 752 says Row J is at “line 552” and attributes the pre-lock disclosure clause to “§5 ... line 518.” In V40, line 552 is the phase paragraph, Row J is line 568, line 518 begins the run-guards paragraph, and the disclosure clause is in §6 at line 534. The substantive inference survives: V11 lines 266–268 say the freedom is exercised after image inference exists, V11 lines 293–294 anchor the trigger after inference exists, and the lifecycle places produced χ before unblinding. But V40 explicitly says the citations were corrected; they were not corrected to the current bytes.

### 7. LOW / ADVISORY — the referenced VOID checker does not pass its own self-test on V40

The normal `tools/void_registry.py` invocation reports 54 antecedents, 20 row names, and digest `a4d1d745b2ed33bc0e01dd39b845f88daffdc542d2bdd98d5e122ab7dd443d37`, as claimed. However, `python3 tools/void_registry.py --self-test <V40>` exits 1: its compound-gap control misses all three expected terms (`chosen`, `degenerate`, `digest`). The cause is visible in tool lines 70–73: it hard-codes the marker `- **VOID:** triggered by`, while V40 line 499 now says `triggered, **at any phase**, by`, so that heuristic silently does no work in the normal run. This does not overturn the draft's candid NAME-only limitation at line 746, but it falsifies the broader assertion that the other checker is healthy and leaves a stale control in a referenced verification tool. Repair the parser and self-test before citing that checker as a maintained guard.

## Targeted attacks that held

- **Subject identity held.** Before reading the draft I recomputed `531d3f40f06130e792ff474e660fde931038e2d7bd8e573612b90c8ec624c1f6`, exactly matching the brief.
- **Misconduct phases held.** The V39→V40 diff changes no registry row. Lines 499–500 retain forbidden acts and protocol/digest deviation at `Any`; only numerical non-finite/degenerate conditions are qualified post-unblinding. The new rules broaden the set of named forbidden rerun acts; I found no narrowing of their phase.
- **§2.7 instant held substantively.** V11 lines 266–268 and 293–294 determine “after inference exists”; current P2 instrument production precedes P7 unblinding. Commit `4d99d1d93` proves those bytes entered at V11 and its body plus model trailer are strong, though not conclusive, lane-authorship evidence. The finding is citation accuracy, not the recovered instant.
- **Counts and DESIGN inventory held.** Independent table parsing and `tools/prereg_counts.py` return 16 Class-P and 8 Class-E rows; the live §7 sentence now names BS-2a, BS-2k, BS-3g, and BS-2v. The defect is BS-3g's omitted receipt schema, not the count or subtype sentence.
- **NAME-coverage wording held.** Section 7.1 explicitly says the normal VOID checker proves NAME-coverage only and does not establish semantic coverage. The normal checker output matches 54 / 20 / `a4d1d745…`.
- **Trace and known lint posture held.** `prereg_trace.py --check` reports 39 transitions / 0 problems. `prereg_lint.py` exits 1 with exactly the quarantined `repair-citations-advisory`, which I did not count as a document finding.
- **Authorization-limit disclosure held.** V40 continues to describe the caller-path/caller-digest guard as file integrity rather than authority and leaves the typed authorization mechanism deliberately unbuilt.

## Evidence ledger and custody

Read as content: `BRIEF_V40_REVIEW.md`; the complete 920-line V40 draft; V39→V40 byte diff; V11 §2.7; both V38 referee reports; `OPEN_QUESTION_VOID_5_PHASE_SCOPE.md`; `gates/FINDINGS_MAP.md`; relevant `successor_ref_v9.py` randomness bytes; and `tools/void_registry.py` including its self-test.

Executed: subject SHA-256; `prereg_counts.py`; `void_registry.py` normal and `--self-test`; `prereg_lint.py`; `prereg_trace.py --check`; V39→V40 diff; V11 commit metadata; targeted independent searches over outcome, attempt, log, slot-schema, and BS-6 language.

I did not inspect `/Users/duhokim/NebulaMindData/`, fetch data, read image bytes, run inference, execute Stage P/C, unblind, fill a slot, alter frozen code, modify the draft, or modify any file outside this report. The only intended write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V40
VERDICT: NOT CLEAR
COUNT: 7
F1 | HIGH | REPAIR-REQUIRED | §5 lines 488–497; §6.1 lines 568, 604 | Computation failure is both a terminal run outcome and a retryable state, while Row J assigns conflicting POWER and VOID consequences.
F2 | HIGH | REPAIR-REQUIRED | §5 lines 494–496 | The rerun is either deterministic repetition or an unbound random fork, and its claimed attempt log has no authenticated schema or verifier.
F3 | HIGH | REPAIR-REQUIRED | §5 line 497; §7 lines 708–733 | The mandatory pre-BS-6 attempt cap has no Class-P dependency edge.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 540–550; §7 line 723 | BS-3g is omitted from the exhaustive gate-readable receipt schema, so its BS-6 edge is not receiptable.
F5 | MEDIUM | REPAIR-REQUIRED | §5 lines 491–493 | Aggregate calibration failures overlap INCONCLUSIVE-BY-CALIBRATION and INCONCLUSIVE-BY-COMPUTATION.
F6 | LOW | REPAIR-REQUIRED | §7.1 line 752 | The §2.7 evidence paragraph still cites the wrong lines and section.
F7 | LOW | ADVISORY | §7.1 line 746 | The referenced VOID checker passes normally but fails its V40 self-test because the revised trigger syntax disables its compound-gap heuristic.
<!-- END FINDINGS-BLOCK -->