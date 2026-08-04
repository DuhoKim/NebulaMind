#!/usr/bin/env python3
"""Comprehensive embedding eval on the UNBIASED citation answer key.
One fixed test set (seed=42) -> every model scored identically -> leaderboard.
Backends: ollama (HTTP) and sentence-transformers (Apple MPS). Incremental + resumable."""
import json, os, random, time, urllib.request, urllib.parse
import concurrent.futures as cf
import numpy as np

HERE=os.path.dirname(os.path.abspath(__file__))
ENV="/Users/duhokim/NebulaMind/NebulaMind/backend/.env"
CORPUS=os.path.join(HERE,"corpus_ga_co_2009_2026.jsonl")
TESTSET=os.path.join(HERE,"testset.json")
LEADER=os.path.join(HERE,"leaderboard.json")
LOG=os.path.join(HERE,"eval.log")
OLLAMA="http://localhost:11434/api/embeddings"
random.seed(42)
N_QUERIES=120; N_DISTRACTORS=2500; TEXTCHARS=1500

def log(m):
    line=f"[{time.strftime('%H:%M:%S')}] {m}"; print(line,flush=True)
    open(LOG,"a").write(line+"\n")

def token():
    for ln in open(ENV):
        if ln.startswith("NM_ADS_API_KEY="): return ln.split("=",1)[1].strip().strip('"').strip("'")

def build_testset():
    log("building test set (load corpus, sample queries, pull citation answer key)...")
    txt={}
    for ln in open(CORPUS):
        d=json.loads(ln); b=d.get("bibcode")
        if b and d.get("abstract"):
            ttl=d.get("title") or ""
            if isinstance(ttl,list): ttl=" ".join(ttl)
            ab=d.get("abstract") or ""
            if isinstance(ab,list): ab=" ".join(ab)
            txt[b]=(ttl+" "+ab)[:TEXTCHARS]
    bibs=list(txt); log(f"corpus: {len(bibs)} papers")
    TOK=token()
    def ads_refs(batch):
        q="bibcode:("+" OR ".join(batch)+")"
        p=urllib.parse.urlencode({"q":q,"fl":"bibcode,reference","rows":len(batch)})
        r=urllib.request.Request("https://api.adsabs.harvard.edu/v1/search/query?"+p,
            headers={"Authorization":f"Bearer {TOK}"})
        with urllib.request.urlopen(r,timeout=120) as resp:
            return json.loads(resp.read().decode())["response"]["docs"]
    qsample=random.sample(bibs,400); refmap={}
    for i in range(0,len(qsample),100):
        for doc in ads_refs(qsample[i:i+100]): refmap[doc["bibcode"]]=doc.get("reference",[]) or []
        time.sleep(0.4)
    cs=set(txt); queries=[]
    for b,refs in refmap.items():
        pos=[r for r in refs if r in cs and r!=b]
        if len(pos)>=3: queries.append({"bib":b,"pos":sorted(set(pos))})
        if len(queries)>=N_QUERIES: break
    pool=set()
    for q in queries: pool|=set(q["pos"])
    qb={q["bib"] for q in queries}; pool-=qb
    distract=random.sample([b for b in bibs if b not in pool and b not in qb],N_DISTRACTORS)
    poollist=sorted(pool)+distract
    keep=set(poollist)|qb
    ts={"queries":queries,"pool":poollist,"n_pos":len(pool),"text":{b:txt[b] for b in keep}}
    json.dump(ts,open(TESTSET,"w"))
    log(f"testset: {len(queries)} queries, pool={len(poollist)} ({len(pool)} pos + {N_DISTRACTORS} distractors)")
    return ts

# ---- backends ----
def embed_ollama(model, items, prefix):
    def one(kv):
        k,t=kv; body=json.dumps({"model":model,"prompt":prefix+t}).encode()
        req=urllib.request.Request(OLLAMA,data=body,headers={"Content-Type":"application/json"})
        for _ in range(4):
            try:
                with urllib.request.urlopen(req,timeout=120) as r:
                    return k,np.array(json.loads(r.read().decode())["embedding"],dtype=np.float32)
            except Exception: time.sleep(2)
        return k,None
    out={}
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for k,v in ex.map(one, items): out[k]=v
    return out

_ST_CACHE={}
def embed_st(hf_id, items, prefix, st_kwargs):
    from sentence_transformers import SentenceTransformer
    if hf_id not in _ST_CACHE:
        _ST_CACHE[hf_id]=SentenceTransformer(hf_id, device="mps", trust_remote_code=True, **st_kwargs.get("init",{}))
    m=_ST_CACHE[hf_id]
    keys=[k for k,_ in items]; texts=[prefix+t for _,t in items]
    vecs=m.encode(texts, batch_size=st_kwargs.get("bs",16), normalize_embeddings=False,
                  convert_to_numpy=True, show_progress_bar=False)
    return {k:v.astype(np.float32) for k,v in zip(keys,vecs)}

def evaluate(name, backend, ref, pq, pd, ts, st_kwargs=None):
    pool=ts["pool"]; text=ts["text"]; queries=ts["queries"]
    t0=time.time()
    if backend=="ollama":
        pe=embed_ollama(ref,[(b,text[b]) for b in pool],pd)
        qe=embed_ollama(ref,[(q["bib"],text[q["bib"]]) for q in queries],pq)
    else:
        pe=embed_st(ref,[(b,text[b]) for b in pool],pd,st_kwargs or {})
        qe=embed_st(ref,[(q["bib"],text[q["bib"]]) for q in queries],pq,st_kwargs or {})
    pk=[b for b in pool if pe.get(b) is not None]
    M=np.vstack([pe[b] for b in pk]); M/=(np.linalg.norm(M,axis=1,keepdims=True)+1e-9)
    idx={b:i for i,b in enumerate(pk)}
    r10=[];r20=[];r100=[];mrr=[]
    for q in queries:
        qv=qe.get(q["bib"])
        if qv is None: continue
        qv=qv/(np.linalg.norm(qv)+1e-9)
        sims=M@qv; order=np.argsort(-sims)
        posset=set(q["pos"]); ranked=[pk[i] for i in order]
        r10.append(len(set(ranked[:10])&posset)/min(10,len(posset)))
        r20.append(len(set(ranked[:20])&posset)/min(20,len(posset)))
        r100.append(len(set(ranked[:100])&posset)/min(100,len(posset)))
        fr=next((i+1 for i,b in enumerate(ranked) if b in posset),0)
        mrr.append(1/fr if fr else 0)
    res={"model":name,"backend":backend,"dim":int(M.shape[1]),
         "recall@10":round(float(np.mean(r10)),4),"recall@20":round(float(np.mean(r20)),4),
         "recall@100":round(float(np.mean(r100)),4),"mrr":round(float(np.mean(mrr)),4),
         "n":len(r10),"sec":round(time.time()-t0)}
    log(f"  {name:30s} dim={res['dim']:5d} R@10={res['recall@10']:.3f} R@20={res['recall@20']:.3f} R@100={res['recall@100']:.3f} MRR={res['mrr']:.3f} ({res['sec']}s)")
    return res

QWEN_Q="Instruct: Given a paper's title and abstract, retrieve the title and abstract of the papers it cites\nQuery: "
MXBAI_Q="Represent this sentence for searching relevant passages: "
# (name, backend, ref, query_prefix, doc_prefix, st_kwargs)
MODELS=[
 ("nomic-embed-text","ollama","nomic-embed-text:v1.5","search_query: ","search_document: ",None),
 ("qwen3-embedding-0.6b","ollama","qwen3-embedding:0.6b",QWEN_Q,"",None),
 ("qwen3-embedding-4b","ollama","qwen3-embedding:4b",QWEN_Q,"",None),
 ("qwen3-embedding-8b","ollama","qwen3-embedding:8b",QWEN_Q,"",None),
 ("bge-m3","ollama","bge-m3","","",None),
 ("snowflake-arctic-embed2","ollama","snowflake-arctic-embed2","query: ","",None),
 ("mxbai-embed-large","ollama","mxbai-embed-large",MXBAI_Q,"",None),
 ("scincl","st","malteos/scincl","","",{"bs":32}),
 ("specter2-base","st","allenai/specter2_base","","",{"bs":32}),
 ("gte-qwen2-1.5b","st","Alibaba-NLP/gte-Qwen2-1.5B-instruct","Instruct: retrieve cited papers\nQuery: ","",{"bs":8}),
]

def main():
    ts=json.load(open(TESTSET)) if os.path.exists(TESTSET) else build_testset()
    board=json.load(open(LEADER)) if os.path.exists(LEADER) else []
    done={r["model"] for r in board}
    only=set(os.environ.get("ONLY","").split(",")) - {""}
    for name,backend,ref,pq,pd,stk in MODELS:
        if name in done: log(f"skip {name} (already scored)"); continue
        if only and name not in only: continue
        # ollama model must be present
        try:
            res=evaluate(name,backend,ref,pq,pd,ts,stk)
        except Exception as e:
            log(f"  {name}: FAILED {type(e).__name__}: {str(e)[:160]}"); continue
        board.append(res); json.dump(board,open(LEADER,"w"),indent=2)
    log("\n===== LEADERBOARD (by recall@10) =====")
    for r in sorted(board,key=lambda x:-x["recall@10"]):
        log(f"  {r['recall@10']:.3f}  R@20={r['recall@20']:.3f} MRR={r['mrr']:.3f}  {r['model']} (dim {r['dim']})")
    log("DONE_ALL")

if __name__=="__main__": main()
