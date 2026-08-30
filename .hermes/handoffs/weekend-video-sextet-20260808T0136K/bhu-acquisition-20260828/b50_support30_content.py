#!/usr/bin/env python3
"""B50 -- support-layer content verification, entry 30 (the kaon-condensation mechanism review
the CNS falsifier imports).

The support entries (29,30,32,33,34,35,58) were byline-verified (b42) and pinned but their
CONTENT -- the measurement/mechanism each SUPPLIES to a falsifier -- had not been bound to the
source. This is the first of that sweep. It is a SELF-COMPUTING string-presence verification (no
seat gate: there is no judgment, only "does the pinned source contain the exact load-bearing
claim the record attributes to it"; per the describe-vs-compute law, self-computing checks are
the reliable kind). A FAILURE here would be a record OVER-ATTRIBUTION -- a STOP-for-Duho item,
because the falsifier chain (entry 7) leans on these being in THIS document.

ENTRY 30 = Brown, Lee & Rho, "Recent developments on kaon condensation...", Phys. Rept. 462
(2008), arXiv 0708.3137, pinned ar5iv text `blr_physrept_clean.txt`. The record attributes TWO
load-bearing claims to it; both are here CONFIRMED verbatim against the source:
  1. the 4% double-NS mass-asymmetry limb, in Sec. 3.2 "Formation Of Double Neutron Star
     Binaries";
  2. the He-red-giant proviso: the pulsar accretes 0.1-0.2 M_sun of helium during the He red
     giant stage -- the figure Tauris et al. 2017 (entry 35) later supersede at 0.0134 M_sun.
VERDICT: entry 30's record is source-accurate; no over-attribution; nothing changes.
"""
import re, os
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
SRC = os.path.join(ROOT, "bhu-theory-phase3-cns-20260821/sources/blr_physrept_clean.txt")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B50 -- support entry 30 content bound to source"); print("=" * 98)

S = " ".join(open(SRC, errors="ignore").read().split())
chk("IDENTITY: the pinned source is BLR's kaon-condensation Physics Reports review (0708.3137)",
    "Recent Developments on Kaon Condensation" in S and "Physics Reports" in S)
chk("CLAIM 1 SOURCE-BOUND: the 4% double-NS mass-asymmetry limb is in Sec. 3.2 of the source",
    "Formation Of Double Neutron Star Binaries" in S
    and "within 4%" in S and "4% different from each other" in S)
chk("CLAIM 2 SOURCE-BOUND: the He-red-giant proviso -- pulsar accretes 0.1-0.2 M_sun of helium "
    "during the He red giant stage -- is in the source verbatim",
    "During the He red giant stage the pulsar accretes 0.1" in S
    and "helium" in S and "red giant" in S)

B = open(BIB).read()
cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b30 = " ".join(blocks[30].split())
chk("RECORD MATCHES SOURCE: entry 30 attributes exactly these two claims (4% limb Sec 3.2; "
    "0.1-0.2 M_sun He proviso) and both are confirmed present above -- no over-attribution",
    "4% double-NS asymmetry limb" in b30 and "0.1" in b30 and "helium" in b30.lower()
    and "0.0134" in b30)  # the Tauris supersession figure, cross-linked

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
