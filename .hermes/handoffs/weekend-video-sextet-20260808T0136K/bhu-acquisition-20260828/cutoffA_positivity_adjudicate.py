#!/usr/bin/env python3
"""Adjudicate the seat disagreement: is monopole-subtracted Reading B a VALID spectrum?

codex: min(P_B) > 0, positivity PASSES, S_1/2 = 23,900 uK^4
agy:   min(P_B) < 0, positivity FAILS,  S_1/2 = 10,063 uK^4

Both agree S_1/2 converges (overturning the earlier "no number" finding). They
disagree on whether the construction is admissible at all, which decides whether
Reading B is a completion or is excluded. That is arithmetic, so it is settled here
independently rather than by preferring a seat.

THE STRUCTURE, which makes the answer predictable before computing:
    P_B(k) = FT[(xi - c) W] = (P (*) W_tilde)(k) - c * W_tilde(k)
The first term is >= 0 (convolution of two non-negative functions). The second is
subtracted and is also >= 0. So P_B is a DIFFERENCE OF NON-NEGATIVE FUNCTIONS and
nothing guarantees its sign. Moreover the no-zero-mode condition forces P_B(0) = 0
exactly, so k=0 sits ON the boundary: P_B >= 0 everywhere requires k=0 to be a
MINIMUM. If the curvature there is negative, P_B dips below zero immediately.

This script computes P_B directly in real space (no convolution needed) as
    P_B(k) = 4 pi \int_0^{chi_S} dr r^2 [xi(r) - c] W(r) sinc(k r)
which is exact for the compactly supported integrand, and inspects the sign.
"""

import numpy as np

CHI_S = 14015.0            # Mpc, Eq.23
AS, NS, K0 = 2.1e-9, 0.9649, 0.05


def xi_of_r(r, k_min, k_max=10.0, n_k=400_000):
    """xi(r) = int dk/k Delta^2(k) sinc(kr), Delta^2 = As (k/k0)^(ns-1)."""
    k = np.geomspace(k_min, k_max, n_k)
    d2 = AS * (k / K0) ** (NS - 1.0)
    out = np.empty_like(r, dtype=float)
    for i, rr in enumerate(r):
        kr = k * rr
        sinc = np.where(kr < 1e-8, 1.0 - kr**2 / 6.0, np.sin(kr) / np.where(kr == 0, 1, kr))
        out[i] = np.trapz(d2 * sinc / k, k)
    return out


def window(r):
    x = np.clip(r / CHI_S, 0, 1)
    return (1 - x) ** 2 * (2 + x) / 2.0


def P_B(kk, k_min, n_r=20000):
    r = np.linspace(1e-6, CHI_S, n_r)
    W = window(r)
    xi = xi_of_r(r, k_min)
    # c = <W xi>/<W> with the d^3r measure
    num = np.trapz(r**2 * W * xi, r)
    den = np.trapz(r**2 * W, r)
    c = num / den
    f = (xi - c) * W
    out = np.empty_like(kk, dtype=float)
    for i, k in enumerate(kk):
        kr = k * r
        sinc = np.where(kr < 1e-8, 1.0 - kr**2 / 6.0, np.sin(kr) / np.where(kr == 0, 1, kr))
        out[i] = 4 * np.pi * np.trapz(r**2 * f * sinc, r)
    return out, c


def main():
    print("=" * 74)
    print("ADJUDICATING: is monopole-subtracted Reading B a valid (non-negative) spectrum?")
    print("=" * 74)
    k_s = 2 * np.pi / CHI_S
    print(f"  chi_S = {CHI_S} Mpc,  k_S = {k_s:.6e} /Mpc")

    for k_min in (k_s * 1e-3, k_s * 1e-5):
        # sample densely from far below k_S up through several k_S
        kk = np.concatenate([np.geomspace(1e-4 * k_s, k_s, 400),
                             np.linspace(k_s, 20 * k_s, 400)])
        p, c = P_B(kk, k_min)
        neg = kk[p < 0]
        print(f"\n  k_min = {k_min:.3e} /Mpc   (monopole c = {c:.6e})")
        print(f"    P_B(k->0) = {p[0]:.6e}   (should be ~0 by construction)")
        print(f"    min(P_B)  = {p.min():.6e}   at k = {kk[np.argmin(p)]:.4e}")
        print(f"    fraction of sampled k with P_B < 0: {len(neg)/len(kk)*100:.1f}%")
        if len(neg):
            print(f"    NEGATIVE over k in [{neg.min():.4e}, {neg.max():.4e}]"
                  f"  = [{neg.min()/k_s:.3f}, {neg.max()/k_s:.3f}] x k_S")
            print("    -> NOT a valid power spectrum. agy's positivity FAILURE is confirmed.")
        else:
            print("    -> no negative values sampled; codex's PASS is supported here.")

    print("\n  INTERPRETATION")
    print("  The no-zero-mode condition forces P_B(0)=0 exactly, so k=0 lies on the")
    print("  boundary of the positivity region. Whether P_B dips below zero just above")
    print("  k=0 is decided by curvature, not by any theorem -- which is why the two")
    print("  seats could disagree without either making an arithmetic slip: a coarse")
    print("  k-grid that skips the dip reports PASS.")
    print("=" * 74)


if __name__ == "__main__":
    main()
