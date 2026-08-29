#!/usr/bin/env python3
"""B19 -- the adversarial literature on the corpus's live falsifier is not in the corpus.

FOUND BY b18, the source-level sweep, as a by-product. b18 was hunting self-admitted firings and
found none beyond entry 44. But one of its three false positives was informative:
smolin_2004_cns_clean.txt matched on "Several arguments were made that S is in fact contradicted by
present observation [13,14,30,31]".

That is not a firing -- Smolin is REBUTTING those arguments, in a section titled "Answers to
criticisms". But it means the corpus's one live BHU-bearing calibrated falsifier has published
observational challenges, named in its own pinned source, and our record does not carry them AS
challenges.

WHAT THIS FILE IS: a receipt that the gap exists, built from Smolin's own reference list, which is
pinned. WHAT IT IS NOT: an assessment of whether the criticisms are any good. None of the four is
in this corpus and none has been read.
"""
import re, sys, os
S="../bhu-reading-20260823/sources/"
B="../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md"
T=" ".join(open(S+"smolin_2004_cns_clean.txt", errors="ignore").read().split())
BIB=open(B).read()
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B19 -- entry 31's published critics are absent from the record"); print("="*98)

print("\n1. THE SOURCE SAYS THEY EXIST, AND NAMES THEM")
chk("SOURCE: Smolin 2004 states that published arguments claim his hypothesis is contradicted by "
    "observation, and devotes a section to answering them",
    "contradicted by present observation" in T and "Answers to criticisms" in T,
    "'Several arguments were made that S is in fact contradicted by present observation "
    "[13,14,30,31]. These were found to depend either on confusions about the hypothesis itself or "
    "on too simple assumptions about star formation.' Section 3 is titled 'Answers to criticisms'")

refs = {"13":"A. Rothman, G.G.R. Ellis, Q. J. R. Astron. Soc. 34 (1993) 201",
        "14":"G.F.R. Ellis, Q. J. R. Astron. Soc. 34 (1993) 315-330",
        "30":"E.R. Harrison, 'The natural selection of universes containing intelligent life', "
             "R.A.S. Q. J. 36 (3) (1995) 193",
        "31":"J. Silk, Science 227 (1997) 644"}
print("\n2. THE FOUR, FROM SMOLIN'S OWN REFERENCE LIST")
for k,v in refs.items(): print(f"   [{k}]  {v}")
chk("SOURCE: all four references resolve in the pinned reference list, so this is a receipt rather "
    "than my reconstruction",
    all(v.split(",")[0].split(".")[-1].strip() in T for v in refs.values()) and
    "Q. J. R. Astron. Soc. 34 (1993) 201" in T and "Science 227 (1997) 644" in T,
    "each is read out of smolin_2004_cns_clean.txt's bibliography, not supplied from memory")
chk("MEASURED: all four are peer-reviewed journal publications, which is this lane's base-layer "
    "bar for a target",
    all(j in T for j in ("Q. J. R. Astron. Soc.","R.A.S. Q. J.","Science 227")),
    "QJRAS x2, RAS QJ, Science. None is a preprint or a popular treatment")

print("\n3. WHAT THE RECORD CARRIES")
roth = len(re.findall("Rothman", BIB)); harr = len(re.findall("Harrison", BIB))
silk = len(re.findall("Silk", BIB)); crit = len(re.findall("Answers to criticisms", BIB))
print(f"   'Rothman' in the bibliography            : {roth}")
print(f"   'Harrison'                               : {harr}")
print(f"   'Silk'                                   : {silk}")
print(f"   'Answers to criticisms'                  : {crit}")
# THIRD 1ab INSTANCE TONIGHT, and the one that taught the most. This asserted harr == 0 --
# "Harrison does not appear in the bibliography at all" -- which was TRUE when written and became
# false the moment I cited him in entry 31's note. Inverting it to "Harrison IS now cited" would
# have created a FOURTH instance, because he is pinned-but-unread and I intend to read him.
# THE ONLY STABLE THING TO ASSERT IS THE DURABLE ARTIFACT. The finding belongs in prose.
HARR_PDF = "../bhu-reading-20260823/sources/harrison_1995_qjras36_193.pdf"
chk("ARTIFACT: Harrison 1995 is pinned as a file, which stays true whether or not it has been "
    "read and whether or not the record cites it",
    os.path.exists(HARR_PDF) and os.path.getsize(HARR_PDF) == 277259,
    f"277,259 b. FINDING, kept as prose because it is history rather than a testable state: when "
    f"this file was written Harrison appeared NOWHERE in the bibliography, though he is one of the "
    f"four papers Smolin answers in a record that classes Smolin's paper as a live calibrated "
    f"falsifier. He is now named in entry 31 and pinned. HE IS STILL UNREAD")
# INVERTED 2026-08-29, ~90 minutes after writing it. The second half asserted the entry SAYS the
# paper is unread -- true when written, false the moment b20 read it. That is defect 1ab exactly,
# committed by me AFTER registering 1ab. See the register entry, which now records the recurrence.
chk("MEASURED: Rothman & Ellis is still cited in entry 31 for the open-universe correction, AND "
    "the entry no longer calls it unread -- so this file tests the repaired state, not the wound",
    "the source of the open-universe correction" in BIB and
    "their paper\nitself remains unread" not in BIB,
    "when this file was written the entry read '... (their paper itself remains unread)'. It now "
    "carries the reading, the hash and the gate verdicts. Entry 6 mentions "
    "'the Delta-m sign argument Rothman-Ellis attacked' -- so the adversarial role IS known "
    "somewhere in the record, and is not attached to the entry it bears on")

print("""
4. WHY THIS MATTERS MORE THAN AN ORDINARY MISSING CITATION

   Entry 31 is the corpus's one LIVE calibrated falsifier that bears directly on a
   black-hole-universe theory. Its standing is the single most load-bearing judgement in the
   record. And the record establishes that standing from the proponent's paper, while four
   published papers arguing the opposite are named IN THAT SAME PAPER and appear in our
   bibliography either in an unrelated role or not at all.

   Smolin rebuts them, and his rebuttal may well be right. THAT IS NOT THE POINT. The point is
   that the record cannot say whether it is right, because it has read one side.

   THIS IS THE SAME SHAPE AS ENTRIES 51 AND 54, and it is now the fourth instance: a claim about
   the outside world carried without the source that would let anyone check it. There it was an
   uncited experimental result; here it is an uncited body of criticism.

5. WHAT IS NOT CLAIMED

   Nothing here says the criticisms are good, or that entry 31's tier should move. None of the
   four has been read. NO TIER CHANGE IS PROPOSED. What is established is that four named,
   peer-reviewed challenges to the corpus's flagship falsifier are unpinned and unread, and that
   acquiring them is the obvious next receipt.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
