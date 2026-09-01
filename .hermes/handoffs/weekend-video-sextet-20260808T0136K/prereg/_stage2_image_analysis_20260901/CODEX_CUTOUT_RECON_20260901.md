# CODEX cutout reconnaissance — 2026-09-01

## Boundary and frozen facts

This is documentation-only reconnaissance. I did not request a cutout, open a FITS
image, read a checksum-list body, or otherwise transport pixel data. Consequently,
facts that are not stated in documentation (notably the returned cutout's exact HDU
schema, dtype and edge fill) remain open rather than being inferred from bytes.

The production binding is Branch B, release `dr10.1`, image tree
`dr10/south/coadd/`, band `r`, HDU 1
([frozen reference, lines 1653–1660](../_successor_build_20260824/ref/successor_ref_v9.py)).
Stage two freezes 0.262 arcsec/pixel but explicitly leaves size, centering and
rotation open; it also says R1–R5 have names but no definitions and prohibits the
predecessor runner ([scope, lines 67–76](STAGE2_SCOPING_20260901.md)).

## 1. Access paths

### Path 1 — Legacy Survey Viewer cutout service (coordinate-native)

- Endpoint: `https://www.legacysurvey.org/viewer/fits-cutout` (the documentation
  also shows the alias `/viewer/cutout.fits`). Use `ra`, `dec`,
  `layer=ls-dr10-south`, `bands=r`, `pixscale=0.262`, and one of `size=N` or
  `width=W&height=H`. The documented DR10 examples and the south-only layer are
  at [DR10 description, lines 90–107](https://www.legacysurvey.org/dr10/description/);
  pixel dimensions are documented at lines 110–116 of the same page.
- Inputs: sky center in decimal degrees; scale in arcsec/pixel; output dimensions
  in pixels. There is no documented `(brickid,objid)` cutout parameter. Resolve
  that key through the DR10.1 catalog to `ra,dec`; the catalog documents `objid`
  as brick-local, uniqueness by `(release,brickid,objid)`, and supplies `ra`,
  `dec`, `bx`, `by` ([catalog format](https://www.legacysurvey.org/dr10/catalogs/)).
- Output: FITS for `fits-cutout`; JPEG is a separate endpoint and is unsuitable
  for the frozen FITS/HDU binding. The FITS is expected to carry celestial WCS
  because this is a WCS cutout of documented TAN image stacks, but the public
  cutout instructions do **not** specify its exact HDU sequence or header-card
  contract. That must be frozen only after an authorized BS-6 probe.
- Coverage/edge behavior is not documented on the DR10 page. Do not assume
  padding, fixed shape, or failure semantics.
- No rate limit, concurrency limit, service-level guarantee, or bulk-use policy
  was found in the cited cutout documentation. Therefore 49,211 independent
  requests require operator confirmation and a preregistered pace/retry policy;
  absence of a published limit is not permission for high concurrency.

### Path 2 — NERSC release coadd tree plus a new local WCS crop (brick-native)

- Source: `https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/`
  with the documented layout
  `<AAA>/<brick>/legacysurvey-<brick>-image-r.fits.fz`. The official
  [DR10 files page](https://www.legacysurvey.org/dr10/files/) describes these
  image stacks; a directory listing demonstrates both product names and a
  per-brick SHA-256 list
  ([example brick directory](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/003/0031p222/)).
- Input: a closed brick manifest, then brickname/path. `(brickid,objid)` can be
  resolved to brickname and `bx,by`, while `ra,dec` can be transformed through
  the coadd WCS. A cutout spanning an overlap may need neighboring bricks; the
  frozen closure rule explicitly includes them and rejects home-brick-only
  enumeration ([draft, lines 215–228](../_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V134_20260831.md)).
- Output/controls: the remote product is a whole tile-compressed FITS coadd, not
  a server-side cutout. Size, centering, interpolation/no-interpolation and edge
  policy would belong to a **new** local producer. This path transports much more
  data but gives producer checksums and explicit auxiliary planes.
- Bulk policy: the release is published for direct file access and the top-level
  index publishes `legacysurvey_dr10.sha256sum`
  ([DR10 index](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/)).
  I found no documented rate/concurrency number. The frozen plan independently
  requires pacing, receipts, a digest-pinned manifest, and a pre-fixed ceiling;
  image bytes are permitted only after freeze under BS-6
  ([draft, lines 257–262](../_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V134_20260831.md)).

Not counted as a DR10.1 path: NOIRLab Data Lab describes SIA cutout URLs for LS
DR8 and DR9, but not DR10; for DR10 it redirects users to the Legacy Survey team
cutout service ([Data Lab LS page, lines 147–166](https://beta.datalab.noirlab.edu/data/legacy-surveys)).

## 2. Format facts

- A full optical brick stack is 3600 × 3600 pixels, approximately 0.25° square,
  with about 130 pixels of overlap, North up, tangent-plane `TAN` WCS and
  0.262 arcsec/pixel. The `g,r,i,z` projections are identical; coadds use
  Lanczos-3 interpolation ([DR10 description, lines 84–85 and 205](https://www.legacysurvey.org/dr10/description/)).
- `legacysurvey-<brick>-image-r.fits.fz` is the inverse-variance-weighted coadd,
  in nanomaggies per pixel, on the AB system. It is a convenience coadd, not the
  single-epoch image used by Tractor ([files page, Image Stacks](https://www.legacysurvey.org/dr10/files/)).
- Frozen `hdu=1` is consistent with reading the image extension of an
  `.fits.fz` tile-compressed product. The survey prose also calls the coadded
  image the “primary HDU.” Because those two descriptions use different FITS
  viewpoints, the exact physical HDU table (including whether HDU 0 is empty)
  must be verified later from an authorized header-only or BS-6 probe; it was
  not verified here.
- The documentation does not state the stored image dtype or the Viewer FITS
  cutout dtype. Do not freeze `float32` merely because it is plausible.
- Auxiliary products are separate files, not established as extra planes of
  the image file: `...-invvar-r.fits.fz` is inverse variance in
  `1/(nanomaggies)^2/pixel`; `...-maskbits.fits.fz` has optical `MASKBITS` in
  HDU1, W1 in HDU2 and W2 in HDU3; `...-nexp-r`, `...-depth-r`,
  `...-galdepth-r`, `...-chi2-r`, `...-model-r`, `...-blobmodel-r`, and
  `...-psfsize-r` are also documented. Mask meanings are defined by the
  [DR10 bitmask table](https://www.legacysurvey.org/dr10/bitmasks/).
- `psfsize-r` is a per-pixel PSF-FWHM map. A PSF *model/cutout plane* is not
  documented as a coadd product; the brick `ccds.fits` table and calibration
  products are a different route. Thus “PSF available” must not be conflated
  with a pixelized PSF kernel.

## 3. Geometry inputs and edge cases

A coordinate service request needs `(ra,dec)`, `bands=r`, south DR10 layer,
`pixscale=0.262`, and square `size` or rectangular `width,height`, all dimensions
in pixels. Its angular footprint is `N × 0.262` arcsec on a side for an `N`-pixel
square. A brick-local producer additionally needs the release-resolved brickname,
the image WCS (or catalog `bx,by`), and the closed set of neighbor bricks.

The service documentation does not say how centers round to pixels, whether an
even-sized cutout centers on a pixel or an inter-pixel point, whether the output
is always North-up with the native handedness, or how missing coverage/tile edges
are represented. The underlying stacks overlap, but that does not define service
stitching or padding. BS-2a already distinguishes a missing/integrity-failed
cutout from an incomplete frozen-shape cutout
([draft, lines 351–371](../_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V134_20260831.md));
stage two must turn those into exact tests without inspecting chirality.

## 4. Integrity hooks

Available hooks, strongest first:

1. Direct-tree source files have producer SHA-256 lists at release and per-brick
   level (the NERSC indices cited above). Verify list custody/authenticity, exact
   relative path, byte count and SHA-256 before decompression.
2. Bind each derived cutout to a canonical manifest row containing release
   (`dr10.1` catalog binding / DR10 image tree), layer/product, brickname(s),
   `(release,brickid,objid)`, catalog `ra,dec`, requested geometry, source-file
   SHA-256 values, producer/version digest, output byte length and output SHA-256.
3. Re-open the exact output bytes and validate FITS parse, selected HDU, 2-D
   shape, finite/header rules, WCS presence and center/scale/orientation against
   the request. Record the header subset (e.g. WCS cards, `BUNIT`, product/band
   identifiers) canonically rather than trusting filenames alone.
4. The Viewer endpoint does not document an expected checksum or immutable
   request-version identifier. A locally computed response hash proves internal
   consistency/custody only, not equivalence to a producer-signed source. This is
   a material disadvantage for `verify_cutout_integrity`.

These hooks fit the frozen requirement that the ledger carry expected and actual
cutout checksums and shapes and that the verdict recompute them
([draft, lines 365–371](../_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V134_20260831.md)).
They are inputs to R1–R5, not proposed final definitions; those checks remain a
stage-two design obligation.

## 5. Scale for the 49,211-object mask

The frozen retained mask is exactly 49,211 rows while the parent remains 65,060
([draft, lines 401–403](../_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V134_20260831.md)).
Therefore an object-cutout design implies 49,211 successful terminal objects (or
49,211 ledger rows partitioned into success/exclusion under the frozen rule), not
one file per unique brick.

For budgeting only, if the selected image array were uncompressed float32 and a
minimal FITS used 2880-byte blocking, plausible single-plane sizes are:

| square | sky width | approximate FITS/object | 49,211 objects |
|---:|---:|---:|---:|
| 64 px | 16.768″ | 20,160 B | 0.99 GB |
| 128 px | 33.536″ | 69,120 B | 3.40 GB |
| 224 px | 58.688″ | 204,480 B | 10.06 GB |
| 256 px | 67.072″ | 267,840 B | 13.18 GB |

These are deterministic **planning examples**, not measured response sizes and
not evidence of dtype. Compression, richer headers, extra HDUs, invvar/mask
planes, HTTP receipts and retries change the total. A safe ceiling must cover
both authorized transport and retained artifacts, state decimal/binary units,
and refuse before exceeding it. The manifest should have exactly one canonical
request/terminal row per masked object plus a separate source-file table so
shared brick hashes are not duplicated ambiguously.

The alternative full-brick route has a frozen predecessor planning fact: 65,060
parent objects closed to 12,117 bricks, budgeted at about 148 GB using a measured
12.2 MB/brick; that ceiling was explicitly not fetch authorization
([queue plan, lines 94–125](../_successor_build_20260824/acquire/DOWNLOAD_QUEUE_PLAN_20260825.md)).
The 49,211-mask closure may be smaller, but reconnaissance cannot derive it; it
must be recomputed by the frozen closure authority after cutout geometry is set.

## 6. Open questions the design must settle

1. Choose Path 1, Path 2, or a preregistered comparison/fallback, and define
   whether a service failure may switch paths without creating non-identical
   pixels.
2. Pin exact endpoint/host/layer semantics for DR10.1. The viewer says DR10,
   while DR10.1 is primarily a catalog-product distinction; document whether the
   image bytes are intentionally the same DR10 tree.
3. Freeze odd/even size, center rounding, angular extent, orientation/rotation,
   resampling prohibition or algorithm, interpolation kernel, and edge stitching.
4. Establish by authorized probe the Viewer FITS HDU layout, dtype, `BUNIT`, WCS
   cards, missing-coverage values, fixed-shape behavior, HTTP errors and whether
   `bands=r` is honored identically by both endpoint aliases.
5. Decide whether the instrument consumes only image HDU 1 or also requires
   invvar, maskbits, nexp, PSF-size or a genuine PSF model; freeze alignment,
   dtype and acceptance use for every auxiliary plane.
6. Define R1–R5 and `verify_cutout_integrity`: checksum authority, canonical
   serialization, source-to-derived provenance, WCS tolerance, shape/dtype/unit
   rules, NaN/Inf/zero-coverage policy, and adversarial fixtures.
7. Define rate, concurrency, timeout, retry/backoff, idempotence and terminal
   failure semantics after obtaining operator guidance; none is published for
   the Viewer or NERSC paths cited here.
8. Recompute neighbor-brick closure for the chosen geometry and 49,211 mask;
   freeze request count, source count, measured/upper-bound bytes, manifest
   digest and refusal-on-ceiling behavior before BS-6.
9. Decide whether checksums lists themselves need an external digest/signature
   anchor; a hash list fetched from the same mutable origin is not independent
   custody evidence.
10. Define cutout filename/key collision rules and the one-to-one join from
    `(release,brickid,objid)` to request, bytes, evidence and terminal ledger row.

SEAT: CODEX
VERSION: RECON-V1
VERDICT: RECONNOITRED
COUNT: 2
