AUDIT_HOLDS_PROSPECT

# Entry 9 deep audit — claude-seat (blind; independent of codex/agy/kimi), 2026-09-02 18:13 KST

Source read in full: `../bhu-reading-20260823/sources/1007.0587_clean.txt` (355 lines; Popławski, PLB 694, 181, 2010).
Line numbers below are line receipts into that file.

**Erratum status:** the only erratum pinned in the sources directory is `poplawski_plb690_erratum_clean.txt`, and it is
NOT the entry-9 erratum: its header reads "Erratum to 'Nonsingular Dirac particles in spacetime with torsion' [Phys.
Lett. B 690 (1) (2010) 73]", published PLB 727 (2013) 575 (erratum file lines 8-9). It corrects sentence wording and
Eq. (29) of a different paper and touches nothing in entry 9. The PLB 701, 672 erratum named in the brief is not pinned.
I do not rely on any recollection of its content. The verdict below is robust to it: no erratum-level correction can move
a 10^-70 quantity to within 67 orders of magnitude of anything measurable (see Q1), and every tier-relevant finding
(closure written in, WMAP value used as input, route without amplitude) is read directly from the pinned text.

## Q1. Ω_S = −8.6×10⁻⁷⁰ — derivation traced and recomputed

**Inputs the paper states.** Spin-fluid coefficient s² = (1/8)(ħcn)² for unpolarized fermions (line 91, Eq. 13,
attributed to Nurgaliev-Ponomariev "NP"); ε_S = −κs²/4 ∝ a⁻⁶ (line 99, Eq. 15); Ω_S = ε_S0/ε_c with
ε_c = 3H₀²/(κc²) (lines 119, 127); H₀⁻¹ = 4.4×10¹⁷ s (line 141); species = relic background neutrinos,
n = 5.6×10⁷ m⁻³ "for each type (out of 6)" (line 143). The paper then writes "Equations (13) and (15) then give
Ω_S = −8.6×10⁻⁷⁰" (lines 144-145, Eq. 23) with no intermediate step and without saying which n (per-type or total) it
inserted into Eq. (13).

**Recomputation** (CODATA ħ = 1.0546×10⁻³⁴ J s, c = 2.9979×10⁸ m/s, G = 6.6743×10⁻¹¹):
- κ = 8πG/c⁴ = 2.0766×10⁻⁴³ m/J
- ε_c = 3H₀²/(κc²) = 3×(2.2727×10⁻¹⁸ s⁻¹)²/(2.0766×10⁻⁴³ × 8.9876×10¹⁶) = 8.303×10⁻¹⁰ J/m³ (ρ_c = 9.24×10⁻²⁷ kg/m³)
- Route A, per-type n = 5.6×10⁷ m⁻³: ħcn = 1.770×10⁻¹⁸ J/m²; s² = (1.770×10⁻¹⁸)²/8 = 3.918×10⁻³⁷ J²/m⁴;
  ε_S = −κs²/4 = −2.034×10⁻⁸⁰ J/m³; **Ω_S = −2.45×10⁻⁷¹**.
- Route B, all six types summed coherently before squaring, n = 6×5.6×10⁷ = 3.36×10⁸ m⁻³: s² = 36× Route A =
  1.4105×10⁻³⁵; ε_S = −7.323×10⁻⁷⁹ J/m³; **Ω_S = −8.82×10⁻⁷⁰**.
- Route C, six types added in quadrature (independent random spins, Σ n_i²): Ω_S = 6× Route A = **−1.47×10⁻⁷⁰**.

**Finding.** The paper's −8.6×10⁻⁷⁰ is reproduced (to 3%, i.e. within rounding of H₀ and constants) only by Route B:
the six neutrino types are lumped into one number density n = 3.36×10⁸ m⁻³ and then squared. That is a choice the text
does not state (line 143 gives only the per-type value), and it is the physically least justified of the three: for
independent, randomly oriented species, the averaged spin-squared adds per species (Route C), not coherently. The
difference is a factor 6 and is immaterial to any conclusion; I flag it only because the brief asks whether any number is
misplaced. Nothing is concealed — the inputs are all on lines 91, 99, 141, 143 — but the species-summing step is silent.

**Downstream numbers, checked from Ω_S = −8.6×10⁻⁷⁰, Ω_R = 8.8×10⁻⁵, Ω = 1.002:**
a₀ = c/(H₀√(Ω−1)) = 2.95×10²⁷ m (paper 2.9×10²⁷, line 142) ✓; â_m = √(−Ω_S/Ω_R) = 3.13×10⁻³³ (line 151) ✓;
a_m = 9.2×10⁻⁶ m (line 153) ✓; Ω(√2â_m) − 1 = −4Ω_S(Ω−1)/Ω_R² = 8.88×10⁻⁶⁴ (line 165) ✓;
t = −Ω_S f(√2)/(Ω_R^{3/2}H₀) with f(√2) = 1.1478 → 5.26×10⁻⁴⁶ s (line 169) ✓; v_a/c = πΩ_R/(2√(−Ω_S(Ω−1))) =
1.05×10³² (line 180) ✓; N = (v_a/c)³ = 1.2×10⁹⁶ (line 190) ✓.
**One number does not reproduce:** line 214 gives ε_R at the minimum radius as 1.1×10¹¹⁶ J/m³. From the paper's own
Eq. (16), ε_R(â_m) = Ω_R ε_c â_m⁻⁴ = 7.31×10⁻¹⁴ × (3.13×10⁻³³)⁻⁴ = 7.7×10¹¹⁶ J/m³, a factor ~7 higher. Both values exceed
the Planck energy density c⁷/(ħG²) = 4.6×10¹¹³ J/m³, so the paper's qualitative statement ("greater than the Planck
energy density by a few orders of magnitude") survives, but the printed figure is not what its own formula yields.

**Observability.** |Ω_S| = 8.6×10⁻⁷⁰ against a CMB precision on Ω_k of ~2×10⁻³: the quantity is 4×10⁻⁶⁷ of the
best available precision, 67 orders of magnitude below detectability. Because ε_S ∝ a⁻⁶ against radiation's a⁻⁴, the
torsion term's fractional weight is Ω_S/(Ω_R â²): ~10⁻⁴⁶ at BBN (â ~ 3×10⁻¹⁰), ~10⁻⁵⁹ at recombination, ~10⁻⁶⁵ today.
It reaches order unity only at â ~ 10⁻³³, where the paper itself puts the density above Planck (line 214) — a regime in
which the classical ECKS spin-fluid treatment the whole derivation rests on (lines 56-59, 74-75) is not established.
**So yes: Ω_S is a derived number placed beyond observability at every epoch any instrument reaches; by the scheme it
cannot earn CALIBRATED-FALSIFIER, because no instrument, existing or conceivable, has a sensitivity floor it could fall
under or over.**

## Q2. Flatness and horizon "solved"

**Same construction as entry 11.** The flatness argument is Eq. (22), Ω(â) = 1 + (Ω−1)â⁴/(Ω_R â² + Ω_S) (line 135),
evaluated at the post-bounce minimum â = √2â_m to give Ω_min − 1 = −4Ω_S(Ω−1)/Ω_R² = 8.9×10⁻⁶⁴ (line 165), then the
statement that this "appears to be tuned to 1 to a precision of about 63 decimal places" arises "naturally" (lines
167, 172). This is a bounce-epoch Ω_min − 1, never propagated forward to a present-day Ω_k: line 173 says explicitly
that after the bounce Ω(â) − 1 grows "according to Ω(â) − 1 = (Ω−1)â²/Ω_R" — i.e. by the ordinary GR relation — with
the present-day value Ω−1 already sitting inside it as an input. Rewriting with line 119 (a₀H₀√(Ω−1) = c):
Ω_min − 1 = 4(−Ω_S/Ω_R²)·c²/(a₀H₀)². The 63-decimal smallness is therefore the product of two inputs, the tiny |Ω_S|
and today's small (Ω−1) (equivalently the large present curvature radius a₀ = 2.9×10²⁷ m, line 142). Had today's Ω−1
been 0.5 instead of 0.002, Ω_min − 1 would be 2×10⁻⁶¹ — still "tuned". The model maps today's flatness to a
bounce-epoch number; it does not make today's flatness generic in the way inflation claims to. The divergence of Ω at
â_m (line 163) is definitional — Ω = 1 + c²/(aH)² diverges wherever H = 0, in any bounce in any closed model — so
"rapidly decreases from infinity" (line 167) is H rising from zero, not a torsion-specific dynamical flattening. The
accelerating phase (line 183, ä > 0) spans an expansion factor of only √2 (line 171), which the paper presents as a
virtue but which is also why it cannot erase an arbitrary initial curvature.

**Closed is assumed, not derived.** k = 1 is written into the FLRW metric at line 77 ("k=1") before any dynamics;
Section III then carries the +1 through Eqs. (10)-(11) (lines 79, 81). Nowhere does the torsion mechanism select k.
The paper's own statement is "our Universe may be indeed closed" (line 140) — a report of data, not a derivation.

**Line 140 WMAP Ω = 1.002 is a selected data input, not a prediction and not a consistency check.** It is used to
compute a₀ (line 142), and it enters Eqs. (26) and (29) as the factor (Ω−1). No error bar is quoted; the WMAP7 value is
the central value of a measurement whose 1σ range (as I recall from Larson et al. 2010, ~±0.005-0.006 on Ω_total)
includes flat — a reader should verify against the pinned WMAP7 if the point is contested. The paper needs Ω > 1 for
√(Ω−1) to be real (line 119) and for the closed metric of line 77; it selects the central value that permits this. If
Ω−1 were ≤ 0 the construction would not run. That is data selection in service of an assumed closure, precisely A(a):
assumed closure is not directional.

**Horizon.** Eqs. (28)-(29) (lines 177-180) give v_a = 1.1×10³² c at √2â_m and N ≈ 10⁹⁶ causally disconnected
volumes (line 190). The claimed resolution rests on the premise "if the closed Universe was causally connected at some
instant t < 0" (line 186) — an assumption about the contracting phase, which the paper later fills with the
collapsing-star scenario (lines 222-226: "such a universe is initially causally connected"). Assumed, not derived.

## Q3. The PROSPECT route — what the paper names as testable

Quoted (lines 243-249): "Since most stars rotate, most astrophysical black holes are rotating black holes. A universe
born from a rotating black hole should inherit its preferred direction, related to the axis of rotation. Such a
preferred direction should introduce small corrections to the FLRW metric, containing the Kerr radius a = M/(mc), where
M is the angular momentum of a rotating black hole and m is its mass. These corrections could then couple to other
fields, allowing to verify whether our Universe was born in a black hole. GRS 1915+105, which is the heaviest and
fastest spinning, known stellar black hole in the Milky Way Galaxy, has a < 26 km. Lighter or slower spinning black
holes have smaller values of a. To compare, the preferred-frame parameter 2.4×10⁻¹⁹ GeV in a model for neutrino
oscillations using Lorentz violation corresponds to the length of 820 m."

What it gives: a physical origin (parent-hole spin axis), a parameter (Kerr radius a), a bound on that parameter for
one example hole (a < 26 km), and a class of comparison (preferred-frame / Lorentz-violation parameters, ref. Katori-
Kostelecký-Tayloe). What it does not give: which "other fields", which observable in our universe carries the
correction, any amplitude of that correction as a function of a, any sign or direction, any scale on the sky, any
instrument. The 26 km vs 820 m comparison is a comparison of two lengths from unrelated contexts; no mapping from a
to an observable anisotropy amplitude is written. The phrasing throughout is modal ("should inherit", "should
introduce", "could then couple"). A second, weaker route at lines 200-204 (torsion coupling to spin or to rotational
angular momentum; Gravity Probe B) is a generic torsion test, not a BHU test, and again carries no amplitude.

**Tier fit.** PROSPECT is defined in the record as "names a verification route — inherited corrections coupling to
other fields — but defines no sensitivity floor or forecast amplitude." Lines 244-246 are that sentence almost
verbatim. Against demotion to CONSISTENCY-ONLY: the paper does more than show compatibility with data — it names a
mechanism (inherited Kerr axis), a controlling parameter with a magnitude (a ≲ 26 km), and a test class; that is a
route, thin as it is. Against promotion to QUALITATIVE-DIRECTIONAL: a "preferred direction" is not a signed
direction on a named observable, and it is conjectured ("should"), not derived from the field equations Eqs. (1)-(11),
which are all isotropic (k = 1 FLRW, random spin averaging, line 74). PROSPECT is the honest bin.

## Q4. Anything else observation-facing

- **Ω_S < 0** (lines 137, 147): signed and derived — but not an observable (Q1).
- **Bounce scale**: a_m = 9×10⁻⁶ m, ε_R = 10¹¹⁶ J/m³ (super-Planckian by the paper's own admission, line 214),
  t = 5.3×10⁻⁴⁶ s. No relic, spectrum, or amplitude is derived from the bounce; the paper says nothing about
  perturbations at all (consistent with RQ-B). No experiment reaches 10¹¹⁶ J/m³.
- **Pair production "would increase Ω_S"** (line 216): direction stated, magnitude absent, and it is a mechanism for the
  bounce, not an observable.
- **Spin alignment via electroweak interactions** (lines 218-221): would make the last term of Eq. (8) nonzero,
  introducing time asymmetry, "mass production", viscosity/entropy — all qualitative, no amplitude.
- **Curvature**: no derived present-day Ω_k; closure is assumed (Q2).
- **Arrow of time** (lines 250-253): interpretive, not observation-facing.
Nothing here yields a number an experiment could reach.

## Q5. Tier consequence, argued

CALIBRATED-FALSIFIER — no: the only derived number, Ω_S = −8.6×10⁻⁷⁰, is 67 orders of magnitude below any
measurement of Ω_k, and the paper defines no threshold for any other quantity; the lane may own a missing threshold
but here the number itself is unreachable, so there is nothing to threshold.
QUALITATIVE-DIRECTIONAL — no: the one signed derived quantity (Ω_S < 0) is not an observable; the closure (k = +1,
line 77) is written into the metric and the WMAP value is selected to support it, so A(a) applies: assumed closure is
not directional; the preferred-axis route is conjectural and unsigned.
CONSISTENCY-ONLY — no: the paper names a route with a mechanism, a parameter, and a magnitude bound (lines 243-249),
which is more than consistency with data.
PROSPECT — yes: a route without a target. **AUDIT_HOLDS_PROSPECT.** Not tier-adjacent; no packet to Duho required.
For the record, two internal numerical notes that do not move the tier: (i) Ω_S is reproduced only by summing six
neutrino types coherently before squaring, a step the text does not state; (ii) line 214's ε_R = 1.1×10¹¹⁶ J/m³ does not
follow from the paper's own Eq. (16) (I get 7.7×10¹¹⁶). The entry-9 erratum (PLB 701, 672) is not pinned; the file
beside the source is the erratum of a different Popławski paper.

## Plain language

This paper says that if you add the spin of particles to Einstein's gravity, the early universe bounces instead of
starting from a point, and that this bounce explains why the universe looks flat and uniform without needing
inflation. I re-did its one real calculation: the amount of "torsion energy" in today's universe. I get the same
number the paper gets, minus 10 to the power of minus 70, but only by adding up all six kinds of neutrinos before
squaring, a step the paper doesn't spell out; done the more careful way the number is six times smaller, which
changes nothing. Either way it is about a million-trillion-trillion-trillion-trillion-trillion times too small for any
telescope or satellite to ever see, so this is not a number that could ever prove the idea wrong. The "flatness
solved" claim turns out to feed today's measured flatness in as an input and hand it back at the bounce, and the
universe being closed is assumed on page one rather than derived. The one thing the paper says could be tested — that
a universe born inside a spinning black hole would inherit a preferred direction — is a real idea but comes with no
number, no sign, and no named measurement. That is exactly what the "PROSPECT" label means: a road named, but no
destination. The label stands.
