#!/usr/bin/env python3
"""Adapter: reranked frontier_map_v3 (57 clusters) -> frontend Frontier[] TS.
Polished acronym-aware names; score = frontier_score_cite (all-domain activity, 0-1);
score_v1 kept as the GA-controversy score. Writes frontiersData.v3.staging.ts."""
import json, os
ENG=os.path.dirname(os.path.abspath(__file__))
BASE=f"{ENG}/frontier_map_v3.json"
SRC=f"{ENG}/frontier_map_v3_reranked.json" if os.path.exists(f"{ENG}/frontier_map_v3_reranked.json") else BASE
m=json.load(open(SRC)); cl=m["clusters"]
baseline=json.load(open(BASE))
delta=[json.loads(line) for line in open(f"{ENG}/delta/new_papers.jsonl") if line.strip()]

def ranks(rows):
    ranked=sorted((r for r in rows if r.get("tractable") == 1),
                  key=lambda r: (-r.get("score_v1", 0), r["cluster"]))
    return {r["cluster"]: i + 1 for i, r in enumerate(ranked)}

previous_ranks=ranks(baseline["clusters"])
current_ranks=ranks(cl)
current_top=sorted((r for r in cl if r.get("tractable") == 1),
                   key=lambda r: (-r.get("score_v1", 0), r["cluster"]))[:12]
stored_movement=m.get("rank_movements") if isinstance(m.get("rank_movements"),dict) else {}
movement={}
for r in current_top:
    key=str(r["cluster"])
    movement[key]=stored_movement.get(key) or {
        "cluster": r["cluster"],
        "previousRank": previous_ranks.get(r["cluster"],current_ranks[r["cluster"]]),
        "currentRank": current_ranks[r["cluster"]],
        "delta": previous_ranks.get(r["cluster"],current_ranks[r["cluster"]])-current_ranks[r["cluster"]],
        "deltaPapers": r.get("delta_papers", 0),
    }
submitted=sorted(str(p["submitted"])[:10] for p in delta if p.get("submitted"))
comparison=m.get("rank_comparison") or {
    "baseline_as_of": "2026-07-18",
    "reranked_as_of": "2026-07-20",
    "delta_from": submitted[0] if submitted else None,
    "delta_to": submitted[-1] if submitted else None,
    "delta_papers": len(delta),
    "assigned_papers": sum(p.get("cluster", -1) != -1 for p in delta),
}
ranking_update={
    "baselineAsOf": comparison["baseline_as_of"],
    "fullSnapshotAsOf": comparison.get("full_snapshot_as_of",comparison["baseline_as_of"]),
    "rerankedAsOf": comparison["reranked_as_of"],
    "deltaFrom": comparison["delta_from"],
    "deltaTo": comparison["delta_to"],
    "deltaPapers": comparison["delta_papers"],
    "assignedPapers": comparison["assigned_papers"],
    "cumulativeDeltaPapers": comparison.get("cumulative_delta_papers",comparison["delta_papers"]),
    "cumulativeAssignedPapers": comparison.get("cumulative_assigned_papers",comparison["assigned_papers"]),
}
import os as _os
NAMES=json.load(open(f"{ENG}/cluster_names.json")) if _os.path.exists(f"{ENG}/cluster_names.json") else {}
ACR={"jwst":"JWST","agn":"AGN","agns":"AGN","tde":"TDE","tdes":"TDEs","pbh":"PBH","pbhs":"PBHs",
 "frb":"FRB","frbs":"FRBs","lae":"LAE","laes":"LAEs","lyc":"LyC","cmb":"CMB","ism":"ISM","mzr":"MZR",
 "fmr":"FMR","sfr":"SFR","ssfr":"sSFR","bao":"BAO","ede":"EDE","smbh":"SMBH","ghz":"GHz","cemp":"CEMP",
 "hi":"HI","co":"CO","uv":"UV","ir":"IR","smg":"SMG","smgs":"SMGs","igm":"IGM","grb":"GRB","sne":"SNe",
 "imf":"IMF","iii":"III","ii":"II","fdm":"FDM","sfdm":"SFDM","eor":"EoR","xray":"X-ray","x-ray":"X-ray",
 "lcdm":"ΛCDM","r-process":"r-process","s-process":"s-process","metal-poor":"metal-poor"}
def nm(w): return ACR.get(w.lower(), w.capitalize())
def title(kws): return " · ".join(nm(k) for k in kws[:3])
def desc(c):
    kws=", ".join(nm(k) for k in c["keywords"][:6]); scope="galaxy-evolution" if c["ga_frac"]>=c["co_frac"] else "cosmology"
    return f"A {scope} cluster ({c['size']} papers, median {c['year_median']}) around {kws}. Contested-measurement rate {c['strict_tension']:.2f}."
rows=[]
for c in sorted(cl,key=lambda x:-x.get("frontier_score_cite",0)):
    rows.append({"cluster":c["cluster"],"name":NAMES.get(str(c["cluster"])) or title(c["keywords"]),"desc":desc(c),"size":c["size"],
        "yearMedian":c["year_median"],"recentFrac":round(c["recent_frac"],3),"citeMedian":c["cite_median"],
        "nDebates":int(round(c["strict_tension"]*c["size"])),"nUnknowns":0,
        "score":round(c.get("frontier_score_cite",0),3),"scoreV1":round(c["score_v1"],3),
        "tractable":c["tractable"],"keywords":c["keywords"],"topic":None,"topicFlagged":False})
hdr=("// Generated from frontier_map_v3 (57 clusters, 120,676 papers) + arXiv delta re-rank.\n"
 "// structure as-of 2026-07-18 (last full re-cluster) · counts current-through the latest arXiv ingest.\n"
 "// score = citation-activity (all-domain, 0-1); scoreV1 = galaxy-evolution controversy score (CO-vetoed=0).\n\n"
 "export type Frontier = {\n  cluster: number; name: string; desc: string; size: number; yearMedian: number;\n"
 "  recentFrac: number; citeMedian: number; nDebates: number; nUnknowns: number;\n"
 "  score: number; scoreV1: number; tractable: number; keywords: string[]; topic: string | null; topicFlagged: boolean;\n};\n\n"
 "export const FRONTIER_RANKING_UPDATE = "+json.dumps(ranking_update,indent=2,ensure_ascii=False)+" as const;\n\n"
 "export type FrontierRankMovement = { cluster: number; previousRank: number; currentRank: number; delta: number; deltaPapers: number };\n"
 "export const FRONTIER_RANK_MOVEMENT: Record<number, FrontierRankMovement> = "+json.dumps(movement,indent=2,ensure_ascii=False)+";\n\n"
 "export const FRONTIERS: Frontier[] = "+json.dumps(rows,indent=2,ensure_ascii=False)+";\n")
open(f"{ENG}/frontiersData.v3.staging.ts","w").write(hdr)
print(f"wrote {len(rows)} clusters. top-14 by citation activity (what the Clustering view will show):")
for r in rows[:14]: print(f"  {r['score']:.2f}  {r['name']}  (size {r['size']}, GA={r['tractable']})")
