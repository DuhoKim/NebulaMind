#!/usr/bin/env python3
"""Weekly incremental re-rank: fold the delta/ papers into each cluster's raw
metrics and recompute score_v1 with the FROZEN v1_constants from the snapshot
(a_half, tension/growth min-max) — never recomputed, so a burst of preprints
cannot rescale every cluster. Writes frontier_map_v3_reranked.json + shows movers."""
import datetime, json, os, re, math
from collections import Counter
ENG=os.path.dirname(os.path.abspath(__file__))
OUT=f"{ENG}/frontier_map_v3_reranked.json"
STRICT=["tension","discrepan","contradict","inconsisten","cannot explain","fail to reproduce","overpredict","underpredict"]
sre={t:re.compile(r'(?<![a-z])'+re.escape(t),re.I) for t in STRICT}
PHYS=re.compile(r'(?<![a-z])(?:strings?|branes?|surface|domain[-\s]?walls?)\s+tension',re.I)
def fires(text):
    cleaned=PHYS.sub(' ',text)
    return any(sre[t].search(cleaned if t=="tension" else text) for t in STRICT)

m=json.load(open(f"{ENG}/frontier_map_v3.json")); C=m["v1_constants"]
previous=json.load(open(OUT)) if os.path.exists(OUT) else m
a_half=C["a_half"]; t_lo,t_hi=C["tension_min"],C["tension_max"]; g_lo,g_hi=C["growth_min"],C["growth_max"]
def mm(x,lo,hi): return 0.0 if hi<=lo else max(0.0,min(1.0,(x-lo)/(hi-lo)))

# delta contributions per cluster
delta=[json.loads(l) for l in open(f"{ENG}/delta/new_papers.jsonl")]
dc={}
for p in delta:
    cl=p["cluster"]
    if cl==-1: continue
    d=dc.setdefault(cl,{"n":0,"hit":0,"ga":0,"co":0})
    d["n"]+=1
    if fires(f'{p["title"]} {p["abstract"]}'): d["hit"]+=1
    cat=(p.get("primary_category") or "").lower()
    if cat=="astro-ph.ga": d["ga"]+=1
    elif cat=="astro-ph.co": d["co"]+=1
    else: d["ga"]+=1  # cross-listed into GA/CO search; default in-scope GA

rows=[]
for c in m["clusters"]:
    cl=c["cluster"]; bs=c["size"]; d=dc.get(cl,{"n":0,"hit":0,"ga":0,"co":0})
    ns=bs+d["n"]
    base_hit=c["strict_tension"]*bs; base_rec=c["recent_frac"]*bs
    base_ga=c["ga_frac"]*bs; base_co=c["co_frac"]*bs
    st=(base_hit+d["hit"])/ns
    rf=(base_rec+d["n"])/ns                       # all delta papers are 2026 => recent
    gf=(base_ga+d["ga"])/ns; cf=(base_co+d["co"])/ns
    act=c["cite_inflow_recent"]/ns                # delta preprints add 0 recent cites (honest dilution)
    sat=act/(act+a_half) if act+a_half else 0.0
    tn=mm(st,t_lo,t_hi); gn=mm(rf,g_lo,g_hi); tr=1 if gf>=cf else 0
    score=sat*tr*(0.6*tn+0.4*gn)
    rows.append({**c,"size":ns,"strict_tension":round(st,5),"recent_frac":round(rf,4),
        "ga_frac":round(gf,5),"co_frac":round(cf,5),"sat_activity":round(sat,5),
        "tension_norm":round(tn,5),"growth_norm":round(gn,5),"tractable":tr,
        "score_v1":round(score,5),"delta_papers":d["n"]})

# rankings (GA-tractable only, as v3 does)
def ranks(rs): 
    g=sorted([r for r in rs if r["tractable"]==1],key=lambda r:-r["score_v1"])
    return {r["cluster"]:i+1 for i,r in enumerate(g)}
old=ranks(previous["clusters"]); new=ranks(rows)

def previous_delta_count(doc):
    comparison=doc.get("rank_comparison") or {}
    for key in ("cumulative_delta_papers","delta_papers"):
        value=comparison.get(key)
        if isinstance(value,int) and value>=0:
            return min(value,len(delta))
    match=re.search(r"base \+ delta \((\d+) arXiv preprints",doc.get("reranked_over", ""))
    return min(int(match.group(1)),len(delta)) if match else 0

previous_count=previous_delta_count(previous)
recent_delta=delta[previous_count:]
submitted=sorted(str(p["submitted"])[:10] for p in recent_delta if p.get("submitted"))
snapshot_match=re.search(r"(\d{8})$", ENG)
full_snapshot_as_of=(datetime.datetime.strptime(snapshot_match.group(1), "%Y%m%d").date().isoformat()
                     if snapshot_match else None)
previous_comparison=previous.get("rank_comparison") or {}
previous_as_of=previous_comparison.get("reranked_as_of")
if not previous_as_of and os.path.exists(OUT):
    previous_as_of=datetime.datetime.fromtimestamp(os.path.getmtime(OUT),datetime.timezone.utc).date().isoformat()
if not previous_as_of:
    previous_as_of=full_snapshot_as_of
recent_cluster_counts=Counter(p["cluster"] for p in recent_delta if p.get("cluster")!=-1)
assigned_papers=sum(1 for p in recent_delta if p.get("cluster")!=-1)
cumulative_assigned_papers=sum(d["n"] for d in dc.values())
rank_movements={}
for cl,current_rank in new.items():
    previous_rank=old.get(cl,current_rank)
    rank_movements[str(cl)]={
        "cluster":cl,
        "previousRank":previous_rank,
        "currentRank":current_rank,
        "delta":previous_rank-current_rank,
        "deltaPapers":recent_cluster_counts.get(cl,0),
    }
rank_comparison={
    "baseline_as_of":previous_as_of,
    "full_snapshot_as_of":full_snapshot_as_of,
    "reranked_as_of":datetime.datetime.now(datetime.timezone.utc).date().isoformat(),
    "delta_from":submitted[0] if submitted else None,
    "delta_to":submitted[-1] if submitted else None,
    "delta_papers":len(recent_delta),
    "assigned_papers":assigned_papers,
    "cumulative_delta_papers":len(delta),
    "cumulative_assigned_papers":cumulative_assigned_papers,
}
out={**m,"clusters":rows,
     "reranked_over":f"base + delta ({len(delta)} arXiv preprints {rank_comparison['delta_from']}..{rank_comparison['delta_to']})",
     "rank_comparison":rank_comparison,"rank_movements":rank_movements,
     "v1_constants":C,"constants_frozen":True}
json.dump(out,open(OUT,"w"),indent=1)

movers=sorted([r for r in rows if r["tractable"]==1 and r["cluster"] in old and r["cluster"] in new],
              key=lambda r:(old[r["cluster"]]-new[r["cluster"]]))
kw=lambda r:", ".join(r["keywords"][:4])
print(f"re-ranked {len(rows)} clusters over base+{sum(d['n'] for d in dc.values())} delta papers. Constants FROZEN.")
print("\nBIGGEST RISERS (GA frontiers, Δrank = old→new):")
for r in movers[:6]:
    d=old[r["cluster"]]-new[r["cluster"]]
    if d<=0: continue
    print(f"  C{r['cluster']:<2} {old[r['cluster']]:>2}→{new[r['cluster']]:<2} (+{d})  +{r['delta_papers']} papers  score {r['score_v1']:.3f}  [{kw(r)[:40]}]")
print("BIGGEST FALLERS:")
for r in movers[::-1][:5]:
    d=old[r["cluster"]]-new[r["cluster"]]
    if d>=0: continue
    print(f"  C{r['cluster']:<2} {old[r['cluster']]:>2}→{new[r['cluster']]:<2} ({d})  +{r['delta_papers']} papers  score {r['score_v1']:.3f}  [{kw(r)[:40]}]")
print(f"\ntop-5 after re-rank: "+" · ".join(f"C{r['cluster']}({r['score_v1']:.2f})" for r in sorted([x for x in rows if x['tractable']==1],key=lambda r:-r['score_v1'])[:5]))
