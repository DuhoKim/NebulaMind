#!/usr/bin/env python3
"""Pull GA+CO refereed 2009-2026 from NASA ADS via cursorMark. Rich metadata, abstract-level (Layer A).
Reference graph is pulled in a separate pass to keep pages fast. Writes JSONL incrementally + is resumable."""
import json, os, time, sys, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ENV = "/Users/duhokim/NebulaMind/NebulaMind/backend/.env"
OUT_JSONL = os.path.join(HERE, "corpus_ga_co_2009_2026.jsonl")
STATE = os.path.join(HERE, "pull_state.json")
LOG = os.path.join(HERE, "pull.log")

def log(m):
    line = f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {m}"
    print(line, flush=True)
    with open(LOG, "a") as f: f.write(line + "\n")

def token():
    for ln in open(ENV):
        if ln.startswith("NM_ADS_API_KEY="):
            return ln.split("=",1)[1].strip().strip('"').strip("'")
    raise SystemExit("no NM_ADS_API_KEY")

Q = '(arxiv_class:"astro-ph.GA" OR arxiv_class:"astro-ph.CO") AND property:refereed AND pubdate:[2009-01 TO 2026-12]'
FL = "bibcode,title,abstract,author,aff,pubdate,year,pub,doi,keyword,citation_count,read_count,property,data,facility,bibgroup,identifier"
BASE = "https://api.adsabs.harvard.edu/v1/search/query"
TOK = token()

def fetch(cursor):
    params = urllib.parse.urlencode({"q": Q, "fl": FL, "rows": 2000, "sort": "bibcode desc, id desc", "cursorMark": cursor})
    req = urllib.request.Request(BASE + "?" + params, headers={"Authorization": f"Bearer {TOK}"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            log(f"  retry {attempt+1}: {e}")
            time.sleep(5 * (attempt + 1))
    raise SystemExit("too many failures")

def main():
    cursor = "*"
    got = 0
    # resume
    if os.path.exists(STATE):
        st = json.load(open(STATE))
        cursor = st.get("cursor", "*"); got = st.get("got", 0)
        log(f"resuming at got={got}")
        mode = "a"
    else:
        mode = "w"
    fout = open(OUT_JSONL, mode)
    total = None
    while True:
        d = fetch(cursor)
        resp = d.get("response", {})
        if total is None:
            total = resp.get("numFound"); log(f"numFound={total}")
        docs = resp.get("docs", [])
        if not docs:
            log("no docs; done"); break
        for doc in docs:
            fout.write(json.dumps(doc, ensure_ascii=False) + "\n")
        got += len(docs); fout.flush()
        nxt = d.get("nextCursorMark")
        json.dump({"cursor": nxt, "got": got}, open(STATE, "w"))
        log(f"got {got}/{total}")
        if nxt == cursor:
            log("cursor stable; done"); break
        cursor = nxt
        time.sleep(0.4)
    fout.close()
    log(f"DONE total_written={got}")

if __name__ == "__main__":
    main()
