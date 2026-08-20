GPT2_INFERENCE_BUILD_COMPLETE — synthetic identity test: 1000/1000 bit-exact PASS

Boundary held

- Synthetic validation only.
- No tensor under `/Users/duhokim/NebulaMindData/cutouts_dr10_south/tensors/` was opened, read, hashed, or passed through the model.
- No authorization artifact exists in this build.
- Non-synthetic execution without `--authorization FILE` exits nonzero; verified exit 2 with `REFUSED_REAL_DATA_UNAUTHORIZED` before input access.
- Paths under the real tensor root are treated as real even when `--synthetic` is supplied, including symlink aliases.

Build

- Runner: `_inference_20260820/inference_runner.py`
- Frozen weights SHA-256 verified before load: `83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d`
- Runner code SHA-256: `16ed3e256ea4fe045ff553036e7f397e7ad07884212d5da663e61f2246c57b45`
- IC-6 reader: exact 65,536-byte little-endian float32 C-order `(1,128,128)` contract.
- Primary chi: one shared CE-ResNet trunk evaluated on `x` and width-axis `torch.flip(x, dims=[3])`, then `(f(x)-f(mirror(x)))/2`.
- Runtime: CPU float32, eval mode, one intra-op thread, one inter-op thread, deterministic algorithms enabled.
- HC-1H committee runs alongside and appears only as stratification metadata.
- Per-object JSON receipts and append-only/resumable JSONL ledger implemented.

Synthetic validation

- Frozen BS-3 generator probes: 1,000.
- Mirror involution: 1,000/1,000 byte-exact PASS.
- Antisymmetry: 1,000/1,000 float32 bit-exact PASS.
- Same-process repeat determinism: 1,000/1,000 PASS.
- Multiprocessing determinism: 4/4 spawned workers identical PASS.
- End-to-end receipts: 1,000.
- Append-only ledger rows: 1,000.
- Resume: 0 processed, 1,000 resumed, no ledger append.
- Committee states: 921 AGREE_CONFIDENT, 38 DISAGREE, 41 LOW_CONFIDENCE.
- Validation receipt: `_inference_20260820/SYNTHETIC_VALIDATION_RECEIPT_20260820.json`
- Validation receipt SHA-256: `b326b154ba9d9a16cdb8a7521ca3c0d42f0d7899b4bf3fe64b4770762762da66`
- Results ledger SHA-256: `c6477cddb127ebb7e5fa2acb0e13e17b02240f4c587dba842fe916f09d79e0b5`

Tests

- 11/11 unit/contract tests PASS.
- Python bytecode compilation PASS for runner, validation, and tests.
