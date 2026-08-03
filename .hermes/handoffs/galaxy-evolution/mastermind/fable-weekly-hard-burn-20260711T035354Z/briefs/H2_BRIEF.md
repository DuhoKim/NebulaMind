# Hard-burn brief H2 — Gemini sidecar REQ prompt-contract packet (offline prep for rollup follow-up item 2)

Burn: `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`)
Root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z`
Prior burn root (read-only inputs): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z`

## Ownership
- Your ONLY write area: `<root>/h2-gemini-req-contract/` — create it. Never write anywhere else on the machine. Do not modify T0.md, `briefs/`, other `h*` subdirs, the prior burn root, the live REQ file, or any repo/runner/live file. Do not create STOP/HOLD files.
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
Safe offline artifacts only. No network/browser, runner/candidate writes, DB/API/wiki publication, deploy/restart, git, cron/launchd/background jobs, billing/account/credentials, cloud/GCP. You draft the contract for a FUTURE supervised Gemini Web run — you do not run, schedule, or contact anything.

## ACK
First action: write `<own>/H2_ACK.md` containing exactly the line `FABLE_HARD_BURN_H2_ACK_20260711T035354Z` plus your UTC start timestamp.

## Inputs (verify pinned sha256 before use; on mismatch, record in receipt and treat that input as unusable — fail closed)
- `p3-m3-rt-baseline/M3_ACCEPTANCE_BASELINE.md` — `d028f3c716cc123be1840170d6111c42e24693451c9d3bf90284fdb19691d433` (esp. its §4 prompt-contract recommendations and per-card reject-if checklists)
- `p3-m3-rt-baseline/RT_CARDS_DEEPENING.md` — `21564dd6d78c72483087d436f4256e461913ec9ab013c4ab7053bfe14eed7e18`
- `p3-m3-rt-baseline/P3_RECEIPT.md` — `70573e18df09cf45b73dcee5b75602541a6e33ea427dfa4b378c2f207eecd90b`
- Current `REQ_M3_RT_20260711T091128Z`: take its path from the P3 receipt / baseline citations. Prefer a hash-pinned copy in P3's `sources-snapshot/` if present; otherwise read the live file strictly read-only and record its sha256 in your receipt.

## Task (max effort — prefer exhaustive coverage over early finish)
P3 found `REQ_M3_RT_20260711T091128Z` lacks a completion-marker/section contract — the exact gap that sank cycle 7. Produce the full contract packet so the future supervised Gemini Web sidecar run (gated under `DUHO_GEMINI_WEB_WIKI_RESEARCH_ARTIFACT_SCOPE_20260711T004710Z`) is cheap to launch and adjudicate. One headline document with four sections: (a) complete revised REQ candidate text — verbatim, paste-ready, NOT applied anywhere — adding an explicit completion marker requirement and a per-card section contract for all six RT cards; (b) per-card adjudication scorecard mapped line-by-line to `M3_ACCEPTANCE_BASELINE.md` acceptance floors and reject-if checklists; (c) supervised-run checklist (operator steps, scope citation, evidence-capture and custody expectations); (d) precise diff summary: current REQ vs your candidate, each change justified from P3 findings.

## Deliverables (all in `<own>/`)
1. Headline: `GEMINI_SIDECAR_REQ_CONTRACT_PACKET.md` — top line marker `FABLE_HARD_BURN_H2_REQ_CONTRACT_20260711T035354Z`.
2. `H2_RECEIPT.md` — input custody results (pinned vs recomputed sha256; live-REQ sha256 if used), every produced file with bytes+sha256, poll log, safety attestation (explicit: no writes outside own subdir, no banned action, REQ not modified), status COMPLETE or PARTIAL, ending with the exact line `FABLE_HARD_BURN_H2_DONE_20260711T035354Z`.
3. 0-byte done marker `<own>/FABLE_HARD_BURN_H2_DONE_20260711T035354Z` — write it when you finish or stop for any reason; the receipt status carries COMPLETE/PARTIAL.

Stretch (only if core is complete inside cap): a failure-mode playbook — for every reject-if trigger, the concrete operator response (re-prompt, discard card, escalate).
