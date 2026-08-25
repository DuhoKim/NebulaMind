# GPT56 ADVERSARIAL GATE — successor preregistration draft V3

## Custody pin

First command, before reading the draft:

`shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V3_20260824.md`

Computed:

`1c4788c5555a9f7ed00c83d0431c6ad4c4730faa79da5da6e7f2580371730532  ../PREREG_SUCCESSOR_DRAFT_V3_20260824.md`

This equals the brief's required pin. Review proceeded on those bytes.

I also independently recomputed the two quoted source pins:

`shasum -a 256 ../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md ../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md`

Results:

- predecessor: `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- BS6-pred: `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`

Both match V3 lines 13–15.

## Numbered findings

### 1. BLOCKER — the BS-2p/BS-5p planning cycle still exists

**Quote.** Section 2 says the selector stops only when `L(S) ≥ L_plan` (lines 54–57). Section 4 says Stage P produces `L_min_plan` and then defines `L_plan = 1.2 × L_min_plan` (lines 95–104). The class-P table requires BS-2p to contain the accepted sequence, `N`, `Var`, and `L`, while BS-5p is explicitly “after BS-2p” (lines 164–167). The common implementation interface likewise emits the accepted sequence and `L at halt` (lines 150–154).

**Why this fails.** BS-2p cannot know where to halt or which sequence prefix is “accepted” until BS-5p has defined `L_plan`. BS-5p cannot find the smallest passing optimizer prefix under the stated slot order until BS-2p has produced the optimizer sequence/prefix geometry. Reclassifying the slots as class P and class E fixed the old BS-6 freeze paradox, but it did not dissolve this separate planning cycle. A full traversal could break the cycle, but neither the selector contract nor BS-2p requires a full traversal or a per-prefix ledger; both require an output “at halt.”

**Minimal repair.** Split BS-2p into a threshold-independent implementation/test receipt that emits the full deterministic traversal and a per-prefix `(N, Var, L)` ledger. Let BS-5p consume that ledger and define `L_plan`. Add a later planning-selection receipt that applies `L_plan` and records the unique halt prefix. Alternatively freeze a threshold before BS-2p by a separately specified, acyclic planning calculation.

### 2. BLOCKER — the acquisition order requires eligible counts that the text says are learned only after that order is chosen

**Quote.** The greedy step chooses the remaining brick maximizing count-weighted `L(S ∪ {j})`; planning inputs are post-photo-z eligible-parent counts (lines 54–61, 95–99). Yet the full sweep set is “NEVER fetched whole”; sweep and photo-z tiles are fetched “in the optimizer's acceptance order, counted on arrival,” and fetching halts at `L_plan` (lines 64–67).

**Why this fails.** Evaluating the argmax over every remaining `j` requires `n_eligible(j)` for every candidate before choosing the next brick. Under the only acquisition mechanism stated, that count is obtained when the brick's sweep/photo-z data arrive. The order therefore depends on counts that depend on executing the order. BS-1b freezes paths, columns, join keys, and predicate provenance, but no slot supplies a complete pre-order per-brick eligible-count census through a bounded metadata/query route. A lazy implementation can probe candidates in any order, thereby making the supposedly unique selection depend on an unstated discovery order; fetching all candidates to obtain the counts violates the explicit bounded-acquisition rule.

**Minimal repair.** Add a preselection slot that obtains and hash-pins the complete `{brickid, ra, dec, n_eligible}` table through an explicitly bounded count query or producer inventory that does not fetch the 1.8-TB row payload. Make that table the sole input to both selectors. If no such count source exists, define and gate an honest online algorithm whose discovery order and maximum byte ceiling are frozen; do not call it the stated all-candidate argmax.

### 3. BLOCKER — the greedy rule is deterministic but does not satisfy the design authority's maximize-leverage requirement

**Quote.** The scope requires a selected subset to maximize `N·Var(cos θ)`. V3 replaces descending `|c|` with a greedy rule that chooses the brick maximizing the next-step `L`, ties first on larger `|c_j|`, then smaller BRICKID (lines 52–59).

**Why this fails.** Local marginal maximization is not global subset maximization with unequal counts. I independently searched finite weighted fixtures using the exact V3 tie rule and obtained this two-brick counterexample (array order serves as increasing BRICKID):

`c = [0.04, -0.99, -0.91, 0.43, -0.94]`

`n = [8, 14, 33, 25, 25]`

For the first brick, every singleton has `L=0`, so V3's `|c|` tie-break selects `c=-0.99, n=14`. The best second brick is `c=0.43, n=25`, giving

`L_greedy = 14·25/(14+25)·(-0.99-0.43)^2 = 18.095897435897434`.

But the two-brick subset `c=-0.91, n=33` and `c=0.43, n=25` gives

`L_better = 33·25/(33+25)·(-0.91-0.43)^2 = 25.540862068965517`,

which is 1.411417265 times the greedy leverage. For any stop threshold between those values, the greedy order fetches at least one unnecessary brick even though a same-cardinality subset already clears the threshold. The mandatory battery contains the old equal-count counterexample but no fixture exposing this new weighted-greedy failure.

**Minimal repair.** Either implement an optimizer that actually solves the frozen subset/cost objective, or amend the design authority openly to permit a specified approximation and freeze a measurable approximation/cost bound. In either case add the fixture above and unequal-count adversarial searches to BS-2p; “optimizer” must not imply global maximization if only a local heuristic is intended.

### 4. BLOCKER — Stage P does not define how the 0.8572 retention bound creates the injected planning sample, and its CP pass threshold is ambiguous

**Quote.** Stage P names eligible-parent per-brick counts and centres plus retention lower bound `0.8572`, then immediately defines Bernoulli signs, 1,000 trials, and a “Clopper–Pearson 95% lower confidence bound” pass rule (lines 95–104). It does not state how retention is applied to integer per-brick counts or whether the CP lower bound is one-sided 95% or the lower endpoint of a central two-sided 95% interval.

**Why this fails.** The retention number alone does not define a planning mask. For a three-brick fixture with `c=[-1,0,1]` and parent counts `[2,3,10]`, independent execution gave:

- fractional weights `0.8572·n`: `N=12.858`, `L=6.629013333333333` — but fractional objects cannot receive Bernoulli signs;
- floor per brick: counts `[1,2,8]`, `N=11`, `L=4.545454545454545`;
- ceil/round per brick: counts `[2,3,9]`, `N=14`, `L=7.5`;
- global floor: `N=12`, with its allocation across bricks still undefined.

All are plausible readings of “retention lower bound 0.8572,” and they change both prefix leverage and injected power. The CP wording also produces two exact pass counts at `n_trials=1000`. Using `Beta^{-1}(0.05; x, 1000-x+1)` for a one-sided 95% lower bound first passes at `x=962` (`LB=0.950487129744074`; `x=961` gives `0.949365993205112`). Using the lower endpoint of a central two-sided 95% CP interval, `Beta^{-1}(0.025; x, 1000-x+1)`, first passes at `x=964` (`LB=0.950507088281988`; `x=963` gives `0.949358876940075`). Thus two standard implementations can produce different `L_min_plan` while both claiming compliance.

**Minimal repair.** Freeze an integer, per-brick retention construction (or a formally defined worst-case optimization over all admissible retained masks), including rounding and tie rules. Freeze the CP formula and alpha explicitly; if the intended rule is one-sided 95%, state `Beta^{-1}(0.05; x, 1001-x) ≥ 0.95`, equivalently at 1,000 trials `x ≥ 962`. Bind the injection and permutation seed schedule in the same pre-freeze mechanism rather than allowing the receipt to choose it after testing prefixes.

### 5. BLOCKER — a single global accuracy does not justify scalar attenuation on the leverage-chosen footprint

**Quote.** Section 3 asserts `E[s_obs|c] = (2a−1)·A_L·c` for “a symmetric classifier with accuracy a,” then corrects by the single global `â` from BS-8f (lines 76–83). BS-8p/f carries the predecessor's machine-state × `|χ|`-tertile hand-check and global `a_LB` machinery, but V3 contains no binding gate that requires accuracy to be constant in `c`, sky position, release, or the accepted-position mask (lines 134–139, 169, 177).

**Why this fails.** Sign-symmetric errors can still have position-dependent accuracy `a(c)`. Then

`E[s_obs|c] = (2a(c)−1)·A_L·c`,

and the centred slope estimates `A_L·Cov(c,(2a(c)−1)c)/Var(c)`, not `(2ā−1)A_L`. A global hand-check average cannot repair that. An executable three-position example satisfying symmetric flips locally used `c=[-1,0.2,1]`, weights `[1,1,4]`, and accuracies `[0.95,0.95,0.80]`. Its population-weighted `ā=0.85`, while `c̄=0.5333333`. For true `A_L=0.0408`, the exact expected centred slope is `0.0298656`, not the scalar model's `0.02856`; division by `2ā−1=0.7` returns `0.04266514285714287`, a +4.5714% amplitude bias. The per-stratum floor cited from HC-1H is 0.70, so the low-accuracy component is not automatically forbidden by the carried rules. The successor's deliberately nonuniform footprint makes this seam load-bearing.

**Minimal repair.** Add a binding accepted-mask calibration gate for accuracy versus `c`/sky and other position-linked covariates, with a prespecified test and failure action. If constancy fails, use a frozen observation/stratum-specific misclassification model in the estimator and power simulation, with uncertainty propagation. Merely reusing the global HC-1H `â` and `a_LB` is insufficient.

### 6. MAJOR — the permutation SE and BS-7 digest still lack byte/numeric canonicalization

**Quote.** Section 3 defines `σ_β` only as the “permutation SE” (line 81). BS-7 asks for the SHA-256 of a “canonical float64 serialization” of the full permutation vector (line 168).

**Why this fails.** The text never selects population versus sample standard deviation (`ddof=0` versus `ddof=1`) for the finite 100,000-vector SE. It also never defines the supposedly canonical serialization's byte order, array order, or exact conversion operation. Native-endian `float64.tobytes()` differs across architectures, and an independently written receipt cannot infer whether “canonical” means little-endian IEEE-754 C-order bytes, a text representation, or another encoding. This can alter `σ_ours` slightly and guarantees digest disagreement across otherwise numerically identical implementations.

**Minimal repair.** Freeze `σ_β = np.std(beta_perm, ddof=<chosen value>)`. Define the digest payload exactly, e.g. the 100,000 values in permutation-index order, converted to contiguous little-endian IEEE-754 binary64 (`<f8`) with no header, then SHA-256 over those 800,000 bytes. Pin finite-value and zero-denominator fail-closed rules.

## Attacks that held

1. **Axis vector.** Independent multiplication by the canonical ICRS↔Galactic rotation gave `(-0.676971771271432, -0.509846551777774, 0.530816083537352)`. Component differences from the printed vector were at most `3.331e-16`; its printed-vector norm squared is `0.9999999999999996`. The implied display coordinates are `(216.984435505215203°, 32.060610901162001°)`. The vector itself is correct to the printed 15 digits, and lines 29–31 clearly make it the sole machine axis while marking both coordinate pairs display-only.
2. **Attenuation delta-method term under the stated scalar model.** For `Â=β/(2a−1)`, independent finite differences gave derivatives `∂Â/∂β=1.42857142855` and `∂Â/∂a=-0.11657142852` at `β=0.02856, a=0.85`, matching the two terms in V3's formula. Finding 5 is the missing validity condition for applying that scalar model, not an algebra error in the displayed derivatives.
3. **Old optimizer counterexample.** For equal counts and `c=[0.99,0.98,-0.50]`, `L([0.99,0.98])=0.00005`, `L([0.99,-0.50])=1.11005`, ratio `22,201`. V3's greedy rule selects `0.99` then `-0.50`, so it repairs that named fixture. Finding 3 is a new unequal-count counterexample.
4. **Plus-one p resolution.** At `n_perm=100,000`, `k=0` gives `p=1/100001=0.000009999900001`; `k=99` gives `0.000999990000100 < 0.001`; `k=100` gives `0.001009989900101 > 0.001`; `k=100000` gives 1. The threshold is non-vacuous and has 100 attainable tail counts below it.
5. **Quotation fidelity attacked.** The Longo amplitude and `σ_pub`, galactic axis, one-sided East-of-North sign, 100,000 permutations, strict F-6 decision regions, `3.09·σ_ours` floor, 0.85 quality floor, 0.8572 retention lower bound, instrument hash prefix, and τ agree with the predecessor. The eight §2 predicates agree in operator and numeric content with BS6-pred; predicate 6 is algebraically restated (`e1²+e2²` versus SQL `POWER(e1,2)+POWER(e2,2)`) rather than byte-identical source syntax. No surface-brightness cut is correctly recorded.
6. **Two-class freeze state.** Classifying BS-6 and the actual-mask/accuracy/final-power receipts as post-freeze class-E gates resolves CODEX V2 finding 6. The remaining cycle in Finding 1 is inside class P and is distinct.
7. **Decision partition.** The §5 p ranges remain mutually exclusive and exhaustive through INCONCLUSIVE, with `p=0.001` and `p=0.05` both INCONCLUSIVE.

## Evidence ledger / executed checks

Content read:

- `BRIEF_GATE_SUCCESSOR_V3.md`
- `../PREREG_SUCCESSOR_DRAFT_V3_20260824.md`
- `GATE_GPT56_SUCCESSOR_V2.md`
- `GATE_CODEX_SUCCESSOR_V2.md`
- `../../SUCCESSOR_SCOPE_20260821.md`
- `../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
- `../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md`
- `../agy/REVIEW_AGY_20260824.md`

Commands/calculations executed:

- SHA-256 commands printed in the custody section.
- Independent Python IAU matrix multiplication, vector norm, and RA/Dec conversion.
- Independent finite-difference check of both delta-method derivatives.
- Exact SciPy beta-quantile evaluation for both CP conventions at every `x=0…1000`.
- Exact plus-one p-value boundary arithmetic at `k=0,99,100,100000`.
- Exhaustive finite weighted-subset comparison and exact weighted-SSE recomputation for the greedy counterexample.
- Independent leverage calculations under fractional, floor-per-brick, ceil/round-per-brick, and global retention readings.
- Exact expectation calculation under a locally sign-symmetric but `c`-dependent accuracy model.
- Targeted repository search for the abbreviated `2df3a220…` inventory reference found no named supporting artifact under the brief's allowed `../../` context; I did not rely on the 1,436-file/1.8-TB numbers for the verdict.

No `/Users/duhokim/NebulaMindData/` path was read. No source artifact was edited. The only lane write is this report.

## Testimony

None. The verdict relies on the pinned text, cited source bytes, and executable calculations above.

**REFUSED** — blocking findings 1–5: the class-P planning cycle persists; the optimizer order lacks pre-order counts; the greedy rule violates the maximize-leverage requirement; Stage P retention and CP semantics are not uniquely executable; and global attenuation is not validly bound on the accepted footprint. Finding 6 is an additional reproducibility defect.
