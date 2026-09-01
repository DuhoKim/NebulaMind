# Program (A) step 2 — the finding: we were trying to complete a spectrum the paper never asks us to complete

**Status: finding recorded, NOT acted on. No tier changed. The reformulation it implies is a
decision for Duho** (below). Physics gate seat still running at the time of writing; the textual
seat returned `READING_C`, verified by me line-by-line against `2003.11544_clean.txt`.

## What step 2 was for, and what it found instead

Step 2 asked which mathematical condition the paper licenses on the primordial spectrum, so the
optimization could run over an admissible class. The answer is **neither of the candidates, and
arguably none** — but chasing that answer through the source turned up something better: **the
paper's actual falsifiable claim is not about the primordial spectrum at all, and needs no
stochastic completion.**

## The paper's claim, traced to its own words

**The scale prediction is real and non-circular.** Eq. 22 relates the causal scale to Ω_Λ, and the
paper runs it forward using *independently measured* Ω_Λ:

> **L332:** "We find χ§ from Eq.22 numerically **using Ω_Λ = Ω§ ≡ ρ§/ρ_c ≃ 0.69±0.01**"
> **L415:** "Thus, we would expect to see no correlations in the CMB on angular scales
> θ > θ§ ≡ χ§/χ_CMB ≃ **60 degrees**"

Ω_Λ ≈ 0.69 comes from supernovae/BAO/acoustic peaks — not from the large-angle correlation being
tested. **So "60°" is a genuine parameter-free consequence of independently measured input.** The
corpus's "one real a-priori prediction" characterization survives this check.

**But the paper also runs the SAME equation backwards and calls that a second prediction:**

> **L429:** "We can also **predict Ω_Λ from the lack of CMB correlations**. From Fig.3 we roughly
> estimate θ§ ≃ 60±3 deg. to find (using Eq.22) **Ω_Λ = 0.7±0.1**."

That is Eq. 22 inverted — one relation presented twice. Not circular in the forward direction, but
the reverse direction is **not independent evidence** and should not be counted as a second success.

**And here is the claim that matters — an OBSERVABLE one, with no free amplitude:**

> **L457:** "It also predicts that **CMB temperature should not be correlated above θ > θ§ ≃ 60 deg.**
> A prediction that matches observations"

With the author's own caveat attached:

> **L431–432:** "this rough estimate does not take into account the foreground (late) ISW and lensing
> effects…, **which add non primordial correlations to the largest scales. This requires further
> investigation.**"

## Why this changes Program (A)

`S₁/₂ ≡ ∫_{−1}^{1/2} C(θ)² d(cos θ)` integrates over **exactly** `θ ∈ (60°, 180°)`. So the paper's
claim "no correlation above 60°" is not a claim about an amplitude to be calibrated — **it is the
statement `S₁/₂ = 0`.** It is parameter-free. It needs no stochastic completion, no initial-condition
model, no state-selection principle. **The entire obstruction that killed the previous three
attempts — and that step 2 just confirmed is unfixable — is irrelevant to it.**

Measured: `S₁/₂ ≈ 1,150 μK⁴`. ΛCDM: `≈ 34,900 μK⁴` (this lane's own validated pipeline: 34,926).
The observed value is ~30× below ΛCDM but **is not zero**, and the author has already named what
must account for the difference: late ISW and lensing, "which add non primordial correlations."

**That makes the test concrete and decidable:**

> Can late ISW + lensing alone produce `S₁/₂ ≈ 1,150 μK⁴` on a sky whose primordial correlation
> vanishes above 60°?
> - **Yes** → the paper's observable prediction survives a real quantitative test it has never faced.
> - **No** (ISW+lensing give ≪ 1,150) → residual primordial correlation exists above 60°, and the
>   model's own stated prediction **fails** — a falsification of a published claim, from public data.

Either branch is a result, and unlike the optimization it rests on a claim the paper **actually
makes** rather than one we had to construct for it. It is also the "further investigation" the
author explicitly says is required and never performs.

## What this does NOT establish

- It does **not** revive calibration of the amplitude. `READING_C` stands: there is no
  initial-conditions model in the paper, and the author says so himself (L466).
- It does **not** move any tier. Entries 23–27 stay QUALITATIVE-DIRECTIONAL. If the ISW+lensing test
  fails, that bears on their tier — **and that decision is Duho's, not mine.**
- It is **not yet computed.** Separating the late-ISW contribution to large-angle `C(θ)` is real
  work and can go wrong; nothing here should be quoted as a result.

## The decision for Duho

Program (A) was chartered as "calibrate or kill the cutoff" via an optimization over admissible
completions. Step 2 established the optimization has **no licensed class to run over**. Options:

- **(1) Re-aim (A) at the observable claim** — test whether ISW+lensing can account for the observed
  `S₁/₂` given the paper's "no correlation above 60°". *Cost:* it is a different question from the
  one chartered, and the ISW/lensing separation is the hard part, with a real chance the answer is
  "consistent, within cosmic variance" — a weak result. *Gain:* it tests a claim the paper actually
  makes, needs no completion, uses public data only, and both outcomes are publishable.
- **(2) Write (A) up as the documented no-go it already is** — the theory contains no
  initial-conditions model (author's own words), so no calibration is possible, with the
  Paley–Wiener incompatibility and the textual analysis as the supporting record. *Cost:* it is a
  negative result about a small literature, and largely restates what three prior attempts found.
  *Gain:* it is finished, honest, and cheap.
- **(3) Stop (A).** *Cost:* the machinery built (validated `S₁/₂` operator, incompatibility proof)
  goes unused. *Gain:* nothing further is spent on a corpus whose central prediction is
  scale-only.

**My recommendation: (1).** It is the only option that produces a new number rather than a better
argument, and the author himself flagged it as the missing investigation. But it changes the
program's question, which is why it is yours to rule on rather than mine.
