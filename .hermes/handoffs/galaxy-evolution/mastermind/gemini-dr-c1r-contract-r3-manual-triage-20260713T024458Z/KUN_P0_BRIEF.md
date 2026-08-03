# Kun P0 brief — input custody gate

Read `HWAO_APPROVAL_BRIEF.md`, `HWAO_PLAN.md`, and `ROLE_TABLE.md` in this packet.

Do only P0 now.

1. Verify the current contract of record is the sealed canary file `../gemini-dr-revised-canary-20260712T045317Z/prompt/C1r.md`, sha256 expected `fffac44fbf6e9abe3afb1f8f34f3a9e3e7688991f319c4927459fb29ac00e1ef`, and byte-identical to sealed `runs/c1r/prompt_submitted.md`.
2. Hash the remaining inputs named in the approval brief: repaired validator result, re-adjudication summary, Hwao final synthesis, T14 adjudication, and Lana T14 countersign.
3. Verify `validator_result_v2.json` contains exactly 73 `MANUAL_REVIEW_REQUIRED` findings and report clause:code counts.
4. Verify the prior repair packet completion marker exists and its published key output hashes match `receipts/TORI_PACKET_RECEIPT.md`.
5. Write only `receipts/KUN_INPUT_CUSTODY_RECEIPT.md`, including exact paths relative to this packet, sha256/bytes, counts, PASS or blocker, and marker `KUN_R3_TRIAGE_INPUT_CUSTODY_GREEN_20260713T024458Z`.

Boundaries: read-only source packets; packet-local receipt only; no network/browser/git/DB/dashboard/deploy/cron/account/secret action. Do not start P3 yet.
