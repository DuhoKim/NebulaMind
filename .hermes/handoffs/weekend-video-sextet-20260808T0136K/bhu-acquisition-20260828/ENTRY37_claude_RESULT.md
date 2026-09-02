AUDIT_HOLDS_CONSISTENCY_ONLY

# Entry 37 — Smoller & Temple, "Shock-wave cosmology inside a black hole" — claude-seat deep audit (BLIND)

Seat: claude-seat (Fable 5.1). Date: 2026-09-02 18:17 KST (`date`). Brief: `ENTRY37_AUDIT_BRIEF_20260902.md`.
Source read: `../bhu-reading-20260823/sources/0210105_clean.txt` (402 lines; arXiv v1 dated "October 17, 2002", L5 — the
pinned text is the arXiv version, not the PNAS typeset). Blind: no ENTRY37_*_RESULT or codex/agy/kimi file opened.
Verdict scope: verdict + case only; no tier changed; obstruction axis (b30) not re-opened.

## 1. The construction — what is proved, what is deferred

**What the paper claims to prove (theorems with stated hypotheses):**
- Setup: a k=0 ("critically expanding", L23) FRW metric with p = σρ, σ constant, 0<σ<1 (L165–172), matched Lipschitz-continuously across a
  shock to a TOV-form metric (3.1) taken *inside* the black hole, i.e. with A = 1 − 2M/r̄ < 0 so r̄ is timelike (L93–95).
  Matching reduces to the ODE system (4.1)–(4.3) in u = p̄/ρ, v = ρ̄/ρ, σ = p/ρ (L118–142), which depends on the FRW side
  only through σ (L150); with σ constant (4.1) uncouples and becomes the scalar equation (5.4) in S = 1/N (L184–191).
- Entropy condition (4.6), 0<p̄<p and 0<ρ̄<ρ, is **imposed** ("we impose the entropy conditions", L152–156) to select
  the explosion over the implosion; together with the physical bound (5.5) it is equivalent to the single inequality (5.6) (L193–205).
- **Theorem 1** (L209–221): for every σ in (0,1) there is a unique solution u_σ(S) of (5.4) satisfying (5.6) for all 0<S<1,
  with 0<u_σ<ū, u_σ→ū = min{1/3, σ} as S→0, and p̄, ρ̄→0 as S→1 (the shock weakens to a zero-pressure OS interface).
- **Theorem 2** (L225–229): the shock is everywhere subluminal iff σ ≤ 1/3. (Obstruction axis; settled by b30; not re-argued.)
- **Theorem 3** (L233–247): shock speed at the Big Bang (S→0) is 0 for σ<1/3, ∞ for σ>1/3, exactly 1 for σ = 1/3 —
  this is the "σ = 1/3 is distinguished by the differential equations" claim of L39–41.
- **Section 6 bounds** ("we prove", L259, L266): first visibility of the shock at the FRW centre at t_0 with 1/H_0 = ((1+3σ)/2) r_* (6.1);
  1 ≤ 2/(1+3σ) ≤ √N_0 ≤ (2/(1+3σ)) e^{√(3σ)(1+3σ)/(1+σ)} (L262); t_crit/t_0 bounds (6.2)/(6.3) (L269–279); numerical
  corollaries √N_0 = 2, t_crit/t_0 = 2 at σ = 0 and 1.8 ≤ t_crit/t_0 ≤ 4.5, 1 < √N_0 ≤ 4.5 at σ = 1/3 (L280–291).
  I checked these: at σ = 1/3 the upper bound is e^{3/2} = 4.48 and the lower e^{√6/4} = 1.84 — the "1.8/4.5" figures are consistent.
- r̄_crit = Hubble length for k=0 ("We show", L58–59), and "the standard TOV metric cannot be continued into a Black Hole" cited to [6] (L60–61).

**What is asserted, cited, or deferred (not proved here):**
- The paper is explicitly a summary: "Details will appear in our forthcoming paper [8]; we wish here to summarize this work" (L44–45);
  [8] is "(preprint)" (L384–385). No proof of Theorems 1–3 or of the Section 6 bounds appears in the pinned text — every "we prove" is a
  statement of result. This is acceptable for the tier question (PNAS summary format) but it means the "theorem-grade" label of the record note
  rests on the authors' word plus [7]/[6], not on text the lane has verified.
- The thermalization remark (L42–44) — see 2(a) — is a "We find it interesting that…" sentence, deferred to [8].
- Uniqueness "the condition that the entropy condition be satisfied globally, determines a unique solution" (L306–307): restated from Theorem 1.
- The authors' own status assessment: "these solutions are only rough qualitative models because the equation of state on the TOV side is
  determined by the equations, and therefore cannot be imposed" (L330–332); the TOV side satisfies only the entropy conditions and "loose physical
  bounds" (L332–335); for realistic equations of state "other waves (e.g. rarefaction waves) would need to be present" that "would be pretty much
  impossible to model in an exact solution" (L338–340).

**On the record note "no underived ingredient":** true of the *equations* (every equation follows from GR + the ansatz), but the
*ingredients* are hypotheses, not derivations: k=0 (L23), FRW homogeneity behind the shock (the ansatz, L23–24), σ constant (L172),
the entropy sign (imposed, L154–156), the free launch position r_* (L296–297: "determined by one free parameter"), and the observer at the
FRW centre (L43–44). None of these is derived; they are the inputs. The note should read "no underived equation".

## 2. Observation-facing candidates — adjudicated one by one

**(a) Thermalization beyond the light cone (L42–44).** Verbatim: "We find it interesting that such a shock wave emerging from the Big Bang beyond
the Hubble length, would thermalize the radiation in a region well beyond the light cone of an observer positioned at the FRW center, even though the
model does not invoke inflation. Details will appear in our forthcoming paper [8]." Ruling: **asserted and deferred, not derived.** Nothing in
Sections 2–6 treats radiation, photons, temperature, or any transport across the shock; the metric is a perfect fluid on both sides (L72, L140).
Worse for the flag: the region "behind" the shock is homogeneous **by the FRW ansatz** (L23–24), so homogeneity is an input to the construction, not
an output of the shock — the sentence reads the ansatz back as a mechanism. No CMB uniformity scale, no temperature gradient, no edge, no sign of
any deviation from standard FRW is stated. An observer at the FRW centre with the shock outside the past light cone sees an exactly flat FRW
universe — i.e. the model's *only* stated observer sees nothing the standard model does not predict.

**(b) The σ = 1/3 selection (L39–41, Theorem 3).** A derived property of the constructed family: the shock leaves the Big Bang at exactly the
speed of light iff σ = 1/3. Ruling: **consistency with radiation-era physics, not a prediction.** The theorem says which member of the family is
"distinguished", not what our universe must show. If the early universe had σ<1/3 the model still admits a solution (speed 0 at launch, Theorem 3,
L237); only σ>1/3 is excluded, and that is the obstruction axis already settled. No observable of our universe takes a sign from this.

**(c) Present-day shock location / strength.** The paper gives: the shock lies "arbitrarily far beyond the Hubble length" (L13, L296); its distance
"is determined by one free parameter … the FRW position of the shock wave at the instant of the Big Bang" (L296–297); it first becomes visible at
the centre at t_0 with 1/H_0 = ((1+3σ)/2) r_* (6.1), at which moment it lies between 1 and 4.5 Hubble lengths (L286–289). Ruling: **no number
reaches an observation.** (i) t_0 is *defined* as the first-visibility instant (L267 "given that t_0 is the first instant at which the shock becomes
visible") and r_* is free, so t_0 in physical units is unconstrained — the paper never identifies t_0 with today, and cannot. (ii) I re-derived (6.1):
with R = (t/t_0)^{2/(3(1+σ))} the comoving particle horizon at t_0 is 3(1+σ)t_0/(1+3σ) and 1/H_0 = 3(1+σ)t_0/2, so (6.1) is exactly the statement
"the shock's *launch point* r_* enters the particle horizon at t_0". What "becomes visible" at t_0 is therefore the shock at the t = 0 surface — the
Big Bang instant, at formally infinite redshift, behind last scattering in any real universe. The named epoch is not an observationally reachable one.
(iii) Strength: Theorem 1 gives p̄, ρ̄→0 as S→1 (L219), i.e. the shock weakens toward the OS limit; no present-day jump is quantified.
(iv) Whether the shock lies inside our past light cone today is not stated and depends on the free r_*.

**(d) White-hole exit / event horizon.** The interface "continues out through the White Hole event horizon … at the instant when the wave is
exactly one Hubble length from the FRW center" (L313–315), at t_crit ≤ 4.5 t_0 (L290–291). Ruling: **no observable consequence stated.** What an
observer at the centre sees at or after t_crit is not addressed; the mass function M is explicitly said to lose its physical interpretation inside
the black hole (L99–108); the closing paragraph is a symmetry argument ("we may well also be forced to accept White Holes", L343–352), not a prediction.

## 3. The 08-28 blind flag — sentences that could carry a signed direction

I searched the text for every sentence carrying a sign on something an observation could touch:
1. L42–44 (thermalization) — **asserted/deferred** (see 2a). No sign, no observable.
2. L156 (4.6), 0<ρ̄<ρ, 0<p̄<p — a derived *existence* (Theorem 1) of solutions with lower density outside the shock, but the sign is **imposed**
   as the entropy condition (L154 "we impose"). Under Duho ruling A(a) an assumed direction is not directional. It is also not on an observable of our
   universe: the TOV region is outside the past light cone until the free-parameter epoch t_0.
3. L15 / L304 (total mass behind the shock decreases) — derived (M′ = −4πp̄r̄² inside the black hole, L106), but M has no physical
   interpretation inside the horizon by the authors' own statement (L99–100, L108). Not an observable.
4. L288–291 (shock within 4.5 Hubble lengths at first visibility; emergence by 4.5 t_0) — derived bounds, but pinned to the free epoch t_0, which is
   the infinite-redshift launch image (2c). No sign on any measurable quantity.
5. L318–322 (finite-mass, bounded universe; "does not require the physically implausible assumption … of infinite mass") — a qualitative
   preference, not a derived observable; the interior is exactly FRW and indistinguishable from infinite-extent FRW to any observer with the shock
   outside the light cone.

No sentence in the paper states a signed, derived direction on an observable that could be contradicted. The 08-28 flag most plausibly latched onto
L42–44 (the only sentence that mentions observers and radiation), and that sentence is the one the authors themselves defer. The flag does not survive.

## 4. What a strict model could compute from this paper alone

**Computable from the text:** u_σ(S) by numerically integrating (5.4) under (5.6); v(S) from (4.3); shock speed s(S) from (4.5); the comoving
shock trajectory r̄(N) from (4.2) up to the free constant r_*; the Section 6 bounds. All of it is *internal geometry of the model* parameterized by
the free r_*.

**Not computable — and not the lane's to complete under the "missing threshold, never a missing number" rule:**
- CMB anisotropy for an off-centre observer: the paper contains no radiation sector, no photon propagation across the shock, and no observer other
  than the FRW centre (L43–44). The interior is exactly homogeneous and isotropic, so any observer with the shock outside their past light cone sees
  zero extra anisotropy; a signal appears only once the shock enters the light cone, which requires (i) r_* (free), (ii) the observer's offset
  (absent), and (iii) a model of what light does at a fluid shock (absent). Three missing numbers/models, not a missing threshold.
- Age/size scales: t_0 and r_* are related only to each other by (6.1); neither is fixed. The σ-constant idealization is disclaimed by the authors as
  "rough qualitative" (L330–332), so a realistic radiation→matter→Λ history would be a lane-built extension, not the paper's model.

So: not a calibratable prediction the paper owns; any calibrated version would be a lane-completed construction with lane-chosen numbers.

## 5. Tier consequence, argued

- **QUALITATIVE-DIRECTIONAL — rejected.** Requires a derived sign on an observable. The only derived signs (2–4 in §3) are either imposed by
  hypothesis (entropy condition), attached to an unobservable quantity (interior mass function), or pinned to a free-parameter epoch that
  corresponds to an infinite-redshift image. The candidate the flag likely used (L42–44) is explicitly deferred to [8].
- **CALIBRATED-FALSIFIER — rejected.** No number reaches an observation; r_* is free; the authors call the model "only rough qualitative" (L330).
- **PROSPECT — rejected for this entry.** The deferred thermalization claim, even if delivered in [8], is a horizon-problem *consistency* (uniform
  radiation without inflation), not a signed prediction distinguishable from inflation; the paper names no observable it would move. If the lane wants
  to chase L42–44 the correct action is to acquire and audit [8] as its own entry (Smoller & Temple, "Cosmology, black holes, and shock waves beyond
  the Hubble length"), not to promote entry 37 on a sentence it defers.
- **CONSISTENCY-ONLY — holds.** The paper is an exact-GR existence-and-uniqueness construction whose stated observer sees exactly flat FRW; every
  observation-facing sentence is either an ansatz read back as a mechanism, a bound on internal geometry at a free epoch, or a deferred remark.
  Consistent with the authors' own framing: "The model does not require the physically implausible assumption…" (L318) and "these solutions are only
  rough qualitative models" (L330). No falsifier stated, none derivable from the text without lane-supplied numbers.

Token: **AUDIT_HOLDS_CONSISTENCY_ONLY**. Not tier-adjacent in my reading; no packet to Duho needed from this seat unless the other seat disagrees.

## Plain language

This paper builds, with real theorems, a universe that is a flat expanding bubble with a shock wave at its edge, sitting inside a black hole. It
proves such a thing can exist in Einstein's equations, that the shock must be an explosion rather than an implosion, and that the radiation-era pressure
law is the one where the shock leaves the Big Bang at exactly light speed. What it never does is say what any of us would see. The one sentence
that sounds like a prediction — that the shock would smooth out the radiation without inflation — is a remark the authors say they will justify in a
later paper, and it leans on the fact that the inside of the bubble is smooth by assumption. Where the shock is today is a free knob the paper leaves
unset, and the only moment it names for "seeing" the shock turns out to be the image of the Big Bang itself, which no telescope can reach. The earlier
flag calling this "directional" was reading the deferred remark as a result. It stays a consistency paper.
