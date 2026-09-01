AMENDMENT_B_REFUTED

# Claims 1–4

## Claim 1 — FAILS

The narrow algebraic observation is true but the claim about this frozen study is false. `beta_slope()` and a permutation record can be evaluated mathematically without dividing by `2â−1`. The frozen run, however, is expressly not allowed to reach them without calibration. Section 3 says: “The branch predicate (after BS-8f, before any real statistic …) first checks the calibration floor: any `a_LB_b < 0.85` emits an immediate pre-unblinding `INCONCLUSIVE-BY-CALIBRATION` and halts.” Section 4 repeats: “Before running Stage C, the measured calibration bound must be checked” and only if every bin passes “may Stage C run.” Section 5 further requires the production runner to “refuse before forming any statistic if the adequacy tree emits an `INCONCLUSIVE` result.” With no BS-8f measurement, neither the passing predicate nor the specified calibration-inconclusive predicate can be evaluated. There is no frozen calibration-free decision path and no frozen detection-class verdict.

## Claim 2 — FAILS

Changing the axis changes more than a column supplied to an otherwise applicable frozen test. Section 1 binds the scientific claim: “This tests that published amplitude at that published axis” and “Fixed-axis. The machine axis is the `AXIS` constant.” The footprint, quality/systematics characterization, power gates, calibration strata, permutation receipts, sign direction, and decision regions are all tied to that axis and to a Longo-amplitude question. A CMB axis therefore requires a new estimand, axis/sign convention, geometry receipt, power evaluation, systematics controls, and detection decision rule. Reusing the slope formula does not make those frozen commitments axis-invariant.

## Claim 3 — FAILS

The machine committee can mechanically emit signs, but that does not remove the inferential blocker. The estimand is conditional: “A sign-symmetric classifier of accuracy a gives `E[s_obs|c] = (2a−1)·A_L·c`.” Unknown machine accuracy means the link from observed slope to a sky modulation is not established; position-dependent response is worse. The draft explicitly says that a classifier responding to position-varying sensitivity “can produce a dipole-like slope under a null sky” and that antisymmetry “does not measure sky-position dependence.” BS-3g models exactly this route as `a(c) = a₀ + γ·(c−c̄)`, and its row says “γ̂ remains unmeasured.” Thus a nonzero machine-only β̂ is not uniquely attributable to a handedness field. Replacing missing human calibration with an uncalibrated committee changes an amplitude-identification failure into an uncontrolled false-detection problem.

## Claim 4 — FAILS

The leverage arithmetic is partly right, but the noise and resulting detectability conclusion are wrong.

The frozen exact relation is `Var(β̂) = Var_pop(s)/((N−1)·Var_pop(c))`. With sign labels and a near-balanced null, `Var_pop(s) ≈ 1`. Since the document defines `N_eq = 3·N·Var(c)`, this gives `σ_β ≈ √(3/N_eq)`, not `1/√N_eq`. Consequently

`σ_A ≈ √3 / ((2a−1)√N_eq)`.

At `N_eq = 110,983` and `a = 0.85`, this is about 0.00743, not 0.00429. The proposed 0.00429 follows its erroneous formula. The apparent agreement with BATTERY-POS's p-value does not validate that formula; 0.04243/0.00429 = 9.9 while the receipt is about 9.5σ, whereas the variance identity depends on the actual `Var_pop(s)` and permutation distribution and must be used directly.

The stated axisymmetric leverage formula is algebraically correct only under its assumptions. Using rounded `Var(c)=0.7517` gives `N_eq` approximately 110,976, 64,652, and 18,329 at 0°, 45°, and 90°, respectively; the frozen 110,983 uses more precise geometry. But the quoted “3σ floors” inherit the missing √3. At `a=0.85`, the approximate correct 3σ amplitude thresholds are 2.23%, 2.92%, and 5.48%, not 1.29%, 1.69%, and 3.17%. A 4.08% signal therefore is not a 3σ detection at the claimed worst-axis geometry. Moreover, azimuthal and north/south symmetry about Longo's axis is an unsupported approximation for the actual DR10-south mask. The new axis's `Var(c')`, mean, tails, quality correlations, and effective power must be calculated from the locked object positions, not inferred from ψ alone.

# A1–A5

## A1 — Frozen decision path

Refutation holds. Raw β̂ and an abstract permutation p-value do not require â, but this preregistration forbids their production before the BS-8f calibration gate. Missing â does not validly produce `INCONCLUSIVE-BY-CALIBRATION`; the specified comparison requires a measured, validated `a_LB_b`. It instead leaves a required allocated calibration output absent (with the document separately naming `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT`) and supplies no authority to run a new detection path. A new path cannot be smuggled in as an interpretation of the frozen one.

## A2 — Machine-only estimand and BS-3g

Refutation holds. Exact mirror antisymmetry closes a spatially uniform parity-even preference, not upstream chirality, non-equivariant selection, or position-varying sensitivity. Under the draft's own warning, an unmeasured γ can manufacture an axis-correlated slope under a null sky. A permutation of observed signs over fixed positions tests exchangeability; it does not distinguish celestial modulation from a fixed instrumental position dependence. No detection-class scientific claim is supportable until the relevant position-dependent response is bounded on the new axis and the bound is incorporated into the null/decision rule. BS-3g is unfilled and γ̂ is unmeasured, so that prerequisite is absent.

## A3 — Power and footprint

Refutation holds. `N_eq = 3N Var(c)` and the conditional leverage formula are reproduced, subject to rounding, but `σ_β = 1/√N_eq` is inconsistent with the frozen exact variance for ±1 signs by a factor √3. The resulting amplitude floors and “Longo-scale stays detectable” conclusion fail. Independently, rotational symmetry is not established for a southern, quality-cut footprint; actual locked-position geometry and Monte Carlo/permutation power on the CMB axis are mandatory.

## A4 — Integrity

This is a post-failure scientific pivot, not a minimal amendment to the signed Longo-amplitude preregistration. The original study bound the Longo axis, Longo sign, amplitude comparisons, calibration gate, and verdict vocabulary. After learning that its required calibration cannot be obtained, the proposal changes both the axis and the claim class to preserve a runnable result. Choosing the CMB axis from independent data before reading handedness reduces outcome-driven axis selection, but it does not make the new question part of the old signed promise. A referee could accept it as a separately frozen successor study with full disclosure; presenting it as amendment B to rescue the closed stage would defeat the preregistration's integrity function.

## A5 — Additional fatal defects

1. No unique CMB axis is specified. “Hemispherical power-asymmetry / low-ℓ alignment axis” denotes multiple literature choices, coordinate conventions, antipodes, and uncertainty treatments. The oriented sign and one- versus two-sided alternative are likewise unbound.
2. The frozen p-value is “one-sided … at Longo's oriented sign.” It is not a generic existence-of-modulation test. A detection question normally needs a precommitted orientation or a two-sided rule and corresponding threshold.
3. The frozen decision helper has no detection-class outcome. Its numeric regions are `REPRODUCED-LONGO`, `REJECTED-AT-LONGO-AMPLITUDE`, and `INCONCLUSIVE`, all involving Â, its calibration uncertainty, or Longo's amplitude. A small p-value alone is not a frozen verdict.
4. The existing power gates were injected at floor `a=0.85` and evaluated for the frozen geometry. Unknown accuracy prevents their reuse; the actual CMB-axis mask can also fail the `N_eq ≥ 100,000` requirement.
5. The draft documents strong position–quality coupling on the frozen axis (`corr(psfsize_r, cos θ)=+0.4188` after cuts). Its projection on the proposed axis is unknown. This makes an axis-specific systematics analysis substantive, not clerical.
6. Acquired bricks are only transport inputs. Acquisition does not authorize cutouts, χ inference, handedness labels, or the proposed analysis, so it supplies no operational shortcut.

# Minimum preconditions for ratification

There is no defensible ratification of amendment B as a modification of the signed Longo study. The minimum conditions below apply only to a separately identified, prospectively frozen successor preregistration, with the original study and its closure left intact:

1. Disclose the pivot and register it as a new study before any χ, committee sign, handedness label, or result is accessed.
2. Pin one exact published CMB axis, frame, epoch, numerical coordinates, antipode/orientation convention, source/version, and rationale; bind whether the test is one- or two-sided and address axis uncertainty and any multiplicity across CMB-axis definitions.
3. Compute and freeze `c'`, its mean and variance, `N_eq`, leverage/tail coverage, quality correlations, and calibration strata directly on the locked 49,211-object mask. Do not use the azimuthal approximation as evidence.
4. Define a detection estimand and a detection-only verdict vocabulary, including null, permutation/exchangeability assumptions, p threshold, effect-size reporting, stopping/halting rules, and treatment of unknown sign dilution. Build and gate a production runner for that path; do not reuse the Longo numeric helper by relabeling its output.
5. Establish the machine committee's absolute sign anchor, sign symmetry, nondegenerate accuracy, uncertainty, and relevant position dependence on accepted real-population objects. If humans remain necessary to establish those properties, the claimed removal of the panel blocker is false.
6. Measure and bound axis-relevant γ or an equivalently strong spatial-response model, fill and pass an axis-appropriate BS-3g-style control, and propagate the bound through the full permutation decision. Only a precommitted `HELD` result may permit inference.
7. Rerun Stage P and Stage C on the exact new-axis geometry using the actual sign variance and full permutation machinery. Demonstrate prospective power at a precommitted scientifically relevant observed-slope effect; use `σ_β² = Var_pop(s)/((N−1)Var_pop(c'))`, not the refuted `1/N_eq` shortcut.
8. Re-evaluate upstream chirality, selection non-equivariance, seeing/depth/coverage gradients, and conditional handedness-selection assumptions specifically for the new axis and bind failure consequences before inference.
9. Obtain fresh authorization for cutouts and instrument inference, complete all required design/build/verification slots, receive independent adversarial review, and freeze/sign the successor protocol before touching handedness-bearing bytes.

Until all of those conditions are prospectively satisfied, the proposed detection is neither a valid output of the frozen study nor an identified instrumental detection in a new one.
