#!/usr/bin/env python3
"""B20 -- Rothman & Ellis 1993 is now READ. Entry 31 said it was not.

GATED 2026-08-29:
  AGATE_B20  TRANSCRIPTION_CONFIRMED
  CGATE_B20  TRANSCRIPTION_NARROWED_MISSED_COBE_CONFRONTATION

BOTH SEATS RENDERED THE SCAN AND CHECKED EVERY QUOTATION WORD BY WORD. All four are accurate;
CGATE independently reproduced the sha256 in full. So the transcription discipline held -- which
matters, because it was the only thing standing in for a grep.

WITHDRAWN: "it is a conceptual objection, NOT a confrontation with data". FALSE. Page 209 confronts
Smolin's cold/tepid-Big-Bang limb with observation: such models "in the wake of the COBE
observations ... can almost certainly be pronounced dead." I read pages 1, 2 and 11 and skimmed the
rest, and the confrontation is in the part I skimmed. BOTH seats found it -- CGATE as a refutation
of my claim, AGATE while calling my characterisation fair anyway.

ALSO MISSED, all from pages I skimmed (CGATE): for dm = 0 the authors say our universe would
probably have MORE black holes, "in contradiction to his hypothesis"; for dm < 0 and for the
opposite extreme they twice conclude Smolin's result is "probably reversed"; and they call
unidirectionality a "basic flaw in Smolin's scenario". The paper attacks the concrete arguments far
harder than my summary allowed.

Entry 31's note: "cites Rothman & Ellis (1993) [13] as the source of the open-universe correction
-- corroborating appendix A0's citation trail (their paper itself remains unread)". It is read now.

################################################################################################
#  PROVENANCE LIMIT, STATED FIRST BECAUSE IT WEAKENS EVERY QUOTE BELOW.
#
#  The ADS scan is JBIG2 images with NO TEXT LAYER -- its only extractable text is the bibcode
#  stamp repeated once per page. So THE QUOTES IN THIS FILE ARE TRANSCRIBED BY ME FROM RENDERED
#  PAGE IMAGES, and this lane's usual predicate -- grep the source for the string -- CANNOT BE
#  APPLIED. The checks below verify the artifact (existence, hash, page count, absence of a text
#  layer); they CANNOT verify a quotation.
#
#  That is a real weakening and it is not fixable with the tooling here. Treat every quotation
#  below as testimony of mine, at the same standing as a seat's testimony -- not as a receipt.
################################################################################################
"""
import fitz, hashlib, os, sys
S="../bhu-reading-20260823/sources/"
F=S+"rothman_ellis_1993_qjras34_201.pdf"
BIB=open("../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md").read()
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B20 -- Rothman & Ellis 1993, read"); print("="*98)
raw=open(F,"rb").read(); d=fitz.open(F)
txt="".join(p.get_text() for p in d)
print(f"\n  {os.path.basename(F)}  {len(raw)} b  sha256 {hashlib.sha256(raw).hexdigest()[:12]}  "
      f"{d.page_count} pp")
SHA="ad76b7ace95cb173e961fe0cc6abb014cf44a776dbda0eee13e1d90ecfd3ae70"
chk("ARTIFACT: the file's sha256 is COMPARED against the expected digest, not merely printed",
    hashlib.sha256(raw).hexdigest()==SHA and d.page_count==12 and len(raw)==179670,
    "CGATE: the earlier version's name said the paper 'hashes' while the predicate never compared "
    "the digest to anything. CGATE reproduced it independently and it is now pinned in the code")
chk("ARTIFACT: the scan carries NO usable text layer, which is why the quotations below cannot be "
    "grep-verified and are labelled testimony",
    len(txt.strip()) < 300 and txt.count("1993QJRAS..34..201R")==12,
    f"{len(txt.strip())} extractable characters, and the predicate now CHECKS that they are the ADS "
    f"bibcode repeated once per page rather than asserting it. CGATE flagged that the detail made a "
    "claim the test did not make")

print("""
1. WHAT THE PAPER IS -- title and framing, transcribed

   "Smolin's Natural Selection Hypothesis", T. Rothman and G.F.R. Ellis, Q. J. R. astr. Soc.
   (1993) 34, 201-212. Summary: "Smolin's considerations do, however, appear to contain a number
   of conceptual and technical flaws, which we point out in this paper."

   IT TARGETS SMOLIN 1992, WHICH IS ENTRY 6 -- not entry 31 (Smolin 2004). The record files this
   citation under entry 31 because Smolin 2004 answers it, but the object of the critique is the
   earlier paper. That distinction is not currently drawn anywhere.

2. THE CENTRAL OBJECTION -- and it is not observational

   "Smolin's scenario, however, requires that changing parameters in either direction decreases
   the number of black holes. But, clearly, raising alpha or M_LC will work in the opposite
   direction ... In general, it is difficult to think of any parameter change that works in only
   one direction."

   This is a UNIDIRECTIONALITY objection to the selection argument itself, and CGATE quotes the
   authors calling it a "basic flaw in Smolin's scenario". THE SENTENCE THAT FOLLOWED HERE -- "it
   is conceptual, not a confrontation with data" -- IS WITHDRAWN; see the header.

3. THEY REQUIRE CNS TO EXCLUDE PRIMORDIAL BLACK HOLES

   "the primary requirement at this stage is a mechanism to exclude primordial black holes from
   the proposal" -- and they suggest a mass-dependent tunnelling rate, noting "it would at least
   exclude microscopic black holes."

   Recorded because it touches tonight's other work on entry 51's minimum-mass floor. NO
   CONNECTION IS CLAIMED between the two; they are different arguments by different authors, and
   asserting a link is exactly the tidy-story move that produced defect 1z.

4. THEIR VERDICT IS CONSTRUCTIVE, NOT A REFUTATION

   "in view of the power of the process of natural selection as a mechanism for creating apparent
   design ... the programme is certainly worth pursuing in the broad context outlined by Smolin."

5. WHAT THIS MEANS FOR THE RECORD -- carefully, because over-attribution is easy here

   Smolin 2004 groups four references as "arguments ... that S is in fact contradicted by present
   observation [13,14,30,31]". I claimed [13] "as read is not that". WITHDRAWN -- page 209's COBE
   passage IS an observational rejection, of the cold/tepid-Big-Bang limb.

   THE RESTRAINT SURVIVES, ITS PREMISE DOES NOT. Both seats agree that nothing can be concluded
   about Smolin's four-way characterisation until [14] Ellis 1993, [30] Harrison 1995 and [31] Silk
   1997 are read -- Ellis and Harrison pinned tonight, Silk paywalled. But CGATE is right that I
   reached that correct restraint from a false premise. What [13] establishes, precisely: an
   observational rejection of ONE limb, not of CNS as a whole.

   AND THE OBJECTION SITS UPSTREAM OF ENTRY 31'S FALSIFIER. The 2.5 M_sun bar tests whether a
   prediction of the selection argument holds; unidirectionality asks whether the argument delivers
   a prediction at all.

   THE SEATS SPLIT ON HOW HARD TO PUT THIS AND I TOOK THE WEAKER FORM. AGATE: "unmoored" is "the
   correct description ... the observational falsifier would thus be severed". CGATE: too strong
   without a parameter-specific derivation, because Rothman & Ellis analyse Smolin 1992's examples
   and never touch the 2004 mass argument; the defensible claim is that the bar's selection-
   theoretic WARRANT is "weakened or made conditional, not that it has no mooring at all".
   ADOPTED: CGATE's. Declining the stronger form of my own inference is not adjudicating between
   seats -- it is the same call made on b13 tonight, and for the same reason.
""")
chk("RECORD: entry 31 now records this paper as READ, with its hash, and no longer calls it "
    "unread",
    "rothman_ellis_1993_qjras34_201.pdf" in BIB and "their paper\nitself remains unread" not in BIB,
    "the earlier predicate tested for 'remains unread' ANYWHERE in the file. That string occurs "
    "TWICE -- entry 31's and an unrelated one at line 121 -- so it would have passed unchanged "
    "after the repair. Now it tests entry 31's exact sentence and the presence of the artifact")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed   [and see the provenance limit at the top]")
sys.exit(0 if n==len(checks) else 1)
