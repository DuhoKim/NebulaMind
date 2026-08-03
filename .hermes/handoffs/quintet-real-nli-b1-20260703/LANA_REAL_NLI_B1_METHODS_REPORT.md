# Lana — Real-NLI Wave B1 methods / gate review

Task: Quintet real-NLI B1 methods/gate review · Lane: Lana (semantic methods & gate reviewer) · Read-only except this report.
Written: 2026-07-03, repo `/Users/duhokim/NebulaMind/NebulaMind`. **No DB/SQL/migrations/deploy/git/Step-8 prose. NLI predictions are not treated as truth.**

## Verdict: **PASS_WITH_PATCHES**

The B1 evaluation is a **valid, reproducible tool-evaluation artifact** that reached the correct top-line conclusion (`auto_stance_authority = False`, `step8_unlocked = False`). What must be patched is the *interpretation*: the run's per-model `b1_fully_satisfied: True` is true only in the sense that *the experiment ran and answered its question* — it does **not** mean B1 delivered the guard it was built for. It didn't. The intended purpose of B1 was a mechanical contradiction/overclaim guard before Step 8, and **all three models have contradiction recall ≈ 0** (0.00, 0.00, 0.33). B1-as-experiment passes; B1-as-Step-8-safety-net fails.

## 1. Was real-NLI B1 executed reproducibly on all 45 rows? — YES

`rows_loaded: 45`, `total: 45`, `all_rows_loaded_each_run: True`, `b1_real_nli_run_complete: True` for all three models. The script is deterministic (softmax → argmax with a fixed 0.55 threshold, no sampling), runs three real Hugging Face NLI checkpoints in an isolated venv, and writes per-model results/validation artifacts. Model downloads and venv installs were operator-authorized; safety ledger is all-zero on writes/deploy/git/Step-8. Reproducibility is satisfied.

## 2. Is the script / mapping sane for a tool-evaluation artifact? — YES, with a structural caveat

The mapping is conservative and defensible for a smoke test:
`contradiction ≥ 0.55 (and max) → contradicts; entailment ≥ 0.55 (and max) → supports; else → qualifies`.

Two structural limits that the Quintet must not gloss over:
- **"qualifies" is the residual bucket, not a learned class.** It captures *neutral OR low-confidence*, so it conflates genuine qualification with model uncertainty. This is why `qualifier_recall` is high (0.90–1.00) while overall accuracy is low (0.22–0.38): the models dump everything they are unsure about into `qualifies` and catch the real qualifiers by accident of the residual mapping. **`qualifier_recall = 1.0` is an artifact, not validation of qualifier understanding.**
- **NLI "contradiction" ≠ scientific "contradicts."** Our gold `contradicts` cases are *scope/attribution/alternative-mechanism* refutations (Peng 2015: strangulation over AGN; Sarzi 2016: SF-driven, not AGN). These rarely raise the NLI contradiction probability above 0.55, so the contradiction branch almost never fires → **contradict_recall ≈ 0**. This is the disqualifying failure for B1's intended purpose.

The script is sane enough to *trust the measurement*; the measurement says generic sentence-pair NLI is the wrong instrument for scientific claim–evidence stance.

## 3. Adoption decision

**Assistive triage only (narrow), plus rerun with a different design. Do not adopt as authority; do not quarantine entirely.**

- **The one usable signal:** `ynie/roberta-large-...` has `support_precision = 0.875` — when it predicts entailment, it is a genuine support ~7/8 of the time. That is usable as a **weak "likely-support → human spot-check" prior**, and nothing more.
- **Hard limits on that use:** because contradiction recall is ~0, the model is **blind to refutations**. It must **never** influence `contradicts` or `qualifies` decisions — a triage that is blind to contradiction is worse than no triage if trusted, because it would let refuting papers pass as "not-support → qualifies." So the assistive use is one-directional (surface likely-supports for review) and never subtractive.
- **Rerun with the right instrument:** the generic-NLI (SNLI/MNLI/FEVER/ANLI) family answered its question — insufficient. Before B1 can count as a working Step-8 contradiction guard, rerun with a **scientific claim-verification design**: SciFact / MultiVerS-style models trained on claim↔evidence with SUPPORT/REFUTE/NOINFO + rationale, **or** a calibrated LLM entailment prompted explicitly on scope/attribution ("does this span establish *this scoped* assertion, or does it attribute the effect elsewhere?"). Retain the roberta support-precision result as the baseline to beat.
- **Net:** quarantine the "NLI-as-stance-authority" idea; keep the narrow assistive support-triage; schedule a redesigned Wave B1′.

## 4. Does this unlock Step 8 automatically? — NO

Not automatically; **operator approval is still required** (the safe default holds, and the artifacts already record `step8_unlocked: False`). Strengthened by this review: since B1 did **not** produce a reliable contradiction guard, Step 8 must **not** lean on this NLI as its overclaim/contradiction safety net. If the operator later approves Step 8, contradiction and scope review remain **human/jury-authoritative**, and ideally the redesigned verifier (B1′) lands first. The mechanical guarantee "modality ≤ certainty / every sentence binds to a findings-level rationale" cannot currently be delegated to this NLI.

## Patches (summary)

1. Reframe `b1_fully_satisfied: True` in downstream cockpit/board text as **"experiment complete; intended guard NOT achieved (contradict_recall ≈ 0)."**
2. Adopt `roberta-large` only as **narrow, one-directional assistive support-triage** — never authority, never for `contradicts`/`qualifies`.
3. Do not cite `qualifier_recall = 1.0` as validation — flag it as a residual-mapping artifact.
4. Schedule **Wave B1′** with a scientific claim-verification model (SciFact/MultiVerS) or calibrated LLM entailment that can detect scope/attribution contradiction.
5. Keep Step 8 operator-gated; do not use this NLI as its contradiction safety net.

## Safety ledger (this review)

- DB writes: 0 · SQL: 0 · migrations: 0 · deploy/restart: 0 · product/wiki publish: 0 · git: 0 · Step-8 prose: 0 · secrets printed: 0
- Reads: master brief, comparison JSON, comparison packet, benchmark script, gold stance matrix / ledger (read-only). Files written by Lana: 1 (this report).

LANA_REAL_NLI_B1_METHODS_DONE_20260703
