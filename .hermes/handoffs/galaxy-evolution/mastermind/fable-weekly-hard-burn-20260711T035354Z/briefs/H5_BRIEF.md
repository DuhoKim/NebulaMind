# Hard-burn brief H5 — Value-level verification of the remaining seven topic artifacts (rollup follow-up item 5, fully offline)

Burn: `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`)
Root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z`
Prior burn root (read-only inputs): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z`

## Ownership
- Your ONLY write area: `<root>/h5-supplement-value-verification/` — create it. Never write anywhere else on the machine. Do not modify T0.md, `briefs/`, other `h*` subdirs, the prior burn root, or any repo/runner/live file. Do not create STOP/HOLD files.
- File-only handoff. No tmux send-keys, no messaging other lanes, no reading other H-lane subdirs.

## Clock
- Cap: 40 minutes from your ACK, or absolute stop `2026-07-11T04:50:00Z` — whichever is earlier.
- Reserve the final 5 minutes for receipt + done marker. Timestamps via `date -u +%Y-%m-%dT%H:%M:%SZ`.

## Stop/hold polling
Poll at ACK and at least every 5 minutes (and between major steps):
- `<root>/GLOBAL_STOP_20260711T035354Z.md` present → finalize immediately (receipt status PARTIAL, write done marker), stop.
- `<root>/HOLD_5H_20260711T035354Z.md` present → pause new work, re-poll every 2 min; if still present at cap or 04:45Z, finalize as PARTIAL.
Log every poll (UTC timestamp + absent/present) in the receipt's Poll log.

## Safety boundary (binding, verbatim from T0)
Safe offline artifacts only. No network/browser, runner/candidate writes, DB/API/wiki publication, deploy/restart, git, cron/launchd/background jobs, billing/account/credentials, cloud/GCP.

## ACK
First action: write `<own>/H5_ACK.md` containing exactly the line `FABLE_HARD_BURN_H5_ACK_20260711T035354Z` plus your UTC start timestamp.

## Inputs (custody chain — verify before use; on mismatch, record in receipt and treat that input as unusable — fail closed)
- `p1-rp1-invariants/P1_RECEIPT.md` — pinned sha256 `bdfebdc10c3166f045e3d3f9edf9804c87ee546d2f0cfd664e83930020fe763a`. It itemizes the 12 hash-verified copies in `p1-rp1-invariants/sources-snapshot/` — that itemization is your source of truth for the topic-artifact and supplement snapshot paths+hashes. Recompute each snapshot hash against the receipt's value before reading it.
- `p1-rp1-invariants/RCA_NUMERIC_DRIFT.md` — `45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096`. Identifies which TWO topic artifacts already received full value-level verification; your scope is the remaining SEVEN.
- `p1-rp1-invariants/INVARIANT_MANIFEST.json` — `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717`.
- Supplement prose snapshot: the copy hashing to `a4e3d66c…` per the P1 receipt itemization (full hash there).
Work exclusively from the hash-pinned snapshot copies, not the live originals.

## Task (max effort — prefer exhaustive coverage over early finish)
Execute rollup follow-up item 5 in full. For EACH of the seven not-yet-value-verified topic artifacts: extract every numeric value (script it — precedent: P4's scripted numerals audit); locate every occurrence of that value (or its expected transformed/rounded form) in the supplement prose snapshot; classify per value as PASS (exact match), DRIFT (nearest-round or referent mismatch — give both values, line numbers on both sides, RCA-style analysis), or ABSENT (in artifact but never surfaced in prose — note whether that is expected); cross-check each value against `INVARIANT_MANIFEST.json` and emit an add-candidate list for legitimate values the 105-entry manifest lacks. Any new drift finding gets the same depth of treatment as P1's RCA entries (drifted digits, direction, suspected mechanism). Finish with a summary table: per artifact — values extracted / PASS / DRIFT / ABSENT / manifest-covered / manifest-add-candidates.

## Deliverables (all in `<own>/`)
1. Headline: `SUPPLEMENT_VALUE_VERIFICATION.md` — top line marker `FABLE_HARD_BURN_H5_VALUE_VERIFICATION_20260711T035354Z`. Extraction script(s) go in `<own>/tools/`.
2. `H5_RECEIPT.md` — input custody results (pinned vs recomputed sha256 for receipt, RCA, manifest, and every snapshot used), every produced file with bytes+sha256, poll log, safety attestation (explicit: no writes outside own subdir, snapshots and originals untouched, no banned action), status COMPLETE or PARTIAL, ending with the exact line `FABLE_HARD_BURN_H5_DONE_20260711T035354Z`.
3. 0-byte done marker `<own>/FABLE_HARD_BURN_H5_DONE_20260711T035354Z` — write it when you finish or stop for any reason; the receipt status carries COMPLETE/PARTIAL.

Stretch (only if core is complete inside cap): extend the same value-level sweep to flagship cross-references of the seven artifacts (flagship snapshot `63b3920e…` per P1 receipt itemization).
