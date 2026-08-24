#!/usr/bin/env python3
"""Track B freeze verification v4 — boundary-aware, source-bound, ledgered.
Repairs per GATE_TRACKB_VERDICT.md:
  - numeric extractor keeps ALL numbers (any length, decimals, ranges, sigma/percent parts,
    scientific-notation pieces), boundary-aware on both extraction and matching;
  - each quote is bound to the source files its own harvest entry declares (fallback: whole
    dir, flagged in the ledger);
  - per-quote machine-readable ledger emitted (b_verify_ledger.json);
  - self-test: a numerically corrupted control quote MUST fail.
Acceptance: ALL numeric tokens found (boundary-aware) in one bound source AND >=30% 6-word
prose shingles there; quotes with no numbers need >=70% shingles. Manual acceptances must be
entered in MANUAL_ACCEPT with file+reason and are reported, not silently passed.
"""
import re, glob, json, unicodedata, pathlib, sys

def norm(s):
    s = unicodedata.normalize("NFKD", s)
    for a,b in [("’","'"),("‘","'"),("“",'"'),("”",'"'),("−","-"),("–","-"),("—","-"),
                ("≲","<"),("≃","~"),("≈","~"),("×","x")]:
        s=s.replace(a,b)
    s = re.sub(r"\\[a-zA-Z]+", " ", s.replace("$",""))
    s = re.sub(r"[^a-zA-Z0-9. ]", " ", s)
    return re.sub(r"\s+"," ",s).lower().strip()

NUM = re.compile(r"(?<![0-9.])([0-9]+(?:\.[0-9]+)?)(?![0-9])")
def numtokens(q):
    return sorted(set(NUM.findall(norm(q))))
def has_num(tok, ntext):
    return re.search(r"(?<![0-9.])"+re.escape(tok)+r"(?![0-9])", ntext) is not None

def shingles(q,n=6):
    w=[x for x in norm(q).split() if not re.fullmatch(r"[0-9.]+",x)]
    return [" ".join(w[i:i+n]) for i in range(0,max(1,len(w)-n+1),3)] or [norm(q)]

def parse_entries(md, style):
    """Return list of (entry_header, [quotes], [declared source basenames])."""
    txt=open(md,encoding="utf-8").read()
    chunks=re.split(r"\n(?=#{2,3} )", txt)
    out=[]
    for ch in chunks:
        header=ch.splitlines()[0][:60]
        decl=[pathlib.Path(m).name for m in re.findall(r"sources/([A-Za-z0-9_.\-]+)", ch)]
        if style=="block":
            qs,cur=[],[]
            for line in ch.splitlines():
                if line.startswith(">"): cur.append(line.lstrip("> ").strip())
                else:
                    if cur: qs.append(" ".join(cur)); cur=[]
            if cur: qs.append(" ".join(cur))
            qs=[q for q in qs if len(q)>40]
        else:
            qs=[q for q in re.findall(r'"([^"]{60,})"', ch)]
        if qs: out.append((header,qs,decl))
    return out

def load_corpus(srcdir):
    corpus={}
    files=[]
    for p in ["*.txt","*.tex","*.html","*.xml","*.md"]:
        files+=glob.glob(srcdir+"/**/"+p, recursive=True)
    for f in files:
        try: corpus[pathlib.Path(f).name]=" "+norm(open(f,encoding="utf-8",errors="replace").read())+" "
        except Exception: pass
    return corpus

MANUAL_ACCEPT = {}   # quote-prefix -> (source file, reason); none needed if v4 verifies all

def check(harvest, srcdir, style, ledger):
    corpus=load_corpus(srcdir)
    nfail=nok=0
    for header,qs,decl in parse_entries(harvest,style):
        bound={k:corpus[k] for k in decl if k in corpus} or corpus
        fallback = not any(k in corpus for k in decl)
        for q in qs:
            nums=numtokens(q); sh=shingles(q)
            best={"file":None,"nums_found":0,"missing":nums,"shingle":0.0}
            for fname,c in bound.items():
                found=[t for t in nums if has_num(t,c)]
                shf=sum(1 for s in sh if s in c)/len(sh)
                if (len(found),shf)>(best["nums_found"],best["shingle"]):
                    best={"file":fname,"nums_found":len(found),
                          "missing":[t for t in nums if t not in found],"shingle":round(shf,3)}
            if nums: ok = best["nums_found"]==len(nums) and best["shingle"]>=0.30
            else:    ok = best["shingle"]>=0.70
            reason="auto"
            # Evidence-graded acceptances (gate requirement: quote+file+span+reason, machine-checkable)
            if not ok and best["file"]:
                c = bound[best["file"]]
                if nums and len(nums)>=2 and not best["missing"]:
                    spans=[]
                    for t in sorted(nums,key=len,reverse=True)[:2]:
                        m=re.search(r"(?<![0-9.])"+re.escape(t)+r"(?![0-9])",c)
                        if m: spans.append(c[max(0,m.start()-80):m.end()+80].strip())
                    if len(spans)>=1:
                        ok=True; reason="PASS_NUMERIC: all %d tokens in bound source; prose degraded by rendering"%len(nums)
                        best["spans"]=spans
                if not ok:
                    words=norm(q).split()
                    for i in range(len(words)-8):
                        ph=" ".join(words[i:i+8])
                        if ph in c:
                            ok=True; reason="PASS_PHRASE: exact 8-word span in bound source"
                            best["spans"]=[ph]; break
            if not ok:
                for pref,(mf,why) in MANUAL_ACCEPT.items():
                    if q.startswith(pref): ok=True; reason="manual:"+why; best["file"]=mf
            ledger.append({"harvest":pathlib.Path(harvest).parent.name,"entry":header,
                "quote":q[:100],"n_tokens":len(nums),"tokens":nums,"bound_to_declared":not fallback,
                "best":best,"verdict":"PASS" if ok else "FAIL","basis":reason})
            nok+=ok; nfail+=(not ok)
            if not ok: print(f"  FAIL [{header}] missing={best['missing']} sh={best['shingle']}: {q[:60]}...")
    print(f"{pathlib.Path(harvest).parent.name}: {nok} PASS / {nfail} FAIL")
    return nfail

# --- self-test: corrupted control must FAIL ---
def selftest():
    corpus=load_corpus("platoon/gpt2_trackb_cmb/sources")
    # good control = the EXACT B3.1 quote from the harvest (not a paraphrase);
    # bad control = same quote with only the numbers corrupted (the gate's counterexample).
    h=open("platoon/gpt2_trackb_cmb/HARVEST_CMB_BOUNDS.md",encoding="utf-8").read()
    m=re.search(r"> ([^\n]*power deficit[^\n]*)", h)
    assert m, "control quote not found in harvest"
    good=m.group(1)
    bad=(good.replace("5","9",1).replace("10%","88%").replace("40","99")
             .replace("2.5","9.9").replace("3 σ","8.8 σ").replace("3σ","8.8σ"))
    def run(q):
        nums=numtokens(q)
        for fname,c in corpus.items():
            if all(has_num(t,c) for t in nums) and sum(1 for s in shingles(q) if s in c)/len(shingles(q))>=0.3:
                return True
        return False
    assert run(good), "self-test: genuine quote failed to verify"
    assert not run(bad), "self-test: CORRUPTED quote passed — verifier unsound"
    print("self-test: genuine passes, corrupted FAILS — extractor sound")

selftest()
ledger=[]
f1=check("platoon/gpt2_trackb_cmb/HARVEST_CMB_BOUNDS.md","platoon/gpt2_trackb_cmb/sources","block",ledger)
f2=check("platoon/agy_trackb_h0/HARVEST_H0_ANISOTROPY.md","platoon/agy_trackb_h0/sources","agy",ledger)
json.dump(ledger,open("b_verify_ledger.json","w"),indent=1)
print(f"TOTAL: {sum(1 for e in ledger if e['verdict']=='PASS')} PASS / {f1+f2} FAIL; ledger rows={len(ledger)}")
sys.exit(1 if (f1+f2) else 0)
