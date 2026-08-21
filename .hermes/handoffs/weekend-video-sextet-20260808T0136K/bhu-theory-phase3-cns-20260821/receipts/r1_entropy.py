#!/usr/bin/env python3
"""R1 — BLR 2008 Eq. (2) and the 10^20 entropy ratio, from first principles."""
import math
G, hbar, c, Msun = 6.67430e-11, 1.054571817e-34, 2.99792458e8, 1.98892e30
S = 4 * math.pi * G * Msun**2 / (hbar * c)      # = (k_B/4)*A/l_P^2 at one solar mass
print(f"Eq.(2) coefficient : {S:.4e} k_B   (printed 1.05e77, dev {abs(S-1.05e77)/1.05e77:.2%})")
print(f"BH / Fe-core ratio : {S/1e57:.3e}       (printed 1e20)")
assert abs(S - 1.05e77) / 1.05e77 < 0.01
assert abs(S/1e57 - 1e20) / 1e20 < 0.10
print("R1 PASS")
