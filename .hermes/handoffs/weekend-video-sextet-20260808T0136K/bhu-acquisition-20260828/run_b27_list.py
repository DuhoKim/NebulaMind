import re, os
BIB="../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md"
T=open(BIB).read(); cut=T.find("## Ranked:")
st=[(m.start(),int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ",T[:cut],re.M)]
bl={n:T[p:(st[i+1][0] if i+1<len(st) else cut)] for i,(p,n) in enumerate(st)}
E={n:b for n,b in bl.items() if "Testability: **" in b}
def title_of(b):
    m=re.search(r'[“"]([^”"]{12,140})[.”"]', b.split("\n")[0])
    return m.group(1) if m else None
def norm(x): return re.sub(r"[^a-z0-9]","",x.lower())
def key_of(t):
    k=norm(t)
    return k[:44] if len(k)>=16 else None
titles={n:title_of(b) for n,b in E.items()}
keys={n:key_of(t) for n,t in titles.items() if t and key_of(t)}

files=[]
for dp,_,fn in os.walk(".."):
    for f in fn:
        if f.endswith((".txt",".pdf")): files.append(os.path.join(dp,f))

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

print("Found files:")
for n, p in sorted(found.items()):
    print(f"{n:>2}: {p}")
