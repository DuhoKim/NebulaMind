GPT2_CUTOUTRUNNER_COMPLETE

# Production cutout runner completion receipt

## Result

Built `_cutout_runner_20260820/` as the IC-1..IC-7 composition layer over the already-gated production read path and the existing resampler-gate-certified adapter. No adapter or cutter was reimplemented. No network capability or selection query was added.

## Law and dependency gate

Measured before implementation and rechecked at runtime:

- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`: SHA-256 `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`, mode `444`.
- `LANA_PC1_INPUT_AMENDMENT_20260815.md`: SHA-256 `519ab5ba33c5e9d670b5654fb41f6941293c5d969c5515fb0284ebe8d52d70fb`, measured mode `644`.
- certified adapter `adapter/nm_brick_cutout_adapter.py`: SHA-256 `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`.
- gated reader `_production_readpath_20260819/production_readpath.py`: SHA-256 `105bd0c6858f27166fecee5ff7ece42c0e993eab8e3bc15b517f9bc9b5418d56`.

The runner re-verifies all four hashes and the frozen prereg mode before composition.

## Implemented contract

- Explicit positions CSV only, exact schema `ra,dec,ls_id`; no source-selection query.
- Explicit per-object brick manifest with expected brick SHA-256 and geometry row.
- IC-1 exact single 2-D `128x128` plane check, fail closed.
- IC-2 delivered nanomaggies passed unconverted to the scaling function.
- IC-3 no background estimation, subtraction, or normalization.
- IC-4 invalid fraction logged; cap is a slot; NaN/Inf replaced by `0.0` only after scaling; over-cap fails closed.
- IC-5 hash-pinned pluggable frozen Python function plus constants; no runner-chosen function or constants.
- IC-6 raw tensor is little-endian float32, C-order, shape `(1,128,128)`; the gated reader owns the FITS big-endian ingest conversion.
- IC-7 mirror is `np.fliplr(tensor[0])` after IC-1..IC-6 and nowhere in the cutter/read path.
- Canonical per-object receipts include brick SHA references, adapter geometry and WCS gate receipts, IC pass/fail flags, invalid fraction, raw output tensor SHA-256, and a receipt content SHA-256.

`_cutout_runner_20260820/ic_slots.json` is intentionally and exactly:

- `ic4_invalid_fraction_cap: null`
- `ic5_scaling_map: null`

A real-sky object is refused before any brick is opened while either slot is null. The synthetic test uses a temporary hash-pinned scaling function and temporary filled slots; it does not modify the production slot file.

## Verification results

1. Strict RED observed first: `ModuleNotFoundError: No module named 'cutout_runner'` before production implementation.
2. Runner tests: `python3 -m unittest -v test_cutout_runner.py` — **5/5 passed in 3.307s**.
   - full synthetic fixture through compressed-FITS read path, certified adapter, and IC-1..IC-7;
   - IC-1 wrong-shape fail closed;
   - IC-4/IC-5 null-slot real-sky refusal;
   - mirror bit-exactness and double-flip identity;
   - explicit positions-file schema/no-selection interface.
3. Gated read-path regression: `python3 -m unittest -v test_production_readpath.py` — **6/6 passed in 3.493s**, including the real accepted brick.
4. Certified adapter regression: `python3 -m unittest -v adapter.test_nm_brick_cutout_adapter` — **30/30 passed in 65.580s**.
5. `py_compile` and CLI `--help` smoke — PASS.
6. Null production slots exact-value check — PASS.
7. Read-only real-brick composition smoke — `PASS_NON_SCIENCE_SMOKE` on receipt-accepted brick `0001m395`; adapter output shape `128x128`, zero uncovered pixels, 16,384 contributed pixels. The staged raster was marked `NON-SCIENCE`, deleted in the same run, and confirmed absent. No IC-4/IC-5 processing and no science tensor were produced. Receipt: `_cutout_runner_20260820/NON_SCIENCE_SMOKE_RECEIPT.json`.
8. Static scan of runner Python for `requests`, `urllib`, `socket`, `portal.nersc`, HTTP URLs, and `subprocess` — zero matches.

Total exercised tests: **41/41 passed**, plus compile, CLI, null-slot, and non-science real-brick smoke checks.

## Artifact hashes

- `_cutout_runner_20260820/cutout_runner.py`: `ccb9b8fed457333669e54fa9f0a3dac645dc866a56c6cd8dc665ffd4d93b1bcc`
- `_cutout_runner_20260820/test_cutout_runner.py`: `da40f8c00e84373aff1310ce625d428787aeebb53e6f6ae7c052b2243945bd6a`
- `_cutout_runner_20260820/ic_slots.json`: `263099856f3d3523179dfdccfe40e7a0b9ddbd9b21fa31824b2eafee94588952`
- `_cutout_runner_20260820/NON_SCIENCE_SMOKE_RECEIPT.json`: `026fced16de456fdcb246f15d975bb1314a5e64d962f77dde446c5cc8464ab3c`

No network used. `portal.nersc.gov` was never contacted. No database, publication, cockpit, git commit, push, or real-sky science output action was taken.
