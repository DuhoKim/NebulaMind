# KUN EXIT-GATE VERDICT — Page-58 Calibrated Vote Model, Slice-2 Dry-Run

- **Reviewer:** Kun (analyst / exit-gate)
- **Date:** 2026-06-22 (UTC 121709Z)
- **Scope:** Bounded, read-only gate of Tori's Slice-2 calibrated dry-run. Verifies the Slice-1 P0/P1 fixes landed and adjudicates two new findings (stance-calibration circularity, tone-transfer gate failure). NOT a redesign.
- **Tori event:** `page58_slice2_20260622T115830Z` / `DRY_RUN_COMPLETE_STANCE_PROVISIONAL_TONE_TRANSFER_NEEDS_FIX`
- **Artifacts reviewed (read in full):**
  - script `backend/scripts/page58_slice2_calibrated_staking_dry_run.py` (sha `157aaf6e…`)
  - dir `docs/page58_slice2_calibrated_staking_20260622T111621Z/` — summary.json, REPORT.md, stance_gold_draft_for_papa.jsonl, relevance_gold.jsonl, tone_transfer_gold.jsonl, pairwise_stance_predictions.jsonl, would_be_sentence_trust_slice2.jsonl
  - production comparator `app/services/trust_calculator.py`

## VERDICT: **PASS-WITH-FIXES**

Real, genuine progress: the stance **sign** is now propositional (pairwise intro↔base), not a tone proxy, and I verified by inspection that the contradictions it surfaces are real scientific dissent — slice-1's keyword degeneracy is gone. The seed-dedup fix is correct and complete. **However, the headline `stance F1 = 1.0 / 1.0` is a degenerate (tautological) number that provides ZERO evidence of stance accuracy, and the classifier it nominally validates is not even the one that drives the rollup.** Proceed to Papa's spot-check (after a cheap gold rebalance) — but the stance classifier MUST NOT be locked, and nothing seeds, until a real accuracy metric exists. Containment is clean and re-verified live.

---

## A. CONTAINMENT — RE-CONFIRMED GREEN (independent live re-query + code audit)

| Check | Expected | Observed | Status |
|---|---|---|---|
| git HEAD | 4ba9675 | 4ba9675 | ✅ |
| `sentence_votes` table | absent | `to_regclass = NULL` | ✅ |
| alembic head | unchanged phantom `intro_synthesis_v2_ab_fold` (migration unapplied) | same | ✅ |
| page-58 `sentence_trust` | 10 rows, 5 consensus / 5 debated | 10, 5/5 | ✅ |
| page-58 `sentence_provenance` | 167 / 10 | 167 / 10 | ✅ |
| `db_write_count` | 0 | 0 | ✅ |
| `paid_lane_touched` | false | false | ✅ |
| `NM_ANTHROPIC_API_KEY` | absent | absent | ✅ |

**Write-path code audit: PASS.** `hydrate_base_rows()` (L261-303) is SELECT-only over `engine.connect()` (sentence_trust + sentence_provenance); `reroll()` (L343-381) is pure in-memory; the only writes are docs artifacts under `--out-dir`. No DML, no commit, no `op.*`/Alembic. Guards (L385-390) refuse without `--no-apply`, refuse if `NM_ANTHROPIC_API_KEY` is set, and refuse if `claude -p` is unreachable. `claude_label()`/`check_claude()` strip every `*ANTHROPIC*` env var before invoking `claude -p` → subscription lane, not metered → `paid_lane_touched=false` is consistent.

**Paid-lane cap held.** `claude_p_invocations=15` = exactly `CLAUDE_CAP`; claude was used only as a tie-break on qwen↔gpt stance disagreements (24 disagreements, 15 arbitration attempts, **3 adopted** as `claude_tiebreak`). This is the lane I authorized ("capped claude -p tie-break only"). Side effect to note: 9 disagreement rows exhausted the cap and fell back to `qwen_default` (unbroken) → see §C-2 for the spot-check implication.

**Migration:** unchanged, unapplied, clean DDL (gated in slice-1). The pre-existing phantom alembic head `intro_synthesis_v2_ab_fold` (no file in `backend/`) still blocks a clean `alembic upgrade` — registered, not mine to fix, but it gates any future apply.

---

## B. SLICE-1 FIX VERIFICATION (by reading the code)

**P0-b — seed-blend dedup: ✅ FULLY FIXED.** `reroll()` L360-363 skips any paper already in `existing_arxiv_ids` (hydrated from `sentence_provenance` in `hydrate_base_rows`) before tallying pro/con; `distinct_sources` is a deduped union (L376). **7 seed-duplicate stakes skipped** — exactly the 7/105 double-count I measured in slice-1. Clean win.

**P0-a — pairwise stance sign (tone removed from sign): ✅ structurally fixed, ⚠️ accuracy unmeasured.** Slice-1's `stance_from_tone()` (tone-tier → sign) is gone. Sign now comes from a pairwise supports/contradicts/neither panel (`classify_all_stance`, L329-340). I read all 18 contradict predictions: the strong ones are **genuine** propositional contradictions, e.g. S0 `2508.06707v1` "AGN kinetic energy almost always <0.1%" vs base "AGN drives powerful outflows"; S8 `2401.12953` "black hole mass is the key predictor" vs base "stellar mass is the primary driver"; S2 `2401.12953` "high-mass satellites behave like centrals (mass-driven)" vs base "satellite quenching distinct from mass-driven"; S0 `2604.15438` "positive AGN feedback leads to star formation" vs base "AGN quenches". This is qualitatively far better than slice-1's two spurious "challenge" keyword hits. **Caveat:** the classifier's accuracy is never scored (see §C-2); ~40% of the 18 are borderline or qwen↔gpt disagreements resolved by confidence (e.g. S8 `2604.15438` qwen=supports/gpt=contradicts; S2 `2605.03008v1` qwen=contradicts/gpt=supports). **Note — tone is not actually "demoted to weight"; it is currently INERT:** `reroll()` tallies unweighted ±1 votes and never multiplies by tone-tier. Tone is computed only for the (failing) transfer gate. Removing tone from the sign is done; "tone as a weight" is not implemented (which is fine — better inert than mis-wired).

**P1 — production-like trust projection: ⚠️ slice-1 artifact replaced, but it's a count-rule simplification, not the production calculator.** Slice-1's `trust_level()` is replaced by `production_sentence_trust()` (L243-258), and the specific divergence I proved in slice-1 (14/2 → production consensus vs dry-run debated) is now fixed (`pro>=10 and con<=2 → consensus`). **But it is still a hand-rolled count rule, not an import of any production path.** The real `trust_calculator.recalculate_trust()` is the *claim* calculator and is quality-weighted (E-component, TS thresholds) — structurally different. More tellingly: the live page-58 `sentence_trust` labels are **not** count-rule-derived — S3 (settled 17 / contested 2) is `debated` while S9 (14 / 2) is `consensus` at near-identical settled-share (0.913 vs 0.912). A pure pro/con/share rule cannot produce that ordering; those labels are tone-calibration-derived and use the schema fields `production_sentence_trust` ignores (`settled_share`, `contested_veto`, `single_source`, `tone_distribution`, `tier2_density`). So the projection is "production-plausible," not production-faithful, and each baseline→would-be transition compares a tone-calibrated label to a count-rule projection — not a clean A/B. The novel heuristic `new_con >= 2 → debated` (L249) has no production provenance and should be explicitly justified/calibrated, not assumed.

---

## C. ADJUDICATION OF THE FIVE ITEMS

### 1. Containment — ✅ see §A. Independent live re-query passes; code literally cannot write to prod.

### 2. Stance calibration — **F1 = 1.0 is DEGENERATE, not merely self-consistency; CONFIRMED and strengthened**

Your read ("measured against the panel's own draft labels → self-consistency, not accuracy") is correct, and it is **worse than that**:

- **The metric is tautological.** In `calibrate_tau_vote.score()` (L234-237): `y_true = [draft_label in {supports,contradicts}]` and `y_pred = [max_conf >= tau AND draft_label in {supports,contradicts}]`. y_pred is a structural **subset** of y_true (both carry the same `draft_label ∈ {supports,contradicts}` term), so a false positive is impossible and the only error is a signed row with confidence < tau. With panel confidences mostly ≥0.85 and tau=0.70, FN≈0 → **F1→1.0 by construction**. The metric scores "does a confidence threshold recover the signed-vs-`neither` partition," **never** supports-vs-contradicts — i.e. it never tests the sign, which is the whole point of P0-a.
- **It validates the wrong classifier.** The gold labels use qwen-default + claude tie-break (`finalize_stance_gold`). The rollup uses a **different** procedure — `classify_all_stance`: qwen/gpt higher-confidence, **no claude** (self-tagged `local_panel_provisional_no_claude_for_full_pass`). The classifier that actually produces the votes is never scored against the gold at all.

→ **Treat `stance F1 = 1.0/1.0` as carrying no accuracy information.** Do not let it read as "validated."

**Gold construction:**
- **Paper-split leakage: ✅ none.** `split_by_paper()` (L210-214) partitions by `arxiv_id`; no paper appears in both tune and validate. Good (though moot under the degenerate metric).
- **Balance: ⚠️ skewed.** Draft labels are **supports 61 / neither 22 / contradicts 7** out of 90. The sampler (`sample_gold_inputs`, L315-318) is cosine-stratified (top-45 + middle-25 + bottom-20 by `max_cosine`), not stance-balanced — so the gold under-samples exactly the rare classes (contradicts, neither) that drive `debated`/`challenged`.
- **Sampling frame: ⚠️ truncated.** The gold is drawn only from the 306 `vote_candidates` (already cosine-filtered survivors), not from the ~1,680 enumerable intro×base pairs. The `neither`/relevance boundary is therefore under-represented.
- **Worth Papa's spot-check? YES — as a draft — but rebalance first** so his time lands on signal: oversample contradicts + low-cosine + the 21 `qwen_default` rows (especially the 9 cap-exhausted unbroken disagreements) + the 24 qwen↔gpt disagreement rows.
- **"Lock requires Papa-spot-checked labels" — right gate, INSUFFICIENT alone.** Locking also requires (i) a non-degenerate supports/contradicts/`neither` accuracy metric (per-class precision/recall, especially **contradict recall**), computed on (ii) the **actual** `classify_all_stance` outputs, against (iii) Papa-reviewed labels, with (iv) real rare-class coverage.

### 3. Tone-transfer gate failure (macro-F1 ~0.61 vs 0.70) — **tolerable-with-caveat for the dry-run; mostly inter-model noise, not a true accuracy failure**

Your hypothesis is correct. The F1 is each model vs the **blended panel draft** (`draft_label` = qwen when models agree, else higher-confidence). The two models **disagree massively** on the 4-class tone task: **qwen↔gpt agree on only 19/60 (32%)**; qwen sees 29 consensus / 25 accepted, gpt sees 15 consensus / 26 accepted / 13 debated. So ~0.61 is dominated by inter-model disagreement against a self-referential draft with **no human labels** — not evidence the tone classifier is wrong vs truth (there is no truth here yet).

- **Blocker? No, not for this dry-run** — tone is **inert** in the rollup (§B, votes are unweighted), so the gate failure changes nothing in the current projection.
- **It IS a hard prerequisite for any future "tone-as-weight" feature.** Minimum fix before tone can weight votes: **human-label** the transfer sample (the 32% panel agreement says the panel itself is too unreliable to self-label tone), compute macro-F1 vs **human** truth, identify the failing tier boundary (the qwen/gpt split is worst around consensus↔accepted↔debated), and only then wire tone as a weight.

### 4. Fixes verified by reading the code — ✅ done in §B (P0-b clean; P0-a structural-yes/accuracy-no; P1 partial).

### 5. Rerun sanity — **de-degeneration is substantially REAL, but unvalidated**

- The 5 con votes (and drop-con sensitivity 2/10 vs slice-1's 0/10) trace to genuine pairwise contradictions, not circular tone labels — I verified the reasons first-hand (§B). The classifier produces **18 contradict predictions**, collapsing to 5 con votes via (idx,arxiv) max-confidence dedup + seed-skip. The contradicts cluster on S0 (the AGN-outflow sentence) precisely because that base claim **is** genuinely contested in the literature (stellar-feedback alternative, positive feedback, negligible kinetic energy) — so S0→`debated` is *correct* behavior, not noise.
- **But it is not validated.** No accuracy metric scores `classify_all_stance` against truth (§C-2). ~40% of the 18 contradicts are borderline or resolved by a confidence tiebreak. The gold has only 7 contradicts, so robustness to label error is plausible-not-proven.
- **Does the 4-debated/1-challenged split survive if the draft labels are wrong?** Mostly yes for the strong cases (S0 AGN-contested, S8 BH-mass-vs-stellar-mass, S2 satellite-vs-central, S9 morphology) — those rest on robust, well-reasoned contradictions. S4→`challenged` is **seed-dominated** (baseline 4 settled / 15 contested; the +2/-0 new votes don't move it) and persists regardless of the new labels — same as slice-1, and it inherits the uncalibrated seed semantics. The borderline sentences' exact tier could shift under modest label noise. Net: directionally real, tier-precision not yet certifiable.

One precision note on the rollup: `reroll()` keeps the single highest-confidence prediction per (idx, arxiv) **regardless of label** (L356-358), so a paper that both supports one clause and contradicts another of a multi-clause base sentence (e.g. S8) collapses to one signed vote. Minor signal loss; acceptable for a dry-run, worth noting before any atomic-sentence design.

---

## D. ORDERED GATE LIST

**Before (a) Papa's stance spot-check is worthwhile — do this cheap rebalance first:**
1. Rebuild/augment the stance gold to oversample **contradicts** and **neither** (target ≥20 each, or balanced), draw some **sub-τ-cosine** pairs so the `neither` boundary is represented, and surface for Papa's eyes the 21 `qwen_default` rows (esp. the 9 cap-exhausted disagreements) + the 24 qwen↔gpt disagreements. Then Papa spot-checks.

**Before (b) any stance-classifier LOCK:**
2. Replace the degenerate `calibrate_tau_vote` metric (L234-237) with a real supports/contradicts/`neither` accuracy metric (per-class precision/recall, **contradict recall** is load-bearing).
3. Score the **actual** rollup classifier (`classify_all_stance`), not the gold-labeler, against Papa-reviewed labels; keep the paper-split (already correct).
4. Lock only if contradict precision/recall clear an explicit threshold; record the metric, not "F1=1.0".

**Before (c) any migration-apply / production seed:**
5. Reconcile the phantom alembic head `intro_synthesis_v2_ab_fold` (re-point `sentence_votes_v1.down_revision` to the true tip) — registered, pre-existing, not introduced here.
6. Do NOT wire tone as a weight until a human-labeled tone transfer sample passes macro-F1 vs truth.
7. Adopt/justify the real sentence-trust semantics (the schema fields `production_sentence_trust` drops) or explicitly accept the count-rule simplification for seed.
8. Standing hard gate: Papa-seed + fresh Kun-gate; nothing writes without both.

---

## E. BOTTOM LINE

PASS-WITH-FIXES. Containment is clean and re-verified live; the paid-lane cap held at 15/15 tie-break. P0-b (dedup) is fully fixed; P0-a moved the sign onto a genuine pairwise basis (verified real contradictions); P1 replaced the slice-1 artifact but with a count-rule simplification, not production fidelity. The two new findings: the stance F1=1.0 is a **tautological metric scoring the wrong classifier** — zero accuracy evidence, do not read as validation; the tone-transfer 0.61 is **inter-model noise on an unlabeled draft** (32% panel agreement), tolerable because tone is inert, but a hard prerequisite for any future tone-as-weight. The de-degeneration is substantially **real** but **unvalidated**. Greenlight Papa's spot-check after the gold rebalance; **block the stance lock** until a non-degenerate accuracy metric on the real classifier clears against Papa-reviewed labels; **block seed/apply** per the standing gates plus the phantom-head reconciliation.

— Kun 🔬
