# GORU PUBLIC TARGET MAPPING RECEIPT

## Deliverable SHA-256
* `publication/goru-target-mapping/PUBLIC_TARGET_MAP.md`: `b8dc09a7075483833c8ca1e4df76567de9bfd652da426b35db69fc96f4d6be0e`

## Served Target & Coupling
The published items are served dynamically by the backend (`backend/app/routers/lab_runner.py`) from the `lab-runs` directory. The coupling mechanism relies on the presence of a valid `.json` manifest (e.g., `gated-e2e-demo.json`) inside the directory, which maps the API paths (`/api/lab/runs/<id>/artifact/<filename>`) to the underlying artifacts. 

## Current Bytes & Hashes
The target paths are **OCCUPIED**. The C2 promotion will replace the following existing artifacts in `lab-runs/gated-e2e-demo/`:
- `draft.pdf`: 76,488 bytes (SHA-256: `0d863bff4d4d260fe32e56617ca6f920f2943574aaff2a5faeee3f7460575933`)
- `draft.tex`: 3,836 bytes (SHA-256: `f1aeadd8ea43f2fd1e22e9686d23066fdf95e3d5c95937a42d8ddd076bc95a8a`)

## Backup & Rollback Requirements
* **Backup**: The existing `draft.pdf`, `draft.tex`, and `gated-e2e-demo.json` must be backed up from `.hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo/` before replacement.
* **Rollback**: Simply `cp` the backed-up files back over the modified artifacts and JSON manifest.
* **Labels**: The `AI-draft`, `forced-demo`, `TENSION`, and `unresolved-calibration` labels must survive into the updated served manifest.

## Blockers
None encountered. The mapping was successfully resolved via static read-only inspection.

## Attestation
**ATTESTATION:** No public write was performed. No browser or live-HTTP requests were made. No candidate copy occurred into any public, repo, or served location.

## Completion State
DONE (Public status remains `AWAITING_EXPLICIT_PUBLISH_APPROVAL`)

OVERNIGHT_PAPER_BOARD_PUBLICATION_GORU_TARGET_MAP_COMPLETE_V1
