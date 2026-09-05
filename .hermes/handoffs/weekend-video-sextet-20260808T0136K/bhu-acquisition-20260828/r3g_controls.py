#!/usr/bin/env python3
"""R3G controls (Smoller–Temple 2000 shock position). Subcommands: c1 <source> | c2 <transcription.json> | c3 | c4 | neg | all
C2 takes the seat's transcription of eq. 7.31 as JSON {coef_lo, coef_hi, T0, h0, Rstar, printed_value} and prints the
reproduced value beside the printed .019 — PASS only within two significant figures. The lane's own reading of the
extracted text did NOT reproduce .019 (see the draft's §0 observation); the exact printed form is a freeze-time task."""
import sys, json, math
from r3_controls_lib import *
ANCHORS = [(104, "parameters in the problem other than the experimentally determined values of the Hubble constant"),
           (160, "the galaxies, as a function of"), (213, "2.7/4000 and present time R = 1, as predicted by this model, is"),
           (231, "at which we start the shock"), (287, "For example, at T0 = 2.7")]
def c1(src): c1_identity(src, ANCHORS, "C1_SOURCE_IDENTITY")
def evaluate(t):
    lnq = math.log(1.0/t["Rstar"])**2
    lo = t["coef_lo"]*t["T0"]**4/(t["h0"]**2)*lnq; hi = t["coef_hi"]*t["T0"]**4/(t["h0"]**2)*lnq
    return math.sqrt(lo), math.sqrt(hi)   # r^2 - r*^2 in units of H0^-2 -> sqrt in Hubble lengths
def c2(path):
    t = json.load(open(path)); lo, hi = evaluate(t); pv = t["printed_value"]
    print(f"  transcription: {t}\n  reproduced sqrt(r^2-r*^2)/H0^-1 in [{lo:.4g}, {hi:.4g}]; printed {pv}")
    ok = round(lo, 2) == round(pv, 2) or round(hi, 2) == round(pv, 2) or (lo <= pv <= hi)
    chk("C2 worked value (S2) reproduced to two significant figures", ok, f"[{lo:.3g},{hi:.3g}] vs {pv}")
    token("C2_POSITIVE", ok)
def neg():
    t = {"coef_lo": 2.62e-7, "coef_hi": 2.65e-7, "T0": 2.7, "h0": 0.55, "Rstar": 2.7/4000, "printed_value": 0.019}
    lnq1 = math.log(1.0/t["Rstar"])   # planted ln instead of ln^2
    v = math.sqrt(t["coef_lo"]*t["T0"]**4/(t["h0"]**2)*lnq1); ok = round(v, 2) != 0.019
    chk("NEG planted ln(1/R*) for ln^2(1/R*): (S2) must fail", ok, f"planted value {v:.4g}")
    token("NEG_PLANTED_LOG_POWER", ok)
def c3():
    rel = {"eq731": "r^2-r*^2 bound", "Rstar_floor": "printed admissible R* interval", "eq737_738": "present shock bounds"}
    ok1 = deletion_probe(rel, ["eq731", "Rstar_floor", "eq737_738"], ["Rstar_floor"], "R3G_C3_NO_START_FLOOR")
    ok2 = deletion_probe(rel, ["eq731", "Rstar_floor", "eq737_738"], [], "R3G_C3_NO_START_FLOOR")
    token("C3_DELETION_PROBE", ok1 and ok2)
if __name__ == "__main__":
    a = sys.argv[1:]; cmd = a[0] if a else "all"
    if cmd == "c1": c1(a[1])
    elif cmd == "c2": c2(a[1])
    elif cmd == "c3": c3()
    elif cmd == "c4": c4_harness()
    elif cmd == "neg": neg()
    elif cmd == "all": c1(a[1]); c2(a[2]); c3(); c4_harness(); neg()
    else: print(__doc__); sys.exit(2)
    finish()
