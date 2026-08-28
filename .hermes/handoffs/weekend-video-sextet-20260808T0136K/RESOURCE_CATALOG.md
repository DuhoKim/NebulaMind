# RESOURCE CATALOG — platoon resource pool (Quartermaster: Blanc/OPS)

Living table per the SESSION_SPLIT_20260819.md platoon amendment. Coordinators
(Hwao, Tori, Blanc) consult this when composing platoons; Blanc keeps it current.
Quota numbers rot — the **live** state is always the cockpit usage cards
(ge-autopilot.html usage panel / live-steering feed); numbers here are seed
readings with their capture time.

Last full verification pass: **2026-08-27 17:39 KST** (Blanc).

> **Verified 2026-08-27 17:39 KST. The previous pass was 2026-08-19 — eight days stale, which is
> my failure as Quartermaster and the reason this table stopped being consulted.**
>
> **The imbalance Duho named, in today's numbers:**
>
> | pool | used | state |
> |---|---|---|
> | Fable (all three coordinators) | **100% weekly** | EXHAUSTED — overflow on usage credits |
> | All Claude models | 64% weekly | |
> | Antigravity / agy (Gemini) | **1%** | a whole subscription, nearly untouched |
> | Codex / gpt seats (ChatGPT Pro) | **3%** | |
> | Moonshot / kimi | $154 of $199 peak | spending steadily, the one pool with real burn |
>
> Referee work IS distributed — codex 19, gpt56 16, kimi 10 gate artifacts on
> 2026-08-27 alone. The imbalance is not in the gates. It is that **all three
> coordinators think on Fable**, and the seats are only ever handed verification.
> Design, drafting and analysis stay on the exhausted pool while two subscriptions
> idle at 1% and 3%.

>
> A contributing cause worth recording: agy's only consumer (Goru) sat blocked on
> an unanswered permission prompt for **55 hours** ending 2026-08-27 16:40. A pool
> at 1% partly means its user could not run.

---

## CORRECTION — 2026-08-28, the coordinators are NOT on Fable

**The table above and the sentence "all three coordinators think on Fable" are wrong, and the
drafting doctrine below rests on them.** Written by Hwao on Duho's instruction ("fix
RESOURCE_CATALOG.md", then "leave it with her"); Blanc stood down as writer to avoid two writers and
verifies after rather than during. Meter figures below are Blanc's captures, carried verbatim.

### Models

| coordinator | model | how established |
|---|---|---|
| **Hwao** | `claude-opus-5[1m]` | self-reported from its own system prompt — authoritative for itself |
| **Blanc** | `claude-opus-5[1m]` | Blanc verified from its own system prompt, 2026-08-28 |
| **Tori** | **UNVERIFIED — do not infer** | Blanc asked at **14:04 KST 2026-08-28**; Tori was mid-task and has not answered. Two confirmed members of a three-member set are not the set. Blanc will supply hers when it lands. |

### Meters — captured 2026-08-28T05:00:52Z from claude.ai/settings/usage, page reading "Last updated: just now"

| meter | reading |
|---|---|
| **All models, weekly** | **69% used** ← the meter that governs the coordinators |
| Fable, weekly | 100% used |
| Current session | 4% |
| Reset | both weeklies **Saturday 2:00 PM** |
| Usage credits | **ON** |
| Plan | **Max (20×)**, limits promo-boosted through **Aug 31** |

**These supersede the 2026-08-27 17:39 table above**, which is kept as the dated reading it was.
Note the all-models figure moved 64% → 69% between captures; the Fable figure did not move because
the coordinators are not spending against it.

**Why the cockpit card read NOT REFRESHING:** the prior capture in
`.hermes/state/claude_plan_usage.json` was **20.5 hours stale**. Refreshed at the capture above. A
stale meter reading as a live one is how the exhausted-pool premise survived a full day.

**Consequence.** If the coordinators run on Opus they are not drawing on the Fable weekly at all, so
**all-models at 69% governs, not Fable weekly at 100%.** Blanc reported the opposite to Duho earlier
on 2026-08-28 and corrected it within the hour.

**Consequence for the drafting doctrine below.** The doctrine still stands, but **not for the reason
it gives.** Its stated premise — that coordinators burn an exhausted pool — is false. The reasons that
survive are independent of cost:

- gate verdicts need **fresh context and multiple engines**, which a coordinator cannot supply;
- a coordinator's context is better spent on work needing the whole lane in one head;
- a seat draft is a draft, and separating drafting from refereeing is the point.

**Do not cite the 100%-exhausted figure as justification for anything.** Two of three coordinators
are verifiably on Opus; the third has not been checked, and two confirmed members of a three-member
set are not the set.


## CLI engines

| Resource | Invocation route | Quota / cost state (seed reading) | Pacing constraints | Authorization |
|---|---|---|---|---|
| **Fable coordinators + claude-seat** | `claude --dangerously-skip-permissions` in a tmux window (`cseat*`) | Shared Claude sub; cockpit card "Claude / Fable + claude-seat" — 16:35 KST: 5h 32%, Fable weekly 61%, resets Sat ~afternoon KST | Weekly cap is SHARED across all three sessions; when it approaches, downshift theory/helper work to non-Claude engines first | Standing rules only; no extra gate |
| **agy** (Antigravity / Gemini CLI) | `agy --dangerously-skip-permissions` (windows `agy`, `old-agy`, `goru-agy:agy`) | Antigravity agent-request pool; card "Antigravity / agy (Gemini)" — 16:35 KST: ~0% weekly, ~0% 5h | Usage refresh only via idle, unscrolled panes OUTSIDE sextet-v2 (monitor enforces); Antigravity pool is separate from the consumer Gemini app meter | Standing rules only |
| **gpt1 / gpt2 / gpt3** (hermes gpt-5.6-sol profiles) | `hermes -Q -q` with profiles `yui` / `tori2` / `tori3` (windows `gpt1..3`) | **Codex OAuth (ChatGPT subscription)** — hermes default provider `openai-codex` (corrected by Duho 2026-08-19; NOT Nous). Account-level ChatGPT limits, cockpit card "Codex / gpt seats (ChatGPT Pro)" — 17:14 KST: weekly 24% used (resets 20 Aug 13:18), Spark 0%. **Meter = the idle Codex CLI window `ge-mastermind:blanc-codex-status`** (codex v0.146.0 at `~/.local/bin/codex`, logged in as duhokim81@gmail.com Pro — same shared OAuth credential `openai-codex-oauth-1` the gpt seats use); hermes itself exposes no rate-limit reader (verified: `/status` = session info, `/usage` = Nous wallet, `--usage-file` = per-run tokens). Keep that window open or the card goes honestly stale | Auto-compaction hits ~280k of a 372k window → frequent mid-task "Compacting" pauses; budget idle-waiters | Subscription-only; no API-key/PAYG |
| **DeepSeek R1** (reasoning, Nous route) | `hermes -z "<task>" --provider nous -m deepseek/deepseek-r1` (also `deepseek-r1-0528`; `deepseek-reasoner`/`v3.1` ids 404). Zero marginal cost (Nous sub) | **Calibrated 2026-08-20** (Blanc): caught a seeded arithmetic defect with recomputation, confirmed a known-good gate with real binomial-sigma work, zero false problems. Diagnosis depth partial (took the broken sum at face value as denominator). Scorecard: blanc-ops-overhaul-20260820/deepseek-calibration/ | **Slow-thinking — minutes per answer; fine for gates, wrong for interactive seats** (Hwao). Keep fresh sessions | Recommended slot: fourth-family verification lens / cheap math checking, paired with a second lens for diagnosis depth. NOT admitted: `deepseek-chat` — missed the seeded defect and hallucinated a confirmation; rejected for gate duty |
| **Hermes / Nous credits** | hermes gateway services (TTS via `gpt-4o-mini-tts`, `--provider nous` runs) | card "Hermes / Nous credits" — 16:35 KST: $57.75 total usable | plan dollars and top-up dollars tracked separately | Subscription-only |
| **kimi** (Kimi K3) | Direct Moonshot key (windows `kimi*`) — UNPAUSED 2026-08-20 (Duho topped up: $199.73). **Economy doctrine (Hwao): default SMALL gates to the free Nous route** — `hermes chat --provider nous -m moonshotai/kimi-k3`, fresh session, **under ~80K context (400s beyond)** — and reserve the direct key for large-context forensic gates; the burn that emptied $95 in a day was mostly small gates Nous handles fine | card "Moonshot / kimi (K3 direct)" — 14:5x KST: $199.73 | Wallet floor $10: below it, gating pauses and surfaces to Duho; gate notes log purpose | Metered-spend discipline; Nous-route gates bill the Nous sub |

## Research & generation

| Resource | Invocation route | Quota / cost state | Pacing constraints | Authorization |
|---|---|---|---|---|
| **Deep Research — Gemini** | browser-driven (already-gated Chrome lane only) | account-level, no meter | **Gentle pacing** — sustained back-to-back runs trip google.com/sorry; few runs, spaced; back off on FIRST soft throttle; cooldown after a block; separate accounts for volume | DR output is FILED REFERENCE feeding lanes — never a direct lane writer, never edits .tex, never writes the DB without an explicit gate |
| **Deep Research — Claude** | claude.ai (browser, gated) | draws on the shared Claude sub | Same reference-not-writer rule as Gemini DR | Same as above |
| **Gemini video — Veo via Flow** | Flow UI (browser, gated); Ingredients-to-Video for character consistency | Flow credit pool via drop-file `flow_credits.json` (operator-confirmed) — **2026-08-20 16:07 KST: 25,028 / 25,050** (25,000 monthly + 50 daily bonus through Aug 31; only 22 credits spent since the 08-04 capture). Refresh = read the ULTRA profile popover in Flow; card auto-flags captures older than 3 days | Generation is ASYNC (minutes) — poll to a terminal state before judging; an immediate read gives a false "Failed" that mimics a throttle | **Credit SPEND is per-decision authorized by Duho — quota existing is NOT spend authorization** |
| **Image generation — Nano Banana Pro** | Gemini app (browser, gated) — use for legible infographic text; Veo can't render text reliably | Counts on the consumer Gemini app meter (card "Gemini app / consumer" — 16:35 KST: 1% current window) | App meter has no API: refreshed by operator capture or the gated crawler drop-file; stale readings report as unknown | Same per-decision spend courtesy as video for bulk generation |
| **TTS / ASR** | inside the Hermes runtime (crew agent / speak tool) — OpenAI `gpt-4o-mini-tts`, covered by the Nous $20 sub; local `say -v Samantha` on the Studio for status reads | no separate key; no marginal cost | Rendered audio goes to scratchpad or the listen page — NEVER into the monitored cockpit root; Gemini TTS key is deliberately disabled | Standing rules only |

## Delivery & infrastructure

| Resource | Invocation route | State | Pacing constraints | Authorization |
|---|---|---|---|---|
| **Per-Fable audio reports** | `/Users/duhokim/HermesOps/scripts/nm_fable_say.sh <hwao\|tori\|blanc> "text"` — voices: Hwao=shimmer (F), Tori=nova (F), Blanc=echo (M); 30-45s (~90-120 words); auto-plays on the Studio AND the MacBook (native listener daemon `net.nebulamind.status-listener`, installed 2026-08-19; Mac Pro deliberately excluded per Duho) and refreshes `reports/status-audio/latest.mp3` + the listen/archive pages | TTS covered by the Nous sub | Audio never goes into the monitored cockpit root; `NM_SAY_NO_PLAY=1` renders without playing | Standing rules only |
| **YouTube uploader** | HermesOps/scripts uploader; `token.json` = upload-only, `token_manage.json` = privacy changes | — | Read `cockpit/videos/published.json` BEFORE uploading (duplicate guard) | Default UNLISTED; public only with Duho's per-video OK |
| **Browser-driven surfaces (CUA / Claude-in-Chrome)** | only lanes already gated for it | — | No cron browser-driving (macOS TCC kills Apple Events from cron) — schedule as in-session wakeups in the lane that already drives Chrome; never System Settings; never install persistence; an auth wall is a report, not a puzzle | Per-lane gating as established |
| **Cockpit rendering** | **Scheduled: LaunchAgent `com.nebulamind.cockpit-render` every 10 min (installed 2026-08-20, Duho-authorized; log `cockpit/render.log`; stop = `launchctl bootout gui/$UID/com.nebulamind.cockpit-render`).** Manual/Blanc single-writer: `render_ge_autopilot_dashboard_v2.py`, `render_spin_parity_status.py`, `render_bhu_lane2_status.py`, `render_cockpit_index.py`, `live_provider_usage_monitor.py` (all need `PATH=/opt/homebrew/bin` prepended for tmux) | live | Hwao/Tori append events to `galaxy-evolution/mastermind/autopilot-events.jsonl` (append-only); Blanc renders | Blanc-owned per charter |

## Keeping this current

- Blanc refreshes seed readings on monitor passes and records new throttle/pacing
  observations here the moment they are learned (do not relearn by outage).
- Any coordinator who observes a new constraint (throttle, quota change, broken
  route) reports it to Blanc's pane or appends a dashboard event; Blanc folds it in.
- Ownership boundaries and verification invariants live in SESSION_SPLIT_20260819.md
  and are NOT restated here — this file is capacity and cost, not governance.

## Drafting doctrine — 2026-08-27 (Duho)

**Coordinator drafting work moves to agy and the gpt seats.** *(Cost premise corrected 2026-08-28 — see CORRECTION above: the coordinators are on Opus, not Fable, so the exhausted-pool argument does not hold. The doctrine stands on the fresh-context and separation-of-roles grounds instead.)* Fable was recorded at 100% of
its weekly allowance with overflow on usage credits, while agy sits at 1% and the
Codex/gpt pool at 3%. Two subscriptions idle while the pool all three coordinators
think on is exhausted.

**Moves to a seat:** first-draft prose, mechanical rewrites, restating a derivation
in our notation, literature fetch and summary, candidate wordings for a clause the
coordinator will judge, sweep bookkeeping that eats context without needing
judgement.

**Stays with the coordinator:** their own judgement, and anything needing the whole
lane in one head.

**Stays fresh-context and multi-engine — do NOT consolidate:** gate verdicts. A
gate's value is having no prior context. On 2026-08-27 kimi cleared a closure v6
that codex had refused, and codex found on the preregistration text what kimi
missed. Spreading drafting across seats is a saving; spreading gates across seats
is the method.

**The standing trap:** a seat draft is a draft, not a result. Verify before
carrying it, or you reproduce the agreed-with-itself failure the referees caught
three times this week — REGATE3's hidden null, the probe that asserted on its own
old wording, the brief that cited a change record which did not exist.

**Brief seats self-containedly.** Hand over receipt paths, not an assumption that
the seat can reconstruct the lane. That is also what makes the returned draft
checkable.
