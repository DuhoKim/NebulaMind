B3_REVIEW=CLASS_STANDS

# KIMI adversarial challenge to B3 (2026-09-07)
Referee: Kimi k3, independent of the B3 worker. Target: `B3_CLASS_FILED_20260907.md` (class `B1_PRODUCTION_RESCUES`), evidence
`B3_RESCUE_20260907.md` + `b3_rescue.py`. I re-derived every identity myself, re-ran the script, stressed the theorem off-grid,
and read the source version the claims are bound to. Verdict: the class stands. Three findings require correction notes; none is
fatal. I did not repair anything.

## What I actually did (grounding)
- Re-ran `/usr/bin/python3 b3_rescue.py` from `bounce/`: exit 0. Totals reproduce exactly: `GRID_TOTAL_b/c: B=782 S=118 X=108`,
  max normalised constraint defect 1.92274e-10, refinement 1.42686e-12, all threshold controls and classification assertions pass.
  I did not trust the printed tokens; the run regenerates them.
- Independent SymPy re-derivation (my own script, not the worker's): `C_dot + 6HC = 0` for the filed off-constraint evolution;
  `H_dot = κ ε/3 − 3H²` confirmed as the directional-equation mean with ρ=ε−αn², P=ε/3−αn² (no constraint used);
  `d ln(αn²)/d ln a = −6 + 2βH³/n`; `d/dt ln(αn²/S) = 2βH⁴/n`; `N_x = β(Q/3)^{3/2}e^{6x}`; `E_x = −2E + 2αN N_x`;
  `Q_x = −2κE`; β=0 reduction `du/dt = −1/(3a)`. All match the filed algebra.
- Closure (c) caloric check: `F'_c = 2T³(4T⁴+7T²+2)/(1+T²)² > 0`, range (0,∞) — the claimed global inverse exists. The (x,u,N,E)
  right-hand side never references T, so (b) and (c) are literally the same ODE with T a passive reconstruction: the filed
  "coordinate equivalence, not two confirmations" is accurate.
- Source: arXiv 2007.11556v2 HTML (self-identifies as GRG 53(2), 18 (2021), v2 dated 23 Jun 2026), read as a web extraction of
  the arXiv endpoint, not the Springer publisher page. Equation claims below bind to that version only. Verified on the page:
  (1) effective source; (14) first law; (33)/(34) number law with Ψ=βH⁴; §9 thermal forms ε=h⋆T⁴, p=ε/3, n=h_nT³; (36); (37);
  and §7 (30) curvature-sourced KS shear.
- Off-grid stress of the theorem (outside the declared α interval [0.25,1] and β grid): α=1e-3 f=0.9 n0=0 β=0.01;
  α=0.25 f=0.999 n0=0 β=1e-3; α=50 f=0 n0=0 β=1e-5; α=1e-4 f=0.99 n0=0.1 β=1 — all bounce in both closures, constraint error
  ≤3.3e-10. Two further cases I constructed (α=100 n0=5; α=5 n0=3) are genuinely inadmissible (1+σ−αn0²<0), correctly X.
- Read `B1_PREREG_BIANCHI_I_BOUNCE_20260907.md` §4 for the declared class content (see FINDING 1).

## ATTACK 1 — the finite-bounce proof: it survives, hardest attacks first
Tried to break it at every point the challenge names:

(a) Hidden β threshold: NONE. Stage 1: while N≤N⋆=√(S0/κα), κE=Q−S0+καN²≤Q, so Q_x≥−2Q, Q≥Q0 e^{−2x}, hence
N_x≥β(Q0/3)^{3/2}e^{3x} — the lower bound GROWS exponentially; the integral is unbounded for any fixed β>0. No admissible datum
keeps the integral term small: the e^{3x} factor dominates the e^{−3x} decay of the Q-bound. As β→0⁺ the proof is non-uniform
(bounce x-location diverges, a_b→0) but the filed claim is explicitly "every fixed β>0", and the non-uniformity is disclosed in
`B3_RESCUE` §2 ("The proof is not uniform as beta→0 or alpha→0"). The claim as filed is exactly what is proved.

(b) Initial-data assumptions: the proof needs only the stated admissibility — ε0>0, n0≥0, S0≥0, 3H0²=κ(ε0−αn0²)+S0>0, H0<0
(strict contraction). It does NOT need n0>0 (the integral form N(t)=n0+∫a³Ψdt covers n0=0; stage 1 works from N0=0, and the
S0=N0=0 case is handled by "initial equality crosses immediately"). It does NOT need anything about the initial contraction RATE
beyond Q0>0. H0<0 is the hypothesis "contracting datum", disclosed everywhere. H0=0 data are not contracting data (see Attack 4).

(c) Exhaustiveness of the dichotomy: while H<0, Q is strictly decreasing (Q_x=−2κE<0, E≥E0 e^{−2x}>0) and u=−Ha³ is strictly
decreasing in both τ and x. Either N crosses N⋆ at finite x (stage 2: N monotone since N_x>0, so for x≥x1,
Q_x=−2(Q+καN²−S0)≤−2D with D=καN1²−S0>0, root by x1+Q(x1)/(2D)), or a bounce intervenes, or N≤N⋆ forever — the last
contradicted by the unbounded integral. No finite-x blow-up before the root: Q≤Q0 bounds N_x on finite intervals, the constraint
bounds E. At the root Q_x=−2κE_b<0 so dt/dx=a³√(3/Q) is integrable (finite proper time), all variables finite, Ḣ_b=κε_b/3>0 —
a genuine smooth minimum, not a solver artefact. Data already above threshold (καN0²>S0) enter stage 2 directly at x1=0.

(d) x-parametrisation validity: requires H<0 throughout, which holds until Q=0, which IS the bounce; H=0 ⟺ u=0 ⟺ Q=0. Airtight.

Verdict: the proof is sound, complete, and matches the claim's quantifiers exactly. Off-grid numerics (above) confirm no
threshold down to β=1e-5, α=1e-4, shear fraction 0.999.

## ATTACK 2 — the scaling claim: correct, including signs and the turning point
`d ln(αn²)/d ln a = −6 + 2βH³/n` re-derived from ṅ=βH⁴−3Hn alone. In contraction H<0, β>0, n>0 ⇒ 2βH³/n<0 ⇒ strictly <−6.
As H→0⁻ the correction →0⁻ and the inequality degenerates toward −6 but stays strict for every H<0; the claim is stated
"during contraction", so the H=0 endpoint is outside its scope. Shear: Ṡ=−6HS exactly (isotropic effective stress; torsion never
enters shear propagation), so d/dt ln(αn²/S)=2βH⁴/n>0 — the torsion term genuinely outruns shear in time during contraction.
The worker's "grows faster than a⁻³, not 'falls slower'" note is correct: as a decreases, the more-negative exponent wins.
The logarithmic form needs n>0; the n0=0 case is covered by the exact integral, as filed.

## ATTACK 3 — consistency with B1/B2: the reconciliation is right, and I verified the load-bearing source claim
The potential contradiction dissolves on inspection, and the reason is checkable: I read the v2 text at (37). The paper prints
"With particle production, this constancy is replaced with a relation that follows from the first equation in (34)" — and (34) is
an equation for n_f, not T. Substituting §9's n_f=h_nT³ into (34) gives exactly (37): Ṫ/T+H=βH⁴/(3h_nT³). So (37) IS (34) under
the n–T closure; B2's instruction "do not retain (37) after dropping n=h_nT³" is textually correct, and retaining (37) under (b)
would secretly re-impose the dropped closure. B3's closures (b),(c) drop only the §9 constitutive relation n=h_nT³ — a closure
choice, not a field equation — keep the field equations, the first law (14), and the number law (34), and correctly decline (37).
No printed field equation of the version inspected is violated. B1's exclusion lives entirely inside the over-determined
specialisation (a) (all three thermal relations + (14) + (34)); B3's sector is the determined complement per B2's count. The
class file's sentence "the mechanism works once a consistent closure is chosen, and the paper's own printed closure is the part
that fails" is accurate to the version bound. One caveat that is NOT a contradiction but worth recording: (b) keeps ε=h⋆T⁴ and
p=ε/3 while n runs free — thermodynamically that is a non-equilibrium gas (which is the physical point of production), and the
docs say so; no equilibrium identity is smuggled in.

## ATTACK 4 — singular vs excluded: clean
β=0 singular cells use the exact reduction (a²=3u²−δ, dt/du=−3a): for δ≥0 the continuation reaches a=0 at finite proper time with
ε=a⁻⁴→∞ — an analytically certified singularity, not an integration failure. β>0 runs have an x=12/τ=2e6 guard that RAISES
"UNRESOLVED" rather than classifying; no run reached it; no finite-density cutoff is called a singularity. Constraint defect
≤1.9e-10, tenfold tolerance refinement 1.4e-12. Excluded (X) cells: q0=1+σ−αn0²≤0 means no real strictly-collapsing H0 exists —
genuinely inadmissible. The boundary case q0=0 (H0=0) has Ḣ=κε0/3>0, so it expands from rest and never contracts; excluding it
from a theorem about contracting data is legitimate and is disclosed as "initially turning". Grid arithmetic independently
verified: X per α = 1+7+10=18 per β slice, ×6 = 108; S=118 all at β=0; each positive-β slice converts all 118 nonbouncing
admissible data (32+118=150=55+49+46 per slice). Counts match; the "not probabilities" disclaimer is present.

## ATTACK 5 — beyond/short of the algebra: three findings

FINDING 1 (moderate, filing-scope): the pre-registered class content is only partially met. `B1_PREREG` §4 declares
`B1_PRODUCTION_RESCUES` as "the bounce set is enlarged from measure-small to open, with the required β range stated and compared
with S1's own values." Two declared components: (i) "from measure-small to open" presupposes a measure-small no-production set —
B3's own §0 refutes that presupposition (the set was already open; the boundary was codimension one). The class file records that
correction, consistent with the lane doctrine that a preregistered name is kept while the physical claim is stated as actually
shown (the same doctrine the B1 referee accepted for `B1_DEGENERATE_FINE_TUNED`). (ii) "required β range stated and compared with
S1's own values" is NOT done and is not recorded as dropped: `B3_RESCUE` states the [0.001,10] range is "exploratory, not
calibrated to the paper or to microscopic production", and the class file never mentions the comparison. The proved statement
("every fixed β>0") is stronger than any threshold and is honestly scoped, but the prereg-declared comparison deliverable is
silently absent. This does not break the filed physical claim; it is an undisclosed narrowing of the declared class content and
should be noted in the class file the way §0 noted the openness error.

FINDING 2 (minor): `B3_CLASS_FILED` §3 says the bounce occurs "where the spin correction exceeds the entire ordinary density".
At the bounce αn_b²=ε_b+S_b/κ≥ε_b with EQUALITY for isotropic data (S_b=0). "Exceeds" overstates the isotropic case;
`B3_RESCUE` §4 says "≥" correctly.

FINDING 3 (minor, attribution travel): the same §3 sentence continues "which is exactly where K3 showed the four-fermion closure
is uncontrolled". Per `B1_RESULT_V2` §2, K3's threshold was computed at the DIRAC turning point (α_D=9κ/16); the fluid-row ratio
≥1 at its own bounce is a separate computation (`C1_REEXAM`), and "neither travels across rows". The substantive conjunction is
true (both computations exist), but attributing the fluid-bounce regime statement to K3 is the V1 cross-row pattern V2 corrected.
`B3_RESCUE` itself avoids it ("rescue does not make the spin-fluid closure controlled", no K3 citation).

No other travel found: nothing is asserted of the Dirac row or curved KS; the KS shear law (30) is correctly NOT imported into
the flat BI reduction (B2 discloses the BI equations as a separate reduction); the "not a proof or disproof of black-hole-universe
cosmology" hedge is present. Nothing material is shown by the algebra and withheld: bounce-radius monotonicity in β is visible in
the grid and explicitly not claimed; the relative boundary in D×[0,∞) is stated.

## Version binding
All equation claims above bind to arXiv 2007.11556v2 HTML (read as an extraction of that endpoint, 2026-09-07), which
self-identifies as the published article. I did not pass the Springer cookie handshake either; publisher-version equation identity
remains unestablished, and no absence of errata is inferred — matching the filed scope qualification.

## Bottom line
The analytic core — constraint propagation, the −6+2βH³/n scaling with correct signs, the two-stage finite-bounce proof for every
α>0 and every fixed β>0 in both closures, the singular/excluded separation, and the B1/B2 reconciliation — survives
re-derivation, re-execution, off-grid stress, and source inspection. The class stands. The three findings above are correction
notes owed to the record (prereg comparison deliverable; "exceeds"→"≥ at S_b=0"; K3 attribution), not refutations.
