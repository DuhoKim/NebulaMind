# CODEX adversarial gate — successor preregistration V7

## Verdict

**REFUSED.** The three custody pins match and the pinned fixture transcript reproduces byte-for-byte, but multiple round-6 attacks still succeed. Most directly: BS-2m still accepts a short manifest when the caller supplies a shortened parent digest, a shortened brick universe, or a zero cutout half-size; Stage C still accepts `FixtureMask`; the production-named planner can skip both power runs; the Sep-5 resolver ignores the date and its invariance check can pass vacuously; the HC-1H producer still has no 3×9 stratum/population-weight contract and its allocator rejects a feasible fixed-budget table; canonical slot receipts cannot be consumed by the production runner; the validation battery is still missing the floor-edge case; and the one-measured-null power method can turn the same 1,000 skies from FAIL into PASS. V7 is not freeze-candidate grade.

## Custody pins — computed before review

`shasum -a 256` produced:

- `../PREREG_SUCCESSOR_DRAFT_V7_20260825.md` = `f15b0b4dad9d5c565969e18aa8dee200cc8a80c9b7f817e68c8b3e239f800286`
- `../ref/successor_ref_v3.py` = `b89c21288935a026f882d2f417c68d82e12934beae1b00e72474186f03d74e90`
- `../ref/FIXTURES_V3_20260825.out` = `445e32c8c573423729a196cfd35f70faf26dc5073ca3295d89219c756142b33a`

All three equal the brief's required pins. Review proceeded.

Binding-source pins independently recomputed:

- `../../SUCCESSOR_SCOPE_20260821.md` = `995b2e729a3362f0445cac9d5da6d290fddac9f8018e75f2c0aa87c190c93de7`
- `../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` = `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- `../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md` = `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`
- `../../VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md` = `43b9a6a843ef08a6528f1132db2bee29000c5ecd3def2a3a03c23f672c81cec7`
- `../../LANA_BS5_LONGO_SIGN_20260814.md` = `b7c32dcf12d9e147e5dee6a8262d925b61011615f2ee1d75d687600abb0a72ca`

## Environment and fixture reproduction

- executable: `/Library/Developer/CommandLineTools/usr/bin/python3`
- CPython 3.9.6
- NumPy 1.26.4
- macOS 26.6.2, arm64, little-endian
- command: `python3 -B ../ref/successor_ref_v3.py --fixtures`
- exit 0; stderr 0 bytes
- stdout 3,359 bytes
- stdout SHA-256 `445e32c8c573423729a196cfd35f70faf26dc5073ca3295d89219c756142b33a`
- byte-equal to `FIXTURES_V3_20260825.out`

## Numbered findings

### 1. BLOCKER — BS-2m moved the caller-trust hole; it did not close it

**Quote / symbol.** V7 §2.4 says `close_manifest()` “derives every object's required bricks itself,” has “no argument through which a caller can hand it an answer,” and prevents an omitted object because its digest changes (V7 lines 117–130). The function actually accepts three answer-defining inputs from the caller: `expected_parent_digest`, `brick_table`, and `halfsize_deg` (`successor_ref_v3.py:223-265`). No BS-2s output binds the selected parent-object digest; no release-brick-universe digest is an input or receipt field; and `halfsize_deg` is freely overridden.

**Executed attacks.** All three lazy paths passed:

1. Starting from a two-object parent, I omitted one object, recomputed `parent_digest()` on the shortened table, and called `close_manifest()` with that matching shortened digest. It returned cleanly with `objects=1`, `required_count=1`, `manifest_count=1`.
2. For an object whose honest two-brick table requires `['east','home']`, I supplied a brick table containing only `home`; `close_manifest(..., ['home'])` passed with no missing or extra brick.
3. On the same honest two-brick table, I supplied `halfsize_deg=0.0`; the one-brick manifest passed. Thus the home-only V6 attack still succeeds through an exposed planner-configuration seam.

The planner constant also contradicts its own stated geometry: `128 × 0.262 / 2 / 3600 = 0.004657777777777778°`, while `CUTOUT_HALFSIZE_DEG=0.0186`, a factor `3.9933` larger. `planner_digest()` hashes only `plan_object_bricks.__code__.co_code` plus the supplied half-size; it omits `co_consts` and helper `_ra_sep` bytecode, so it is not the claimed digest of the planner's effective code bytes.

**Why it blocks.** The named 60,308-versus-60,310 defect is prevented only if the caller truthfully supplies the complete selected parent, complete release brick universe, and frozen geometry. Those are exactly the upstream facts BS-2m must establish, not assume. The negative fixture retains the full-parent digest while dropping a row, so it tests an inconsistent attacker and misses the compliant lazy one that regenerates all downstream digests from the shortened parent.

**Minimal repair.** Make one production closure runner consume the BS-2s parent artifact and digest directly, with exact object-key equality to the selected catalog result; consume a separately pinned complete release-brick-universe artifact and digest; remove the half-size override from production; correct and gate the 128-pixel geometry against the actual cutout/WCS contract; hash the complete transitive planner source/configuration; reject duplicate manifest entries; and replay omitted-parent, shortened-universe, zero/small-halfsize, wraparound-RA, and the two historical edge-object cases.

### 2. BLOCKER — Stage C still accepts fixture inputs, and its receipt cannot bind the mask later required by production

**Quote / symbol.** V7 §3 says production entry points call `require_sealed()`; §4 says Stage C runs on the sealed accepted-position mask before unblinding; §5 calls the runner the only production verdict path (V7 lines 164–172, 201–217). But `stage_power()` calls `require_any_mask()`, not `require_sealed()`, regardless of `stage` (`successor_ref_v3.py:640-651`). `perm_record()` likewise accepts any `_BaseMask` even for `STAGE_REAL` (`562-577`). There is no integrated Stage-C production runner.

**Executed attacks.** A `FixtureMask` passed `stage_power(fx, 0.9, STAGE_C, 1, n_trials=1)` and returned `(0, None)`. The same fixture passed `perm_record(fx, STAGE_REAL, ..., n_perm=3)` and returned p=0.75. This is the CODEX-V6 fixture-to-production attack, still executable; `MASK-REFUSALS` tests `require_sealed(fx)` directly rather than either exposed stage function.

There is also an unsatisfiable digest chronology. A legitimate pre-unblinding unsigned `SealedMask` had digest `81ac926f…`; adding the real sign vector with `.with_signs()` changed it to `2ff8c64f…` because signs are digest-bound. `run_production_verdict()` requires signs and compares the BS-5f receipt's `mask_digest` to the signed digest (`926-950`). Therefore a Stage-C receipt made before unblinding cannot match the signed mask required later; making it match requires Stage C to know the signs it is supposed to precede.

**Why it blocks.** A fixture geometry can still produce the class-E power result, while the honest unsigned Stage-C artifact cannot be consumed after signs are attached. This breaks both admissibility and chronology.

**Minimal repair.** Add a no-override `run_stage_c()` that requires an unsigned `SealedMask`, a typed BS-8f receipt, exactly 1,000 trials, and the fixed addresses. Split an immutable accepted-position/geometry digest from a signed-record digest; bind BS-5f to the former and BS-7f to both. Make `stage_power(STAGE_C, ...)` and `perm_record(STAGE_REAL, ...)` private or enforce operation-specific types and fixed counts.

### 3. BLOCKER — the production path is still bypassable, and calibration can halt only after the real statistic is formed

**Quote / symbol.** V7 says both gates' monkeypatched-guard attacks are closed by `PROD-NO-SEAMS`, `PROD-CALLS-GUARDS`, and `PROD-REFUSES` (V7 lines 209–217), and says calibration failure halts pre-unblinding so “no real-sky statistic is ever formed” (lines 201–205, 259–261).

**Executed attacks.** On a signed 120,000-row `SealedMask` with `N_eq=117,613.96`, I monkeypatched `require_environment`, `require_authorization`, `require_complete_sample`, and `require_sealed` to record-and-return, and monkeypatched `perm_record` to return a fabricated `(beta, vector, p, sigma)`. `run_production_verdict()` called all five patched names and returned `REPRODUCED-LONGO`. The fixture checks only that mutable global names occur in `co_names`; it does not prove their implementations or outputs are authentic.

Separately, I supplied calibration with `min(a_lb_b)=0.576034`. The runner called `perm_record` first, forming the marked `REAL_STAT_FORMED`, and only then `_decide_from()` raised `InconclusiveByCalibration`. This order is explicit at code lines 946–950. The runner neither emits nor locks `INCONCLUSIVE-BY-CALIBRATION`.

**Why it blocks.** The brief explicitly required the monkeypatched guards to be retried; they still yield a verdict. More fundamentally, the calibration condition that must stop the run before unblinding is not checked until after the full real-sky permutation statistic exists.

**Minimal repair.** Use a hash-verified standalone production entry point rather than mutable imported globals; verify its own source/environment and typed receipt envelopes before reading signs. Validate/adjudicate the BS-8f calibration receipt and Stage-C receipt before accepting a signed record or calling `perm_record`. Emit a receipted calibration-halt outcome without a real statistic. Add executed fixtures that replace every guard/record symbol and require refusal, and an order fixture asserting zero calls to the statistic producer on calibration failure.

### 4. BLOCKER — `build_plan()` exposes a production-named route that skips both Stage-P runs and the count-oracle proofs

**Quote / symbol.** V7 §2.3 says `build_plan()` performs BS-2c → BS-2o → BS-5p → BS-2s in one frozen call and that BS-2s includes a mandatory Stage-P re-pass (V7 lines 87–108, 293–297). The code exposes `l_plan_override`, `n_trials`, and optional universe/grouped-total inputs (`successor_ref_v3.py:665-704`). If `l_plan_override` is supplied, both the prefix power search and final re-pass are skipped.

**Executed attack.** `build_plan([1,2],[-1,1],[100,100], l_plan_override=100.0, n_trials=1)` returned a selected set with `l_min_plan=None` and `repass=None`. It also accepted omitted `universe_brickid`, `grouped_sum`, and `ungrouped_total`, so the asserted universe closure and grouped/ungrouped agreement were not required.

**Why it blocks.** The V6 `_perm` seam was removed from one runner but the same class of override remains in the normative planning orchestrator. A lazy BS-2s producer can choose the threshold, omit count-oracle proof inputs, skip both stochastic gates, and still invoke the exact code symbol named by §7.

**Minimal repair.** Split test/exploration helpers from a production `build_plan` with no threshold/trial override and mandatory typed BS-2c input receipt. Require universe, raw grouped keys, independent total proof, branch/product digests, 1,000 trials, x≥962, and the final-set re-pass. Return a typed BS-2s receipt only from that path.

### 5. BLOCKER — HC-1H remains underimplemented; its allocator rejects a feasible frozen-budget input and its tie rule still contradicts its body

**Quote / symbol.** V7 says `accuracy_from_handcheck()` implements the inherited HC-1H estimator and that the 3×9 allocation is proportional/largest-remainder with both floors and one stated-and-implemented tie rule (V7 lines 246–263). V3-pred instead defines nine inherited HC strata, Neyman allocation, per-stratum correction, and population-weighted `a = Σ w_s a_s` (`V3-pred:279-303`).

**Executed attacks and code evidence.** `accuracy_from_handcheck()` accepts only agreement/count arrays plus epsilon parameters; it accepts three already-pooled values and has no stratum population weights. It also accepted arrays of length 27 and returned a 27-vector and 27×27 covariance, although downstream profile code assumes three calibration bins. The numeric epsilon correction itself is repaired, but the quoted 3×9 → nine-stratum population-weighted producer is still absent.

For allocation, I supplied a 3×9 integer capacity table with total capacity exactly 500, every cell non-empty, minimum 10, and maximum 37. Because budget=capacity, allocation of every available object is trivially feasible and meets all cell/stratum floors. `allocate_handcheck(...,500)` raised `allocation exceeds available objects in a cell`: after assigning floors it apportions the remainder against original counts rather than residual capacities (`735-778`). The public `budget` override also remains.

Finally, the docstring says `side='left'` sends equality to the higher bin (`716-720`), but `assign_bins([0,1],[0,1])` returned `[0,1]`; equality to the first boundary went to bin 0, the lower bin. The all-tied refusal fixture does not exercise this nondegenerate tie.

**Why it blocks.** The calibration point estimates, covariance, scalar/profile/halt branch, Stage-C accuracies, attenuation, decision band, and floor can all change. This is still not the inherited estimator or a reliable frozen allocator.

**Minimal repair.** Implement a typed 3×9 realized-cell producer with nine stratum populations and weights, fixed 500-real-label budget, the inherited Neyman rule, epsilon diagnostics/integrity triggers, per-stratum correction, population aggregation into exactly three calibration-bin values, and full covariance. Allocate only over residual capacity after floors. Remove production budget choice. State one actual boundary rule and test repeated values at each nondegenerate boundary.

### 6. BLOCKER — the Sep-5 branch choice remains a caller assertion and the “invariance” comparator proves the wrong thing

**Quote / symbol.** V7 §2.1 says Branch B is selected on Sep 5 if DR11 photo-z is still absent and that downstream artifacts use the same code path while only recorded paths/versions differ (V7 lines 59–76). `resolve_branch(photoz_available, resolution_date)` simply selects A for true and B for false; it does not parse or enforce the date or perform an availability probe (`successor_ref_v3.py:993-1003`).

**Executed attacks.** `resolve_branch(False,'2026-08-25')` selected `B_DR10_1` eleven days early. `resolve_branch(False,'not-a-date')` also selected B. `branch_invariance(lambda cfg: {'constant':1})` returned `invariant=True`, reproducing the fixture's vacuous strategy: the fixture function ignores the configuration. Conversely, any artifact that truthfully records the allowed branch-specific input paths will hash differently, while `branch_invariance()` defines equality of whole output digests as the only pass (`1006-1014`).

**Why it blocks.** The choice can be made on any date from an unverified Boolean, and the advertised check rewards ignoring the selected branch rather than proving identical code/structure with enumerated configuration differences. This is not a bound choice-point.

**Minimal repair.** Freeze a fail-closed availability probe and timestamp/error policy; reject absent DR11 before Sep 5 as unresolved rather than choosing B; type and digest the raw probe evidence; generate BS-1/BS-1b from the resolved config; and compare normalized traces/code/schema digests after removing only an explicitly enumerated set of branch-path/version fields. Test early absence, malformed dates, transient errors, and a function that ignores configuration.

### 7. BLOCKER — one 20,000-permutation measured null per prefix can change the x=962 decision; 1% deflation does not make the contract conservative

**Quote / symbol.** V7 §4 claims one standardized null per prefix can judge all 1,000 trials, that `PWR_CONSERVATISM=1.01` absorbs residual multiset dependence, and that `PWR-CONTRACT` establishes decision-metric conservatism (V7 lines 174–199; code `580-651`, `1114-1165`).

**Executed decision-boundary attack.** On the pinned `polar-1000` geometry, ten independent 20,000-permutation null calibrations made from realistically near-balanced `inject_signs(...,a=.85)` multisets produced the operative 20th-largest standardized thresholds

`3.0759, 3.1474, 3.2301, 3.1901, 3.1410, 3.1269, 3.0883, 3.0709, 3.1474, 3.0779`

(range 0.1592; sample sd 0.05295). Judging the same fixed 1,000 injected skies at a boundary-tuned stress amplitude 0.194 after the 1% deflation produced between 947 and 966 successes; four calibrations PASSed x≥962 and six FAILed. More sharply, at amplitude 0.1925 the 20k calibration with q=3.0709 gave exactly 962 (PASS), while an independent 300,000-permutation calibration gave q=3.090065 and 958 (FAIL). The stress amplitude is deliberately chosen to place this fixture geometry at the gate boundary; the equality contract is supposed to protect the decision metric there, not only strong signals far from it.

The fixture does not test that. It uses only eight trials per geometry and injects amplitude 0.14 (`successor_ref_v3.py:1131-1145`), retaining only 22 strong successes total. It never compares a 1,000-trial x=962 verdict. `PWR-Z-STABLE` itself reports 35% relative tail-mass spread yet accepts anything below 50%. Around z=3.0902, a 1% z deflation reduces a normal tail by only 9.92%, not 35%, and neither quantity is a confidence bound for the empirical-null order statistic.

**Why it blocks.** A Stage-P PASS can still overstate the result obtained from a substantially better measured null, exactly at the preregistered 962/1000 boundary. Clopper–Pearson bounds (0.949366 at 961; 0.950487 at 962) condition on a fixed trial success definition; they do not account for the shared random calibration threshold estimated once and reused across all trials.

**Minimal repair.** Either run an independently calibrated/full permutation test per addressed trial, or establish a simultaneous upper confidence bound on the null tail/critical threshold that covers calibration Monte Carlo error and admissible sign-multiset variation. Define PASS using that worst-case threshold and demonstrate the 1,000-trial verdict at the actual prefix/final geometries with an error budget that cannot move x across 962. Do not infer a 35% tail-mass guarantee from a 1% z rescaling.

### 8. BLOCKER — the lapsed-spec validation battery is still materially weakened, and V7 dropped fixtures it says are present

**Quote / symbol.** V7 says the lapsed build-spec battery is restored “at its named boundaries” and §10 says “the battery is weakened” is repaired (V7 lines 229–239, 367). The build spec requires a just-below-evaluated-floor case and an integrated power refusal (`VERDICT_ESTIMATOR_BUILD_SPEC:66-77`). V7/code contain no below-floor or floor-edge fixture.

`BATTERY-NEQ` only computes `n_eq_small < NEQ_MIN`; it never calls `run_production_verdict()` or asserts an `INCONCLUSIVE-BY-POWER` outcome (`successor_ref_v3.py:1291-1296`). `BATTERY-POS` calls `explore_verdict()` with a normal-tail p-value rather than the full production permutation/guard path (`1265-1290`). Thus the fixture prose “the runner derives” is unsupported by its body.

V7 §2.3 also says all five historical selector counterexamples “are fixtures and pass” (lines 104–107). They existed as `SEL-A` through `SEL-E` in ref v2, but no `SEL-*` fixture or output exists in ref v3; searches found only the 17/16 raw-boundary fixture and `RAW-RET`.

**Why it blocks.** The same V6 battery attack still succeeds: the required floor boundary is absent, the power fixture is arithmetic rather than an executed refusal, and the positive integration test bypasses production. V7 additionally claims coverage that its fixture transcript no longer contains.

**Minimal repair.** Restore and execute the just-below-floor case, an N_eq-derived refusal through the actual production runner before `perm_record`, and a positive target through a fixed-count full-permutation integration path. Restore all five named selector counterexamples to V3 fixtures and pinned output. Assertions must test the specified outcome/prohibition, not merely an inequality or exploration helper.

### 9. BLOCKER — the slot “schemas” are field-name lists that cannot carry their own values into production; eight slots remain unschematized

**Quote / symbol.** V7 §7 retains the same table columns as V6 — `slot | producer | content | code symbol | blocks` — despite its heading promising inputs and schemas/digests (V7 lines 285–313). Section 10 claims the missing-schema finding is repaired by `SLOT_SCHEMA` and `receipt()` (lines 368–369).

**Executed attacks and code evidence.** `SLOT_SCHEMA` omits BS-1, BS-1b, BS-3, BS-9, BS-4, BS-7p, BS-8p, and BS-6. `receipt('BS-1', {'anything': b'ok'})` passed. For a known slot, field names alone suffice: a BS-2c receipt with every required field equal to empty bytes passed and emitted a digest. No type, shape, canonical decoding, predecessor digest, or cross-slot constraint is enforced.

More fundamentally, `receipt()` returns only `slot`, `schema`, `environment`, `body_sha256`, and `envelope_sha256`; it discards all field values. A canonical BS-5f receipt therefore has no top-level `passed` or `mask_digest`, while `run_production_verdict()` requires exactly those ad hoc top-level keys. The canonical producer and consumer are incompatible. BS-2m's schema also omits the prose-promised missing/extra brickname lists.

**Why it blocks.** This is not the machine-checkable slot contract §10 claims. A slot can hash empty assertions, several slots accept arbitrary fields, and the one production consumer cannot consume the canonical receipt type. This finding does not count the three items §10 openly leaves unfinished (clean-room spec, BS-9 input schema, BS-V lock); seven other missing schemas and the generic producer/consumer break are additional.

**Minimal repair.** Define a typed, versioned schema for every slot with exact field encodings/shapes, predecessor/input digests, code/spec hash, failure outcome, and cross-slot bindings. Preserve canonical field values in a verifiable envelope or provide a verified decoder. Make every consumer accept only decoded canonical receipts. Add round-trip producer→serialize→decode→consumer fixtures and refuse empty payloads. Add the missing schema/input columns to §7.

### 10. MAJOR — the count oracle still cannot prove a dropped nonzero group was a true zero

**Quote / symbol.** V7 §2.3 claims independently enumerated universe closure, zero materialization, and grouped/ungrouped agreement (lines 89–95). `validate_count_table()` receives only the final materialized table plus two optional scalar totals (`successor_ref_v3.py:280-318`). It receives no raw grouped key set, raw grouped records/digest, query scope, or independently partitioned total evidence; and all proof inputs are optional in `build_plan()`.

**Why it matters.** A nonzero grouped row can still be dropped, materialized as zero, and accepted if grouped and ungrouped totals were both produced under the same accidental footprint restriction. Final key equality is then true by construction. V7 fixed negative/float/duplicate/length inputs, but not the completeness half of the CODEX-V6 finding.

**Minimal repair.** Make the raw grouped key/count artifact and query digest explicit; require raw keys to be a unique subset of the independently pinned universe; derive zero rows inside the validator; require a total produced by a demonstrably independent partition/query scope; and make all artifacts mandatory in production `build_plan()`. Add a dropped-nonzero-group fixture.

### 11. MAJOR — §8's inherited-defect list is incomplete even where the code presently carries the repair

The amended successor scope names “Project the monopole out” and “Fix the sidedness seam” as design requirements (`SUCCESSOR_SCOPE:46-56`). Neither monopole leakage nor the one-sided/two-sided harness seam appears in V7 §8's eight-item inherited-defect list. The centred `beta_slope()` and one-sided comparisons presently address them, so this omission is not by itself a separate code blocker; it is a failure of §8's promised complete named inventory and makes later regression easier.

**Minimal repair.** Add both known predecessor defects to §8 with their exact code/fixture closure evidence, without claiming the currently open mechanisms above are closed.

## Complete slot walk

### Class P

- **BS-1:** chronology is stated, but resolver/date/probe and comparator are blocked by Finding 6; no slot schema.
- **BS-1b:** branch config literals exist, but no canonical slot schema/producer or availability-derived binding. BS-9's release-specific input schema remains openly unfinished and is not counted as a new finding.
- **BS-2c:** strict integer/key checks improved; raw-group completeness, mandatory universe/total proofs, typed receipt, and query custody remain open (Findings 4, 9, 10).
- **BS-2o:** ledger symbol exists and uses positive raw counts; receipt has names but no typed values/round trip (Finding 9).
- **BS-5p:** power symbol exists, but one-null equality and production overrides block it (Findings 4, 7).
- **BS-2s:** raw-positive 17/16 dispatch is repaired and normal-path re-pass code exists; public override skips the entire power chain, and five claimed selector fixtures were dropped (Findings 4, 8).
- **BS-2m:** blocked by unbound parent/universe/configuration and planner geometry (Finding 1).
- **BS-3:** inherited weights/tau text is available pre-image; no exact schema or code producer.
- **BS-9:** V7 correctly preserves R1–R5 rerun and `nm_acquire_cutouts.py` prohibition. Its unfinished schema is acknowledged by §10 and not counted anew.
- **BS-4:** sign direction and synthetic requirement are sound, but `inject_signs`/`decide` are not the pixel-level absolute-sign anchor producer; no slot schema.
- **BS-7p:** environment and fixture transcript exist, but battery fidelity is blocked by Finding 8 and no slot schema exists.
- **BS-8p:** blocked by the allocator, HC-1H producer mismatch, and missing schema (Finding 5).

No class-P slot inherently requires post-freeze real χ, but several cannot emit the promised pre-freeze evidence.

### Class E

- **BS-6:** transport chronology is coherent; no schema/code producer.
- **BS-2f:** sealed type and bin recomputation improved, but unsigned/signed digest identity is not separated (Finding 2).
- **BS-8f:** numeric epsilon correction improved, but the 3×9 stratum/population producer and typed receipt remain absent (Findings 5, 9).
- **BS-5f:** no sealed-only fixed-parameter Stage-C runner exists; fixture masks pass and canonical receipts cannot be consumed (Findings 2, 9).
- **BS-7f:** the integrated runner hard-codes 100,000 permutations on its honest path, but canonical BS-7f receipt production/consumption is absent and calibration is checked too late (Findings 3, 9).
- **BS-V:** pure decision code exists. The primary lock is openly unfinished in §10 and is not counted as a new finding; calibration-halt ordering is an additional blocker (Finding 3).

## Inherited-defect closure (§8)

1. **Manifest-versus-parent gap — OPEN.** Short parent/universe/configuration inputs pass (Finding 1).
2. **Footprint-blind power — OPEN as an admissibility/equality contract.** Stage C accepts fixtures and the measured-null gate is unstable at x=962 (Findings 2, 7).
3. **Full-sky normalization constant — CLOSED for the named defect.** `beta_slope()` is centred; no `3·D` decision path found.
4. **Attenuation-versus-target mismatch — OPEN at the producer.** β/Â separation exists, but the inherited 3×9 population-weighted HC-1H producer does not (Finding 5).
5. **Unreachable significance threshold — PARTLY CLOSED, still blocked.** The honest runner hard-codes 100,000; monkeypatch and validation paths bypass/replace it (Findings 3, 8).
6. **Silent axis divergence — CLOSED for this reference.** One pinned unit vector is used; citation/sign/axis checks held.
7. **Count stopping on ordered brick IDs — PARTLY CLOSED.** Contiguous selection is absent and 17/16 dispatch is repaired; count proof and power overrides remain (Findings 4, 10).
8. **Verdict by human reading — PARTLY CLOSED.** A decision helper/runner exists, but canonical receipts do not connect, calibration is checked after statistic formation, and the lock is openly absent (Findings 3, 9).

Known omitted inherited items: monopole leakage and sidedness seam (Finding 11).

## Quotation/source fidelity and attacks that held

1. The arXiv record independently confirms Michael J. Longo, the title, 15,158 spirals, published amplitude `−0.0408±0.011`, approximate Galactic axis `(52°,68.5°)`, arXiv:1104.2815, and DOI `10.1016/j.physletb.2011.04.008`.[1] Crossref independently confirms the DOI, author, journal, volume 699, and pages 224–229.[2] The ADS URL is the exact bibcode `2011PhLB..699..224L`, although its page presented a human-verification wall in this run.[3]
2. Sign mapping is internally consistent and source-grounded: Longo's native `(R−L)/(R+L)` value is negative; the project defines positive χ as Longo-Left/CCW East-of-North, hence the same effect is `+0.0408`. V7 and code keep `A_LONGO_PUBLISHED_SIGNED=-0.0408` and `A_LONGO=+0.0408`. No inversion found.
3. All eight §2.2 predicates occur in V7 and BS6-pred with matching operator/numeric content; the ellipticity expression is byte-identical. The no-surface-brightness-cut disclosure is preserved.
4. V3-pred's 100,000 permutations, strict p thresholds, 3.09 floor multiplier, 0.85 lower-bound floor, and 85.72% retention survive in substance. The build-spec battery fidelity does not (Finding 8).
5. Scope Amendment 1's no-global-optimality discipline is preserved in prose; exact mode is the algorithm for ≤16 raw-positive candidates.
6. Independent exact enumeration reconfirmed the permutation-variance formula. CP_PASS_X=962 is correct: one-sided 95% Clopper–Pearson lower bounds are 0.9493659932 at x=961 and 0.9504871297 at x=962.
7. Static AST checks found zero matrix-multiply nodes, zero `.spawn`, zero `.binomial`, and exactly two `rng.random()` calls in `inject_signs()`. Those body claims held.
8. The draft repeatedly limits authority to writing. It does not authorize or assume a real run, fetch, freeze, publication, or disclosure.

## Testimony

- V7 explicitly labels `Cov(β̂,â)=0` and the profile analogue as Testimony. I did not accept them as proved or use them to rescue any finding.
- The drafting-time DR11-page/photo-z status was not independently re-fetched; it is not a verdict premise.
- I did not read `/Users/duhokim/NebulaMindData/` and do not independently certify the historical 60,308/60,310 object facts. Finding 1 is established by executed miniature attacks on the pinned code.
- The power-boundary stress amplitude was selected to place the pinned polar fixture near x=962; it is an algorithmic contract test, not a claim about the future realized prefix.
- ADS metadata content was blocked by human verification; the exact bibcode is supported here by the record URL plus the independently matching Crossref bibliographic fields, not by a successfully extracted ADS abstract.

## Evidence ledger and custody boundary

Read: the V7 brief; the three pinned V7 artifacts; both V6 gate reports; amended scope; V3-pred; BS6-pred; lapsed build spec; and the Longo sign receipt. External source checks used the arXiv API record, Crossref, and the ADS record URL.

Executed: required/source hashes; exact fixture reproduction; all CODEX-V6 attack classes requested by round 6; shortened-parent/universe/halfsize closure attacks; fixture Stage-C/real-stage calls; unsigned/signed digest comparison; planning override; allocation/tie/HC-shape attacks; early/malformed branch dates and vacuous invariance; monkeypatched guards/permutation record; calibration-halt call order; receipt round-trip/empty-field attacks; selector-fixture inventory; AST randomness/BLAS checks; cut-string/source checks; Clopper–Pearson recomputation; ten independent 20k power-null calibrations; fixed-1,000-sky decision comparisons; and an independent 300k-null comparison.

No source artifact was edited. No run, study-data fetch, authorization, git mutation, publication, freeze, or execution approval occurred. The only gate-directory write by this CODEX review is this report.

## Sources

[1] https://export.arxiv.org/api/query?id_list=1104.2815 — arXiv record 1104.2815
[2] https://api.crossref.org/works/10.1016/j.physletb.2011.04.008 — Crossref DOI record
[3] https://ui.adsabs.harvard.edu/abs/2011PhLB..699..224L/abstract — NASA ADS bibcode record

**REFUSED**
