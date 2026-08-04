#!/usr/bin/env python3
"""Pull the outbound citation graph (bibcode -> [cited bibcodes]) for the full GA+CO corpus.
Runs on ADS only (no GPU) so it's safe alongside embedding. Resumable via cursorMark state."""
import json, os, time, urllib.request, urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__))
ENV="/Users/duhokim/NebulaMind/NebulaMind/backend/.env"
OUT=os.path.join(HERE,"references.jsonl"); STATE=os.path.join(HERE,"refs_state.json"); LOG=os.path.join(HERE,"refs.log")
def log(m):
    line=f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}] {m}"; print(line,flush=True); open(LOG,"a").write(line+"\n")
def token():
    for ln in open(ENV):
        if ln.startswith("NM_ADS_API_KEY="): return ln.split("=",1)[1].strip().strip('"').strip("'")
Q='(arxiv_class:"astro-ph.GA" OR arxiv_class:"astro-ph.CO") AND property:refereed AND pubdate:[2009-01 TO 2026-12]'
BASE="https://api.adsabs.harvard.edu/v1/search/query"; TOK=token()
def fetch(cursor):
    p=urllib.parse.urlencode({"q":Q,"fl":"bibcode,reference","rows":2000,"sort":"bibcode desc, id desc","cursorMark":cursor})
    req=urllib.request.Request(BASE+"?"+p,headers={"Authorization":f"Bearer {TOK}"})
    for a in range(6):
        try:
            with urllib.request.urlopen(req,timeout=180) as r: return json.loads(r.read().decode())
        except Exception as e:
            log(f"  retry {a+1}: {str(e)[:70]}"); time.sleep(5*(a+1))
    raise SystemExit("too many failures")
def main():
    cursor="*"; got=0; withrefs=0; totrefs=0; mode="w"
    if os.path.exists(STATE):
        st=json.load(open(STATE)); cursor=st["cursor"]; got=st["got"]; withrefs=st.get("withrefs",0); totrefs=st.get("totrefs",0); mode="a"; log(f"resume got={got}")
    f=open(OUT,mode); total=None
    while True:
        d=fetch(cursor); resp=d.get("response",{})
        if total is None: total=resp.get("numFound"); log(f"numFound={total}")
        docs=resp.get("docs",[])
        if not docs: log("no docs; done"); break
        for doc in docs:
            refs=doc.get("reference",[]) or []
            f.write(json.dumps({"bibcode":doc["bibcode"],"reference":refs},ensure_ascii=False)+"\n")
            if refs: withrefs+=1; totrefs+=len(refs)
        got+=len(docs); f.flush()
        nxt=d.get("nextCursorMark")
        json.dump({"cursor":nxt,"got":got,"withrefs":withrefs,"totrefs":totrefs},open(STATE,"w"))
        log(f"got {got}/{total}  ({withrefs} w/refs, {totrefs} edges)")
        if nxt==cursor: log("cursor stable; done"); break
        cursor=nxt; time.sleep(0.4)
    f.close(); log(f"DONE papers={got} with_refs={withrefs} total_edges={totrefs} -> {OUT}")
if __name__=="__main__": main()
