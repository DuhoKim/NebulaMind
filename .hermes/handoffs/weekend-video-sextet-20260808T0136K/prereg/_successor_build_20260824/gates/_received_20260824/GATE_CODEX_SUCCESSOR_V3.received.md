# CODEX adversarial gate — successor preregistration draft V3

## Custody pin

The first review command was:

`shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V3_20260824.md`

Computed:

`1c4788c5555a9f7ed00c83d0431c6ad4c4730faa79da5da6e7f2580371730532  ../PREREG_SUCCESSOR_DRAFT_V3_20260824.md`

This equals the brief's required pin. Review proceeded on those bytes.

## Numbered findings

### 1. BLOCKER — the replacement greedy rule still does not maximize weighted leverage

**Quote.** Section 2 lines 54–57 calls the procedure a “deterministic greedy marginal-gain optimizer” and accepts the brick maximizing `L(S ∪ {j})` at each step. The design authority requires a subset to be chosen to maximize `N·Var(c)`.

**Why this fails.** Forward greedy maximization is not global maximization for unequal brick counts. An exact-rational brute-force fixture gives:

- `c = [-0.12, 0.15, -0.67, 0.43, -0.78]`
- `n = [8, 8, 18, 7, 3]`
- greedy three-brick sequence `[4,3,2]`, `L = 367719/56000 = 6.566410714285714`
- globally best three-brick subset `(1,2,3)`, `L = 63419/8250 = 7.687151515151515`
- optimum/greedy ratio `1.1706778405480402`

At a leverage threshold of 7, greedy needs four bricks (`L = 8.495363888888889`), while a three-brick subset already clears it. Thus V3 repairs the published three-point descending-|c| counterexample but replaces it with another non-maximizing rule. The claim of implementation-level determinism is also incomplete: no arithmetic or comparison law is frozen for marginal gains/ties, although the blind double demands an exact sequence. Ordinary float evaluation even gives a singleton `L` of `3.697785493223493e-32` for one member of the fixture while the mathematical value is zero.

**Minimal repair.** Either select the full footprint; freeze an exact optimizer under a stated resource constraint and verify small cases against a brute-force oracle; or obtain a scope amendment that explicitly authorizes a heuristic and stops calling it maximizing. Freeze the numeric comparison/tie law used by both implementations.

### 2. BLOCKER — the `L_plan` dependency cycle remains, and the common interface cannot receive its stop value

**Quote.** Section 2 line 57 stops the selector at `L_plan`. Section 4 lines 102–103 says BS-5p produces `L_min_plan` and `L_plan`. Section 6 lines 150–151 gives the implementation only `{brickid, ra, dec, n_eligible}` plus the axis vector and requires output “at halt.” The slot table line 164 requires BS-2p's accepted sequence/N/Var/L, while line 167 puts BS-5p “after BS-2p.”

**Why this fails.** The declared order is still circular:

`BS-2p accepted-at-halt → needs L_plan → produced by BS-5p → declared after BS-2p`.

The interface lines contain zero `L_plan` inputs. BS-2p therefore cannot produce its required halted sequence, and BS-5p cannot receive the optimizer prefixes it needs under the slot order as written. This is the V2 `L_min` cycle under renamed slots, not a dissolved cycle.

**Minimal repair.** Split the planning selector into an acyclic chain: (1) BS-2o emits a full deterministic order and prefix-leverage curve without a halt; (2) BS-5p computes `L_min_plan` and `L_plan`; (3) a later BS-2s supplies `L_plan` explicitly to both implementations and records the halted prefix. Make every interface and slot dependency say this same order.

### 3. BLOCKER — Stage P is not the deterministic, independently rederivable algorithm it claims to be

**Quote.** Section 4 lines 95–102 calls Stage P deterministic, inputs the 0.8572 retention lower bound, writes latent `s ~ Bernoulli((1 + A_L·c)/2)`, applies a symmetric flip, runs 1,000 skies, and passes on a “Clopper–Pearson 95% lower confidence bound” at least 0.95.

**Why this fails.** Four outcome-changing operations are unspecified:

1. Section 3 defines `s ∈ {+1,−1}`, but a Bernoulli draw is `{0,1}`. V3 does not say `P(s=+1|c)=...` or `s=2B−1`, nor whether “flip” means complement or multiplication by −1.
2. The 0.8572 retention bound is named but never applied: deterministic per-brick floor/rounding, fractional weights, or random thinning produce different masks and power.
3. Section 3 fixes the permutation RNG, but no injection RNG/seed, prefix traversal order, trial/permutation stream-reset law, or exact NumPy permutation call is frozen. BS-5p merely records “seeds” after the computation; it is not a precommit producer.
4. “Clopper–Pearson 95% lower confidence bound” does not select a tail convention. At `n_trials=1000`, scanning exact beta quantiles gives a minimum of 962 successes (38 failures) for a one-sided 95% lower bound, lower endpoint `0.950487129744074`; the lower endpoint of an equal-tailed two-sided 95% interval needs 964 successes (36 failures), `0.9505070882819876`. Both are conventionally described as a 95% CP lower bound.

Because `L_min_plan` is the smallest passing prefix, any of these choices can move the stopping threshold. The receipt cannot repair a procedure after seeing its outputs.

**Minimal repair.** Freeze `P(s=+1|c)`, the ±1 mapping and flip operation; the exact conservative retention transform; injection/permutation RNG APIs, versions, seeds, reset/order law across prefixes/trials/permutations; and the CP beta-quantile formula/tail. State the resulting integer pass count (for example, `x ≥ 962` if the one-sided convention is chosen) before BS-5p runs.

### 4. BLOCKER — the optimizer needs all eligible counts before the bounded acquisition order can exist

**Quote.** Section 2 lines 54–61 maximizes over per-brick post-photo-z eligible counts. Lines 64–67 say sweep and photo-z tiles are fetched in that optimizer's acceptance order, “counted on arrival,” never fetched whole, and governed by an approval ceiling. BS-1b supplies product paths/columns/join keys; no slot supplies a complete count oracle or the catalog-fetch approval ceiling.

**Why this fails.** Scoring every remaining candidate `j` requires `n_eligible(j)` before the next brick can be chosen. Under the stated mechanism those counts appear only when tiles arrive, but their arrival order is the optimizer output that already needs the counts. The cited GPT1 artifact does not close this: its hash matches `2df3a22065344a3378e069b022d316f39164ddc908f73d0fb4cfcf40323e0550`, but it is a URL inventory (2,872 rows, 2,862 null sizes), not a post-photo-z per-brick eligible-count table. The “≈1.8 TB” value is an extrapolation from five known DR10.1 sizes, not a complete byte inventory.

**Minimal repair.** Add a pre-BS-2p class-P producer for a hash-pinned count-oracle table covering every candidate brick, with a specified query/fetch path, complete-count proof, and approval/byte ceiling fixed before catalog access. The optimizer consumes that artifact; only later image/catalog payload retrieval may follow its order. If producing the oracle itself requires the whole catalog, state and gate that instead of claiming the whole set is never fetched.

### 5. BLOCKER — the detection-floor uncertainty has two incompatible accuracy inputs

**Quote.** Section 3 line 82 uniquely defines `σ_ours` using the point estimate `â`. Section 5 lines 122–123 then requires the `3.09·σ_ours` floor to be “evaluated at the receipted a_LB,” and line 139 repeats that rule without defining a second sigma function.

**Why this fails.** One compliant implementation can use the only defined `σ_ours(â)`; another can substitute `a_LB` for `â` only for the floor. They can classify amplitudes differently. For an illustrative executable input (`β̂=.02856`, `σ_β=.005`, `â=.90`, `σ_a=.02`, hence `a_LB=.8671`), the stated formula gives floor `0.02008469694002127` at `â` and `0.02203871711591712` after substitution of `a_LB`, a 9.73% difference. The delta-method square term itself has the correct derivative magnitude, but the document also does not state the zero-covariance assumption needed to omit the `Cov(β̂,â)` term.

**Minimal repair.** Define `σ_ours(a*)` as an explicit function and state the exact `a*` used in each decision band and floor. Define `σ_a`, and either enforce an independent/disjoint attenuation sample or freeze the covariance term/rule. Then give BS-7/BS-8 fixtures that evaluate both the point-estimate band and conservative floor.

### 6. MAJOR — BS-7's full-vector digest still has no canonical byte or RNG contract

**Quote.** Slot BS-7 line 168 requires sha256 of the “canonical float64 serialization” of the full `β̂_perm` vector. Section 3 lines 88–89 says only `default_rng(20260824)` and the generator's “k-th draw.”

**Why this fails.** “Canonical” is asserted, not defined: byte order, contiguity/order, headerlessness, finite-value rule, NumPy version, exact permutation API, and stream-reset behavior are absent. Independent implementations can generate mathematically equal vectors but different bytes, or different permutation vectors with the same valid p-value. Under the no-reconciliation rule that makes the slot either unfillable or subject to an undocumented choice.

**Minimal repair.** Freeze the exact permutation-index generator/API and environment; serialize vector index order 0…99,999 as raw little-endian IEEE-754 binary64 C-order bytes with no header (and reject non-finite values); pin expected fixture digests. Have the receipt recompute from raw indices as well as labels.

### 7. MAJOR — the claimed byte-for-byte Cut-6 restatement changes one executable predicate

**Quote.** Section 2 line 38 calls the list the full predecessor Cut-6 predicate set. The gate brief requires comparison to BS6-pred byte-for-byte. V3 line 47 writes `shape_e1² + shape_e2² < 0.1836734693877551`; BS6-pred lines 36–37 writes `POWER(shape_e1,2)+POWER(shape_e2,2) < 0.1836734693877551`.

**Why this fails.** A byte comparison passes predicates 1–5 and 7–8 but fails predicate 6; the exact BS6-pred inclination string is absent from V3. The two forms are mathematically equivalent, so this is not a threshold change, but the V3 form is mathematical display text rather than the hash-pinned executable SQL predicate demanded by the brief.

**Minimal repair.** Quote the exact BS6-pred `POWER(...)` predicate as the executable rule, optionally followed by the squared-display equivalence.

### 8. MINOR — one slot reference survived the P/f split

**Quote.** Section 6 line 132 says the labelling audit's strata are “in BS-8.” The V3 register defines only BS-8p and BS-8f.

**Why this fails.** A mechanical reference inventory finds all §1–§9 section references, but `BS-8` is the sole undefined slot reference. It leaves unclear whether the strata design belongs to the freeze-prerequisite measurement plan or the post-freeze measurement receipt.

**Minimal repair.** Replace it with `BS-8p/BS-8f` (or the one intended slot) and state producer/consumer responsibility.

## Checks that held

- Frozen predecessor hash recomputed as `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`; BS6-pred as `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`.
- The IAU constants-only rotation of `(l,b)=(52°,68.5°)` produced `(-0.676971771271432, -0.509846551777774, +0.530816083537352)`, with component differences from the printed vector at `[-2.220e-16, +1.110e-16, +3.331e-16]`. It renders as `(RA,Dec)=(216.9844355052152°,32.060610901162°)`. The text makes both RA/Dec pairs display-only and the implementation interface accepts the vector, so the textual runtime-frame-conversion repair held.
- Attenuation held: at `a=.85`, `(2a−1)·0.0408 = 0.02856`, and division by `(2a−1)` recovers `0.0408`. The delta derivatives are `1/(2a−1)` and `−2β̂/(2a−1)^2`; line 82 has the correct squared magnitude subject to Finding 5's covariance/input contract.
- The mandatory V2 three-point fixture held under the new greedy rule: it chooses `[0.99,−0.50]` after the first singleton and reaches `L=1.11005`, versus `0.00005` for `[0.99,0.98]`, ratio 22,201.
- Plus-one resolution held: with 100,000 permutations, zero exceedances gives `9.99990000099999e-6`; 99 gives `0.000999990000099999` (pass); 100 gives `0.001009989900100999` (fail).
- The Stage-C admissibility language excludes uniform-sphere, parent-position, and every non-mask input, and its class-E chain BS-2f + BS-8f → BS-5f → unblinding is acyclic.
- Predecessor values attacked — 0.0408, 0.011, axis, 100,000 permutations, 0.001/0.05 thresholds, 3.09 factor, 0.85 floor, 0.8572 retention restatement, τ, East-of-North sign — were present in the pinned predecessor. All eight Cut-6 predicates are semantically present and ordered; Finding 7 is the one literal byte discrepancy.

## Commands/checks shown

- `shasum -a 256` on V3, V3-pred, BS6-pred, and GPT1 inventory.
- Constants-only Python rotation from NGP `(192.85948°,27.12825°)` and `l_NCP=122.93192°`, with vector/RA/Dec comparison.
- Exact `fractions.Fraction` greedy enumeration plus brute-force three-subset oracle.
- `scipy.stats.beta.ppf` scan over 0…1,000 successes for one-sided and equal-tailed CP lower bounds.
- Python plus-one p-value count boundary at 0, 99, and 100 exceedances.
- Python extraction of the BS-2p/BS-5p dependency lines and common-interface fields.
- Python byte-string comparison of all eight BS6-pred predicates and mechanical §/BS reference inventory.
- GPT1 JSONL parse: 2,872 rows, 10 known sizes, 2,862 null sizes, 12,365,527,680 known bytes across both version samples.

No `/Users/duhokim/NebulaMindData/` path was read. No source artifact was edited.

## Testimony

None. The verdict rests on pinned files and the executable checks summarized above.

**REFUSED** (blocking findings 1–5: non-maximizing weighted selector; surviving `L_plan` cycle; under-specified Stage-P power algorithm; count-before-order acquisition cycle; ambiguous detection-floor uncertainty).
