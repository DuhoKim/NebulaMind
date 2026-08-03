# Hwao Deepening Gate 4 Request

Marker: `OVERNIGHT_PAPER_BOARD_HWAO_GATE4_REQUEST_V1`

Do not write memory or configuration.

Read:
- `reviews/kun/KUN_C2_V2_AUDIT_RECEIPT.md`
- `packets/C-candidate-build/kun-c2-v2-audit/C2_V2_CONTRACT_AUDIT.md`
- `publication/GORU_C2_V2_NEW_RUN_MAPPING_RECEIPT.md`
- `publication/goru-v2-new-run-map/NEW_RUN_TARGET_MAP.md`
- `publication/TORI_C2_V2_ROUTE_VALIDATION.md`
- `backend/app/routers/lab_runner.py`

Under the approved output root only, write:

1. `reviews/hwao/HWAO_C2_V2_FINAL_ACCEPTANCE.md`
   - Accept V2 candidate mechanics based on Kun's independent nine-item PASS.
   - Keep publication blocked because the Goru new-run mapping used an invalid hyphenated id and failed route validation.

2. `publication/GORU_C2_V2_NEW_RUN_MAPPING_REPAIR_BRIEF.md`
   - Preserve the failed first Goru map and receipt unchanged.
   - Lane: Antigravity/Gemini subscription only.
   - Correct legal run id: `c2v2e2e0726a` (12 characters, alphanumeric, currently absent).
   - Re-run read-only create-path mapping grounded in `lab_runner.py` route validators and list visibility requirements.
   - Verify exact ABSENT paths for `c2v2e2e0726a.json` and `c2v2e2e0726a/`.
   - Verify route `/api/lab/runs/c2v2e2e0726a/artifact/draft.pdf` is source-code-valid.
   - Record precise manifest requirements: top-level `id`, `status`, `created_utc`, `spec`; non-empty `result.summary`; `result.figure_url` and `result.pdf_url`; omit optional review fields unless backed by actual review artifacts.
   - Require visible AI-draft, forced-demo, TENSION, and unresolved-calibration labels.
   - Write only a versioned deliverable under `publication/goru-v2-new-run-map-v2/` and a versioned receipt `publication/GORU_C2_V2_NEW_RUN_MAPPING_RECEIPT_V2.md`.
   - No live HTTP, browser, public/current-Lab/source writes.

3. `reviews/hwao/HWAO_DEEPENING_GATE4_DISPATCH_RECEIPT.md`

Return exact marker: `HWAO_C2_V2_ROUTE_REPAIR_BRIEF_READY`.

Public status remains `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.
