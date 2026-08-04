#!/usr/bin/env python3
"""Simulate a few days of daily ingest by paging back through recent arXiv
astro-ph.GA/CO submissions. Reuses ingest_incremental (dedup, embed, assign,
append-only delta store). Politeness-paced. Frozen snapshot untouched."""
import sys, time, json, os, urllib.request, numpy as np
import ingest_incremental as ii
ENG=os.path.dirname(os.path.abspath(__file__)); DELTA=f"{ENG}/delta"

def fetch_page(start, per=100):
    import xml.etree.ElementTree as ET
    q=("https://export.arxiv.org/api/query?search_query=cat:astro-ph.GA+OR+cat:astro-ph.CO"
       f"&start={start}&max_results={per}&sortBy=submittedDate&sortOrder=descending")
    xml=urllib.request.urlopen(urllib.request.Request(q,headers={"User-Agent":"NebulaMind-ingest/1"}),timeout=60).read()
    root=ET.fromstring(xml); out=[]
    A=ii.ATOM; X=ii.ARX
    for e in root.findall(f"{A}entry"):
        aid=e.find(f"{A}id").text.split("/abs/")[-1]; base=aid.split("v")[0]
        prim=e.find(f"{X}primary_category"); cat=prim.get("term") if prim is not None else ""
        yr=(e.find(f"{A}published").text or "")[:10]
        out.append({"arxiv_id":base,"version":aid,"title":ii.clean(e.find(f"{A}title").text),
                    "abstract":ii.clean(e.find(f"{A}summary").text),"primary_category":cat,
                    "year":int(yr[:4]) if yr[:4].isdigit() else None,"submitted":yr})
    return out

def main():
    pages=int(sys.argv[1]) if len(sys.argv)>1 else 4
    cents=np.load(f"{ENG}/centroids_v2.npy"); cm=json.load(open(f"{ENG}/centroids_meta.json"))
    order,TAU,TDR=cm["order"],cm["tau_assign"],cm["tau_drift"]
    dl=f"{DELTA}/new_papers.jsonl"
    seen={json.loads(l)["arxiv_id"] for l in open(dl)} if os.path.exists(dl) else set()
    lab=json.load(open(f"{DELTA}/new_labels.json")) if os.path.exists(f"{DELTA}/new_labels.json") else {}
    total=0; dates=set()
    for pg in range(pages):
        raw=fetch_page(pg*100,100)
        papers=[p for p in raw if p["arxiv_id"] not in seen and len(p["abstract"].split())>=40]
        for p in papers: seen.add(p["arxiv_id"])
        if not papers: print(f"page {pg}: nothing new"); time.sleep(3.2); continue
        V=ii.embed([f'{p["title"]}. {p["abstract"]}' for p in papers])
        Vn=V/(np.linalg.norm(V,axis=1,keepdims=True)+1e-9); sims=Vn@cents.T
        best=sims.argmax(1); bs=sims.max(1)
        with open(f"{DELTA}/new_emb.f32","ab") as fe: fe.write(np.ascontiguousarray(V,np.float32).tobytes())
        with open(dl,"a") as fj:
            for i,p in enumerate(papers):
                cl=order[int(best[i])] if float(bs[i])>=TAU else -1
                fj.write(json.dumps({**p,"source":"arxiv_new","source_tier":"preprint","cluster":cl,
                    "assign_cos":round(float(bs[i]),3),"keyword":[p["primary_category"]],"bibcode":None})+"\n")
                lab[p["arxiv_id"]]=cl; dates.add(p.get("submitted"))
        total+=len(papers); print(f"page {pg}: +{len(papers)} (cum {total})  dates {min(dates)}..{max(dates)}")
        time.sleep(3.2)  # arXiv politeness
    json.dump(lab,open(f"{DELTA}/new_labels.json","w"))
    print(f"\nbackfill done: +{total} papers over dates {min(dates)}..{max(dates)} ({len(dates)} distinct submit dates)")

if __name__=="__main__": main()
