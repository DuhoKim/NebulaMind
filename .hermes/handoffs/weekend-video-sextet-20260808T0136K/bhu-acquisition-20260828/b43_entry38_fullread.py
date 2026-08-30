#!/usr/bin/env python3
"""B43 -- entry 38 read IN FULL under the census rule. The census's last unreceipted paper.

WHY THIS EXISTS. CGATE_B41 refuted the coverage proof on one premise: B32's gates read entry 57
in full but only AUDITED entry 38's relevant passages, and b33's retrospective "38 and 57 were
done in b32's gate" laundered that into a full-read receipt which b41 then bound by substring.
Corrected coverage was 38/39. This file is the missing paper's full read.

THE READ. math-ph_0302036_clean.txt (Smoller & Temple, "Cosmology, Black Holes and Shock Waves
Beyond the Hubble Length", Methods Appl. Anal. 11, 77-132), all 3262 lines sequentially,
2026-08-30, Tori. (The record carries a "READ 2026-08-23" note -- that read predates the b28
census rule and left no rule-adjudication; today's read supplies it.)

RULE, unchanged from b28: does the paper PROVE that no member of a specified class of models can
satisfy a specified conjunction of conditions -- refutable by counterexample, not by measurement?

VERDICT (mine, to the gate): NOT AN OBSTRUCTION at paper level. Complete theorem inventory:
  Thm 1 (age/redshift-limit bounds under 0<=p<=rho/3)      bounds, not exclusions
  Thm 2 + Cor 1 (closed-form constant-sigma FRW solutions) constructive
  Sec 3 (OS-inside-BH via Eddington-Finkelstein)           constructive
  Sec 4 (TOV-inside-BH: co-moving A<0 system (4.16-4.18))  constructive derivation
  Thm 3 (RH conditions <-> single constraint (5.25))       equivalence machinery
  Thm 4 (change of variables to (u,N))                     machinery
  Thm 5 (entropy bounds from one inequality)               machinery
  Thm 6 (EXISTENCE+uniqueness of u_sigma for all sigma)    the operative result, constructive
  Thm 7 (subluminous everywhere IFF sigma<=1/3)            family-delimiting -- claim-level
  Thm 8 (Big-Bang speed trichotomy: light speed only at 1/3) family-delimiting -- claim-level
  Thm 9 + Cor 2 (shock-position estimates)                 constructive
The paper's operative contribution is the exact-solution construction (abstract's first words:
"We construct"). Its two impossibility-adjacent claims were already adjudicated in b32 (the
"[15] proved TOV-continuation" attribution -- unsupported by entry 57; and the infinite-FRW
aside -- a finite-mass junction limitation). NEW FROM THE FULL READ: Theorems 7/8 were
unrecorded. They are the same claim-level shape as entry 37's recorded sigma<=1/3 constraint
(B30's ruling: a theorem delimiting a constructed family stays with the construction), so the
record now carries them as claim item 3 and the tier stays CONSISTENCY-ONLY.

WHAT WOULD HAVE CHANGED MY VERDICT: a theorem whose conclusion is "no solution of class X
exists" as the paper's endpoint rather than a domain statement about its own constructed family.
Sections 5-7 contain no such theorem; the closest is footnote 10's characteristic-solution
warning, which motivates a construction repair, not an exclusion.
"""
import re, os, hashlib
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
SRC = os.path.join(ROOT, "bhu-reading-20260823/sources/math-ph_0302036_clean.txt")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

raw = open(SRC, errors="ignore").read()
S = " ".join(raw.split())          # squeeze whitespace incl. the ar5iv zero-width runs
nl = raw.count("\n") + 1
sha = hashlib.sha256(raw.encode()).hexdigest()[:12]

print("=" * 98); print("B43 -- entry 38 full read under the census rule"); print("=" * 98)
print(f"\n  source: {os.path.basename(SRC)}  lines={nl}  sha256={sha}")

chk("SOURCE: the pinned file is the MAA paper, complete through the reference list",
    "Shock Waves Beyond the Hubble Length" in S and "[24]" in S and "Weinberg" in S
    and nl > 3000)
chk("READ RECEIPT: the operative result is constructive -- the abstract opens with construction "
    "and Theorem 6 proves existence/uniqueness of the shock family",
    S.startswith("[math-ph/0302036]") and "We construct exact, entropy satisfying shock wave" in S
    and "there exists a unique solution" in S)
chk("CLAIM 1 (adjudicated in b32): the TOV-continuation sentence and its [15] delegation are in "
    "the source", "cannot be continued into a Black Hole" in S and "we proved this in" in S)
chk("CLAIM 2 (adjudicated in b32): the infinite-FRW aside is in the source",
    "the infinite FRW metric cannot be matched to the Schwarzschild metric" in S)
chk("CLAIM 3 (NEW from this read): Theorem 7's iff-subluminality and Theorem 8's light-speed "
    "trichotomy are in the source",
    "subluminous" in S and r"\sigma\leq 1/3" in S
    and r"\lim_{S\rightarrow 0}s_{\sigma}(S)=1" in S)
B = open(BIB).read()
chk("REPAIRED STATE: entry 38's record now carries the Theorem 7/8 constraint as claim item 3, "
    "in entry 37's claim-level style",
    "Theorem 8 proves the trichotomy" in B and "staying with the construction" in B)
# tier assertion scoped to entry 38's block, not the whole file
cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
m = re.search(r"Testability: \*\*([A-Z-]+)\*\*", blocks[38])
chk("TIER UNCHANGED: entry 38 remains CONSISTENCY-ONLY at paper level",
    m is not None and m.group(1) == "CONSISTENCY-ONLY")

print()
fails = [x for x, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
