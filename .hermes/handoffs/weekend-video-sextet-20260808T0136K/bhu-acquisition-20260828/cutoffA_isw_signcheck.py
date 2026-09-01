#!/usr/bin/env python3
"""Adjudicate the seat disagreement by computation, not by my say-so.

THE DISAGREEMENT (recorded per MUST-STOP):
  agy   -- adding late ISW/lensing power "strictly increases the expected value of
           S_1/2", so omitting it flatters the model and C2 was conservative.
  codex -- not guaranteed: S_1/2 = integral of (C_prim + C_ISW)^2 carries a CROSS
           TERM that can be negative.

I told Duho codex is right, on the argument that S_1/2 = C^T M C is a quadratic
form whose matrix M has negative off-diagonal entries. That was reasoning, not a
receipt. This script settles it.

THE DECISIVE TEST. S(C + x) = (C+x)^T M (C+x), so the gradient at x = 0 is 2 M C.
If ANY component of (M C) is negative, then adding a SMALL AMOUNT OF NON-NEGATIVE
POWER in that single multipole DECREASES S_1/2. Since a physical ISW contribution
must satisfy C_l^ISW >= 0 for every l -- but is otherwise free in shape -- a single
negative component of (M C) is sufficient to refute "strictly increases".

Note what this does and does not settle: it settles whether the increase is
GUARANTEED (agy's word was "strictly"). It does NOT settle whether the REAL ISW
spectrum happens to increase or decrease S_1/2, which needs the actual ISW C_l and
is a separate question left open.
"""

import numpy as np
from cutoffA_s12_machinery import s12_matrix, s12_from_cl, lcdm_cl

L_MAX = 100


def main():
    print("=" * 74)
    print("SEAT DISAGREEMENT, ADJUDICATED BY COMPUTATION")
    print("=" * 74)
    M = s12_matrix(L_MAX)
    cl = lcdm_cl(L_MAX)

    print("\n[1] Does M have negative off-diagonal entries? (my stated reason)")
    off = M - np.diag(np.diag(M))
    n_neg = int((off < 0).sum())
    print(f"    off-diagonal entries: {off.size - M.shape[0]:,}   negative: {n_neg:,}")
    print(f"    most negative off-diagonal: {off.min():.4e}")
    print(f"    -> claim as I stated it to Duho: {'CONFIRMED' if n_neg else 'FALSE'}")

    print("\n[2] THE DECISIVE TEST: any negative component of (M C)?")
    g = M @ cl
    # l = 0,1 carry C_l = 0 by construction (monopole/dipole removed), so a
    # "bump" there adds literally nothing. The first version of this script
    # picked l=1 as its counterexample and therefore tested nothing -- the
    # check reported that failure rather than hiding it. Restrict to l >= 2,
    # the multipoles that actually carry power.
    neg = np.array([l for l in np.where(g < 0)[0] if l >= 2 and cl[l] > 0])
    print(f"    multipoles l=2..{L_MAX}: {len(g)-2} components")
    print(f"    components with (M C)_l < 0 (l>=2, C_l>0): {len(neg)}")
    if len(neg):
        print(f"    such l values (first 15): {list(neg[:15])}")
        worst = neg[np.argmin(g[neg])]
        print(f"    most negative at l={worst}: (M C)_l = {g[worst]:.4e}")

    print("\n[3] EXPLICIT COUNTEREXAMPLE (construct it, do not argue it)")
    if len(neg):
        l0 = int(neg[np.argmin(g[neg])])
        s0 = s12_from_cl(cl, M)
        # add a small NON-NEGATIVE bump in the single multipole l0
        best = None
        for frac in (0.01, 0.05, 0.10, 0.25, 0.50):
            x = np.zeros_like(cl)
            x[l0] = frac * cl[l0]              # strictly positive added power
            s1 = s12_from_cl(cl + x, M)
            tag = "DECREASES" if s1 < s0 else "increases"
            print(f"    add {frac:5.0%} of C_{l0} as extra power -> "
                  f"S_1/2 {s0:,.0f} -> {s1:,.0f}   ({tag})")
            if s1 < s0 and best is None:
                best = (frac, s1)
        print()
        if best:
            print(f"    -> A physically admissible addition (C_l^extra >= 0 everywhere,")
            print(f"       nonzero only at l={l0}) DECREASES S_1/2 from {s0:,.0f} to")
            print(f"       {best[1]:,.0f}. 'Strictly increases' is therefore FALSE.")
            print("       CODEX IS RIGHT; agy's claim is refuted; my adjudication to")
            print("       Duho stands, and is now computed rather than asserted.")
        else:
            print("    -> no decrease found at the tested amplitudes; my adjudication")
            print("       is NOT supported by this test and must be revisited.")
    else:
        print("    (M C) has no negative component -> agy may be right after all and")
        print("    MY ADJUDICATION TO DUHO WAS WRONG. This must be corrected.")

    print("\n[4] WHAT THIS DOES NOT SETTLE")
    print("    Whether the REAL late-ISW spectrum increases or decreases S_1/2 for")
    print("    this model. That needs the actual ISW C_l, is a different question,")
    print("    and remains open. Only the word 'strictly' is adjudicated here.")
    print("=" * 74)


if __name__ == "__main__":
    main()
