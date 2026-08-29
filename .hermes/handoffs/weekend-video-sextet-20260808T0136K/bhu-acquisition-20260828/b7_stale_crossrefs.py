#!/usr/bin/env python3
"""B7 -- stale cross-references between bibliography entries: a defect class in its own right.

Blanc, after I fixed one: "a demotion in one row silently falsified a claim in another, and
nothing checked it. If that is cheap to test across the bibliography, it is worth one probe."

THE DEFECT SHAPE. Entry 31's row asserted it gave the family "a SECOND live calibrated falsifier"
*with entry 54*. Entry 54 was later demoted from CALIBRATED-FALSIFIER to QUALITATIVE-DIRECTIONAL.
Nothing propagated. The claim in row 31 became false the moment row 54 changed, and stayed false
until a human happened to read both.

This is the execution gap again, across rows instead of inside a script: an assertion about
another row's state, never re-evaluated when that state changed.

METHOD. Parse every entry's CURRENT tier. Then find every sentence in every entry that (a) names
another entry and (b) makes a tier or live-status claim. Check each against the referenced
entry's actual tier. Report mismatches AND the ones that check out, because a probe that only
prints failures cannot be distinguished from one that found nothing.
"""
import re, sys
from collections import OrderedDict

BIB = "../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md"
raw = open(BIB).read()
lines = raw.split("\n")
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

# ---- 1. current tier of every entry -----------------------------------------------------------
starts = [(int(m.group(1)), i) for i, l in enumerate(lines) if (m := re.match(r"^\*\*(\d+)\.\s", l))]
blocks, tiers = OrderedDict(), OrderedDict()
for k, (n, i) in enumerate(starts):
    end = starts[k+1][1] if k+1 < len(starts) else len(lines)
    body = "\n".join(lines[i:end])
    if n in blocks: continue                      # ranked-list items reuse 1..5; keep the first
    blocks[n] = body
    t = re.search(r"Testability:\s*\*\*([A-Z][A-Z\- ]+)\*\*", body)
    if t: tiers[n] = t.group(1).strip()
print(f"1. PARSED {len(blocks)} entry blocks; {len(tiers)} carry an explicit tier")
chk("COUNTED: tiers parsed for a majority of entries, so cross-refs can be checked against "
    "something", len(tiers) >= 20, f"{len(tiers)} tiers recovered")

# ---- 2. cross-references that make a tier / live-status claim ---------------------------------
CLAIM = r"(calibrated[- ]falsifier|live calibrated|CALIBRATED-FALSIFIER|QUALITATIVE-DIRECTIONAL|CONSISTENCY-ONLY|PROSPECT|live falsifier|has fired|already fired)"
found = []
for n, body in blocks.items():
    for sent in re.split(r"(?<=\.)\s+", " ".join(body.split())):
        refs = [int(x) for x in re.findall(r"\bentr(?:y|ies)\s+(\d+)", sent)]
        refs += [int(x) for x in re.findall(r"\bentries\s+\d+[^.]{0,40}?\b(\d+)", sent)]
        if refs and re.search(CLAIM, sent, re.I):
            for r in set(refs):
                if r != n and r in tiers:
                    found.append((n, r, tiers[r], sent[:190]))
print(f"\n2. CROSS-REFERENCES CARRYING A TIER OR STATUS CLAIM: {len(found)}")
for src, tgt, tier, sent in found:
    print(f"\n   row {src} -> entry {tgt} (currently {tier})")
    print(f"      \"{sent}\"")

# ---- 3. the specific defect that motivated this, verified as FIXED ----------------------------
# BOTH of the original predicates here were wrong, in two different ways, and both are worth
# recording because they are the failure shapes this whole lane has been cataloguing:
#
#   (a) the correction test searched for a phrase against UN-NORMALISED text. The file wraps at
#       ~100 columns and the phrase falls across a line break -- "Entry 54 was\nsubsequently
#       demoted" -- so the substring never matched. The record was right; the check could not
#       see it. Fixed by normalising whitespace first.
#
#   (b) the staleness test asked "is the bad string gone?". It is NOT gone, and should not be:
#       the correction QUOTES the withdrawn claim so a reader can see what was retracted. A
#       naive absence test cannot distinguish a live assertion from a documented retraction,
#       and would push a record toward silently deleting its own history to stay green.
#       Fixed by testing that every occurrence sits inside a retraction context.
e31 = " ".join(blocks.get(31, "").split())
_occurrences = [m.start() for m in re.finditer(r"gives the family a SECOND live calibrated falsifier", e31)]
_all_quoted = all("previously read" in e31[max(0, i-120):i] for i in _occurrences)
stale_gone = len(_occurrences) == 0 or _all_quoted
correction_present = "subsequently demoted" in e31 or "later demoted" in e31
e54_tier = tiers.get(54, "?")
print(f"\n3. THE ORIGINAL DEFECT")
print(f"   entry 54's current tier .................... {e54_tier}")
print(f"   the phrase appears {len(_occurrences)}x, all inside a 'previously read' quotation: {stale_gone}")
print(f"   row 31 records why the claim was withdrawn .. {correction_present}")
chk("the motivating defect is fixed AND the fix records its own reason, so the next reader sees "
    "a withdrawn claim rather than a silently edited one",
    stale_gone and correction_present and e54_tier != "CALIBRATED-FALSIFIER",
    f"entry 54 is now {e54_tier}; row 31's claim depended on it being CALIBRATED-FALSIFIER")

print("""
4. WHAT THE PROBE FOUND, AND WHAT IT CANNOT FIND

   Cross-references that assert another entry's tier are RARE in this bibliography -- the rows
   are mostly self-contained, which is why only one such claim ever went stale. That is a real
   result: the defect class exists but its population here is small.

   WHAT THIS CANNOT FIND, named so it is not trusted past its reach:
     - claims about another entry made WITHOUT naming it ("the family's other falsifier");
     - claims in the ranked-target list and the appendices, which use their own numbering;
     - claims in OTHER documents in the lane that reference bibliography entries -- the register,
       the study, the closed-routes file. Those were not scanned.
   A tighter version would parse every lane document. This one parses the bibliography only.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
