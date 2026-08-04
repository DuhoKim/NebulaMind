#!/usr/bin/env python3
"""Honest frontier ranking via the citation graph (no LLM, no GPU).
For each emergent cluster, measure RECENT citation inflow = how many citations the cluster's papers
receive from recent (2023+) papers. That is a real 'the field is actively building on this' signal,
in the spirit of open-question density x growth. Enriches frontier_map_v2.json + rewrites the summary."""
import json, os
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__))
def P(n): return os.path.join(HERE, n)

lab = json.load(open(P("cluster_labels_v2.json")))          # bibcode -> cluster
fm = json.load(open(P("frontier_map_v2.json")))
# bibcode -> year
year = {}
for ln in open(P("corpus_ga_co_2009_2026.jsonl")):
    d = json.loads(ln); b = d.get("bibcode")
    try: year[b] = int(str(d.get("year") or (d.get("pubdate") or "0")[:4]))
    except Exception: year[b] = 0

# recent (2023+) citation inflow per cluster, from the 8.9M-edge graph
inflow = Counter(); inflow_recent = Counter()
for ln in open(P("references.jsonl")):
    d = json.loads(ln); citing = d.get("bibcode"); cy = year.get(citing, 0)
    for cited in (d.get("reference") or []):
        cl = lab.get(cited)
        if cl is None: continue
        inflow[cl] += 1
        if cy >= 2023: inflow_recent[cl] += 1

# enrich clusters + a citation-velocity frontier score
def mm(vals):
    vals = list(vals); lo, hi = min(vals), max(vals)
    return {i: (v - lo) / (hi - lo + 1e-9) for i, v in enumerate(vals)}
cl = fm["clusters"]
for c in cl:
    k = c["cluster"]; sz = max(1, c["size"])
    c["cite_inflow"] = int(inflow.get(k, 0))
    c["cite_inflow_recent"] = int(inflow_recent.get(k, 0))
    c["recent_cites_per_paper"] = round(inflow_recent.get(k, 0) / sz, 2)
rc = mm([c["recent_cites_per_paper"] for c in cl])
gr = mm([c["recent_frac"] for c in cl])
for i, c in enumerate(cl):
    # frontier = actively-cited-now (0.6) x growth (0.4)
    c["frontier_score_cite"] = round(0.6 * rc[i] + 0.4 * gr[i], 3)
cl.sort(key=lambda c: -c["frontier_score_cite"])
fm["note"] = "frontier_score_cite = recent(2023+) citations-per-paper (0.6) x recent-paper growth (0.4); citation-graph derived, no LLM"
json.dump(fm, open(P("frontier_map_v2.json"), "w"), indent=2)

with open(P("topics_summary.txt"), "w") as f:
    f.write(f"EMERGENT FRONTIERS from {fm['n_papers']} papers -> {fm['n_clusters']} clusters ({100*fm['noise']/fm['n_papers']:.0f}% noise)\n")
    f.write("ranked by CITATION-VELOCITY frontier score (recent citations/paper x growth); citation-graph derived\n\n")
    for i, c in enumerate(cl, 1):
        f.write(f"{i:2d}. [{c['frontier_score_cite']:.3f}] size {c['size']}, med.yr {c['year_median']}, "
                f"recent {int(100*c['recent_frac'])}%, recent-cites/paper {c['recent_cites_per_paper']}, "
                f"tot-cites-in {c['cite_inflow']:,}\n    {', '.join(c['keywords'])}\n\n")
print(f"ranked {len(cl)} frontiers by citation velocity; total recent inflow edges scored")
print("TOP 8:")
for c in cl[:8]:
    print(f"  [{c['frontier_score_cite']:.3f}] rc/p={c['recent_cites_per_paper']:>5} sz={c['size']:>4} | {', '.join(c['keywords'][:5])}")
