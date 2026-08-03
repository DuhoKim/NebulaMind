# TORI — one bounded Pro Deep Research run final receipt

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
Final verification UTC: 2026-07-14T10:10:26Z
Authority: `receipts/DUHO_PRO_CDP_SIGNED_IN.md`

## Attach and page preflight

- Studio loopback SSH forward `127.0.0.1:19223` to Pro `127.0.0.1:9223`: running
- Dedicated target ID: `C92443095EE9116210C178D855DF3329`
- Dedicated profile: `dr-live-cdp-20260714`
- Gemini page-only preflight: signed-in page, prompt editor present, Deep Research control present
- Page challenge: false throughout the run
- Chrome toolbar/profile badge: not inspected and not used as a challenge signal
- Broker remained unfrozen

## Exactly one bounded run

Prompt:

> Using official Apple and Google Chrome documentation, explain in no more than eight bullets how a direct Thunderbolt Bridge between two Macs can support isolated browser automation. Include two limitations and source links.

Run identity:

- Conversation ID: `8af765be7d623416`
- Captured initial title: `Using official Apple and Google Chrome documentation, explain in no more than eight bullets how a direct Thunderbolt Bridge betw`
- Exact deletion-match title: full prompt above
- Prompt submit UTC: `2026-07-14T09:45:28.451996Z`
- Research start UTC: `2026-07-14T09:47:23Z`
- Identity receipt: `receipts/GORU_DR_RUN_IDENTITY.json`
- Identity SHA-256: `69bc9899ee044326ec97b5ef1f1bc2971557c6964e5f69dfa0dfeb3f42957fee`

The prompt submit used target lease `L00039` and serialized account-submission lease `L00040`; both were released. Gemini then produced a research plan. The single `Start research` confirmation for that same conversation used target lease `L00041` and serialized account-submission lease `L00042`; both were released. No second conversation, retry, or scale action occurred.

## Result custody — completed before deletion

Completion was detected only after:

- `Stop response` was absent
- Research-in-progress state was absent
- Three message blocks were present
- Final result contained 7,687 characters
- Result text was stable across a second capture
- Page challenge remained false

Saved artifacts:

- Result receipt: `receipts/GORU_DR_RESULT.md`
- Result receipt SHA-256: `84f3ebfee6ddc51fbfdbc918911fd1977f7943c7ddd5837e69c7784a12aed755`
- Raw result text SHA-256: `cde518029c15d0b65963b316bb551f479c57ff7c3d597d790bb066c499c0a44f`
- Metadata: `receipts/GORU_DR_RESULT_METADATA.json`
- Metadata SHA-256: `17e137def32fb920662ed61de1d0f7f26bf88520ec3a33384cc4697082ccc13f`
- Eight official Apple, Chrome, and Chromium source links were captured from the result page
- Result-save ledger: epoch 220, entry `3380829d0daf5f92c31086fce2870b18191841c0cdf1c7f214dea1139068c47d`
- Full ledger chain verified before deletion

Quality note: the raw result was preserved without rewriting, but it exceeded the requested no-more-than-eight-bullets format. This is a result-quality miss, not a custody failure. No rerun is authorized or attempted.

## Save-then-delete-own

Only after the verified result-save entry:

- Exact history href matched `/app/8af765be7d623416`
- Exact row title matched the captured run title and full prompt
- The exact row's `More options` menu was used
- The single `Delete` menu item and `Delete chat?` confirmation dialog were used
- Deleted UTC: `2026-07-14T10:02:01.833828Z`
- Post-delete target path: `/app`
- Old conversation path and history row: absent
- Bulk delete: false
- Unrelated conversation touched: false

Deletion evidence:

- `receipts/GORU_DR_EXACT_OWN_DELETION.json`
- SHA-256: `759d150ff71074e8d6a09c5e14c4ce2516a00ec45e8b65fd6c08d9a184bdc43c`
- Deletion ledger: epoch 239
- Exact-title correction ledger: epoch 240

The correction entry records the exact title omitted from epoch 239 by shell quoting; it represents no additional browser or deletion action.

## Final state

- Goru ran the reviewed read-only final verifier: PASS, no failed checks
- Ledger: `VERIFY_OK OK (241 entries)` before this final receipt
- Broker frozen: false
- Live broker leases: none
- Dedicated target: one, at `/app`
- Deleted conversation present: false
- SSH loopback forward remains running for Hwao/user disposition
- No scale action was taken

TORI_DR_ONE_BOUNDED_FINAL_20260714T101026Z
