# KUN VERDICT — Page-58-Local Neutral-Seed Vote Guard (page-local redo)

- Verdict timestamp: 2026-06-23T083040Z
- Artifact under audit: `page58_local_neutral_seed_guard_proposal_20260623T080837Z.md`
  - sha256 `b11f507387c270933b058d3b309d9ae02b5a71aa103ce746d0b9f9510c43f287` (MATCHES brief `b11f5073…`)
- Certifies: the **page-58-local seed-write config** as a closure of automatic jury-vote paths. Does **not** authorize any seed or live write.

## Headline

**CERTIFY / PASS** — the page-local seed-write spec closes **every automatic jury-vote path** for the neutral seed without any shared-code edit. Tori's load-bearing claim (NULL abstract/intro closes `drain_jury_fast_pass` priority-2) is **verified true against real code** at HEAD `4ba9675`.

- Ask 1 (closes every automatic path?) → **YES, PASS.**
- Ask 2 (direct-id residual) → **ACCEPTABLE known-limitation, NOT a blocker** — with a sharpening caveat (below): the residual is *non-inert* (a direct vote on a `none` row moves trust via the V-component), but it is non-automatic, pre-existing, and not widened by the seed.
- Ask 3 (E3 / C1) → **CONFIRMED not triggered. Prior C1 holds.**

## Containment verified (read-only)

- Host `Duhoui-MacStudio.local`; NebulaMind local (no SSH wrap).
- NM HEAD `4ba9675f1f23…` = brief `4ba9675` ✓.
- `git status`: `backend/app/agent_loop/tasks.py` and `backend/app/routers/jury.py` **not listed** (clean/unchanged). Only `backend/scripts/page58_sign_suppressed_gate_score.py` untracked; only tracked diff is `wiki_schema.md` (1-line timestamp). Matches HwaO's first-hand report.
- Locked gold sha `de7ec421…` unchanged (not load-bearing for this cert; no scoring done here).
- No DB write, no alembic, no paid lane, no live page write. I only read code and wrote this verdict file.

## Method

Did **not** trust the artifact's table. Re-traced each named selector first-hand and, independently, enumerated **every** live `EvidenceVote(` write site and **every** `JuryTask(` creator to confirm the path list is complete (not just per-row correct).

- Live vote-WRITE sites (6): `run_stance_jury_for_evidence` (tasks.py:2950), `run_stance_jury_single` (tasks.py:4955), citation `miner.py:393`, `dynamic_miner.py:524`, direct endpoint `claims.py:462`, jury endpoint `jury.py:169`.
- Live `JuryTask(` creator (1): `_maybe_create_jury_task` (tasks.py:1788), called only from evidence-INSERT paths (L1982/2459/4838) — **no scheduled scan backfills tasks over existing evidence**.
- Thresholds positive: `STANCE_JURY_MIN_ABSTRACT_CHARS=100`, `INTRO_EXCERPT_MIN_CHARS=200` (config.py:144,53) → `length(NULL)`=SQL-NULL fails every `>=` predicate; `len("")`=0 fails every `< min` writer branch.

Tori's enumeration is **COMPLETE** — no automatic vote path omitted.

## Ask 1 — per-path certification (all verified at HEAD 4ba9675)

| Path | Closure mechanism | Code | Result |
|---|---|---|---|
| `schedule_stance_jury` | `run_at IS NULL` filter **and** `abstract IS NOT NULL` filter | tasks.py:1760-1764 | Excluded (double) |
| `drain_stance_jury_backlog` | `run_at IS NULL` **and** `or_(len(abstract)>=100, len(intro)>=200)` | tasks.py:3054-3058 | Excluded (double) |
| `drain_jury_fast_pass` p1 | `run_at IS NULL` **and** `or_(len…)` **and** `having count(votes)=0` | tasks.py:5015-5025 | Excluded (triple) |
| **`drain_jury_fast_pass` p2 (load-bearing)** | selection key is `run_at IS NOT NULL`, so run_at cannot exclude; the separately-ANDed `or_(len(abstract)>=100, len(intro)>=200)` is **NULL** for NULL text → row dropped regardless of votes/trust/cutoff | tasks.py:5052-5064 | **Excluded by NULL text — Tori's claim confirmed exactly** |
| `run_stance_jury_for_evidence` (writer) | early-return on `run_at IS NOT NULL`; else insufficient-text branch sets run_at and returns with no vote | tasks.py:2884, 2893-2900 | No vote (double) |
| `run_stance_jury_single` (writer) | same double early-return | tasks.py:4879, 4888-4892 | No vote (double) |
| `_maybe_create_jury_task` → `/api/jury/tasks` → `…/vote` | no `JuryTask` created for seed; `cast_jury_vote` 404s without an open task | tasks.py:1788; jury.py:159-161 | Closed iff no task (writer behavior) |
| citation miners | create their **own** new evidence row + self-vote; never select an existing seed row | miner.py:373-399 | Not a selector for the seed |

**The NULL abstract/intro fields are load-bearing and correct.** For p2 specifically, `run_at = now()` only *defers* (now() eventually < cutoff), and the zero-vote condition is not robust (an outside vote could satisfy `vote_count BETWEEN 1 AND 2`); the only robust closure for p2 is the NULL-text predicate, exactly as Tori states. Verified at L5057-5060.

Net: with `stance="none"` + `stance_jury_run_at=now()` + `abstract=NULL` + `intro_excerpt=NULL` + no `JuryTask`, **no scheduled/automatic path can write a vote on or move trust from a seed row.**

## Ask 2 — direct `/api/evidence/{evidence_id}/vote` residual

**Ruling: ACCEPTABLE known-limitation. NOT a blocker for the neutral-only seed.**

2026-06-24 update: this section records the historical residual. Commit `a0909a2` later froze the legacy endpoint as authenticated deprecated/no-write, with replacement `/api/jury/tasks/{task_id}/vote`.

Historical finding before `a0909a2` (claims.py:456-469): the endpoint had **no** stance/text/`JuryTask`/`run_at` predicate and wrote a vote for any existing `evidence_id`. Tori's description was exact at the time.

Why acceptable:
1. **Not automatic.** No scheduler/cron/jury selector reaches it; it requires a deliberate external POST with a known id. The cert's bar ("every *automatic* vote path") is fully met.
2. **Pre-existing and not widened.** Every already-live evidence row (~11.6k) shares this identical endpoint today. The seed adds 105 ids to an existing global surface; it does not create a new hole. Holding the seed to a higher bar than the entire live corpus is incoherent.
3. Rate-limited (`@limiter.limit(VOTES_LIMIT)`); seed rows render as non-corroborating context (`stance="none"`).

**Sharpening caveat (do not bury): the residual is NOT inert.** `recalculate_trust` is a shim to `recalculate_trust_v2` (claims.py:56-58). The E-component correctly ignores `none` ("neutral counts as 0", L144-147), **but the V-component (L151-165) collects votes by `evidence_id IN (claim's evidence)` with no stance filter** — so a direct vote on a `none` seed row *does* move trust via `TRUST_W_VOTES · V`. This is the concrete realization of the forward-caveat I flagged in the C1/C2 certs.

Therefore: accept as a **monitored** limitation. Preventive closure was declined by Papa (shared-endpoint guard). Recommended controls:
- **Detective (cheap, now):** after the live write, watch the seeded `evidence_id`s for any unexpected `EvidenceVote` rows.
- **Preventive structural fix (if/when Papa wants closure — the principled one, not an endpoint patch):** add a stance filter to the V-component so votes on `stance="none"` rows are not counted — i.e., make V treat `none` as "context only," matching E. One query change in `recalculate_trust_v2`, applies to all `none` rows site-wide. It is a shared-code change, out of this page-local redo scope, and **not required** to clear the neutral seed.

## Ask 3 — E3 / C1

**E3 not triggered — CONFIRMED.** `tasks.py`, `jury.py`, and the trust calculators (`claims.py`) are byte-unchanged (git clean; re-read confirms E-component still counts only `supports`/`challenges`). My prior **C1 holds** as previously scoped. The V-component vote behavior above is **unchanged from prior certs** — a pre-existing property, not a regression introduced by this redo.

## Execution conditions ride the future (separate, Papa-gated) live write

Two of the closures depend on **writer behavior**, not column state, so they must be **read back post-write** (same discipline as E1):
- **E1 (prior):** stance stored as `none` (not the `supports` default).
- **E-A (new):** `abstract IS NULL` and `intro_excerpt IS NULL` for every seeded row — load-bearing for p2 and the writer text-branches.
- **E-B (new):** **zero `JuryTask` rows** reference any seeded `evidence_id` — this is what closes the entire jury.py vote path.
- **E3 (prior):** re-verify C1 if any trust code changes before the write (not triggered now).

These are conditions for the live-write execution cert, not blockers for this config cert.

## Containment footer

- NM HEAD `4ba9675`; db_write 0; paid_lane false; no alembic; no live page-57/58 write; no stance lock.
- Files I wrote: this verdict only.

**Kun authorizes neither the seed nor the live write.** This cert covers the page-local guard config only; the live page-58 write remains Papa-gated. The gate re-opens for the live-write execution cert (E1/E-A/E-B/E3 read-backs) or any change to the guard spec.
