# Hwao execution acceptance — Fable weekly burn 20260711T010503Z

Marker: `HWAO_FABLE_BURN_EXECUTION_ACCEPTED_20260711T010503Z`
Written: 2026-07-11 ≈01:28Z by Hwao (coordinator, director pane — coordination and review only). Clock check at acceptance: `2026-07-11T01:26:37Z`.
Accepted plan: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/HWAO_FABLE_WEEKLY_BURN_PLAN_20260711T010503Z.md` (`HWAO_FABLE_WEEKLY_BURN_PLAN_READY_20260711T010503Z`).

## 1. Approval record

- Duho approval received verbatim: `approve fable burn 20260711T010503Z` — exact match to the plan's suggested approval phrase, with no packet include/exclude list attached. Therefore **P1, P2, P3 are accepted as planned; P4 remains conditional-only and is NOT briefed by this acceptance.**
- T0 preflight meter row already logged by Tori in `../METER_LOG.md` at `2026-07-11T01:23:27Z`: Fable 5-hour **12%** (reset ≈ 2 h ≈ 03:05Z), Fable weekly **6%** (reset ≈ 3 h ≈ 04:05Z), 19 active Claude panes, runner PID 45665 healthy and untouched. Headroom confirmed; window open.
- Effective window: now → **hard stop 2026-07-11T03:50:00Z** (15 min before weekly reset), per plan §1. All three packet ETAs fit comfortably.

## 2. Scope accepted (and nothing more)

| Packet | Lane | Output dir (under burn root) | Done marker | ETA from lane ACK |
|---|---|---|---|---|
| P1 — RP-1 numeric-invariant RCA + manifest + verbatim-carry reference | Lana Fable lane A | `p1-rp1-invariants/` | `FABLE_BURN_P1_DONE_20260711T010503Z` | 75 min (hard cap 150 min) |
| P2 — Cycle-7 rejected-report source-lead ledger + AGN–SFR status/debate map + prior-work comparison candidate | Lana Fable lane B | `p2-cycle7-source-ledger/` | `FABLE_BURN_P2_DONE_20260711T010503Z` | 60 min (hard cap 120 min) |
| P3 — M3 sidecar acceptance baseline + RT-card deepening (local evidence only) | Lana Fable lane C | `p3-m3-rt-baseline/` | `FABLE_BURN_P3_DONE_20260711T010503Z` | 55 min (hard cap 110 min) |

Burn root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/`

- **P4 (derived claims/evidence candidates from clean cycle 5)** runs only if: P1–P3 complete AND weekly meter < 60% used AND clock < 03:15Z. If that condition lands, Hwao writes a separate P4 brief at that time (30 min hard cap). It does not start from this acceptance.
- Optional non-Fable cross-checks (Kun/Codex strict recompile for P1; Goru/Gemini format audit for P3) remain optional, skip-if-busy, on their own quotas, and are **not dispatched** by this acceptance.

## 3. Relay order and handoff protocol (Tori)

1. Relay `P1_BRIEF_RP1_INVARIANTS_20260711T010503Z.md` and `P2_BRIEF_CYCLE7_SOURCE_LEDGER_20260711T010503Z.md` now (two separate Claude/Fable panes).
2. Relay `P3_BRIEF_M3_RT_BASELINE_20260711T010503Z.md` ≈10 minutes later (third pane), per the plan's stagger.
3. **File handoff only.** No tmux send-keys of free text into any agent pane (standing protocol). Point each lane at its brief file path; each lane's T0 is its own ACK timestamp.
4. Every brief is self-contained: sources, outputs, markers, stop conditions, and safety boundaries are inside the brief. Lanes do not need the plan file to execute.

## 4. Coordination files at burn root (owners fixed)

- `METER_LOG.md` — **Tori-owned** (exists). Cadence: every ~30 min, at each packet completion, once at final rollup. Same on-demand OAuth usage fetch as the preflight; no cron/launchd, no new daemons.
- `GLOBAL_STOP_20260711T010503Z.md` — created by **Tori or Hwao only**, on any of: weekly reset observed (weekly % drops), clock ≥ 03:50:00Z, or Duho order. Lanes poll for it and stop when present.
- `HOLD_5H_20260711T010503Z.md` — created by **Tori only** if Fable 5-hour ≥ 80% before its ≈03:05Z reset. Lanes finish the artifact in progress, write a receipt with status `HELD_5H`, and stop; Tori re-relays continuation after the 5-hour reset (file-based).
- Lanes never create, edit, or delete any of these coordination files. Each lane writes only inside its own packet directory.

## 5. Roles

- **Duho** — approver. Already given for P1–P3; everything in §6 still needs him.
- **Hwao** — coordination and receipt review only. No packet substance, no lane execution, no dispatch. Writes `BURN_ROLLUP.md` at global stop or when all accepted packets complete.
- **Tori** — brief relay, meter cadence, stop/hold files, custody/hash checks on receipts (P2 especially).
- **Lana Fable lanes A/B/C** — packet execution per their briefs, one pane each.

## 6. Explicitly NOT authorized by this acceptance (separately gated on Duho)

- Any network fetch for `NEEDS_NETWORK_VERIFICATION` leads (ADS/arXiv/VizieR/SDSS or any other page) — queued in P2's ledger for a later explicitly-approved pass.
- The supervised Gemini Web sidecar run for `REQ_M3_RT_20260711T091128Z` — own protocol chain per `DUHO_GEMINI_WEB_WIKI_RESEARCH_ARTIFACT_SCOPE_20260711T004710Z`.
- Any integration of P1/P2/P3 material into the runner's `candidates/` tree, any promotion decision, any runner interaction at all (PID 45665 untouched; its sprint tree is read-only for every burn lane).
- DB/SQL, `/api/pages`/page_versions/live wiki publication, product mutation, deploy/restart, git actions, cron/launchd, browser automation, billing/account/OAuth/API-key/credential access, cloud/GCP. All standing gates stay closed.
- P4, until its stated condition is met and Hwao issues its brief.

## 7. Briefs issued with this acceptance

- `briefs/P1_BRIEF_RP1_INVARIANTS_20260711T010503Z.md` — `HWAO_FABLE_BURN_P1_BRIEF_20260711T010503Z`
- `briefs/P2_BRIEF_CYCLE7_SOURCE_LEDGER_20260711T010503Z.md` — `HWAO_FABLE_BURN_P2_BRIEF_20260711T010503Z`
- `briefs/P3_BRIEF_M3_RT_BASELINE_20260711T010503Z.md` — `HWAO_FABLE_BURN_P3_BRIEF_20260711T010503Z`

## 8. Rollup commitment

On global stop, or when all accepted packets have their done/partial receipts, Hwao writes `fable-weekly-burn-20260711T010503Z/BURN_ROLLUP.md`: per-packet outcome (done / partial / dropped), artifact list with paths and hashes, final meter line, and the follow-up queue (network verification pass, sidecar run, integrator handoff) — each still gated on separate Duho approval.

---

Acceptance complete. No lane dispatched by this document, no packet substance performed, no runner interaction, no writes outside `fable-weekly-burn-20260711T010503Z/briefs/`. **Hwao stops here; next actor is Tori (relay per §3).**

`HWAO_FABLE_BURN_EXECUTION_ACCEPTED_20260711T010503Z`
