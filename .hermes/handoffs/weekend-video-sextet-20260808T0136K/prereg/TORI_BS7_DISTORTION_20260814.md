# Tori BS-7 distortion branch — DR10.1 South

Recorded: 2026-08-14

## Verdict

**PASS — one branch declared and its receipts pass.**

## The one declared branch

**FAIL_CLOSED.** The local-Jacobian branch is not selected and is not implemented.

Frozen PC-4 text, verbatim from `PREREG_LONGO_AMPLITUDE_TEST_20260812.md`:

> - **PC-4** **Distortion policy (branch declared at BS-7):** fail closed on SIP/PV/CPDIS/DET2IM
>   keywords, **or** tested local Jacobian-sign receipts across the cutout. **No silent
>   linear-determinant fallback** (frozen).

Operational rule for every future delivered FITS product: reject before any object-level statistic if SIP, PV, CPDIS, or DET2IM metadata is present; also reject non-celestial, partial, singular, or numerically indeterminate WCS. There is no silent linear-determinant fallback. A clean prior example does not waive the per-product check.

## Actual survey WCS convention — primary documentation

Primary source: https://www.legacysurvey.org/dr10/description/ [2]

> For all of the DESI Legacy Imaging Surveys, coadded images and
> Tractor catalogs are presented in "bricks" of approximate
> size 0.25° × 0.25°. Each brick is defined in terms of a box in RA,Dec
> coordinates. The [image stacks](https://www.legacysurvey.org/dr10/files/#image-stacks-south-coadd) use a simple tangent-plane (WCS TAN)
> projection around the brick center. The projections for the g,r,i,z filters are identical, with
> a pixel scale of 0.262″/pix. The projections for the four WISE filters are also identical
> but with a pixel scale of 2.75″/pix.

Primary source: https://www.legacysurvey.org/dr10/files/ [3]

> Image stacks are on tangent-plane (WCS TAN) projections, 3600 × 3600 pixels, at 0.262 arcseconds per pixel.\

These statements support a TAN/CD-or-PC×CDELT route. They do not prove that every generated future header is free of distortion metadata, which is why the selected branch remains fail-closed per product.

## Bound-route receipt

Existing metadata-only route receipt: `_tori_survey_route_binding_evidence/legacy_dr10_south_header_verification_r_16px.receipt.json`

- receipt SHA-256: `a573d8993b40cfbde143f9bd653cf7579dc1e73467a04fb9ed36b716efbc77e6`;
- retained product SHA-256: `ac212f9d9003688a266273452b22385d8e13a9d613bbc4a873291ff544e1c24c`;
- CTYPE: `RA---TAN`, `DEC--TAN`;
- CD determinant independently recomputed from the receipt: `-5.296604938271607e-09`;
- parity: `REVERSING`;
- distortion families found: none;
- status under the selected branch: `PASS`.

No FITS image was opened for this BS-7 task. The already-existing JSON receipt was hash-verified and evaluated.

## Fail-closed detector receipt

Machine receipt: `_tori_bs7_distortion_evidence/FINAL_DISTORTION_BRANCH_RECEIPT.json`

- SHA-256: `64a7f2ed61a5faad5c289e5a5293ff67bc493d0d92883ec6effaad580602419a`;
- status: `PASS`;
- declared branch: `FAIL_CLOSED`;
- local-Jacobian branch selected: `false`;
- future per-product audit required: `true`;
- new network requests: `0`;
- images opened: `0`.

Synthetic-only contract test: `_tori_bs7_distortion_evidence/test_fail_closed_wcs.py`, SHA-256 `5d48194d331bac54160fb73dab820286a3e40ffb5f0f053f9f8983cf00c4e2e9`.

Implementation: `_tori_bs7_distortion_evidence/fail_closed_wcs.py`, SHA-256 `cae1b1b7ef4e25000ad5d8c906647216b1425638ac737b4ea7363ca948760569`.

Test result: `bs7_fail_closed_contract=PASS synthetic_cases=10 new_images=0 new_requests=0`. It covers clean CD/TAN, complete PC×CDELT/TAN, SIP, PV, CPDIS, both D2IM and DET2IM spellings, singular CD, incomplete linear WCS, and non-celestial CTYPE.

## Input pins

- Controlling brief SHA-256: `6431f9cf56fc4732162059e08a97b944a48d2b8ad79dd560d1747342b0c9e190`.
- Frozen preregistration SHA-256: `ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590`.
- Bound route receipt SHA-256: `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87`.
- Prior machine header receipt SHA-256: `a573d8993b40cfbde143f9bd653cf7579dc1e73467a04fb9ed36b716efbc77e6`.
- DR10 description source copy SHA-256: `ef77ba7682239ff129c041f4da0fa59a8bc26b423e560747df50f977a55559c2`; accessed 2026-08-14.
- DR10 files source copy SHA-256: `82ab89c527c58ecca33f8c7757d02e93bf6a4e1557138c5df6166ffa1636a3e2`; accessed 2026-08-14.
- Citation ledger: `_tmp_bs1247_citations.json` (source IDs [2] and [3]).

## Boundary

Documentation and synthetic WCS dictionaries only. New data-product requests: 0. Images opened: 0. Object rows: 0. Positions: 0. Chirality/morphology labels: 0. Sky statistics: 0. Publication, acceptance, commit, or push: none.

## Sources

[2] https://www.legacysurvey.org/dr10/description
[3] https://www.legacysurvey.org/dr10/files
