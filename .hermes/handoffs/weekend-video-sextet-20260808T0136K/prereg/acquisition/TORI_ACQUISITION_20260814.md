# Tori acquisition build receipt — 2026-08-14

Status: **BUILT AND SELF-TESTED; BUILD ONLY; REAL ACQUISITION CLOSED**

This receipt records implementation, not authorization to run it against the survey. Duho owns acceptance; Kun gates any later execution.

## Hard boundary outcome

The brief's successful stop condition was obeyed:

> “the moment the next step would touch real galaxies, this lane STOPS and reports that as the successful outcome.”

The build never reached that moment because the executable contains no real transport. It can construct synthetic dry-run requests and process bytes supplied by its exact `MockTransport` class. The CLI exposes only a fixed synthetic `--dry-run`. A non-dry invocation, a non-synthetic identifier, or any transport other than the exact mock class fails with `BUILD_ONLY_STOP` before fetch.

Boundary ledger:

- real catalogue rows read: **0**
- real positions read: **0**
- real cutouts requested/received: **0 / 0**
- network calls: **0**
- chirality/morphology outputs: **0**
- sky statistics: **0**
- publication/acceptance/commit/push: **0 / 0 / 0 / 0**

## Deliverables

| File | Purpose | SHA-256 |
|---|---|---|
| `nm_acquire_cutouts.py` | Build-only pipeline, exact route planning, synthetic selection, mock custody, resume, rate/backoff, FITS and WCS gates | `5f48066b8a7d56e6d595765cca7ea762197b0473fdde2820acaa0cf59862f400` |
| `test_nm_acquire_cutouts.py` | Synthetic FITS fixtures, mock interruptions/pressure, and 14 offline tests | `6e68af6229af087762313dc335bed3f3c20fdb70d55b19985ac202b772f4c3a8` |
| `SELFTEST.md` | Actual test, static-audit, and release-linter results | `b984f8c768953d6256252bce7ea75258db9ccdeae136fcd374c797bf78966b6c` |
| `TORI_ACQUISITION_20260814.md` | This receipt | hash recorded after final verification |

## PC-1 route — quoted, not reconstructed

The controlling route binding says:

> **BOUND PRODUCT ROUTE:** the current DESI Legacy Imaging Surveys **DR10.1 southern
> (DECam) route**, using the `ls-dr10-south` generated FITS-cutout product as the measurement
> pixels and the updated DR10.1 southern sweeps and matched products as the source/covariate
> catalogue route.

It freezes this later-run request:

> `https://www.legacysurvey.org/viewer/fits-cutout`
>
> `?ra=<DR10.1_RA>&dec=<DR10.1_DEC>&layer=ls-dr10-south&pixscale=0.262&bands=grz&size=256`

And defines:

> - `layer=ls-dr10-south`: southern DECam DR10/DR10.1 only;
> - `pixscale=0.262`: the documented optical brick scale in arcsec/pixel;
> - `bands=grz`: exactly g, r, and z, in that order; i and WISE are not measurement channels;
> - `size=256`: a square 256×256 analysis raster per optical band;
> - response format: FITS only, never JPEG/PNG;
> - no post-delivery rotate, reproject, interpolate, resize, or WCS transform;
> - the delivered FITS planes in FITS-native row order are the final analysis raster.

The implementation constructs that exact South-only parameterization. During exact-text verification, a first draft using composite `ls-dr10` was caught by a RED test and corrected to `ls-dr10-south`. The corrected route passed the complete suite.

## Frozen Cut 1–6 selection

`FROZEN_SELECTION_STAGES` and `evaluate_frozen_selection()` encode this ordered chain:

1. `brick_primary = 1 AND maskbits = 0`;
2. `type <> 'PSF' AND flux_r > 0`;
3. exact photo-z join on `(ls_id, release, brickid, objid)` and `0 <= z_phot_median < 0.15`;
4. `dered_mag_r < 17.7`;
5. `shape_r > 1.5`;
6. `POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551`.

The selector is executable only on records marked `SYNTHETIC_ONLY_BUILD`; it retains no input row in its result. Tests observe one pass and one failure at every stage. There is deliberately no catalogue reader or TAP/filesystem adapter for real rows.

## Request and checksum custody

For every synthetic plan or mock response:

1. Request fields are canonicalized as sorted compact JSON and SHA-256 hashed.
2. `request_log.jsonl` is append-only and hash chained with `previous_event_sha256` and `event_sha256`.
3. Existing log hashes are verified before each append; tampering stops the run.
4. Before mock fetch, state becomes `IN_FLIGHT_UNCERTAIN` and is written atomically.
5. Response bytes are SHA-256 hashed and staged before validation.
6. State becomes `RESPONSE_CUSTODIED` with the staged relative path and response hash.
7. FITS and WCS gates run before the staged bytes become a cutout.
8. The final file is re-read and hashed; response and output hashes must match.
9. A per-object private receipt records request, response, output, validator, parity, and distortion custody.

The request log and receipts are private analysis custody. They are not release artifacts.

## Resumability

The state machine is fail closed:

| Existing state | Resume action |
|---|---|
| `COMPLETED` | Re-read receipt and output, verify all hashes, log `RESUME_COMPLETE_NOT_REFETCHED`, do not fetch |
| `RESPONSE_CUSTODIED` | Verify staged path and response hash, log `RESUME_RESPONSE_CUSTODIED`, validate staged bytes, do not fetch |
| `IN_FLIGHT_UNCERTAIN` | Log and count `RESUME_IN_FLIGHT_UNCERTAIN_NOT_REFETCHED`; operator authorization is required before any retry |
| terminal FITS/WCS/transport failure | Verify private failure receipt, log/count `RESUME_TERMINAL_FAILURE_NOT_REFETCHED`, do not retry silently |
| `RETRY_WAIT_SAFE` in the same bounded attempt | Retry only the explicit `RetryableTransportError` path after frozen backoff |

Completed, response-custodied, uncertain, and terminal-failure resume branches were all observed in synthetic tests. A state/receipt/hash mismatch raises and never falls through to fetch.

## Rate limiting and backoff

Frozen policy values:

- maximum concurrent requests: **1**;
- minimum interval between request starts: **5.0 seconds**;
- explicit retry backoff: **30, 60, 120 seconds**;
- maximum attempts after three backoffs: **4 total attempts**;
- retryable class: only explicit `RetryableTransportError`;
- all other transport/program errors: no catch-all retry.

The tests use an injected fake clock. Two mock requests occurred at monotonic times 100 and 105, and synthetic service pressure produced exactly one 30-second backoff before success. No real sleeping or service access occurred in verification.

## FITS integrity

The parser fails closed unless the response is a complete FITS primary cube with:

- byte length divisible by 2880;
- `SIMPLE = T` and an `END` card;
- supported `BITPIX`;
- `NAXIS = 3` and shape exactly `[3, 256, 256]` for ordered g/r/z planes;
- exact padded byte length, with no truncated data or undeclared extension bytes.

Corrupt or truncated bytes produce `FAILED_FITS_INTEGRITY`, a response hash, a counted private failure receipt, no stored cutout, and no staged residue.

## PC-3 parity — one reused implementation

The pipeline imports Yui's validator at runtime from:

`yui_bs5_sign_anchor_20260814/validate_wcs_parity.py`

Pinned SHA-256:

`7bf0201917e7722ee9545c9c11b6cc1cbdec345504e3f29fa1aeb01e58edaa55`

It reuses Yui's `determinant_2x2`, `multiply_2x2`, and `build_parity_receipt()` row-order convention. It does not copy a second determinant implementation. For each mock object it logs:

- complete CD or PC×CDELT matrix;
- linear determinant;
- FITS-native row-order transform and determinant convention;
- combined pixel-to-sky matrix, determinant, and sign;
- North-up and East-left predicates.

A non-finite/singular determinant or anything other than North-up/East-left is rejected before output. The parity-flipped fixture fired `REJECTED_PARITY`.

## PC-4 / BS-7 distortion branch

The pipeline imports the fail-closed detector from:

`_tori_bs7_distortion_evidence/fail_closed_wcs.py`

Pinned SHA-256:

`cae1b1b7ef4e25000ad5d8c906647216b1425638ac737b4ea7363ca948760569`

It rejects before output when the header contains:

- SIP `A/B/AP/BP` terms;
- `PV1_*` or `PV2_*`;
- `CPDIS*`;
- `D2IM*` or `DET2IM*`;
- non-celestial CTYPE;
- partial, missing, or ambiguous CD / PC×CDELT representation;
- singular or indeterminate linear WCS.

The local-Jacobian branch is absent. The SIP fixture fired `REJECTED_DISTORTION` and left no cutout.

## Public-output boundary

`release_linter/nm_release_lint.py` SHA-256:

`7ff18bfc9272bcbb924b77cb81f2b37c45a130c2b1c5ba1fbc9b95baaab323ac`

Its own synthetic matrix passed **22/22**. A temporary proposed package containing a synthetic acquisition state, request log, per-object receipt, and FITS was then rejected with:

- `E_R1_EMBEDDED_OBJECT_RECORD`;
- `E_FILE_UNKNOWN_TYPE`.

Therefore the acquisition outputs remain private analysis inputs. The build proposes no public files, derived catalogue, request log, receipt, object identifier, position, URL, or FITS cutout.

## Limits

This build intentionally does not include:

- a real HTTP transport or network client import;
- a real catalogue/sweep reader;
- real coordinates or object identifiers;
- bulk-mirroring logic;
- a local-Jacobian distortion path;
- any post-delivery transform;
- a public-output exporter;
- model inference, chirality, morphology, or sky-statistic code;
- standing authorization to execute.

The strict FITS parser is bound to the frozen three-plane primary-cube design. A future service response with a different HDU layout is rejected until separately audited; it is not accepted by weakening the parser.

## Hash-pinned inputs

| Input | SHA-256 |
|---|---|
| `_tmp_TORI_ACQUISITION_BRIEF.md` | `96894ca7060100716016cac04c4af149cf48fd8f8719ef19993a58e57bcfd3c2` |
| `TORI_SURVEY_ROUTE_BINDING_20260812.md` | `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87` |
| `PREREG_LONGO_AMPLITUDE_TEST_20260812.md` | `ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590` |
| `TORI_BS1_CLOSURE_PACKET.md` | `50bf06b0f28c690360751d60cb150387446fee1c5f3629036515234b0301b8f5` |
| Hwao acquisition relay receipt | `e644d0f3a8c766b007d549d88b7e7d7e56b429f63fa54e4775300db169b12a66` |

## Exact future gate

The next step is **not** to run this artifact. A real acquisition requires a fresh, separate authorization that identifies the exact real parent-input custody, permits image requests, confirms service policy/rate values, and opens an execution guard. Kun must then gate the exact revised execution package. Until that happens, the correct state is:

**PIPELINE BUILT; REAL TRANSPORT ABSENT; ACQUISITION CLOSED.**
