RULE_A_LOCAL_ANCHORING__B_ADIABATIC_CARRY_GEOMETRICALLY_FORBIDDEN

# EPOCH gate verdict — how T_s varies with crossing epoch eta
(2026-08-27, K-seat. Adjudication of KICKOFF_GATE_EPOCH.txt. This is a ruling on the
construction, justified from the pinned geometry only: 0210105_clean.txt sec. 3-7, the gated
A1 orbit, and the two named implementations. The transfer, the optical depth, and the null's
existence are not re-opened, per the kickoff's instruction.)

## 1. The ruling

**(a) — LOCAL junction anchoring — is the construction the pinned geometry forces. (b) —
adiabatic carrying along the crossing-epoch sequence — is ruled out: it applies a
single-element evolution law along a locus that is not a single element.**

The locus swept by varying the crossing epoch is a **spacelike family of DISTINCT comoving
fluid elements, each sampled exactly once, at the instant of its own creation at the shock**.
It is not a fluid worldline, and no segment of it is tangent to one.

One caveat belongs to the record and is stated in sec. 4: (a)'s exponent 1/4 is forced by the
pinned material only at w = 1/3; for w != 1/3 it is a declared junction-microphysics
assumption (radiation-dominated thermal content at the shock). The *structure* of (a) —
event-by-event local anchoring — is forced at every w. The *exponent* of (a) is forced at
w = 1/3 and assumed elsewhere. No chained law of type (b) is available at any w.

## 2. The locus: what varying the crossing epoch actually sweeps

**Setup.** Observer inside the FRW at conformal time eta_o = 2, offset x; direction mu. Each
sight line is a null ray from the observer back to the shock worldsheet, meeting it at epoch
eta(mu). The family of crossing events {P(mu)} is the observer's past light cone intersected
with the shock worldsheet.

**It is a spacelike family.** Any two distinct events P1, P2 on one observer's past cone are
spacelike separated: the segments P1->O and P2->O are future-directed null vectors k1, k2
from the same vertex; for non-parallel future null vectors k1.k2 < 0 (signature -+++), so
|P1P2|^2 = -2 k1.k2 > 0. The locus is therefore a spacelike curve on the boundary — a cut of
the shock worldsheet, not a trajectory.

**Each event on it is a different exterior fluid element.** In the exterior the fluid is
"co-moving with the metric" (0210105_clean.txt:72) of the ansatz (3.1) with A = 1-N < 0,
so rbar is "the timelike variable" (:93-97). The comoving four-velocity has only the timelike
rbar component (gated P1; confirmed in GATE_PHASE5B_VERDICT.md:45): worldlines are the curves
tbar, theta, phi = const. A spacelike locus cannot be tangent to a timelike congruence.
Moreover the shock is *non-comoving everywhere on the gated orbit*: pinned (4.5) gives
s = sqrt(N)(sigma-u)/(1+u); on the gated orbit s spans [0.3333, 0.999959] and equals 0.5252
at the centered crossing (verified against the stored shock_speed_s column, agreement to all
quoted digits). The worldsheet is pierced transversally by the flow: the element found just
outside the junction at epoch eta is the element *born* at the shock at that event. Distinct
crossing epochs = distinct births = distinct worldlines.

**The twist that makes (b) arguable — and why it does not rescue (b).** Inside the horizon
rbar is time, and everything exterior depends on rbar alone: the ansatz makes
(rhobar, pbar, N, B) functions of rbar only, and the pinned text says it outright — "the
density rhobar(rbar) and mass M(rbar) are both constant at each fixed time in the TOV
spacetime beyond the shock wave" (:308-311). The exterior is *homogeneous at each instant*.
So along the crossing sequence, d ln rhobar/d eta = (d ln rhobar/d rbar)(d rbar_s/d eta) is a
genuine TIME variation, identical to the gradient along every worldline at that instant. That
is the kickoff's "not cleanly separable," and it is real — for the density. It does not carry
over to the temperature, for the reason in sec. 3.

## 3. Why (b) is ruled out

The adiabatic law d ln T = [w/(1+w)] d ln rhobar is a per-element *evolution* law: it chains
states of ONE element along ITS worldline. Three independent defects block its use here.

1. **Wrong curve.** The blind seat integrates d ln T/d eta = [w/(1+w)] d ln rhobar/d eta along
   the crossing sequence (p7_blind_dipole.py:94-126) from a single normalization at the
   centered crossing. The sequence is a spacelike cut across distinct worldlines (sec. 2);
   there is no shared history along it to carry a normalization through.

2. **Evolution vs. initial data.** Even granting homogeneity, each element's post-birth
   evolution obeys T(rbar) = C(tbar) [rhobar(rbar)]^{w/(1+w)}, with C(tbar) the element's
   adiabat, fixed at its birth by the shock. The junction value at epoch eta is
   T_s(eta) = C(tbar_s(eta)) [rhobar(eta)]^{w/(1+w)}. The junction samples each worldline
   once, AT its birth — so the junction temperatures across eta are *initial data*, which the
   adiabatic law does not constrain. Construction (b) is the C = const sub-case, adopted
   silently. The post-shock state itself varies along the shock (du/dN != 0 on the gated
   orbit, measured up to 0.125; the shock weakens, d ln rhobar/d eta < 0 at the crossing,
   measured -8.67): there is no pinned equation forcing a common adiabat across births.

3. **Conflict with the junction's own physics except at one point.** Local post-shock
   thermalization — the assumption the observable's thick regime already lives on — sets each
   newborn element's radiative temperature from its own post-shock state, which makes
   C(tbar_s(eta)) proportional to rhobar(eta)^{1/4 - w/(1+w)}. That is constant only at
   w = 1/3. So (b) disagrees with junction-local physics at exactly the w-range both nulls
   live in, and agrees with it only at w = 1/3 — the value the pinned paper itself singles
   out (Theorem 3, :233-245), and the value where the two constructions coincide by
   arithmetic (1/4 = w/(1+w)).

Defect 1 alone is fatal; defects 2 and 3 show the repair is not a better integration path but
a different kind of statement (initial data at the shock, per event).

## 4. Why (a) is the correct structure — and precisely what in it is not pinned

Construction (a) anchors the junction temperature event-by-event from the local post-shock
state supplied by the gated orbit (rhobar(eta) = v(eta) rho_FRW(eta)), and then — correctly —
applies the adiabatic law along each element's OWN worldline as the exterior profile descends
from the junction (p6_path_transfer.py:84-91: blackbody anchor at the junction, exponent
w/(1+w) along the depth). That is the only placement of the adiabatic law the geometry
permits: along rbar at fixed tbar, with per-element normalization set at the birth event.

What is pinned in (a):
- the locality: T_s(eta) is a function of the post-shock state at the single event eta, and
  of nothing else. Forced by sec. 2.
- the full law at w = 1/3, where blackbody, adiabatic, and the pinned distinguished case all
  coincide.

What is NOT pinned in (a): the exponent 1/4 for w != 1/3. T_s ∝ rhobar^{1/4} identifies the
radiative energy density at the junction with the total rhobar — radiation-dominated thermal
content behind the shock. That is the natural closure in the model's own thick regime (the
emitting skin sits at the junction; the junction w = u/v = 0.2456 at the crossing is
relativistic, not cold), but it is microphysics, not an output of (3.1)-(3.5). The general
forced form is T_s(eta) = [epsilon_rad(eta)/a]^{1/4} with epsilon_rad set by post-shock
thermalization — still local, still not (b).

## 5. Consequences for the null's location

- The blind seat's null at w = 0.0815 rests on the ruled-out carrying law and is withdrawn as
  a candidate location. The (a)-construction's null — w = 0.0408 at unit opacity, migrating
  upward with opacity over the resolved rows of P8_THICK_LIMIT_RECEIPT.md — is the operative
  one, quoted CONDITIONAL on the sec. 4 radiation-content assumption at the junction.
- The phenomenon (a real cancellation in both treatments) is untouched and is not this gate's
  business. The two constructions' agreement at w = 1/3 is now explained rather than
  coincidental: it is the unique point where local initial data and adiabatic evolution are
  the same law — and the same point the pinned source distinguishes dynamically.

## 6. Answer to the kickoff's third question

Is the choice irreducible from the pinned material? **No, for (a) vs (b): the geometry
decides it — the locus is a spacelike family of distinct elements, so the law must be local.**
Yes-but-narrowly for the local exponent at w != 1/3: the pinned system carries no temperature
variable, so the T-rhobar map at the junction is a declared microphysical input, to be stated
alongside any quoted null location. That is a much smaller ambiguity than the one the kickoff
posed: one local assumption, named, versus two incompatible global constructions.

## Verification anchors
- Pinned: metric (3.1) 0210105_clean.txt:66-70; field equations (3.2)-(3.4) :75-91;
  A = 1-N < 0 / rbar timelike :93-97; comoving fluid :72; shock speed (4.5) :144-148;
  homogeneity per instant :308-311; Theorem 3 :233-245.
- Gated orbit (a1_results.csv), recomputed this gate: crossing eta = 0.563389,
  sqrtN = 2.5499 (A = -5.50, inside horizon); u = 0.105623, v = 0.429999, w_junction =
  0.245635; s = 0.5252 at crossing, s in [0.3333, 0.999959] over the orbit (never comoving);
  d ln rhobar/d eta = -8.67 at crossing (junction density falls with epoch).
- Exponents: w/(1+w) = 0.0392 at w = 0.0408; 0.0754 at w = 0.0815; 0.2500 at w = 1/3.
- Implementations read directly: p6_path_transfer.py:84-91 (construction a);
  platoon/gpt1_blind_p7/p7_blind_dipole.py:94-126 (construction b).
