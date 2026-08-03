# Hard-burn brief H10 — Cross-packet reproducibility + integration-order audit of P1–P4 (stretch wave)

Burn: `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`)
Root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z`
Prior burn root (read-only inputs): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z`

## Ownership
- Your ONLY write area (`<own>`): `<root>/h10-cross-packet-repro-integration-audit/` — create it. Never write anywhere else on the machine. Do not modify T0.md, `briefs/`, other `h*` subdirs, the prior burn root, or any repo/runner/live file. Do not create STOP/HOLD files.
- Independent lane: no dependency on H1–H9 outputs. You MAY read the five brief files `<root>/briefs/H1_BRIEF.md`…`H5_BRIEF.md` (director-authored inputs, read-only) to map which forward lane consumes which packet; you may NOT read any `h1`…`h9` output subdir. File-only handoff; no tmux send-keys.

## Clock
- Cap: 35 minutes from your ACK, or absolute stop `2026-07-11T04:45:00Z` — whichever is earlier.
- Reserve the final 5 minutes for receipt + done marker. Timestamps via `date -u +%Y-%m-%dT%H:%M:%SZ`.

## Stop/hold polling
Poll at ACK and at least every 5 minutes (and between major steps):
- `<root>/GLOBAL_STOP_20260711T035354Z.md` present → finalize immediately (receipt status PARTIAL, write done marker), stop.
- `<root>/HOLD_5H_20260711T035354Z.md` present → pause new work, re-poll every 2 min; if still present at cap or 04:45Z, finalize as PARTIAL.
Log every poll (UTC timestamp + absent/present) in the receipt's Poll log.

## Safety boundary (binding, verbatim from T0)
Safe offline artifacts only. No network/browser, runner/candidate writes, DB/API/wiki publication, deploy/restart, git, cron/launchd/background jobs, billing/account/credentials, cloud/GCP. This audit is read-only on every input and performs ZERO network calls. The integration order you produce is a PLAN — you integrate nothing.

## ACK
First action: write `<own>/H10_ACK.md` containing exactly the line `FABLE_HARD_BURN_H10_ACK_20260711T035354Z` plus your UTC start timestamp.

## Inputs (verify pinned sha256 before use; on mismatch, record in receipt and treat that input as unusable — fail closed)
Under the prior burn root:
- `BURN_ROLLUP.md` — `b15afe07317ad1a5326dfa3b873be5a4fba01bad199534da96b5d9d519e24088`
- P1 `p1-rp1-invariants/`: `INVARIANT_MANIFEST.json` `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717`; `RCA_NUMERIC_DRIFT.md` `45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096`; `INTRODUCTION_LITERATURE_REFERENCE.md` `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d`; `P1_RECEIPT.md` `bdfebdc10c3166f045e3d3f9edf9804c87ee546d2f0cfd664e83930020fe763a`
- P2 `p2-cycle7-source-ledger/`: `SOURCE_LEAD_LEDGER.json` `faadcc22f20e0037771f55e84e624a782ed93257716a779205dd6f5563ab0d07`; `AGN_SFR_STATUS_DEBATE_MAP.md` `8f3d33429bd70b372887fca3115e813189395d1203eff3f410344da64d0aafee`; `PRIOR_WORK_COMPARISON_CANDIDATE.md` `2545c71295d1c51fd4593a1ce0000cf6b7450d7db03e2fa32f7c6a1061414035`; `P2_RECEIPT.md` `ddcb5eaa74abaf849953d3728d15b53f23dd9f3e07a73fe5a9001863934bd83a`
- P3 `p3-m3-rt-baseline/`: `M3_ACCEPTANCE_BASELINE.md` `d028f3c716cc123be1840170d6111c42e24693451c9d3bf90284fdb19691d433`; `RT_CARDS_DEEPENING.md` `21564dd6d78c72483087d436f4256e461913ec9ab013c4ab7053bfe14eed7e18`; `P3_RECEIPT.md` `70573e18df09cf45b73dcee5b75602541a6e33ea427dfa4b378c2f207eecd90b`
- P4 `p4-derived-claims/`: `CLAIM_EVIDENCE_CANDIDATES.md` `1c8d9a7d28566a19a957cac754a7b8c6c5981a3ad445eb3d3f9daacbd49f8b39`; `P4_RECEIPT.md` `27a1efc000a6a5044e5a9a3199e3ef22dfebe9f33d522bafd8e8e98a6909a85b`
Unpinned (read-only; recompute and record sha256): `P4_CONDITION_PACKET.md`, `METER_LOG.md` (prior root), `<root>/briefs/H1..H5_BRIEF.md`.

## Task (adversarial, max effort — hunt defects, do not summarize; prefer exhaustive coverage over early finish)
Audit the four packets AS A SET. Checks, each recorded with verdict CLEAN / DEFECT / UNVERIFIABLE-OFFLINE plus evidence:
1. Reproducibility scorecard per packet: inputs enumerated and pinned? steps deterministic and re-runnable offline? receipt hash/byte claims correct when recomputed? Score each packet REPRODUCIBLE / PARTIALLY / NOT, with the missing pieces named.
2. Custody sweep: recompute every pinned sha256 above; verify each `FABLE_BURN_Pn_DONE_20260711T010503Z` marker is exactly 0 bytes (sha256 must equal `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).
3. Cross-packet fact table: every fact quoted in ≥2 packets (counts, headline values, lead totals, candidate ids, rollup claims in `BURN_ROLLUP.md`) tabulated with per-packet values; any disagreement is a MAJOR defect.
4. Integration-order plan: the dependency-safe order for landing P1–P4 outputs downstream (manifest registration, ledger-driven verification, acceptance gating, candidate ingestion) — hard prerequisites, cycles, and conflicts called out; map which H1–H5 forward brief consumes which packet and flag any ordering hazard between the running lanes' future outputs (from their briefs only).
5. Gap sweep: anything the rollup promises that no packet delivers, or a packet delivers that the rollup omits.

## Deliverables (all in `<own>/`)
1. Headline: `CROSS_PACKET_REPRO_INTEGRATION_AUDIT.md` — top line marker `FABLE_HARD_BURN_H10_XPACKET_AUDIT_20260711T035354Z`. Must contain: per-packet reproducibility scorecard, custody sweep results, cross-packet fact table, ordered integration plan (numbered steps with prerequisites), findings table (id H10-F01…, severity BLOCKER/MAJOR/MINOR/NOTE, exact file+line/quote, why wrong, proposed disposition), and an overall verdict: SAFE-TO-INTEGRATE / INTEGRATE-WITH-FIXES / DO-NOT-INTEGRATE.
2. `H10_RECEIPT.md` — input custody results (pinned vs recomputed sha256, plus recorded hashes for unpinned inputs), every produced file with bytes+sha256, poll log, safety attestation (no writes outside `<own>`, no banned action, zero network calls, prior burn root untouched), status COMPLETE or PARTIAL, ending with the exact line `FABLE_HARD_BURN_H10_DONE_20260711T035354Z`.
3. 0-byte done marker `<own>/FABLE_HARD_BURN_H10_DONE_20260711T035354Z` — write it when you finish or stop for any reason; the receipt status carries COMPLETE/PARTIAL.
