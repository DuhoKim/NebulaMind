#!/usr/bin/env python3
"""Tori's own verification of the two seat derivations (codex + agy) for the entry-1 (Pathria 1972)
standing adjudication. Eval-what-you-print: every number in the reconciliation note is computed here.
Inputs are the pinned Planck 2018 values (1807.06209_clean.txt lines 471, 1773, 1775, 2169-2170)
and Pathria's printed representative bounds (pathria_1972_..._clean.txt lines 443-453)."""
import math
Mpc = 3.0856776e24; c = 2.99792458e10; G = 6.67430e-8            # cgs
H0, sH0 = 67.36, 0.54; Om, sOm = 0.3158, 0.0073; OL, sOL = 0.6847, 0.0073
OK, sOK = 0.001, 0.002; OLh2, sOLh2 = 0.3107, 0.0082
h = H0*1e5/Mpc
q0 = Om/2 - OL; sq = 1.5*sOm                                     # flat fit: OL = 1-Om -> q0 = 1.5 Om - 1
print(f"H0 = {h:.5e} s^-1 ; q0 = {q0:.4f} +- {sq:.5f} (flat-fit propagation)")
print(f"  (1/2 - q0)/sigma = {(0.5-q0)/sq:.1f} sigma ; (q0 - (-1))/sigma = {(q0+1)/sq:.1f} sigma")
rc = 3*h**2/(8*math.pi*G); rm = Om*rc
print(f"rho_crit = {rc:.4e} ; rho_m = {rm:.4e} +- {rm*math.sqrt((sOm/Om)**2+(2*sH0/H0)**2):.2e} g cm^-3")
Lam = 3*OL*h**2/c**2; Lam2 = 3*OLh2*(1e7/Mpc)**2/c**2; sLam2 = 3*sOLh2*(1e7/Mpc)**2/c**2
print(f"Lambda = {Lam:.4e} cm^-2 (from OL,H0) ; {Lam2:.4e} +- {sLam2:.2e} (from OL h^2)")
print(f"  ratio to Pathria's printed Lambda_c = 1.0e-57: {Lam/1e-57:.2f}")
# Pathria's own Lambda_c at his representative H0=75, q0=1 -- check his printed 1.0e-57
lc = lambda q: q*q/2 - 2*q + 0.5 + math.sqrt(3)/6*math.sqrt((q+1)**3*(3*q-1))   # codex closed form
u75 = (75e5/Mpc)**2/c**2
print(f"lambda_c(q0=1) = {lc(1):.4f} -> Lambda_c(H0=75,q0=1) = {lc(1)*u75:.3e} cm^-2 (Pathria prints 1.0e-57)")
lam = lc(1); print(f"  cubic identity residual at critical point: {lam*(3+lam)**2-(2-1+lam)**3:.1e}")
# measured configuration against the two inequalities: closed (lambda > 1-2q0) and Lambda<=Lambda_c
lam_m = 3*OL; x = 2*q0 - 1 + lam_m
print(f"lambda_meas = {lam_m:.4f} ; closed needs lambda > {1-2*q0:.4f} ; x = Om+OL-1 = {x:.4f}")
print(f"  Lambda<=Lambda_c needs lam(3q0+lam)^2 <= x^3 : LHS {lam_m*(3*q0+lam_m)**2:.4f} vs RHS {x**3:.2e} -> VIOLATED")
xneed = (27*OL*Om**2/4)**(1/3)
print(f"  at Planck Om,OL the bound needs Om+OL-1 >= {xneed:.3f}, i.e. Omega_K <= {-xneed:.3f} ; Planck 0.001+-0.002 -> {(OK+xneed)/sOK:.0f} sigma")
Lc = (4/9)*(h**2/c**2)*(0.001)**3/Om**2                          # agy's formula, Omega_K = -0.001 (1-sigma closed side)
print(f"agy's Lambda_c(Omega_K=-0.001) = {Lc:.3e} cm^-2 ; ratio Lambda/Lambda_c = {Lam/Lc:.2e}")
# existence of a closed, Lambda<=Lambda_c dust model as a function of q0 (positive root of 3x^2+3(1-q0^2)x+(1-2q0)(1+q0)^2)
def exists(q):
    a, b, cc = 3, 3*(1+q)*(1-q), (1-2*q)*(1+q)**2
    d = b*b - 4*a*cc
    return d >= 0 and any((-b+s*math.sqrt(d))/(2*a) > 0 for s in (1, -1))
print("closed+Lambda<=Lambda_c model exists for q0 =", {q: exists(q) for q in (-2, -1.2, -0.9, round(q0,3), 0, 0.4, 0.49, 0.51, 1)})
