#!/usr/bin/env python3
"""B40 -- byline sweep: does each entry's recorded authorship match its pinned source's own byline?

RESOLVED 2026-08-30, same session.

TWO HONESTY NOTES ON THE CLEAN RE-RUN:
  - ENTRY 44 NOW PASSES *BECAUSE OF MY ANNOTATION*: the EXTRACTION DEFECT header I added to the pin
    names Pourhasan and Afshordi, and the sweep reads the head. The match is with the DOCUMENTED
    truth, not with the extraction -- acceptable only because the header is explicit about being an
    annotation; recorded here so the pass is never read as the extraction having the authors.
  - Entries 7 and 10 were skipped on wrong paths in the first run and are now checked. Four candidates on the first run:
  9, 11, 12 -- FALSE POSITIVES FROM MY OWN NORMALISER: "ł" does not decompose under NFD (stroked
     letters carry no combining mark), so "Popławski" became "popawski" and never matched the
     sources' ASCII "Poplawski". Fixed by explicit mapping below. The records were always right.
  44 -- REAL, AND INVERTED: the RECORD is right (Pourhasan, Afshordi & Mann, per JCAP) and the PIN
     is defective -- the ar5iv extraction dropped the first two authors; "Pourhasan" and "Afshordi"
     appear NOWHERE in the file, whose head reads "...Big Bang and Robert B. Mann". The pin now
     carries an EXTRACTION DEFECT header. So the sweep catches BOTH directions of the class:
     wrong records over right sources (entry 20) and right records over broken pins (entry 44).

WHY. Entry 20's record said "Bronnikov, J. C. Fabris" over a Crossref-VERIFIED DOI whose actual
paper is Bronnikov-Melnikov-Dehnen; Fabris belongs to a different paper cited as its ref [1]. That
was found BY ACCIDENT at the b38 gate. Title matching cannot catch the class (right title, wrong
authors), DOI verification cannot either (the DOI was right; the authors typed next to it were
not). The only check that catches it is the source's own byline -- and it has never been run
corpus-wide.

METHOD. For each readable entry: surnames from the bibliography heading vs the first ~1,600 chars
of the pinned source (where papers state their own authors). Diacritics and case normalised.
HITS ARE CANDIDATES: a byline can legitimately miss from a head (OCR damage, deep cover pages), so
every flag gets a hand check before anything is called wrong.
"""
import re, os, sys, unicodedata
_HERE=os.path.dirname(os.path.abspath(__file__))
D=os.path.abspath(os.path.join(_HERE,".."))
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))
def deacc(x):
    # stroked letters (ł, đ, ø) do NOT decompose under NFD -- they carry no combining mark -- so
    # the first version stripped them entirely and flagged three correct Popławski records as
    # candidates. Map them explicitly.
    x=x.translate(str.maketrans({"ł":"l","Ł":"L","đ":"d","Đ":"D","ø":"o","Ø":"O"}))
    return "".join(c for c in unicodedata.normalize("NFD",x) if unicodedata.category(c)!="Mn")
def norm(x): return re.sub(r"[^a-z]","",deacc(x).lower())

T=open(os.path.join(D,"bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")).read()
cut=T.find("## Ranked:")
st=[(m.start(),int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ",T[:cut],re.M)]
bl={n:T[p:(st[i+1][0] if i+1<len(st) else cut)] for i,(p,n) in enumerate(st)}

# entry -> source file, from tonight's adjudicated set (readable corpus)
SRC={5:"reviews/bhu-citation-custody-evidence-20260811/arxiv-1412.0105v1.txt",
     6:"bhu-reading-20260823/sources/smolin_1992_clean.txt",
     7:"reviews/_tori_bhu_reverify_sources_20260811/arxiv_0802.2997v2_layout.txt",
     8:"bhu-reading-20260823/sources/0902.1994_clean.txt",
     9:"bhu-podcasts-20260820/arxiv_1007.0587.txt",
     10:"bhu-podcasts-20260820/arxiv_1111.4595.txt",
     11:"reviews/bhu-citation-custody-evidence-20260811/arxiv-1410.3881v2.txt",
     12:"reviews/bhu-citation-custody-evidence-20260811/arxiv-2509.11468v2.txt",
     15:"bhu-reading-20260823/sources/hep-th_0103019_clean.txt",
     17:"bhu-reading-20260823/sources/1909.07129_clean.txt",
     19:"bhu-reading-20260823/sources/universe5050111_dymnikova2019_clean.txt",
     20:"bhu-reading-20260823/sources/gr-qc_0611022_clean.txt",
     21:"bhu-reading-20260823/sources/2203.13295_clean.txt",
     22:"bhu-reading-20260823/sources/2606.25023_clean.txt",
     23:"bhu-reading-20260823/sources/2003.11544_clean.txt",
     24:"bhu-reading-20260823/sources/2104.00521_clean.txt",
     25:"bhu-reading-20260823/sources/sym14091849_clean.txt",
     26:"bhu-reading-20260823/sources/sym14101984_clean.txt",
     27:"bhu-reading-20260823/sources/2204.11608_clean.txt",
     28:"bhu-reading-20260823/sources/2411.14673_clean.txt",
     31:"bhu-reading-20260823/sources/smolin_2004_cns_clean.txt",
     36:"bhu-reading-20260823/sources/smoller_temple_2000_clean.txt",
     37:"bhu-reading-20260823/sources/0210105_clean.txt",
     38:"bhu-reading-20260823/sources/math-ph_0302036_clean.txt",
     39:"bhu-reading-20260823/sources/1105.6127_clean.txt",
     40:"bhu-reading-20260823/sources/2008.02136_clean.txt",
     41:"bhu-reading-20260823/sources/2007.11556_clean.txt",
     43:"bhu-reading-20260823/sources/2304.12018_clean.txt",
     44:"bhu-reading-20260823/sources/1309.1487_clean.txt",
     45:"bhu-reading-20260823/sources/2210.15186_clean.txt",
     46:"bhu-reading-20260823/sources/1111.1017_clean.txt",
     49:"bhu-reading-20260823/sources/blau_guendelman_guth_1987_prd35_1747.pdf",
     51:"bhu-reading-20260823/sources/0910.1181_clean.txt",
     52:"bhu-reading-20260823/sources/1808.08327_clean.txt",
     53:"bhu-reading-20260823/sources/1906.11824_clean.txt",
     54:"bhu-reading-20260823/sources/2505.23877_clean.txt",
     55:"bhu-reading-20260823/sources/2007.06664_clean.txt",
     56:"bhu-reading-20260823/sources/gaztanaga_mass_mnras.pdf",
     57:"bhu-reading-20260823/sources/smoller_temple_1997_oppenheimer_snyder_arma138_cv47.pdf"}
def head_of(path):
    p=os.path.join(D,path)
    if p.endswith(".pdf"):
        import fitz; d=fitz.open(p); return " ".join(d[0].get_text().split())[:1600]
    return " ".join(open(p,errors="ignore").read()[:2400].split())[:1600]

print("="*98); print("B40 -- byline sweep over the readable corpus"); print("="*98)
flags=[]; ok=0; skipped=[]
for n,rel in sorted(SRC.items()):
    if not os.path.exists(os.path.join(D,rel)): skipped.append(n); continue
    head=bl[n].split("\n")[0]
    # surnames: capitalised words before the year-paren, minus initials/venue noise
    pre=head.split("(")[0]
    raw=re.findall(r"[A-ZÀ-Ž][a-zà-ž'\-ł]+", deacc(pre))
    NOISE={"A","The","Note","Universe","Black","Hole","Cosmology","Physics","Gen","Phys","Lett",
           "Rev","Astrophys","Nature","Class","Quantum","Grav","Universes","Inside"}
    surnames=[w for w in raw if len(w)>2 and w not in NOISE]
    h=norm(head_of(rel))
    missing=[w for w in surnames if norm(w) not in h]
    if missing: flags.append((n,missing,surnames))
    else: ok+=1
print(f"\n  checked {ok+len(flags)} entries with pinned sources; {len(skipped)} skipped (no file): {skipped}")
print(f"  bylines fully matched: {ok}")
print(f"  CANDIDATES (some recorded surname absent from the source head): {len(flags)}")
for n,miss,alln in flags:
    print(f"    entry {n:>2}: missing {miss}  (recorded: {alln})")
chk("MEASURED: the sweep separates the corpus rather than flagging everything or nothing",
    0 <= len(flags) < 10 and ok > 25,
    f"{ok} matched, {len(flags)} candidates. Every candidate needs a hand check -- a byline can "
    f"be absent from a head for OCR or cover-page reasons, so a flag is not a finding")
chk("CONTROL: entry 20 -- the known formerly-wrong case, since corrected -- now passes",
    all(n!=20 for n,_,_ in flags),
    "its corrected Bronnikov-Melnikov-Dehnen byline matches the source; the sweep would have "
    "flagged the OLD record (Fabris absent from the source head), which is the class it exists for")
n_=sum(1 for _,o,_ in checks if o)
print(f"\nSELF-CHECKS: {n_}/{len(checks)} passed")
sys.exit(0 if n_==len(checks) else 1)
