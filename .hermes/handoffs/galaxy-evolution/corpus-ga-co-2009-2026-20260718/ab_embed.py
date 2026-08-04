#!/usr/bin/env python3
"""Fair A/B of embedding models on an UNBIASED citation answer key.
Given a query paper, a good model ranks the papers it actually cites near the top.
Models compared (all Ollama-served): nomic-embed-text, qwen3-embedding:0.6b, qwen3-embedding:4b.
Each uses its own recommended query/doc prompt. Metric: recall@10 / recall@20."""
import json, os, random, time, urllib.request, urllib.parse
import concurrent.futures as cf
import numpy as np

HERE=os.path.dirname(os.path.abspath(__file__))
ENV="/Users/duhokim/NebulaMind/NebulaMind/backend/.env"
CORPUS=os.path.join(HERE,"corpus_ga_co_2009_2026.jsonl")
OLLAMA="http://localhost:11434/api/embeddings"
LOG=os.path.join(HERE,"ab.log")
random.seed(42)

def log(m):
    line=f"[{time.strftime('%H:%M:%S')}] {m}"; print(line,flush=True)
    open(LOG,"a").write(line+"\n")

def token():
    for ln in open(ENV):
        if ln.startswith("NM_ADS_API_KEY="): return ln.split("=",1)[1].strip().strip('"').strip("'")

TOK=token()
N_QUERIES=120
N_DISTRACTORS=3000
ABS_CHARS=1200

# ---- load corpus ----
log("loading corpus...")
absmap={}
for ln in open(CORPUS):
    d=json.loads(ln)
    b=d.get("bibcode"); a=d.get("abstract")
    if b and a: absmap[b]=a[:ABS_CHARS]
bibs=list(absmap.keys())
log(f"corpus in memory: {len(bibs)} papers with abstracts")

# ---- sample queries, pull their references (answer key) from ADS ----
qsample=random.sample(bibs, 400)
def ads_refs(batch):
    q="bibcode:(" + " OR ".join(batch) + ")"
    params=urllib.parse.urlencode({"q":q,"fl":"bibcode,reference","rows":len(batch)})
    req=urllib.request.Request("https://api.adsabs.harvard.edu/v1/search/query?"+params,
        headers={"Authorization":f"Bearer {TOK}"})
    with urllib.request.urlopen(req,timeout=120) as r:
        return json.loads(r.read().decode())["response"]["docs"]
log("pulling reference lists for candidate queries...")
refmap={}
for i in range(0,len(qsample),100):
    for doc in ads_refs(qsample[i:i+100]):
        refmap[doc["bibcode"]]=doc.get("reference",[]) or []
    time.sleep(0.4)
corpus_set=set(absmap)
queries=[]
for b,refs in refmap.items():
    pos=[r for r in refs if r in corpus_set and r!=b]
    if len(pos)>=3:
        queries.append((b,set(pos)))
    if len(queries)>=N_QUERIES: break
log(f"usable queries (>=3 in-corpus citations): {len(queries)}")

# ---- build retrieval pool: all positives + distractors ----
pool=set()
for _,pos in queries: pool|=pos
qbibs={b for b,_ in queries}
pool-=qbibs
distract=random.sample([b for b in bibs if b not in pool and b not in qbibs], N_DISTRACTORS)
pool=list(pool)+distract
log(f"pool size: {len(pool)} ({len(pool)-N_DISTRACTORS} positives + {N_DISTRACTORS} distractors)")

# ---- embedding via Ollama with per-model prompts ----
def prompts(model, text, is_query):
    if model.startswith("nomic"):
        return ("search_query: " if is_query else "search_document: ")+text
    if model.startswith("qwen3-embedding"):
        if is_query:
            return "Instruct: Given a scientific paper abstract, retrieve the abstracts of the papers it cites\nQuery: "+text
        return text
    return text

def embed_one(model,text):
    body=json.dumps({"model":model,"prompt":text}).encode()
    req=urllib.request.Request(OLLAMA,data=body,headers={"Content-Type":"application/json"})
    for _ in range(4):
        try:
            with urllib.request.urlopen(req,timeout=120) as r:
                return np.array(json.loads(r.read().decode())["embedding"],dtype=np.float32)
        except Exception as e:
            time.sleep(2)
    return None

def embed_many(model, items, is_query):
    out={}
    def work(kv):
        k,txt=kv; return k, embed_one(model, prompts(model,txt,is_query))
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for k,v in ex.map(work, items):
            out[k]=v
    return out

def recall_at(qvec, posset, poolkeys, poolmat, ks=(10,20)):
    sims=poolmat@qvec
    order=np.argsort(-sims)
    ranked=[poolkeys[i] for i in order]
    res={}
    for k in ks:
        topk=set(ranked[:k])
        res[k]=len(topk & posset)/min(k,len(posset))
    return res

MODELS=["nomic-embed-text:v1.5","qwen3-embedding:0.6b","qwen3-embedding:4b"]
results={}
for model in MODELS:
    t0=time.time()
    log(f"=== {model}: embedding pool ({len(pool)}) ===")
    pe=embed_many(model, [(b,absmap[b]) for b in pool], is_query=False)
    poolkeys=[b for b in pool if pe.get(b) is not None]
    M=np.vstack([pe[b] for b in poolkeys]); M/= (np.linalg.norm(M,axis=1,keepdims=True)+1e-9)
    log(f"  embedding {len(queries)} queries ...")
    qe=embed_many(model, [(b,absmap[b]) for b,_ in queries], is_query=True)
    r10=[]; r20=[]
    for b,pos in queries:
        qv=qe.get(b);
        if qv is None: continue
        qv=qv/(np.linalg.norm(qv)+1e-9)
        rr=recall_at(qv,pos,poolkeys,M)
        r10.append(rr[10]); r20.append(rr[20])
    results[model]=(float(np.mean(r10)),float(np.mean(r20)),len(r10),time.time()-t0)
    log(f"  {model}: recall@10={np.mean(r10):.3f} recall@20={np.mean(r20):.3f}  ({time.time()-t0:.0f}s)")

log("\n===== RESULTS (higher = better) =====")
for m,(a,b,n,t) in results.items():
    log(f"  {m:26s}  recall@10={a:.3f}  recall@20={b:.3f}  (n={n}, {t:.0f}s)")
json.dump(results, open(os.path.join(HERE,"ab_results.json"),"w"), indent=2)
log("DONE")
