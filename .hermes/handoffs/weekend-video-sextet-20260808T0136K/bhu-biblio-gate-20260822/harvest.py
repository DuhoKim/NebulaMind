#!/usr/bin/env python3
"""BHU literature harvest — everything, including unpublished, with queries recorded.

The founding sweep recorded no queries, so its coverage could not be characterized.
This one writes its own coverage into the output: every query, every host, every count.
Hosts: arXiv API, INSPIRE, Crossref, Semantic Scholar — all keyless. Never portal.nersc.gov.
"""
import json, re, sys, time, urllib.request, urllib.parse, pathlib

OUT = pathlib.Path(__file__).parent / "harvest.json"
UA = {"User-Agent": "NebulaMind-BHU-biblio-gate/1.0 (mailto:duhokim81@gmail.com)"}

# One query set per bibliography branch, plus generic family terms.
QUERIES = [
 "universe inside a black hole", "universe as a black hole", "black hole cosmology interior",
 "cosmological natural selection", "black hole bounce new universe",
 "Einstein-Cartan cosmology torsion bounce", "spin fluid bounce cosmology",
 "baby universe black hole", "Schwarzschild interior cosmology",
 "regular black hole de Sitter core cosmology", "white hole big bang",
 "holographic big bang brane", "black hole universe expansion Gaztanaga",
 "torsion dark energy black hole", "every black hole contains a new universe",
]

def get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
        except Exception as e:
            if i == tries - 1: return None
            time.sleep(3 * (i + 1))

def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()

RECORDS, COVERAGE = {}, []

def add(rec):
    key = (rec.get("arxiv") or "").lower() or (rec.get("doi") or "").lower() or norm_title(rec.get("title"))
    if not key: return
    old = RECORDS.get(key)
    if old:   # merge: prefer filled venue/doi
        for k, v in rec.items():
            if v and not old.get(k): old[k] = v
    else:
        RECORDS[key] = rec

def arxiv_search(q, n=40):
    u = ("http://export.arxiv.org/api/query?search_query=" +
         urllib.parse.quote(f'all:"{q}"') + f"&start=0&max_results={n}")
    t = get(u)
    if not t: COVERAGE.append(["arxiv", q, "FAILED"]); return
    entries = re.findall(r"<entry>(.*?)</entry>", t, re.S)
    COVERAGE.append(["arxiv", q, len(entries)])
    for e in entries:
        g = lambda tag: (re.search(rf"<{tag}>(.*?)</{tag}>", e, re.S) or [None, ""])[1]
        aid = (g("id") or "").split("/abs/")[-1]
        jr = re.search(r"<arxiv:journal_ref[^>]*>(.*?)</arxiv:journal_ref>", e, re.S)
        doi = re.search(r"<arxiv:doi[^>]*>(.*?)</arxiv:doi>", e, re.S)
        add({"title": re.sub(r"\s+", " ", g("title")).strip(), "arxiv": re.sub(r"v\d+$", "", aid),
             "year": (g("published") or "")[:4], "journal_ref": jr.group(1).strip() if jr else "",
             "doi": doi.group(1).strip() if doi else "", "src": "arxiv"})

def inspire_search(q, n=40):
    u = ("https://inspirehep.net/api/literature?sort=mostrecent&size=%d&q=" % n +
         urllib.parse.quote(f'"{q}"') + "&fields=titles,arxiv_eprints,dois,publication_info,earliest_date")
    t = get(u)
    if not t: COVERAGE.append(["inspire", q, "FAILED"]); return
    try: hits = json.loads(t)["hits"]["hits"]
    except Exception: COVERAGE.append(["inspire", q, "PARSE-FAIL"]); return
    COVERAGE.append(["inspire", q, len(hits)])
    for h in hits:
        m = h.get("metadata", {})
        pi = (m.get("publication_info") or [{}])[0]
        add({"title": (m.get("titles") or [{}])[0].get("title", ""),
             "arxiv": ((m.get("arxiv_eprints") or [{}])[0].get("value", "")),
             "doi": ((m.get("dois") or [{}])[0].get("value", "")),
             "journal_ref": " ".join(str(pi.get(k, "")) for k in ("journal_title", "journal_volume", "year") if pi.get(k)),
             "year": str(m.get("earliest_date", ""))[:4], "src": "inspire"})

def s2_search(q, n=40):
    u = ("https://api.semanticscholar.org/graph/v1/paper/search?limit=%d&fields=title,year,externalIds,venue,publicationTypes&query=" % n
         + urllib.parse.quote(q))
    t = get(u)
    if not t: COVERAGE.append(["s2", q, "FAILED"]); return
    try: data = json.loads(t).get("data", [])
    except Exception: COVERAGE.append(["s2", q, "PARSE-FAIL"]); return
    COVERAGE.append(["s2", q, len(data)])
    for d in data:
        ex = d.get("externalIds") or {}
        add({"title": d.get("title", ""), "arxiv": ex.get("ArXiv", ""),
             "doi": (ex.get("DOI") or ""), "journal_ref": d.get("venue", ""),
             "year": str(d.get("year", "")), "src": "s2"})

def main():
    for q in QUERIES:
        arxiv_search(q); time.sleep(1)
        inspire_search(q); time.sleep(1)
        s2_search(q); time.sleep(1)
        print(f"  done: {q}  (records so far: {len(RECORDS)})", file=sys.stderr)
    OUT.write_text(json.dumps({
        "harvested_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "hosts": ["export.arxiv.org", "inspirehep.net", "api.semanticscholar.org"],
        "coverage": COVERAGE, "n_records": len(RECORDS),
        "records": sorted(RECORDS.values(), key=lambda r: r.get("year") or "")}, indent=1))
    print(f"  TOTAL unique records: {len(RECORDS)}", file=sys.stderr)

if __name__ == "__main__":
    main()
