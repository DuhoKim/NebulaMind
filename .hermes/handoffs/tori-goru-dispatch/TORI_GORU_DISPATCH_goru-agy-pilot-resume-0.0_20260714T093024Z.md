# Tori -> Goru dispatch

Target: goru-agy-pilot-resume:0.0
Timestamp: 20260714T093024Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260714T093024Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

# GORU DR PROCEDURE ADDENDUM — save, verify, then delete only this run's conversation

Authority: updated `receipts/DUHO_GATE_PRO_CDP_CHROME.md`
Updated gate SHA-256: `c78b8dc7940673d0b399584b11c59233010ce24a93fa0fc719c21088cdca3155`

This binds the one bounded live DR run after Duho confirms sign-in.

Required custody sequence:

1. During submit/run initiation, capture the exact conversation ID, exact title, and submit UTC timestamp for the conversation created by this run.
2. When the DR run completes, save the complete result/artifact to the run receipt.
3. Compute and record the result/receipt SHA-256, append the result-save entry to the ledger, and verify the full ledger chain is `VERIFY_OK`.
4. Only after step 3 passes, delete exactly the conversation identified in step 1.
5. Append a deletion ledger entry containing that exact conversation ID/title and the verified result-save receipt/hash it followed.
6. Verify no unrelated conversation or account area was touched, then stop and report to Tori/Hwao.

Binding guards:

- Never clear all history and never use a bulk-delete control.
- Never delete any pre-existing, unrelated, ambiguous, or merely similar-titled conversation.
- Never touch account settings, passwords, saved account data, or any object outside the run-owned conversation.
- If the conversation identity is incomplete or not positively matched across ID, title, and submit timestamp, do not delete; leave it and report.
- If result capture, receipt hashing, ledger append, or ledger verification fails, do not delete.
- Any deletion write requires a live, exact target lease with per-action broker check; lease loss or target mismatch means stop without deleting.

No history action is authorized before a live DR result has been saved and verified. Continue holding for Duho's explicit signed-in confirmation.

GORU_DR_SAVE_THEN_DELETE_OWN_ADDENDUM_20260714

Done marker: TORI_GORU_DISPATCH_DONE_20260714T093024Z

```
