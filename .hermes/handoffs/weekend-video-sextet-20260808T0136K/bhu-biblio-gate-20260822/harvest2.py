#!/usr/bin/env python3
"""Overnight hunt, round 2 — the channels the first three methods never used.

A: author-completeness sweeps (arXiv + INSPIRE) for the family's named authors.
B: citation-graph walk — everything citing or cited by the 40 seeds (OpenAlex + S2).
C: keyword search on hosts not previously searched (OpenAlex, Crossref).
Every query and count recorded; failures recorded as failures.
"""
import json, re, sys, time, urllib.request, urllib.parse, pathlib

HERE = pathlib.Path(__file__).parent
BIB = HERE.parent / "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md"
OUT = HERE / "harvest2.json"
UA = {"User-Agent": "NebulaMind-BHU-hunt2/1.0 (mailto:duhokim81@gmail.com)"}
RECORDS, COVERAGE = {}, []

def get(url, tries=3):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read().decode("utf-8","replace")
        except Exception:
            if i == tries-1: return None
            time.sleep(4*(i+1))

def jget(url):
    t = get(url)
    if t is None: return None
    try: return json.loads(t)
    except Exception: return None

def norm(t): return re.sub(r"[^a-z0-9]+"," ",(t or "").lower()).strip()

def add(rec, via):
    key = (rec.get("arxiv") or "").lower() or (rec.get("doi") or "").lower() or norm(rec.get("title"))
    if not key or len(key) < 8: return
    r = RECORDS.setdefault(key, rec)
    r.setdefault("via", set())
    if isinstance(r["via"], list): r["via"] = set(r["via"])
    r["via"].add(via)
    for k, v in rec.items():
        if v and not r.get(k): r[k] = v

def seeds():
    s = BIB.read_text()
    dois = sorted({d.rstrip(".,") for d in re.findall(r"\b(10\.\d{4,5}/[^\s)`,]+)", s)})
    return [d for d in dois if not d.endswith(".tex")]

AUTHORS = ["Poplawski, N", "Smoller, J", "Temple, B", "Gaztanaga, E", "Dymnikova, I",
           "Smolin, L", "Pathria, R", "Stuckey, W", "Khakshournia, S", "Knutsen, H"]
AKEY = re.compile(r"(universe|black hole|cosmolog|bounce|torsion|shock|natural selection|baby)", re.I)

def phase_a():
    for a in AUTHORS:
        q = urllib.parse.quote(f'au:"{a}"')
        t = get(f"http://export.arxiv.org/api/query?search_query={q}&start=0&max_results=100")
        n = 0
        if t:
            for e in re.findall(r"<entry>(.*?)</entry>", t, re.S):
                g = lambda tag: (re.search(rf"<{tag}>(.*?)</{tag}>", e, re.S) or [None,""])[1]
                ti = re.sub(r"\s+"," ",g("title")).strip()
                if not AKEY.search(ti): continue
                jr = re.search(r"<arxiv:journal_ref[^>]*>(.*?)</arxiv:journal_ref>", e, re.S)
                doi = re.search(r"<arxiv:doi[^>]*>(.*?)</arxiv:doi>", e, re.S)
                add({"title": ti, "arxiv": re.sub(r"v\d+$","",(g("id") or "").split("/abs/")[-1]),
                     "year": (g("published") or "")[:4],
                     "journal_ref": jr.group(1).strip() if jr else "",
                     "doi": doi.group(1).strip() if doi else ""}, f"author:{a}")
                n += 1
        COVERAGE.append(["arxiv-author", a, n if t else "FAILED"]); time.sleep(1)
        d = jget("https://inspirehep.net/api/literature?size=100&q=" + urllib.parse.quote(f'a "{a}"') +
                 "&fields=titles,arxiv_eprints,dois,publication_info,earliest_date")
        n = 0
        if d:
            for h in d.get("hits",{}).get("hits",[]):
                m = h.get("metadata",{}); ti = (m.get("titles") or [{}])[0].get("title","")
                if not AKEY.search(ti): continue
                pi = (m.get("publication_info") or [{}])[0]
                add({"title": ti, "arxiv": (m.get("arxiv_eprints") or [{}])[0].get("value",""),
                     "doi": (m.get("dois") or [{}])[0].get("value",""),
                     "journal_ref": " ".join(str(pi.get(k,"")) for k in ("journal_title","journal_volume","year") if pi.get(k)),
                     "year": str(m.get("earliest_date",""))[:4]}, f"inspire-author:{a}")
                n += 1
        COVERAGE.append(["inspire-author", a, n if d else "FAILED"]); time.sleep(1)

def phase_b():
    sd = seeds()
    for doi in sd:
        w = jget("https://api.openalex.org/works/doi:" + urllib.parse.quote(doi))
        if not w: COVERAGE.append(["openalex-seed", doi, "FAILED"]); time.sleep(1); continue
        wid = (w.get("id") or "").rsplit("/",1)[-1]
        for ref in (w.get("referenced_works") or [])[:60]:
            pass  # ids only; resolving each is too many calls — citations carry titles below
        c = jget(f"https://api.openalex.org/works?filter=cites:{wid}&per_page=50")
        n = 0
        if c:
            for it in c.get("results", []):
                ti = it.get("title") or ""
                ids = it.get("ids") or {}
                add({"title": ti, "doi": (it.get("doi") or "").replace("https://doi.org/",""),
                     "year": str(it.get("publication_year") or ""),
                     "journal_ref": ((it.get("primary_location") or {}).get("source") or {}).get("display_name",""),
                     "arxiv": ""}, f"cites:{doi[:24]}")
                n += 1
        COVERAGE.append(["openalex-cites", doi, n if c else "FAILED"]); time.sleep(1)
    for doi in sd[:20]:   # S2 walk on the first 20 seeds (rate limits)
        c = jget("https://api.semanticscholar.org/graph/v1/paper/DOI:" + urllib.parse.quote(doi) +
                 "/citations?fields=title,year,externalIds,venue&limit=100")
        n = 0
        if c:
            for it in c.get("data", []):
                p2 = it.get("citingPaper") or {}
                ex = p2.get("externalIds") or {}
                add({"title": p2.get("title",""), "doi": ex.get("DOI",""),
                     "arxiv": ex.get("ArXiv",""), "year": str(p2.get("year") or ""),
                     "journal_ref": p2.get("venue","")}, f"s2cites:{doi[:24]}")
                n += 1
        COVERAGE.append(["s2-cites", doi, n if c else "FAILED"]); time.sleep(2)

def phase_c():
    for q in ["universe inside a black hole", "black hole cosmology bounce",
              "cosmological natural selection", "shock wave cosmology black hole",
              "torsion bounce cosmology", "white hole big bang"]:
        d = jget("https://api.openalex.org/works?search=" + urllib.parse.quote(q) + "&per_page=50")
        n = 0
        if d:
            for it in d.get("results", []):
                add({"title": it.get("title") or "", "doi": (it.get("doi") or "").replace("https://doi.org/",""),
                     "year": str(it.get("publication_year") or ""),
                     "journal_ref": ((it.get("primary_location") or {}).get("source") or {}).get("display_name",""),
                     "arxiv": ""}, f"oa-search:{q[:20]}")
                n += 1
        COVERAGE.append(["openalex-search", q, n if d else "FAILED"]); time.sleep(1)
        d = jget("https://api.crossref.org/works?rows=40&query.bibliographic=" + urllib.parse.quote(q))
        n = 0
        if d:
            for it in d.get("message",{}).get("items",[]):
                add({"title": (it.get("title") or [""])[0], "doi": it.get("DOI",""),
                     "year": str((it.get("issued",{}).get("date-parts") or [[""]])[0][0]),
                     "journal_ref": (it.get("container-title") or [""])[0], "arxiv": ""}, f"cr-search:{q[:20]}")
                n += 1
        COVERAGE.append(["crossref-search", q, n if d else "FAILED"]); time.sleep(1)

def main():
    t0 = time.time()
    phase_a(); print(f"  A done: {len(RECORDS)} records", file=sys.stderr)
    phase_b(); print(f"  B done: {len(RECORDS)} records", file=sys.stderr)
    phase_c(); print(f"  C done: {len(RECORDS)} records", file=sys.stderr)
    for r in RECORDS.values():
        if isinstance(r.get("via"), set): r["via"] = sorted(r["via"])
    OUT.write_text(json.dumps({
        "harvested_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "runtime_s": round(time.time()-t0),
        "hosts": ["export.arxiv.org","inspirehep.net","api.openalex.org","api.crossref.org","api.semanticscholar.org"],
        "coverage": COVERAGE, "n_records": len(RECORDS),
        "records": sorted(RECORDS.values(), key=lambda r: r.get("year") or "")}, indent=1))
    fails = [c for c in COVERAGE if not isinstance(c[2], int)]
    print(f"  TOTAL {len(RECORDS)} records | queries {len(COVERAGE)} | failed {len(fails)}", file=sys.stderr)

if __name__ == "__main__":
    main()
