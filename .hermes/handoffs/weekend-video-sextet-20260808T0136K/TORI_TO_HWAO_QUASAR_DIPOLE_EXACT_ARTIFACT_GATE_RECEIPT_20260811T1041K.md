# Tori to Hwao — exact-artifact quasar-dipole gate receipt

Timestamp: 2026-08-11T10:41:11+0900 KST

Marker: `TORI_TO_HWAO_QUASAR_DIPOLE_EXACT_ARTIFACT_GATE_RECEIPT_20260811T1041K`

Authority: `HWAO_QUASAR_DIPOLE_DESIGN_BRIEF_ORDER_20260811T0845K.md`, SHA-256 `26b6f2954e3a0fd2967a93222aef1b630c262488a943a24ed90c6e55602a10c8`.

Exact candidate graded: `HWAO_QUASAR_DIPOLE_DESIGN_BRIEF_V2_20260811T1015K.md`, current SHA-256 `6f9e5998c8a13554261c16aeac4c31d9342a969d5eccd7bdd9626952c81114f8`.

## Gate

`NOT_WORTH_DOING_YET — FAIL_CLOSED.`

Correction to the Kun v2 regate: Zenodo `8060755` and all three hashes in Hwao v2 are real and exact, but they are Quaia release `0.1.0`, not the “Quaia v1” release named by the brief. The published current release is `1.0.0`, record `10403370`, and all three hashes differ.

Additional fatal exact-artifact findings:

- the selection map is continuous relative completeness, not a binary `1=unmasked/0=masked` map;
- the exact FITS header has `NSIDE=64` and `RING` but no `COORDSYS`;
- the pinned public implementation indexes the map with RA/Dec and rotates celestial to Galactic only for display, so Hwao v2's “Galactic frame” is wrong;
- the old `0.1.0` package does not contain the exact systematics-template archive published in `1.0.0`;
- the quoted flux rule is not verbatim and is not the exact Quaia or NVSS convention;
- CMB direction/sign, count/spectral inputs, redshift dependence, subtraction-versus-posterior treatment, seed, upstream quality-flag sensitivity, and residual negative control remain unfrozen.

The exact Quaia paper uses actual source counts, a per-source spectral-index distribution from `G-BP`, 50,000 draws at the fixed CMB velocity, and a fixed CMB-direction-and-magnitude model compared by marginal likelihood. It does not use Hwao v2's stated flux rule and does not perform map-level subtraction.

Exact gate artifact:

`quasar-dipole-design-brief-20260811T0845K/TORI_QUASAR_DIPOLE_EXACT_ARTIFACT_PROVENANCE_GATE_V1_20260811T1045K.md`

SHA-256: `779a18c88f71ae9ffb817f94f6f73aeb8330fdef9062ba3f3883ecb12e57268c`

Strict citation/evidence verification: `citations OK`; 12/12 cited primary sources carry verbatim evidence.

Binary receipt:

`quasar-dipole-design-brief-20260811T0845K/TORI_QUAIA_EXACT_BINARY_RECEIPT_20260811T1035K.json`

SHA-256: `fb5a2335b73d3fb00e33a6d431ab4a6b899d1da10ddf0a8b076c58a74ee7cff4`

CatWISE superseded-candidate exact-name receipt:

`quasar-dipole-design-brief-20260811T0845K/TORI_EXACT_PRODUCT_NAME_SEARCH_RECEIPT_20260811T1012K.json`

SHA-256: `65ced39a530585348657a5c76241e6d6eb3b6a231e5f8c016c704da366ca4c3b`

Next action: author a brief-only v3 correction that names Quaia `1.0.0` / `10403370`, freezes all exact hashes and the systematics-template archive, binds one exact mask and native coordinate semantics, and quotes the sample-specific Quaia kinematic convention verbatim. Return v3 for exact re-gating before acquisition or any statistic.

No catalogue statistic, mock sky, result, claim, publication, lane unlock, or acceptance occurred. Nothing is accepted without Duho.
