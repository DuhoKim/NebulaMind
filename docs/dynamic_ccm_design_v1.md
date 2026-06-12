# Dynamic Citation Context Mining (DCCM) — Design v1

**Author:** Kun (analyst)
**Date:** 2026-06-08
**Status:** Draft for HwaO review → Tori implementation. **Contains two BLOCKING prerequisites (§2) that must be resolved before DCCM is enabled.**
**Live grounding:** Read against the committed CCM system on Mac Studio (`Duhoui-MacStudio.local`) on 2026-06-08. CCM v1 is live: 75 `evidence` rows with `source_channel='citation_context_mining'` across the 12 Page-57 seminal claims; 13 `trust_audit_log` rows with `trigger='ccm_citation_context'`. The FK-import fix I flagged in the CCM audit is present (`miner.py:19 import app.models.jury`). Empirical `evidence` snapshot: 11,997 rows, 1,335 distinct `ads_bibcode`, 11,444 `peer_reviewed=True`, 10,878 `stance='supports'`.

---

## 0. Relationship to CCM v1

CCM v1 (`docs/citation_context_mining_design_v1.md`, `app/agent_loop/citation_context/miner.py`) mines modern citers of a **static, hand-curated** `seminal_claim_map` (16 rows). DCCM generalizes the *seed set* from 16 curated bibcodes to **the live `evidence` table itself**, and inverts the trigger: instead of a scheduled sweep over fixed seeds, DCCM fires **on ingestion of each new paper**, checking whether that paper's bibliography intersects our existing evidence.

DCCM **reuses CCM's proven machinery wholesale**: the `CitationContext` dataclass, `classify_context` (Pico), `insert_supportive_evidence`, `already_attached`/`ccm_already_linked` dedup, the partial unique index, and the `recalculate_trust_v2` audit path. DCCM is **not** a rewrite; it is a new seeding+trigger layer (`app/agent_loop/citation_context/dynamic.py`) on top of the same insert/classify/trust core.

This document will not restate CCM internals that are unchanged. It focuses on the seven required areas and, critically, on the two systemic defects that DCCM would amplify.

---

## 1. The Central Epistemic Question (read before the architecture)

CCM v1 is safe *because its seeds are curated*. A human (me) verified that each of the 16 bibcodes is a genuine foundational result whose modern introductory citations constitute real endorsement. DCCM removes that human gate: **every paper in `evidence` becomes a consensus-tracking seed automatically.** That is powerful and it is also where the epistemic risk concentrates.

The proposal's mechanism — "if a new paper's bibliography cites a paper already in our evidence table, and Pico calls the citing sentence SUPPORTIVE, append the new paper as supporting evidence and let trust recompute" — has a failure mode that does not exist in CCM v1:

> **Transitive consensus drift.** Claim C is backed by evidence paper A. New paper B cites A. DCCM links B to C as new support. But B citing A does **not** mean B supports claim C — B may cite A for an unrelated result, or to *dispute* A, or A itself may be a weak/non-refereed seed that should never have anchored a green claim. Generalized naively, "consensus" degrades from *agreement among the literature* into *a citation-popularity count*.

This is not a reason to reject DCCM. It is the reason the design must impose **seed-eligibility gates**, **claim-relevance gates** (not just paper-cites-paper), and **a hard floor that no claim greens on transitive intro-citations alone**. These are specified in §8 and §9 and are non-negotiable. I state this up front so reviewers evaluate the architecture against the risk it actually carries, not the happy path.

---

## 2. 🔴 BLOCKING PREREQUISITES (must fix before DCCM is enabled)

I discovered both of these while grounding this design against the live committed system. **Neither is hypothetical; both are reproduced below against live data.** DCCM cannot be safely enabled until both are resolved, because DCCM's entire value proposition is *self-reinforcing real-time consensus* (deliverable #6), and both defects directly attack that proposition.

### 2.1 Trust-write fragmentation — the stored `trust_level` already diverges from the audited truth

**Reproduced, live, 2026-06-08:** For the 12 committed CCM claims, the `trust_audit_log` and a fresh call to `recalculate_trust_v2` both report **11/12 = consensus** (claim 1632 correctly `accepted`). But the persisted `claims.trust_level` **column** reads `accepted` for **10 of the 12** — i.e. the column is stale relative to the audited recalculation. Raw SQL (not ORM cache) confirms: claim 1630 has `trust_level='accepted'`, `trust_score=0.7986`, `trust_score_updated_at=01:38:12`, while its last `trust_audit_log` row (`new_level='consensus'`) is timestamped `01:35:18`. **A write at 01:38 changed the column without emitting an audit row** — i.e. some path persisted trust outside the audited `recalculate_trust_v2`.

Root cause — **there are at least three competing trust-write paths**, and they disagree on whether `consensus` is even reachable:

| Writer | Location | Reaches `consensus`? | Writes audit row? |
|---|---|---|---|
| **v2 calculator** | `app/routers/claims.py:recalculate_trust_v2` | **Yes** (votes-aware: `V` from `EvidenceVote`) | Yes |
| **v1 calculator** | `app/services/trust_calculator.py:recalculate_trust` | **No** — `V` is hardwired to `0.0` (line 42), so `TS = 0.45·E + 0.10·T` saturates near ~0.45 and caps at `accepted` | Only on level change |
| **Direct demotion** | `app/agent_loop/tasks.py:run_temporal_decay` (line 4439) | n/a — writes `claim.trust_level = "accepted"` / `"unverified"` directly | **No** |

The v1 calculator is still invoked by ingestion-adjacent code: `app/services/arxiv_ingest.py:224`, the evidence-POST endpoint (`routers/claims.py:418`), the vote endpoint (`routers/claims.py:440`), and `tasks.py:1552`. Whichever path last touches a CCM/DCCM claim **wins the column**, and if that path is v1, the claim is silently demoted from `consensus` to `accepted` even though the votes-aware truth is `consensus`.

> Aside: `arxiv_ingest.py:224` does `from app.agent_loop.tasks import recalculate_trust` — which **raises `ImportError`** (no such symbol in that module; verified) and is swallowed by a bare `except Exception: pass`. So that particular trust hook is currently a **silent no-op**. This is its own bug, but it also means the demotion is coming from the other v1 call sites and the decay task, not from arXiv ingest today. Once DCCM starts touching these claims on every relevant ingestion, the v1/direct writers will demote freshly-greened claims continuously.

**Why this blocks DCCM specifically:** DCCM's premise is that growing literature citations push claims to green *and keep them there*. If a v1 recalc or the decay task can silently overwrite `consensus → accepted` with no audit trail, then DCCM will spend Pico cycles greening claims that a competing writer un-greens minutes later — an oscillation with no observability. We saw the column already wrong on day one with only CCM running; DCCM multiplies the write frequency by orders of magnitude.

**Required fix (prerequisite P1):** Establish **`recalculate_trust_v2` as the single sanctioned trust-write path.**
1. Replace the v1 `recalculate_trust` call sites (`arxiv_ingest.py`, `routers/claims.py:418/440`, `tasks.py:1552`) with `recalculate_trust_v2(claim_id, db, trigger=...)`. Fix the dead import in `arxiv_ingest.py`.
2. Make `run_temporal_decay` route demotions **through** `recalculate_trust_v2` (or at minimum emit a `trust_audit_log` row), so no level change is ever unaudited.
3. Add an invariant test: after any trust write, `claims.trust_level` equals the level implied by the latest `trust_audit_log` row for that claim.
4. One-time reconciliation: run `recalculate_trust_v2` over the 12 CCM claims to repair the stale column (expected result: 11 flip to `consensus`).

### 2.2 Per-claim insert cap is not enforced across runs

**Reproduced:** claim 1630 carries **11** `citation_context_mining` evidence rows, exceeding the `CCM_MAX_EVIDENCE_PER_CLAIM_PER_RUN = 6` cap. CCM's `inserted_by_claim` counter is per-*process*, not per-*claim-lifetime* (verified in `run_ccm_cycle`), so repeated `--commit` runs stack rows. For CCM (16 seeds) this is cosmetic. For **DCCM, which re-touches the same claim on every intersecting ingestion**, an unbounded per-claim accumulation will (a) inflate the E-component unboundedly, (b) make the quality clamp meaningless, and (c) bloat the references UI.

**Required fix (prerequisite P2):** Enforce a **lifetime** cap per `(claim_id, source_channel)` checked against the DB (`SELECT count(*) ... WHERE claim_id=:c AND source_channel='dynamic_ccm'`), not an in-process counter. Specified in §8.3.

---

## 3. Stage 1 — Dynamic Seeding Architecture

DCCM replaces the static `seminal_claim_map` lookup with a **live view over `evidence`**. Conceptually, every eligible evidence row is a seed: "papers that cite *this* paper, in their introduction, in a supportive way, are candidate new support for *this paper's claim*."

### 3.1 Seed eligibility — the first safety gate (do NOT seed from everything)

Generalizing to all 1,335 distinct bibcodes is the risk in §1. We constrain the seed set to evidence that is itself trustworthy enough to anchor transitive support:

```sql
-- A seed is an (evidence_id, claim_id, bibcode/doi) that is eligible to attract
-- new supporting citers. Eligibility is deliberately strict.
CREATE VIEW dccm_seed_candidates AS
SELECT e.id AS evidence_id, e.claim_id, e.ads_bibcode, e.doi, e.arxiv_id,
       e.year, e.quality, e.citation_count_cache
FROM evidence e
JOIN claims c ON c.id = e.claim_id
WHERE e.stance = 'supports'
  AND e.peer_reviewed = TRUE
  AND e.quality >= 0.50                 -- no weak/low-quality anchors
  AND (e.ads_bibcode IS NOT NULL OR e.doi IS NOT NULL)
  AND c.claim_type <> 'debate'          -- never auto-reinforce a debate stance
  AND COALESCE(c.human_trust_override_locked, FALSE) = FALSE;  -- respect human locks
```

Rationale per clause:
- `stance='supports'` + `peer_reviewed` + `quality≥0.50`: a transitive endorsement is only as good as the paper it flows through. A non-refereed or low-quality seed cannot manufacture consensus.
- `claim_type<>'debate'`: debate claims must never be auto-pushed toward agreement; their bucket is decided by `_bucket_debate`, and DCCM stays out.
- `human_override_locked=FALSE`: a human pin is sacrosanct; DCCM never feeds a locked claim.

This is the structural analogue of CCM's curation: instead of a human picking 16 bibcodes, DCCM admits ~the refereed-supports subset and lets the downstream Pico+gate stack do the per-citation rigor.

### 3.2 Seed index (materialized for intersection speed)

Bibliography intersection (Stage 3) must be O(1) per cited reference. Maintain a lookup table keyed by normalized identifier:

```sql
CREATE TABLE dccm_seed_index (
    id            SERIAL PRIMARY KEY,
    norm_id       VARCHAR(120) NOT NULL,   -- normalized bibcode OR 'doi:<lower doi>'
    id_kind       VARCHAR(10)  NOT NULL,   -- 'bibcode' | 'doi' | 'arxiv'
    evidence_id   INT NOT NULL REFERENCES evidence(id) ON DELETE CASCADE,
    claim_id      INT NOT NULL REFERENCES claims(id)  ON DELETE CASCADE,
    eligible      BOOLEAN NOT NULL DEFAULT TRUE,
    refreshed_at  TIMESTAMP DEFAULT NOW(),
    UNIQUE (norm_id, evidence_id)
);
CREATE INDEX ix_dccm_seed_index_norm ON dccm_seed_index(norm_id) WHERE eligible;
CREATE INDEX ix_dccm_seed_index_claim ON dccm_seed_index(claim_id);
```

A nightly Celery task `refresh_dccm_seed_index` repopulates from `dccm_seed_candidates` (one bibcode can map to several `(evidence_id, claim_id)` rows — the fan-out is intentional and capped at intersection time, §3.3). Empirically the index is ~the eligible subset of 1,335 bibcodes × their claim links — small, fully in-memory cacheable.

### 3.3 Fan-out cap

Some bibcodes back many claims (live: `2016PhRvL.116f1102A` and `2016Natur.536..437A` each link to 44 claims — these are the LIGO GW150914 discovery papers, cited everywhere). A single incoming paper citing such a hub must **not** fan out to 44 claims. Cap fan-out per cited seed to `DCCM_MAX_CLAIMS_PER_SEED = 3`, ranked by claim-relevance score (§4.4). A hub citation is weak evidence for any *one* specific claim precisely because it is generic; the cap encodes that.

---

## 4. Stage 2 — Bibliographic Ingestion Hook

### 4.1 Where DCCM fires

DCCM triggers when a new paper enters the system with a resolvable identifier. The existing ingestion surfaces (verified): `app/agent_loop/arxiv_fetch.py:fetch_arxiv_daily`, `app/services/arxiv_ingest.py`, and `targeted_ads_miner`. DCCM adds a **post-ingestion hook** that runs *after* the paper's own evidence row is committed, so the new paper is already in the system before we mine its bibliography.

The hook enqueues an isolated Celery task (does not block ingestion):

```python
# at the end of arxiv_ingest insert path, after db.commit():
from app.agent_loop.citation_context.dynamic import dccm_process_paper
dccm_process_paper.delay(arxiv_id=arxiv_id, doi=doi, bibcode=bibcode)
```

### 4.2 Bibliography extraction — ADS primary, S2 fallback

We have a paid ADS token and `references()` works (verified live): `references(bibcode:"2026MNRAS.548ag650S")` returned 30 cited papers, **including `1978MNRAS.183..341W` (White & Rees) and `2013ApJ...770...57B` (Behroozi)** — both already in our evidence table. This is the intersection DCCM depends on, proven against real data, with `X-RateLimit-Remaining: 812` headroom.

New function in `app/services/paper_search.py` (extends, mirrors `ads_citing_papers`):

```python
def ads_reference_bibcodes(bibcode: str, *, rows: int = 200) -> list[PaperRecord]:
    """Return the BIBLIOGRAPHY (papers cited BY `bibcode`) via ADS references() op."""
    if not settings.ADS_API_KEY:
        raise PaperSearchError("ADS_API_KEY not configured")
    q = f'references(bibcode:"{bibcode}")'
    params = {"q": q, "fl": ADS_FIELDS, "rows": rows, "sort": "date desc",
              "fq": "database:astronomy"}
    # ... same auth/request/_ads_to_record path as ads_citing_papers ...
```

**S2 fallback** (`/paper/{id}/references`, fields `contexts,intents,citedPaper.externalIds,...`) is used when the incoming paper has an arXiv ID but no ADS bibcode yet (very recent preprints). S2's free tier is **429-prone** (observed live in the worker log), so S2 is fallback-only and must honor `Retry-After`; never the primary path.

### 4.3 Identifier normalization

ADS bibcodes, DOIs, and arXiv IDs must normalize to the same key space as `dccm_seed_index.norm_id`. Reuse CCM's `normalize_text` discipline plus a dedicated `normalize_identifier()` (lower-case DOI; strip `arXiv:`; canonical bibcode). The DOI form must match how `to_evidence_dict` stored it (verified: `evidence.doi` is the bare DOI).

### 4.4 Claim-relevance pre-score (the second safety gate)

Before extracting any context, score how relevant the incoming paper is to the *claim*, not merely whether it cites the seed paper. Reuse CCM's keyphrase mechanism, but since DCCM claims have no hand-authored keyphrases, derive them on the fly from the claim text (top TF-IDF noun phrases, cached on the claim). A citing paper whose title+abstract shares `< 1` claim keyphrase is dropped pre-Pico, exactly as CCM's on-topic gate (`keyphrase_hits < 1`). This is what stops a paper that cites White & Rees for an unrelated reason from being scored against the cooling claim.

---

## 5. Stage 3 — Citation Intersection Resolver

### 5.1 Algorithm

```
dccm_process_paper(new_paper):
  refs = ads_reference_bibcodes(new_paper.bibcode)         # bibliography
  if not refs: refs = s2_references(new_paper.arxiv_id)    # fallback
  hits = []
  for r in refs:
      for key in normalize_identifier(r):                  # bibcode/doi/arxiv forms
          seeds = dccm_seed_index.lookup(key, eligible=True)   # O(1)
          for seed in seeds[:DCCM_MAX_CLAIMS_PER_SEED]:    # fan-out cap, relevance-ranked
              if not ccm_already_linked(db, seed.claim_id, new_paper_record):
                  hits.append((seed, r))
  # de-dup: one (claim_id, new_paper) pair even if it cites several of the claim's seeds
  hits = dedup_by(seed.claim_id, new_paper.key)
```

Key correctness point: **a new paper citing three different seed-papers of the same claim is ONE piece of evidence for that claim, not three.** Dedup by `(claim_id, new_paper_identifier)` before context extraction. (CCM did not need this because each seed was a distinct claim binding; DCCM does because seeds collapse onto shared claims.)

### 5.2 Mapping back to `claim_id`

`dccm_seed_index` already carries `claim_id`, so the resolver yields `(claim_id, seed_evidence_id, new_paper_record, cited_bibcode)` tuples directly. The `seed_evidence_id` is retained for the audit trail (which existing paper's citation pulled the new one in).

---

## 6. Stage 4 — Context Extractor Cascade

Identical to CCM v1's cascade, with the same Tier-A starvation caveat I documented in the CCM audit (`docs/ccm_full_audit_report_v1.md §7.1`) — and DCCM has a structural advantage here:

- **Tier A — S2 citation contexts.** For DCCM we query S2 from the **citing (new) paper's** side: `/paper/{new_id}/references?fields=contexts,intents,citedPaper.externalIds`. The `contexts` for the matched `citedPaper` (the seed) is exactly the pinpoint sentence where the new paper cites our seed. **This is more precise than CCM's citer-side lookup** because we already hold the citing paper and ask directly for its reference contexts — the join is on a single paper, not a 2024+ filtered citer set. This should materially raise the Tier-A hit rate above CCM's ~20%.
- **Tier B — abstract proxy.** The new paper's abstract, when S2 has no context.
- **Tier C — arXiv intro extraction (`ar5iv`), capped.** Reuse `extract_arxiv_intro_context`, searching for the seed paper's author-surname+year token in the new paper's introduction.

Output is CCM's existing `CitationContext` dataclass (unchanged), with `context_source ∈ {s2_context, abstract, arxiv_intro}` and the seed's `seminal_label`/`bibcode` populated from the matched evidence row.

---

## 7. Stage 5 — Pico (Atom-7B) Prompt Tuning

CCM's classifier prompt assumes the cited work is a *settled foundational* result. DCCM's seeds are often **recent, still-contested research** (2020–2025). The prompt must not assume the cited work is textbook-settled, and must distinguish "builds on this recent result" from "notes this recent result among alternatives."

### 7.1 Refined system prompt (`ccm_dynamic_classifier`, policy `dccm_v1`)

Changes from CCM's `ccm_intro_classifier` (registered separately in `PromptRegistry`, versioned/hashed):

```
You are a precise astronomy citation-context classifier for a knowledge base.

You are given:
  CLAIM: an astronomy statement (it may be recent and still under active study,
         NOT necessarily a settled textbook fact).
  CITED WORK: a paper already in our evidence base that the CLAIM relies on.
  CITATION CONTEXT: one sentence from a NEWER paper that cites the CITED WORK.

Decide how the newer sentence uses the cited work, WITH RESPECT TO THE CLAIM:

  SUPPORTIVE   - The newer paper adopts, confirms, extends, or builds on the
                 cited result as a premise it accepts, AND the sentence concerns
                 the CLAIM's specific subject. Recent corroboration counts.

  NONSUPPORTIVE - The newer paper disputes, revises, contrasts, fails to
                 reproduce, or finds tension with the cited result.

  OFFTOPIC     - The citation is generic/list-style, or concerns a different
                 result of the cited work unrelated to the CLAIM, or merely
                 acknowledges existence without endorsing the CLAIM's substance.

Hard rules:
1. Judge ONLY the provided sentence. No outside knowledge about either paper.
2. SUPPORTIVE requires endorsement of the CLAIM's SUBSTANCE, not mere topical
   overlap. "We also study X" is OFFTOPIC, not SUPPORTIVE.
3. For RECENT/contested claims, be MORE conservative: if the sentence lists the
   cited work alongside competing results without committing, choose OFFTOPIC.
4. Any disputing or "in tension with" framing => NONSUPPORTIVE.
5. Output ONLY the final block.

Output EXACTLY:
###LABEL: <SUPPORTIVE|NONSUPPORTIVE|OFFTOPIC>
###CONFIDENCE: <LOW|MEDIUM|HIGH>
```

The decisive additions are rules 2–3: because DCCM's claims are recent and its citations are abstract-heavy (Tier-B fallback), Pico must resist crediting topical-but-noncommittal sentences. My CCM audit found a HIGH-confidence skew under abstract-mode classification (256/263 HIGH); rule 3 plus the LOW→hold escalation (unchanged from CCM) is the counterweight. **Calibrate this prompt before enable** with a labeled set (§10).

### 7.2 Quality mapping (tightened for transitive evidence)

DCCM's quality clamp is **stricter** than CCM's, because transitive intro-citations of recent work are weaker evidence than intro-citations of textbook foundations:

| Pico LABEL | CONFIDENCE | Action | `quality` |
|---|---|---|---|
| SUPPORTIVE | HIGH | insert `supports` | **0.72** (CCM: 0.80) |
| SUPPORTIVE | MEDIUM | insert `supports` | **0.60** (CCM: 0.68) |
| SUPPORTIVE | LOW | hold → escalate to full jury | — |
| NONSUPPORTIVE | any | drop; emit `dccm_challenge_candidate` | — |
| OFFTOPIC | any | drop | — |

Lower ceilings mean DCCM evidence contributes to `E` but cannot by itself saturate it — which feeds directly into the §9 hard floor.

---

## 8. Stage 6 — Self-Reinforcing Recalculation

### 8.1 The trigger (only after P1 is fixed)

After DCCM inserts its capped `supports` rows for a claim, it calls the **single sanctioned writer**:

```python
recalculate_trust_v2(claim_id, db, trigger="dccm_citation_context",
                     actor_agent_id=dccm_agent_id)
```

`recalculate_trust_v2` recomputes E/V/T/H, buckets, applies the freshness floor, persists, and audits — exactly as CCM. The `EvidenceVote` written per DCCM row (Pico verdict, `value=1`) contributes to V, just as in CCM. **This is the "self-reinforcing" mechanism: as more papers cite a claim's seed papers supportively, n_supports and V rise, and the claim crosses 0.75.**

### 8.2 Why P1 (§2.1) is a hard precondition for this stage

"Self-reinforcing real-time consensus" is only coherent if `consensus` is **stable** under the system's other writers. Today it is not: a v1 recalc or the decay task can silently revert `consensus → accepted`. If DCCM greens a claim at 10:00 and an unrelated arXiv ingest runs a v1 recalc at 10:05, the claim un-greens with no audit row — and DCCM, seeing it non-green, may re-mine and re-insert on the next intersecting paper, an oscillation. **Unifying on `recalculate_trust_v2` (P1) is what makes the self-reinforcing loop converge instead of flap.**

### 8.3 Lifetime insert cap (P2) and idempotency

`dccm_process_paper` checks the **DB-backed lifetime count** before inserting:

```python
existing = db.query(func.count(Evidence.id)).filter(
    Evidence.claim_id == claim_id,
    Evidence.source_channel == "dynamic_ccm").scalar()
budget = max(0, DCCM_MAX_EVIDENCE_PER_CLAIM_LIFETIME - existing)   # default 10
```

Combined with `ccm_already_linked` dedup and the partial unique index (extended to cover `source_channel='dynamic_ccm'`), reprocessing the same paper is a no-op, and a claim's DCCM-sourced support is bounded for life.

---

## 9. Stage 7 — Anti-False-Consensus & Concurrency Guards

### 9.1 The hard floor: no green on transitive evidence alone

**The single most important guard.** A claim must **not** reach `consensus` if its supporting evidence is *entirely* transitive intro-citations (CCM + DCCM channels) with **zero primary, jury-verified support**. Concretely, add to the consensus bucket test (in `recalculate_trust_v2`, gated behind a config flag so it is reviewable):

```python
PRIMARY_CHANNELS = {"targeted_ads_miner", "arxiv_ingest", "manual"}
has_primary = any(e.stance == "supports" and e.source_channel in PRIMARY_CHANNELS
                  for e in evidence)
# consensus additionally requires at least one primary support OR a human nudge
if new_level == "consensus" and not has_primary and not claim.human_trust_override:
    new_level = "accepted"   # transitive-only evidence caps at accepted
```

This directly answers §1: citation popularity alone cannot green a claim; there must be at least one piece of evidence that was vetted *for that claim's substance* by the jury or a human. DCCM accelerates claims that already have a real anchor; it does not invent consensus from a citation graph. **(For the 12 CCM claims this is satisfied — they retain their original curated evidence.)**

### 9.2 Preserve `n_challenges == 0`

Unchanged and inviolable. DCCM never writes `challenges` rows; NONSUPPORTIVE citations are dropped (and optionally routed to a separate challenge pipeline). The existing gate means even a Pico false-positive cannot green a claim that has any real challenge on record.

### 9.3 Concurrency / race guards (bulk parallel ingestion)

DCCM fires per-ingestion, and ingestion is parallel (multiple Celery workers). Guards:
- **Per-claim advisory lock.** Before insert+recalc for a claim, acquire a Postgres advisory lock `pg_advisory_xact_lock(hashtext('dccm:claim:'||claim_id))`. Serializes concurrent DCCM writers on the *same* claim without blocking different claims. Released at transaction end.
- **Partial unique index** (extends CCM's): `UNIQUE (claim_id, ads_bibcode) WHERE source_channel='dynamic_ccm'` — DB-level dedup under races; insert uses `ON CONFLICT DO NOTHING`.
- **Idempotent task.** `dccm_process_paper` keyed by the new paper's identifier; a `dccm_runs` row (mirroring `ccm_runs`) records processed papers so a retried task is a no-op.
- **Recalc-once.** Within one `dccm_process_paper`, recalc each affected claim exactly once after all inserts, not per row (bounds recalc storms when a paper hits several claims).
- **Decay/recalc ordering.** Because trust now flows only through v2 (P1), the decay task and DCCM cannot disagree on the column; the advisory lock plus single-writer invariant prevents lost updates.

### 9.4 Rate-limit discipline

ADS `references()` is one call per ingested paper (~hundreds/day given `ARXIV_INGEST_MAX_PER_RUN=50` and daily cadence) — far under the 5,000/day quota (observed `X-RateLimit-Remaining: 812` mid-day). Read the header; if `< DCCM_ADS_RL_FLOOR (200)`, defer remaining papers to the next beat. S2 fallback honors `Retry-After` (429 observed live). Pico runs off-peak relative to the stance-jury beats, with the 0.3 s inter-call sleep and `InferenceScheduler` advisory lock (CCM discipline, unchanged).

### 9.5 Observability

Every DCCM transition is auditable: `trust_audit_log.trigger='dccm_citation_context'`, `evidence.source_channel='dynamic_ccm'`, `evidence.summary` = verbatim context sentence, the Pico `EvidenceVote`, and a `dccm_runs` row linking new-paper → seed-evidence → claim. Add a weekly Kun review (heartbeat) of: claims greened by DCCM, transitive-only-blocked count (§9.1 firings), and Tier-A/B ratio.

---

## 10. Implementation Plan & File Manifest

**Phase 0 — Prerequisites (BLOCKING, must merge first):**
- P1: unify trust writes on `recalculate_trust_v2`; fix `arxiv_ingest.py` dead import; audit-route `run_temporal_decay`; invariant test; reconcile the 12 CCM claims. (§2.1)
- P2: DB-backed lifetime insert cap. (§2.2)

**Phase 1 — DCCM core:**
1. `migrations_runs/NNNN_dccm.sql` — `dccm_seed_index`, `dccm_runs`, `dccm_seed_candidates` view, extended partial unique index; optional `evidence.citation_count_cache`, `claims.keyphrase_cache`.
2. `app/services/paper_search.py` — add `ads_reference_bibcodes()`, `s2_references()`.
3. `app/agent_loop/citation_context/dynamic.py` — `dccm_process_paper` task, intersection resolver, fan-out/relevance ranking, reuse of CCM `classify_context`/`insert_supportive_evidence` with `source_channel='dynamic_ccm'`.
4. `PromptRegistry` — register `ccm_dynamic_classifier`/`dccm_v1` (§7.1).
5. `app/config.py` — `DCCM_ENABLED=False`, `DCCM_MAX_CLAIMS_PER_SEED=3`, `DCCM_MAX_EVIDENCE_PER_CLAIM_LIFETIME=10`, `DCCM_ADS_RL_FLOOR=200`, `DCCM_REQUIRE_PRIMARY_FOR_CONSENSUS=True`, quality constants.
6. `app/routers/claims.py` — add the §9.1 transitive-floor branch behind `DCCM_REQUIRE_PRIMARY_FOR_CONSENSUS`; add `dccm_citation_context` to the `get_trust_history` trigger allow-list.
7. Ingestion hooks — enqueue `dccm_process_paper.delay(...)` after commit in `arxiv_ingest` and `arxiv_fetch`.
8. `worker.py` — `refresh-dccm-seed-index` nightly beat; no recurring sweep needed (DCCM is event-driven).

**Phase 2 — Calibration & enable:**
9. Labeled Pico calibration set (Kun): 50 hand-labeled DCCM contexts spanning recent contested claims; confirm SUPPORTIVE precision before flipping `DCCM_ENABLED`.
10. Shadow run: `dccm_process_paper` in dry-run over one week of ingested papers; Kun audits projected transitions (same savepoint-rollback harness method as the CCM audit) before any write.

**Tests:** `tests/dccm/` — `test_reference_intersection.py`, `test_seed_eligibility.py`, `test_transitive_floor.py` (asserts a claim with only `dynamic_ccm`+`citation_context_mining` support is capped at `accepted`), `test_concurrency_advisory_lock.py`, `test_lifetime_cap.py`, `test_dynamic_classifier_parse.py`.

---

## 11. Final Position

DCCM is a sound generalization **conditional on three things**, in priority order:

1. **Fix trust-write fragmentation (P1).** Without a single audited writer, "self-reinforcing real-time consensus" is incoherent — I reproduced the stored column already disagreeing with the audit log on the live CCM claims. This is the gate; everything else is secondary.
2. **Enforce the transitive-only floor (§9.1).** This is what separates DCCM from a citation-popularity counter. A claim greens only if it has at least one jury-/human-vetted primary support; DCCM then *accelerates and sustains* green as the literature piles on. Citations grow trust; they do not, alone, create it.
3. **Bound and observe (P2, §9.3–9.5).** Lifetime caps, advisory locks, audited transitions, and a weekly review keep the self-reinforcing loop convergent and inspectable.

With those, DCCM turns our entire refereed-evidence base into a living consensus tracker, and — as a side benefit — its citing-paper-side S2 context lookup should beat CCM's Tier-A hit rate. Without them, it would amplify a latent demotion bug and risk laundering citation counts into false consensus. The architecture above is designed so the safeguards are structural (DB constraints, single writer, hard floor), not advisory.

I recommend Phase 0 ships and is verified **before** any DCCM code is enabled. I will run the Phase-2 shadow audit personally, as I did for CCM v1.

— Kun 🔬
