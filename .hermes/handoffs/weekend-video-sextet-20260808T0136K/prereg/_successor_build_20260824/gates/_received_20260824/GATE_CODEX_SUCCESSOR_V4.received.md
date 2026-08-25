# CODEX adversarial gate — successor preregistration draft V4

## Custody pin

The first review command after reading the dispatch brief was:

`shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V4_20260824.md`

Computed:

`1ea8bb8d8e236049b2e73091770f3a7f58dbee5a3b8385ba3f30cb11fd31adcb  ../PREREG_SUCCESSOR_DRAFT_V4_20260824.md`

This equals the brief's required pin. Review proceeded on those bytes.

Independent source pins:

- V3-pred: `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- BS6-pred: `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`
- sweep inventory: `2df3a22065344a3378e069b022d316f39164ddc908f73d0fb4cfcf40323e0550`

All three agree with the values or prefixes used by V4.

## Numbered findings

### 1. BLOCKER — the local-improvement procedure is not executable as written and a seven-brick fixture defeats its claimed brick-count minimization

**Quote.** V4 lines 80–90 says the pass “minimizes brick count,” then specifies removals followed by a swap “when the swap keeps `L ≥ L_plan` and reduces…”; the object of “reduces” is missing. It then permits an equal-count leverage-raising swap “only if [it] then enable[s] a removal,” but gives no accepted/unaccepted pair scan order, no definition of removal-side `ΔL`, and no fail action at the 10,000-move cap.

**Why this fails.** The prose does not select a unique next move. Worse, the literal immediate-removal reading has strict local minima above the minimum brick count. I executed the frozen greedy rule with ascending BRICKIDs `0…6` on:

- `c = [-0.38, 0.67, 0.57, 0.21, -0.32, 0.99, -0.35]`
- `n = [8, 2, 1, 13, 10, 1, 13]`
- `L_plan = 1.9`

The full greedy prefixes begin `{5}` at `L=0`, `{5,0}` at `L=1.6683555555555551`, and `S0={5,0,1}` at `L=2.9872727272727273`. No removal is legal: the three resulting pair leverages are `1.7640000000000002`, `0.06826666666666664`, and `1.6683555555555551`. Exhaustive enumeration finds exactly one passing pair, `{3,6}`, at `L=2.0383999999999998`. It is disjoint from `S0`, so no single swap from `S0` can produce a set from which one removal reaches that pair. The stated pass therefore stops at three bricks while the brute-force optimum uses two. This is a ≤12-brick unequal-count adversarial fixture of the exact class the receipt claims to certify. The randomized-search count, distribution, seed, and pass/fail consequence are themselves unfrozen, so a lazy compliant battery can simply miss it.

**Minimal repair.** Define every move and pair scan order, the removal-loss formula/ties, a strict anti-cycle potential, and cap-exhaustion as FAIL. On candidate universes of ≤12 bricks, make the brute-force oracle's minimum-cardinality subset the required output, not merely a comparison. For production, call the result only the output of the stated local procedure unless an actual global certificate exists; add the fixture above to the mandatory battery.

### 2. BLOCKER — class-P BS-7 either requires real labels before freeze or fails to bind the production permutation record

**Quote.** V4 lines 3–6 says every class-P slot must hold before the text becomes a preregistration and class-E slots are filled during the run. Yet class-P BS-7 at line 222 requires `β̂_obs`, the full 100,000-value `β̂_perm` digest, and recomputation “from raw indices AND labels.” The separate asymmetric fixture is named later in the same cell.

**Why this fails.** If `β̂_obs` and the full vector are the production values, BS-7 consumes real χ labels before the draft is frozen, contradicting the class definition, the disclosure boundary, and the draft's “nothing is in force” status. If they are fixture values, the class-P slot can pass without ever binding the production `β̂_obs` or production permutation payload. The explicit later mention of a fixture does not resolve which interpretation applies to the earlier fields. Either reading leaves the slot chain invalid.

**Minimal repair.** Split BS-7 into (a) class-P BS-7p for the declaration, finite-value checks, asymmetric fixtures, boundary p-values, environment, and pinned fixture digests, and (b) a class-E BS-7f for the sealed production `β̂_obs`, raw-index/label reconstruction, and canonical 800,000-byte payload digest, with an explicit downstream block before decision release.

### 3. BLOCKER — the calibration-bin boundaries are assigned to a producer that cannot possess the accepted mask

**Quote.** Lines 189–190 fix the three c-bin boundaries “at BS-2s as the accepted mask's count-weighted c-tertile boundaries.” But class-P BS-2s consumes the count oracle/order/power threshold and produces the selected brick set (lines 202–203, 219). The actual accepted-position mask is a post-freeze class-E artifact produced only at BS-2f (line 230), after image inference.

**Why this fails.** At BS-2s there are brick centres and eligible-parent counts, not per-object inference acceptance flags or the actual accepted-position mask. The document separately names BS-2f as the producer of exactly that later object-level mask. Thus the requested boundaries cannot be fixed at the named slot. “Count-weighted” is also ambiguous once the input is already one row per accepted object. In addition, V3-pred's HC-1H allocation is over nine machine-state × `|χ|` strata, while V4 adds three c strata without freezing the joint-cell allocation, floors, or weighting rule.

**Minimal repair.** Freeze the bin-construction algorithm and joint HC allocation in BS-8p. Instantiate and hash-pin the numeric boundaries at BS-2f from positions plus acceptance flags only, before any χ sign is opened, and make BS-8f consume that artifact. State whether each accepted object has unit weight and how the three c bins cross the inherited nine HC strata.

### 4. BLOCKER — the fallback point correction can be right, but the fallback decision uncertainty is not defined

**Quote.** Lines 126–132 define `ŵ = Cov_w(c,(2â_b−1)c)/Var_w(c)` and `Â_L=β̂/ŵ`, then say the fallback “replaces the two derivatives by the frozen per-bin delta-method gradient.” Lines 173–174 invoke a “frozen per-bin conservative gradient.” BS-8f supplies only `â_b`, marginal `σ_ab`, and `a_LB_b` (line 231).

**Why this fails.** Independent algebra confirms the point estimator only if `Cov_w` and `Var_w` use the same equal-object empirical measure as the raw centred slope. V4 defines no `w_i`, so another compliant implementation can use calibration/population weights and obtain a different correction. The uncertainty is more seriously incomplete: no gradient formula, no covariance matrix among the three `â_b`, no fallback `Cov(β̂,â_b)` rule, and no formula for `a_LB_b` are frozen. The inherited HC-1H correction contains a shared synthetic-error estimate, so the bin accuracies are not generally independent. In an executable six-position example, `β̂=0.03459539170506913`, `ŵ=0.8479262672811061`, and `β̂/ŵ=0.0408` exactly recover the injected amplitude under unit weights. Its three accuracy derivatives are `[-0.04700869565217392, -0.001552173913043479, -0.04767391304347826]`. With identical marginal `σ_ab=0.01`, independence gives sigma `0.0006697035684280154`, while correlation `ρ=0.8` gives `0.0009113677877851929`, 1.36085× larger. Both satisfy the fields currently required at BS-8f but move every fallback band and floor.

**Minimal repair.** Define `w_i=1/N` over the sealed accepted objects (or another explicit measure matched to `β̂`), print the analytic derivatives, require the full per-bin covariance matrix including the shared-error term, declare/freeze all cross-covariance handling with `β̂`, and define each `a_LB_b`. Bind one numeric fixture for the point estimate, decision sigma, and conservative floor.

### 5. BLOCKER — the seed-spawn contract has no prefix/stage dimension, so BS-5p is not reproducible

**Quote.** Lines 112–118 create one `root.spawn(1+n_trials)` array. Lines 145–151 use `children[t]` for injection trial t and `children[t].spawn(1)[0]` for that trial's permutation stream. BS-5p must evaluate prefixes to find the smallest passing one, and BS-2s later reruns Stage P on `S_final`.

**Why this fails.** NumPy `SeedSequence.spawn` is stateful. Executing `children[1].spawn(1)[0]` twice on the same object under NumPy 2.4.3 produced states `[1206732362,2993308790,2232908008,737755349]` and `[1237200367,1208386509,3370498468,3454587257]`; rebuilding the root reproduced the first. Therefore “rebuild the root for every prefix” and “reuse the child objects while walking prefixes” are both natural readings and produce different permutation skies. The contract does not assign streams by prefix, distinguish Stage P from the S_final re-pass or Stage C, or freeze reset order. The first passing prefix can consequently differ while every implementation uses the printed seed and APIs.

**Minimal repair.** Give every stochastic operation an immutable hierarchical address including stage, prefix identity (or S_final digest), trial index, and injection/permutation role. Construct each `SeedSequence` from that address without stateful repeated `spawn` calls, pin NumPy version, and publish fixtures covering at least two prefixes plus the S_final/Stage-C namespaces.

### 6. BLOCKER — the 100,000 full-sphere-equivalent rule does not identify raw versus retained leverage

**Quote.** The only defined `L` is the BS-2o ledger SSE over eligible counts `n_j` (lines 68–78), where BS-5p “also requires `N_eq=3·L≥100,000`.” Stage P later transforms those counts to `n_ret_j=floor(0.8572 n_j)` (lines 141–149), but defines no retained-leverage symbol. The design authority's requirement is accepted-sample leverage.

**Why this fails.** One implementation can apply `N_eq` to the already available raw ledger L; another can recompute L from retained counts and reasonably call that the Stage-P L. On the V3 retention fixture `c=[-1,0,1]`, `n=[2,3,10]`, the frozen floor gives `[1,2,8]`: raw `L=7.733333333333333` (`N_eq=23.2`) versus retained `L=4.545454545454545` (`N_eq=13.636363636363635`). The same ambiguity can move the first passing prefix and therefore `L_min_plan` and `L_plan`. The floor operation itself is now deterministic; the threshold it feeds is not.

**Minimal repair.** Define `L_raw(k)` and `L_ret(k)` explicitly, state which one must satisfy `3L≥100,000`, and state which ledger quantity is returned as `L_min_plan` and multiplied by 1.2. If the scope requirement is accepted-sample equivalent, apply it to the retained planning construction and separately report raw leverage.

### 7. BLOCKER — the greedy identity is mathematically correct, but exact-order and digest determinism remain under-specified

**Quote.** Lines 68–75 require exact-float tie comparisons and an exact order while freezing only the marginal-gain identity. Lines 200–206 give the implementations `{brickid,ra,dec,n_eligible}` plus the axis vector, allow `Var`, `L`, and `N_eq` to differ by `1e-9`, but also require equal digests of unspecified “canonical serializations” of their JSON outputs.

**Why this fails.** The update identity is correct: 1,000 independent float64 comparisons against direct weighted-SSE recomputation had maximum absolute path difference `8.526512829121202e-14`. That nonzero path difference is precisely why the remaining contract matters. V4 does not freeze the RA/Dec-to-unit-vector formula and angle conversion for brick `c_j`, the `c̄_S` update/reduction order, the ledger `Var_k` denominator, use of fused operations, or the JSON canonicalization (field order, float rendering, Unicode, separators). Near-equal gains can change an exact-float tie/order; compliant floating ledgers can pass the stated tolerance but cannot be required to have byte-equal full-JSON digests without a serialization and numeric identity law. The no-reconciliation STOP rule then turns this omission into an unfillable gate.

**Minimal repair.** Hash-pin canonical little-endian `<f8` `c_j` values as BS-2c fields or freeze their exact computation; freeze incremental `N`, mean, and L update operations and `Var_k=L_k/N_k`; define the exact serialized fields/bytes. Either require bit identity for digested floats or digest only exact discrete fields and retain the numeric tolerance for floats—do not require both without a canonical quantization rule.

### 8. BLOCKER — the stated count-oracle equality is not a full-footprint completeness proof

**Quote.** Lines 51–60 require a table covering every candidate brick and call “sum over bricks equals the ungrouped total count from the same service” the completeness proof.

**Why this fails.** Equality of two counts over the same unstated query domain proves closure only inside that domain. A grouped query under the eight predicates normally emits no row for a candidate brick with zero eligible objects; the ungrouped total still equals the sum. More generally, the same accidental footprint restriction can appear in both query texts and preserve equality. V4 hash-pins neither a release-wide candidate-brick manifest nor its cardinality, and it does not require an outer join/zero fill. Thus the laziest compliant implementation can omit candidate bricks while satisfying the only specified proof. This also conflicts with BS-2o's promised FULL traversal.

**Minimal repair.** Pin an independently enumerated release/hemisphere candidate-brick manifest and count. Left-join predicate counts onto that domain, materialize `n_eligible=0`, prove key equality/domain cardinality as well as grouped-sum closure, and make both grouped and ungrouped query scopes mechanically compare to the manifest.

### 9. BLOCKER — the post-χ void rule excludes outcome-changing §6 provisions

**Quote.** Lines 195–196 void only a change to a “§1–§5 parameter” after the first real-sky χ read. But §6 contains the calibration bins, scalar-admissibility threshold `0.03`, per-bin `0.85` floors, fallback-path choice, and calibration halt.

**Why this fails.** A literal amendment to any of those §6 decision-critical rules after χ exists does not trigger the written void clause. Those rules determine whether the run halts, which estimand is used, and its uncertainty; they are no less outcome-changing than §§1–§5. General custody language does not repair an explicit narrowly scoped void law.

**Minimal repair.** Void any post-first-χ change to every binding rule, parameter, algorithm, slot schema, or decision threshold in the preregistration, while explicitly exempting only the mechanical filling of predeclared class-E values under their frozen producers.

### 10. MINOR — the sweep-inventory sentence combines a two-version row count with a one-version byte estimate

**Quote.** Lines 62–64 say the inventory has 2,872 files, 10 measured sizes averaging 1.24 GB, and an estimated ~1.8 TB.

**Why this fails.** Parsing the pinned JSONL gives 2,872 rows, 10 known sizes, mean `1,236,552,768` bytes. Multiplying all 2,872 rows gives `3,551,379,549,696` bytes = 3.551 TB. The file actually contains two 1,436-row version groups (10.0 and 10.1), each with five measured sizes and a 1.776-TB extrapolation. Thus ~1.8 TB is a defensible one-release estimate, but not the arithmetic attached to the printed 2,872-file/10-size description.

**Minimal repair.** Say explicitly that the inventory contains two version groups, while the selected release would fetch 1,436 files and extrapolates to ~1.776 TB from its five measured sizes; or retain 2,872/10 and print ~3.551 TB.

## Attacks that held

1. **Authority amendment.** Amendment 1 textually licenses a deterministic threshold-reaching heuristic with no global-subset-optimality requirement. V4's affirmative “maximizing” is step-local `argmax`; its global-maximizer/optimizer occurrences are historical or explicit negations. Finding 1 attacks the separate claimed local minimization/small-case certificate.
2. **Acyclic top-level slot chain.** Ignoring the independent defects above, the named selection dependency is now directional: BS-2c → BS-2o → BS-5p → BS-2s, and BS-2o has no threshold input. The old BS-2p/BS-5p cycle is removed.
3. **Three published counterexamples.** Under representative separating thresholds 1.0, 20.0, and 7.0, greedy-cut plus legal removals reaches the brute-force minimum on all three printed fixtures: `L=1.11005` on pair `{0,2}`; `L=25.540862068965517` on pair `{2,3}`; and `L=7.687151515151514` on triple `{1,2,3}`. Finding 1 is a new adversarial fixture.
4. **Greedy update identity.** The printed weighted-SSE marginal identity is algebraically correct. The singleton exact-zero convention also repairs the V3 residual-roundoff first-step issue.
5. **CP arithmetic.** Independent `Beta.ppf(0.05;x,1001−x)` evaluation gives lower bounds `0.9493659932051121` at x=961 and `0.950487129744074` at x=962. The first passing count is exactly 962.
6. **Fallback point algebra.** With equal object weights and piecewise-constant bin accuracies, `E[β̂]=A_L·Cov(c,(2a_b−1)c)/Var(c)`, so `β̂/ŵ` does deconvolve the mean slope. Finding 4 is the missing measure and uncertainty contract, not a rejection of that identity.
7. **Axis and quotation fidelity.** Independent rotation from the printed IAU constants gives `(-0.6769717712714325,-0.5098465517777737,+0.5308160835373523)`, within `4.441e-16` per component of V4, with display `(216.98443550521517°,32.060610901162°)`. The Longo amplitude/sigma, axis, sidedness, p thresholds, 3.09 floor, 0.85 quality floor, 0.8572 retention value, τ, and carried design values resolve in V3-pred or the amended scope. All eight BS6 predicates occur in both sources, and predicate 6's executable `POWER(...)` string is byte-identical.
8. **Permutation bytes.** The production payload format itself is now exact: index order, contiguous little-endian `<f8`, C-order, no header, 800,000 bytes, finite-only, SHA-256. Finding 2 concerns when/where the production payload is receipted; Finding 7 concerns the separate BS-2 JSON digest.
9. **Stage-C admissibility and decision thresholds.** Stage C expressly excludes uniform-sphere, parent-position, and all non-mask inputs, halts before unblinding on failure, and uses the same one-sided p<0.001 / x≥962 rule. §5 preserves p<0.001, p>0.05, and the inclusive 0.001…0.05 inconclusive gap.
10. **No-reconciliation policy.** V4 explicitly says a blind-double divergence is a STOP and cannot be edited into agreement. That policy held; Findings 1, 5, and 7 identify contracts that must become unique before the policy can operate safely.

## Evidence ledger

Content read:

- `BRIEF_GATE_SUCCESSOR_V4.md`
- `../PREREG_SUCCESSOR_DRAFT_V4_20260824.md`
- `GATE_GPT56_SUCCESSOR_V3.md`
- `GATE_CODEX_SUCCESSOR_V3.md`
- `../../SUCCESSOR_SCOPE_20260821.md`, including Amendment 1
- `../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
- `../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md`
- `../../_successor_build_20260824/gpt1/sweep_inventory.jsonl`

Executed checks:

- SHA-256 on V4 and all three source artifacts listed in custody.
- Independent IAU-basis construction, vector/norm/display-coordinate comparison.
- Exact and float64 weighted-SSE recomputation; 1,000 random update-identity checks.
- Full greedy traversals and brute-force subset enumeration for all three published fixtures and the new seven-brick fixture.
- Exact Clopper–Pearson scan over x=0…1000.
- NumPy `SeedSequence` fresh-root versus repeated-spawn state comparison.
- Raw-versus-floor-retained leverage arithmetic.
- Piecewise-constant attenuation point-estimator and delta-gradient recomputation, with two covariance matrices sharing identical marginals.
- Mechanical slot/term/reference inventory and global-optimality wording sweep.
- JSONL count/size/version-group reconciliation.
- Byte-substring checks for the predecessor values and all eight BS6 predicates.

No `/Users/duhokim/NebulaMindData/` path was read. No source artifact was edited. The only write is this report.

## Testimony

None. Every verdict-bearing statement above is supported by pinned source text or an executed calculation shown in this report.

**REFUSED** — blocking findings 1–9: the local pass is neither uniquely executable nor minimum-cardinality on a new ≤12-brick fixture; BS-7 has an impossible/ambiguous class assignment; calibration bins are assigned to the wrong producer; fallback uncertainty is not defined; stochastic streams lack prefix/stage identity; the 100,000-equivalent threshold does not bind raw versus retained leverage; float/order/JSON digest determinism is incomplete; the count-oracle proof does not close the candidate-brick domain; and the post-χ void law excludes decision-critical §6 rules.
