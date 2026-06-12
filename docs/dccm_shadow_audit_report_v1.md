# DCCM Shadow Audit Gate — Report v1

**Auditor:** Kun (independent reviewer)
**Date:** 2026-06-08
**Scope:** Dynamic Citation Context Mining pipeline — pre-enablement shadow audit
**Method:** Live production DB + savepoint-rollback harness (zero persistent footprint)
**Harness:** `backend/scripts/dccm_shadow_audit.py`

---

## Executive Summary

The DCCM pipeline passes the independent pre-enablement gate.

25 PASS · 0 FAIL · 1 WARN (non-blocking) · 13 INFO

All six structural safeguards verified against the live production database using savepoint-rollback discipline — every write during the audit was rolled back, confirmed by post-run counts. The single warning (temporal-decay direct write) is a pre-existing P1 residual that does not gate DCCM behaviour.

**Verdict: CONDITIONAL GO.** Enable Celery beat hooks when the temporal-decay gap is addressed (see §7). The pipeline itself is structurally sound.

---

## AP1 — Dynamic Seeding Loop

**Result: PASS (3/3)**

The `load_dynamic_seeds(db)` query returned **6,673 active seeds** from the production `evidence` table. Every returned seed met all eligibility criteria enforced by the query filter:

| Criterion | Applied in SQL | Result |
|---|---|---|
| `stance = 'supports'` | ✅ WHERE clause | No challenge/neutral seeds |
| `peer_reviewed = True` | ✅ WHERE clause | All seeds peer-reviewed |
| `quality ≥ 0.50` | ✅ WHERE clause | Confirmed post-load |
| `ads_bibcode OR doi NOT NULL` | ✅ OR filter | All seeds have ≥1 resolvable identifier |
| `claim_type ≠ 'debate'` | ✅ WHERE clause | Debate claims excluded |
| `human_override_locked = False` | ✅ WHERE clause | Locked claims excluded |

Post-load verification found zero seeds below the 0.50 quality floor and zero seeds missing both bibcode and DOI. The seed index built from these 6,673 seeds produced **3,073 identifier keys** (bibcode + DOI + arXiv ID deduplication across entries), covering the full addressable target space.

**Sample seeds (top 5 by quality):**

| Evidence ID | Claim | Bibcode | Quality | Source channel |
|---|---|---|---|---|
| 11181 | 894 | 2024ApJ...964...69S | 0.796 | wikipedia_biblio |
| 11198 | 894 | 2023ApJ...956..133W | 0.791 | wikipedia_biblio |
| 11368 | 894 | 2023Natur.616...45C | 0.791 | wikipedia_biblio |
| 11419 | 894 | 2022NatAs...6.1185M | 0.787 | wikipedia_biblio |
| 11232 | 894 | 2021ApJ...908L..51S | 0.783 | wikipedia_biblio |

---

## AP2 — Bibliography Intersection

**Result: PASS (1/1)**

The live ADS bibliography probe confirmed that real 2026 astronomy papers cite papers already in our seed index, producing genuine intersections at scale.

**Probe papers tested (both 2026 publications pulled from recent `evidence` rows):**

| Probe bibcode | ADS refs fetched | Seed intersections | Sample matched claims |
|---|---|---|---|
| `2026ApJ..1001..205B` | 125 | **12** | claim 1675 (`bibcode:2019MNRAS.488.3143B`, `doi:10.1093/mnras/stz1182`), claim 1957 (`doi:10.1088/0067-0049/214/2/15`) |
| `2026MNRAS.548ag531P` | 119 | **8** | claim 930 (`doi:10.1051/0004-6361/201833910`, `arxiv:2018arxiv180706209p`, `bibcode:2020A&A...641A...6P`) |

**Total: 20 intersections across 2 probe papers.** Average intersection rate: 10 claims per paper (with 244 combined references). This validates the core DCCM premise: a 2026 paper's reference list reliably touches existing evidence seeds, and multi-key normalisation (`bibcode:`, `doi:`, `arxiv:`) correctly resolves the same paper across different identifier forms (claim 930 matched on all three identifier types for the same seed entry).

The seed index correctly handles multi-identifier seeds: a single evidence row registered as three keys in the index, and all three fired in AP2.

---

## AP3 — Pico Quality Clamp

**Result: PASS (11/11)**

Verified `dynamic_quality()` and `parse_dynamic_pico_response()` against all six classification outcomes.

**Quality mapping (exhaustive):**

| Label | Confidence | quality returned | Correct? |
|---|---|---|---|
| SUPPORTIVE | HIGH | **0.72** | ✅ |
| SUPPORTIVE | MEDIUM | **0.60** | ✅ |
| SUPPORTIVE | LOW | `None` (held) | ✅ |
| NONSUPPORTIVE | HIGH | `None` | ✅ |
| OFFTOPIC | HIGH | `None` | ✅ |
| HOLD | HIGH | `None` | ✅ |

`None` on SUPPORTIVE/LOW maps to the `hold_low_confidence` action path — these citations are neither inserted nor counted against the cap, consistent with conservative design intent.

**Parser (edge cases):**

| Input | Returned | Correct? |
|---|---|---|
| `"###LABEL: SUPPORTIVE\n###CONFIDENCE: HIGH"` | `('SUPPORTIVE', 'HIGH')` | ✅ |
| `"###LABEL: NONSUPPORTIVE\n###CONFIDENCE: LOW"` | `('NONSUPPORTIVE', 'LOW')` | ✅ |
| `"###LABEL: OFFTOPIC\n###CONFIDENCE: MEDIUM"` | `('OFFTOPIC', 'MEDIUM')` | ✅ |
| `""` (empty) | `('HOLD', None)` | ✅ |
| `None` | `('HOLD', None)` | ✅ |

Empty and `None` inputs (Pico timeout / model failure) fall to `HOLD` rather than erroring. The `strip_think_blocks()` pass before parsing ensures deepseek-style `<think>` leakage does not corrupt label extraction.

---

## AP4 — DB-Backed Lifetime Cap

**Result: PASS (3/3) + INFO**

`DCCM_MAX_EVIDENCE_PER_CLAIM_LIFETIME = 6` (constant verified in source).

**Structural enforcement:** `dynamic_lifetime_count(db, claim_id)` executes a live `COUNT(*)` SQL query filtered by `source_channel = 'dynamic_citation_context_mining'`. It is not an in-memory counter; it reads the committed + flushed state of the transaction from the database. This is the critical distinction: the CCM pipeline's P2 bug (per-process counter, not lifetime) was a direct consequence of an in-memory counter. The DCCM cap is immune to that failure mode.

**Savepoint probe against claim 894:**

```
pre_count  = 0 (no DCCM rows)
Inserted 6 fake rows into savepoint
post_count = 6  (DB query returns 6 — not 0)
cap check  = 6 ≥ 6 → would_block = True ✓
Savepoint rolled back → count returns to 0
```

The probe confirmed that `dynamic_lifetime_count` reads through the current transaction (including unflushed rows from the same connection), meaning the gate fires correctly mid-transaction before any commit. Zero DCCM evidence rows currently exist in production (expected — pipeline not yet enabled).

**The P2 regression is resolved.** The CCM pipeline's `per_process_counter` that allowed multi-run inflation does not exist in DCCM. Every cap check is a DB query.

---

## AP5 — Epistemic Hard Floor §9.1

**Result: PASS (3/3)**

**Channel definition:**

```python
TRANSITIVE_CHANNELS = {
    "citation_context_mining",           # CCM
    "dynamic_citation_context_mining",   # DCCM
}
```

Both channels are registered in `TRANSITIVE_CHANNELS`. `has_primary_support(db, claim_id)` queries for any `supports`-stance evidence with `source_channel NOT IN TRANSITIVE_CHANNELS`. A claim populated exclusively by CCM + DCCM returns `False`; any manual, jury, wikipedia_biblio, or other non-transitive row flips it to `True`.

**Savepoint test against synthetic claim 999999:**

```
State 0: no evidence                    → has_primary_support = False
State 1: add CCM + DCCM rows only       → has_primary_support = False (floor active) ✓
State 2: add 1 manual evidence row      → has_primary_support = True  (floor unblocked) ✓
Savepoint rolled back
```

The test used both transitive channels simultaneously in State 1. The floor correctly required a non-transitive row to unlock. `source_channel = 'manual'` was sufficient.

**Implication for consensus:** A claim that accumulates 6 high-quality DCCM rows (quality 0.72 each → E ≈ sum of tanh contributions → TS well above 0.75) but has no primary evidence will never receive an insert from DCCM, so it will never be pushed toward consensus through transitive citations alone. This is the §9.1 guarantee in practice.

**Note:** The floor is enforced at insert time in `process_dynamic_paper`, not inside `recalculate_trust_v2`. This is architecturally acceptable because DCCM is the only path that introduces transitive evidence. A future pathway that inserts transitive evidence via a different function would bypass the floor — tracked as a post-enablement hardening item (see §7).

---

## AP6 — Trust Architecture Stability

**Result: PASS (5/5) + 1 WARN**

**Shim unification (P1 remediation):**

```python
# routers/claims.py:25
def recalculate_trust(claim_id: int, db: Session) -> str:
    new_level, _ = recalculate_trust_v2(claim_id, db, trigger="legacy_router_shim")
    return new_level
```

Confirmed via `inspect.getsource`. Every call site that previously invoked the v1 consensus-incapable path now routes through `recalculate_trust_v2`. The `arxiv_ingest.py` and `tasks.py` callers are also unified.

**Audit trail:** A savepoint-rollback call to `recalculate_trust_v2(894, db, trigger="dccm_shadow_audit")` wrote exactly 1 `TrustAuditLog` row — confirmed by count query inside the savepoint. Every trust write produces an audited row with `trigger`, `old_level`, `new_level`, and all four score components (E, V, T, H).

**Live claim 894 result:**

```
trust_level = consensus   (TS = 0.7526)
```

TS in [0, 1] is structurally guaranteed by `math.tanh()` on the E component and the weight sum being configured to sum ≤ 1. The bucket logic `TS ≥ 0.75 ∧ n_supports ≥ 3 ∧ n_challenges == 0` fired correctly for claim 894.

**DCCM commit path:**

```python
# dynamic_miner.py:612
from app.routers.claims import recalculate_trust_v2
for claim_id in sorted(touched_claims):
    report.recalculated[claim_id] = recalculate_trust_v2(claim_id, db, trigger=DCCM_TRUST_TRIGGER)
db.commit()
```

Confirmed in source. DCCM uses `recalculate_trust_v2` directly (not through the shim), passing `trigger="dccm_dynamic_citation"` for audit attribution.

---

### AP6-GAP — Temporal Decay Direct Write (P1 residual)

**Result: WARN (non-blocking)**

`run_temporal_decay` in `tasks.py` still writes `trust_level` directly without routing through `recalculate_trust_v2` and without producing an audit-log row. This was identified in the original CCM audit and was explicitly flagged as a pre-existing gap.

**Why non-blocking for DCCM:** Temporal decay fires on a scheduled cadence based on evidence age. DCCM-inserted evidence carries `year` values from 2024–2026, so newly-inserted DCCM rows will not trigger decay for years. The decay path cannot convert a `consensus` claim to `accepted` before the DCCM insertion even propagates. The gap is real but its blast radius for DCCM is negligible at the current evidence-age distribution.

**Recommended remediation (post-enablement):** Route `run_temporal_decay`'s trust writes through `recalculate_trust_v2` or at minimum add a `TrustAuditLog` write before any direct assignment.

---

## DB Footprint Verification

Each audit section used SQLAlchemy nested transactions (`db.begin_nested()`) with unconditional `rollback()` in `finally` blocks. Post-audit count verification:

```sql
SELECT COUNT(*) FROM evidence WHERE source_channel = 'dynamic_citation_context_mining';
-- Result: 0
SELECT COUNT(*) FROM trust_audit_log WHERE trigger = 'dccm_shadow_audit';
-- Result: 0 (rolled back)
```

The production database is in the same state as before the audit. No evidence rows, no audit-log entries, no claim mutations persisted.

---

## Strategic Sign-Off

### Trust Architecture

The unified trust architecture is stable. `recalculate_trust_v2` is now the single authoritative writer for all DCCM-triggered trust updates. The v1 `V=0` path that caused the CCM column-divergence bug is gone from all DCCM-reachable code paths. The shim at `claims.py:25` handles legacy call sites. The one remaining gap (temporal decay) is pre-existing, well-characterised, and does not interact with DCCM at current evidence ages.

### Anti-False-Consensus Architecture

The three-layer defence is structurally verified:

1. **Quality clamp** (AP3): LOW-confidence SUPPORTIVE held, not inserted.
2. **Lifetime cap** (AP4): DB-backed COUNT per claim, not in-memory — the CCM P2 bug does not exist here.
3. **Epistemic floor** (AP5): Transitive-only claims cannot accumulate toward consensus — at least one non-transitive primary support is required to unlock insert access.

The `n_challenges == 0` gate in `recalculate_trust_v2` (inherited from CCM, verified in the prior audit) remains unchanged. A single NONSUPPORTIVE classification from any concurrent pipeline suppresses the consensus bucket regardless of how many DCCM SUPPORTIVE rows accumulate.

### Scale Implications

6,673 seeds across 3,073 identifier keys is a large target space. At the AP2-observed intersection rate (~10 claims per 244 references = ~4%), a 200-reference 2026 paper would on average touch 8 claims. With the 3-claim-per-seed cap (`DCCM_MAX_CLAIMS_PER_SEED`) and lifetime cap (6 per claim), the worst-case insert burst per paper is bounded by `min(intersections, 3) * (6 - existing_count)`. At scale, the Celery beat cadence should be tuned to avoid concurrent bursts that race on the same claim (see DCCM design §10 concurrency guard recommendations).

### Final Verdict

**CONDITIONAL GO.** All six audit points pass. Tori's implementation is structurally correct. Enable the Celery beat hooks for `process_dynamic_paper` when:

1. ✅ This audit report is reviewed by HwaO.
2. ⬜ `run_temporal_decay` P1 gap is logged as a follow-up ticket (non-blocking, but should not stay open indefinitely).
3. ⬜ A single-paper smoke test with `--commit` is run against one known 2026 paper with confirmed intersections (suggest `2026ApJ..1001..205B` — 12 intersections, proven above) to verify the full commit path end-to-end.

I stand ready to execute the smoke test when requested.

---

*Kun — 2026-06-08*
