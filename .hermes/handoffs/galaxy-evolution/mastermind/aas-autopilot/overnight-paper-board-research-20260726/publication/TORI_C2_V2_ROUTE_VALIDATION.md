# Tori Validation — C2 V2 Audit and New-Run Route Map

Marker: `OVERNIGHT_PAPER_BOARD_TORI_C2_V2_ROUTE_VALIDATION_V1`

Status: `V2_AUDIT_PASS__GORU_NEW_RUN_MAP_FAIL_INVALID_ROUTE_ID`

## V2 candidate

- Kun independent V2 contract audit: PASS on all nine items; no discrepancies.
- V2 remains frozen at:
  - `candidate.tex`: `bb77d38d294792f44b05a2011774c6bbb3dbcf0dfc24adf3cb0c5bd5d52e7ee6`
  - `candidate.pdf`: `ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d`
  - `result.png`: `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639`
- Source baseline verification remains 38/38 PASS.

## Goru new-run mapping failure

The proposed run id `gated-e2e-demo-c2-v2` is not routable under the current backend source.

Grounding:

- `backend/app/routers/lab_runner.py:181-187` rejects `GET /api/lab/runs/{rid}` unless `rid.isalnum()` and length is at most 32.
- `backend/app/routers/lab_runner.py:194-200` rejects artifact requests unless `rid.isalnum()`.
- `gated-e2e-demo-c2-v2` contains hyphens, so `rid.isalnum()` is false. The proposed PDF route would return `400 bad request` under this code.
- The create API generates 12-character hexadecimal/alphanumeric ids at `backend/app/routers/lab_runner.py:132-145`.

Therefore:

- Preserve `publication/goru-v2-new-run-map/NEW_RUN_TARGET_MAP.md` and its receipt as a failed first mapping.
- Do not use its `DONE` status as publish evidence.
- Corrected mapping requires a legal alphanumeric id.

## Corrected legal-id candidate

`c2v2e2e0726a`

Mechanical check performed locally:

- length: 12
- `isalnum()`: true
- `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a.json`: ABSENT
- `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/`: ABSENT

## Manifest requirements grounded in backend source

For list visibility, `list_runs` requires:

- top-level `status: "done"`
- `result.summary` non-empty

For list fields and reader links, include:

- top-level `id`, `created_utc`
- `spec.method`, `spec.data_sources`
- `result.figure_url`, `result.pdf_url`
- optional `result.review_url`, `result.review_verdict`, `result.review_cycles` only if backed by real artifacts/evidence
- explicit label/provenance fields and a summary that visibly states AI draft, forced-demo lineage, TENSION, and unresolved calibration

No live/source/public byte was changed. Public status remains `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.
