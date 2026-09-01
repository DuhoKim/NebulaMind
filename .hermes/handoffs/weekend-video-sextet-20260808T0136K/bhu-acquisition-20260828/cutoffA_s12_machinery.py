#!/usr/bin/env python3
"""Program (A), step 1: the S_1/2 machinery, built and validated.

PROGRAM (A) -- "calibrate or kill the 60-degree causal cutoff". The decisive
question is made COMPUTABLE like this:

  The Gaztanaga causal condition Phi(chi > chi_S) = 0 (arXiv 2003.11544 Eq.16-17)
  fixes the causal SCALE and, in the source's own words, leaves "an infrared
  cutoff in the spectrum of inhomogeneities for chi > chi_S" -- with no covariance
  and no matching law. So define the ADMISSIBLE CLASS of stochastic completions:

    (i)   IR cutoff:   P(k) = 0 for k < k_S          [the causal condition]
    (ii)  positivity:  P(k) >= 0                      [it is a power spectrum]
    (iii) normalized:  P(k) = P_LCDM(k) for k > k_norm [high-l is measured, held out]

  and ask for the RANGE of S_1/2 over that class. Because C_l is LINEAR in P and
  S_1/2 is a positive-semidefinite QUADRATIC FORM in C_l, S_1/2 is a CONVEX
  quadratic functional of P, so its minimum over the (convex) admissible set is a
  convex program with a unique global optimum -- reducible to non-negative least
  squares, hence certifiable rather than argued.

  DECISION RULE, stated in advance:
    S_min >  S_Planck (~1150 uK^4)  ->  the model CANNOT produce the observed
                                        deficit: the "causal cutoff explains the
                                        low quadrupole" claim is REFUTED.
    S_min <= S_Planck               ->  the model can ACCOMMODATE but not PREDICT
                                        it: report [S_min, S_max] as the exact
                                        measure of the freedom (a no-go on
                                        calibration, quantified).
  Either branch is a result. Neither requires new data.

THIS FILE IS STEP 1 ONLY: build the S_1/2 operator and validate it. It does NOT
yet do the optimization -- no conclusion about the model is drawn here.

S_1/2 convention (Spergel et al. / WMAP):
    S_1/2 = int_{-1}^{1/2} [C(theta)]^2 d(cos theta)
    C(theta) = sum_l (2l+1)/(4pi) * C_l * P_l(cos theta)
  =>  S_1/2 = sum_{l,l'} [(2l+1)(2l'+1)/(16 pi^2)] C_l C_l' I_{l l'}
      with I_{l l'} = int_{-1}^{1/2} P_l(x) P_l'(x) dx.

I_{l l'} is computed by Gauss-Legendre quadrature on [-1, 1/2]. P_l*P_l' is a
polynomial of degree l+l', and n-point Gauss-Legendre is EXACT to degree 2n-1, so
with n > l_max this is exact to machine precision -- not an approximation.
"""

import numpy as np
from numpy.polynomial import legendre

S_PLANCK_UK4 = 1150.0        # observed, approx (1142-1209 across masks/pipelines)
LCDM_REFERENCE_UK4 = 34900.0  # INDEPENDENT reference: prior blind seats + literature


def s12_matrix(l_max):
    """M[l,l'] such that S_1/2 = C^T M C, for C indexed l = 0..l_max.

    Exact: Gauss-Legendre with (l_max+1) nodes integrates degree <= 2*l_max+1,
    and the integrand degree is at most 2*l_max.
    """
    n_nodes = l_max + 2
    # nodes/weights on [-1,1], then affine-mapped to [-1, 1/2]
    x_std, w_std = np.polynomial.legendre.leggauss(n_nodes)
    a, b = -1.0, 0.5
    x = 0.5 * (b - a) * x_std + 0.5 * (b + a)
    w = 0.5 * (b - a) * w_std

    # P_l(x) for all l at all nodes
    P = np.zeros((l_max + 1, len(x)))
    for l in range(l_max + 1):
        c = np.zeros(l + 1)
        c[l] = 1.0
        P[l] = legendre.legval(x, c)

    I = (P * w) @ P.T                       # I[l,l'] = int P_l P_l'
    l = np.arange(l_max + 1)
    pref = (2 * l + 1) / (4 * np.pi)
    M = np.outer(pref, pref) * I
    return M


def s12_from_cl(cl, M):
    """cl[l] in uK^2 (l = 0..l_max, monopole/dipole zeroed) -> S_1/2 in uK^4."""
    return float(cl @ M @ cl)


def lcdm_cl(l_max, lensed=True):
    """Planck-2018-like LCDM TT spectrum in uK^2, indexed by l (0..l_max)."""
    import camb
    pars = camb.set_params(
        H0=67.36, ombh2=0.02237, omch2=0.1200, mnu=0.06, omk=0, tau=0.0544,
        As=2.1e-9, ns=0.9649, halofit_version="mead", lmax=max(l_max + 500, 2500),
    )
    pars.set_for_lmax(max(l_max + 500, 2500), lens_potential_accuracy=1)
    results = camb.get_results(pars)
    powers = results.get_cmb_power_spectra(pars, CMB_unit="muK", raw_cl=True)
    tt = powers["total" if lensed else "unlensed_scalar"][:, 0]
    cl = np.zeros(l_max + 1)
    cl[2:l_max + 1] = tt[2:l_max + 1]     # drop monopole+dipole, as always
    return cl


def main():
    print("=" * 74)
    print("PROGRAM (A) STEP 1 — S_1/2 operator, built and validated")
    print("=" * 74)

    print("\n[1] EXACTNESS OF THE OPERATOR (internal, not physics)")
    # A polynomial identity check: for C = delta_{l,L}, S_1/2 must equal
    # ((2L+1)/4pi)^2 * int_{-1}^{1/2} P_L^2 dx, computable independently.
    ok_all = True
    for L in (2, 5, 17):
        M = s12_matrix(40)
        c = np.zeros(41)
        c[L] = 1.0
        got = s12_from_cl(c, M)
        # independent high-density Simpson evaluation of the same 1-D integral
        xs = np.linspace(-1.0, 0.5, 200001)
        cc = np.zeros(L + 1)
        cc[L] = 1.0
        pl = legendre.legval(xs, cc)
        from scipy.integrate import simpson
        want = ((2 * L + 1) / (4 * np.pi)) ** 2 * simpson(pl ** 2, x=xs)
        rel = abs(got - want) / want
        ok = rel < 1e-9
        ok_all &= ok
        print(f"    l={L:>3}: quadrature {got:.6e}  independent {want:.6e}  "
              f"rel.diff {rel:.2e}  {'OK' if ok else 'FAIL'}")
    print(f"    -> operator exact: {ok_all}")

    print("\n[2] CONVERGENCE IN l_max (is the large-angle sum saturated?)")
    prev = None
    for l_max in (10, 20, 30, 50, 80, 120):
        M = s12_matrix(l_max)
        cl = lcdm_cl(l_max)
        s = s12_from_cl(cl, M)
        delta = "" if prev is None else f"   change {100*(s-prev)/prev:+.2f}%"
        print(f"    l_max={l_max:>4}  S_1/2 = {s:10.1f} uK^4{delta}")
        prev = s

    print("\n[3] PHYSICS VALIDATION against an INDEPENDENT reference")
    print("    Reference is NOT produced by this pipeline: LCDM S_1/2 ~ 34,900 uK^4")
    print("    from the prior blind seats (codex+agy, separate CAMB runs) and the")
    print("    published literature range. This check therefore does not share its")
    print("    suspect quantity with the thing under test (register 1al).")
    l_max = 100
    M = s12_matrix(l_max)
    cl = lcdm_cl(l_max)
    s_lcdm = s12_from_cl(cl, M)
    rel = abs(s_lcdm - LCDM_REFERENCE_UK4) / LCDM_REFERENCE_UK4
    print(f"    this pipeline, LCDM   : {s_lcdm:10.1f} uK^4")
    print(f"    independent reference : {LCDM_REFERENCE_UK4:10.1f} uK^4")
    print(f"    relative difference   : {rel*100:.1f}%")
    verdict = "PASS" if rel < 0.15 else "FAIL"
    print(f"    -> {verdict} (bar: within 15%, since the reference itself varies")
    print("       with mask/pipeline/lensing convention across sources)")

    print(f"\n    observed Planck S_1/2 ~ {S_PLANCK_UK4:.0f} uK^4 "
          f"= {s_lcdm/S_PLANCK_UK4:.1f}x below this LCDM value")
    print("\n    NOT VALIDATED BY THE ABOVE, stated explicitly: that the admissible")
    print("    class in the docstring is the right formalization of the causal")
    print("    condition. That is a physics judgement for the gate seats, not")
    print("    something this arithmetic can establish.")
    print("=" * 74)


if __name__ == "__main__":
    main()
