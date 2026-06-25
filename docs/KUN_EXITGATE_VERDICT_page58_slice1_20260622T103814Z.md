# KUN EXIT-GATE VERDICT — Page-58 Paper-Driven Vote Staking, Slice-1 Dry-Run

- **Reviewer:** Kun (analyst / exit-gate)
- **Date:** 2026-06-22 (UTC 103814Z)
- **Scope:** Bounded, read-only gate of Tori's Slice-1 `--no-apply` dry-run. NOT a redesign.
- **Artifacts reviewed:**
  - Script `backend/scripts/page58_sentence_vote_staking_dry_run.py` (sha256 `03157eeb44d5…`, read in full)
  - Migration `backend/alembic/versions/sentence_votes_v1.py` (sha256 `4a5326b05c84…`, read in full — NOT applied)
  - Report dir `docs/page58_sentence_vote_staking_dry_run_20260622T090031Z/` (`summary.json`, `would_be_sentence_trust.jsonl`, `vote_candidates.jsonl`)

## VERDICT: **PASS-WITH-FIXES**

Slice-1 did its job as a **diagnostic**: containment is perfect, the pipeline runs end-to-end, and — critically — it **self-flagged its own central defect** (`sign_calibration: "UNCALIBRATED_pairwise_stance_gold_missing"`). It is sound to proceed to Slice-2 (build the held-out golds). It is **NOT** sound to advance toward any write/seed path until the P0/P1 fixes below land. Hard gate unchanged: nothing reaches a DB write without Papa-seed + Kun-gate.

---

## A. CONTAINMENT — RE-CONFIRMED GREEN (live re-query, not report self-attestation)

Verified directly against the live DB and repo at review time:

| Check | Expected | Observed | Status |
|---|---|---|---|
| git HEAD | 4ba9675 (= `git_head_required`) | 4ba9675 | ✅ |
| `sentence_votes` table | absent (migration unapplied) | `to_regclass = NULL` | ✅ |
| page-58 `sentence_trust` | 10 rows, 5 consensus / 5 debated | 10 rows, 5 consensus / 5 debated | ✅ |
| page-58 `sentence_provenance` | 167 edges / 10 sentences | 167 / 10 | ✅ |
| `db_write_count` | 0 | 0 | ✅ |
| `paid_lane_touched` | false | false | ✅ |

**Write-path code audit (the "can it literally write to prod" ask): PASS.**
- `load_base_and_intros()` issues SELECT-only over `engine.connect()` — no `commit`, no DML, no `session.add`.
- No `op.*` / Alembic invocation anywhere in the script; the migration is a separate, unapplied file.
- Two hard guards: refuses to run unless `--no-apply` is set; refuses to run if `NM_ANTHROPIC_API_KEY` is present in env.
- `db_write_count: 0` is therefore **structurally guaranteed**, not merely reported.

**One pre-apply finding (NON-blocking for Slice-1, BLOCKING for any future migration apply):**
The live `alembic_version` is **`intro_synthesis_v2_ab_fold`**, which has **no migration file** anywhere in `backend/` (verified by direct search). This is a **pre-existing phantom alembic head** — it predates and is unrelated to this work — but it means `alembic upgrade head` cannot locate the current DB revision, so `sentence_votes_v1` **cannot cleanly apply to this database** until the alembic graph is reconciled. Additionally, `sentence_votes_v1.down_revision = "pipeline_runs_schedule_name_widen_v1"`, which is not the live tip. Flag to Tori/HwaO; do not let the migration silently fail or fork the graph at apply time. (The migration DDL itself is clean: see §D.)

---

## B. THE THREE THINGS TO GATE — ADJUDICATION

### Concern 1 — Degenerate stance sign: **DEGENERACY CONFIRMED (not a data/threshold artifact)**

The 2-con-out-of-105 imbalance is **proxy degeneracy by construction**, not thin data.

- Root cause in code: `stance_from_tone()` (L268-277) maps **single-assertion tone-tier → stance sign**: `consensus|accepted → agree(+1)`, `challenged → disagree(-1)`, `debated → refine(None)`. This is **certainty-as-stance**. It never compares the paper's claim against the base sentence, so it cannot represent "this paper *contradicts* the base." The sign is decided before the two propositions ever meet.
- Evidence: candidate tone distribution is `accepted 234 / consensus 60 / debated 10 / challenged 2` → **96% map to agree** mechanically. Of the **2** disagree votes, **both are spurious keyword hits**: S9 paper `2512.05584v2` ("…potentially *challenging* the theory…") and S5 paper `2605.31052v1` ("…*challenge* current ΛCDM…"). Neither expresses disagreement with the *base sentence* — the word "challenge" in the intro triggered `tone=challenged`.
- **0/10 sensitivity (con-drop, τ±0.10): I AGREE this is a symptom of degeneracy, not robustness.** You cannot perturb a con signal that essentially does not exist. The flat sensitivity is the *fingerprint* of the missing axis, not evidence of stability.

→ **A real pairwise stance classifier + held-out stance gold is MANDATORY before any write.** This is exactly Revision-1 Point-2 target #2 (the gap I flagged: the 94-row tone gold calibrates single-assertion certainty, NOT pairwise agree/disagree). Tone-tier stays — but as a *trust weight*, never as the *sign*.

### Concern 2 — Seed-vs-new rollup weighting: **SHAPE IS RIGHT; TWO REAL DEFECTS MAKE THE TRANSITIONS UNTRUSTWORTHY**

Seed-as-prior is a legitimate design (existing accumulation should anchor the page). It is **not** gross double-counting. But two concrete defects mean the reported tier transitions cannot be read as vote signal yet:

1. **Dedup defect (P0).** `rollup()` blends `pro = existing_pro + new["pro"]` (L332) and `con = existing_con + new["con"]` (L333) **additively**, while `distinct_sources = existing_sources | new["papers"]` (L334) is correctly a deduped union. So a paper already in the seed that votes again is **counted twice in pro/con but once in sources**. Measured: **7 of 105 new stakes (6.7%)** are papers already present in the seed (e.g. `2401.12953`, `2604.03503`, `2605.27507`, `2605.23338`). Note the migration's `UniqueConstraint(page_version_id, sentence_index, sentence_hash, arxiv_id)` does **NOT** protect against this — seed papers live in `sentence_trust`/provenance, not in `sentence_votes` rows, so the DB constraint can't see them. The dedup MUST happen at the rollup/blend layer.
2. **Parallel-tiering defect (P1).** `trust_level()` (L280-293) is a **reimplemented** rule that **diverges from the production `trust_calculator`**. Proof: a 14-pro/2-con sentence → **production = consensus**, but the dry-run rule → **debated/accepted**. Consequence: the eye-catching transitions are largely **rule artifacts, not vote movement** —
   - S6 (baseline consensus, +5/-0) → "accepted" and S9 (baseline consensus, +17/-1) → "accepted": these are **demotions caused by the divergent rule**, not by new evidence.
   - S3 (baseline debated, +4/-0) → "accepted": rule-driven promotion.
   - S4 (baseline debated, blended ~6/15, +2/-0) → "challenged": this one is **seed-dominated and internally consistent** (the con weight is overwhelmingly seed, the new stakes barely move it) — but it rests on **uncalibrated seed semantics**, so "challenged" here is only as trustworthy as the pre-existing contested_votes, which were themselves never validated as genuine disagreement.

→ The blend cannot feed a write until: dedup fixed, **production tiering** substituted for the reimplemented rule (Revision-1 §3.2), and **both** vote layers calibrated. Also: re-validate that the seed's existing `contested_votes` are *real* disagreement once the stance classifier exists — today they inherit the same certainty-as-stance ambiguity.

### Concern 3 — Slice-2 greenlight + performance

- **Greenlight: YES.** Slice-1 is sound *as a diagnostic*. Containment is perfect, the pipeline executes, and it correctly surfaced its own blocking gap. Proceed to build the three held-out golds — **stance gold FIRST and MANDATORY** (it is the load-bearing one), then τ_rel relevance gold and the tone-tier transfer gold.
- **Performance (non-blocking):** Atom-7B claim-filter = **4317.9s of 4744.8s total (91%)**. Mitigations for when volume scales: a cheap `heuristic_finding()` lexical pre-pass to shed obvious non-findings before the LLM; larger batches / async dispatch; and a persistent claim-filter cache keyed by sentence hash. Diagnostic-stage only — do not let it block Slice-2.

---

## C. PRIORITIZED FIX LIST

**P0 — mandatory before ANY write path:**
- **P0-a — Real pairwise stance.** Replace `stance_from_tone()` sign logic with a stance classifier that compares paper-claim ↔ base-sentence (supports / contradicts / neither), calibrated on a NEW held-out stance gold. Keep tone-tier for trust weighting only.
- **P0-b — Dedup new stakes against seed sources.** In `rollup()` L332-333, exclude papers already in `existing_sources` before adding to pro/con. (Union at L334 is already correct.)

**P1 — before write path:**
- **P1 — Use production tiering.** Replace the reimplemented `trust_level()` (L280) with the adapted production `trust_calculator.recalculate_trust()` so dry-run tiers match live semantics.

**RECOMMENDED (Slice-2 / pre-write):**
- Build τ_rel relevance gold + tone-tier transfer gold; replace placeholder `τ_rel=0.55` / `τ_vote=0.70` with calibrated values.
- Define seed-blend semantics explicitly (full-weight prior vs decaying prior).
- Re-validate seed `contested_votes` as genuine disagreement once the stance classifier exists.

**PRE-APPLY (migration, non-blocking for Slice-1):**
- Reconcile the alembic graph (phantom live head `intro_synthesis_v2_ab_fold` has no file) and re-point `sentence_votes_v1.down_revision` to the true tip before any `alembic upgrade`.

**PERF (non-blocking):** `heuristic_finding()` pre-pass + larger/async batches + claim-filter cache.

---

## D. MIGRATION DDL — clean (for the record)

`sentence_votes_v1` creates one table with: `value SmallInteger` + `CheckConstraint value IN (-1,1)` (so only signed pro/con become rows; no_op/refine/neutral are correctly NOT persisted), `UniqueConstraint(page_version_id, sentence_index, sentence_hash, arxiv_id)` (ledger-internal one-vote-per-paper-per-sentence), FK `page_version_id → page_versions.id ON DELETE CASCADE`, and three supporting indexes. DDL is well-formed. Caveats: (1) it is unapplied; (2) it is not apply-ready against this DB until the alembic graph is reconciled (§A); (3) the UNIQUE constraint does not address the seed-vs-ledger dedup defect (§B-1).

---

## E. BOTTOM LINE

PASS-WITH-FIXES. Containment all-green and re-verified live. Slice-1 is a clean diagnostic that correctly named its own blocker. Greenlight Slice-2 with the **stance gold first and mandatory**. The degenerate sign is real (not artifact); 0/10 sensitivity is its fingerprint; the rollup shape is right but the dedup + parallel-tiering defects make today's transitions rule artifacts, not vote signal. No write, no seed, no migration apply without the P0/P1 fixes, graph reconciliation, Papa-seed, and a fresh Kun gate.

— Kun 🔬
