# A1 metadata pins — 2026-09-07

These are actual SHA-256 observations of permitted label-free metadata and the selected rendering code. No protected image, tensor or label artifact was opened or hashed. Existing files were not changed. Old renderers and the legacy driver/builder are not imported by run_path.py.

## Files used by the selected rendering path

| File (relative to lane root) | Bytes | SHA-256 computed now | Actual read/use |
|---|---:|---|---|
| `scratch/survey-bricks-dr9-north.fits.gz` | 20882100 | `2edd5c295fdad26852c6f224a3ff023cff43dd0e03a53acd35b767e726ee72fb` | INPUT brick table: adapter verifies its bytes; eligibility/coordinate producer owns the half-open assignment. |
| `validation_bricks/_bricks_without_r_coverage.txt` | 36 | `ba2eb9d16d0d1d47eef2e0d52497b56d44ac979ebe67dd54b33f57c117d7a2fe` | INPUT no-r registry: adapter verifies its bytes; no new eligibility filtering is performed. |
| `miniprereg_pins/render_config_v2.json` | 327 | `b1c0c6d6dca9ee438a474a96b884b5164c1731c95392be04726b1e49f3d34db4` | Renderer_v4 reads and compares the full geometry JSON at import. |
| `miniprereg_pins/protected_region_v2.py` | 3258 | `4b4fb5ca17953e0933bd5c2286ca23063247a472fbe2be5f4fc6d4a57e195faf` | Render chain imports this module and calls r_t_validation (23.0) / contamination rules. |
| `study_renderer/__init__.py` | 564 | `659b763c83a948825d285e51671c28173b446f428bcd32d941811bf6cdaf5721` | Package initializer imports renderer_v4. |
| `study_renderer/render_chain_v3.py` | 4253 | `7835fda76591bfe5cd9fd4d3413654e212ed7a0f73a45da29b6cc324bbd0cf5e` | Executed cleaning, rendering, refusal and normalization chain. |
| `study_renderer/renderer_v4.py` | 13435 | `dad904ffb0dbc68fcb350be6fbee7ea57a5bf66503d61bf77a4272e0cb812b02` | Executed geometry, reprojection and integer-plane carriage. |
| `study_renderer/pixel_rejection_v2.py` | 5026 | `075d73460645ab4c8353a468c8f3a7eabed8e9339198ea26f0dd51a35db02e54` | Executed source cleaning, rejection and MEDIUM counting. |

The pure in-memory renderer receives RA, DEC and the primary brick from its caller; it does not open a coordinate catalogue or survey-bricks table itself. The new adapter reads its pinned label-free coordinate JSON and verifies the brick-table and no-r registry digests as INPUT checks. It uses the coordinate producer's assigned brick, without rebuilding the selection brick test or consulting checksum membership for eligibility. All three groups use the NO-DR10 validation protected-radius branch (23.0); no shape_r catalogue is read.

## Coordinate input that cannot yet be pinned

Required concrete proposed path: `_optionA_dev/agreement_run/inputs/render_coordinates_20260907.json`. **Not present / not produced in this bounded file whitelist; no SHA-256 is claimed.** This is a required C.inputs.coordinates file, and every stage refuses if its pin or bytes are missing or wrong.

The fixed consumer schema is a JSON array of rows containing exactly `objid` (canonical nonnegative integer), `ra`, `dec` (finite binary64-compatible values) and `brick` (DR9-north brick name). It must cover every eligible ID, with one unique row per identity. Proposed producer procedure: a permitted metadata producer projects only GZ1_OBJID/RA/DEC from the established coordinate source, never decodes or emits its label column, assigns bricks with the already established DR9-north binary64 half-open/wrap rule and no-r registry, then emits rows for all pinned eligible identities in numeric ID order. Hash the actual JSON and bind its producer/derivation receipt before C. No seed or real selection is needed.

Concrete companion producer/receipt paths for the owner's next preparation scope: `_optionA_dev/agreement_run/inputs/BUILD_RENDER_COORDINATES_20260907.py` and `_optionA_dev/agreement_run/inputs/RENDER_COORDINATES_RECEIPT_20260907.md`. They are proposed remaining filenames, not claimed existing outputs. The current task permits neither of those new files nor the coordinate JSON. The adapter therefore has a tested consumer but this INPUT remains explicitly open.

`coords.csv` and `recovered_coords.json` are not substitutes: inspection of their generator code shows DR10_BRICKID/DR10_OBJID keys, not the GZ1 identity domain. Their contents were not opened for this task and the adapter does not read them. The label-bearing guarded pool must not become the adapter's runtime coordinate source; producing a separate label-free projection keeps its labels outside pre-access INPUT checks.

## Other actual renderer reads, due only at their access stage

The adapter reads each stage's pinned inventory, its exact drawn coordinate list, each object's pinned published checksum file, its separately pinned label JSON, and the three individually pinned FITS plane files (`image-r`, `maskbits`, `nexp-r`). The WCS comes from the pinned image HDU header, with its HDU index fixed by the stage inventory. A downloaded plane must use the DR9-north coadd URL derived from the assigned brick and match the already pinned published checksum. A missing published checksum is recorded as RENDER-REFUSED; missing/mismatched supplied plane or tensor digests stop.

Those future checksum/plane/label/tensor paths are the STAGED ACCESS inventory, not pre-seed coordinate INPUT omissions. They are not opened or hashed now. The procedure fixes their schema and individual-pin requirement; actual names follow the draw and authorized staging. The full output name rules are in the run-path report.

Python, NumPy, Astropy, py_ecc, package initializers, bytecode, native libraries and package resources are listed separately in `RUNTIME_EVIDENCE_20260907.md`. That file explicitly names the system-library pinning limit; the geometry/code table here does not claim to cover it.

## Reproduction command and observed hashes

Run from the lane root. This hashes only the named permitted metadata/code/environment files.

```sh
PYTHONDONTWRITEBYTECODE=1 /Library/Developer/CommandLineTools/usr/bin/python3 -c 'from pathlib import Path
import hashlib,json
names=[
"scratch/survey-bricks-dr9-north.fits.gz",
"validation_bricks/_bricks_without_r_coverage.txt",
"miniprereg_pins/render_config_v2.json",
"miniprereg_pins/protected_region_v2.py",
"study_renderer/__init__.py",
"study_renderer/render_chain_v3.py",
"study_renderer/renderer_v4.py",
"study_renderer/pixel_rejection_v2.py",
"_optionA_dev/agreement_run/select_sample.py",
"_optionA_dev/fourier_chirality/fourier_chirality.py",
"_optionA_dev/drand_only/verify_drand_v2.py",
"miniprereg_pins/validation_gate.py",
"_optionA_dev/fourier_chirality/env_lock.json",
]
for name in names:
 p=Path(name)
 print(json.dumps({"path":name,"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"bytes":p.stat().st_size}))
'
```

```text
{"path": "scratch/survey-bricks-dr9-north.fits.gz", "sha256": "2edd5c295fdad26852c6f224a3ff023cff43dd0e03a53acd35b767e726ee72fb", "bytes": 20882100}
{"path": "validation_bricks/_bricks_without_r_coverage.txt", "sha256": "ba2eb9d16d0d1d47eef2e0d52497b56d44ac979ebe67dd54b33f57c117d7a2fe", "bytes": 36}
{"path": "miniprereg_pins/render_config_v2.json", "sha256": "b1c0c6d6dca9ee438a474a96b884b5164c1731c95392be04726b1e49f3d34db4", "bytes": 327}
{"path": "miniprereg_pins/protected_region_v2.py", "sha256": "4b4fb5ca17953e0933bd5c2286ca23063247a472fbe2be5f4fc6d4a57e195faf", "bytes": 3258}
{"path": "study_renderer/__init__.py", "sha256": "659b763c83a948825d285e51671c28173b446f428bcd32d941811bf6cdaf5721", "bytes": 564}
{"path": "study_renderer/render_chain_v3.py", "sha256": "7835fda76591bfe5cd9fd4d3413654e212ed7a0f73a45da29b6cc324bbd0cf5e", "bytes": 4253}
{"path": "study_renderer/renderer_v4.py", "sha256": "dad904ffb0dbc68fcb350be6fbee7ea57a5bf66503d61bf77a4272e0cb812b02", "bytes": 13435}
{"path": "study_renderer/pixel_rejection_v2.py", "sha256": "075d73460645ab4c8353a468c8f3a7eabed8e9339198ea26f0dd51a35db02e54", "bytes": 5026}
{"path": "_optionA_dev/agreement_run/select_sample.py", "sha256": "8e517aab2715e6ec814a37f0dfb517b186f2f0ed7b64f045ae6a2a34120144b5", "bytes": 4325}
{"path": "_optionA_dev/fourier_chirality/fourier_chirality.py", "sha256": "a026fe5fa168ca1eb2056829d86fb549dec4a61596b5d122f60c2a389e2d98a2", "bytes": 6068}
{"path": "_optionA_dev/drand_only/verify_drand_v2.py", "sha256": "e982d9441f5c8d8b9d4cdf43b4bd44a03c5de42d4246c5bdc5531f4ba5d5ed7b", "bytes": 4948}
{"path": "miniprereg_pins/validation_gate.py", "sha256": "65e241cad76b6150f625ac5aad085ed528004153d8590f8c32b07895c0c75e5b", "bytes": 3827}
{"path": "_optionA_dev/fourier_chirality/env_lock.json", "sha256": "4e2c851fe1f22f4bc28f121cf3ff4326f036be57fc100b34af9e5501d6c74251", "bytes": 898}
EXIT_CODE=0
```
