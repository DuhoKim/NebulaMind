# Phase 6 opening finding — our own classification of the falsifier is wrong

Tori, 2026-08-27 23:10 KST. First act of the phase: read the target from the source rather than
from our note. The note does not survive.

**Target:** Gaztañaga, Kumar, Pradhan & Gabler, *"Gravitational bounce from the quantum exclusion
principle"*, **Phys. Rev. D 111, 103537 (2025)**, DOI 10.1103/physrevd.111.103537.
Pinned text: `../bhu-reading-20260823/sources/2505.23877_clean.txt`.

---

## What our record says

`BHU_PUBLISHED_BIBLIOGRAPHY.md`, entry 54:

> Testability: **CALIBRATED-FALSIFIER**. […] The family's only LIVE numeric falsifier: predicted
> closed curvature −0.07 ± 0.02 ≤ Ω_k < 0; **a confirmed flat universe refutes it.**

And `TORI_TO_HWAO_LIVE_FALSIFIER_20260823T1450K.md`, which I sent to Hwao on 23 August:

> **A confirmed flat universe kills it.**

**Both are wrong on the falsification condition.** The bracket is real; what it means is not.

---

## What the paper actually says

### The prediction is a scaling relation, not a window — Eq. 27, §VI, verbatim

> `Ω_k ≡ −k(1/H_0)² = −(0.07 ± 0.02)(χ_*/χ_k)²`

with, from the top of §VI:

> "Recall from Eq. 8 that χ_k needs to be larger than the cloud boundary: **χ_k > χ_***."

Since `χ_k > χ_*`, the factor `(χ_*/χ_k)² < 1` **strictly**. So Eq. 27 does not predict a value.
It supplies a **ceiling on the magnitude**:

    −0.09 ≲ Ω_k < 0        (taking the +1σ edge of 0.07 ± 0.02)

The −0.07 ± 0.02 is the abstract's "lower bound" — the *most negative* Ω_k can be. Ω_k may lie
anywhere between that and zero, approaching zero arbitrarily closely as χ_k grows.

### And the magnitude is conditional — the paper says so itself

The 0.07 ± 0.02 descends from `χ_* ≃ 15.93 ± 2.22 Gpc` (Eq. 26), which descends from
`θ_cut ≃ 65.9 ± 9.2 degrees` (Eq. 25, Camacho-Quevedo & Gaztañaga 2022) — i.e. from reading the
CMB homogeneity scale and low quadrupole as the cloud boundary. The authors then withdraw their
own insistence on it, verbatim:

> "The limits for Ω_k above **assume that the homogeneity scale is the result of only χ_***. […]
> **However, if the homogeneity scale or the low value of C₂ has a different origin, then the
> value of Ω_k in the floating FLRW cloud could be smaller.** Inflation preceded by a bounce
> requires **Ω_k < 0**."

The last sentence is the model's actual hard content.

---

## The correction

**The hard prediction is a SIGN: `Ω_k < 0`.** The magnitude ceiling is conditional on an
auxiliary identification the paper declines to insist on.

Therefore:

| | |
|---|---|
| **Refuted by** | a confirmed **OPEN** universe, `Ω_k > 0` — or a confirmed `Ω_k < −0.09` (too closed) |
| **NOT refuted by** | a flat measurement. `Ω_k = −0.0001` satisfies the model exactly, and no finite-precision measurement excludes it |

Our record has the falsification condition **backwards on the near side**. "A confirmed flat
universe kills it" is false: flatness is where this model is *comfortable*, because χ_k ≫ χ_*
drives Ω_k → 0⁻ while keeping the sign.

**This matters operationally.** The DESI curvature watch (hermes cron, Mondays 10:00 KST) exists
to flag movement against this falsifier. If it is watching for a flat result as the kill
condition, it is watching the wrong side of zero.

---

## What this does to the classification

**CALIBRATED-FALSIFIER is not the right tier for this paper as written.** A calibrated falsifier
needs a number and a threshold — entry 7 (Brown/Lee/Rho 2008: `M_max ≈ 1.5 M☉`, falsified by a
`≳ 2 M☉` neutron star) is what that tier looks like, and it *fired*. Entry 54 supplies a sign
plus a soft, self-withdrawn ceiling.

I am **not** unilaterally re-tiering it. The bibliography is a gated artifact and the change
should be adjudicated, not asserted by the person who got it wrong the first time. Proposed for
gate: demote to a new or existing tier meaning *one-sided sign prediction, falsifiable only from
the open side*.

**Note against myself:** I classified this on 2026-08-23 having, per the record, read the paper
in full. The abstract states the bracket in the compact form our note copied. The qualification
sits in §VI, four sentences after Eq. 27. I copied the abstract's framing and did not carry the
section's caveat — the same failure the anchor-block law exists to prevent, and the same one that
cost this lane a phase headline earlier today.

---

## What the study becomes

Not "does current data fall inside the window". The real questions:

1. **Is `Ω_k > 0` excluded, and at what significance, by current published constraints?** That is
   the live falsification test, and it is answerable from published Planck / ACT / DESI results.
2. **Does the paper's observational support survive dataset selection?** §VIII cites "Planck PR3
   lensed power spectrum revealed a 3σ preference for positive curvature […] Ω_k ≃ −0.04 ± 0.01",
   plus ACT and DESI "hinting". Planck-alone closed preference is a known, contested feature
   entangled with the lensing-amplitude anomaly, and CMB+BAO combinations pull to flat. Whether
   the paper's cited support is combination-selected is a checkable question with a real answer.
3. **Is the χ_* identification independently supported**, or does the model's only number rest on
   one group's own prior homogeneity-scale measurement (Camacho-Quevedo & Gaztañaga 2022, same
   lead author)?

Question 3 is the one I would attack first if I were gating this paper.

---

*Next action: pull current published Ω_k constraints from primary sources — not from memory —
for CMB-alone, CMB+lensing, and CMB+BAO/DESI, and confront (1) and (2).*
