# P1 brief — RP-1 numeric-invariant root cause, invariant manifest, verbatim-carry reference

Marker: `HWAO_FABLE_BURN_P1_BRIEF_20260711T010503Z`
Issued: 2026-07-11 ≈01:28Z by Hwao (coordinator). Relayed by Tori, file handoff only.
Lane: **Lana Fable lane A** (one Claude/Fable pane). Supervision: Tori (meter, stop/hold files, custody), Hwao (receipt review).
Authorization: Duho `approve fable burn 20260711T010503Z` → `HWAO_FABLE_BURN_EXECUTION_ACCEPTED_20260711T010503Z` (this directory).

This brief is self-contained. If anything you find on disk conflicts with it, the safety boundaries in §7 win; note the conflict in your receipt.

## 1. Mission

RP-1 is the flagship AGN–sSFR association manuscript in the galaxy-evolution program. An autonomous 48-hour journal sprint (runner process, PID 45665 — **not yours to touch**) rewrites it in cycles; integrity audits gate each cycle. Cycles 6 and 7 both failed on the identical blocker: a bootstrap 95% CI that reads `[-1.334,-1.283]` in the last clean package (cycle 5) came back as `[-1.334,-1.282]` after the prose-phase rewrite — the same one-digit drift, twice, in every occurrence, even though cycle 7 was rebuilt from clean cycle 5. Recon conclusion (yours to confirm): prose phases regenerate numbers from memory instead of carrying them verbatim.

Your packet converts this from "fail, restart" into "checkable against a manifest": document the drift, produce a machine-checkable invariant manifest of the clean cycle-5 numbers, write the root-cause + verbatim-carry rule, and produce an invariant-safe introduction/literature reference block for future prose lanes. **Reference material only — you fix nothing in the runner's tree.**

## 2. Write scope (your ONLY writable directory)

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/p1-rp1-invariants/`

Create it (`mkdir -p`) as your first action. Everything else on this machine is read-only to you.

## 3. Sources (read-only, absolute paths)

Sprint tree root (LIVE, runner-owned, strictly read-only):
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/`

Under it:
- Clean base (cycle 5):
  - `candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex`
  - `candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`
- Cycle 6: same two relative tex paths under `candidates/cycle_06_package/`, plus audit `candidates/cycle_06_package/CYCLE_06_literature_AUDIT.json`
- Cycle 7: same two relative tex paths under `candidates/cycle_07_package/`, plus audit `candidates/cycle_07_package/CYCLE_07_introduction_AUDIT.json`
- Context only (do not rely on it staying stable): `SPRINT_STATUS.json`

Recon facts to re-verify yourself (with `grep -n`, not trust): cycle 5 flagship carries `[-1.334,-1.283]` at lines 13, 57, 65, 74; cycles 6 and 7 flagship carry `[-1.334,-1.282]` at the same four locations; both audits fail `numeric_invariants_missing: ["[-1.334,-1.283]"]` and repeat quality blockers `missing explicit quantitative comparison to prior work`, word-count targets, and `workflow/operator safety prose remains in manuscript`.

**Snapshot first.** The runner's next cycle slot is ≈01:46:31Z and it writes into this tree. Before analysis, copy the eight source files above (6 tex + 2 audit JSON) into `p1-rp1-invariants/sources-snapshot/` preserving relative paths, record `shasum -a 256` of each in your receipt, and work exclusively from the snapshot so your line references stay stable. If a `cycle_08_package` appears mid-run, ignore it — out of scope.

## 4. Deliverables (exact filenames, in your write dir)

1. **`INVARIANT_MANIFEST.json`** — every numeric invariant in the clean cycle-5 flagship + supplement. Enumerate ALL numerals: point estimates, CI bounds, dex values, N counts, percentages, sample sizes — not just the known interval. Required fields per entry: `id`, `file` (path relative to `candidates/cycle_05_package/`), `line`, `exact_string`, `kind` (e.g. `ci_bound`/`point_estimate`/`count`/`dex`/`percent`/`other`), `allowed_context` (short surrounding phrase). Top-level: `marker: "FABLE_BURN_P1_INVARIANT_MANIFEST_20260711T010503Z"`, `base_package`, `snapshot_sha256` map. Add helpful extras (e.g. `occurrences_expected`) freely; do not omit required fields. Exclude non-invariant numerals (section numbers, years in citations) but say in the RCA what you excluded and why.
2. **`RCA_NUMERIC_DRIFT.md`** — (a) the full drift story: a table of every numeric invariant across cycle 5 vs 6 vs 7 (flagship + supplement), with per-cycle values, file:line, and drift flags — confirm or amend the four-location `-1.283 → -1.282` finding and catch any other drifts recon missed; (b) root cause: why prose phases reintroduce `-1.282` from a clean `-1.283` base (regeneration-not-copy failure), citing your diff evidence; (c) the **verbatim-carry rule** future phase lanes must follow (numbers are copied character-for-character from the base package, never re-derived or re-typed; every candidate is checked against `INVARIANT_MANIFEST.json` before audit).
3. **`INTRODUCTION_LITERATURE_REFERENCE.md`** — an invariant-safe reference text block: introduction + literature deltas built strictly on cycle-5 wording, every numeral matching the manifest exactly, suitable for future pilot lanes to check candidates against. Mark it clearly as reference material, not a candidate. It must NOT be written anywhere near `candidates/`.
4. **`P1_RECEIPT.md`** — see §8.
5. On full completion only: empty marker file named exactly `FABLE_BURN_P1_DONE_20260711T010503Z`.

Priority under time pressure: manifest → RCA → reference block. A complete manifest + partial RCA beats three half-artifacts.

## 5. First action (ACK)

`mkdir -p` your write dir, then write `P1_ACK.md` containing: the line `FABLE_BURN_P1_ACK_20260711T010503Z`, your ACK timestamp UTC (this is your T0_lane), your tmux pane id, and the brief marker you received (`HWAO_FABLE_BURN_P1_BRIEF_20260711T010503Z`). Then snapshot sources (§3) before anything else.

## 6. Timeline and stop conditions

- Target: T0_lane + 75 min. Hard overrun cap: T0_lane + 150 min → write partial receipt and stop.
- Absolute stops, whichever comes first:
  1. `GLOBAL_STOP_20260711T010503Z.md` exists at the burn root (`fable-weekly-burn-20260711T010503Z/`);
  2. your clock ≥ **2026-07-11T03:50:00Z**;
  3. hard overrun cap reached.
- Poll the burn root between artifacts and at least every ~15 min for `GLOBAL_STOP_20260711T010503Z.md` and `HOLD_5H_20260711T010503Z.md`.
- `HOLD_5H` present → finish only the artifact in progress, write receipt with status `HELD_5H`, stop. Tori re-relays continuation after the 5-hour reset.
- Any stop before completion → receipt status `PARTIAL` (or `HELD_5H`/`BLOCKED`), final line `FABLE_BURN_P1_PARTIAL_20260711T010503Z`, and NO done marker file.
- Done early → stop immediately. Do not invent extra work; leftover quota is not your concern.

## 7. Safety boundaries (absolute — crossing any of these ends the packet)

1. **Write scope:** create/modify files ONLY inside `p1-rp1-invariants/`. Everything else — the burn root, `briefs/`, `METER_LOG.md`, other `p*` dirs, the sprint tree, the repo — is read-only to you.
2. **Runner isolation:** the sprint tree `ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/` is live and runner-owned: never write there, never write into any `candidates/` tree, never promote anything, never touch/signal/patch/kill PID 45665 or any other process.
3. **No network:** no browser or browser automation, no WebFetch/WebSearch, no curl/wget or package installs, no ADS/arXiv/VizieR/SDSS lookups, no MCP network tools. Anything that would need the network goes in the receipt as `GATED` follow-up.
4. **No product/state mutation:** no DB/SQL, no API calls (incl. `/api/pages`, page_versions), no live wiki publication, no deploy/restart, no service changes.
5. **No git:** no add/commit/push/branch/tag/stash — not even for your own artifacts.
6. **No scheduling/daemons:** no cron, launchd, background jobs, or new monitors.
7. **No credentials/billing/cloud:** no OAuth/API-key/credential access, no reading `.env*` or secret files, no billing/account/`/credits` actions, no gcloud/GCP/cloud CLIs.
8. **No pane interference:** no tmux send-keys of any free text to any pane; do not interact with other panes; the unsent composer text in `ge-mastermind:0.0` must not be disturbed. You communicate only via files in your own write dir.
9. **Fail closed:** if a step seems to require crossing any line above, don't — record the conflict in the receipt and continue with what is allowed, or stop with status `BLOCKED`.

Allowed tooling: local read-only text processing (`grep -n`, `diff`, `awk`, `wc`, `shasum -a 256`, etc.) plus file writes inside your write dir.

## 8. Receipt spec (`P1_RECEIPT.md`)

- `status:` COMPLETE | PARTIAL | HELD_5H | BLOCKED
- `t_ack` / `t_end` (UTC), pane id
- Artifact table: filename, byte size, sha256
- Source snapshot table: original absolute path, sha256
- Findings summary in ≤10 lines (drift confirmed? additional drifts found? invariant count)
- Deviations from this brief (should be none) and any ambiguity you resolved, with the choice made
- Follow-up queue, each line labeled `GATED — needs separate Duho approval` (e.g. integrator handoff of the manifest into the sprint's audit flow)
- Coordination-file checks performed (timestamps, result)
- Final line: exactly `FABLE_BURN_P1_DONE_20260711T010503Z` (complete) or `FABLE_BURN_P1_PARTIAL_20260711T010503Z` (anything less)

`HWAO_FABLE_BURN_P1_BRIEF_20260711T010503Z`
