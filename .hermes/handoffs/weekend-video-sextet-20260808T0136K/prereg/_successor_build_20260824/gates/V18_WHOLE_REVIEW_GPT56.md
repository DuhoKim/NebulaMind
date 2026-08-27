# V18 WHOLE-DOCUMENT REFEREE REPORT — GPT56

Verdict: **NOT CLEAR**. The subject digest matches, the prose-level cardinality split is genuinely disjoint, the confidence-owner and scalar/profile-precedence repairs hold, and the unbriefed Row-I abort belongs in a complete run-level registry. But the repaired registry still does not satisfy its own executable exactly-one claim: §5 assigns pre-BS-8f and fail-closed branches to `run_production_verdict()` that the pinned function cannot emit, and it classifies all non-finite/degenerate decision-input failures as calibration failures although the code raises uncategorized exceptions and some such failures are not calibration failures. The two new §10 trace entries are also not fully accurate: one omits an actual V16→V17 change, and the other invents “Blocker 6” where the repair brief has **Repair 6**.

## Digest-first identity and custody

- Subject: `../PREREG_SUCCESSOR_DRAFT_V18_20260827.md`.
- Brief-pinned sha256: `ce144dc23ba8605df1a3b7590464fc3de09c313a597168f91c80d4b29ab302f4`.
- Independently computed **before opening**: `ce144dc23ba8605df1a3b7590464fc3de09c313a597168f91c80d4b29ab302f4`.
- Result: **MATCH**. This report binds those exact bytes.
- Recomputed held predecessors: V15 `efb27c619c063f8f82c36a7930cf883c43823b8d17d0b4e63eb04d841035fb28`; V16 `1b9b9486736bf734c8cb4ac8cedf54870fd179587e3e1455273ec4724132a0da`; V17 `1a0a259a91f5a73a80fc864148e5fb6b0a2014dbf2494d243484e3948c16fce5`. All match their reviewed pins.
- Recomputed §0 pins: `successor_ref_v9.py` `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.
- V18 has 802 lines and runs through §11. Mechanical V17→V18 comparison found 11 non-equal opcodes, 17 removed lines and 37 added lines; excluding the four-line version/provenance header, this is the brief’s 50 changed lines.

## Numbered findings

### 1. HIGH / BLOCKING — the registry is disjoint in prose but not executable as the exactly-one output of `run_production_verdict()`

- **Section / lines:** §0 lines 73–104; §3 lines 388–395; §5 lines 458–473; Row I line 527; Clause 10 line 564; pinned `ref/successor_ref_v9.py` lines 1492–1496, 1500–1517 and 1591–1625.
- **What holds:** The two namespaces are disjoint by construction at the prose level. The run-level labels and the per-attempt labels have an empty string intersection; §5 explicitly says the latter are zero-or-more and never a run outcome. The per-attempt set is complete for Row P’s valid-record classifications: absence, non-finite, low-confidence and accepted-finite. Any exclusion projects deterministically to one run-level calibration outcome.
- **Failure 1 — wrong producer/phase:** §5 says `run_production_verdict()` emits exactly one run-level outcome, and includes `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT`, explicitly a **Row-I pre-BS-8f abort**. Row I terminates before BS-8f exists. The pinned function requires `cal` and a BS-5f Stage-C receipt and begins only at lines 1591–1605; it has no Row-I input or branch and cannot emit that label. The Row-I category has a reachable lifecycle antecedent, but not an antecedent in the producer to which §5 assigns the entire run-level registry.
- **Failure 2 — the newly classified fail-closed branch is not what the pinned code does:** §5 now maps “non-finite/degenerate decision inputs” to `INCONCLUSIVE-BY-CALIBRATION`. In the pinned definition, `adjudicate_path()` raises `InconclusiveByCalibration` only for a finite lower bound below 0.85. `_finite()` and `w_profile()` raise `RuntimeError` for non-finite or degenerate quantities, and `run_production_verdict()` does not catch and convert those exceptions. A non-finite permutation/statistic failure is not necessarily a calibration failure at all. Thus a reachable fail-closed code branch has no stated emitted run-level category, while the registry category’s broad prose antecedent does not match the code.
- **Why it fails:** §0 makes the pinned code the definition and prose disagreement a defect. Clause 10 requires one terminal category for every branch. A prose set can be disjoint while its asserted producer still cannot emit all members and leaves executable exceptions outside the set.
- **Smallest sufficient repair:** Scope the exactly-one claim to the **run lifecycle**, not this function, and name the producer for each pre-verdict halt; or implement a gated orchestration function that actually emits every category. Separately split non-finite/degenerate failures by phase and cause: calibration-input failure may map to calibration inconclusive, while permutation/statistic/protocol failures need their own honest fail-closed category (or a precisely defined `VOID` rule). Implement/catch those branches in the normative code or list the implementation as unresolved required work before claiming executable closure.

### 2. MEDIUM / BLOCKING UNDER §6.3 — the two new §10 trace entries are not fully accurate

- **Section / lines:** §6.3 lines 594–596; §10 lines 771–789; V16→V17 and V17→V18 mechanical diffs; `BRIEF_V17_REPAIR.md` lines 15–29; `BRIEF_V18_REPAIR.md` lines 55–73.
- **V16→V17:** The entry accurately records the restored §6.3 bodies, §4/Row-J additions, 14/8 count repair, candidate-evidence narrowing, 0.03 addition, and the three partial repairs. But the actual diff also changes Row P from citing superseded “V15 lines 570–573” to citing restored §6.3. That was an explicit half of V17 Blocker 1’s required repair and is an actual gated hunk; the new trace does not record it. The generic “§6.3 operative bodies” row describes restoration to the titles, not the separate Row-P citation change.
- **V17→V18:** The substantive changes in rows 783–787 match the actual diff: §2.7 ownership/reason repair, cardinality split plus Row-I category, calibration precedence, historical-claim deletion, both trace entries, future-trace sentence, and fold chronology. But line 786 labels its source **“Blocker 4 & 6.”** `BRIEF_V18_REPAIR.md` has Blockers 1–4 and then **Repair 5** and **Repair 6**; there is no Blocker 6. The accurate label is “Blocker 4 & Repair 6.”
- **Why it fails:** §6.3 requires the finding→change map and separately requires untraced changes to be listed. The current brief also warns that a trace misdescribing its own change is worse than a missing one. One actual hunk is omitted, and one cited finding identifier is false.
- **Smallest sufficient repair:** Add the Row-P citation change to the V16→V17 Blocker-1 row (or a separate row), and change “Blocker 4 & 6” to “Blocker 4 & Repair 6.” Do not alter the accurately described substantive changes.

## Cardinality split and Clause-10 audit, both directions

### Run-level set

Textual antecedents exist for all named labels:

- numeric regions → `REPRODUCED-LONGO`, `REJECTED-AT-LONGO-AMPLITUDE`, residual `INCONCLUSIVE`;
- Stage-C/floor failures → `INCONCLUSIVE-BY-POWER`;
- pre-unblinding low calibration or any post-unblinding removal → `INCONCLUSIVE-BY-CALIBRATION`;
- Row I’s unusable allocated output → `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT`;
- Row P’s ordered missing/duplicate/orphan/malformed accounting branches → their four named refusals;
- forbidden acts and protocol/digest deviation → `VOID`.

The ordering surfaces prevent simultaneous run labels in prose: Row P gives precedence to accounting defects; any valid-record exclusion projects to one calibration outcome; numeric regions are reached only after prior gates. The defect is executable/producer closure in Finding 1, not string-set overlap.

### Per-attempt set

The four labels are mutually exclusive classifications of a valid attempt record: absence, non-finite, low confidence, or accepted-finite. Each has a Row-P witness, and zero or more attempts may carry each label. They do not overlap the run-level namespace. Zero exclusions permits the numeric path; one or more exclusions deterministically terminates the run at calibration inconclusive without a Stage-C rerun.

### Other forward/reverse branches attacked

The following held: BS-1 A/B/date fallback; exact `<=16` versus production selection; manifest pass/refusal; the calibration-first `<0.85` halt versus admitted `>=0.85`; spread `<=0.03` scalar versus `>0.03` profile only after calibration admission; exactly 1,000 Stage-C trials; 961/962 boundary; `refuted`/`nonconservative` fail-closed behavior; Row O one-use/replay; zero versus any post-unblinding attrition; and BS-V-before-disclosure. Stage P remains openly dual-valued and BS-5p blocked rather than falsely presented as filled.

## Unbriefed Row-I abort — merits

The abort **belongs**. Row I already requires termination before BS-8f when any allocated object lacks a usable finite output, and V17’s registry had no run-level category for that reachable branch. Adding a category closes a real reverse/forward registry hole and leaks no more than Row I already expressly accepts (“at least one allocated object was missing/non-finite”). It should remain, but its producer must be the Row-I/run-lifecycle orchestrator rather than the current `run_production_verdict()` function. For lexical precision, define “missing allocated output” to mean “missing usable finite allocated output” or rename the label so its non-finite witness is not hidden.

## Threshold sweep — value, phase, failure effect

- **Calibration and path selection:** `a_LB_b < 0.85` halts pre-unblinding; equality passes. Only then does spread `<=0.03` select scalar and `>0.03` profile. V18 §3 matches `adjudicate_path()` lines 1492–1496.
- **Stage C:** `N_TRIALS = 1,000`; 962 passes and 961 fails subject to no `refuted`/`nonconservative`; failure is power inconclusive before lock/unblinding; protocol deviation is VOID. Prose matches constants 77–81 and lines 1275–1277.
- **Production decision:** 100,000 permutations; reproduction strict `p < 0.001`; rejection strict `p > 0.05`; equalities fall to residual numeric inconclusive; `A_LONGO = 0.0408`; `SIGMA_PUB = 0.011`; three-sigma bands; floor multiplier 3.09. These match pinned constants and lines 1577–1584.
- **Planning:** retention 0.8572, `L_plan = 1.2 × L_min_plan`, `N_eq >= 100,000`, and exact mode `<=16` match pinned constants.
- **Allocation:** at least 10 per non-empty joint cell and at least 30 real labels per live inherited stratum; infeasibility fails rather than shrinking.
- **Post-unblinding attrition:** zero removals proceeds; any single removal emits calibration inconclusive; no Stage-C rerun.
- **Confidence:** value intentionally unresolved; BS-2a is now the sole pre-BS-6 owner and Row P only applies it. The two remaining “reason (d)” occurrences are historical §10 trace statements, not live alternative authority.
- **Defect:** the broad non-finite/degenerate decision-input classification lacks a phase-correct failure effect and executable mapping (Finding 1).

## Overclaim and standing-state check

V18 remains explicit that it is a draft and nothing is in force; Findings 1, 2, 2b and 3 remain unresolved; BS-2a is refused/unfilled; Rows C2/E cannot run; BS-6 and the first image byte remain blocked; exact Stage P is not in the definitional code; and `verify_lock()`, the unblinding-receipt schema and associated verifiers remain required, unimplemented work. I found no new overclaim on those standing limitations. The new overclaims are limited to the executable exactly-one registry assertion and the two trace inaccuracies above.

## Failed attacks / credited repairs

1. Tried to recover live reason (d) or alternative threshold ownership: failed; only §10 historical trace occurrences remain, and BS-2a is the sole authority.
2. Tried to overlap the two registry namespaces by label or cardinality: failed; their intersection is empty and their multiplicities are explicit.
3. Tried the low-calibration plus high-spread counterexample: failed; V18 now halts at calibration before profile selection, matching the pinned code.
4. Tried the `0.85`, `0.03`, 962, `0.001` and `0.05` equality seams: their intended sides are consistent.
5. Tried to recover the fold-record chronology conflict: failed; the fold record now distinguishes instruction/initiation, verdict arrival during assembly, and final bytes after the schema repair.
6. Tried to recover the false V15→V16 “all conforming edits applied” claim: failed; it is removed.
7. Recounted §7: 14 Class-P rows and 8 Class-E rows remain consistent with the prose.

## Testimony / limits

- The raw 21:48 instruction, historical science measurements, source-citation verification, archive state and prior multi-seat refusal state were not independently re-executed. The instruction time remains Testimony; the document/report byte ordering was checked.
- Future custody, lock, unblinding, mediator, C2, Row-J and adequacy implementations remain requirements, not executed protections.
- I did not read `/Users/duhokim/NebulaMindData/`, fetch anything, inspect secrets, or touch χ-bearing material.

## Evidence ledger

Content read: `BRIEF_V18_WHOLE_REVIEW.md`; complete pinned V18; complete V17/V16 GPT56 and CODEX whole-review reports; `BRIEF_V17_REPAIR.md`; `BRIEF_V18_REPAIR.md`; whole-file V17→V18 and V16→V17 diffs; pinned v9 constants, Stage-P fail-closed region, `adjudicate_path()`, decision helper and production runner.

Independent checks: digest-first subject verification; held-draft and §0-code hashes; line count; mechanical opcode/change count; prose registry extraction and set intersection; forward/reverse Row A–S and §§0–11 branch walk; reason-(d) search; threshold/equality comparison to pinned code; and exact trace-to-diff comparison.

No source, code, draft, brief, prior report or data artifact was modified. This report is the sole write by GPT56.

**NOT CLEAR**