# TORI DR PREFLIGHT BLOCKER — no authenticated CDP target on Mac Pro

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
UTC: 2026-07-14T08:28:31Z and follow-up state through ledger epoch 49

## Resume custody

Tori verified the Duho resume authorization and broker-authored resume before relaying it to Goru:

- Authorization SHA-256: `9f6654c61b91940420793e5e2d06d114b797a97ad27d7932c0b11f4b8246d0b5`
- Ledger reset: epoch 22, type `frozen_reset`
- Reset entry SHA-256: `3ee6ff45d8db6ee45cb2c947a6d37f7a5ec4860f92881163eb1d4c15074310c2`
- Ledger after reset: `VERIFY_OK`
- Broker after reset: `frozen=false`

Tori dispatched the resume marker to `goru-agy-pilot-resume:0.0` through the approved dispatch protocol. Resume brief SHA-256: `a3baa9e51fef688bdc9c69b7e3b4e6e746eedff83c99f61eede5bfa210381949`.

## Correct Mac Pro preflight

Goru initially checked the old Studio `writerA` sandbox. Tori denied a premature blocker append and redirected the read-only preflight to the canonical Mac Pro over direct Thunderbolt. Correction brief SHA-256: `8081e4845499d206e555bb216cb9a73c99460dfe20f5574d0083a68fc64e5de1`.

Goru and Tori independently established these non-secret facts on the Mac Pro:

- Chrome root processes: 1
- Chrome version: 149.0.7827.199
- Root process has a remote-debugging flag: false
- Root process has a custom user-data-dir flag: false
- Root process has a profile-directory flag: false
- Chrome TCP listeners: 0
- Existing CDP endpoint: none
- DR task processes launched: 0

The existing browser is therefore the default Chrome profile with no CDP endpoint. It cannot supply the exact authenticated DOM/CDP target required by the live order. Tori and Goru did not launch or relaunch Chrome, copy a profile, inspect browser/profile data, navigate, request a DR target lease, submit, or spend DR quota.

## Concurrent Flow state

The resume is valid and the Studio broker remains unfrozen. The ledger shows Yui's bounded Flow work in progress. At the latest preflight snapshot, Flow held the shared `account-submission` lease `L00008` (ledger epoch 49). DR would not have been permitted to submit while that lease was live even if a CDP target had existed.

The prior epoch-17 event was a false-positive Chrome toolbar sync/profile badge, not a Flow/Gemini-page challenge. No challenge STOP is active now.

## Blocker and exact next gate

The DR run is blocked by control-plane readiness, not by authorization:

1. Duho manually prepares a dedicated, non-default Chrome user-data directory on the Mac Pro with remote debugging enabled and signs it into the intended DR account; agents do not handle sign-in or credentials; or
2. Duho explicitly authorizes another control path compatible with the live rails.

Until then, Goru remains unarmed. Flow may continue through the broker. No broker freeze was requested for this non-safety blocker.

TORI_DR_PREFLIGHT_BLOCKER_NO_CDP_20260714
