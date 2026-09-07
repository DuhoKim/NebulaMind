Shear can sort spins by particle momentum without aligning the spins of an entire fluid cell. A local application of the leading published shear response to homogeneous Kantowski–Sachs (KS) collapse gives precisely this cancellation under a symmetric momentum distribution. It therefore supplies **neither a justified numerical correction to Popławski’s spin-fluid source nor a demonstrated contradiction of it**. The unresolved quantity is the stress and spin-density correlation response of the actual matter. KS symmetry allows anisotropy in those quantities but does not determine its size.

**B8 · 2026-09-07 · Weyssenhoff FLUID only · single-worker assessment, not independently reviewed.** This supplements [B5](../B5_VALIDITY_20260907.md), its [Kimi challenge](../KIMI_B5_CHALLENGE_20260907.md), and [B6](../B6_APPLICABILITY_20260907.md). Their findings remain unchanged. The target is the curved metric in [Popławski, GRG 53, 18 (2021), Eqs. (1), (6), (10)](https://doi.org/10.1007/s10714-021-02790-7), inspected in the saved publisher HTML. No B7 result was consulted. Microscopic fermion-spin results below do not import the separate Dirac gravitational row.

**Which average matters.** Momentum-resolved polarization \(\mathcal P_i(p)\), the conditional first spin moment at fixed momentum, differs from its particle-weighted cell average. For the coarse-grained spin-density pseudovector \(s_i\), distinguish

\[
M_i=\langle s_i\rangle,\qquad
C_{ij}=\tfrac12\langle s_i s_j+s_j s_i\rangle,\qquad
C_{\langle ij\rangle}=C_{ij}-\delta_{ij}C_{kk}/3.
\]

The effective anisotropic stress is another object, \(\pi_{ij}=T^{\rm eff}_{\hat i\hat j}-\delta_{ij}T^{\rm eff}_{\hat k\hat k}/3\). It includes momentum transport, interaction and spin terms; it is not determined by \(M_i\), or by squaring \(\mathcal P_i(p)\).

The source’s random-spin interpretation requires a justified isotropic correlation reduction and scalar relation giving \(\tilde\epsilon=\epsilon-\alpha n_f^2\), \(\tilde p=p-\alpha n_f^2\). Its dynamical requirement is negligible effective heat flux and anisotropic stress, including discarded spin-gradient and spin–flow correlations. In the *already assumed* Weyssenhoff constitutive tensor, the quadratic term is scalar even before averaging; an anisotropic \(C_{ij}\) is therefore not automatically a new stress term. One must derive its contribution in a matched microscopic description. Zero mean or zero vorticity alone establishes neither that matching nor isotropic momentum stress. [Brechet–Hobson–Lasenby (BHL), Eqs. (8)–(13), (30)–(32)](https://infoscience.epfl.ch/server/api/core/bitstreams/66a4adbd-9c64-44ae-98ec-b323e021bc76/content).

There is an additional quantum distinction: a single spin-1/2 particle’s symmetrized *rest-spin operator* product is \(\hbar^2\delta_{ij}/4\), irrespective of polarization. That identity does not fix the spatially coarse-grained density correlator, which includes pair correlations and the chosen relativistic spin observable. Replacing that correlator by products of polarization vectors would silently introduce a closure.

**What KS actually fixes.** Use a comoving orthonormal frame, positive Euclidean spatial indices, and \(c=\hbar=k_B=1\). Set

\[
H_X=\dot X/X,\quad H_Y=\dot Y/Y,\quad
H=(H_X+2H_Y)/3,\quad \Delta=H_X-H_Y,\quad K=Y^{-2},
\]
\[
\sigma_{ij}=\operatorname{diag}(2\Delta/3,-\Delta/3,-\Delta/3),
\qquad \sigma^2=\Delta^2/3.
\]

The connected spatial isometries leave rotations about the local radial direction \(e\). Requiring \(RM=M\), \(RCR^T=C\) for every such rotation gives

\[
M_i=M_\parallel e_i,\quad
C_{ij}=C_\perp\delta_{ij}+(C_\parallel-C_\perp)e_i e_j,
\quad \pi_{ij}=\Pi(e_i e_j-\delta_{ij}/3),
\]

where \(\Pi=P_\parallel-P_\perp\), and coefficients depend only on time. Tangential means, mixed components and unequal tangential diagonal components are excluded. Equality of radial and tangential variances or pressures is **not** required. Connected KS symmetry permits a radial axial mean. If the matter also inherits a sphere reflection, for example \(\varphi\mapsto-\varphi\), axial transformation \(M\mapsto\det(R)RM\) forces that mean to vanish. This is an additional discrete-symmetry assumption; spatial parity by itself does not forbid an axial vector. Symmetry permits radial heat flux, but this comoving diagonal metric requires its *total effective* value to vanish through the \(0r\) field equation.

**A local transfer that can be checked.** For homogeneous \(T(t)\), \(b_\mu=u_\mu/T\) obeys \(\nabla_{[\mu}b_{\nu]}=0\), since \(b=dt/T\). Acceleration and vorticity vanish, but thermal shear does not:

\[
\xi_{\hat\mu\hat\nu}=\nabla_{(\hat\mu}b_{\hat\nu)}
=\operatorname{diag}(-\dot T/T^2,-H_X/T,-H_Y/T,-H_Y/T).
\]

This is an exact Levi-Civita kinematic statement. Transferring a flat-space response to a locally inertial cell remains an **approximation**, not an EC kinetic derivation.

Liu–Yin’s axial Wigner function has a shear term proportional to \(\epsilon^{ijk}Q_{j\ell}(p)\sigma_{\ell k}\), with \(Q_{ij}=\hat p_i\hat p_j-\delta_{ij}/3\). Its one-loop coefficient, Eq. (5.2), is \(g_\sigma=(|\mathbf p|^2/E^2)E[-\partial_E f]=|\mathbf p|^2f(1-f)/(ET)\) for the Fermi distribution. This is a phase-space response coefficient, not a stress or relaxation coefficient. The calculation isolates shear about an isotropic, parity-invariant reference state; a separate initial spin potential or axial density is not excluded by this test. In a comoving local hypersurface prescription, Becattini–Buzzegoli–Palermo’s (BBP) Eq. (23) has the same angular structure: temperature time derivatives and isotropic expansion cancel in the Levi-Civita contraction. Normalizations and observables must still be matched. Factoring out a momentum-magnitude-dependent coefficient, either angular structure reduces, up to sign convention, to

\[
v=\hat p\times(\sigma\hat p)
=\Delta(0,\hat p_r\hat p_\varphi,-\hat p_r\hat p_\vartheta).
\]

Thus \(\langle v\rangle_\Omega=0\). In fact any axisymmetric scalar momentum weight preserves this cancellation by the azimuthal integral. Under isotropic angular weighting,

\[
\langle v_i v_j\rangle_\Omega={\Delta^2\over15}\operatorname{diag}(0,1,1),
\qquad \langle v_\vartheta\hat p_r\hat p_\varphi\rangle_\Omega=\Delta/15.
\]

These demonstrate hidden angular structure despite a zero mean. The first expression is the product of the *mean-response pattern*, **not** the physical \(C_{ij}\); it supplies neither a stress coefficient nor proof that spin-density anisotropy begins at second order. Symmetry also permits a linear tensor response \(\delta C_{\langle ij\rangle}\propto\sigma_{ij}\). The isotropic-background cancellation is explicitly stated by [Liu–Yin, §2, Eqs. (2.3), (2.7)–(2.9)](https://doi.org/10.1007/JHEP07(2021)188); the axisymmetric specialization above is this worker’s calculation.

**A second, conditional check prevents overclaiming.** BHL’s unaveraged tensor contains \(-2\sigma_{(\mu}{}^\lambda S_{\nu)\lambda}\) and \(-2u_{(\mu}D^\lambda S_{\nu)\lambda}\). For a homogeneous radial mean, only \(S_{\hat\vartheta\hat\varphi}\) survives. Equal tangential shear eigenvalues make the first term zero. The second vanishes because \(S_{\vartheta\varphi}=M_\parallel Y^2\sin\vartheta\) is proportional to the covariantly constant sphere area form on each spatial slice. Consequently even this permitted nonzero mean does not necessarily generate effective anisotropic stress in the assumed Weyssenhoff model.

BHL Eq. (52) also gives \(\dot s_i+3Hs_i=0\) in a parallel-transported comoving tetrad. Without creation or extra microscopic torques, every component scales as \((XY^2)^{-1}\): an initially isotropic ensemble remains isotropic under that *postulated transport*. It contains no calculation of shear-induced kinetic response. Popławski’s number-production Eq. (34) supplies no spin-resolved injection or correlation law, so this conditional preservation cannot simply be extended to his producing medium.

**Evidence and transfer checks.** Publisher copies were read at the indicated equations; custody and exact access details are in [SOURCE_ACCESS_NOTES.md](SOURCE_ACCESS_NOTES.md).

| Proposed transfer | Primary result and regime | Required KS check | Status |
|---|---|---|---|
| Random-spin perfect-fluid reduction | BHL (2008), Eqs. (12), (30)–(32), (52); Frenkel Weyssenhoff medium, no acceleration/vorticity, assumed averaging | Scalar variance relation, ordinary pressure isotropy, surviving mixed correlations; spin production law | Algebraic cancellations checked; microscopic validity unestablished |
| Thermal-shear particle polarization | [BBP (2021), Eqs. (10), (12), (23)–(24)](https://doi.org/10.1016/j.physletb.2021.136519); first-gradient LTE, free/quasi-free particles, specified hypersurface | Correlation-scale separation; local comoving surface versus freeze-out observable; species/mass and torsion matching | Angular form conditional; no transferable numerical coefficient established |
| Local shear quadrupole | Liu–Yin (2021), Eqs. (2.7), (3.8), (3.11), (5.2); hydrodynamic gradients and one-loop weak-coupling coefficient | Slow local deformation, energy/rate hierarchy, covariant Wigner definition and stress mapping | Mean cancellation checked; KS coefficient and stress unestablished |
| Choice of spin/stress variables | [Buzzegoli (2022), Eqs. (39)–(43), §VI](https://doi.org/10.1103/PhysRevC.105.044907); free-field, first-gradient LTE | Match statistical state, spin potential, spin current and gravitational coupling | No universal insertion justified; Eq. (43) cancels the BBP shear term in GLW/HW LTE constructions |

The last result concerns different local-equilibrium constructions, not permission to change a fixed physical state’s predictions arbitrarily. It makes matching the microscopic stress/spin current to the EC source essential. None of these calculations supplies a spin-torsion-dominated KS closure or relaxation coefficient.

**Quantitative conditions and the B7 interface.** A diagnostic hierarchy, not a newly adopted closure, is

\[
\max(n_f^{-1/3},\ell_{\rm corr},\ell_{\rm mfp})\ll L_{\rm cell}
\ll\min(L_{\rm matter},L_R),\qquad L_R^{-2}=\max|R_{\hat a\hat b\hat c\hat d}|.
\]

The first-gradient expansion requires small \(|H_X|/T,|H_Y|/T,|\dot T|/T^2\), small changes across correlation lengths, and slow variation of these rates. For hydrodynamic equilibration, \(\tau_R\Omega\ll1\); integrating spin relaxation out additionally requires \(\tau_s\Omega\ll1\). Here \(\Omega\) must cover directional deformation, thermal/chemical evolution, fractional production \(|\Psi|/n_f\), and driving frequencies—not merely \(|H|\). Liu–Yin’s coefficient extraction further assumes \(E_{\rm qp}\gg\tau_R^{-1}\gg\Omega\) in the hydrodynamic application, and separates slow and fast limits in its Kubo construction. Their §3 discusses Wigner covariance explicitly; replacing partial derivatives with covariant ones alone is not a full curved-space derivation. Fast relaxation would establish approach to a local response, not its vanishing.

Missing inputs are species-resolved distributions, chemical/spin potentials, spin correlations and their lengths, collision/spin relaxation spectra, spin-resolved production, and the EC-matched effective-stress response. Strong spin backreaction also requires checking interaction corrections to the free/quasi-free calculation. A future B7 output could supply \(X,Y,T,n_f,H_X,H_Y,\dot H_X,\dot H_Y,\dot T,\Psi/n_f\) along its stated trajectory to evaluate the geometric side of these conditions. At \(H=0\), finite \(\Delta\), \(K\), and evolution rates still matter. No B7 computation was duplicated or awaited.

There is an exact place for any measured correction: replacing the common pressure in GRG Eq. (10) by directional effective pressures and subtracting gives

\[
\boxed{\dot\Delta+3H\Delta=K+\kappa\Pi},\qquad
\dot\sigma^2+6H\sigma^2={2\Delta\over3}(K+\kappa\Pi).
\]

This preserves KS curvature. A small correction requires controlling \(\kappa\Pi\) against the actual finite evolution terms and its accumulated effect, especially near cancellations; a polarization percentage alone is insufficient. [ks_spin_checks.py](ks_spin_checks.py) verifies the geometry, symmetry, angular integrals, Weyssenhoff cancellations and Einstein-tensor subtraction symbolically; [its output](ks_spin_checks.txt) records all assertions passing.

**Narrow conclusion.** The inspected literature establishes a conditional momentum-space response, not net alignment or a quantitative failure of the KS scalar spin-fluid source. The smallest next calculation is **one local, EC-matched shear-response calculation of \(\Pi\)** for the specified matter state, retaining the connected spin-density correlators: extract \(\delta\Pi(\omega)/\delta\Delta(\omega)\), its relaxation range and approximation error. This directly tests the missing stress term above. If small-gradient conditions fail, the same local test must use finite-rate driving; its linear limit cannot certify the collapse. Until that response and its regime are known, both a negligible correction and a dynamically important one remain unestablished.
