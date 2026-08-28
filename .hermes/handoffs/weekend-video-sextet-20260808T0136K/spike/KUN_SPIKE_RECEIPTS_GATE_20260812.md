# KUN SPIKE RECEIPTS GATE

Timestamp: 2026-08-12 KST

Targets:

- `spike/YUI_IDENTITY_UNITTEST_RECEIPT_20260812.md`
- `spike/GORU_STATS_RECOVERY_TEST_20260812.md`
- `spike/TORI_PIXEL_PATH_AUDIT_20260812.md`

Binding prior gate: `reviews/KUN_SPIN_DESIGN_BRIEF_GATE_20260812.md`

## Verdict

PASS FEASIBILITY SPIKE WITH HARD FREEZE CONDITIONS.

The three receipts together establish that the design is technically feasible in the narrow sense authorized by the prior gate: synthetic identity works, the fixed-axis statistic/power machinery behaves on simulated catalogues, and the FITS/WCS pixel-path audit can detect the silent row-flip failure mode.

They do **not** establish a frozen preregistration, and they do **not** authorize an empirical sky run.

## Boundary Gate

PASS. I found no empirical sky run.

What I checked:

- `spike/yui_identity/w_chi.py` and `spike/yui_identity/run_identity_test.py` generate synthetic images only. No catalogue, sky position, network fetch, or real image path is present.
- `spike/sim_power.py` generates random coordinates and synthetic signs with injected amplitudes. No survey labels or catalogue files are read.
- `spike/pixel_path_audit.py` has no network path and no catalogue path. It audits FITS headers/pixels and its chirality recovery path explicitly refuses non-synthetic FITS unless `SYNTHET` and `SKYCHIR` headers are present.
- Tori's retained Legacy cutout hash matches disk: `601c309771ed5da0a15defc0b4ccfc1063ee8422a89fbc969d916bba6c1f257a`.
- Tori's receipt hash matches the dispatched value: `b711b7305c3512ce71821174bcc1a7fc6f18eb6fe303107d0fedf8c3d48db266`.
- I re-ran Tori's test suite: `21 passed in 1.37s`.
- I re-ran Yui's identity runner and reproduced the reported identity/signed-zero/broken-mirror values.

Boundary nuance: Tori did read the retained 5,760-byte Legacy calibration FITS for audit/conversion checks. That is allowed under Lana §10's "public calibration frames" exception and did not compute chirality or a sky statistic on the real pixels. Synthetic substitution into that header is also within the spike boundary because the pixel plane is replaced and the harness refuses non-synthetic chirality recovery.

## 1. Yui Identity Result

PASS, with one mandatory preregistration rule.

Yui's reasoning is sound for the identity actually needed:

`chi(x) = (w(x) - w(mirror(x))) / 2`, with `mirror(x) = np.fliplr(x)`.

For a deterministic `w` and pure index reversal, `chi(mirror(x))` and `-chi(x)` reduce to the same two floating-point evaluations in opposite sign. The receipt and rerun show `1000/1000` bit-exact matches on synthetic spirals, `mirror(mirror(x))` byte-identical, and max `|chi(mirror(x)) + chi(x)| = 0.0`.

The signed-zero edge case is real and bounded. On a perfectly symmetric image, `+0.0` and `-0.0` can differ as bits while remaining equal as numeric values. The mitigation is sufficient if frozen explicitly:

> All chirality decisions use value comparisons with `|chi| > tau` and ordered numeric comparisons. No code may branch on `signbit`, `copysign`, raw IEEE-754 bit patterns, or the sign of zero. Exact zero and sub-threshold values abstain.

I would add a unit test that fails if any classification function uses sign-bit zero semantics.

## 2. Broken Interpolating Mirror

This is a hard design constraint.

Yui's deliberately broken mirror violates the identity by `0.058` to `0.944`. Against Longo's reported amplitude scale around `0.04`, a resampling mirror can inject an artifact as large as or larger than the disputed signal.

Therefore the frozen preregistration must state:

> The mirror operation inside `chi` is pure pixel-index reversal on the final analysis raster. It is never an affine, WCS, interpolation, rotation, reprojection, or subpixel reflection transform. `mirror(mirror(x)) == x` must be byte-exact on the exact dtype passed to `w`.

Implications beyond the mirror itself:

- Any preprocessing that changes raster orientation must carry an explicit determinant receipt and be tested by injected chiral sources.
- The measurement path must avoid discretionary reprojection/rotation/resampling after the chosen archive pixel product is selected.
- If a survey cutout service has already resampled the pixels, that is not automatically fatal, but the delivered pixels plus WCS become the measurement input and must pass Tori-style parity/injection tests.
- Any local rendering/conversion for the estimator must be lossless and row-order-explicit.
- Do not create mirrored inputs in sky coordinates via interpolation. Mirror only by index reversal on the analysis raster, then account for sky parity separately.

This is one of the most important spike findings.

## 3. Goru Power Curve

PASS AS A CORRECTION TO THE DESIGN; BLOCKS THE OLD 30K FREEZE.

Goru's statistic behaves correctly in the limited synthetic setting:

- injected `A=0.0400`, recovered reconstructed amplitude `0.0402`;
- null p-values are acceptably uniform (`KS p = 0.5003`);
- permutation machinery does not manufacture confidence in the null simulation.

The important result is negative for Lana's indicative estimate. `N=30,000` accepted spirals gives only `8.0%` power at `A=0.02` under the strict `p < 0.001` criterion. That cannot support a preregistration whose `REJECTED-AT-CLASS` floor is `0.02`.

For the current decision regions, the preregistration should mandate:

> Minimum accepted sample size: `N >= 200,000` accepted spirals after all quality cuts, abstentions, and mirror-pair exclusions, unless the preregistration explicitly narrows the target away from the `[0.02,0.08]` class floor.

If the study is narrowed to Longo's specific `A ~ 0.04` scale, then `N=100,000` accepted spirals appears sufficient in Goru's simulation. But that is a different question and must be stated as such before freeze.

This is accepted-count, not parent-count. Given Yui's crude synthetic estimator abstained around `92%`, a `200,000` accepted sample could imply a parent sample in the millions unless the production estimator is materially less abstaining. That may decide survey feasibility.

Status of my prior §7 blocker:

- The bad 30k estimate is closed as wrong.
- The replacement minimum for the current class-floor design is `N >= 200,000` accepted spirals.
- Full freeze is still not closed until the accepted-count forecast is tied to the actual chosen survey, actual estimator, and actual hand-check attenuation protocol.

## 4. Tori Silent-Flip Result

PASS, with fail-closed conservatism.

Tori demonstrated the exact catastrophic failure mode: if a row flip is performed and its determinant is honored, the known sky sign recovers; if the same flip is silently ignored, the recovered sign inverts. A single undeclared flip can invert every galaxy consistently and invisibly.

The checker plus declared-row-order converter is an adequate control for the failure mode it targets:

- WCS `CD` or `PC*CDELT` determinant is logged;
- row-order transform determinant is logged;
- combined pixel-to-output-sky sign is logged;
- decoded pixel conversion is byte/lossless checked;
- synthetic known-sign injection uses retained WCS cards;
- silent row-flip and scrambled-WCS controls prove the harness detects the fault;
- chirality recovery refuses non-synthetic FITS in the spike.

Fail-closed on distortion keywords is the right conservatism for this stage, not too weak. A linear determinant is not enough when SIP/PV/CPDIS/DET2IM or similar distortions are in play. The frozen options are:

1. reject distorted products, or
2. implement and test a true local Jacobian-sign calculation across the cutout with injected-source receipts.

Do not silently fall back to a linear determinant for distorted WCS.

## 5. What Is Still Missing Before Preregistration Freeze

Still missing:

1. **Exact covariate battery.** This is not closed. The preregistration still needs executable definitions: covariate sources, maps, binning or model form, matching/regression/adversarial test, leakage thresholds, multiple-testing handling, and exact `INCONCLUSIVE` triggers.
2. **Survey route and scale.** Tori must bind a real public FITS/WCS route and Goru/Lana must show it can plausibly yield `N >= 200,000` accepted spirals for the class-floor design, or explicitly narrow the question.
3. **Production estimator freeze.** Yui's `w` proves identity but is too abstaining and crude to assume feasibility at scale. The exact production `w`, `tau`, null calibration, and abstention rules must be frozen before sky data.
4. **Hand-check attenuation protocol.** The outline exists, but freeze needs exact sample size, strata, adjudication, uncertainty calculation, and how attenuation affects confidence intervals and decision regions.
5. **No resampling mirror rule.** Must be written into the preregistration as a hard rule, with a byte-exact `mirror(mirror(x))` test.
6. **Signed-zero rule.** Must be written into code and preregistration: value comparisons only, no sign-bit semantics.
7. **Distortion policy.** Either fail closed on all distortion keywords or implement local-Jacobian parity receipts before freeze.

## Plain Verdict For Duho

The feasibility spike succeeded, but it made the study harder, not easier.

Established:

> The core antisymmetry identity is sound under pure index reversal; resampling mirrors are dangerous; the fixed-axis statistic is unbiased in simulation; permutation nulls behave; WCS/row-order parity can be audited; and silent row flips are detectable.

Not established:

> That any real survey can supply enough accepted galaxies, or that the covariate/systematics battery is freeze-ready.

Power blocker status:

> Partly closed. The correct accepted-count target for the current class-floor design is approximately `N >= 200,000`, not `30,000`. Freeze still needs to bind that to real survey yield and attenuation.

Covariate blocker status:

> Still open. No executable covariate battery exists yet.

Final gate:

> Proceed to preregistration drafting only if it incorporates the hard constraints above. Do not run on real sky data yet.
