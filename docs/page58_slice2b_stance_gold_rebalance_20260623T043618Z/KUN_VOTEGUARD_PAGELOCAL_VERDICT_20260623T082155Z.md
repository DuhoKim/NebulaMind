# KUN VERDICT — page58 slice-2b neutral-seed VOTE-GUARD (page-local redo)

- **Timestamp:** 2026-06-23 08:21 UTC
- **Cert scope:** page-local neutral-seed vote-guard CONFIG only. NOT the live page-58 write (Papa-gated, separate).
- **NM HEAD:** 4ba9675 (unchanged). /api/health 200 (per brief; not re-pinged — read-only trace).
- **Containment:** read-only. No DB write, no alembic, no paid lane, no page-57/58 live write, no stance lock.

## Verified change-set (first-hand)
- `git diff backend/app/agent_loop/tasks.py backend/app/routers/jury.py` = **EMPTY** (confirmed; matches HwaO).
- `backend/app/routers/claims.py`, `backend/app/services/trust_calculator.py` = **clean** (no status entry).
- Only changed file: `backend/scripts/page58_sign_suppressed_gate_score.py` (untracked dry-run tooling, `??`).
- Host = `Duhoui-MacStudio.local` (NebulaMind local; read directly, no SSH).

## Page-local neutral-seed write spec under test
`stance="none"`, `stance_jury_run_at=now()`, `create_jury_task=false`, `abstract_for_write=NULL`, `intro_excerpt_for_write=NULL`.

---

## ASK 1 — does the page-local spec close EVERY automatic vote path? → **PASS (all automatic paths closed), but NOT via the claimed mechanism.**

Census of every `EvidenceVote(...)` injector in `backend/app` and every selector named in the brief, traced at HEAD 4ba9675:

| Path | File:line | Selector that excludes a 0-vote, run_at=now() seed row | Closed? |
|---|---|---|---|
| `schedule_stance_jury` | tasks.py:1751 | `stance_jury_run_at IS NULL` (1762) **and** `abstract IS NOT NULL` (1763) | ✅ (double) |
| `drain_stance_jury_backlog` (hourly :00) | tasks.py:3029 | `stance_jury_run_at IS NULL` (3054) **and** abstract/intro ≥ MIN (3055-58) | ✅ (double) |
| `drain_jury_fast_pass` P1 (every 30m) | tasks.py:5011 | `stance_jury_run_at IS NULL` (5015) **and** abstract/intro ≥ 100 (5017-18) **and** `count(votes)==0` on accepted/consensus | ✅ |
| `drain_jury_fast_pass` P2 (every 30m) | tasks.py:5052 | requires `run_at IS NOT NULL` (seed qualifies) + `run_at < cutoff` (defer only) + text ≥ MIN + **`vote_count > 0` (5062)** | ✅ via `vote_count>0`, NOT via text |
| `run_stance_jury_for_evidence` | tasks.py:2875 | returns if `run_at is not None` (2884); returns if text<MIN (2893) | ✅ (double) + only enqueued by drainers above |
| `run_stance_jury_single` | tasks.py:4864 | returns if `run_at is not None` (4879); returns if text<MIN (4888) | ✅ (double) + only enqueued by fast-pass |
| `cast_jury_vote` (POST /tasks/{id}/vote) | jury.py:120 | requires existing open `JuryTask` (159) | ✅ via `create_jury_task=false` |
| `list_jury_tasks` (GET /tasks) | jury.py:39 | lists only rows with open `JuryTask` (50) | ✅ via `create_jury_task=false` |
| `dispatch_jury_webhooks` (hourly :30) | tasks.py:3248 | iterates only open `JuryTask` rows | ✅ via `create_jury_task=false` |
| `settle_evidence_and_update_rep` (hourly :15) | tasks.py:3087 | reads votes; `continue` if `<MIN votes` (3114); **injects no votes** | ✅ inert (and non-injecting) |
| citation miners `insert_supportive_evidence` / dynamic | miner.py:393 / dynamic_miner.py:524 | **mint a NEW Evidence row + self-vote**; never touch pre-existing rows | ✅ N/A to seed |
| `vote_evidence` (POST /evidence/{id}/vote) | claims.py:458 | Historical residual; as of `a0909a2`, route is deprecated/no-write and points to `/api/jury/tasks/{task_id}/vote`. | ✅ frozen |

**Result: every AUTOMATIC vote injector is closed for a 0-vote, `stance_jury_run_at=now()` seed row.** Historical note: the non-automatic `vote_evidence` residual is now frozen as deprecated/no-write by `a0909a2`.

### REQUIRED CORRECTION to Tori's stated mechanism (load-bearing)
Tori certifies that **NULL abstract/intro closes the P2 text predicate**. That is **FALSE as a durable invariant.**

- `backfill_intro_excerpts` is **beat-scheduled** (worker.py:273-275, `crontab(minute=10, hour="*/2")` — every 2h). Its selection (tasks.py:2074-2087) is `arxiv_id IS NOT NULL` **AND** `intro_excerpt IS NULL` **AND** (`abstract IS NULL` OR len<100 OR `run_at IS NULL`). A seed row (abstract=NULL, intro=NULL, **arxiv_id present** as a paper citation) **matches**, and the task sets `ev.intro_excerpt = excerpt` (2097). So within ~2h the NULL-text belt is **automatically removed**.
- Therefore the P2 text predicate is NOT what holds P2 shut. **The durable closures are:**
  1. **`stance_jury_run_at=now()`** → permanently excludes the three `run_at IS NULL` drainers (schedule / backlog / fast-P1). Backfill does **not** touch `run_at`, so this holds.
  2. **P2's `vote_count > 0` gate (tasks.py:5062)** → a 0-vote seed row never enters P2, text notwithstanding.
  3. **`create_jury_task=false`** → no JuryTask exists; the three JuryTask paths cannot see the row (no task auto-creates JuryTasks for existing evidence — `_maybe_create_jury_task` fires only at insert: tasks.py:1982/2459/4838).

The conclusion (automatic inertness) **survives on a stronger invariant than the one claimed.** NULL abstract/intro is cosmetic for vote-closure (reverted in ≤2h) — harmless, but it must NOT be certified as the P2 closure.

**Hardening (recommended, not blocking):** treat `stance_jury_run_at=now()` as the **inviolable** seed invariant. If anyone later drops it trusting the NULL-text rationale, the seed becomes exposed the moment backfill runs + any vote lands. (Optional: exclude seed `arxiv_id`s from `backfill_intro_excerpts` if you actually want NULL-text to persist — unnecessary for safety.)

---

## ASK 2 — direct-id residual (`POST /api/evidence/{evidence_id}/vote`) → **ACCEPTABLE known-limitation for the neutral-only seed. NOT a blocker for this page-local cert.** With a sharpened caveat.

2026-06-24 update: this section records the historical residual. Commit `a0909a2` later froze the legacy endpoint as authenticated deprecated/no-write, with replacement `/api/jury/tasks/{task_id}/vote`.

Historical finding before `a0909a2`: `vote_evidence` (claims.py:458) was **unauthenticated** (no `require_api_key`, rate-limited only by `VOTES_LIMIT`), accepted caller-supplied `agent_id`, created an `EvidenceVote`, and called `recalculate_trust` → moved trust via the stance-independent V-component. (This was exactly the forward-caveat from my C2 recert.)

**Why acceptable for THIS cert:**
- It is **non-automatic** — requires a caller who already knows the specific freshly-minted seed `evidence_id`; this cert's scope (ask 1) is *automatic* paths.
- It is a **pre-existing, wiki-wide** property: all ~11.6k existing evidence rows are already votable through this identical public endpoint. The 105 neutral seed rows add to an existing surface; they do not create a new vulnerability class.
- Closing it requires a **shared-endpoint change** (auth + reject/skip-recalc on `stance="none"` evidence) — the global change Papa declined. Blocking a page-local neutral seed on a pre-existing global exposure would be scope-creep.

**Sharpened caveat (must travel with the live write):**
- Post-backfill, a **single** residual vote does more than nudge V: `vote_count` becomes 1 → after the retry age, fast-pass **P2 requalifies the row** (text now populated by backfill) → line 5076 resets `run_at=None` → enqueues `run_stance_jury_single` → text guard now passes → **jury votes cast → `recalculate_trust_v2` moves trust.** So one residual vote can **unlock the otherwise-closed automatic jury pile-on.** Blast radius of the residual > "one V-vote."
- Consequence for messaging: **"neutral seed" guarantees (a) the seed-written stance is non-corroborating/non-voting and (b) freedom from *automatic* solicitation — it does NOT guarantee immunity to externally-initiated trust movement.** A hard "vote-proof" guarantee is **impossible page-locally**; it needs the declined shared-endpoint fix.

**Conditions to carry to the Papa-gated live write (R1/R2):**
- **R1:** keep seed `evidence_id`s un-advertised as "needs votes" (already true — no JuryTask, rows render non-corroborating). Do not surface them in any vote-solicitation list.
- **R2:** record in the live-write cert that neutral ≠ vote-proof (residual + backfill chain above), and that the only hard close is the shared-endpoint change currently out of scope.

---

## ASK 3 — E3 (re-verify C1)? → **NOT triggered. CONFIRMED.**
Shared trust code is **untouched** at HEAD 4ba9675: `tasks.py` + `jury.py` diffs empty; `claims.py` (`recalculate_trust` / `recalculate_trust_v2`) and `services/trust_calculator.py` both clean (trust_calculator.py mtime Jun 22, pre-dates this work). My prior C1 (trust E/tier moves only on `stance ∈ {supports, challenges}`; neutral `none` non-voting) **still holds**. HwaO's read confirmed.

---

## BOTTOM LINE
- **Ask 1 → PASS** (every automatic vote path closed) **with a required rationale correction**: the closure rests on `stance_jury_run_at=now()` + P2 `vote_count>0` + `create_jury_task=false`, **NOT** on NULL abstract/intro (auto-reverted by beat task `backfill_intro_excerpts` every 2h).
- **Ask 2 → residual ACCEPTABLE** known-limitation (non-automatic + pre-existing wiki-wide), **not a blocker**, with R1/R2 carried to the live write and the post-backfill amplification flagged.
- **Ask 3 → E3 not triggered**, prior C1 holds.

This cert covers the **page-local guard config only**. The live page-58 write remains **Papa-gated**. **Kun authorizes neither seed nor live write.**

Gate re-opens on: a change to the seed write spec (esp. `stance_jury_run_at`), a shared-endpoint change touching the residual, or any edit to trust code (would re-trigger E3/C1).
