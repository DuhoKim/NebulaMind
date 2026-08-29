#!/usr/bin/env python3
"""B24 -- warrant check on the corpus's ONE no-go entry.  GATED, and I was unfair to the paper.

  AGATE_B24  SCOPE_REFUTED_INFLATED_COUNT_AND_HOSTILE_FRAMING
  CGATE_B24  SCOPE_NARROWED_COUNT_AND_CELL

WITHDRAWN #1 -- THE COUNT. I said Theorem 1 carries ELEVEN conditions and called the count honest
because it was mechanical. It was mechanical and wrong: I counted PHRASES, not assumptions.
"Darmois boundary", "no-shell" and "no independent shell stress tensor" are the same physical
requirement stated three ways; "asymptotically flat" and "no modified asymptotics" are one boundary
condition stated twice. CGATE enumerates EIGHT hypothesis groups for the closed branch; AGATE puts
the independent physical assumptions at four or five. Adopted: eight, with CGATE's caveat that no
number here is canonical -- and the point stands that eleven overstates independence.

WITHDRAWN #2 -- THE FRAMING. "Real but narrow" is damning ordinary rigour with scope. The paper
ADVERTISES its narrowness in its own title, defines "minimal" in its introduction, and repeatedly
says it does not exclude more elaborate constructions. Stating hypotheses is what a theorem is.
CGATE's replacement, adopted: "explicitly scope-bounded, with structurally broad results inside
each stated branch."

WITHDRAWN #3 -- THE FOLLOW-UP I FLAGGED. I suggested this corpus's interior-matching series might
fall OUTSIDE the no-go because it uses Israel junction conditions while Theorem 1 assumes no-shell.
FALSE, and verified false against the sources rather than accepted from a seat:
  - Easson himself cites Israel and calls his own conditions "the Darmois-Israel NO-SHELL
    conditions". Using Israel formalism does not mean carrying a shell.
  - 2505.23877 says outright: "No additional surface term or exotic matter layer is required."
THE SEATS SPLIT HERE -- AGATE called it a real gap, CGATE called it false -- and this is NOT a
substantive disagreement to escalate: AGATE reasoned from the general formalism, CGATE checked the
pinned text, and the pinned text settles it. I checked it myself before writing this.

AND I DID NOT READ THE PROPOSITIONS. CGATE did. Proposition 1 needs no matching, no asymptotics and
no shell assumption at all; Proposition 2 is independent of the regular core and survives a static
redshift function, so it is LESS restricted than Theorem 1's headline. My "narrow" gloss was built
on the one part of the paper I had read.

WHAT SURVIVES: the escape routes are real (both seats), and the record still does not say anywhere
a reader would meet it WHICH class the no-go covers. That was the finding worth having.
"""
import re, sys
T=" ".join(open("../bhu-reading-20260823/sources/2606.25023_clean.txt",errors="ignore").read().split())
BIB=open("../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md").read()
# whitespace-normalised: two predicates below failed on strings that span a line break in the
# source file. Matching literal text against wrapped markdown is a recurring own-goal here.
BIBN=" ".join(BIB.split())
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B24 -- entry 22's no-go: how wide is it really?"); print("="*98)

print("\n1. THE THEOREM IS HEAVILY CONDITIONED -- eleven clauses, counted not eyeballed")
COND=["static","spherically symmetric","asymptotically flat","one-function class",
      "finite ADM mass","nondegenerate comoving spherical Darmois boundary","no-shell",
      "fixed by the parent metric profile","no additional late-time bulk component",
      "modified asymptotics","independent shell stress tensor"]
i=T.find("Theorem 1 (Minimal asymptotically flat FRW daughters)")
stmt=T[i:i+900]
present=[c for c in COND if c in stmt]
for c in COND: print(f"   {'YES' if c in stmt else 'no ':<4} {c}")
chk("LEXICAL: eleven distinct condition-PHRASES appear in the theorem statement -- a fact about "
    "wording, not about independent hypotheses",
    len(present) >= 10,
    f"{len(present)} of {len(COND)} PHRASES found inside the 900 characters following 'Theorem 1' "
    f"-- and PHRASES ARE NOT ASSUMPTIONS. Both seats refuted the count: CGATE enumerates eight "
    f"hypothesis groups, AGATE four or five independent physical assumptions. This check now "
    f"reports a lexical fact and its name says so")
chk("MEASURED: the phrase count exceeds every assumption count either seat arrived at, which is the "
    "defect rather than the finding",
    len(present) > 8,
    "11 phrases against 8 groups (CGATE) and 4-5 physical assumptions (AGATE). I called the count "
    "honest BECAUSE it was mechanical; mechanical counting of the wrong objects is not rigour")

print("\n2. THREE OF THEM ARE ESCAPE HATCHES THE AUTHOR NAMES HIMSELF")
chk("SOURCE: the theorem explicitly excludes three additions, so a model carrying any of them is "
    "outside the obstruction by the author's own wording",
    "no additional late-time bulk component, modified asymptotics, or independent shell stress "
    "tensor" in T,
    "'Assume that the matching is no-shell and that the daughter evolution is fixed by the parent "
    "metric profile, with no additional late-time bulk component, modified asymptotics, or "
    "independent shell stress tensor.' Each 'no additional X' is a named way out")
chk("SOURCE: and the paper scopes itself in its own title -- the obstruction is to MINIMAL "
    "constructions",
    "Obstructions to Minimal Regular Black Hole Cosmologies" in BIBN and "minimal" in T.lower(),
    "the word is the author's, in the title, and it is doing work: 'minimal' is what the eleven "
    "conditions add up to")

print("\n3. WHAT THE RECORD SAYS, AND WHETHER IT MATCHES")
chk("RECORD: the tier definition is correctly scoped -- it says a SPECIFIED class and a SPECIFIED "
    "conjunction, not that regular black hole cosmologies are impossible",
    "no member of a specified class of models can satisfy a specified conjunction of conditions" in BIBN,
    "so the definition is honest. The gap is elsewhere: WHICH class and WHICH conjunction is "
    "nowhere stated in the entry, so a reader meets a no-go without its scope")

print("""
4. THE WARRANT CELL, IN CGATE's WORDING RATHER THAN MINE

   "EXPLICITLY DOMAIN-BOUNDED -- Proposition 1 excludes identifying the natural trapped slicing with
   exact FRW; Proposition 2 bounds nondegenerate comoving no-shell closed-FRW daughters of static
   asymptotically flat finite-ADM parents; the flat/open limb additionally assumes curvature
   regularity, regular affine ends and ANEC. Shells, modified asymptotics, non-FRW/non-comoving
   evolution, or added bulk stress-energy are expressly outside the result. Proof skeleton checked
   against the source; external completeness theorem not independently verified."

   CGATE's ruling on why mine had to go: "scope is not a warrant defect unless the bibliography has
   advertised a broader conclusion than the source proves." IT HAS NOT -- check 4 below confirms the
   tier definition is honest. So there was never a warrant defect here to find, and I went looking
   for one anyway.

5. WHAT THE RECORD SHOULD ACTUALLY GAIN

   Not a warrant flag. The gap is narrower and duller: the entry says the tier asserts "no member of
   a specified class ... can satisfy a specified conjunction", and never says WHICH class or WHICH
   conjunction. A reader meets a no-go with no domain attached. The cell above supplies it.

6. NO TIER CHANGE. Entry 22 stays THEORETICAL-OBSTRUCTION.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
