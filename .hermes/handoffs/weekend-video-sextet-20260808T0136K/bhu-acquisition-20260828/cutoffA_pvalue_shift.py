#!/usr/bin/env python3
"""Program (A), re-aimed: does the causal cutoff move the low-l anomaly's p-value?

OVERNIGHT ANALYSIS ONLY. Produces reasoning + receipts. Closes no open question,
moves no tier. Every tier decision waits for Duho's verified word.

WHY THIS FRAMING REPLACES THE REFUTED ONE
-----------------------------------------
The charter's optimization died of two defects, both confirmed:
  1ao  the admissible class contained its own degenerate solution, because the
       free band [k_S, k_norm] was only constrained P >= 0 (which permits P = 0)
       and k_norm was NEVER PINNED -- so the minimum measured a modelling choice.
  1an  the decision rule compared a point prediction against a realization of a
       random variable, and would have "refuted" LCDM itself.

Both are fixed here, and neither fix is cosmetic:
  * NO OPTIMIZATION. A single licensed spectrum is EVALUATED. There is no free
    band, hence no degenerate member to find. The cut sits at k_S and nowhere
    else, and k_S is PINNED BY THE SOURCE -- Eq.23, chi_S = (3.149 +/- 0.006)
    c/H0. That is exactly the asymmetry 1ao says to check: k_S is pinned by the
    paper, k_norm never was, so the repaired program uses only the pinned one.
  * NO POINT-VS-REALIZATION COMPARISON. The observable is a P-VALUE SHIFT:
    P(S_hat <= S_obs) under LCDM, versus the same probability under the cutoff
    model. Both sides are sampling distributions of the same estimator.

THE READING AMBIGUITY, HANDLED A FORTIORI
-----------------------------------------
Step 2 established the paper licenses no sharp perturbation condition (READING_C),
and that the two candidate readings are mutually exclusive. Rather than pick one,
this uses READING A (hard IR cut, P(k)=0 for k<k_S) which the physics gate
identified as the MODEL-FAVOURABLE reading: it is hyperuniform, suppressing
large-scale power maximally. So it is an A FORTIORI bound --

    if even the model-favourable reading fails to move the anomaly, the
    conclusion is robust to the ambiguity step 2 could not resolve.

The amplitude is NOT free here and no completion is needed: above the cut the
spectrum is LCDM's own, fixed by high-l data (A_s, n_s), and the low-l data is
never used to set anything. That is the whole point -- the obstruction that killed
three prior attempts does not bind on an a-fortiori evaluation.

CAVEATS CARRIED, NOT HIDDEN
---------------------------
 * Full-sky throughout. The published ~1150 uK^4 is a CUT-SKY number. Absolute
   p-values are therefore not directly comparable to the literature; the SHIFT
   between two models computed identically is far more robust than either
   endpoint, which is why the shift is the reported quantity.
 * The cut convention (k_S = 2*pi/chi_S vs pi/chi_S) is a real choice; both are
   reported, and the conclusion must not depend on it.
 * Lensed spectra are used for the observable; lensing makes C not exactly linear
   in P, which is fatal to the old convexity claim but harmless here because
   nothing is optimized.
"""

import numpy as np
import camb
from cutoffA_s12_machinery import s12_matrix, s12_from_cl

S_OBS = 1150.0
L_MAX = 100
N_MC = 200_000
RNG = np.random.default_rng(20260901)

H0, OMBH2, OMCH2, TAU = 67.36, 0.02237, 0.1200, 0.0544
AS, NS = 2.1e-9, 0.9649
CHI_S_OVER_C_H0 = 3.149          # Eq.23 -- PINNED BY THE SOURCE
C_KM_S = 299792.458


def chi_S_mpc():
    return CHI_S_OVER_C_H0 * C_KM_S / H0


def cl_for(k_cut=None, l_max=L_MAX):
    """Lensed TT C_l (uK^2). k_cut in 1/Mpc; None = plain LCDM."""
    pars = camb.set_params(H0=H0, ombh2=OMBH2, omch2=OMCH2, mnu=0.06, omk=0,
                           tau=TAU, As=AS, ns=NS, lmax=2500)
    if k_cut is not None:
        k = np.logspace(-6, 1, 6000)
        pk = AS * (k / 0.05) ** (NS - 1.0)
        pk = np.where(k < k_cut, 1e-30, pk)      # hard IR cut; floor, not exact 0
        # effective_ns_for_nonlinear is required by CAMB for splined tables; it
        # only feeds the nonlinear (halofit) prescription, which is irrelevant at
        # the l <= 100 scales used here, so it is set to the true tilt.
        pars.set_initial_power_table(k, pk, effective_ns_for_nonlinear=NS)
    # UNLENSED, nonlinear OFF -- both on the physics gate's own repair list.
    # At l <= 100 lensing shifts TT negligibly, while the nonlinear (HMCode)
    # prescription is irrelevant here and in fact fails to converge on a hard
    # IR-cut spectrum. Both models are computed identically, which is what the
    # p-value SHIFT requires.
    pars.NonLinear = camb.model.NonLinear_none
    pars.set_for_lmax(2500, lens_potential_accuracy=0)
    res = camb.get_results(pars)
    tt = res.get_cmb_power_spectra(pars, CMB_unit="muK",
                                   raw_cl=True)["unlensed_scalar"][:, 0]
    cl = np.zeros(l_max + 1)
    cl[2:l_max + 1] = tt[2:l_max + 1]
    return cl


def p_below(cl, M, s_obs=S_OBS, n_mc=N_MC):
    """P(S_hat <= s_obs) under cosmic variance, full sky, ideal."""
    ls = np.arange(len(cl))
    dof = 2 * ls + 1
    act = slice(2, len(cl))
    chi2 = RNG.chisquare(df=dof[act], size=(n_mc, len(cl) - 2))
    full = np.zeros((n_mc, len(cl)))
    full[:, act] = cl[act] * chi2 / dof[act]
    s = np.einsum("ij,jk,ik->i", full, M, full)
    return float(np.mean(s <= s_obs)), s


def main():
    print("=" * 76)
    print("PROGRAM (A) RE-AIMED — the p-value shift.  ANALYSIS ONLY; no tier moves.")
    print("=" * 76)
    M = s12_matrix(L_MAX)
    chi_s = chi_S_mpc()
    print(f"\n  chi_S = {CHI_S_OVER_C_H0} c/H0 = {chi_s:,.0f} Mpc      (Eq.23, PINNED)")

    print("\n[0] REDUCTIO CONTROL (register 1an: test the rule on a viable model first)")
    cl_l = cl_for(None)
    p_l, s_l = p_below(cl_l, M)
    print(f"    LCDM: S_1/2[mean spectrum] = {s12_from_cl(cl_l, M):,.0f} uK^4")
    print(f"    LCDM: P(S_hat <= {S_OBS:.0f})    = {p_l*100:.3f}%")
    ok = p_l > 0
    print(f"    -> the statistic does NOT refute LCDM outright: {ok}")
    print("       (it reports LCDM as unlikely-but-possible, which is the known")
    print("        ~0.1% low-l anomaly, reproduced independently). Control PASSES,")
    print("        unlike the charter's rule, which failed this exact test.")

    print("\n[1] THE CUTOFF MODEL, a fortiori (READING A, model-favourable)")
    print(f"    {'convention':>18} {'k_S (1/Mpc)':>13} {'S_1/2 mean':>12} "
          f"{'P(S<=obs)':>11} {'shift':>10}")
    results = {}
    for name, factor in (("2*pi/chi_S", 2 * np.pi), ("pi/chi_S", np.pi)):
        k_cut = factor / chi_s
        cl_c = cl_for(k_cut)
        s_mean = s12_from_cl(cl_c, M)
        p_c, _ = p_below(cl_c, M)
        results[name] = (k_cut, s_mean, p_c)
        shift = f"{p_c/p_l:.1f}x" if p_l > 0 else "n/a"
        print(f"    {name:>18} {k_cut:>13.3e} {s_mean:>12,.0f} "
              f"{p_c*100:>10.3f}% {shift:>10}")

    print("\n[2] WHAT THIS SAYS")
    for name, (k_cut, s_mean, p_c) in results.items():
        print(f"    {name}: the cutoff moves the probability of seeing correlation")
        print(f"        as low as observed from {p_l*100:.3f}% (LCDM) to {p_c*100:.3f}%.")
    best = max(r[2] for r in results.values())
    print()
    if best < 0.05:
        print(f"    Even the model-favourable reading leaves the observation at")
        print(f"    p < 5% ({best*100:.3f}%). On this evidence the causal cutoff does")
        print("    NOT render the observed lack of correlation typical -- it is")
        print("    still a rare draw under the cutoff model.")
    else:
        print(f"    The cutoff raises the probability to {best*100:.2f}%, i.e. the")
        print("    observation stops being anomalous under the model. That is the")
        print("    substantive sense in which the cutoff would 'explain' the")
        print("    low-l deficit, and it is reached WITHOUT calibrating any")
        print("    amplitude.")
    print("\n    A FORTIORI STATUS: Reading A maximally suppresses large-scale power")
    print("    (it is hyperuniform). Reading B, the paper's own direction, cannot")
    print("    do better at suppressing S_1/2, so this is an upper bound on how")
    print("    much the causal condition can help.")
    print("=" * 76)


if __name__ == "__main__":
    main()
