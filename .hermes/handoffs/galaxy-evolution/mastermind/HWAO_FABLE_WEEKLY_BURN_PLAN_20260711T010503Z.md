# Hwao plan — productive Fable weekly-quota burn before reset

Marker: `HWAO_FABLE_WEEKLY_BURN_PLAN_READY_20260711T010503Z`
Brief: `HWAO_FABLE_WEEKLY_BURN_PLAN_BRIEF_20260711T010503Z.md` (`HWAO_PLAN_FABLE_WEEKLY_BURN_BEFORE_RESET_20260711T010503Z`)
Written: 2026-07-11T01:20Z by Hwao (director). Read-only recon only; no lane dispatched, no burn work started.

**This is a plan. Nothing below executes until Duho approves.** Suggested approval phrase:
`approve fable burn 20260711T010503Z` (optionally listing packet IDs to include/exclude).

## 1. Window and usage facts

- Brief-time meter (local Claude OAuth usage monitor, fetched 2026-07-11T01:04:54Z): Fable 5-hour `9%` (reset ≈ 2 h → ≈ 03:05Z); Fable weekly `5%` (reset ≈ 3 h → ≈ 04:05Z). 18 active Claude/Fable/Lana panes.
- Effective burn window: approval time (T0) → **hard stop 2026-07-11T03:50Z** (15 min before weekly reset). If approval lands late, packets drop in priority order P1 > P2 > P3 (P4 first).
- `.hermes/logs/provider-usage-monitor.log` is stale (last snapshot 2026-07-10T12:27:14Z, pane counts only, no Fable quota fields). It may be used for pane census only; quota checkpoints use the same on-demand OAuth usage fetch that produced the brief numbers. No cron/launchd.

## 2. Read-only findings the plan is built on (evidence paths)

All paths below are relative to `.hermes/handoffs/galaxy-evolution/mastermind/` unless absolute.

1. **RP-1 weekend journal sprint is burning cycles on one reproducible integrity failure.**
   `aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/SPRINT_STATUS.json`: cycle 7 complete, state `waiting_next_phase`, heartbeat 01:08:20Z fresh, PID 45665 healthy, next slot ≈ 01:46:31Z (cycle 8). Ledger: cycles 02, 03, 06, 07 all integrity-fatal; cycle 5 remains the last clean candidate.
   - Cycle 6 audit (`candidates/cycle_06_package/CYCLE_06_literature_AUDIT.json`) and cycle 7 audit (`candidates/cycle_07_package/CYCLE_07_introduction_AUDIT.json`) fail on the identical blocker: `numeric_invariants_missing: ["[-1.334,-1.283]"]`.
   - Recon smoking gun: cycle 5 tex (`candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex` lines 13, 57, 65, 74) carries the bootstrap 95% CI `[-1.334,-1.283]`; cycles 6 **and** 7 both carry `[-1.334,-1.282]` in all four locations. Cycle 7 was rebuilt from clean cycle 5, so the corruption is **reintroduced by the prose-phase rewrite itself** — the lane regenerates numbers from memory instead of carrying them verbatim. Same one-digit drift, twice, in every occurrence.
   - Both audits also repeat the same quality blockers, notably `missing explicit quantitative comparison to prior work`, word-count targets, and `workflow/operator safety prose remains in manuscript`.
2. **Cycle-7 Gemini Web report was rejected; a local verification pass was explicitly deferred to Hwao.**
   `gemini-web-deep-research/integrations/JOURNAL_CYCLE7_GEMINI_WEB_20260710T232711Z_INTEGRATION.md`: verdict `REJECTED_RETAIN_VERIFIED_SOURCE_LEADS_ONLY`. Five leads retained (Ellison et al. 2016 `−0.06 dex`; Cid Fernandes arXiv:1012.4426 WHAN `W_Hα = 3 Å`; Gawade arXiv:2512.22268 TNG/EAGLE medians; Simard VizieR `J/ApJS/196/11`; SDSS-V SPIDERS) plus 26 `UNCITED_NOT_USABLE` leads, all pending "a later Hwao-directed local ADS/full-source pass." Raw materials with hashes are on disk under `gemini-web-deep-research/outputs/JOURNAL_CYCLE7_GEMINI_WEB_20260710T232711Z/`.
3. **M1/M3 are complete and waiting only on the supervised Gemini sidecar.**
   `autopilot/DIRECTOR_FINAL_ROLLUP_RUTHLESS_USAGE_SURGE_20260711T002524Z.md`: all Goru surge briefs and method verdicts landed; sole open dependency is `REQ_M3_RT_20260711T091128Z` (`gemini-web-deep-research/requests/RT_GEMINI_WEB_REQUEST_M3_20260711T091128Z.md`) — six research-topic cards, local evidence anchors `evidence-basis-20260708T014205Z.md#s2–#s8`, Gemini output advisory-only and must be locally checked before use.
4. **No other unfinished pool competes.** Wiki quality sprint continuation has its final completion receipt (`wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/FINAL_WIKI_QUALITY_SPRINT_COMPLETION_RECEIPT.md`). `docs/baseline_step9e_*` ends at a DB-write approval packet — hard-gated, not burnable. Autopilot status: 0 blockers, all hard gates closed.

## 3. Why this work is Fable work

Chosen packets are estimand-wording, numeric-integrity, and evidence-adjudication reasoning — the exact failure class that already slipped past mechanical checks (compile passed while a digit silently drifted). Routed elsewhere deliberately: TeX overfull/underfull cleanup and strict recompiles → Kun/Codex; format/word-count/schema audits → Goru/Gemini; the Gemini sidecar run itself → Tori's supervised protocol (Gemini quota, separately gated). No new projects are invented; every packet continues an in-flight thread.

## 4. Work packets (3 core + 1 conditional stretch)

Burn root (new, outside the runner-owned sprint tree): `.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/`
The runner's `ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/` tree is **read-only** for all burn lanes; PID 45665 is not touched, signaled, or patched.

### P1 — RP-1 numeric-invariant root-cause + invariant manifest + verbatim-carry reference (highest value, time-sensitive)

- **Owner:** Lana Fable lane A (one Claude/Fable pane). Tori relays. Optional non-Fable cross-check: Kun/Codex strict recompile of the reference block (Codex quota, skip if busy).
- **Work:** (a) Confirm and document the full drift story: diff every numeric invariant between `cycle_05_package` and cycles 06/07 tex (not just the known interval — enumerate all numerals, N counts, dex values, CI bounds). (b) Write `INVARIANT_MANIFEST.json`: every numeric invariant in the clean cycle 5 flagship+supplement with file, line, exact string, and allowed context. (c) Write `RCA_NUMERIC_DRIFT.md`: why prose phases reintroduce `-1.282` from a clean `-1.283` base (regeneration-not-copy failure), with the verbatim-carry rule the phase lanes must follow. (d) Produce `INTRODUCTION_LITERATURE_REFERENCE.md`: an invariant-safe reference text block (introduction + literature deltas built strictly on cycle 5 wording) that future pilot lanes can check candidates against. Reference material only — no writes into `candidates/`, no promotion, no runner interaction.
- **Artifacts:** `fable-weekly-burn-20260711T010503Z/p1-rp1-invariants/{RCA_NUMERIC_DRIFT.md, INVARIANT_MANIFEST.json, INTRODUCTION_LITERATURE_REFERENCE.md, P1_RECEIPT.md}`
- **Expected value:** cycles 6 and 7 each burned a ~2 h runner slot on this exact failure; cycle 8 (≈ 01:46:31Z) rebuilds from cycle 5 and will plausibly repeat it. This packet converts the loop from "fail, restart" to "checkable against a manifest," and is reusable for every later prose phase.
- **ETA:** T0 + 75 min. **Stop:** all four artifacts + done marker `FABLE_BURN_P1_DONE_20260711T010503Z` written, or 2× ETA overrun → write partial receipt and stop, or global meter stop.

### P2 — Cycle-7 rejected-report source-lead ledger + AGN–SFR status/debate map + quantitative prior-work comparison candidate

- **Owner:** Lana Fable lane B (second Claude/Fable pane), parallel with P1. Hwao reviews verdict wording. Tori custody/hash checks.
- **Work:** From on-disk materials only (raw + corrected Gemini outputs, acceptance JSON, Tori preliminary review): (a) `SOURCE_LEAD_LEDGER.json` — every lead in the rejected report classified `VERIFIED_LOCAL` / `NEEDS_NETWORK_VERIFICATION` / `REJECTED`, with the exact claim, the exact locally-checkable basis, and what a later network pass must confirm. No network fetches in this packet. (b) `AGN_SFR_STATUS_DEBATE_MAP.md` — reader-facing research-status/debate map for the AGN–sSFR association question, binding RP-1's own estimand (association-only, morphology-uncontrolled, fiber-centered, `−1.309 dex`, CI `[-1.334,-1.283]`) against the retained external leads, with the wording contract from `HWAO_GEMINI_WEB_VERDICT_20260711T000400Z.md` (no "establishes"; non-commensurable absolute quantities labeled). (c) `PRIOR_WORK_COMPARISON_CANDIDATE.md` — a candidate "quantitative comparison to prior work" section (the recurring cycle audit quality blocker), using only leads whose numbers are locally supported, each row flagged with its verification status.
- **Artifacts:** `fable-weekly-burn-20260711T010503Z/p2-cycle7-source-ledger/{SOURCE_LEAD_LEDGER.json, AGN_SFR_STATUS_DEBATE_MAP.md, PRIOR_WORK_COMPARISON_CANDIDATE.md, P2_RECEIPT.md}`
- **Expected value:** converts a rejected 34.8 KB report into fail-closed research assets; directly targets the audits' `missing explicit quantitative comparison to prior work` blocker; the status/debate map is mission-line output (papers → status/debate map → reader-facing artifact → derived claims) reusable for both the manuscript and wiki research topics.
- **ETA:** T0 + 60 min. **Stop:** artifacts + `FABLE_BURN_P2_DONE_20260711T010503Z`, or 2× ETA overrun → partial receipt, or global meter stop.

### P3 — M3 sidecar acceptance baseline + research-topic card deepening (local evidence only)

- **Owner:** Lana Fable lane C (third Claude/Fable pane), start T0 + 10 min (staggered so Tori relays briefs sequentially). Optional non-Fable: Goru mechanical format audit (Gemini quota, skip if Gemini headroom is needed elsewhere).
- **Work:** For each of the six research-topic cards in `REQ_M3_RT_20260711T091128Z`: (a) `M3_ACCEPTANCE_BASELINE.md` — the local evidence basis per card (from `evidence-basis-20260708T014205Z.md#s2–#s8` and the RT artifacts), the claims a Gemini sidecar answer must not contradict, and a per-card acceptance checklist (mirroring the cycle-7 lesson: exact completion-marker placement, banned verbs, uncited-lead labeling). (b) `RT_CARDS_DEEPENING.md` — Fable-side deepening of each card: tightened decision criteria, falsifiable predictions, overclaim risks, and what local evidence already answers — independent of, and later cross-checkable against, the sidecar output.
- **Artifacts:** `fable-weekly-burn-20260711T010503Z/p3-m3-rt-baseline/{M3_ACCEPTANCE_BASELINE.md, RT_CARDS_DEEPENING.md, P3_RECEIPT.md}`
- **Expected value:** the M3 sidecar is the only open dependency in the surge rollup; cycle 7 showed that a Gemini report without a pre-agreed local acceptance baseline costs a full supervised run. This packet makes the pending sidecar run fail-closed and cheap to adjudicate, and deepens reader-facing RT cards either way.
- **ETA:** T0 + 55 min (from its T0+10 start). **Stop:** artifacts + `FABLE_BURN_P3_DONE_20260711T010503Z`, or 2× ETA overrun → partial receipt, or global meter stop.

### P4 (conditional stretch) — derived claims/evidence candidates from clean cycle 5

- **Runs only if** P1–P3 are complete, the meter shows Fable weekly < 60% used, and it is not yet 03:15Z. Otherwise dropped without regret.
- **Owner:** whichever Lana Fable lane frees first. 30 min hard cap.
- **Work:** extract candidate claim/evidence pairs from the cycle 5 clean package (flagship + supplement) into offline wiki-shaped candidates (`wiki_schema.md` conventions), each with source line references and the association-only wording contract. Offline candidates only — no DB/API/wiki writes.
- **Artifacts:** `fable-weekly-burn-20260711T010503Z/p4-derived-claims/{CLAIM_EVIDENCE_CANDIDATES.md, P4_RECEIPT.md}` + `FABLE_BURN_P4_DONE_20260711T010503Z` marker.

### Order and parallelism

P1 and P2 start at T0 in parallel (two Fable panes); P3 at T0 + 10 min (third pane). P4 only under its condition. Hwao reviews each packet's receipt as it lands (director pane, review-only). Everything else among the 18 panes stays untouched; the unsent composer text in `ge-mastermind:0.0` is not disturbed; no tmux send-keys of free text (briefs hand off via files per standing protocol).

## 5. Meter / checkpoint cadence (existing monitor, no new jobs)

- **Instrument:** the same on-demand local Claude OAuth usage fetch that produced the brief's 01:04:54Z numbers, run by Tori. No cron/launchd, no new daemons. (`provider-usage-monitor.log` is stale and lacks Fable quota fields — pane census only.)
- **Cadence:** T0 preflight, every ~30 min, at each packet completion, and once at final rollup. Each reading appended as one line `{ts_utc, fable_5h_pct, fable_5h_reset, fable_weekly_pct, fable_weekly_reset, panes}` to `fable-weekly-burn-20260711T010503Z/METER_LOG.md`.
- **Thresholds:**
  - Fable 5-hour ≥ 80% before its ≈ 03:05Z reset → no new packet starts; in-flight lanes finish their current artifact, then hold until the 5-hour reset.
  - Weekly reset observed (weekly % drops) or clock ≥ 03:50Z → **global stop**: lanes write receipts, Tori takes a final meter reading, Hwao writes `BURN_ROLLUP.md`.
  - All selected packets complete early → **stop immediately.** Per the brief, quota is not spent to hit a number; leftover weekly quota simply resets. P4's condition is the only sanctioned stretch.

## 6. Startable immediately on Duho approval vs separately gated

**Starts on approval of this plan (nothing else):** P1, P2, P3 (and P4 under its stated condition); the meter cadence; all writes confined to `fable-weekly-burn-20260711T010503Z/` under `.hermes`.

**Remains separately gated — not authorized by this plan or its approval:**

- Any network fetch for `NEEDS_NETWORK_VERIFICATION` leads (ADS/arXiv/VizieR/SDSS pages) — queued in P2's ledger for a later explicitly-approved pass.
- The supervised Gemini Web sidecar run for `REQ_M3_RT_20260711T091128Z` (own protocol chain: Hwao scope → Tori fail-closed consumer-quota preflight `burn` → supervised run → verification, per `DUHO_GEMINI_WEB_WIKI_RESEARCH_ARTIFACT_SCOPE_20260711T004710Z`).
- Any integration of P1/P2 material into the runner's `candidates/` tree or any promotion decision (integrator lane, separate direction).
- DB/SQL, `/api/pages`/page_versions/live wiki publication, product mutation, deploy/restart, git actions, cron/launchd, browser automation, billing/account/OAuth/API-key/credential access, cloud/GCP. All remain closed per standing gates.

## 7. Rollup

On global stop, Hwao writes `fable-weekly-burn-20260711T010503Z/BURN_ROLLUP.md`: per-packet outcome (done / partial / dropped), artifact list with paths, final meter line, and the follow-up queue (network verification pass, sidecar run, integrator handoff) — each still gated on separate Duho approval.

---

Plan complete. No lane dispatched, no burn work executed, no runner interaction, no writes outside this plan file. Awaiting Duho's decision.

`HWAO_FABLE_WEEKLY_BURN_PLAN_READY_20260711T010503Z`
