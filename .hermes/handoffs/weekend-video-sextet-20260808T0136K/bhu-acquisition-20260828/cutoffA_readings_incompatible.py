#!/usr/bin/env python3
"""Program (A), step 2: are the two readings of the causal condition the same?

The source (2003.11544) says the causal condition leaves "an infrared cutoff in
the spectrum of inhomogeneities for chi > chi_S". That sentence admits TWO
readings, and step 1's admissible class assumed the first:

  READING A (Fourier support):  P(k) = 0 for k < k_S
      "no power in modes larger than the causal scale"

  READING B (real-space support): xi(r) = 0 for r > chi_S
      "no correlation between points separated by more than the causal scale"

They sound like paraphrases. THE CLAIM UNDER TEST HERE: they are not merely
different, they are MUTUALLY EXCLUSIVE (up to the trivial zero field), so the
choice is forced and it is physics, not bookkeeping.

The argument: xi and P are a 3-D isotropic Fourier pair,
    xi(r) = int_0^inf dk k^2/(2 pi^2) P(k) sinc(k r).
If xi has COMPACT SUPPORT, its transform P extends to an ENTIRE function of
exponential type (Paley-Wiener). A non-trivial entire function cannot vanish on a
whole interval (its zeros are isolated). So xi compactly supported => P(k) CANNOT
vanish identically on [0, k_S). Conversely a hard IR cut in P leaves xi with
oscillatory, non-compact tails.

This script does not assert that -- it COMPUTES both directions and prints the
numbers, so the claim stands or falls on output rather than on prose.
"""

import numpy as np

CHI_S = 1.0      # causal scale, working units
K_S = np.pi / CHI_S


def xi_from_P(P_of_k, r_grid, k_max=400.0, n_k=400_000):
    """xi(r) = int dk k^2/(2 pi^2) P(k) sinc(kr), sinc(x)=sin(x)/x."""
    k = np.linspace(1e-6, k_max, n_k)
    Pk = P_of_k(k)
    integ = k ** 2 / (2 * np.pi ** 2) * Pk
    out = np.empty_like(r_grid)
    for i, r in enumerate(r_grid):
        kr = k * r
        sinc = np.where(kr < 1e-8, 1.0 - kr ** 2 / 6.0, np.sin(kr) / np.where(kr == 0, 1, kr))
        out[i] = np.trapz(integ * sinc, k)
    return out


def P_from_xi(xi_of_r, k_grid, r_max, n_r=200_000):
    """P(k) = 4 pi int_0^{r_max} dr r^2 xi(r) sinc(kr)  (inverse of the above)."""
    r = np.linspace(0.0, r_max, n_r)
    xr = xi_of_r(r)
    out = np.empty_like(k_grid)
    for i, k in enumerate(k_grid):
        kr = k * r
        sinc = np.where(kr < 1e-8, 1.0 - kr ** 2 / 6.0, np.sin(kr) / np.where(kr == 0, 1, kr))
        out[i] = 4 * np.pi * np.trapz(r ** 2 * xr * sinc, r)
    return out


def main():
    print("=" * 74)
    print("PROGRAM (A) STEP 2 — are READING A and READING B the same condition?")
    print("=" * 74)
    print(f"    working units: chi_S = {CHI_S}, k_S = pi/chi_S = {K_S:.4f}")

    # ---------- direction 1: impose READING B, look at P(k) on [0, k_S) -------
    print("\n[1] IMPOSE READING B (xi compactly supported on r <= chi_S),")
    print("    then ask whether READING A (P(k)=0 for k<k_S) can also hold.")

    def xi_compact(r):
        """A smooth, non-negative-definite bump supported on [0, chi_S].

        Chosen as the self-convolution of a spherical top hat (the 'spherical
        overlap' kernel), which is a genuine correlation function -- its
        transform is (3 j_1(x)/x)^2 >= 0, so it is positive-definite by
        construction and not merely a convenient shape.
        """
        a = CHI_S / 2.0                     # top-hat radius; support of xi is 2a
        x = np.clip(r / (2 * a), 0, 1)
        return (1 - x) ** 2 * (2 + x) / 2.0   # spherical overlap volume, normalised

    k_lo = np.linspace(0.02, K_S, 25)
    P_lo = P_from_xi(xi_compact, k_lo, r_max=CHI_S)
    P_ref = P_from_xi(xi_compact, np.array([K_S * 3]), r_max=CHI_S)[0]
    frac = np.abs(P_lo) / abs(P_ref)
    print(f"    P(k) for k in (0, k_S), relative to P(3k_S) = {P_ref:.4e}:")
    for kk, pp, ff in list(zip(k_lo, P_lo, frac))[::4]:
        print(f"       k={kk:6.3f}  P={pp: .4e}   |P|/|P(3k_S)| = {ff:8.2f}")
    print(f"    min |P| on (0,k_S) = {np.min(np.abs(P_lo)):.4e}")
    print(f"    -> READING A demands this be ZERO on the whole interval.")
    print(f"       It is not: the smallest value is {np.min(frac):.1f}x the reference,")
    print("       and P is LARGEST at the smallest k. The two cannot both hold.")

    # ---------- direction 2: impose READING A, look at xi(r) beyond chi_S -----
    print("\n[2] IMPOSE READING A (hard IR cut P(k)=0 for k<k_S, ~scale-invariant")
    print("    above it), then ask whether xi vanishes beyond chi_S (READING B).")

    def P_hardcut(k):
        return np.where(k < K_S, 0.0, k ** (-3.0) * K_S ** 3)

    r_out = np.array([1.0, 1.5, 2.0, 3.0, 5.0, 8.0]) * CHI_S
    xi_out = xi_from_P(P_hardcut, r_out)
    xi0 = xi_from_P(P_hardcut, np.array([0.05 * CHI_S]))[0]
    print(f"    xi(0.05 chi_S) = {xi0:.4e}  (reference scale)")
    for r, xv in zip(r_out, xi_out):
        print(f"       r = {r/CHI_S:4.1f} chi_S   xi = {xv: .4e}   "
              f"|xi|/|xi_0| = {abs(xv/xi0):.4f}")
    tail = max(abs(xi_out[-1] / xi0), abs(xi_out[-2] / xi0))
    print(f"    -> READING B demands xi = 0 for r > chi_S. It is not:")
    print(f"       correlation persists at the {tail*100:.1f}% level out to 8 chi_S,")
    print("       decaying as an oscillatory tail, never identically zero.")

    print("\n[3] CONCLUSION OF THIS SCRIPT (arithmetic only, no physics claim)")
    print("    The two readings are NOT paraphrases and cannot both be imposed:")
    print("    compact correlation support forces a strictly positive spectrum at")
    print("    small k; a hard spectral IR cut forces correlations beyond chi_S.")
    print("    Program (A)'s admissible class therefore depends on a CHOICE that")
    print("    the arithmetic cannot make. That choice is step 2's gate question.")
    print("=" * 74)


if __name__ == "__main__":
    main()
