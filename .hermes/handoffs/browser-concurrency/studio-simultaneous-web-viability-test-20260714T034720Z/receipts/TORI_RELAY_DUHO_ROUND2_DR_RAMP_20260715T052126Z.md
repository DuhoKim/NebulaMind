# Tori relay — Duho round-2 Deep Research re-research ramp

Verified UTC: 2026-07-15T05:21:26Z

Authorization source:
- `receipts/DUHO_MAX_CONSUMPTION_20260715.md`
- SHA-256: `a0cf2c39c219a1e2df531dbb1667a0e106e43362f6684c9791272bb5bf90604c`

Authorized Goru/Pro scope:
- Ordered round-2 Deep Research re-research for papers 01..09.
- Reference-only, advisory-only packets; no manuscript, DB, wiki, deploy, git, publish, cron, billing, credential, account-setting, bulk-history, or unrelated-conversation mutation.
- Save and hash each complete packet before deleting only its exact-owned conversation.
- Flow may run independently on Studio; the global broker serializes account-submit instants only.

Ramp:
- Start-to-Start ladder: 30 -> 20 -> 15 -> 10 -> 8 minutes after accepted Goru Starts.
- First anchor is the verified paper_08 Start at `2026-07-15T04:35:09Z`, lease `L00496`, epoch `2939`.
- First round-2 Start not before `2026-07-15T05:05:09Z`; this gate had passed at verification.
- On the first positively unaccepted or soft-throttled attempt: no retry, step the current gap up one notch, stop later papers, and HOLD at that sustainable gap.
- On a hard `google.com/sorry`, account/security redirect, CAPTCHA, login, or page challenge: do not interact; freeze the broker, stop, hold, and wake Hwao -> Duho.

Preflight result: PASS.
- Prompt count: 9.
- Prompt manifest SHA-256: `8442b235c12f1b1e3da4ccfb2ebf68c7c41d27e2455c1b060c2c1ded343865b7`.
- Ramp runner SHA-256: `c108922ba2cafc39d1a48821bd1d4ac182006c71897ed545f9fa5b1355cbd66e`.
- Account driver SHA-256: `0ecb34fbc4cc8e26e74aa37e7040b2dc1ebbb4e46874e79fa26bf7dd2f9aa276`.
- Ledger: `OK (3068 entries)`.
- Broker: unfrozen, zero live leases at the preflight snapshot.
- Exact Pro target: `C92443095EE9116210C178D855DF3329`, clean route `/app`.
- Fresh re-research output set: empty.

Terminal boundary: after paper 09 verification, HOLD for a fresh Duho gate. No packet is auto-applied and no publication is authorized.
