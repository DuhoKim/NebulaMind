# GORU C2 V2 NEW RUN MAPPING RECEIPT V2

## Deliverable SHA-256
* `publication/goru-v2-new-run-map-v2/NEW_RUN_TARGET_MAP_V2.md`: `748d9e717420e46047fae743e74cffbbf4212385f203a027d9ebb7604d61811f`

## Legal-ID / Route-Validity Confirmation
The corrected ID `c2v2e2e0726a` is 12 characters and purely alphanumeric. This satisfies the `rid.isalnum()` checks in both `get_run` and `get_artifact` within `backend/app/routers/lab_runner.py`. The route `/api/lab/runs/c2v2e2e0726a/artifact/draft.pdf` is fully valid and will not result in a 400 Bad Request (unlike the previous hyphenated ID).

## ABSENT / Create Target Paths
The following paths have been verified as ABSENT (safe for create-only promotion):
- `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a.json`
- `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/draft.pdf`
- `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/draft.tex`
- `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/result.png`

## Manifest Requirements
To be dynamically served via `list_runs`, `c2v2e2e0726a.json` must include:
- `id`, `status: "done"`, `created_utc`, `spec` (`method`, `data_sources`).
- `result.summary` (must be non-empty).
- `result.figure_url` = `/api/lab/runs/c2v2e2e0726a/artifact/result.png`
- `result.pdf_url` = `/api/lab/runs/c2v2e2e0726a/artifact/draft.pdf`
- Omit review fields and `lit_grounded` logic unless real artifacts back them up.

## Visible-Label Requirement
The four labels (`AI-draft`, `forced-demo`, `TENSION`, `unresolved-calibration`) must be surfaced within the `result.summary` text string to survive into the served representation.

## Create-only Backup / Rollback & Verification Plans
* **Backup**: None required.
* **Rollback Plan**: `rm -rf .hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a` and `rm -f .hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a.json`.
* **Verification Plan**: SHA check the copied PDF, perform an HTTP `curl -I` on the `/api/lab/runs/c2v2e2e0726a/artifact/draft.pdf` endpoint (asserting a 200 OK, not a 400), and check the visible labels on the UI and PDF.

## Blockers
None.

## Attestation
**ATTESTATION:** first map preserved unchanged / no `lab-runs` create / no public write / no browser / no live-HTTP / no candidate copy.

## Completion State
DONE (Public status remains `AWAITING_EXPLICIT_PUBLISH_APPROVAL`)

OVERNIGHT_PAPER_BOARD_PUBLICATION_GORU_C2_V2_NEW_RUN_MAP_V2_COMPLETE_V1
