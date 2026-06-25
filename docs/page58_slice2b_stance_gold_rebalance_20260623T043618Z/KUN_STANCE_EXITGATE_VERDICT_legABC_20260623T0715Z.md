# KUN EXIT-GATE VERDICT (FULL: LEG A + B + C) — page58 slice-2b stance gate

- **Reviewer:** Kun 🔬 (independent exit-gate; implementer must not self-certify)
- **Date:** 2026-06-23 ~16:15 KST (07:15Z)
- **Host:** Duhoui-MacStudio.local (NebulaMind local), NM HEAD `4ba9675`
- **Scored artifact:** `local_stance_classifier_score_20260623T064710Z.json`
- **Supersedes:** `KUN_STANCE_GATE_VERDICT_064710Z.md` (that file was LEG C only; this one folds in the
  LEG A gold-quality check and LEG B structural concurrence that gate whether the score is interpretable).
- **Containment:** read-only. Locked gold sha256 `de7ec421…dbe27` unchanged (re-hashed). No DB, no Alembic,
  no page57/58 live write, no stance-lock write, paid lane untouched. My analysis ran stdlib-only python
  reading the locked jsonl (scripts in `/tmp`, not the live tree). **Kun authorizes NEITHER seed NOR write.**

---

## 0. INDEPENDENT REPRODUCTION (precondition for any cert)
Recomputed every headline metric directly from the locked gold (not trusting the scorer's own output):
- Stage-1 related **P 0.9333 / R 0.8909** — match.
- Stage-2 supports **TP 21 / FP 22 → P 0.4884** — **byte-match** to the scored artifact.
- Stage-2 contradicts **TP 1 / FP 17 → P 0.0556** — match.
- Stage-2 confusion cells (1 / 17 / 12 / 37 / 22 / 21) reproduced exactly.
The scored artifact is faithful to the locked gold. The score is mechanically trustworthy; the only open
question is whether the **gold** it scores against is trustworthy — that is LEG A.

---

## LEG A — GOLD-QUALITY CHECK → **GOLD IS SOUND; SCORE IS INTERPRETABLE; NO RE-ADJUDICATION REQUIRED**

### Method (this was a CENSUS, not a spot-check)
I read base/intro text first-hand for **every gold row that touches a supports or contradicts decision**:
- all **22** false-supports (gold=rdf, gate=supports),
- all **21** true-supports (gold=supports, gate=supports) — i.e. *every* gold=supports row in the set,
- all **17** false-contradicts (gold=rdf, gate=contradicts), plus the n=1 sentinel.
That is the complete population where Claude-tiebreak bias on the supports↔facet (and facet↔contradicts)
boundary could matter. Each row judged against Papa's locked operating definition (supports = affirms the
assertion; rdf = different/complementary aspect, no denial; contradicts = denies the explicit assertion even
in a sub-regime, applying variable-degeneracy domain knowledge, not syntactic "names a different driver").

### Provenance correction to the brief's premise
The brief assumed "the rest were set by the Claude plan-lane tiebreak." Actual `label_source` histogram of
the locked 129: **papa 3, claude_tiebreak 55, qwen_gpt_agree 71.** Most non-Papa rows are panel-*consensus*,
not Claude-decided. The Claude-bias surface is the 55 tiebreak rows (15 of the 22 false-supports; 5 of the 17
false-contradicts). This *shrinks* the gold-error surface the brief was worried about.

### Finding 1 — the 22 false-supports are GENUINE GATE ERRORS, not gold errors
19/22 are clear-correct rdf; 3 are borderline (032, 046, 118); **0 are clear gold errors.** The intros are
structural section-outlines (105, 107), different mechanism/scale (026, 030, 038), simulation-method/artifact
notes (040, 041), correlation-vs-causation (042), scaling-relation facets (115), or investigative questions
(127) — **none affirm the base assertion.** Crucially, the gold-construction `gpt` model itself over-called
"supports" on many of these, and **Claude tiebreak *corrected* it down to rdf** (e.g. 018/027/038/116/118/
125/127). That is the *opposite* of the brief's hypothesis: Claude tiebreak *reduced* supports over-call in
the gold; it did not inflate it. The over-call lives in the **gate** (`prior_stance_label`), which reproduces
exactly the "same topic ⇒ supports" error the gold avoided.

### Finding 2 — the gold did NOT over-call supports (complete census of all 21 gold=supports)
17/21 are clear/strong supports; 3 defensible-but-weak (033 turbulence-vs-ejection; 034/035 a method
sentence that enacts the mechanism); 1 inconsistency (047, see Finding 3). **0 rows flip cleanly to rdf.**
So the gate's "21/21 supports recall" is real, not an artifact of a permissive gold.

### Finding 3 — one real gold defect: the 046/047 inconsistency (isolated, non-material)
`stance2b-046` and `stance2b-047` carry **identical base+intro** (arxiv 0901.1880 v1/v2) yet Claude tiebroke
them to **opposite** labels — 046→rdf, 047→supports. A programmatic scan confirms this is the **only**
(base,intro) pair in the entire 129-row gold with conflicting labels. One of the two is wrong; impact on the
metric is < 0.03 either way (see sensitivity). Worth a one-line Papa fix for hygiene; **not** a blocker.

### Finding 4 — the 17 false-contradicts are GATE over-calls; contradicts genuinely stays n=1
15/17 clear-correct rdf; 2 borderline (007 outflow fallback/recycling; 008 centrals-also-env-quenched);
**0 clear true-contradicts.** Many are the *exact* pattern Papa already overturned in mine-024/066
(BH-mass primacy co-varying with stellar mass — see 004, 009) or stellar-vs-AGN feedback in a different mass
regime (010, 011, 014, 016). The gate reproduces the syntactic "names opposite outcome / different driver ⇒
contradicts" error; the gold (and Claude tiebreak) correctly applies the denial test.

### Quantified gold-error vs gate-error (the number the brief asked for)
Of the **39** stage-2 sign errors (22 false-supports + 17 false-contradicts): **~34 are clear genuine gate
errors, ~5 are borderline** (gold defensible but a strict reader *might* side with the gate: 032/046/118 on
supports; 007/008 on contradicts), **0 are clear gold errors.**

**Gold-skeptical sensitivity (flip ALL 5 borderline rows in the gate's favor):**
- supports precision 0.4884 → **0.5581** (still fails the 0.90 bar by ~0.34),
- contradicts precision 0.0556 → **0.1667**, n_true 3 (still uninterpretable, still catastrophic).

**Conclusion:** the gold is good enough to certify against; the score is interpretable; the FAIL is a property
of the **gate**, not of a biased gold. The right output is a cert (LEG C), **not** "re-adjudicate N rows first."

---

## LEG B — STRUCTURAL CALLS → **CONCUR on both**

1. **Contradicts as a 1-row sentinel (n=1, not scored P/R/F1): CONCUR.** First-hand read of all 17 false-
   contradicts confirms none is a clear true-contradicts, so the class really is n=1 (stance2b-001). P/R/F1 on
   n=1 is statistically meaningless; the sentinel (does the gate emit the *one* true contradiction correctly —
   yes) is the correct treatment. The n=1 is a genuine **corpus** property, not a labeling artifact: an
   intro-citation corpus cites papers because they are relevant/supportive, and the denial test is strict.
   The mine pass (278 candidates, 1.1% surface, both overturned by Papa) independently confirms exhaustion.
2. **024/066 kept out of the scored set: CONCUR.** They are expert-ambiguous BH-mass-primacy papers — the very
   denial-cue that biases the draw — and Papa adjudicated both rdf. Including them would import an adversarial,
   non-representative subset. Note the scored set *already* contains the same pattern as on-distribution rdf
   (004, 009), so excluding 024/066 hides nothing from the gate; it just drops the two most adversarial draws.
   Keep them as the optional tagged hard-negative toggle.

   *One optional Papa-eyeball (does not change the call):* **008** is the single row that structurally rhymes
   with the confirmed contradicts 001 (it blurs the satellite/central "distinct" dichotomy, from the central
   side). I read it as rdf (it *adds* a central env-channel rather than asserting satellites are mass-driven),
   but it is the closest coin-flip in the set. Even if Papa flipped it, contradicts → n=2, still a sentinel,
   gate still over-calls 16/18 — the structural call holds.

---

## LEG C — SEED-READINESS CERT

### THE BAR (set by wiki failure cost, not generic ML thresholds)
Cardinal sins, each of which has halted this page-family before:
- false `supports` → inflated trust (false-consensus);
- false `contradicts` → phantom conflict (hollow-debate).
Safe failure mode = under-labeling (a true sign seeded as neutral rdf): loses signal, fabricates nothing.

- **Bar (a) Stage-1 used only as a relatedness pre-filter (casts no vote):** related P ≥ 0.85 AND R ≥ 0.80,
  and "related" must render as neutral non-voting context.
- **Bar (b) Stage-2 sign auto-written to LIVE evidence:** each trust-bearing class P ≥ 0.90 on the locked gold
  AND n_true ≥ ~10 (a class you cannot measure, you cannot auto-write). `related_different_facet` is trust-
  neutral, exempt from the 0.90 bar **iff** the live scorer treats rdf as casting no vote (condition C1).

### CERTIFICATION
- **Bar (a) Stage-1 filter → PASS.** related P 0.9333 / R 0.8909 (clears 0.85/0.80). The 7 unrelated-leaks are
  tolerable *only* because downstream they become neutral rdf and cast no vote. Usable as a recall-oriented
  pre-filter; "related" ≠ an on-page vote.
- **Bar (b) Stage-2 sign auto-apply → FAIL (robust after LEG A).**
  - supports P **0.4884** (≤ 0.5581 even gold-skeptical) — ~half of auto-`supports` would fabricate trust.
  - contradicts P **0.0556**, n=1 — fails on precision *and* on sample; uncertifiable.
  Both trust-bearing classes reproduce, on validated gold, the precise false-consensus + hollow-debate
  anti-patterns this page-family has been halted for.
- **OVERALL → CONDITIONAL.**
  - **AUTO-APPLY Stage-2 sign to live page-58 = FAIL / DO NOT SEED.**
  - **Stage-1 filter + rdf-only neutral auto-seed = CONDITIONAL-PASS**, conditions C1+C2 below.

### MINIMAL GATE CHANGE (smallest viable, not a redesign)
1. **Auto-seed writes ONLY `related_different_facet`** (neutral related context). Worst case = some off-topic
   neutral context (the 7 stage-1 leaks) + true signs under-counted — all safe.
2. **Suppress local `contradicts` → human-review queue.** 18 predicted (1 real + 17 phantom). The machine
   never auto-writes a conflict.
3. **Hold local `supports` out of auto-write → human-review queue.** 43 predicted (21 real + 22 phantom);
   collapse to rdf for the auto pass, queue the 43 for optional human promotion. Volume is tiny; a human
   recovers the real signal without the machine fabricating it.
4. **C1 (load-bearing): verify rdf is trust-neutral in the LIVE scorer** — no contribution to the
   supports/challenge tally that sets the trust tier — *before* any auto-seed. If rdf counts as a soft
   support, even rdf-only auto-seed must be gated.
5. **C2: re-score the reconfigured (sign-suppressed) gate on the locked gold before auto-seed.** This verdict
   certifies the *current* config; the gate's own model name (`local_panel_provisional_no_claude_for_full_pass`)
   already declares the sign stage provisional.

**Do NOT chase a tau_vote tweak as the fix.** The false signs come from a *semantic* confusion (supports vs
different-facet; contradicts vs different-facet), not low confidence; tuning a threshold on the same locked
gold you certify against overfits the lock.

### OPTIONAL GOLD HYGIENE (non-blocking, for Papa, does not affect this cert)
- Resolve the 046/047 identical-text label conflict (pick one of {rdf, supports}).
- If Papa wants the contradicts class airtight, eyeball 008 (and 007). Outcome cannot change the FAIL.

---

## BOTTOM LINE
- **LEG A:** gold is sound (complete census of all supports/contradicts-relevant rows; 0 clear gold errors;
  1 isolated 046/047 inconsistency; Claude tiebreak *corrected* gpt's over-calls rather than inflating them).
  The score is interpretable; the FAIL is the gate's, not the gold's. **No re-adjudication needed before cert.**
- **LEG B:** CONCUR — contradicts = n=1 sentinel (corpus genuinely exhausted), 024/066 stay out of the scored
  set. Optional Papa-eyeball on 008 cannot move the call.
- **LEG C:** Stage-1 filter **PASS**; Stage-2 sign auto-apply **FAIL**; overall **CONDITIONAL** — ship only a
  sign-suppressed, rdf-only neutral auto-seed, conditioned on C1 (rdf trust-neutral) + C2 (re-score the
  reconfigured gate). **Kun authorizes neither seed nor write.** Gate re-opens on a re-scored sign-suppressed
  config, or a genuinely improved sign stage (e.g. Claude-in-loop) with contradicts n large enough to measure.

— 🔬 Kun
