# Hard-burn brief H3 — Runner/manuscript integration change-packet (offline prep for rollup follow-up item 3)

Burn: `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`)
Root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z`
Prior burn root (read-only inputs): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z`

## Ownership
- Your ONLY write area: `<root>/h3-runner-integration-packet/` — create it. Never write anywhere else on the machine. The runner tree (PID 45665's working area), candidates, manuscript, audit config, and repo are STRICTLY read-only: you produce proposed changes as text in your subdir; you apply nothing. Do not modify T0.md, `briefs/`, other `h*` subdirs, or the prior burn root. Do not create STOP/HOLD files.
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
Safe offline artifacts only. No network/browser, runner/candidate writes, DB/API/wiki publication, deploy/restart, git, cron/launchd/background jobs, billing/account/credentials, cloud/GCP. The live weekend-sprint runner must remain untouched — read-only contact only, exactly like the prior burn.

## ACK
First action: write `<own>/H3_ACK.md` containing exactly the line `FABLE_HARD_BURN_H3_ACK_20260711T035354Z` plus your UTC start timestamp.

## Inputs (verify pinned sha256 before use; on mismatch, record in receipt and treat that input as unusable — fail closed)
- `p1-rp1-invariants/INVARIANT_MANIFEST.json` (105 entries) — `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717`
- `p1-rp1-invariants/RCA_NUMERIC_DRIFT.md` — `45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096` (its pointers locate the prose-phase prompt and the audit `numeric_invariants` list; read those live locations read-only)
- `p1-rp1-invariants/INTRODUCTION_LITERATURE_REFERENCE.md` — `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d`
- `p2-cycle7-source-ledger/PRIOR_WORK_COMPARISON_CANDIDATE.md` — `2545c71295d1c51fd4593a1ce0000cf6b7450d7db03e2fa32f7c6a1061414035` (sequencing dependency only)

## Task (max effort — prefer exhaustive coverage over early finish)
Prepare the complete, paste-ready integration change-packet for rollup follow-up item 3 so the gated integrator pass becomes mechanical. One headline document with four sections: (a) proposed extension of the runner audit `numeric_invariants` list — exact entries derived from the 105-entry manifest, in the audit's own format, with a mapping table manifest-entry → audit-entry and explicit coverage stats (which manifest entries are already covered, which are new); (b) verbatim-carry rule prompt patch — exact current text of the prose-phase prompt (quoted from the live file, read-only, with its path and sha256) and exact proposed replacement text; (c) canon adjudication memo for `-1.283` vs `-1.282` and `2.830` vs `2.831` — evidence from RCA both ways, a recommendation, and the atomic-change checklist (manuscript + audit list + manifest must change together, with ordered steps and rollback); (d) integration sequencing, including that the P2 comparison candidate integrates only after the network pass (follow-up item 1) upgrades its leads.

## Deliverables (all in `<own>/`)
1. Headline: `RUNNER_INTEGRATION_CHANGE_PACKET.md` — top line marker `FABLE_HARD_BURN_H3_INTEGRATION_PACKET_20260711T035354Z`.
2. `H3_RECEIPT.md` — input custody results (pinned vs recomputed sha256; live files read, each with path+sha256), every produced file with bytes+sha256, poll log, safety attestation (explicit: no writes outside own subdir, runner/manuscript/audit/repo untouched, no banned action), status COMPLETE or PARTIAL, ending with the exact line `FABLE_HARD_BURN_H3_DONE_20260711T035354Z`.
3. 0-byte done marker `<own>/FABLE_HARD_BURN_H3_DONE_20260711T035354Z` — write it when you finish or stop for any reason; the receipt status carries COMPLETE/PARTIAL.

Stretch (only if core is complete inside cap): a small offline consistency-check script in `<own>/tools/` that cross-validates your proposed audit list against the manifest (runs locally, reads only; precedent: P1's `tools/build_manifest.py`).
