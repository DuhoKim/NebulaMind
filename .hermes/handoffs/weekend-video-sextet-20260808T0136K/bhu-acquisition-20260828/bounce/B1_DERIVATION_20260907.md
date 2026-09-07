# B1 — C1 recovery failure, 2026-09-07

**C1=FAIL. STOP. C2=NOT_RUN. C3=NOT_RUN.** The S1 spin-fluid system specified in the task does not recover S3's isotropic cusp under the requested reduction. The pressure corrections have opposite signs. This report contains the pre-gate derivation and failure evidence only. Per the explicit C1 stop rule, steps 3–6, the anisotropic criterion, and any assessment of pre-registration §3 are not evaluated. No outcome class is filed.

Inputs are exclusively `B1_PREREG_BIANCHI_I_BOUNCE_20260907.md` and `SOURCES_20260907.md`. All published equation references below refer to the latter's verified transcriptions: S1, *Gen. Relativ. Gravit.* **53**, 18; S3, *Phys. Rev. D* **85**, 107502 (2012). No chapter equation is used. The companion script performs symbolic differentiation, integration and simplification with SymPy; it makes no network calls or file writes.

## Explicit assumptions and model choices

These are the choices needed to construct and compare the system; the sources do not print this complete Bianchi I model. Choices transferred from a source are identified separately from the geometric extension.

1. Use units `c=1`, signature `(+---)`, proper comoving time, and no cosmological constant, consistent with the source conventions used here.
2. Replace S1's Kantowski–Sachs metric, Eq. (6), by diagonal Bianchi I, `ds²=dt²−Σᵢ aᵢ(t)²(dxᵢ)²`, with positive, twice-differentiable directional scale factors. This replacement is an added model assumption, not a solution supplied by S1.
3. Extend S1 Eq. (1) to a Levi-Civita effective Einstein equation `G^μ_ν=κ diag(ρ_eff,−p_eff,−p_eff,−p_eff)` in that geometry. Algebraic torsion effects are represented entirely by the effective source.
4. Assume spin averaging leaves isotropic pressure and no anisotropic stress, heat flux or polarization-current contribution. Choose comoving, geodesic, irrotational flow. This restricts the possible anisotropic spin sources; it does not derive a microscopic closure.
5. Carry `α∈[α₋,α₊]` as an unspecified interval, constant in time for each formal model. Constancy is an added closure assumption. No free-gas coefficient is installed at the bounce.
6. Impose local effective energy conservation. Interpret no production as `ṅ+3Hn=0`, the `β=0` specialization of S1 Eq. (34); identify the density symbol `n_f` with `n` for comparison.
7. Only for the C1 formal comparison, use the quoted thermal forms `ε=h_*T⁴`, `p=ε/3`, `n=h_nT³`, with positive, constant `h_*`, `h_n` and positive temperature. These are source-model formulas being checked, not a controlled interacting thermal calculation.
8. Compare a common symbolic correction magnitude `αn²` without identifying the two sources' different printed numerical prescriptions for α. Restrict to symbolic `α>0` when testing S3's real positive-temperature cusp. In the script this parameter is named `alpha_cusp`; it is not a selected numerical value.
9. Bianchi I has zero spatial curvature, whereas S3's published FLRW geometry has `k=1`. Also compare its flat `k=0` limit to isolate the pressure mismatch. Dropping curvature does not change the pressure sign or S3's Eq. (14) temperature relation.

## Pre-gate symbolic derivation

Write `Hᵢ=ȧᵢ/aᵢ`, `a=(a₁a₂a₃)^(1/3)`, and `H=ΣᵢHᵢ/3`. Use the shear normalization consistent with S1 Eqs. (23), (25):

\[
\sigma^2=\frac12\sum_i(H_i-H)^2,
\qquad \sum_iH_i^2=3H^2+2\sigma^2.
\]

The script constructs the Christoffel symbols from the metric, contracts the Ricci tensor, and forms the mixed Einstein tensor. Its results are

\[
R^0{}_0=-\sum_i(\dot H_i+H_i^2),\qquad
R^i{}_i=-\dot H_i-3HH_i,
\]
\[
G^0{}_0=H_1H_2+H_1H_3+H_2H_3,
\qquad
G^i{}_i=\dot H_j+\dot H_k+H_j^2+H_k^2+H_jH_k
\quad(\{i,j,k\}=\{1,2,3\}).
\]

The geometric identity `G⁰₀−(3H²−σ²)` and the sum-of-squares identity both have symbolic residual **0**. Substituting S1 Eq. (1),

\[
\rho_{\rm eff}=\epsilon-\alpha n^2,\qquad
p_{\rm eff}=p-\alpha n^2,
\]

gives the generalized Friedmann constraint

\[
\boxed{3H^2=\kappa(\epsilon-\alpha n^2)+\sigma^2.}
\]

Use `R⁰₀=κ(ρ_eff+3p_eff)/2`, consistent with S1 Eq. (9), and the sum-of-squares identity to obtain

\[
\boxed{\dot H=-H^2-\frac23\sigma^2
-\frac\kappa6(\epsilon+3p-4\alpha n^2).}
\]

This is the geodesic, zero-vorticity specialization of S1 Eq. (31) with its §7 source substitution, extended to the chosen metric. The directional equations are

\[
\dot a_i=H_i a_i,\qquad
\dot H_i+3HH_i=\frac\kappa2(\rho_{\rm eff}-p_{\rm eff})
=\frac\kappa2(\epsilon-p).
\]

Subtracting two spatial equations yields
`d(Hᵢ−Hⱼ)/dt+3H(Hᵢ−Hⱼ)=0`. Effective energy conservation is
`ρ̇_eff+3H(ρ_eff+p_eff)=0`. No anisotropic scaling criterion or constraint-propagation control is evaluated after the failed gate.

## C1 — compared expressions and failure

**The source mismatch is already present before choosing a temperature normalization.** S1 Eq. (1) gives `p_eff=p−αn²`. S3 Eq. (10) uses tildes for corrections, not totals: `ε̃=−p̃=−αn²`. Consequently its total pressure in Eq. (12) is `p+αn²`. At matched symbolic correction magnitude the difference is

\[
p_{{\rm eff},S1}-p_{{\rm eff},S3}=-2\alpha n^2.
\]

Setting shear to zero or dropping S3's curvature term cannot remove this difference. Changing the common α normalization cannot simultaneously fix pressure and preserve the matched density correction.

For clarity, independently integrate S3 Eq. (14):

\[
\frac{d\log a}{dT}=-\frac1T+\frac{3\alpha h_n^2}{2h_*}T
\quad\Longrightarrow\quad
 a_{S3}(T)=\frac{C}{T}\exp\!\left(\frac{3\alpha h_n^2T^2}{4h_*}\right),
\quad C=a_rT_r.
\]

This reproduces Eq. (15), with symbolic difference **0**. Its cusp condition gives precisely S3 Eqs. (16)–(17):

\[
T_{\rm cr}=\sqrt{\frac{2h_*}{3\alpha h_n^2}},\qquad
\left.\frac{da_{S3}}{dT}\right|_{T_{\rm cr}}=0,
\qquad
 a_{\rm cr}=C\sqrt{\frac{3e\alpha h_n^2}{2h_*}}.
\]

The derivative residual and `a_S3(T_cr)−a_cr` are both **0**. The script labels this **S3_REFERENCE_ALGEBRA=PASS**; reproducing S3 from S3's own equations is not recovery from S1.

In contrast, the two thermal continuity equations are

\[
\begin{aligned}
S1:\quad &(4h_*T^3-6\alpha h_n^2T^5)(\dot T+HT)=0,\\
S3:\quad &(4h_*T^3-6\alpha h_n^2T^5)\dot T+4h_*HT^4=0.
\end{aligned}
\]

Their left-hand-side difference is **`−6αh_n²HT⁶`**, as computed symbolically. Conserved fermion number with `n=h_nT³` fixes `Ṫ=−HT`, hence `a_S1(T)=C/T`. This number equation avoids dividing by the thermal continuity coefficient, which vanishes at `T_cr`. At S3's proposed cusp,

\[
\left.\frac{da_{S1}}{dT}\right|_{T_{\rm cr}}
=-\frac{3C\alpha h_n^2}{2h_*}\ne0,
\qquad
\frac{a_{S1}(T_{\rm cr})}{a_{\rm cr}}=e^{-1/2}\ne1.
\]

The amplitude comparison uses the same integration constant; the nonzero derivative is independent of any nonzero normalization choice. S3's thermal curve also satisfies

\[
\frac{d\log(n a_{S3}^3)}{dT}=\frac{9\alpha h_n^2T}{2h_*}\ne0,
\]

so it does not obey the conserved-number thermal relation imposed for the S1 reduction. The absence of an explicit production law in S3 does not establish that extra conservation relation for its chosen thermal source.

As an additional C1 diagnostic, the flat constraint's stationary temperature is

\[
T_{\rm st}^2=\frac{h_*}{\alpha h_n^2},\qquad
\frac{T_{\rm st}^2}{T_{\rm cr}^2}=\frac32.
\]

This matches S3's distinct Eq. (23), **not** Eq. (16). At Eq. (16), the computed ratio `αn²/ε` is **2/3**, and the flat constraint gives

\[
H^2(T_{\rm cr})=\frac{4\kappa h_*^3}{81\alpha^2h_n^4}>0
\quad(\kappa>0).
\]

Thus a smooth `H=0` turning point cannot be substituted for S3's stated cusp. The full closed S3 geometry is an additional obstruction to exact recovery by simply setting Bianchi I shear to zero; the pressure and temperature-law failures persist even in the flat comparison.

**C1=FAIL:** the requested S1 reduction does not reproduce S3 Eqs. (16)–(17) and `da/dT=0`. This is a failure of this cross-model recovery requirement. It is not a decision on the broader physics question.

## Stop receipt and α scope

`C2=NOT_RUN` and `C3=NOT_RUN`: their PASS/FAIL judgments and residuals are deliberately not manufactured after C1 fails. `CRITERION=NOT_EVALUATED_C1_FAILED`. No step-3 S4 reduction, step-4 criterion, step-5 propagation check or step-6 interval sweep is performed.

α remains an unspecified interval parameter. `SOURCES_20260907.md` §D supplies no controlled numerical interval for the interacting bounce coefficient: the quoted free-gas exchange bounds are not a replacement α interval at the bounce. Its approximately `0.32 T_cr` controlled range and two-thirds correction belong to the S3 calculation. The formal positive-α comparison above does not assert validity of either thermal closure there. The C1 mismatch persists for every finite positive α with nonzero thermal fermion density; α=0 removes the finite S3 cusp rather than recovering it.

Run from `bounce/` as `/usr/bin/python3 b1_derive.py`. Verified with SymPy 1.14.0. Expected and observed exit code: **1**, signaling the failed recovery gate. Final control tokens: **C1=FAIL, C2=NOT_RUN, C3=NOT_RUN**.
