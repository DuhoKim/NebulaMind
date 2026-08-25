# GPT56 referee gate — successor preregistration V10 (round 9)

## Recommendation

**REVISE.** The pinned digests and 36-check fixture transcript reproduce, and the production manifest-closure entry point now calls the frozen planner and refuses each historical missing neighbour. However, guarantees still fail at production boundaries: the fast selector diverges from frozen `local_pass()` near a threshold crossing; Stage P still counts largely unaudited successes; the count oracle still accepts no independent witness; canonical receipts cannot carry the fields their consumers require; calibration can fail only after the real permutation record; the inherited hand-check estimator omits population weights; and the authorization/completeness and release-choice guards remain caller assertions rather than verified custody.

No run or freeze is authorized by this recommendation.

## Dispatch digests — computed before substantive review

Command:

`shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V10_20260825.md ../ref/successor_ref_v4.py ../ref/FIXTURES_V4_20260825.out`

Computed:

- `../PREREG_SUCCESSOR_DRAFT_V10_20260825.md` = `cca636b9444c4f5a1df47aaddf419443caa27350adfbdbfd5c3ba31065ea39c7`
- `../ref/successor_ref_v4.py` = `0b312c96db0b4551bcafd554b4bdd7124d3104cef4cc7f405eea3f849e08e21c`
- `../ref/FIXTURES_V4_20260825.out` = `6b14d8a69b606cbf5ddb6d0e82f856a08d6a5928227c3cba4956a1c02636e436`

All three equal the brief. Review proceeded.

## Environment and mandatory reference execution

The fixture command was executed as child argv `['/Library/Developer/CommandLineTools/usr/bin/python3', '../ref/successor_ref_v4.py', '--fixtures']` with `PYTHONDONTWRITEBYTECODE=1`; stdout was captured in memory and compared byte-for-byte with the pinned transcript.

- executable: `/Library/Developer/CommandLineTools/usr/bin/python3`
- Python: `3.9.6` (Clang 21.0.0)
- NumPy: `1.26.4`
- platform: `macOS-26.6.2-arm64-arm-64bit`
- machine: `arm64`
- byte order: `little`
- exit: `0`
- stdout: `4,317` bytes
- stderr: `0` bytes
- stdout SHA-256: `6b14d8a69b606cbf5ddb6d0e82f856a08d6a5928227c3cba4956a1c02636e436`
- pinned transcript SHA-256: same
- byte-identical: `True`
- parsed named checks: 36 PASS; final line `ALL FIXTURES PASS`

The fixture transcript is genuine. Several findings below concern production paths or adversarial regimes the fixtures do not exercise.

## Numbered findings

### 1. BLOCKER — the fast swap/removal repair is not equivalent to frozen `local_pass()` at a near-crossing target, and the real producer still does not execute the full `build_plan()` chain

**Quoted guarantee / symbols.** V10 §10 says `_swap_then_remove` “matches `local_pass` on 400 cases in the referee's own seed and regime, zero mismatches” and that the real selection remains 6,445 bricks (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:417-422`). The brief explicitly asks for tests outside that regime, including targets near the crossing. The operative definitions are `local_pass()` (`successor_ref_v4.py:452-505`) and `reduce_removals()` / `_swap_then_remove()` (`reduce_fast.py:24-107`).

**What held.** I independently recreated the round-8 CODEX regime with seed `2026082509`, 400 cases, 18–30 bricks, alternating one/two-decimal tied `c`, integral raw counts 1–59, and targets 0.25–0.90 of full retained SSE. Result: `400 cases, 0 mismatches`. A second wider test with seed `31415926`, 2,000 cases, 18–120 bricks, tied values, counts 1–150, and targets no closer than `10^-6` of a crossing also gave `2,000 cases, 0 mismatches`.

**Counterexample outside that regime.** Command form:

`python3 -B <inline deterministic comparison of successor_ref_v4.local_pass and real/reduce_fast.reduce_removals>`

Seed `27182818`, trial 26, 35 bricks, one-decimal tie-dense `c`, and a target `10^-12` of the way above the preceding greedy-prefix crossing produced:

- target `516.5317718940938`
- fast set (30 bricks): `[30000,30001,30002,30003,30004,30006,30008,30010,30011,30012,30013,30014,30015,30016,30017,30019,30021,30022,30023,30024,30025,30026,30027,30028,30029,30030,30031,30032,30033,30034]`
- frozen set (31 bricks): the same set plus `30009`
- fast reported L `516.5317718940938`
- frozen L `516.7381891348089`
- `brickid = [30004,30031,30009,30015,30024,30026,30022,30029,30025,30030,30033,30001,30023,30014,30018,30020,30032,30011,30005,30028,30010,30034,30016,30002,30027,30013,30019,30021,30006,30000,30017,30012,30008,30003,30007]`
- `c = [0.2,0.4,0.1,0.2,0.4,-0.2,-0.4,0.5,0.8,-0.8,-0.5,-0.1,-0.5,0.2,0.0,-0.0,-0.2,0.9,-0.5,-0.7,-0.9,-0.4,-0.6,0.7,-0.8,0.8,-1.0,0.7,-0.1,0.6,0.8,0.4,0.4,-1.0,0.0]`
- `n_raw = [100,71,22,76,60,91,67,65,12,24,32,31,68,29,66,44,95,94,1,86,95,4,22,56,100,66,81,35,38,87,6,83,58,3,90]`

This is a floating-operation boundary defect: the vectorized SSE comparison permits removal of brick 30009 where the normative scalar `sse()`/`local_pass()` comparison does not. The claim is exact equivalence, not approximate agreement away from thresholds.

There is also still no real execution of the full frozen planning chain. `rerun_reduction_v2.py:15-16` substitutes `target = L_PLAN_MARGIN * NEQ_MIN / 3.0`; it does not derive `L_min_plan` from the first Stage-P-passing prefix as `build_plan()` does (`successor_ref_v4.py:819-843`). `rerun_real_power_v4.py:15-16` still loads the pre-reduction `real_selection_dr10.npz`, not `real_selection_swapped.npz`. V10 correctly discloses that the final-set Stage-P re-pass is absent, but §10's statement that the round-8 selection finding is repaired is therefore too broad.

**Smallest sufficient repair.** Reconfirm every fast candidate decision whose vectorized L is within a declared rounding envelope of the target using the normative scalar `sse()` operation order, and add this exact counterexample as a pinned fixture. Produce the real artifact through a scalable implementation of the complete `build_plan()` chronology: derive the actual `L_min_plan` by Stage P, apply the 1.2 margin, run the exact-equivalent reduction, and re-run Stage P on that exact final artifact.

### 2. BLOCKER — Stage P still returns PASS while most counted successes and almost all trial-specific nulls are unchecked

**Quoted guarantee / symbols.** V10 says a deterministic sample of non-boundary successes is confirmed and the shared reference null is measured against trials' own nulls, with a non-conservative reference failing closed (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:243-256,417-422`). The operative code is `stage_power()` (`successor_ref_v4.py:719-778`).

**Control-flow execution.** I fixed all 1,000 calibrated p-values at `0.00005` (far from the old boundary band), supplied safe results for every confirmation the routine actually requested, and instrumented both `perm_record()` and `reference_null_z()`. This is an adversarial branch test, not a claim about the real geometry. Result:

- `successes = 1000`
- returned `passed = True`
- independent confirmation calls = `50`
- counted successes with no independent confirmation = `950`
- own-null measurements after the shared reference = `8`
- trials with no own-null measurement = `992`
- audit reports `boundary_trials=50`, `confirmed=50`, `nonconservative_nulls=[]`

The result follows directly from `take = max(5, len(far)//20)` (`successor_ref_v4.py:751-756`) and the own-null loop over only the first eight sampled records (`759-764`). An unsafe success among the other 950 can still be counted while every named audit reports success. An unsafe trial-specific null among the other 992 is never compared. The unused assignment `trials_for_null = [x for x in interior][:0] or []` at line 759 provides no coverage. Confirmation also uses `confirm_perm=20,000`, not the production 100,000-permutation contract.

The fixture does not establish the promised invariant. `PWR-SELF-VERIFYING` checks a small near-50%-power fixture; its `invariant_ok = (passed_v is not False) or True` expression is tautologically true unless the separate `refuted` branch overwrites it (`successor_ref_v4.py:1361-1368`). It does not prove shared-null conservatism over admissible trial sign multisets.

**Why the guarantee fails.** Sampling can estimate an error rate, but this code uses the sample as a universal fail-closed guarantee without a simultaneous statistical bound. One shared empirical null is likewise not proved conservative for all 1,000 changing sign multisets by checking eight selected successes.

**Smallest sufficient repair.** Either confirm every counted success with the same 100,000-permutation contract used by the scientific decision, or define and implement a finite-sample simultaneous bound covering reference-null estimation, all admissible sign multisets, and all 1,000 decisions. If sampling is retained as estimation rather than certification, propagate its uncertainty into a conservative lower bound on the number of true successes before comparing with 962.

### 3. BLOCKER — the count-oracle completeness proof remains optional and can pass with no independent witness

**Quoted guarantee / symbols.** V10 says `validate_count_oracle()` refuses any grouped/ungrouped disagreement and §10 says the ungrouped total must equal an independently pinned release total, with omitted proof input refused (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:89-97,417-422`). The code symbol is actually `validate_count_table()` (`successor_ref_v4.py:348-395`).

**Direct executions.** The following calls were made in the pinned module:

- `validate_count_table([1,2],[-.5,.5],[3,4], universe_brickid=None, grouped_sum=None, ungrouped_total=None)` returned `{'rows': 2, 'zero_rows': 0}`.
- A synthetic one-brick table with count `832393`, synthetic universe `[1]`, and both caller totals set to `832393` returned `{'rows': 1, 'zero_rows': 0, 'universe': 1, 'total': 832393}`.

The code checks the pinned total only inside `if grouped_sum is not None` (`successor_ref_v4.py:380-394`), so explicit `None` still disables the proof. `build_plan()` requires the argument names syntactically but forwards their values unchanged (`792-813`). `PINNED_COUNTS_SHA256` occurs exactly once in the file — its declaration at line 105 — and is never consumed. The real producer still passes `grouped_sum=int(n_elig.sum())` and `ungrouped_total=int(n_elig.sum())` from the same left-joined array (`build_real_oracle.py:69-72`). A copied constant equal to that same sum is not an independently produced ungrouped Cut-6 witness.

**Why the guarantee fails.** A caller can omit every proof artifact or construct a self-consistent table with the copied total. The validator checks a value, not its independent provenance, so a shared query-scope omission can still pass.

**Smallest sufficient repair.** Make proof artifacts non-optional at the first production boundary. Consume and hash-verify separately pinned universe bytes, grouped query/results, and a genuinely independent ungrouped Cut-6 query/result; derive the totals inside the consumer; verify `PINNED_COUNTS_SHA256` (or replace it with the correct typed artifact digests); and add negative production-entry fixtures for explicit `None`, same-source totals, and scope-mismatched queries.

### 4. BLOCKER — receipt payloads are discarded, their consumers require unbound fields, and Stage-C mask binding conflicts with pre-unblinding chronology

**Quoted guarantees / symbols.** V10 says receipts carry enforceable schemas and are consumable by routines that need them; BS-2m binds to the BS-2s parent digest; BS-5f binds Stage C to the exact sealed accepted-position mask (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:117-125,258-270,342-370`). Relevant code is `SLOT_SCHEMA` / `receipt()` (`successor_ref_v4.py:138-177`), `close_manifest()` (`261-333`), and `run_production_verdict()` (`1092-1126`).

**Direct production-path results.** The repaired geometric closure itself now works: with the real `GeometryIndex` and the two historical parent rows, the complete required set was

`['2857m870', '2894m872', '2902m870', '3385m885', '3471m885']`.

`close_manifest()` accepted that set with frozen planner digest `36bbbf2502159474e0a56ec904e924e2ee80645b485c2ee20208ef25a514f610`, and separately refused omission of `2857m870` and `3471m885`, naming the omitted brick each time. This round-8 wiring repair holds computationally.

The receipt boundary does not:

- `SLOT_SCHEMA['BS-2s']` has no `parent_digest` field.
- `receipt('BS-2s', ...)` returns only `slot`, `schema`, `environment`, `body_sha256`, and `envelope_sha256`; it does not return any supplied body field. A canonical BS-2s receipt therefore cannot satisfy `close_manifest().get('parent_digest')`. The successful closure test necessarily used the bare dict `{'slot':'BS-2s','parent_digest':pd}`, which is not a canonical receipt or verified external witness.
- A canonical BS-5f receipt likewise contains neither `passed` nor `mask_digest`, yet `run_production_verdict()` requires both as top-level keys.
- Appending `passed=True` and `mask_digest=<chosen value>` after `receipt()` was called left `envelope_sha256` unchanged and was accepted by the consumer far enough to return `INCONCLUSIVE-BY-POWER`. The appended fields are not bound by either digest, and the consumer never recomputes the envelope.

Chronology also makes the stated exact digest impossible. A signless sealed Stage-C mask had digest `6c68f28e04d8b0358ff3670b11ccb383d868a762b8fc23d675c84b7f8da81ff4`; adding the real-sign vector with `with_signs()` changed it to `3b3119d0f0fad960ed4602213e896b42609dfcb36f796f22ad04216ccf291bef`. Stage C is supposed to run on a position-only mask, but production requires signs and compares the Stage-C receipt against the signed-mask digest. Moreover, `require_sealed(signed_mask, need_signs=False)` accepts a mask that already contains signs, so the Stage-C path does not enforce the claimed “never a χ sign” input state.

**Why the guarantee fails.** The receipts prove hashes of payload bytes that are then discarded; consumers trust separately appended top-level values not covered by those hashes. BS-2m lacks a consumable parent witness, and BS-5f can match the production mask only by loading signs before the pre-unblinding gate or by appending an unbound digest.

**Smallest sufficient repair.** Return/store the canonical typed body alongside its digest and have every consumer reserialize and recompute the body/envelope hash. Add `parent_digest` to the canonical BS-2s schema and require a verified receipt in `close_manifest()`. Define a position-mask digest that explicitly excludes signs and is preserved when signs are attached; bind BS-2f, BS-8f, BS-5f, BS-7f, and BS-V to that stable digest. Stage C must reject `s is not None` rather than merely not requiring signs.

### 5. BLOCKER — calibration admissibility is not fully validated before the real statistic

**Quoted guarantee / symbols.** V10 says the calibration decision precedes the real statistic and a calibration failure halts before unblinding (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:258-262,305-320`). `run_production_verdict()` calls `adjudicate_path(cal)` before `perm_record()` (`successor_ref_v4.py:1107-1119`).

**Direct production-path attack.** On a sealed signed mask with `N_eq = 120002.00001666677`, I supplied calibration values that pass `adjudicate_path()` (`a_hat=0.95`, equal `a_b`, and every `a_lb_b=0.90`) but set `sigma_a=NaN`. I instrumented `perm_record()` and used synthetic no-I/O guard stubs. Result:

- `perm_record_calls_before_refusal = 1`
- only afterward: `RuntimeError: non-finite decision quantity — FAIL`

This is the exact ordering the prose prohibits. `adjudicate_path()` validates only `a_lb_b`, `a_b`, and `a_hat` (`successor_ref_v4.py:993-997`); the scalar/profile uncertainty inputs, covariance, epsilon, dimensions, and finiteness are not validated until `_decide_from()` after the permutation record. `run_production_verdict()` also consumes a raw calibration dict, not a hash-verified BS-8f receipt bound to the mask and hand-check allocation.

**Smallest sufficient repair.** Add one fail-closed BS-8f parser/validator that verifies the canonical receipt and stable mask digest, exact dimensions, finite/range-valid estimates, covariance symmetry/positive semidefiniteness, and all scalar/profile uncertainty inputs. Run that complete validation and compute/freeze the chosen calibration path before loading any sign vector or calling `perm_record()`.

### 6. BLOCKER — `accuracy_from_handcheck()` does not implement the inherited population-weighted HC-1H estimand

**Quoted guarantee / symbol.** V10 says BS-8f implements the inherited HC-1H estimator (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:305-315`). The predecessor defines `a = Σ w_s·a_s` with population weights after a disproportional nine-stratum hand-check allocation (`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md:279-303`). The operative function is `accuracy_from_handcheck()` (`successor_ref_v4.py:947-990`).

**Direct execution and API trace.** Its signature is only

`(agree_counts, n_counts, epsilon_hat, sigma_epsilon)`.

It has no stratum population counts or weights and pools sampled agreements as `sum(agree)/sum(n)` (`successor_ref_v4.py:982-987`). With two equal-sized hand-check cells having agreements 99/100 and 50/100, it returns `a_hat=0.745`. If those cells represent 90% and 10% of the accepted population, the inherited estimand is `0.9*0.99 + 0.1*0.50 = 0.941`. The function also accepts this two-element input despite the frozen three calibration bins and 3×9 allocation.

The boundary-tie prose remains wrong as well: `calibration_bins()` says `side='left'` puts a value equal to a boundary in the higher bin (`successor_ref_v4.py:860-876`), but `assign_bins([0.0], [0.0,1.0])` returns `[0]`; the higher bin would be 1. This changes allocation and sealed bin labels at ties.

**Why the guarantee fails.** Pooling a disproportional hand-check sample estimates the allocation-weighted agreement rate, not the accepted-population attenuation required by HC-1H. The shared-epsilon derivative and covariance do not repair a wrong central estimand.

**Smallest sufficient repair.** Consume the complete 3×9 cell population counts and realized hand-check counts, compute noise-corrected cell/stratum accuracies, aggregate with frozen accepted-population weights, and propagate the shared-epsilon derivative after weighting exactly as the predecessor specifies. Enforce exact shapes and counts. Either change assignment to `side='right'` to implement “equal goes higher” or correct every prose/docstring statement to the normative `side='left'` behavior and re-freeze affected fixtures/digests.

### 7. BLOCKER — the authorization and complete-sample guards authenticate caller assertions, not authorization or sample custody

**Quoted guarantee / symbols.** V10 says `require_authorization()` refuses real data without an authorization file pinned to a SHA-256 that does not yet exist, and `require_complete_sample()` refuses unless every parent object has a measurement receipt (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:293-296`). The production runner accepts caller-provided `authorization_path`, `authorization_sha256`, `n_receipts`, and `n_parent` (`successor_ref_v4.py:1092-1100`).

**Direct executions.** SHA-256 of this referee brief is `c02e301f8402bc78c0b1b232ac4e6f82f510df0d414e875ed19e1c1f51f43332`. It is not a run authorization. Nevertheless:

`require_authorization('BRIEF_GATE_SUCCESSOR_V10.md', 'c02e...43332')`

returned that digest and accepted the brief as authorization. The function checks only that the caller-supplied digest matches the caller-supplied path (`successor_ref_v4.py:1137-1145`); it validates no authorization schema, authority, study/run identity, or separately pinned expected digest.

Likewise, `require_complete_sample(1,1)` returns normally. The function compares two caller integers (`successor_ref_v4.py:1148-1150`); it does not inspect a parent manifest, receipt set, unique object IDs, per-receipt digests, or a parent digest. A caller can assert any equal pair.

**Why the guarantee fails.** Both guards can report success with no real authorization and no evidence of a complete sample. The preamble correctly says no authorization exists, but the operative code cannot distinguish one from arbitrary bytes.

**Smallest sufficient repair.** Define a typed authorization record naming this preregistration hash, run ID, allowed operation, authority, issue time, and independently pinned/signed digest; the production runner must obtain the expected identity from frozen configuration, not a caller pair. Derive sample completeness by matching a hash-verified parent manifest against a hash-verified set of unique per-object receipts, not two counts.

### 8. MAJOR — the release branch-invariance guarantee has no production consumer or non-vacuous check

**Quoted guarantee / symbols.** V10 requires every downstream artifact to use the same code path under either release branch and says any branch-specific logic is a defect (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:59-75`). The operative helpers are `resolve_branch()` and `branch_invariance()` (`successor_ref_v4.py:1153-1201`).

**Code trace and direct checks.** None of `build_plan`, `close_manifest`, `stage_power`, or `run_production_verdict` accepts a branch config or references `BRANCH_CONFIG`. The fixture calls `branch_invariance(lambda cfg: {'selected':..., 'L':...})` while ignoring `cfg` (`successor_ref_v4.py:1568-1571`), so it passes vacuously. Directly, a constant-output lambda returns `invariant=True`; a lambda that merely returns `cfg['release']` returns `invariant=False`, even though differing recorded input release/path is explicitly allowed by the prose. Thus the helper neither traces same-code-path execution nor defines the allowed path-only differences.

**Why the guarantee fails.** Every named fixture can pass while a later DR11/DR10 producer uses arbitrary branch-specific logic, because no frozen downstream orchestrator consumes the config and no trace schema distinguishes permitted path/version differences from forbidden logic differences.

**Smallest sufficient repair.** Route both branches through one frozen production orchestrator accepting a typed branch config. Define and compare normalized execution traces that exclude only explicitly allowed input path/version fields while binding function/code hashes, predicate/query templates, schemas, and downstream slot producers. Replace the fixture's cfg-ignoring lambda with end-to-end dry runs of that orchestrator under both configs.

## Statistical, fidelity, and production attacks that held

1. The three dispatch digests match and the fixture transcript reproduces byte-for-byte.
2. `close_manifest()` now uses the real frozen planner end to end. A complete historical manifest passes; omission of either named neighbour is refused by name. Finding 4 concerns receipt custody and chronology, not the geometric planner result.
3. The round-8 400-case fast-reducer regime reproduced with zero mismatches, and a wider 2,000-case test away from machine-near crossings also had zero mismatches. Finding 1 is the additional near-crossing counterexample and the still-incomplete real planning chronology.
4. `real_selection_reduced.npz` and `real_selection_swapped.npz` are byte-identical (both SHA-256 `b913939d54b66bda5a4ef05ee46d0b1321a6b490d1d232ba197c9aa0c9a3804e`). Independently recomputed from the saved arrays: 6,445 bricks, 65,060 raw objects, 53,005 retained, `L=40000.959939179214`, `N_eq=120002.87981753764`.
5. The exact permutation-variance identity held over all 25 exhaustive `(N, sign-balance)` cases for `N=4..8`; maximum standard-deviation discrepancy was `1.11e-16`.
6. The one-sided 95% Clopper–Pearson lower bounds independently computed as `0.9493659932051121` for 961/1000 and `0.950487129744074` for 962/1000, confirming the frozen 962 threshold.
7. All eight §2.2 predicate strings occur in both V10 and BS6-pred. The executable ellipticity predicate `POWER(shape_e1,2)+POWER(shape_e2,2) < 0.1836734693877551` is present byte-for-byte in both. The predecessor contains the quoted HC correction formula, 100,000 permutations, and one-sided Longo-sign rule.
8. V10's preamble correctly preserves writing-only authority and says no run, fetch, data touch, or freeze is authorized. I found no prose assumption that authorization already exists.
9. V10 accurately assigns the reported 997/1000 Stage-P result to the pre-reduction geometry and says it has not been re-run on the reduced artifact. I did not treat it as a measurement on the 6,445-brick set.
10. The 3×9 allocation fixtures enforce both stated floors and fail a sparse infeasible stratum closed. Finding 6 concerns the downstream population estimand, not those integer floor checks.

## Scope exclusions honored

Per §10 and the brief, I did not re-report or adjudicate the four disclosed-not-closed items: the clean-room normative specification, BS-9's input-function schema, the BS-V primary lock, and production scaling of the frozen O(n²) `greedy_ledger()` / `local_pass()` implementations. Findings above address separate claims presented as repaired or operative.

## Testimony

None. No unsupported testimony is used to support the recommendation.

## Custody boundary

I did not read `/Users/duhokim/NebulaMindData/`. I made no network request, catalog/image fetch, χ access, run authorization, freeze, publication, git mutation, or source-artifact edit. Review executions used the pinned fixtures, synthetic arrays, the already-acquired geometry/count artifacts named by the brief, and read-only inspection of the named files. The only persistent write made by this referee is this report.

Blocking findings: F1 fast reduction/full planning-chain equivalence; F2 Stage-P audit coverage; F3 count-oracle witness; F4 receipt interoperability and Stage-C chronology; F5 pre-statistic calibration validation; F6 HC-1H population weighting; F7 authorization and sample-completeness custody. F8 release branch invariance is major and also requires revision.

**REVISE**