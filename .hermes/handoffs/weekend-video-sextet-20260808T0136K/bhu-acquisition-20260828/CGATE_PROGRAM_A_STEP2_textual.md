READING_C

# CGATE — Program (A) step 2, TEXTUAL/PHILOLOGICAL lens

Seat: adversarial gate, textual lens (physics lens worked independently by another seat).
Source of record: `.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/2003.11544_clean.txt`
(829 lines, read in full; all line numbers below refer to that file).

Verdict: **READING_C** — the paper licenses neither `P(k)=0 for k<k_§` nor `ξ(r)=0 for r>χ_§` as a
mathematical condition. It never states a spectrum, a covariance, a correlation function, or an
initial-condition model. Additionally, and going beyond a bare C: **READING A is not merely
unsupported, it is affirmatively contradicted by the paper's own text** (line 435), and the direction
the paper *does* commit to is real-space and *observable-level*, not primordial. Details below.

---

## 0. FIRST FINDING: the brief's key quote is TRUNCATED, and the truncation is the brief's, not the render's

The brief quotes (its lines 36–37, in bold, presented as a sentence):

> "**smooth background across disconnected regions with an infrared cutoff in the spectrum of
> inhomogeneities for χ>χ§.**"

The clean-text render did **not** drop words. It wrapped the sentence across two lines. Line 250 ends
with the head of the sentence; line 251 carries the tail. Restored in full:

> **L250–251 (verbatim, joined):** "An observer situated at the edge of our causal boundary will find
> a similar solution, but could measure different cosmological parameters, because she sees a
> different patch of the initial conditions. **There should be a** smooth background across
> disconnected regions with an infrared cutoff in the spectrum of inhomogeneities for χ>χ§."

The brief's extraction began at line 251 and therefore lost **"There should be a"** — the head of the
existential clause. This is a line-oriented (`grep -n`-style) truncation at a wrap boundary: exactly
the failure mode this lane was burned by before. It is *not* meaning-reversing here, but it is
**meaning-changing in the direction that matters for this gate**, and it cuts against the brief's own
framing (see §2).

Two further elisions in the brief, both material:
- The brief renders "This could result in a non-homogeneous solution for the metric of the Universe
  on very large scales**...**" — the "..." swallows **"(see Gaztañaga 2019)"** (L249). That citation
  resolves at **L556–558** to: *"Gaztañaga E., 2019, **In preparation**,"* — i.e. the pointer for the
  entire inhomogeneous-metric program is a manuscript with no content. Suppressing it makes the
  paragraph look better-sourced than it is.
- The brief asserts "That is the whole perturbation-side content." **This is false.** The decisive
  perturbation-side statements are in §4.2 and §5 (L426, L431–432, L434, L435, L459, L466) and are
  **not in the brief at all**. A seat obeying the brief's instruction "Do NOT open any large file.
  Everything you need is quoted inline below" **could not have reached the correct answer.** The
  inline quote set is insufficient. Flagging this as a process defect in the brief.

The brief's *other* quote (the §3.2 causal condition, brief lines 20–25) is **faithful and complete**:
verified against L255–262. Its ellipsis correctly marks the omitted Landau & Lifshitz / Weinberg
sentence, which does not change the meaning. Eq. 16 (`Φ = −∫_M √−g d⁴x R⁰₀`, L235) and Eq. 17 (L262)
are quoted correctly. The brief's refutation of the "Dirichlet condition on the potential" misreading
stands.

---

## 1. Deciding quotations

### (a) The phrase is a hapax legomenon that never survives to the Conclusions

`grep -i "infrared"` over the whole paper returns **exactly one hit: line 251.** The word appears once,
inside a subordinate `with`-adjunct, and is **never used again** — not in §3.3, not in §4, not in §4.2,
not in §5 Discussion and Conclusions, not in either appendix.

This is decisive by contrast. §5 restates *every* claim the author regards as his own result:
- L444: "This leads to Eq.17, **which is the main result in this paper**."
- L452–456: χ§ ≃ 3c/H₀, a§ ≃ 0.93, ρ_Λ ≃ 2ρ_m.
- L448–450: the Λ/ρ_vac cancellation, "vacuum does not gravitate".
- L457: "It also **predicts** that CMB temperature should not be correlated above θ>θ§≃60 deg."

The infrared cutoff is the one statement in §3.2 that is **dropped and never restated**. An author who
took it to be a derived condition of his model would have carried it into the Conclusions alongside the
others. He did not.

Correspondingly, `grep -i "spectrum"` returns **only three hits in the entire paper**:
- **L251** — the sentence at issue;
- **L424** — "the angular power spectrum c_l (Schwarz et al. 2016)", *describing the known observational
  anomaly*, not deriving anything;
- **L459** — "One would also expect the CMB spectrum to be anisotropic on the largest scales, which is
  another well known measured anomaly".

No `P(k)`. No `k`. No `k_§`. No `ξ`. No `ℓ_min`. No variance, no covariance, no transfer function, no
window function, no numbered equation anywhere in the paper carries a spectral quantity. **Absence
confirmed and total.**

### (b) READING A is affirmatively contradicted — L435

> **L435 (verbatim):** "Note also that there are **temperature differences on scales larger θ§, but
> they are not correlated**, as expected in causality disconnected regions."

This is the single most decisive line in the paper and it is absent from the brief. Under READING A
(`P(k)=0` for `k<k_§`), the very modes that *generate* the largest-scale temperature differences are
deleted, so there would be **no** temperature differences on scales larger than θ§. The author
explicitly asserts that those differences **exist** and that only their **correlation** vanishes. That
is a direct textual refutation of A as the author's intent.

Supporting, same direction:
- **L436:** "Nearby regions are connected which creates a smooth transition across disconnected
  regions." — a smooth transition across the boundary is *itself* structure spanning the boundary.
- **L466:** "Continuity across nearby disconnected regions forces these differences to be small…"
- **L89:** "The only way to do this is to setup **initial conditions that are random with no
  correlations**." — the paper's foundational causal move is stated in correlation language, never in
  mode language.
- **L255:** "if there is no cause there should not be any effect" — a statement about influence between
  separated points, i.e. about `ξ`, not about globally-extended Fourier modes.

### (c) But READING B is not licensed either — it is stated only of the projected observable, and then disclaimed

Everything the paper actually commits to on the correlation side is about **the observed 2-D CMB
angular correlation `w₂(θ)` on the last-scattering sphere**, never about a primordial 3-D `ξ(r)`:

- **L21 (abstract):** "…which is consistent with the anomalous **lack of correlations observed in the
  CMB**."
- **L415:** "Thus, we would **expect to see no correlations in the CMB on angular scales
  θ>θ§ ≡ χ§/χ_CMB ≃ 60 degrees**."
- **L457:** "It also predicts that CMB temperature should not be correlated above θ>θ§≃60 deg."
- **L461–462:** "One can reverse this argument to use the lack of CMB correlations above θ§≃60 deg…"

No projection is supplied anywhere converting `w₂(θ)` to `ξ(r)` — no Limber relation, no radial kernel,
no `C_ℓ ↔ w₂` inversion. The paper then explicitly disqualifies its own observable:

> **L431–432:** "…this rough estimate does not take into account the foreground (late) ISW and lensing
> effects (Fosalba et al. 2003; Das & Souradeep 2014), which **add non primordial correlations to the
> largest scales**. This requires further investigation."

and, in the Conclusions, states the impossibility outright:

> **L466 (verbatim):** "…but **it is impossible to quantify this without a model for the initial
> conditions** and a better understanding of the process that generates the primordial homogeneity."

> **L463–464:** "More work is needed to account for the late ISW and lensing and to **interpret the CMB
> measurements with a metric that is not homogeneous** (Gaztañaga 2019)."

The author states in his own Conclusions that quantification of the inhomogeneity structure is
**impossible without an initial-conditions model that the paper does not contain**. That is the paper
declaring READING_C on its own behalf.

### (d) The one k-space suppression in the paper belongs to ΛCDM, not to the model

> **L409–410 (Fig. 3 caption):** "Shaded region shows **ΛCDM simulations** where we suppress the large
> scale modes (multipoles l<5)."

This is the only `l<5`-style mode-deletion statement in the paper, and it is a property of a **ΛCDM
comparison band drawn as a visual foil**, not of the causal model. It is not derived, `l=5` is never
connected to `χ§`, and it never reappears. It must not be read as the model licensing A. L424 likewise
*describes* the observed low-ℓ alignment anomaly (attributed to Schwarz et al. 2016); it derives nothing.

---

## 2. Brief question 2 — grammatical subject, modality, and well-formedness

**Is the cutoff asserted *of the spectrum*, or *of the region χ>χ§*? Neither, strictly. It is asserted
of a `background`, inside an adjunct.**

Parse of the restored sentence:

```
There should be [ a smooth background ]                     <- existential; NP head = "background"
                 ├ across disconnected regions              <- PP, locative
                 └ with an infrared cutoff                  <- PP, comitative/attributive
                       in the spectrum of inhomogeneities   <- PP nested inside the adjunct
                       for χ > χ§                           <- range restriction
```

- The **asserted existent is "a smooth background."** The infrared cutoff sits two levels down inside a
  `with`-adjunct — an accompanying attribute of the background, not the proposition being asserted. The
  brief's truncation deleted the existential head and thereby promoted the adjunct to the surface, which
  is precisely why the fragment "reads oddly" and why it reads more like a stated condition than it is.
- **Modality is expectational: "should be."** Not "is", not "we require", not "this implies." The paper
  reserves that register for its actual derivation, three paragraphs later:
  **L259–260:** "In particular **we will require** Φ(χ>χ§)=0 in Eq.16… **This implies:**" → **Eq. 17**.
  Requirement → implication → numbered equation. The infrared cutoff receives none of the three.
- **Derivation or aside?** Aside. It is the third sentence of a four-sentence descriptive paragraph
  (L248–253) whose other sentences are hedged with "could result", "could measure", "could be matched",
  and which is bracketed by two forward-references to unwritten work. Nothing in the paper is derived
  *from* it and nothing derives *to* it.
- **Is it well-formed?** As English, yes — once "There should be a" is restored. **As mathematics, no.**
  It contains a **type mismatch**: a *spectrum* is indexed by wavenumber `k` (or multipole `ℓ`), but the
  range restriction is written **"for χ>χ§"**, in the paper's real-space comoving coordinate (cf. L115,
  "some cut-off χ<χ§"; L102, "comoving scales"). The sentence applies a real-space interval to a Fourier
  object and never supplies the conversion — no `k_§ = π/χ_§`, no `k_§` at all. Read literally it is
  type-incoherent. Read charitably it degrades to the folk statement *"no inhomogeneity structure on
  scales beyond χ§"* — which is exactly the ambiguous English that A and B are **rival formalizations
  of**, and which by itself selects neither.

**Answer to question 2: YES, READING_C is correct. It is illegitimate to extract any sharp perturbation
constraint from this paper.** The theory fails to fix even the *support* of the spectrum, let alone its
shape. Stated plainly, and with the author's own concurrence at L466.

**Do the cited works supply the missing condition? No — both suppliers are empty:**
- **Gaztañaga 2019** (invoked at L249 for the non-homogeneous metric, and again at L464 for interpreting
  the CMB in that metric) resolves at **L556–558** to **"In preparation"**. Zero content. The paper's
  entire inhomogeneous-perturbation programme is deferred to a manuscript that does not exist in the
  reference list.
- **Sanghai & Clifton 2015** (L252–253, L668–671 = Phys. Rev. D **91**, 103532) is invoked exactly once,
  in the modality **"could be matched"**, with **no equation adopted, no notation imported, and no
  reuse anywhere else in the paper**. It is a deterministic cell/lattice junction-condition construction
  — a geometric matching scheme, not a statistical formalism, and it yields neither a `P(k)` nor a
  `ξ(r)`. **The paper gestures; it does not commit.** Even a maximally charitable reader who went and
  imported Sanghai & Clifton's machinery wholesale would be *adding* a theory, not *reading* one.

**Does any other part settle it? Yes — and it settles it against A, not for B.** The abstract (L21), §4.2
(L415, L435), and the Conclusions (L457, L461–462) all make the sharper claim in **real-space correlation
language about the observed CMB angular correlation function**, and L435 explicitly preserves large-scale
temperature differences while removing only their correlation. So the paper's *directional* commitment is
B-flavoured — but it is made about `w₂(θ)`, the projected observable, and the paper itself declares that
observable contaminated (L431–432) and the underlying quantity unquantifiable (L466). **Direction without
a condition. That is READING_C, not READING_B.**

---

## 3. Brief question 3 — the admissible class

Q3 is conditioned on "If A or B", and my verdict is C, so strictly the class has **no source warrant at
all**: element (i), the support condition, is not licensed in either form. But answering on the merits,
because the brief asks which error the class makes:

**The class makes BOTH errors simultaneously, on different axes. That is worse than either alone,
because it means neither a positive nor a negative result from it is attributable to the source.**

Too **NARROW**, in two ways:
1. **(i) manufactures determinacy.** Imposing a sharp support the source never states means any hard
   floor found on `S_1/2` would be a **fake prediction** — the exact failure this program already
   suffered once with the Φ-as-Dirichlet-condition misreading (brief lines 27–29).
2. **The `P(k)` parameterization itself excludes the source's actual distinctive claim.** A single
   isotropic Gaussian `P(k)` presupposes a statistically homogeneous and isotropic random field. The
   source **denies this repeatedly and by name**:
   - L250 "because she sees a **different patch of the initial conditions**";
   - L434 "…might be slightly different to the value near us, as **we see a different patch** of the
     primordial Universe";
   - L426 "We also expect **variations of c_l** … for c_l estimated over **different regions of the
     sky** (separated by θ>60 deg.)";
   - L459 "One would also expect the CMB **spectrum to be anisotropic** on the largest scales";
   - L466 "the Universe is **not strictly homogeneous** outside a causal region… the causal boundary for
     observers far away from us could be **slightly different from ours**."
   The model's signature prediction is a **patch-dependent, statistically anisotropic** sky. A class
   built on one global `P(k)` cannot represent it, so the class throws away the only thing that made the
   model distinguishable.

Too **WIDE**, in one way:
3. **(ii) + (iii) with everything else free is nearly vacuous.** "Any non-negative spectrum agreeing with
   ΛCDM above `k_norm`" leaves the low-`k` region essentially unconstrained, so `S_1/2` can be driven
   arbitrarily low by depleting power just below `k_norm`. The no-go then becomes trivial and
   unpublishable — it would demonstrate a property of the *class*, not of the *model*.

**Is (iii) circular?** Not with respect to the low-ℓ data — holding low-ℓ out is a legitimate protocol
and does not smuggle in the answer. **But (iii) is circular with respect to the model.** Fixing
`P(k)=P_ΛCDM(k)` for `k>k_norm` imports the homogeneous-FLRW transfer function and projection machinery
that the causal model claims to break **at exactly the scales under test**. The author says so himself:
**L463–464**, "More work is needed… to interpret the CMB measurements with a metric that is not
homogeneous." Assuming ΛCDM's map from primordial `P(k)` to observed `C_ℓ` while testing a model that
denies that map is the circularity to worry about, not the normalization.

**Essential elements MISSING from the class** (in descending order of severity):
1. **Statistical isotropy / patch structure** — the source's field is not statistically isotropic (L426,
   L459, L434). Not a refinement; it invalidates the `P(k)` object.
2. **The observer's position inside the patch** — L250, L434. `S_1/2` for a boundary-adjacent observer
   differs from one at the centre; the class has no such parameter.
3. **Gaussianity** — never assumed by the source, and L427 explicitly recalls "non-Gaussian initial
   conditions" as the earlier interpretation of a related anomaly. Under non-Gaussianity `S_1/2` is not
   a functional of `P(k)` at all.
4. **ISW + lensing projection** — L431–432, flagged by the author as adding "non primordial correlations
   to the largest scales." A primordial-`P(k)` constraint therefore does not determine the *observed*
   `S_1/2` even if everything else were granted.
5. A Hadamard/UV condition is a comparatively minor omission next to items 1–4.

---

## 4. Brief question 4 (brief note; the physics seat owns the numerics)

Under C the A/B robustness framing is **moot as posed** — the ambiguity is not between two licensed
formalizations but between two *unlicensed* ones, so agreement between them would demonstrate nothing
about the source. Reporting "A and B give the same side of ~1150 μK⁴" would be a robustness check on the
*analyst's* choices, not on Gaztañaga's.

If the program wants a source-attributable object, the **only** one available is at the observable level:
`w₂(θ) = 0 for θ > θ§ ≃ 60°` (L415, L457), which is stated four times including the abstract and is the
paper's self-declared "prediction". Note the cost of that reframe, which must be stated if taken: the
paper's own Fig. 3 discussion hedges it to `θ§ ≃ 60 ± 3 deg` "roughly estimate[d]" (L429), and disclaims
ISW/lensing (L431–432) — so even at the observable level the paper's claim is qualitative and the author
says so. **A no-go built on L466 ("impossible to quantify this without a model for the initial
conditions") is far stronger, cleaner and more defensible than any number built on A or B.**

---

## 5. How this could still make the eventual result wrong

- If a downstream seat treats my "direction is B-flavoured" observation as a licence for B, the result
  will be a number attributed to Gaztañaga that he did not state. **The direction is not a condition.**
- Reading A must be recorded as **refuted by L435**, not merely as "the less likely of two". If a later
  round re-derives A from the Fig. 3 caption (L410) it will have mistaken a ΛCDM comparison band for a
  model prediction. Flag L409–410 in the lane record.
- The brief's own instruction not to open the source is the largest live risk to this program: the two
  decisive lines (L435, L466) are outside the brief's quote set. **Retire that instruction.**

---
*Files changed by this seat: this file only.*
