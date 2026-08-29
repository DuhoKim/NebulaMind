#!/usr/bin/env python3
"""B22 -- the published case against entry 31, characterised. Three of four read.

SAME PROVENANCE LIMIT as b20/b21: all three are ADS image scans with no text layer, so every
characterisation here is transcription and reading of rendered pages. Not grep-verifiable.

Smolin 2004 §3: "Several arguments were made that S is in fact contradicted by present observation
[13,14,30,31]. These were found to depend either on confusions about the hypothesis itself or on
too simple assumptions about star formation."

WHAT THE FOUR ACTUALLY ARE:

  [13] Rothman & Ellis 1993, QJRAS 34, 201 -- "Smolin's Natural Selection Hypothesis".
       A direct critique. Core objection UNIDIRECTIONALITY: the scenario needs every parameter
       change to reduce black-hole counts, and raising alpha or M_LC does the opposite -- a "basic
       flaw". Twice concludes his result is "probably reversed". CONTAINS ONE OBSERVATIONAL
       REJECTION: cold/tepid-Big-Bang models, "in the wake of the COBE observations ... can almost
       certainly be pronounced dead." Closes endorsing the programme as "certainly worth pursuing".
       Gated b20; both seats verified every quotation.

  [14] Ellis 1993, QJRAS 34, 315 -- "The Physics and Geometry of the Universe: Changing
       Viewpoints". NOT A CRITIQUE OF SMOLIN. A review of five philosophical paradigms in
       cosmology, from a 1990 conference talk. It cites Smolin 1992 and Rothman & Ellis 1993 in
       its reference list, so it engages the idea, but its subject is the paradigms.

  [30] Harrison 1995, QJRAS 36, 193 -- "The Natural Selection of Universes Containing Intelligent
       Life". A RIVAL COSMOLOGY. Its objection to Smolin is in reference-note (11) and is
       TOPOLOGICAL: a closed universe recollapsing to one future singularity gives "at most one
       offspring universe". Body criticism at p. 196 is conceptual. Gated b21; both seats verified.

  [31] Silk, Science (1997) 644 -- PAYWALLED, UNREAD, and Smolin's volume number (227) is wrong;
       volume 227 is 1985, the 1997 volume is 277.
"""
import os, sys
S="../bhu-reading-20260823/sources/"
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B22 -- the published case against entry 31"); print("="*98)
PINS={"rothman_ellis_1993_qjras34_201.pdf":179670,
      "ellis_1993_qjras34_315.pdf":223655,
      "harrison_1995_qjras36_193.pdf":277259}
for f,sz in PINS.items(): print(f"   {f:<38} {sz:>7} b   {'pinned' if os.path.exists(S+f) else 'MISSING'}")
chk("ARTIFACT: three of the four criticisms are pinned at the sizes recorded when acquired",
    all(os.path.exists(S+f) and os.path.getsize(S+f)==sz for f,sz in PINS.items()),
    "the fourth, Silk 1997, is paywalled and was not attempted")

print("""
1. WHAT THE THREE PAPERS ATTACK -- narrowed by both seats, and one claim of mine is contested

   THEY ATTACK THE WARRANT, NOT THE MASS PHYSICS. CGATE, after reading all three: "I found no
   objection in the three pinned papers that bears on the content or empirical satisfaction of the
   2004 2.5 M_sun prediction itself." Rothman & Ellis attack the 1992 selection warrant; Ellis 1993
   points back to them; Harrison questions differential reproduction in a recollapsing closed
   universe.

   BUT "THEY DO NOT THREATEN ENTRY 31 AT ALL" IS THE WRONG PARAPHRASE, and my first draft made it.
   CGATE: they "weaken or condition the inference from 'a heavy neutron star exists' to
   'cosmological natural selection is false'". They do not say the bar is wrong; they question its
   force as a test.

   AND AGATE READS ONE PASSAGE AS GOING FURTHER. On pp. 210-211 Rothman & Ellis attack the claim
   that our universe sits at a local maximum with respect to M_LC, the mass limit for collapse,
   arguing that LOWERING it might INCREASE black holes. AGATE: because the 2.5 M_sun bar is derived
   from the assumption that easier collapse must decrease black holes, attacking that direction is
   an attack on the prediction itself. CGATE holds it is still warrant, not mass physics.
   THE SEATS DISAGREE, AND THE DISAGREEMENT IS FILED, NOT RESOLVED HERE.

   I HAD TRANSCRIBED "raising alpha or M_LC will work in the opposite direction" MYSELF IN B20 AND
   DID NOT CONNECT M_LC TO THE NEUTRON-STAR BAR. The material was in my own quotation.

2. ON SMOLIN'S CHARACTERISATION -- sharper now, and still short of an accusation

   [13] a direct heterogeneous critique with one observationally rejected limb;
   [14] NOT AN INDEPENDENT ATTACK -- both seats confirm. Ellis gives a FAVOURABLE exposition on
        p. 328, calling the idea capable of "uniting ideas from biology and physics in a powerful
        way", and delegates criticism in one clause: "not without problems (Rothman & Ellis 1993)";
   [30] a rival proposal with conceptual and topological objections;
   [31] unread, paywalled.

   SO THE CITATION IS COMPRESSED AND POTENTIALLY MISLEADING AS BIBLIOGRAPHY -- [14] contributes no
   independent argument at all. AGATE calls that an unambiguous mischaracterisation of that paper
   and says Silk need not be read. CGATE holds the collective sentence is not thereby proved false,
   since [13] carries both the observational and star-formation material Smolin invokes.
   ADOPTED: CGATE's narrower form. The record may say the references are heterogeneous and that
   [14] is not independently critical; it may NOT yet say Smolin mischaracterised the cited set.
   FOURTH TIME TONIGHT THE PULL RAN THIS WAY; the narrower form is the one that keeps surviving.

3. TWO FACTUAL DEFECTS IN THE FIRST DRAFT, both CGATE's, both mine

   "The record has no column for it" -- STALE. The bibliography now separates tier from standing in
   an explicit table, a change made EARLIER TODAY in this same lane. I wrote a sentence about the
   record's shape that my own edit had already falsified.

   And the draft asserted entry 31's LIVE standing as free prose. It is not this file's to
   adjudicate: PSR J0952-0607 sits below 2.5 M_sun on its quoted central value, GW190814 reaches
   the range with its secondary's identity unresolved, and the record separately tracks the weaker
   conditional 1.5 M_sun bar as already passed. These three 1990s papers adjudicate none of it.

4. NO TIER CHANGE IS MADE, AND THE SEATS DISAGREE ABOUT WHETHER ONE IS DUE.

   CGATE: tier confirmed -- "Entry 31 contains a numerical threshold and remains a
   CALIBRATED-FALSIFIER under the bibliography's claim-form taxonomy. An upstream challenge to the
   theoretical derivation is not evidence that the numerical bar has fired."

   AGATE: tier must fall -- "A theory cannot remain CALIBRATED-FALSIFIER if its own internal logic
   doesn't actually produce the falsifier. If the warrant is destroyed, the falsifier is lost."

   That is a substantive disagreement about a tier, which is twice over a stop condition. FILED IN
   OPEN_QUESTIONS_FOR_DUHO.md. Nothing is changed in the bibliography.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed   [provenance limit at the top governs the prose]")
sys.exit(0 if n==len(checks) else 1)
