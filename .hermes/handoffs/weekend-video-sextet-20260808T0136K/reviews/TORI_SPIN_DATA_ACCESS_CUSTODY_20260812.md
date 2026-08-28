# TORI — Spin-Handedness Imaging Data Access and Orientation-Custody Check

Date checked: 2026-08-12 KST  
Seat: access custody and verification only  
Decision authority: Duho  
Scope: HSC-SSP public releases, DESI Legacy Imaging Surveys DR10, SDSS legacy imaging, and Pan-STARRS1 public imaging

## Absolute-path correction and prerequisite binding

| Artifact | Absolute path | Bytes | SHA-256 / status |
|---|---|---:|---|
| Required prior-art receipt | `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/TORI_SPIN_PRIOR_ART_20260811.md` | 25,248 | `034b1bb27bff6637d9dda695739d474b0a925ac567c93cf6e10d794d62f66bf1` |
| This corrected access receipt | `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/TORI_SPIN_DATA_ACCESS_CUSTODY_20260812.md` | reported in the external final receipt | self-hash intentionally not embedded |
| Evidence ledger | `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/_tori_spin_access_evidence/ledger.json` | 15,100 | `0a81fc12f75ff5166e97e0afb840345a3bca177f6af2cbf758d618eaf81d32e3` |
| One permitted test cutout | `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/_tori_spin_access_evidence/legacy_dr10_one_test_cutout_r_16px.fits` | 5,760 | `601c309771ed5da0a15defc0b4ccfc1063ee8422a89fbc969d916bba6c1f257a` |

The actual prior-art receipt has now been read from its absolute path and is bound above by full hash, not by the earlier summary.[19]

It says that Shamir's 2024 HSC paper does not identify its downloaded image format, FITS-to-display conversion, pixel-axis/WCS convention, cutout service, or orientation-preservation checks.[19]

It also quotes Ganalyzer's supported inputs as TIFF, JPG, PPM, and BMP, with FITS requiring conversion before analysis.[19]

The access audit therefore had to distinguish native or generated FITS with recoverable WCS from rendered JPEG, rather than treating every public image endpoint as equivalent.[19][20]

The current design brief requires per-cutout CD/PC parity logging and native-format pixels with WCS; Kun's gate further requires valid delivered WCS plus later parity/injection tests.[20][21]

Re-reading the real prerequisite did not overturn an access fact below, but it tightened the grade: one valid FITS header is an access/header receipt, not by itself an end-to-end parity validation.[19][21]

## Path-side-effect disclosure

| Question | Recorded fact |
|---|---|
| Did Tori previously write under the bare repo-root `reviews/` path? | Yes: the first report and `_/.tori_spin_access_evidence` artifacts were initially written there because of the incorrect working directory. |
| Did Tori delete those root artifacts? | No. |
| Current root state | Both root paths were absent when rechecked after the path correction. |
| Current lane state | The report and original test-cutout receipt were already present in the lane; the quote-backed source bundle and ledger were rebuilt/copied into the lane. |
| Cleanup action in this correction | None. No root path was deleted. |

## Scope and side-effect boundary

This receipt establishes access and orientation-custody facts only; it does not judge scientific merit or choose a survey.[19][20]

HSC credentials were unavailable, so no HSC account was created and no HSC terms were accepted.

No bulk survey pixels were downloaded.

Exactly one small DR10 cutout request was made in the earlier pass, and no second cutout was requested during this correction.[22]

Nothing was published, uploaded, accepted, registered, or run as a sky analysis.[20][22]

## Access result at a glance

| Source/product | Registration or affiliation | Pixel route | Product-schema grade | Exact delivered-parity grade tonight | Decisive fact |
|---|---|---|---|---|---|
| HSC-SSP PDR3 | Account and term acceptance required; institutional affiliation not stated as mandatory, but `Institute` is requested | Portal, direct file tree, authenticated FITS client | `DOCUMENTED — IMAGE SOURCE ONLY` | `UNDOCUMENTED` | FITS documented, but no accessible WCS manual/header receipt without credentials |
| Legacy DR10 default FITS cutout | Anonymous; no affiliation encountered | `viewer/fits-cutout` plus NERSC bulk tree | `DOCUMENTED — IMAGE SOURCE ONLY` | `DOCUMENTED FOR ONE EXACT DELIVERY` | Live float32 FITS contained TAN WCS and full CD matrix; service-generated/resampled, not detector-native |
| SDSS SkyServer `ImgCutout` | Anonymous | `getjpeg` | `UNSUITABLE — RENDERED DISPLAY` | `UNDOCUMENTED / NO FITS HEADER` | Convenient cutout is JPEG created after multiple transformations |
| SDSS SAS corrected frame | Anonymous HTTP/wget; Globus account optional | Full corrected-frame FITS | `DOCUMENTED — IMAGE SOURCE ONLY` | `UNDOCUMENTED FOR AN EXACT DELIVERY TONIGHT` | Documentation states corrected WCS; local cropping is required for per-object stamps |
| Pan-STARRS1 DR2 FITS cutout | Anonymous | `ps1filenames.py` + `fitscut.cgi` | `DOCUMENTED — IMAGE SOURCE ONLY` | `UNDOCUMENTED FOR AN EXACT DELIVERY TONIGHT` | FITS cutouts have `RADESYS` but obsolete PC cards; full skycells and polar WCS have caveats |

`DOCUMENTED — IMAGE SOURCE ONLY` is not a study-readiness verdict; the estimator, selection, injected-image round trip, and full preprocessing path remain separate gates.[20][21]

## Volume convention

The table below is a storage-order estimate for 32-bit image planes, not a scientific choice of field size or bands.

| Objects | Bands | 256 × 256 | 512 × 512 |
|---:|---:|---:|---:|
| 10,000 | 3 | 7.32 GiB | 29.30 GiB |
| 30,000 | 3 | 21.97 GiB | 87.89 GiB |
| 50,000 | 3 | 36.62 GiB | 146.48 GiB |
| 30,000 | 5 | 36.62 GiB | 146.48 GiB |
| 200,000 | 3 | 146.48 GiB | 585.94 GiB |
| 200,000 | 5 | 244.14 GiB | 976.56 GiB |

The 200,000-object rows are included because the current design brief names an indicative parent sample of approximately 200,000 candidates supporting approximately 30,000 accepted spirals.[20]

FITS headers and padding add overhead, while compression can reduce transfer bytes; masks, inverse variance, variance, exposure-count, or PSF planes add further arrays.

At documented nominal sampling, 256–512 pixels spans approximately 43–86 arcsec for HSC, 67–134 arcsec for Legacy, 101–203 arcsec for SDSS, and 64–128 arcsec for PS1.[5][11][14]

HSC's survey page states a 0.168 arcsec pixel scale.[18]

Whether 256 or 512 pixels and which bands are adequate is outside this access audit.

---

## 1. Subaru Hyper Suprime-Cam — HSC-SSP PDR3

### Concrete access routes

- Primary access page: https://hsc-release.mtk.nao.ac.jp/doc/index.php/data-access__pdr3/
- Account registration: https://hsc-release.mtk.nao.ac.jp/datasearch/new_user/new
- Browser cutout: https://hsc-release.mtk.nao.ac.jp/das_cutout/pdr3/
- Browser search: https://hsc-release.mtk.nao.ac.jp/das_search/pdr3/
- Wide direct tree: https://hsc-release.mtk.nao.ac.jp/archive/filetree/pdr3_wide/
- Deep/UltraDeep direct tree: https://hsc-release.mtk.nao.ac.jp/archive/filetree/pdr3_dud/
- FITS client documentation: https://hsc-gitlab.mtk.nao.ac.jp/ssp-software/data-access-tools/-/raw/master/pdr3/downloadCutout/README.md

The primary access page says:

> “You need to register for a user account if you wish to search/request/retrieve the data. The use of the HSC data archive is restricted to non-commercial, scientific/educational purposes.”[1]

The signup form requests account name, full name, institute, country, email, position, purpose, CAPTCHA, and term acceptance.[2]

The position list includes `Student`, `Researcher`, `Amateur`, and `Teacher`, so no institutional-affiliation condition is stated, although the form still requests an institute.[2]

This audit cannot establish whether an unaffiliated entry would be accepted without completing the unauthorized registration step.

The client accepts coordinate lists and returns binary FITS data decodable with Astropy.[4]

### Documented limits

No numeric daily quota or request-per-second entitlement was located in the cited access/client pages.[1][4]

The official client does state that the server refuses too many simultaneous client instances.[4]

Its supplied synchronization example uses:

> `--semaphore=/home/yourname/semaphore --max-connections=4`[4]

Four is a conservative example setting, not a published server entitlement.[4]

### Licence and citation terms

The registration terms say:

> “This archive provides scientific data for the purposes of astronomical research and education.”[2]

> “It is strictly prohibited to make use of the data for commercial purposes.”[2]

> “All users are requested to include an acknowledgement in any publications that make use of data obtained from the system.”[2]

The PDR3 acknowledgment page says the supplied acknowledgment text “should be included” in all publications based on public HSC-SSP data.[3]

Full required wording and references: https://hsc-release.mtk.nao.ac.jp/doc/index.php/acknowledging-hsc__pdr3/

### FITS/WCS decision

The official client says “Download FITS cutouts from the website of HSC data release.”[4]

That proves a FITS route exists, but the public README does not specify the delivered celestial cards, parity, or resampling behavior.[4]

The browser cutout manual required credentials during this audit, and no HSC header was inspected.

Access grade: `DOCUMENTED — IMAGE SOURCE ONLY`; exact delivered parity: `UNDOCUMENTED`.

A later authorized one-cutout test would need to freeze the bytes and inspect `CTYPE*`, `CRPIX*`, `CRVAL*`, CD/PC, `RADESYS`, dimensions, HDUs, and any resampling before HSC can pass the header-delivery gate.[20][21]

---

## 2. DESI Legacy Imaging Surveys — DR10

### Concrete access routes

- DR10 file descriptions: https://www.legacysurvey.org/dr10/files/
- Anonymous NERSC tree: https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/
- Service URL documentation: https://www.legacysurvey.org/viewer/urls/
- FITS pattern: `https://www.legacysurvey.org/viewer/fits-cutout?ra=<deg>&dec=<deg>&layer=ls-dr10&pixscale=0.262&bands=grz&size=<pixels>`
- Rendered JPEG pattern: `https://www.legacysurvey.org/viewer/jpeg-cutout?...`

No login, token, or affiliation was required to browse DR10 or obtain the one test cutout.[5][22]

The viewer documentation separately exposes FITS cutouts and rendered JPEG cutouts.[6]

It documents a `subimage` mode as “no resampling; subimage from Data Release coadd image; includes invvar map,” but the example is for an older layer rather than `ls-dr10`.[6]

No second request was made to test DR10 `subimage` support.[22]

DR10 stacks are 3600 × 3600 TAN-projection images at 0.262 arcsec/pixel.[5]

The file documentation explicitly says those images use Lanczos-3 resampling.[5]

### Documented limits

No numeric quota, rate, or concurrency limit was located in the cited DR10 file/service/publication pages.[5][6][7]

That is a scoped documentation gap, not evidence of unlimited service.

A production pull would therefore require provider contact or an explicitly conservative concurrency/backoff plan before acquisition.

### Licence and citation terms

For Legacy-produced viewer layers, the acknowledgment page says:

> “Images are licensed under a Creative Commons Attribution 4.0 International License, and hence may on a non-exclusive basis be reproduced without fee provided the credit is clear and visible.”[7]

The prescribed viewer credit is:

> “Legacy Surveys / D. Lang (Perimeter Institute)”[7]

For papers it says:

> “When using data from the Legacy Surveys in papers, please use the following acknowledgment”[7]

The publications page repeats that papers should include the acknowledgment-page text.[8]

Full wording: https://www.legacysurvey.org/acknowledgment/

The CC-BY statement applies to Legacy-produced layers and should not be generalized to unrelated Sky Viewer layers.[7]

### One permitted FITS/header test

| Receipt field | Value |
|---|---|
| URL | `https://www.legacysurvey.org/viewer/fits-cutout?ra=190.1086&dec=1.2005&layer=ls-dr10&pixscale=0.262&bands=r&size=16` |
| File | `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/_tori_spin_access_evidence/legacy_dr10_one_test_cutout_r_16px.fits` |
| Size | 5,760 bytes |
| SHA-256 | `601c309771ed5da0a15defc0b4ccfc1063ee8422a89fbc969d916bba6c1f257a` |
| Data | one primary 16 × 16 float32 image |
| Astropy check | `WCS(header).has_celestial == True` |
| `RADESYS` | absent |

The inspected receipt confirms float32 FITS and a parseable celestial WCS.[22]

Observed cards:

```text
SIMPLE  = True
BITPIX  = -32
NAXIS1  = 16
NAXIS2  = 16
CTYPE1  = 'RA---TAN'
CTYPE2  = 'DEC--TAN'
CRVAL1  = 190.1086
CRVAL2  = 1.2005
CRPIX1  = 8.5
CRPIX2  = 8.5
CD1_1   = -7.27777777777778e-05
CD1_2   = 0.0
CD2_1   = 0.0
CD2_2   = 7.27777777777778e-05
BANDS   = 'r'
BAND0   = 'r'
```

The full CD matrix makes the local axis parity recoverable rather than silently embedding it in a headerless JPEG.[22]

This passes the exact-delivery FITS/header gate for that request, but it is a generated TAN cutout and not an untouched detector frame.[5][22]

It does not pass the future end-to-end parity/injection gate, which remains outside this access receipt.[20][21]

---

## 3. SDSS legacy imaging

### Concrete access routes

- DR17 access overview: https://www.sdss4.org/dr17/data_access/
- Rendered API: `https://skyserver.sdss.org/dr17/SkyServerWS/ImgCutout/getjpeg?ra=<deg>&dec=<deg>&scale=<arcsec-per-pixel>&width=<px>&height=<px>`
- SAS root: https://data.sdss.org/sas/dr17/
- Corrected-frame tree: https://data.sdss.org/sas/dr17/eboss/photoObj/frames/
- Bulk instructions: https://www.sdss4.org/dr17/data_access/bulk/

SDSS says users can view online images and download image fields as FITS.[9]

Direct SAS HTTP/wget is public; Globus is optional and requires a separate account.[10]

### Documented limits

For transfers above 1 TB, SDSS asks users to contact its helpdesk for a custom transfer.[10]

SDSS says rsync connections are throttled while wget connections are not.[10]

No numeric SkyServer cutout rate was located in the cited DR17 pages.[9][10][12]

The comparative wget statement is not permission for unbounded concurrency.

### Licence and citation terms

SDSS-IV says all public-release SDSS data are considered public domain.[13]

It also supplies website images under CC-BY provided image credits are maintained.[13]

For papers using DR13–DR17, SDSS requests the SDSS-IV acknowledgment.[13]

Full terms and wording:

- https://www.sdss4.org/collaboration/#sdss4acknowledgement
- https://www.sdss4.org/collaboration/citing-sdss/

### FITS/WCS versus rendered cutout

SkyServer visual tools use JPEG versions constructed on demand by the `ImgCutout` service.[12]

The documented conversion reads g/r/i corrected FITS frames, transforms them into a color JPEG, interpolates among zoom levels, mosaics frames, applies an affine transform, and trims the canvas.[12]

The returned JPEG carries no FITS header, so it cannot serve as parity authority.[12][21]

The SAS route is different: SDSS says it provides corrected-frame FITS for quantitative analysis and that the headers contain WCS corrected to the final astrometric solution.[11]

Access result: SkyServer `ImgCutout/getjpeg` fails; SAS corrected-frame FITS passes the documented product-schema gate.[11][12]

No exact SDSS frame header was inspected tonight, so exact delivered parity remains `UNDOCUMENTED` for this receipt.

Per-object stamps would require grouping targets by unique fields, downloading each corrected frame once, cropping locally, and preserving the original/sliced WCS.

---

## 4. Pan-STARRS1 public imaging — DR2

### Concrete access routes

- Archive home: https://outerspace.stsci.edu/spaces/PANSTARRS/pages/298812201/Pan-STARRS1+data+archive+home+page
- Image-service documentation: https://outerspace.stsci.edu/spaces/PANSTARRS/pages/298812251/PS1+Image+Cutout+Service
- Browser: https://ps1images.stsci.edu/cgi-bin/ps1cutouts
- Filename/list API: https://ps1images.stsci.edu/cgi-bin/ps1filenames.py
- FITS/JPEG cutout: https://ps1images.stsci.edu/cgi-bin/fitscut.cgi

The service says postage stamps are available as browser JPEG or FITS.[14]

No login, token, or institutional affiliation is stated for these image endpoints.[14]

PS1 CasJobs is a separate catalog service and is not needed for the image routes above.[14]

### Documented limits

The cutout size is limited to 6000 pixels.[14]

The documentation says uploading 1000 positions in one query is much faster than querying them one at a time.[14]

It asks clients not to use more than ten simultaneous download threads and warns that excessive rates will be blocked.[14]

### Licence and citation terms

MAST says most hosted data are public domain and without use restrictions, then lists the collections to which restrictions apply.[15]

The listed copyrighted collections are DSS and Guide Star Catalogs rather than PS1.[15]

This supports public scientific reuse but is an archive-wide policy, not a separate PS1-specific licence grant.[15]

MAST says papers using MAST data should include a DOI.[16]

The PS1 home page supplies publication acknowledgment text and asks users to cite appropriate instrument, survey, processing, calibration, and data-product papers.[17]

### FITS/WCS decision

The service says FITS cutouts have a correct `RADESYS` keyword.[14]

It also says cutouts retain obsolete WCS keywords: `PC001001`, `PC001002`, `PC002001`, and `PC002002`.[14]

The raw cards should therefore be retained and any normalization logged.

Full skycell FITS products lack `RADESYS`, use obsolete PC cards, and have additional compression/scaling caveats.[14]

The archive warns that warp and stack images near the celestial pole may have incorrect WCS.[17]

Access grade: `DOCUMENTED — IMAGE SOURCE ONLY`; exact delivered parity: `UNDOCUMENTED` because the sole test allowance had already been used on DR10.[14][22]

A later authorized PS1 header check would need to retain source filenames, the full PC matrix, `RADESYS`, request parameters, and polar-field rejection/validation rules.[14][20]

---

## Failures and unresolved facts

| Item | Facts-only result |
|---|---|
| HSC credentials | Mandatory and unavailable; no HSC acquisition or term acceptance occurred |
| HSC exact WCS delivery | `UNDOCUMENTED` tonight despite documented FITS output |
| Legacy numeric rate limit | Not located in the cited official pages; unlimited service must not be inferred |
| Legacy DR10 no-resampling mode | `subimage` documented for an older layer; not tested for `ls-dr10` |
| Legacy complete parity custody | One exact FITS/header receipt passes; injected-image and full preprocessing checks are not executed |
| SDSS convenient cutout | Rendered JPEG, not a custody FITS product |
| SDSS exact frame delivery | Corrected-frame WCS is documented; no exact frame header was inspected tonight |
| PS1 exact cutout delivery | FITS/WCS documented with caveats; no exact header inspected tonight |
| PS1 licence | Archive-wide MAST terms located; no separate named PS1 licence located |

## Door status for Duho

- **HSC-SSP:** access is registration-gated, and exact delivered WCS remains undocumented for this session.[1][4]
- **Legacy DR10:** anonymous access works, and one exact default cutout passes the FITS plus explicit celestial-WCS header gate.[5][22]
- **SDSS:** anonymous corrected-frame FITS is documented with WCS, but SkyServer's cutout is rendered JPEG.[11][12]
- **Pan-STARRS1:** anonymous FITS cutouts are documented with PC/`RADESYS`, rate, and polar-WCS caveats; no exact delivery was tested.[14][17]

At least one route therefore provides an observed public FITS/WCS delivery, satisfying Kun's narrow access-header prerequisite in principle; this does not authorize a survey choice, preregistration freeze, bulk acquisition, or empirical sky run.[21][22]

No production acquisition, registration, term acceptance, or publication follows from this receipt without Duho's decision.

## Sources

[1] https://hsc-release.mtk.nao.ac.jp/doc/index.php/data-access__pdr3
[2] https://hsc-release.mtk.nao.ac.jp/datasearch/new_user/new
[3] https://hsc-release.mtk.nao.ac.jp/doc/index.php/acknowledging-hsc__pdr3
[4] https://hsc-gitlab.mtk.nao.ac.jp/ssp-software/data-access-tools/-/raw/master/pdr3/downloadCutout/README.md
[5] https://www.legacysurvey.org/dr10/files
[6] https://www.legacysurvey.org/viewer/urls
[7] https://www.legacysurvey.org/acknowledgment
[8] https://www.legacysurvey.org/pubs
[9] https://www.sdss4.org/dr17/data_access
[10] https://www.sdss4.org/dr17/data_access/bulk
[11] https://www.sdss4.org/dr17/imaging/images
[12] https://www.sdss4.org/dr17/imaging/jpg-images-on-skyserver
[13] https://www.sdss4.org/collaboration
[14] https://outerspace.stsci.edu/spaces/PANSTARRS/pages/298812251/PS1+Image+Cutout+Service
[15] https://archive.stsci.edu/publishing/data-use
[16] https://archive.stsci.edu/publishing/data-attributions
[17] https://outerspace.stsci.edu/spaces/PANSTARRS/pages/298812201/Pan-STARRS1+data+archive+home+page
[18] https://hsc.mtk.nao.ac.jp/ssp/survey
[19] file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/TORI_SPIN_PRIOR_ART_20260811.md
[20] file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/LANA_SPIN_DESIGN_BRIEF_20260812.md
[21] file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/KUN_SPIN_DESIGN_BRIEF_GATE_20260812.md
[22] file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/_tori_spin_access_evidence/legacy_dr10_one_test_cutout_receipt.txt
