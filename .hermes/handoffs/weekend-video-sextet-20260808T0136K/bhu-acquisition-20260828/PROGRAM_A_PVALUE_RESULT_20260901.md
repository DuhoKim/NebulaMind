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

---

## GATED at last — `PVALUE_RESULT_REFUTED`. C1 is retracted; C2 survives and is strengthened.

The gate ran once the dispatch bug was fixed (see register §1aq-CORRECTION: the "seat outage" was
my own backgrounding). Verdict: `AGATE_PROGRAM_A_PVALUE_agy.md`.

**C1 — "the cutoff moves the anomaly to AT MOST ~3%" — RETRACTED.** The gate broke it **using my own
table**, which I had printed and not read properly: the smoothed cut at 0.3 k_§ gives
**S₁/₂ = 6,113 against the hard cut's 6,897** — so the hard cut is *not* the strongest suppressor,
and my a-fortiori reasoning ("Reading A suppresses maximally, so Reading B cannot do better") is
false. I had checked the *p-value* column, where the hard cut does lead (3.31% vs 3.12%), and stated
a conclusion about *suppression* that the S₁/₂ column beside it contradicted. **The "at most" is
withdrawn**: with only three smoothing widths tested, nothing establishes an upper bound, and a
different admissible spectrum could plausibly reach a higher p-value.

**C2 — the 6× overshoot — HOLDS, and the gate says it is conservative.** On the ISW sign question I
asked explicitly: late ISW and lensing *add* large-angle power, and since S₁/₂ integrates C(θ)²,
including them **increases** the model's predicted S₁/₂. So omitting them *flatters* the model, and
a correct treatment **widens** the gap between the model's 6,897 and the observed 1,150 rather than
closing it.

**Three further objections, all substantive and none yet answered:**
1. **Cut-sky is not a detail.** The observed 1,150 comes from a masked sky, and the mask suppresses
   exactly the low multipoles that dominate S₁/₂. Full-sky MC against a cut-sky observation is
   apples-to-oranges; the gate expects the correct treatment to move the p-values materially.
2. **ΛCDM transfer functions may smuggle in the answer.** A strict causal boundary should make the
   mode spectrum discrete and alter the transfer functions; keeping infinite-volume late-time
   transfer functions while imposing a primordial horizon cut is internally inconsistent.
3. **The deepest one — the model I built cannot represent the claim I tested it against.** A sharp
   *k*-space cut mathematically *guarantees* C(θ) ≠ 0 above 60° (its ξ has sinc-like infinite
   tails). So "the cut fails to deliver S₁/₂ = 0" is partly an artifact of implementing the causal
   condition in Fourier space. **This is step 2's incompatibility result returning as a
   methodological verdict:** testing the paper's real-space claim requires the real-space (Reading
   B) construction, which is precisely the one this analysis did not build.

**Minimum repairs the gate demands:** build P(k) from a genuine real-space cut ξ(r>χ_§)=0; apply the
actual mask and pseudo-C_ℓ estimator to the MC; add late ISW and lensing to the theory expectation;
and retract C1 (done here).

**Standing status:** C2 is the surviving claim and it is now gated, with the caveat that repair 3
could still change what it means. No tier moves. Still Duho's call.

---

## SECOND GATE: `C2_REFUTED` too. Nothing I constructed in Program (A) survives.

`CGATE_PROGRAM_A_PVALUE_codex.md`, codex, run independently (explicitly barred from reading agy's
verdict). **Both seats now refute; C1 was already retracted, and C2 falls here.**

**The central refutation, which both seats reached independently:** a hard `P(k)=0` cut below `k_§`
is *not* equivalent to `C(θ)=0` above 60°. A spectral step is non-local in real space and produces
ringing and long-range tails, so **the non-zero 6,897 may be guaranteed by my implementation rather
than by the model.** In codex's words, the result establishes "that a hard infrared cutoff does not
reproduce a vanishing angular correlation — **not** that the source paper's correctly formulated
causal-boundary model cannot do so."

**The sentence I should have written**, and codex supplies it exactly: not "the paper's model leaves
6,897" but "**this particular Fourier-cut implementation has full-sky ensemble value 6,897**."

**Codex adds a point neither I nor agy made:** `S₁/₂ = 0` requires `C(θ) = 0` across the whole
60°–180° range — an infinite family of constraints — and tuning one cutoff scale in an otherwise
standard spectrum cannot generally satisfy them. So the target C2 tests against was never reachable
by this kind of model at all.

### The seats disagree on one substantive point, and codex is right

- **agy:** ISW/lensing "**strictly increase** the expected value of S₁/₂", so omitting them flatters
  the model and C2 is *conservative*. I recorded that last section.
- **codex:** since `S₁/₂ = ∫(C_prim + C_ISW)² dμ`, **the cross term can be negative**, so "ISW adds
  correlations" does not mathematically guarantee S₁/₂ rises.

**Codex has the mathematics.** S₁/₂ is a quadratic form `CᵀMC` whose matrix `M` has negative
off-diagonal entries (`∫P_ℓP_ℓ'` over a partial interval is not sign-definite), so raising every
`C_ℓ` need not raise S₁/₂. **My "the gate says C2 is conservative" line from the previous section is
therefore withdrawn** — it rested on agy's claim, and the claim is false as stated. Recorded per the
MUST-STOP rule as a seat disagreement on substance, though it does not change the outcome: **both
seats refute C2 regardless.**

### Where Program (A) actually stands

| finding | status |
|---|---|
| the 60° **scale** prediction is sound and non-circular | **holds** (verified by me from the source) |
| the cutoff **cannot be calibrated**; no initial-conditions model exists, author's own words | **holds** (textual, verified) |
| a gate's "22°, not 60°" charge against the paper | **refuted by me** |
| C1 — "moves the anomaly to at most ~3%" | **retracted** (my own table contradicted it) |
| C2 — "the cut leaves 6× the observed correlation" | **refuted by both seats** |

**Every constructive claim I built in Program (A) has now been refuted.** What survives is two
verification findings, both negative or defensive, and a much clearer statement of what a real
attempt would require: build the causal condition in **real space**, apply the **actual mask and
estimator** to every simulation, separate **primordial/ISW/cross** terms, and **derive** `k_§` and
its convention from the source rather than choosing it.

**No tier moves. Program (A)'s direction remains Duho's call**, now with the honest information that
its constructive output so far is zero.
