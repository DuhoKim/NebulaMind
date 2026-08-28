# Tori exact-artifact provenance gate: quasar number-count dipole design brief

Marker: `TORI_QUASAR_DIPOLE_EXACT_ARTIFACT_PROVENANCE_GATE_V1_20260811T1045K`

## Authority and scope

Sole authority is `HWAO_QUASAR_DIPOLE_DESIGN_BRIEF_ORDER_20260811T0845K.md`, SHA-256 `26b6f2954e3a0fd2967a93222aef1b630c262488a943a24ed90c6e55602a10c8`.

The exact active candidate graded here is `HWAO_QUASAR_DIPOLE_DESIGN_BRIEF_V2_20260811T1015K.md`, SHA-256 at gate time `6f9e5998c8a13554261c16aeac4c31d9342a969d5eccd7bdd9626952c81114f8`.

This is provenance review only. No catalogue statistic, estimator, mock sky, significance, result, scientific claim, publication, or acceptance was produced.

Grades have only the requested meanings:

- `DOCUMENTED`: the exact named artifact or convention is pinned and supported by primary public documentation quoted below.
- `UNDOCUMENTED`: the exact named artifact, semantic convention, or immutable coupling is absent, contradicted, ambiguous, or falsely named after checking the primary public products.
- `NOT-YET-CHECKED`: the exact item has not been checked. No named item remains in this state.

## Gate result

**`NOT_WORTH_DOING_YET — FAIL_CLOSED.`**

The three file names, byte counts, and MD5 values in the Hwao v2 brief are real exact artifacts, but they belong to Quaia release `0.1.0`, Zenodo record `8060755`; they are not the published Quaia `1.0.0` release named by the brief. [13]

The current published Quaia release is `1.0.0`, Zenodo record `10403370`, and all three core MD5 values differ from the values frozen in Hwao v2. [15]

The brief also freezes the wrong coordinate frame, treats a continuous selection function as a binary mask, does not bind the published systematics-template archive, and gives an unattributed kinematic flux rule that is not the exact Quaia or NVSS convention. [17][24]

No scientific run may proceed from this brief.

## A. Exact Hwao-v2 product matrix

| Exact item in Hwao v2 | Grade | Primary-documentation finding |
|---|---|---|
| Zenodo record `8060755` | `DOCUMENTED` | The record is immutable and identifies Quaia release `0.1.0`, not `1.0.0`. [13] |
| Label “Quaia v1” attached to record `8060755` | `UNDOCUMENTED` | The exact record says `version: 0.1.0` and is not the last version. [13] |
| `quaia_G20.0.fits`, 99,786,240 bytes, MD5 `42cec6519d139ac5fdcf4f891a68b5d4` | `DOCUMENTED` | Name, byte count, and MD5 match record `8060755` exactly. [13] |
| `selection_function_NSIDE64_G20.0.fits`, 400,320 bytes, MD5 `e62df7437156763ee59210976a808e45` | `DOCUMENTED` for byte identity | Name, byte count, and MD5 match record `8060755` exactly. [13] |
| `random_G20.0_10x.fits`, 151,122,240 bytes, MD5 `c5d5240d8bf72dbf1d19eebee9dddf2c` | `DOCUMENTED` for byte identity | Name, byte count, and MD5 match record `8060755` exactly. [13] |
| `G < 20.0` threshold | `DOCUMENTED` | The primary catalogue paper defines the 755,850-source `G < 20.0` sample as the cleaner bright catalogue. [22] |
| Selection-function systematics model | `DOCUMENTED` at family level | The primary paper says the model considers dust, parent-survey source density, and parent-survey scan patterns. [22] |
| Exact systematics template maps for record `8060755` | `UNDOCUMENTED` | The `0.1.0` package does not contain `selection_function_template_maps.zip`; that frozen archive first appears in record `10403370`. [15] |
| Random-catalogue meaning | `DOCUMENTED` | The primary paper says random catalogues are Poisson-distributed points with the same modeled selection effects as Quaia. [22] |
| Claim that the random catalogue freezes “all regression coefficients” | `UNDOCUMENTED` | The public description defines a sampled random catalogue, not a coefficient or model-state archive. [22] |
| Mask `selection_function > 0` | `UNDOCUMENTED` as a published mask | The published product is a continuous relative-completeness map, not a binary mask product. [22] |
| Mask value rule “1 = unmasked, 0 = masked” | `UNDOCUMENTED` | The primary paper explicitly says selection-map values are relative completeness and “should not be interpreted as a probability.” [22] |
| HEALPix `NSIDE=64`, `RING` ordering | `DOCUMENTED` | The exact downloaded binary has `PIXTYPE=HEALPIX`, `NSIDE=64`, and `ORDERING=RING`; the verified receipt is `TORI_QUAIA_EXACT_BINARY_RECEIPT_20260811T1035K.json`. |
| Galactic coordinate frame for that map | `UNDOCUMENTED` and contradicted by the implementation | The FITS header has no `COORDSYS`; the pinned public notebook indexes pixels from `ra, dec` and rotates `C` to `G` only for display. [24] |
| No smoothing or apodization | `DOCUMENTED` only as a design choice | It is written in the brief, but it does not repair the missing coordinate and mask semantics. |
| Upstream Gaia/unWISE row-level artifact or processing-warning sensitivity | `UNDOCUMENTED` | Quaia’s published schema contains join identifiers and science columns but no row-level parent quality bits; the primary paper says it starts from the full Gaia candidate sample rather than cutting on other Gaia pipeline flags. [22] |
| Published residual-systematics control | `UNDOCUMENTED` in the brief | The catalogue paper reports biased residuals near the Galactic plane and says precision measurements may require masking the plane and the LMC/SMC regions. [22] |
| Exact kinematic-dipole quotation in Hwao v2 | `UNDOCUMENTED` | The prose is not found verbatim in the checked Quaia or NVSS primary sources. [5][17] |
| Flux rule `S = S0[1+(2+alpha) beta cos(theta)]` | `UNDOCUMENTED` and technically mismatched | The NVSS primary simulation applies Doppler flux as a factor raised to `1+alpha`; the separate aberration step supplies the angular factor. [5] |
| CMB velocity amplitude `369.82 km/s` | `DOCUMENTED` | The Quaia dipole paper gives `369.82 +/- 0.11 km/s`. [17] |
| CMB vector direction and sign | `UNDOCUMENTED` in the brief | The primary convention is motion *towards* Galactic `(l,b)=(264.021 deg,48.253 deg)`, but the brief freezes no direction or forward-overdensity sign. [17] |
| Count slope `x` | `UNDOCUMENTED` in the brief | The Quaia analysis explicitly replaces a single proxy `x` with the actual source-count distribution. [17] |
| Spectral-index input `alpha` | `UNDOCUMENTED` in the brief | The Quaia analysis derives a per-source distribution from Gaia `G-BP` colour; `alpha` is not a free scalar to be selected after opening the catalogue. [17] |
| Redshift dependence | `UNDOCUMENTED` in the brief | The primary formula states that `x` and `alpha` are conventionally assumed not to be redshift-dependent and flags that assumption as debatable. [17] |
| Kinematic treatment: subtraction versus posterior comparison | `UNDOCUMENTED` in the brief | The Quaia primary analysis does not subtract a map-level dipole; model `M6` fixes direction and magnitude to the CMB kinematic dipole and computes marginal likelihood. [17] |
| Exact Monte Carlo realization or seed | `UNDOCUMENTED` | The Quaia paper documents 50,000 draws of the measured `alpha` distribution but the brief binds neither that procedure nor an immutable seed or null-realization receipt. [17] |
| Three-sigma decision threshold | `DOCUMENTED` only as a design choice | It cannot be evaluated reproducibly until the null distribution, mask, coordinate transform, count/spectral inputs, and one-time seed receipt are frozen. |

## B. Exact release correction

If the brief intends the public release used by the published Quaia catalogue paper, it must name `Quaia 1.0.0`, Zenodo record `10403370`, not record `8060755`. [15][22]

The corresponding exact `G < 20.0` artifacts are:

| Quaia `1.0.0` artifact | Exact MD5 | Grade |
|---|---:|---|
| `quaia_G20.0.fits` | `72531bc67bde1b08a69d5aeae03fb26e` | `DOCUMENTED` [15] |
| `selection_function_NSIDE64_G20.0.fits` | `9bec5ff5d2bda8f283fd99d6db6621df` | `DOCUMENTED` [15] |
| `random_G20.0_10x.fits` | `e89dc31635d4688c8f3861dfb8a7e546` | `DOCUMENTED` [15] |
| `selection_function_template_maps.zip` | `5a887fcdbcb2bb3f2bc4b9de58cd9c67` | `DOCUMENTED` [15] |

The exact v1 selection-map binary also verifies as `NSIDE=64`, `RING`, with no `COORDSYS` header keyword; its MD5 receipt is frozen alongside the v0.1 map in `TORI_QUAIA_EXACT_BINARY_RECEIPT_20260811T1035K.json`.

The public notebook must therefore be pinned at an immutable commit if it is used to supply the otherwise absent coordinate-frame semantics; current primary code maps `ra, dec` directly to HEALPix and displays the map after a celestial-to-Galactic rotation. [24]

## C. Verbatim Quaia kinematic convention that may be frozen instead

The primary Quaia dipole paper states:

> “Here, we instead use the actual source counts themselves – rather than their proxy x – and take the distribution of alpha to find a distribution of dipole amplitudes D given v.” [17]

It then applies a per-source Doppler change, counts sources above the fixed limiting flux, multiplies by the aberration factor, and defines `D=(n_b-n_i)/n_i`. [17]

For Quaia `G < 20.0`, the paper fixes the limiting flux near the catalogue limit and samples the measured `alpha` distribution 50,000 times after substituting `v=v_CMB`. [17]

For the hypothesis test, it states:

> “Finally, we may totally align this model’s dipole in both direction and magnitude with the CMB kinematic dipole and compute the marginal likelihood.” [17]

This convention is `DOCUMENTED`, but it is not the convention currently written in Hwao v2.

To adopt it, the brief must freeze all of the following without later revision:

1. Quaia release `1.0.0` and the four exact artifact hashes above.
2. Native equatorial HEALPix ordering plus an immutable coordinate-rotation implementation.
3. One exact Galactic-plane/LMC/SMC mask, because the primary papers document selection-function residuals there. [17][22]
4. Per-source `alpha` derivation from `G-BP`, actual source-count distribution, `G < 20.0` limiting flux, and no redshift dependence. [17]
5. The velocity vector *towards* Galactic `(264.021 deg,48.253 deg)` at `369.82 +/- 0.11 km/s`, making the forward count residual positive. [17]
6. Joint posterior comparison through the fixed kinematic model, with no map-level subtraction. [17]
7. One immutable seed and fresh null receipt if any random draw is retained; the paper does not publish a seed.
8. An upstream Gaia/unWISE quality-flag sensitivity branch and a residual-map negative control, because neither is supplied by the released Quaia row schema and the published selection residuals are not clean near the plane. [22]

Until those eight items are in the brief, the exact kinematic convention remains unbound.

## D. NVSS convention: documented, but not portable to Quaia

The official HEASARC `nvss` table documents its field semantics, J2000 coordinates, residual codes, and that its underlying product was updated in June 2009. [6]

It does not supply an immutable semantic release version, exact table checksum, or frozen query row manifest, so exact NVSS input bytes remain `UNDOCUMENTED`. [6]

The Rubart–Schwarz NVSS analysis documents the family-specific expectation `d=[2+x(1+alpha)]v/c`, with `x=1.10 +/- 0.02`, `alpha=0.75 +/- 0.25`, and CMB velocity about `369 km/s`. [5]

Its Appendix A documents uniform isotropic coordinates, count-law flux generation, a Mersenne Twister generator, a separate Doppler flux transformation with exponent `1+alpha`, and a separate aberration transformation. [5]

The paper documents the Singal-style mask `|delta|<=40 deg` and `|b|>=10 deg`, then evaluates estimator and masking bias with 100,000 simulations at the CMB expectation. [5]

Those NVSS mask, count-slope, spectral-index, and radio-flux conventions are `DOCUMENTED` for that published NVSS analysis. [5]

The machine-readable mask bytes and random seed are `UNDOCUMENTED`, and applying the radio convention to the optical Quaia catalogue is `UNDOCUMENTED` because Quaia uses a different sample-specific source-count and spectral-index construction. [5][17]

## E. Superseded CatWISE Goru candidate

`GORU_QUASAR_DIPOLE_DESIGN_BRIEF_20260811T0959K.md`, SHA-256 `e11b72b14959bfa0cb83161bbc2f588e86a2a4a4c2cc717fc9c2110061443b7f`, is not the active Hwao family, but its exact names were also checked.

| Goru exact name or rule | Grade | Finding |
|---|---|---|
| Zenodo record `8303800`, Secrest release `v3` | `DOCUMENTED` | Versioned release with exact file checksums. [1][2] |
| `CatWISE2020_Secrest_v3.fits` | `UNDOCUMENTED` | No file with this name exists in the complete v3 release or either released code archive. [1][9] |
| Actual `catwise_agns_masked_final_w1lt16p5_alpha.fits` | `DOCUMENTED` for identity | The exact v3 release pins the name, size, and MD5. [1] |
| `CatWISE_v3_mask_NSIDE64.fits` | `UNDOCUMENTED` | No file with this name exists in the v3 release. [1] |
| Actual `MASKS_exclude_master_final.fits` | `DOCUMENTED` for identity | The v3 release pins the mask-ellipse table and checksum. [1] |
| `w1ab_map.fits`, `w2ab_map.fits`, `sfd98_dust_nside64.fits` | `UNDOCUMENTED` | None exists in the complete v3 release or code archives. [1][10] |
| Threshold ladder `W1<16.5,16.0,15.5` | `UNDOCUMENTED` | The primary analysis freezes the final sample at `W1<16.4`; the released `W1<16.5` file is a parent superset. [11] |
| Exact released ecliptic correction | `DOCUMENTED` as code | The release implements a fitted correction versus absolute ecliptic latitude. [10][11] |
| Frozen corrected-map bytes and checksum | `UNDOCUMENTED` | The code names generated map outputs, but those generated map files are absent from the immutable v3 release. [1][10] |
| Claimed verbatim `S=S0[1+(2+alpha)beta cos(theta)]` convention | `UNDOCUMENTED` | It is not verbatim in the primary CatWISE or NVSS sources and combines the separate Doppler and aberration terms incorrectly. [5][11] |

The exact-name mechanical receipt is `TORI_EXACT_PRODUCT_NAME_SEARCH_RECEIPT_20260811T1012K.json`, SHA-256 `65ced39a530585348657a5c76241e6d6eb3b6a231e5f8c016c704da366ca4c3b`.

## F. What makes this not worth doing yet

A published Quaia dipole analysis already compares the catalogue with a fixed CMB-kinematic model while explicitly studying selection-function residuals and multiple Galactic masks. [17]

A rerun that merely changes to a three-sigma amplitude rule, while leaving the release version, mask semantics, coordinate frame, sample-specific kinematic null, and artifact-flag sensitivity unresolved, would not add a provenance-clean test.

The first admissible next action is therefore a brief-only v3 correction that freezes the eight items in Section C and then returns for exact-product re-gating.

No acquisition or statistic may begin before that re-gate and Duho’s acceptance.

## Sources

[1] https://zenodo.org/api/records/8303800 — Zenodo API: Secrest CatWISE v3 exact record
[2] https://zenodo.org/records/8303800 — Zenodo: Secrest CatWISE v3 dataset, mask and code
[5] https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html — Rubart and Schwarz 2013 NVSS dipole analysis
[6] https://heasarc.gsfc.nasa.gov/w3browse/all/nvss.html — HEASARC NVSS catalog and data dictionary
[9] https://zenodo.org/api/records/8303800/files/Generatecode.tar.gz/content — Secrest v3 Generatecode archive
[10] https://zenodo.org/api/records/8303800/files/Resultscode.tar.gz/content — Secrest v3 Resultscode archive
[11] https://arxiv.org/pdf/2009.14826v2 — Secrest et al. 2021 CatWISE quasar dipole paper v2 PDF
[13] https://zenodo.org/api/records/8060755
[15] https://zenodo.org/api/records/10403370
[17] https://arxiv.org/html/2311.14938v2
[22] https://arxiv.org/pdf/2306.17749
[24] https://raw.githubusercontent.com/kstoreyf/gaia-quasars-lss/3c4d0a3fbe21209d5627f480a4da01830062c77c/notebooks/2023-10-08_data_products_inclzsplit.ipynb
