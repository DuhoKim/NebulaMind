# Tori survey-route custody binding — DESI Legacy DR10.1 South for the Longo-amplitude test

**Tori (access/orientation-custody seat), 2026-08-12.**  This is a preregistration-input
custody receipt.  It selects and names one survey product route; it is not an empirical run,
a result, a publication, scientific acceptance, or permission to begin any of those things.

> **BOUND PRODUCT ROUTE:** the current DESI Legacy Imaging Surveys **DR10.1 southern
> (DECam) route**, using the `ls-dr10-south` generated FITS-cutout product as the measurement
> pixels and the updated DR10.1 southern sweeps and matched products as the source/covariate
> catalogue route.
>
> **KUN FREEZE CONDITION 2:** **PARTLY CLOSED, NOT CLOSED.**  This Tori custody receipt now
> exists.  A revised file titled `GORU_ACCEPTED_YIELD_RECEIPT_20260812.md` also exists, but it still
> marks every cut-survival count `[UNKNOWN — requires catalog query]`.  Kun's gate rule is explicit:
> if `[UNKNOWN]` remains, BS-1 remains open.  The claimed `~175,000` accepted yield remains an
> assumption-chain output, not a measured or documented DR10.1 product count; Kun has not yet
> hash-gated Goru's latest revision.
>
> **EMPIRICAL STATUS:** **BLOCKED.**  No real-galaxy query, parent count, image request beyond
> the single header-only verification request recorded in §6, chirality computation, sky
> statistic, result, publication, or accepted status is authorized.

The title deliberately says **“Longo-amplitude test.”**  This artifact is not titled or framed
as a general spin-anisotropy test, in accordance with Kun's V2 ruling.

## 0. Custody scope; Lana's repair is an independent parallel lane

This receipt does **not** carry Lana's boundary sentence forward, does not derive from that
sentence, and is not gated on the §0/§6 “verbatim” repair.  Per Duho's clarification, that repair
belongs to Lana and applies to the preregistration and later artifacts that quote or inherit the
boundary claim.  Lana's repair proceeds independently in parallel; this receipt makes no custody
claim about its completion.

The earlier version of this receipt incorrectly described Lana's repair as a prerequisite and
said this custody receipt derived from the repaired sentence.  That coupling is withdrawn here.
The only work bound by this receipt is the survey product route, access and licence terms,
WCS/parity and distortion branch, exact covariate-product availability, and the accepted-yield
premise audit.  Its “Longo-amplitude test” title follows Kun's separate naming condition; it does
not import or restate Lana's scientific boundary claim.

Kun's controlling regate is:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/KUN_SPIN_V2_REGATE_20260812.md`

SHA-256: `003779cd067686675562926b1e0fc04bb21f9d59027e0d55f059648fdbbcc404`.
Its scope is obeyed here: **“Preregistration drafting is authorized under my prior ruling.”**
Nothing empirical or public is inferred from that drafting authorization.

## 1. Why this route is bound on evidence

The earlier Tori access-custody audit compared HSC-SSP, DESI Legacy, SDSS, and Pan-STARRS:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/TORI_SPIN_DATA_ACCESS_CUSTODY_20260812.md`

SHA-256: `ba76df6c68a3b126878425358c55189ba3b151da69adeb05fcac7c05e924b1d7`.

DESI Legacy is selected here for product-custody reasons, not because it was inherited as a
favourite:

1. Its primary documentation names a public FITS cutout route and direct HTTPS product tree.
2. DR10 documents a simple TAN brick WCS, identical optical-band projections, and 0.262 arcsec
   pixels; the generated southern cutout route returned that structure in the one permitted
   verification request (§6).
3. The updated DR10.1 sweep route exposes stable row keys and every Legacy-side product needed
   by Lana's covariate list: depth, PSF size, SFD98 extinction, model size, model ellipticity,
   fluxes, mask bits, fit bits, and a row-matched photo-z product.
4. Its documented southern imaging footprint is large: DR10 reports 19,885 deg² with at least
   one r-band pass under the official southern definition and 15,342 deg² with at least one pass
   in all g,r,i,z bands.  This establishes a large product footprint, **not** a usable-parent or
   accepted-yield count.
5. In contrast, the earlier custody audit found that SDSS SkyServer image cutouts are transformed
   JPEGs unless a separate SAS FITS route is built, HSC access carries registration and
   non-commercial terms and had no locally testable header route, and Pan-STARRS carried WCS and
   practical-yield caveats.  Those routes are not selected here.

This comparison establishes that Legacy is the cleanest *documentable product route*.  It does
not establish that it yields 100,000 classifier-accepted galaxies; §8 records the contradiction
that prevents that inference.

## 2. Frozen survey and version identity

The chosen route is one route, not a mix of northern and southern layers:

- **Survey:** DESI Legacy Imaging Surveys.
- **Imaging release:** the current **DR10 southern DECam product tree**, including the DR10.1
  replacements described by the DR10 known-issues page.
- **Catalogue release:** **DR10.1**, identified by updated sweeps under `10.1/` and by catalogue
  `RELEASE` values `10000` (ordinary DR10 rows) and `10002` (rows updated in DR10.1).
- **Camera/filter mapping:** the release map documents `10000/10002` as DECam g,r,i,z primary
  imaging and WISE W1–W4 non-primary photometry.
- **Pipeline versions documented for the release:** LegacyPipe versions through `DR10.0.12`
  (per-file `LEGPIPEV` records the exact one), Tractor `dr10.1`, Astrometry.net
  `0.90-8-g575ad17b`, Astropy `5.0.4`, fitsio `1.1.6`, NumPy `1.21.2`.
- **Boundary:** do not merge in `ls-dr9-north`; do not use the composite `ls-dr10` layer that
  joins northern DR9 and southern DR10 at Dec = 32.375 degrees.

For route geometry only, Astropy's Galactic→ICRS transform maps Lana's frozen Longo direction
`(l,b)=(52°,68.5°)` to `(RA,Dec)=(216.984434295527°,32.060611193471°)` and its antipode to
`(36.984434295527°,-32.060611193471°)`.  Both declinations lie on the DR10-south side of the
documented 32.375° north/south seam.  This avoids an immediate layer-seam contradiction, but it
does not establish the actual selected-sample footprint variance around that axis; Kun's later
gate requires `var(cos theta)>=0.15` from real selected positions, which remains empirical and
uncomputed.

The known-issues page says that 598 `SUB_BLOB`-affected bricks were reprocessed in 2023, that
coadds and Tractor files were replaced, and that updated sweeps are in `10.1`, `10.1-extra`,
and `10.1-lightcurves`.  It recommends always using the latest versions.  It also says the
brick summary file was completely replaced in December 2023 after inaccurate source counts and
covariate columns were found.  Therefore a later authorized acquisition must use the current
files and SHA-pin every acquired product; stale `10.0` sweeps or pre-replacement brick summaries
are forbidden.

Primary URLs:

- release description: https://www.legacysurvey.org/dr10/description/
- file/product model: https://www.legacysurvey.org/dr10/files/
- Tractor/sweep schema: https://www.legacysurvey.org/dr10/catalogs/
- release-number map: https://www.legacysurvey.org/release/
- known issues and DR10.1 replacements: https://www.legacysurvey.org/dr10/issues/
- masks and fitting flags: https://www.legacysurvey.org/dr10/bitmasks/

## 3. Exact measurement-pixel product

### 3.1 Product and request template

The measurement pixels are the generated FITS product from:

`https://www.legacysurvey.org/viewer/fits-cutout`

with this frozen parameterization for a later authorized run:

`?ra=<DR10.1_RA>&dec=<DR10.1_DEC>&layer=ls-dr10-south&pixscale=0.262&bands=grz&size=256`

Frozen meanings:

- `ra`, `dec`: the DR10.1 sweep row coordinates for the same
  (`RELEASE`, `BRICKID`, `OBJID`) object;
- `layer=ls-dr10-south`: southern DECam DR10/DR10.1 only;
- `pixscale=0.262`: the documented optical brick scale in arcsec/pixel;
- `bands=grz`: exactly g, r, and z, in that order; i and WISE are not measurement channels;
- `size=256`: a square 256×256 analysis raster per optical band;
- response format: FITS only, never JPEG/PNG;
- no post-delivery rotate, reproject, interpolate, resize, or WCS transform;
- the delivered FITS planes in FITS-native row order are the final analysis raster;
- the mirror operation is a byte-exact pixel-index reversal on that raster only.

The service supports explicit band strings and explicit square sizes; its documented maximum is
512 pixels.  The release description says `pixscale=0.262` returns approximately the native
pixels used by Tractor.  “Approximately native” is not treated as raw detector custody: the
**delivered generated TAN pixels are the measurement product**, exactly as Lana V2 §4.3 requires.

The underlying current coadd product family is:

`https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/<AAA>/<brick>/legacysurvey-<brick>-image-<filter>.fits.fz`

Product name: `legacysurvey-<brick>-image-<filter>.fits.fz`, for filters g, r, z.  The file page
states that the primary HDU is an inverse-variance-weighted coadd in nanomaggies/pixel, covering
0.25°×0.25°, and that it was resampled upstream with Lanczos-3.  This upstream resampling is
accepted only because the delivered cutout plus WCS is defined as the measurement input.  It is
never repeated downstream.

Related pixel-custody products, to be acquired only under a future explicit empirical gate, are:

- `legacysurvey-<brick>-invvar-<filter>.fits.fz` — inverse variance;
- `legacysurvey-<brick>-maskbits.fits.fz` — optical `MASKBITS` in HDU1;
- `legacysurvey-<brick>-nexp-<filter>.fits.fz` — contributing unmasked exposure count;
- `legacysurvey-<brick>-psfsize-<filter>.fits.fz` — weighted PSF FWHM in arcsec.

They are quality/custody inputs, not chirality pixels.  Their exact hashes would have to be pinned
with the future object manifest.

### 3.2 Account, licence, credit, and citation terms

The Viewer and NERSC product URLs are public HTTPS routes.  The documentation's “For Web Access”
paths and the successful anonymous header verification required no account, credential, token,
or click-through registration.  No separate catalogue licence was found on the primary DR10 file
or catalogue pages; absence of a displayed catalogue licence is not rewritten here as a broader
licence grant.

For Sky Viewer images, the Legacy acknowledgment page states exactly:

> “Images are licensed under a Creative Commons Attribution 4.0 International License, and hence
> may on a non-exclusive basis be reproduced without fee provided the credit is clear and visible.”

It requires the unaltered visible credit:

> “Legacy Surveys / D. Lang (Perimeter Institute)”

For papers using Legacy Survey data, the same page says:

> “When using data from the Legacy Surveys in papers, please use the following acknowledgment:”

The complete required acknowledgment is maintained at:
https://www.legacysurvey.org/acknowledgment/#scientific-publication-acknowledgment

If DR10.1 photo-z sweeps are used, the file page additionally requires citation of Zhou et al.
(2023), in this exact instruction:

> “Work which uses the photometric redshift sweeps should cite Zhou et al. (2023) and include the
> additional acknowledgment for photometric redshifts.”

The additional acknowledgment is at:
https://www.legacysurvey.org/acknowledgment/#photometric-redshifts

The primary DR10 files/catalogue pages did not supply a separate catalogue-licence statement.
The Viewer image CC BY 4.0 statement is therefore **not** silently extended to derived catalogues.
Permission/terms sufficient for later derived-catalogue publication remain an open freeze item,
matching Kun's later requirement.  No publication is authorized here.

These are future-use obligations only.  Nothing is being published by this receipt.

## 4. Exact catalogue and join products

### 4.1 Parent and covariate catalogue

Use the updated DR10.1 sweep files:

`https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.1/sweep-<brickmin>-<brickmax>.fits`

Product name: `10.1/sweep-<brickmin>-<brickmax>.fits`.
The files are lightweight FITS binary tables containing common Tractor measurements for
`BRICK_PRIMARY==T` objects.  The stable row identity is the three-column key:

`(RELEASE, BRICKID, OBJID)`.

No coordinate-only join is allowed when a row-key join exists.

Use the row-matched redshift product:

`https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.1-photo-z/sweep-<brickmin>-<brickmax>-pz.fits`

Product name: `10.1-photo-z/sweep-<brickmin>-<brickmax>-pz.fits`.
The documentation says it is row-by-row matched to the DR10.1 sweeps.  It provides `Z_SPEC`,
`SURVEY`, `Z_PHOT_MEAN`, `Z_PHOT_MEDIAN`, uncertainty intervals, and i-band variants.  It fills
photo-z values with `-99` when its exposure requirements are not met, does not itself perform
star/galaxy separation, and warns that objects fainter than z≈21 become increasingly unreliable.
Those are selection/yield facts that Goru's 2,000,000 parent estimate did not count.

A later accepted-yield receipt must freeze which redshift field, validity/uncertainty rule,
brightness rule, and star/galaxy cut are used before counting any row.  This receipt does not
silently choose them because doing so and counting real objects is the now-reached empirical
boundary.

### 4.2 Brick summary product

Use only the current replacement of:

`https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/survey-bricks-dr10-south.fits.gz`

Product name: `survey-bricks-dr10-south.fits.gz`, current post-December-2023 replacement.
Join by `BRICKNAME`/`BRICKID` after verifying the mapping.  The original release file is forbidden
because the known-issues page says its source counts and multiple environmental columns were
inaccurate and it was completely replaced.

## 5. Covariate product matrix

Every named requirement exists, with one important version distinction: Legacy's embedded Gaia
reference fields are **Gaia EDR3**, not the required Gaia DR3 density product.  Gaia DR3 must be
obtained independently from the exact ESA table below; the embedded EDR3 columns are not an
allowed substitute.

| Required quantity | Frozen product/version and fields | Existence/status |
|---|---|---|
| Imaging depth | current `survey-bricks-dr10-south.fits.gz`, `psfdepth_r`: median 5σ r-band PSF detection depth in AB mag per brick | **EXISTS**; use post-Dec-2023 replacement only |
| Seeing / PSF size | same product, `psfsize_r`: median r-band PSF size in arcsec per brick | **EXISTS**; use post-Dec-2023 replacement only |
| SFD98 extinction | DR10.1 sweep `EBV` per object, explicitly SFD98 E(B−V); `MW_TRANSMISSION_G/R/Z` are derived linear transmissions | **EXISTS**; cite Schlegel, Finkbeiner & Davis 1998; do not replace with another dust map |
| Gaia DR3 counts | ESA Gaia Archive table `gaiadr3.gaia_source`, fields `source_id`, `ra`, `dec`, `phot_g_mean_mag`; count `phot_g_mean_mag < 19` in the preregistered Nside=128 cells | **EXISTS EXTERNALLY**; Legacy's own Gaia columns are EDR3 and are **NOT** the required version |
| Half-light radius | DR10.1 sweep `SHAPE_R` in arcsec for the selected galaxy `TYPE` | **EXISTS** |
| Axis ratio | DR10.1 sweep `SHAPE_E1`, `SHAPE_E2`; derive `e=sqrt(E1²+E2²)`, `b/a=(1-e)/(1+e)`; non-finite values or `e>=1` fail the shape-validity rule | **EXISTS as a deterministic derived field**; no native `b/a` column |
| Colour | DR10.1 sweep `FLUX_G`, `FLUX_R`, `MW_TRANSMISSION_G`, `MW_TRANSMISSION_R`; extinction-corrected AB `g-r` from `flux/transmission` using `m_AB=22.5-2.5 log10(nanomaggy)` | **EXISTS as a deterministic derived field** |
| Magnitude | DR10.1 sweep `FLUX_R`, `MW_TRANSMISSION_R`; extinction-corrected r-band AB magnitude by the same formula | **EXISTS as a deterministic derived field** |
| Crowding proxy | DR10.1 sweep `RA`, `DEC`; neighbour count within 30 arcsec after a frozen catalogue-quality selection | **FIELDS EXIST**; the quality selection and actual count remain unexecuted |
| Deblend/fit quality | DR10 `MASKBITS` and `FITBITS`; names and bit meanings are frozen by the DR10 bitmask page and LegacyPipe `DR10.0.12` definitions | **EXISTS**, but no single native “deblend quality” scalar exists; exact excluded bits must be frozen before counting |
| Photo-z | DR10.1 `10.1-photo-z/*-pz.fits`, joined by `(RELEASE,BRICKID,OBJID)` | **EXISTS**, with `-99`, exposure, reliability, and star/galaxy caveats |

Gaia DR3 access is the public/anonymous TAP endpoint:

`https://gea.esac.esa.int/tap-server/tap`

The exact table is `gaiadr3.gaia_source`.  ESA documents both anonymous and registered access;
registration is unnecessary for public queries, while persistent private jobs/tables require an
account.  Gaia data are distributed under **CC BY-NC 3.0 IGO**; commercial use is subject to ESA
archive terms.  The Gaia DR3 credit instructions require this acknowledgment:

> “This work has made use of data from the European Space Agency (ESA) mission Gaia
> (https://www.cosmos.esa.int/gaia), processed by the Gaia Data Processing and Analysis Consortium
> (DPAC, https://www.cosmos.esa.int/web/gaia/dpac/consortium). Funding for the DPAC has been
> provided by national institutions, in particular the institutions participating in the Gaia
> Multilateral Agreement.”

They also require citation of the Gaia mission paper and Gaia DR3 release paper.  Sources:
https://gea.esac.esa.int/archive/documentation/GDR3/Miscellaneous/sec_credit_and_citation_instructions/
and https://www.cosmos.esa.int/web/gaia-users/license .

No Gaia rows were queried for this receipt.

## 6. WCS, parity, and Kun freeze condition 7

### 6.1 Documented WCS situation

The DR10 description says the g,r,i,z brick image stacks use a simple tangent-plane **WCS TAN**
projection around each brick center, that their optical projections are identical, and that the
pixel scale is 0.262 arcsec/pixel.  The coadd image documentation says those images were already
resampled upstream with Lanczos-3.  The route therefore does not pretend to preserve detector
pixels: the generated FITS cutout and its delivered WCS are the orientation-custodied measurement
input.

### 6.2 Frozen branch: fail closed on distortion

This route selects Kun's **fail-closed-on-distortion branch**.  It does **not** select or implement
a tested-local-Jacobian branch.

For every later requested FITS product, before pixels can enter an instrument:

1. parse the delivered celestial WCS;
2. reject partial, singular, numerically indeterminate, or non-celestial WCS;
3. search for SIP (`A_*`, `B_*`, `AP_*`, `BP_*` and order cards), PV, CPDIS, and DET2IM
   distortion metadata;
4. if any distortion metadata is present, **halt the route before any object-level statistic**;
   do not silently use a linear determinant and do not merely drop the object;
5. if no distortion is present, compute the sign of the full 2×2 `CD` matrix, or `PC×CDELT`
   when that is the complete representation;
6. preserve FITS-native row order and record the array-transform determinant;
7. record the combined pixel-to-sky parity in the per-product manifest;
8. require identical delivered WCS geometry across g,r,z planes; any discrepancy halts the route.

A determinate positive or negative linear determinant is not itself a pass/fail preference: it
means preserving or reversing, respectively, and the sign is carried explicitly into the
orientation dictionary.  The fail condition is ambiguity, unsupported distortion, or silent
array transformation.

The checker and test receipt already established these semantics in:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/TORI_PIXEL_PATH_AUDIT_20260812.md`

SHA-256: `b711b7305c3512ce71821174bcc1a7fc6f18eb6fe303107d0fedf8c3d48db266`.

### 6.3 One permitted route-specific header request

The prior retained test file used the composite `ls-dr10` layer.  The exact bound product class
was `ls-dr10-south`, so one small request was genuinely needed to establish its header structure.
No catalogue row, galaxy candidate, or morphology was selected.  The documentation's example
coordinate was used solely for a 16×16 r-band header check:

`https://www.legacysurvey.org/viewer/fits-cutout?ra=190.1086&dec=1.2005&layer=ls-dr10-south&pixscale=0.262&bands=r&size=16`

Frozen local evidence:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_survey_route_binding_evidence/legacy_dr10_south_header_verification_r_16px.fits`

- bytes: `5760`;
- SHA-256: `ac212f9d9003688a266273452b22385d8e13a9d613bbc4a873291ff544e1c24c`;
- data shape/dtype: `16×16`, `>f4`;
- `CTYPE1='RA---TAN'`, `CTYPE2='DEC--TAN'`;
- `CRVAL=(190.1086, 1.2005)`, `CRPIX=(8.5, 8.5)`;
- `CD=[[-7.27777777777778e-05,0],[0,7.27777777777778e-05]]`;
- determinant: `-5.2966049382716104e-09`;
- linear WCS parity: **REVERSING**;
- SIP/PV/CPDIS/DET2IM keys found: none;
- FITS-native array transform determinant: `+1`;
- combined mapping parity: **REVERSING**;
- chirality computed: `false`;
- sky statistic computed: `false`.

Machine-readable receipt:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_survey_route_binding_evidence/legacy_dr10_south_header_verification_r_16px.receipt.json`

SHA-256: `a573d8993b40cfbde143f9bd653cf7579dc1e73467a04fb9ed36b716efbc77e6`.

This one header proves that the named route can deliver the expected determinate TAN form.  It is
**not** extrapolated into a claim that every future cutout has the same header.  That is why the
per-product fail-closed audit is part of the bound route.

## 7. Quality products and known product exclusions

The exact DR10 mask definitions exist, but this route receipt does not invent population cuts that
Goru did not count.  The future yield preregistration must name excluded bits.  At minimum it must
decide, before counting, how to handle:

- `MASKBITS`: `BRIGHT`, band saturation, `ALLMASK_*`, `BAILOUT`, `MEDIUM`, `GALAXY`,
  `CLUSTER`, `SUB_BLOB`, and the i-band equivalents;
- `FITBITS`: radius/Sérsic limit hits, frozen sources, bright/medium/Gaia/Tycho flags,
  large-galaxy fits, walkers/runners, and iterative detections;
- invalid or missing `SHAPE_R/E1/E2` and inverse variances;
- the 52 large galaxies documented as missing from the SGA version used during DR10 processing;
- the documented duplicate Gaia `ref_id` issue;
- the documentation warning that headers may disagree with catalogue values for about 2% of
  Tractor bricks due to files changing during rsync.

These are real product-level cuts or caveats.  None appears in Goru's 2,000,000-parent arithmetic.
Their yield effect is therefore unknown, not zero.

## 8. Contradiction audit of Goru's `~175,000`

Goru's original feasibility source artifact is:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/GORU_SAMPLE_FEASIBILITY_20260812.md`

SHA-256: `8cde575b324f64a90536212e7dab3fcce82f95adf2e64eeb3fdfba2086ecb041`.

A later artifact arrived while this receipt was being verified and was then revised in place:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GORU_ACCEPTED_YIELD_RECEIPT_20260812.md`

Current SHA-256: `df08a525ef7fbff4bae9dc0069b6d3cbda653454c678ccd00361e88dac654476`
(5,384 bytes; modification time 2026-08-12 12:57:16 KST).  This revision corrects several
query-plan defects: it is south-only, selects `maskbits==0`, selects `r<17.7`, requires
`0<=Z_PHOT_MEDIAN<0.15` so missing-value sentinels do not pass, and requires `FLUX_R>0` so
zero-optical-flux `DUP` rows do not survive merely because `TYPE!='PSF'`.

Those are useful repairs, but they do not change the yield verdict.  Every surviving count,
including the final parent, is still `[UNKNOWN — requires catalog query]`.  The initial
`~2.8 billion` is explicitly a full-survey count, not a DR10.1-south parent count.  The revision
still calls `BRICK_PRIMARY==T` a duplicate-removal cut even though documented sweeps already
contain only `BRICK_PRIMARY==T` rows.  It still has no counted all-band/exposure, inverse-variance,
shape-validity, PSF-relative resolution, cutout-delivery, WCS-pass, or covariate-coverage losses;
no selected-footprint `var(cos theta)`; and no measured production-estimator retention.  It then
uses external spiral/inclination/classifier priors plus a footprint analogy to call N=100,000
“plausible.”  That remains a query plan and assumption audit, not an accepted-yield receipt.

Kun gated the earlier incoming revision in:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/KUN_PREREG_DRAFT_GATE_20260812.md`

SHA-256: `5d726380d64e34a1188a5bfb0b080962008bc80746e86fc5e39bde75a6264dff`.
That gate predates Goru's 12:57 revision and therefore is **not** a hash-bound review of the current
Goru bytes.  Its controlling rule is nevertheless explicit and directly testable: “If the receipt
still says `[UNKNOWN]`, BS-1 remains open.”  The current revision still says `[UNKNOWN — requires
catalog query]` after every cut.  Kun's gate also requires actual surviving counts, footprint
variance around Longo's axis, measured production-estimator retention, publication-permitting
licence terms, and a hashed rerunnable query/code receipt.  The current revision supplies none of
those.  This receipt therefore preserves `HOLD FREEZE` without claiming Kun re-gated the revision.

Its Legacy chain is arithmetically correct given its inputs:

`2,000,000 × 0.25 × 0.70 × 0.50 = 175,000`.

But its inputs are not an accepted-yield receipt:

| Chain term | What Goru records | What the bound product establishes | Custody verdict |
|---|---:|---|---|
| parent | 2,000,000 galaxies at arm-resolving depth, roughly z<0.15 | DR10 has 2,827,055,986 unique sources overall; DR10.1 provides morphology and photo-z fields, but no documented row count for Goru's unstated z/depth/size/mask/footprint cuts | **ASSUMED, NOT COUNTED** |
| spiral fraction | 25% | DR10 `TYPE` is a Tractor light-profile model, not a spiral-arm label; the primary instrument's mirror-invariant spirality acceptance must operate on images | **EXTERNAL HEURISTIC, NOT A PRODUCT COUNT** |
| inclination survival | 70% | `SHAPE_E1/E2` can produce b/a, but Goru gives only an example `b/a>0.4` and did not count the exact DR10.1 selection | **ASSUMED, NOT COUNTED** |
| CE-ResNet acceptance | optimistic 50% | no trained, frozen synthetic-only production estimator has been run on this route; Lana itself marks the real rate `[VERIFY in production]` | **OPTIMISTIC ASSUMPTION** |
| quality/product losses | effectively 100% survival beyond the three rates | photo-z validity/reliability, g/r/z coverage, morphology validity, masks, fit flags, cutout completeness, WCS failures, and known issues all remain uncounted | **OMITTED** |

The contradiction is therefore precise:

> **The real DR10.1 products are field-complete enough to define a route, but they do not support
> the status claim that Legacy “yields ~175,000 accepted” or “easily supplies 100,000.”  The
> `~175,000` value is a multiplication of an uncited 2,000,000 parent assumption and three assumed
> survival rates; it is not a count from the bound DR10.1 products and not a production-estimator
> acceptance receipt.**

Nothing in the product documentation proves the opposite either.  The products may eventually
supply the sample, but the present evidence cannot distinguish that from a shortfall after the
missing cuts.  That is exactly why Kun required two receipts.

Useful arithmetic boundaries, without touching real rows:

- with Goru's 25% and 70% factors, an accepted N=100,000 from a 2,000,000 parent requires the
  production estimator to retain at least `28.5714%` of the surviving face-on spirals;
- Goru's 50% assumption gives 175,000;
- his 14% deterministic-estimator assumption gives 49,000;
- any actual parent below `1,142,858` cannot produce 100,000 at the optimistic 25%×70%×50% chain.

### 8.1 Required completion/replacement of the non-closing Goru receipt

Freeze condition 2 can close only after a separately authorized, count-bearing receipt for this
exact route records, in order:

1. hashes and versions of the current `10.1` sweeps, row-matched `10.1-photo-z`, brick summary,
   mask definitions, and production estimator;
2. the exact parent predicates, including footprint, required bands/exposures, redshift field and
   bounds, redshift validity/uncertainty/brightness rule, non-PSF/star-galaxy rule, magnitude,
   half-light-radius/PSF resolution rule, b/a rule, `MASKBITS`, `FITBITS`, and duplicate policy;
3. row counts after every predicate, not only a final number;
4. cutout-delivery and per-product WCS pass/fail counts;
5. mirror-pair-valid, classifier-accepted, and hand-check-eligible counts from the frozen
   synthetic-only estimator;
6. a final proof that N≥100,000 after **all** losses, or an `INCONCLUSIVE-BY-POWER` stop.

Executing item 2 onward touches real galaxy rows and, later, real image pixels.  It is outside
this drafting authorization.  **The next natural step is therefore a real-catalogue parent/yield
count, and this receipt stops here.  Reaching that boundary is the successful outcome requested
by Duho.**

## 9. What is and is not frozen by this receipt

Frozen now:

- DESI Legacy DR10.1 southern DECam route only;
- public `ls-dr10-south` FITS cutout, `pixscale=0.262`, `bands=grz`, `size=256`;
- delivered generated TAN pixels as the measurement input;
- no downstream resampling and byte-exact pixel-index mirror;
- current DR10.1 `10.1` sweeps and `10.1-photo-z` row-matched product;
- current post-December-2023 brick summary;
- exact Legacy and Gaia covariate products in §5;
- per-product WCS audit and **fail-closed-on-distortion** branch;
- required licences, credits, acknowledgments, citations, and product hashes at future use;
- no empirical execution until a count-bearing Goru accepted-yield receipt closes N≥100,000.

Not frozen or authorized here:

- a real parent sample or any row count;
- final catalogue selection thresholds not already specified by Lana V2;
- any model training or production weights;
- any real-image classifier acceptance rate;
- any real galaxy cutout beyond the one 16×16 header-only request;
- any chirality label, monopole, dipole, permutation, sky statistic, result, interpretation,
  publication, upload, or accepted status.

## 10. Boundary ledger

- Documentation requests: allowed and performed.
- Data-product requests: **1**, the 5,760-byte header-only FITS in §6.3.
- Bulk acquisition: **0**.
- Catalogue row queries: **0**.
- Gaia row queries: **0**.
- Real-galaxy selection/counts: **0**.
- Real-pixel chirality computations: **0**.
- Sky statistics: **0**.
- Results: **none**.
- Publication/upload: **none**.
- Scientific or package acceptance: **none**.
- Git commit/push: **none**.

**Final custody verdict:** `ROUTE_BOUND_DESI_LEGACY_DR10_1_SOUTH / YIELD_RECEIPT_PRESENT_BUT_NOT_CLOSED /
FREEZE_CONDITION_2_PARTLY_CLOSED / EMPIRICAL_RUN_BLOCKED`.

## 11. Primary-source URL ledger

1. DR10 release description, footprint, TAN WCS, cutout routes, pipeline versions:
   https://www.legacysurvey.org/dr10/description/
2. Exact files, sweeps, photo-z, brick summary, coadds, masks, PSF products:
   https://www.legacysurvey.org/dr10/files/
3. Tractor schema, SFD98 fields, fluxes, shape fits, ellipticity-to-b/a definition:
   https://www.legacysurvey.org/dr10/catalogs/
4. DR10 bit definitions:
   https://www.legacysurvey.org/dr10/bitmasks/
5. DR10/DR10.1 release IDs:
   https://www.legacysurvey.org/release/
6. DR10.1 replacements and known product issues:
   https://www.legacysurvey.org/dr10/issues/
7. Viewer/cutout URL patterns:
   https://www.legacysurvey.org/viewer/urls/
8. Legacy image licence, exact credit, paper acknowledgment, and photo-z acknowledgment:
   https://www.legacysurvey.org/acknowledgment/
9. Gaia public/anonymous TAP access:
   https://www.cosmos.esa.int/web/gaia-users/archive/programmatic-access
10. Gaia DR3 exact TAP endpoint:
    https://gea.esac.esa.int/tap-server/tap
11. Gaia DR3 credit and citation instructions:
    https://gea.esac.esa.int/archive/documentation/GDR3/Miscellaneous/sec_credit_and_citation_instructions/
12. Gaia data licence:
    https://www.cosmos.esa.int/web/gaia-users/license
13. SFD98 primary record:
    https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract
