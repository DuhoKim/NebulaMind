# P2 brief — Cycle-7 rejected-report source-lead ledger, AGN–SFR status/debate map, prior-work comparison candidate

Marker: `HWAO_FABLE_BURN_P2_BRIEF_20260711T010503Z`
Issued: 2026-07-11 ≈01:28Z by Hwao (coordinator). Relayed by Tori, file handoff only.
Lane: **Lana Fable lane B** (one Claude/Fable pane, parallel with P1). Supervision: Tori (meter, stop/hold files, custody/hash checks), Hwao (verdict-wording review).
Authorization: Duho `approve fable burn 20260711T010503Z` → `HWAO_FABLE_BURN_EXECUTION_ACCEPTED_20260711T010503Z` (this directory).

This brief is self-contained. If anything you find on disk conflicts with it, the safety boundaries in §7 win; note the conflict in your receipt.

## 1. Mission

A Gemini Web deep-research report for RP-1's cycle 7 (34.8 KB) was **rejected** — verdict `REJECTED_RETAIN_VERIFIED_SOURCE_LEADS_ONLY` — with five source leads retained and 26 marked `UNCITED_NOT_USABLE`, all pending a later locally-directed verification pass. Meanwhile the cycle audits keep failing the same quality blocker: `missing explicit quantitative comparison to prior work`.

Your packet converts that rejected report into fail-closed research assets, **from on-disk materials only** (no network): a complete lead-by-lead ledger, a reader-facing AGN–sSFR research-status/debate map, and a candidate "quantitative comparison to prior work" section built only on locally supported numbers.

## 2. Write scope (your ONLY writable directory)

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/p2-cycle7-source-ledger/`

Create it (`mkdir -p`) as your first action. Everything else on this machine is read-only to you.

## 3. Sources (read-only, absolute paths)

Mastermind root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/`

- Integration verdict: `gemini-web-deep-research/integrations/JOURNAL_CYCLE7_GEMINI_WEB_20260710T232711Z_INTEGRATION.md`
- Tori preliminary review: `gemini-web-deep-research/integrations/JOURNAL_CYCLE7_GEMINI_WEB_20260710T232711Z_TORI_PRELIMINARY.md`
- Raw + corrected report materials (with hashes), all under `gemini-web-deep-research/outputs/JOURNAL_CYCLE7_GEMINI_WEB_20260710T232711Z/`:
  `CAPTURE_STATUS.json`, `GEMINI_WEB_OUTPUT.md`, `GEMINI_WEB_OUTPUT.meta.json`, `GEMINI_WEB_OUTPUT.links.json`, `GEMINI_WEB_OUTPUT_CORRECTED.md`, `GEMINI_WEB_OUTPUT_CORRECTED.chat.md`, `GEMINI_WEB_OUTPUT_CORRECTED.meta.json`, `GEMINI_WEB_OUTPUT_CORRECTED.links.json`, `GEMINI_WEB_OUTPUT_CORRECTED.acceptance.json`
- Wording contract: `HWAO_GEMINI_WEB_VERDICT_20260711T000400Z.md` — read the full contract there; the two rules you must apply everywhere: **no "establishes"** (or equivalent causal/settled verbs) and **non-commensurable absolute quantities must be labeled as such**.
- RP-1's own estimand ground truth (read-only; live runner tree — copy what you cite into your dir first):
  `aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex` (supplement beside it under `supplementary_denominator_atlas/aastex/` if needed)

Recon facts to re-verify against the files (not trust): the five retained leads are Ellison et al. 2016 (`−0.06 dex`); Cid Fernandes arXiv:1012.4426 (WHAN, `W_Hα = 3 Å`); Gawade arXiv:2512.22268 (TNG/EAGLE medians); Simard VizieR `J/ApJS/196/11`; SDSS-V SPIDERS. RP-1's estimand: association-only, morphology-uncontrolled, fiber-centered, `−1.309 dex`, 95% CI `[-1.334,-1.283]`.

Recommended: snapshot the files you quote into `p2-cycle7-source-ledger/sources-snapshot/` and record `shasum -a 256` for each in your receipt (Tori runs custody/hash checks on this packet).

## 4. Deliverables (exact filenames, in your write dir)

1. **`SOURCE_LEAD_LEDGER.json`** — **every** lead in the rejected report: the 5 retained, the 26 `UNCITED_NOT_USABLE`, and any others you find in the raw/corrected outputs. Required fields per entry: `lead_id`, `source_ref` (as the report gives it), `exact_claim` (verbatim quantity/statement the report attributes to it), `classification` ∈ `VERIFIED_LOCAL` | `NEEDS_NETWORK_VERIFICATION` | `REJECTED`, `local_basis` (the exact locally-checkable file + line supporting it — or `null` with reason), `network_pass_must_confirm` (precisely what a later approved network pass has to check), `notes`. Top-level: `marker: "FABLE_BURN_P2_SOURCE_LEAD_LEDGER_20260711T010503Z"`, source-file sha256 map, counts per classification. **Classification is fail-closed: anything not fully checkable on local disk is `NEEDS_NETWORK_VERIFICATION` or `REJECTED`, never `VERIFIED_LOCAL`. You perform zero network fetches.**
2. **`AGN_SFR_STATUS_DEBATE_MAP.md`** — reader-facing research-status/debate map for the AGN–sSFR association question. Bind RP-1's own estimand (association-only, morphology-uncontrolled, fiber-centered, `−1.309 dex`, CI `[-1.334,-1.283]` — quote these verbatim from the cycle-5 tex, character-for-character; cycles 6/7 corrupted this exact CI by regenerating it) against the retained external leads. Apply the wording contract throughout: no "establishes"; label non-commensurable absolute quantities; carry each lead's verification status inline.
3. **`PRIOR_WORK_COMPARISON_CANDIDATE.md`** — a candidate "quantitative comparison to prior work" section targeting the recurring cycle-audit blocker. Only leads whose numbers are locally supported; every row flagged with its ledger verification status; RP-1 numerals verbatim from cycle-5 tex. Mark it clearly as a candidate/reference block — it is NOT to be placed in any `candidates/` tree by you or anyone without a separate integrator approval.
4. **`P2_RECEIPT.md`** — see §8.
5. On full completion only: empty marker file named exactly `FABLE_BURN_P2_DONE_20260711T010503Z`.

Priority under time pressure: ledger → status/debate map → comparison candidate.

## 5. First action (ACK)

`mkdir -p` your write dir, then write `P2_ACK.md` containing: the line `FABLE_BURN_P2_ACK_20260711T010503Z`, your ACK timestamp UTC (this is your T0_lane), your tmux pane id, and the brief marker you received (`HWAO_FABLE_BURN_P2_BRIEF_20260711T010503Z`).

## 6. Timeline and stop conditions

- Target: T0_lane + 60 min. Hard overrun cap: T0_lane + 120 min → write partial receipt and stop.
- Absolute stops, whichever comes first:
  1. `GLOBAL_STOP_20260711T010503Z.md` exists at the burn root (`fable-weekly-burn-20260711T010503Z/`);
  2. your clock ≥ **2026-07-11T03:50:00Z**;
  3. hard overrun cap reached.
- Poll the burn root between artifacts and at least every ~15 min for `GLOBAL_STOP_20260711T010503Z.md` and `HOLD_5H_20260711T010503Z.md`.
- `HOLD_5H` present → finish only the artifact in progress, write receipt with status `HELD_5H`, stop. Tori re-relays continuation after the 5-hour reset.
- Any stop before completion → receipt status `PARTIAL` (or `HELD_5H`/`BLOCKED`), final line `FABLE_BURN_P2_PARTIAL_20260711T010503Z`, and NO done marker file.
- Done early → stop immediately. Do not invent extra work.

## 7. Safety boundaries (absolute — crossing any of these ends the packet)

1. **Write scope:** create/modify files ONLY inside `p2-cycle7-source-ledger/`. Everything else — the burn root, `briefs/`, `METER_LOG.md`, other `p*` dirs, the sprint tree, the repo — is read-only to you.
2. **Runner isolation:** the sprint tree `ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/` is live and runner-owned: never write there, never write into any `candidates/` tree, never promote anything, never touch/signal/patch/kill PID 45665 or any other process.
3. **No network:** no browser or browser automation, no WebFetch/WebSearch, no curl/wget or package installs, no ADS/arXiv/VizieR/SDSS lookups, no MCP network tools. Every lead needing the network is classified `NEEDS_NETWORK_VERIFICATION` in the ledger — resolving them is a later, separately-approved pass.
4. **No product/state mutation:** no DB/SQL, no API calls (incl. `/api/pages`, page_versions), no live wiki publication, no deploy/restart, no service changes.
5. **No git:** no add/commit/push/branch/tag/stash — not even for your own artifacts.
6. **No scheduling/daemons:** no cron, launchd, background jobs, or new monitors.
7. **No credentials/billing/cloud:** no OAuth/API-key/credential access, no reading `.env*` or secret files, no billing/account/`/credits` actions, no gcloud/GCP/cloud CLIs.
8. **No pane interference:** no tmux send-keys of any free text to any pane; do not interact with other panes; the unsent composer text in `ge-mastermind:0.0` must not be disturbed. You communicate only via files in your own write dir.
9. **Fail closed:** if a step seems to require crossing any line above, don't — record the conflict in the receipt and continue with what is allowed, or stop with status `BLOCKED`.

Allowed tooling: local read-only text processing (`grep -n`, `diff`, `awk`, `wc`, `shasum -a 256`, etc.) plus file writes inside your write dir.

## 8. Receipt spec (`P2_RECEIPT.md`)

- `status:` COMPLETE | PARTIAL | HELD_5H | BLOCKED
- `t_ack` / `t_end` (UTC), pane id
- Artifact table: filename, byte size, sha256
- Source table: every file read, absolute path, sha256 (Tori cross-checks these)
- Ledger counts: total leads, per-classification counts (VERIFIED_LOCAL / NEEDS_NETWORK_VERIFICATION / REJECTED)
- Deviations from this brief (should be none) and any ambiguity you resolved, with the choice made
- Follow-up queue, each line labeled `GATED — needs separate Duho approval` (at minimum: the network verification pass over `NEEDS_NETWORK_VERIFICATION` leads; integrator handoff of the comparison candidate)
- Coordination-file checks performed (timestamps, result)
- Final line: exactly `FABLE_BURN_P2_DONE_20260711T010503Z` (complete) or `FABLE_BURN_P2_PARTIAL_20260711T010503Z` (anything less)

`HWAO_FABLE_BURN_P2_BRIEF_20260711T010503Z`
