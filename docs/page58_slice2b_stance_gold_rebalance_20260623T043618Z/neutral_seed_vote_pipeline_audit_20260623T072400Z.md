# Page 58 Neutral Seed Vote Pipeline Audit

Read-only report for Kun/Papa live-write prep. No code or DB changes were made.

## Containment

- NM HEAD: `4ba9675`
- `/api/health`: `200`
- DB writes: `0`
- Paid lane touched: `false`
- No live write, no alembic, no stance lock, no page-57/58 write.

## Answer

Yes. A freshly seeded evidence row with `stance="none"` can automatically accrue `evidence_votes` before a human promotes it if it is inserted with:

- `stance_jury_run_at = NULL`, and
- enough `abstract` or `intro_excerpt` text to satisfy the jury selectors, and
- its claim/page/evidence id is not in the explicit stance-jury hold lists.

The active stance-jury selectors do not filter by `Evidence.stance`. The trust `E` component treats neutral stance as non-voting, but the live `V` component is stance-independent and aggregates all `EvidenceVote` rows for all evidence on the claim.

## Trust Caveat Confirmed

`recalculate_trust_v2` loads all evidence for a claim, then loads all votes for those evidence ids and computes `V` from `v.value`, independent of `Evidence.stance`.

- `backend/app/routers/claims.py:137` loads all claim evidence.
- `backend/app/routers/claims.py:144` and `backend/app/routers/claims.py:145` restrict only the `E` component to `supports` / `challenges`.
- `backend/app/routers/claims.py:153` through `backend/app/routers/claims.py:160` aggregate all `EvidenceVote` rows for the `V` component, with no stance filter.

So a neutral seed with auto-generated votes can move trust through `V`.

## Vote-Writing Paths

### 1. `schedule_stance_jury`

Path: `backend/app/agent_loop/tasks.py:1751`

Selector:

- Same claim id.
- `Evidence.stance_jury_run_at.is_(None)` at `backend/app/agent_loop/tasks.py:1762`.
- `Evidence.abstract.isnot(None)` at `backend/app/agent_loop/tasks.py:1763`.
- Held filters only exclude configured page/claim/evidence ids.

Neutral included? Yes. There is no `Evidence.stance` predicate. A neutral seed with abstract text and `stance_jury_run_at = NULL` can be enqueued.

Vote writer reached: `run_stance_jury_for_evidence`, which writes `EvidenceVote` at `backend/app/agent_loop/tasks.py:2950`.

Smallest guard: add `Evidence.stance.notin_(["none", "neutral", "related_different_facet"])` to the selector, and also add the same defensive early return in `run_stance_jury_for_evidence`.

### 2. Hourly `drain_stance_jury_backlog`

Path: `backend/app/agent_loop/tasks.py:3028`

Beat schedule: `backend/app/agent_loop/worker.py:70`

Selector:

- `Evidence.stance_jury_run_at.is_(None)` at `backend/app/agent_loop/tasks.py:3054`.
- Abstract or intro length threshold at `backend/app/agent_loop/tasks.py:3055`.
- Held filters only at `backend/app/agent_loop/tasks.py:3061`.

Neutral included? Yes. There is no stance filter.

Vote writer reached: `run_stance_jury_for_evidence`, which can write non-zero jury votes.

Smallest guard: add `Evidence.stance.notin_(["none", "neutral", "related_different_facet"])` to the candidate query, plus the runner-side defensive return.

### 3. Fast 30-minute `drain_jury_fast_pass`

Path: `backend/app/agent_loop/tasks.py:4993`

Beat schedule: `backend/app/agent_loop/worker.py:106`

Priority 1 selector:

- `Evidence.stance_jury_run_at.is_(None)` at `backend/app/agent_loop/tasks.py:5015`.
- Abstract or intro length threshold at `backend/app/agent_loop/tasks.py:5016`.
- Claim trust in `accepted` / `consensus` at `backend/app/agent_loop/tasks.py:5020`.
- Zero existing votes at `backend/app/agent_loop/tasks.py:5025`.

Priority 2 selector:

- Already run, low vote count, accepted/debated claim at `backend/app/agent_loop/tasks.py:5052` through `backend/app/agent_loop/tasks.py:5063`.

Neutral included? Yes for Priority 1 if the claim is accepted/consensus, and yes for Priority 2 if a neutral row already somehow has 1-2 votes. There is no stance filter.

Vote writer reached: `run_stance_jury_single`, which writes `EvidenceVote` at `backend/app/agent_loop/tasks.py:4955`.

Smallest guard: exclude neutral stances in both priority queries and add a runner-side defensive return in `run_stance_jury_single`.

### 4. Direct `run_stance_jury_for_evidence`

Path: `backend/app/agent_loop/tasks.py:2873`

Selector/guards:

- Looks up evidence id directly.
- Skips only missing rows, already-run rows, held rows, or insufficient abstract/intro text.
- It includes `Asserted stance: {ev.stance}` in the prompt at `backend/app/agent_loop/tasks.py:2918`, but does not skip neutral stances.

Neutral included? Yes if called directly with a neutral evidence id.

Smallest guard: early return when `ev.stance in {"none", "neutral", "related_different_facet"}` before the prompt/model call.

### 5. Direct `run_stance_jury_single`

Path: `backend/app/agent_loop/tasks.py:4868`

Selector/guards:

- Looks up evidence id directly.
- Skips only missing rows, already-run rows, held rows, or insufficient abstract/intro text.
- It includes `Asserted stance: {ev.stance}` in the prompt at `backend/app/agent_loop/tasks.py:4908`, but does not skip neutral stances.

Neutral included? Yes if called directly with a neutral evidence id.

Smallest guard: early return when `ev.stance in {"none", "neutral", "related_different_facet"}` before the prompt/model call.

### 6. `JuryTask` creation and external/manual jury API

Task creation helper: `backend/app/agent_loop/tasks.py:1777`

Selector:

- `_maybe_create_jury_task` creates an open `JuryTask` for an evidence id without checking `Evidence.stance`.

Open task listing: `backend/app/routers/jury.py:50`

- Lists open `JuryTask` rows by status/category/agent assignment.
- It does not exclude neutral evidence.

Vote endpoint: `backend/app/routers/jury.py:159`

- Writes `EvidenceVote` at `backend/app/routers/jury.py:169`.
- It does not exclude neutral evidence.

Neutral included? Yes if a neutral evidence row has a `JuryTask`. The current page-58 neutral seed dry-run plan does not create tasks, but any live seed path that calls `_maybe_create_jury_task` would expose neutral rows to external/manual jury voting.

Smallest guard: do not create `JuryTask` for neutral evidence in `_maybe_create_jury_task`; also hide/deny existing neutral evidence tasks in `/jury/tasks` and `/jury/tasks/{task_id}/vote`.

### 7. Legacy/manual evidence vote API

Path: `backend/app/routers/claims.py:456`

Selector:

- Any existing evidence id.
- Writes `EvidenceVote` at `backend/app/routers/claims.py:462`.
- No stance filter.

Neutral included? Yes, but this is an explicit API call, not automatic accrual. It still can move trust through `V`.

2026-06-24 update: the legacy `/evidence/{evidence_id}/vote` route is now deprecated/no-write in `a0909a2`; it validates auth/evidence but writes no vote and does not recalculate trust. Replacement: `/api/jury/tasks/{task_id}/vote`.

### 8. Adversarial pass

Path: `backend/app/agent_loop/tasks.py:4763`

Selector:

- Selects accepted claims for adversarial search.
- Inserts new `stance="challenges"` evidence and enqueues its own jury.
- Does not select existing neutral rows for voting.

Neutral included? No, not as existing neutral rows. This path creates separate challenge evidence.

Smallest guard: none for neutral seed protection, unless the new challenge insert path is reused for page-58 seeds.

### 9. Targeted ADS miner

Path: `backend/scripts/targeted_ads_miner.py:1055`

Selector:

- Runs on miner-selected candidates, inserts new evidence only when `commit` and `decision.merge_eligible`.
- Writes juror votes immediately for the newly inserted row at `backend/scripts/targeted_ads_miner.py:1076`.
- Sets `stance_jury_run_at` at insert time.

Neutral included? No for existing neutral rows. It writes votes only for its own newly inserted evidence.

Smallest guard: none for page-58 neutral seeds, unless this script is reused as the seed writer.

### 10. Citation-context miners

Paths:

- `backend/app/agent_loop/citation_context/miner.py:370`
- `backend/app/agent_loop/citation_context/dynamic_miner.py:501`

Selector:

- They insert new supportive evidence with `stance="supports"`.
- They set `stance_jury_run_at=now`.
- They immediately write a positive `EvidenceVote` for the newly inserted supportive evidence at `miner.py:393` and `dynamic_miner.py:524`.

Neutral included? No for existing neutral rows. They create their own support rows and votes.

Smallest guard: none for page-58 neutral seeds, unless this code is reused as the seed writer.

### 11. Grounded chat retrieval

Path: `backend/app/services/chat_retrieve.py`

Selector:

- Reads evidence and counts votes for display/retrieval.
- It does not create `EvidenceVote` rows.

Neutral included? It may display neutral evidence, but it does not auto-vote.

Smallest guard: none for vote accrual.

## Minimum Safe Guard Before Live Neutral Seed

Best small guard set:

1. In the page-58 neutral seed writer, set:
   - `stance="none"`
   - `stance_jury_run_at=now`
   - no `JuryTask`
2. In `schedule_stance_jury`, `drain_stance_jury_backlog`, and both fast-jury priority selectors, exclude neutral stances:
   - `Evidence.stance.notin_(["none", "neutral", "related_different_facet"])`
3. In `run_stance_jury_for_evidence` and `run_stance_jury_single`, add the same early-return guard as defense-in-depth.
4. In `_maybe_create_jury_task` and `/jury/tasks/{task_id}/vote`, reject/hide neutral evidence tasks.

Smallest single guard if only one place is allowed: set `stance_jury_run_at=now` and do not create `JuryTask` in the neutral seed writer. That blocks the automatic drains for fresh rows, but it is less robust than adding stance guards because direct task calls and future seed code could bypass it.

## Bottom Line

Kun's caveat is real. Neutral stance is trust-neutral only in the evidence `E` component. The live vote `V` component is stance-independent, and the active jury drains do not exclude neutral evidence. A page-58 neutral seed should not go live until neutral evidence is excluded from automatic jury/vote paths or the seed writer marks neutral rows as already jury-closed and creates no jury task.
