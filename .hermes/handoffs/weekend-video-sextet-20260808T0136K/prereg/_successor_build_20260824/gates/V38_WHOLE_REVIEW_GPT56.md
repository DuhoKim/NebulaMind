# V38 whole-document referee — GPT56

## Verdict

**NOT CLEAR.** The dispatched subject matches the required SHA-256, the §2.7 instant recovery holds against V11's own bytes, BS-3g creates the missing BS-6 dependency edge, the 16/8 recount is real, the VOID checker is accurately limited to NAME-coverage, and the newly candid authorization paragraph matches the frozen code. But the 15/8 → 16/8 edit left a live §7 inventory sentence stale: line 701 says the DESIGN slots are BS-2a, BS-2k, and BS-2v, while the new BS-3g row at line 716 is explicitly a fourth DESIGN slot. A preregistration cannot simultaneously define DESIGN as answer-changing work requiring a new revision/gate and omit one such slot from its current DESIGN inventory.

## Finding

### 1. MEDIUM / REPAIR-REQUIRED — §7 line 701 omits BS-3g from the current DESIGN inventory

Line 701 says, in present tense, “On today's count: **BS-2a, BS-2k, and the `BS-2v` VOID converter are DESIGN slots.**” Independent parsing of the Class-P table finds four rows marked DESIGN:

- line 707: BS-2a — `DESIGN, CLASS P — UNFILLED`
- line 708: BS-2k — `DESIGN`
- line 709: BS-2v — `DESIGN, CLASS P — UNRESOLVED`
- line 716: BS-3g — `DESIGN, CLASS P — UNFILLED`

This is not a historical quotation. It is the live §7 classification immediately above the operative table, and its preceding sentence defines the consequence of that classification: filling a DESIGN slot requires a new text revision and fresh text gate rather than receipt insertion. The row-count tools do not catch the defect: `prereg_counts.py` reports 16/8 and says the prose matches because it checks class counts, not the DESIGN-name inventory; `prereg_lint.py` likewise reports 16/8 and only the quarantined citation advisory. The V36→V37 diff shows the regression directly: the class count changed from fifteen to sixteen and BS-3g was inserted, but the three-name DESIGN sentence was left byte-identical.

Smallest sufficient repair: add BS-3g to line 701's current DESIGN-slot inventory and re-run the count, trace, registry, and lint checks. Do not change its UNFILLED status or the 16/8 count.

## Targeted attacks that held

1. **Subject identity held.** Before reading V38 I recomputed `b5776d287a22cff71fe34d1ee1dbe937f1af61d51ad70530f378668cbfe1ec56`, exactly matching the brief.

2. **The §2.7 instant recovery held.** V11 lines 264–294 are the relevant authorship bytes. They say the dangerous acceptance freedom is exercised “after image inference exists” (lines 266–271), immediately fix the rule “before any image byte” (line 273), and state that a threshold chosen or moved “after inference exists” voids the run (lines 293–294). In that context, image inference existing means that real image-inference output exists; the first such output is the first real χ. Current phase ordering independently places instrument inference at P2 and stores its χ-bearing receipts before P3–P6 and unblinding (V38 lines 545, 555). Thus `Post-first-real-χ`, not `Post-unblinding`, recovers the authored trigger. Commit `4d99d1d93c14351cfc54b5ffeb841f3be5cd7de5` contains V11 as the sole added file and its commit message identifies §2.7 as the repair for GPT56 F2 and CODEX 1. I found no evidence that the phase should move.

3. **BS-3g's dependency edge held.** Section 1 line 120 requires seven design elements to be bound before BS-6 and now points to BS-3g. The new Class-P row at line 716 names all seven—statistic, sample, positional stratification, uncertainty, bound, acceptance rule, and failure consequence—and its `blocks` cell is BS-6. It also says the slot is UNFILLED, the completeness fork is open, γ̂ is unmeasured, and the row does not license an image byte. Both cited gain-v6 reports are scoped CLEAR reports and explicitly preserve the T-completeness fork; the live estimator and verifier hashes recompute to the prefixes quoted at line 716. This makes the §1 precondition enforceable at document-contract level without pretending it is filled.

4. **The 16/8 class move itself held.** Independent table parsing and `tools/prereg_counts.py` both produce 16 Class-P and 8 Class-E rows, with BS-2m the only claimed filled Class-P slot. `tools/prereg_trace.py <lane> --check V38` reports 37 computed transitions and 0 problems. Recomputed predecessor hashes match the brief: V36 `e4d7b175ac270f4cdc0bc4af3a16af0e834aa3e4eacc174a73d10798cd4b6177`; V37 `62dd8a7525c399126477573d55a952f1ed2f147d16f8bfbb12aa89a295821c42`. I found no code-side hard-coded expectation of 15 Class-P rows. The only live break is finding 1's stale DESIGN-name sentence.

5. **The §7.1 checker-scope claim held.** `tools/void_registry.py` reports 54 antecedents, 20 §6.1 rows, digest `a4d1d745b2ed33bc0e01dd39b845f88daffdc542d2bdd98d5e122ab7dd443d37`, plus two expressly advisory compound-subject candidates. V38 lines 737–745 distinguish the registry's substantive claim from what the checker proves and repeatedly limit the machine result to NAME-coverage. I parsed every row's forbidden column against its row-prefixed antecedents: A through S each has a one-for-one semantic match for every listed forbidden branch. The three repaired prose gaps are separately represented as `VOID-5-DEGENERATE`, `VOID-5-DIGEST-DEVIATION`, and `VOID-2.7-THRESHOLD-CHOSEN-OR-MOVED`. I found no surviving semantic overclaim hidden behind the NAME-coverage wording.

6. **The authorization walk-back held.** Frozen `ref/successor_ref_v9.py` recomputes to the §0 pin `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`. Its lines 1636–1644 only hash the caller's path, compare it with the caller's expected digest, and return it. V38 lines 511–523 now say exactly that, explicitly deny schema/signer/study/run/operation custody, and keep the mechanism unbuilt and blocked. The paragraph no longer presents file integrity as authority.

7. **Absence-clause attack did not expose another new defect.** I tested the live universal negatives against their declared construction, slot, schema, or refusal consequence rather than crediting their wording. The known unfinished mechanisms remain identified as required/unimplemented or DESIGN/UNFILLED, and BS-6 plus the first image byte remain blocked. I did not re-derive the quarantined citation advisory or the decided gain-control fork, as instructed.

## Evidence and custody

Read as content: the complete 909-line V38 draft; `BRIEF_V38_REVIEW.md`; V11 lines 255–294; V36 and V37 through byte diffs and hashes; `DECISIONS_FOR_DUHO.md`; `OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md`; `OPEN_QUESTION_VOID_2.7_PHASE.md`; `OPEN_QUESTION_T_COMPLETENESS.md`; `LANE_STATE_20260829.md`; `SELF_CONTINUATION_ORDERS.md`; `gates/FINDINGS_MAP.md`; gain-v6 GPT56/CODEX reports; and `ref/successor_ref_v9.py` lines 1628–1649. I recomputed the draft, predecessor, reference-code, BS-2a, and gain-control hashes; ran `prereg_counts.py`, `void_registry.py`, `prereg_lint.py`, and the correctly scoped `prereg_trace.py --check`; and independently parsed the Class-P DESIGN rows and the §6.1 forbidden-column/registry mapping.

I did not read `/Users/duhokim/NebulaMindData/`, fetch any image or catalogue datum, execute a study run, modify frozen code, modify the draft, or write outside this report. The linter's sole `repair-citations-advisory` is the brief's known quarantined result and was not counted as a document finding.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V38
VERDICT: NOT CLEAR
COUNT: 1
F1 | MEDIUM | REPAIR-REQUIRED | §7 line 701 | Live DESIGN-slot inventory omits newly added DESIGN slot BS-3g
<!-- END FINDINGS-BLOCK -->