# GPT56 ADVERSARIAL GATE — successor preregistration V7

## Verdict

**REFUSED.** The three custody pins match and the pinned fixture transcript reproduces byte-for-byte, but V7 is not freeze-candidate grade. Several V6 attacks still succeed. Stage C and BS-7f still accept `FixtureMask`; the production runner accepts self-asserted authorization/completeness/Stage-C inputs and computes the real permutation record before discovering a calibration halt; `build_plan()` still has a public override that bypasses Stage P and its closure proofs remain optional; the HC allocator still refuses a feasible allocation and the estimator still cannot implement population-weighted HC-1H; the release resolver still takes an unverified caller Boolean and its invariance fixture is vacuous; the lapsed floor-edge battery remains missing; and the claimed slot-schema repair consists mostly of field names, omits eight slots, accepts empty payloads, and leaves §7 pointing at nonexistent symbols.

The directed measured-null repair also fails as a power-equality contract. A 20,000-permutation reference has only about twenty observations in the decision tail, the 1% deflation does not cover the pinned fixture's own sign-multiset critical-value spread, and 22/22 high-signal spot confirmations do not bound the 962/1000 power decision. The analytic Stage-P path can therefore overstate true full-permutation power.

## Custody pins — computed before review

Command:

`shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V7_20260825.md ../ref/successor_ref_v3.py ../ref/FIXTURES_V3_20260825.out`

Computed:

- `f15b0b4dad9d5c565969e18aa8dee200cc8a80c9b7f817e68c8b3e239f800286  ../PREREG_SUCCESSOR_DRAFT_V7_20260825.md`
- `b89c21288935a026f882d2f417c68d82e12934beae1b00e72474186f03d74e90  ../ref/successor_ref_v3.py`
- `445e32c8c573423729a196cfd35f70faf26dc5073ca3295d89219c756142b33a  ../ref/FIXTURES_V3_20260825.out`

All three equal the brief's required pins. Review proceeded on those bytes.

Binding-source pins independently recomputed:

- amended scope: `995b2e729a3362f0445cac9d5da6d290fddac9f8018e75f2c0aa87c190c93de7`
- V3-pred: `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- BS6-pred: `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`
- lapsed build spec: `43b9a6a843ef08a6528f1132db2bee29000c5ecd3def2a3a03c23f672c81cec7`
- signed decline memo: `b4a1f1fcaa9acbaa6b9efd3ebbe9496be8c1d83c690a012dc7a4f8520840374f`
- predecessor Longo-sign receipt: `b7c32dcf12d9e147e5dee6a8262d925b61011615f2ee1d75d687600abb0a72ca`

## Environment and fixture reproduction

- command: `python3 -B ../ref/successor_ref_v3.py --fixtures`
- executable: `/Library/Developer/CommandLineTools/usr/bin/python3`
- Python: `3.9.6`, Clang 21.0.0 build
- NumPy: `1.26.4`
- platform: `macOS-26.6.2-arm64-arm-64bit`
- machine: `arm64`
- byte order: little-endian
- exit: 0
- stdout: 3,359 bytes
- stdout SHA-256: `445e32c8c573423729a196cfd35f70faf26dc5073ca3295d89219c756142b33a`
- byte comparison with the pinned fixture output: exact

## V6 reattack summary

The required first attacks produced these results:

- **Still succeeds:** `stage_power(FixtureMask, STAGE_C, n_trials=1)` returned `(0, None)` rather than refusing.
- **Still succeeds:** `perm_record(FixtureMask, STAGE_REAL, n_perm=2)` returned a numeric production-shaped record.
- **Still succeeds in a new explicit seam:** monkeypatching `stage_power()` to raise did not stop `build_plan(..., l_plan_override=1.0)`; it returned a selected set with `repass=None`.
- **Still succeeds beneath the new guards:** a 100,100-row mask was accepted as complete from caller values `n_receipts=n_parent=1`; an arbitrary `/tmp` file authorized itself when the caller supplied its own digest; a free dictionary stood in for BS-5f. Instrumentation showed the permutation record was called before `InconclusiveByCalibration` was raised.
- **Still succeeds:** a feasible 500-label HC allocation was refused.
- **Still contradicted:** `assign_bins()` puts equality to the first boundary in bin 0 while `calibration_bins()` says `side='left'` sends equality to the HIGHER bin.
- **Repaired:** negative counts, floating counts, duplicate brick keys and unequal table lengths refused.
- **Repaired:** the 17-raw-positive/16-retained-positive case takes the heuristic branch.
- **Repaired at the named runner signature:** `run_production_verdict()` exposes no `_perm`, `n_perm`, stage or trial parameter and names all five guards/full-permutation calls.
- **Repaired:** extra-length signs and disagreeing supplied bins are refused by `SealedMask` construction.
- **Repaired in the basic formula only:** raw 0.9 with epsilon 0.02 gives 0.9166666666666667 and the shared-epsilon term creates off-diagonal covariance. Finding 6 explains why the full HC-1H producer is still absent.

## Numbered findings

### 1. BLOCKER — the measured Stage-P null is not conservative by construction and does not protect the 962/1000 decision

**Quote / symbol.** V7 §4 says one measured standardized null per prefix, 20,000 permutations and `PWR_CONSERVATISM = 1.01` make an analytic success imply a full-Monte-Carlo success (`V7:182-199`; `successor_ref_v3.py:580-651`). The fixture calls 22/22 individual confirmations across four toy geometries a decision-metric contract and lets `PWR-Z-STABLE` pass whenever relative tail-mass spread is below 50% (`1114-1165`).

**Executed attacks.** Recomputing the fixture's four polar sign multisets gave empirical 0.999 critical values:

- plus fraction 0.500: `q=3.230688`, 1%-inflated `3.262995`
- plus fraction 0.334: `q=3.199589`, inflated `3.231585`
- plus fraction 0.200: `q=3.081627`, inflated `3.112443`
- plus fraction 0.143: `q=3.108094`, inflated `3.139175`

The measured critical spread is `0.149061`, while 1% of the smallest critical value is only `0.030816`; inflating the smallest by 1% still leaves it below the largest. Thus the fixture's own 35% fixed-z tail-mass spread is not “absorbed” by the deflation in the statistic that actually controls the decision.

Independently, under the normal model used only to quantify the finite-reference uncertainty, a raw statistic with true one-sided full-null `p=0.001` has `z=3.0902323`; after division by 1.01 the reference-tail probability is `0.00110803`, or 22.16 expected exceedances in 20,000. The empirical rule passes with at most 19 exceedances. The exact binomial probability of that empirical Stage-P success is **0.29422**. The 1% margin therefore does not even make an individual boundary statistic fail closed against reference-tail sampling noise.

The 22/22 fixture confirmations are at an artificial `0.14` signal, use only 5,000 permutations for the purported “full” check, and do not compare analytic versus full-MC success counts over 1,000 addressed trials. A one-sided 95% lower bound for 22/22 is only `0.87269`. The same estimated reference is shared by the 1,000 decisions, so its threshold error is common-mode and is absent from the Clopper–Pearson calculation. Although the correct CP lower bounds are `0.94936599` at 961 and `0.95048713` at 962, those bounds apply only when each success classification is valid.

**Why it blocks.** A low empirical reference tail can jointly inflate the 1,000 success indicators. Nothing in PWR-CONTRACT or PWR-Z-STABLE bounds the probability or magnitude of that inflation at the `x=962` boundary. Stage P can therefore pass while true full-permutation power is below 0.95. Production's eventual full permutation record does not repair a footprint selected under an overstated planning-power gate.

**Minimal repair.** Treat null calibration uncertainty and sign-multiset dependence as part of the power test. For every actual prefix/final geometry, compare addressed 1,000-trial analytic and 100,000-permutation decisions (or establish a proved finite-population conservative bound), and require a confidence-bounded lower limit on full-MC power ≥0.95. If a measured reference remains, use enough independent null draws/permutations to bound its tail threshold and include that common calibration uncertainty in the pass rule. Tail mass at one fixed z and 22 high-signal spot checks are not substitutes.

### 2. BLOCKER — Stage C and BS-7f still accept fixture inputs, while `SealedMask` is a caller-selected label rather than sealed provenance

**Quote / symbol.** V7 says production entry points call `require_sealed()` and Stage C runs on the sealed accepted-position mask (`V7:164-172,201-205`). `stage_power()` instead calls `require_any_mask()` (`successor_ref_v3.py:640-651`), and `perm_record()` does the same (`562-577`). `SealedMask` can be constructed directly from arbitrary arrays and has no accepted-mask source digest, sealing receipt, parent digest or issuer field (`431-505`).

**Executed attacks.** A `FixtureMask` passed `stage_power(..., STAGE_C, n_trials=1)` and returned normally. The same fixture passed `perm_record(..., STAGE_REAL, n_perm=2)` and returned numeric beta, p and sigma. Separately, arbitrary caller arrays wrapped directly in `SealedMask` passed `require_sealed()`; the class slots contain only arrays, kind and digest, not a sealing/source credential.

**Why it blocks.** The exact V6 FIXTURE-mask-to-production attack remains available through the symbols assigned to BS-5f and BS-7f. Where the runner does call `require_sealed()`, a lazy caller can relabel parent/planning/rejected positions as `SealedMask`; the digest proves those caller-selected bytes, not that BS-2f produced them. Distinct Python classes prevent accidental interchange, not provenance substitution.

**Minimal repair.** Add operation-specific production functions `run_stage_c()` and `run_bs7f()` that require a verified BS-2f envelope, accepted-parent/source digest, boundary digest and immutable sealing authority; make generic `stage_power()` and reduced-count `perm_record()` explicitly synthetic/private. A production mask must be reconstructed from and cross-checked against the BS-2f receipt rather than accepted because its constructor name says “Sealed.”

### 3. BLOCKER — production guards are self-asserted, BS-5f is an unverified dictionary, and calibration is checked after the real statistic

**Quote / symbol.** V7 says `run_production_verdict()` requires pinned authorization, sample completeness and a BS-5f receipt, and emits `INCONCLUSIVE-BY-CALIBRATION` pre-unblinding (`V7:209-224,236-239,259-261`; code `926-977`).

**Executed attack.** On a 100,100-row `SealedMask`, the runner accepted:

- `n_receipts=1, n_parent=1`, because `require_complete_sample()` compares only the two caller integers and never binds either to the mask or parent receipt;
- an arbitrary temporary text file, because the caller supplied both its path and matching expected SHA;
- `{'slot':'BS-5f','passed':True,'mask_digest':m.digest}`, a free dictionary with no envelope/schema/digest verification.

With an inadmissible calibration, instrumentation recorded `perm_record()` called before `_decide_from()` raised `InconclusiveByCalibration`. With an admissible calibration and the same self-asserted guards, the path reached a numeric verdict. The monkeypatch of `perm_record()` in this probe was instrumentation to avoid a 100,000 × 100,100 kernel; the ordering and unbound guard acceptance are explicit in the body.

**Why it blocks.** The authorization hash is not pinned by the code or a predecessor receipt; sample completeness is detached from the actual mask/parent; and BS-5f is neither the output of `receipt()` nor verified against one. Most seriously, calibration invalidity is discovered only after a real-sky permutation statistic has been formed, contradicting the pre-unblinding halt. The V6 calibration-exception defect therefore survives, and the new guard calls do not establish what their names claim.

**Minimal repair.** One immutable run configuration must pin the authorization path/hash, parent digest/count, BS-2f envelope and BS-5f envelope. Verify all envelope digests and schemas, require mask cardinality/source consistency, and call `adjudicate_path(cal)` before any sign-bearing input reaches `perm_record()`. Return and atomically receipt `INCONCLUSIVE-BY-CALIBRATION`; never raise it after unblinding.

### 4. BLOCKER — manifest closure moved the supplied-answer seam into an unbound brick table, and the planner fails a wrap rectangle

**Quote / symbol.** V7 says `close_manifest()` derives every required brick from the frozen parent and implemented planner and cannot be handed an answer (`V7:110-130`; code `167-265`). The entry point nevertheless accepts caller-supplied `brick_table` without an expected survey-bricks digest. Its receipt result does not bind that table. `planner_digest()` hashes only `plan_object_bricks.__code__.co_code` and halfsize, excluding `_ra_sep` and code constants (`207-210`).

**Executed attacks.** A one-object frozen parent plus a lazy one-row brick table and one-brick manifest passed with `required_count=manifest_count=1`, zero missing and zero extra. A duplicate candidate manifest `['home','home']` was set-deduplicated and recorded as one entry, also passing. For a rectangle `(ra1,ra2)=(350°,10°)` that contains an object at RA 0°, `plan_object_bricks()` returned an empty set because it computes the wrapped half-width but the arithmetic centre as 180°.

**Why it blocks.** V7 prevents the caller from supplying a per-object answer map but still lets it supply the geometric universe from which the answer is derived. A truncated, wrong-release or home-only brick table recreates the short-manifest defect with a clean receipt. The planner digest cannot prove the helper or input geometry used, and the stated every-intersecting-rectangle contract is false at RA wrap.

**Minimal repair.** Pin and verify the exact release survey-bricks payload digest and schema inside `close_manifest()` and BS-2m; bind it into the plan and receipt. Hash the complete source/dependency closure plus constants/configuration, or pin the whole reference-file hash as planner code identity. Reject duplicate manifest entries. Implement and test wrapped RA intervals and the actual release's polar/edge geometry, including the two inherited objects against the pinned release table.

### 5. BLOCKER — `build_plan()` still permits a no-power path and makes BS-2c closure proofs optional

**Quote / symbol.** V7 says `build_plan()` performs BS-2c → BS-2o → BS-5p → BS-2s in one frozen call with integrated oracle and mandatory final Stage-P re-pass (`V7:87-108`; code `665-704`). But `universe_brickid`, `grouped_sum` and `ungrouped_total` default to `None`, and `l_plan_override` skips both planning power and final re-pass.

**Executed attack.** After replacing `stage_power()` with a function that raises if called, `build_plan([1,2],[-1,1],[100,100],l_plan_override=1.0)` returned selected bricks `[1,2]` and `repass=None`. No universe, grouped total or ungrouped total was supplied. `validate_count_table([1,2],[-1,1],[5,7])` likewise returned a clean record containing only rows/zero_rows.

**Why it blocks.** The exact production symbol can satisfy the constitution while bypassing the power gate, final re-pass and both count-closure proofs. The strict negative/float checks are real, but they do not establish universe completeness or independent grouped/ungrouped accounting when those inputs are optional.

**Minimal repair.** Split an explicitly named synthetic helper from a production `build_plan()` with no `l_plan_override` and mandatory universe/query-proof receipts. Require independently scoped grouped and ungrouped evidence, exact typed totals and branch/query digests. The production function must always emit a passing 1,000-trial Stage-P receipt for the prefix and final selected mask or return `INCONCLUSIVE-BY-POWER`.

### 6. BLOCKER — the HC-1H producer remains incomplete, the allocator still rejects a feasible plan, and the tie statement still contradicts the body

**Quote / symbol.** V7 claims the inherited HC-1H estimator, 3×9 allocation, population logic and both floors are implemented (`V7:248-263`; code `716-824`). V3-pred requires nine strata, fixed 500 real labels, floor 30 per stratum, population weighting, and the synthetic/repeat integrity protocol (`V3-pred:279-329`).

**Executed attacks.** A 3×9 capacity table with live cells `[10,100]` in stratum 0 and one 100-capacity cell in each other stratum has an explicit feasible 500-label allocation: stratum totals `[80,53,53,53,53,52,52,52,52]`, every live cell ≥10, every live stratum ≥30, every allocation ≤ capacity. `allocate_handcheck()` nevertheless raised `allocation exceeds available objects in a cell` because its post-floor proportional share uses original counts rather than residual capacity.

`accuracy_from_handcheck()` accepted two bins and has signature `(agree_counts, n_counts, epsilon_hat, sigma_epsilon)`: no 3×9 records, stratum population weights, synthetic/repeat roles or integrity triggers. The same pooled counts yield `a_hat=0.7083333`, although two admissible population-weight vectors over raw rates 0.9 and 0.5 imply corrected accuracies `0.8750` and `0.5416667`. The producer cannot distinguish them. Finally, equality to boundary 0 is assigned bin 0 by `side='left'`, while the code docstring says HIGHER bin.

**Why it blocks.** Calibration controls attenuation, scalar/profile selection, Stage C, uncertainty and the final floor. A feasible realized sample can be falsely halted, while a formally populated but population-misweighted sample can emit the wrong point estimate/covariance. Correcting `(raw−epsilon)/(1−2epsilon)` alone did not implement HC-1H.

**Minimal repair.** Consume the raw 3×9 realized records, frozen population counts/weights, synthetic and repeat roles, sealed-key/integrity receipts and fixed 500-label budget. Allocate over residual capacities with a proved capacity-safe integer method and test adversarial sparse cells. Produce population-weighted scalar/per-bin estimates and full shared-epsilon covariance. State the actual tie direction correctly and test high-multiplicity boundary ties.

### 7. BLOCKER — the release choice remains a caller assertion and branch invariance is vacuous or incompatible with provenance

**Quote / symbol.** V7 calls the choice point bound and machine-checkable (`V7:59-76`; code `980-1014`). `resolve_branch(photoz_available, resolution_date)` accepts a caller value; no availability-probe symbol, endpoint, status/error rule or immutable timestamp verifier exists. It validates neither Boolean type nor date.

**Executed attacks.** `resolve_branch('false','not-a-date')` selected `A_DR11`, because a nonempty string is truthy. Symbol inventory found no availability/probe producer. The fixture's invariance lambda ignores `cfg`, so both hashes are necessarily equal. A function that records the branch's required release provenance makes the hashes differ and therefore fails `branch_invariance()`.

**Why it blocks.** The Sep-5 datum still cannot slot in as a verified fact; a caller narrates availability. Equality of output digests proves only that the fixture ignored configuration, while real branch-specific input provenance must differ. The mechanism neither proves a common code path nor permits enumerated configuration differences. This is the V6 finding restated in code, not repaired.

**Minimal repair.** Pin a deterministic availability probe with exact URL/product identifiers, accepted status/content rules, retries/timeouts and fail-closed behavior; validate the immutable resolution date. Define a common typed configuration including columns/join keys/HDU/layout. Verify code-path identity separately from output provenance, with a comparator that permits only enumerated config fields to differ and requires all algorithm/schema digests to match.

### 8. BLOCKER — §10 claims slot schemas are repaired, but the slot machine still has stale/nonexistent symbols and accepts empty payloads

**Quote / symbol.** V7 §10 says “slot register lacks schemas” is repaired by `SLOT_SCHEMA` and `receipt()` (`V7:354-369`). Section 7 still has the old five-column/four-column tables with no inputs or schemas (`285-313`). Code `SLOT_SCHEMA` covers only 10 slots (`successor_ref_v3.py:125-152`) and checks only exact field names.

**Executed attacks and slot walk.** A BS-2c receipt with every required field set to empty bytes passed. `receipt('BS-1', {})` also passed because unknown slots are unrestricted. The 18-slot register has schemas only for BS-2c, 2o, 5p, 2s, 2m, 2f, 8f, 5f, 7f and V; BS-1, 1b, 3, 9, 4, 7p, 8p and 6 are absent. In addition:

- BS-2c points to nonexistent `validate_count_oracle` (actual body: `validate_count_table`).
- BS-2o points to nonexistent `ledger_digest`.
- BS-2m points to nonexistent `manifest_closure` and `require_manifest_closure` (actual body: `close_manifest`).
- BS-4 and BS-V point to nonexistent `decide`.
- Class E still has no code-symbol column.
- BS-5f's runner expects a free dictionary with direct `passed` and `mask_digest` keys, but `receipt()` returns only slot/schema/environment/body/envelope hashes; the two representations do not connect.
- BS-2m's schema omits the brick-table digest and the promised missing/extra names; BS-8f omits `sigma_epsilon` and integrity triggers; BS-5p/2s do not bind actual masks/nulls/addresses.

I did **not** count §10's acknowledged open clean-room specification, BS-9 input schema or BS-V primary lock as new findings. The blocker is that the rest is claimed closed when it is not.

**Why it blocks.** Producers can emit semantically empty, wrong-type or wrong-shape receipts with valid envelope hashes. Several slots cannot invoke the symbol named by the constitution, and execution gates do not consume the claimed envelopes. There is no machine-checkable acyclic slot contract.

**Minimal repair.** Replace §7 with the promised register: exact predecessor/input digests available at that time, typed fields and shapes, canonical serialization, actual code symbol/file hash, producer, predecessor dependencies, failure outcome and next block. Reject unknown slots and validate field content, not names alone. Make each consumer verify the predecessor envelope it names. Correct every symbol to an existing body and add cross-slot end-to-end fixtures.

### 9. BLOCKER — the lapsed-spec floor-edge validation case is still missing

**Quote / symbol.** The lapsed spec requires “A just below the evaluated floor must not return REPRODUCED even when the band would allow it” (`VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md:68-77`). Both V6 gates named its absence. V7 says the battery is restored at the lapsed spec's named boundaries (`V7:229-234,367`; fixtures `successor_ref_v3.py:1265-1296`).

**Code evidence.** The V7 battery contains A=0, negative sign, positive +0.0408 and a low-N_eq geometry. Source inspection found no just-below-floor fixture. `BATTERY-NEQ` also checks only the geometry arithmetic; it does not call the production runner and assert the returned outcome.

**Why it blocks.** This is an explicit V6 repair obligation that V7 claims to have carried but did not. A body-level floor condition exists, but the named boundary/integration test that should catch attenuation, lower-bound evaluation and strict verdict wiring is absent. Under the brief, a repair that responds without repairing is a refusal.

**Minimal repair.** Add an addressed synthetic case whose A is just below the evaluated `3.09·sigma_ours(a_LB)` floor while p and the Longo band would otherwise permit reproduction, and assert non-REPRODUCED through the integrated production-equivalent decision path. Add a runner-level N_eq case asserting `INCONCLUSIVE-BY-POWER`, not merely `n_eq_small < NEQ_MIN`.

## Directed citation and sign-anchor result

This attack held. arXiv:1104.2815 independently verifies Michael J. Longo, the title, 15,158 spirals, redshift `<0.085`, amplitude `−0.0408±0.011`, chance probability `7.9×10⁻4`, approximate Galactic axis `(52°,68.5°)`, and related DOI `10.1016/j.physletb.2011.04.008`. Crossref independently verifies the DOI, author, journal, volume 699 and pages 224–229. ADS presented a human-verification wall, but the exact record identifier is consistent with the citation `2011PhLB..699..224L` and the DOI metadata.

The predecessor sign receipt quotes Longo's `(R−L)/(R+L)` convention and maps the published negative amplitude to the project's `(L−R)` / CCW-positive convention. V7 and code consistently record Longo's `−0.0408` and the project target `+0.0408`; no inversion was found. Independent Galactic-to-ICRS conversion produced vector `[-0.6769717712430396,-0.5098465517524211,0.5308160835723453]`, RA `216.984435505°`, Dec `32.060610904°`, maximum component difference `3.50e-11` from `AXIS`, and code-axis norm `0.9999999999999998`.

## Quotation fidelity and attacks that held

1. All eight photometric predicates occur in V7 and BS6-pred with matching operator/numeric content; the ellipticity executable string is byte-identical. The no-surface-brightness-cut disclosure is preserved.
2. The amended scope's prohibition on contiguous BRICKID selection and its no-global-optimality discipline are preserved.
3. Exact permutation mean zero and the variance formula held under independent exhaustive enumeration for N=4…7 and multiple sign balances; maximum mean/sd discrepancy was `1.11e-16`.
4. Static AST checks found zero matrix-multiply nodes, zero `.spawn()` calls, zero `.binomial()` calls and exactly two `rng.random()` calls inside `inject_signs()`.
5. `sigma_ours_profile()` uses the explicit scalar double loop; no matrix-multiply body contradicted the no-BLAS claim.
6. Negative/floating count-table attacks and the 17/16 branch attack are genuinely repaired as stated above.
7. The draft/run boundary is explicit. V7 authorizes writing only and assumes no authority to run, fetch, freeze, publish, commit or disclose.
8. The predecessor was declined by the signed memo at the pinned digest; V7 correctly treats its sample as archived successor input, not as a continuing run authorization.
9. The historical manifest-defect shape is consistent with the Trio report section: 60,310 required vs 60,308 frozen, with the two named objects/bricks. I treat those historical numbers as an author record, not an independent raw-data reproduction.

## Inherited-defect closure matrix

| inherited defect | V7 result |
|---|---|
| 1. manifest-versus-parent gap | **OPEN:** parent completeness is better, but the caller supplies an unbound/truncatable brick table; wrapped RA geometry also fails (Finding 4). |
| 2. footprint-blind power | **OPEN:** the planning null is not a valid 962/1000 equality contract, Stage C accepts `FixtureMask`, and arbitrary arrays can self-declare `SealedMask` (Findings 1–2). |
| 3. full-sky `3·D` normalization | **CLOSED for the named estimator defect:** centred `beta_slope()` is used; `3·D` is not a decision estimator. |
| 4. attenuation-versus-target mismatch | **OPEN as an HC-1H production contract:** beta/A split exists and the basic epsilon correction is fixed, but population weighting and valid allocation are not implemented (Finding 6). |
| 5. unreachable p threshold | **CLOSED in `run_production_verdict()` for the named plus-one defect:** it fixes 100,000 permutations. Generic BS-7f still permits reduced counts, but the runner does not consume that path. |
| 6. silent axis divergence | **CLOSED for the pinned reference:** one axis constant; independent transform held. |
| 7. contiguous/count-based selection | **PARTLY CLOSED:** raw boundary and leverage selection are repaired, but the production-named orchestrator can bypass Stage P and closure proofs (`l_plan_override`, optional oracle inputs; Finding 5). |
| 8. verdict by human reading | **OPEN:** a runner exists, but guard evidence is self-asserted, calibration halts after the real statistic, and the lock remains acknowledged-open (Finding 3; acknowledged lock not counted separately). |

## Testimony

- V7 explicitly labels `Cov(beta_hat,a_hat)=0` and the profile analogue as freeze testimony. I found no independent proof and did not use them to rescue a finding.
- The drafting-time DR11-page/photo-z status is not tied to a receipt in this packet and was not re-fetched; no release branch was resolved by this gate.
- The exact historical 60,308/60,310 object/brick facts were checked only against the cited author record under the allowed tree. No source row, image or `/Users/duhokim/NebulaMindData/` path was read.
- The claim that 1% deflation “absorbs” measured sign-multiset dependence is not testimony I accept: the pinned test's own critical-value spread contradicts it quantitatively (Finding 1).

## Evidence ledger and boundary

Read: the V7 brief; pinned V7 constitution, code and fixtures; both V6 gate reports; amended scope; V3-pred; BS6-pred; lapsed build spec; signed decline memo; predecessor Longo-sign receipt; and the cited Trio manifest section. External source checks used arXiv and Crossref; ADS was blocked by human verification.

Executed: all required/source hashes; exact fixture subprocess and byte comparison; environment inventory; all named V6 attacks; Stage-C and BS-7f fixture-kind probes; arbitrary-SealedMask construction; self-asserted production-guard and calibration-order instrumentation; lazy/truncated brick-table closure; duplicate-manifest and RA-wrap planner probes; `build_plan` Stage-P/oracle bypass; feasible HC allocation witness; HC population-weight and tie probes; branch resolver/invariance probes; empty/unknown receipt probes; lapsed-battery source inspection; measured-null critical-value recomputation; exact binomial/Clopper–Pearson calculations; exhaustive permutation checks; independent axis conversion; byte-substring cut checks; and AST checks for BLAS/spawn/binomial/random-call claims.

No `/Users/duhokim/NebulaMindData/` path was read. No real survey product, object row, image, chi value or sky statistic was fetched or computed. No source artifact, git state, process, authorization, freeze, publication or runtime was mutated. Temporary probe files were confined to `/tmp` and removed. GPT56's only write in this directory is this report.

## Sources

[1] https://arxiv.org/abs/1104.2815 — Longo 2011 arXiv abstract and related DOI

[2] https://api.crossref.org/works/10.1016/j.physletb.2011.04.008 — Crossref journal metadata

[3] https://ui.adsabs.harvard.edu/abs/2011PhLB..699..224L/abstract — ADS record locator (human-verification wall during this gate)

**REFUSED**
