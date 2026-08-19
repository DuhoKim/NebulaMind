# Session split — one coordinator per project (2026-08-19 16:2x KST)

Duho, verbatim: "kinda confused with running two projects, spin-parity study with desi and
second lane, with you on the same session. how can we improve? two Claude sessions for each?"
Decision: two sessions total, split by project, disjoint write areas and panes, cockpit as the
shared view.

## Session ACQ (the EXISTING session) — spin-parity / DESI acquisition

Owns: `prereg/` + `_tori_harvest_20260817/` + `_tori_transfer_20260819/`; tmux panes
`sextet-v2:tori` and `sextet-v2:mir1`; the acquisition task chain (transport gate → transfer
execution → cutouts → 150-label pilot per `PILOT_DECISION_20260818.md` and
`ACQUISITION_PREAUTH_20260818.md`); the cockpit regenerations (single-writer for renderers);
ops/infra incidents; the standing human items (NERSC inbox, Globus Connect Personal, YouTube
personal-channel toggle).

## Session BHU (the NEW session) — theory + videos lane

Owns: `bhu-*` lanes under this handoff dir (`bhu-theory-phase2-20260819/` is live;
`bhu-published-bibliography-20260819/` gated; earlier bhu lanes frozen); tmux panes
`sextet-v2:p0-lana`, `sextet-v2:biblio-lana`, `sextet-v2:p0-goru`, `sextet-v2:mir2` (+ new
windows it creates, prefixed `bhu-`); the Phase 2 chain per `PHASE2_BRIEF.md` (stage-1 seats
were dispatched ~15:57 KST and are running: A1 bounce audit, A2 interior audit, Goru ECSK
ingredients; watcher was armed in the ACQ session and will be REPLACED by the BHU session's own
watcher — first act of the new session: arm its own stage-1 watcher on the three DONE markers).

Kickoff for the new session, paste as its first message:
> You are the BHU-lane coordinator (Hwao-BHU). Read
> .hermes/handoffs/weekend-video-sextet-20260808T0136K/SESSION_SPLIT_20260819.md and
> .hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-theory-phase2-20260819/PHASE2_BRIEF.md,
> then take over the Phase 2 chain: arm watchers on the three stage-1 DONE markers, run the
> Miru stage-1 gate when they land (fresh one-shot, window mir2), then the Track B derivation
> chain with per-step gates, then PHASE2_SUMMARY. Respect every rule in the brief; the
> acquisition session owns portal.nersc.gov, the tori/mir1 panes, and cockpit rendering — never
> touch them. Append dashboard events via autopilot-events.jsonl only.

## Shared-resource rules (both sessions)

1. **Cockpit renderers: ACQ session only** (single-writer). BHU appends events to
   `galaxy-evolution/mastermind/autopilot-events.jsonl` (append-only, race-safe) and asks ACQ
   for a re-render or waits for its next cycle.
2. **Moonshot wallet** is shared (~$27 at split time): each gate note logs its purpose; if the
   wallet dips under $10, both sessions pause gating and surface to Duho.
3. **git**: commit per-lane scopes only (`bhu-*` vs `prereg/` + tools); pull/rebase not needed
   (same clone, sequential commits); never commit the other project's dirty files.
4. **Fable weekly cap** is shared (52% used at split, resets Sat ~afternoon KST): direction is
   cheap, but if the cap approaches, the BHU session downshifts model first (theory seats run on
   non-Claude engines anyway).
5. **Claude-engine seats**: p0-lana/biblio-lana are BHU's; if ACQ ever needs a Claude seat it
   opens its own window (`acq-lana`).
6. **Emergency stop**: either session may stop the OTHER's runaway process only if it is
   actively violating a frozen rule (report immediately); otherwise hands off.

## Why split now (and not earlier)

Earlier today spin-parity had no unblocked agent work, so a second session would have idled.
Since then the pre-auth chain went live (transport building at split time) AND Phase 2 launched
— two active campaigns with different cadences. One coordinator per campaign; the cockpit
(`ge-autopilot.html` + `spin-parity-status.html` + `bhu-lane2-status.html`) stays the single
pane of glass across both.

## Amendment 16:2x KST — third session: OPS (Duho, verbatim: "why don't we launch another Fable
and attach in the middle pane, and I deal with other stuffs such as updating dashboard stuff
with him or her.")

**Session OPS (middle pane, ge-mastermind:0.1)** owns: cockpit rendering (the single-writer role
TRANSFERS here from ACQ — render_ge_autopilot_dashboard_v2.py, render_bhu_lane2_status.py,
render_spin_parity_status.py, render_cockpit_index.py, live_provider_usage_monitor.py), the
usage-monitor modernization task, dashboard event rendering, infra incidents (crash dialogs,
launchd services, tmux hygiene), YouTube registry maintenance, and whatever Duho hands it
directly. It does NOT touch: `prereg/` work products (ACQ's), `bhu-*` lane work products
(BHU's), portal.nersc.gov, or the seats owned by the other sessions. ACQ and BHU append events
to autopilot-events.jsonl as before; OPS renders.

Layout: **left = ACQ (DESI) · middle = OPS · right = BHU.** The Goru read-only viewer is
retired (BHU supervises its own seats; Duho follows all lanes via the cockpit OPS keeps fresh).

## Amendment — naming reform (Duho, verbatim: "why don't we retire all agents' name and use
models instead such as, agy, gpt1,2 and so on. and we only name 3 Fables, Hwao (You), Tori
(BHU), and Blanc (OPS)")

**Named coordinators (Fable sessions only):**
- **Hwao** — left pane, DESI/spin-parity coordinator (this doc's "ACQ")
- **Tori** — right pane, BHU-lane coordinator (the name is REASSIGNED from the retired hermes
  seat persona; see collision note)
- **Blanc** — middle pane, OPS coordinator

**Helper seats: engine names only, personas retired** (Yui, Lana, Kun, Goru, Miru — all retired):
| New name | Engine/route | Was |
|---|---|---|
| `agy` | Antigravity/Gemini CLI | Goru |
| `gpt1` | hermes profile `yui` (gpt-5.6-sol) | Yui |
| `gpt2` | hermes profile `tori2` (gpt-5.6-sol) | Tori (seat) |
| `gpt3` | hermes profile `tori3` (gpt-5.6-sol) | (spare) |
| `kimi` | Kimi K3, Moonshot direct one-shots | Kun / Miru |
| `claude-seat` | claude CLI worker windows | Lana / Lana-2 |

**Collision note:** legacy tmux window names (`sextet-v2:tori`, `p0-lana`, `p0-goru`, `mir1`,
`mir2`, `biblio-lana`) keep their names until each owning session renames them — the reform
governs how we COMMUNICATE, not a live rename of running panes. In particular
`sextet-v2:tori` currently hosts the gpt2 transport builder and has nothing to do with
Tori-the-BHU-coordinator. Lane records already written keep their historical names; new
records use the new names.

## Amendment — role tables retired; platoon doctrine (Duho, verbatim: "and also retire all the
role table and let you three Fables construct your own Agent Platoon leveraging available
resources")

The quintet/sextet role tables, fixed seat assignments, and ACK-phrase protocol are RETIRED.
Each named coordinator (Hwao, Tori, Blanc) composes their own Agent Platoon per task from the
available resources: `agy` (Gemini subscription), `gpt1/gpt2/gpt3` (hermes gpt-5.6-sol
profiles, Nous subscription), `kimi` (Moonshot direct one-shots, metered wallet),
`claude-seat` windows (shared Fable cap), plus each coordinator's own subagents and tools.
Composition, sizing, and sequencing are the coordinator's judgment call.

**What is NOT retired (lane-verification invariants, engine-agnostic):**
- Frozen artifacts stay frozen; gates and receipts discipline stays wherever a claim or an
  irreversible step is produced — cross-engine adversarial review remains the house standard
  because it has caught real errors all month, but WHO gates WHAT is now the coordinator's call.
- Ownership boundaries from this doc (write areas, panes, portal.nersc.gov = Hwao's,
  cockpit rendering = Blanc's) and the shared-resource rules (wallet floor, cap awareness,
  per-lane git scopes).
- Subscription-only/metered-wallet cost discipline; every outward action's authorization rules.
- Each coordinator is ACCOUNTABLE for their lane's verification quality — the retirement of
  the role table transfers responsibility, it does not dilute it.

## Amendment — full resource pool; Blanc is quartermaster (Duho, verbatim: "don't forget you can
also use Deep Research on Gemini and also Claude. and on Gemini you can also use features like
Video and Image generation, we have Flow quota, and so on. Blanc should table all availalbe
resources and manage")

The platoon resource pool includes, beyond the CLI engines: **Deep Research on Gemini and on
Claude**; **Gemini video generation (Veo via Flow, quota exists)** and **image generation**
(incl. Nano Banana Pro for legible infographic text); browser-driven surfaces where already
gated; TTS/ASR via the managed gateway; and whatever else is legitimately provisioned.

**Blanc (OPS) owns the RESOURCE CATALOG**: a living table of every available resource — what it
is, how to invoke it, current quota/cost state, pacing constraints, and what authorization its
use requires. Coordinators consult the catalog when composing platoons; Blanc keeps it current
(quota reads, drop-file protocols, throttle observations). Known constraint facts to seed the
catalog (hard-won, do not relearn by outage): Deep Research must be paced gently — sustained
back-to-back runs trip google.com/sorry throttles; DR output is filed reference material feeding
lanes, never a direct lane writer; Flow/Veo credits are recorded via the flow-credits drop-file
(operator-confirmed) and Veo prompt/credit mechanics are mapped in the standing capability
notes; video-generation credit SPEND remains per-decision authorized by Duho — quota existing
is not spend authorization.
