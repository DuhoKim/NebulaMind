# KUN EXIT-GATE VERDICT — page58 slice-2b stance gate seed-readiness

- **Reviewer:** Kun (independent exit-gate; implementer must not self-certify)
- **Date:** 2026-06-23 KST
- **Scored artifact:** `local_stance_classifier_score_20260623T064710Z.json`
- **Host:** Duhoui-MacStudio.local (NebulaMind local)

## Containment verified (read-only)
- Locked gold sha256 = `de7ec421d5092e5cccb7a1b70af4fc84463aaad08164a30c8e2a2eadd0bdbe27` — **MATCH** (`stance_gold_LOCKED_v1.jsonl`).
- Score JSON sha256 = `b9a27dc38c4ea5e2ec7a931d74b3c56fe9ee3f13b4a16864d3c8cca6f7bbd205` — **MATCH**.
- Score MD sha256 = `d9f3ab4a99b5925b6fcedefd7ec39b98e7eba2a9909c75ce5d8a82f82809f273` — **MATCH**.
- Artifact self-attests: db_write_count 0, no_db_apply, no_alembic, no page57/58 live write, no stance-lock write, paid_lane untouched. NM HEAD 4ba9675, /api/health 200.
- This verdict file is a new analysis artifact only. **Kun authorizes NEITHER seed NOR write.**

---

## 1. THE BAR

Set by the wiki failure cost, not by generic ML thresholds. Cardinal sins (each has halted this page-family before):
- **false `supports` → inflated trust** (false-consensus).
- **false `contradicts` → phantom conflict** (hollow-debate).
- Safe failure mode = **under-labeling** (a true support/contradict seeded as neutral `related_different_facet`): loses signal, fabricates nothing.

Two separate bars, per the two use modes:

### Bar (a) — Stage-1 used ONLY as a relatedness filter
Stage-1 decides related-vs-unrelated and **casts no vote / moves no trust**; "related" rows must render as neutral, non-voting context. Worst case = some off-topic neutral context shown + some real context dropped. Lenient bar:
- **related-class precision ≥ 0.85 AND recall ≥ 0.80**, AND "related" must not itself render as a trust-bearing vote.

### Bar (b) — Stage-2 sign auto-applied to LIVE evidence
Stage-2 writes a trust-bearing label (`supports`/`contradicts`) directly onto live evidence. Strict bar — **each auto-written trust-bearing class** must clear BOTH:
- **precision ≥ 0.90** on the locked gold (≤1 in 10 votes fabricates trust/conflict), AND
- **n_true ≥ ~10** so the precision is statistically estimable. A class you cannot measure, you cannot auto-write.

`related_different_facet` is **trust-neutral** and therefore exempt from the 0.90 trust bar — but only *if* the live scorer treats rdf as casting no support/challenge vote (load-bearing condition C1 below).

---

## 2. CERTIFICATION

### Bar (a) Stage-1 filter — **PASS**
- related: P **0.9333** / R **0.8909** / F1 0.9116 (n=110; 98 caught, 12 dropped). Clears 0.85 / 0.80.
- unrelated: P 0.50 / R 0.6316 (n=19; 7 leak through as related). The 7 leaks are the weak spot but are tolerable **only** because, downstream, they become neutral rdf and cast no vote.
- Verdict: usable as a recall-oriented pre-filter that gates what reaches the sign stage / human. "related" ≠ on-page vote.

### Bar (b) Stage-2 sign auto-apply — **FAIL**
- **`supports` P 0.4884** (n_true=21, all caught). Predicted-supports = 43 = 21 true + **22 false** (true-rdf→supports). **51% of `supports` calls are fabricated trust.** Fails the 0.90 precision bar by ~0.41.
- **`contradicts` precision ≈ 0.0556** (predicted 18 = 1 real sentinel + **17 false** true-rdf→contradicts). P/R/F1 = `not_computed_n_equals_1_sentinel_only`. **Fails on precision AND on sample** — uncertifiable at n=1. The sentinel being classified *correctly* does not help; the class is wrong 17 of 18 times it fires.
- `related_different_facet`: P **1.0** (stage-2-only) / 0.8409 (composite, due to 7 stage-1 leaks) — the one safe class.
- macro-F1 excluding contradicts = 0.6241 (stage-2) / 0.5916 (composite). The explicit *exclusion* of contradicts from macro is itself a tell that the class is uncertifiable.

**Net: the gate as currently configured (auto-applying Stage-2 sign) FAILS for auto-seed.** Both trust-bearing classes reproduce, on the locked gold, the precise false-consensus + hollow-debate anti-patterns this page-family has been halted for.

### Overall: **CONDITIONAL**
- **AUTO-APPLY Stage-2 sign to live page-58 = FAIL.**
- **Stage-1 filter + rdf-only neutral auto-seed = CONDITIONAL-PASS** (conditions C1+C2 below).

---

## 3. DISCREPANCY RESOLVED (the `no_stage2_prediction` note)
Not a mapping bug and not a scoring bug in production terms. The 12 `no_stage2_prediction` rows are **Stage-1 false-negatives**: 12 true-rdf rows that Stage-1 labeled *unrelated* (they ARE the "related→unrelated = 12" cell of the Stage-1 confusion), so Stage-2 never ran. Evidence: `supports` recall is 1.0 and the sentinel reached Stage-2, so all 12 drops come from the 88 rdf. The `{"neither":"related_different_facet"}` mapping IS applied for every row that reached Stage-2 (rdf=37 includes the neither→rdf successes); it simply cannot apply to rows Stage-2 never saw.
- **Seed-time behavior is SAFE**: a Stage-1-dropped row is not seeded — no orphan, no undefined label.
- **Effect on metric**: rdf recall is mildly understated because 12 Stage-1 drops sit in the Stage-2 rdf denominator. Stage-2 recall on the 76 rows that actually reached it = 37/76 = **0.4868** (vs 0.4205).
- **Fix is REPORTING-only** (attribute the 12 to Stage-1 recall, or report Stage-2 recall on the 76). No production code change; **tau_rel needs no change for safety.**

---

## 4. MINIMAL GATE CHANGE (smallest viable, not a redesign)

Do **not** auto-apply Stage-2 sign. Concretely:

1. **Auto-seed writes ONLY `related_different_facet`** (neutral related context). Everything that passes Stage-1 and is not a human-confirmed support/contradict seeds as neutral rdf. Worst case = neutral context, possibly off-topic for the 7 Stage-1 leaks, and true supports/contradicts under-counted — all safe (no trust inflation, no phantom conflict).
2. **Suppress local `contradicts` → human-review queue.** 18 predicted contradicts (1 real + 17 phantom); the machine never auto-writes a conflict.
3. **Hold local `supports` out of auto-write → human-review queue.** 43 predicted supports (21 real + 22 phantom); collapse to rdf for the auto pass, queue the 43 for optional human promotion. (Volume is small; human recovers real signal without the machine fabricating it.)
4. **C1 — verify rdf is trust-neutral** in the live scorer (no contribution to the supports/challenge tally that sets the trust tier) **before any auto-seed.** This is the load-bearing condition: if rdf counts as a soft support, even rdf-only auto-seed must be gated.
5. **C2** — re-score the reconfigured (sign-suppressed) gate on the locked gold before auto-seed; this verdict certifies the *current* scores, not a yet-unbuilt config.

**Do NOT chase a tau_vote tweak as the fix.** The false supports/contradicts come from a *semantic* confusion (supports vs different-facet; contradicts vs different-facet), not low confidence; there is no evidence here that any tau reaches 0.90 supports-precision, and tuning a threshold on the same locked gold you certify against overfits the lock. The gate's own model name — `local_panel_provisional_no_claude_for_full_pass` — already declares the sign stage provisional.

**Non-blocking residual:** the 7 Stage-1 unrelated-leaks seed as neutral rdf = mild off-topic context, no trust move. Optional light human skim of the auto-rdf set on a flagship page.

---

## 5. BOTTOM LINE
- **FAIL** to auto-apply Stage-2 sign (supports P 0.49 → trust inflation; contradicts ~0.06 / n=1 → phantom conflict + uncertifiable).
- **CONDITIONAL-PASS** for a sign-suppressed gate: Stage-1 relatedness filter + rdf-only neutral auto-seed, supports/contradicts routed to human, conditioned on rdf trust-neutrality (C1) and a re-score of the reconfigured gate (C2).
- Kun authorizes neither seed nor write. Gate re-opens on a re-scored sign-suppressed config or a genuinely improved sign stage (e.g., Claude-in-loop) with contradicts n large enough to measure.
