# Hard-burn brief H1 — Unified network-verification workplan (offline prep for rollup follow-up item 1)

Burn: `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`)
Root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z`
Prior burn root (read-only inputs): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z`

## Ownership
- Your ONLY write area: `<root>/h1-network-verification-workplan/` — create it. Never write anywhere else on the machine. Do not modify T0.md, `briefs/`, other `h*` subdirs, the prior burn root, or any repo/runner/live file. Do not create STOP/HOLD files.
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
Safe offline artifacts only. No network/browser, runner/candidate writes, DB/API/wiki publication, deploy/restart, git, cron/launchd/background jobs, billing/account/credentials, cloud/GCP. This lane plans network verification — it performs ZERO network calls.

## ACK
First action: write `<own>/H1_ACK.md` containing exactly the line `FABLE_HARD_BURN_H1_ACK_20260711T035354Z` plus your UTC start timestamp.

## Inputs (verify pinned sha256 before use; on mismatch, record in receipt and treat that input as unusable — fail closed)
All under the prior burn root:
- `p2-cycle7-source-ledger/SOURCE_LEAD_LEDGER.json` — `faadcc22f20e0037771f55e84e624a782ed93257716a779205dd6f5563ab0d07`
- `p2-cycle7-source-ledger/AGN_SFR_STATUS_DEBATE_MAP.md` (§6 priority order) — `8f3d33429bd70b372887fca3115e813189395d1203eff3f410344da64d0aafee`
- `p1-rp1-invariants/INTRODUCTION_LITERATURE_REFERENCE.md` (EXT-1…EXT-4) — `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d`
- `p3-m3-rt-baseline/M3_ACCEPTANCE_BASELINE.md` — `d028f3c716cc123be1840170d6111c42e24693451c9d3bf90284fdb19691d433`
- `p3-m3-rt-baseline/RT_CARDS_DEEPENING.md` (per-card network items) — `21564dd6d78c72483087d436f4256e461913ec9ab013c4ab7053bfe14eed7e18`
- `p4-derived-claims/CLAIM_EVIDENCE_CANDIDATES.md` (enrichment targets) — `1c8d9a7d28566a19a957cac754a7b8c6c5981a3ad445eb3d3f9daacbd49f8b39`
- `p1-rp1-invariants/INVARIANT_MANIFEST.json` (for registration stubs) — `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717`

## Task (max effort — prefer exhaustive coverage over early finish)
Build the single coherent gated network-verification pass that rollup follow-up item 1 calls for, as a plan only. Merge into ONE deduplicated, priority-ordered queue: all 39 P2 `NEEDS_NETWORK_VERIFICATION` leads (honor debate-map §6 priority order; the 5 retained leads first), P1's EXT-1…EXT-4 literature slots, every P3 per-card network item, and P4 external-value enrichment targets. Per queue item: stable id, source lane + source item id, exact claim/value at stake, proposed query/URL strategy, acceptance criterion (what evidence upgrades it), expected output artifact, manifest-registration stub (which INVARIANT_MANIFEST entry gains/changes on adoption), and risk notes. Mark cross-item dependencies and dedup collisions explicitly.

## Deliverables (all in `<own>/`)
1. Headline: `NETWORK_VERIFICATION_WORKPLAN.md` — top line marker `FABLE_HARD_BURN_H1_NETWORK_WORKPLAN_20260711T035354Z`. Optionally a machine-readable `network_verification_queue.json` alongside.
2. `H1_RECEIPT.md` — input custody results (pinned vs recomputed sha256), every produced file with bytes+sha256, poll log, safety attestation (explicit: no writes outside own subdir, no banned action, zero network calls), status COMPLETE or PARTIAL, ending with the exact line `FABLE_HARD_BURN_H1_DONE_20260711T035354Z`.
3. 0-byte done marker `<own>/FABLE_HARD_BURN_H1_DONE_20260711T035354Z` — write it when you finish or stop for any reason; the receipt status carries COMPLETE/PARTIAL.

Stretch (only if core is complete inside cap): per-item alternate query phrasings and a cross-lead dependency graph section.
