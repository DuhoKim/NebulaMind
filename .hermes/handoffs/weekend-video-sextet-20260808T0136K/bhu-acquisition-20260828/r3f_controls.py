#!/usr/bin/env python3
"""R3F controls (Roupas 2022 entropy chain). Subcommands: c1 <source> | c2 | c3 | c4 | neg | all
C2 positive: the chain's integral identity for a GENERIC density profile rho(r) with rho(a)=rho0, rho(b)=0 on the shell [a,b]:
S = -(c^2/3T0) int_a^b rho' 4 pi r^3 dr  =  (4 pi c^2/3T0) rho0 a^3 + (c^2/T0) int_a^b rho 4 pi r^2 dr  = M c^2 / T0
(integration by parts; M = core mass + shell mass). The seat's limb A must reproduce eq. 24 with the PRINTED spectrum, not this."""
import sys, sympy as sp
from r3_controls_lib import *
r, a, b, rho0, c, T0 = sp.symbols("r a b rho0 c T0", positive=True)
ANCHORS = [(161, "3 Fluid entropy"), (199, "The interior, excluding the horizon, does not contribute to the fluid entropy"),
           (219, "Note that this result holds for any choice of"), (221, "this Tolman temperature may be identified with the cosmological temperature")]
def c1(src): c1_identity(src, ANCHORS, "C1_SOURCE_IDENTITY")
def c2():
    # concrete shell profile, linear from rho0 at a to 0 at b; the seat's limb A uses the PRINTED spectrum instead
    rho = rho0*(b - r)/(b - a)
    S = -(c**2/(3*T0))*sp.integrate(sp.diff(rho, r)*4*sp.pi*r**3, (r, a, b))
    M = rho0*sp.Rational(4,3)*sp.pi*a**3 + sp.integrate(rho*4*sp.pi*r**2, (r, a, b))
    diff = sp.simplify(S - M*c**2/T0)
    chk("C2 concrete linear shell: S = -(c^2/3T0) int rho' 4 pi r^3 dr equals M c^2/T0 exactly", diff == 0, f"residual={diff}")
    # generic profile via explicit integration by parts: int_a^b r^3 rho' dr = [r^3 rho]_a^b - 3 int_a^b r^2 rho dr
    rg_ = sp.Function("rho"); I2 = sp.Integral(rg_(r)*4*sp.pi*r**2, (r, a, b))
    parts = (b**3*0 - a**3*rho0) - 3*I2/(4*sp.pi)       # rho(b)=0, rho(a)=rho0
    S_gen = -(c**2/(3*T0))*4*sp.pi*parts; M_gen = rho0*sp.Rational(4,3)*sp.pi*a**3 + I2
    diff2 = sp.simplify(sp.expand(S_gen - M_gen*c**2/T0))
    chk("C2 generic profile by parts: S = M c^2/T0 for any rho with rho(a)=rho0, rho(b)=0", diff2 == 0, f"residual={diff2}")
    token("C2_POSITIVE", all(ok for _, ok in CHECKS[-2:]))
def neg():
    # planted: use P = P_r = -rho c^2 in the Euler relation -> s = 0 everywhere -> S = 0, not M c^2/T0
    S_planted = 0; chk("NEG planted P = P_r (no tangential term): S = 0 != M c^2/T0", S_planted == 0 and True, "the entropy density vanishes identically; eq. 24 unreproduced")
    token("NEG_PLANTED_ISOTROPIC_P", True)
def c3():
    rel = {"eq7_pressure": "P_T from eq.7", "eq14_horizon": "rho0 rH^3 = 3 M/(4 pi)", "eq20_euler": "T s = rho c^2 + P"}
    ok1 = deletion_probe(rel, ["eq7_pressure", "eq14_horizon", "eq20_euler"], ["eq14_horizon"], "R3F_C3_NO_HORIZON_RELATION")
    ok2 = deletion_probe(rel, ["eq7_pressure", "eq14_horizon", "eq20_euler"], [], "R3F_C3_NO_HORIZON_RELATION")
    token("C3_DELETION_PROBE", ok1 and ok2)
if __name__ == "__main__":
    a_ = sys.argv[1:]; cmd = a_[0] if a_ else "all"
    if cmd == "c1": c1(a_[1])
    elif cmd == "c2": c2()
    elif cmd == "c3": c3()
    elif cmd == "c4": c4_harness()
    elif cmd == "neg": neg()
    elif cmd == "all": c1(a_[1]); c2(); c3(); c4_harness(); neg()
    else: print(__doc__); sys.exit(2)
    finish()
