#!/usr/bin/env python3
"""B24 -- warrant check on the corpus's ONE no-go entry, where warrant matters most.

WHY THIS ONE. Both seats refuted my claim that only calibrated falsifiers have warrants, naming
THEORETICAL-OBSTRUCTION as a class that can "rest on a disputed no-go". The corpus has exactly one
such entry, 22 (Easson 2026, PRD). AND A NO-GO IS NOTHING BUT ITS DERIVATION: a calibrated
falsifier survives a bad warrant as a number someone might still measure, but an obstruction whose
theorem is narrower than advertised has no residue at all. Source pinned: 2606.25023_clean.txt,
with a real text layer, so every quotation here is grep-verifiable.

THIS IS NOT A TIER QUESTION. Entry 22 is THEORETICAL-OBSTRUCTION and stays there. The question is
what its warrant cell should say if the axis is ever extended past the calibrated four.
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
chk("SOURCE: the theorem's own statement carries at least ten separate conditions on the parent, "
    "the boundary and the daughter",
    len(present) >= 10,
    f"{len(present)} of {len(COND)} found inside the 900 characters following 'Theorem 1'. A no-go "
    f"is exactly as wide as its assumptions, and these are not incidental -- they name the "
    f"construction class")

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
4. THE WARRANT CELL THIS ENTRY WOULD GET

   NOT "disputed" -- nothing in this corpus challenges the derivation, and I have not searched the
   literature. NOT "sound" either, which would be a claim about the mathematics I have not checked.

   WHAT IS ESTABLISHED: the obstruction is REAL BUT NARROW, and its narrowness is the author's own,
   stated in his title and in three explicit "no additional ..." clauses. A regular-black-hole
   cosmology carrying a shell stress tensor, a late-time bulk component, or modified asymptotics is
   OUTSIDE Theorem 1 by construction.

   So the honest cell is: "SCOPE-LIMITED BY CONSTRUCTION -- eleven stated conditions, three of them
   explicit exclusions; the author's own title says 'minimal'. Derivation not independently
   checked."

5. A FOLLOW-UP I AM NAMING AND NOT INVESTIGATING

   This corpus's largest interior-matching series uses Israel junction conditions, which concern
   shells. Easson's Theorem 1 assumes NO-SHELL matching. WHETHER ANY CORPUS ENTRY FALLS INSIDE OR
   OUTSIDE THIS NO-GO IS THEREFORE A REAL QUESTION -- and I am not answering it here.

   I proposed a cross-entry link once tonight already (b21, entries 31 and 54) and both seats
   refuted it on a distinction I had not checked. The same shape is present here: two things I
   read the same evening, a tidy connection, and no verification. It is recorded as a question.

6. NO TIER CHANGE. Entry 22 stays THEORETICAL-OBSTRUCTION.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
