#!/usr/bin/env python3
"""Producer-vs-consumer digest cross-check. Rerun any time; final run at transfer completion.

Compares local_sha256 in every ACCEPTED transfer receipt against Dustin Lang's
independently produced digest list (dr10-r-path.sha256sum, archived beside this script).
sha256sum binary-mode lines (`hash *path`) are handled; a leading `*` is part of the
format, not the path — the first run of this comparison misread it and reported 140
phantom "not in list" rows.
"""
import json, sys
D = {}
for line in open(__file__.rsplit("/",1)[0] + "/dr10-r-path.sha256sum"):
    parts = line.rstrip("\n").split(None, 1)
    if len(parts) == 2:
        D[parts[1].lstrip("*")] = parts[0]
m = x = a = 0
bad = []
for line in open("/Users/duhokim/NebulaMindData/dr10_south_image_r/receipts.jsonl"):
    try: r = json.loads(line)
    except Exception: continue
    if r.get("outcome") != "ACCEPTED": continue
    a += 1
    his = D.get(r["destination_relative_path"])
    if his == r["local_sha256"]: m += 1
    else: x += 1; bad.append((r["destination_relative_path"], r["local_sha256"][:16], (his or "ABSENT")[:16]))
print(f"accepted {a:,}  match {m:,}  problem {x:,}")
for b in bad[:10]: print("  !!", b)
sys.exit(1 if x else 0)
