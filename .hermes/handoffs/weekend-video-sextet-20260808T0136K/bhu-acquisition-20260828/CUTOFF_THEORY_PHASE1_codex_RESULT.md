IRREDUCIBLE_AMBIGUITY_STOCHASTIC_COMPLETION

# Phase 1 result: the causal flux condition does not determine a CMB covariance

## Executive result

The requested unique calibration does **not** follow from the stated axiom.  In the primary source, capital
\(\Phi\) is the *integrated gravitational flux/boundary term*, not the stochastic scalar potential: Eq. (16) is
\(\Phi=-\int_M\sqrt{-g}\,d^4x\,R^0{}_0\), and the imposed condition is zero flux outside the causal region
(`2003.11544_clean.txt:235,255-265`).  The text later speaks qualitatively of an infrared cutoff
(`:248-253`), but supplies neither a two-point covariance nor a finite-domain quantum state.  Thus neither R1
nor R2 is implied by the actual boundary equation.  They are extra stochastic completions.

Even granting the two readings in the brief, R1 fixes only the *support* of a covariance and R2 fixes only the
allowed eigenfunctions.  Neither fixes their shape/occupation.  Consequently there is no unique \(W(k)\),
\(C_\ell\), \(S_{1/2}\), or refutation threshold.  The representative, non-fitted computations below show the
size of the surviving ambiguity.

## R1: compact-support correlation

For a homogeneous isotropic field,

\[
 \xi_\Phi(r)={1\over2\pi^2}\int_0^\infty dk\,k^2P_\Phi(k)j_0(kr),\qquad
 P_\Phi(k)=4\pi\int_0^Ldr\,r^2\xi_\Phi(r)j_0(kr),                 \tag{1}
\]

where \(L=\chi_\S\).  The condition \(\xi(r>L)=0\) gives the second integral's upper limit, but not its
integrand.  Infinitely many positive-definite compactly supported radial covariances (with different tapers at
\(L\)) obey it.  Hence support alone is not a spectral window and is not equivalent to a sharp \(k\)-step.

There is a second precise problem with “a scale-invariant \(\xi\)”: scale invariance specifies
\(P_\Phi\propto k^{-3}\), whose real-space integral \(\int dk\,j_0(kr)/k\) is IR divergent.  Only a difference is
defined.  The most literal renormalized choice that also vanishes continuously at the edge is

\[
 \xi_L(r)=B\ln(L/r)\,\Theta(L-r).                               \tag{2}
\]

Its transform is analytic.  With \(x=kL\),

\[
 P_L(k)=4\pi B L^3\int_0^1du\,u^2\ln(1/u)j_0(xu)
       ={4\pi B\over k^3}[\operatorname{Si}(x)-\sin x],          \tag{3}
\]

so normalization to the high-\(k\) Cesaro mean gives

\[
 W_{R1}(k)={2\over\pi}[\operatorname{Si}(kL)-\sin(kL)].          \tag{4}
\]

This is positive but has order-unity, non-decaying high-\(k\) ringing because the edge is sharp.  It does not
approach one pointwise.  A smooth edge removes the ringing, but its width/profile is a new free function and
changes low \(k\).  Thus even the brief's added “truncated scale-invariant correlation” is not a unique model
compatible with a smooth small-scale power law.  Equation (4) is one literal convention, not a derived unique
prediction.

## R2: field vanishes outside a patch

For a spherical patch of radius \(L\) with a Dirichlet boundary, the regular eigenfunctions are

\[
 u_{\ell mn}({\bf x})=N_{\ell n}j_\ell(k_{\ell n}r)Y_{\ell m}(\hat x),\qquad
 k_{\ell n}={\alpha_{\ell n}\over L},\quad j_\ell(\alpha_{\ell n})=0. \tag{5}
\]

Writing \(\Phi=\sum a_{\ell mn}u_{\ell mn}\), its covariance additionally requires every
\(\langle a_{\ell mn}a^*_{\ell'm'n'}\rangle\).  The boundary fixes the \(u\)'s but not these mode occupations.
Neumann/Robin/matching conditions give different roots; patch shape, whether \(L\) is radius or diameter, and
the observer position are also unspecified.  A finite ball is not translation invariant, and an off-centre
observer is not statistically isotropic, so an exact R2 sky cannot be passed through standard homogeneous CAMB
as a scalar \(P(k)\).

For scale only, I computed two explicitly labelled continuum surrogates: retain the standard small-scale
spectrum above (i) the lowest Dirichlet radial root \(k_c=\pi/L\), or (ii) the first \(j_1\) root
\(k_c=4.493409/L\), with a 1% numerical transition.  These are not claimed as R2 derivations; their disagreement
quantifies just one boundary/mode-sector choice before occupation freedom is even varied.

## Non-circular normalization and CAMB propagation

I used \(L=3.15c/H_0=14019.392\) Mpc (the source gives \(3.149\pm0.006\,c/H_0\) at
`2003.11544_clean.txt:332-346`), \(A_s=2.100549\times10^{-9}\), \(n_s=0.9649\), and pivot
\(0.05\,\mathrm{Mpc}^{-1}\), with Planck-like \(H_0=67.36\), \(\omega_b=0.02237\),
\(\omega_c=0.1200\), \(\tau=0.0544\), and \(\sum m_\nu=0.06\) eV.  These amplitude/tilt parameters are fixed by
\(\ell\simeq200\)--2500, not by \(C_2,C_3\), the \(\theta>60^\circ\) correlation, or \(S_{1/2}\).  Therefore the
normalization is non-circular with respect to the anomaly under test.  R1's unavoidable high-k ringing is why
I state the Cesaro-mean convention explicitly rather than fitting its phase to data.

CAMB 1.6.0 propagated each primordial table through the full scalar temperature transfer, with recombination,
reionization, late-time ISW and lensing enabled.  In particular, this is **not** a Sachs--Wolfe-only
calculation.  ISW is part of the coherent total transfer (including cross terms), so it should not be added as
an independent positive \(C_\ell\).  This implements the source's warning that late ISW/lensing add large-angle
correlations (`2003.11544_clean.txt:429-435`).

I evaluated

\[
 C(\mu)=\sum_{\ell=2}^{300}{2\ell+1\over4\pi}C_\ell P_\ell(\mu),\qquad
 S_{1/2}=\int_{-1}^{1/2}d\mu\,C(\mu)^2                         \tag{6}
\]

with 1600-point Gauss--Legendre quadrature.  The complete executable is `cutoff_phase1_camb.py`; it constructs
the spline tables and calls `get_lensed_scalar_cls(..., raw_cl=True, CMB_unit='muK')`.  Run:

```sh
python3 cutoff_phase1_camb.py
```

Numerical results (\(C_\ell\) are raw \(\mu\mathrm K^2\), not \(D_\ell\)):

| model/completion | \(S_{1/2}\,[\mu\mathrm K^4]\) | \(C_2\,[\mu\mathrm K^2]\) | \(C_3\,[\mu\mathrm K^2]\) |
|---|---:|---:|---:|
| standard \(\Lambda\)CDM | 34,940 | 1,071.1 | 507.2 |
| R1 literal log truncation, Eq. (4) | 22,327 | 897.4 | 570.2 |
| R2 surrogate, \(k_c=\pi/L\) | 14,002 | 710.3 | 448.9 |
| R2 surrogate, \(k_c=4.493409/L\) | 6,230 | 499.4 | 286.9 |

An earlier 2x-accuracy/12,000-k-node run gave \(S_{1/2}=34904\) (LCDM) and 22273 (R1), changes of 0.10% and
0.24%, respectively.  The displayed production run uses 2,000 nodes; the R2 transition width is 1% of \(k_c\).

## Three-way comparison and verdict

Planck 2018 reports TT \(S_{1/2}=1209.2,1156.6,1146.2,1142.4\,\mu\mathrm K^4\) for Commander, NILC, SEVEM,
and SMICA, respectively, and a greater-than-99.9% low-tail significance under its fiducial LCDM simulations
(`1906.02552v2_planck2018_isotropy_clean.txt:2416-2434`).  Thus the requested shorthand \(\simeq1150\) is
reproduced by the source table, while this pipeline reproduces the brief's LCDM benchmark \(\simeq34,900\).
Relative to 1150, the representative predictions are factors 30.4 (LCDM), 19.4 (literal R1), 12.2 (R2-\(\pi\)),
and 5.42 (R2-4.493) larger.  I do not quote a “sigma” for the theory means: that requires a fully specified
ensemble/covariance, precisely the missing stochastic completion, and converting the Planck LCDM tail into a
Gaussian sigma would be unjustified.

The irreducible input is therefore **the stochastic completion**: for R1, the interior covariance/edge taper
(and IR renormalization); for R2, geometry, boundary/matching condition, observer position, and eigenmode
occupation.  The source itself concedes that patch differences are impossible to quantify without an initial-
condition model (`2003.11544_clean.txt:463-466`).  No single Planck-test threshold follows.  A future completion
would be refuted by its preregistered ensemble p-value for the observed \(S_{1/2}\), \(C_2\), and \(C_3\); choosing
that completion after seeing the deficit would be the forbidden circular fit.

Absence audit: I searched the primary paper for `correl|cutoff|Phi|potential|ISW|lensing|causal`.  It gives the
flux condition and qualitative IR language, but no stochastic two-point kernel, edge taper, eigenmode
occupation, or CAMB-ready transfer.  One easy-to-miss class was finite-domain matching: the paper mentions that
different regions “could be matched” (`:248-253`) but specifies no matching law.  I therefore did not promote
either representative completion or change any tier.
