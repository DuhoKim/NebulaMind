AUDIT_HOLDS_CONSISTENCY_ONLY

# Entry-13 deep audit — claude-seat, independent (2026-09-02 21:05 KST)

**Entry:** Frolov, Markov & Mukhanov (1989), "Through a black hole into a new universe?", Phys. Lett. B 216, 272–276.
**Source read:** `../bhu-reading-20260823/sources/frolov_markov_mukhanov_1989_plb216_272_clean.txt` (709 lines), ONLY.
**Decode:** 8→B, 0→O, 1→I/l, 5→S, 7→T, 6→G. Note the scan also renders proper time **τ as "r"**, so "Ar/r = r~ - r0"
at L219 is Δτ = τ₁ − τ₀; I flag each place this matters. Σ is rendered variously as `2`, `E`, `Y`, `~`.
Blind: no ENTRY13_*RESULT*, no SWEEP5_*, no codex/kimi file opened. No file changed but this one.

---

## 1. The construction — what is matched to what, computed vs. hypothesised

**Two hypotheses, both stated as hypotheses, neither derived.**

- H1 (limiting curvature), L37–42: *"It is natural to assume that the curvature for the solutions of these modified
  equations is limited by some universal value ~ l⁻², where l plays the role of fundamental length. In what follows we
  suppose that l ~ l_Pl = (ħG/c³)^{1/2} ~ 10⁻³³ cm."* Formalised at L135–139 as eq. (5), *"ℬ² = R_{μν;λ}R^{μν;λ} ≲ α/l⁴,
  where l is the characteristic (planckian) length and α is a dimensionless parameter of order one."*
- The authors label it a hypothesis and say it is unverifiable now, L44–47: *"Unfortunately we do not know the exact
  modified equations yet and therefore cannot verify this assumption. But we can accept this assumption as a hypothesis
  and investigate its possible consequences."*
- H2 (vacuum-like equation of state at maximal curvature), L147–150: *"As a second hypothesis we assume that when the
  curvature reaches its maximum value the equation of state becomes of the vacuum-like type (4)"*, i.e. R_{μν} = Λ g_{μν}.

**The chain actually built is Schwarzschild interior → (thin layer Σ₀) → de Sitter core. It stops there.**
The closed Friedmann piece is *not* part of this matching (see §2).

- Computed step A — where the junction sits. L163–167, eq. (6): *"The Schwarzschild metric (i.e. eq. (1) with
  g = f = −1 + 2m/r) can be used to approximate the geometry for r > r₀, where **r₀ = (12/α)^{1/6}(2m/l)^{1/3} l**"*,
  L172–174: *"the value of the radius r at which the invariant ℬ² for the Schwarzschild metric reaches its limiting value
  α/l⁴. For 2m ≫ l one has l ≪ r₀ ≪ 2m."* L175–177: Σ₀ (r = r₀) *"is spacelike. It lies inside the event horizon and has
  the topology S²×R¹."* This step **is** computed: r₀ is fixed by m and l.
- Hypothesised step B — the core is de Sitter. L203–209: *"Nevertheless our second hypothesis guarantees that beginning at
  some time moment τ₁ > τ₀ we can approximate these field equations by eq. (4). In the case of a spherically symmetric
  spacetime this means that the geometry is described by the de Sitter metric ... with g = f = (r/l)² − 1."*
  Preceded by the explicit admission of ignorance, L200–203: *"As for the future evolution of the geometry for τ > τ₀ we
  cannot specify the two unknown functions in eq. (1) until we know the exact field equations."*
- Idealising step C — the thin layer. L216–227: *"In the general case the global structure of the spacetime under
  consideration may depend on the details of the transition region τ₀ < τ < τ₁. But in the particular case when the
  duration Δτ = τ₁ − τ₀ of this transition is short (Δτ/l ~ 1) only some of its integral characteristics become important.
  In the latter case one may consider this layer as a thin massive shell and sew the Schwarzschild metric (τ < τ₀) with the
  de Sitter one (τ > τ₁) using the approach developed by Israel [5]. According to this approach we suppose that τ₀ = τ₁ and
  consider Σ₀ (τ = τ₀ = τ₁) as a junction surface."*
- Computed step D — the Israel conditions, eqs. (7)–(10). L229–235: *"The junction conditions at this surface require the
  three-geometries induced by both geometries to be identical while for the jumps of the extrinsic curvature
  K_{mn} = (K_deSitter)_{mn} − (K_Schwarzschild)_{mn} one has (m,n = 1,2,3): K_{mn} − δ_{mn}K = −8π S_{mn}"* (7), with S_{mn}
  the integral of the effective T_{mn} across the layer (8). Explicit components at L260–305, eq. (9), in
  x = r₀/l and y = 2m/r₀; limiting form eq. (10) at L308–314.
- Collapse case, computed analogue. Dust cloud eqs. (11)–(12); L434–443, eq. (13): the FRW dust interior is approximated
  *"until the moment τ = τ₀ when a = a\* = (60/α)^{1/6}(a₀/l)^{1/3} l. At this moment the spacetime curvature inside the cloud
  ℬ² [OCR-garbled exponents] reaches its limit α/l⁴."* L444–446: *"According to our hypotheses some time later after the
  transition layer the geometry in the region occupied by matter would also become de Sitter-like."*
  Note L453–457 promises only that a matching analysis *"allows one to describe the complete structure of the spacetime"*
  — the analysis itself is not shown; only the Penrose diagram (fig. 2) is given.
- Evaporating case: Vaidya (14)–(15); junction surface L516–522: *"r = r₀(v) = (12/α)^{1/6}[2m(v)/l]^{1/3} l"*, with
  ℬ² = 48m²(v)/r⁶ — again computed from H1.

**Is the de Sitter scale fixed by the limiting curvature, or free?** *Fixed to a Planckian value, but by an explicitly
declared additional assumption, not by derivation — and the fixing runs backwards.* L209–211: *"Here l = (3/Λ)^{1/2} and
**if we assume** that this length parameter l coincides with the parameter l in (5) then we have α = 24."* Read carefully:
the paper does not compute the de Sitter radius from eq. (5); it *posits* the identification and then uses it to pin the
otherwise free order-one α at 24. Without that assumption the de Sitter Λ is a second free scale. Two consequences worth
recording: (i) the fixed scale is Planckian and **contains no m** — the core's Λ is the same for a stellar and a
supermassive parent; (ii) the only quantities carrying the parent's mass are the junction locations
r₀ ∝ (2m)^{1/3} (eq. 6) and a\* ∝ a₀^{1/3} (eq. 13), not the interior's inflationary scale.

## 2. "Expanding closed Friedmann universe" — derived from the matching, or chosen? **Chosen.**

This is the load-bearing finding, and it is unambiguous in the text.

- The whole passage sits under a hedge and after a preceding branch, L567–577: *"Now we briefly discuss the **possible fate**
  of the de Sitter world which **according to our model may be** present in the interior of a black hole. First of all it
  should be noted that the de Sitter space is usually unstable [12]. It **seems likely** that if the hypothesis about the
  existence of a limiting curvature is valid then such an instability at the stage of deflation **might be** suppressed.
  There is **a possibility** that at the end of the deflation when the closed world has planckian dimensions it can just
  **disappear** in the process of quantum annihilation."* — i.e. branch zero is that there is no daughter at all.
- The closed-FRW step itself, L577–589: *"**If this does not happen** then the decay of this world which begins its
  inflationary expansion **may** create a new macroscopic universe in the same manner as happens in the usual inflation
  models [12]. **The result of this decay depends on the effective hypersurface on which it occurs and hence on the nature
  of the Λ-term.** In particular **one may expect** that a new closed Friedmann universe **will arise** as a result of this
  process. **In this case** the de Sitter space decays on some hypersurface Σ₂ (see fig. 2). The spacetime in the future
  with respect to Σ₂ will coincide with the spacetime of an expanding closed Friedmann universe."*
  Four hedges in five sentences, plus an explicit statement that the outcome depends on an unspecified input ("the nature
  of the Λ-term") that the paper never specifies.
- **The decisive receipt: the alternative branch is not closed.** L589 + L656–658: *"**Another possibility** is the creation
  of a white hole in a **new asymptotically flat universe** which lies in the absolute future with respect to the original
  asymptotically flat space."* The model therefore does not even determine the *sign of the daughter's curvature*;
  "closed" is one listed option against an asymptotically-flat option.
- **No junction computation exists at Σ₂.** The Israel machinery (eqs. 7–10) is applied at Σ₀ only. Σ₂ is introduced
  verbally, is placed "on some hypersurface", is drawn in fig. 2, and no equation follows it — the paper's last displayed
  equation is (15), 66 lines earlier (L491). Σ₁, distinct from both, is the deflation→inflation turning surface:
  L357–362, *"The anisotropic (Kasner-like) contraction of space in the interior of the black hole changes into the de
  Sitter deflation which in its turn (at the surface Σ₁) changes into the inflationary de Sitter expansion. The surface Σ₁
  has topology S³ and in this sense the diagram presented in fig. 1 describes the closed world formation inside the black
  hole."* Note this S³ is the *core's* spatial topology in the model, not a derived FRW.
- **Parameters of the daughter: not given, and not tied to the parent's mass.** The paper states no curvature radius,
  no matter content, no density, no e-fold count, no entropy for the post-Σ₂ Friedmann universe. Nothing anywhere in the
  text relates any daughter parameter to m. The only m-dependences in the paper are eqs. (6) and (13) (junction location)
  and the evaporation discussion. Search of the text finds no post-Σ₂ formula at all.

**Verdict on axis 2: chosen, hedged, alternative-bearing, and parameter-free.** The record's phrasing (*"will coincide with
the spacetime of an expanding closed Friedmann universe"*) is verbatim accurate (L587–589) but must always be carried with
its governing clause *"In this case"*, which is governed in turn by *"one may expect"*, which is governed by *"If this does
not happen"*.

## 3. Junction physics — surface layer and energy conditions: **yes, and the paper says so, twice.**

- Surface layer: required and explicit. L222–226: *"one may consider this layer as a **thin massive shell** and sew the
  Schwarzschild metric with the de Sitter one using the approach developed by Israel [5]."* Eq. (7) sets the extrinsic-
  curvature jump equal to −8π S_{mn}, a non-zero surface stress-energy given componentwise in eq. (9) and, for 2m ≫ l, in
  eq. (10) (L308–314). So the matching is **not** smooth (not a Darmois/Lichnerowicz junction): it carries a distributional
  shell by construction.
- Self-consistency check the authors run on that shell, L325–335: *"It is worthwhile noting the large parameter 2m/l does
  not enter these relations and hence there is no contradiction with our assumption that the time interval of the
  transition Δτ is short. Indeed if we suppose that in the transition layer T_{mn} reaches the planckian value
  (T_{mn} ~ l⁻²) then the proper time duration Δτ of this layer estimated as Δτ ~ S_{(mn)}/T_{(mn)} is comparable with the
  planckian time l."* The shell's stress is Planckian and mass-independent.
- Energy-condition violation: **stated, and used as the escape from a no-go theorem.** L660–674: *"The model considered may
  be interpreted as 'the creation of the universe in a laboratory' via a black hole which may be formed by contraction of
  matter up to high density. **This conclusion contradicts the theorem of ref. [13]** [Farhi & Guth]. **The reason is that in
  our case the assumptions of this theorem (in particular the existence of a global Cauchy surface as well as the condition
  of energodominance) may be violated.**"* That is an explicit admission that the construction lives outside the dominant/
  energy-condition regime — the limiting-curvature matter is what buys the evasion.
- Second, independent negative-energy statement in the evaporating case, L466–469 and L511–512: *"The radiation of energy to
  infinity in this process is accompanied by a **negative energy flux** through the horizon inside the black hole"*;
  *"For dm/dv < 0 the energy density of this radiation is negative."*
- Global causal pathology acknowledged: L346–351: *"The spacetime in the region lying in the future with respect to any
  Cauchy surface Σ in the Kruskal region is regular and complete. It should be noted that Σ is not a global Cauchy surface.
  Since H_C are Cauchy horizons such a global Cauchy surface does not exist at all."*
  The Cauchy-horizon stability claim is itself only an expectation, L381–386: *"in our case **if only** the hypothesis about
  the limiting curvature is valid, the backreaction of matter does not allow ℬ² and hence T_{mn} to grow without limit ...
  Hence **we may expect** that in our case there is no such instability."* No stability calculation is performed.

## 4. Observation-facing content — **none. Zero statements about our universe as an interior.**

- The paper contains no observational quantity, no data, no comparison to any measurement, no relic, no signature, and no
  number characterising any daughter universe. Every numeric value in the text is a Planck-scale definition
  (l ~ 10⁻³³ cm, L41–42; m_Pl ~ 10⁻⁵ g, L70–71) or a model constant (α = 24, L211).
- The only sentence touching "our universe" places us as the **parent**, not the interior, and even that is conditional and
  hedged, L686–695: *"Nevertheless **we hope** that the model described with a closed world in the interior of a black hole
  **may be useful** and that this picture or its main features **will survive in a future theory**. **If this happens then**
  the possibility (which was discussed earlier in connection with the Reissner-Nordström or Kerr spacetime) 'to travel'
  **from our universe into a new one** which is the absolute future with respect to us **may still be open**."*
- The "laboratory" framing (L660–668, quoted in §3) is likewise about *us making* a universe, never about *us being* one.
- **The title's question mark is never answered affirmatively.** The closest the paper comes is *"may still be open"*
  (L695). It is answered, if at all, in the conditional mood, and the paper opens the same passage by disowning certainty,
  L678–686: *"In conclusion, it should be stressed once again that the consideration in this paper is based on rather
  **restrictive assumptions** about the properties of the effective gravitational equations at high curvatures. **There exist
  various possibilities to violate our assumptions.** For example at small distances it may become important that the
  dimensionality of real spacetime is higher than four."*
- Additional self-limiting caution on the small-mass end, L539–546: *"It is necessary to stress that the thin shell approach
  in such a situation becomes questionable and one must treat the results obtained in the framework of this approach with
  caution."*
- So: **possibility construction only.** No "we are such an interior", no relic, no parameter tied to the parent mass, no
  testable consequence anywhere in the 709 lines.

## 5. Tier consequence — argued

**AUDIT_HOLDS_CONSISTENCY_ONLY.**

*Adversarial upward (could it be more?).* The strongest available challenge is QUALITATIVE-DIRECTIONAL, on the reading that
the paper directs a daughter universe to be spatially **closed** (L584–589), which maps onto the lane's Ω_k < 0 axis. That
challenge fails on three independent receipts, any one of which is sufficient:
(i) the paper never identifies our universe with a daughter — the one sentence naming "our universe" makes us the parent
(L692–695), so no observable of ours is directed;
(ii) even for the daughter, closedness is not directed: the very next sentence offers a **new asymptotically flat universe**
as the alternative outcome (L589, L656–658), so the model does not fix the sign of the daughter's curvature;
(iii) the closed-FRW step is not derived — it is "one may expect ... In this case", downstream of an explicitly unspecified
input ("the nature of the Λ-term", L583) and of a branch in which the world simply annihilates (L574–577). A directional
tier requires the paper to point at a sign for an observable; this paper points at a menu.
A PROSPECT challenge fails a fortiori: prospect requires an identified route to a number, and here there is not even a
proposed observable — no candidate signature is named anywhere in the text.
CALIBRATED-FALSIFIER is unreachable: no threshold, no amplitude, no datum.

*Adversarial downward (is CONSISTENCY-ONLY generous?).* No — it is earned rather than assumed. The paper does real
computation: eq. (6) locates Σ₀ from the limiting-curvature invariant, and eqs. (7)–(10) carry out the Israel matching with
explicit surface stress and a self-consistency check on the layer's duration (L325–335). That is a genuine demonstration
that a Schwarzschild-interior → de Sitter core geometry is constructible under H1+H2 — which is exactly what
CONSISTENCY-ONLY certifies. It also honestly flags the price (energodominance violated, L672).

*Grade:* **A(a)** — the construction is clean, the hedges are the authors' own and are correctly placed, and nothing is
overclaimed by the paper. The lane owns no missing threshold here: this entry has no number to be missing, by the paper's
own framing.

*Recorded refinements to the lane record (no tier change, no other file touched):*
- The record's "Σ₂" is correct for the de Sitter decay hypersurface, but the **Israel matching happens at Σ₀** (r = r₀,
  Schwarzschild|de Sitter, L227), and **Σ₁** is a third, distinct surface (deflation→inflation, topology S³, L358–360).
  Σ₂ carries no junction computation.
- The de Sitter scale is fixed to Planckian **by assumption** (L209–211), not by derivation; the identification is what
  fixes α = 24, not the other way round. It carries no dependence on the parent's mass.
- The closed-FRW alternative in the same paragraph is an **asymptotically flat** universe (L656–658) — worth carrying
  forward, since any downstream BHU chain that cites Frolov et al. for "closed" is citing one arm of a stated dichotomy.

---

## Plain language

This is a 1989 thought-experiment paper, and it is honest about being one. The authors make two guesses they say they
cannot check — that curvature can never exceed a Planck-scale value, and that when matter hits that ceiling it behaves like
vacuum energy — and then they do a careful, real calculation of what that would imply just inside a black hole's horizon:
the Schwarzschild geometry can be stitched to a de Sitter (inflating) core across a thin, spacelike shell, and they write
down the stitching conditions and the shell's stress explicitly. That much is computed, and it is why the entry deserves a
consistency-only rating rather than nothing. But the famous part — that a whole new expanding closed universe grows out of
that core — is not computed at all. It arrives in a single paragraph of "it seems likely", "one may expect", "in this case",
sitting downstream of an admission that the answer depends on something the paper never specifies, and immediately followed
by a competing option in which the new universe is *not* closed but infinite and flat. No equation follows that paragraph.
Nothing about the new universe's size, contents, or age is derived, and nothing about it is tied to the mass of the black
hole it came from. Most importantly for us: the paper never suggests our universe is one of these interiors. Its only
mention of "our universe" puts us on the outside as the potential maker, and its closing line answers the title's question
mark with "may still be open". There is nothing here to test against a sky. The tier stands.
