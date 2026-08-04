#!/usr/bin/env python3
"""Dual-endpoint work-stealing embedder for the full GA+CO corpus with qwen3-embedding:4b.
Two Ollama boxes pull batches from one shared queue -> faster box does more. Resumable via done flags."""
import json, os, time, threading, queue, urllib.request
import numpy as np

HERE=os.path.dirname(os.path.abspath(__file__))
CORPUS=os.path.join(HERE,"corpus_ga_co_2009_2026.jsonl")
EMB=os.path.join(HERE,"emb_qwen4b.f32"); BIBS=os.path.join(HERE,"bibcodes.json")
DONE=os.path.join(HERE,"done_qwen4b.npy"); META=os.path.join(HERE,"embed_meta.json")
LOG=os.path.join(HERE,"embed.log")
MODEL="qwen3-embedding:4b"; DIM=2560; BATCH=64; TEXTCHARS=4000
# (name, url, n_threads)
ENDPOINTS=[("main","http://localhost:11434/api/embed",4),("macpro","http://192.188.0.4:11435/api/embed",2)]

lock=threading.Lock()
def log(m):
    line=f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}] {m}"
    with lock:
        print(line,flush=True); open(LOG,"a").write(line+"\n")

def load_text():
    bibs=[]; texts=[]
    for ln in open(CORPUS):
        d=json.loads(ln); b=d.get("bibcode"); ab=d.get("abstract")
        if not (b and ab): continue
        ttl=d.get("title") or ""
        if isinstance(ttl,list): ttl=" ".join(ttl)
        if isinstance(ab,list): ab=" ".join(ab)
        bibs.append(b); texts.append((ttl+". "+ab)[:TEXTCHARS])
    return bibs,texts

def embed_batch(url,texts):
    body=json.dumps({"model":MODEL,"input":texts}).encode()
    req=urllib.request.Request(url,data=body,headers={"Content-Type":"application/json"})
    for _ in range(6):
        try:
            with urllib.request.urlopen(req,timeout=300) as r:
                return np.array(json.loads(r.read().decode())["embeddings"],dtype=np.float32)
        except Exception as e:
            log(f"   {url.split('//')[1].split(':')[0]} retry: {str(e)[:70]}"); time.sleep(4)
    return None

def main():
    bibs,texts=load_text(); n=len(bibs)
    log(f"corpus loaded: {n} papers | endpoints: {[e[0] for e in ENDPOINTS]}")
    if not os.path.exists(BIBS): json.dump(bibs,open(BIBS,"w"))
    json.dump({"n":n,"dim":DIM,"model":MODEL,"batch":BATCH,"text_chars":TEXTCHARS,"dtype":"float32"},open(META,"w"),indent=2)
    mm=np.memmap(EMB,dtype=np.float32,mode=("r+" if os.path.exists(EMB) else "w+"),shape=(n,DIM))
    nb=(n+BATCH-1)//BATCH
    done=np.load(DONE) if os.path.exists(DONE) else np.zeros(nb,dtype=bool)
    q=queue.Queue()
    for i in range(nb):
        if not done[i]: q.put(i)
    total_todo=q.qsize()
    log(f"batches: {nb} total, {total_todo} to do, {int(done.sum())} done")
    state={"did":0,"t0":time.time(),"lastflush":time.time(),"percount":{e[0]:0 for e in ENDPOINTS}}

    def worker(name,url):
        while True:
            try: bi=q.get_nowait()
            except queue.Empty: return
            s=bi*BATCH; e=min(s+BATCH,n)
            vecs=embed_batch(url,texts[s:e])
            if vecs is None or len(vecs)!=(e-s):
                q.put(bi); time.sleep(2); continue
            mm[s:e]=vecs
            with lock:
                done[bi]=True; state["did"]+=1; state["percount"][name]+=1
                if time.time()-state["lastflush"]>20:
                    mm.flush(); np.save(DONE,done); state["lastflush"]=time.time()
                    did=state["did"]; el=time.time()-state["t0"]; rate=did/max(1e-9,el)
                    eta=(total_todo-did)/max(1e-9,rate)/60
                    pct=100*int(done.sum())/nb
                    log(f"  {int(done.sum())}/{nb} ({pct:.1f}%)  {rate*BATCH:.0f} papers/s  ETA~{eta:.0f}min  split={state['percount']}")
    threads=[]
    for name,url,nt in ENDPOINTS:
        for _ in range(nt):
            t=threading.Thread(target=worker,args=(name,url),daemon=True); t.start(); threads.append(t)
    for t in threads: t.join()
    mm.flush(); np.save(DONE,done)
    log(f"DONE {int(done.sum())}/{nb} batches in {(time.time()-state['t0'])/60:.1f}min  split={state['percount']} -> {EMB}")

if __name__=="__main__": main()
