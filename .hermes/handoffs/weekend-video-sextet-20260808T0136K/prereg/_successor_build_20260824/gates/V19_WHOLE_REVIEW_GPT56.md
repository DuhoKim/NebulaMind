# V19 WHOLE-DOCUMENT REFEREE REPORT — GPT56

Verdict: **NOT CLEAR**. The dispatched digest matches. The lifecycle renaming correctly removes the impossible claim that one late function owns every earlier halt, and the two registry namespaces remain disjoint. But the new narrower function-level claim is still the reverse of the pinned function's actual capability, `VOID` still has no named producer, and the claimed calibration-input non-finite/degenerate branch has neither a phase-complete producer nor a failure conversion. In addition, the V16→V17 §10 trace still falsely says both slot-class counts changed when only Class E changed.

## Digest-first identity and custody

- Subject: `../PREREG_SUCCESSOR_DRAFT_V19_20260827.md`.
- Brief-pinned sha256: `b7deb106eb81b3e13376e7049263b355ba90982656f7de30964c0d3bfda5e63b`.
- Independently computed **before opening**: `b7deb106eb81b3e13376e7049263b355ba90982656f7de30964c0d3bfda5e63b`.
- Result: **MATCH**. This report binds those exact bytes.
- Recomputed predecessors: V16 `1b9b9486736bf734c8cb4ac8cedf54870fd179587e3e1455273ec4724132a0da`; V17 `1a0a259a91f5a73a80fc864148e5fb6b0a2014dbf2494d243484e3948c16fce5`; V18 `ce144dc23ba8605df1a3b7590464fc3de09c313a597168f91c80d4b29ab302f4`. These match the revision provenance.
- Recomputed §0 pins: `ref/successor_ref_v9.py` `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `ref/closure_worker_v9.py` `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.

## Numbered findings

### 1. HIGH / BLOCKING — the renamed lifecycle registry still overclaims unchanged producer capability

- **Section / lines:** §0 lines 73–104; §3 lines 388–395; §5 lines 458–475, especially 469, 471 and 473; Rows I/J/P lines 529–536; Clause 10 line 566; §11 lines 802–810. Pinned `ref/successor_ref_v9.py` lines 1446–1496, 1500–1557 and 1591–1625.
- **What the naming repair genuinely fixes:** Line 466 now defines one outcome per study run, not per function call. Row J is correctly named for the pre-unblinding power and finite-low-calibration branches; Row I is named for its pre-BS-8f missing/invalid allocated-output abort; Row P has the ordered post-unblinding accounting and per-attempt branches; the numeric helper has the three mutually exclusive numeric regions. The per-attempt registry remains disjoint and its four states have Row-P antecedents.
- **Failure 1 — line 473 is false under the document's own code-precedence rule.** It says `run_production_verdict()` can actually return numeric verdicts, post-unblinding accounting refusals, post-unblinding calibration halts, and `VOID`. The pinned function accepts only `mask`, `cal`, authorization/count arguments and a Stage-C receipt. It has no BS-L, unblinding-receipt, adequacy-receipt, terminal-partition or final-mask input and no accounting validator. Its only literal early return is `INCONCLUSIVE-BY-POWER` (reference lines 1610–1616), which line 473 omits. It can then return the numeric helper's result. It cannot return any accounting label or `VOID`; low calibration raises `InconclusiveByCalibration` rather than returning a verdict. Thus the supposedly narrowed claim lists outcomes the function cannot return and omits one it does return.
- **Failure 2 — `VOID` still has no named producer.** V19 line 466 promises the producing phase or process for each lifecycle category. Numeric, Row-I, Row-J and Row-P categories name one. Line 471 only says what triggers `VOID`; it names no process that detects, records, authenticates or emits it. `VOID` appears nowhere else in V19 except line 473's false runner-return claim. Forbidden acts can arise throughout Rows A–S, while permutation/statistic failures arise in the late runner, so a trigger list is not a producer or a receiptable phase.
- **Failure 3 — calibration-input non-finite/degenerate handling is asserted closed without a producer or conversion.** Line 469 appends that cause to `INCONCLUSIVE-BY-CALIBRATION`, but unlike the adjacent Row-J and pre-verdict-validator branches it names no producer. Row J line 530 only tests `< 0.85`; a NaN makes that comparison false. `accuracy_from_handcheck()` does not comprehensively reject non-finite inputs and can produce NaNs; `adjudicate_path()` likewise lets a NaN lower bound miss the `< 0.85` branch. Later `_finite()`, `w_profile()` and sigma helpers raise uncategorized `RuntimeError`s. V19 honestly marks permutation/statistic conversion unresolved at line 471, but does not mark the calibration-input conversion unresolved or put it in §11.
- **Why it fails:** §0 says pinned code defines mechanisms and prose disagreement is the prose defect. Clause 10 requires every branch to terminate in a stated outcome. V19 repaired ownership vocabulary but not the claimed function capability, and it still lacks an emitting phase for two newly distinguished failure surfaces. This is exactly a correct-sounding name over unchanged capability.
- **Smallest sufficient repair:** Replace line 473 with an honest current-capability statement (numeric results plus its existing power return, while explicitly listing accounting, calibration-return and `VOID` conversion as unresolved code work), or implement and gate the required inputs/validators/conversions before claiming them. Name a canonical producer/receipt point for `VOID`. Name and specify the producer that validates calibration aggregates as finite/nondegenerate before the `<0.85` comparison, including its emitted authenticated outcome, and add that implementation/fixture to §11. Do not invent an orchestration symbol unless its contract is actually specified.

### 2. MEDIUM / BLOCKING UNDER THE DOCUMENT'S TRACE LAW — V16→V17 still overstates the count repair

- **Section / lines:** §6.3 lines 596–598; §10 lines 773–795, especially line 778; actual V16 line 636 and V17 line 669.
- **Evidence:** V19's V16→V17 row says, “Repaired the Class P and Class E counts in §7 to match the table.” The exact V16 and V17 bytes both say **one of fourteen Class-P slots is filled**. The only count edit is Class E, from **7** in V16 to **8** in V17. The V16 referee finding itself says the parsed Class-P count already agreed and only the Class-E count failed closure.
- **Why it fails:** §6.3 requires a finding→change map, and the brief requires all three entries to match what actually changed. This row claims a Class-P count repair that did not occur and was not needed.
- **Smallest sufficient repair:** Change the row to “Repaired the Class E count in §7 from 7 to 8; the already-correct Class P count remained 14.”

## Lifecycle registry and Clause-10 audit, both directions

### Run-level categories

- **Numeric helper:** `REPRODUCED-LONGO`, `REJECTED-AT-LONGO-AMPLITUDE`, residual `INCONCLUSIVE` — reachable, mutually exclusive, and matched by pinned decision lines 1579–1584.
- **Row J:** finite `a_LB_b < 0.85` → calibration inconclusive; Stage-C failure, fewer than 962/1,000, or self-verification failure → power inconclusive. These phase assignments hold at document-contract level; implementation remains openly required in §11.
- **Row I:** missing/unusable finite allocated output has the named pre-BS-8f lifecycle category. The category belongs, although Row I's emission/receipt wording should be made explicit when implemented.
- **Row P:** missing, duplicate, orphan and malformed accounting refusals have ordered antecedents. Valid attempts partition into absence, non-finite, low-confidence and accepted-finite. Any exclusion deterministically yields one calibration-inconclusive run outcome; zero exclusions permits continuation.
- **`VOID`:** trigger antecedents exist, but reverse producer reachability fails because no producer/phase is named (Finding 1).
- **Non-finite/degenerate surfaces:** permutation/statistic handling is honestly disclosed as unresolved; calibration-input handling is not phase-complete (Finding 1).

The namespace intersection remains empty. Earlier halts precede Row P and numeric evaluation, Row-P accounting precedence precedes attempt classification, and any attempt exclusion stops before numeric evaluation, so I found no multiple-run-outcome overlap in the prose ordering.

## Threshold sweep — value, phase, failure effect

- Release fallback date 2026-09-05; catalog cuts; retention 0.8572; exact-mode boundary `<= 16`; `L_plan = 1.2 × L_min_plan`; and `N_eq >= 100,000` remain seated in their planning/acquisition phases.
- Confidence threshold value remains intentionally unresolved and solely owned by refused BS-2a before BS-6. Row P only applies it; below threshold → `EXCLUDED-BY-CONFIDENCE` → calibration-inconclusive run.
- Calibration floor: finite `< 0.85` halts pre-unblinding; equality belongs to the admitted `>= 0.85` side. Spread is tested only after that admission: `<= 0.03` scalar, `> 0.03` profile, with profile not a failure.
- Stage C: exactly 1,000 trials; 962 passes and 961 fails, subject to no `refuted`/`nonconservative` fail-closed return. Failure occurs before lock/unblinding; protocol deviation is intended to void, with the producer defect in Finding 1.
- Production: 100,000 permutations; reproduction strict `p < 0.001`; rejection strict `p > 0.05`; equality cases fall to residual numeric inconclusive; target 0.0408; public sigma 0.011; three-sigma bands; detection-floor multiplier 3.09.
- Calibration allocation: at least 10 per non-empty joint cell and at least 30 labels per live inherited stratum; infeasibility fails rather than shrinking.
- Post-unblinding attrition: zero removal may continue; any one or more removals gives calibration inconclusive with no Stage-C rerun.
- The unresolved phase/cause effect for non-finite/degenerate inputs is the defect in Finding 1; I found no additional threshold-side contradiction.

## §10 trace verification

- **V16→V17: NOT fully accurate.** The restored §6.3 bodies, Row-P citation replacement, §4/Row-J additions, Class-E 7→8 repair, candidate-evidence narrowing, 0.03 addition and listed partial repairs all appear in the diff. The Class-P count-repair claim is false (Finding 2).
- **V17→V18: accurate against the byte diff.** It records the BS-2a ownership/reason repair, registry cardinality split plus Row-I category, calibration precedence, historical-claim deletion, trace additions/future requirement and chronology change. “Blocker 4 & Repair 6” is now the correct label.
- **V18→V19: accurate as a description of the textual hunks.** The lifecycle naming, category annotations, line-473 emitter sentence, non-finite prose split and trace edits all appear. Its substantive assertion that the narrowed runner set is what the function can actually return fails independently under Finding 1.

## Failed attacks / credited repairs

1. Tried to relocate the V18 ownership defect without fixing it: the lifecycle-level renaming itself holds; earlier Row-I and Row-J outcomes are no longer assigned to the late runner merely because they are registry members.
2. Tried to overlap run-level and per-attempt namespaces: failed; their string sets and cardinalities remain disjoint.
3. Tried to orphan any Row-P accounting or valid-attempt classification: failed; all eight ordered Row-P states have antecedents and fixed consequences.
4. Tried the low-calibration/high-spread and equality seams: failed; calibration precedence and the `0.85`/`0.03` boundaries remain consistent.
5. Tried the 961/962, `p == 0.001`, and `p == 0.05` seams: their intended sides remain explicit and code-consistent.
6. Tried to recover alternative confidence-threshold ownership: failed; BS-2a remains the sole authority and is openly refused/unfilled.
7. Recounted §7: 14 Class-P and 8 Class-E rows match V19's live prose; the defect is only the historical trace's claim about what V16→V17 changed.
8. Verified the V16→V17 Row-P citation and partial-repair trace additions requested by V18: they are now present.
9. Standing limitations remain disclosed: Findings 1, 2, 2b and 3 unresolved; BS-2a refused; Rows C2/E blocked; BS-6 and first image byte blocked; exact Stage P not in definitional code; `verify_lock()` and unblinding-receipt machinery required, not implemented.

## Testimony / limits

- The 21:48 instruction/initiation, historical measurements, source citation, archive state and prior seat decisions were not independently re-executed. They remain Testimony where relied upon.
- Future mediator, C2, Row-J, lock, unblinding, adequacy and schema mechanisms were reviewed as document requirements, not executed protections.
- I did not read `/Users/duhokim/NebulaMindData/`, fetch anything, inspect secrets, or touch χ-bearing material.

## Evidence ledger

Content read: `BRIEF_V19_WHOLE_REVIEW.md`; complete exact V19; exact V16/V17/V18/V19 pairwise diffs; V18 whole-review reports for the prior finding definitions; relevant V16 count finding; pinned v9 calibration, path adjudication, sigma, decision-helper and production-runner regions.

Independent checks: digest-first V19 verification; predecessor and §0-code hashes; complete outcome-token inventory; producer/phase mapping for every run-level category and per-attempt state; forward/reverse Clause-10 walk across Rows A–S and §§0–11; threshold/equality sweep; §7 recount; all three trace-to-diff comparisons; and exact runner-input/return inspection.

No source, pinned code, draft under review, prior report, brief or data artifact was modified. This report is GPT56's sole authorized write.

**NOT CLEAR**