#!/usr/bin/env python3
# Limb B numeric evaluation of the horizon-criticality coefficient for the
# Dymnikova metric g_tt(r) = 1 - r_g (1 - exp(-r^3/r_*^3))/r, r_*^3 = r0^2 r_g.
# Horizons exist iff max_r [R_g(r)/r] >= 1. With x = r/r_*:
#   R_g/r = (r_g/r_*) (1 - e^{-x^3})/x ; criticality: (r_g/r_*) g_max = 1.
# g'(x)=0 <=> e^{-x^3}(3x^3+1) = 1 <=> e^w = 3w + 1 with w = x^3 (nonzero root).
from mpmath import mp, findroot, exp

mp.dps = 30  # protocol stall-guard precision

f = lambda w: exp(w) - 3*w - 1
w_star = findroot(f, 1.9)          # nonzero root
x_star = w_star ** (mp.mpf(1)/3)
g_max = (1 - exp(-w_star)) / x_star
kappa = 1 / g_max                  # critical r_g/r_*
# r_*^3 = r0^2 r_g and r_g = kappa r_*  =>  r_g = kappa^{3/2} r0
rg_over_r0 = kappa ** (mp.mpf(3)/2)
Mcrit_coeff = rg_over_r0 / 2       # Mcrit = Mcrit_coeff * c^2 r0 / G

G = mp.mpf("6.67430e-11")
c = mp.mpf("2.99792458e8")
kg_per_metre = Mcrit_coeff * c**2 / G   # Mcrit in kg for r0 = 1 m

print("w*   =", w_star)
print("x*   =", x_star)
print("g_max=", g_max)
print("kappa = 1/g_max =", kappa)
print("r_g(crit)/r0 = kappa^(3/2) =", rg_over_r0)
print("Mcrit = kappa^(3/2) c^2 r0 / (2G) =", Mcrit_coeff, "* c^2 r0 / G")
print("Mcrit per metre of r0 (kg/m) =", kg_per_metre)
