AUDIT_HOLDS_CONSISTENCY_ONLY

## 1. Mechanism and borrowed closures

The microscopic torsion elimination is genuinely carried out.  The Cartan equation is algebraic (lines 29–41); for a minimally coupled Dirac field the paper derives the axial spin tensor and contortion (4)–(5), then obtains the combined source (9), including the local four-fermion/axial-spin term (lines 70–108).  Kerlick [6] and the author's earlier Hehl–Datta derivation [7] are explicitly credited at lines 102–108, so even this algebra is not first derived here, although it is reproduced.

This is **not** the Papapetrou/Weyssenhoff closure used in the spin-fluid papers.  The paper contrasts that closure, `s_ijk=s_ij u_k`, and its `s^2=n^2/8`, negative stiff component `rho_tilde=p_tilde=-kappa s^2/4`, citing Hehl–von der Heyde–Kerlick and Nurgaliev/Gasperini [8,9] (lines 119–125).  It says the spin-fluid particle approximation comes from multipole-expanded conservation laws [13], is not self-consistent for Dirac fields [4], and violates the cosmological principle [14] (lines 126–129).  Instead it retains the completely antisymmetric Dirac tensor, citing [2,6,12,15] (lines 125–133).

The cosmological closure is nevertheless borrowed/assumed in several distinct steps:

- The GR part of the Dirac stress tensor is *macroscopically averaged* as a perfect fluid, and the squared spatial axial spin is set to `<s^2>=3n^2/4` (lines 109–117).  This produces `rho_tilde=-p_tilde=-alpha n^2`, `alpha=9 kappa/16`: a negative energy density but positive pressure, unlike the negative stiff spin fluid.
- A closed FLRW background with `k=+1` is assumed “as in [16]” (lines 134–138), not dynamically selected.  Thus positive curvature is an input.
- Ultrarelativistic kinetic equilibrium is assumed “as in [17]”, with textbook thermodynamics from [18]: `rho=h_* T^4`, `p=rho/3`, `n=h_n T^3`, and constant effective degrees of freedom over the relevant interval (lines 152–168).  Consequently the torsion term is proportional to `n^2`, hence to `T^6`; it is not simply `a^-6` because integrating conservation gives `a(T)=(a_r T_r/T) exp(3 alpha h_n^2 T^2/4h_*)` (13)–(15), lines 144–176.  Only at `T << T_cr` does `aT=constant`, so only there does the term scale approximately as `a^-6` (lines 193–194).

Accordingly, the paper derives the Dirac-specific local source but does not derive the macroscopic ensemble average, equilibrium distribution, fixed particle content, or FLRW closure from the spinor dynamics.  It does not derive the spin-fluid closure borrowed by entry 9; it explicitly replaces and criticizes it.

## 2. The cusp

Within the paper's reduced thermodynamic model, the cusp is imposed by branch selection, not obtained as a smooth solution through a stationary point.  Equation (15) has a minimum in `a(T)` at `T_cr` (lines 177–193).  Equation (19) restricts `T<=T_cr`; the parameter is then declared to jump from `-eta_cr` to `+eta_cr` at `t=0` (lines 218–250).  The paper explicitly finds that the formal stationary temperature is `T_st>T_cr`, so the universe never reaches `dot a=0`; instead `dot a` jumps from `-v` to `+v` (lines 273–301).  Restoring the dropped `k=1` in (18) would change `v^2` by only 1 for the quoted enormous `v`, so that omission does not by itself smooth the cusp.  The cusp depends more fundamentally on the perfect-fluid/equilibrium relations and constant `g_*`,`g_n` used to create the nonmonotonic `a(T)` and on grafting the two allowed branches together.

No microphysical transition, varying-degree-of-freedom calculation, finite-duration layer, junction stress, or other regulator is supplied.  More sharply, an instantaneous finite jump in `dot a` makes `ddot a` distributional, while the right side of the printed second Friedmann equation (12) contains only finite equilibrium `p+alpha n^2`.  The paper therefore does not demonstrate that the grafted cusp satisfies its own full field equations in a distributional sense.  Its statement that the bounce is “nonsingular (with respect to curvature)” (lines 260–265) is not established by the displayed cusp: a jump in extrinsic curvature normally contributes a delta-function curvature unless a surface layer/matching prescription is provided.

The only crossing discussion is for the homogeneous congruence: `theta=3 dot a/a` jumps, and the author asserts that this prevents focusing and guarantees continuation of timelike geodesics (lines 318–340).  There is no perturbation action, scalar/tensor mode equation, junction condition, vacuum choice, transfer matrix, or spectrum.  Thus the paper does not address transmission or matching of perturbations across the cusp, and no observable can safely be propagated through it from this calculation.

## 3. Numbers and recomputation

The numerical inputs printed are standard-model `g_b=28`, `g_f=90` (lines 341–343), hence `g_*=28+(7/8)90=106.75` and `g_n=(3/4)90=67.5`; `T_r=T_eq=0.75 eV`, `a_0=2.9e27 m`, and `z_eq=3200`, with `a_r=a_eq=a_0/(1+z_eq)` (lines 344–348).  The printed outputs are `T_cr=0.78 m_P`, `a_cr=5.9e-4 m`, `v_ant=8.9e34`, and `Omega_cr=1+1.3e-70` (lines 341–354).  No bounce density or e-fold count is printed.

Using the paper's reduced-Planck convention `kappa=m_P^-2` (lines 70–72),

`h_*=pi^2 g_*/30=35.1193`, `h_n=zeta(3)g_n/pi^2=8.22108`, and `alpha=9/(16m_P^2)`.

Equation (16) then gives

`T_cr/m_P = sqrt[2h_*/(3(9/16)h_n^2)] = 0.78476`,

confirming (28).  At that temperature the ordinary radiation density and number density are

`rho_cr=h_* T_cr^4=13.3197 m_P^4`, `n_cr=h_n T_cr^3=3.97320 m_P^3`.

The torsion subtraction is `alpha n_cr^2=8.87982 m_P^4=(2/3)rho_cr`, leaving the Friedmann-source density `rho_eff,cr=4.43991 m_P^4`.  These very super-Planckian densities expose an unquantified regime-of-validity issue; the paper prints none of these density values or a quantum-gravity error estimate.

For the length, `a_r=2.9e27/3201=9.0597e23 m`.  Taking the stated reduced Planck mass `m_P=2.435e27 eV`, equation (17) yields `a_cr=5.8625e-4 m`, confirming (29).  The associated expansion ratios are `a_r/a_cr=1.545e27` (`62.60` logarithmic e-folds) and `a_0/a_cr=4.947e30` (`70.68` e-folds); these are recomputed, not printed.

The last two printed outputs do **not** follow consistently from the printed inputs.  With `hbar c=1.97327e-7 eV m`, `a_r T_r=3.4434e30` in natural units.  Equation (24) gives `v=8.8008e30`, hence `v_ant=pi v=2.7649e31`, and equation (25) gives `Omega_cr-1=1/v^2=1.2911e-62`.  The paper's `8.9e34` and `1.3e-70` are approximately what results from inserting the temperature's kelvin numerical value while otherwise treating it as eV (an extra factor near `1.16e4`, squared in `Omega-1`).  No conversion convention capable of reconciling that mixture is stated.  On the paper's printed `v_ant`, its causal-volume estimate `N~v_ant^3` would be about `7.0e104`; using the dimensionally consistent recomputation gives about `2.1e94`.  In either case no observational threshold is attached.

## 4. Observation-facing content

Lines 53–56 offer the stated low-density consistency argument: torsion is important only near the Cartan density, vanishes in vacuum, and below that density ECSK reproduces GR, so existing GR tests are passed.  Beyond it, the paper claims solutions of the flatness and horizon problems (lines 353–378), but these are background-model interpretations, not derived observables: `k=+1` was assumed, not predicted; the tiny `Omega_cr-1` inherits the externally normalized `a_r T_r` and is numerically inconsistent as printed; and the causal-volume count has no perturbative or observational map.  There is no relic abundance, signed observable deviation, spectral tilt/amplitude, tensor prediction, non-Gaussianity, or data likelihood.  The `Omega-1 ~ T^-2` background scaling (lines 302–317) is conditional on the assumed closed FLRW solution and is not a derived sign under rule A(a).

## 5. Tier consequence

**Hold CONSISTENCY-ONLY.**  The paper does reproduce a Dirac-torsion background mechanism and argues recovery of GR at low density.  It does not derive positive curvature, a perturbation spectrum, cusp matching, a relic, or any other observation-facing signed direction.  Its numerical background outputs have neither an observational threshold nor, for `v_ant` and `Omega_cr`, consistent arithmetic from the stated inputs.  A lane may supply a missing threshold but not repair missing observable numbers or missing propagation physics; therefore neither QUALITATIVE-DIRECTIONAL, PROSPECT, nor CALIBRATED-FALSIFIER is supported.

In plain language: this paper shows how a Dirac spinor's torsion interaction can generate a negative high-density term and, after several cosmological averaging assumptions, prevent the scale factor from reaching zero.  But its “bounce” is a sharp splice with an unexplained jump in expansion rate, and it never shows how fluctuations cross that splice.  Spatial closure is assumed, the most dramatic velocity/flatness numbers contain a unit inconsistency, and there is no measurable prediction with a comparison threshold.  It therefore remains useful as a background consistency mechanism, not as an observational discriminator.
