PASS_READSTAGE_AND_ROUND4

# KUN READSTAGE + ROUND-4 GATE -- 2026-08-16

## Verdict

**PASS_READSTAGE_AND_ROUND4.**

The read/decompression stage is a real architectural separation, not a cosmetic
rename. The adapter remains byte-identical to the resampler-gated adapter and
keeps its stdlib-only source boundary. The new readstage owns the `astropy` /
`numpy` dependency and emits canonical uncompressed adapter-input bytes.

Round-4 now passes as a read-path gate: compressed `.fits.fz` HDU-1 sources are
decoded, chained through read receipts, staged into the adapter's unchanged
input format, and crossed against the uncompressed staging path with exact byte
identity for all three round-4 cases.

This remains build-only and synthetic-only. It authorizes no network, no real
survey data, no source manifest against the real parent set, no sky statistic,
no rows/positions/images/chirality, no publication, no accepted status, no
commit, and no push.

## Hashes Measured

- brief `prereg/_tmp_kun_readstage_gate_brief_20260816.md`
  - SHA-256 `565790f820065f414cd2e62e1dc9afc97196cb6c5fe8c868632ea9edfd2b020a`
- readstage `prereg/readstage/nm_brick_read_stage.py`
  - SHA-256 `6662c8c74d71b81216149596d65deeaa39c07a19a57e50ba9bbe4ac22d478b0a`
- readstage tests `prereg/readstage/test_nm_brick_read_stage.py`
  - SHA-256 `dd669e434de0319d237f53a16792c3a9c0a2b61457b84ea81a01d9d71c325790`
- adapter `prereg/adapter/nm_brick_cutout_adapter.py`
  - SHA-256 `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`
- cross-runner `prereg/adapter/cross_check_yui_boundary.py`
  - SHA-256 `3bb84cefe44eea4a49b8d8ef7bad6a64a92137d67731606e4bccbe33703f9436`
- round-1 fixture generator
  - SHA-256 `24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d`
- round-2 fixture generator
  - SHA-256 `60e3d662d72fbc87e0c82889b4f9174c033882b8f9a2019011c5104bb4aa15bc`
- round-3 fixture generator
  - SHA-256 `6b410fb40def2869d4f3431f029654d8fa7cacd20741dca5a84b12409d5e5e62`
- round-4 fixture generator
  - SHA-256 `d6c193841ff8ff52f1188ae1d48bbe5ea8c89bf553c542ad176f70189b7b7533`
- dependency lock `prereg/YUI_DEPENDENCY_ENVIRONMENT_LOCK_20260816.json`
  - SHA-256 `6e0c9ae2c414f0659c1dda5fba4f42bb417924fb64bb0bb08fb60d6d0f6e24ab`

Final cross receipt:

- path `prereg/adapter/CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json`
- file SHA-256 `b0a41f9b7be1a8965238e5d73a82ca7426add6159c64ef1d8ea061b919acabac`
- internal `content_sha256`
  `c30a7b315a55a24bb3a022bc851f38b7c79e12b8f58903e7dece7b344773a978`
- `content_hash_excludes`: `["content_sha256", "recorded_utc"]`

## Runs Performed

Cross-runner run 1:

- command: `python3 prereg/adapter/cross_check_yui_boundary.py`
- status: `PASS`
- `content_sha256`
  `c30a7b315a55a24bb3a022bc851f38b7c79e12b8f58903e7dece7b344773a978`
- `recorded_utc` `2026-08-16T10:06:39Z`
- round 1: `29/29`, `0` failed
- round 2: `4/4`, `0` failed
- round 3: `10/10`, `0` failed
- round 4: `3/3`, `0` failed

Cross-runner run 2:

- status: `PASS`
- `content_sha256`
  `c30a7b315a55a24bb3a022bc851f38b7c79e12b8f58903e7dece7b344773a978`
- `recorded_utc` `2026-08-16T10:07:07Z`
- round 1: `29/29`, `0` failed
- round 2: `4/4`, `0` failed
- round 3: `10/10`, `0` failed
- round 4: `3/3`, `0` failed

Readstage unit tests:

- command from `prereg/readstage`: `python3 -m unittest test_nm_brick_read_stage`
- result: `9/9` passed

Receipt hash recomputation:

- main cross receipt content hash: `PASS`
- embedded round-4 read receipts: `5/5` content hashes recomputed

The four blocks are reported separately. I found no standalone merged `46`
case-count field in the cross-runner or receipt.

## Rulings

1. **Separation is real.**

   The adapter source imports only stdlib modules:
   `argparse`, `datetime`, `hashlib`, `importlib.util`, `json`, `math`,
   `pathlib`, `re`, `struct`, `sys`, and `typing`.

   The readstage imports `numpy`, `astropy`, and `astropy.io.fits`, then imports
   the adapter. The adapter does not import the readstage. The dependency
   direction is therefore readstage -> adapter, not adapter -> readstage.

   There is one important wording boundary: in the same cross-runner process,
   `numpy` and `astropy` are loaded before adapter calls happen. So the
   stdlib-only invariant is a module/input-contract invariant, not a claim
   that the whole test process contains no third-party packages. That is the
   correct separation for the chosen architecture.

2. **Round-4 size is adequate for this gate.**

   Round-4 has only three cases, so it is not a broad transfer/read-path
   validation. It is adequate for this gate because it tests the new container
   class rather than redoing coverage geometry: empty primary, RICE_1 compressed
   image HDU 1, raw compression cards, HDU-1 decode, WCS verification, canonical
   adapter staging, and byte-identity against the uncompressed path.

   It is not adequate before transfer or real-source-manifest use. A later
   production-read gate still needs real route artifact binding, the real
   decoder environment lock, and production `.fits.fz`/HDU behavior under the
   exact execution environment.

3. **Exact equality is enforced where it must be.**

   Round-4 does not use a tolerance to compare compressed-vs-uncompressed
   read-path output. The receipt reports:

   - `round4_byte_identity.all_cases_byte_identical: true`
   - comparison: `adapter output bytes, read-stage path vs uncompressed staging path, exact`

   The round-4 pixel-agreement block still records parent-round tolerances for
   comparison against Yui's expected arrays. That is separate from the
   read-path equality question. The codec/readstage path itself is checked by
   exact output-file byte identity for all three round-4 cases.

4. **Receipt chain binds.**

   Each embedded read receipt includes and hash-binds:

   - `source_file_sha256`
   - `raw_primary_header_sha256`
   - `raw_hdu1_header_sha256`
   - `raw_compression_cards`
   - `decompressed_array_sha256`
   - `decoder_environment_lock`
   - `adapter_input_file_sha256`
   - `adapter_sha256`
   - `content_sha256`

   The cross-runner also checks `decompressed_array_sha256` against the parent
   fixture `data_sha256`, and the readstage unit test checks the staged adapter
   input bytes against direct uncompressed staging of the same decoded array.
   This is not decorative receipt text; the values are compared in code.

5. **Dependency lock status.**

   Yui's dependency lock covers the installed `astropy` and `numpy` versions
   present here: `astropy 6.0.1` and `numpy 1.26.4`. The readstage receipt also
   embeds a partial decoder lock with Python version, those package versions,
   and hashes of Astropy's tiled-compression modules.

   But the Yui lock predates this readstage file and does not include the
   readstage source as a locked artifact. For this synthetic gate that is
   acceptable because the readstage file is hash-pinned separately above. Before
   production reliance, the dependency lock should be reissued or amended to
   include the readstage source, moved cross-runner hash, and decoder-module
   fingerprints as a single production-read environment record.

## Earlier Passes

The adapter is byte-identical to the resampler-gated adapter:
`267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`.

Therefore the earlier corner-repair, round-2, round-3, and resampler passes
carry without revisiting the adapter. This gate adds a separate synthetic
readstage pass and round-4 read-path cross-check on top of them.

The pass stops at the synthetic read/decompression boundary. Any next step that
touches real galaxies, real bricks, real source manifests, sky statistics, or
chirality is outside this gate.
