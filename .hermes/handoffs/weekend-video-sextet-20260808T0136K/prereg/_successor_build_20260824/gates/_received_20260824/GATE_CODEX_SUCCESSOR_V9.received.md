# CODEX referee report — successor preregistration V9 (round 8)

## Recommendation

**REVISE.** The three dispatch digests match, the 34-check fixture transcript reproduces byte-for-byte, the frozen planner itself returns both historical neighbour bricks, and the corrected 6,445-brick NPZ reproduces exactly. Those positive results do not make V9 ready to freeze.

Four blocking findings remain outside the six open findings and four disclosed-not-closed items that V9 §10 instructs this round not to re-report:

1. the production closure entry point still calls the retired planner and therefore cannot produce any closure;
2. the fast reduction omits the frozen algorithm's swap-plus-removal phase and is demonstrably not equivalent to `local_pass()`;
3. the one-null/10×-band Stage-P mechanism can still count an unconfirmed unsafe success outside its audit band;
4. the claimed grouped-versus-ungrouped count-oracle completeness proof still compares one computed total with itself and accepts absent proof inputs.

No run, fetch, freeze, authorization, publication, git mutation, or study-data access was performed.

## Dispatch digests — computed before review

Command: `shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V9_20260825.md ../ref/successor_ref_v4.py ../ref/FIXTURES_V4_20260825.out`

- `../PREREG_SUCCESSOR_DRAFT_V9_20260825.md` = `b97ba35c8d1eeb66cc44e6915d2ae752fd19c374ff4906c9d15b8518056919b6`
- `../ref/successor_ref_v4.py` = `ffea5b6c58956c1f6c2e44939113f5170e459e566d132e8e3f69d117344e657b`
- `../ref/FIXTURES_V4_20260825.out` = `c5a4b95b554e16a7aea99213b06f21b18868e701c5a9682e8d3b325a18b10e72`

All three equal the brief's required values. Review proceeded.

Background-source digests independently computed:

- `../../SUCCESSOR_SCOPE_20260821.md` = `995b2e729a3362f0445cac9d5da6d290fddac9f8018e75f2c0aa87c190c93de7`
- `../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` = `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- `../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md` = `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`
- `../../VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md` = `43b9a6a843ef08a6528f1132db2bee29000c5ecd3def2a3a03c23f672c81cec7`
- `GATE_CODEX_SUCCESSOR_V8.md` = `d71dc0ae1b38cfaadc64a4397e2cc31720797d4a1bb35a6fee9084f53adc84ce`
- `../real/REAL_GEOMETRY_RESULT_20260825.md` = `1c5ee1f7987dc14edff360cc8681b54cbe1223684940cb51f839281407052f30`

## Environment and mandatory reference execution

- executable: `/Library/Developer/CommandLineTools/usr/bin/python3`
- CPython: `3.9.6`, Clang `21.0.0`
- NumPy: `1.26.4`
- platform: `macOS-26.6.2-arm64-arm-64bit`
- machine: `arm64`
- byte order: `little`
- command: `python3 -B ../ref/successor_ref_v4.py --fixtures`
- exit: `0`
- stdout bytes: `4,060`
- stdout SHA-256: `c5a4b95b554e16a7aea99213b06f21b18868e701c5a9682e8d3b325a18b10e72`
- `cmp` against `../ref/FIXTURES_V4_20260825.out`: exit `0`, byte-identical
- parsed named checks: `34`, all PASS; final transcript line: `ALL FIXTURES PASS`

## Numbered findings

### 1. BLOCKER — `close_manifest()` still invokes the retired planner, so the claimed production closure cannot run

**Quoted guarantee / symbols.** V9 §2.4 says `close_manifest()` is the single production entry point, derives every object's required bricks itself, binds BS-2m to the frozen `plan_candidate_bricks`, and refuses a manifest missing either historical neighbour (`V9:117-125,136-152`). The operative code retires `plan_object_bricks()` (`successor_ref_v4.py:198-215`) and exposes `frozen_plan_object()` (`232-235`).

**Direct execution.** The frozen planner itself works:

- `10997315463551936` → `['3385m885', '3471m885']`
- `10995116744378804` → `['2857m870', '2894m872', '2902m870']`
- `frozen_planner_digest()` → `36bbbf2502159474e0a56ec904e924e2ee80645b485c2ee20208ef25a514f610`
- direct calls to `plan_object_bricks()` refuse, as intended.

But `close_manifest()` still executes:

- `bs = plan_object_bricks(ra[i], dec[i], brick_table, halfsize_deg)` at `successor_ref_v4.py:308`.

I supplied a one-row parent with a matching parent digest, a cardinality-366,912 table, the pinned universe digest/cardinality, and a matching BS-2s witness. The production entry point reached line 308 and returned:

`RuntimeError: plan_object_bricks is RETIRED — it reproduced the defect it was written to prevent; use frozen_plan_object()`

The fixtures do not catch this wiring failure. `CLOSURE-FROZEN-PLANNER` calls `frozen_plan_object()` directly; `CLOSURE-CATCHES-HISTORICAL` computes a set difference directly; neither calls `close_manifest()` (`successor_ref_v4.py:1202-1238`). `planner_digest()` also still hashes `_ra_sep` plus the retired `plan_object_bricks`, not the operative frozen planner (`245-254`), and `close_manifest()` emits that retired digest (`324`).

**Why the guarantee fails.** V9 repaired the helper but did not wire it into the only production consumer. A complete manifest and a short manifest both fail before closure is evaluated. Thus BS-2m cannot be filled, and the fixture transcript can pass while the production path is unusable.

**Smallest sufficient repair.** Make `close_manifest()` consume the verified `GeometryIndex` produced by `load_geometry_sidecar()` and call `frozen_plan_object(geometry, objid, ra, dec)` for every parent row. Emit `frozen_planner_digest()`, not `planner_digest()` of the retired routine. Add positive and negative fixtures that call `close_manifest()` itself against the pinned real sidecar and historical rows: complete manifest accepts; omission of `3471m885` refuses by name; omission of `2857m870` refuses by name. This finding does not re-adjudicate §10's separately disclosed caller-trust issue.

### 2. BLOCKER — the 6,445-brick fast reduction is not equivalent to frozen `local_pass()`

**Quoted guarantee / symbols.** V9 says the corrected selection was run through the frozen reduction and that the fast reduction is “proven equal to `local_pass` on 30 random cases” (`V9:171-181,417-418`; real receipt `129-149`). The frozen `local_pass()` performs repeated removals and then a swap-plus-removal search (`successor_ref_v4.py:470-497`). The fast `reduce_removals()` performs only the repeated-removal phase and returns as soon as no single removal is legal (`reduce_fast.py:24-56`). It implements no swap.

**Direct reproduction of the reported artifact.** SHA-256 of `real_selection_reduced.npz` is `b913939d54b66bda5a4ef05ee46d0b1321a6b490d1d232ba197c9aa0c9a3804e`. Reapplying `reduce_removals()` to `real_selection_dr10.npz` at the actual margin target `L=40,000` reproduces the NPZ exactly:

- index array equal: `True`
- brickid array equal: `True`
- removed brick: `[155487]`
- bricks: `6,445`
- raw objects: `65,060`
- retained objects: `53,005`
- `L_ret = 40000.959939179214`
- `N_eq = 120002.87981753764`
- retained-object `Var(c) = 0.7546638984846565`

Those numbers are correct for the removal-only artifact.

**Counterexample to equivalence.** The shipped 30-case check passes, but an expanded deterministic stress test with `np.random.default_rng(2026082509)`, 18–30 bricks, alternating one- and two-decimal tied `c`, integral raw counts 1–59, and target uniformly 0.25–0.90 of full retained SSE found a mismatch at trial 47. Inputs were:

- `brickid = [1018,1009,1000,1021,1016,1019,1017,1026,1014,1010,1005,1002,1020,1003,1024,1013,1008,1012,1023,1022,1015,1007,1001,1004,1006,1025,1011]`
- `c = [-0.79,0.63,-0.43,0.81,0.99,0.12,0.97,-0.49,0.03,0.17,-0.39,-0.8,0.35,-0.96,-0.75,0.1,-0.2,0.54,-0.4,-0.75,0.92,-0.89,-0.53,0.67,0.58,-0.23,0.52]`
- `n_raw = [37,43,58,51,12,19,56,34,15,11,44,36,36,41,35,54,34,44,15,55,20,19,14,20,14,3,22]`
- target `165.70553675316538`

Fast removal returned seven bricks `[1002,1003,1016,1017,1018,1021,1022]`, `L=177.63594221311476`. Frozen `local_pass()` used a swap followed by a removal and returned six bricks `[1003,1015,1017,1018,1021,1022]`, `L=165.7432886877828`.

The fast greedy implementation withstood its shipped 40 cases, and the V3/V4 source bodies of `greedy_ledger`, `local_pass`, `retained_counts`, and `sse` are byte-equal. Those failed attacks support the order implementation; they do not repair the missing reduction phase.

**Stage-P consequence.** `rerun_real_power_v4.py:15-16` loads `real_selection_dr10.npz`, not `real_selection_reduced.npz`. Therefore the reported `997/1000, 77/77` is the explicitly disclosed pre-reduction result. No Stage-P receipt exists for either the removal-only 6,445 set or the actual full-`local_pass()` result.

**Why the guarantee fails.** Thirty random cases were evidence, not proof, and this counterexample defeats the claimed equivalence. The corrected NPZ is demonstrably the output of a strict subset of the frozen algorithm. Its cardinality and geometry cannot be represented as the frozen `local_pass()` output until the omitted phase is implemented and run. The final-set Stage-P re-pass required by BS-2s is also absent.

**Smallest sufficient repair.** Implement a scalable equivalent of both frozen phases, including the exact selected-brick and outside-brick ordering for swap-plus-removal; replay this counterexample as a pinned fixture; expand adversarial tie/near-threshold tests; emit a hash-pinned producing script and artifact; then rerun Stage P on that exact final set before claiming BS-2s filled or freeze readiness.

### 3. BLOCKER — the 10× power audit still permits unconfirmed unsafe successes outside the band

**Quoted guarantee / symbols.** V9 says Stage P measures one 20,000-permutation standardized null per prefix, judges 1,000 trials against it, confirms successes “within 10× of the decision threshold,” and fails on one refutation (`V9:229-252`). `stage_power()` confirms only when `0.0001 <= p_calibrated < 0.001`; a smaller calibrated p is counted without confirmation (`successor_ref_v4.py:711-747`). Confirmation uses 20,000 permutations, not production's 100,000 (`MC_CAL_PERM`, lines 92 and 738).

**Finite-sample counterexample.** Under the benign case where calibration and confirmation Monte Carlo are independent draws from the same true tail probability `q=0.001`:

- with 20,000 calibration permutations, `X <= 1` has probability `4.289410839921657e-08`;
- at `X=1`, plus-one `p_cal = 2/20001 = 9.99950002499875e-05`, which is below the confirmation band and is therefore unconfirmed;
- with 100,000 full permutations, `X >= 100` (plus-one p at or above 0.001) has probability `0.5133187403795949`;
- the independent joint probability is `2.201834969319165e-08` per trial, or `2.2018107539323317e-05` for at least one among 1,000 independent trials.

A guarantee fails on a possible input regime; it need not be likely. The current design explicitly counts this calibrated success without asking the full test.

The pinned transcript independently shows that standardization does not make the null invariant across sign multisets: tail masses at z=3.090 are `0.00135, 0.00130, 0.00100, 0.00110`, a 35% relative spread. `PWR-Z-STABLE` accepts any spread below 50% and merely states that a 1% statistic deflation “absorbs it”; no simultaneous bound connects those two percentages. The transcript also records that calibrated decisions alone confirmed only 21/22 in its tested family.

**Why the guarantee fails.** The 10× boundary is an affordability heuristic, not an equality or conservatism proof. Every counted success outside it bypasses the check that V9 relies on to turn a measured approximation into a self-confirming gate. One shared null per 1,000 changing sign multisets is likewise measured on examples, not bounded over admissible trials.

**Smallest sufficient repair.** Confirm every counted success at the same 100,000-permutation contract used for the scientific decision, or derive a finite-sample simultaneous upper bound that covers reference-null sampling error and every admissible sign multiset, then count only successes certified under that bound. If a band remains, prove that an outside-band calibrated success cannot cross p=0.001 under the bound.

### 4. BLOCKER — the count-oracle completeness proof still compares one total with itself and accepts absent proof inputs

**Quoted guarantee / symbols.** V9 says BS-2c uses a complete left join over an independently enumerated universe, materializes zero rows, and refuses “any grouped/ungrouped disagreement”; `build_plan()` is said to perform this complete chain (`V9:89-97`).

**Real-number reproduction.** I read only the already-acquired lane artifacts named by the brief, not `/Users/duhokim/NebulaMindData/`:

- universe digest: `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a`
- grouped-count digest: `4e4ec45d83f156e8daa738d81cd71a1e140d4ccbadd5343dc0bb8ed9f2479aa0`
- universe rows: `366,912`
- grouped keys: `270,577`
- materialized zeros: `96,335`
- total: `832,393`
- keys outside universe: `0`
- count-weighted `Var(c) = 0.4452013461602878`

These numeric claims hold for the inspected bytes.

**Proof failure.** `build_real_oracle.py:69-72` supplies:

- `grouped_sum=int(n_elig.sum())`
- `ungrouped_total=int(n_elig.sum())`

Both come from the same left-joined array. No independent ungrouped query/result is run or consumed. The validator therefore proves one integer equals itself. Independently, `validate_count_table([1,2],[-.5,.5],[1,1], None, None, None)` returned `{'rows': 2, 'zero_rows': 0}`. Although `build_plan()` names the three proof arguments as keyword-only, explicit `None` values reach this accepting path (`successor_ref_v4.py:349-387,761-782`).

**Why the guarantee fails.** Universe closure establishes key coverage for the grouped rows that exist; it does not prove the grouped query omitted no nonzero group because of a shared scope/join defect. The named grouped-versus-ungrouped independent total is absent, and production does not fail closed when all proof inputs are explicitly absent.

**Smallest sufficient repair.** Produce and pin a genuinely independent ungrouped total with separately specified query text/scope and raw receipt; prohibit `None` in `build_plan()` before calling the validator; derive the grouped total and zero materialization inside the consumer from typed, hash-verified artifacts; add negative fixtures for omitted proof inputs and deliberately scope-mismatched grouped/ungrouped results.

## Statistical and quotation checks that held

1. The exact permutation-variance identity held across 25 exhaustive `(N, sign-balance)` cases for `N=4..8`; maximum formula-versus-enumeration standard-deviation difference was `2.220446049250313e-16`.
2. The centred `beta_slope()` projects out the monopole; no `3*D` production decision path was found.
3. All eight V9 §2.2 cut strings occur in BS6-pred with matching executable/numeric content. The ellipticity predicate is byte-identical: `POWER(shape_e1,2)+POWER(shape_e2,2) < 0.1836734693877551`. The no-surface-brightness-cut disclosure is preserved.
4. The predecessor states the our-convention target as `+0.0408`; V9 and the code preserve `A_LONGO=+0.0408` and `A_LONGO_PUBLISHED_SIGNED=-0.0408`. No sign inversion found.
5. The frozen planner's two historical outputs and retirement refusal hold. Finding 1 is strictly the production wiring and fixture-coverage failure.
6. The corrected reduction-only NPZ's 6,445/65,060/53,005/0.754664/120,002.9 values reproduce exactly. Finding 2 is strictly whether that artifact is the frozen algorithm's output and whether it has its required final-set power receipt.
7. The preamble correctly preserves writing-only authority and says no run, fetch, data touch, or freeze is authorized. I found no text assuming an authorization exists.

## Scope exclusions honored

Per the brief, I did not re-report or re-adjudicate V9 §10's six explicitly open findings: closure caller-trust custody, Stage-C mask chronology, receipt round-trip consumption, HC-1H population weights/boundary tie, the release availability probe, and the integrated production battery. I also did not re-report the four disclosed-not-closed items: clean-room specification, BS-9 input schema, BS-V primary lock, and production scaling of the frozen O(n²) routines. Findings 1–4 above attack separate claims that V9 presents as operative or repaired.

## Testimony

- V9's declared `Cov(beta_hat, a_hat)=0` and profile analogue remain testimony. I did not treat either as proved or use either to rescue a finding.
- I did not re-check live DR11 photo-z availability; it is not a premise of this recommendation.

## Custody boundary

Read-only review covered the dispatch artifacts, V8 gate, real receipt and scripts, amended scope, frozen predecessor, BS-6 receipt, lapsed build spec, and the frozen object-manifest planner named by V9. Executions used fixtures, synthetic arrays, finite combinatorics, and already-acquired catalog-count/geometry artifacts in the lane. `/Users/duhokim/NebulaMindData/` was not read. The only persistent write authorized and made by this referee is this report.

Blocking findings: F1 production closure calls the retired planner; F2 fast reduction is not frozen `local_pass`; F3 the 10× power audit can miss unsafe successes; F4 the count-oracle completeness proof is self-comparison and optional.

**REVISE**
