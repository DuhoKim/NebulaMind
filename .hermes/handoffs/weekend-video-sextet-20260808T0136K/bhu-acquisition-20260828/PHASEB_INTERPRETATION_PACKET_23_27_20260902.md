# Decision packet — do the phase (b) numbers change how we file Gaztañaga's 60° cutoff (entries 23–27)?

**Date:** 2026-09-02 · **Author:** Tori · **Ordered by Duho in direct chat:** "start the phase (b) interpretation packet for 23–27".
**Status:** GATED `PACKET_SOUND_WITH_REPAIRS` (codex, `PACKET_GATE_codex.md`, 15:58 KST; three wording repairs applied: the 1-in-500/670 range, the 2,000-vs-500 sky counts, the receipt pointer). Filed to `OPEN_QUESTIONS_FOR_DUHO.md`.
**Nothing in this packet moves a tier. The stamp is Duho's.**

## The question in everyday words

Gaztañaga's papers make the one prediction in this corpus that was written down before the data it
speaks to: the sky should lose its large-angle correlations beyond about 60°. The sky does show a
weak large-angle correlation. Program (A) asked whether the papers say *how much* weaker, and found
they do not. Phase (b) then asked: if we complete the prediction in the most natural ways we could
find, does the observed sky become a normal sky under the model? **Answer: not quite. It goes from roughly a
1-in-500 to 1-in-670 sky to, at best, a 1-in-40 sky.** What to do with that in the bibliography is the decision.

## What is established (receipts, all in-lane, all gated)

1. **The scale is the paper's own and is not circular.** χ_§ = 3.149 c/H₀ from Ω_Λ measured elsewhere;
   θ_§ = 57.4° (paper rounds to 60 ± 3). `cutoffA_check_60deg_chain.py`; freedom map §1.
2. **The amplitude is not the paper's.** The papers supply no perturbation prescription; three seats
   returned `READING_C` and a fourth `CLASS_REFUTED` against the one proposed formalisation; the
   author himself: "it is impossible to quantify this without a model for the initial conditions"
   (2003.11544, L466). Freedom map §2.
3. **Every natural completion we built still leaves the observed sky unlikely.** Like-for-like on the
   masked Planck SMICA map, pre-registered, controls C1/C2/C3 passed, 5 × 2,000 skies in production, blind-doubled
   by codex from the prereg alone at 500 skies per row (`PHASEB_RESULT_RECONCILIATION_20260902.md`):

   | model | P(S₁/₂ ≤ observed) |
   |---|---|
   | ΛCDM | 0.15–0.20% |
   | Reading A, 2π/χ_§ (best row) | 2.2–2.8% |
   | Reading A, π/χ_§ | 0.4–0.8% |
   | Reading B, spliced | 1.1–1.6% |
   | Reading B, no splice | 0.60–0.65% |

   Best improvement over ΛCDM roughly 15×; no row above ~3%. Each row's number is attributable to a
   declared completion of ours, not to the theory (freedom map §6–§7).
4. **Two open flags stand against the prediction's logic** (freedom map §2): absence of causal contact
   does not by itself imply zero correlation (common initial conditions can correlate disconnected
   regions); and the paper's one derived condition, Φ(χ>χ_§)=0, has never been imposed on the
   perturbed solution by anyone, including us.
5. **Structural caveat:** every row assumes standard ΛCDM transfer physics with only the primordial
   spectrum modified; a genuine causal boundary could change more than that, and no receipt here
   constrains it (freedom map §7).

## Current filing

Entries 23, 25, 26, 27 are QUALITATIVE-DIRECTIONAL (27 promoted to match 25/26 on your ruling B(a),
2026-09-01); 24 is QUALITATIVE-DIRECTIONAL and subsumed by 23/25/26. 25/26 carry the RQ-C map
("scale-level CMB falsifier CANDIDATE … NOT yet calibrated: the papers supply no cutoff amplitude").

## Your options

- **(a) Keep QUALITATIVE-DIRECTIONAL; annotate all five with the phase (b) result.** One paragraph
  per entry (draft below), saying: direction confirmed in sign, scale a priori and non-circular,
  amplitude unfixed by the papers, and under every completion we tried the observed deficit stays at
  or below ~3%. *Cost:* none beyond the edit. *What it records:* the corpus's one real prediction is
  real but cannot be scored, and the best we could do for it still leaves the anomaly mostly
  unexplained. **Recommended.**
- **(b) Re-tier 23/25/26/27 to CALIBRATED-FALSIFIER, using our completions as the calibration.** The
  lane's threshold rule lets us supply a missing threshold and own it. *Cost:* it would file as
  "calibrated" a number Program (A) proved the theory does not fix (item 2), so any LIVE/FIRED
  standing would be a verdict on our construction, not on Gaztañaga's; it also contradicts the RQ-C
  annotation you ruled on 08-31. *Against.*
- **(c) Demote to CONSISTENCY-ONLY** on the ground that a direction with no fixable amplitude is not a
  test. *Cost:* throws away the genuinely a-priori 57.4° scale and the ~15× improvement in the
  predicted direction, both of which are real; treats "unscorable" as "unfalsifiable", which the
  freedom map does not claim. *Against.*
- **(d) Hold; name what else you want computed first** (e.g. imposing Φ=0 on the perturbed solution,
  item 4(ii), which nobody has done — real work, unbounded, and the author's own "in preparation"
  reference never appeared).

**Recommendation: (a).** Why it cannot be mine: the prereg reserved interpretation beyond the
percentile table to you (§5), and this touches the filing of five entries that carry the corpus's
headline prediction.

## Draft annotation for (a), for your edit or approval

> **Phase (b) map (2026-09-02; Duho ruling ___):** The 60° causal-horizon cutoff was tested
> like-for-like on the masked Planck SMICA map (pre-registered, controls passed, blind-doubled). The
> direction is right — every causal-cutoff completion raises the probability of the observed
> large-angle deficit, by up to ~15× — but the papers fix no amplitude (READING_C ×3; author's own
> L466), and under every completion we built the observed sky stays at or below the ~3% level
> (ΛCDM 0.15–0.2%). **Tier UNCHANGED (QUALITATIVE-DIRECTIONAL):** scale a priori, amplitude
> unscorable. Receipts `bhu-acquisition-20260828/PROGRAM_A_FREEDOM_MAP_20260902.md` §§1–2, 7, 9,
> `PHASEB_RESULT_RECONCILIATION_20260902.md`.
