# DIRECTION — Pilot resume with deliberate Gemini leverage
Handoff ID: `pilot-gemini-resume-20260711T050514Z` · Author: Hwao (coordinator only) · UTC anchor: 20260711T050514Z

## 1. Objective
Return to the original 48-hour research-journal pilot and deliberately leverage the two idle Gemini quota pools while the Claude runner continues untouched:

- **Workstream A — Goru / Gemini CLI (Antigravity):** fresh read-only analysis lane producing a substantial offline blocker/debate-map/repair-priority artifact for the cycle-9 audit rejection. Brief: `CLI_BRIEF.md`.
- **Workstream B — Gemini Web (AI Ultra), supervised operator run:** one advisory-only Deep Research run of the r2 six-card M3 prompt (hard-burn H2 contract), explicitly approved by Duho now. Packet: `WEB_OPERATOR_PACKET.md`.

Both are sidecars. Neither touches the runner, candidates, or SPRINT_STATUS. Their outputs are advisory inputs to the next writer-slot brief only after fail-closed adjudication.

## 2. Live state snapshot (operator-supplied by Duho at 20260711T050514Z; not re-verified by Hwao)
- Runner PID **45665** healthy. SPRINT_STATUS: **cycle 9, discussion, waiting_next_phase, 33.57%**, next slot ~**43 min** from snapshot (≈05:48Z), last clean cycle **5**.
- Cycle-9 audit: **builds but rejects** on missing invariants **`249,917`** and **`24.0`**, plus gates: **prior-work comparison, length, equations, tables, operator-prose, warnings**.
- Quota: Antigravity Gemini **1% of 5h used, 7% weekly used**; Gemini Web AI Ultra **1% app compute used**. Both pools have large headroom — the point of this resume is to spend them deliberately.

## 3. T0 safety locks — ALL PRESERVED (restated, binding on both workstreams)
1. Runner PID 45665 untouched: no signals, restarts, env or config changes. SPRINT_STATUS, runner state, and candidate/journal directories are **read-only** for every lane in this handoff.
2. All writes from this handoff confined to `pilot-gemini-resume-20260711T050514Z/` (CLI lane → `cli/`, web operator → `web/`). Temp files stay inside the lane dir as `_tmp_*`.
3. External-model output (Gemini CLI or Web) is **advisory only**: never evidence, never pasted into candidates, never claim/cite binding. Fail-closed adjudication before it influences any writer slot.
4. All externally supplied citations/IDs are `QUARANTINED_PENDING_LOCAL_CHECK` until the gated Tori verification pass. No numeric imports without local support.
5. Web runs are supervised-only, single conversation, with explicit per-run Duho approval. **Approval for exactly one run is granted now** (Duho direction, 20260711T050514Z). No unattended runs, no account/billing/extension changes, no purchases, no /credits or paid-quota actions without per-step user approval.
6. Quota guardrails: CLI lane caps at ≤40% of the Antigravity 5h window; web operator aborts preflight at ≥80% app compute or any billing/upsell interstitial. Usage logged before/after in receipts.
7. Secrets hygiene: no `.env`/secret material in prompts, captures, receipts, or packets.
8. Quintet role-table protocol: no solo lanes — Hwao coordinates only and does not self-dispatch; lanes ACK per protocol before substantive work; the web run is the **one** supervised Ultra-style second opinion for this resume.

## 4. Deliverables map
| Item | Path (relative to this handoff root) |
|---|---|
| This direction | `DIRECTION.md` |
| Goru CLI lane brief | `CLI_BRIEF.md` |
| Web operator packet (incl. embedded r2 paste text) | `WEB_OPERATOR_PACKET.md` |
| CLI analysis artifact + receipt + done marker | `cli/GORU_CYCLE9_BLOCKER_DEBATE_REPAIR_ANALYSIS.md`, `cli/GORU_CLI_RECEIPT.md`, `cli/GORU_PILOT_CLI_DONE_20260711T050514Z` |
| Web capture + adjudication + fail-closed markers | `web/answers/REQ_M3_RT_20260711T091128Z-r2-<UTC>/`, `web/ADJUDICATION_REQ_M3_RT_20260711T091128Z-r2.md`, `web/WEB_RUN_CAPTURED_20260711T050514Z` or `web/WEB_RUN_VOID_20260711T050514Z` |
| Hwao ready marker | `HWAO_PILOT_GEMINI_RESUME_READY_20260711T050514Z` |

## 5. Timing
Next runner slot ≈05:48Z. The CLI lane should aim to land its artifact ≤35 min after dispatch so repairs can inform the next writer-slot brief; if it misses the slot, the artifact applies to the following cycle — do not rush past the read-only and receipt requirements. The web run is operator-paced (Deep Research can take 10–20+ min); its output only ever enters via adjudication, whichever cycle that lands in. The runner proceeds autonomously regardless — nothing here gates or delays it.

## 6. Adjudication flow (both workstreams)
CLI artifact: quintet review of receipt + artifact before any repair from it is quoted into a writer-slot brief. Web capture: fail-closed adjudication per H2 contract §B (gates → floors → per-card CHKs → wholesale verdict), advisory ceiling always; accepted leads go to the Tori local-verification queue, nothing imports directly.

## 7. What Hwao did and did not do
Did: wrote the three packets + marker under this root; copied the r2 paste text verbatim from the H2 contract (`fable-weekly-hard-burn-20260711T035354Z/h2-gemini-req-contract/GEMINI_SIDECAR_REQ_CONTRACT_PACKET.md` §A, minus the OPERATOR-SIDE block, per its step R2). Did **not**: dispatch any lane, browse, run any analysis, touch the runner/candidates/SPRINT_STATUS/live REQ file, or modify anything outside this root.

## 8. Next actions (orchestrator / Duho)
1. Dispatch the fresh Goru/Antigravity lane with `CLI_BRIEF.md`.
2. Hand `WEB_OPERATOR_PACKET.md` to the human operator for the approved supervised run.
3. On completion markers, run adjudication/quintet review; fold accepted advisory items into the next writer-slot brief.
