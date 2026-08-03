# GORU BRIEF — Joint-run local preflight

Task ID: `goru-joint-preflight-20260711T100852Z`
Packet root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-joint-burn-recovery-20260711T100139Z`

## Role lock — acknowledge first

Append exactly one `GORU_ACK` row to the packet's `WAVE_LEDGER.md`, quoting this DIRECTION §2 role line verbatim:

`LOCAL-ONLY mechanical helper under goru/: topic dedupe (§7), prompt schema validation, expected-marker map, post-capture receipt/count/hash checks`

Also quote the ban verbatim:

`Chrome, System Events, Playwright, any browser automation, cookies, profiles, login, CAPTCHA/verification, Gemini Web in any form, network calls to Google`

The packet remains NOT_ARMED. This ledger ACK is the sole write outside `goru/` authorized by this brief.

## Read-only inputs

Packet:
- `DIRECTION.md`
- `MANIFEST.json`
- `prompts/C1.md`
- `WAVE_LEDGER.md`

Weekend topic prompts only, never their invalid outputs:
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-deep-research/requests/REQ_*_WEEKEND_BURN_PROMPT.md`

The 15 valid report bodies, topic/heading inspection only:
- base packet `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-rampage-20260711T052300Z/runs/`
  - wave1: R1, R2, R3
  - wave2: R4
  - wave3: R3b, R5b, R6b
  - wave4: R1b, R2b, R4b
- extension packet `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-rampage-extension-20260711T064115Z/runs/`
  - wave5: R7, R8, R9
  - wave6: R10, R12

The 93 macro output files are invalid/audit-only. Do not read them as scientific content, cite them, or treat them as completed coverage.

## Tasks

1. Write `goru/TOPIC_DEDUPE.md`.
   - Inventory every existing weekend prompt topic.
   - Compare topic text against the topic/scope of the 15 valid report bodies only.
   - One row per weekend topic: request ID, topic, `COVERED_BY_VALID_REPORT | NOT_COVERED | UNPARSEABLE`, matched valid run(s), one-sentence mechanical rationale.
   - Report exact input count and verdict counts. Do not make scientific truth judgments.

2. Write `goru/PROMPT_SCHEMA_CHECK.md`.
   - Recompute SHA-256 of `prompts/C1.md` and compare with `MANIFEST.json`.
   - Verify BEGIN/END sentinel presence and matching REQ ID.
   - Verify C1–C8 contract labels are present.
   - Verify request ID and expected marker exactly match the manifest.
   - Verify marker instruction says exactly once and final non-empty line.
   - Verify the canary is the only manifest run and packet run-count cap is 1.
   - Verdict `PASS` only if every mechanical check passes.

3. Write `goru/EXPECTED_MARKERS.json` exactly as a JSON object mapping `C1` to the manifest marker.

4. Write `goru/GORU_PREFLIGHT_RECEIPT.md` with UTC start/end, model/tool, every input root, output hashes/byte counts, verdict counts, safety attestation, and final `PASS | BLOCKED`.

5. Write zero-byte marker `goru/GORU_PREFLIGHT_DONE_20260711T100852Z` last, only on PASS. On failure write `goru/GORU_PREFLIGHT_BLOCKED_20260711T100852Z` plus reason instead.

## Hard exclusions

- No Chrome/System Events/browser/Google/Gemini Web/network calls.
- No Playwright/headless/stealth/profile/cookie/API/login/CAPTCHA/verification work.
- Do not restart or modify `ruthless_weekend_burn.py` or `capture_current.py`.
- No deleting/quarantining/moving the 93 invalid files; report only.
- No writes outside this packet's `goru/` except the one append-only GORU_ACK ledger row.
- No DB/wiki/candidates/SPRINT_STATUS/runner/runtime/git/publish/deploy/cron/cloud/billing/account/credential/extension writes.

Done response must include the standalone line:
`GORU_JOINT_PREFLIGHT_DONE_20260711T100852Z`
