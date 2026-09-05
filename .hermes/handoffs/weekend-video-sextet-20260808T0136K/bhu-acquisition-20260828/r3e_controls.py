#!/usr/bin/env python3
"""R3E controls (Dymnikova 1992 source consistency). Subcommands: c1 <source> | c2 | c3 | c4 | neg | all
C2 benchmark: static spherically symmetric metric ds^2 = f dt^2 - dr^2/f - r^2 dOmega^2 (G=c=1);
Einstein tensor components G^t_t = (r f' + f - 1)/r^2, G^theta_theta = (r f'' + 2 f')/(2 r). Schwarzschild must give 0;
de Sitter f = 1 - r^2/r0^2 must give G^t_t = G^th_th = -3/r0^2 (= -Lambda), i.e. isotropic."""
import sys, json, sympy as sp
from r3_controls_lib import *
r, rg, r0, rs3 = sp.symbols("r r_g r_0 rstar3", positive=True)
def Gtt(f): return sp.simplify((r*sp.diff(f, r) + f - 1)/r**2)
def Gthth(f): return sp.simplify((r*sp.diff(f, r, 2) + 2*sp.diff(f, r))/(2*r))
ANCHORS = [(118, "Now we have to make one assumption concerning the specific form of the"), (119, "stress-energy tensor (4). If we assume that"),
           (122, "where r0 is connected with e0 by the de Sitter relation"), (145, "From the Einstein equations we derive the remaining components of")]
def c1(src): c1_identity(src, ANCHORS, "C1_SOURCE_IDENTITY")
def c2():
    s = Gtt(1 - rg/r); t = Gthth(1 - rg/r); chk("C2 Schwarzschild: G^t_t = 0 and G^th_th = 0", s == 0 and t == 0, f"{s}, {t}")
    d1 = Gtt(1 - r**2/r0**2); d2 = Gthth(1 - r**2/r0**2)
    chk("C2 de Sitter: G^t_t = G^th_th = -3/r0^2 (isotropic, Lambda = 3/r0^2)", sp.simplify(d1 + 3/r0**2) == 0 and sp.simplify(d2 + 3/r0**2) == 0, f"{d1}, {d2}")
    token("C2_GR_BENCHMARK", all(ok for _, ok in CHECKS[-2:]))
def dym(coef):
    """printed profile (P2) and tangential pressure (P4) with the OCR-ambiguous coefficient `coef` (3/2 as read)."""
    Rg = rg*(1 - sp.exp(-r**3/rs3)); f = 1 - Rg/r
    T00_metric = -Gtt(f)/(8*sp.pi)          # 8 pi T^t_t = G^t_t with the paper's sign convention (rho = -G^t_t/8pi in these units)
    eps0 = 3*rg/(8*sp.pi*rs3)               # from r*^3 = r0^2 r_g and r0^2 = 3/(8 pi eps0) (G=c=1)
    T00_printed = eps0*sp.exp(-r**3/rs3)
    T22_printed = eps0*(1 - coef*r**3/rs3)*sp.exp(-r**3/rs3)
    T22_metric = -Gthth(f)/(8*sp.pi)
    return sp.simplify(T00_metric - T00_printed), sp.simplify(T22_metric - T22_printed)
def neg():
    res00, res22 = dym(sp.Integer(1))       # planted 3/2 -> 1
    chk("NEG planted coefficient 1 in (P4): tangential residual is NON-zero", res22 != 0, f"residual={res22}")
    token("NEG_PLANTED_COEFFICIENT", res22 != 0)
def c3():
    rel = {"metric": "P1", "field_equations": "G = 8 pi T", "profile": "P2"}
    ok1 = deletion_probe(rel, ["metric", "field_equations", "profile"], ["field_equations"], "R3E_C3_NO_FIELD_EQUATIONS")
    ok2 = deletion_probe(rel, ["metric", "field_equations", "profile"], [], "R3E_C3_NO_FIELD_EQUATIONS")
    token("C3_DELETION_PROBE", ok1 and ok2)
if __name__ == "__main__":
    a = sys.argv[1:]; cmd = a[0] if a else "all"
    if cmd == "c1": c1(a[1])
    elif cmd == "c2": c2()
    elif cmd == "c3": c3()
    elif cmd == "c4": c4_harness()
    elif cmd == "neg": neg()
    elif cmd == "all": c1(a[1]); c2(); c3(); c4_harness(); neg()
    else: print(__doc__); sys.exit(2)
    finish()
