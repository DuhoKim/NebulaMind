# Lana — does spin–LSS alignment threaten the Longo-amplitude test?

**Lana (science / claim-boundary seat), 2026-08-12.** Duho's systematic, relayed by Hwao: intrinsic
spin–large-scale-structure alignment could imprint a coherent handedness pattern on a partial sky —
real, physical, non-cosmological, and untouched by instrument/pixel/selection controls. Assessed from
primary literature fetched today (Tempel & Libeskind 2013, ApJL 775, L42; Laigle et al. 2015, MNRAS 446,
2744; Wang et al. 2021, Nat. Astron. 5, 839; Motloch et al. 2021, Nat. Astron., + Motloch et al. 2022,
PRD 105, 083512), with [VERIFY] on anything not pinned. **Nothing published, accepted, or run.**

---

## 0. Verdict up front

**The concern is real physics, and working it through dissolves most of it by a symmetry that deserves
to be in the prereg in its own right:** everything the alignment literature actually establishes is an
**axis** effect — a statement about the headless vector ±L̂ — and any spin distribution that is even
under L̂ → −L̂ projects to **exactly zero** net chirality, per galaxy, on any footprint, however
partial. Partial sky does not break this; the cancellation is per-object, not across the sky. What
survives are the **parity-odd channels** — filament vorticity, filament rotation, signed spin–initial-
condition correlations — and the pinned literature makes each of them weak, sign-alternating, or both.
A generous end-to-end estimate puts the structure-induced contamination of our statistic at
**|ΔA| ≲ 4×10⁻³ — an order of magnitude below Longo's 0.0408** — and to *fake* Longo's amplitude a
single structure would need ~80% signed spin coherence over ~5% of the sample, two orders of magnitude
beyond anything observed. **At the amplitude this study tests, the concern is dismissed with a number.
It is not dismissible for any future study chasing A ~ 0.005-class signals, and one genuine design
improvement falls out of the analysis** (§3: the independent-permutation null is mildly optimistic if
spin signs correlate spatially; a blocked-jackknife supplement closes it cheaply). Per Q4 discipline, a
pre-committed boundary amendment is drafted in §5 regardless — named beforehand, it constrains what a
positive may claim; discovered afterwards, it becomes an argument.

## 1. Q1 — Does axis alignment project into net chirality? Worked, not asserted.

**The observable.** For trailing spiral arms (the near-universal case **[VERIFY: canonical references
for trailing-arm universality; rare leading-arm exceptions exist, e.g. NGC 4622]**), the projected
handedness seen from Earth is set by which way the spin vector points along the line of sight:
apparent chirality = sign(**L** · n̂). Our statistic is A ∝ ⟨sign(**L** · n̂)⟩ over the accepted sample.

**What the alignment literature establishes.** Tempel & Libeskind 2013 (SDSS): spiral spin **axes** are
*weakly* aligned with filament directions. Laigle et al. 2015 (simulation): vorticity is confined to
filaments; low-mass haloes acquire spin **along** the filament, high-mass perpendicular, transition
~10¹² M☉. Every such statistic is a function of |L̂ · f̂| — the **axis**, not the arrow. None of these
papers measures or claims a preferred *sign* of L along the aligned direction.

**The projection theorem, such as it is.** Let f(L̂ | env) be the spin-direction distribution given the
local environment. Axis alignment of any strength means f is even: f(L̂) = f(−L̂). Then
⟨sign(L̂ · n̂)⟩ = ∫ f(L̂) sign(L̂ · n̂) dL̂ = 0 identically, because the integrand is odd under
L̂ → −L̂ while f is even. **This holds per galaxy, for any n̂, any footprint, any volume, any alignment
strength.** A dominant local filament that aligns every spin axis in the survey with itself still
contributes zero net chirality unless something *also* picks which way the spins point.

**What axis alignment does do to us:** it modulates the |L · n̂| distribution — the face-on fraction,
hence classifiability and abstention — coherently with local structure. That is a **sensitivity/
selection modulation**, exactly the channel the design already treats (covariate battery arm-contrast
and inclination proxies; the C5/CB-7 monopole–gradient coupling bound). It cannot flip signs.

**So the concern survives only through parity-odd channels — a net ⟨**L**⟩ in the volume:**
1. **Filament vorticity** (Laigle 2015): signed, but filament cross-sections partition into (typically
   four) **quadrants of alternating vorticity sign**. Summed over a filament, the signed contribution
   largely cancels by construction; summed over the many filaments in a z < 0.15 survey volume, the
   senses are uncorrelated.
2. **Filament rotation** (Wang et al. 2021): a real candidate signal — but detected only by **stacking
   thousands of filaments under an orientation convention**; per-filament rotation sign varies, no
   universal handedness is claimed, and the paper's own title says "possible." Contributes as a random
   per-structure sign, not a coherent survey-wide one.
3. **Signed spin–initial-condition correlation** (Motloch et al. 2021): the strongest evidence that
   spin *arrows* are partially predictable from LSS — **2.7σ with ~15,000 galaxies**, i.e., a
   per-galaxy signed correlation of order 2.7/√15000 ≈ 0.02 in correlation units [order-of-magnitude
   reading of their significance — **[VERIFY against their stated correlation amplitude]**]. Their
   2022 follow-up finds left- and right-helical correlations identical within errors (no chirality
   violation). The channel exists; it is ~2%-weak and it correlates spins with a zero-mean helicity
   field, not with a fixed sky direction.

**Answer to Q1: alignment as established does not project — by exact symmetry. Only the weak signed
channels can, and they enter as spatially fluctuating fields with zero mean, not as a coherent dipole.**

## 2. Q2 — Amplitude, generously

Model the signed channels as coherent sign-domains: N accepted galaxies composed of domains of
effective size m_eff = 1 + (m̄ − 1)ρ_sign, where ρ_sign is the pairwise signed-spin correlation within
a domain and m̄ the galaxies per domain. The structure-induced statistic is a random variable of
magnitude ~ √(m_eff/N) — and note it is a *fluctuation with random direction*, not a bias toward any
axis.

- Generous inputs: ρ_sign ~ 0.02–0.05 at group/filament-quadrant scales (Motloch-scale coherence
  applied wholesale **[generous — VERIFY any published signed-spin two-point amplitude; Shamir has
  claimed neighbour spin correlations, contested]**), m̄ ~ 10 → m_eff ≲ 1.5.
- At N = 10⁵: |ΔA| ~ √(1.5/10⁵) ≈ **0.004**. An order of magnitude below 0.0408, and random in
  direction — the chance it lands within the frozen band *at Longo's axis with Longo's sign* is smaller
  still.
- **The fake-Longo requirement, inverted:** a single structure holding fraction f of the sample with
  signed coherence c contributes ΔA ≤ f·c. To reach 0.0408: f = 5% (larger than any single structure's
  share of a flux-limited z < 0.15 footprint sample [estimate — **[VERIFY with the bound survey's n(z)
  at BS-1]**]) requires **c ≈ 0.8** — i.e., four of five galaxies in the structure pointing their spin
  arrows the same way along our line of sight. The strongest signed effect in the pinned literature is
  the ~2%-class Motloch correlation. Nothing within two orders of magnitude of c ≈ 0.8 exists in the
  record.

**Answer to Q2: at Longo's amplitude the concern is quantitatively negligible — ≲ 0.004 generous, ≲
10⁻³ realistic, versus 0.0408 tested.** Stated with the converse: a study chasing amplitudes at or
below ~0.005 could NOT dismiss this channel and would need the §3 separators as decision-bearing
controls. Our narrowed design is protected by its own narrowing.

## 3. Q3 — Separable in principle? Yes, and one genuine design fix falls out.

A structure-induced pattern and a cosmological dipole differ observably:

- **Redshift coherence:** a structure signal tracks the structure's radial profile — it lives in
  specific shells; a cosmological dipole is shell-stable. Control: D̂(n̂_L) by redshift (or, absent
  photo-z, magnitude) tertile; heterogeneity χ².
- **Angular coherence scale:** a structure signal is patch-coherent at the structure's angular size
  and unstable under spatial jackknife (drop-one-region); a dipole is footprint-stable.
- **The null-calibration fix (new, and worth having regardless of this concern):** the frozen
  permutation null shuffles signs **independently**, which understates the variance if signs correlate
  spatially (design effect 1 + (m̄−1)ρ_sign — the same m_eff as §2; a percent-level to few-percent
  inflation of σ_D at the generous inputs). **Supplement: a spatially blocked jackknife error estimate
  (HEALPix Nside = 8 blocks, drop-one-block), reported alongside the permutation p; if the blocked σ
  exceeds the permutation σ by more than 20%, the permutation p is demoted and the blocked estimate
  governs.** Cheap, frozen, and it makes the null honest against exactly the physics Duho raised.

**Answer to Q3: separable — shell-coherence, jackknife stability, and a blocked null are the
separators, and all three are cheap enough to pre-commit.**

## 4. Q4 — Into the preregistration regardless

Even dismissed at amplitude, the channel goes in **pre-committed**, for the reason Hwao stated: named
beforehand it constrains claims; discovered afterwards it becomes an argument. The Mittal–Singal
discipline, applied prospectively.

## 5. Ready-to-fold prereg amendment (drafted here; **the prereg is NOT edited** pending Kun's gate)

**5a. Add to §6 negative controls, as NC-7 (frozen):**
> **NC-7 Structure-coherence controls.** (i) D̂(n̂_L) recomputed in three redshift shells (photo-z per
> BS-2; magnitude tertiles as the declared fallback if BS-2 drops photo-z), heterogeneity χ² published;
> flag if p < 0.01. (ii) Spatial jackknife: drop-one-HEALPix-block (Nside = 8) distribution of D̂(n̂_L)
> published; flag if any single block shifts D̂ by > 3·σ_D. (iii) Blocked-jackknife σ reported beside
> the permutation σ; **if σ_blocked > 1.2·σ_perm, the blocked estimate governs all §2 decision
> regions.** Flags (i) and (ii) are diagnostics; trigger (iii) is decision-bearing.

**5b. Add to §7 boundary (frozen text):**
> **Named alternative explanation, pre-committed:** intrinsic spin–LSS alignment can contaminate this
> statistic only through parity-odd channels (filament vorticity, filament rotation, signed
> spin–initial-condition correlations). From the primary literature these contribute |ΔA| ≲ 4×10⁻³
> under generous coherence assumptions — an order of magnitude below the tested amplitude
> (`prereg/LANA_FILAMENT_ALIGNMENT_ASSESSMENT_20260812.md`). Nevertheless: **a REPRODUCED-LONGO
> outcome may not be described as cosmological unless NC-7 shows shell- and footprint-stability**; a
> shell-localized or single-block-driven positive is reported as "consistent with local-structure
> contamination" and triggers the adversarial re-audit with this channel first in line. A null is
> unaffected: structure contamination of ≲ 0.004 cannot mask a real 0.04-class dipole.

**5c. Register addition:** BS-2 gains one line — the photo-z decision now also determines NC-7(i)'s
shell variable, and the fallback (magnitude tertiles) must be declared at binding, not at analysis.

## 6. Answer to Hwao's framing question

Duho's instinct located the one systematic that is genuinely physics rather than instrumentation — and
the answer is that the design's narrowing saves it: **the axis-alignment literature projects to zero by
symmetry; the signed channels are real but two orders of magnitude too weak to fake 0.0408; they are
separable by shell and block controls that cost almost nothing; and the one place the physics genuinely
touches our machinery — spatially correlated signs versus an independence-assuming permutation null —
is fixed by the blocked-jackknife supplement in 5a.** The concern is dismissed at this study's
amplitude *with numbers*, and pre-committed as a named alternative anyway, which is what makes the
dismissal trustworthy.

**Sources (fetched today):** Tempel & Libeskind 2013, ApJL 775, L42 (axis alignment, SDSS, "weakly");
Laigle et al. 2015, MNRAS 446, 2744 (vorticity quadrants, alternating signs, ~10¹² M☉ transition);
Wang et al. 2021, Nat. Astron. 5, 839–845 (filament rotation via stacking; viewing-angle dependent);
Motloch et al. 2021, Nat. Astron. (spins–ICs, 2.7σ, ~15,000 galaxies); Motloch et al. 2022, PRD 105,
083512 (no chirality violation; L/R helical correlations equal within errors). **[VERIFY] register:**
trailing-arm universality citation; Motloch stated correlation amplitude vs my significance-derived
order-of-magnitude; any published signed-spin two-point amplitude; largest-structure sample fraction at
BS-1 binding.

— Lana, 2026-08-12. Assessment only; prereg amendment drafted in §5, not applied. Kun gates; Duho
decides.
