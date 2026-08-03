# Hard-burn brief H9 — Adversarial audit of P4's 13 claim/evidence candidates vs sources + wiki schema (stretch wave)

Burn: `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`)
Root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z`
Prior burn root (read-only inputs): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z`

## Ownership
- Your ONLY write area (`<own>`): `<root>/h9-p4-candidate-source-schema-audit/` — create it. Never write anywhere else on the machine. Do not modify T0.md, `briefs/`, other `h*` subdirs, the prior burn root, or any repo/runner/live file. Do not create STOP/HOLD files.
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
Safe offline artifacts only. No network/browser, runner/candidate writes, DB/API/wiki publication, deploy/restart, git, cron/launchd/background jobs, billing/account/credentials, cloud/GCP. Read-only on every input, including the repo schema file; ZERO network calls — external sources you cannot reach offline are marked UNVERIFIABLE-OFFLINE, never fetched.

## ACK
First action: write `<own>/H9_ACK.md` containing exactly the line `FABLE_HARD_BURN_H9_ACK_20260711T035354Z` plus your UTC start timestamp.

## Inputs
Pinned (verify sha256 before use; on mismatch record in receipt and fail closed), under the prior burn root, `p4-derived-claims/`:
- `CLAIM_EVIDENCE_CANDIDATES.md` — `1c8d9a7d28566a19a957cac754a7b8c6c5981a3ad445eb3d3f9daacbd49f8b39` (expected: exactly 13 candidates, `P4-C01`…`P4-C13`)
- `P4_RECEIPT.md` — `27a1efc000a6a5044e5a9a3199e3ef22dfebe9f33d522bafd8e8e98a6909a85b`
Unpinned (read-only; recompute and record sha256 at read time in your receipt):
- Schema: `/Users/duhokim/NebulaMind/NebulaMind/wiki_schema.md` (live working-tree file — record the hash you audited against)
- `<prior root>/P4_CONDITION_PACKET.md` (candidate conditions/context, if referenced)

## Task (adversarial, max effort — hunt defects, do not summarize; prefer exhaustive coverage over early finish)
Try to break the P4 candidate set. Checks, each recorded with verdict CLEAN / DEFECT / UNVERIFIABLE-OFFLINE plus evidence:
1. Census: exactly 13 candidates, ids P4-C01…P4-C13 with no gaps or duplicates; any deviation is a MAJOR defect.
2. Per-candidate source traceability (all 13, no sampling): every quantitative claim carries an explicit source + line reference per the packet's §Provenance and §Conventions; where the referenced snapshot is reachable offline (inside the prior burn root or quoted in-packet), confirm the quoted value matches character-for-character; unreachable sources → UNVERIFIABLE-OFFLINE with the exact path listed.
3. Conventions compliance: units, uncertainty/error treatment, and estimate-preference rules stated in §Conventions actually applied in every candidate.
4. Schema conformance: map each candidate onto the claim/evidence structure required by `wiki_schema.md` — required fields present, evidence typing legal, trust/stance fields representable; list any candidate that cannot be ingested as-is and exactly which field is missing/illegal.
5. Internal contradiction sweep: no candidate contradicts another candidate (denominators, counts, subset definitions across C01–C13); cross-check overlapping quantities.
6. Receipt custody recheck: recompute sha256 + bytes for every file `P4_RECEIPT.md` lists and compare against its claims.

## Deliverables (all in `<own>/`)
1. Headline: `P4_CANDIDATE_SOURCE_SCHEMA_ADVERSARIAL_AUDIT.md` — top line marker `FABLE_HARD_BURN_H9_P4_AUDIT_20260711T035354Z`. Must contain: a 13-row per-candidate verdict table (traceability / conventions / schema / contradiction columns), findings table (id H9-F01…, severity BLOCKER/MAJOR/MINOR/NOTE, exact file+line/quote, why wrong, proposed disposition), the full check log (clean checks included), and a packet verdict: PASS / PASS-WITH-FIXES / FAIL.
2. `H9_RECEIPT.md` — input custody results (pinned vs recomputed sha256, plus recorded hashes for unpinned inputs), every produced file with bytes+sha256, poll log, safety attestation (no writes outside `<own>`, no banned action, zero network calls, prior burn root untouched), status COMPLETE or PARTIAL, ending with the exact line `FABLE_HARD_BURN_H9_DONE_20260711T035354Z`.
3. 0-byte done marker `<own>/FABLE_HARD_BURN_H9_DONE_20260711T035354Z` — write it when you finish or stop for any reason; the receipt status carries COMPLETE/PARTIAL.
