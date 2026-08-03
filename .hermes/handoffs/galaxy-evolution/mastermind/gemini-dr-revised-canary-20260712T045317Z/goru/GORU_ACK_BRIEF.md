# GORU BRIEF — revised C1r role-lock ACK

Packet: `gemini-dr-revised-canary-20260712T045317Z`
Scope: LOCAL-ONLY read verification plus one ACK file.

Read only:
- `MANIFEST.json`
- `prompt/C1r.md`
- `validator/VALIDATOR_RECEIPT.json`
- `postmortem/POSTMORTEM.md`
- `postmortem/INDEPENDENT_AUDIT_ADDENDUM.md`
- marker filenames in this packet root

Verify:
1. `prompt/C1r.md` SHA-256 is `fffac44fbf6e9abe3afb1f8f34f3a9e3e7688991f319c4927459fb29ac00e1ef` and matches the current manifest.
2. `validator/VALIDATOR_RECEIPT.json` SHA-256 is `7f6dfcc14a896198f02e344496143dd0c8ca5f31e1ecaf2056baafa89a7a17dc` and matches the current manifest.
3. The current manifest SHA-256 is `5d955e1728d868ee488a3707b04f274d54b8b42fed83f4bced16f5b9bc9fc29a`.
4. `DR_REVISED_NOT_ARMED_20260712T045317Z` and `DR_C1R_NOT_ARMED_READ_CHANNEL_LOSS_20260712T055023Z` exist; no `DR_C1R_ARMED_*` marker exists at verification time.

Write exactly one file:
- `goru/GORU_ACK.md`

The ACK must state the UTC time, the verified hashes above, and that Goru accepts:
- LOCAL-ONLY role only;
- no browser/network/Gemini/account/verification action;
- no DB/product/git/deploy/cron action;
- no live execution or arming authority;
- Tori is sole browser operator only after a separate arming marker;
- one Duho Start, zero Tori/Goru Start;
- ambiguity or integrity mismatch fails closed.

Do not edit any other file, marker, manifest, ledger, prompt, validator, or receipt.
Done marker in the file: `GORU_C1R_ROLE_ACK_DONE_20260712T045317Z`
