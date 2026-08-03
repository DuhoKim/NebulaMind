# Kun dual P0 brief

Read the coordination `HWAO_APPROVAL_RELAY.md`, `HWAO_PARALLEL_PLAN.md`, and `ROLE_TABLE.md`, plus both gate `APPROVAL_AND_BOUNDARIES.md` files.

Before either gate starts, write:

- Gate A `receipts/KUN_INPUT_CUSTODY_RECEIPT.md`
- Gate B `receipts/KUN_INPUT_CUSTODY_RECEIPT.md`

Gate A pin at minimum:

- sealed prompt and submitted prompt;
- sealed captured body and relevant spec;
- repair `structured_capture_v2.json`, `validator_result_v2.json`, validator/capture code, tests, fixtures, and repair completion/packet receipts;
- r3 `CONTRACT_R3_DRAFT.md`, `HWAO_R3_REVIEW.md`, `HWAO_FINAL_RECOMMENDATION.md`, and completion marker.

Gate B pin at minimum:

- r3 `TRIAGE_LEDGER.json` and Markdown, final recommendation, and completion marker;
- repair `structured_capture_v2.json`, `validator_result_v2.json`, captured body, chip index/ledger mapping, and repair completion/packet receipts;
- sealed prompt/body hashes.

Each receipt records path, bytes, sha256, boolean existence, and a GREEN/STOP decision. Verify the three prior packets have completion markers and no immutable input mismatch. Never print secrets. No network. Write only the two receipts.

KUN_DUAL_P0_BRIEF_20260713T034742Z
