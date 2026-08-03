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
