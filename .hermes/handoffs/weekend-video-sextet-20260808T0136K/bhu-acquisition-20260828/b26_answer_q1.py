#!/usr/bin/env python3
"""B26 -- question 1.  GATED, REFUTED ON ITS CENTRAL REASONING, AND REWRITTEN.

  AGATE_Q1  Q1_ANSWER_REFUTED_COUNT_AND_REASONING
  CGATE_Q1  Q1_ANSWER_REFUTED_UNMEASURED_RECALL_CANNOT_LICENSE_SCREEN

FOUR WITHDRAWALS. This was my fourth answer to a delegated question and the first refuted outright.

1. THE COUNT. I said 18 papers have no text, from parsing the SOURCE MAP. The map is not the
   filesystem, and my parser was wrong in BOTH directions -- all three defects verified here:
     - entry 56 has a 775,903-byte published MNRAS PDF in the sources directory; the map never
       indexes it (CGATE)
     - entry 5 has arxiv-1412.0105v1.pdf AND a text extraction under reviews/; unmapped (CGATE).
       My first attempt to check this used a path that resolved outside the repo and "confirmed"
       only abstract files -- my own path error nearly rejected a correct finding
     - the map's correction table has a FILENAME in its first cell, `1111.1017_clean.txt`, and my
       unanchored \\d{1,2} pulled "17" out of it, registering entry 17 as pinned (AGATE)
   AN EXACT COUNT NEEDS A REPO-WIDE FILESYSTEM AUDIT AND IS NOT DONE HERE. What is established:
   at least two "unpinned" papers are readable, at least one "pinned" one is not, and the map
   cannot be used as an index of what can be read.

2. "A VERIFIED SCREEN IS SAFE AT ANY PRECISION." FALSE, and it was the load-bearing claim.
   It conflates precision, flag rate and recall. Hand-checking stops a false positive being FILED
   -- subject to reviewer error -- and does nothing about a false negative sitting silently in its
   old tier. CGATE's model: screening saves effort only when s*N < c*(N-F), where F is the flag
   count. At 30 flags of 33 the saving is three reads before overhead; at F=N it is negative. My
   "precision only determines wasted reading" was true only because F=3 TODAY, which is a fact
   about the current queue and not a theorem.

3. "RECALL CANNOT BE MEASURED HERE." FALSE, and AGATE calls it an abdication. It can be measured
   by hand-auditing a random sample of the UNFLAGGED papers, blinded to screen status. CGATE
   supplies the power curve, which is the actual cost-completeness trade Duho was asked about:
     auditing 10 of 30 unflagged, finding nothing -> still 66.7% chance of missing one hidden case
     >=95% chance of catching one when 6/30 are hidden -> 11 reads
     same confidence when 3/30 are hidden           -> 19 reads
     for a single hidden case                       -> 29 reads, essentially a census
   So a cheap sample exposes a GROSS failure; a strong guarantee costs nearly full hand-sorting.
   I converted "not yet measured, expensive to bound tightly" into "cannot be measured" and
   thereby erased the middle ground the question is about.

4. "NO TIER MOVED." Context-free and misleading. Entry 22 DID move earlier, from CONSISTENCY-ONLY
   into the obstruction tier. The defensible claim is that THIS screen-and-check pass caused no
   ADDITIONAL move.

WHAT SURVIVED: the three current flags have all been read, and the two false positives were not
filed (both seats confirm). And the acquisition observation is real -- but it is an ADDITIONAL
workstream, not a substitute for the answer. Both seats called the substitution an evasion.
"""
import re, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__))
D=os.path.abspath(os.path.join(_HERE,".."))
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B26 -- question 1 [REFUTED AND REWRITTEN]"); print("="*98)

print("\n1. THE MAP IS NOT THE FILESYSTEM -- all three parser defects, verified on disk")
e56=os.path.join(D,"bhu-reading-20260823/sources/gaztanaga_mass_mnras.pdf")
e5 =os.path.join(D,"reviews/bhu-citation-custody-evidence-20260811/arxiv-1412.0105v1.pdf")
e5t=os.path.join(D,"reviews/bhu-citation-custody-evidence-20260811/arxiv-1412.0105v1.txt")
print(f"   entry 56 PDF : {os.path.exists(e56)}  {os.path.getsize(e56) if os.path.exists(e56) else 0:,} bytes")
print(f"   entry  5 PDF : {os.path.exists(e5)}  {os.path.getsize(e5) if os.path.exists(e5) else 0:,} bytes")
print(f"   entry  5 txt : {os.path.exists(e5t)}  {os.path.getsize(e5t) if os.path.exists(e5t) else 0:,} bytes")
chk("VERIFIED ON DISK: papers my parser reported as having no source are readable, so the count "
    "I gave Duho was false and the map cannot serve as an index of what can be read",
    os.path.exists(e56) and os.path.exists(e5) and os.path.exists(e5t),
    "CGATE found both. My own first check of entry 5 used a path that resolved OUTSIDE the repo and "
    "reported only abstract files -- I nearly rejected a correct refutation with a path error, "
    "which is the fifth path error in this lane today")
M=open(os.path.join(D,"bhu-theory-phase6-curvature-20260827/ENTRY_SOURCE_MAP.md")).read()
chk("VERIFIED: the map's correction table puts a FILENAME in its first cell, which an unanchored "
    "two-digit match reads as an entry number",
    "| `1111.1017_clean.txt` |" in M,
    "AGATE: my regex pulled '17' from the filename and registered entry 17 as pinned. Wrong in the "
    "opposite direction from CGATE's two -- the parser erred both ways at once")

print("""
2. THE ANSWER, AT THE WIDTH BOTH SEATS ALLOW

   USE THE SCREEN AS A FIRST PASS AND HAND-CHECK EVERY FLAG -- WITH TWO CONDITIONS I DID NOT
   ORIGINALLY ATTACH, both of which are the seats':

     (a) A FLAG-VOLUME STOP RULE. The screen is worth running only while the flag count stays well
         below the paper count; at high flag rates "check every flag" IS hand-sorting, plus
         overhead. Today it is 3 flags, which is comfortably affordable. That is a fact about
         today, and the rule is what makes it safe tomorrow.

     (b) A RECALL PLAN, OR AN EXPLICIT ACCEPTANCE OF THE RISK. Positive verification of flags does
         nothing about what the screen misses. Either run the blinded random audit of unflagged
         papers -- 11 reads to catch a 20% miss rate at 95%, 19 for 10%, ~29 for a single case --
         or record that Duho is accepting an unquantified completeness loss. CGATE: "absence of
         evidence that recall is bad is not evidence that recall is acceptable."

   AND SEPARATELY, NOT INSTEAD: some papers cannot be classified by anyone until they are acquired.
   That queue is real and is its own workstream. Presenting it as the answer was an evasion and
   both seats said so.

3. WHAT IS ACTUALLY COMPLETE: the three current flags are read, the two false positives were not
   filed, and this pass moved nothing. A re-sort is NOT complete until the unflagged set is either
   audited to a stated tolerance or the risk is explicitly accepted.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
