#!/usr/bin/env python3
"""B25 -- observed precision of the obstruction screen ON THE CURRENTLY PINNED SUBSET.
EVIDENCE FOR QUESTION 1. NOT A CORPUS-WIDE FIGURE, AND NOT NEUTRAL -- see the honesty note.

GATED 2026-08-29 and corrected on four counts:
  AGATE_B25  PRECISION_REFUTED_ARTEFACT_AND_HONESTY
  CGATE_B25  PRECISION_NARROWED_CURRENT_SUBSET_ONLY

WHAT SURVIVED: b1's printed "flags 4 of 29 sources and only 1 is correct" IS STALE. Both seats
re-ran its criterion independently on the current pool and both got the same SIX files that its own
live loop emits, while its prose and check name stay fixed at four.

WHAT WAS CORRECTED:
  1. I HARDCODED THE FLAGGED LIST from b1's earlier printout. CGATE: "A newly pinned file or
     criterion edit can otherwise leave all four B25 predicates green while its precision is wrong."
     This file now RE-RUNS the criterion.
  2. MY POPULATION SPLIT WAS WRONG. I said 27 corpus / 14 receipts. Entries 9 and 11 map to
     `../bhu-podcasts-20260820/arxiv_1007.0587.txt` and `..._1410.3881.txt`, and copies of both sit
     in the sources directory -- my parser required a backticked name ending `_clean.txt` and missed
     them. Verified directly. The split is at least 29 corpus / at most 12 receipts.
  3. THE "IMPROVEMENT" MAY BE A COMPOSITION EFFECT, NOT A PROPERTY OF THE SCREEN. AGATE: the
     excluded receipts are long collaboration and review texts whose sheer volume of "assume that",
     "cannot be" and "unless" language nearly guarantees tripping a word counter. Removing the
     longest documents is not evidence the screen filters theory papers well. Length is measured
     below instead of argued about.
  4. "DECIDES NOTHING" WAS NOT HONEST ENOUGH. Both seats. The file supplies directional evidence
     favouring one side of a live decision and told Duho to rule on its number. Both figures are
     now given equal billing, with which side each favours stated.

AND THE GROUND TRUTH IS A CONVENTION, NOT A MEASUREMENT. CGATE found an arguable local no-go inside
entry 25 -- its introduction argues a static interior of regular matter or radiation cannot exist
because the Buchdahl radius exceeds the Schwarzschild radius. Under PAPER-level labelling entry 25
is a false positive; under CLAIM-level labelling precision would be 2/3. The convention is stated
below rather than hardcoded silently.

RECALL IS UNMEASURED. Nothing here tests what the screen MISSES.
"""
import re, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__))
S=os.path.join(_HERE,"../bhu-reading-20260823/sources/")
MAP=os.path.join(_HERE,"../bhu-theory-phase6-curvature-20260827/ENTRY_SOURCE_MAP.md")
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

# --- b1's criterion, reproduced verbatim from b1_theoretical_obstruction_tier.py -----------------
IMPOSSIBILITY = r"cannot be both|cannot be\b|can not be\b|does not yield|no .{0,30}(?:can|exists?)\b|impossible|obstruct\w*|must give up|prevents?\b"
DOMAIN        = r"[Cc]onsider a .{0,80}(?:spacetime|metric|parent|class|solution)|[Aa]ssume that|under the (?:same )?assumptions?|hypothes[ei]s"
REFUTABLE     = r"escape|evasion|requires? an? (?:additional|extra)|must give up at least one|unless"
def is_obstruction(T):
    return (len(re.findall(IMPOSSIBILITY,T))>=5 and len(re.findall(DOMAIN,T))>=2
            and len(re.findall(REFUTABLE,T))>=2)

# --- map: accept ANY row whose first cell is an entry number and which names a file --------------
f2e={}
for line in open(MAP).read().splitlines():
    if not line.startswith("|"): continue
    cells=[c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells)<3: continue
    nums=re.findall(r"\d{1,2}", cells[0].replace("~",""))
    if not nums: continue
    for m in re.finditer(r"`([^`]+)`", line):                    # any backticked path
        base=os.path.basename(m.group(1))
        stem=re.sub(r"^arxiv_|_clean\.txt$|\.txt$","",base)      # CGATE: cross-directory rows
        f2e.setdefault(stem, nums[-1])

allsrc=sorted(f for f in os.listdir(S) if f.endswith("_clean.txt"))
def stem_of(f): return f[:-len("_clean.txt")]
entry_src=[f for f in allsrc if stem_of(f) in f2e]
receipts=[f for f in allsrc if stem_of(f) not in f2e]

print("="*98); print("B25 -- observed precision on the CURRENTLY PINNED subset  [GATED]"); print("="*98)
print(f"\n  pinned sources now : {len(allsrc)}   (b1's prose says 29)")
print(f"  identified corpus  : {len(entry_src)}")
print(f"  unmapped/receipts  : {len(receipts)}")
chk("PARSED: the map parse now recovers entries whose rows point at files in ANOTHER directory, "
    "which the first version missed and mischaracterised as receipts",
    "1007.0587" in f2e and "1410.3881" in f2e,
    f"entries {f2e.get('1007.0587')} and {f2e.get('1410.3881')}. The first version reported 27/14; "
    f"it is {len(entry_src)}/{len(receipts)}. CGATE caught this and it was verified directly")

flagged=[f for f in allsrc if is_obstruction(" ".join(open(S+f,errors="ignore").read().split()))]
fe=[f for f in flagged if stem_of(f) in f2e]
print("\n  RE-RUN of b1's criterion over every current source:")
for f in flagged: print(f"     {'ENTRY '+f2e[stem_of(f)] if stem_of(f) in f2e else 'receipt ':<9} {f}")
chk("RE-RUN, not hardcoded: the criterion is executed here and flags the same set both seats "
    "independently reproduced",
    len(flagged)==6 and any("2606.25023" in f for f in flagged),
    f"{len(flagged)} flagged. The first version hardcoded these names from an earlier printout, so "
    f"a new pin or a criterion edit could have left every predicate green while the answer rotted")

TRUE_POS="2606.25023"   # PAPER-level convention, stated not assumed
tp=sum(1 for f in fe if TRUE_POS in f)
print(f"\n  precision over ALL pinned sources : {tp}/{len(flagged)} = {tp/len(flagged):.2f}")
print(f"  precision over CORPUS entries     : {tp}/{len(fe)} = {tp/len(fe):.2f}")
print(f"  under CLAIM-level labelling       : 2/{len(fe)} = {2/len(fe):.2f}  (entry 25's Buchdahl argument)")
chk("MEASURED: under PAPER-level labelling the screen is wrong more often than right on both "
    "populations -- and under CLAIM-level labelling it is NOT, which cuts the other way",
    tp/len(flagged) < 0.5 and tp/len(fe) < 0.5 and 2/len(fe) > 0.5,
    f"{tp/len(flagged):.2f} and {tp/len(fe):.2f} at paper level; {2/len(fe):.2f} at claim level, "
    f"where it is right twice in three. AN EARLIER VERSION OF THIS CHECK WAS NAMED 'wrong more "
    f"often than right on EVERY convention' -- FALSE at claim level, and false in the direction "
    f"unfavourable to the screen, written minutes after both seats caught me framing the same "
    f"number the other way. The predicate is now split by convention because the two conventions "
    f"disagree about the verdict, which is itself the finding")

print("\n  IS THE 'IMPROVEMENT' A LENGTH EFFECT? -- AGATE's charge, measured rather than argued")
L_r=[len(open(S+f,errors="ignore").read()) for f in receipts]
L_e=[len(open(S+f,errors="ignore").read()) for f in entry_src]
mr, me = sorted(L_r)[len(L_r)//2], sorted(L_e)[len(L_e)//2]
print(f"     median receipt length : {mr:,} chars")
print(f"     median corpus length  : {me:,} chars")
chk("MEASURED: the excluded receipts really are the longer documents, so AGATE's composition "
    "objection has a factual basis and the direction of the correction cannot be trusted as a "
    "property of the screen",
    mr > me,
    f"{mr:,} against {me:,}. A criterion that COUNTS tokens will trip more often on longer text, so "
    f"removing the long documents raises precision for a reason that has nothing to do with "
    f"whether the screen recognises a no-go")

print("""
HONESTY NOTE -- rewritten because both seats called the first version's framing a thumb on the scale

  THIS FILE IS NOT NEUTRAL AND SHOULD NOT CLAIM TO BE. It produces the number question 1 turns on,
  and my first version led with the figure favourable to keeping the screen while insisting it
  "decides nothing". Both figures now lead together:

     1-in-6 over everything pinned   -- the harsher reading, favours hand-sorting
     1-in-3 over identified corpus   -- the kinder reading, favours screening
     2-in-3 at claim level           -- kinder still, and the ONLY figure on which the screen is
                                        right more often than wrong; rests on a labelling
                                        convention nobody has ruled on

  AND THE KINDER NUMBERS ARE THE LESS TRUSTWORTHY ONES. The 1-in-3 depends on excluding documents
  that are measurably longer, which a token-counting criterion trips on for reasons unrelated to
  no-go structure. The 2-in-3 depends on a convention that would also change how every other entry
  in the corpus is filed.

  WHAT IS NOT MEASURED AT ALL: recall. Nothing here tests what the screen MISSES, and a screen used
  to re-sort a corpus is judged at least as much on that.

  AND THE POPULATION IS AN ACQUISITION SAMPLE, NOT A SAMPLE. These sources were pinned because
  research needed them. 22 of the 51 BHU papers have never been scored. CGATE: this is "observed
  precision among the flagged identifiable corpus papers in this current source-directory subset",
  and it is not corpus-wide.

  QUESTION 1 REMAINS DUHO'S AND IS UNTOUCHED.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
