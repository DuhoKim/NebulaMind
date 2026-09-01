# GATE — Program (A) step 2: which perturbation condition does the source actually license?

**Do NOT open any large file. Everything you need is quoted inline below.** (A previous round lost
four dispatches to seats that tried to read a huge document whole and died silently.) Answer from
these quotes and your own physics. **Your job is to decide a formalization question, and to refuse
the question if neither option is licensed.**

## Context

Program (A) asks whether the Gaztañaga causal-horizon CMB cutoff can be turned into a calibrated
prediction or proved permanently free. The plan is to optimize the observable `S_1/2` over the whole
class of admissible primordial spectra, which requires writing the model's causal condition as a
mathematical constraint. **That constraint is what you are gating.** If it is wrong, every number
downstream is wrong in the same direction, so this is the load-bearing step.

## What the source says — verbatim, from arXiv 2003.11544 ("The size of our causal Universe")

The causal condition itself, §3.2:

> "We usually assume that particles should be free at infinity, because of lack of causality: if
> there is no cause there should not be any effect. This is why boundary terms are usually set to
> zero at infinity... On scales χ<χ§ we have a homogeneous expanding Universe with ρ̄=ρ. On larger
> scales we require boundary terms to vanish. **In particular we will require Φ(χ>χ§)=0 in Eq.16, so
> that there is no flux (i.e. no effects of gravity) beyond the causal scale. This implies:**"
> [Eq. 17: `Λ/8πG = (1/2M§)∫_{M§} √−g d⁴x (ρ+3p) ≡ (⟨ρ⟩§+3⟨p⟩§)/2`]

with Eq. 16 being **`Φ = −∫_M √−g d⁴x R⁰₀`** — a 4-volume integral of `R⁰₀`, i.e. a **flux**, not a
perturbation field. (An earlier round of this program misread Φ as a Dirichlet condition on the
potential field and manufactured a spurious "unique" prediction from it; that reading is refuted.)

The ONLY statement in the paper about the perturbation spectrum, same section:

> "This could result in a non-homogeneous solution for the metric of the Universe on very large
> scales... An observer situated at the edge of our causal boundary will find a similar solution,
> but could measure different cosmological parameters, because she sees a different patch of the
> initial conditions. **smooth background across disconnected regions with an infrared cutoff in the
> spectrum of inhomogeneities for χ>χ§.** Solutions in different regions **could be matched** as in
> Sanghai & Clifton 2015."

That is the whole perturbation-side content. There is no covariance, no matching law, no
initial-condition model anywhere in the paper.

## The question

"An infrared cutoff in the spectrum of inhomogeneities for χ>χ§" admits at least two readings:

- **READING A (Fourier/mode support):** `P(k) = 0` for `k < k_§ ≈ π/χ_§` — no power in modes longer
  than the causal scale.
- **READING B (real-space/correlation support):** `ξ(r) = 0` for `r > χ_§` — no correlation between
  points separated by more than the causal scale.
- **READING C:** the sentence licenses **neither** as a precise mathematical condition — it is a
  qualitative remark about a consequence, and the only derived condition in the paper is Eq. 17,
  which constrains Λ and says nothing about perturbations at all.

**These are not paraphrases. I computed it: A and B are mutually exclusive.**
- Impose B (a genuine compactly-supported correlation — the spherical-overlap kernel, whose
  transform `(3j₁(x)/x)² ≥ 0`, so it is positive-definite by construction): the resulting `P(k)` on
  `(0, k_§)` is not merely nonzero, it is **largest at the smallest k** — 729× to 1217× its value at
  `3k_§`. A demands exactly this be zero.
- Impose A (hard IR cut, scale-invariant above it): `ξ(r)` does **not** vanish beyond `χ_§`; it
  decays as an oscillatory tail still at the 0.2% level at `8χ_§`.
- This is the Paley–Wiener obstruction: compact support in `r` forces `P` entire in `k`, and a
  non-trivial entire function cannot vanish on an interval.

## What I need from you

1. **Which reading, if any, does the source license?** A, B, or C. Quote the words that decide it.
   Note the tension: "spectrum of inhomogeneities" is Fourier language (favours A), while the
   *physical* argument being made is about causal influence — "if there is no cause there should not
   be any effect" — which is a statement about correlations (favours B). Note also that removing
   modes with `k < k_§` is a statement about **globally extended** Fourier modes, which is arguably
   not a local causality statement at all. Press on that.
2. **Is READING C correct** — i.e. is it illegitimate to extract ANY sharp perturbation constraint
   from this paper? If so, say so plainly. **That is a permitted and possibly correct answer**, and
   it would strengthen rather than weaken the program's negative result: the theory would fail to
   fix even the *support* of the spectrum, let alone its shape.
3. **If A or B: is the admissible class below the right one, and is it non-circular?**
   - (i) the chosen support condition, (ii) `P(k) ≥ 0`, (iii) `P(k) = P_ΛCDM(k)` for `k > k_norm`
     with the low-ℓ data **held out** and never used to fix anything.
   - Is (iii) legitimate, or does normalizing at high ℓ already smuggle in the answer?
   - Is anything ESSENTIAL MISSING from the class — e.g. a Hadamard/UV condition, isotropy of the
     patch, or the observer's position inside the patch (the source says a different observer "sees
     a different patch")? **An admissible class that is too WIDE makes the no-go trivial and
     unpublishable; too NARROW manufactures a fake prediction. Say which error this class makes.**
4. **Does the choice even matter for the answer?** If `S_1/2` minimized under A and under B lands on
   the same side of the observed ~1150 μK⁴, the ambiguity is harmless and can be reported as a
   robustness check rather than resolved. Say whether you expect that, and why.

## Output

Start with ONE token: `READING_A` / `READING_B` / `READING_C` / `CLASS_REFUTED`.
Then: the deciding quotation; your answer to 2, 3 and 4; and any way this formalization could make
the eventual result wrong. Be adversarial — I would rather lose the program now than publish a
number built on the wrong constraint. Review only; change no file except your verdict file.

---

## CORRECTION TO THIS BRIEF, 2026-09-01 — I truncated the key quote, and it mattered

**The textual gate seat caught this brief committing the §1ak defect that §1ak exists to prevent.**
The quotation above beginning "smooth background across disconnected regions…" is **truncated**.
The clean-text render wraps the sentence across two lines: L250 ends **"There should be a"**, and
L251 continues **"smooth background across disconnected regions with an infrared cutoff in the
spectrum of inhomogeneities for χ>χ§."** I grepped L251 alone and lost the existential head — which
is why the excerpt "reads oddly," as this brief itself noticed and then failed to chase.

**Restored, the grammar changes the answer.** The asserted existent is **"a smooth background"**;
the infrared cutoff sits two levels down inside a `with`-adjunct, in **expectational modality
("There should be")**. Compare the register the paper uses for its actual condition three paragraphs
earlier: "we will require… **This implies:**" followed by a numbered equation. The cutoff receives
none of that.

**Two further decisive lines are OUTSIDE this brief's quote set**, so the instruction "everything you
need is quoted inline" was false and an obedient seat could not have reached the right answer:
- **L435:** "there are temperature differences on scales larger θ§, **but they are not correlated**,
  as expected in causality disconnected regions." — this **affirmatively refutes READING A**: under
  `P(k)=0` for `k<k_§` those large-scale temperature differences would not exist at all.
- **L466:** "Continuity across nearby disconnected regions forces these differences to be small,
  **but it is impossible to quantify this without a model for the initial conditions** and a better
  understanding of the process that generates the primordial homogeneity."
  *(Scope note, stated precisely: "this" refers to the inter-patch energy-content differences, not
  literally to S₁/₂. What it establishes is that the author names the missing ingredient — a model
  for the initial conditions — as absent, which is exactly the stochastic completion Program (A)
  set out to supply.)*
- **L558:** the cited supplier "Gaztañaga E., 2019" resolves to **"In preparation"** — an empty
  citation trail; and Sanghai & Clifton 2015 is invoked once as "**could** be matched", with no
  equation adopted and never reused.
- **"infrared" is a hapax** — exactly one occurrence in the paper (verified `grep -c` = 1), never
  restated, and absent from §5 where the author restates every claim he owns.

All of the above verified by me directly against `2003.11544_clean.txt`, not accepted on the seat's
word. **The lesson is the brief's own: an instruction to work only from inline quotes is safe only
if the quote set is complete, and mine was not.**
