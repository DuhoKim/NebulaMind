# GORU — verify completed one-run custody and exact-own deletion

Read-only verification only. Do not touch the browser or acquire any lease.

Expected completed run:

- Conversation ID: `8af765be7d623416`
- Submit UTC: `2026-07-14T09:45:28.451996Z`
- Result receipt: `receipts/GORU_DR_RESULT.md`
- Result receipt SHA-256: `84f3ebfee6ddc51fbfdbc918911fd1977f7943c7ddd5837e69c7784a12aed755`
- Result text SHA-256: `cde518029c15d0b65963b316bb551f479c57ff7c3d597d790bb066c499c0a44f`
- Metadata SHA-256: `17e137def32fb920662ed61de1d0f7f26bf88520ec3a33384cc4697082ccc13f`
- Identity SHA-256: `69bc9899ee044326ec97b5ef1f1bc2971557c6964e5f69dfa0dfeb3f42957fee`
- Result-save ledger: epoch 220, entry `3380829d0daf5f92c31086fce2870b18191841c0cdf1c7f214dea1139068c47d`
- Exact-own deletion evidence: `receipts/GORU_DR_EXACT_OWN_DELETION.json`
- Deletion evidence SHA-256: `759d150ff71074e8d6a09c5e14c4ce2516a00ec45e8b65fd6c08d9a184bdc43c`
- Deletion ledger: epoch 239; exact-title correction epoch 240
- Expected current ledger chain: `VERIFY_OK` with at least 241 entries

Verify mechanically:

1. File hashes match.
2. The saved result precedes deletion in the ledger.
3. Identity fields agree across identity, result, metadata, and deletion evidence.
4. Deletion evidence records exact ID/title/submit UTC, dialog confirmation, post path `/app`, no bulk delete, and no unrelated conversation touched.
5. Ledger chain verifies.
6. Note the raw result quality miss: it was saved intact but exceeded the requested eight-bullet format; no rerun is authorized.

Return a concise PASS/FAIL with exact mismatches. No writes.

GORU_DR_FINAL_CUSTODY_VERIFY_20260714
