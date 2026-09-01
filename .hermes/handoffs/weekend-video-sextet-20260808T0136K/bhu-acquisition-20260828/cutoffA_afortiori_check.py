#!/usr/bin/env python3
"""Is the hard IR cut really the MOST suppressive reading? (discharging a 1ap flag)

OVERNIGHT ANALYSIS ONLY. No tier moves, closes nothing.

I published "the cutoff moves the anomaly to AT MOST ~3.2%" and called it an upper
bound. The upper-bound status rests on a claim I did NOT verify: the physics gate's
assertion that READING A (hard IR cut, P(k)=0 below k_S) is hyperuniform and hence
the MODEL-FAVOURABLE reading, so READING B (compact correlation support) cannot
suppress S_1/2 further. Register 1ap says verify adverse/convenient claims with the
same rigour as any other -- and this one flatters my own negative conclusion.

WHAT IS TESTED, AND WHAT THAT CANNOT COVER
  Reading B forces xi(r)=0 beyond chi_S. By Paley-Wiener (already computed in
  cutoffA_readings_incompatible.py) that makes P(k) ENTIRE, so a Reading-B spectrum
  can NEVER have a hard edge -- it must approach the cut smoothly. So the
  Reading-B-compatible family is, at minimum, the SMOOTHED cuts.

  PATTERN USED: compare the hard cut against smoothed cuts of increasing width at
  the same k_S, and see whether smoothing ever suppresses S_1/2 MORE.
  ONE CLASS THIS MISSES: a Reading-B spectrum need not be a smoothed version of
  LCDM at all -- it could have an entirely different shape near k_S (e.g. a bump
  below the cut, or oscillatory structure) that this family never reaches.
  WHAT WAS DONE ABOUT THAT: a deliberately adversarial member is included -- a
  spectrum with EXCESS power just below k_S (the opposite of a cut), which is what
  the compact-xi construction actually produces (cutoffA_readings_incompatible.py
  measured P largest at the SMALLEST k under Reading B). If even that does not beat
  the hard cut, the a-fortiori claim survives the most hostile member available
  cheaply. It remains a family test, not a proof over all of Reading B, and is
  reported as such.
"""

import numpy as np
import camb
from cutoffA_s12_machinery import s12_matrix, s12_from_cl

S_OBS = 1150.0
L_MAX = 100
N_MC = 100_000
RNG = np.random.default_rng(20260902)
H0, OMBH2, OMCH2, TAU = 67.36, 0.02237, 0.1200, 0.0544
AS, NS = 2.1e-9, 0.9649
CHI_S = 3.149 * 299792.458 / H0          # Mpc, Eq.23
K_S = 2 * np.pi / CHI_S


def cl_for_shape(shape_fn, l_max=L_MAX):
    pars = camb.set_params(H0=H0, ombh2=OMBH2, omch2=OMCH2, mnu=0.06, omk=0,
                           tau=TAU, As=AS, ns=NS, lmax=2500)
    k = np.logspace(-6, 1, 6000)
    pk = AS * (k / 0.05) ** (NS - 1.0) * shape_fn(k)
    pk = np.maximum(pk, 1e-30)
    pars.set_initial_power_table(k, pk, effective_ns_for_nonlinear=NS)
    pars.NonLinear = camb.model.NonLinear_none
    pars.set_for_lmax(2500, lens_potential_accuracy=0)
    res = camb.get_results(pars)
    tt = res.get_cmb_power_spectra(pars, CMB_unit="muK",
                                   raw_cl=True)["unlensed_scalar"][:, 0]
    cl = np.zeros(l_max + 1)
    cl[2:l_max + 1] = tt[2:l_max + 1]
    return cl


def p_below(cl, M):
    ls = np.arange(len(cl))
    dof = 2 * ls + 1
    act = slice(2, len(cl))
    chi2 = RNG.chisquare(df=dof[act], size=(N_MC, len(cl) - 2))
    full = np.zeros((N_MC, len(cl)))
    full[:, act] = cl[act] * chi2 / dof[act]
    s = np.einsum("ij,jk,ik->i", full, M, full)
    return float(np.mean(s <= S_OBS))


def main():
    print("=" * 76)
    print("A-FORTIORI CHECK: is the HARD cut the most suppressive? (1ap discharge)")
    print("=" * 76)
    M = s12_matrix(L_MAX)
    print(f"  k_S = 2*pi/chi_S = {K_S:.4e} /Mpc")

    shapes = {
        "LCDM (no cut)":        lambda k: np.ones_like(k),
        "HARD cut (Reading A)": lambda k: (k >= K_S).astype(float),
        "smoothed, w=0.3 k_S":  lambda k: 0.5 * (1 + np.tanh((k - K_S) / (0.3 * K_S))),
        "smoothed, w=1.0 k_S":  lambda k: 0.5 * (1 + np.tanh((k - K_S) / (1.0 * K_S))),
        "smoothed, w=3.0 k_S":  lambda k: 0.5 * (1 + np.tanh((k - K_S) / (3.0 * K_S))),
        "ADVERSARIAL: excess below k_S":
            lambda k: np.where(k < K_S, 3.0, 1.0),
    }

    print(f"\n  {'spectrum':>30} {'S_1/2 mean':>12} {'P(S<=1150)':>12}")
    out = {}
    for name, fn in shapes.items():
        cl = cl_for_shape(fn)
        s = s12_from_cl(cl, M)
        p = p_below(cl, M)
        out[name] = (s, p)
        print(f"  {name:>30} {s:>12,.0f} {p*100:>11.3f}%")

    hard_s, hard_p = out["HARD cut (Reading A)"]
    print("\n  VERDICT")
    beaten = [n for n, (s, p) in out.items()
              if n not in ("LCDM (no cut)", "HARD cut (Reading A)") and p > hard_p]
    if beaten:
        print("  a-fortiori claim FAILS -- these suppress MORE than the hard cut:")
        for n in beaten:
            print(f"      {n}: P = {out[n][1]*100:.3f}% > {hard_p*100:.3f}%")
        print("  => '3.2% is an upper bound' must be WITHDRAWN.")
    else:
        print(f"  No tested alternative beats the hard cut "
              f"(P = {hard_p*100:.3f}%, S_1/2 = {hard_s:,.0f}).")
        print("  The a-fortiori claim SURVIVES this family test. It is NOT a proof")
        print("  over all Reading-B spectra -- see the docstring's stated miss.")

    print("\n  SEPARATE FINDING, from numbers already in hand:")
    print(f"  the paper claims CMB temperature 'should not be correlated above")
    print(f"  60 deg' (L457), i.e. S_1/2 = 0. The hard cut -- its own most")
    print(f"  favourable implementation -- leaves S_1/2 = {hard_s:,.0f} uK^4,")
    print(f"  which is {hard_s/S_OBS:.1f}x the OBSERVED {S_OBS:.0f} and only")
    print(f"  {34924/hard_s:.1f}x below LCDM. The causal cut does not deliver the")
    print("  vanishing correlation the paper asserts; it delivers a partial one.")
    print("=" * 76)


if __name__ == "__main__":
    main()
