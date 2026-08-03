# Hard-burn brief H4 — Wiki/DB integration dry-run plan for P4 candidates (offline prep for rollup follow-up item 4)

Burn: `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`)
Root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z`
Prior burn root (read-only inputs): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z`
Repo (read-only): `/Users/duhokim/NebulaMind/NebulaMind`

## Ownership
- Your ONLY write area: `<root>/h4-wiki-integration-plan/` — create it. Never write anywhere else on the machine. Do not modify T0.md, `briefs/`, other `h*` subdirs, the prior burn root, or any repo/runner/live file. Do not create STOP/HOLD files.
- NO database connections of any kind (not even read-only), NO API calls, NO server start. Schema knowledge comes from local files only: `wiki_schema.md` and backend wiki/trust code, read-only.
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
Safe offline artifacts only. No network/browser, runner/candidate writes, DB/API/wiki publication, deploy/restart, git, cron/launchd/background jobs, billing/account/credentials, cloud/GCP. Nothing in this lane publishes anything; you produce the plan the gated pass will execute.

## ACK
First action: write `<own>/H4_ACK.md` containing exactly the line `FABLE_HARD_BURN_H4_ACK_20260711T035354Z` plus your UTC start timestamp.

## Inputs
- `p4-derived-claims/CLAIM_EVIDENCE_CANDIDATES.md` (13 candidates) — pinned sha256 `1c8d9a7d28566a19a957cac754a7b8c6c5981a3ad445eb3d3f9daacbd49f8b39`; verify before use; on mismatch record in receipt and fail closed.
- `p4-derived-claims/P4_RECEIPT.md` — pinned sha256 `27a1efc000a6a5044e5a9a3199e3ef22dfebe9f33d522bafd8e8e98a6909a85b`.
- Repo `wiki_schema.md` and backend wiki/claim/trust code — live working-tree files, read-only; record path+sha256 of each file you rely on in your receipt (no pins available; note them as current-state reads).

## Task (max effort — prefer exhaustive coverage over early finish)
Convert P4's 13 offline claim/evidence candidates into a complete dry-run integration plan so the gated wiki/DB pass (rollup follow-up item 4) is a mechanical execution. For EVERY one of the 13 candidates: proposed target page slug (and how to resolve the real page id at gate time), exact insert location/section, exact payload shaped to the schema in `wiki_schema.md` (claim text, evidence references, source/trust fields), idempotency/duplicate-check plan (how the gated pass detects the claim already exists before writing), publish-state proposal, and rollback note. Add a plan-level preamble: ordered execution steps for the gated pass, what requires live-DB confirmation (ids, existing page state), and a schema-conformance statement per payload. Flag any candidate that cannot be mapped cleanly and say exactly why.

## Deliverables (all in `<own>/`)
1. Headline: `WIKI_INTEGRATION_DRYRUN_PLAN.md` — top line marker `FABLE_HARD_BURN_H4_WIKI_DRYRUN_20260711T035354Z`, covering all 13 candidates.
2. `H4_RECEIPT.md` — input custody results (pinned vs recomputed sha256; live repo files read, each with path+sha256), every produced file with bytes+sha256, poll log, safety attestation (explicit: no writes outside own subdir, no DB/API contact, no banned action), status COMPLETE or PARTIAL, ending with the exact line `FABLE_HARD_BURN_H4_DONE_20260711T035354Z`.
3. 0-byte done marker `<own>/FABLE_HARD_BURN_H4_DONE_20260711T035354Z` — write it when you finish or stop for any reason; the receipt status carries COMPLETE/PARTIAL.

Stretch (only if core is complete inside cap): field-by-field schema-conformance checklist per payload validated against `wiki_schema.md`, plus a dedup matrix across the 13 candidates.
