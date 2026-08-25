# GPT56 referee gate — successor preregistration V9 (round 8)

## Recommendation

**REVISE.** Four stated guarantees fail: the production manifest-closure entry point does not call the frozen planner; the reported 6,445-brick result is not shown to be the frozen selection chain's output; Stage P does not self-confirm most counted successes or establish that one reference null is conservative for all trials; and the count-oracle completeness proof remains self-referential and optional in code.

## Custody digests — computed before review

Command: `shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V9_20260825.md ../ref/successor_ref_v4.py ../ref/FIXTURES_V4_20260825.out`

- `../PREREG_SUCCESSOR_DRAFT_V9_20260825.md` = `b97ba35c8d1eeb66cc44e6915d2ae752fd19c374ff4906c9d15b8518056919b6`
- `../ref/successor_ref_v4.py` = `ffea5b6c58956c1f6c2e44939113f5170e459e566d132e8e3f69d117344e657b`
- `../ref/FIXTURES_V4_20260825.out` = `c5a4b95b554e16a7aea99213b06f21b18868e701c5a9682e8d3b325a18b10e72`

All three match the brief. Review proceeded.

Background-source digests independently computed:

- `GATE_CODEX_SUCCESSOR_V8.md` = `d71dc0ae1b38cfaadc64a4397e2cc31720797d4a1bb35a6fee9084f53adc84ce`
- `../real/REAL_GEOMETRY_RESULT_20260825.md` = `1c5ee1f7987dc14edff360cc8681b54cbe1223684940cb51f839281407052f30`
- `../../SUCCESSOR_SCOPE_20260821.md` = `995b2e729a3362f0445cac9d5da6d290fddac9f8018e75f2c0aa87c190c93de7`
- `../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` = `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- `../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md` = `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`
- `../../VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md` = `43b9a6a843ef08a6528f1132db2bee29000c5ecd3def2a3a03c23f672c81cec7`

## Environment and mandatory reference execution

- executable: `/Library/Developer/CommandLineTools/usr/bin/python3`
- Python: `3.9.6`
- NumPy: `1.26.4`
- platform: `macOS-26.6.2-arm64-arm-64bit`
- machine: `arm64`
- byte order: `little`
- command: `python3 -B ../ref/successor_ref_v4.py --fixtures` (executed through a subprocess capture to permit byte comparison)
- exit: `0`
- stdout: `4,060` bytes
- stderr: `0` bytes
- stdout SHA-256: `c5a4b95b554e16a7aea99213b06f21b18868e701c5a9682e8d3b325a18b10e72`
- pinned transcript SHA-256: the same
- byte comparison: `True`

The transcript contains 34 named PASS checks and ends `ALL FIXTURES PASS`. Passing the fixture transcript does not rescue the findings below because the relevant production paths are not exercised by those fixtures.

## Numbered findings

### 1. BLOCKER — `close_manifest()` still calls the retired planner, so the round-7 closure repair is not connected to the production entry point

**Quoted claim / symbol.** V9 §2.4 says the reimplementation is retired, BS-2m binds to the frozen `plan_candidate_bricks`, the historical missing-neighbour manifests are refused by name, and the closure fixtures include `CLOSURE-CALLER-TRUST` (`PREREG_SUCCESSOR_DRAFT_V9_20260825.md:136-152`). The operative entry point is `close_manifest()` (`successor_ref_v4.py:267-334`).

**Direct code trace.** `frozen_plan_object()` correctly delegates to the frozen planner (`successor_ref_v4.py:232-235`), but `close_manifest()` never calls it. Its object loop calls the retired `plan_object_bricks()` at line 308. That routine unconditionally raises at lines 198-215. The receipt also writes `planner_digest()` at line 324; that digest hashes `_ra_sep` plus the retired `plan_object_bricks` source (`245-254`), not `frozen_planner_digest()`.

**Executed production-entry attacks.** With a cardinality-matched 366,912-row stand-in, the pinned universe digest string, a self-consistent two-object parent, a matching BS-2s-shaped witness, and the complete five-brick historical manifest, `close_manifest()` returned:

`RuntimeError: plan_object_bricks is RETIRED — it reproduced the defect it was written to prevent; use frozen_plan_object()`

Passing the real `GeometryIndex` loaded by the frozen planner fails even earlier:

`TypeError: object of type 'GeometryIndex' has no len()`

The production signature/check expects a len-able `brick_table` (`281`), whereas the frozen planner consumes a `GeometryIndex`. There is no connected input type between those paths.

The two planner-digest functions independently produced:

- `planner_digest()` (the value `close_manifest()` would receipt) = `312e979c26fd8e626cc0ca9a16605e46887afb079e4a417ec898d7b0f8d7b9e4`
- `frozen_planner_digest()` = `36bbbf2502159474e0a56ec904e924e2ee80645b485c2ee20208ef25a514f610`
- equality = `False`

**Fixture gap.** The three closure fixtures at `successor_ref_v4.py:1202-1238` call `frozen_plan_object()` directly and compute a Python set difference. They never call `close_manifest()`. Programmatic enumeration of the pinned transcript found 34 checks but no `CLOSURE-CALLER-TRUST`, despite V9's claim that this named check exists. `CLOSURE-CATCHES-HISTORICAL` proves only that the two names are absent from a manually shortened list; it does not prove the production closure entry point refuses that list.

**Why the guarantee fails.** The frozen planner itself returns the correct historical neighbours, but the only declared production closure path cannot use it and cannot emit a receipt binding it. BS-2m therefore cannot be filled by the claimed mechanism.

**Smallest sufficient repair.** Make `close_manifest()` consume/load the frozen planner's actual `GeometryIndex`, call `frozen_plan_object(geometry, objid, ra, dec)` for every parent row, and receipt `frozen_planner_digest()`. Add a fixture that invokes `close_manifest()` itself on the real sidecar and historical parent, first with the exact closed manifest (accept) and then with each neighbour omitted separately (refuse by name). The separately disclosed caller-custody seam remains open and is not counted again here.

### 2. BLOCKER — the 6,445-brick artifact is a fast removal result, not an evidenced execution of the frozen selection chain

**Quoted claim / symbol.** V9 reports “Selection through the frozen reduction pass” and says the fast reduction is “proven equal to `local_pass()` on 30 random cases” (`PREREG_SUCCESSOR_DRAFT_V9_20260825.md:171-181`). Its repair trace says the 6,446-brick prefix was re-run through the frozen reduction (`417-418`). The operative frozen chain derives `L_min_plan` from the first Stage-P-passing prefix, applies the 1.2 margin, runs `local_pass()`, and re-passes Stage P (`successor_ref_v4.py:761-817`).

**The real driver still does not execute that chain.** `run_real_selection.py` sets `L_REQ = NEQ_MIN / 3` (`18`), creates a greedy prefix at that threshold (`22`), then creates the saved set at `1.2 * L_REQ` (`37-53`). It does not run Stage P to derive `L_min_plan`; it does not call `build_plan()`; and it does not call `local_pass()`. The real receipt itself correctly discloses that Stage P was measured on the pre-reduction set and must be rerun on the reduced set (`REAL_GEOMETRY_RESULT_20260825.md:147-149`).

**The fast reducer is not equivalent to `local_pass()`.** `reduce_fast.py:24-56` implements repeated removals only. Frozen `local_pass()` additionally tries every inside/outside swap and then another removal (`successor_ref_v4.py:485-494`). A deterministic random attack found a mismatch on trial 3, well inside a 20,000-case search:

- 21 bricks, target `28.134414700530833`
- greedy brick order: `[1012, 1020, 1017, 1002, 1016, 1005, 1013, 1015, 1018, 1009, 1001, 1010, 1006, 1019, 1004, 1000, 1007, 1011, 1003, 1008, 1014]`
- fast removal result: `[1012, 1017, 1020]`, `L=36.09726377142857`
- frozen `local_pass()` result: `[1002, 1017]`, `L=28.980211764705885`

The failing inputs were:

- `c = [0.26, 0.56, -0.546, 0.075, -0.16, -0.359, 0.338, 0.229, 0.178, -0.595, 0.503, 0.054, 0.902, 0.777, 0.144, -0.599, 0.724, 0.774, 0.467, 0.535, -0.702]`
- `n_raw = [39, 16, 46, 48, 22, 46, 28, 24, 9, 13, 11, 25, 21, 11, 34, 14, 22, 34, 33, 8, 27]`

This is exactly the omitted swap surface: the fast routine remains at three bricks while the frozen routine swaps in brick 1002 and removes to two.

**What did reproduce.** Applying `reduce_removals()` at target `40,000.0` to the saved 6,446-brick prefix exactly reproduced `real_selection_reduced.npz`: 6,445 bricks, removed brick 155487, `L=40000.959939179214`, and byte-array-equal selected indices. The corrected summary also independently reproduced: 65,060 raw objects, 53,005 retained, retained-weighted `Var(c)=0.7546638984846564`, and `N_eq=120002.87981753764`. This establishes what the fast removal artifact is; it does not make it `local_pass()` output.

The fast greedy order itself survived an additional 5,000 randomized/tie-heavy comparisons with zero mismatches. That is positive evidence for `greedy_fast.py`, not for the incomplete reduction or the absent Stage-P-derived threshold.

**Why the guarantee fails.** Thirty random reduction cases missed a counterexample found almost immediately under another seed. The real artifact omits the frozen swap phase and was cut at an assumed `1.2 * NEQ_MIN/3`, not at `1.2 *` the first Stage-P-passing leverage. Therefore the claimed 6,445-brick frozen selection is not established, and the pre-reduction Stage-P result cannot certify the unknown frozen final set.

**Smallest sufficient repair.** Implement a scalable equivalent of the complete `local_pass()` state machine, including the exact swap-then-removal order and tie rules; add this counterexample and the five inherited selector cases to pinned fixtures; derive `L_min_plan` by the frozen Stage-P rule rather than substituting `NEQ_MIN/3`; and rerun Stage P on the exact final artifact. Pin the producer script and all real input/output digests in the resulting receipts.

### 3. BLOCKER — Stage P's “self-confirmation” can count an unsafe success without any confirmation, and one reference null is not shown conservative for 1,000 trials

**Quoted claim / symbol.** V9 says every calibrated success within 10× of the threshold is independently retested, “Far-from-boundary successes need no confirmation,” and one refutation fails the stage (`PREREG_SUCCESSOR_DRAFT_V9_20260825.md:241-252`). It also says one standardized 20,000-permutation null legitimately serves all 1,000 trials (`229-234`). The real Stage-P record reports 997 calibrated successes and 77 boundary confirmations.

**Code trace.** `stage_power()` confirms only a calibrated success with `p_calibrated >= 0.0001` (`successor_ref_v4.py:729-742`). Any success with `p_calibrated < 0.0001` is counted with no independent test. The code contains no bound proving such a value cannot cross 0.001 under a different sign multiset or full production permutation record. Its confirmation count is only `MC_CAL_PERM = 20,000`, not production's 100,000 (`91-93`, `711-747`).

**Executed branch attack.** Holding the mask/injection machinery fixed while forcing the calibrated decision to `0.00005` and the independent full result to an unsafe `0.5`, `stage_power(..., n_trials=1)` returned:

`(1, None, {'boundary_trials': 0, 'confirmed': 0, 'refuted': [], 'confirm_perm': 1})`

The tracked full-confirmation call count was zero. This directly demonstrates the control-flow claim: an unsafe out-of-band success can be counted while every named confirmation check reports no refutation.

On the reported real run, 997 successes minus 77 boundary trials leaves **920 counted successes with no independent confirmation**. The 77/77 result is genuine evidence about those 77 trials only.

**One-null defect.** `PWR-Z-STABLE` measures four hand-chosen sign multisets and accepts a relative tail-mass spread below an arbitrary 50%. The pinned transcript itself reports tail masses `[0.00135, 0.00130, 0.00100, 0.00110]`, a 35.0% spread, then asserts that the 1% z deflation absorbs it. No inequality in code links that spread to `PWR_CONSERVATISM`, no simultaneous bound covers all sign multisets generated in 1,000 trials, and `reference_null_z()` uses only trial 1's sign multiset (`successor_ref_v4.py:651-683,726-727`). A finite four-case measurement cannot establish the promised universal implication.

**What held.** The exact Clopper–Pearson threshold is correct: independently computed one-sided 95% lower bounds are `0.9493659932` for 961/1000 and `0.9504871297` for 962/1000. The exact permutation-variance identity also held across 25 exhaustive N/sign-balance cases, with maximum absolute discrepancy `1.11e-16`. The defect is not those formulas; it is the classification evidence supplied to the 962-success rule.

**Why the guarantee fails.** Stage P counts calibrated classifications that it neither confirms nor proves conservative. The named checks can all pass while an unconfirmed out-of-band calibrated success would fail an independent full run. The real `997/1000` therefore supports calibrated power on the pre-reduction geometry, plus 77 successful spot confirmations; it does not support 997 full-MC successes or the claimed equality contract.

**Smallest sufficient repair.** Confirm every counted success with the production 100,000-permutation contract, or derive and implement a finite-sample simultaneous upper bound that covers reference-null estimation and every admissible sign multiset. If a band remains, prove in code that every value outside it cannot cross 0.001 under that bound; a factor of ten and a four-case `<50%` spread fixture are not such a proof.

### 4. BLOCKER — the count-oracle completeness proof still compares one derived total to itself and can be omitted entirely

**Quoted claim / symbol.** V9 says the count oracle is left-joined to an independently enumerated universe, materializes zeros, and refuses any grouped/ungrouped disagreement through the production chain (`PREREG_SUCCESSOR_DRAFT_V9_20260825.md:89-97`). The review brief specifically requires an end-to-end completeness proof.

**Real-data reproduction held.** I independently read the already-acquired release sidecar and grouped-count CSV, without network access or writes. Their hashes match the receipt (`863e5ded…` and `4e4ec45d…`). The reconstruction produced 366,912 unique universe bricks, 270,577 positive rows, 96,335 materialized zeros, zero count keys outside the universe, total 832,393, count-weighted `Var(c)=0.4452013461602878`, and arrays exactly equal to `real_oracle_dr10.npz`. These values are sound for the bytes inspected.

**The proof is still self-referential.** `build_real_oracle.py:69-72` passes both `grouped_sum=int(n_elig.sum())` and `ungrouped_total=int(n_elig.sum())`. They are the same value from the same left-joined array, not independently produced grouped and ungrouped queries. `validate_count_table()` therefore checks equality to itself.

**The production requirement is optional in substance.** Although `build_plan()` makes the three keywords syntactically present, it accepts explicit `None` and forwards them (`successor_ref_v4.py:761-782`). `validate_count_table()` skips universe equality when `universe_brickid is None` and skips grouped/ungrouped closure when `grouped_sum is None` (`349-387`). The direct probe

`validate_count_table([1,2], [-0.5,0.5], [3,4], universe_brickid=None, grouped_sum=None, ungrouped_total=None)`

returned `{'rows': 2, 'zero_rows': 0}`.

The archived per-brick ADQL is genuinely grouped by `brickid`; the separate ungrouped file inspected (`06_cut3_photoz_indexed.adql`) stops at Cut 3 and is not an independent Cut-6 total matching the grouped query's full predicate. Thus the real script does not consume the independent completeness witness the prose promises.

**Why the guarantee fails.** A common query-scope omission can remove a nonzero group while the supplied totals still agree, and a caller can disable every completeness witness with explicit `None`. Correct numbers on this one reconstruction do not establish a fail-closed production proof.

**Smallest sufficient repair.** Produce and pin an independent ungrouped Cut-6 count with the same frozen predicate and independently specified scope; consume its raw receipt rather than a caller integer derived from the grouped array; reject `None` in `build_plan()` and its production validator; and bind the universe bytes, grouped query family/results, ungrouped query/result, scripts, and generated oracle digest in typed BS-2c custody.

## Guarantees and attacks that held

1. The mandatory reference fixture run reproduced byte-for-byte in the frozen environment.
2. Called directly, the frozen planner returned `['3385m885', '3471m885']` and `['2857m870', '2894m872', '2902m870']`; the retired routine refused. Finding 1 is the missing production connection, not a defect in those direct frozen-planner results.
3. The real count-oracle values and `real_oracle_dr10.npz` arrays independently reproduced from the two pinned, already-acquired artifacts. Finding 4 concerns completeness custody, not those numeric values.
4. The 6,445-row reduced artifact and its published summary independently reproduced from `reduce_removals()` at target 40,000. Finding 2 concerns equivalence to the larger frozen algorithm and the missing Stage-P-derived threshold.
5. The fast greedy order survived 5,000 additional randomized/tie-heavy comparisons with zero mismatches.
6. Calibration adjudication precedes the real statistic in `run_production_verdict()`: with a failing calibration and a tracked `perm_record`, the runner raised `InconclusiveByCalibration` and made zero permutation calls.
7. The exact permutation-variance formula and the 962/1000 Clopper–Pearson threshold held independently.
8. All eight §2.2 predicate literals occur in both V9 and BS6-pred; the executable ellipticity literal `POWER(shape_e1,2)+POWER(shape_e2,2) < 0.1836734693877551` is byte-identical. The predecessor contains the quoted HC-1H correction, population-weighting statement, 100,000-permutation count, and one-sided Longo-sign rule. I found no new quotation-fidelity defect.
9. V9's preamble correctly states draft-only writing authority and no run/fetch/data-touch/freeze authority. The completed catalog-only count step is separately disclosed. I found no assumption of a run or freeze authorization that does not exist.
10. V9 accurately says the 997/1000 Stage-P result belongs to the pre-reduction geometry and must be rerun on the reduced set. I did not treat it as a claimed measurement on the 6,445-brick artifact.

## Brief-mandated exclusions

Per review dimension 6, I do not re-report the six findings V9 §10 explicitly leaves open: closure caller custody, Stage-C mask-digest chronology, receipt round-trip/consumption, HC-1H population weighting and boundary-tie wording, the release availability probe, and the integrated power battery. I also do not re-report the four disclosed-not-closed items: the clean-room normative specification, BS-9 input schema, BS-V primary lock, and the O(n²) scaling of frozen `greedy_ledger()`/`local_pass()`.

Finding 1 is narrower and new to the claimed round-7 repair: the production closure entry point still invokes the retired routine and receipts the wrong planner digest. Finding 2 directly refutes the claimed repair's fast-equivalence evidence and full-chain execution. Finding 3 is the separately requested self-confirmation/equality-contract audit. Finding 4 is the separately requested count-oracle completeness proof.

## Testimony

None. No unsupported testimony is used to support the recommendation.

## Custody boundary

I did not read `/Users/duhokim/NebulaMindData/`. I made no network request, study-data fetch, image access, χ access, run authorization, freeze, publication, git mutation, or source-artifact edit. The only review write is this report.

Blocking findings: F1 production closure is disconnected from the frozen planner; F2 the 6,445-brick artifact is not established as frozen-chain output; F3 Stage P's self-confirmation/equality contract does not cover its counted successes; F4 count-oracle completeness is self-referential and optional.

**REVISE**
