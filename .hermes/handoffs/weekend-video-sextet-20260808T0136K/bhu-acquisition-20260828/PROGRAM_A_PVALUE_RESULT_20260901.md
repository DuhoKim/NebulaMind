# Program (A), re-aimed — the p-value shift. First real number.

**OVERNIGHT ANALYSIS ONLY.** Relayed by Blanc as an *unverified* pane line and treated exactly as
Blanc scoped it: analysis work producing reasoning and receipts. **It closes no open question,
answers nothing, and moves no tier.** Entries 23–27 remain QUALITATIVE-DIRECTIONAL; every tier
decision waits for Duho's verified word at the 07:00 handover.

Receipt: `cutoffA_pvalue_shift.py`, run to completion.

## The result

| model | S₁/₂ of mean spectrum | P(Ŝ ≤ 1150 μK⁴) | shift vs ΛCDM |
|---|---|---|---|
| ΛCDM | 34,924 μK⁴ | **0.126%** | — |
| causal cutoff, `k_§ = 2π/χ_§` | 6,897 μK⁴ | **3.188%** | **25.4×** |
| causal cutoff, `k_§ = π/χ_§` | 14,000 μK⁴ | **0.354%** | 2.8× |

**In one sentence: the causal cutoff moves the low-ℓ anomaly from p ≈ 0.13% to at most p ≈ 3.2% — a
25× improvement that still does not make the observation typical.**

## Why this framing is sound where the charter's was not

Both refuted defects are structurally fixed, not patched:

- **§1ao (the class contained its own degenerate solution).** There is **no optimization here** — a
  single licensed spectrum is *evaluated*. There is no free band, so no degenerate member to find.
  The cut sits at `k_§` and nowhere else, and **`k_§` is pinned by the source**: Eq. 23,
  `χ_§ = (3.149 ± 0.006) c/H₀` = 14,015 Mpc. That is precisely the asymmetry §1ao says to check —
  `k_§` was pinned by the paper, `k_norm` never was, so only the pinned one is used.
- **§1an (a point prediction compared against a realization).** Both sides are now sampling
  distributions of the same estimator. **The reductio control that the charter's rule failed, this
  one passes:** applied to ΛCDM it returns 0.126% — unlikely-but-possible — rather than "refuted".
  That 0.126% also independently reproduces the known ~0.1% low-ℓ anomaly significance, which is
  corroboration that the operator is right.

**No completion is needed and no amplitude is calibrated.** Above the cut the spectrum is ΛCDM's
own, fixed by high-ℓ data; the low-ℓ data sets nothing. The obstruction that killed three prior
attempts (READING_C: the paper contains no initial-conditions model) simply does not bind on an
evaluation of this kind.

**Corroboration of the earlier lanes:** the cutoff's S₁/₂ means (6,897 and 14,000 μK⁴) land inside
the 6,230–22,327 μK⁴ band the earlier blind seats reported for "principled completions" — computed
here by a completely different route.

## What must be said against it

1. **The convention matters, by a factor of nine in the p-value.** `2π/χ_§` gives 3.19%; `π/χ_§`
   gives 0.354%. The source does not fix which is meant. **The headline claim must therefore be the
   weaker one** — "at most ~3%" — and any writeup that quotes only 3.19% is overselling.
2. **Full-sky throughout; the published ~1,150 μK⁴ is a CUT-SKY number.** Absolute p-values here are
   therefore not directly comparable to the literature. The *shift* between two models computed
   identically is far more robust than either endpoint, which is why the shift is the reported
   quantity — but this caveat is real and unresolved.
3. **The a-fortiori claim is the physics gate's, and I have NOT independently verified it.** The
   gate holds that Reading A (hard IR cut) is *hyperuniform* and therefore the model-favourable
   reading, so Reading B cannot suppress S₁/₂ better and this is an upper bound on how much the
   causal condition can help. **Per register §1ap I flag rather than assert it**: it is a claim that
   flatters the negative conclusion, which is exactly when a check gets skipped. Verifying it is the
   obvious next step.
4. **Unlensed spectra, nonlinear off** — both on the gate's own repair list, and both models computed
   identically. Defensible at ℓ ≤ 100, and it also avoids an HMCode convergence failure on the
   hard-cut spectrum; but it is a deviation from the observed (lensed) sky and should be stated.
5. **`S₁/₂` remains an a-posteriori statistic**, chosen historically because it maximizes the
   apparent anomaly. The p-value shift framing is much less exposed to that objection than a
   threshold test would be, but it does not eliminate it.

## What this would mean, if it survives review

A defensible, quantitative statement about the corpus's one a-priori prediction that nobody has
made: **the causal cutoff is a real but insufficient explanation of the large-angle deficit.** It
improves the odds of the observed sky by up to ~25×, and leaves it at the few-percent level rather
than removing the anomaly. That is neither the "it explains the anomaly" of the source nor the
"it says nothing" of a dismissal — and both halves are new.

**Not yet done, and required before any of the above is claimed anywhere:** independent verification
of point 3; a cut-sky treatment for point 2; and an adversarial gate on the whole thing. **No tier
implication is drawn here, and none may be drawn without Duho.**

---

## The §1ap flag, discharged — and a second finding that may matter more

`cutoffA_afortiori_check.py`, run to completion. Last section flagged that the "upper bound" status
of the ~3% figure rested on the physics gate's unverified claim that the hard IR cut is the
*model-favourable* reading. Tested rather than left standing:

| spectrum | S₁/₂ of mean spectrum | P(Ŝ ≤ 1150) |
|---|---|---|
| ΛCDM, no cut | 34,924 | 0.106% |
| **HARD cut (Reading A)** | **6,897** | **3.312%** |
| smoothed, width 0.3 k_§ | 6,113 | 3.119% |
| smoothed, width 1.0 k_§ | 8,713 | 1.934% |
| smoothed, width 3.0 k_§ | 10,095 | 1.932% |
| adversarial: excess power below k_§ | 157,151 | 0.001% |

**The a-fortiori claim survives.** Nothing tested beats the hard cut. This is the right family to
test because Paley–Wiener forces any Reading-B spectrum to be *entire*, hence to approach the cut
smoothly — so the smoothed cuts are Reading-B-compatible where the hard cut is not.

**Stated limitation, per the absence-claim standard.** *Pattern:* hard cut vs smoothed cuts at the
same `k_§`. *One class it misses:* a Reading-B spectrum need not be a smoothed ΛCDM at all — it could
carry different structure near `k_§`. *What was done anyway:* the most hostile cheaply-available
member was included — excess power *below* `k_§`, which is what the compact-ξ construction actually
produces (measured earlier: under Reading B, `P` is **largest at the smallest k**). It loses
catastrophically (0.001%). So the claim survives the most adverse member available, but **this is a
family test, not a proof over all of Reading B**, and must not be quoted as one.

### The second finding

The paper claims (L457) that "**CMB temperature should not be correlated above θ > θ§ ≃ 60 deg**" —
which is the statement `S₁/₂ = 0`. Its own most favourable implementation does not deliver that:

> **the hard cut leaves `S₁/₂ = 6,897 μK⁴` — six times the OBSERVED 1,150, and only 5.1× below
> ΛCDM's 34,924.**

So the causal cut produces a **partial** suppression, not the vanishing correlation asserted. It
moves ~4/5 of the way in `S₁/₂` and ~25× in probability, and then stops — overshooting the observed
value by a factor of six. This is a sharper and more direct statement about the paper's own claim
than the p-value shift, because it needs no distributional argument at all.

**MC precision, noted honestly:** the ΛCDM baseline reads 0.106% here against 0.126% in the previous
run (different seed, 100k vs 200k draws) — consistent within ~1.5σ of Monte-Carlo scatter, but it
means the headline figures carry a relative uncertainty of order 10% and should be quoted as
"~0.1%" and "~3%", never to three digits.

**Unchanged:** analysis only; no tier moves; the cut-sky treatment and an adversarial gate on all of
this are still owed before any of it is claimed anywhere.
