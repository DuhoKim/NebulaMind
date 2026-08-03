# Hwao Publication Preflight Gate 5 Request

Marker: `OVERNIGHT_PAPER_BOARD_HWAO_GATE5_PUBLISH_PACKET_REQUEST_V1`

Do not write memory or configuration. Do not publish. Do not write any `lab-runs` or public/current-Lab byte.

Read:
- `reviews/hwao/HWAO_C2_V2_FINAL_ACCEPTANCE.md`
- `publication/GORU_C2_V2_NEW_RUN_MAPPING_RECEIPT_V2.md`
- `publication/goru-v2-new-run-map-v2/NEW_RUN_TARGET_MAP_V2.md`
- `publication/TORI_NEW_RUN_MAP_V2_VALIDATION.md`
- `backend/app/routers/lab_runner.py`
- frozen V2 candidate and its receipt

Prepare the exact candidate-specific packet `NM-C2V2-20260727-A` under:

`publication/publish-packet-NM-C2V2-20260727-A/`

Write only these packet artifacts:

1. `PREVIEW_MANIFEST.json`
   - Exact new run id: `c2v2e2e0726a`.
   - Top-level: `id`, `spec`, `status: "done"`, `created_utc` (use a real tool-derived UTC timestamp), `log`, `artifacts`, `result`, and a machine-readable `provenance` block.
   - `spec`: original topic, `topic_source: "overnight-paper-board-c2-v2"`, data sources `tng` and `sdss`, method `mass-metallicity`, output `aastex-draft`, and `force: true`.
   - `result.summary` must explicitly and visibly include the exact labels `AI-draft`, `forced-demo`, `TENSION`, and `unresolved-calibration`, and say not submitted/not peer-reviewed, no fresh data run, and not a physical interpretation.
   - `result.figure_url` and `result.pdf_url` must use the legal id.
   - Omit review fields because no review artifact will be copied into the served run.
   - Do not fabricate literature retrieval. The provenance block may reference source run `gated-e2e-demo`, forced lineage, no fresh data run, retained TENSION, and unresolved calibration.

2. `PUBLISH_PACKET.md`
   - Status `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.
   - Candidate V2 hashes and the exact four ABSENT/create paths.
   - State: create-only additive public/current-Lab/source mutation; no baseline overwrite; no deploy/restart required by current dynamic serving code.
   - Exact approval phrase: `APPROVE PUBLISH NM-C2V2-20260727-A`.
   - The user's earlier broad approval authorized preparing this packet, not executing its unseen exact diff.

3. `EXACT_DIFF.md`
   - Four creates only:
     - `lab-runs/c2v2e2e0726a.json` from `PREVIEW_MANIFEST.json`
     - `lab-runs/c2v2e2e0726a/draft.pdf` from frozen V2 `candidate.pdf`
     - `lab-runs/c2v2e2e0726a/draft.tex` from frozen V2 `candidate.tex`
     - `lab-runs/c2v2e2e0726a/result.png` from frozen V2 `result.png`
   - No replace, update, delete, or baseline mutation.
   - Show exact before state `ABSENT` and after hashes/bytes.

4. `BACKUP_ROLLBACK.md`
   - Backup: none, because all exact targets must be ABSENT immediately before execution; any occupied target aborts.
   - Ordering: create artifact directory and three artifacts first, verify hashes, create manifest last so discovery never exposes a partial run.
   - Rollback order: remove manifest first, then remove only the three exact files and the exact now-empty directory. Include guard conditions; never use an unguarded broad deletion.

5. `VERIFY_PLAN.md`
   - Pre-write: recheck legal id, source/V1/V2 hashes, target absence, manifest schema/labels/routes.
   - Post-write local SHA/byte checks for all four creates.
   - GET/list checks: new record appears, legal `get_run`, artifact PDF/figure endpoints return 200, expected bytes/hash, and no 400.
   - Visible-label checks in `result.summary` and PDF text.
   - Baseline `gated-e2e-demo` hashes unchanged.
   - Any failure: stop, unpublish by manifest-first rollback, verify absence.

6. `PUBLISH_COMMANDS.md`
   - Exact, guarded command sequence as a plan only; DO NOT execute it.
   - All paths absolute or rooted explicitly at the NebulaMind repo.
   - Manifest copied last.
   - Post-write verification commands and guarded rollback commands.

7. `MANIFEST_VALIDATION.md`
   - Run local read-only validation of the preview manifest: valid JSON; id alphanumeric/length; status/result.summary visibility gate; required four labels; URLs match id; optional review fields absent; all target paths absent; candidate hashes match; source baseline unchanged.
   - Cite route validators accurately: `get_run` checks alphanumeric + max length; `get_artifact` checks alphanumeric + safe artifact name (no extra length claim).

8. `HWAO_PUBLISH_PREFLIGHT_RECEIPT.md`
   - Hash every packet file, summarize scope/risk/rollback/verification, confirm no publication/current-Lab/source/public write occurred, state status and exact approval phrase.
   - Completion marker: `OVERNIGHT_PAPER_BOARD_HWAO_PUBLISH_PACKET_READY_V1`.

Public status stays `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.

Return exact marker: `HWAO_PUBLISH_PACKET_NM_C2V2_20260727_A_READY`.
