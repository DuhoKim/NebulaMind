# GAIN CONTROL v4 REVIEW — CODEX

## Verdict

**NOT CLEAR.** The v3 normalisation blocker is repaired: `gamma_hat = slope/intercept` is the parameter of the stated uncentred model, and both values and their covariance come from one pinned GLS fit. There is no residual free `n_b` or count-weighting convention; the only weighting left is the GLS weighting fixed by the supplied `cov_a`. The delta-method Jacobian is correct, the official batteries pass, and the production-relevant domain probes refuse rather than clamp. However, the deliberately open p-gated decision boundaries remain an answer-determining design hole, not a missing numerical fill: perturbing the accepted-sign field can move both `A` and the permutation `p`, while §4 proves invariance only with `p` held fixed. That alone blocks freezing the complete control. I also broke two universal code/test-contract claims with direct inputs: the estimator can raise instead of returning a refusal for finite inputs (so G08 is not unreachable under the declared guards), and the verifier's end-to-end recipe can turn an out-of-domain per-object accuracy field into a value by averaging within bins before sampling.

## Digest comparisons and custody

1. `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`
   - supplied: `47b4ce87bc89d919200081ec0c3d9148cc09000aba8464946dccea394ecc45f6`
   - recomputed with `shasum -a 256`: `47b4ce87bc89d919200081ec0c3d9148cc09000aba8464946dccea394ecc45f6`
   - comparison: **MATCH**, exact 64-hex equality.

2. `../ref/gain_gradient_estimator.py` (NEW)
   - supplied: `287ffe841400fff8462708bc6d423dbdf0ef62fc998f9a52cceaeb8ad488556e`
   - recomputed: `287ffe841400fff8462708bc6d423dbdf0ef62fc998f9a52cceaeb8ad488556e`
   - comparison: **MATCH**, exact 64-hex equality.

3. `verify_mu_gamma.py`
   - supplied: `43243fe73769deee371ee7896e1f917fdb680dd92f0e9f7772047387f8d2efc5`
   - recomputed: `43243fe73769deee371ee7896e1f917fdb680dd92f0e9f7772047387f8d2efc5`
   - comparison: **MATCH**, exact 64-hex equality.

4. Not a subject: `../PREREG_SUCCESSOR_DRAFT_V33_20260828.md`
   - supplied full pin: `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`
   - recomputed: `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`
   - comparison: **MATCH**, byte-identical to the pinned draft.
   - `git status --porcelain` and `git diff --stat HEAD` on the three subjects plus this draft were empty before this report write. The two scripts contain no draft/V33/credit/fill reference; the design mentions `CODEX-V33-1` only as the name of the earlier estimand finding and states `gamma_hat` is UNFILLED. Nothing in this round is credited to, filled into, or adjudicated as part of the unchanged draft.

## Official executions

### Estimator self-test

Ran unmodified:

`python3 ../ref/gain_gradient_estimator.py --self-test`

Exit code `0`. It recovered `gamma = 0, +/-0.2, +/-0.5`; reproduced the old-normalisation predictions (`+0.206541826`, `-0.193859852`, `+0.542995950`) while the fixed estimates were exact; exercised G01--G07; named G08 exempt; and ended:

`self-test: 0 failure(s)`

### Bias/domain/recipe verifier

Ran unmodified:

`python3 verify_mu_gamma.py`

Exit code `0`. All ten in-domain cases were `OK`; all three named domain controls refused; the end-to-end recipe returned:

- `gamma_true=+0.00 -> gamma_hat=+0.0447 +/- 0.0262`
- `gamma_true=+0.20 -> gamma_hat=+0.2326 +/- 0.0245`
- `gamma_true=-0.20 -> gamma_hat=-0.2287 +/- 0.0335`

It ended: `10 in-domain cases, 3 domain controls, 0 failure(s)`.

## Numbered findings

### 1. HIGH / BLOCKS FREEZING — design lines 145--157 and the admitted open item in brief lines 62--69 — p-gated boundaries are not covered by the claimed invariance rule

**Why it fails.** Section 4 varies `A_hat` over `[A_hat-Gamma, A_hat+Gamma]` and checks only amplitude thresholds `T`. The live production decision (`successor_ref_v9.py:1579--1584`) also changes branch at `p < P_REPRODUCED` and `p > P_REJECT_MIN`. `A` and `p` are both functions of the same accepted-sign vector. A gain gradient that perturbs that vector is not shown to leave `p` fixed, nor is its effect on `p` bounded. Therefore completeness of amplitude thresholds cannot establish verdict invariance. This is not merely the absent measured value of `gamma_hat`; it is missing answer-determining content in the rule to be frozen.

**Smallest sufficient repair.** Before freezing, either (a) derive and code a conservative joint perturbation rule for both `A` and `p`, including the two p boundaries, or (b) prove and control that the permitted gain-gradient perturbation cannot cross either p boundary. Enumerate the complete resulting boundary set and its digest pre-result. Merely recording an amplitude-only `T` at filling time is insufficient.

### 2. MEDIUM / BLOCKS THE CLAIMED CODE CONTRACT — estimator lines 87--111 and 139--164 — G08 is not unreachable after the named guards, and a finite input can escape the refusal API by exception

**Why it fails.** The proof of unreachability assumes finite inputs imply finite derived linear algebra. They do not in float64. Direct call:

- `a_hat=[0.8,0.8,0.8]`
- `cov_a=diag(1e308,1e308,1e308)` (all entries finite)
- `c_bar=[-0.9,0,0.9]`

passes G01/G02, overflows at `S = 4*cov_a`, and raises `LinAlgError: Eigenvalues did not converge` at `eigvalsh`; it returns neither a result nor a refusal set. Thus the module-level promise at lines 68--73 and the G08-unreachable claim at lines 159--164 are false over the accepted input surface. Separately, `c_bar=[-2,0,2]` is accepted and returns a value even though bin means of `cos(theta)` must lie in `[-1,1]`; there is no c-domain refusal. These are wrong-input paths, not evidence that normal production values fail.

**Smallest sufficient repair.** Validate `c_bar` in `[-1,1]`; check `S=4*cov_a` for finiteness before eigendecomposition; catch deterministic `numpy.linalg` failures and map them to a pinned refusal code; then either add a real G08 control or narrow and prove its exemption over an explicitly bounded input domain.

### 3. MEDIUM / BLOCKS THE VERIFIER'S UNIVERSAL REFUSAL CLAIM, NOT THE IN-DOMAIN NORMALISATION RESULT — verifier lines 86--108

**Why it fails.** `simulate()` correctly checks every per-object accuracy before sampling, but `recipe_gamma()` does not. It first averages `a_true` within a bin, then passes that mean to `rng.binomial`. On the real retained `c` array, `gamma=0.251, gbar=0.8` produces per-object accuracy range `[0.7996001587, 1.0003957145]`, so the generative field is outside `(0.5,1.0]`. `simulate(c,0,0.251,0.8)` refuses, but `recipe_gamma(c,0.251,0.8)` returns `(0.2655480516, 0.0254813988)`. This is not literal clipping, but it has the prohibited effect: an invalid probability field is silently converted by bin averaging into a valid probability and a numerical result rather than refusal. At `gamma=0.30`, the same helper raises `ValueError` rather than returning a refusal.

The three published recipe controls are in-domain and remain valid; this does not undo their evidence that the intercept normalisation is exercised end to end.

**Smallest sufficient repair.** In `recipe_gamma()`, apply the same per-object accuracy and latent-probability domain checks as `simulate()` before bin averaging; return a named refusal shape rather than a value or raw NumPy exception; add one just-outside-domain recipe control.

### 4. ADVISORY / ONLY BLOCKS FILLING ON THIS LEGITIMATE INPUT — estimator lines 101--111; v9 lines 1446--1489 — G03 refusal is fail-closed and preferable to an unpinned pseudo-inverse

For `agree=[100,100,100]`, `n=[100,100,100]`, `epsilon=0`, `sigma_epsilon=0`, v9's inherited covariance is exactly zero. Passing `a_b=[1,1,1]`, zero `cov_a`, and spanning bin centres to the estimator returns `None` with exact code set `{G03}`. This is a legitimate hand-check outcome, so the gradient control is unrunnable and must remain unfilled/inconclusive on it. Nevertheless, refusal is the correct frozen behavior: substituting a generalized inverse would introduce an unpinned metric and the inherited plug-in zero variance is itself falsely certain at an all-success binomial boundary. This does not by itself block freezing because the failure mode is explicit and fail-closed.

**Smallest sufficient repair if operational continuity is required.** Repair the upstream binomial covariance contract pre-result (for example, a frozen boundary-safe interval/covariance construction) and then feed a positive-definite covariance. Do not weaken G03 with an operator-chosen pseudo-inverse.

## Normalisation and weighting adjudication

The fix fully closes CODEX-GAINV3-1 and the `n_b` ambiguity. In the uncentred model `g_b=theta0+theta1*c_bar_b`, `theta0=g0` and `theta1=g0*gamma`, hence `gamma=theta1/theta0`. Code lines 116--138 use the same GLS solution and joint `cov_theta`; the Jacobian `[-theta1/theta0^2, 1/theta0]` is correct. No population-count or hand-check-count scalar remains. A non-collinear three-point realization can still make the fitted ratio depend on GLS weights, but those weights are not a free convention: they are determined by the supplied full covariance and the pinned Cholesky solve.

## Failed attacks / held claims

- Just-below `a=0.5` and just-above `a=1.0` inputs returned G07, with no clipping.
- The published accuracy-domain and latent-probability controls in `simulate()` all refused, including the new `mu=1.2` case.
- The stated perfect-agreement singular case returned exact G03; no pseudo-inverse or partial value appeared.
- All five noiseless gamma fixtures recovered exactly, and the regression controls numerically distinguish the old sample-mean normalisation from intercept normalisation.
- The three end-to-end in-domain recipe controls genuinely call v9's `calibration_bins()`/`assign_bins()` and the production estimator; none is a hard-coded result.
- I found no residual `n_b` choice in the estimator or receipt fields.

## FREEZING versus FILLING, plainly

The absence of a measured `gamma_hat` is only a **FILLING** condition, and G03 on the legitimate all-perfect fixture is a fail-closed **FILLING** halt. The unresolved p-gated decision boundaries are different: they leave the verdict map itself incomplete and therefore **block FREEZING**. Findings 2 and 3 also require small code-contract repairs before claiming the exact refusal/unreachability battery is frozen as written.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch images, form a science result, fill `gamma_hat`, alter the three subjects, or alter the unchanged V33 draft.
- I read the brief, all three subjects, my pinned gain-v3 report, and the relevant live v9 calibration and decision functions.
- The only durable write is this report.
- BS-6 and the first image byte remain blocked; nothing in this review authorizes either.

**NOT CLEAR**