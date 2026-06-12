# NebulaMind — Beat Schedule v3 (overnight-data-driven retune)

**Author:** Kun 🔬
**Date:** 2026-05-15 00:15 KST
**Supersedes:** `job_schedule_v1.md` §9 v2 (job_schedule_v1.md remains the canonical source for design rationale; this doc covers v3-specific changes only).
**Status:** Draft — pending Papa approval, then Tori implements.
**Prereq:** v2 is **already deployed** in `worker.py` (verified lines 127–198). v3 is a diff on top of the live state.

---

## 1. Overnight diagnosis (last 24 h, queried 2026-05-15 00:10 KST)

### 1.1 What ran

| Lane (proposal_type) | n (24h) | commits | rollbacks | gate_rejects | errors | avg delta_q | status |
|---|---:|---:|---:|---:|---:|---|---|
| `section_rewrite` (AstroSage + Nutty judge) | 32 | 24 | 8 | — | — | **+0.039** | working |
| `section_rewrite` (AstroSage, judge=None) | 29 | 0 | 0 | 7 | 22 | null | **36% error rate** |
| `sonnet_audit` (Claude Sonnet 4.6) | 53 | 0 | 0 | 0 | 0 | null (q1=**0.765**) | passive — audit only |
| `opus_audit` (Claude Opus 4.7) | 18 | 0 | 0 | 0 | 0 | null (q1=**0.350**) | passive — audit only |
| `rakon_deep_pass` | 6 (7d=13) | 0 | 0 | 0 | **13** | null | **100% error** — Rakon not loaded |

### 1.2 What didn't run (Papa's "research_ideas = 0" finding, root-caused)

- `research_ideas` table: **15 rows total ever**, all `kun-seed` from 2026-05-13. Zero from any model.
- `autowiki_runs WHERE proposal_type='research_ideas_lightweight'`: **0 rows ever**. J1 has never reached its logging line.
- v2 §9 lanes deployed in beats (verified `worker.py:127–198`) but no `idea_judge_pool`, `rakon_draft_async`, `mima_draft_async`, `tera_draft_async`, `rakon_adversarial_probe`, etc. autowiki_runs rows exist either.

### 1.3 Three failure modes confirmed

**A. J1 silently fails before logging.**
- `process_lightweight_event` queue route IS landed (`worker.py:213` → `autowiki`).
- `autowiki` queue depth = 0 (worker drains everything).
- `celery` queue depth = 6,350 (backlog from earlier, unrelated to J1).
- All Redis flags healthy: `phase3_enabled=1`, `autowiki:enabled=1`, no mutex held, `nutty:rate:hourly` unset.
- Last 24 h had 24 J1-eligible `section_rewrite` commits — every one should have fired `process_lightweight_event.delay()`.
- **Hypothesis:** the task runs but errors early. Likely culprits: `_build_page_context(db, 57)` returns None (some recent schema change?), or `_nutty_rate_check_and_increment` raises, or the Mac Studio Ollama call to `deepseek-r1:14b` is timing out. **Tori needs to check Mac Studio Celery worker logs.**

**B. Rakon 100% error rate.**
- All 13 `rakon_deep_pass` attempts over the last 7 days errored. Recent errors: 5 with "Errno 61 connection refused" (1 s); 4 with "timed out" (600 s).
- Mac Pro Ollama `/api/ps` (queried 2026-05-14 22:06 KST): `gemma3:27b`, `qwen3:30b`, `deepseek-r1:14b` resident — **but NOT `deepseek-r1:671b` (Rakon)**.
- **Hypothesis:** Mac Pro Rakon resident-set fix (§7.2 B4) still pending. Until Rakon is preloaded on Mac Pro every 24 h, every R1/R2/R3 lane errors out cleanly. **HwaO action needed:** add `deepseek-r1:671b` to the Mac Pro keep-alive set so Ollama doesn't evict it between calls.

**C. Cloud models are passive (audit-only).**
- Sonnet auditing 53×/day, Opus 18×/day, both scoring **q1 only** — no `q0`, no `delta_q`. By design: they're read-only quality scorers, not actors.
- Sonnet's mean q1 = 0.765 (relatively forgiving); Opus's mean q1 = 0.350 (more critical).
- **Papa's diagnosis was right.** To get `delta_q` from cloud models, give them active roles. v3 does this.

---

## 2. v3 design intent (Papa Qs answered)

| Papa Q | v3 answer |
|---|---|
| Get Rakon more involved | (1) Tighten R2 idea-draft from 3×/day → **every 4 h (6×/day)**. (2) Tighten R3 adversarial from 3×/wk → **daily**. (3) Add new lane **R4 `rakon_synthesis_pass` every 8 h** — Rakon directly authors a section rewrite proposal (active role, delta_q-tracked). |
| Cloud models in measurable-delta_q roles | (1) Sonnet as **alt section_rewrite proposer** alongside AstroSage (round-robin per tick — measurable A/B on delta_q). (2) Opus as **JI final-promotion judge** (replaces Atom for the promote step, keeps Atom for dedup pre-filter). (3) Opus also as **hero refresh proposer** (replaces AstroSage for that lane — highest-quality model on smallest surface). |
| Fix gaps in pipeline | (1) J1 root-cause investigation (§1.3 A). (2) Mac Pro Rakon resident-set fix (§1.3 B). (3) Document that v2 lanes are deployed but most haven't produced their first row — escalation flag, not a v3 change. |

---

## 3. v3 beat schedule diff (from v2 / current `worker.py`)

### 3.1 Tighten existing Rakon lanes

```python
# CHANGE: idea draft 3×/day → every 4h (6×/day)
"rakon-draft-async-q4h": {                                # was "rakon-draft-async" inside JI step
    "task": "app.agent_loop.research_ideas.auto_improvement.rakon_draft_async",
    "schedule": crontab(minute=0, hour="*/4"),            # 00/04/08/12/16/20 UTC = 09/13/17/21/01/05 KST
    "kwargs": {"page_id": 57},
},

# CHANGE: adversarial 3×/wk → daily
"rakon-adversarial-probe-daily": {                        # was "rakon-adversarial-probe-mwf"
    "task": "app.agent_loop.research_ideas.auto_improvement.rakon_adversarial_probe",
    "schedule": crontab(minute=0, hour=15),               # 15 UTC = 00 KST daily
    "kwargs": {"page_id": 57},
},
```

**Delete:** `rakon-adversarial-probe-mwf` (replaced by `-daily`).

### 3.2 Add new Rakon lane: synthesis pass (active proposer role)

```python
# NEW: Rakon directly authors section rewrites every 8h (offset from rakon_deep_pass)
"rakon-synthesis-pass-q8h": {
    "task": "app.agent_loop.research_ideas.auto_improvement.rakon_synthesis_pass",
    "schedule": crontab(minute=30, hour="1,9,17"),        # 01/09/17 UTC = 10/18/02 KST (offset +30min from rakon-deep-pass to avoid collision)
    "kwargs": {"page_id": 57},
},
```

**Function `rakon_synthesis_pass(page_id)`** — new in `auto_improvement.py`:

- Acquire `rakon:lock` (TTL 8 h, same key as other Rakon lanes — naturally serializes).
- Pick the section with lowest `delta_q` history (last 14 days, from `autowiki_runs WHERE proposal_type='section_rewrite' AND page_id=57`).
- Prompt Rakon with the full current section + all claims + recent arxiv → ask for a complete rewrite with improved coherence and citation density.
- Submit through normal `propose_section_rewrite` → judge → commit path (so delta_q is computed by autowiki_tick's q0/q1 machinery).
- Logged as `proposal_type='section_rewrite'`, `model_proposer='deepseek-r1:671b'` so it's distinguishable from AstroSage.

This is the lane that gets Rakon making measurable contributions — not just running deep-pass in the background.

### 3.3 Add Sonnet as active section_rewrite proposer (A/B with AstroSage)

```python
# NEW: Sonnet writes section rewrites every 30 min — round-robin with AstroSage
"sonnet-section-rewrite-q30m": {
    "task": "app.agent_loop.autowiki.tasks.sonnet_section_rewrite",
    "schedule": crontab(minute="15,45"),                  # :15 and :45 (offset from autowiki_tick :00)
    "kwargs": {"page_id": 57},
},
```

**Function `sonnet_section_rewrite(page_id)`** — new in `autowiki/tasks.py`:

- Pick a section by same priority heuristic as autowiki_tick (lowest delta_q history).
- Build the same `claims_block` + `arxiv_block` context.
- Call Anthropic API with `claude-sonnet-4-6`, structured prompt for section rewrite (mirror AstroSage prompt shape so the comparison is clean).
- Submit through the same judge → commit path.
- Logged as `proposal_type='section_rewrite'`, `model_proposer='claude-sonnet-4-6'`.

**Why round-robin not replace:** keeps AstroSage's domain-finetuned proposals in the mix; lets the data tell us which proposer wins on delta_q over 2–4 weeks.

**Cost estimate:** 48 ticks/day × ~$0.02/call = ~$1/day. Fits Papa's existing cloud budget.

### 3.4 Move Opus into the JI promotion-judge slot

This is a code change inside `judge_idea_pool` (§8.5.3 in `job_schedule_v1.md`) — no new beat needed.

**Current JI step 5 (in §8.2.3):** Atom-7b → Takji (phi4) → AstroSage polish → promote.

**v3 JI step 5:** Atom-7b → Takji (phi4) → AstroSage polish → **Opus final-promotion judge** → promote.

The Opus call gets the top-N candidates plus their Atom scores + Takji verdicts + AstroSage-polished prose, and returns `{promote: bool, rationale: str}` per candidate. Final say.

- **Why Opus and not Sonnet at this gate:** the promotion decision is rare (5 per JI tick × 6 JI ticks/day in v3 = 30 calls/day) and load-bearing (an `active` idea is a public claim). Opus's deeper rubric is worth the ~$0.10/call cost = $3/day.
- **Why keep Atom + Takji upstream:** Atom is the cheap pre-filter (avoid sending 80 drafts to Opus); Takji catches methodology failures that Opus's general reasoning would miss. Each filter catches a different failure class.
- **Cost:** 30 calls/day × $0.10 = $3/day. Total cloud spend ~$5/day with §3.3 Sonnet rewrites — well under any sane budget.

Add Redis kill switch: `idea_judge:opus_judge_enabled` (default 1). Off → falls back to top-N promotion by score alone.

### 3.5 Move Opus into the hero refresh proposer slot

Replace AstroSage in `astrosage_hero_refresh` with Opus. Rename the task to `opus_hero_refresh`. Schedule unchanged (3×/day at 05/13/21 KST).

- **Why Opus here:** hero tagline + 3 hero facts is ~150 characters of page chrome. Highest-stakes, smallest surface area. Opus's prose quality > AstroSage's for the front-of-page text. ~3 calls/day × $0.10 = $0.30/day — trivial.
- **Old `astrosage-hero-refresh-8h` beat:** delete. Replace with `opus-hero-refresh-8h`.

### 3.6 Tighten JI judge cadence (v2 was 3×/day, v3 = 6×/day)

```python
# CHANGE: 3×/day → every 4h
"idea-judge-q4h": {                                       # was "idea-judge-tri-daily"
    "task": "app.agent_loop.research_ideas.auto_improvement.judge_idea_pool",
    "schedule": crontab(minute=0, hour="*/4"),            # 00/04/08/12/16/20 UTC
},
```

With Rakon idea spawns every 4 h, draft pool fills faster — judge keeps pace.

### 3.7 Tighten Buddle B2 draft (v2 was 3×/day, v3 = 4×/day) and add B4

```python
# CHANGE: 3×/day → 4×/day (every 6h)
"buddle-draft-q6h": {                                     # was "buddle-draft-tri-daily"
    "task": "app.agent_loop.research_ideas.auto_improvement.buddle_draft_async",
    "schedule": crontab(minute=0, hour="*/6"),            # 00/06/12/18 UTC
},

# NEW: Buddle proposes new claims from §16 orphan idea signals every 3h
"buddle-claim-propose-q3h": {
    "task": "app.agent_loop.research_ideas.auto_improvement.buddle_claim_propose",
    "schedule": crontab(minute=15, hour="*/3"),           # :15 offset to avoid collision
    "kwargs": {"page_id": 57},
},
```

**Function `buddle_claim_propose(page_id)`** — new:

- Query §16 step 3.5 output: orphan high-value idea signals on `page_id` (ideas with no anchoring claim).
- For each, call Buddle to draft a candidate `Claim` row text + cited evidence.
- Submit through normal `propose_claim_insert` → judge → commit path.
- Logged as `proposal_type='claim_insert_subtopic'`, `model_proposer='deepseek-r1:32b'`.

Gives Buddle a delta_q-trackable role beyond drafting research_ideas.

### 3.8 Tighten autowiki_tick (v2 = 15 min, v3 = 10 min)

```python
# CHANGE: 900s (15 min) → 600s (10 min)
"autowiki-tick": {
    "task": "app.agent_loop.autowiki.tasks.autowiki_tick",
    "schedule": 600.0,
},
```

Body takes ~60–90 s per tick (per existing observation). 10 min is safe.

Daily tick count goes from 96 → 144. AstroSage proposer load: 144 × 30 s = **72 min/day Mac Studio** (was 48 min). Comfortably within budget (Mac Studio at 19% v2, ≤ 22% v3).

### 3.9 What v3 does NOT change

- `rakon-deep-pass-2h` — keep at every 2 h, lane is value-positive once Rakon resident set is fixed.
- All Mac-Studio non-cloud lanes already at tight v2 cadences (Tera/Takji/Mima/AstroSage/Nutty/Atom) — no further tightening needed; calibrate first.
- All non-galaxy-evolution ops jobs (`fetch-arxiv-daily`, `drain-stance-jury-hourly`, etc.) — untouched.
- `sonnet-judge-tick` 20 min + `opus-judge-tick` 60 min — keep as **passive audits** in addition to the new active roles. The passive audits give us q1 ground-truth for the active proposers to be measured against.

---

## 4. Wall-clock budget (v3 vs v2)

### Mac Pro (Rakon-bound, assuming B4 fixed)

| Lane | v2 calls/day | v3 calls/day | v3 min/day (median) |
|---|---:|---:|---:|
| `rakon_deep_pass` (q2h) | 12 | 12 | 60–120 |
| `rakon_draft_async` | 3 | 6 | 480 (480–2400) |
| `rakon_adversarial_probe` | 0.43 (3/wk) | 1 (daily) | 100–200 |
| `rakon_synthesis_pass` (q8h) | 0 | 3 | 240 |
| `buddle_draft_async` | 3 | 4 | 20–40 |
| `buddle_evidence_pair` (hourly) | 24 | 24 | 72–120 |
| `buddle_claim_propose` (q3h) | 0 | 8 | 40 |
| **Total median** | — | — | **~1100 min/day = 18 h ≈ 76 % util** |

Tight — but `rakon:lock` mutex absorbs overruns; over-prescription is intentional. If `rakon:lock` skip rate exceeds 40 %, slow R2 back to 4×/day.

### Mac Studio (sequential inference)

| Lane | v2 min/day | v3 min/day |
|---|---:|---:|
| AstroSage proposer | 48 | 72 (more ticks) |
| Sonnet proposer (NEW) | 0 | ~3 (cloud, doesn't burn local inference) |
| Other lanes (Mima/Tera/Nutty/Takji/Atom) | ~150 | ~150 (unchanged) |
| **Total** | ~205 | ~225 (~16 % util) |

Sonnet/Opus are cloud calls — they free up Mac Studio. Net Mac Studio load actually drops slightly per autowiki_tick (no more local proposer call on ticks owned by Sonnet).

### Cloud cost (Anthropic API)

| Lane | Calls/day | $/call | $/day |
|---|---:|---|---:|
| `sonnet-judge-tick` (existing audit) | 72 | $0.01 | $0.72 |
| `opus-judge-tick` (existing audit) | 24 | $0.05 | $1.20 |
| `sonnet_section_rewrite` (NEW v3) | 48 | $0.02 | $0.96 |
| `opus_hero_refresh` (NEW v3) | 3 | $0.10 | $0.30 |
| Opus JI judge step (NEW v3) | 30 | $0.10 | $3.00 |
| **Total** | — | — | **~$6.20/day ≈ $185/month** |

---

## 5. Net throughput delta (v3 vs current live state)

| Metric | Current (24h actual) | v3 (target after fixes) | Multiplier |
|---|---:|---:|---:|
| Rakon idea drafts | 0 (Rakon dead) | 42/wk | ∞ |
| Rakon adversarial probes | 0 | 7/wk | ∞ |
| Rakon section rewrites | 0 | 21/wk | NEW |
| Sonnet section rewrites | 0 | 336/wk | NEW |
| Opus hero refreshes | 0 | 21/wk | NEW |
| Opus JI promotion judgments | 0 | 210/wk | NEW |
| Buddle claim proposals | 0 | 56/wk | NEW |
| Nutty drafts (J1) | 0 | TBD (gated on §6.1 debug) | TBD |
| autowiki_tick frequency | 96/day | 144/day | 1.5× |
| JI judge ticks | 0 (lane dead) | 42/wk | NEW |

Mostly NEW — because the v2 lanes are largely silent. v3 lights them up + adds active cloud roles.

---

## 6. Critical fixes Tori needs (in priority order)

### 6.1 P0 — J1 silent failure investigation

J1 routing is correct in code (worker.py:213). All Redis flags healthy. Yet `research_ideas_lightweight = 0 ever`. **Tori action:**

1. Tail the autowiki Celery worker log on Mac Studio for the next 10 min (or check existing log) — look for any line containing "process_lightweight_event" or "[J1]".
2. If no such lines appear during a section_rewrite commit, the `.delay()` call in `autowiki/tasks.py:671` isn't actually being reached — check whether `claim_ids_inserted` (line 671) or whatever conditional gates the dispatch evaluates to truthy on `section_rewrite` commits. May need to relax the gate.
3. If the lines appear but log "rate limit hit" / "debounced" / "page_not_found", that's the bug — debug accordingly.
4. Most likely culprit if no log lines: `_build_page_context` returns None silently (page 57 schema diverged from expected). Add a `log.warning` if context is None and verify.

### 6.2 P0 — Mac Pro Rakon resident set (HwaO action)

`deepseek-r1:671b` must be in the Mac Pro Ollama keep-alive list. Currently every R1/R2/R3 lane errors out cleanly. **HwaO action:** add the model to whatever script keeps Mac Pro Ollama warm (or use `ollama run deepseek-r1:671b` in a launchd-managed wrapper that keeps the connection open).

### 6.3 P1 — v3 task additions

Net new tasks to add in `auto_improvement.py`:
- `rakon_synthesis_pass(page_id)` — §3.2
- `buddle_claim_propose(page_id)` — §3.7

Net new tasks to add in `autowiki/tasks.py`:
- `sonnet_section_rewrite(page_id)` — §3.3
- Rename `astrosage_hero_refresh` → `opus_hero_refresh`, swap model — §3.5

Edit `judge_idea_pool` to add Opus final-judge step — §3.4.

### 6.4 P2 — Beat schedule changes (in `worker.py`)

The diff is the §3 entries. Specifically:
- Replace `rakon-adversarial-probe-mwf` with `rakon-adversarial-probe-daily`.
- Replace `rakon-draft-async` (3×/day) with `rakon-draft-async-q4h` (6×/day).
- Replace `idea-judge-tri-daily` with `idea-judge-q4h`.
- Replace `buddle-draft-tri-daily` with `buddle-draft-q6h`.
- Replace `astrosage-hero-refresh-8h` with `opus-hero-refresh-8h`.
- Add `rakon-synthesis-pass-q8h`, `sonnet-section-rewrite-q30m`, `buddle-claim-propose-q3h`.
- Change `autowiki-tick` schedule from 900.0 to 600.0.

---

## 7. Acceptance criteria

Run these after v3 deploys:

1. **J1 produces drafts.** Within 1 h of deploy, `research_ideas` should have ≥1 new row with `model_chain LIKE '%14b%'` and `status='draft'`. (Requires §6.1 fix.)
2. **Rakon synthesis fires.** Within 8 h of deploy + §6.2 fix, `autowiki_runs` should have ≥1 row with `model_proposer='deepseek-r1:671b'` AND `proposal_type='section_rewrite'` AND `delta_q IS NOT NULL`.
3. **Sonnet active rewrites land.** Within 1 h of deploy, `autowiki_runs` should have ≥1 row with `model_proposer='claude-sonnet-4-6'` AND `delta_q IS NOT NULL`. This is the headline v3 win — Sonnet's first measurable contribution to page quality.
4. **Opus promotion judgments logged.** First JI tick after deploy should have an `autowiki_runs` row with `idea_signals_json` containing an `opus_judge_verdicts` key per candidate.
5. **autowiki_tick rate up.** Within 24 h of deploy, count of `autowiki_runs WHERE proposal_type='section_rewrite' AND started_at >= NOW() - INTERVAL '24 hours'` should be ≥120 (was 61).
6. **Cloud cost on track.** Anthropic dashboard daily spend ≤ $10 (target ~$6).

If 2 fails after 24 h: Rakon still not loaded on Mac Pro — re-escalate B4.
If 3 fails: Sonnet API call shape bug or Anthropic key permissions issue.

---

## 8. What stays from v2

- All §9 v2 lane definitions (Mima, Tera, Takji, Atom, AstroSage, Nutty lanes) — unchanged.
- All v2 mutexes (`rakon:lock`, `mima:lock`, `tera:lock`, `buddle:lock`, TTLs from §9.4.1).
- Page-57 containment (`wiki_improvement:priority_page_id` Redis flag — though currently unset; v3 may keep it unset so all lanes default to picker which targets page 57 anyway).
- Sonnet/Opus passive audit ticks (sonnet-judge-tick 20 min, opus-judge-tick 60 min) — kept as ground-truth scorers for the active proposers.

— 🔬 Kun
