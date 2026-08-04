#!/usr/bin/env python3
"""Emergent topic derivation from the qwen3-embedding-4b vectors — from scratch, no inherited topics.
Pipeline (BERTopic-style): L2-normalize -> UMAP(2560->N) -> HDBSCAN -> c-TF-IDF labels -> provisional
frontier score. Outputs frontier_map_v2.json, cluster_labels_v2.json, topics_summary.txt.

Run AFTER embedding completes:
  python derive_topics.py                 # full 120k
  python derive_topics.py --subset 20000  # quick sanity on a slice
  python derive_topics.py --min-cluster-size 300
"""
import argparse, json, os, re, sys, time, html
import numpy as np
_TAG2=re.compile(r"<[^>]+>")
def _clean(x):
    if not x: return ""
    if isinstance(x,list): x=" ".join(x)
    x=html.unescape(x); x=_TAG2.sub(" ",x); return re.sub(r"\s+"," ",x).strip()

HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,"emb_qwen4b.f32"); BIBS=os.path.join(HERE,"bibcodes.json")
META=os.path.join(HERE,"embed_meta.json"); CORPUS=os.path.join(HERE,"corpus_ga_co_2009_2026.jsonl")
DONE=os.path.join(HERE,"done_qwen4b.npy")
OUT_MAP=os.path.join(HERE,"frontier_map_v2.json"); OUT_LAB=os.path.join(HERE,"cluster_labels_v2.json")
OUT_SUM=os.path.join(HERE,"topics_summary.txt"); LOG=os.path.join(HERE,"topics.log")
RECENT_YEAR=2023  # papers from this year onward count as "recent" for growth

ASTRO_STOP={"galaxy","galaxies","star","stars","stellar","using","use","used","results","result","show",
 "shows","find","found","observations","observation","observed","sample","samples","data","study","studies",
 "present","paper","also","however","within","two","one","three","new","high","low","large","small","based",
 "may","can","would","could","these","those","our","we","been","between","different","towards","toward",
 "cosmic","cosmological","astrophysics","physics","models","model","mass","masses"}

def log(m):
    line=f"[{time.strftime('%H:%M:%S')}] {m}"; print(line,flush=True); open(LOG,"a").write(line+"\n")

def load_meta_and_text():
    bibs=json.load(open(BIBS)); idx={b:i for i,b in enumerate(bibs)}
    n=len(bibs)
    year=np.zeros(n,dtype=np.int32); cite=np.zeros(n,dtype=np.int32)
    text=[""]*n; title=[""]*n
    for ln in open(CORPUS):
        d=json.loads(ln); b=d.get("bibcode")
        if b not in idx: continue
        i=idx[b]
        try: year[i]=int(str(d.get("year") or (d.get("pubdate") or "0")[:4]))
        except: year[i]=0
        cite[i]=int(d.get("citation_count") or 0)
        tt=_clean(d.get("title")); ab=_clean(d.get("abstract"))
        title[i]=tt; text[i]=(tt+". "+ab)[:2000]
    return bibs,idx,year,cite,text,title

def ctfidf_labels(labels, text, k=8):
    from sklearn.feature_extraction.text import CountVectorizer
    uniq=sorted(set(labels)-{-1})
    docs=[" ".join(text[i] for i in range(len(text)) if labels[i]==c) for c in uniq]
    stop="english"
    cv=CountVectorizer(stop_words=stop, token_pattern=r"[A-Za-z][A-Za-z\-]{2,}", max_features=40000, lowercase=True)
    X=cv.fit_transform(docs)                       # clusters x terms
    vocab=np.array(cv.get_feature_names_out())
    keep=np.array([not (v in ASTRO_STOP) for v in vocab])
    tf=X.toarray().astype(float)
    tf[:,~keep]=0
    # c-TF-IDF: term freq per class * log(1 + N_docs_total / df_across_classes)
    df=(tf>0).sum(0)+1e-9
    idf=np.log(1+len(uniq)/df)
    w=tf*idf
    labels_out={}
    for r,c in enumerate(uniq):
        top=vocab[np.argsort(-w[r])[:k]]
        labels_out[c]=list(top)
    return labels_out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--subset",type=int,default=0)
    ap.add_argument("--min-cluster-size",type=int,default=400)
    ap.add_argument("--umap-dim",type=int,default=15)
    ap.add_argument("--allow-partial",action="store_true")
    a=ap.parse_args()
    meta=json.load(open(META)); N=meta["n"]; DIM=meta["dim"]
    log(f"loading embeddings {EMB} ({N}x{DIM})")
    X=np.array(np.memmap(EMB,dtype=np.float32,mode="r",shape=(N,DIM)))
    norms=np.linalg.norm(X,axis=1)
    embedded=norms>1e-6
    log(f"embedded rows: {int(embedded.sum())}/{N}")
    if int(embedded.sum())<N and not a.allow_partial and a.subset==0:
        log("ERROR: embedding not complete. Re-run after it finishes, or use --allow-partial/--subset."); sys.exit(2)
    bibs,idx,year,cite,text,title=load_meta_and_text()
    rows=np.where(embedded)[0]
    if a.subset: rows=rows[:a.subset]
    log(f"clustering {len(rows)} papers")
    Xn=X[rows]/ (norms[rows][:,None])
    import umap, hdbscan
    log(f"UMAP -> {a.umap_dim}d (cosine)...")
    t=time.time()
    red=umap.UMAP(n_neighbors=15,n_components=a.umap_dim,metric="cosine",random_state=42,low_memory=True).fit_transform(Xn)
    log(f"  UMAP done {time.time()-t:.0f}s")
    log(f"HDBSCAN (min_cluster_size={a.min_cluster_size})...")
    t=time.time()
    cl=hdbscan.HDBSCAN(min_cluster_size=a.min_cluster_size,min_samples=10,metric="euclidean",
                       cluster_selection_method="eom",core_dist_n_jobs=-1).fit(red)
    lab=cl.labels_
    ncl=len(set(lab)-{-1}); noise=int((lab==-1).sum())
    log(f"  HDBSCAN done {time.time()-t:.0f}s -> {ncl} clusters, {noise} noise ({100*noise/len(rows):.1f}%)")
    # local text arrays aligned to rows
    ltext=[text[i] for i in rows]; lyear=year[rows]; lcite=cite[rows]; lbib=[bibs[i] for i in rows]
    log("c-TF-IDF labels...")
    kw=ctfidf_labels(list(lab), ltext, k=8)
    # per-cluster stats + frontier score
    clusters=[]
    for c in sorted(set(lab)-{-1}):
        m=lab==c; sz=int(m.sum())
        yr=lyear[m]; ct=lcite[m]
        recent=float((yr>=RECENT_YEAR).mean())
        ymed=int(np.median(yr[yr>0])) if (yr>0).any() else 0
        cmed=float(np.median(ct))
        # representatives: highest-cited in cluster
        order=np.argsort(-ct); reps=[lbib[i] for i in np.where(m)[0][order[:5]]]
        clusters.append({"cluster":int(c),"size":sz,"year_median":ymed,"recent_frac":round(recent,3),
                         "cite_median":round(cmed,1),"keywords":kw.get(c,[]),"sample_bibcodes":reps})
    # provisional frontier score: growth-weighted activity (NOTE: debate/unknown overlay to be added later)
    sizes=np.array([c["size"] for c in clusters],float); rec=np.array([c["recent_frac"] for c in clusters])
    cm=np.array([c["cite_median"] for c in clusters])
    def mm(x): return (x-x.min())/(np.ptp(x)+1e-9)
    score=0.55*rec + 0.25*mm(np.log1p(sizes)) + 0.20*mm(np.log1p(cm))
    for c,s in zip(clusters,score): c["frontier_score_provisional"]=round(float(s),3)
    clusters.sort(key=lambda c:-c["frontier_score_provisional"])
    json.dump({"n_clusters":ncl,"n_papers":len(rows),"noise":noise,
               "note":"provisional frontier score = growth-weighted; debate/unknown overlay TBD",
               "clusters":clusters}, open(OUT_MAP,"w"), indent=2)
    json.dump({lbib[i]:int(lab[i]) for i in range(len(rows))}, open(OUT_LAB,"w"))
    with open(OUT_SUM,"w") as f:
        f.write(f"EMERGENT TOPICS from {len(rows)} papers -> {ncl} clusters ({100*noise/len(rows):.1f}% noise)\n")
        f.write("(ranked by provisional frontier score; debate/unknown overlay pending)\n\n")
        for i,c in enumerate(clusters,1):
            f.write(f"{i:2d}. [score {c['frontier_score_provisional']}] size {c['size']}, "
                    f"med.yr {c['year_median']}, recent {int(100*c['recent_frac'])}%, med.cites {c['cite_median']}\n")
            f.write(f"    {', '.join(c['keywords'])}\n\n")
    log(f"DONE -> {OUT_MAP}, {OUT_LAB}, {OUT_SUM}")

if __name__=="__main__": main()
