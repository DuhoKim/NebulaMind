#!/usr/bin/env python3
"""Freeze verification v3 — numbers-first.
A quote VERIFIES if (a) every distinctive numeric token in it appears in a single local
source file, and (b) that file also matches >=30% of the quote's 6-word shingles (guard
against numeric coincidence). Corpus: txt, tex, html, xml, md."""
import re, glob, unicodedata, pathlib

def norm(s):
    s = unicodedata.normalize("NFKD", s)
    for a,b in [("’","'"),("‘","'"),("“",'"'),("”",'"'),("−","-"),("–","-"),("—","-")]:
        s=s.replace(a,b)
    s = re.sub(r"\$[^$]*\$", lambda m: m.group(0).replace("$",""), s)  # unwrap inline math
    s = re.sub(r"\\[a-zA-Z]+", " ", s)                                  # strip latex commands
    s = re.sub(r"[^a-zA-Z0-9. ]", " ", s)
    return re.sub(r"\s+"," ",s).lower().strip()

def numtokens(q):
    toks = re.findall(r"\d+\.\d+|\d{3,}", norm(q))
    return sorted(set(t for t in toks if len(t.replace(".","")) >= 3))

def shingles(q,n=6):
    w=[x for x in norm(q).split() if not re.fullmatch(r"[\d.]+",x)]
    return [" ".join(w[i:i+n]) for i in range(0,max(1,len(w)-n+1),3)]

def blockquotes(txt):
    qs,cur=[],[]
    for line in txt.splitlines():
        if line.startswith(">"): cur.append(line.lstrip("> ").strip())
        else:
            if cur: qs.append(" ".join(cur)); cur=[]
    if cur: qs.append(" ".join(cur))
    return [q for q in qs if len(q)>40]

def agy_quotes(txt):
    return [q for q in re.findall(r'"([^"]{60,})"', txt)]

def load_corpus(srcdir):
    corpus={}
    pats=["*.txt","*.tex","*.html","*.xml","*.md"]
    files=[]
    for p in pats: files+=glob.glob(srcdir+"/**/"+p, recursive=True)
    for f in files:
        try: corpus[f]=" "+norm(open(f,encoding="utf-8",errors="replace").read())+" "
        except Exception: pass
    return corpus

def check(harvest, srcdir, style):
    txt=open(harvest,encoding="utf-8").read()
    qs = blockquotes(txt) if style=="block" else agy_quotes(txt)
    corpus=load_corpus(srcdir)
    nfail=0
    for q in qs:
        nums=numtokens(q); sh=shingles(q)
        best=(0,None,0)
        for f,c in corpus.items():
            nh=sum(1 for t in nums if t in c)
            shh=sum(1 for s in sh if s in c)/max(1,len(sh))
            score=(nh,shh)
            if (nh,shh)>(best[0],best[2]): best=(nh,f,shh)
        ok = nums and best[0]==len(nums) and best[2]>=0.30
        if not nums: ok = best[2]>=0.7   # no numbers: fall back to strong shingle match
        if not ok:
            nfail+=1
            print(f"  MISS nums {best[0]}/{len(nums)} sh {best[2]:.0%}: {q[:64]}...")
    print(f"{pathlib.Path(harvest).parent.name}: {len(qs)-nfail}/{len(qs)} verified (numbers-first)")
    return nfail

f1=check("platoon/gpt2_trackb_cmb/HARVEST_CMB_BOUNDS.md","platoon/gpt2_trackb_cmb/sources","block")
f2=check("platoon/agy_trackb_h0/HARVEST_H0_ANISOTROPY.md","platoon/agy_trackb_h0/sources","agy")
print("TOTAL FAILURES:", f1+f2)
