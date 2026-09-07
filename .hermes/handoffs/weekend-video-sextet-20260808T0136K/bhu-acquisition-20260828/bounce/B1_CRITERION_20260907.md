# B1 C2, C3 and the criterion — 2026-09-07

**C2_FLUID=PASS; C2_DIRAC=PASS. C3_FLUID=FAIL; C3_DIRAC=FAIL.**
The overall C3 tokens require both the no-production and production checks to pass.
The separate results are **C3_FLUID_NO_PRODUCTION=PASS**, **C3_DIRAC_NO_PRODUCTION=FAIL**,
and **C3_FLUID_PRODUCTION_THERMAL=FAIL**, **C3_DIRAC_PRODUCTION_THERMAL=FAIL**.
Thus the no-production FLUID criterion below describes a consistent reduced system;
the DIRAC root is only a formal constraint root. No physical interpretation is made
for either failed production case or for the failed no-production DIRAC case.
These tokens do not revise C1 and do not file an outcome class.

The controlling document is [the pre-registration, including Amendment 1](B1_PREREG_BIANCHI_I_BOUNCE_20260907.md).
The [settled C1 record](C1_REEXAM_20260907.md) is retained. The companion
[b1_criterion.py](b1_criterion.py) runs from `bounce/` as `/usr/bin/python3 b1_criterion.py`.
It uses exact SymPy algebra and writes no files. Verified with system Python and
SymPy 1.14.0, exit status 0. C3 PASS here certifies constraint propagation for the
stated homogeneous ODE system, not a general Einstein–Cartan PDE well-posedness theorem.

## Assumptions and notation

Use signature (-+++) and proper time, with c=1, no cosmological constant, and
\(\kappa>0\). The signature is that of RMP; converting the GRG/PRD perfect-fluid
formula to this signature gives \(T_{\mu\nu}=(\rho+P)u_\mu u_\nu+Pg_{\mu\nu}\).
Here \(u^\mu u_\mu=-1\). In a rest orthonormal frame the covariant tensor is
\(\operatorname{diag}(\rho,P,P,P)\).

| Row | Total density \(\rho\) | Total pressure \(P\) | Symbolic coefficient label |
|---|---|---|---|
| FLUID | \(\epsilon-\alpha_F n^2\) | \(\epsilon/3-\alpha_F n^2\) | \(\alpha_F=\kappa\hbar^2/32\) |
| DIRAC | \(\epsilon-\alpha_D n^2\) | \(\epsilon/3+\alpha_D n^2\) | \(\alpha_D=9\kappa/16\), PRD's \(\hbar=1\) units |

All results retain \(\alpha_F\) and \(\alpha_D\) as symbols, constant in time and
positive. Comparing the printed coefficients requires common \(\hbar=1\) units.
No numerical coefficient or thermal free-gas value is selected at a bounce.
Amendment 1 supplies no independently controlled fluid interval endpoints; none
are invented here. The formulas apply pointwise for every positive constant alpha.

The following are the assumptions of this reduction, including additions that the
sources do not print as a Bianchi I model:

1. The chosen metric is diagonal Bianchi I,
   \(ds^2=-dt^2+\sum_i a_i^2 dx_i^2\), with \(a=(a_1a_2a_3)^{1/3}>0\).
   The flow is comoving, geodesic and irrotational. No tilt, curvature, heat flux,
   magnetic stress or anisotropic effective matter stress is retained.
2. Spin is eliminated algebraically before averaging. Unpolarized, locally
   isotropic spin correlations and vanishing averaged linear spin/gradient and
   polarization-current terms are assumed. Extending these matter averages into
   an anisotropic spacetime is a model assumption, not a result for every
   homogeneous microscopic spinor or polarized spin distribution.
3. The ordinary part has \(p=\epsilon/3\). For the no-production test, both
   \(\epsilon=\epsilon_0a^{-4}\) and \(n=n_0a^{-3}\), with
   \(\epsilon_0,n_0>0\), are imposed as requested. In the DIRAC row they are
   hypotheses being tested, not consequences of PRD's matter evolution.
4. \(S:=\sigma^2=\tfrac12\sum_i(H_i-H)^2\), \(H=\dot a/a\).
   The isotropic-stress spatial equations imply
   \(\dot{(H_i-H)}+3H(H_i-H)=0\), hence
   \(\dot S=-6HS\) and \(S=\Sigma^2a^{-6}\), with \(\Sigma^2\ge0\).
   This is the Bianchi I result, not the curved Kantowski–Sachs shear law.
5. The source normalization for the averaged FLUID spin square in RMP notation
   is fixed by matching the printed Weyssenhoff density correction to the printed
   GRG/PRD fluid coefficient. Specifically, RMP's \(q_F^2:=s_{\rm RMP}^2\)
   is \(\alpha_F n^2/\kappa\). This is a normalization/closure identification;
   it is not an independent interacting determination of spin correlations.
   The DIRAC averaging uses PRD's printed axial-spin square
   \(\langle s_{\rm ax}^2\rangle=3n^2/4\), solely to compare the published
   coefficient. Both coefficients remain symbolic in the dynamics.
6. For production set \(\Psi=\dot n+3Hn\). The direct test retains the same
   Einstein evolution equations and adds no creation pressure or extra stress
   tensor. GRG's thermal prescription is tested conditionally through
   \(\dot\epsilon+4H\epsilon=4\epsilon\Psi/(3n)\), without using numerical
   thermal constants. Applying that prescription to DIRAC is explicitly an
   additional trial, not a production law supplied by PRD. A number-only trial
   is also printed, so the result does not depend on concealing an energy law.

## C2: combined-source reduction, before matter evolution

The [local RMP publisher PDF](prd_publisher_verify_20260907/rmp_pdf.pdf), printed
p. 400, was read and visually checked. Equation (3.23) is
\(G^{ij}(\{\})=\kappa\bar\sigma^{ij}\); (3.24) defines
\(\bar\sigma^{ij}=\sigma^{ij}+\kappa Q^{ij}[\tau]\), with its displayed
quadratic spin contractions. The accompanying passage specifies that the combined
tensor is symmetric and Levi-Civita conserved after eliminating torsion using the
algebraic second field equation. The metric stress \(\sigma^{ij}\) in (3.24)
must include its matter-model dependence; adding only a geometric quadratic term
to an arbitrary ordinary-fluid tensor would not be this reduction.

For explicit evaluation of (3.24), use RMP's own matter-specific combined tensors
(5.18) and (5.15), both visually checked on p. 408. This avoids replacing the
Dirac current by a Weyssenhoff current. The script compares these **specialized
printed tensors**, not all components of the unrestricted (3.24) for arbitrary spin.

**FLUID.** RMP (5.16)–(5.18), with its convective spin current and the rest-frame
Frenkel restriction, gives in the stated unpolarized limit
\[
\langle\bar\sigma^{\mu\nu}\rangle_F
=(\epsilon+p-2\kappa q_F^2)u^\mu u^\nu
 +(p-\kappa q_F^2)g^{\mu\nu}.
\]
The linear polarization terms in (5.18) average to zero under assumption 2.
With \(\kappa q_F^2=\alpha_Fn^2\), the compared expression is exactly
\[
T_F^{\mu\nu}=(\epsilon+p-2\alpha_Fn^2)u^\mu u^\nu
 +(p-\alpha_Fn^2)g^{\mu\nu}.
\]
The [local PRD publisher PDF](prd_publisher_verify_20260907/prd_pdf.pdf), p. 107502-2,
paragraph immediately below (10), independently prints the fluid corrections
\(\delta\rho=\delta P=-\kappa s_{\rm phys}^2/4\) and
\(s_{\rm phys}^2=n^2/8\) in natural units. Restoring \(\hbar^2\) gives
\(-\kappa\hbar^2n^2/32\), fixing the above RMP-normalization identification
\(q_F^2=s_{\rm phys}^2/4\). Thus **C2_FLUID=PASS** in this limit.

**DIRAC.** RMP (5.13) uses the fully antisymmetric spin current; (5.15) gives
\[
\bar\sigma_{\mu\nu,D}
=\Sigma_{(\mu\nu)}(\{\})-\frac\kappa2g_{\mu\nu}
 \tau^{abc}\tau_{abc}.
\]
With the PRD axial-spin normalization, \(\tau\) is dual to
\(s_{\rm ax}/2\). In signature (-+++), for a spatial axial vector,
\(\tau^{abc}\tau_{abc}=-6s_{\rm ax}^2/4\). Accordingly,
\[
\langle\tau^{abc}\tau_{abc}\rangle=-\frac98n^2,
\qquad
-\frac\kappa2\langle\tau^2\rangle g_{\mu\nu}
=\frac{9\kappa}{16}n^2g_{\mu\nu}=\alpha_Dn^2g_{\mu\nu}.
\]
This matches PRD (9)–(10) after signature conversion. Averaging its ordinary
Levi-Civita term as a perfect fluid yields the compared expression
\[
T_{\mu\nu,D}=(\epsilon+p)u_\mu u_\nu+(p+\alpha_Dn^2)g_{\mu\nu},
\quad \rho_D=\epsilon-\alpha_Dn^2.
\]
Thus **C2_DIRAC=PASS**, with a pressure correction opposite to the fluid row.
Both 4-by-4 tensor-difference matrices printed by the code are identically zero.

For either row, the combined Einstein equation in Bianchi I gives
\[
3H^2=\kappa\rho+S,\qquad
\dot H=-H^2-\frac23 S-\frac\kappa6(\rho+3P).
\]
The second equation also follows from RMP (5.21) with convergence \(z=-3H\),
zero acceleration/vorticity, and \(E=(\rho+3P)/2\). The shear law above follows
by subtracting spatial Einstein equations. There is no further independent
torsion-shear term in this specified averaged, isotropic-stress limit. C2 is an
algebraic formalism match; the p. 400 conservation requirement is tested next.

## C3: constraint propagation

Define the constraint and energy-balance residual by
\[
\mathcal C=3H^2-\kappa(\epsilon-\alpha n^2)-S,
\qquad \mathcal E=\dot\rho+3H(\rho+P).
\]
Direct differentiation with the acceleration and shear equations, without
division by H or use of a Friedmann square-root branch, gives
\[
\boxed{\dot{\mathcal C}=-2H\mathcal C-\kappa\mathcal E},\qquad
\boxed{\mathcal R_C:=\dot{\mathcal C}+2H\mathcal C=-\kappa\mathcal E}.
\]
Thus \(\mathcal R_C\) is the constraint derivative on \(\mathcal C=0\).
It must vanish identically along the proposed evolution, not just at one event.
Writing \(J:=\dot\epsilon+4H\epsilon\) and \(\dot n=-3Hn+\Psi\) gives
\[
\mathcal E_F=J-2\alpha_F n\Psi,\qquad
\mathcal E_D=J+6H\alpha_Dn^2-2\alpha_Dn\Psi.
\]

**No production and the requested scalings:** \(\Psi=J=0\).
\[
\boxed{\mathcal R_{C,F}=0},\qquad
\boxed{\mathcal R_{C,D}=-6\kappa H\alpha_D n^2}.
\]
Therefore **C3_FLUID_NO_PRODUCTION=PASS** and
**C3_DIRAC_NO_PRODUCTION=FAIL**. Vanishing of the latter at H=0 alone does not
establish propagation. Stop physical interpretation of this DIRAC case here.
The failure is specifically of simultaneously imposing the two requested
scalings with DIRAC pressure; it does not withdraw its different C1 recovery.

The fluid ODEs for \((a,H,\epsilon,n,S)\) are smooth for finite variables and
\(a>0\); no equation is singular at H=0. Standard local ODE existence and
uniqueness, together with the homogeneous constraint equation, suffices for this
reduced control. There are no numerical trajectories or claims of microscopic
validity at high density.

**Production, number-only insertion:** retaining \(J=0\) gives
\[
\mathcal R_{C,F}=2\kappa\alpha_Fn\Psi,\qquad
\mathcal R_{C,D}=-6\kappa H\alpha_Dn^2+2\kappa\alpha_Dn\Psi.
\]
Both are generically nonzero: **C3_FLUID_PRODUCTION_NUMBER_ONLY=FAIL**,
**C3_DIRAC_PRODUCTION_NUMBER_ONLY=FAIL**. No physical interpretation follows.

**Production, GRG thermal insertion:** the formal relation
\(J=4\epsilon\Psi/(3n)\) gives
\[
\boxed{\mathcal R_{C,F}
=-\kappa\left(\frac{4\epsilon}{3n}-2\alpha_Fn\right)\Psi},
\]
\[
\boxed{\mathcal R_{C,D}
=-\kappa\left[6H\alpha_Dn^2+
 \left(\frac{4\epsilon}{3n}-2\alpha_Dn\right)\Psi\right]}.
\]
The script also prints each with \(\Psi=\beta H^4\). Neither is identically
zero. Hence **C3_FLUID_PRODUCTION_THERMAL=FAIL** and
**C3_DIRAC_PRODUCTION_THERMAL=FAIL**. Special zeros at H=0 or at a particular
density do not repair propagation on an interval. Stop physical interpretation
of both production cases here.

The missing consistency condition is explicit: retaining the printed pressures
would require \(J_F=2\alpha_Fn\Psi\) or
\(J_D=2\alpha_Dn\Psi-6H\alpha_Dn^2\). Alternatively an additional stress
sector/creation pressure would have to supply the missing energy balance. These
are necessary equations, not an adopted repair or a solved production model.
Evolving only the constraint and a chosen production law would instead imply a
different pressure; that cannot certify the original full Einstein system.

## No-production criterion and ratios

All algebra below assumes \(\epsilon_0,n_0,\kappa,\alpha_r>0\),
\(\Sigma^2\ge0\), for \(r=F,D\). For the failed DIRAC case it is only the
requested formal substitution into the constraint, not a physical bounce claim.

**FLUID:** multiplying the H=0 constraint by \(a^6>0\) gives
\[
0=\kappa\epsilon_0a^2+\Sigma^2-\kappa\alpha_Fn_0^2.
\]
Consequently the exact finite positive root criterion and root are
\[
\boxed{\kappa\alpha_Fn_0^2>\Sigma^2},\qquad
\boxed{a_{\min,F}=\sqrt{\frac{\kappa\alpha_Fn_0^2-\Sigma^2}
 {\kappa\epsilon_0}}}.
\]
Equality gives only a=0 after multiplication, outside the allowed domain, and
no finite root. Reversing the inequality gives no positive real root. At the
strict root the consistent fluid evolution gives
\(\dot H_b=\kappa\epsilon_b/3>0\), so the mean scale factor has a smooth
local minimum. This assertion concerns the mean volume, not simultaneous
minima of all three directional scale factors.

Both terms have exactly the same power:
\[
\kappa\delta\rho_F=-\kappa\alpha_Fn_0^2a^{-6},\qquad
S=\Sigma^2a^{-6}.
\]
Their ratio of magnitudes for nonzero shear is
\(\kappa\alpha_Fn_0^2/\Sigma^2\), a constant. **SCALING_DEGENERATE_FLUID=YES**:
the pre-registration's fluid scaling and constant comparison are verified within
this reduction. No conclusion about fine tuning, measure or genericity is filed.

**DIRAC, formal algebra only:** its density has the same functional form, so
\[
\boxed{\kappa\alpha_Dn_0^2>\Sigma^2},\qquad
\boxed{a_{\min,D}^{\rm formal}=\sqrt{\frac{\kappa\alpha_Dn_0^2-\Sigma^2}
 {\kappa\epsilon_0}}}.
\]
The constraint-root criterion does not differ in form. Its imposed torsion and
shear terms both scale as \(a^{-6}\): **SCALING_DEGENERATE_DIRAC=YES** for
these formal substitutions. C3 has failed, so neither this token nor the
label `A_MIN_DIRAC` certifies a dynamically attained minimum. No alternative
DIRAC evolution is solved here.

**The correction ratio, keeping the tilde distinction explicit.** K3's diagnostic
means the magnitude of the interaction correction, so define
\(R_r=|\delta\rho_r|/\epsilon=\alpha_rn^2/\epsilon\).
PRD's \(\tilde\epsilon\) is this correction; GRG's \(\tilde\epsilon\) is
the total. They cannot be substituted into the same ratio silently.
At the respective root, with \(\Delta_r:=\kappa\alpha_rn_0^2-\Sigma^2>0\),
\[
\boxed{R_F=\frac{\kappa\alpha_Fn_0^2}{\Delta_F}},\qquad
\boxed{R_D^{\rm formal}=\frac{\kappa\alpha_Dn_0^2}{\Delta_D}}.
\]
For each row,
\[
R_r=1+\frac{\Sigma^2}{\Delta_r}>1>0.1
\quad\hbox{when }\Sigma^2>0.
\]
Both exceed K3's small-correction threshold; the DIRAC statement is conditional
algebra at its formal root. The positive shear-dependent excess is derived by
substitution, but the lower bound is forced by the constraint balance
\(\alpha_rn_b^2=\epsilon_b+S_b/\kappa\). It is not an independent test
confirming a controlled closure. In flat shear-free FLUID, R=1 **by construction**
because the H=0 constraint equates ordinary density and the correction. The same
identity holds at the shear-free formal DIRAC root; this is not its C1 thermal
cusp with the different ratio 2/3.

For completeness, using GRG's tilde literally gives the different quantity
\[
\frac{|\tilde\epsilon_F|}{\epsilon_b}
=\frac{|\rho_F|}{\epsilon_b}=\frac{\Sigma^2}{\Delta_F}=R_F-1.
\]
The analogous total-density ratio for DIRAC is \(\Sigma^2/\Delta_D\).
These are not necessarily greater than 0.1: each exceeds it precisely when
\(\Sigma^2>\kappa\alpha_rn_0^2/11\), subject to the root criterion.
They vanish without shear and are not the K3 correction diagnostic.

For an unspecified allowed interval I of positive constant alpha, the criterion
holds for exactly \(I\cap(\Sigma^2/(\kappa n_0^2),\infty)\).
For a closed interval \([\alpha_-,\alpha_+]\) it holds throughout only if
\(\kappa\alpha_-n_0^2>\Sigma^2\). These are symbolic interval statements;
no K3 DIRAC interval is transferred numerically to FLUID.

## Production pivot: equations only

[GRG 53,18, (33)–(34)](https://arxiv.org/html/2007.11556v2#S0.E33)
specifies \(\Psi=\beta H^4\) and
\(\dot n+3Hn=\Psi\), \(\dot{(n^2)}+6Hn^2=2n\Psi\).
Its [thermal equations (36)–(38)](https://arxiv.org/html/2007.11556v2#S0.E36)
use \(\epsilon=h_*T^4\), \(n=h_nT^3\) and
\(\dot T/T+H=\beta H^4/(3h_nT^3)\), rewritten in (38) by factoring H.
Equation (35) compares production with the **KS** shear source in (30).
Equation numbering was checked in the linked manuscript; the existing
[source ledger](SOURCES_20260907.md) records its publisher comparison. No
claim of whole-document byte identity is added here.

For the stipulated Bianchi I shear law, define \(N(t)=na^3\). Then
\[
\dot N=a^3\Psi,\qquad
\frac{d}{dt}(\kappa\alpha_r n^2a^6)
=2\kappa\alpha_rna^6\Psi,\qquad
\frac{d}{dt}(Sa^6)=0.
\]
Thus nonzero net production over an interval breaks \(n\propto a^{-3}\) and
the constant coefficient of the torsion \(a^{-6}\) term. Under the thermal
trial it also breaks \(\epsilon\propto a^{-4}\), since
\(d(\epsilon a^4)/dt=4\epsilon a^4\Psi/(3n)\).
The formal H=0 comparison becomes
\[
0=\kappa\epsilon(t)a^6+\Sigma^2-\kappa\alpha_rN(t)^2.
\]
To cease being the original comparison of fixed constants, a proposed production
law must actually change N along the relevant history (not vanish identically
on it), while the shear coefficient remains constant; a physical model must
also satisfy the C3 energy-balance condition. A law vanishing at one event,
such as \(\beta H^4\) at H=0, need not conserve N over an interval.
During contraction, positive production means
\(d\log n/d\log a=-3+\Psi/(Hn)<-3\): n grows faster as a shrinks.
This fixes the contraction/expansion ambiguity of saying “falls slower.”

The C3 failures above preclude interpreting these trial production systems
physically. No production trajectory, rescue condition, beta range or outcome
class is computed. C5 independent critique has not been claimed.
