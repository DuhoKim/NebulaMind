#!/usr/bin/env python3
"""Embed the full GA+CO corpus with qwen3-embedding:4b (2560-d) via Ollama batched /api/embed.
Resumable: memmap for vectors + per-batch done flags. Output aligned to bibcodes.json order."""
import json, os, time, urllib.request
import concurrent.futures as cf
import html, re as _re
import numpy as np
_TAG=_re.compile(r"<[^>]+>")
def clean(x):
    if not x: return ""
    if isinstance(x,list): x=" ".join(x)
    x=html.unescape(x); x=_TAG.sub(" ",x); return _re.sub(r"\s+"," ",x).strip()

HERE=os.path.dirname(os.path.abspath(__file__))
CORPUS=os.path.join(HERE,"corpus_ga_co_2009_2026.jsonl")
EMB=os.path.join(HERE,"emb_qwen4b.f32")
BIBS=os.path.join(HERE,"bibcodes.json")
DONE=os.path.join(HERE,"done_qwen4b.npy")
META=os.path.join(HERE,"embed_meta.json")
LOG=os.path.join(HERE,"embed.log")
MODEL="qwen3-embedding:4b"; DIM=2560; BATCH=64; WORKERS=4; TEXTCHARS=4000
URL="http://localhost:11434/api/embed"

def log(m):
    line=f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}] {m}"
    print(line,flush=True); open(LOG,"a").write(line+"\n")

def load_text():
    bibs=[]; texts=[]
    for ln in open(CORPUS):
        d=json.loads(ln); b=d.get("bibcode"); ab=d.get("abstract")
        if not (b and ab): continue
        ttl=clean(d.get("title")); ab=clean(ab)
        bibs.append(b); texts.append((ttl+". "+ab)[:TEXTCHARS])
    return bibs,texts

def embed_batch(texts):
    body=json.dumps({"model":MODEL,"input":texts}).encode()
    req=urllib.request.Request(URL,data=body,headers={"Content-Type":"application/json"})
    for _ in range(5):
        try:
            with urllib.request.urlopen(req,timeout=300) as r:
                return np.array(json.loads(r.read().decode())["embeddings"],dtype=np.float32)
        except Exception as e:
            log(f"   batch retry: {str(e)[:80]}"); time.sleep(4)
    raise RuntimeError("batch failed after retries")

def main():
    bibs,texts=load_text(); n=len(bibs)
    log(f"corpus loaded: {n} papers")
    if not os.path.exists(BIBS): json.dump(bibs,open(BIBS,"w"))
    json.dump({"n":n,"dim":DIM,"model":MODEL,"batch":BATCH,"text_chars":TEXTCHARS,"dtype":"float32"},open(META,"w"),indent=2)
    mm=np.memmap(EMB,dtype=np.float32,mode=("r+" if os.path.exists(EMB) else "w+"),shape=(n,DIM))
    nb=(n+BATCH-1)//BATCH
    done=np.load(DONE) if os.path.exists(DONE) else np.zeros(nb,dtype=bool)
    todo=[i for i in range(nb) if not done[i]]
    log(f"batches: {nb} total, {len(todo)} to do, {int(done.sum())} already done")
    t0=time.time(); base=int(done.sum()); did=0; lastflush=time.time()
    def work(bi):
        s=bi*BATCH; e=min(s+BATCH,n)
        return bi,s,embed_batch(texts[s:e])
    with cf.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        for bi,s,vecs in ex.map(work,todo):
            mm[s:s+len(vecs)]=vecs; done[bi]=True; did+=1
            if time.time()-lastflush>20 or did==len(todo):
                mm.flush(); np.save(DONE,done); lastflush=time.time()
                el=time.time()-t0; rate=did/max(1e-9,el)  # batches/sec this session
                remain=len(todo)-did; eta=remain/max(1e-9,rate)/60
                pct=100*(base+did)/nb
                log(f"  {base+did}/{nb} batches ({pct:.1f}%)  ~{(base+did)*BATCH}/{n} papers  {rate*BATCH:.0f} papers/s  ETA~{eta:.0f}min")
    mm.flush(); np.save(DONE,done)
    log(f"DONE embedded {int(done.sum())*BATCH}~{n} papers in {(time.time()-t0)/60:.1f}min -> {EMB}")

if __name__=="__main__": main()
