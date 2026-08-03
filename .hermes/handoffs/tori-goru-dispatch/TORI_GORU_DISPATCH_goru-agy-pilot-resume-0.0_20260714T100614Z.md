# Tori -> Goru dispatch

Target: goru-agy-pilot-resume:0.0
Timestamp: 20260714T100614Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260714T100614Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

# GORU correction — final verification script requirements

The proposed read-only command was denied because it was incomplete and would mis-check the schema.

Corrections:

- Hash all four files: result, metadata, identity, and deletion evidence.
- Pass `Path("ledger/RUN_LEDGER.jsonl")` to `ledger.verify` and `ledger.read_entries`, not a string.
- Deletion evidence uses `captured_title`, not `conversation_title`.
- Title agreement is:
  - `identity.conversation_title == deletion.captured_title`; and
  - `identity.prompt == deletion.deletion_match_title`.
- Verify identity `conversation_id` and `submit_utc` exactly match deletion evidence.
- Do not print full ledger entries; print only epoch/type/hash/order booleans.
- The result quality miss remains expected and is not a custody failure.

Run one corrected read-only command only. No browser, lease, or file writes.

GORU_DR_FINAL_VERIFY_CORRECTION_20260714

Done marker: TORI_GORU_DISPATCH_DONE_20260714T100614Z

```
