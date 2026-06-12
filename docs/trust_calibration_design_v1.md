# Trust Calibration v1 — Design

**Author:** Kun 🔬
**Date:** 2026-05-20 23:10 KST
**Status:** Draft → Locked on Papa approval
**Live grounding:** Probe of page_id=57 (galaxy-evolution) at 2026-05-20 23:05 KST against `nebulamind` DB on Mac Studio. Findings in §1.
**Scope:** trust-level audit + recalibration workflow for galaxy-evolution before Citation View trust colors are shown to readers. Generalises to all flagship pages once validated here.

---

## 1. Live grounding — what's actually in the DB

Page: `wiki_pages.id=57`, slug=`galaxy-evolution`, last_renovated_at=2026-05-12, health_score=100, updated 2026-05-20 05:38 KST.

**Claim inventory (41 total):**

| trust_level | count | trust_score range |
|---|---:|---|
| consensus | 2 | 0.78, 0.79 |
| accepted | 25 | 0.31 → 0.80 |
| debated | 5 | −0.30 → 0.75 |
| challenged | 9 | −0.74 → −0.43 |

`human_trust_override` set on: 0. `human_override_locked`: 0. **All trust levels are automated** — no human floor anywhere.

**Coverage gaps:**
- 36/41 claims have `evidence_search_attempted_at IS NULL` — they've never been run through the evidence-search loop. The 767 evidence rows came from arxiv_ingest, marker-embed, and renovation flows, not from a targeted per-claim search.
- 24/41 claims have `last_adversarial_probe_at IS NULL` — never tested with a "find me a counter-paper" jury.

**Evidence quality (767 rows total):**

| field | value |
|---|---|
| Stance distribution | supports=571 · challenges=174 · contradicts=16 · contests=5 · mismatch=1 |
| `arxiv_verified=true` | 309 / 767 (40.3%) |
| `peer_reviewed=true` | 399 / 767 (52.0%) |
| Has arxiv_id or DOI | 767 / 767 (100%) — no orphan rows |
| Year 2024+ | 393 / 767 (51.2%) — feed is fresh |
| Top year | 2026 (n=257), 2025 (n=111) |

Critical: **0 claims have <5 evidence items**. The earlier worry that "many claims are evidence-starved" doesn't hold for this page — min=5, max=41 evidence/claim. The pathology is elsewhere.

**Contested-claim deep view (14 claims):**

| cid | trust | tscore | ev | sup | chal/contra | sec |
|---:|---|---:|---:|---:|---:|---|
| 1488 | debated | −0.28 | 15 | 4 | 11 | High-z Universe |
| 1489 | challenged | −0.69 | 21 | 3 | 18 | High-z Universe |
| 1490 | challenged | −0.48 | 11 | 4 | 7 | Structural Evolution |
| 1491 | challenged | −0.74 | 13 | 4 | 9 | Quenching |
| 1521 | debated | +0.74 | 9 | 5 | 4 | Quenching |
| 1522 | debated | +0.28 | 5 | 3 | 2 | DM Halos |
| 1523 | debated | +0.75 | 17 | 10 | 7 | DM Halos |
| 1524 | challenged | −0.45 | 10 | 0 | 10 | Structural Evolution |
| 1525 | debated | −0.30 | 8 | 5 | 3 | Quenching |
| 1526 | challenged | −0.45 | 10 | 3 | 7 | Structural Evolution |
| 1527 | challenged | −0.43 | 8 | 3 | 5 | Open Questions |
| 1528 | challenged | −0.43 | 8 | 3 | 5 | Open Questions |
| 1529 | challenged | −0.43 | 8 | 3 | 5 | Quenching |
| 1530 | challenged | −0.43 | 8 | 3 | 5 | High-z Universe |

Observations from the table:
- cid=1521 has tscore=+0.74 but trust_level=debated. That can only happen if the scorer used the n_supports/n_challenges gate (debated when ≥1 of each). It's nominally consistent but the *display* (orange "Debated") will undersell a claim with 5 supports and 4 challenges at score +0.74.
- cid=1527/1528/1529/1530 all share trust_score=−0.4338. Suspicious — looks like a copy-paste artifact from a batch insert. Manual inspection candidates.
- cid=1524 has 0 supports, 10 challenges → genuinely challenged (this is what the level is for).

**arXiv pipeline state:** total=1243 papers ingested · last-7d=282 · processed=1243 (100%) · `related_pages LIKE '%galaxy-evolution%'`=222. Pipeline is alive and routing papers to this page, but only 309/767 evidence rows are `arxiv_verified=true`, so the verify gate is the dominant block (see arxiv_wiki_feed_design_v1 §11.2).

**Existing scorer:** `app/services/trust_calculator.py::recalculate_trust`. Phase 1 formula:
```
E = (Σq_supports − Σq_challenges) / Σq      (arxiv-verified only)
V = 0   (reserved)
T = 0   (reserved)
TS = 0.45·E + 0.35·V + 0.10·T               (weights sum to 0.90 — see §4)
Levels: consensus (TS≥0.75 ∧ sup≥3 ∧ chal=0) | accepted (TS≥0.30)
       | debated (|TS|<0.30 ∧ sup≥1 ∧ chal≥1) | challenged (TS≤−0.30)
       | unverified
```
trust_audit_log has 8138 rows for page 57 claims — the scorer runs *often*. The question this design answers: are those scores **right**?

---

## 2. Evidence audit (Step A — fast, no LLM)

**Goal:** flag claims whose evidence shape suggests the trust score is mis-set.

**Already implemented as `/tmp/probe_page57.py`** — the audit produced §1. Promotion to a stable artifact:

- New file: `~/NebulaMind/NebulaMind/backend/scripts/trust_audit.py`
- CLI: `trust_audit.py --page-id 57 --out /tmp/audit_page57.json [--all-pages]`
- Output JSON shape: `{ page_id, claims: [ {id, trust_level, trust_score, evidence_count, supports, challenges, contradicts, contests, mismatch, neutral, arxiv_verified_count, peer_reviewed_count, avg_quality, recent_2024_plus, flags: [...] } ], summary: {...} }`

**Flags emitted (no LLM, deterministic):**

| flag | rule | action downstream |
|---|---|---|
| `LOW_EVIDENCE` | n_evidence < 5 | queue evidence_search (Phase D arxiv) |
| `UNVERIFIED_DOM` | arxiv_verified_count / n_evidence < 0.30 | re-run `verify_for_claim` after ADS lag retry |
| `STANCE_SKEW` | trust_level ∈ {debated, challenged} ∧ (supports = 0 ∨ challenges = 0) | Rakon verify (§3) |
| `SCORE_DEGENERATE` | ≥3 claims share the *same* trust_score to 4dp | manual inspection (likely batch artifact) |
| `LEVEL_MISMATCH` | trust_level=debated ∧ trust_score ≥ +0.50 (or ≤ −0.50) | Rakon verify (§3) — display lies about the score |
| `STALE_AUDIT` | last entry in trust_audit_log older than 30 days for this claim | enqueue `recalculate_trust` |

For page 57 today (audit run 2026-05-20 23:11 KST via `scripts/trust_audit.py`):

| flag | count | notes |
|---|---:|---|
| LOW_EVIDENCE (<5) | 0 | — |
| UNVERIFIED_DOM (arxiv_verified ratio <0.30) | **18** | dominant pathology — Phase D ADS-lag work consumes this |
| STANCE_SKEW (contested w/ supports=0 or opposing=0) | 1 | one genuinely one-sided contested claim |
| SCORE_DEGENERATE (≥3 claims share trust_score to 4dp) | 7 | two groups: {1466,1467,1516}@0.7826 and {1527,1528,1529,1530}@−0.4338 |
| LEVEL_MISMATCH (debated w/ \|score\|≥0.50) | 2 | cid 1521 (+0.74), cid 1523 (+0.75) |

These are the empirically right numbers. The earlier 14-STANCE_SKEW estimate in the §1 working notes used a wrong stance vocabulary; the audit uses the real DB values (`supports`, `challenges`, `contradicts`, `contests`, `mismatch`).

**Cost:** pure Python + SQL, ~0.4s per page on Mac Studio. Trivial.

---

## 3. Rakon verification pass (Step B — contested claims only)

**Why:** the stance jury (the path that wrote `supports` / `challenges`) classifies an *abstract* against a *claim*. It cannot read the paper body. For contested claims, the call between "this paper genuinely challenges the claim" vs "this paper is on the topic but the abstract only mentions the counter-position rhetorically" needs body-reading. Rakon (DeepSeek-R1-671B, Mac Pro) is the only platoon member with that level of synthesis under our infra.

**New celery task:** `app.agent_loop.autowiki.rakon_verify.rakon_contested_verify`
- File: `~/NebulaMind/NebulaMind/backend/app/agent_loop/autowiki/rakon_verify.py` (new — sibling to `deep_synthesis.py`)
- Queue: `autowiki` (same as `rakon_deep_pass`) so the lock mutex in §7 of `job_schedule_v1.md` covers it
- Signature: `rakon_contested_verify(claim_id: int) -> dict`
- Reuses `_call_rakon` from `deep_synthesis.py`

**Prompt template (English; per PROTOCOLS.md):**
```
You are verifying whether opposing evidence rows attached to an astronomy claim
are GENUINELY in conflict with it, or whether they were misclassified by an
abstract-only stance jury.

CLAIM (page: galaxy-evolution, section: <section>):
  <claim.text>

ATTACHED EVIDENCE (showing only abstract; stance was assigned by an LLM jury):
  [1] arxiv_id=<id>  stance=<stance>  quality=<q>  year=<y>  abstract=<abstract>
  [2] ...
  ... (up to 25 items, prioritising challenges/contradicts/contests)

Return JSON, no prose outside:
{
  "claim_id": <int>,
  "verdict": "genuinely_contested" | "false_challenge" | "stance_misclassified" | "needs_more_evidence",
  "confidence": 0.0..1.0,
  "evidence_corrections": [
    { "evidence_id": <int>, "current_stance": "...", "proposed_stance": "...", "reason": "..." }
  ],
  "recommended_trust_level": "consensus" | "accepted" | "debated" | "challenged" | "unverified",
  "rationale": "<= 4 sentences"
}
```

**Inputs assembled by the task:**
- Claim text, section, current trust_level / trust_score
- Up to 25 evidence rows (prefer challenges/contradicts/contests first, then top-quality supports)
- For each evidence row: `evidence.id, arxiv_id, year, stance, quality, abstract`

**Outputs persisted:**
- `evidence_corrections[*]` → write to `evidence_mismatches` table (already exists per §schema_dump.py) keyed on `evidence_id` with proposed_stance, reason, decided_by_agent=rakon
- `recommended_trust_level` + rationale → write a row to `trust_audit_log` with `trigger='rakon_contested_verify'`, `notes=<rationale>`
- Do **NOT** auto-apply Rakon's recommendation to `claims.trust_level` in v1. Kun reviews the 14 verdicts; recalibration (§4) applies them in a controlled batch.

**Cost / latency:** ~6 minute/claim on Mac Pro (Rakon 671B). 14 claims sequential = ~1.5 h. Run during the existing 03:00 KST `rakon_deep_pass` slot or after it. Mutex `rakon:lock` (per `job_schedule_v1.md §7.3`) prevents collision.

**Enqueue plan (today):** push all 14 contested claim_ids onto the autowiki queue with a 60-second stagger, so they don't race the next `rakon_deep_pass` beat at 03:00:

```python
for cid in CONTESTED_CIDS:
    rakon_contested_verify.apply_async((cid,), queue="autowiki", countdown=...)
```

If the task isn't shipped tonight (it needs implementation), enqueue a placeholder via `claim_marker_runs` insert + send the proposal to Tori for the task body. This is acceptable because the audit (§2) is the load-bearing step; Rakon verification is the *quality gate*, not the *recalibration trigger*.

---

## 4. Trust recalibration (Step C — formula tightening)

**Current Phase 1 formula has two known issues:**

1. **Weights sum to 0.90, not 1.0.** `0.45·E + 0.35·V + 0.10·T` leaves 0.10 unaccounted. With V=T=0, TS_max = 0.45 (E=+1). The "TS ≥ 0.75 → consensus" gate is *unreachable* under Phase 1 unless I'm misreading the code. Yet the DB has 2 claims at TS ≈ 0.78 and many at 0.6+. Either (a) someone wrote those scores via a different path, or (b) the formula in `trust_calculator.py` is not what's authoritatively used. **Action: trace which writer is canonical** before any change. The 8138 trust_audit_log rows for page 57 are the source of truth; sample 20 to see what `e_component / v_component / t_component / h_component / new_score` actually look like.

2. **`debated` displays mute high-confidence claims.** Per §1, cid=1521 (5 supports, 4 challenges, TS=+0.74) gets the orange "Debated" badge that visually equates it with cid=1488 (4 supports, 11 challenges, TS=−0.28). The level is *categorically* right ("there is opposition") but the *score* shows the asymmetry. Either: change Citation View to show trust_score numerically alongside the level, or tighten the gate so `debated` requires opposition ratio ≥ 0.30 (challenges / (supports+challenges)), demoting cid=1521 back to `accepted`.

**Proposed Phase 2 formula (tentative — locked after §3 verdicts land):**

```
E = (Σq_arxiv·supports − Σq_arxiv·challenges) / max(1, Σq_arxiv·all)
V = (Σw_pro·votes − Σw_con·votes) / max(1, Σw·votes)        # evidence_votes table
T = 1.0  if recent_2024_plus / n_evidence ≥ 0.50
    0.5  if 0.20 ≤ ratio < 0.50
    0.0  if < 0.20
H = +1 if human_trust_override='consensus' else 0           # human floor
TS = 0.50·E + 0.30·V + 0.10·T + 0.10·H                      # sums to 1.0
```

Level gates (English-only, keep the four-tier vocabulary the UI already speaks):

| level | gate |
|---|---|
| consensus | TS ≥ 0.70 ∧ supports ≥ 5 ∧ challenges = 0 ∧ arxiv_verified ≥ 3 |
| accepted | TS ≥ 0.30 |
| debated | challenges / (supports+challenges) ≥ 0.30 ∧ \|TS\| < 0.50 |
| challenged | TS ≤ −0.30 |
| unverified | otherwise |

Order of evaluation matters: `consensus` first (strict), then `debated` (separation), then `accepted` / `challenged` (numeric), then `unverified` (fallback). The current code does `accepted` before `debated` which is why score-positive debated claims slip through.

**Migration:** new column not needed; the formula change is in `recalculate_trust()`. Backfill via celery task `recalculate_trust_for_page(57)` that loops the 41 claims, writes a single audit-log entry per claim (`trigger='phase2_migration'`), and reports the diff in a structured row (old_level → new_level counts).

---

## 5. arXiv Phase D integration (cross-reference)

Phase D is a separate workstream in `arxiv_wiki_feed_design_v1.md §12` (owner: Tori for 2.5d Tori + 1h Kun). This design does **not** re-design that pipeline; it only specifies **what** the calibration loop needs from it:

| need | Phase D item | status |
|---|---|---|
| Per-claim evidence search that doesn't drop on ADS lag | §11.2 item #1 (48h-lag retry) | pending implementation |
| Stance jury reliability for fresh arxiv_ingest rows | §11.7 (jury enqueue audit) | open |
| Page-extension fallback when claim_evidence verify_rejected | §11.3 | open |

**Wiring needed for the trust calibration loop:**
- After Phase D #1 ships, the audit (§2) `LOW_EVIDENCE` flag enqueues `evidence_search_for_claim(claim_id)`. This task is `evidence_search.run_per_claim` (already exists per the renovation pipeline) — confirm it consumes the 48h retry path properly.
- After Phase D #2 ships (split `verify_rejected` reasons), the audit `UNVERIFIED_DOM` flag becomes actionable instead of cosmetic — we can target the `verify_rejected_ads_lag` slice, leaving `verify_rejected_quality` for human review.

No new code in arxiv_ingest.py from this design. The calibration loop is the *consumer* of Phase D outputs.

---

## 6. Platoon assignment

Per `feedback_platoon_assignment.md` — every step names its model with capability/cost/speed justification.

| Step | Model / agent | Where | Why |
|---|---|---|---|
| §2 evidence audit | Python + SQL (no LLM) | Mac Studio (backend venv) | Pure aggregation. Sub-second per page. Free. |
| §3.a load evidence rows + format prompt | Python | Mac Studio | I/O only. |
| §3.b body-level verification of contested claims | **Rakon** (deepseek-r1:671b) | Mac Pro (10.0.0.119) | Needs deep multi-paper synthesis from abstracts → verdict. Buddle 32B can't hold 25-paper context with reasoning depth this asks. Atom-7B is too shallow. Cost: free (local Ollama), latency ~6 min/claim. Mutex `rakon:lock` shared with `rakon_deep_pass`. |
| §3.c persist `evidence_mismatches` rows | Python | Mac Studio | DB write. |
| §3.d optional fallback if Rakon backlog | **Buddle** (deepseek-v3-31b-q5_k_m) | Mac Pro | Same hardware, 6× faster, 80% of the quality. Acceptable on low-stakes claims (debated, not challenged). |
| §4 trust recalibration | Python | Mac Studio (celery beat-triggered) | No LLM needed; formula is deterministic. |
| §5 arXiv Phase D pipeline | **Mima** (qwen2.5:14b) for stance pre-judge, **Buddle** for stance jury escalation | Mac Studio / Mac Pro | Mima is the existing arxiv_ingest stance writer (fast, free). Buddle is reserved for the contested 5–10% the audit re-flags. |
| Orchestration / scheduling | **Tori** (Codex CLI) | Mac Studio | Cron beat + queue config; this is her lane. |
| Verdict review (post-Rakon, pre-recalibrate) | **Kun** | (this session) | Human-in-the-loop check on the 14 Rakon outputs before they touch claims.trust_level. |
| Frontend display tweaks (§4 mismatch issue) | **Mima** or direct Kun | Mac Studio | One-component change if we decide to surface trust_score numerically. Held until §3 verdicts arrive. |

No model runs on the Mac Pro alongside Rakon — co-residency is forbidden (see `feedback_platoon_assignment.md` and the ClaimMarkerEmbed v1 design).

---

## 7. Sequencing

| Day | Step | Owner | Output |
|---|---|---|---|
| 2026-05-20 (tonight) | §2 audit script promoted to `scripts/trust_audit.py`; artifact `/tmp/audit_page57.json` produced | Kun | flag counts, JSON dump |
| 2026-05-20 (tonight) | §3 `rakon_verify.py` task body + 14 claim_ids enqueued (or proposal handoff to Tori if non-trivial) | Kun → Tori | celery task + queued jobs |
| 2026-05-21 morning | Rakon verdicts land; Kun reviews 14 outputs | Kun | review notes in this doc §8 |
| 2026-05-21 afternoon | §4 Phase 2 formula implemented behind a feature flag `TRUST_PHASE2=true`; backfill on page 57 only | Kun + Tori | new `trust_calculator.py::recalculate_trust_phase2` |
| 2026-05-22 | Compare Phase 1 vs Phase 2 level diff on page 57; ship if diff is sane | Kun + Papa | decision: ship Phase 2 / iterate |
| Continuous | §5 Phase D items #1-4 land in their own workstream; calibration auto-benefits | Tori | (tracked in arxiv design) |

## 8. Acceptance criteria

- [ ] `scripts/trust_audit.py --page-id 57` produces a JSON artifact with the §2 flag schema
- [ ] 14 contested-claim Rakon verdicts written to `trust_audit_log` with `trigger='rakon_contested_verify'`
- [ ] Of those 14, at least N verdicts are `genuinely_contested` (estimated 8–10 from §1 evidence shape) — the rest become stance-correction candidates
- [ ] Phase 2 formula migration produces 0 false demotions on the 2 consensus claims (cid=1466, cid=1474 must remain `consensus`)
- [ ] Citation View on `/wiki/galaxy-evolution` reads the new trust levels (the panel from earlier today already binds to `claim.trust_level`)
- [ ] No human override needed for the green-light: the formula either lands correctly automated, or we add a deliberate Kun-locked override row before showing colors publicly

---

— 🔬 Kun
