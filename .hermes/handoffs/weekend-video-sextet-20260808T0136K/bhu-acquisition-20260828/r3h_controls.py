#!/usr/bin/env python3
"""R3H controls (entry 10 coefficient propagation). Subcommands: c1 <entry10_source> | c2 <rows.json> | c3 | c4 | neg | all
classify(old, new, precision_digits, magnitude_claim) -> SIGN_FLIPS | ORDER_MOVES | WITHIN_PRECISION per the draft's §3 step 3
(factor-3 threshold fixed before any number)."""
import sys, json, math
from r3_controls_lib import *
ANCHORS = [(113, "The average value of its square is"), (121, "This behavior is significant in spin fluids at extremely high densities")]
def c1(src): c1_identity(src, ANCHORS, "C1_SOURCE_IDENTITY")
def classify(old, new, precision_digits=2, magnitude_claim=True, inequality=None):
    if inequality is not None:   # inequality: (lhs_old, lhs_new, rhs) -> sign of (lhs - rhs) flips?
        lo, ln, rhs = inequality
        if (lo - rhs) * (ln - rhs) < 0: return "SIGN_FLIPS"
    if old != 0 and (new/old <= 0): return "SIGN_FLIPS"
    ratio = abs(new/old) if old else float("inf")
    if magnitude_claim and (ratio >= 3 or ratio <= 1/3): return "ORDER_MOVES"
    return "WITHIN_PRECISION" if round(old, precision_digits) == round(new, precision_digits) or not magnitude_claim else "ORDER_MOVES" if ratio >= 3 else "WITHIN_PRECISION"
def c2(path):
    rows = json.load(open(path)); allok = True
    for row in rows:
        got = classify(row["old"], row["new"], row.get("precision", 2), row.get("magnitude_claim", True), row.get("inequality"))
        ok = got == row["expect"]; allok &= ok
        chk(f"C2 classifier row {row['id']}: expect {row['expect']} got {got}", ok)
    token("C2_CLASSIFIER", allok)
def neg():
    rows = [(2.218e31, 2.218e31), (1.0, 1.0), (5e16, 5e16)]
    ok = all(classify(o, n) == "WITHIN_PRECISION" for o, n in rows)
    chk("NEG planted factor 1: every row WITHIN_PRECISION", ok); token("NEG_PLANTED_FACTOR_ONE", ok)
def c3():
    rel = {"entry10_L113": "3/4", "entry10_L121": "1/8", "inheritance_39": "row 39 sentence"}
    ok1 = deletion_probe(rel, ["entry10_L113", "entry10_L121", "inheritance_39"], ["inheritance_39"], "R3H_C3_NO_INHERITANCE_ANCHOR")
    ok2 = deletion_probe(rel, ["entry10_L113", "entry10_L121", "inheritance_39"], [], "R3H_C3_NO_INHERITANCE_ANCHOR")
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
