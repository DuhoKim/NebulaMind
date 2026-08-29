#!/usr/bin/env python3
"""B39 -- entry 19 acquired by the browser route and adjudicated. Readable corpus: 38 -> 39.

ACQUISITION. Dymnikova 2019, Universe 5(5) 111, doi:10.3390/universe5050111 -- MDPI open access
(CC BY 4.0), Cloudflare-blocked to plain HTTP (403 on /htm and /pdf), captured via the browser in
a SINGLE get_page_text pass (the 25/26-era three-capture stitching was not needed) and pinned as
universe5050111_dymnikova2019_clean.txt. Identity: title, author, DOI, and dates all in the head.

SCREEN + ADJUDICATION per the Q1 protocol for new acquisitions. VERDICT (mine, to the gate):
NOT AN OBSTRUCTION -- a comparative survey-plus-calculation of quantum-birth probabilities inside
regular de-Sitter-core black holes, concluding the flat-universe birth is "the most plausible
case". Its enabling condition -- a barrier EXISTS ONLY WITH a negative-deficit-angle string
component (the k - B_s term) -- is the existence-CONDITIONAL shape that entries 52/53 taught this
lane to flag, so it is NAMED to the gate rather than waved through: my reading is that it is an
enabling mechanism inside a constructive probability comparison (the paper's point is that the
birth IS possible and more probable than from "nothing"), not a class exclusion, but 52/53 began
exactly this way.

BONUS RECEIPT: the paper INDEPENDENTLY CONFIRMS entry 49/48's attribution -- "Farhi and Guth
concluded that the initial singularity would be an unavoidable obstacle to the creation of a
universe in the laboratory [4]", with [4] = Phys. Lett. B 183, 149 -- exactly the ownership chain
CGATE_B30 established and the corpus could not verify because entry 48 is paywalled. A second
published source now testifies to what entry 48 proves.
"""
import re, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__))
D=os.path.abspath(os.path.join(_HERE,".."))
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))
T=" ".join(open(os.path.join(D,"bhu-reading-20260823/sources/universe5050111_dymnikova2019_clean.txt"),errors="ignore").read().split())
def norm(x): return re.sub(r"[^a-z0-9]","",x.lower())
print("="*98); print("B39 -- entry 19 acquired and adjudicated"); print("="*98)
chk("PINNED: the capture carries title, author, DOI and dates at head",
    "universesinsideablackholewiththedesitterinterior" in norm(T[:900]) and "10.3390/universe5050111" in T,
    "single-pass browser capture; CC BY 4.0 open access")
chk("SOURCE-READ: the operative conclusion is a plausibility COMPARISON, not an exclusion",
    "the most plausible case is the birth of a flat" in T,
    "and 'not negligible ... makes it possible to speculate (at least not exclude)' -- the paper "
    "argues FOR possibility throughout")
chk("SOURCE-READ: the existence-conditional (the barrier needs the string component) is present "
    "and is flagged to the gate rather than waved through",
    "provides the appearance" in T and "makes the quantum birth" in T,
    "the 52/53 lesson: 'exists only when' shapes get named, not pattern-cleared. My verdict is "
    "enabling-mechanism-inside-a-construction; the gate rules")
chk("RECEIPT: independent published confirmation of the entry 49 -> 48 proof-ownership chain",
    "unavoidable obstacle to the creation of" in T,
    "'Farhi and Guth concluded that the initial singularity would be an unavoidable obstacle' "
    "[4] = PLB 183, 149 = corpus entry 48, paywalled. A second source now testifies to its content")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
