# GORU C2 V2 NEW RUN MAPPING RECEIPT

## Deliverable SHA-256
* `publication/goru-v2-new-run-map/NEW_RUN_TARGET_MAP.md`: `bfc81c45987e96f52586d5dd120dd60f3e208e80b2aeedc0ac7fea1a31db0088`

## ABSENT / Create Target Paths
The following paths for the `gated-e2e-demo-c2-v2` run are verified as strictly ABSENT (create-only pathway):
- `.hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo-c2-v2.json`
- `.hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo-c2-v2/draft.pdf`
- `.hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo-c2-v2/draft.tex`
- `.hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo-c2-v2/result.png`

## Route Coupling
A new run is served automatically by the backend globally aggregating `*.json` inside the `lab-runs` directory. By creating `<id>.json` and the corresponding `lab-runs/<id>/` artifacts directory, it becomes discoverable by the API route `/api/lab/runs/gated-e2e-demo-c2-v2/artifact/<name>`. NO existing run or JSON manifest is edited.

## V2 Candidate Hashes (Source)
- `candidate.pdf`: `ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d`
- `candidate.tex`: `bb77d38d294792f44b05a2011774c6bbb3dbcf0dfc24adf3cb0c5bd5d52e7ee6`
- `result.png`: `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639`

## Preview / Manifest Field Requirements
The new `gated-e2e-demo-c2-v2.json` file must contain `id`, `status: done`, `created_utc`, and a `result` block with `pdf_url` set to `/api/lab/runs/gated-e2e-demo-c2-v2/artifact/draft.pdf`. Critically, the `result.summary` must surface the required visible labels: `AI-draft`, `forced-demo`, `TENSION`, `unresolved-calibration`.

## Create-only Backup & Rollback Plan
- **Backup**: None required (no files are overwritten).
- **Rollback**: Delete the newly created `.hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo-c2-v2` directory and the `gated-e2e-demo-c2-v2.json` file. The baseline `gated-e2e-demo` run is never touched.

## Verification Plan (Future)
- **SHA**: Verify the created `draft.pdf` matches `ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d`.
- **HTTP**: `curl -I /api/lab/runs/gated-e2e-demo-c2-v2/artifact/draft.pdf` must return `200 OK` and a valid `Content-Length`.
- **Labels**: Verify the labels exist in the served JSON summary and the text of the PDF.

## Blockers
None.

## Attestation
**ATTESTATION:** No public write / no browser / no live-HTTP / no candidate copy / no baseline-run edit.

## Completion State
DONE (Public status remains `AWAITING_EXPLICIT_PUBLISH_APPROVAL`)

OVERNIGHT_PAPER_BOARD_PUBLICATION_GORU_C2_V2_NEW_RUN_MAP_COMPLETE_V1
