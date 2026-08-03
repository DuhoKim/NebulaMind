# Hwao brief — prepare P1/P3 read-only/local preflight packet

Marker: `HWAO_P1_P3_READONLY_PREFLIGHT_REQUEST_20260706T0750Z`

User request: "ask Hwao to prepare a read-only/local preflight packet from these exact P1/P3 choices."

Lane: Hwao/Fable. Tori is relay/verify only.

## Hard boundary

This is a local read-only preflight packet, not execution.

Required invariants:

- Active execution phrase: `NO ACTIVE EXECUTION PHRASE`
- DB writes: `0`
- SQL/apply/rollback execution: `0`
- Trust recompute: `0`
- Prose/wiki/page_versions publish: `0`
- Backend/API restart: `0`
- Frontend restart: `0`
- Deploy/git/cloud/API mutation: `0`
- No apply SQL file.
- No `sql/` directory.
- Do not mint or quote any exact execute/apply approval phrase.
- Do not touch product source code.
- Do not run live DB/API/network checks unless you explicitly mark them as blocked and ask first; use the existing local docs/snapshots already present.

## Exact user choices to encode

1. **P1 / 2298:** Recast 2298 to scoped wording, or retire into 2946.
2. **P1 / 2299:** Recast 2299 to scoped wording, or re-parent into 2945.
3. **P1 / 2924:** Finish display cleanup: if `parent_replaced`, hide legacy display and label as replaced.
4. **P3 / 2572:** Use cautious guard wording.
5. **Trust timing:** Stage trust recompute as a separate packet after P4 guard.

## Source files to read, local only

- `docs/hwao_morning_blocker_specs_20260706T0308Z/P1_LEGACY_OVERCLAIMS_2298_2299_2924_SPEC.md`
- `docs/hwao_morning_blocker_specs_20260706T0308Z/P3_2572_PRIMACY_RECAST_SPEC.md`
- `docs/hwao_morning_blocker_specs_20260706T0308Z/P4_LEVEL_SCORE_GUARD_RECOMPUTE_SPEC.md`
- `.hermes/handoffs/autonomy_continue_20260706T002104Z/USER_P1_P3_WORDING_DECISIONS_RECEIVED_20260706T074535Z.md`
- Optional context only: `frontend/public/agent-reports/p1-p3-wording-decisions.html`

## Packet directory to create

Create a new local packet directory:

`docs/hwao_p1_p3_readonly_preflight_20260706T0750Z/`

Required files:

1. `P1_P3_READONLY_PREFLIGHT_PACKET.md`
   - status: `READONLY_LOCAL_PREFLIGHT_NOT_EXECUTABLE`
   - marker: `HWAO_P1_P3_READONLY_PREFLIGHT_PACKET_20260706T0750Z`
   - exact user choices section
   - target claims: 2298, 2299, 2924, 2572; context successors 2945, 2946, 2573; P4 guard context
   - proposed non-executable route for each claim
   - draft wording to carry forward for 2298, 2299, 2572 exactly from source specs
   - explicit excluded actions
   - future packet requirements if user later asks for an exact write packet
   - clear stop condition: no active execution phrase, no SQL/apply, no writes
2. `decision_matrix.csv`
   - rows for 2298, 2299, 2924, 2572, trust_timing
   - columns: item_id, user_choice, hwao_route, proposed_future_packet_class, dependencies, excluded_now, notes
3. `proposed_diff_outline_NOT_EXECUTABLE.json`
   - machine-readable outline only
   - include `active_execution_phrase: null`, `sql_apply_authored: false`, `db_writes_executed: 0`, `trust_recompute_executed: 0`, `prose_publish_executed: 0`
   - no SQL strings
4. `validation/readonly_no_write_verification.json`
   - static validation booleans: no SQL dir/file, no execute/apply phrase, active phrase null, DB writes 0, source docs read-only
5. `artifacts/manifest.json`
   - list files with sha256, status, marker
6. Handoff report:
   `.hermes/handoffs/autonomy_continue_20260706T002104Z/HWAO_P1_P3_READONLY_PREFLIGHT_REPORT_20260706T0750Z.md`
   - include paths, marker, summary, and safety ledger

## Recommended packet logic

- P1 / 2298: carry forward scoped wording from the P1 spec; classify future work as either in-place recast or retirement into 2946, with exact write packet still needed later.
- P1 / 2299: carry forward scoped wording from the P1 spec; classify future work as either in-place recast or re-parent into 2945, with exact write packet still needed later.
- P1 / 2924: carry forward display cleanup: verify/handle `parent_replaced`; hide/suppress legacy display or label endpoint-visible audit behavior as replaced; exact UI/API contract check still needed later.
- P3 / 2572: carry forward cautious guard wording from the P3 spec; keep 2573 separate; exact write packet still needed later.
- Trust timing: do not recompute now; trust recompute belongs in a separate later packet after P4 guard decisions.

## Report requirement

End the report and main packet with standalone marker:

`HWAO_P1_P3_READONLY_PREFLIGHT_PACKET_20260706T0750Z`

Do not update the public cockpit. Tori will verify files and update public surfaces after your report.
