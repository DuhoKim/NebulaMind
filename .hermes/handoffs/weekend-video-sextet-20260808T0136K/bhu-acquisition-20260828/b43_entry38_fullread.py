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

GATED 2026-08-30: CGATE_B43 ENTRY38_NARROWED_THEOREM8_STATEMENT_AND_SCOPE (independent full
sequential read; tier CONFIRMED; census reading coverage 39/39 CONFIRMED). Three narrowings,
all applied:
  1. claim item 3 re-scoped to the exact constant-sigma family (0<sigma<1) and now DISCLOSES
     Theorem 8's printed-hypothesis typo -- it opens "Let 0<sigma<=1/3" then immediately states
     the sigma>1/3 limb; the intended domain is Theorem 6's 0<sigma<1. I read past that defect;
     the gate did not.
  2. footnote 10's rejected characteristic branch (not a weak solution of G=kT for A<0) added
     to the record as methodological claim-level content I had inventoried but not recorded.
  3. the "READ RECEIPT" check RENAMED -- phrase presence cannot certify a human read; the read
     itself is testimony in this docstring, and the check below is only a landmark smoke test.
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
chk("LANDMARK SMOKE TEST (not a read certificate -- the read is testimony in the docstring): "
    "the operative result is constructive; abstract opens with construction and Theorem 6 "
    "proves existence/uniqueness",
    S.startswith("[math-ph/0302036]") and "We construct exact, entropy satisfying shock wave" in S
    and "there exists a unique solution" in S)
chk("CLAIM 1 (adjudicated in b32): the TOV-continuation sentence and its [15] delegation are in "
    "the source", "cannot be continued into a Black Hole" in S and "we proved this in" in S)
chk("CLAIM 2 (adjudicated in b32): the infinite-FRW aside is in the source",
    "the infinite FRW metric cannot be matched to the Schwarzschild metric" in S)
chk("CLAIM 3 (NEW from this read): Theorem 7's iff-subluminality and ALL THREE trichotomy limbs "
    "are in the source, plus the family domain",
    "subluminous" in S and r"\sigma\leq 1/3" in S
    and r"\lim_{S\rightarrow 0}s_{\sigma}(S)=1" in S
    and r"s_{\sigma}(S)=\infty" in S and r"s_{\sigma}(S)=0" in S and r"0<\sigma<1" in S)
chk("THEOREM 8 TYPO (CGATE_B43): the printed hypothesis 0<sigma<=1/3 and the sigma>1/3 limb "
    "coexist in the source -- the defect the record now discloses",
    S.count(r"0<\sigma\leq 1/3") >= 1 and r"\sigma>1/3" in S)
chk("FOOTNOTE 10 (CGATE_B43): the rejected everywhere-characteristic branch is in the source",
    "everywhere characteristic" in S and "does not represent an actual weak" in S)
B = open(BIB).read()
cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b38 = blocks[38]
chk("REPAIRED STATE, scoped to entry 38's block: claim item 3 carries the family scope, the "
    "Theorem 8 typo disclosure, and footnote 10's branch",
    "0 < σ < 1" in b38 and "disclosed rather than smoothed over" in b38
    and "everywhere characteristic" in b38 and "staying with the" in b38)
m = re.search(r"Testability: \*\*([A-Z-]+)\*\*", b38)
chk("TIER UNCHANGED: entry 38 remains CONSISTENCY-ONLY at paper level",
    m is not None and m.group(1) == "CONSISTENCY-ONLY")

print()
fails = [x for x, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
