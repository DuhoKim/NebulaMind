# P3 brief — M3 sidecar acceptance baseline + research-topic card deepening (local evidence only)

Marker: `HWAO_FABLE_BURN_P3_BRIEF_20260711T010503Z`
Issued: 2026-07-11 ≈01:28Z by Hwao (coordinator). Relayed by Tori ≈10 min after P1/P2, file handoff only.
Lane: **Lana Fable lane C** (one Claude/Fable pane). Supervision: Tori (meter, stop/hold files, custody), Hwao (receipt review).
Authorization: Duho `approve fable burn 20260711T010503Z` → `HWAO_FABLE_BURN_EXECUTION_ACCEPTED_20260711T010503Z` (this directory).

This brief is self-contained. If anything you find on disk conflicts with it, the safety boundaries in §7 win; note the conflict in your receipt.

## 1. Mission

The M1/M3 usage-surge rollup is complete except for one open dependency: a supervised Gemini Web sidecar run over six research-topic cards (`REQ_M3_RT_20260711T091128Z`). The cycle-7 lesson: a Gemini report evaluated **without a pre-agreed local acceptance baseline** cost a full supervised run (it came back and was rejected wholesale). Your packet makes the pending M3 sidecar run fail-closed and cheap to adjudicate — a per-card acceptance baseline the sidecar's answers will be checked against — and independently deepens the six reader-facing RT cards from local evidence alone.

**This packet prepares for the sidecar run; it does not perform, request, or schedule it.** The run itself stays separately gated under its own protocol chain (`DUHO_GEMINI_WEB_WIKI_RESEARCH_ARTIFACT_SCOPE_20260711T004710Z`).

## 2. Write scope (your ONLY writable directory)

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/p3-m3-rt-baseline/`

Create it (`mkdir -p`) as your first action. Everything else on this machine is read-only to you.

## 3. Sources (read-only, absolute paths)

- The M3 request (six research-topic cards):
  `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-deep-research/requests/RT_GEMINI_WEB_REQUEST_M3_20260711T091128Z.md`
- Local evidence basis (anchors `#s2`–`#s8`) — note it lives OUTSIDE the mastermind tree:
  `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/static-publish-20260709T124353Z/live-root-before/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md`
- RT artifacts referenced from within the request file: follow those references on **local disk only**. If a referenced path does not exist locally, record it as a gap in your receipt — do not fetch anything.
- Cycle-7 lesson (what a sidecar answer gets rejected for), read both:
  `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-deep-research/integrations/JOURNAL_CYCLE7_GEMINI_WEB_20260710T232711Z_INTEGRATION.md`
  `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/HWAO_GEMINI_WEB_VERDICT_20260711T000400Z.md` (wording contract: no "establishes"; non-commensurable absolute quantities labeled; uncited leads are not usable)
- Context only: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot/DIRECTOR_FINAL_ROLLUP_RUTHLESS_USAGE_SURGE_20260711T002524Z.md`

Recommended: snapshot the request file and the `#s2`–`#s8` sections you rely on into `p3-m3-rt-baseline/sources-snapshot/` and record `shasum -a 256` of each source in your receipt.

## 4. Deliverables (exact filenames, in your write dir)

1. **`M3_ACCEPTANCE_BASELINE.md`** — for **each of the six cards** in the request:
   - the local evidence basis (specific claims from `evidence-basis-20260708T014205Z.md#s2–#s8` and the RT artifacts, cited by anchor/file+line);
   - the claims a Gemini sidecar answer **must not contradict** (the fail-closed floor);
   - a per-card acceptance checklist mirroring the cycle-7 lesson: exact completion-marker placement, banned verbs (no "establishes" or equivalent causal/settled phrasing), uncited-lead labeling (`UNCITED_NOT_USABLE` unless the answer carries a checkable citation), non-commensurable absolute quantities labeled, and any card-specific pass/fail checks.
   Top line marker: `FABLE_BURN_P3_ACCEPTANCE_BASELINE_20260711T010503Z`. Structure it so a later adjudicator can score a sidecar answer card-by-card without re-deriving anything.
2. **`RT_CARDS_DEEPENING.md`** — Fable-side deepening of each card, independent of (and later cross-checkable against) the future sidecar output: tightened decision criteria, falsifiable predictions, overclaim risks, and what local evidence already answers. Local evidence only; where a question genuinely needs the network, say so explicitly and mark it for the gated sidecar/network pass rather than speculating.
3. **`P3_RECEIPT.md`** — see §8.
4. On full completion only: empty marker file named exactly `FABLE_BURN_P3_DONE_20260711T010503Z`.

Priority under time pressure: acceptance baseline → deepening. A complete baseline for all six cards beats a deep treatment of three.

## 5. First action (ACK)

`mkdir -p` your write dir, then write `P3_ACK.md` containing: the line `FABLE_BURN_P3_ACK_20260711T010503Z`, your ACK timestamp UTC (this is your T0_lane), your tmux pane id, and the brief marker you received (`HWAO_FABLE_BURN_P3_BRIEF_20260711T010503Z`).

## 6. Timeline and stop conditions

- Target: T0_lane + 55 min. Hard overrun cap: T0_lane + 110 min → write partial receipt and stop.
- Absolute stops, whichever comes first:
  1. `GLOBAL_STOP_20260711T010503Z.md` exists at the burn root (`fable-weekly-burn-20260711T010503Z/`);
  2. your clock ≥ **2026-07-11T03:50:00Z**;
  3. hard overrun cap reached.
- Poll the burn root between artifacts and at least every ~15 min for `GLOBAL_STOP_20260711T010503Z.md` and `HOLD_5H_20260711T010503Z.md`.
- `HOLD_5H` present → finish only the artifact in progress, write receipt with status `HELD_5H`, stop. Tori re-relays continuation after the 5-hour reset.
- Any stop before completion → receipt status `PARTIAL` (or `HELD_5H`/`BLOCKED`), final line `FABLE_BURN_P3_PARTIAL_20260711T010503Z`, and NO done marker file.
- Done early → stop immediately. Do not invent extra work.

## 7. Safety boundaries (absolute — crossing any of these ends the packet)

1. **Write scope:** create/modify files ONLY inside `p3-m3-rt-baseline/`. Everything else — the burn root, `briefs/`, `METER_LOG.md`, other `p*` dirs, the sprint tree, the repo — is read-only to you.
2. **Runner isolation:** the sprint tree `ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/` is live and runner-owned: never write there, never write into any `candidates/` tree, never promote anything, never touch/signal/patch/kill PID 45665 or any other process.
3. **No network:** no browser or browser automation, no WebFetch/WebSearch, no curl/wget or package installs, no ADS/arXiv/VizieR/SDSS lookups, no MCP network tools. **Explicitly: you do not run, trigger, or request the Gemini sidecar** — it has its own gated protocol chain.
4. **No product/state mutation:** no DB/SQL, no API calls (incl. `/api/pages`, page_versions), no live wiki publication, no deploy/restart, no service changes.
5. **No git:** no add/commit/push/branch/tag/stash — not even for your own artifacts.
6. **No scheduling/daemons:** no cron, launchd, background jobs, or new monitors.
7. **No credentials/billing/cloud:** no OAuth/API-key/credential access, no reading `.env*` or secret files, no billing/account/`/credits` actions, no gcloud/GCP/cloud CLIs.
8. **No pane interference:** no tmux send-keys of any free text to any pane; do not interact with other panes; the unsent composer text in `ge-mastermind:0.0` must not be disturbed. You communicate only via files in your own write dir.
9. **Fail closed:** if a step seems to require crossing any line above, don't — record the conflict in the receipt and continue with what is allowed, or stop with status `BLOCKED`.

Allowed tooling: local read-only text processing (`grep -n`, `diff`, `awk`, `wc`, `shasum -a 256`, etc.) plus file writes inside your write dir.

## 8. Receipt spec (`P3_RECEIPT.md`)

- `status:` COMPLETE | PARTIAL | HELD_5H | BLOCKED
- `t_ack` / `t_end` (UTC), pane id
- Artifact table: filename, byte size, sha256
- Source table: every file read, absolute path, sha256; any referenced-but-missing local paths listed as gaps
- Card coverage: which of the six cards have a complete baseline entry and a complete deepening entry
- Deviations from this brief (should be none) and any ambiguity you resolved, with the choice made
- Follow-up queue, each line labeled `GATED — needs separate Duho approval` (at minimum: the supervised Gemini sidecar run itself; any network verification the deepening surfaced)
- Coordination-file checks performed (timestamps, result)
- Final line: exactly `FABLE_BURN_P3_DONE_20260711T010503Z` (complete) or `FABLE_BURN_P3_PARTIAL_20260711T010503Z` (anything less)

`HWAO_FABLE_BURN_P3_BRIEF_20260711T010503Z`
