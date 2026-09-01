Query: CRITICAL: you have NO file access and NO search tools. Do NOT attempt to 
search or open any file -- every quote you need is inline below. Answer directly
in prose from the brief alone. Begin your answer with ONE token: READING_A, 
READING_B, READING_C, or CLASS_REFUTED.

# GATE — Program (A) step 2: which perturbation condition does the source 
actually license?

**Do NOT open any large file. Everything you need is quoted inline below.** (A 
previous round lost
four dispatches to seats that tried to read a huge document whole and died 
silently.) Answer from
these quotes and your own physics. **Your job is to decide a formalization 
question, and to refuse
the question if neither option is licensed.**

## Context

Program (A) asks whether the Gaztañaga causal-horizon CMB cutoff can be turned 
into a calibrated
prediction or proved permanently free. The plan is to optimize the observable 
`S_1/2` over the whole
class of admissible primordial spectra, which requires writing the model's 
causal condition as a
mathematical constraint. **That constraint is what you are gating.** If it is 
wrong, every number
downstream is wrong in the same direction, so this is the load-bearing step.

## What the source says — verbatim, from arXiv 2003.11544 ("The size of our 
causal Universe")

The causal condition itself, §3.2:

> "We usually assume that particles should be free at infinity, because of lack 
of causality: if
> there is no cause there should not be any effect. This is why boundary terms 
are usually set to
> zero at infinity... On scales χ<χ§ we have a homogeneous expanding Universe 
with ρ̄=ρ. On larger
> scales we require boundary terms to vanish. **In particular we will require 
Φ(χ>χ§)=0 in Eq.16, so
> that there is no flux (i.e. no effects of gravity) beyond the causal scale. 
This implies:**"
> [Eq. 17: `Λ/8πG = (1/2M§)∫_{M§} √−g d⁴x (ρ+3p) ≡ (⟨ρ⟩§+3⟨p⟩§)/2`]

with Eq. 16 being **`Φ = −∫_M √−g d⁴x R⁰₀`** — a 4-volume integral of `R⁰₀`, 
i.e. a **flux**, not a
perturbation field. (An earlier round of this program misread Φ as a Dirichlet 
condition on the
potential field and manufactured a spurious "unique" prediction from it; that 
reading is refuted.)

The ONLY statement in the paper about the perturbation spectrum, same section:

> "This could result in a non-homogeneous solution for the metric of the 
Universe on very large
> scales... An observer situated at the edge of our causal boundary will find a 
similar solution,
> but could measure different cosmological parameters, because she sees a 
different patch of the
> initial conditions. **smooth background across disconnected regions with an 
infrared cutoff in the
> spectrum of inhomogeneities for χ>χ§.** Solutions in different regions **could
be matched** as in
> Sanghai & Clifton 2015."

That is the whole perturbation-side content. There is no covariance, no matching
law, no
initial-condition model anywhere in the paper.

## The question

"An infrared cutoff in the spectrum of inhomogeneities for χ>χ§" admits at least
two readings:

- **READING A (Fourier/mode support):** `P(k) = 0` for `k < k_§ ≈ π/χ_§` — no 
power in modes longer
  than the causal scale.
- **READING B (real-space/correlation support):** `ξ(r) = 0` for `r > χ_§` — no 
correlation between
  points separated by more than the causal scale.
- **READING C:** the sentence licenses **neither** as a precise mathematical 
condition — it is a
  qualitative remark about a consequence, and the only derived condition in the 
paper is Eq. 17,
  which constrains Λ and says nothing about perturbations at all.

**These are not paraphrases. I computed it: A and B are mutually exclusive.**
- Impose B (a genuine compactly-supported correlation — the spherical-overlap 
kernel, whose
  transform `(3j₁(x)/x)² ≥ 0`, so it is positive-definite by construction): the 
resulting `P(k)` on
  `(0, k_§)` is not merely nonzero, it is **largest at the smallest k** — 729× 
to 1217× its value at
  `3k_§`. A demands exactly this be zero.
- Impose A (hard IR cut, scale-invariant above it): `ξ(r)` does **not** vanish 
beyond `χ_§`; it
  decays as an oscillatory tail still at the 0.2% level at `8χ_§`.
- This is the Paley–Wiener obstruction: compact support in `r` forces `P` entire
in `k`, and a
  non-trivial entire function cannot vanish on an interval.

## What I need from you

1. **Which reading, if any, does the source license?** A, B, or C. Quote the 
words that decide it.
   Note the tension: "spectrum of inhomogeneities" is Fourier language (favours 
A), while the
   *physical* argument being made is about causal influence — "if there is no 
cause there should not
   be any effect" — which is a statement about correlations (favours B). Note 
also that removing
   modes with `k < k_§` is a statement about **globally extended** Fourier 
modes, which is arguably
   not a local causality statement at all. Press on that.
2. **Is READING C correct** — i.e. is it illegitimate to extract ANY sharp 
perturbation constraint
   from this paper? If so, say so plainly. **That is a permitted and possibly 
correct answer**, and
   it would strengthen rather than weaken the program's negative result: the 
theory would fail to
   fix even the *support* of the spectrum, let alone its shape.
3. **If A or B: is the admissible class below the right one, and is it 
non-circular?**
   - (i) the chosen support condition, (ii) `P(k) ≥ 0`, (iii) `P(k) = P_ΛCDM(k)`
for `k > k_norm`
     with the low-ℓ data **held out** and never used to fix anything.
   - Is (iii) legitimate, or does normalizing at high ℓ already smuggle in the 
answer?
   - Is anything ESSENTIAL MISSING from the class — e.g. a Hadamard/UV 
condition, isotropy of the
     patch, or the observer's position inside the patch (the source says a 
different observer "sees
     a different patch")? **An admissible class that is too WIDE makes the no-go
trivial and
     unpublishable; too NARROW manufactures a fake prediction. Say which error 
this class makes.**
4. **Does the choice even matter for the answer?** If `S_1/2` minimized under A 
and under B lands on
   the same side of the observed ~1150 μK⁴, the ambiguity is harmless and can be
reported as a
   robustness check rather than resolved. Say whether you expect that, and why.

## Output

Start with ONE token: `READING_A` / `READING_B` / `READING_C` / `CLASS_REFUTED`.
Then: the deciding quotation; your answer to 2, 3 and 4; and any way this 
formalization could make
the eventual result wrong. Be adversarial — I would rather lose the program now 
than publish a
number built on the wrong constraint. Review only; change no file except your 
verdict file.
Initializing agent...
────────────────────────────────────────


╭─ ⚕ Hermes ───────────────────────────────────────────────────────────────────╮
READING_C

Deciding quotation — the modal asymmetry inside §3.2 itself. When the paper means a constraint it knows how to say so: "In particular we will require Φ(χ>χ§)=0 in Eq.16" — that is the one and only imposed condition, and it lands on the background flux. The perturbation content arrives in a different mood entirely: "This could result in a non-homogeneous solution...", "she ... could measure different cosmological parameters", "Solutions in different regions could be matched". Three "could"s, no "require". And the load-bearing phrase itself — "smooth background across disconnected regions with an infrared cutoff in the spectrum of inhomogeneities for χ>χ§" — is not even a sentence; it is a verbless fragment in a list of possible features of a hypothetical non-homogeneous solution. The only derived equation in the paper, Eq. 17, fixes Λ from ⟨ρ+3p⟩ inside the causal volume and says nothing about perturbations at all. C is exactly right: the paper licenses neither A nor B as a precise condition.

1. Why neither reading is licensed, pressed on the merits. A hooks on the word "spectrum"; B hooks on the real-space variable in "for χ>χ§" and on the paper's own causal principle, "if there is no cause there should not be any effect". The fragment uses both vocabularies in one breath, which is only possible because it is not making a precise claim. On the Fourier side: a hard cut P(k)=0 for k<k_§ is an operation on the ensemble's globally extended plane waves. No local observer ever measures a Fourier mode; deleting modes of wavelength ≫ χ§ is not a local causality statement, it is a statement about the global realization of the field — and the paper's justifying argument is explicitly local-causal. The standard causality results in the literature (causal seed mechanisms, defect spectra) are B-type: compactly supported correlation, analytic P(k). So the physical argument points to B while the vocabulary points to A, and the text resolves the tie nowhere. It also never says ξ or P of which field (δ? Φ? at which epoch?), never gives the k_§↔χ_§ conversion, never states isotropy or the observer's position. The only intent recoverable from the fragment is qualitative smoothness — the Universe should look homogeneous beyond χ§ so that disconnected patches share a background. A and B would each achieve that approximately, and they disagree on the flagship observable's sign (item 4). A sentence whose two defensible formalizations predict opposite outcomes does not constrain anything.

2. Yes — say it plainly: it is illegitimate to extract ANY sharp perturbation constraint from this paper. That is stronger than "proved permanently free": the theory fixes neither the support nor the shape of the spectrum, so S_1/2 is not a calculable number from the source. There is nothing to optimize over until a non-source assumption is added, and any added assumption must be labelled as the formalizer's, with its sensitivity reported. The honest headline result is underdetermination, exhibited constructively (A vs B straddling the data). That is a publishable no-go; a number read off reading A is not.

3. The admissible class.
   (ii) P≥0 is minimal and unobjectionable.
   (iii) High-ℓ matching to ΛCDM with low-ℓ held out is legitimate in intent — it encodes "new physics lives in the IR", which is the premise of any cutoff model — and it is non-circular only if two things are enforced. First, the ℓ–k transfer kernel is non-local (finite last-scattering shell, plus late-time ISW leaking small-scale power into low ℓ): k_norm must sit well above k_§ with margin for the kernel width, or sub-cutoff modes contaminate the normalization region and the fit silently trades them off — that is the smuggling channel. Second, k_§ ≈ π/χ_§ is a convention (1/χ§, π/χ§, 2π/χ§ are all defensible); it moves S_1/2 at O(1) and must be scanned and reported, not fixed. Fixing it silently is a hidden free parameter that can manufacture agreement or disagreement at will.
   Which error the class makes: it is narrow in the load-bearing place and wide in the cosmetic ones — the worst combination. Narrow: it imposes a hard support condition as if derived (it is not); it assumes statistical isotropy and a typical/central observer, while the source explicitly says an edge observer "sees a different patch" — a real-space patch cutoff seen off-center is anisotropic on the sky, and the isotropic P(k) class has quietly chosen the observer's position; it demands exact P_ΛCDM above k_norm with a join whose continuity/smoothness is fixed by nothing and which, under A, can dominate the low-ℓ answer. Wide: nothing requires the perturbed solution to still satisfy the one condition the paper does derive — Φ(χ>χ§)=0 on the full 4-volume flux of R⁰₀, which is sensitive to metric perturbations through √−g and the curvature component. Whether A- or B-type spectra are even compatible with the flux condition is unchecked; as stated, the class can "minimize" over spectra that fail the actual causal condition. Also missing: any matching-law requirement (the paper names Sanghai & Clifton only as a "could"), and any restriction on the mid-band (k_§, k_norm), where arbitrary narrow spikes are admissible and move low ℓ through kernel leakage. Missing essentials in order of danger: (1) consistency with Φ=0/Eq. 17 on the perturbed metric — the sole source-derived constraint, currently absent from the class; (2) observer-position/isotropy treatment; (3) the k_§↔χ_§ convention; (4) join regularity. A Hadamard/UV condition is not needed — (iii) already pins the UV; the live ambiguity is IR/mid-band.

4. Does the choice matter? Yes — decisively, and this is the strongest internal argument for C. Expect the two minima on opposite sides of ~1150 μK⁴. Under A, minimizing S_1/2 suppresses low-ℓ power toward and plausibly below the observed value, with a floor set by kernel leakage and late ISW. Under B, the brief's own computation shows the positive-definite compactly-supported ξ forces P(k) nonzero and rising toward small k — (3j₁(x)/x)²→1 as k→0, white-noise-like low-k power — so after high-k normalization, low-ℓ S_1/2 sits at or above the ΛCDM-like level, on the far side of 1150. The minima straddle the data. So this cannot be reported as a robustness check: the theory's only perturbation sentence, read two defensible ways, either produces the quadrupole suppression or forbids it. That straddle IS the result — a no-prediction theorem — provided the program does not pick A for tractability and call the output a prediction.

Ways this formalization could make the eventual result wrong:
- Reporting a number from A alone: the number is a property of the Fourier reading, not of the theory; a referee holding the paper's causality language (B) reverses the conclusion.
- Unreported k_§=π/χ_§ convention: O(1) movement of the "prediction" at the formalizer's discretion.
- Kernel leakage across k_norm: held-out low-ℓ data silently constraining the fit unless the held-out ℓ-range covers the kernel image of everything below k_norm.
- Off-center observer ignored: anisotropic sky makes isotropic S_1/2 the wrong statistic under B; B without position modelling is not even the theory's own B.
- Φ(χ>χ§)=0 never imposed on the perturbed solution: the only derived constraint unused, so every optimized number may be a minimum over inadmissible spectra.
- "Could be matched (Sanghai & Clifton)" treated as established: the matching law is unconstrained and changes the effective spectrum.

Bottom line: verdict READING_C. Report underdetermination as the finding, with A and B exhibited as the two formally incompatible refinements whose minima straddle the observed ~1150 μK⁴. Do not emit a number from either reading alone; do not let the tractability of A masquerade as a prediction of the paper.
╰──────────────────────────────────────────────────────────────────────────────╯

Resume this session with:
  hermes --resume 20260901_215138_d98970
  hermes -c "Decide licensed perturbation condition"

Session:        20260901_215138_d98970
Title:          Decide licensed perturbation condition
Duration:       4m 19s
Messages:       2 (1 user, 0 tool calls)
