#!/usr/bin/env python3
"""Canonical deep-layer pre-warm: full-text-embed the top-N most-cited corpus papers.
Self-gating: WAITS until the abstract embedding finishes (no GPU contention), then runs.
Reuses fulltext_layer.deep_layer_for -> cached + resumable (skips papers already deep-read)."""
import json, os, re, sys, time
sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/tools")
import nm_fulltext_layer as ft

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "corpus_ga_co_2009_2026.jsonl")
EMB_LOG = os.path.join(HERE, "embed.log")
LOG = os.path.join(HERE, "prewarm.log")
N = 5000
ARX = re.compile(r"(?:arXiv:)?(\d{4}\.\d{4,5})", re.I)

def log(m):
    line = f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {m}"
    print(line, flush=True); open(LOG, "a").write(line + "\n")

def abstract_embedding_done():
    try:
        return "DONE embedded" in open(EMB_LOG).read()
    except Exception:
        return False

def main():
    # 1. gate on the abstract embedding finishing
    waited = 0
    while not abstract_embedding_done():
        if waited % 1800 == 0:
            log("waiting for abstract embedding to finish before pre-warm (no GPU contention)...")
        time.sleep(300); waited += 300
    log("abstract embedding complete -> starting canonical full-text pre-warm")

    # 2. pick top-N most-cited papers that have an arXiv id
    rows = []
    for ln in open(CORPUS):
        d = json.loads(ln); c = d.get("citation_count") or 0
        aid = next((ARX.search(str(s)).group(1) for s in (d.get("identifier") or []) if ARX.search(str(s))), None)
        if aid:
            rows.append((c, aid, d["bibcode"]))
    rows.sort(key=lambda r: -r[0])
    top = rows[:N]
    log(f"selected top {len(top)} most-cited papers (cite range {top[0][0]}..{top[-1][0]})")

    # 3. full-text-embed each (cached + resumable)
    ok = fail = skip = 0; t0 = time.time()
    for i, (c, aid, bib) in enumerate(top):
        cj = os.path.join(ft.CACHE, f"{aid}.vecs.npy")
        if os.path.exists(cj):
            skip += 1
        else:
            try:
                ch, _ = ft.deep_layer_for(aid); ok += 1
            except Exception as e:
                fail += 1; log(f"  [skip] {aid}: {str(e)[:70]}")
        if i % 50 == 0 and i:
            el = (time.time() - t0) / 60
            rate = (ok + fail) / max(1e-9, el)  # papers/min this session
            eta = (len(top) - i) / max(1e-9, rate)
            log(f"  {i}/{len(top)}  new={ok} cached={skip} fail={fail}  {el:.0f}min  ETA~{eta:.0f}min")
    log(f"DONE pre-warm: new={ok} cached={skip} fail={fail} in {(time.time()-t0)/60:.0f}min")

if __name__ == "__main__":
    main()
