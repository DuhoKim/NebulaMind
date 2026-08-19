# RESOURCE CATALOG — platoon resource pool (Quartermaster: Blanc/OPS)

Living table per the SESSION_SPLIT_20260819.md platoon amendment. Coordinators
(Hwao, Tori, Blanc) consult this when composing platoons; Blanc keeps it current.
Quota numbers rot — the **live** state is always the cockpit usage cards
(ge-autopilot.html usage panel / live-steering feed); numbers here are seed
readings with their capture time.

Last full verification pass: **2026-08-19 16:43 KST** (Blanc).

## CLI engines

| Resource | Invocation route | Quota / cost state (seed reading) | Pacing constraints | Authorization |
|---|---|---|---|---|
| **Fable coordinators + claude-seat** | `claude --dangerously-skip-permissions` in a tmux window (`cseat*`) | Shared Claude sub; cockpit card "Claude / Fable + claude-seat" — 16:35 KST: 5h 32%, Fable weekly 61%, resets Sat ~afternoon KST | Weekly cap is SHARED across all three sessions; when it approaches, downshift theory/helper work to non-Claude engines first | Standing rules only; no extra gate |
| **agy** (Antigravity / Gemini CLI) | `agy --dangerously-skip-permissions` (windows `agy`, `old-agy`, `goru-agy:agy`) | Antigravity agent-request pool; card "Antigravity / agy (Gemini)" — 16:35 KST: ~0% weekly, ~0% 5h | Usage refresh only via idle, unscrolled panes OUTSIDE sextet-v2 (monitor enforces); Antigravity pool is separate from the consumer Gemini app meter | Standing rules only |
| **gpt1 / gpt2 / gpt3** (hermes gpt-5.6-sol profiles) | `hermes -Q -q` with profiles `yui` / `tori2` / `tori3` (windows `gpt1..3`) | **Codex OAuth (ChatGPT subscription)** — hermes default provider `openai-codex` (corrected by Duho 2026-08-19; NOT Nous). Account-level ChatGPT limits, cockpit card "Codex / gpt seats (ChatGPT Pro)" — 17:14 KST: weekly 24% used (resets 20 Aug 13:18), Spark 0%. **Meter = the idle Codex CLI window `ge-mastermind:blanc-codex-status`** (codex v0.146.0 at `~/.local/bin/codex`, logged in as duhokim81@gmail.com Pro — same shared OAuth credential `openai-codex-oauth-1` the gpt seats use); hermes itself exposes no rate-limit reader (verified: `/status` = session info, `/usage` = Nous wallet, `--usage-file` = per-run tokens). Keep that window open or the card goes honestly stale | Auto-compaction hits ~280k of a 372k window → frequent mid-task "Compacting" pauses; budget idle-waiters | Subscription-only; no API-key/PAYG |
| **Hermes / Nous credits** | hermes gateway services (TTS via `gpt-4o-mini-tts`, `--provider nous` runs) | card "Hermes / Nous credits" — 16:35 KST: $57.75 total usable | plan dollars and top-up dollars tracked separately | Subscription-only |
| **kimi** (Kimi K3, Moonshot direct one-shots) | one-shot hermes runs on the Moonshot direct key (windows `kimi*`) | Metered wallet; card "Moonshot / kimi (K3 direct)" — 16:35 KST: $24.40 available | **Wallet floor $10**: below it, both lane sessions pause gating and surface to Duho; every gate note logs its purpose | Metered-spend discipline per charter |

## Research & generation

| Resource | Invocation route | Quota / cost state | Pacing constraints | Authorization |
|---|---|---|---|---|
| **Deep Research — Gemini** | browser-driven (already-gated Chrome lane only) | account-level, no meter | **Gentle pacing** — sustained back-to-back runs trip google.com/sorry; few runs, spaced; back off on FIRST soft throttle; cooldown after a block; separate accounts for volume | DR output is FILED REFERENCE feeding lanes — never a direct lane writer, never edits .tex, never writes the DB without an explicit gate |
| **Deep Research — Claude** | claude.ai (browser, gated) | draws on the shared Claude sub | Same reference-not-writer rule as Gemini DR | Same as above |
| **Gemini video — Veo via Flow** | Flow UI (browser, gated); Ingredients-to-Video for character consistency | Flow credit pool via drop-file `flow_credits.json` (operator-confirmed) — 16:35 KST: 25,050 / 25,050 credits | Generation is ASYNC (minutes) — poll to a terminal state before judging; an immediate read gives a false "Failed" that mimics a throttle | **Credit SPEND is per-decision authorized by Duho — quota existing is NOT spend authorization** |
| **Image generation — Nano Banana Pro** | Gemini app (browser, gated) — use for legible infographic text; Veo can't render text reliably | Counts on the consumer Gemini app meter (card "Gemini app / consumer" — 16:35 KST: 1% current window) | App meter has no API: refreshed by operator capture or the gated crawler drop-file; stale readings report as unknown | Same per-decision spend courtesy as video for bulk generation |
| **TTS / ASR** | inside the Hermes runtime (crew agent / speak tool) — OpenAI `gpt-4o-mini-tts`, covered by the Nous $20 sub; local `say -v Samantha` on the Studio for status reads | no separate key; no marginal cost | Rendered audio goes to scratchpad or the listen page — NEVER into the monitored cockpit root; Gemini TTS key is deliberately disabled | Standing rules only |

## Delivery & infrastructure

| Resource | Invocation route | State | Pacing constraints | Authorization |
|---|---|---|---|---|
| **Per-Fable audio reports** | `/Users/duhokim/HermesOps/scripts/nm_fable_say.sh <hwao\|tori\|blanc> "text"` — voices: Hwao=shimmer (F), Tori=nova (F), Blanc=onyx (M); 30-45s (~90-120 words); auto-plays on the Studio AND the MacBook (native listener daemon `net.nebulamind.status-listener`, installed 2026-08-19) and refreshes `reports/status-audio/latest.mp3` + the listen/archive pages | TTS covered by the Nous sub | Audio never goes into the monitored cockpit root; `NM_SAY_NO_PLAY=1` renders without playing | Standing rules only |
| **YouTube uploader** | HermesOps/scripts uploader; `token.json` = upload-only, `token_manage.json` = privacy changes | — | Read `cockpit/videos/published.json` BEFORE uploading (duplicate guard) | Default UNLISTED; public only with Duho's per-video OK |
| **Browser-driven surfaces (CUA / Claude-in-Chrome)** | only lanes already gated for it | — | No cron browser-driving (macOS TCC kills Apple Events from cron) — schedule as in-session wakeups in the lane that already drives Chrome; never System Settings; never install persistence; an auth wall is a report, not a puzzle | Per-lane gating as established |
| **Cockpit rendering** | Blanc single-writer: `render_ge_autopilot_dashboard_v2.py`, `render_spin_parity_status.py`, `render_bhu_lane2_status.py`, `render_cockpit_index.py`, `live_provider_usage_monitor.py` (all need `PATH=/opt/homebrew/bin` prepended for tmux) | live | Hwao/Tori append events to `galaxy-evolution/mastermind/autopilot-events.jsonl` (append-only); Blanc renders | Blanc-owned per charter |

## Keeping this current

- Blanc refreshes seed readings on monitor passes and records new throttle/pacing
  observations here the moment they are learned (do not relearn by outage).
- Any coordinator who observes a new constraint (throttle, quota change, broken
  route) reports it to Blanc's pane or appends a dashboard event; Blanc folds it in.
- Ownership boundaries and verification invariants live in SESSION_SPLIT_20260819.md
  and are NOT restated here — this file is capacity and cost, not governance.
