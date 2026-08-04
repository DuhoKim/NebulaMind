#!/usr/bin/env python3
"""Re-warm the deep layer with table-aware chunking. Re-extracts from CACHED html/pdf (no re-download)
and re-embeds, so every deep-read paper gets [TABLE] chunks. Also clears stale KB extractions.
Resumable: skips papers already re-done (marked by a .v2 flag)."""
import os, glob, sys, time
sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/tools")
import nm_fulltext_layer as ft
CACHE = ft.CACHE
KB = os.path.join(os.path.dirname(CACHE), "kb_cache")
LOG = os.path.join(os.path.dirname(CACHE), "rewarm.log")
def log(m):
    line=f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}] {m}"; print(line,flush=True); open(LOG,"a").write(line+"\n")
aids = sorted({os.path.basename(f).rsplit(".",1)[0].replace(".chunks","").replace(".vecs","")
               for f in glob.glob(os.path.join(CACHE,"*.html")) + glob.glob(os.path.join(CACHE,"*.pdf"))})
log(f"re-warming {len(aids)} deep-layer papers with table-aware chunking")
done=0; t0=time.time()
for i,aid in enumerate(aids):
    flag=os.path.join(CACHE,f"{aid}.v2")
    if os.path.exists(flag): continue
    for ext in (".chunks.json",".vecs.npy"):
        f=os.path.join(CACHE,aid+ext)
        if os.path.exists(f): os.remove(f)
    kbf=os.path.join(KB,f"{aid}.json")            # invalidate stale KB extraction
    if os.path.exists(kbf): os.remove(kbf)
    try:
        ft.deep_layer_for(aid); open(flag,"w").write("v2"); done+=1
    except Exception as e:
        log(f"  [skip] {aid}: {str(e)[:60]}")
    if i%50==0 and i:
        el=(time.time()-t0)/60; rate=done/max(1e-9,el); eta=(len(aids)-i)/max(1e-9,rate)
        log(f"  {i}/{len(aids)}  redone={done}  {el:.0f}min  ETA~{eta:.0f}min")
log(f"DONE rewarm: redone={done} in {(time.time()-t0)/60:.0f}min")
