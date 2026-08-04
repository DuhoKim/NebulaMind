#!/usr/bin/env python3
"""LLM-polish the 57 cluster names from their c-TF-IDF keywords. Local ollama;
concise human-readable astronomy topic names. Writes cluster_names.json."""
import json, os, re, urllib.request, sys
ENG=os.path.dirname(os.path.abspath(__file__))
MODEL=os.environ.get("NAME_MODEL","qwen3:30b-a3b-instruct-2507-q4_K_M")
SRC=f"{ENG}/frontier_map_v3_reranked.json" if os.path.exists(f"{ENG}/frontier_map_v3_reranked.json") else f"{ENG}/frontier_map_v3.json"
clusters=json.load(open(SRC))["clusters"]
SYS=("Name astronomy research-topic clusters. Given a cluster's distinctive keywords, reply with ONE "
     "concise, human-readable topic name of 3 to 7 words — the kind a review paper would use. "
     "Examples: 'Dark energy and the Hubble tension'; 'JWST high-redshift galaxy formation'; "
     "'r-process nucleosynthesis in metal-poor stars'; 'Supermassive black-hole accretion and AGN'. "
     "Use standard acronyms (JWST, AGN, CMB, LyC, FRB). Reply with ONLY the name — no quotes, no preamble.")
def name(kws):
    body=json.dumps({"model":MODEL,"prompt":f"Keywords: {', '.join(kws)}\nTopic name:","system":SYS,
        "stream":False,"options":{"temperature":0.2,"num_predict":24}}).encode()
    r=urllib.request.urlopen(urllib.request.Request("http://localhost:11434/api/generate",data=body,
        headers={"Content-Type":"application/json"}),timeout=120)
    t=json.load(r)["response"]
    t=re.sub(r"<think>.*?</think>","",t,flags=re.S).strip().splitlines()
    t=[x for x in t if x.strip()][-1] if t else ""
    return t.strip().strip('"').strip("'").rstrip(".").strip()
out={}
for i,c in enumerate(sorted(clusters,key=lambda x:-x.get("frontier_score_cite",0))):
    nm=name(c["keywords"][:8]); out[str(c["cluster"])]=nm
    if i<12: print(f"  C{c['cluster']:<2} {nm}   [{', '.join(c['keywords'][:4])}]")
json.dump(out,open(f"{ENG}/cluster_names.json","w"),indent=1,ensure_ascii=False)
print(f"\nnamed {len(out)} clusters -> cluster_names.json  (model {MODEL})")
