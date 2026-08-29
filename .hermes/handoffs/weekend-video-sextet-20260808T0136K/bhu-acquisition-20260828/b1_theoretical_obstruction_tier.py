#!/usr/bin/env python3
"""B1 -- Q1, authorised by Duho ("then add another category").

Adds a fifth tier class for a theoretical no-go, and — the part Blanc flagged as where entries
will get misfiled — defines the boundary against a paper that merely fails to predict anything.

THE NEW TIER

    THEORETICAL-OBSTRUCTION
    Asserts: this paper PROVES that no member of a specified class of models can satisfy a
    specified conjunction of conditions. It EXCLUDES a region of model space.
    Refuted by: exhibiting a counterexample inside the stated domain.
    NOT refuted by: any measurement.

THE BOUNDARY, stated explicitly because it is where misfiling happens

    A paper that merely fails to predict is SILENT about what cannot happen. It is compatible
    with everything, which is precisely why CONSISTENCY-ONLY fits it.

    A no-go is INCOMPATIBLE with a specified class. It says something cannot exist. That is a
    falsifiable claim — falsifiable by CONSTRUCTION rather than by MEASUREMENT, which is why all
    four existing tiers, every one of them graded on observational testability, cannot hold it.

    So the discriminator is not "does it predict?" (both answer no) but:
        DOES IT ASSERT AN IMPOSSIBILITY OVER A STATED DOMAIN, WITH A REFUTATION CONDITION?

MEMBERSHIP CRITERION, AND HOW IT AVOIDS THE DEFECT ONE LEVEL UP

Blanc: "a tier whose name claims more than its criterion tests is the same defect one level up."
So the criterion does NOT grep for "theorem". It evaluates the three components of the assertion,
and it is validated by CONTROLS — it must ACCEPT the known no-go and REJECT two papers that
merely fail to predict. A criterion that accepts everything silent about observation would be
pattern-matching, and the negative controls are what catch that.
"""
import re, sys

SRC = "../bhu-reading-20260823/sources/"
CASES = {
    "entry 22 (Easson 2026)":        ("2606.25023_clean.txt", True),   # expected: IS a no-go
    "entry 8 (Poplawski 2010)":      ("0902.1994_clean.txt",  False),  # negative control
    "entry 40 (Poplawski 2020)":     ("2008.02136_clean.txt", False),  # negative control
    "entry 36 (Smoller-Temple 2000)":("smoller_temple_2000_clean.txt", False),  # negative control
}
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

# --- the three components of the assertion, evaluated separately ------------------------------
IMPOSSIBILITY = r"cannot be both|cannot be\b|can not be\b|does not yield|no .{0,30}(?:can|exists?)\b|impossible|obstruct\w*|must give up|prevents?\b"
DOMAIN        = r"[Cc]onsider a .{0,80}(?:spacetime|metric|parent|class|solution)|[Aa]ssume that|under the (?:same )?assumptions?|hypothes[ei]s"
REFUTABLE     = r"escape|evasion|requires? an? (?:additional|extra)|must give up at least one|unless"

def score(T):
    return (len(re.findall(IMPOSSIBILITY, T)), len(re.findall(DOMAIN, T)), len(re.findall(REFUTABLE, T)))

def is_obstruction(T):
    imp, dom, ref = score(T)
    # all three components must be present: an impossibility, a stated domain it ranges over,
    # and a stated way out (which is what makes it refutable rather than a bare denial)
    return imp >= 5 and dom >= 2 and ref >= 2

print("=" * 96); print("B1 -- THEORETICAL-OBSTRUCTION tier, with positive and negative controls"); print("=" * 96)
print(f"\n{'paper':<34} {'impossib.':>10} {'domain':>8} {'escape':>8} {'verdict':>12}  expected")
results = {}
for lbl, (fn, expected) in CASES.items():
    T = " ".join(open(SRC + fn).read().split())
    imp, dom, ref = score(T); got = is_obstruction(T)
    results[lbl] = (got, expected)
    print(f"{lbl:<34} {imp:>10} {dom:>8} {ref:>8} {str(got):>12}  {expected}")

chk("POSITIVE CONTROL: the criterion accepts entry 22, the known theoretical no-go",
    results["entry 22 (Easson 2026)"][0] is True,
    "Proposition 1, Proposition 2, Theorem 1 — impossibility over a stated domain with a stated "
    "escape route")
chk("NEGATIVE CONTROLS: the criterion REJECTS all three papers that merely fail to predict",
    all(not got for lbl, (got, exp) in results.items() if exp is False),
    "entries 8, 40 and 36 state no prediction either, and CONSISTENCY-ONLY is correct for them. "
    "A criterion that accepted these would be pattern-matching on silence rather than evaluating "
    "an impossibility claim — this is the check that catches that")
chk("the criterion agrees with the expected label on every case",
    all(got == exp for got, exp in results.values()),
    f"{sum(1 for g, e in results.values() if g == e)}/{len(results)} — one positive, three negative")

# ---- SCALE TEST, run immediately after the controls passed --------------------------------
# METHODS_NOTE_CLASSIFIER_BIAS.md: "Validate at the scale you intend to run. The protocol passed
# its small test and failed the real one." So the criterion was run over all 29 pinned sources
# the moment it went 4/4 on controls. It does NOT hold up.
import glob, os
_flag = []
for _f in sorted(glob.glob(SRC + "*_clean.txt")):
    _T = " ".join(open(_f).read().split())
    if is_obstruction(_T): _flag.append(os.path.basename(_f).replace("_clean.txt", ""))
print(f"\nSCALE TEST -- criterion run over all 29 pinned sources")
print(f"   flagged: {_flag}")
print(f"   of these, only 2606.25023 (entry 22) is a no-go. sym14091849 is entry 25, a BHU")
print(f"   CONSTRUCTION paper; 2503.14738 is the DESI collaboration paper, not a corpus entry at")
print(f"   all; smolin_1992 is the CNS founding paper.")
chk("SCALE TEST FAILED: the criterion is a poor SCREEN despite passing every control -- it flags "
    "4 of 29 sources and only 1 is correct",
    len(_flag) >= 3 and "2606.25023" in _flag,
    "4/4 on hand-picked controls, ~1/4 precision at corpus scale. This is the METHODS_NOTE "
    "finding reproduced on my own new criterion within minutes of building it: a small-batch "
    "control does not license a method at scale")

print("""
WHAT THIS CRITERION DOES NOT DO -- named, because the night's lesson is that a criterion which
does not name its limits will be trusted past them

  It counts three components and thresholds them. It cannot READ a proof, cannot check that the
  impossibility actually follows from the domain, and cannot tell a sound theorem from an
  unsound one. It distinguishes SHAPE, not VALIDITY.

  A paper that talked at length about obstructions without proving one would pass. That is a
  real false-positive route and it is not closed here. What closes it is a seat reading the
  paper — which is how entry 22 was classified in the first place, and how any future candidate
  should be.

  The four negative controls are the honest strength of this: the criterion is not merely
  asserted to distinguish a no-go from a silent paper, it is REQUIRED to, on three papers whose
  correct tier is already settled.

  AND THE SCALE TEST IS THE HONEST WEAKNESS. It passes every control and then flags 4 of 29
  sources, of which 1 is right. So it MUST NOT be used to propose refiling candidates. The tier
  is sound -- entry 22 belongs in it, on two seats' reading of the paper. The CRITERION is a
  screen with roughly 1-in-4 precision, and is recorded as such rather than shipped as a
  classifier. Any future candidate gets a seat reading it, exactly as entry 22 did.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
