# DETECTION_VERDICT — adversarial ruling on Phase B "validated detection"

**Referee:** Goru (skeptic/gate) · **Ruled:** 2026-07-20 16:18 KST · **Run:** overnight-z7-mzr-v2-detection-20260720 (Pick #1)
**Governing docs:** DETECTION_PREREG.md (locked truth table + honesty guardrail), PHASE_B_RESULTS.md, detection_results.json, DATA_ACQUISITION.md.

---

## 1. Does the word "detection" survive? — NO (as an unqualified word). The mechanical PASS is a bookkeeping artifact.

Phase B fired truth-table cell #1 mechanically: PASS_S=2, PASS_C=2, PASS_O=TRUE. I reject the mechanical firing, on
the record of Phase B's own independence cross-match:

- **The two "independent axes" collapse to ONE N=4 set doing double duty.** Heintz's 11 CEERS objects are the same
  public CEERS/NIRSpec galaxies as Nakajima's (redshift match <0.01, ~8/11). The only cleanly-independent Heintz
  contribution is the 5 lensed (N=4 with measured O/H in overlap). So axis S ("≥2 independent surveys") and axis O
  ("orthogonal subsample survives") are carried by the **same 4 lensed galaxies**. The rule counted one small anchor
  twice. Strip the double-count and the emission-line side is effectively a **single survey** (Nakajima N=16; Heintz
  CEERS duplicate it; Curti+24 unreachable per-object) — the very "Nakajima-23-specific artifact" guard that S≥2 exists
  to provide is NOT independently satisfied. The prereg's own guardrail says adding more of the same selection cannot
  break the degeneracy; conversely, letting the degeneracy-breaker also stand in for the independent-survey axis is not
  two confirmations, it is one.

- **N=4 is fragile, and the 4 are a distinct metal-poor population.** Bootstrap of 4 values cannot probe tail behavior;
  the CI (KE08 [+0.335,+1.00], Curti20 [+0.475,+1.075]) and LOO floor (+0.60) exclude 0 arithmetically, but they rest on
  4 lensed dwarfs that happen to be strongly metal-poor (O/H 7.29–7.97). "CI excludes 0 at N=4" is a necessary condition
  the rule required, not the robust multi-object confirmation the word "detection" advertises to a reader.

- **What IS real (do not bury it):** the deficit does NOT collapse under orthogonal (lensed, continuum/dropout)
  selection — it GROWS to +0.68/+0.78 dex — and it survives a fully Te-anchored, KE08-independent calibration
  (Curti+2020 ≥ KE08 on every cell). Selection can therefore **no longer be the sole explanation** of the z>7 deficit;
  the selection↔evolution degeneracy the prior run could not break is genuinely broken here. That is the load-bearing
  advance the prereg identified (axis O), and it stands. This is a real, publishable step beyond cell #2.

**Ruling:** the evidence is genuinely stronger than cell #2 (selection IS broken) but strictly weaker than cell #1
(the S and O axes are not independent; they are one N=4 anchor). The honest cell is a **refinement between #4 and #1**:
selection-broken and multi-calibration, but the independent-survey axis is not independently met — so the locked word
**"validated detection" is NOT earned.** Honesty guardrail applied: "detection"/"validated" are forbidden outside a
genuine cell #1.

## 2. Final honest label (one sentence, limiting caveat in the same sentence — per the guardrail)

> **Selection-robust z>7 MZR deficit — a mass-controlled 12+log(O/H) shortfall of ~0.45–0.55 dex (Nakajima+23, N=16)
> that survives two independent local calibrations (KE08 and the Te-anchored Curti+2020) and, critically, does NOT
> collapse but GROWS to ~0.68–0.78 dex in an orthogonally-selected lensed subsample — breaking the selection↔evolution
> degeneracy and giving strong evidence for genuine chemical evolution; but the second-survey and orthogonal axes both
> rest on the SAME 4 lensed galaxies (Heintz's CEERS objects duplicate Nakajima's), so this is confirmation on a single
> small (N=4) orthogonal anchor, not a fully independent multi-axis detection — pending a larger, independent
> orthogonally-selected sample.**

Title/abstract/verdict must use this; the words "detection", "validated", "measurement of evolution" are barred until
the N=4 / S≡O collapse is retired.

## 3. The one decisive next step

Pull a **second, larger, independently-selected orthogonal sample** — lensed-cluster or deep-continuum/dropout z>7
galaxies with O-based O/H in [8.0,9.5], from fields NOT in Nakajima+23 (e.g. additional Heintz cluster fields, UNCOVER/
Abell-2744, GLASS/A2744 continuum, or a JADES deep-continuum cut with per-object O/H). If the orthogonal deficit's CI
still excludes 0 at N≳15 **independent of the emission-line survey axis**, axes S and O separate, the double-count
dissolves, and cell #1 ("validated detection") fires honestly. This single addition is make-or-break; nothing else is.

## 4. Referee verdict on the paper this becomes: **MINOR revision**

The data are sound and the central novel claim (selection-robust deficit confirmed on an orthogonal subsample) is
ALREADY supported by the numbers on disk — no reanalysis or new data is needed for a fully publishable, genuinely new
result. Only the label is overclaimed. That is a MINOR, not MAJOR, revision — but the three conditions are
non-negotiable and touch the title:

- **C1 — Strike "validated detection."** Retitle/abstract to the §2 sentence. Demote the mechanical "cell #1" to the
  refined honest label; state explicitly that the rule fired cell #1 only because one N=4 anchor was counted on two axes.
- **C2 — Same-sentence caveat everywhere.** Every headline number (0.45–0.55 / 0.68–0.78 dex) carries its dominant
  caveat in the same sentence: for the orthogonal number, "N=4, and the 2nd-survey and orthogonal axes are the same 4
  lensed galaxies." No figure or number floats free of it.
- **C3 — Report the N=4 fragility honestly** (bootstrap + LOO floors, the intrinsically metal-poor nature of the 4
  lensed dwarfs, and that Curti+24 was unreachable per-object so the emission-line side is effectively single-survey);
  keep the full-Heintz N=13 / CEERS-only N=9 runs labelled non-independent sensitivity, not confirmation.

Meets these → publishable as a strong selection-robust result. Add the §3 orthogonal sample → resubmit as the
validated detection.
