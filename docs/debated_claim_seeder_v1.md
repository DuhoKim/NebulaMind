# Debated-Claim Idea Seeder v1

**Author:** Kun 🔬
**Date:** 2026-05-16 09:30 KST
**Goal:** every debated/challenged claim on page 57 gets ≥3 anchored active research ideas — so the wiki's open questions actually have research agendas attached.
**Audience:** Tori (implementer), HwaO (coordinator), Papa.
**Companion docs:** `job_schedule_v1.md` §9 (multi-model platoon), `research_ideas_design_v1.md` §16 (idea signals), `beat_schedule_v3.md` (active proposer model assignment).

---

## 1. The gap (live audit, 2026-05-16 09:25 KST)

DB query: `claims c LEFT JOIN research_idea_anchors a ON a.kind='claim' AND a.ref_id=c.id::text LEFT JOIN research_ideas ri ON ri.id=a.idea_id WHERE c.page_id=57 AND c.trust_level IN ('debated','challenged') GROUP BY c.id`:

| trust_level | n_claims | n_with_≥1_anchored_idea | n_with_≥3_anchored_ideas |
|---|---:|---:|---:|
| debated | 6 | 0 | 0 |
| challenged | 9 | 0 | 0 |
| **TOTAL** | **15** | **0** | **0** |

**Zero anchored ideas across all 15 contested claims.** A separate query via `research_ideas.claim_id` direct column finds 3 weak links (id=1488 has 2, id=1526 has 1, all others 0) — those 3 are kun-seed leftovers, not auto-generated.

### 1.1 Why Rakon's existing `rakon_draft_async` doesn't close this gap

Rakon's R2 lane (§9.2.1 in job_schedule_v1) drafts ideas at the **page level**: prompt includes "claims_block" (the top-10 claims by trust) + "arxiv_block" + "existing_block". Rakon picks whatever angle it finds interesting. Empirically, it gravitates toward consensus/accepted claims (broad-coverage ideas) rather than contested ones (claim-specific ideas), because the contested claims are noisier signal and the dedup floor knocks them out.

R3 `rakon_adversarial_probe` (§9.2.1) operates on **accepted** claims (oldest 3 — finds falsifying evidence), not debated/challenged ones. Wrong target.

What's missing is a lane that **iterates per debated claim**, prompts the LLM to generate ideas *anchored to that specific claim*, and writes `research_ideas.claim_id = <claim_id>` plus an anchor row (`kind='claim', ref_id='<claim_id>'`).

---

## 2. Design: `seed_debated_claim_ideas`

### 2.1 Function signature

New Celery task in `app/agent_loop/research_ideas/auto_improvement.py`:

```python
@shared_task(
    name="app.agent_loop.research_ideas.auto_improvement.seed_debated_claim_ideas",
    bind=True, max_retries=0,
)
def seed_debated_claim_ideas(self, page_id: int = 57, target_per_claim: int = 3):
    """Seed research ideas anchored to specific debated/challenged claims.
    Picks claims with < target_per_claim active ideas; generates targeted ideas per claim."""
```

### 2.2 Step-by-step logic

```
1. Acquire Mac Pro mutex (rakon:lock, TTL 4h) — fail-fast skip if held
2. Build candidate list:
     SELECT c.id, c.text, c.trust_level
     FROM claims c
     LEFT JOIN research_ideas ri
       ON ri.claim_id = c.id AND ri.status IN ('active','draft','saved')
     WHERE c.page_id = :page_id
       AND c.trust_level IN ('debated','challenged')
     GROUP BY c.id
     HAVING COUNT(ri.id) < :target_per_claim
     ORDER BY c.trust_level DESC, COUNT(ri.id) ASC, c.id ASC
     LIMIT 5   -- one tick processes at most 5 claims, mutex-bounded
3. For each candidate claim:
     a. Build per-claim context:
        - claim.text  (the contested statement)
        - 5 most-recent supporting/contradicting EvidenceLinks for that claim
        - 5 recent astro-ph.GA arxiv papers (cosine vs. claim.text)
        - existing ideas already anchored to this claim (to avoid dup)
     b. Call generate_ideas_for_claim(claim, ctx) — 3-5 candidate idea skeletons
     c. For each skeleton:
        - _validate_skeleton  (existing helper)
        - _atom_score vs. existing_block
        - if dedup_cosine ≥ DEDUP_COSINE_THRESHOLD → reject
        - if novelty < NOVELTY_FLOOR → reject
        - _persist_draft(db, page_id, skel, score, trigger='debated_claim_seed', cause_id=str(claim.id))
        - ALSO write research_idea_anchors row: (idea_id, kind='claim', ref_id=str(claim.id))
        - ALSO set research_ideas.claim_id = claim.id  (belt-and-suspenders linkage)
4. _log_autowiki_run(db, page_id, "debated_claim_seed",
                     idea_signals_json={"claims_visited":N, "ideas_generated":M,
                                         "per_claim_counts":{...}})
5. db.commit()
6. Release rakon:lock in finally
```

### 2.3 Cadence — every 6 h via beat schedule

`worker.py` `beat_schedule`:

```python
"debated-claim-seeder-6h": {
    "task": "app.agent_loop.research_ideas.auto_improvement.seed_debated_claim_ideas",
    "schedule": crontab(minute=15, hour="*/6"),  # :15 offset to avoid 04:00/12:00/20:00 collisions
    "kwargs": {"page_id": 57, "target_per_claim": 3},
},
```

Rationale (capacity math from §9.5.1):
- 5 claims/tick × 3 ideas/claim × 1.34 h Rakon/idea = up to **20 h Mac Pro/tick worst-case**. Hard skip via `rakon:lock` if it overruns.
- Realistic median: 5 × 2 ideas committed × 1.0 h = **10 h Mac Pro/tick**.
- 4 ticks/day × 10 h = 40 h/day median — **over-prescribed** to ensure backlog drain when Rakon is healthy; `rakon:lock` absorbs.
- 15 claims × 3 ideas = 45 idea-slots to fill. At 5 successful drafts/tick, **filled in 9 ticks ≈ 2.25 days**.

Once the gap is closed, the task self-throttles: candidate query returns 0 rows → task no-ops in <100ms.

### 2.4 Per-claim trigger (event-driven, in addition to cron)

In `autowiki/tasks.py` post-commit dispatcher, after the existing J1 dispatch block (around line 814), add:

```python
# §16 — when an autowiki tick promotes a claim to 'debated' or 'challenged',
# fire the seeder for just that page right away (don't wait for the 6h tick).
if _phase3_on and proposal_type == "claim_insert_debate":
    seed_debated_claim_ideas.delay(page_id=page_id, target_per_claim=3)
```

Also fire when a stance jury **demotes** an accepted claim to debated — currently `settle_evidence_and_update_rep` writes the trust_level change. Add at the end of its loop (after the trust_level update commit):

```python
if new_trust_level in ('debated', 'challenged') and old_trust_level not in ('debated', 'challenged'):
    seed_debated_claim_ideas.delay(page_id=claim.page_id, target_per_claim=3)
```

Together: cron sweeps every 6 h **plus** event-driven seeding immediately after a claim becomes contested.

### 2.5 Prompt for per-claim idea generation

New prompt constant in `auto_improvement.py`:

```python
DEBATED_CLAIM_SEEDER_PROMPT = """\
You are an astronomy research strategist. A specific claim on the Wikipedia-style page
"{page_title}" is currently {trust_level}. Generate {n_ideas} testable research
questions that would help resolve this specific disagreement.

THE CONTESTED CLAIM
-------------------
{claim_text}

EVIDENCE ALREADY ON FILE FOR THIS CLAIM
---------------------------------------
{evidence_block}

RECENT RELEVANT LITERATURE (last 12 mo)
---------------------------------------
{arxiv_block}

EXISTING IDEAS ALREADY ANCHORED TO THIS CLAIM (avoid duplicating)
-----------------------------------------------------------------
{existing_anchored_block}

REQUIREMENTS
------------
For each idea:
- question: a 1-2 sentence research question that would discriminate between the
            disputed positions. Must reference the specific claim.
- why_now: 1 sentence on what makes this answerable in 2024-2026 (new instrument,
           new dataset, new theoretical framework).
- approach: 1-2 sentences naming the concrete dataset, survey, simulation suite,
            or experimental technique. Must be a REAL named dataset/instrument.
- novelty: do NOT propose ideas covered by the existing anchored ideas above.

Return JSON: {"drafts": [{"question": "...", "why_now": "...", "approach": "...",
                          "systematics_json": {...}}, ...]}
"""
```

Three-part Δ from the existing `RAKON_DRAFT_PROMPT`: (a) page-level context shrunk to per-claim, (b) explicit "must discriminate between positions" framing, (c) hard rule against duplicating anchored ideas.

### 2.6 Why this isn't a configuration tweak to `rakon_daily_idea_draft`

I considered adding "prefer contested claims" to the existing R2 prompt. Reasons against:

1. R2 generates page-wide ideas (3-5 per tick). Targeting individual claims would need 5× the calls per tick (one per claim) and reshape the output schema. Cleaner as a separate task.
2. R2's prompt already has 5 input blocks (claims, debates, arxiv, ideas, hero). Adding "per-claim emphasis" makes the prompt longer and the output less focused.
3. Separation lets each lane have its own dedup floor / novelty floor calibrated to its target. Per-claim ideas need a stricter novelty floor against the claim's anchored set, not against the whole page.

So: new lane, dedicated prompt, dedicated trigger.

---

## 3. Platoon Assignment (per Papa's standing rule)

| Step | Model | Why this model | Fallback |
|---|---|---|---|
| 1. Build candidate list (SQL) | none | pure aggregation, <100ms | — |
| 2. Build per-claim context | none | SQL only | — |
| 3. **Generate per-claim ideas** | **Rakon (deepseek-r1:671b, Mac Pro)** | the **most important step** — needs the deepest reasoning to find research questions that discriminate between contested positions. Galaxy-evolution debates ARE the hard parts of the field; structural reasoning > token-prediction here. ~1.34 h median per call. | **Buddle (deepseek-r1:32b)** if Rakon mutex held — same architecture, faster but shallower. **Mima (qwen3:30b)** if Mac Pro entirely down — different attention pattern; weaker on long structural reasoning but reliable on Mac Studio. |
| 4. Validate skeleton | none | Python regex/schema check | — |
| 5. Score (dedup + novelty + feasibility) | **Atom-7b** (vanta/atom-astronomy-7b) | astronomy-domain classifier, fast (~2s/skeleton), existing helper. | none — if Atom unreachable, log warning and persist without score |
| 6. Persist + link | none | SQL inserts | — |
| 7. Log (`_log_autowiki_run`) | none | DB write | — |
| Downstream JI promotion (existing pipeline) | Takji → AstroSage polish | already in place per §8.2.3 | — |

**Why Rakon and not Sonnet here?** Sonnet's strengths are prose quality + speed (cloud). For idea-generation against contested astronomy claims, Rakon's structural reasoning depth > Sonnet's general intelligence. Sonnet's strength on section_rewrite (v3 spec) doesn't translate to dispute-resolution idea generation. Also: Sonnet costs ~$0.02/call × 5 claims × 3 ideas × 4 ticks/day = $1.20/day for marginal quality gain over Rakon (free, local). Cost-benefit favors Rakon.

**Why not Tera (gemma3:27b, 128 k context)?** Tera's value is long-context aggregation (whole-page-in-prompt). Per-claim context is small (~3 k chars per claim). Tera's strength is wasted here; Rakon's depth wins.

---

## 4. Acceptance criteria

After Tori lands the task + beat + post-commit trigger:

1. **Within 12 h** of deploy: at least 3 of the 15 debated/challenged claims on page 57 have **≥ 1 anchored active or draft research idea** (currently 0/15).
2. **Within 48 h**: at least 10 of the 15 claims have **≥ 1 anchored idea**.
3. **Within 5 days**: all 15 claims meet the **≥ 3 anchored ideas** target. Query:
   ```sql
   SELECT c.id, c.trust_level, COUNT(ri.id) AS n_ideas
   FROM claims c
   LEFT JOIN research_ideas ri ON ri.claim_id = c.id AND ri.status IN ('active','draft','saved')
   WHERE c.page_id = 57 AND c.trust_level IN ('debated','challenged')
   GROUP BY c.id, c.trust_level
   HAVING COUNT(ri.id) < 3;
   -- expected: 0 rows
   ```
4. **No regression**: the existing R2 `rakon_daily_idea_draft` continues to produce ideas at its prior rate. Verify in `autowiki_runs WHERE proposal_type = 'research_ideas_weekly' OR proposer = 'rakon→…'`.
5. **Audit trail**: every `seed_debated_claim_ideas` tick produces one `autowiki_runs` row with `proposal_type='debated_claim_seed'` and a populated `idea_signals_json`.

---

## 5. Tori implementation checklist

### 5.1 Code changes (3 files)

| File | Change |
|---|---|
| `auto_improvement.py` | Add `seed_debated_claim_ideas` task body (§2.2). Add `DEBATED_CLAIM_SEEDER_PROMPT` constant (§2.5). Add helper `_generate_ideas_for_claim(claim, ctx)` that wraps the Rakon→Buddle→Mima fallback chain and returns a list of skeleton dicts. |
| `worker.py` | Add `debated-claim-seeder-6h` beat entry (§2.3). Add `"app.agent_loop.research_ideas.auto_improvement.seed_debated_claim_ideas": {"queue": "autowiki"}` to `task_routes`. |
| `autowiki/tasks.py` | Add the post-commit trigger for `claim_insert_debate` (§2.4) — one line below the existing J1 dispatch. |
| `tasks.py` (legacy) | At the end of `settle_evidence_and_update_rep`, add the demotion trigger (§2.4) — fires when a previously-accepted claim is voted down to debated/challenged. |

### 5.2 Schema (no migration needed)

The task uses existing tables only:
- `research_ideas.claim_id` (existing column)
- `research_idea_anchors(idea_id, kind='claim', ref_id=str(claim.id), created_at)` (existing)
- `autowiki_runs(proposal_type='debated_claim_seed', idea_signals_json)` (existing)

### 5.3 Tests

- Unit: candidate-list SQL returns expected count for a fixture page with 5 debated + 10 accepted claims, 2 ideas anchored to one of the debated.
- Integration: dispatch `seed_debated_claim_ideas.delay(57, 3)` once, wait 5 min, query `autowiki_runs` for one new row + at least 1 new `research_ideas` row with `claim_id IS NOT NULL`.
- Fallback: with `rakon:lock` set externally, the task should fall to Buddle and still produce ideas (verify `model_chain` on the resulting `research_ideas` row).

### 5.4 Acceptance gates for the PR

1. `pytest backend/tests/test_debated_claim_seeder.py` passes.
2. Manual `celery -A app.agent_loop.worker.celery_app call seed_debated_claim_ideas --args '[57, 3]'` returns within 30 min with at least 1 idea generated.
3. `celery -A app.agent_loop.worker.celery_app inspect registered | grep seed_debated_claim_ideas` shows the task on both workers.

---

## 6. Risks + mitigations

| Risk | Mitigation |
|---|---|
| Rakon mutex contention starves the existing R2 lane | `rakon:lock` TTL is 4 h for seeder vs 8 h for R2 — seeder yields naturally |
| 15 claims × 3 ideas = 45 calls overwhelms cloud API budget if Mac Pro down → falls all the way to cloud | The fallback chain is Rakon → Buddle → Mima, all LOCAL. No cloud spillover by design. |
| Per-claim prompt produces noisy ideas (claim text is debated → harder to reason about) | Atom-7b dedup + novelty floor (existing) + Takji methodology verify (in JI promote step §8.2.3) catches noise downstream. |
| The 15 claims drift back below 3 ideas if some get retired by §10 J11 coverage detection | Cron tick re-fires every 6 h; gap is detected and refilled automatically. Self-healing by design. |

---

## 7. What this design does NOT do

- It does **not** modify R2 `rakon_daily_idea_draft` (page-level drafting stays as is).
- It does **not** add new tables or columns.
- It does **not** change the JI promotion pipeline — drafts produced here flow through the existing Atom → Takji → AstroSage polish → Opus judge chain (§8.2.3).
- It does **not** extend to non-debated claims. Accepted-claim ideas come from R2 + R3 (adversarial) + J1 (per-commit Nutty).

— 🔬 Kun
