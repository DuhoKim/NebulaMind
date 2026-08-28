# GAIN CONTROL V3 REVIEW — GPT56

## Verdict

**NOT CLEAR.** The central repair is real: v3 now measures the accepted-sign gain `g_b = 2a_b - 1` from the production calibration rather than a response of `χ`. I independently confirmed that `calibration_bins()` bins the sealed accepted objects by empirical count tertiles of `cos θ`, and that `accuracy_from_handcheck()` returns per-bin corrected accuracies and a covariance matrix with the shared-`epsilon` off-diagonals. However, §3 is still not freezeable. Its normalization estimates a different `γ` from the one used in its bias equation, its GLS/delta-method contract has no executable definition or singular-covariance rule, and its threshold set is left for a later receipt rather than frozen as a closed set now. Those are answer-determining **FREEZING** defects. The absence of measured `γ̂` is separately a **FILLING** state only.

## Exact subjects and digest comparisons

1. `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`
   - supplied SHA-256: `25f6772c39f19b061b171c049cc7b88b48562e8988477060ff8ac9fd31e639b5`
   - recomputed SHA-256: `25f6772c39f19b061b171c049cc7b88b48562e8988477060ff8ac9fd31e639b5`
   - comparison: **MATCH**, exact 64-hex equality.

2. `verify_mu_gamma.py`
   - supplied SHA-256: `43e31c262e205e79ee0157056d8c1bba2910d21b3422abc4b41297abf4c13b71`
   - recomputed SHA-256: `43e31c262e205e79ee0157056d8c1bba2910d21b3422abc4b41297abf4c13b71`
   - comparison: **MATCH**, exact 64-hex equality.

3. Unchanged, out-of-scope draft `../PREREG_SUCCESSOR_DRAFT_V33_20260828.md`
   - supplied prior SHA-256: `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`
   - recomputed SHA-256: `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`
   - comparison: **MATCH**. It is byte-identical to the pinned V33 cleared last round.
   - credit audit: **nothing from v3 is credited to V33**. The draft remains unchanged, still says BS-2a is DESIGN/UNFILLED and the implementation unresolved, and contains no `γ̂`/gain-gradient result or produced bound. This review credits no repair to the draft.

## Numbered findings

### 1. HIGH / BLOCKING FREEZE — design lines 51–70 — `γ̂ = slope / ĝ_bar` is not the `γ` used by the bias equation

**Why it fails.** Lines 54–56 define `ĝ_bar` as the count-weighted sample mean of the three gains and define `γ̂ = slope / ĝ_bar`. Lines 64–70 then use the model

`g(c) = g0 (1 + γ c)`

and the consequence `A + γ(μ + Aκ)`. In that model the regression intercept is `g0` and the slope is `g0 γ`; the sample mean is instead `g0(1 + γ mean(c))`. Therefore the statistic actually defined by lines 54–56 is

`r = slope / sample_mean(g) = γ / (1 + γ mean(c))`,

not `γ`. The distinction is real on the frozen retained geometry: I independently obtained `mean(c) = -0.158387518`. With true `γ = +0.2`, the defined statistic is `r = +0.206542759`; with `γ = -0.2`, it is `r = -0.193859030`; with `γ = +0.5`, it is `r = +0.543002401`. The script does not expose this defect because it simulates with the intercept-normalized input `gbar` and tests the algebra directly; it does not construct `γ̂` by §3's three-bin recipe.

This is the same class of estimand-boundary error as the v2 blocker, now inside the normalization rather than between `χ` and accepted signs. It can move `Γ` and the threshold-crossing result.

**Smallest sufficient repair.** Either (a) fit an intercept and slope by a fully specified GLS and define `γ̂ = slope/intercept`, propagating their joint covariance by an explicit delta-method Jacobian, or (b) redefine the model as centered, `g(c)=g_mean[1+γ(c-mean(c))]`, and rederive the bias equation and verifier for that centered parameterization. Do not mix a sample-mean denominator with the uncentered equation.

### 2. HIGH / BLOCKING FREEZE — design lines 51–60 — the claimed covariance exists, but the GLS and delta-method statistic are not frozen and are not defined for every accepted covariance

**Why it fails.** The premise survives inspection: v9 lines 1359–1370 construct boundaries from sorted accepted-object `c` values at `floor(n/3)` and `floor(2n/3)`, and lines 1446–1489 return `a_b` plus `cov_a`, with off-diagonals `d_eps(i)d_eps(j)sigma_epsilon²`. An ordinary fixture gave a full-rank positive covariance with nonzero off-diagonals.

But `accuracy_from_handcheck()` supplying a covariance does not itself supply a three-point GLS slope. No reviewed production function implements the new slope, intercept convention, inverse/solver, covariance conditioning, delta-method Jacobian, or failure result. Lines 55–57 are prose only. In particular, an input accepted by v9 can yield a singular covariance: `agree=[100,100,100]`, `n=[100,100,100]`, `epsilon=0`, `sigma_epsilon=0` returns `a_b=[1,1,1]` and an all-zero rank-0 `cov_a`; direct inversion fails with `LinAlgError: Singular matrix`. The design states neither refusal nor a pinned generalized-inverse rule. A shared-error-only case can likewise be rank 1.

Thus the answer to the brief's compound claim is: **yes**, the bins are `cos θ` count-tertiles and **yes**, BS-8f supplies a per-bin covariance; **no**, that fact alone does not yet guarantee or freeze a usable three-point GLS statistic.

**Smallest sufficient repair.** Add and digest-bind one production producer/verifier defining the design matrix (including the intercept), stable solver, rank/condition checks, exact refusal outcome, joint coefficient covariance, normalization, delta-method Jacobian, and fixtures for ordinary full-rank, rank-1, rank-0, nearly singular, and non-finite covariance inputs. The receipt must bind these producer bytes and outputs.

### 3. HIGH / BLOCKING FREEZE — design lines 106–118 — completeness of `T` is deferred to a later receipt

**Why it fails.** The exact interval logic is sound only after the complete set of breakpoints is fixed. The design names categories—detection floor, amplitude-band edges, rejection upper limit, sign boundary—but does not enumerate the actual conditional formulas/values in `T`, pin canonical serialization, or provide the claimed completeness checker. It instead says the future receipt “records `T` and its digest.” A receipt can authenticate whichever set a later operator supplies; it cannot prove that the set includes every breakpoint of v9's conditional decision helper.

This is relocated deferral. In v9 lines 1561–1579 and onward, decision boundaries depend on the selected scalar/profile path, `p`, `sigma_beta`, calibration values, `sigma_comb`, the floor, the Longo band, sign, and the rejection inequality. A single control showing that an inserted threshold fires proves interval membership code, not completeness against all branches of the production decision function.

**Smallest sufficient repair.** Freeze an executable function that derives the closed breakpoint set from the exact pinned decision inputs and selected branch, and a verifier that compares its canonical output against all decision predicates in `successor_ref_v9.py`. Bind the code and canonical set schema now, not merely the filled values later. Add branch fixtures for reproduction, rejection, sign, floor, scalar/profile, inactive-`p` branches, coincident boundaries, and equality at both interval ends.

### 4. MEDIUM / VERIFIER DEFECT; NOT THE CORE FREEZE BLOCKER — `verify_mu_gamma.py` lines 54–65 — latent-probability domain is silently clamped

**Why it fails.** The new accuracy-domain refusal at lines 56–58 works for the two shipped controls, but the simulator separately forms latent probability `(1 + μ + A c)/2` at line 62 and never validates it. NumPy's comparison silently behaves as probability 1 above one and probability 0 below zero.

I made the helper return a false result without violating its checked accuracy domain. For `(μ,γ,gbar)=(2.0,0.2,0.8)`, accuracy remains in range, but latent probability spans `1.479600032` to `1.520399129`. `simulate()` returned `0.201192899 ± 0.000516758` while the asserted formula is `0.440841649`; the main tolerance would mark it a mismatch. For `μ=-2.0`, latent probability spans `-0.520399968` to `-0.479600871`, and the same silent saturation occurs in the opposite direction. The shipped ten cases are within the latent domain, so this does not invalidate their reported pass; it refutes the broader claim that the helper refuses all domain violations.

**Smallest sufficient repair.** Before drawing latent signs, compute the complete latent probability vector and refuse unless every value is finite and in `[0,1]`. Add positive- and negative-`μ` domain controls. Also validate finite `c`, `μ`, `γ`, and `gbar` explicitly.

## Required execution

From the build root I ran exactly:

`python3 gates/verify_mu_gamma.py`

It exited 0 and reported:

- `N = 49,211`
- `kappa = +0.005104`
- `A*kappa = +0.000208`
- ten shipped in-domain cases: all `OK`
- two shipped accuracy-domain controls: both refused
- final count: `10 in-domain cases, 2 domain controls, 0 failure(s)`

That execution supports the stated `γμ` behavior for the shipped domain. It does not discriminate the `Aκ` term, does not execute §3's binned GLS estimator, and does not survive the additional latent-domain attack above.

## Failed attacks and held claims

1. **Wrong-estimand persistence — failed.** v3's load-bearing data are accepted-sign accuracies `a_b`; no response of `χ` enters §3.
2. **Calibration-bin misdescription — failed.** `calibration_bins()` really uses the empirical count tertiles of accepted-object `cos θ`, with its documented tie rule and empty-bin refusal.
3. **Missing per-bin covariance — failed.** `accuracy_from_handcheck()` returns `cov_a` with genuine shared-`epsilon` off-diagonals, and BS-8f's schema requires `cov_a`.
4. **Different accuracy from production — failed.** `inject_signs()` consumes the same per-bin `a` indexed by the calibration-bin label, and its gain is algebraically `2a-1`.
5. **Naive-form overclaim persistence — failed.** The design and script explicitly say the simulation cannot distinguish `Aκ` and identify that term as algebraic rather than simulated evidence.
6. **Accuracy clamp in shipped controls — failed.** Both supplied out-of-domain accuracy cases were refused and the script exited 0.
7. **Draft mutation or sidecar credit — failed.** V33 matches its prior pin and contains no produced v3 bound.
8. **v2 subtraction overclaim in the load-bearing path — failed.** §3 no longer depends on injection subtraction. Section 6's balanced-accuracy statement is secondary and expressly unfreezeable; it is not being credited as a frozen result here.

## Freeze versus fill ruling

The remaining defects in Findings 1–3 block **FREEZING**, not merely filling. They leave the parameter normalization, estimator/failure semantics, and decision-breakpoint completeness answer-determining after the proposed freeze. Finding 4 is a verifier-hardening defect and does not by itself kill the algebra for the shipped domain, but it should be repaired before the script is cited as a general domain-safe control.

After Findings 1–3 are repaired, implemented, fixture-tested, digest-bound, and frozen, an unmeasured `γ̂` would block only **FILLING**. Nothing in this review fills `γ̂`, authorizes an image fetch, or changes the standing BS-2a/BS-2v/BS-6 blockers.

## Testimony, scope, and evidence ledger

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch images, run an injection campaign, fill `γ̂`, unblind any result, or edit either subject or V33.
- I read the dispatched brief, both dispatched subjects, my V33 report, the relevant production regions of `ref/successor_ref_v9.py`, and targeted unchanged-V33 passages.
- I recomputed all stated SHA-256 values; ran the required verifier; independently loaded the same frozen `cos θ` geometry; measured `mean(c)`; attacked the latent domain; exercised ordinary and singular `cov_a` cases; and checked the draft for gain-control credit.
- Historical authorization and custody statements remain **Testimony**. This review establishes only the current bytes, code behavior, computations, and comparisons stated above.

**NOT CLEAR**