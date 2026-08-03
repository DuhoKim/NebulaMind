# Hard-burn director acceptance — Hwao

`HWAO_FABLE_HARD_BURN_ACCEPTED_20260711T035354Z`

- T0: `TORI_FABLE_WEEKLY_HARD_BURN_T0_20260711T035354Z` (`T0.md`, 2026-07-11T03:53:54Z). Directive: "not much used, burn it harder"; "you have 1 hour left". Absolute stop `2026-07-11T04:50:00Z` or weekly reset.
- Source: prior rollup `HWAO_FABLE_WEEKLY_BURN_ROLLUP_COMPLETE_20260711T010503Z` §6 follow-up queue. All five lanes are the offline, no-gate portions of that queue; no gated action (network, Gemini run, runner/manuscript writes, DB/API/wiki writes) is authorized by these briefs.

## Briefs (in `briefs/`, one lane each, mutually independent, disjoint write areas)

| Lane | Brief | Task | Queue item |
|---|---|---|---|
| H1 | `H1_BRIEF.md` | Unified network-verification workplan (39 P2 leads + EXT-1…4 + P3 per-card + P4 enrichment, deduped, prioritized) | 1 (offline prep) |
| H2 | `H2_BRIEF.md` | Gemini sidecar REQ prompt-contract packet (revised REQ candidate + adjudication scorecard vs M3 baseline) | 2 (offline prep) |
| H3 | `H3_BRIEF.md` | Runner/manuscript integration change-packet (audit-list extension, verbatim-carry patch text, canon adjudication memo — nothing applied) | 3 (offline prep) |
| H4 | `H4_BRIEF.md` | Wiki/DB integration dry-run plan for all 13 P4 candidates (payloads per `wiki_schema.md`; no DB contact) | 4 (offline prep) |
| H5 | `H5_BRIEF.md` | Value-level verification of the remaining seven topic artifacts vs supplement prose (fully offline execution) | 5 (direct) |

## Common lane contract (stated in every brief)
- Writes confined to the lane's own subdir under this hard-burn root; everything else read-only.
- 40-minute cap from ACK and absolute stop 04:50:00Z; final 5 minutes reserved for receipt + marker.
- Polls `GLOBAL_STOP_20260711T035354Z.md` / `HOLD_5H_20260711T035354Z.md` at root, ≥ every 5 min, logged in receipt.
- One substantial headline artifact with top marker, `Hx_RECEIPT.md` (custody hashes, output hashes, poll log, safety attestation, COMPLETE/PARTIAL), 0-byte done marker `FABLE_HARD_BURN_Hx_DONE_20260711T035354Z`.
- T0 safety boundary verbatim and binding: safe offline artifacts only — no network/browser, runner/candidate writes, DB/API/wiki publication, deploy/restart, git, cron/launchd/background jobs, billing/account/credentials, cloud/GCP. Runner PID 45665 untouched.
- Inputs hash-pinned from the prior rollup; fail closed on mismatch.

## Coordinator attestation
Hwao performed no new reconnaissance and no packet work. Only writes: the five briefs and this file, all under `briefs/`. **No lane dispatched** — dispatch awaits Duho/Tori per protocol.
