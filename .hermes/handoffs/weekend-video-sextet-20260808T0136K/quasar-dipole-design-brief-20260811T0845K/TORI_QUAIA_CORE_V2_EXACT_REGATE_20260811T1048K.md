# Tori exact regate — Hwao Quaia-core design brief v2

Marker: `TORI_QUAIA_CORE_V2_EXACT_REGATE_20260811T1048K`

## Exact scope

Authority: `HWAO_QUASAR_DIPOLE_DESIGN_BRIEF_ORDER_20260811T0845K.md`, SHA-256 `26b6f2954e3a0fd2967a93222aef1b630c262488a943a24ed90c6e55602a10c8`.

Coordinator brief graded: `HWAO_QUASAR_DIPOLE_DESIGN_BRIEF_V2_20260811T1015K.md`, SHA-256 `6f9e5998c8a13554261c16aeac4c31d9342a969d5eccd7bdd9626952c81114f8`.

Lana review consulted: `reviews/LANA_QUASAR_DIPOLE_DESIGN_BRIEF_V2_20260811.md`, SHA-256 `d39f31a1f7edeceb99c01ff7f0f4897638f699e5c9ad199d2c15ce7a50fcad0d`.

No family-level grade is inherited. Every exact named product and semantic convention is re-graded below.

Grades are only `DOCUMENTED`, `UNDOCUMENTED`, or `NOT-YET-CHECKED`. No named item remains `NOT-YET-CHECKED`.

## Result

**`NOT_WORTH_DOING_YET — HOLD_DESIGN_BRIEF_FREEZE_NOT_GATEABLE.`**

The exact three core hashes are real, but they are Quaia `0.1.0`, not the Quaia `1.0.0` release claimed by the brief. [13]

The brief skips Tori’s mandatory upstream artifact/quality-flag sensitivity gate; Lana’s review handles it honestly by declaring it unmet, but that finding is not incorporated into the Hwao coordinator brief.

## Exact artifact grades

| Named v2 item | Grade | Exact finding |
|---|---|---|
| Zenodo record `8060755` | `DOCUMENTED` | Immutable record for Quaia `0.1.0`; it is not the latest release. [13] |
| Label `Catalogue Package (Quaia v1)` for record `8060755` | `UNDOCUMENTED` | The exact record says `version: 0.1.0`. [13] |
| `quaia_G20.0.fits`, MD5 `42cec6519d139ac5fdcf4f891a68b5d4`, 99,786,240 bytes | `DOCUMENTED` | Exact record name, checksum, and byte count match. [13] |
| `selection_function_NSIDE64_G20.0.fits`, MD5 `e62df7437156763ee59210976a808e45`, 400,320 bytes | `DOCUMENTED` for byte identity | Exact record name, checksum, and byte count match. [13] |
| `random_G20.0_10x.fits`, MD5 `c5d5240d8bf72dbf1d19eebee9dddf2c`, 151,122,240 bytes | `DOCUMENTED` for byte identity | Exact record name, checksum, and byte count match. [13] |
| One primary sample `G < 20.0` | `DOCUMENTED` | The primary catalogue paper defines the 755,850-source cleaner `G < 20.0` sample. [22] |
| Threshold multiplicity | `DOCUMENTED` | Only one threshold is named; there is no selectable ladder. |
| Current Quaia `1.0.0` package | `UNDOCUMENTED` in v2 | Record `10403370` has different core hashes and adds `selection_function_template_maps.zip`. [15] |
| Exact published systematics-template archive | `UNDOCUMENTED` in v2 | The named `0.1.0` record does not contain the template archive. [15] |

## Selection-function package grades

| Named convention | Grade | Exact finding |
|---|---|---|
| HEALPix `NSIDE=64`, `RING` | `DOCUMENTED` | Verified directly from the exact map binary; see `TORI_QUAIA_EXACT_BINARY_RECEIPT_20260811T1035K.json`. |
| `Galactic coordinate frame` | `UNDOCUMENTED` and contradicted | The exact FITS header has no `COORDSYS`; the pinned public notebook creates pixels from `ra, dec` and rotates celestial to Galactic only for display. [24] |
| `selection_function > 0.0` as the sole published mask | `UNDOCUMENTED` | The public product is a continuous relative-completeness map, not a binary mask artifact. [22] |
| `1=unmasked, 0=masked` | `UNDOCUMENTED` | The catalogue paper explicitly says the map values are relative completeness and should not be interpreted as probabilities. [22] |
| Continuous inverse-probability weighting | `UNDOCUMENTED` as written | The brief does not specify the exact estimator operation, normalization, or how randoms enter it. |
| `Linear scaling via randoms` | `UNDOCUMENTED` | Randoms are sampled points carrying the modeled selection, not a documented linear link function. [22] |
| Gaia scanning law, unWISE depth, and dust represented by the family model | `DOCUMENTED` at method level | The primary paper names dust, parent-source density, and parent scan patterns as modeled inputs. [22] |
| All regression coefficients “instantiated in the randoms” | `UNDOCUMENTED` | The random catalogue is not a coefficient or fitted-state archive. [22] |
| Train/test split | `UNDOCUMENTED` in v2 | No value is stated. |
| Mask-interaction terms fixed to zero | `UNDOCUMENTED` | No primary product or method quotation supports this rule. |
| Selection residual control | `UNDOCUMENTED` in v2 | The primary paper reports biased residuals near the Galactic plane and recommends possible plane/LMC/SMC masking, but v2 names no such frozen control. [22] |

## Mandatory upstream artifact/quality-flag sensitivity gate

**Grade: `UNDOCUMENTED` and skipped in the Hwao v2 coordinator brief.**

Quaia’s released row schema contains Gaia and unWISE join identifiers but does not carry the upstream row-level warning/quality bits required for a direct sensitivity split. [22]

The primary catalogue construction starts from the full Gaia quasar-candidate sample rather than cutting on other Gaia pipeline flags, so the absence is substantive rather than a cosmetic schema omission. [22]

Hwao v2 contains no external Gaia scanning-law or unWISE coverage artifact, no checksum, no fixed sensitivity statistic, no tolerance, and no `INCONCLUSIVE` branch tied to that test.

Lana v2 correctly says this mandatory gate is unmet and that an external artifact/scanning-law map would have to be bound as a value. That review does not repair the coordinator brief until Hwao incorporates the actual product, checksum, statistic, tolerance, and fail-closed branch.

## Kinematic convention grades

| Named convention | Grade | Exact finding |
|---|---|---|
| CMB speed `369.82 km/s` | `DOCUMENTED` | The Quaia dipole paper gives `369.82 +/- 0.11 km/s`. [17] |
| CMB direction/sign | `UNDOCUMENTED` in v2 | The primary convention is motion toward Galactic `(264.021 deg, 48.253 deg)` with positive forward count enhancement; v2 states neither. [17] |
| Quoted flux rule `S=S0[1+(2+alpha) beta cos(theta)]` | `UNDOCUMENTED` and mismatched | The exact NVSS simulation applies a Doppler factor with exponent `1+alpha` and handles aberration separately. [5] |
| Count-slope `x` | `UNDOCUMENTED` | It is absent from v2; the Quaia paper instead uses actual source counts rather than a scalar proxy `x`. [17] |
| `alpha=1.0`, described as selectable before run | `UNDOCUMENTED` | The Quaia paper derives a per-source `alpha` distribution from `G-BP`; it does not publish this scalar default for the frozen sample. [17] |
| Redshift dependence | `UNDOCUMENTED` | No value is frozen. The primary paper explicitly identifies the no-redshift-dependence assumption. [17] |
| Map-level subtraction | `UNDOCUMENTED` | Section 3 is titled “Subtraction Convention” but never states that a map-level component is subtracted. |
| Joint-posterior comparison | `UNDOCUMENTED` in v2 | The primary Quaia method fixes CMB magnitude and direction in model `M6` and compares marginal likelihood, but v2 does not adopt that procedure. [17] |
| Null draw procedure and seed | `UNDOCUMENTED` | No exact Quaia source-count/colour method, draw count, seed, or null-artifact hash is frozen. [17] |

The exact primary Quaia convention that could replace v2’s text is documented: use actual source counts, derive the per-source `alpha` distribution from `G-BP`, sample that distribution at fixed `v_CMB`, and compare the CMB-fixed model by marginal likelihood without map-level subtraction. [17]

## Decision, receipt, and novelty grades

| Item | Grade | Finding |
|---|---|---|
| Detection threshold `>=3 sigma` | `DOCUMENTED` only as a design value | It is stated, but its null is unreproducible while the kinematic procedure is unfrozen. |
| Exact `INCONCLUSIVE` conditions | `UNDOCUMENTED` | V2 combines “Null / Inconclusive” into one `<3 sigma` branch and omits selection-residual and upstream-artifact failures. |
| One-run execution script hash | `DOCUMENTED` only as an intention | The brief states a script hash will be logged. |
| Exact one-run receipt | `UNDOCUMENTED` | It omits frozen environment, input-manifest hash, RNG seed, null-realization hash, no-overwrite path, and the mandatory upstream sensitivity receipt. |
| Claimed novelty over published work | `UNDOCUMENTED` | The Quaia dipole and its selection function have already been analyzed; the proposed randoms treatment is not new by itself. [17] |
| Pre-registered adjudication of catalogue/selection dependence | `UNDOCUMENTED` in Hwao v2 | This could be new, but only after one exact selection treatment and one upstream-artifact control are frozen. |

## Exact flip condition

The brief becomes gateable only if a corrected coordinator artifact does all of the following before any statistic is seen:

1. Names Quaia `1.0.0`, record `10403370`, with the exact catalogue, selection-map, random, and template-archive hashes. [15]
2. Freezes the native equatorial HEALPix interpretation by binding an immutable implementation commit; no unreceipted coordinate conversion is allowed. [24]
3. Freezes one exact Galactic-plane/LMC/SMC mask or explicitly justifies another single mask from the published residual evidence. [22]
4. Specifies the selection estimator, normalization, smoothing, model-state artifact, split policy, and mask interaction as exact values.
5. Binds one external Gaia/unWISE quality or coverage artifact, checksum, fixed sensitivity statistic, tolerance, and `INCONCLUSIVE` branch.
6. Uses the sample-specific Quaia kinematic procedure, including vector sign, source-count and spectral-index treatment, redshift assumption, posterior-versus-subtraction choice, draw count, and seed. [17]
7. Defines a no-overwrite, exact-hash one-run receipt covering inputs, code, environment, random output, controls, and decision.

If any item remains selectable or absent, `NOT_WORTH_DOING_YET` remains the successful and binding outcome.

No acquisition, mock generation, estimator, statistic, result, scientific claim, publication, or acceptance occurred.

## Sources

[5] https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html — Rubart and Schwarz 2013 NVSS dipole analysis
[13] https://zenodo.org/api/records/8060755
[15] https://zenodo.org/api/records/10403370
[17] https://arxiv.org/html/2311.14938v2
[22] https://arxiv.org/pdf/2306.17749
[24] https://raw.githubusercontent.com/kstoreyf/gaia-quasars-lss/3c4d0a3fbe21209d5627f480a4da01830062c77c/notebooks/2023-10-08_data_products_inclzsplit.ipynb
