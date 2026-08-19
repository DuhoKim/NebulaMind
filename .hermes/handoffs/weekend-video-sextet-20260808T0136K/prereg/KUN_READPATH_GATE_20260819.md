PASS_PRODUCTION_READPATH

# KUN PRODUCTION READ-PATH GATE -- 2026-08-19

## Verdict

**PASS_PRODUCTION_READPATH.** I re-ran the deliverable's own tests and its
real-brick verifier, recomputed every receipted hash, and independently
checked the reader's interface against the hash-pinned gated adapter. Every
claim in `GPT2_READPATH_DONE.md` reproduced. No repairs required.

## What I ran myself (not just read)

1. `python3 -m unittest -v test_production_readpath.py` in
   `_production_readpath_20260819/`: **6/6 passed in 3.373s** (DONE doc: 6/6
   in 3.403s). The real-accepted-brick test ran, not skipped.
2. `python3 verify_real_brick.py` (backs up then regenerates both receipts):
   **status PASS**. Brick `0001m395`, receipt outcome ACCEPTED,
   digest_verified true.
   - Sequential reads byte-identical: true. Sequential header receipts
     identical: true.
   - Regenerated `real_header_receipt.json` is **byte-identical** to the
     recorded one (fully deterministic).
   - Regenerated `real_verification_receipt.json` differs only in
     `recorded_utc` — a field inside the declared
     `content_hash_excludes: ["observed_completion_order", "recorded_utc"]`,
     which sits inside the hashed stable body. Stable multiprocessing content
     SHA-256 `6bd4925ee1c7fd14ca1cdab19ab083ac9e886938b8c792d907bc452d4e9493b5`
     reproduced exactly; the two forced completion orders differed.
   - Array SHA-256 `1a2dbb0fff233c2aeea08b907e088807b6036d868b5913e3e40f9d68af82a285`
     from every read and every one of the 4 spawned processes.

## HDU-1 selection and decompression pin (receipted)

- `real_header_receipt.json` records `hdu_index: 1`, `hdu_class:
  CompImageHDU`, `compression_type: RICE_ONE`, `decompressor:
  astropy.io.fits`, `astropy_version: 6.0.1`, `numpy_version: 1.26.4`.
- `requirements.lock` pins `astropy==6.0.1`, `numpy==1.26.4`; its measured
  SHA-256 `e4c38a4d117c52795fbdb7928d71237236ce2fac046df7eeac07585cb66ee906`
  matches the DONE doc. System python3 (3.9.6) reports exactly those versions.
- Code reading confirms drift refusal: `ProductionBrickSource.__init__`
  raises `FAILED_DEPENDENCY_PIN` before any file open if versions differ, and
  `FAILED_HDU_SELECTION` if HDU 1 is missing or not a `CompImageHDU`.

## WCS custody per the PC-3/PC-4 concern

- The reader extracts the decompressed logical HDU-1 header cards and passes
  them through the adapter's hash-pinned `fail_closed_header_gate` (PC-4)
  **before** materializing the array (production_readpath.py:154-162).
- The receipt's `wcs_custody` block carries `status: VERIFIED_NOT_ASSUMED`,
  the full WCS card set, linear matrix and determinant, combined
  pixel-to-sky determinant `-5.296604938271607e-09`, east-left/north-up true,
  FITS one-based origin, `array[iy-1, ix-1]` row-order transform, and the
  complete PC-4 gate receipt. This matches the round-4 scoping
  recommendation (`KUN_ROUND4_READPATH_SCOPE_20260816.md`): a separate pinned
  decompression stage whose receipt ties source-file hash, logical-header
  hash, decompressed-array hash, and decoder environment together.
- Pinned validator hashes inside the receipt match the on-disk files I
  re-hashed: parity `7bf0201917e7722ee9545c9c11b6cc1cbdec345504e3f29fa1aeb01e58edaa55`,
  distortion `cae1b1b7ef4e25000ad5d8c906647216b1425638ac737b4ea7363ca948760569`.
- The gated adapter itself is unchanged: measured SHA-256
  `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`, matching
  the resampler-gate-pinned value. Reader SHA-256
  `105bd0c6858f27166fecee5ff7ece42c0e993eab8e3bc15b517f9bc9b5418d56` matches
  the DONE doc.

## Interface vs the resampler-gate-certified adapter contract

I ran an independent structural conformance probe (16 checks, all green,
INTERFACE_MATCH) against the adapter the resampler gate certified
(`KUN_RESAMPLER_GATE_20260816.md`, same adapter SHA):

- Constructor first three positional parameters are exactly
  `(path, row, expected_sha256)` on both classes.
- Live instance on the real brick exposes `path`, `sha256`, `header_sha256`,
  `cards`, `data_offset`, `wcs`, `gate_receipt`; `pixel(ix, iy)` and
  `close()` are callable with matching signatures; context-manager protocol
  works.
- `wcs` is an instance of the adapter's own `TanWcs` loaded through the
  hash-pinned import (same class object), so `sky_to_pixel`/`pixel_to_sky`
  semantics are the gated ones, not a reimplementation.
- `pixel()` 1-based FITS semantics verified against direct astropy reads on
  the real brick at 7 positions (all four corners, centre, two off-diagonal):
  all equal. Out-of-range `(0,1),(1,0),(3601,1),(1,3601)` all raise
  IndexError.
- Noted, not a defect: `data_offset` is `None` on the production source (an
  int on the synthetic one). The certified adapter consumes sources only via
  `source.wcs` and `source.pixel` in `render_cutout`; no external consumer of
  `source.data_offset` exists (grep-verified), so `None` is contract-safe.
  `expected_shape` is an additive keyword-only parameter used only for small
  offline fixtures.

## Read-only on the data root

- The reader opens sources `"rb"` / `fits.open(mode="readonly")`; all receipt
  writes target the deliverable directory, never
  `/Users/duhokim/NebulaMindData/dr10_south_image_r/`. The verifier
  prioritizes `coadd/` and falls back only to a staging file whose hash
  matches an ACCEPTED, digest-verified receipt.
- Files currently changing under the data root (receipts.jsonl, new staging
  bricks) are the separately-authorized live transfer appending new bricks,
  observed mid-gate; the tested brick `0001m395` itself was untouched (mtime
  predates this gate; only atime could have moved).

## Boundaries

Findings-only. No network used by this gate; `portal.nersc.gov` never
contacted. No adapter, source-data, transfer, database, cockpit, publication,
or git action taken. Determinism evidence remains scoped to one real brick,
4 processes, 2 forced completion orders, one machine, one OS — as the DONE
doc itself declares.
