# KUN PHASE-0 CERT — Orphan vote endpoint lock (`POST /api/evidence/{id}/vote`)

> 2026-06-24 update: this cert is historical. Commit `a0909a2` later froze the legacy endpoint as authenticated deprecated/no-write: it validates evidence existence but writes no `EvidenceVote`, performs no commit, and does not call `recalculate_trust`. Replacement path: `/api/jury/tasks/{task_id}/vote`.

- **Reviewer:** Kun (independent trust-surface review; read-only)
- **Date:** 2026-06-23 (UTC 20260623T152439Z)
- **Host:** Duhoui-MacStudio.local · **NM HEAD:** `4ba9675` (no drift)
- **Scope:** narrow endpoint lock, Phase 0 of the orphan-vote remove/lock sequence. NOT a redesign.
- **Containment:** read-only. No DB write, no code edit, no migration, no restart/deploy, no paid lane, no page-57/58 live write, no gold/cert mutation.

## VERDICT: **PASS** (commit + restart to make live; no blockers)

Phase 0 does exactly what it claims — closes the **unauthenticated** and **spoofable** vectors — and nothing more. All three Tori-flagged residuals are acceptable follow-ups; **none is a blocker**. Verified first-hand at HEAD `4ba9675`, not relayed.

---

## Q1 — Smallest safe closure? **PASS**

Diff (claims.py:456-480) verified line-by-line:
- `agent: Agent = Depends(require_api_key)` added to the handler signature.
- Vote write changed `agent_id=body.agent_id` → **`agent_id=agent.id`** (claims.py:473). `body.agent_id` is now inert (still on `VoteCreate` but unused).
- **Imports resolve** — `require_api_key` (claims.py:17) and `Agent` (claims.py:18) are real imports; `require_api_key` is already an established dependency in this same file (also at :577). No NameError risk; pytest exercising the authed path (200 + vote written) confirms resolution at runtime.

`require_api_key` (auth.py:41-63) rejects, **before the body runs**:
- **missing** header → 422 (FastAPI required-`Header(...)` validation, pre-body);
- **invalid** key → 401; **expired** → 401; **banned/suspended** → 401.

Dependencies resolve before the handler body, so the `EvidenceVote` write at :473-479 is unreachable on any reject path. Test `test_evidence_vote_requires_api_key` asserts 422 **and 0 rows written**; `test_evidence_vote_uses_authenticated_agent_id` posts `agent_id=999` with a valid key and asserts the stored row has `agent_id=42` (the authed id) — **spoof ignored, proven**.

Net surface change: **anyone-on-the-network with unlimited self-declared identities → one valid API key, one fixed identity.** That is the correct, strict reduction for an endpoint-lock increment.

> Honesty caveat (do not oversell): "locked" here = **no longer anonymous/spoofable**, NOT "no longer able to move trust." A single valid key can still move trust — see Q2/R1. Phrase the changelog accordingly.

## Q2 — Residuals: all acceptable follow-ups, **0 blockers**

**R1 — repeated votes by one authenticated agent (no dedup): ACCEPTABLE follow-up · HIGHEST priority · not a blocker.**
- Root: the trust **V-component** (claims.py:155-156) sums `v.weight` over *all* votes with **no agent_id dedup**; `confidence = 1 − exp(−n_total/half_life)` saturates after ~a dozen same-sign votes, so one key can drive `V → ~1.0`.
- Why not a blocker: this is a **pre-existing trust-engine property** affecting *every* vote producer (incl. the legitimate jury path), **not introduced** by this change, and Phase 0 strictly *reduces* surface. The catastrophic form (unauthenticated, unlimited distinct fake agent_ids) is **now closed**.
- Caveat for the record: **`VOTES_LIMIT=200/minute` is NOT a meaningful mitigation** — V saturates far below 200, so the rate limit is a DoS guard, not an anti-stuffing guard. Note the asymmetry: the **display** path already dedups by agent_id (`_dedup_vote_counts`, claims.py:37-53) while the **trust** path does not.
- Recommended later-phase fix (trust-engine layer, out of Phase-0 scope): dedup the V-component by `agent_id` (mirror `_dedup_vote_counts` — one latest vote per agent), or add a `UNIQUE(evidence_id, agent_id)` constraint on `evidence_votes`.

**R2 — endpoint accepts any integer `value`: ACCEPTABLE · LOWEST priority · downgraded below Tori's framing — NOT a trust risk at all.**
- Both the V-component (claims.py:155-156) and the display dedup (claims.py:51-52) use `value` by **sign only**; magnitude never enters the math. `value=0` is inert (neither `>0` nor `<0`). A `value=1_000_000` vote == a `value=1` vote. Unbounded integer `value` **cannot inflate trust.**
- Optional hygiene only: constrain to `{-1,0,1}`. No safety urgency.

**R3 — default weight / voter_type (no reputation weighting): ACCEPTABLE follow-up · fidelity, not safety.**
- New row uses model defaults `weight=1.0`, `voter_type="agent"` (models/claim.py:85-86) — i.e. a standard weight-1 agent vote, identical magnitude to the pre-change behavior. Reputation-weighting is an enhancement, not a gap.

## Q3 — Hidden page-58 regression? **NONE (confirmed first-hand)**

Static guarantee: this is a request handler — it executes only on *future* POSTs and cannot mutate existing rows. Read-only SELECT confirms live state:
- seed evidence `28060-28161`: **102 rows, all `stance='none'`** (0 not-none, 0 null);
- **votes on seed = 0**, **JuryTasks on seed = 0**;
- page-58 claims `2929-2936`: **8 present, all `unverified`**.
- (Total `evidence_votes` in DB = 3161, all on unrelated evidence; seed share = 0.)

## Q4 — Commit / deploy recommendation (PASS)

1. **Commit now** — stage **only** `backend/app/routers/claims.py` + `backend/tests/test_claims_api_v2.py`. **Do NOT sweep in** `wiki_schema.md` (daily bump), the untracked `page58_*` dry-run scripts/docs, or `alembic/versions/sentence_votes_v1.py` (unrelated, unapplied migration). `git diff --stat` confirms the two files are the entire change (15 + 42 lines).
2. **Restart REQUIRED to go live.** Routes load at process start; running uvicorn/gunicorn workers hold the OLD unauthenticated handler until reloaded — **the lock is not in effect until the API process is restarted.** No migration, no schema change (`weight`/`voter_type` already exist).
3. **Post-deploy smoke (use a throwaway/test evidence id — NOT a live flagship/page-58 row; each authed POST writes a real vote + moves trust):**
   - no `X-API-Key` → **422**, no row written;
   - invalid `X-API-Key` → **401** (covers the path the unit tests don't);
   - valid key + `body.agent_id=<other>` → **200**, then read back `evidence_votes.agent_id` == the authed agent's id (spoof ignored);
   - confirm zero smoke votes land on seed `28060-28161`.
4. **E3 / prior C1 holds — CONFIRMED.** `tasks.py`, `jury.py`, `trust_calculator.py` are **diff-clean** (zero `git diff` output); shared trust math untouched.

**Non-blocking test-coverage note:** unit tests cover missing-key (422) and authed-spoof-ignored (200); they do **not** assert the invalid-key 401 / expired / banned paths. Those live in shared `require_api_key`; one added invalid-key test would fully close the "missing/invalid" claim. Optional.

---

**Kun authorizes the commit/restart recommendation but performs no writes.** Gate re-opens on the next phase (R1 dedup / endpoint removal) or a new artifact.
