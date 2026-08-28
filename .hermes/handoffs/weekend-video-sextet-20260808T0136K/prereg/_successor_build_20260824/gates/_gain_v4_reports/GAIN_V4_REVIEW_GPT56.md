# GAIN CONTROL V4 REVIEW — GPT56

## Verdict

**NOT CLEAR.** The normalization repair is correct: `gamma_hat = slope/intercept` estimates the `gamma` in the uncentred model, and it removes `n_b` from the statistic. The required executions pass. But the deliberately deferred completeness of `T`, including the unaddressed p-gated decision boundaries, remains an answer-determining post-data freedom and therefore still blocks **FREEZING**, not merely filling. I also found that the new estimator is not total over inputs that pass G01/G03/G05/G06: legitimate finite, in-range, distinct but nearly coincident bin centres can reach an uncaught `LinAlgError` rather than a refusal. Separately, `verify_mu_gamma.py` can silently saturate instead of refuse NaN parameters. The absence of a measured `gamma_hat` would block only **FILLING** after the freeze defects are repaired.

## Exact subjects and digest comparisons

1. `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`
   - supplied SHA-256: `47b4ce87bc89d919200081ec0c3d9148cc09000aba8464946dccea394ecc45f6`
   - recomputed SHA-256: `47b4ce87bc89d919200081ec0c3d9148cc09000aba8464946dccea394ecc45f6`
   - comparison: **MATCH**, exact 64-hex equality.

2. `../ref/gain_gradient_estimator.py` (NEW)
   - supplied SHA-256: `287ffe841400fff8462708bc6d423dbdf0ef62fc998f9a52cceaeb8ad488556e`
   - recomputed SHA-256: `287ffe841400fff8462708bc6d423dbdf0ef62fc998f9a52cceaeb8ad488556e`
   - comparison: **MATCH**, exact 64-hex equality.

3. `verify_mu_gamma.py`
   - supplied SHA-256: `43243fe73769deee371ee7896e1f917fdb680dd92f0e9f7772047387f8d2efc5`
   - recomputed SHA-256: `43243fe73769deee371ee7896e1f917fdb680dd92f0e9f7772047387f8d2efc5`
   - comparison: **MATCH**, exact 64-hex equality.

4. Unchanged, out-of-scope `../PREREG_SUCCESSOR_DRAFT_V33_20260828.md`
   - supplied prior SHA-256: `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`
   - recomputed SHA-256: `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`
   - comparison: **MATCH**. It is byte-identical to the pinned V33 bytes cleared previously.
   - credit audit: V33 is not a subject and receives no credit for any v4 repair. Its bytes remain unchanged and still describe the relevant design/implementation state as unresolved or DESIGN/UNFILLED.

## Numbered findings

### 1. HIGH / BLOCKING FREEZE — design lines 145–157 — `T` is still not complete and p-gated decision boundaries remain outside the frozen rule

**Why it fails.** The rule is exact only conditional on `T` being the complete breakpoint set of the production verdict. The design names categories and says a future receipt will enumerate `T` and its digest, but it does not freeze executable derivation of the complete set from every production predicate. The brief expressly confirms that completeness and the p-gated boundaries were not fixed this round. A future receipt can authenticate a supplied set; it cannot establish that no omitted production branch changes verdict inside `[A_hat-Gamma, A_hat+Gamma]`. Because membership of a missing breakpoint can change whether the result is forced to `INCONCLUSIVE-BY-SENSITIVITY-GRADIENT`, this leaves answer-determining freedom after the proposed freeze.

**Smallest sufficient repair.** Freeze and digest-bind one executable breakpoint producer/checker tied to the exact production verdict function. It must enumerate every active amplitude and p-gated boundary for the selected scalar/profile branch, canonically serialize `T`, and prove branch completeness with controls for reproduction, rejection, sign, floor, inactive/active p gates, coincident boundaries, and equality at both interval endpoints.

This defect alone blocks **FREEZING**. It is not reduced to a filling issue merely because `gamma_hat` is currently unmeasured.

### 2. HIGH / BLOCKING FREEZE — estimator lines 116–140 — accepted near-degenerate designs can crash instead of returning a result or refusal

**Why it fails.** The advertised contract says `estimate_gamma()` returns a result or refusal set and never leaves an operator a solver choice. G05 checks `matrix_rank(X)`, but the code does not rank/condition-check the whitened normal matrix `XtX` before `np.linalg.solve` and `np.linalg.inv` at lines 126–127. I supplied finite accuracies in `(0.5,1]`, a finite positive-definite covariance with condition number 1, and distinct finite bin centres inside the physical `cos(theta)` range:

- `a_hat = [0.8, 0.81, 0.82]`
- `cov_a = diag(1e-20, 1e-20, 1e-20)`
- `c_bar = [1-1e-8, 1, 1+1e-8]`

`matrix_rank(X)` was 2, so G05 did not fire, but `estimate_gamma()` raised `numpy.linalg.LinAlgError: Singular matrix`. The same uncaught exception occurred for separations `5e-9`, `1e-9`, `1e-10`, and `1e-12`. These are legitimate three nonempty positional-bin means, not malformed shapes or non-finite inputs. Thus the eight-code refusal contract is not total, and the statement that the post-G01/G03/G05/G06 path cannot fail is too strong. I did not make G08 itself fire; instead I found an uncovered solver failure before the G08 postcondition.

**Smallest sufficient repair.** Rank- and condition-check the whitened design or `XtX` before solving, with a frozen ceiling and an exact refusal code (either broaden G05 explicitly or add a code). Compute `cov_theta` by a checked solve rather than an unchecked explicit inverse, catch numerical linear-algebra failure into that exact refusal, and add a near-coincident-but-formally-rank-2 control.

### 3. MEDIUM / VERIFIER DEFECT; NOT BY ITSELF THE CORE FREEZE BLOCKER — verifier lines 55–69 — NaN parameters bypass both domain guards and silently saturate comparisons

**Why it fails.** The accuracy and latent-probability checks compare minima/maxima to bounds but do not first require finiteness. With a 1001-point `c` vector in `[-1,1]`:

- `simulate(c, mu=0, gamma=NaN, gbar=0.8, reps=3)` returned the finite value `0.049097608977848484 +/- 0.028789578861566988`, not `(None,None)`.
- `simulate(c, mu=NaN, gamma=0, gbar=0.8, reps=3)` returned `0.019466561382729033 +/- 0.007976051206775879`, not refusal.
- `simulate(c, mu=0, gamma=0, gbar=NaN, reps=3)` returned `(NaN,NaN)`, not refusal.

NumPy comparisons against NaN are false. In the first case `rng.random < (1-a)` is therefore always false, effectively selecting the no-flip branch as if accuracy had saturated at one; in the second, the latent comparison is always false, effectively selecting latent sign `-1`. This is exactly a silent clamp/saturation-shaped behavior rather than refusal.

**Smallest sufficient repair.** Require finite scalar `mu`, `gamma`, and `gbar`, finite `c`, finite `a`, and finite `p_lat` before any bound comparison or random draw. Add NaN controls for each scalar and the vector input.

### 4. ADVISORY / FILL-RUNNABILITY, NOT A FREEZE BLOCKER — estimator lines 101–111 — G03 conservatively refuses legitimate zero-variance calibration outputs

**Why it holds sufficiently for freeze.** I reproduced the named case `agree=[100,100,100]`, `n=[100,100,100]`, `epsilon=0`, `sigma_epsilon=0`: production's `accuracy_from_handcheck()` yields zero covariance, and the new estimator returns `None` with exact code `G03`. A shared-error-only rank-1 covariance also returns G03. Such inputs can represent exact or boundary calibration outcomes, so refusal can make a later fill inconclusive even when an exact algebraic fit might be possible. But it cannot silently create a wrong value, and choosing a generalized inverse after seeing the data would create new freedom. The conservative, predeclared refusal is therefore acceptable for **FREEZING**. If it occurs, it blocks/reroutes **FILLING**; no pseudo-inverse should be introduced ad hoc.

**Smallest sufficient repair if runnability is required.** Pre-freeze a mathematically justified exact-constraint treatment and controls. Otherwise retain G03 and state the resulting run-level inconclusive consequence explicitly.

## Required execution

I ran, rather than accepted testimony for:

1. `python3 ../ref/gain_gradient_estimator.py --self-test`
   - exit code: 0
   - five recovery fixtures: all OK
   - three old-normalization regression fixtures: all OK
   - reachable refusal coverage: 7 of 8 exact codes
   - G08 named exempt/unreachable
   - final result: `self-test: 0 failure(s)`

2. `python3 verify_mu_gamma.py`
   - exit code: 0
   - `N = 49,211`
   - `kappa = +0.005104`; `A*kappa = +0.000208`
   - ten in-domain cases: all OK
   - three shipped domain controls: all refused
   - end-to-end recipe results:
     - `gamma_true=+0.00 -> gamma_hat=+0.0447 +/- 0.0262`
     - `gamma_true=+0.20 -> gamma_hat=+0.2326 +/- 0.0245`
     - `gamma_true=-0.20 -> gamma_hat=-0.2287 +/- 0.0335`
   - final result: `10 in-domain cases, 3 domain controls, 0 failure(s)`

The shipped tests pass, but they do not cover Findings 1–3.

## Failed attacks and held claims

1. **Old sample-mean normalization persistence — failed.** The live estimator returns exactly `gamma` on the noiseless fixtures; the old normalization returns the predicted different values (`+0.206541826` for true `+0.2`, `-0.193859852` for true `-0.2`, and `+0.542995950` for true `+0.5`).
2. **Residual `n_b` normalization ambiguity — failed.** The returned statistic contains no `n_b` or sample-mean denominator. It is slope/intercept from one GLS fit. The point estimate still depends on the supplied `Cov(a)` as GLS necessarily does—I demonstrated `gamma_hat=0.3335126412` under equal covariance and `0.3154077328` when the third point was more precise—but that weighting is data supplied by the pinned BS-8f covariance and code-fixed by the GLS contract, not a free choice among population counts, hand-check allocation, or another `n_b` convention.
3. **Rank-deficient covariance pseudo-inversion — failed.** Rank-0 and rank-1 cases returned only G03; no value or pseudo-inverse appeared.
4. **Shipped accuracy/latent-domain clamp — failed.** All three dispatched out-of-domain controls refused. The successful clamp-shaped attack required NaN, as recorded in Finding 3.
5. **End-to-end recipe still absent — failed.** The verifier calls v9's `calibration_bins()` and `assign_bins()`, constructs three bin accuracies and centres, and calls the production estimator. All three recipe fixtures passed.
6. **G08 directly reachable — not established.** I did not make G08 fire. The stronger totality claim nevertheless failed earlier through an uncaught normal-matrix singularity after the named guards had passed.
7. **Draft mutation or repair credit — failed.** V33 matches its prior full digest exactly and receives no v4 credit here.

## Freeze versus fill ruling

Plain answer: **remaining defects still block FREEZING**. Finding 1 alone is sufficient because the complete verdict boundary set is not frozen. Finding 2 independently leaves estimator failure semantics incomplete. Finding 3 is verifier hardening and is not independently the core design blocker. The deterministic G03 refusal is conservative and affects later runnability/filling, not freeze validity.

After Findings 1 and 2 are repaired, tested, digest-bound, and frozen, the fact that `gamma_hat` is unmeasured would block only **FILLING**. Nothing in this review fills `gamma_hat`, authorizes BS-6, authorizes the first image byte, or changes the standing block on image work.

## Testimony, scope, and evidence ledger

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch or inspect images, run an injection campaign, fill `gamma_hat`, alter any subject, or alter V33.
- I read the governing V4 brief, all three exact subjects, my gain-v3 report, targeted production functions in `successor_ref_v9.py`, and targeted unchanged-V33 passages.
- I recomputed all four SHA-256 values; ran both required test programs; exercised rank-0, rank-1, near-singular covariance, degenerate-centre, near-coincident-centre, and non-finite simulation attacks; and checked normalization/weight dependence directly.
- Assertions about historical authorization, custody, or work not executed here remain **Testimony**. This report establishes current bytes and the executions/comparisons listed above.

**NOT CLEAR**