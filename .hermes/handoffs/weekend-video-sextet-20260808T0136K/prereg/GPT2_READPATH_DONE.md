GPT2_READPATH_COMPLETE

# Production DR10 South coadd read path — 2026-08-19

## Result

PASS. `_production_readpath_20260819/production_readpath.py` now provides a production `ProductionBrickSource` whose first three constructor arguments and runtime fields match the gated adapter source contract: `path`, `row`, `expected_sha256`; `sha256`, `header_sha256`, `cards`, `data_offset`, `wcs`, `gate_receipt`; `pixel(ix, iy)`; and `close()`.

The existing gated adapter was not edited. Its measured SHA-256 remains:

`267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`

Reader SHA-256:

`105bd0c6858f27166fecee5ff7ece42c0e993eab8e3bc15b517f9bc9b5418d56`

## Decompression and dependency pin

- Decompressor: `astropy.io.fits`, backed by Astropy's CFITSIO handling of fpack compressed images.
- Physical selection: exactly HDU index 1.
- Required HDU class: `CompImageHDU`; any missing, wrong, or unreadable HDU fails closed.
- Real compression observed: `RICE_ONE`.
- Versions pinned in `_production_readpath_20260819/requirements.lock`:
  - `astropy==6.0.1`
  - `numpy==1.26.4`
- Lock SHA-256: `e4c38a4d117c52795fbdb7928d71237236ce2fac046df7eeac07585cb66ee906`.
- Runtime refuses dependency-version drift.

## WCS custody / PC-3 and PC-4

The reader does not assume that decompression preserves a usable WCS. It extracts the decompressed logical HDU-1 header, passes its ordered value cards through the adapter's hash-pinned fail-closed PC-4 gate before exposing the array, then builds the adapter's `TanWcs` from the verified matrix.

The logged receipt records:

- source-file and logical-header SHA-256;
- physical HDU index, HDU class/name, compression algorithm, shape, dtype, byte order, and C memory order;
- `CTYPE1/2`, `CRVAL1/2`, `CRPIX1/2`, and `CD1_1..CD2_2`;
- linear matrix and determinant;
- combined pixel-to-sky determinant;
- North-up and East-left predicates;
- FITS one-based pixel-centre origin;
- row-order transform `array[iy-1, ix-1]`;
- pinned distortion/parity validator hashes and complete PC-4 gate receipt;
- decompressed array SHA-256.

Real header receipt: `_production_readpath_20260819/real_header_receipt.json`.

For brick `0001m395`, PC-4 passed with no distortion family, CD representation, North-up/East-left true, and determinant `-5.296604938271607e-09`.

## Determinism verification

Command:

`python3 -m unittest -v test_production_readpath.py`

Result: `6/6` tests passed in `3.403s`.

Covered:

1. Offline-safe synthetic fpack fixture reads HDU 1 and matches the adapter source interface.
2. Header/WCS custody receipt is atomically logged as canonical JSON.
3. Wrong source digest fails closed.
4. Two independent reads produce literally byte-identical float32 arrays and identical header receipts.
5. Four spawned processes read the same fixture and produce identical array hashes and canonical worker receipts under two different forced completion orders.
6. The same sequential and four-process checks pass on a real receipt-accepted DR10 South brick.

Real verification command:

`python3 verify_real_brick.py`

Result: `PASS`.

- Brick: `0001m395`
- Receipt outcome: `ACCEPTED`
- Receipt digest verification: `true`
- Source-file SHA-256: `43c58507cc8edfed5607436c1e4834f01c1f360091bac14ad6a4e2a0dea4855a`
- Array SHA-256 from every read/process: `1a2dbb0fff233c2aeea08b907e088807b6036d868b5913e3e40f9d68af82a285`
- Sequential arrays byte-identical: `true`
- Sequential header receipts identical: `true`
- Process count: `4`
- Forced completion-order probes: `2`
- Observed completion orders differed: `true`
- Stable multiprocessing content SHA-256 across both orders: `6bd4925ee1c7fd14ca1cdab19ab083ac9e886938b8c792d907bc452d4e9493b5`
- Stable receipt explicitly excludes only `observed_completion_order` and `recorded_utc`; that exclusion list is inside the hashed stable body. PID, hostname, worker identity, temp path, and timestamps do not enter stable worker content.

Full receipt: `_production_readpath_20260819/real_verification_receipt.json`.

## Source-location note

At verification time, `/Users/duhokim/NebulaMindData/dr10_south_image_r/coadd/` did not yet exist. The transfer receipt already marked the tested brick `ACCEPTED` and digest-verified, but the transfer-owned file remained at:

`/Users/duhokim/NebulaMindData/dr10_south_image_r/staging/coadd/000/0001m395/legacysurvey-0001m395-image-r.fits.fz`

The verifier prioritizes the requested final `coadd/` path and falls back only to a file under `staging/coadd/` whose on-disk SHA-256 exactly matches an `ACCEPTED`, `digest_verified=true` receipt. Nothing under `/Users/duhokim/NebulaMindData/dr10_south_image_r/` was written, moved, renamed, or modified.

## Boundaries

- No network access was used by this build or verification.
- `portal.nersc.gov` was never contacted.
- No adapter, source-data, transfer, database, cockpit, publication, git commit, or push action occurred.
- The multiprocessing evidence covers one real brick, four spawned processes, two observed completion orders, one machine, and one OS. It does not claim cross-platform or full-campaign-scale determinism.
