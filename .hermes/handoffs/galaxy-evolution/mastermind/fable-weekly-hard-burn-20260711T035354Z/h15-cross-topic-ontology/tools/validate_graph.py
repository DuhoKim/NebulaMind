#!/usr/bin/env python3
"""H15 graph validator: JSON well-formed, edge endpoints exist, counts match, dep refs resolve."""
import json, sys
g = json.load(open(sys.argv[1]))
ids = {n["id"] for n in g["nodes"]}
errs = []
for e in g["edges"]:
    for k in ("src", "dst"):
        if e[k] not in ids: errs.append(f"dangling {k} {e[k]}")
for n in g["nodes"]:
    for d in n.get("deps", []):
        if d not in ids: errs.append(f"dangling dep {d} on {n['id']}")
c = g["counts"]
real = {"nodes": len(g["nodes"]), "edges": len(g["edges"]),
        "contradicts_edges": sum(1 for e in g["edges"] if e["kind"] == "contradicts"),
        "cross_topic_edges": sum(1 for e in g["edges"] if e["src"].split("-")[0] != e["dst"].split("-")[0])}
for k, v in real.items():
    if c.get(k) != v: errs.append(f"count {k}: stated {c.get(k)} actual {v}")
kinds = sorted({e["kind"] for e in g["edges"]})
print("kinds:", kinds, "| actual:", real)
print("ERRORS:" if errs else "VALIDATION OK", *errs, sep="\n" if errs else " ")
sys.exit(1 if errs else 0)
