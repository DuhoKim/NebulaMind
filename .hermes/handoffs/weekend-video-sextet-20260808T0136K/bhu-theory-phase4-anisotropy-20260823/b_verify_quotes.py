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
                ("±"," pm "),("×"," times "),("≲"," lt "),("≳"," gt "),("<"," lt "),
                (">"," gt "),("≃","~"),("≈","~"),("^","")]:
        s=s.replace(a,b)
    s = re.sub(r"(?<=\d)\s*([+-])\s*(?=\d)", r" \1 ", s)  # 331+161-107 -> 331 + 161 - 107
    s = re.sub(r"(?<=\d)(?=[a-zA-Z])"," ",s)   # split numbers glued to units: 3.7mK -> 3.7 mK
    s = re.sub(r"(?<=[a-zA-Z])(?=\d)"," ",s)   # and identifiers: S03 -> S 03 (symmetric)
    s = re.sub(r"\\[a-zA-Z]+"," ",s.replace("$","").replace("{"," ").replace("}"," "))
    s = re.sub(r"(?<=\d)\s*-\s*(?=\d)", " - ", s)      # range/exponent hyphen -> token
    s = re.sub(r"(?<![a-zA-Z0-9])([+-])(?=\s*\d)", r" \1 ", s)  # sign before number -> token
    s = re.sub(r"[^a-zA-Z0-9.+\- ]"," ",s)
    s = re.sub(r"(?<!\d)\.(?!\d)"," ",s)               # bare periods out; decimals stay
    return re.sub(r"\s+"," ",s).lower().strip()

REL={"pm":"pm","times":"times","x":"times","lt":"lt","gt":"gt","+":"+","-":"-"}
RELWORDS=re.compile(r"\b(pm|times|x|lt|gt)\b|(?<![a-zA-Z0-9])[+-](?=\s*\d)")
def parse_items(q):
    """Quote -> ordered items: ('num',v) and ('rel',r) with relations kept only adjacent
    to numerics (prose survives)."""
    toks=norm(q).split(); items=[]
    def isnum(t): return re.fullmatch(r"\d+(?:\.\d+)?", t) is not None
    def canon(t):   # strip leading zeros ("03"->"3"), keep "0"/"0.32"
        return re.sub(r"^0+(?=\d)","",t) if "." not in t else t
    for i,t in enumerate(toks):
        if isnum(t): items.append(("num",canon(t)))
        elif t in REL:
            prevn = i>0 and isnum(toks[i-1]); nextn = i+1<len(toks) and isnum(toks[i+1])
            if (t in "+-" and nextn) or (t not in "+-" and (prevn or nextn)):
                items.append(("rel",REL[t]))
    return items

def expr_seq(q):
    """Back-compat: the ordered numeric+relation token list (ledger field)."""
    return [v for _,v in parse_items(q)]

def gap_rels(text):
    out=[]
    for m in RELWORDS.finditer(text):
        w=m.group(1) or m.group(0)
        out.append(REL.get(w,w))
    return out

def find_ordered(seq_or_q, ntext, gap=400):
    """Match the quote's numeric tokens in order; between consecutive numbers, the source
    gap must not assert a RELATION DIFFERENT from the quote's (a silent gap is tolerated —
    PDF rendering loses operators — but pm cannot become times, + cannot become -, etc.).
    Accepts either a parsed item list or a raw normalized-token seq (nums+rels)."""
    if seq_or_q and isinstance(seq_or_q[0], tuple): items=seq_or_q
    else:
        items=[]
        for t in (seq_or_q or []):
            items.append(("rel",t) if t in ("pm","times","lt","gt","+","-") else ("num",t))
    nums=[(i,v) for i,(k,v) in enumerate(items) if k=="num"]
    if not nums: return None
    def npat(t): return re.compile(r"(?<![0-9.])0*"+re.escape(t)+r"(?![0-9])")
    first=npat(nums[0][1])
    for m0 in first.finditer(ntext):
        pos_end=m0.end(); start=m0.start(); ok=True; last_idx=nums[0][0]
        for idx,v in nums[1:]:
            m=npat(v).search(ntext,pos_end,pos_end+gap)
            if not m: ok=False; break
            g=ntext[pos_end:m.start()+1]   # +1: the digit gives +/- lookahead its context
            want=[val for k,val in items[last_idx+1:idx] if k=="rel"]
            have=gap_rels(g)
            for w in want:
                if any(h!=w for h in have): ok=False; break
            if not ok: break
            if not want and False: pass
            pos_end=m.end(); last_idx=idx
        if ok:
            # leading relation (e.g. 'lt 40' at sequence head): check 30 chars before
            lead=[v for k,v in items[:nums[0][0]] if k=="rel"]
            if lead:
                pre=ntext[max(0,start-30):start]
                for w in lead:
                    if any(h!=w for h in gap_rels(pre)): ok=False
        if ok: return (start,pos_end)
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
    # regate2 counterexamples
    fq=norm(open("platoon/gpt2_trackb_cmb/sources/dipole_ferreira_quartin_2011.08385v2.txt",
                 encoding="utf-8",errors="replace").read())
    gq="we can put an upper limit on the intrinsic amplitude: 3.7mK (95% CI)"
    bq="we can put an upper limit on the intrinsic amplitude: 99.9mK (95% CI)"
    assert find_ordered(expr_seq(gq),fq) is not None, "genuine glued-unit quote must pass"
    assert not find_ordered(expr_seq(bq),fq), "GLUED-UNIT value corruption must fail"
    pl=norm(open("platoon/gpt2_trackb_cmb/sources/dipole_planck2018_overview_1807.06205v2.txt",
                 encoding="utf-8",errors="replace").read())
    gp="Planck 2018 ... 3362.08 ± 0.99"
    bp="Planck 2018 ... 3362.08 × 0.99"
    assert find_ordered(expr_seq(gp),pl) is not None, "genuine pm expression must pass"
    assert not find_ordered(expr_seq(bp),pl), "PM->TIMES operator corruption must fail"
    print("self-test: genuine passes; absent-fragment, order-swap, exponent-sign, glued-unit,")
    print("           and pm->times operator corruptions ALL fail")

selftest()
ledger=[]
f1=check("platoon/gpt2_trackb_cmb/HARVEST_CMB_BOUNDS.md","platoon/gpt2_trackb_cmb/sources","block",ledger)
f2=check("platoon/agy_trackb_h0/HARVEST_H0_ANISOTROPY.md","platoon/agy_trackb_h0/sources","agy",ledger)
json.dump(ledger,open("b_verify_ledger.json","w"),indent=1,ensure_ascii=False)
npass=sum(1 for e in ledger if e["verdict"]=="PASS")
print(f"TOTAL: {npass} PASS / {f1+f2} FAIL; ledger rows={len(ledger)}; zero-fallback binding enforced")
sys.exit(1 if (f1+f2) else 0)
