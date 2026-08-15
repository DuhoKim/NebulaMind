# TORI route binding — Globus DR10.1 South bricks, then guarded local cutting

Date: 2026-08-15 KST
Owner: Tori, bounded paper route binding
Decision authority: Duho
Execution acceptance: Duho and Kun
Status: **ROUTE SELECTED; NOT EXECUTABLE; ZERO TRANSFER**

## 1. Verdict

Duho selected the bulk route: use Globus to transfer the exact DR10.1 South r-band brick images needed by the frozen parent set, then make the frozen 128 × 128 float32 r-band cutouts locally.

This document replaces only the acquisition route referenced by §6 of `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`. It does not change the frozen input contract, sample, estimator, thresholds, exclusions, interpretation, or stopping rules.

The selected route is supported by combining two documented components:

1. The `decam-legacy-survey` thread supports using the open Imagine cutout code locally, grouping work by brick, staging the needed images, and caching neighbouring images [1].
2. NERSC documents Globus/NERSC DTN as the recommended mechanism for significant transfers from CFS [4].

No single thread post prescribes the exact sequence “Globus bricks out of NERSC, then cut on our local machine.” The thread's first recommendation was to generate at NERSC and Globus-transfer the resulting cutouts. Duho chose the alternative ordering assembled from the same documented local-code/brick-cache design and the official bulk-transfer mechanism. This distinction is preserved rather than overstated.

The route is not yet open. A guarded production adapter, dependency/container lock, synthetic boundary fixtures, and Kun acceptance are mandatory before a source manifest or Globus task may be created.

## 2. Frozen custody

| Input | SHA-256 |
|---|---|
| `_tmp_TORI_ROUTE_AMENDMENT_BRIEF.md` | `e9a7b57381de86d356df17bed49b7c5cde9c29ac5f12ee7d5e59f8f90792a599` |
| `ACQUISITION_ROUTE_DECISION_20260815.md` | `26b7142e430ca05b275e9d9d03734493eef2d5dce16fe5e6eb87dd5de1e2c7fd` |
| `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` | `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7` |
| predecessor `TORI_SURVEY_ROUTE_BINDING_20260812.md` | `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87` |
| `_tori_bs7_distortion_evidence/fail_closed_wcs.py` | `cae1b1b7ef4e25000ad5d8c906647216b1425638ac737b4ea7363ca948760569` |
| `yui_bs5_sign_anchor_20260814/validate_wcs_parity.py` | `7bf0201917e7722ee9545c9c11b6cc1cbdec345504e3f29fa1aeb01e58edaa55` |
| Hwao relay | `c1ac2f2eed533962fc0f73a68e6ad3e84972342d3ce7010bee8ff6964f9a4190` |
| Hwao receipt | `01b7c75cdb0fc7c10b8b60a44d68b57aaa9c4183aedeb06d08f77c1c0f840098` |

Coordinator receipt marker: `HWAO_ROUTE_AMENDMENT_RELAY_DONE`.

Frozen V3 image contract remains:

- one band: `r`;
- shape: exactly `128 × 128`;
- dtype delivered to the estimator: `float32`;
- native pixel scale: `0.262 arcsec/pixel`;
- no route-induced resize, crop, rotation, clipping, normalization, or band combination;
- image values remain in coadd nanomaggies per pixel [2].

## 3. Required primary-thread quotations

Dustin Lang wrote on 2025-05-19:

> “You are going to want to run the cutout generation code locally on NERSC. This job will want to be run on Cori/Perlmutter to get the local filesystem bandwidth.” [1]

He linked the open `many-cutouts.py` wrapper and warned that the resulting output transfer would itself take time [1].

On 2025-05-21 he identified the boundary problem:

> “The tricky part is that the files are stored in "bricks"; if your requested position is within a couple of pixels of the edge of one brick, it will pull from the image in the neighbouring brick.” [1]

His dependency statement was tentative, not a guarantee:

> “Yeah, like you said, it looks like only the images are required. Just test and find out.” [1]

Andrew Engel then proposed sorting the parent catalogue into brick work units and staging image files in a temporary fast-I/O directory. Lang replied:

> “yes, that will work! (You could also overlap loading and computation by cutting out images from one brick while you transfer the next brick images.)” [1]

Engel later reported that:

> “The main change was sorting the input table by brick-id and setting up a cache with all the local images needed to produce the cutouts.” [1]

He reported thousands of images per second in his own workload. That is historical evidence about his implementation, not a throughput promise for this project.

Operational interpretation: the pixel product can be image-only, but the route also requires hash-pinned brick geometry metadata and source FITS WCS headers. No Tractor catalogue, sweep, inverse-variance map, model, residual, or maskbits product is added by this route.

## 4. Exact survey product and source path

### 4.1 Pixel product

Product: latest DR10.1-replaced bytes in the DR10 South coadd tree, r-band stacked image.

For every source brick `BRICKNAME`, define `AAA = BRICKNAME[0:3]` and require exactly:

`/global/cfs/cdirs/cosmo/data/legacysurvey/dr10/south/coadd/<AAA>/<BRICKNAME>/legacysurvey-<BRICKNAME>-image-r.fits.fz`

The survey documents the image-stack template, WCS TAN projection, `3600 × 3600` dimensions, `0.262 arcsec/pixel`, and nanomaggy units [2]. Compressed files are read from image HDU 1 by the pinned Imagine layer.

### 4.2 Why “DR10.1” must be byte-bound

DR10.1 is not a separate coadd directory. The survey says affected coadds were replaced in the existing DR10 release directory and recommends always using the latest versions [3]. Therefore:

- the text `dr10` in a path is not version proof;
- filename and release label alone are not version proof;
- each source file must be bound by a source-side SHA-256, byte size, modification timestamp, exact path, and manifest hash before transfer;
- a later byte change at the same path is a different input and requires a new source manifest and re-gate.

### 4.3 Geometry sidecar

The brick planning adapter must also bind the latest DR10 South brick summary used to map `BRICKID ↔ BRICKNAME` and obtain centres/bounds. Its intended CFS path is:

`/global/cfs/cdirs/cosmo/data/legacysurvey/dr10/south/survey-bricks-dr10-south.fits.gz`

This is metadata, not an image input. Its source-side SHA-256, size, path, and local SHA-256 are mandatory. The adapter must read it explicitly; it must not pretend the unmodified Imagine directory layout consumes this filename automatically.

## 5. Globus transfer custody

Source collection: NERSC DTN, UUID `9d6d994a-6d04-11e5-ba46-22000b92c6ec`. NERSC documents it as the primary multi-node route with CFS access [4].

The future authorized transfer must use an explicit file batch. Recursive transfer of `south/coadd/`, wildcard expansion at execution time, portal HTTP, range requests, or public cutout calls are forbidden.

### 5.1 Pre-transfer sealed manifest

Before task submission, write and hash a sorted manifest with one record per file:

- `release = dr10.1-latest-byte-bound`;
- source collection UUID;
- absolute CFS source path;
- destination relative path;
- brickname and `AAA`;
- product `image-r` or geometry sidecar;
- source byte size and modification time;
- source SHA-256 computed at NERSC;
- reason: primary brick, edge neighbour, corner neighbour, or geometry sidecar;
- sorted list or hash of private object IDs requiring the source file;
- manifest format version and creation time.

No source file may be added after the manifest hash is approved. A missing required file is terminal, not skippable.

### 5.2 Task fields and mandatory options

The transfer receipt must record:

- source and destination collection UUIDs;
- source and destination root paths;
- approved batch-manifest SHA-256;
- submission ID and task ID;
- immutable task label containing the manifest hash prefix;
- `verify_checksum = true` / explicit `--verify-checksum`;
- `sync_level = checksum` for a restart;
- `skip_source_errors = false`;
- file count and total source bytes;
- start and completion timestamps;
- final status exactly `SUCCEEDED`;
- faults, retries, skipped items, and task-event-log hash.

The CLI and Transfer API have different checksum defaults, so this route never relies on a default. Globus documents that checksum verification compares source and destination and retries a mismatch; it also warns that weaker restart levels can cause corruption [5].

### 5.3 Destination acceptance

Receive files under a manifest-specific staging directory. For every file:

1. require the expected relative path and byte size;
2. compute local SHA-256;
3. require exact equality with the approved source SHA-256;
4. open FITS only after digest equality;
5. atomically rename the complete staging root only after every record passes;
6. write an append-only destination receipt containing the task, manifest, and tree hashes.

A `SUCCEEDED` task without per-file digest equality is insufficient. Extra files, missing files, checksum mismatch, a changed manifest, or a nonzero skipped count closes the gate and preserves no accepted production root.

## 6. Brick mapping and exact margin rule

### 6.1 Human-readable scalar

For a 128-pixel output at `0.262 arcsec/pixel`, the output WCS extends exactly:

`(128 / 2) × 0.262 = 16.768 arcsec`

from its centre to each pixel-edge side.

If the object centre is less than `16.768 arcsec` from a unique brick edge, the output footprint crosses that unique boundary. At two such edges, the output crosses a corner and side plus diagonal neighbours may be involved.

This scalar is not the source-file selection rule. Survey image stacks overlap adjacent images by approximately 130 pixels [3]. A neighbouring 3600-pixel coadd can contribute even when the output does not cross the neighbour's unique-area boundary.

A nominal equatorial illustration gives a 471.6-arcsec image half-width, a 450-arcsec unique-brick half-width, 21.6 arcsec of source intrusion, and a nominal neighbour-intersection threshold of 38.368 arcsec. This number is explanatory only. It must never be used as the executable threshold because RA convergence, TAN geometry, and the actual brick grid matter.

### 6.2 Authoritative executable rule

For each object:

1. Construct the exact output TAN WCS in §7.2.
2. Load the hash-pinned brick geometry row for every candidate near the output centre.
3. Construct each candidate's exact 3600 × 3600, 0.262-arcsec TAN WCS using the pinned Imagine/legacypipe implementation.
4. Represent both images by the pinned nine-point pixel-edge boundary: four corners, four edge midpoints, and the repeated starting corner. For the 128-pixel output each axis samples `0.5`, `64.5`, and `128.5`; the 3600-pixel source uses `0.5`, `1800.5`, and `3600.5` [6].
5. Include a source brick iff the two projected boundary polygons intersect under the pinned `bricks_touching_aa_wcs`/`polygons_intersect` implementation [6].
6. Record candidate, planned-intersecting, opened, resampled-contributing, and zero-pixel-touch sets separately.

The object’s catalogue `BRICKID/BRICKNAME` is a cache-grouping hint, not a sufficient source set. Work is sorted by the complete working-set signature so adjacent and diagonal files can remain cached.

Fail if any planned intersecting brick is absent, digest-mismatched, header-invalid, or unreadable. The current Imagine implementation can log a missing source and continue; the guarded adapter must replace that behavior with a terminal error.

## 7. Frozen local-cut procedure

### 7.1 Code custody

Reference implementation: `https://github.com/legacysurvey/imagine` commit `a06b328e512490ed3a58f753c7649794ae2537b0`, tree `b1d17ce6c26506a6810788615235c532af95e2e3`.

| File | Git blob | SHA-256 |
|---|---|---|
| `many-cutouts.py` | `2b3fb37ed9084148cb3b5e8bb6071a4fb8b29369` | `de6c8dd4b0d1f7500e765ac104728452494d8b810b1ac26f6580316db3fad75a` |
| `cutout.py` | `23a52a0c71fd7840afbe60d1318e086ae9706d99` | `fdc85dfa9098aba4b2acdc41f628dbbbf68fcb95f34c92575e0422c44268ed76` |
| `map/views.py` | `e17a20069e14834f35959c544d80ba1c4aa72cdb` | `c49d3ba9cf05a125ba5a0c6ccead553ae50c069394564c725415f72c88d16e08` |
| `map/coadds.py` | `381a2f8f0b60b5bde292fb2d2df3446de6f16f0b` | `01376b10b338eb561cc589fc5d035b77c81b38cea3e8b56221317757913e8177` |

Manifest SHA-256: `ee2e1d1b5cf433255088e64371537686ca0d7cf042ce8c330dd0d0ae2677c087`.

The commit is reference code, not accepted production code. Before execution, freeze:

- a reviewed guarded adapter hash;
- full dependency lock, including astrometry.net, legacypipe, fitsio, numpy, scipy and resampler code;
- Python version;
- OCI image digest or equivalent immutable environment receipt;
- single-thread and multi-process determinism tests;
- synthetic test corpus and expected-output hashes.

### 7.2 Output WCS

For object `(RA, Dec)`, construct a non-rotated 128 × 128 TAN WCS:

- `NAXIS1 = NAXIS2 = 128`;
- `CTYPE1 = RA---TAN`, `CTYPE2 = DEC--TAN`;
- `CRVAL1 = RA`, `CRVAL2 = Dec`;
- `CRPIX1 = CRPIX2 = 64.5`;
- `CD1_1 = -0.262/3600 = -0.00007277777777777778 deg/pixel`;
- `CD1_2 = 0`;
- `CD2_1 = 0`;
- `CD2_2 = +0.262/3600 = +0.00007277777777777778 deg/pixel`;
- determinant `-5.296604938271605e-09 deg²/pixel²`.

This makes North up and East left. Any rotation, alternate transform, or non-TAN output is outside the frozen contract.

### 7.3 Rendering

1. Validate every source byte digest and original FITS header before invoking Imagine.
2. Select all polygon-intersecting r-band brick images.
3. Read compressed image HDU 1 only.
4. Resample each intersecting source into the exact output WCS using the hash-pinned resampler and interpolation environment [6].
5. Accumulate rendered values and the reference implementation's weight map exactly as pinned. The guarded adapter must additionally maintain a distinct-contributing-source count per output pixel; that count is an added PC-3/PC-4 guard, not a feature attributed to unmodified Imagine.
6. Require positive accumulated weight and at least one valid contributing source for every output pixel.
7. Produce exactly one 2-D float32 r-band image in nanomaggies per pixel.
8. Apply only the frozen V3 nonfinite/invalid-pixel rule; add no route-specific normalization, clipping, stretch, crop, mask, or channel transform.
9. Write to a temporary output, verify §8 and §9, then atomically rename.
10. Hash output bytes and append the immutable per-output receipt.

No public HTTP cutout call, portal image fetch, model, residual, invvar, or maskbits plane is part of this procedure.

## 8. Amended PC-3 — WCS parity and reproducible local geometry

PC-3 no longer accepts “the service returned North-up/East-left.” Our code creates the WCS and is responsible for proving it.

### 8.1 Per-source evidence, mandatory

For every opened source brick, record:

- object/batch ID, brickname, exact source path, source and local SHA-256;
- FITS HDU index and canonical header SHA-256;
- `NAXIS1/2`, `CTYPE1/2`, `CRVAL1/2`, `CRPIX1/2`;
- complete CD matrix or the one explicitly accepted PC×CDELT representation;
- finite, nonzero determinant and its sign;
- source WCS pixel-edge sky coordinates;
- output/source polygon-intersection verdict;
- resampler source/output index-array hashes and contributed-pixel count.

### 8.2 Per-output evidence, mandatory

For every cutout, record and verify:

1. Shape is exactly `(128,128)`, one plane, dtype float32.
2. The exact WCS constants in §7.2 are present.
3. `CRVAL` maps to `(64.5,64.5)` within `1e-6` pixel on both axes.
4. CD determinant is finite, nonzero, and negative.
5. A `+1 arcsec` RA perturbation at the centre decreases output x; a `+1 arcsec` Dec perturbation increases output y.
6. Pixel→sky→pixel round trips at the centre, four pixel centres nearest the corners, and four pixel-edge corners have maximum absolute residual `≤1e-6` pixel.
7. Existing `validate_wcs_parity.py` passes on a production-derived parity receipt; synthetic labels may not substitute for FITS-derived values.
8. Planned source set, opened source set, contributing source set, and zero-touch source set are recorded; any unexplained difference fails.
9. Per-pixel coverage-count plane is hashed; its minimum is at least 1; zero-coverage count is 0.
10. Output header hash, data-array hash, whole-file SHA-256, code-manifest hash, container digest, source-manifest hash, and transform-receipt hash are recorded.

### 8.3 Boundary test matrix before production

The guarded adapter must pass deterministic synthetic fixtures for:

- centre of a brick;
- within, exactly at, and beyond `16.768 arcsec` of each unique edge;
- all four unique-area corners;
- cases where overlapping source images contribute without the output crossing a unique boundary;
- RA wrap at 0/360 degrees;
- the highest and lowest declinations in the selected South footprint;
- one, two, three, and four contributing source images;
- reversed source order and multi-process scheduling.

The source-set signature, output WCS receipt, coverage receipt, and output-array hash must match the fixture expectation.

## 9. Amended PC-4 — fail-closed source and output distortion handling

PC-4 moves ahead of the local WCS parser. It applies separately to every source header and again to every output header.

### 9.1 Pre-parse source-header gate

Read the original HDU-1 header as cards without first reducing it to a TAN object. Run the hash-pinned `fail_closed_wcs.py` policy, extended only through a reviewed successor adapter, and reject:

- SIP (`-SIP`, `A_*`, `B_*`, `AP_*`, `BP_*`);
- PV/TPV terms;
- CPDIS, DP/DQ, D2IM, DET2IM and other lookup distortions;
- non-celestial, missing, duplicated, swapped, or ambiguous celestial axes;
- missing CRVAL or CRPIX terms;
- incomplete CD matrices;
- incomplete PC/CDELT matrices;
- mixed CD and PC/CDELT encodings unless one reviewed canonical rule proves exact equivalence;
- nonfinite coefficients;
- zero or singular determinant;
- unsupported alternate WCS versions;
- any unrecognized distortion-bearing keyword.

This must occur before `map/coadds.py`. The pinned fallback calls `hdr.get('CD…', 0.)`, so allowing it to parse first could turn missing matrix terms into zeros [6]. No default-zero recovery is allowed.

### 9.2 Runtime fail-closed conditions

Any of the following is terminal for that output and batch shard:

- required source absent, digest mismatch, truncated FITS, unreadable HDU, or unexpected shape;
- planned source omitted by the renderer;
- WCS parse warning or exception;
- resampling exception, empty index arrays where overlap is expected, or nonfinite mapping;
- unexplained planned/opened/contributing source-set difference;
- any output pixel with zero coverage;
- output WCS keyword mismatch, determinant/parity/round-trip failure, or forbidden distortion keyword;
- output shape, dtype, band, unit, or invalid-pixel-policy mismatch;
- receipt or hash write failure.

On failure: write a terminal error receipt, delete/quarantine the staged output, do not rename it, do not mark the object complete, do not continue as a successful zero-filled cutout, and do not silently refetch.

### 9.3 Required PC-4 rejection fixtures

Before production, prove rejection with synthetic FITS headers for:

- SIP, PV/TPV, CPDIS, D2IM and DET2IM;
- partial CD matrix;
- partial PC/CDELT matrix;
- simultaneous CD and PC/CDELT;
- singular, NaN and infinite matrix terms;
- missing CRPIX, CRVAL or CTYPE;
- non-celestial and swapped axes;
- alternate WCS suffixes;
- source file missing after manifest approval;
- intersecting neighbour absent;
- one uncovered output pixel;
- output header altered after generation.

A clean canonical TAN source/output pair must pass. The fixture ledger must bind fixture bytes, expected error code, observed error code, staged-file absence, and test-run hash.

## 10. Current code gaps that keep the gate closed

The unmodified reference code is insufficient for production acceptance:

1. It can skip a missing brick image and continue rendering.
2. Its TAN fallback can default missing CD terms to zero [6].
3. It does not emit the complete source-set, per-source header, per-pixel coverage, parity, and distortion receipts required here.
4. Its repository commit does not freeze external dependency behavior.
5. It does not make the existing PC-3 and PC-4 validators part of an atomic output-acceptance transaction.

These are implementation obligations, not reasons to abandon the chosen route. A successor build packet must add the guard/receipt adapter without altering V3.

## 11. Gate sequence

No steps may be collapsed:

1. **Paper acceptance:** Duho accepts this successor route wording.
2. **Build gate:** implement guarded adapter, immutable environment, synthetic fixtures, and receipts; no survey data.
3. **Kun reproducibility gate:** independently reproduce code hashes, fixture results, PC-3 evidence, PC-4 rejection matrix, and atomic-failure behavior.
4. **Manifest-only gate:** using the already-authorized frozen parent, compute the exact brick working set and sealed source manifest; transfer nothing.
5. **Transfer approval:** Duho explicitly approves the manifest hash, destination, and byte total.
6. **Globus transfer:** explicit batch, checksum verification, zero skipped files.
7. **Destination acceptance:** all local SHA-256s equal source manifest.
8. **Local-cut canary:** edge/corner-stratified bounded canary; PC-3/PC-4 receipts reviewed.
9. **Production approval:** separate explicit gate.

Until step 5, no Globus task may be submitted or endpoint activated. Until step 8 passes, no production shard may run.

## 12. Zero-transfer and custody receipt

This lane performed documentation and public source-code retrieval only.

- Globus endpoints activated: 0
- Globus tasks submitted: 0
- transfer manifests executed: 0
- survey image files listed or fetched: 0
- brick images transferred: 0
- cutouts requested or generated: 0
- catalogue rows or positions read/exported: 0
- HTTP HEAD/range/product probes: 0
- empirical estimator runs: 0
- publication/acceptance/deploy/restart: 0
- git commit/push/merge: 0

Supporting evidence:

- `_tmp_route_source_01_thread.md` through `_tmp_route_source_06_imagine_code.md`;
- `_tmp_route_citations.json`;
- `_tmp_route_code_manifest.json`;
- `_tmp_route_margin_arithmetic.json`;
- `_tmp_HWAO_ROUTE_AMENDMENT_RELAY_RECEIPT.md`.

Citation-ledger SHA-256 before final report verification: `452156c6456f7db5747e6fc15dabc5ce08014fa3cda9221cc0f51516969a1a0c`.

Branch at custody check: `feat/paper-workflow-v2`.
HEAD at custody check: `6a74f6a811435cbe5dd927c8a82f04e0157b0159`.
Tori made no commit.

## 13. Exact next action

Build, offline only, the guarded local-cut adapter and its synthetic edge/distortion fixture suite. It must make the source-set/coverage evidence and PC-3/PC-4 checks atomic prerequisites to output acceptance. Do not construct the real brick manifest and do not submit Globus until that build passes Kun’s independent reproducibility gate and Duho separately approves transfer.

## Sources

[1] [decam-legacy-survey: “NERSC cutout service?”](https://groups.google.com/g/decam-legacy-survey/c/TnFOmW_DDfM/m/FwlPbZSJAgAJ), posts by Andrew Engel, Dustin Lang, and John Moustakas, May 2025; stable per-message locators are preserved in `_tmp_route_source_01_thread.md`.

[2] [Legacy Survey DR10 files — Image Stacks](https://www.legacysurvey.org/dr10/files/#image-stacks-south-coadd), accessed 2026-08-15.

[3] [Legacy Survey DR10 known issues](https://www.legacysurvey.org/dr10/issues/#the-sub-blob-issue) and [DR10 description](https://www.legacysurvey.org/dr10/description/#image-stacks-south-coadd), accessed 2026-08-15.

[4] [NERSC Globus documentation](https://docs.nersc.gov/services/globus/) and [Data Transfer Nodes](https://docs.nersc.gov/systems/dtn/), accessed 2026-08-15.

[5] [Globus CLI transfer reference](https://docs.globus.org/cli/reference/transfer/) and [Transfer API task submission](https://docs.globus.org/api/transfer/task_submit/), accessed 2026-08-15.

[6] [Legacy Survey Imagine repository at commit `a06b328e512490ed3a58f753c7649794ae2537b0`](https://github.com/legacysurvey/imagine/tree/a06b328e512490ed3a58f753c7649794ae2537b0), commit dated 2026-08-11; per-file Git and SHA-256 hashes are in `_tmp_route_code_manifest.json`.
