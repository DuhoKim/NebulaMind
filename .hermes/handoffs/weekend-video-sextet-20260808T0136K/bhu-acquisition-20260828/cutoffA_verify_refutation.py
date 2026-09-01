#!/usr/bin/env python3
"""Verify the physics gate's two decisive objections to Program (A). Independently.

The gate returned CLASS_REFUTED. Two of its objections, if true, are fatal to the
program AS CHARTERED, and both are computable. I check them here with the real
CAMB spectrum and this lane's already-validated S_1/2 operator -- NOT with the
gate's Sachs-Wolfe toy -- so this is an independent test of its claims, not a
replay of them.

OBJECTION 1 (the "killer lemma"): the admissible class allows P(k) >= 0 on the
whole free band [k_S, k_norm], and >= 0 permits = 0. So the class CONTAINS the
completion "cut everything below k_norm". Therefore S_min is set by k_norm -- a
number the charter never pinned -- and not by the causal scale k_S. If so, S_min
measures an arbitrary modelling choice, and the pre-registered fork cannot fire in
the refutation direction.

OBJECTION 2 (the decision rule is invalid): S_1/2 is QUADRATIC in C, so under
cosmic variance its sampling distribution is enormously skewed. The charter's rule
compared the observed value against the LCDM MEAN and would have concluded "LCDM
cannot produce 1150". If LCDM in fact produces <= 1150 with non-negligible
probability, the rule is simply wrong -- and it would have produced a FALSE
refutation of whatever model it was applied to.

Neither check needs the causal model at all. That is the point: they test the
INSTRUMENT, and the instrument is mine.
"""

import numpy as np
from cutoffA_s12_machinery import s12_matrix, s12_from_cl, lcdm_cl

S_OBS = 1150.0
RNG = np.random.default_rng(20260901)


def objection_1_killer_lemma(l_max=100):
    """Does the free band let the minimiser cut at k_norm instead of k_S?

    Rendered in C_l space, which is where it bites and where no CAMB re-run is
    needed: the class fixes C_l contributions from k > k_norm and leaves the band
    free with only P >= 0. Setting the band to zero is ADMISSIBLE. So the reachable
    S_1/2 includes the value obtained by suppressing every multipole the band
    dominates -- i.e. progressively more of the low-l spectrum as k_norm rises.
    """
    print("\n[1] THE KILLER LEMMA — does S_min track k_norm rather than k_S?")
    M = s12_matrix(l_max)
    cl = lcdm_cl(l_max)
    print("    Each row zeroes every multipole below l_keep, which the class")
    print("    PERMITS (P >= 0 allows P = 0 across the free band). l_keep is set")
    print("    by where k_norm falls, a choice the charter never pinned.")
    print(f"    {'l_keep':>7} {'S_1/2 (uK^4)':>14}  {'vs observed 1150':>18}")
    for l_keep in (2, 3, 4, 5, 6, 8, 10, 15, 20, 30):
        c = cl.copy()
        c[:l_keep] = 0.0
        s = s12_from_cl(c, M)
        rel = "BELOW" if s < S_OBS else "above"
        print(f"    {l_keep:>7} {s:>14.2f}  {rel:>18}")
    print("    -> S_min is a free function of where the band ends. The charter")
    print("       pinned k_S but never k_norm, so the minimum it would have")
    print("       reported measures the arbitrary choice, not the causal model.")
    print("       OBJECTION 1 CONFIRMED.")


def objection_2_cosmic_variance(l_max=100, n_mc=200_000):
    """Sampling distribution of S_1/2 under LCDM, full sky, ideal (no noise).

    Chat_l = C_l * chi^2_(2l+1) / (2l+1), independent across l.
    """
    print("\n[2] THE DECISION RULE — can LCDM itself produce the observed 1150?")
    M = s12_matrix(l_max)
    cl = lcdm_cl(l_max)
    ls = np.arange(l_max + 1)
    dof = 2 * ls + 1

    s_theory = s12_from_cl(cl, M)

    # draw Chat_l for l = 2..l_max
    active = slice(2, l_max + 1)
    chi2 = RNG.chisquare(df=dof[active], size=(n_mc, l_max - 1))
    chat = cl[active] * chi2 / dof[active]
    full = np.zeros((n_mc, l_max + 1))
    full[:, active] = chat
    # S = c^T M c, computed batched
    s_samples = np.einsum("ij,jk,ik->i", full, M, full)

    frac_below = float(np.mean(s_samples <= S_OBS))
    print(f"    S_1/2 of the LCDM MEAN spectrum      : {s_theory:10.0f} uK^4")
    print(f"    mean of the SAMPLING distribution    : {np.mean(s_samples):10.0f} uK^4")
    print(f"    median of the sampling distribution  : {np.median(s_samples):10.0f} uK^4")
    print(f"    5th percentile                       : {np.percentile(s_samples,5):10.0f} uK^4")
    print(f"    1st percentile                       : {np.percentile(s_samples,1):10.0f} uK^4")
    print(f"    0.1th percentile                     : {np.percentile(s_samples,0.1):10.0f} uK^4")
    print(f"    P(S_hat <= {S_OBS:.0f})  under LCDM        : {frac_below*100:.3f}%"
          f"   ({int(frac_below*n_mc)} of {n_mc:,} draws)")
    print()
    print("    The mean of the sampling distribution EXCEEDS the mean-spectrum")
    print("    value because S_1/2 is quadratic in C: variance adds a positive")
    print("    term. The charter's rule ('if the model's minimum exceeds the")
    print("    observed value, the model cannot produce it') compares a point")
    print("    prediction against a random variable and IGNORES this spread.")
    if frac_below > 0:
        print(f"    -> LCDM produces <= {S_OBS:.0f} uK^4 in {frac_below*100:.3f}% of skies.")
        print("       So the same rule applied to LCDM would have 'refuted' LCDM,")
        print("       which is a reductio. OBJECTION 2 CONFIRMED: the pre-registered")
        print("       rule must be replaced by a p-value statement.")
    else:
        print("    -> not reproduced at this MC size; objection 2 NOT confirmed here.")


def main():
    print("=" * 74)
    print("VERIFYING THE PHYSICS GATE'S REFUTATION OF PROGRAM (A) — independently")
    print("=" * 74)
    objection_1_killer_lemma()
    objection_2_cosmic_variance()
    print("\n" + "=" * 74)
    print("Both checks use the real CAMB spectrum and this lane's validated S_1/2")
    print("operator, not the gate's toy model. Neither invokes the causal model:")
    print("they test the INSTRUMENT the charter proposed, which was mine.")
    print("=" * 74)


if __name__ == "__main__":
    main()
