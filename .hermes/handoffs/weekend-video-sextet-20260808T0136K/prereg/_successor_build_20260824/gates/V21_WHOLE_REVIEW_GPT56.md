# V21 WHOLE-DOCUMENT REVIEW — GPT56

## Verdict

V21 is **NOT CLEAR**. It correctly repairs V20's false present-tense runner-guard sentence and it does place a second, separately named `VOID` prerequisite on BS-6 in §7. But that insertion creates a false §7 count/lint assertion, the new prerequisite is not yet specified as a receiptable slot, and “branch-complete fixtures” has no closed antecedent inventory or coverage condition by which a gate can fail an incomplete fixture set. In addition, §5's extended unresolved-work list and §11 still omit the exact final-mask/adequacy-validator work explicitly required in the immediately preceding sentence. V21 is substantially more honest and remains a potentially sound unfinished programme, but these are contract defects in the unfinished-programme boundary itself.

## Subject identity — verified before opening

I first compared the SHA-256 computed from the live bytes of `../PREREG_SUCCESSOR_DRAFT_V21_20260827.md` with the brief's required digest `8386d5f0b3cdc8ed4161545dbcf2f8e4898c9c68942ddfc117b3103ef6ea10e5`.

`shasum -a 256` returned:

`8386d5f0b3cdc8ed4161545dbcf2f8e4898c9c68942ddfc117b3103ef6ea10e5  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V21_20260827.md`

Result: **MATCH**. I opened V21 only after that comparison.

I separately compared the live V20 bytes with V21's banner pin. The computed V20 SHA-256 was `607df3dd5b022a299162dac501b9c5766dda87bac8b3ba1cea11a105efa00261`: **MATCH**. The live reference pins also matched §0: `successor_ref_v9.py` returned `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`, and `closure_worker_v9.py` returned `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.

## Numbered findings

### 1. HIGH / BLOCKING — §7 lines 664–703: the new `VOID` dependency is present, but §7's count is now false and the prerequisite is not receiptable as written

**What held.** The pre-BS-6 dependency is real at the prose dependency-graph level. The new row at line 680 is explicitly `DESIGN, CLASS P — UNFILLED`, its `blocks` cell is `BS-6`, and the surrounding §7 heading defines Class P as freeze prerequisites. Clause 10 line 567 independently says BS-6 and the first image byte remain blocked on this ground. This is a second reason, distinct from BS-2a.

**Why it still fails.** I parsed the Class-P table between its heading and the Class-E heading and counted **15 data rows**, exactly one marked filled (BS-2m). Line 672 still says “One of fourteen class-P slots is filled” and asserts that prose count equals parsed table count. Before V21 there were 14 rows; V21 added the `VOID` converter row without changing the count. The assertion is therefore mechanically false.

The added row also has no slot identifier, no producer, no code symbol, no receipt/schema, and no explicit gate output. That matters because V21 line 61 says the draft becomes a preregistration only when every Class-P slot holds a receipt, and Clause 3(b) line 550 requires BS-L to bind the ordered manifest of every Class-P slot receipt. A row literally named ``VOID` converter` with producer `—` cannot satisfy those receipt requirements as written. It conservatively blocks BS-6, but it is not a fillable/receiptable dependency contract.

**Smallest sufficient repair.** Change the count to **15** and preserve “one filled.” Give the converter a stable slot ID and define its producer-of-record, canonical receipt/schema, pinned implementation digest, branch-coverage manifest, gate report, and fill condition. Then make BS-6 require that passing receipt, rather than relying only on a free-text `blocks` cell.

### 2. HIGH / BLOCKING — §6.1 Clause 10 line 567, §7 line 680, §10 line 814, §11 line 833: “branch-complete fixtures” is not specified tightly enough to fail an incomplete fixture set

**Why it fails.** The four new/changed locations consistently require a converter to handle “every enumerated void antecedent” and require “branch-complete fixtures.” But V21 supplies no canonical, closed, machine-readable antecedent inventory; no stable antecedent IDs; no one-to-one coverage rule; no expected fixture count; no assertion that extra/missing/duplicate antecedent IDs fail; and no required report field proving closure.

The source universe is not a single short enumeration. §5 groups `VOID` triggers as forbidden acts, protocol/digest deviations, and permutation/statistic/protocol non-finite or degenerate failures; §6.1's table has row-specific “what voids the run” cells; §6.1 Clause 5 adds out-of-table access; and §6.3 adds post-first-real-χ binding changes. “Every enumerated void antecedent” does not say whether the gate enumerates category labels, every table cell, every semicolon-separated branch, or executable branch sites. A fixture author can therefore call a subset “branch-complete” without violating a machine-checkable cardinality or set-equality rule.

This is exactly the brief's incomplete-fixture attack: the words request completeness, but nothing makes an incomplete fixture set fail.

**Smallest sufficient repair.** Add a canonical closed antecedent registry with stable IDs and exact source/phase/failure-effect for each `VOID` branch. Require the converter gate to compare `set(fixture.antecedent_id)` and `set(converter.branch_id)` by exact set equality against that registry, refusing missing, extra, duplicate, or unreachable IDs. Bind the registry, converter, fixtures, and returned coverage manifest by SHA-256 in the new Class-P receipt.

### 3. MEDIUM / BLOCKING — §5 lines 462–474 and §11 lines 824–833: the extended unresolved implementation inventory still omits the exact final-mask/adequacy guard named in the adjacent sentence

**Why it fails.** Line 462 honestly labels five guards as required but unimplemented: (1) BS-L verification, (2) one-use unblinding-receipt verification, (3) exact final-mask binding, (4) post-unblinding ledger recomputation, and (5) refusal before any statistic when the adequacy tree emits `INCONCLUSIVE`.

Line 474 adds the first two by name, but the remaining list uses only the broad labels “accounting” and “post-unblinding calibration return.” Those do not explicitly require exact final-mask binding, recomputation of the post-unblinding ledger from evidence, or the pre-statistic adequacy-tree refusal. The whole-document occurrence comparison reinforces the gap: `final-mask`, `post-unblinding ledger`, and `adequacy tree` occur in the required-but-unimplemented sentence (and Row P supplies the desired receipt content), but §11 has no implementation item for the Row-P exact-parent validator/ledger recomputation/final-mask verification and no negative fixture proving that an adequacy `INCONCLUSIVE` makes statistic formation unreachable. §11's `recompute_acceptance_ledger` item is Row C2/E pre-lock work, not Row P's post-unblinding recomputation.

The pinned source confirms this is real missing work, not only wording. Its SHA matched `6a9abbbd…`; the AST of `run_production_verdict()` at lines 1591–1625 returned arguments `mask`, `cal`, `authorization_path`, `authorization_sha256`, `n_receipts`, `n_parent`, and `stage_c_receipt`, and no lock, unblinding, final-mask, ledger, or adequacy input/call.

**Smallest sufficient repair.** Extend line 474 and §11 with a named post-unblinding adequacy validator that authenticates the receipt, independently recomputes the exact-parent terminal partition and final-mask digest from pinned evidence, checks exact binding to the mask passed to the runner, and refuses before `perm_record()` on every non-passing adequacy branch. Require positive and negative fixtures, including an `INCONCLUSIVE` receipt that proves no statistic call occurs.

## V20→V21 changed-line and neighbour audit

A line-sequence comparison returned **9 non-equal hunks, 7 old lines, 18 new lines, 25 changed lines total**, matching the brief's 25-line statement. I inspected six context lines on both sides of every hunk.

- **Banner hunk, lines 1–6:** V21/V20 identity and pin are correct. The new repair summary is directionally accurate, but “VOID reachability [is] repaired” is stronger than the under-specified fixture/receipt contract in Findings 1–2.
- **§5 guard hunk, lines 459–467:** both neighbours held. The preceding exact call list remains source-true; the following `N_eq`/permutation sequence remains source-true. The changed sentence is now explicitly required-but-unimplemented and no longer falsely claims those guards exist.
- **§5 unresolved-list hunk, lines 469–478:** the exact return inventory remains true; the neighbouring run-level/per-attempt partition remains intact. Finding 3 records the residual inventory gap.
- **Clause-10 hunk, lines 561–571:** Clauses 7–9 and §6.2 remained unchanged. The inserted unresolved status correctly avoids implying closure and directly blocks BS-6.
- **§7 row hunk, lines 674–686:** the adjacent BS-2a, BS-2k, BS-2c, BS-2o, and BS-5p dependencies remained unchanged. Findings 1–2 arise from the inserted row and its unchanged count sentence above.
- **§10 V19→V20 correction hunk, lines 799–807:** the new wording accurately weakens “producer” to validator/authenticated aggregate outcome and matches the actual V19→V20 §5/§11 additions.
- **§10 V20→V21 hunk, lines 810–817:** all three rows accurately describe the bytes changed. Their semantic completeness fails only as specified in Findings 1–3.
- **§11 hunk, lines 824–833:** neighbouring aggregate validation remains explicitly future work. The `VOID` item is future work and pre-BS-6, but lacks the closure contract in Finding 2 and the list lacks Finding 3's Row-P validator.

I found no unrelated V20→V21 body edit.

## Central capability ruling

The V21 repair of §5's immediate V20 blocker holds. I parsed the exact pinned source and compared the runner plus helper against V21 lines 459–474:

- `run_production_verdict()` return sites were source lines **1611, 1615, and 1625**.
- Its direct verdict literal set was exactly `INCONCLUSIVE-BY-POWER`.
- `_decide_from()` returned exactly `REPRODUCED-LONGO`, `REJECTED-AT-LONGO-AMPLITUDE`, and `INCONCLUSIVE`.
- Whole-source counts for `verify_lock`, `verify_unblinding_receipt`, `VOID`, `validate_calibration_aggregates`, `INCONCLUSIVE-BY-MISSING-RECORD`, and `EXCLUDED-BY-ABSENCE` were all **0**.

Result: line 474's exact return-value sentence is true, and line 462 now honestly marks the additional guards unimplemented. I found no remaining present-tense claim in §5 or §11 that those new orchestration capabilities already exist; §11 consistently uses “Add,” “Require,” and “Implement.” Finding 3 concerns completeness of the unresolved inventory, not a false present-tense implementation claim.

## Clause 10 and threshold audit, both directions

I read §§0–11 forward (branch → outcome) and backward (outcome → antecedent/phase), expecting `VOID` to be explicitly unresolved.

- **`VOID`: intended unresolved state is explicit.** §5 says it is not executable; line 474 lists conversion as unresolved; Clause 10 says reverse reachability and Clause 10 executability are unresolved; §7 makes it Class-P/unfilled and blocks BS-6; §11 calls for implementation. This is honest unfinished status. Findings 1–2 concern the malformed/incomplete prerequisite contract, not hidden closure.
- **Numeric decision, P8:** source constants `P_REPRODUCED=0.001`, `P_REJECT_MIN=0.05`, `FLOOR_MULT=3.09`, and helper lines 1579–1584 match §5: strict `p < 0.001` plus sign/band/floor reproduces; strict `p > 0.05` plus amplitude band rejects; complement is numeric inconclusive.
- **Calibration, P5 before Stage C/statistic:** source `A_FLOOR=0.85` and `adjudicate_path()` lines 1492–1496 match the prose: `<0.85` halts; on the complement `<=0.03` selects scalar and `>0.03` selects profile. Profile is not a failure. The lifecycle conversion remains disclosed as unimplemented.
- **Stage P/C:** source `N_TRIALS=1_000`, `CP_PASS_X=962`, and lines 1275–1277 match the prose: `refuted` or `nonconservative` fails closed; otherwise 1,000 trials pass iff successes are `>=962`. The document separately discloses that its preferred exact Stage-P route is not in the definitional code.
- **Production `N_eq`:** source `NEQ_MIN=100_000` and lines 1613–1616 match the prose: `<100,000` returns `INCONCLUSIVE-BY-POWER`; equality passes.
- **Row I / Row P:** the prose gives phases and fixed effects for missing allocated output, accounting refusals, and post-unblinding attrition. Whole-source scans returned no corresponding implementation names, and V21 marks that work unresolved; Finding 3 identifies the incomplete implementation inventory.

No threshold value, phase, or inequality direction changed in V21. I found no new threshold inversion.

## §10 repair-trace audit — all five entries

I compared complete adjacent line sequences with `difflib.SequenceMatcher(autojunk=False)` and inspected the returned hunks. Counts were: V16→V17 **14 hunks, 27 old/60 new**; V17→V18 **13, 15/35**; V18→V19 **8, 11/19**; V19→V20 **8, 7/19**; V20→V21 **9, 7/18**.

1. **V16→V17 — ACCURATE in V21.** The diff restored §6.3 operative bodies and Row-P citation, added §4 calibration/pre-attrition handling, changed only Class E 7→8 while Class P stayed 14, narrowed candidate evidence, and added the 0.03 spread rule.
2. **V17→V18 — ACCURATE.** The diff removed disjunctive threshold ownership/stale reason (d), made calibration precede spread, split run outcomes from attempt states with Row-I abort, repaired chronology, and added the traces.
3. **V18→V19 — ACCURATE.** The diff rewrote the lifecycle registry with named producers, narrowed the runner claim at that stage, split non-finite causes, and repaired the prior trace descriptions/label.
4. **V19→V20 — ACCURATE after V21's correction.** The diff added both runner power producers, declared `VOID` non-executable, inserted the exact return inventory, corrected the Class-E-only trace, and added aggregate validation as required future work. V21's corrected E row now matches the added validator/outcome wording rather than falsely calling it the producer.
5. **V20→V21 — BYTE-ACCURATE, SEMANTICALLY INCOMPLETE.** The diff contains every edit the three trace rows claim. Findings 1–3 show what the trace does not establish: correct Class-P closure/count, a mechanically complete fixture contract, and a complete unresolved guard inventory.

## Failed attacks / points that held

- Digest attack failed: V21, V20, and both §0 code pins matched exactly.
- Central return-inventory attack failed: the AST returned only the three numeric helper outcomes plus the runner's two power branches.
- Adjacent false-present-tense attack failed in §5/§11: the V20 guard claim is now explicitly unimplemented and §11 remains future imperative work.
- Clause-10 concealment attack failed: V21 plainly states `VOID` reverse reachability is unresolved and Clause 10 is not executable.
- Missing-BS-6-link attack failed at the prose graph level: §7's new Class-P row directly blocks BS-6, and Clause 10 repeats the block.
- Threshold inversion attack failed: values, strictness/equality, phases, and stated failure effects remain aligned with the pinned source where implemented.
- V19→V20 trace-overclaim attack failed after V21's wording correction.

## Testimony / unverified assertions

I did not promote the following to mechanical findings: Longo bibliographic/quotation claims; historical fold times and prior-seat chronology; real-geometry and Stage-P measurement values; historical fixture and closure-reproduction counts; authorization history; or custody/immutability claims for old gates beyond the hashes computed here. Those remain **Testimony**.

I did not read `/Users/duhokim/NebulaMindData/`, fetch anything, run real data, inspect secrets, or modify the reviewed draft or code.

## Evidence ledger and constraints

Content read:

- `gates/BRIEF_V21_WHOLE_REVIEW.md`, all 63 lines.
- `PREREG_SUCCESSOR_DRAFT_V21_20260827.md`, all 833 lines, only after digest match.
- The complete V20→V21 unified diff with six context lines, covering every changed line and both-side neighbours.
- `ref/successor_ref_v9.py` decision/power/calibration regions, including lines 1188–1282 and 1485–1659.
- V16–V21 through complete adjacent line-sequence diffs needed for the five §10 trace entries.
- The two V20 reports as historical inputs-to-attack, not ground truth.

Mechanical comparisons/results:

- Absolute `cd` + `pwd`: returned the assigned gates directory.
- SHA-256 comparisons: V21, V20, and both code pins matched the values recorded above.
- V20→V21 sequence diff: 9 hunks, 7 old lines, 18 new lines, 25 total changed lines.
- Class-P table parse: 15 data rows, one filled; prose says 14.
- AST runner/helper parse: argument, call, return-site, and verdict-literal sets recorded above.
- Source occurrence checks: all six named unimplemented orchestration/outcome symbols returned zero occurrences.
- Five adjacent version comparisons: hunk/change counts and trace results recorded above.
- Threshold/source comparison: constants and branch lines recorded in the Clause-10 section.
- Pre-write report-path status: absent/clean at that path.

The only authorized write was this report.

**NOT CLEAR**