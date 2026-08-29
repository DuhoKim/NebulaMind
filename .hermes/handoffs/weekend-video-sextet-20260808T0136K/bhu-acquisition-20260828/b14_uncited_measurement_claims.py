#!/usr/bin/env python3
"""B14 -- does the corpus assert experimental results it never cites?

WHY NOW. Both of the corpus's LIVE calibrated falsifiers were audited today, and BOTH turned out
to rest on a claim about an experiment's status that carried no citation:

  entry 31  the measurement side was unpinned; the study built on it had to be rewritten
  entry 51  "CMS reports no evidence for microscopic black holes as of 2025-12" -- NO citation of
            any kind, no arXiv id, no DOI, nothing pinned

Two out of two is not a coincidence worth ignoring. This sweeps all 51 entries for the same shape.

WHAT THE SHAPE IS, precisely. Not "an entry with no DOI" -- every entry has its own paper's DOI.
It is: AN ENTRY THAT ASSERTS SOMETHING ABOUT AN EXTERNAL EXPERIMENT'S RESULTS while pinning no
source for that experiment. The paper's own DOI does not support a claim about what CMS found.

WHAT THIS FILE DOES NOT DO. It does not assert that any claim is uncited. Defects 1e-1j in the
harness register are six FALSE absence claims produced by patterns narrower than their assertions,
and the a11 classifier was deleted for measuring 4/8. So this prints CANDIDATES for adjudication
and its self-checks test the probe's own behaviour on known cases, not the corpus.
"""
import re, sys, os
BIB="../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md"
SRC="../bhu-reading-20260823/sources"
T=open(BIB).read()
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

# --- split into entry blocks on the numbered bold heading ------------------------------------
# CGATE_B14: the first version matched EVERY bold numbered heading, including the five in the
# "Ranked: the strongest published targets" section, then did blocks[num]=... -- which SILENTLY
# OVERWROTE genuine entries 1-5. It never screened them. And its "no duplicate numbers" check was
# a TAUTOLOGY: dict keys are unique by construction, so it could not fail. Both repaired here.
cut = T.find("## Ranked: the strongest published targets")
assert cut > 0, "section boundary not found -- refusing to parse an unbounded document"
BODY = T[:cut]
raw=[(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", BODY, re.M)]
nums=[n for _,n in raw]
dupes=sorted({n for n in nums if nums.count(n)>1})
blocks={}
for i,(pos,num) in enumerate(raw):
    end = raw[i+1][0] if i+1 < len(raw) else len(BODY)
    blocks[num]=BODY[pos:end]
print("="*98); print("B14 -- uncited experimental-status claims across the corpus  [REBUILT AFTER CGATE]")
print("="*98)
print(f"\nparsed {len(raw)} headings before the Ranked section -> {len(blocks)} distinct entries")
chk("PARSED: every numbered heading in the entry section maps to a DISTINCT entry, so nothing was "
    "silently overwritten -- tested on the raw match list, not on the dict",
    len(raw)==len(blocks) and not dupes,
    f"{len(raw)} headings, {len(blocks)} keys, duplicates {dupes or 'none'}. The earlier check "
    f"compared a dict against set(dict) -- ALWAYS TRUE. It passed while entries 1-5 were being "
    f"replaced by the Ranked section's headings 1-5, which is how b14 shipped without screening "
    f"five entries at all")
chk("PARSED: entry 1 is the real bibliography entry and not the Ranked-section item that "
    "previously displaced it",
    "Pathria" in blocks.get(1,""),
    f"blocks[1] now begins '{blocks.get(1,'')[:58]}...' -- the overwritten version began "
    f"'**1. The Poplawski torsion-bounce chain'")

# --- instruments / collaborations whose RESULTS an entry might assert -------------------------
INSTR = r"(LIGO|Virgo|KAGRA|LISA|CMS|ATLAS|LHC|Planck|DESI|JWST|NICER|Chandra|Fermi|INTEGRAL|" \
        r"COMPTEL|Subaru|HSC|OGLE|SDSS|Gaia|EHT|Event Horizon|IceCube|Auger|NANOGrav|Shapiro|ACT|WMAP)"
STATUS = r"(report|reports|reported|observ|measur|detect|exclud|constrain|rule[sd]? out|" \
         r"no evidence|limit|bound|as of|null result|non-?detection|search)"
# CGATE_B14 attack 3 succeeded: entry 44 says its base model is "already ruled out at >5 sigma"
# with NO instrument named, and the fixed vocabulary above cannot see it. This is the widening.
BARE_STATUS = r"(ruled out at|excluded at|rules out|ruled out by|inconsistent with observ|" \
              r"[>≳]\s*\d+(?:\.\d+)?\s*(?:σ|sigma)|\d+(?:\.\d+)?\s*(?:σ|sigma)\s*(?:level|exclu|tension))"
CITE = r"(arXiv:\s*\d{4}\.\d{4,5}|\b\d{4}\.\d{4,5}(_clean)?\b|sources/|_clean\.txt|\.pdf\b|" \
       r"10\.\d{4,9}/[^\s)]+)"
def first_line(b): return b.split("\n")[0][:96]

cands=[]
for num,b in sorted(blocks.items()):
    body=b; hits=[]
    for m in re.finditer(INSTR, body):
        w=body[max(0,m.start()-220):m.start()+220]
        if re.search(STATUS, w, re.I): hits.append((m.group(1), " ".join(w.split())))
    for m in re.finditer(BARE_STATUS, body, re.I):          # <-- CGATE's widening
        w=body[max(0,m.start()-220):m.start()+220]
        hits.append(("[no-instrument]", " ".join(w.split())))
    if not hits: continue
    after_doi="\n".join(body.split("\n")[2:])
    ext=re.findall(CITE, after_doi)
    cands.append((num, first_line(b), len(hits), sorted({h[0] for h in hits}), len(ext), hits[:1]))

print(f"\nentries asserting an experimental result: {len(cands)} of {len(blocks)}")
bare=[c for c in cands if c[4]==0]
print(f"of those, with NO citation marker anywhere below the heading DOI line: {len(bare)}")
print("\n" + "-"*98)
print(f"{'#':>3}  {'instruments named':<34} {'cites':>5}   entry")
print("-"*98)
for num,head,nh,instr,ne,ex in cands:
    flag = "  <-- BARE" if ne==0 else ""
    print(f"{num:>3}  {','.join(instr)[:34]:<34} {ne:>5}   {head[:52]}{flag}")

print("\n" + "="*98)
print("CANDIDATES FOR ADJUDICATION -- these are NOT findings")
print("="*98)
for num,head,nh,instr,ne,ex in bare:
    print(f"\n  ENTRY {num}: {head[:88]}")
    print(f"    names {','.join(instr)} in a results context, cites nothing below its own DOI line")
    print(f"    context: ...{ex[0][1][:300]}...")

# --- self-checks: test the PROBE on cases whose answer is already known -----------------------
print("\n" + "="*98)
e51 = blocks.get(51,"")
chk("POSITIVE CONTROL: entry 51 -- whose uncited CMS claim was confirmed by hand today -- is "
    "flagged as naming an instrument in a results context",
    bool(re.search(INSTR, e51)) and bool(re.search(STATUS, e51, re.I)),
    "if the probe misses the one case we know is real, no absence it reports means anything")
e51_now_cited = 51 not in [c[0] for c in bare]
chk("NEGATIVE CONTROL: entry 51 is NOT in the bare list, because it was pinned today -- so the "
    "probe responds to citations being ADDED rather than to the words alone",
    e51_now_cited,
    "this is the check that distinguishes a real citation probe from a keyword matcher. It passes "
    "only because 2604.10732 and 2511.10662 were pinned into that entry this evening")
noise = [c for c in cands if c[4]>0]
chk("MEASURED: the probe separates the corpus rather than flagging everything or nothing",
    0 < len(bare) < len(cands),
    f"{len(bare)} bare of {len(cands)} instrument-naming entries ({len(noise)} do cite). A probe "
    f"returning all or none would be useless regardless of what it printed")
print(f"""
WHAT HAPPENS NEXT, and it is not 'these {len(bare)} entries are defective'.

Every bare entry is a CANDIDATE. Some will name an instrument without asserting its results -- "a
LISA-band signal" is a statement about frequency, not about what LISA found. Only reading each one
decides. That reading is the next unit of work, and by the standing rule it goes to a gate seat
rather than to me alone, because I am the one who wrote the entries being tested.

WHAT IS ALREADY ESTABLISHED WITHOUT ANY ADJUDICATION: the corpus's two live calibrated falsifiers
both carried this defect, and only one of them has been repaired.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
