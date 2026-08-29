#!/usr/bin/env python3
"""B27 -- which BHU papers can actually be READ? Filesystem, not the index.

WHY. My answer to question 1 attaches a condition: measure the screen's miss rate, or say plainly
we accept the risk. Measuring it means sampling the papers the screen did NOT flag -- which requires
knowing which papers can be read at all. I gave Duho that number by parsing ENTRY_SOURCE_MAP.md and
BOTH SEATS REFUTED IT, in both directions at once: two "unpinned" papers had full text on disk, and
one "pinned" entry was an artefact of a filename ending in 17.

So this looks at files. Search space: every .txt and .pdf under the handoff tree.
"""
import re, os, sys, subprocess
_HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.abspath(os.path.join(_HERE,".."))
BIB=os.path.join(ROOT,"bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

T=open(BIB).read(); cut=T.find("## Ranked:")
st=[(m.start(),int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ",T[:cut],re.M)]
bl={n:T[p:(st[i+1][0] if i+1<len(st) else cut)] for i,(p,n) in enumerate(st)}
E={n:b for n,b in bl.items() if "Testability: **" in b}

def title_of(b):
    m=re.search(r'[“"]([^”"]{12,140})[.”"]', b.split("\n")[0])
    return m.group(1) if m else None
def norm(x):
    # ALL spaces removed. Two failures forced this, both caught by the positive controls:
    #  - the first version built a key from words LONGER THAN THREE CHARACTERS and then searched
    #    for it as a CONTIGUOUS substring. "note pathria model universe black" is not contiguous
    #    in "A note on Pathria's model of the universe as a black hole" -- the dropped short words
    #    sit between them. It could never match anything.
    #  - PDF extraction splits words: entry 56's page 1 reads "The mass of our obser v able
    #    Uni v erse". Any space-sensitive match fails on it.
    # Stripping spaces entirely fixes both and costs nothing here.
    return re.sub(r"[^a-z0-9]","",x.lower())
def key_of(t):
    k=norm(t)
    return k[:44] if len(k)>=16 else None   # 24 excluded short real titles: entry 6 is
                                       # "Did the universe evolve?" = 20 stripped chars.
                                       # A short key is safe here because a match must
                                       # also sit in the document HEAD, not a reference list.

titles={n:title_of(b) for n,b in E.items()}
# a None key silently entered the match set and raised on `None in h`. The check below
# then reported '51 of 51' because it counted TITLES, not usable keys.
keys={n:k for n,k in ((n,key_of(t)) for n,t in titles.items() if t) if k}
nokey=sorted(set(E)-set(keys))
print("="*98); print("B27 -- readability audit, from the filesystem"); print("="*98)
print(f"\n  BHU entries: {len(E)}   with a usable title key: {len(keys)}")
chk("PARSED: a distinctive title fragment was extracted for nearly every entry, so absence of a "
    "match means something",
    len(keys) >= len(E)-3,
    f"{len(keys)} of {len(E)} have a USABLE KEY (not merely a title). Entries without one: "
    f"{nokey or 'none'} -- reported, not counted as unreadable")

# --- index every candidate file's HEAD, which is where a paper states its own title -------------
files=[]
for dp,_,fn in os.walk(ROOT):
    for f in fn:
        if f.endswith((".txt",".pdf")): files.append(os.path.join(dp,f))
print(f"  candidate files: {len(files)}")
heads={}
for p in files:
    try:
        if p.endswith(".pdf"):
            import fitz
            d=fitz.open(p); h=" ".join((d[0].get_text() if d.page_count else "").split()); n=d.page_count*4000
        else:
            raw=open(p,errors="ignore").read(); h=" ".join(raw[:6000].split()); n=len(raw)
        heads[p]=(norm(h), n)
    except Exception: pass

MINLEN=8000
found={}
for n,k in keys.items():
    hits=[p for p,(h,ln) in heads.items() if k in h and ln>=MINLEN]
    if hits: found[n]=sorted(hits,key=lambda p:-heads[p][1])[0]
missing=sorted(set(E)-set(found))
print(f"\n  READABLE (title appears at the head of a document >= {MINLEN:,} chars): {len(found)}")
print(f"  NOT LOCATED                                                        : {len(missing)}")
print(f"  {missing}")

for n,exp in ((56,True),(5,True)):
    print(f"    entry {n:>2}: located={n in found}   {os.path.basename(found[n]) if n in found else '-'}")
chk("VERIFIED: the two papers CGATE proved readable, which my index-parse had called unpinned, are "
    "found by a filesystem search",
    56 in found and 5 in found,
    "entry 56's MNRAS PDF and entry 5's arXiv PDF. A search that missed them would reproduce the "
    "defect this file exists to repair")
chk("MEASURED: the filesystem answer differs from the index answer, which is the point",
    len(missing) != 18,
    f"{len(missing)} not located against the 18 I reported from ENTRY_SOURCE_MAP.md")

print(f"""
ABSENCE CLAIM, to the lane's standard.

  PATTERN: the paper's title, lowercased with ALL non-alphanumerics removed (first 44 chars),
    appearing in the first 6,000 characters of a .txt or on page 1 of a .pdf, in a document of at
    least {MINLEN:,} characters -- so a passing CITATION does not count as possessing the paper,
    and so PDF word-splitting ("obser v able") does not defeat the match.

  ONE CLASS IT WOULD MISS: a paper held under a title the bibliography records differently --
    a preprint title later changed for publication, a translated title, or an OCR scan whose
    first page mangles the words. Any of those reads as NOT LOCATED while the text sits on disk.

  WHAT WAS DONE ABOUT IT: the two known cases of exactly this failure -- entries 5 and 56, which
    the index missed -- are used as positive controls above and both are found. That does not
    prove the class is empty; it proves the search reaches into the directories where the index
    did not look. THE NOT-LOCATED LIST IS A CANDIDATE LIST, NOT A FINDING, and each would need a
    hand check before anyone calls a paper unavailable.
""")
# ---------------------------------------------------------------------------------------------
# RECALL PROBE -- cheap, and NOT the blinded audit. It scores every readable paper on b1's own
# criterion and reports how close the UNFLAGGED ones come to the threshold. A cluster just below
# would be evidence recall is fragile; a wide gap is weak evidence it is not. Neither substitutes
# for reading unflagged papers, which is what actually measures a miss.
IMP = r"cannot be both|cannot be\b|can not be\b|does not yield|no .{0,30}(?:can|exists?)\b|impossible|obstruct\w*|must give up|prevents?\b"
DOM = r"[Cc]onsider a .{0,80}(?:spacetime|metric|parent|class|solution)|[Aa]ssume that|under the (?:same )?assumptions?|hypothes[ei]s"
REF = r"escape|evasion|requires? an? (?:additional|extra)|must give up at least one|unless"
print("\nRECALL PROBE -- b1's score on every readable paper (threshold: imp>=5, dom>=2, ref>=2)")
scored=[]
for e,path in sorted(found.items()):
    try:
        if path.endswith(".pdf"):
            import fitz; d=fitz.open(path); txt=" ".join(" ".join(pg.get_text() for pg in d).split())
        else: txt=" ".join(open(path,errors="ignore").read().split())
    except Exception: continue
    i,dd,r=len(re.findall(IMP,txt)),len(re.findall(DOM,txt)),len(re.findall(REF,txt))
    scored.append((e,i,dd,r,(i>=5 and dd>=2 and r>=2)))
flag=[x for x in scored if x[4]]; unflag=[x for x in scored if not x[4]]
near=[x for x in unflag if x[1]>=3 and x[2]>=1 and x[3]>=1]
print(f"   scored {len(scored)} readable papers: {len(flag)} flagged, {len(unflag)} not")
print(f"   of the unflagged, NEAR the threshold (imp>=3, dom>=1, ref>=1): {len(near)}")
for e,i,dd,r,_ in sorted(near,key=lambda x:-x[1])[:6]:
    print(f"      entry {e:>2}  imp={i:<3} dom={dd:<3} ref={r}")
chk("MEASURED: the recall probe runs and separates the readable set rather than flagging all or "
    "none, so its near-miss count means something",
    0 < len(flag) < len(scored),
    f"{len(flag)} flagged of {len(scored)} scored. THIS IS NOT A RECALL MEASUREMENT -- a near-miss "
    f"is a paper the screen ALMOST flagged, not a paper it wrongly missed. Only reading unflagged "
    f"papers measures that, and CGATE prices it at 11 reads for a gross failure, ~29 for certainty")

n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
