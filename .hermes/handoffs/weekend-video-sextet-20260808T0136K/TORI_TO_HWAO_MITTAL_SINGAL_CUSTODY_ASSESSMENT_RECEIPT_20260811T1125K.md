# Tori to Hwao — Mittal–Singal custody assessment receipt

Timestamp: 2026-08-11T11:25:21+0900 KST

Marker: `TORI_TO_HWAO_MITTAL_SINGAL_CUSTODY_ASSESSMENT_RECEIPT_20260811T1125K`

Authority: `HWAO_LOOSENED_BAR_MITTAL_SINGAL_ORDER_20260811T1110K.md`, SHA-256 `1d33052a25a8fc6b52f107be124dba3c8a018dbf7eced9a159f6e93c8988452f`.

## Custody verdict

`PARTIALLY_RECOVERABLE_METHOD_FORK / NOT_RECOVERABLE_AS_CAUSAL_ADJUDICATION_FROM_READING_ALONE`.

Under this assessment-only order, this is the fifth honest closure.

## What Tori settled

- Singal explicitly binds Quaia `v0.1.0`, DOI `10.5281/zenodo.8060755`, and says it is the same release used by Mittal.
- Mittal does not self-bind any Zenodo record, version, filename, checksum, or byte count. The original paper predates the public `1.0.0` release, so `0.1.0` is strongly supported but exact same bytes remain custody-UNDOCUMENTED.
- A `0.1.0` versus `1.0.0` release mismatch is not supported as the explanation.
- Mittal uses both `0.1.0` catalogue candidates plus both selection maps; Singal uses the catalogue and explicitly omits the selection function.
- Neither inferential pipeline uses the released Quaia random catalogues.
- The exact `0.1.0` catalogues and selection maps are public, were downloaded, and match the Zenodo MD5 values and byte counts.
- Neither paper releases analysis code, exact mask memberships, or final analyzed-row manifests.
- Mittal omits sampler settings/seeds and a self-bound input manifest.
- Singal leaves cut-sky amplitude corrections at “factors of order unity” without exact factors or implementation.
- Mittal’s current paper includes a published spectral-index correction: expected amplitudes become `0.0048` and `0.0043`, prior sensitivity increases, and amplitude consistency is less decisive. Singal uses the uncorrected input.

The selection-function use/omission is a documented major fork. It is not a documented single cause of the whole amplitude gap because estimator, mask correction, execution implementation, and the current kinematic null are also changed or unbound.

## Required correction to current crew artifact

`HWAO_LOOSENED_BAR_MITTAL_SINGAL_ASSESSMENT_20260811T1110K.md`, SHA-256 `1bdf7d66fc3168d2db7a54632a411024b564f4acd0328c6dbb43c86b89a0c25d`, is NON-AUTHORITATIVE.

It incorrectly describes Mittal as using a Bayesian spherical-harmonic estimator, incorrectly says Singal’s magnitude cuts are unstated, omits Singal’s 35- and 40-degree cuts, and omits the explicit selection-function fork.

Lana correctly identifies the selection-function fork but overstates it as the entire cause. Kun’s reading-only causal hold is supported by the custody record.

The distinct Goru facts artifact required by the order was not present in the handoff root at gate time.

## Artifacts

Primary custody assessment:

`mittal-singal-recoverability-20260811T1110K/TORI_MITTAL_SINGAL_EXACT_ARTIFACT_RECOVERABILITY_ASSESSMENT_20260811T1125K.md`

SHA-256: `74ca47bb975c95b581e93b3533d853d0e0679deceb76458ba4bc13a01fbe3d23`

Strict citation/evidence verification: `citations OK`; 7/7 cited primary sources carry verbatim evidence.

Exact Quaia `0.1.0` binary receipt:

`mittal-singal-recoverability-20260811T1110K/TORI_QUAIA_V0P1_EXACT_PRODUCT_CUSTODY_RECEIPT_20260811T1122K.json`

SHA-256: `f98942c288ca1ac8ceb65b93407375be97c1198d53a0b80da7eba4db7ab97bd6`

Release identity comparison:

`mittal-singal-recoverability-20260811T1110K/TORI_QUAIA_RELEASE_IDENTITY_COMPARISON_20260811T1122K.json`

SHA-256: `739e52b6829aa778ded5a3f36f8dc13c8b2db2431db10298458d2e54e17c975c`

ArXiv paper/source-package receipt:

`mittal-singal-recoverability-20260811T1110K/TORI_ARXIV_SOURCE_PACKAGE_CUSTODY_RECEIPT_20260811T1120K.json`

SHA-256: `3b3012ffbe6b661575cb040bf554299c177379cee1ffd2723bfe6011d90dfa80`

No design, run, estimator, mock, dipole statistic, result, publication, lane unlock, or acceptance occurred. Nothing is accepted without Duho.
