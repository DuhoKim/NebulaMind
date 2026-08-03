# Hard-burn brief H7 — Adversarial audit of P2 source ledger + debate map (stretch wave)

Burn: `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`)
Root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z`
Prior burn root (read-only inputs): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z`

## Ownership
- Your ONLY write area (`<own>`): `<root>/h7-p2-ledger-debate-audit/` — create it. Never write anywhere else on the machine. Do not modify T0.md, `briefs/`, other `h*` subdirs, the prior burn root, or any repo/runner/live file. Do not create STOP/HOLD files.
- Independent lane: no dependency on H1–H5 or the other stretch lanes. File-only handoff; no tmux send-keys; do not read any other `h*` subdir.

## Clock
- Cap: 35 minutes from your ACK, or absolute stop `2026-07-11T04:45:00Z` — whichever is earlier.
- Reserve the final 5 minutes for receipt + done marker. Timestamps via `date -u +%Y-%m-%dT%H:%M:%SZ`.

## Stop/hold polling
Poll at ACK and at least every 5 minutes (and between major steps):
- `<root>/GLOBAL_STOP_20260711T035354Z.md` present → finalize immediately (receipt status PARTIAL, write done marker), stop.
- `<root>/HOLD_5H_20260711T035354Z.md` present → pause new work, re-poll every 2 min; if still present at cap or 04:45Z, finalize as PARTIAL.
Log every poll (UTC timestamp + absent/present) in the receipt's Poll log.

## Safety boundary (binding, verbatim from T0)
Safe offline artifacts only. No network/browser, runner/candidate writes, DB/API/wiki publication, deploy/restart, git, cron/launchd/background jobs, billing/account/credentials, cloud/GCP. This audit is read-only on every input and performs ZERO network calls (lead verification itself stays OUT of scope — you audit the ledger's internal integrity only).

## ACK
First action: write `<own>/H7_ACK.md` containing exactly the line `FABLE_HARD_BURN_H7_ACK_20260711T035354Z` plus your UTC start timestamp.

## Inputs (verify pinned sha256 before use; on mismatch, record in receipt and treat that input as unusable — fail closed)
All under the prior burn root, `p2-cycle7-source-ledger/`:
- `SOURCE_LEAD_LEDGER.json` — `faadcc22f20e0037771f55e84e624a782ed93257716a779205dd6f5563ab0d07`
- `AGN_SFR_STATUS_DEBATE_MAP.md` — `8f3d33429bd70b372887fca3115e813189395d1203eff3f410344da64d0aafee`
- `PRIOR_WORK_COMPARISON_CANDIDATE.md` — `2545c71295d1c51fd4593a1ce0000cf6b7450d7db03e2fa32f7c6a1061414035`
- `P2_RECEIPT.md` — `ddcb5eaa74abaf849953d3728d15b53f23dd9f3e07a73fe5a9001863934bd83a`

## Task (adversarial, max effort — hunt defects, do not summarize; prefer exhaustive coverage over early finish)
Try to break the P2 packet. Checks, each recorded with verdict CLEAN / DEFECT / UNVERIFIABLE-OFFLINE plus evidence:
1. Ledger integrity: valid JSON; unique lead ids; legal status vocabulary used consistently; no orphan fields; every lead carries source identification sufficient to act on later.
2. Count recompute: recount every status bucket yourself. Downstream lanes were told there are 39 `NEEDS_NETWORK_VERIFICATION` leads with 5 retained leads prioritized — verify both numbers against the ledger and against every count the debate map and `P2_RECEIPT.md` assert; any mismatch is a MAJOR defect.
3. Debate map §6 priority order: every lead referenced in the map exists in the ledger and vice versa (set-difference both ways); the priority order is total, deterministic, and free of contradictions.
4. Stance integrity: no source cited on both sides of the same claim without an explicit reconciliation note; stance labels consistent between map body and ledger entries.
5. `PRIOR_WORK_COMPARISON_CANDIDATE.md` consistency with the ledger it draws from.
6. Receipt custody recheck: recompute sha256 + bytes for every file `P2_RECEIPT.md` lists and compare against its claims.

## Deliverables (all in `<own>/`)
1. Headline: `P2_LEDGER_DEBATE_ADVERSARIAL_AUDIT.md` — top line marker `FABLE_HARD_BURN_H7_P2_AUDIT_20260711T035354Z`. Must contain: findings table (id H7-F01…, severity BLOCKER/MAJOR/MINOR/NOTE, exact file+line/quote, why wrong, proposed disposition), recomputed count table (claimed vs recounted per status bucket), the full check log (all 6 check families, clean checks included), and a packet verdict: PASS / PASS-WITH-FIXES / FAIL.
2. `H7_RECEIPT.md` — input custody results (pinned vs recomputed sha256), every produced file with bytes+sha256, poll log, safety attestation (no writes outside `<own>`, no banned action, zero network calls, prior burn root untouched), status COMPLETE or PARTIAL, ending with the exact line `FABLE_HARD_BURN_H7_DONE_20260711T035354Z`.
3. 0-byte done marker `<own>/FABLE_HARD_BURN_H7_DONE_20260711T035354Z` — write it when you finish or stop for any reason; the receipt status carries COMPLETE/PARTIAL.
