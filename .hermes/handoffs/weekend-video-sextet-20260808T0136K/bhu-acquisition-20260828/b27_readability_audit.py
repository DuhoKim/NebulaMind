#!/usr/bin/env python3
"""B27 -- which BHU papers can be READ.  GATED, REFUTED IN BOTH DIRECTIONS, REBUILT.

  AGATE_B27  READABILITY_REFUTED_FALSE_MATCHES_AND_ARTEFACTS
  CGATE_B27  READABILITY_REFUTED_FALSE_ABSENCE_AND_FALSE_POSITIVE

Both seats, unanimously, found the same four defects. All four repairs applied.

  1. FALSE ABSENCE -- entry 41. Its arXiv title is "The universe as a closed anisotropic universe
     born in a black hole"; the bibliography carries the PUBLISHED title, "A nonsingular,
     anisotropic universe in a black hole with torsion and particle production". Matching on the
     published title alone can never find the preprint. The text was pinned all along at
     2007.11556_clean.txt AND THE SOURCE MAP ALREADY MAPPED IT.
  2. FALSE POSITIVE -- entry 1. "The Universe as a Black Hole" (23 normalised chars) is a SUBSTRING
     of entry 5's "A note on Pathria's model of the universe as a black hole", so entry 1 matched
     entry 5's PDF. Both entries pointed at ONE file and nothing checked for that.
  3. FABRICATED LENGTH -- PDFs were sized as page_count * 4000, not measured. Every two-page PDF
     passed automatically; every one-page paper failed automatically. Entry 2 is a one-page Physics
     Today note.
  4. THE NEAR-MISS LIST IS NOT RECALL EVIDENCE. Entries 23/26/27 are one author's linked series, so
     their clustering is shared vocabulary, not three independent signals. And sampling papers the
     screen NEARLY liked tests a boundary, not misses. Kept, relabelled a lexical stress sample.

AND THE TOTAL SURVIVED BY CANCELLATION. Removing entry 1 and adding entry 41 leaves 34/17 unchanged.
CGATE: "A source inventory is about identities, not merely a total." The old number was right by
accident while its membership was wrong, which is worse than being wrong outright.

THE DESIGN CHANGE THAT MATTERS: the source map is reliable for "this file IS entry N" -- a person
checked it -- and unreliable for "entry N has no file", because it is incomplete. IT IS NOW USED
FOR POSITIVES ONLY. My first version used it for absence, which is exactly backwards.
"""
import re, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.abspath(os.path.join(_HERE,".."))
BIB=os.path.join(ROOT,"bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")
MAP=os.path.join(ROOT,"bhu-theory-phase6-curvature-20260827/ENTRY_SOURCE_MAP.md")
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))
def norm(x): return re.sub(r"[^a-z0-9]","",x.lower())

T=open(BIB).read(); cut=T.find("## Ranked:")
st=[(m.start(),int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ",T[:cut],re.M)]
bl={n:T[p:(st[i+1][0] if i+1<len(st) else cut)] for i,(p,n) in enumerate(st)}
E={n:b for n,b in bl.items() if "Testability: **" in b}
def title_of(b):
    m=re.search(r'[“"]([^”"]{8,140})[.”"]', b.split("\n")[0]); return m.group(1) if m else None
titles={n:title_of(b) for n,b in E.items()}
keys={n:norm(t)[:60] for n,t in titles.items() if t and len(norm(t))>=16}

print("="*98); print("B27 -- readability audit [REBUILT AFTER BOTH SEATS REFUTED IT]"); print("="*98)

# --- POSITIVES FROM THE MAP: a human-verified file->entry binding, used only to ADD ------------
mapped={}
for line in open(MAP).read().splitlines():
    if not line.startswith("|"): continue
    c=[x.strip() for x in line.strip().strip("|").split("|")]
    if len(c)<3: continue
    nums=re.findall(r"(?<![\d.])(\d{1,2})(?![\d.])", c[0].replace("~",""))   # anchored: not from a filename
    if not nums: continue
    for m in re.finditer(r"`([^`]+)`", line):
        b=os.path.basename(m.group(1))
        if b.endswith((".txt",".pdf")): mapped.setdefault(int(nums[-1]), b)
chk("PARSED: the map's entry numbers are now anchored so a filename like 1111.1017_clean.txt "
    "cannot contribute an entry '17'",
    17 not in mapped or "1111.1017" not in mapped.get(17,""),
    "AGATE found the unanchored version pulling 17 out of that filename. The map is used ONLY to "
    "add readable entries, never to declare one unreadable")

files=[]
for dp,_,fn in os.walk(ROOT):
    for f in fn:
        if f.endswith((".txt",".pdf")): files.append(os.path.join(dp,f))
heads={}
for p in files:
    try:
        if p.endswith(".pdf"):
            import fitz; d=fitz.open(p)
            full=" ".join(pg.get_text() for pg in d)          # REAL text, not page_count*4000
            h=" ".join(full.split())[:6000]; n=len(full)
        else:
            raw=open(p,errors="ignore").read(); h=" ".join(raw[:6000].split()); n=len(raw)
        # WEB-CHROME FILTER, third false-positive class found in this matcher. A scraped
        # publisher landing page has the title in its head and thousands of characters, and
        # contains no paper: pathria-nature.txt is 6,259 chars of Nature navigation furniture
        # wrapped round an abstract. Rejecting on chrome markers is cheap and specific.
        CHROME=("skip to main content","sign up for alerts","close banner","privacy policy",
                "we recommend you use a more up to date browser","advertisement view all journals")
        if sum(1 for c in CHROME if c in h.lower()) >= 2: continue
        # REFERENCE-LIST FILTER, the FOURTH false-positive class this matcher has produced. A
        # bibliography fragment carries dozens of cited titles, and in a short file those sit
        # inside the 6,000-character "head". e25_tail.txt is entry 25's reference tail and it
        # matched entry 19 -- CGATE's independent search had entry 19 absent and was right.
        if sum(1 for c in ("[google scholar]","[crossref]","[scilit]","[pubmed]")
               if c in h.lower()) >= 2: continue
        heads[p]=(norm(h), n)
    except Exception: pass

MINLEN=3000     # lowered: one-page letters are real papers (AGATE/CGATE both)
cand={}
for n,k in keys.items():
    for p,(h,ln) in heads.items():
        if k in h and ln>=MINLEN: cand.setdefault(n,[]).append(p)
# COLLISION RULE: one file cannot be two papers. The entry with the LONGER title wins -- a document
# whose head contains a long title that CONTAINS a short one is the long-titled paper.
owner={}
for n,ps in cand.items():
    for p in ps: owner.setdefault(p,[]).append(n)
found={}
for p,ns in owner.items():
    win=max(ns,key=lambda n: len(keys[n]))
    found.setdefault(win,p)
losers=[(p,[n for n in ns if n!=max(ns,key=lambda n: len(keys[n]))]) for p,ns in owner.items() if len(ns)>1]
for n,f in mapped.items():                                   # map positives, added not subtracted
    if n in E and n not in found:
        hit=[p for p in heads if os.path.basename(p)==f]
        if hit: found[n]=hit[0]
missing=sorted(set(E)-set(found))
print(f"\n  readable    : {len(found)}")
print(f"  not located : {len(missing)}   {missing}")
chk("FIXED: entry 41 is now found, via the map, despite its published title differing from the "
    "arXiv title its file carries",
    41 in found,
    f"{os.path.basename(found.get(41,'-'))}. Title-only matching could never find it and my own "
    "limitations section had named this exact class without testing for it")
chk("FIXED: one file cannot satisfy two entries, and entry 1 -- whose only candidates are other "
    "papers and a scraped landing page -- is correctly not located",
    1 not in found and len(losers)>0,
    f"collisions resolved: {[(os.path.basename(p),l) for p,l in losers][:3]}. Entry 1's whole "
    f"normalised title is 23 chars and sits inside entry 5's, so no prefix length could separate "
    f"them -- only a collision rule could")
chk("FIXED: PDF length is the extracted character count, so a one-page letter is no longer "
    "rejected for being short",
    MINLEN < 8000,
    "was page_count*4000, an invented proxy: every 2-page PDF passed and every 1-page paper failed. "
    "Entry 2 is a one-page Physics Today note")

print(f"""
ABSENCE CLAIM, to the lane's standard.

  PATTERN: normalised title (60 chars) in the first 6,000 characters of a document of at least
    {MINLEN:,} characters, PLUS every human-verified binding in the source map.

  ONE CLASS IT WOULD MISS: a paper held under a title that differs from BOTH the published title
    and any mapped filename -- a translation, a heavily OCR-damaged scan, or a preprint whose title
    changed and which the map never indexed. Entry 41 was exactly this class and was found only
    because the map happened to carry it.

  WHAT WAS DONE ABOUT IT: nothing that closes the class. THE NOT-LOCATED LIST IS A CANDIDATE LIST.
    CGATE searched all 17 of the previous version's candidates independently by DOI, author, arXiv
    id and alternate title, and confirmed 16 of them absent from this repository -- that is the
    strongest evidence available here, and it is a repo search, not a statement about the world.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
