#!/usr/bin/env python3
"""Track B freeze verification v5 — ordered numeric relations, per-entry binding, span ledger.
Repairs per REGATE_TRACKB_VERDICT.md:
  R1: quotes are verified as ORDERED sequences of signed numeric expressions (signs and
      hyphens adjacent to digits survive normalization as tokens), matched as an in-order
      subsequence within a bounded window of one bound source. Order swaps and exponent-sign
      flips now fail (self-tested below with the gate's own counterexamples).
  R2: per-entry binding extended: entries that declare no sources/ path bind via their arXiv
      ID to the matching source subtree; zero directory-wide fallbacks permitted (a quote with
      no resolvable binding FAILS).
  R3: ledger stores the full quote + sha256, bound source path + sha256, and the matched span
      (offset + excerpt from first to last expression) sufficient to reproduce the match.
"""
import re, glob, json, hashlib, unicodedata, pathlib, sys

def norm(s):
    s = unicodedata.normalize("NFKD", s)
    for a,b in [("’","'"),("‘","'"),("“",'"'),("”",'"'),("−","-"),("–","-"),("—","-"),
                ("≲","<"),("≃","~"),("≈","~"),("×","x"),("^","")]:
        s=s.replace(a,b)
    s = re.sub(r"\\[a-zA-Z]+"," ",s.replace("$","").replace("{"," ").replace("}"," "))
    s = re.sub(r"(?<=\d)\s*-\s*(?=\d)", " - ", s)      # range/exponent hyphen -> token
    s = re.sub(r"(?<![a-zA-Z0-9])([+-])(?=\s*\d)", r" \1 ", s)  # sign before number -> token
    s = re.sub(r"[^a-zA-Z0-9.+\- ]"," ",s)
    s = re.sub(r"(?<!\d)\.(?!\d)"," ",s)               # bare periods out; decimals stay
    return re.sub(r"\s+"," ",s).lower().strip()

def expr_seq(q):
    """Ordered sequence of numeric/sign tokens. A +/- token is kept ONLY when the next
    token is numeric (drops prose dashes; keeps range hyphens and exponent signs)."""
    toks=norm(q).split(); out=[]
    for i,t in enumerate(toks):
        if re.fullmatch(r"\d+(?:\.\d+)?", t): out.append(t)
        elif t in "+-" and i+1<len(toks) and re.fullmatch(r"\d+(?:\.\d+)?", toks[i+1]): out.append(t)
    return out

def find_ordered(seq, ntext, gap=400):
    """Find seq as in-order tokens in ntext, each within `gap` chars of the previous.
       Returns (start,end) char offsets or None. Greedy with restarts."""
    if not seq: return None
    pats=[re.compile(r"(?<![0-9.])"+re.escape(t)+r"(?![0-9])") if t not in "+-" else
          re.compile(r"(?<![a-zA-Z0-9])"+re.escape(t)+r"(?=\s*\d)") for t in seq]
    for m0 in pats[0].finditer(ntext):
        pos=m0.end(); start=m0.start(); ok=True
        for p in pats[1:]:
            m=p.search(ntext,pos,pos+gap)
            if not m: ok=False; break
            pos=m.end()
        if ok: return (start,pos)
    return None

def shingles(q,n=6):
    w=[x for x in norm(q).split() if not re.fullmatch(r"[+-]|[0-9.]+",x)]
    return [" ".join(w[i:i+n]) for i in range(0,max(1,len(w)-n+1),3)] or [norm(q)]

def sha(b): return hashlib.sha256(b).hexdigest()

ATTR = re.compile(r"\s*[—–-]\s*(Abstract|Summary|Results|Introduction|Conclusion|Discussion|Sect\.?|§)[^\n]*$")
CITE = re.compile(r"\s*\[\d+\]\s*$")
def segments(q):
    """Composite quotes stitched from adjacent table cells ('..." "...') verify per segment."""
    parts=re.split(r'[”"]\s+[“"]', q)
    return [p for p in parts if len(p)>8] if len(parts)>1 else [q]

def strip_attr(q):
    """gpt2's radio-section quotes end with an embedded '— <Location>...[n]' attribution;
    its digits are locations, not quoted values — strip before expression extraction."""
    q = CITE.sub("", q)
    q = ATTR.sub("", q)
    return CITE.sub("", q).strip()

def parse_entries(md, style):
    txt=open(md,encoding="utf-8").read()
    out=[]
    for ch in re.split(r"\n(?=#{2,3} )", txt):
        header=ch.splitlines()[0][:70]
        decl=[pathlib.Path(m).name for m in re.findall(r"sources/([A-Za-z0-9_.\-]+)", ch)]
        arx=re.findall(r"arXiv[: ]*(\d{4}\.\d{4,5})", ch)+re.findall(r"abs/(\d{4}\.\d{4,5})", ch)
        if style=="block":
            qs,cur=[],[]
            for line in ch.splitlines():
                if line.startswith(">"): cur.append(line.lstrip("> ").strip())
                else:
                    if cur: qs.append(" ".join(cur)); cur=[]
            if cur: qs.append(" ".join(cur))
            qs=[strip_attr(q) for q in qs if len(strip_attr(q))>40]
        else:
            qs=[strip_attr(q) for q in re.findall(r'"([^"]{60,})"', ch)]
        if qs: out.append((header,qs,decl,sorted(set(arx))))
    return out

def load_file(f):
    try: return norm(open(f,encoding="utf-8",errors="replace").read())
    except Exception: return None

def bound_files(srcdir, decl, arx):
    out=[]
    for d in decl:
        out += [f for f in glob.glob(srcdir+"/**/"+d, recursive=True)]
    for a in arx:
        for f in glob.glob(srcdir+"/**/*", recursive=True):
            if a in f and pathlib.Path(f).suffix in (".txt",".tex",".html",".xml",".md"):
                out.append(f)
        for f in glob.glob(srcdir+"/*"+a+"*/**/*", recursive=True):
            if pathlib.Path(f).suffix in (".txt",".tex",".html",".xml",".md"): out.append(f)
    return sorted(set(f for f in out if pathlib.Path(f).is_file()
                      and pathlib.Path(f).suffix in (".txt",".tex",".html",".xml",".md")))

import json as _json
BMAP=_json.load(open("b_binding_map.json")) if pathlib.Path("b_binding_map.json").exists() else {}

def check(harvest, srcdir, style, ledger):
    nfail=nok=0
    hname=pathlib.Path(harvest).parent.name
    for header,qs,decl,arx in parse_entries(harvest,style):
        files=bound_files(srcdir,decl,arx)
        bm=BMAP.get(hname,{})
        for k,v in bm.items():
            if header.startswith(k):
                files=sorted(set(files+[srcdir+"/"+f for f in v["files"]]))
        for q in qs:
            segs=segments(q)
            seq=expr_seq(q); sh=shingles(q)
            row={"harvest":pathlib.Path(harvest).parent.name,"entry":header,
                 "quote_full":q,"quote_sha256":sha(q.encode()),
                 "expr_seq":seq,"declared_files":len(files),"verdict":"FAIL","basis":None,
                 "source":None,"source_sha256":None,"span":None,"shingle":0.0}
            best=None
            for f in files:
                c=load_file(f)
                if c is None: continue
                if len(segs)>1:
                    spans=[find_ordered(expr_seq(sg),c) for sg in segs if expr_seq(sg)]
                    span=(min(a for a,_ in spans),max(b for _,b in spans)) if spans and all(spans) else None
                else:
                    span=find_ordered(seq,c) if seq else None
                shf=sum(1 for s in sh if s in c)/len(sh)
                cand={"f":f,"span":span,"sh":shf}
                if best is None or ((span is not None, shf) > (best["span"] is not None, best["sh"])):
                    best=cand
            if best:
                row["source"]=best["f"]; row["shingle"]=round(best["sh"],3)
                row["source_sha256"]=sha(open(best["f"],"rb").read())
                distinctive = any(len(t.replace(".",""))>=6 for t in seq)
                shmin = 0.0 if (distinctive or len(segs)>1) else (0.05 if len(seq)>=5 else 0.20)
                # len(segs)>1: composite table-cell quotes carry no prose; every segment
                # already ordered-matched in the same file, which is the evidence.
                if seq and best["span"] and best["sh"]>=shmin:
                    c=load_file(best["f"]); a,b=best["span"]
                    row["span"]={"start":a,"end":b,"excerpt":c[a:min(b,a+600)]}
                    row["verdict"]="PASS"; row["basis"]="ordered-expressions+shingle"
                elif not seq:
                    # evidence = an exact contiguous >=6-word span; no shingle gate needed
                    w=norm(q).split()
                    for i in range(len(w)-6):
                        ph=" ".join(w[i:i+6]); c=load_file(best["f"]); j=c.find(ph)
                        if j>=0:
                            row["span"]={"start":j,"end":j+len(ph),"excerpt":ph}
                            row["verdict"]="PASS"; row["basis"]="exact-phrase-span"; break
            ledger.append(row)
            ok=row["verdict"]=="PASS"; nok+=ok; nfail+=(not ok)
            if not ok:
                print(f"  FAIL [{header[:48]}] files={len(files)} sh={row['shingle']}: {q[:56]}...")
    print(f"{pathlib.Path(harvest).parent.name}: {nok} PASS / {nfail} FAIL")
    return nfail

def selftest():
    h=open("platoon/gpt2_trackb_cmb/HARVEST_CMB_BOUNDS.md",encoding="utf-8").read()
    m=re.search(r"> ([^\n]*power deficit[^\n]*)", h); good=m.group(1)
    src=norm(open("platoon/gpt2_trackb_cmb/sources/anomaly_planck2013_1303.5075v2_pages.txt",
                  encoding="utf-8",errors="replace").read())
    def runs(q): return find_ordered(expr_seq(q),src) is not None
    assert runs(good), "genuine B3.1 must pass"
    bad1=good.replace("5-10","99-88").replace("5–10","99–88").replace("2.5–3","9.9–8.8").replace("2.5-3","9.9-8.8").replace("40","99")
    assert not runs(bad1), "absent-fragment corruption must fail"
    bad2=good.replace("5–10","10–5").replace("5-10","10-5").replace("2.5–3","3–2.5").replace("2.5-3","3-2.5")
    assert bad2!=good and not runs(bad2), "ORDER-SWAP corruption must fail"
    e="the dipole moment is 3.15 x 10 - 5 in these units"
    srcx=norm("we measure the dipole moment is 3.15 x 10 - 5 in these units exactly")
    assert find_ordered(expr_seq(e),srcx) is not None
    eflip="the dipole moment is 3.15 x 10 + 5 in these units"
    assert find_ordered(expr_seq(eflip),srcx) is None, "EXPONENT-SIGN flip must fail"
    print("self-test: genuine passes; absent-fragment, order-swap, and exponent-sign corruptions ALL fail")

selftest()
ledger=[]
f1=check("platoon/gpt2_trackb_cmb/HARVEST_CMB_BOUNDS.md","platoon/gpt2_trackb_cmb/sources","block",ledger)
f2=check("platoon/agy_trackb_h0/HARVEST_H0_ANISOTROPY.md","platoon/agy_trackb_h0/sources","agy",ledger)
json.dump(ledger,open("b_verify_ledger.json","w"),indent=1,ensure_ascii=False)
npass=sum(1 for e in ledger if e["verdict"]=="PASS")
print(f"TOTAL: {npass} PASS / {f1+f2} FAIL; ledger rows={len(ledger)}; zero-fallback binding enforced")
sys.exit(1 if (f1+f2) else 0)
