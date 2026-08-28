# Tori custody assessment — can the Mittal–Singal disagreement be recovered from the papers?

Marker: `TORI_MITTAL_SINGAL_EXACT_ARTIFACT_RECOVERABILITY_ASSESSMENT_20260811T1125K`

## Authority and scope

Authority: `HWAO_LOOSENED_BAR_MITTAL_SINGAL_ORDER_20260811T1110K.md`, SHA-256 `1d33052a25a8fc6b52f107be124dba3c8a018dbf7eced9a159f6e93c8988452f`.

Novelty alone is loosened. Exact provenance and pre-registration are not.

This is a reading and custody assessment only. Public paper versions, arXiv source packages, and public Zenodo products were inspected. No design, estimator, mock, dipole statistic, causal ablation, scientific result, or claim was produced.

## Answer up front

**The broad methods disagreement is recoverable; the factor-of-three causal attribution is not recoverable from the stated papers at custody grade.**

The papers openly state a major fork: Mittal includes the Quaia selection function in pixel likelihoods and Singal explicitly omits it. [1][3]

But neither paper holds selection treatment fixed while changing only the estimator, mask, or correction, and neither releases its analysis code. Mittal binds no Zenodo record or input checksum, while Singal leaves the exact cut-sky amplitude-correction implementation at “factors of order unity.” [1][3]

The current authoritative Mittal record also includes a published correction that changes the kinematic expectation and softens the amplitude conclusion; Singal’s final arXiv version predates Mittal’s corrected arXiv v2. [2][7][8]

Therefore the defensible disposition is:

**`PARTIALLY_RECOVERABLE_METHOD_FORK / NOT_RECOVERABLE_AS_CAUSAL_ADJUDICATION_FROM_READING_ALONE`.**

Under the exact assessment-only order, this is the fifth honest closure. It does not establish that a separately authorized reconstruction is impossible.

## 1. Did the papers use different Quaia releases?

**No release mismatch is supported as the explanation.**

Singal states verbatim that it used Quaia `v0.1.0`, “the same as used by Mittal et al. (2024),” and its Data Availability section binds DOI `10.5281/zenodo.8060755`. [3]

Mittal’s original paper was accepted on 2023-11-24 and submitted to arXiv on 2023-11-25, before public Quaia `1.0.0` record `10403370` was created on 2023-12-18. [1][5][7]

That chronology and Singal’s explicit statement strongly identify the original shared candidate as release `0.1.0`; however, Mittal itself does not name a version, DOI, filename, checksum, or byte count, and says only that data are available on reasonable request. [1]

Accordingly:

- Singal → Quaia `0.1.0` exact release identity: `DOCUMENTED`.
- Mittal → Quaia `0.1.0` exact self-bound release identity: `UNDOCUMENTED`.
- Claim that both used identical catalogue bytes: `UNDOCUMENTED` at strict custody grade, although the primary evidence strongly supports it.
- Claim that one used `0.1.0` and the other used `1.0.0`: unsupported.

The release ambiguity is real because the `0.1.0` and `1.0.0` catalogue files and selection maps retain identical names and, for four products, identical byte counts while their MD5 values differ. [4][5]

That exact comparison is frozen in `TORI_QUAIA_RELEASE_IDENTITY_COMPARISON_20260811T1122K.json`.

## 2. Exact products bound by Mittal et al.

| Artifact or convention | Grade | Custody finding |
|---|---|---|
| Original analysis paper, arXiv `2311.14938v1` | `DOCUMENTED` | Exact PDF and source tar obtained and hashed. [1] |
| Current paper plus published correction, arXiv `2311.14938v2` | `DOCUMENTED` | Exact PDF and source tar obtained and hashed. [2][7] |
| Quaia release/version | `UNDOCUMENTED` | No Zenodo record, DOI, version, checksum, or byte count is bound by Mittal. [1] |
| `G<20.0` and `G<20.5` catalogue families | `DOCUMENTED` at sample-definition level | The paper names both samples and their published row counts. [1] |
| Exact catalogue filenames and bytes | `UNDOCUMENTED` by Mittal | The likely `0.1.0` candidates are obtainable, but the paper does not bind them. |
| Exact selection-function filenames and bytes | `UNDOCUMENTED` by Mittal | The paper uses a map for each sample but does not name a file, version, record, or checksum. [1] |
| Candidate `0.1.0` selection maps | `DOCUMENTED` for public availability | Both exact maps were downloaded from record `8060755`; MD5 and byte counts match. [4] |
| Selection-map native coordinate frame | `UNDOCUMENTED` | Exact FITS headers have `NSIDE=64`, `RING`, and no `COORDSYS`; no analysis code binds the intended interpretation. |
| Quaia random catalogue | `DOCUMENTED` as not used in the inferential pipeline | Mittal uses the selection map value `s_i` in its Poisson and point-by-point likelihoods; the released random files are not invoked. [1] |
| Galactic masks `0,10,20,30,40,30*` | `DOCUMENTED` as prose definitions | The `30*` definition adds a 4 sr circle centered at Galactic `(0,0)` to the 30-degree plane mask. [1] |
| Exact mask pixels/rows/checksum | `UNDOCUMENTED` | No mask file, row manifest, partial-pixel rule, or coordinate-transform receipt is released. |
| Poisson likelihood and point-by-point likelihood | `DOCUMENTED` as equations | Both explicitly multiply the signal by selection value `s_i`. [1] |
| Dynesty configuration, RNG seed, environment, analysis code | `UNDOCUMENTED` | The paper names packages but supplies no code or immutable run configuration. |
| Exact analyzed row manifests | `UNDOCUMENTED` | None is released. |
| Redshift cut | `DOCUMENTED` as none | The paper says it did not use the quasar redshift distribution. [1] |
| Original kinematic expectation | `DOCUMENTED` but superseded | The original spectral-index calculation was wrong. [2] |
| Corrected kinematic expectation | `DOCUMENTED` in prose | Correction gives mean amplitudes `0.0048` for Quaia low and `0.0043` for Quaia high. [2] |
| Corrected null implementation bytes/seed | `UNDOCUMENTED` | No code or random-draw receipt is released. |

The current correction says the original spectral-index calculation contained a units error, changes the expected amplitudes, makes conclusions sensitive to the amplitude prior to an extent, and states that the amplitude is not decisive. [2]

That correction is load-bearing: any comparison that still describes Mittal’s null solely by the original `0.0080/0.0068` values is stale.

## 3. Exact products bound by Singal

| Artifact or convention | Grade | Custody finding |
|---|---|---|
| Singal paper, arXiv `2403.16581v2` | `DOCUMENTED` | Exact PDF and source tar obtained and hashed. [3][8] |
| Quaia `v0.1.0`, DOI `10.5281/zenodo.8060755` | `DOCUMENTED` | Explicitly named in the paper and Data Availability section. [3] |
| `quaia_G20.5.fits` from `0.1.0` | `DOCUMENTED` | DOI package resolves uniquely to MD5 `8b816b719e8c8ccd1c0a648b53557ddd`, 171,020,160 bytes. [4] |
| `quaia_G20.0.fits` from `0.1.0` | `DOCUMENTED` | DOI package resolves uniquely to MD5 `42cec6519d139ac5fdcf4f891a68b5d4`, 99,786,240 bytes. [4] |
| Selection-function product | `DOCUMENTED` as deliberately not used | Singal says, “We did not incorporate the selection function.” [3] |
| Quaia random catalogue | `DOCUMENTED` as not used | No random product appears in the stated pipeline or arXiv source package. |
| Magnitude samples | `DOCUMENTED` | `G<20.5`, `G<20.0`, and `20<G<20.5` are tabulated. [3] |
| Galactic cuts | `DOCUMENTED` | `|b|>30`, `35`, and `40` degrees are tabulated. [3] |
| Vector and hemisphere estimators | `DOCUMENTED` as prose/equations | The paper defines the vector sum, 422-cell hemisphere grid, and count asymmetry. [3] |
| Exact mask row manifests and boundary rule | `UNDOCUMENTED` | No immutable membership list or code is released. |
| Cut-sky amplitude-correction factors | `UNDOCUMENTED` | The paper says corrections “of the order of unity” are applied but supplies no exact factors or implementation. [3] |
| Estimator code, grid generator, RNG/environment | `UNDOCUMENTED` | The arXiv source package contains TeX and figures only. |
| Kinematic coefficient using `x=1.3`, `alpha≈2.4` | `DOCUMENTED` for Singal’s paper | Singal states these values and attributes `alpha` to the uncorrected Mittal analysis. [3] |
| Compatibility with corrected Mittal null | `UNDOCUMENTED` | Singal does not incorporate the later corrected spectral-index distribution and expectations. [2][3] |

## 4. Which exact products can we obtain?

Obtained and checksum-verified from Quaia `0.1.0`:

- `quaia_G20.0.fits` — MD5 `42cec6519d139ac5fdcf4f891a68b5d4`; SHA-256 `87b03f9dc9bd5105c9df85574a890a269a7d404392b3907d15c790082bbf2ef1`.
- `quaia_G20.5.fits` — MD5 `8b816b719e8c8ccd1c0a648b53557ddd`; SHA-256 `918fbac2aa6303ff627ad356a1663c3401f8326240fbd75c22b29c38ea915a6d`.
- `selection_function_NSIDE64_G20.0.fits` — MD5 `e62df7437156763ee59210976a808e45`; SHA-256 `f51b40b4ec42bec91f0e8972515247ea6cb06c0c77b6d9af4b97beddb71aa887`.
- `selection_function_NSIDE64_G20.5.fits` — MD5 `d327cafb2011ac4a4ceafb57e7b553f3`; SHA-256 `24e24bab959806c95ec8330993e4a6a33af053ad8615f7950341a2ea57814cd4`.

The `0.1.0` random products are also public and exactly identified, but neither paper uses them:

- `random_G20.0_10x.fits` — MD5 `c5d5240d8bf72dbf1d19eebee9dddf2`.
- `random_G20.5_10x.fits` — MD5 `ba9f7f1428ab27cb28b13e8b4b488457`. [4]

Exact binary receipt: `TORI_QUAIA_V0P1_EXACT_PRODUCT_CUSTODY_RECEIPT_20260811T1122K.json`.

What cannot be obtained from the public paper packages:

- Mittal’s self-bound input manifest;
- either analysis codebase;
- exact mask membership files;
- Mittal’s sampler configuration and seeds;
- Singal’s exact mask-amplitude correction implementation;
- either paper’s final analyzed-row manifest;
- an immutable coupling between Mittal’s selection-map bytes and its unstated native coordinate convention.

The four arXiv source packages were inspected mechanically and contain no Python, notebook, R, Julia, C/C++, Fortran, MATLAB, or shell analysis files. See `TORI_ARXIV_SOURCE_PACKAGE_CUSTODY_RECEIPT_20260811T1120K.json`.

## 5. What is recoverable from stated methods?

`DOCUMENTED` stated differences:

1. Mittal applies selection values inside both likelihood formulations; Singal omits the selection function. [1][3]
2. Mittal uses Bayesian Poisson and point-by-point likelihoods; Singal uses vector/hemisphere/count-asymmetry methods. [1][3]
3. Mittal selects Quaia low with the 40-degree mask for its principal interpretation; Singal reports a nominally matched `G<20.0`, `|b|>40` row as well as other cuts. [1][3]
4. Mittal’s current corrected kinematic null differs from the uncorrected spectral-index input inherited by Singal. [2][3]
5. Neither study uses a redshift cut. [1][3]

`UNDOCUMENTED` causal claims:

- “The entire factor of three is caused by the selection function.”
- “The entire factor of three is caused by mask leakage or the estimator.”
- “The papers compare identical analyzed row sets.”
- “The current papers use the same kinematic null.”

Singal’s own wording is explicitly tentative: the selection procedure “might be the reason” for the difference. [3]

Because the papers change selection treatment, estimator, cut-sky correction, and versioned kinematic null together, they do not provide a one-choice-at-a-time comparison. The unavailable code and exact run receipts prevent custody-grade re-creation of either published pipeline.

## 6. Crew-claim reconciliation

- Lana’s finding that the explicit selection-function fork is important is supported, but “the entire factor of three” is stronger than the papers establish.
- Kun’s adversarial conclusion—that the stated fork is readable but causal attribution is not recoverable from reading alone—is supported by the custody record.
- `HWAO_LOOSENED_BAR_MITTAL_SINGAL_ASSESSMENT_20260811T1110K.md`, SHA-256 `1bdf7d66fc3168d2db7a54632a411024b564f4acd0328c6dbb43c86b89a0c25d`, is non-authoritative. It incorrectly calls Mittal’s estimator “Bayesian spherical harmonic,” incorrectly says Singal’s magnitude cuts are unstated, omits Singal’s 35- and 40-degree cuts, and omits the explicit selection-function fork. [1][3]
- The distinct Goru facts artifact required by the order was not present in the handoff root at this gate; the current Hwao assessment cannot substitute for it because it contains the errors above.

## Final custody answer

The best evidence says both original analyses used Quaia `0.1.0`; a `0.1.0` versus `1.0.0` release mismatch is not the factor-of-three explanation.

The exact public catalogue and selection-map candidates are obtainable. Randoms are obtainable but irrelevant because neither paper uses them.

What is not recoverable is the complete published execution identity and therefore the causal decomposition of the amplitude gap. The papers establish a disputed selection-function/estimator/mask complex, not which component quantitatively causes the published difference.

**Current disposition: fifth honest closure for reading-only causal adjudication.**

No design, run, statistic, result, publication, lane unlock, or acceptance occurred. Nothing is accepted without Duho.

## Sources

[1] https://arxiv.org/pdf/2311.14938v1 — Mittal et al. original arXiv v1 PDF
[2] https://arxiv.org/pdf/2311.14938v2 — Mittal et al. arXiv v2 with published correction
[3] https://arxiv.org/pdf/2403.16581v2 — Singal 2024 arXiv v2 PDF
[4] https://zenodo.org/api/records/8060755 — Quaia 0.1.0 exact Zenodo record
[5] https://zenodo.org/api/records/10403370 — Quaia 1.0.0 exact Zenodo record
[7] https://arxiv.org/abs/2311.14938 — Mittal arXiv version history
[8] https://arxiv.org/abs/2403.16581 — Singal arXiv version history
