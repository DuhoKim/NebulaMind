# GPT56 ADVERSARIAL GATE — successor preregistration draft V4

## Custody pin

The first review command was:

`shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V4_20260824.md`

Computed:

`1ea8bb8d8e236049b2e73091770f3a7f58dbee5a3b8385ba3f30cb11fd31adcb  ../PREREG_SUCCESSOR_DRAFT_V4_20260824.md`

This equals the brief's required pin. Review proceeded on those bytes.

## Numbered findings

### 1. BLOCKER — class-P BS-7 requires the real-sky result before the preregistration can exist

**Quote.** The preamble says the draft becomes a preregistration only when every class-P slot holds (lines 3–6). The class-P table then requires BS-7 to contain `β̂_obs` and the SHA-256 of the real 100,000-value `β̂_perm` payload (lines 210–223). Stage C, however, is a class-E gate that must pass before unblinding and before any real-sky statistic is formed (lines 157–162).

**Why this fails.** `β̂_obs` and permutations of the observed signs cannot exist pre-freeze: they require the real `χ` signs and belong after BS-5f and unblinding. The draft therefore has the cycle/temporal contradiction

`preregistration exists → every class-P slot filled → real β̂_obs already exists → Stage C and unblinding already occurred → preregistration had to exist to govern them`.

This is not a receipt-detail issue. Filling BS-7 as written would either compute the decision statistic before its preregistration exists or leave the draft permanently unable to become a preregistration.

**Minimal repair.** Split BS-7 into a class-P `BS-7p` containing only the frozen RNG/API/serialization declaration and synthetic expected-digest fixtures, and a class-E result receipt after BS-5f/unblinding containing `β̂_obs`, the real permutation payload digest, p, and environment. State the exact class-E order through primary lock.

### 2. BLOCKER — the local pass does not minimize brick count or provide the claimed small-case optimality

**Quote.** BS-2s says the pass “minimizes brick count subject to `L ≥ L_plan`,” permits swaps only when they then enable a removal, and claims certified small-case optimality (lines 79–95). It also requires oracle verification on the three published counterexamples but lists only `c` and `n`, not a fixture `L_plan` (lines 87–91).

**Why this fails.** An exact seven-brick fixture defeats the stated removal plus one-swap-then-removal neighborhood:

- `c = [0.552, 0.094, -0.676, -0.683, -0.836, 0.173, -0.073]`
- `n = [3, 14, 5, 17, 6, 8, 20]`
- `L_plan = 4.147539428571428`
- V4 greedy order: `[4, 0, 5, 3, 1, 2, 6]`
- cut set `S0 = {4,0,5}`, `L = 5.117239058823530`
- removing 0, 4, or 5 gives respectively `3.4905634285714284`, `0.31339854545454543`, and `3.853088`, all below threshold
- the best result after **any** accepted↔unaccepted swap followed by one removal is `3.98608384`, also below threshold
- but the two-brick subset `{1,3}` has `L = 4.635080709677419 ≥ L_plan`.

The frozen move set must stop at three bricks although two suffice. The executed exhaustive check was:

```text
T 4.147539428571428 order [4, 0, 5, 3, 1, 2, 6] S0 [0, 4, 5] L0 5.117239058823529
direct_removals [(0, 3.490563428571428), (4, 0.3133985454545455), (5, 3.8530879999999996)]
best_swap_then_remove (3.98608384, 4, 3, 0, 6.460212678571429)
feasible_pairs [(4.63508070967742, (1, 3))]
```

Thus “minimizes” is a false global optimization claim despite Amendment 1's no-global-optimality discipline. If “every fixture with ≤12 bricks” means every fixture in a selected test file rather than all such inputs, passing that file is test coverage, not certified small-case optimality. In addition, the three named gate fixtures are not executable fixtures without exact `L_plan` values. The swap clause does not freeze pair scan order or the exact look-ahead operation, and the 10,000-move cap has no fail-closed outcome if reached before local exhaustion.

**Minimal repair.** Replace “minimizes” with the exact weaker claim actually provided; specify operation-level pseudocode, pair ordering, look-ahead, and cap failure. Freeze `L_plan` in every fixture. If universal optimality is claimed for `m ≤ 12`, make exhaustive enumeration part of the algorithm for every such input and add this fixture. Otherwise call the oracle battery finite test evidence, not a certificate of optimality.

### 3. BLOCKER — calibration bins are assigned before their input exists, and fallback uncertainty is not frozen

**Quote.** Section 6 says the three `c` bins are “fixed at BS-2s as the accepted mask's count-weighted c-tertile boundaries” (lines 185–194). BS-2s is class P, operates on the count table and selected bricks, and precedes catalog-row acquisition (lines 79–100, 210–223). The actual accepted-position mask first appears as class-E BS-2f after inference (lines 225–232). The fallback uncertainty is described only as “the frozen per-bin delta-method gradient over {â_b}” (lines 129–133), but no gradient, covariance matrix, or vector covariance assumption is actually stated; BS-8f emits only marginal `σ_ab` values.

**Why this fails.** The classifier-accepted mask does not exist at BS-2s, so its tertile boundaries cannot be fixed there. Eligible counts or selected brick centres are not the actual accepted-position mask, and silently substituting either changes the calibration estimand.

The fallback point estimator itself is algebraically sound for piecewise-constant accuracy:

`ŵ = Cov(c,q(c)c)/Var(c)` implies `E[β̂]=A_L ŵ`.

An executed example with `c=[-1,.2,1]`, weights `[1,1,4]`, and `a=[.95,.95,.80]` gave `ŵ=.732`, `β=.0298656`, and exact profile recovery `β/ŵ=.0408`; the scalar correction instead gave `.04266514285714285`.

But its uncertainty is not executable. With object weights, if

`g_b = ∂ŵ/∂a_b = 2 Σ_{i∈b}(c_i-c̄)c_i / Σ_i(c_i-c̄)^2`,

then the attenuation contribution is proportional to `gᵀ Cov(â_b) g`. The cited predecessor's HC-4 explicitly uses a shared synthetic-error estimate, so bin estimates are generally correlated. On the executed example, equal marginal `σ_ab=.02` gave an attenuation variance term `2.612603493684495e-06` under zero correlation and `3.791655146466006e-06` at common correlation 0.5. Both have the same reported marginal sigmas. V4 declares only `Cov(β̂, â)=0` for the scalar path, not `Cov(β̂,{â_b})=0`, and cannot derive the fallback decision band or floor from BS-8f's fields.

**Minimal repair.** Freeze the bin-construction algorithm pre-run but compute and seal actual boundaries at BS-2f, before hand-check allocation, rather than claiming they exist at BS-2s. State the exact fallback gradient, full covariance matrix producer (including the shared-ε contribution), covariance with `β̂`, and separate point-estimate versus conservative-floor evaluations. Add those fields to BS-8f and fixtures that recompute both decision quantities.

### 4. BLOCKER — Stage P/C randomness remains non-reproducible despite the seed-spawn prose

**Quote.** Stage P says “draw `B ~ Bernoulli`,” then draw `U`, with all draws from `children[t]` (lines 143–151). It freezes `rng.permutation` for the real-data permutation stream (lines 112–118) but never freezes the injection generator constructor or Bernoulli API. Stage C says to use the same contract on a mask containing positions and flags only (lines 157–161; BS-2f lines 229–231), while the only stated object order is ascending BRICKID then within-brick index in Stage P.

**Why this fails.** `Generator.binomial(1,p)` and `Generator.random()<p` are both ordinary NumPy implementations of the stated Bernoulli draw but consume the stream differently. From the exact V4 seed child on 1,000 frozen probabilities, the executed comparison found 493 differing latent labels:

```text
bernoulli_api_differences 493
first10_binomial [0, 1, 1, 0, 1, 1, 1, 0, 1, 1]
first10_uniform  [1, 0, 0, 1, 0, 0, 0, 1, 0, 0]
```

`SeedSequence.spawn` is stateful. Two successive calls to `children[1].spawn(1)` yielded spawn keys `(1,0)` and `(1,1)`. V4 does not say whether the root/children are reconstructed for each prefix or reused while searching for the first passing prefix.

Stage C's allowed mask omits BRICKID and within-brick indices and provides no replacement canonical row ordering. Running the same physical 1,000-position mask in forward and reverse row order with the same stated seed produced trial slopes `0.07177222777222779` and `-0.04087912087912087`, with 522 labels assigned differently after mapping back to physical positions. Power success can therefore change without changing the mask.

**Minimal repair.** Freeze executable pseudocode: fresh-root/reset law per prefix and per Stage-C run; `default_rng` calls; the exact Bernoulli and uniform APIs and call shapes; child-spawn timing; and a canonical row order representable by BS-2f. Pin expected injection-label, flip, permutation-index, and success-count digests, not only the final real permutation vector.

### 5. BLOCKER — the count-oracle “completeness proof” does not prove footprint completeness, and zero-count bricks break BS-2o

**Quote.** BS-2c requires every candidate brick, but its specified completeness proof is only “sum over bricks equals the ungrouped total count from the same service” (lines 51–60). The grouped query naturally returns only groups with rows. BS-2o starts from every table candidate, gives every singleton `L=0`, and breaks that tie by larger `|c_j|` (lines 68–75).

**Why this fails.** A grouped and ungrouped query against the same incomplete service partition agree even when an entire brick/sky region is absent. Their equality proves internal aggregation, not that the release's candidate-brick universe was covered. It also does not prove that zero-eligible candidate bricks were anti-joined into the table.

If zero-count bricks are included as “EVERY candidate brick,” the first singleton tie can select a zero-count extreme-|c| brick. Then `N_S=0` and `c̄_S` is undefined for the next update. The literal executed two-brick case (`n=0, |c|=1` selected before `n=10, |c|=.1`) produced:

`first_pick_zero_count_then_next_delta nan isfinite False`

If zero-count bricks are silently omitted, the promised every-brick table and its alleged completeness proof are false.

**Minimal repair.** Pin an independent release brick-universe manifest; left-join grouped counts onto it; emit and count explicit zeros; prove the anti-join is empty and universe hash matches the release. Exclude `n_eligible=0` from BS-2o by an explicit frozen rule (while retaining them in the oracle receipt), and state the positive-count invariant.

### 6. BLOCKER — “IEEE-754 float64” does not determine the exact sequence or the demanded digests

**Quote.** BS-2o requires exact-sequence agreement while giving only an algebraic update identity “in IEEE-754 float64” (lines 68–75, 200–206). It does not freeze the `c̄` recurrence, operation association, integer-to-float conversion, `Var_k` convention, or a canonical JSON serialization, yet requires canonical-serialization digests to match.

**Why this fails.** Two algebraically identical float64 associations can reverse a candidate order. The executed finite fixture was

`N_S=605939, n1=558, n2=3964, d1=.39017359187169964, d2=.1467993743143592`.

Evaluating `((N*n)/(N+n))*(d*d)` gave scores `84.86921617200353` and `84.86921617200355` (candidate 2 wins), while `(N/(N+n))*n*d*d` gave `84.86921617200355` and `84.86921617200353` (candidate 1 wins). Both use float64 throughout. A relative tolerance on L cannot repair an already divergent exact sequence, and “canonical serializations” is asserted without defining bytes.

**Minimal repair.** Freeze operation-level reference pseudocode, input dtypes, `c_j` construction, weighted-mean update, FMA policy, `Var=L/N` or other exact convention, non-finite handling, and comparison order. Define the order/ledger/final-set JSON schema and canonical bytes (for example RFC 8785 plus explicit float encoding, or a headerless binary schema) before asking for digest equality.

### 7. BLOCKER — V4 carries receipts that its cited predecessor says are not evidence for the production input path

**Quote.** V4's class-P BS-3 says the instrument and identity receipts are carried from the predecessor tree, and §8 says cutout/inference runners are carried (lines 220, 237–243). But V3-pred's binding prerequisites to sky access say the exact single-band HDU/plane route must be newly bound, the input function and full R1–R5 battery must be rerun, the old R1–R5 receipts “are not evidence about the instrument as now consumed,” and `nm_acquire_cutouts.py` must not execute because it hardcodes the superseded `grz`, 256, `[3,256,256]` contract (V3-pred lines 374–386).

**Why this fails.** A targeted search of V4 for `input-function`, `R1`–`R5`, `nm_acquire_cutouts`, `HDU/plane`, `single-band`, and `128` found no carried prerequisite. The only matches were unrelated axis/release text. The class-P register can therefore be filled with receipts the cited source expressly disqualifies, while BS-6 covers transport checksums/bytes but not the tensor-producing function or superseded-runner ban. DR11 versus DR10.1 makes the omitted route binding more, not less, important.

**Minimal repair.** Add class-P slots for exact release-specific HDU/plane schema, input-function code/hash/tensor layout, full R1–R5 rerun through the production function, and the gated replacement runner. Carry the old-runner prohibition and conditional local WCS re-gates explicitly. Do not label BS-3 filled from predecessor receipts that the predecessor itself declares stale.

### 8. BLOCKER — the void rule excludes the calibration rules that determine the decision estimand

**Quote.** “Any change to a §1–§5 parameter after the first real-sky χ read voids the run” (lines 195–196). The c-bin definitions, scalar-admissibility threshold, fallback choice, calibration floors, and `INCONCLUSIVE-BY-CALIBRATION` rule are all in §6 (lines 177–194).

**Why this fails.** Under the laziest literal reading, those §6 parameters can be changed after real `χ` has been read without triggering the stated void. They affect whether the scalar or profile estimator is used, its uncertainty, whether Stage C runs, and the final outcome. The predecessor explicitly treated changes to its hand-check protocol after a real statistic as void; V4's section-number restriction drops that safeguard.

**Minimal repair.** Make any change to §§1–6, the binding-slot semantics, RNG/serialization contract, or calibration/power implementation after the first real-sky `χ` read void the run. State that post-read amendments cannot cure the void.

## Attacks that held

1. **Custody and quotations.** Recomputed source hashes were predecessor `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`, BS6-pred `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`, and amended scope `995b2e729a3362f0445cac9d5da6d290fddac9f8018e75f2c0aa87c190c93de7`. The Longo amplitude/uncertainty/axis, East-of-North sign, 100,000 permutations, 0.001/0.05 decision thresholds, 3.09 floor, 0.85 quality floor, 0.8572 retention value, weight prefix, and τ agree with the cited predecessor. All eight BS6-pred cuts agree in operator/numeric content; predicate 6 now contains the exact executable `POWER(shape_e1,2)+POWER(shape_e2,2) < 0.1836734693877551` string.
2. **Axis.** Independent ICRS/Galactic matrix multiplication produced `(-0.676971771271432,-0.509846551777774,+0.530816083537352)`. Printed-minus-computed component differences were `[+2.220e-16,-1.110e-16,-3.331e-16]`; the displayed RA/Dec was `(216.9844355052152°,32.060610901162°)`.
3. **Acyclic headline chain.** The narrow BS-2o → BS-5p → BS-2s threshold dependency repairs the V3 `L_plan` cycle. Findings 1 and 3 are separate class/timing defects elsewhere.
4. **Amendment authority and no leverage-global claim.** Amendment 1 really does authorize a deterministic threshold-reaching heuristic without global leverage maximization. V4 does not retain a positive global leverage-maximizer claim. Finding 2 is the new, false global brick-count minimization/small-case certification claim.
5. **Greedy update and power arithmetic.** The weighted-SSE update identity is algebraically correct. The one-sided CP scan first passes at `x=962`, lower bound `0.950487129744074`; `x=961` gives `0.9493659932051121`. The integer per-brick retention transform and ±1/flip law are now stated. Finding 4 is the remaining API/reset/order nondeterminism.
6. **Fallback point algebra.** `β̂/ŵ` correctly deconvolves a piecewise-constant `a(c)` at the population-expectation level. Finding 3 concerns impossible bin timing and the absent uncertainty/covariance contract, not the point formula.
7. **Inventory claim.** The cited inventory hash is `2df3a22065344a3378e069b022d316f39164ddc908f73d0fb4cfcf40323e0550`; parsing found 2,872 rows, 10 known sizes, mean 1,236,552,768 bytes, and 1,436 rows per version. Applying that mean to one version gives 1.775689774848 decimal TB. V4 correctly labels ~1.8 TB an estimate, not an inventory.

## Evidence ledger / shown commands and calculations

Content read:

- `BRIEF_GATE_SUCCESSOR_V4.md`
- `../PREREG_SUCCESSOR_DRAFT_V4_20260824.md`
- `GATE_GPT56_SUCCESSOR_V3.md`
- `GATE_CODEX_SUCCESSOR_V3.md`
- `../../SUCCESSOR_SCOPE_20260821.md`
- `../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
- `../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md`
- `../gpt1/sweep_inventory.jsonl` (parsed as JSONL; first five rows displayed)

Commands/checks executed:

- `shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V4_20260824.md`
- `shasum -a 256 ../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md ../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md ../../SUCCESSOR_SCOPE_20260821.md`
- `shasum -a 256 ../gpt1/sweep_inventory.jsonl`
- Targeted repository searches for global-optimality language, every BS reference, fallback-uncertainty symbols, MUST/exact/determinism language, predecessor quotations, and the missing input-path prerequisites.
- Exact-rational and float64 weighted-SSE enumeration for the seven-brick local-minimum counterexample and all direct-removal / swap-then-removal neighbors.
- Float64 candidate-order reversal search under algebraically equivalent update associations.
- NumPy SeedSequence/Bernoulli API and Stage-C row-order experiments from seed 20260824.
- SciPy `beta.ppf` scan for the one-sided Clopper–Pearson threshold.
- Independent matrix rotation and display-coordinate calculation for the machine axis.
- Exact profile-attenuation and per-bin gradient/covariance calculations.
- JSONL row/version/known-size inventory aggregation.

No `/Users/duhokim/NebulaMindData/` path was read. No source artifact was edited. The only lane write is this report.

## Testimony

None. The verdict relies on the pinned source bytes and the shown executable checks.

**REFUSED** — blocking findings 1–8: pre-freeze BS-7 requires post-unblinding statistics; the local selector falsely claims minimization/certified small-case optimality; calibration bins precede their mask and fallback uncertainty is undefined; injection/Stage-C randomness is not reproducible; count completeness and zero-count handling are invalid; float/serialization rules cannot support exact blind-double agreement; stale input-path receipts are carried despite the predecessor's explicit disqualification; and the void rule excludes decision-changing §6 calibration rules.
