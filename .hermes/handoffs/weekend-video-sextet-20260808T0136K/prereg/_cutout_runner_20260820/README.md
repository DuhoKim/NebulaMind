# Production cutout runner (composition layer)

Scope: local/offline composition only. This directory contains no acquisition or selection query. It accepts an explicit `ra,dec,ls_id` CSV and an explicit receipt-pinned brick manifest, then composes the gated production reader with the resampler-gate-certified adapter and IC-1..IC-7.

Hard gates:

- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` SHA-256 `b06901c8...`, mode `444`.
- `LANA_PC1_INPUT_AMENDMENT_20260815.md` SHA-256 `519ab5ba...`.
- gated adapter SHA-256 `267b2a93...`; never copied or reimplemented.
- gated read path SHA-256 `105bd0c6...`.
- `_cutout_runner_20260820/ic_slots.json` was filled by the synthetic-only R1–R5 rerun and is pinned at SHA-256 `10d24a6e...`: IC-4 cap `0.0`; IC-5 fixed monotone identity map `tensor=float32(nanomaggy)`, gain `1.0`, offset `0.0`. See `_icrerun_20260820/ICRERUN_RECEIPT_20260820.md`. The runner still refuses any alternate slot file while either slot is null.

Inputs:

1. Positions CSV with the exact header `ra,dec,ls_id`. No selection query is present.
2. Brick manifest JSON:

```json
{
  "schema_version": 1,
  "objects": {
    "an-ls-id": [
      {
        "brickname": "0001m395",
        "path": "/absolute/receipt-accepted/brick.fits.fz",
        "sha256": "<accepted brick sha256>",
        "row": {"ra": 0.161579892280072, "dec": -39.5}
      }
    ]
  }
}
```

The manifest keys must exactly equal the explicit position `ls_id` values. Brick selection/provisioning is deliberately outside this runner.

The filled IC-5 value identifies a hash-pinned Python module with a callable `scale(values, constants)`:

```json
{
  "ic4_invalid_fraction_cap": 0.01,
  "ic5_scaling_map": {
    "module_path": "/absolute/path/to/frozen_scaler.py",
    "module_sha256": "<sha256>",
    "callable": "scale",
    "constants": {}
  }
}
```

The runner does not choose these values. The synthetic rerun filled them through this pluggable frozen-function boundary; changing either value requires a new gated synthetic rerun and hash pin.

Run:

```sh
python3 cutout_runner.py \
  --positions /absolute/positions.csv \
  --brick-manifest /absolute/brick-manifest.json \
  --slots /absolute/pinned-slots.json \
  --output-dir /absolute/private-output
```

Use `--mirror` to apply `np.fliplr(tensor[0])` after IC-1..IC-6. `--synthetic` is only for explicitly synthetic fixtures and does not bypass the need for filled test slots.

Outputs are private per-object raw little-endian float32 C-order tensors (`.f32le`, shape `(1,128,128)`) and canonical JSON receipts. Receipts contain brick SHA references, adapter geometry custody, IC pass/fail flags, invalid fraction, and tensor SHA-256.

Tests:

```sh
python3 -m unittest -v test_cutout_runner.py
```

Read-only real-brick smoke (no IC/science tensor):

```sh
python3 smoke_real_readpath_composition.py
```

The smoke stages one raster only inside a `NON_SCIENCE_SMOKE_*` temporary directory, deletes it in the same run, and persists only `NON_SCIENCE_SMOKE_RECEIPT.json` recording deletion. It does not fill or bypass the null production slots.
