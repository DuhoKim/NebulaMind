# V32 WHOLE-DOCUMENT REFEREE REVIEW — GPT56

## Verdict

**NOT CLEAR.** V32 exactly matches the dispatched SHA-256, the V31→V32 delta is confined to the four dispatched regions, my V31 blocker is genuinely answered, the antisymmetry refutation is algebraically and operationally correct for the deployed pure-index mirror, the new catalogue decomposition reproduces, and all required checker invocations exit 0. The new gain-gradient control does not yet define one executable acceptance statistic: it says the decision reads a two-hemisphere contrast while its estimator and inequality read a continuous quality slope; its `0.011` tolerance cannot support the claim that a passing systematic “cannot flip the verdict”; and its one-dimensional seeing propagation does not bound the broader image-quality route it claims to bound. The `|μ|_max=0.10` point comparisons are numerically true but not a defensible “generous” ceiling, and the claimed stronger blindness is false as written because the inputs contain real DR10 sky backgrounds. These are design defects in the newly assigned control, not evidence that any bound has already been measured. V32 itself remains honest that the control is DESIGN, UNFILLED and that BS-6 remains blocked.

## Exact subject and predecessor comparison

I recomputed both digests from the current bytes:

- V32 supplied: `02a922167bcb77082a72ef0b3da0642975c39c7fef4ebd75ca28fd8d8a708e95`
- V32 recomputed: `02a922167bcb77082a72ef0b3da0642975c39c7fef4ebd75ca28fd8d8a708e95`
- V32 comparison: **MATCH**, exact 64-hex equality.
- V31 supplied: `ce1b6914eae0d36b38d5fc77bb0a8d17c3502d4a007611ad39efe7fe78f1349c`
- V31 recomputed: `ce1b6914eae0d36b38d5fc77bb0a8d17c3502d4a007611ad39efe7fe78f1349c`
- V31 comparison: **MATCH**, exact 64-hex equality.

The direct unified diff contains exactly four semantic regions: (1) V31→V32 retitle; (2) replacement of §1 line 120; (3) insertion of the new §2.7 paragraph at V32 line 390; and (4) addition of the V30→V31 row in §10. No other byte region changed.

I judged that delta and then reread all 883 lines of V32. The §1 scope block remains at lines 131–133 and is byte-identical to V30: both slices have SHA-256 `51d738df155f2d3a8ecbbc53aeb3ae7fa0f9a2b0957a56535fda34528156d8bc`. V32 line 384 is still at line 384 and byte-identical to V30 line 384: both line bytes have SHA-256 `69cca2922ea7470a8241288050eb6d7b985994099cd43133422f5aee5a296746`.

## Delta judgement: my V31 blocker is answered

My V31 report faulted the old line 120 for treating BS-3's `antisymmetry_receipt` as a measurement of a position-dependent component and for smuggling back an invalid scale comparison through “modest” and “both percent-level.” V32 removes all three claims. Its replacement says the Galaxy Zoo number motivates architecture rather than calibration, says no cross-metric ratio is available, identifies the antisymmetry receipt as an implementation check of an identity, expressly says it does **not** measure sky-position dependence, and labels the surviving explicit control DESIGN, UNFILLED. That is a refutation of the proposed stratified-`d` repair, not a retreat from a needed empirical bound.

The refutation holds:

1. With `M` an involution and `χ(x)=[w(x)-w(Mx)]/2`, `χ(Mx)=[w(Mx)-w(MMx)]/2=[w(Mx)-w(x)]/2=-χ(x)`. Therefore `d(x)=χ(x)+χ(Mx)=0` identically for every deterministic `w` and input raster.
2. `paper/PAPER_DRAFT_SPIN_INSTRUMENT_20260812.md` lines 75–85 defines `mirror` as `np.fliplr`, pure index reversal with no resampling, and records exact antisymmetry. Its §3.1 lines 133–146 distinguishes the deliberately wrong interpolating reflection, for which `M(Mx) != x` and the residual is 0.058–0.944.
3. The feasibility implementation `spike/yui_identity/w_chi.py` lines 27–30 returns `np.fliplr(x)`. The deployed inference runner `_inference_20260820/inference_runner.py` lines 191–203 returns `torch.flip(..., dims=[2])` and computes the shared-model difference with `torch.flip(..., dims=[3])`. Both are index reversal, not affine/WCS interpolation. The interpolating canary is a deliberate substitution, not a reachable branch of these mirror functions. Upstream survey resampling can create route (a) but cannot make this internal `d` nonzero while the deployed `M` remains an involution.
4. The V32 paragraph still has legitimate motivation: the human-bias example explains why a uniform preference must not be trusted away; the antisymmetric architecture cancels its parity-even component; and the paragraph immediately names the distinct surviving threats. It does not under-claim by refusing to use the Galaxy Zoo scale as a calibration.

## Numbered findings

### 1. HIGH / BLOCKING — gain-control lines 88–102 and 116–124 — the frozen statistic and frozen decision rule name incompatible observables

**Why it fails.** Lines 90–96 define the statistic as weighted least squares of recovered fractional gain on normalized `psfsize_r`, producing `β̂` and `σ_β`. Lines 116–124 then accept on `|μ|_max (|β̂|+1.96σ_β) K <= 0.011`. But lines 98–102 separately say the **headline and acceptance decision read the two-hemisphere contrast**, not an eight-bin fit. No formula converts that contrast into `β̂`, no uncertainty for the contrast is defined, and the acceptance inequality never consumes it. Conversely, if the continuous gain-on-quality slope is the decision statistic, the hemisphere contrast is descriptive and cannot truthfully be called what the acceptance decision reads.

The missing details are answer-determining rather than clerical: the number and allocation of backgrounds/injections, whether quality support is balanced within hemisphere or follows the retained joint distribution, the WLS weights, intercept treatment, repeated-injection/background clustering, injection-amplitude and morphology grid, and the covariance estimator can all move `β̂` or `σ_β`. “Frozen and non-tunable” bin labels do not freeze those freedoms.

**Smallest sufficient repair.** Choose one decision path and delete the other claim. The smaller repair is to make the continuous pre-frozen `β̂ K` propagation the sole acceptance statistic; label both hemisphere and eight-bin displays diagnostic-only. Freeze the injection/background allocation, amplitude/morphology support, normalization, WLS design matrix including intercept, weights, dependence unit, covariance construction, and exact receipt fields. Alternatively, define a direct hemisphere-contrast estimator and a separate acceptance threshold derived for that estimator, without also calling `β̂ K` the decision.

### 2. HIGH / BLOCKING — gain-control lines 116–128 — `0.011` is an external tolerance, not proof that a passing systematic cannot flip this study's verdict

**Why it fails.** The arithmetic is reproducible: with the frozen constants, `0.011/(0.10*0.483014)=0.227736670`, so the printed `0.2277` is correct. The logical claim at lines 120–122 is not. Any nonzero nuisance shift can change an outcome arbitrarily close to a decision boundary. This study's outcomes depend on its own permutation `p`, sign, detection floor, amplitude band, and rejection upper limit; none is invariant to an additive spurious amplitude merely because that amplitude is smaller than Longo's published `1σ`. A possible `0.011` shift is also about 27% of the tested `0.0408` amplitude. The external anchor may be a policy tolerance, but it does not imply “cannot flip the verdict at the tested amplitude.”

The rule also assumes the normal-WLS expression `|β̂|+1.96σ_β` is a valid magnitude bound without freezing or validating the sampling/covariance model noted in Finding 1. The propagation equation should use `|K|`; the current selected `K` happens to be positive, but the same design prints a negative `K(flux_ivar_r)` and states a general absolute bound.

**Smallest sufficient repair.** Remove the no-flip claim. Either call `0.011` an explicitly chosen external tolerance with no invariance guarantee, or incorporate the systematic interval into the actual decision function: require the same outcome for every signed nuisance shift in the frozen bound, otherwise emit a named inconclusive result. Freeze and validate the confidence construction, and write the propagation as `|μ| |β| |K|`.

### 3. HIGH / BLOCKING — gain-control lines 30–44, 70–96 and 104–145 — a univariate seeing slope does not bound the full route (b) claimed by the design

**Why it fails.** The design correctly says sensitivity is gain and image quality tracks the axis. It injects across both `psfsize_r` and `flux_ivar_r`, and it reports `K(psfsize_r)=+0.483014` and `K(flux_ivar_r)=-0.270181`. It then fits only one `s`, defined at line 72 as normalized `psfsize_r`, and accepts only with the seeing kernel. Gain dependence on flux inverse variance, their joint/correlated response, `nobs_r`, or another position-coupled background property is not bounded by that inequality. A univariate slope on whatever joint distribution the non-sample backgrounds happen to have can absorb confounding differently from the retained study sample.

Thus the narrow statement “this bounds the psfsize-mediated part of route (b)” could be true after Findings 1–2 are repaired. The current table and prose instead mark route (b) simply “yes — this is the target” and say the control bounds one route by which a violation reaches the estimator. That exceeds the statistic.

**Smallest sufficient repair.** Either narrow the claim everywhere to the seeing-mediated linear first-order component, leaving the rest of route (b) open, or freeze a multivariate gain model and vector propagation `γ = β^T K` (including covariance, interactions/nonlinearity diagnostics, support and extrapolation refusal) over every quality variable the acceptance rule claims to cover.

### 4. HIGH / BLOCKING — gain-control lines 104–128 and 146–148 — `|μ|_max=0.10` exceeds two point estimates but is not established as a conservative ceiling, and its fallback is not executable

**Why it fails.** Both cited point comparisons check out:

- Land's superclean counts `(Z,S)=(6106,7034)` give normalized asymmetry `(S-Z)/(S+Z)=0.070624049`.
- The lane record gives 3,290 versus 3,618 paired flips; `2(3618-3290)/(3618+3290)=0.094962362`, matching `≈0.095`, with the record's `SE≈0.024`.

But `0.10` exceeds the latter point estimate by only 5.305%. Using the stated standard error gives an approximate 95% upper value `0.142`, so “generous” is not supported even relative to that proxy's uncertainty. More fundamentally, both proxies are human-label statistics from GZ1, one of them explicitly `FRAME_UNSTATED` and uncitable as a sky quantity. They do not bound the accepted ±1 output monopole of this automated instrument on this study population. Architectural cancellation of a parity-even instrument offset does not bound genuine population asymmetry or route (a), which the design itself says remain possible.

Lines 146–148 admit the value is assumed and say that if the realized monopole exceeds it, the bound “must be recomputed with the measured value before any verdict is read.” That is not yet an executable rule: `μ` is not operationally defined (raw continuous `χ` versus accepted sign mean), its population, producer, phase, authenticated receipt, and exact branch consequence are absent. A post-unblinding operator must not get to decide how to perform the recomputation after seeing an aggregate outcome.

**Smallest sufficient repair.** Define `μ` exactly on the same accepted sign population used by the estimator; bind an automated post-unblinding producer and receipt before any result display; and state the deterministic consequence. For example, use `max(0.10, |μ_obs|)` in the already-frozen nuisance formula and emit `INCONCLUSIVE-BY-SENSITIVITY-GRADIENT` if the resulting bound fails, with no human-visible intermediate and no recalibration. Do not call `0.10` empirically generous; call it an assumed pre-unblinding working ceiling backed only by the two disclosed point comparisons.

### 5. MEDIUM / BLOCKING — gain-control lines 90–95 and 130–135 — the stronger blindness claim confuses “non-sample” with “no real sky”

**Why it fails.** The inputs are synthetic spirals injected into **real non-sample DR10 cutout backgrounds**. The real sky is therefore not “simply absent.” A background can contain real galaxies or structure, and unless the statistic uses a paired construction that cancels the unchanged background, the recovered amplitude can contain a real-background contribution. Exact exclusion from the 49,211-object mask establishes non-overlap with the analyzed mask, not synthetic-only input and not absence of all real `χ` from the composite raster.

The defensible blindness claim is narrower and still useful: no study-sample `χ` and no study verdict enter; the injection's amplitude/handedness is known; the quality–position kernel is catalogue-only; and exact key exclusion can make the control outcome-blind with respect to this study. That is not the same as the text's stronger “real sky absent” proof.

**Smallest sufficient repair.** Replace “real sky is simply absent” with the exact study-outcome blindness claim. Define a same-background paired ±handedness or injected-minus-uninjected recovery statistic that cancels background chirality, or require and receipt a background-screening rule sufficient to justify “no real `χ` enters.” Freeze the non-overlap universe and exact-key check in the receipt.

### 6. LOW / NON-BLOCKING — V32 §2.7 line 390, final sentence — the conditional-independence qualifier ends with one ambiguous overreach

**Why it fails.** The paragraph correctly says the coupling is seeing-to-position, `χ` is unread, and the result is not evidence of dependence on handedness. Its final clause nevertheless says the assumption of conditional independence “no longer rests on nothing.” The measured marginal seeing–position coupling makes a sensitivity-gradient failure more consequential, but it supplies no evidence about `selection ⟂ handedness | position`; the preceding sentence has just said so.

**Smallest sufficient repair.** Say that the assumption remains untested, while the measured position coupling raises the consequence of a violation and motivates the separate sensitivity control. The existing explicit ban on revisiting thresholds is clear and should remain unchanged.

## Independent catalogue and kernel recomputation

`python3 ref/gain_gradient_kernel.py` exited 0 and reported:

- retained `N=49,211`
- parent correlation `+0.3659`
- retained correlation `+0.4188`
- `Var(cos theta)=0.751761`
- `K(psfsize_r)=+0.483014`
- hemisphere delta `+0.8104 sigma`, `n+=20,063`, `n-=29,148`

Its `--self-test` exited 0:

- baseline `K=+0.483014`
- axis reversed `K=-0.483014`
- unnormalised quality `K=+0.059666`
- shuffled quality–position pairing `K=+0.001795`, which collapses to the stated near-zero null
- v9 freeze intact; 4 controls, 0 failures

I also recomputed the quantities without calling the module's `kernel()` helper, using centered sums on the digest-verified joined rows:

- parent: `N=65,060`, `corr=+0.36588135`, `sd(psfsize_r)=0.17601798`
- retained: `N=49,211`, `corr=+0.41879299`, `Var(c)=0.751761351`, `K=+0.483013647`
- excluded: `N=15,849`, `corr=+0.09636540`
- `flux_ivar_r`/`nobs_r` only retained: `N=53,161`, `corr=+0.43861896`
- those two criteria removed: `N=11,899`, `corr=+0.05889925`, `sd(psfsize_r)=0.23516696`

This independently confirms every number in V32's new §2.7 decomposition to its displayed precision, including the claimed wider spread in the population removed by the depth/coverage criteria. The range-restriction attack therefore fails.

## Required tool executions

All four required checks were run against the exact V32 bytes.

1. `python3 tools/prereg_lint.py <V32> --gates <gates>` — exit **0**:
   - `§7 data rows: 23 (15 class P, 8 class E) — 22 carry a BS- identifier`
   - `no inconsistencies found (all 6 checks demonstrated they can fail)`
2. `python3 tools/prereg_lint.py <V32> --gates <gates> --self-test` — exit **0**:
   - all six controls `OK`
   - `self-test: 6 controls, 0 failure(s)`
3. `python3 tools/prereg_trace.py <build-root> --check <V32>` — exit **0**:
   - `31 computed transition(s); 0 problem(s)`
4. `python3 tools/prereg_trace.py <build-root> --check <V32> --self-test` — exit **0**:
   - in-band removal detection `OK`
   - V31→V32 current-transition sidecar `OK`
   - synthetic V33 out-of-scope rule `OK`
   - `self-test: 3 scope rules, 0 failure(s)`

Passing these checks establishes their implemented contracts; it does not resolve the semantic and statistical design findings above.

## Failed attacks and held boundaries

1. **Subject substitution — failed.** V31 and V32 both match their supplied full SHA-256 pins.
2. **Hidden delta — failed.** The direct diff contains only the four dispatched semantic regions.
3. **Antisymmetry refutation — held.** The algebra is exact for an involutive deterministic mirror, and both inspected implementations use pure index reversal. The interpolating 0.058–0.944 canary is not a deployed mirror branch.
4. **Prior-blocker persistence — failed.** V32 no longer credits BS-3 with a measured position-dependent bound and no longer uses “modest,” “both percent-level,” or “not realistic.”
5. **Motivation deletion — failed.** Line 120 still motivates the architecture and names the surviving threats without using the human-bias number as calibration.
6. **Catalogue decomposition — held.** Every displayed correlation, count, variance, hemisphere contrast and spread reproduces; the flux/nobs-only decomposition defeats the simple truncation explanation.
7. **Post-hoc threshold invitation — failed.** V32 explicitly says the predicate is frozen and that revisiting it after measuring the systematic would be the prohibited post-hoc selection.
8. **Produced-bound over-credit — failed.** Both V32 and the control design say `β` is unmeasured and the control is DESIGN, defined, UNFILLED.
9. **Route-scope concealment — partly failed.** The design explicitly says it does not close conditional independence and does not cover routes (a) or (c). Finding 3 concerns overbreadth *within* route (b), not concealment of those other routes.
10. **Unfinished-programme overclaim — failed.** The whole-document reread still states: BS-2a DESIGN/UNFILLED; one of fifteen class-P slots filled; BS-2v UNRESOLVED; findings 1, 2, 2b and 3 UNRESOLVED; Rows C2 and E unable to run; Stage P superseded for the 49,211 mask; BS-5p unfillable pending rerun; and BS-6 plus the first study image byte blocked.
11. **Scope drift — failed.** The V30 scope bytes remain unchanged in content and position; V32 still tests Longo's published amplitude at his fixed axis and does not test Shamir, BHU or isotropy.
12. **Mechanical trace failure — failed.** Lint, lint self-test, trace check and trace self-test all exit 0.

## Testimony, limits and evidence ledger

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch or authorize any study image byte, run real-data inference, execute Stage P, unblind anything, or modify either preregistration draft or the control design.
- Claims about historical authorization, prior custody and whether any image byte has ever been fetched remain **Testimony** except where this report verifies current bytes or code. The principal-authorization quotation in the design is Testimony.
- I inspected content from: `BRIEF_V32_REVIEW.md`; V32; V31; `V31_WHOLE_REVIEW_GPT56.md`; `V30_WHOLE_REVIEW_GPT56.md`; `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`; `MIRROR_TEST_DESIGN_20260828.md`; `ref/gain_gradient_kernel.py`; `ref/bs2a_quality_gate.py` relevant predicate/schema regions; `ref/successor_ref_v9.py` relevant AXIS/schema/statistic regions; `paper/PAPER_DRAFT_SPIN_INSTRUMENT_20260812.md`; `paper/RECORD_SPIN_PROGRAM_20260812.md` R1; `spike/yui_identity/w_chi.py`; and `_inference_20260820/inference_runner.py` relevant mirror/inference regions.
- I listed/searched filenames and symbols within the assigned handoff and repository to locate the above sources. I did not open secret, credential, `.env`, token or key contents.
- Commands run included: `shasum -a 256` on V31/V32; direct `diff -u`; byte-slice SHA/equality checks against V30; the kernel report and self-test; an independent NumPy centered-sum recomputation; the four required lint/trace commands; arithmetic recomputation of the Land and GZ1 point statistics and the `β` ceiling; and read-only git lookup used to locate the cited paper path.
- The only intended artifact write by this seat is this report.

**NOT CLEAR**