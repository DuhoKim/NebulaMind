# Hard-burn brief H8 — Adversarial audit of P3 acceptance baseline + RT-card deepening (stretch wave)

Burn: `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`)
Root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z`
Prior burn root (read-only inputs): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z`

## Ownership
- Your ONLY write area (`<own>`): `<root>/h8-p3-acceptance-deepening-audit/` — create it. Never write anywhere else on the machine. Do not modify T0.md, `briefs/`, other `h*` subdirs, the prior burn root, or any repo/runner/live file. Do not create STOP/HOLD files.
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
Safe offline artifacts only. No network/browser, runner/candidate writes, DB/API/wiki publication, deploy/restart, git, cron/launchd/background jobs, billing/account/credentials, cloud/GCP. This audit is read-only on every input and performs ZERO network calls; do NOT execute any acceptance test against a live system — audit the documents.

## ACK
First action: write `<own>/H8_ACK.md` containing exactly the line `FABLE_HARD_BURN_H8_ACK_20260711T035354Z` plus your UTC start timestamp.

## Inputs (verify pinned sha256 before use; on mismatch, record in receipt and treat that input as unusable — fail closed)
All under the prior burn root, `p3-m3-rt-baseline/`:
- `M3_ACCEPTANCE_BASELINE.md` — `d028f3c716cc123be1840170d6111c42e24693451c9d3bf90284fdb19691d433`
- `RT_CARDS_DEEPENING.md` — `21564dd6d78c72483087d436f4256e461913ec9ab013c4ab7053bfe14eed7e18`
- `P3_RECEIPT.md` — `70573e18df09cf45b73dcee5b75602541a6e33ea427dfa4b378c2f207eecd90b`

## Task (adversarial, max effort — hunt defects, do not summarize; prefer exhaustive coverage over early finish)
Try to break the P3 packet. Checks, each recorded with verdict CLEAN / DEFECT / UNVERIFIABLE-OFFLINE plus evidence:
1. Criterion testability: every acceptance criterion in `M3_ACCEPTANCE_BASELINE.md` must be decidable — measurable threshold, defined input, defined pass/fail. Flag vacuous, self-satisfying, ambiguous, or unfalsifiable criteria.
2. Card ↔ baseline bijection: every RT card in `RT_CARDS_DEEPENING.md` maps to a baseline entry and vice versa (set-difference both ways); statuses agree between the two docs.
3. Numeric consistency: every threshold, count, or value appearing in both docs must match exactly; recompute any derived numbers.
4. Evidence for claimed status: any criterion or card already marked met/passed/accepted must cite in-packet evidence; a claimed pass without evidence is a MAJOR defect.
5. Per-card network items: each is well-formed (what to fetch, what would count as confirmation) and correctly marked as pending, never silently assumed done.
6. Receipt custody recheck: recompute sha256 + bytes for every file `P3_RECEIPT.md` lists and compare against its claims.

## Deliverables (all in `<own>/`)
1. Headline: `P3_ACCEPTANCE_DEEPENING_ADVERSARIAL_AUDIT.md` — top line marker `FABLE_HARD_BURN_H8_P3_AUDIT_20260711T035354Z`. Must contain: findings table (id H8-F01…, severity BLOCKER/MAJOR/MINOR/NOTE, exact file+line/quote, why wrong, proposed disposition), a criterion-by-criterion testability table, the full check log (all 6 check families, clean checks included), and a packet verdict: PASS / PASS-WITH-FIXES / FAIL.
2. `H8_RECEIPT.md` — input custody results (pinned vs recomputed sha256), every produced file with bytes+sha256, poll log, safety attestation (no writes outside `<own>`, no banned action, zero network calls, prior burn root untouched), status COMPLETE or PARTIAL, ending with the exact line `FABLE_HARD_BURN_H8_DONE_20260711T035354Z`.
3. 0-byte done marker `<own>/FABLE_HARD_BURN_H8_DONE_20260711T035354Z` — write it when you finish or stop for any reason; the receipt status carries COMPLETE/PARTIAL.
