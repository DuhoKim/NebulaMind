# V15 GATE OUTCOME — selection rule (option A) — 2026-09-06 — **SIGNABLE (both seats), NOT SIGNED**

**Target:** `OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V15_20260906.md`
**SHA-256 (= §17.2-style preimage digest; signature lines blank):** `fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1`

## Seats
| seat | engine | dispatch | ACCESS_SHA proof | verdict |
|---|---|---|---|---|
| B | codex (via `_tmp_codex_as_agy_shim.sh`) | 01:55 KST | proven, = target digest; process exited before read | **SIGNABLE-AS-PRECOMMITMENT** — no FATAL, no MAJOR |
| A | agy (Gemini) | 01:54 KST | — | provider network error at 01:59, no verdict (quarantined `_networkerror_0159`) |
| A (re-run) | agy (Gemini) | 02:00 KST | proven, = target digest; wrapper rc=0, exited before read | **SIGNABLE-AS-PRECOMMITMENT** — no FATAL, no MAJOR (nine MINOR-tagged sections, every one answered in the affirmative; item 9: "Nothing is missing") |

## Cap (Blanc 00:49, released narrowly 01:49 for this one round)
Re-arms after this round. Outcome rule applied: **clear pair → file SIGNABLE, pin digest, prepare freeze statement, STOP.** No fatal at the beacon-record/builder boundary was returned by either seat, so the cap has nothing to fire on; it is nonetheless re-armed: no V16 without a human ruling. Filed 02:08 KST.

## What is NOT done (prohibitions in force)
No signature, no freeze, no seal, no beacon read for a real T_sign, no development draw, no fetch, no frozen pixel, nothing outward. Blanc brings this file to Duho in the morning.

## Freeze statement Duho would give (if he chooses to sign) — chat convention (§10 order step 1)
> "OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V15_20260906.md signed: fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1 at <UTC>"

then the lane fills SIGNATURE UTC / DUHO SIGNATURE and re-runs `signature_preimage.py` (two-step; stop on mismatch). Still blocked before any run: custodian account `nmcustody` and server-side branch protection (Duho's two jobs). Open finding for Duho: NIST live pulses carry 512-byte signatures under a 2048-bit certificate — refused under the rule as written; whether the beacon is worth keeping is his call.

## Seat evidence (verbatim tokens)
- `CODEX_SELRULE_V15_SEATB.md` line 2: `VERDICT: SIGNABLE-AS-PRECOMMITMENT`; summary: "V15 closes the sole V14 acceptance gap … The required suites pass warning-strict, all pins match, both generated artifacts reproduce byte-for-byte, and the retained NIST sample shows exactly the disclosed limitation."
- `AGY_SELRULE_V15_SEATA.md` line 2: `VERDICT: SIGNABLE-AS-PRECOMMITMENT`; run outputs it reproduced: 27 / 4 / 19 tests OK, 23-row probe table, observed-behaviour digest c68d49e22427a328… reproduced, `signature_verifies_under_leaf` False on the live sample (key 2048, sig 512), every pinned file hashed and matched.
- Both reports' first line `ACCESS_SHA=` equals the target's own SHA-256 recomputed here.

## Independence note
Codex authored the beacon_v2 code (00:13–02:00 window) and gated the document that pins it; it disclosed this in its first paragraph as instructed (Blanc 00:19). Agy did not author any of it. A third, non-authoring gate on the code alone remains available to Duho if he wants one before signing.
