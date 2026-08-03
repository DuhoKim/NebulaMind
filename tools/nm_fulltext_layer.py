#!/usr/bin/env python3
"""On-demand full-text grounding for the research pipeline (Astro-Note style, scoped per study).

For a study, this selects relevant refereed papers (ADS topic search), fetches only THAT working
set from arXiv, extracts + chunks + embeds their full text (qwen3-embedding-4b), and grounds the
study's claims against real passages — so drafts cite real, verifiable prior work instead of the
model's memory. Only a few dozen papers are ever fetched, so a deep read is ~minutes, not the
~week it would take to vectorize all 120k full texts. Cached per paper, reused across studies.

TODO: swap select_papers() from ADS topic search to the local 120k semantic index once built.
"""
import html, json, os, re, time, urllib.parse, urllib.request
import numpy as np

_ROOT = "/Users/duhokim/NebulaMind/NebulaMind"
_CORP = f"{_ROOT}/.hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718"
CACHE = os.environ.get("NM_FULLTEXT_CACHE", f"{_CORP}/fulltext_cache")
ENV = f"{_ROOT}/backend/.env"
OLLAMA = os.environ.get("NM_EMBED_URL", "http://localhost:11434/api/embed")
MODEL = "qwen3-embedding:4b"
ADS = "https://api.adsabs.harvard.edu/v1/search/query"
UA = "NebulaMind-AI-Scientist/1.0 (research; duhokim81@gmail.com)"
ARX = re.compile(r"(?:arXiv:)?(\d{4}\.\d{4,5})", re.I)
GROUND_INSTR = "Instruct: Given a scientific claim or question, retrieve the passage that best supports, refutes, or answers it\nQuery: "
os.makedirs(CACHE, exist_ok=True)

def _token():
    for ln in open(ENV):
        if ln.startswith("NM_ADS_API_KEY="):
            return ln.split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError("NM_ADS_API_KEY not found")

def _ads_select_papers(topic: str, rows: int = 6):
    """[fallback] ADS topic search. Relevant, well-cited refereed papers: [{bibcode,arxiv,title,authors,year,cites}]."""
    q = f'abs:("{topic}") AND property:refereed AND (arxiv_class:"astro-ph.GA" OR arxiv_class:"astro-ph.CO")'
    params = urllib.parse.urlencode({"q": q, "fl": "bibcode,identifier,title,author,year,citation_count",
                                     "sort": "citation_count desc", "rows": rows})
    req = urllib.request.Request(f"{ADS}?{params}", headers={"Authorization": f"Bearer {_token()}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        docs = json.loads(r.read().decode())["response"]["docs"]
    out = []
    for d in docs:
        aid = next((ARX.search(str(s)).group(1) for s in (d.get("identifier") or []) if ARX.search(str(s))), None)
        out.append({"bibcode": d["bibcode"], "arxiv": aid, "title": html.unescape(" ".join(d.get("title") or []))[:200],
                    "authors": d.get("author") or [], "year": d.get("year"), "cites": d.get("citation_count", 0)})
    return out


# ---- local semantic retrieval over our 120k corpus (primary; ADS is fallback) ----
_EMB_PATH = f"{_CORP}/emb_qwen4b.f32"
_BIBS_PATH = f"{_CORP}/bibcodes.json"
_META_PATH = f"{_CORP}/embed_meta.json"
_CORPUS_JSONL = f"{_CORP}/corpus_ga_co_2009_2026.jsonl"
RETRIEVE_INSTR = "Instruct: Given a research topic, retrieve the abstracts of the most relevant papers\nQuery: "
_IDX = {"emb": None, "bibs": None, "meta": None}

def _load_index():
    if _IDX["emb"] is not None:
        return
    import html as _html
    m = json.loads(open(_META_PATH).read()); n, dim = m["n"], m["dim"]
    _IDX["emb"] = np.array(np.memmap(_EMB_PATH, dtype=np.float32, mode="r", shape=(n, dim)))  # ~1.2GB into RAM
    _IDX["bibs"] = json.loads(open(_BIBS_PATH).read())
    meta = {}
    for ln in open(_CORPUS_JSONL):
        d = json.loads(ln); b = d.get("bibcode")
        aid = next((ARX.search(str(s)).group(1) for s in (d.get("identifier") or []) if ARX.search(str(s))), None)
        ttl = d.get("title") or []
        ttl = _html.unescape(" ".join(ttl)) if isinstance(ttl, list) else str(ttl)
        meta[b] = {"arxiv": aid, "title": ttl[:200], "authors": d.get("author") or [],
                   "year": d.get("year"), "cites": d.get("citation_count") or 0}
    _IDX["meta"] = meta

def local_select_papers(topic: str, rows: int = 6):
    """Semantic retrieval over the curated 120k (qwen3-embedding-4b index)."""
    _load_index()
    qv = _norm(_embed([topic], instr=RETRIEVE_INSTR))[0]
    sims = _IDX["emb"] @ qv                      # cosine; corpus vectors are unit-normalized
    out = []
    for i in np.argsort(-sims)[:rows]:
        b = _IDX["bibs"][i]; mt = _IDX["meta"].get(b, {})
        out.append({"bibcode": b, "arxiv": mt.get("arxiv"), "title": mt.get("title", ""),
                    "authors": mt.get("authors", []), "year": mt.get("year"),
                    "cites": mt.get("cites", 0), "score": float(sims[i])})
    return out

def select_papers(topic: str, rows: int = 6):
    """Prefer the local 120k semantic index; fall back to ADS topic search."""
    try:
        r = local_select_papers(topic, rows)
        if r:
            return r
    except Exception as e:
        print(f"  [local retrieval unavailable, ADS fallback] {type(e).__name__}: {str(e)[:80]}")
    return _ads_select_papers(topic, rows)

def cite_key(paper: dict) -> str:
    au = paper.get("authors") or ["Anon"]
    last = re.sub(r"[^A-Za-z]", "", au[0].split(",")[0]) or "Anon"
    return f"{last}{paper.get('year','')}"

def format_ref(paper: dict) -> str:
    au = paper.get("authors") or []
    lead = au[0].split(",")[0] if au else "Anon"
    etal = " et al." if len(au) > 1 else ""
    return f"{lead}{etal} ({paper.get('year','?')}). {paper.get('title','')}. bibcode {paper.get('bibcode','')}"

def fetch_pdf(arxiv_id: str) -> bytes:
    path = os.path.join(CACHE, f"{arxiv_id}.pdf")
    if os.path.exists(path):
        return open(path, "rb").read()
    req = urllib.request.Request(f"https://arxiv.org/pdf/{arxiv_id}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        data = r.read()
    open(path, "wb").write(data); time.sleep(3)
    return data

def extract_text(pdf_bytes: bytes) -> str:
    import fitz
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = "\n".join(p.get_text("text") for p in doc); doc.close()
    cut = re.search(r"\n\s*(References|Bibliography|REFERENCES)\s*\n", text)
    if cut and cut.start() > 0.4 * len(text):
        text = text[:cut.start()]
    text = re.sub(r"-\n(\w)", r"\1", text)
    return re.sub(r"[ \t]+", " ", text)

def extract_html_structured(html: str):
    """Return (prose, tables). Tables are linearized row-by-row so a numeric value stays glued to its
    row label + column header (what prose-flattening destroys). ar5iv/arXiv-HTML use LaTeXML tables."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml")
    for t in soup(["script", "style", "nav", "header", "footer"]):
        t.decompose()
    for b in soup.select(".ltx_bibliography, .ltx_appendix, .ltx_page_footer, .ar5iv-footer"):
        b.decompose()
    tables = []
    for fig in soup.select("figure.ltx_table, table.ltx_tabular"):
        tbl = fig if fig.name == "table" else fig.select_one("table.ltx_tabular")
        if tbl is None:
            continue
        cap_el = fig.select_one(".ltx_caption")
        cap = cap_el.get_text(" ", strip=True) if cap_el else "Table"
        rows = []
        for tr in tbl.select("tr"):
            cells = [c.get_text(" ", strip=True) for c in tr.find_all(["td", "th"])]
            if any(cells):
                rows.append(" | ".join(cells))
        if rows:
            tables.append((cap + "\n" + "\n".join(rows[:45]))[:1900])
        fig.decompose()   # drop from prose so table values are not also flattened into it
    art = soup.find("article") or soup.find("div", class_="ltx_page_content") or soup.body
    prose = re.sub(r"\s+", " ", art.get_text(" ", strip=True)) if art else ""
    return prose, tables

def chunk_text(text: str, target=1400, overlap=1):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if len(p.strip()) > 60]
    chunks, cur, prev = [], "", []
    for p in paras:
        if len(cur) + len(p) > target and cur:
            chunks.append(cur.strip()); cur = (" ".join(prev[-overlap:]) + " ") if prev else ""
        cur += p + "\n\n"; prev.append(p)
    if len(cur.strip()) > 120:
        chunks.append(cur.strip())
    return [c[:2000] for c in chunks]

def _embed(texts, is_query=False, instr=None):
    pre = instr if instr is not None else (GROUND_INSTR if is_query else "")
    payload = [pre + t for t in texts]
    body = json.dumps({"model": MODEL, "input": payload}).encode()
    req = urllib.request.Request(OLLAMA, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return np.array(json.loads(r.read().decode())["embeddings"], dtype=np.float32)

def _norm(M):
    return M / (np.linalg.norm(M, axis=1, keepdims=True) + 1e-9)

def fetch_html(arxiv_id: str):
    """Try official arXiv HTML, then ar5iv (broad backfill). Returns (html, source) or (None, None)."""
    path = os.path.join(CACHE, f"{arxiv_id}.html")
    if os.path.exists(path):
        return open(path, encoding="utf-8", errors="replace").read(), "cache"
    for url, tag in ((f"https://arxiv.org/html/{arxiv_id}", "arxiv-html"),
                     (f"https://ar5iv.labs.arxiv.org/html/{arxiv_id}", "ar5iv")):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                html = r.read().decode(errors="replace")
            if ("ltx_para" in html) or ("ltx_document" in html):   # real LaTeXML content
                open(path, "w", encoding="utf-8").write(html); time.sleep(2)
                return html, tag
            time.sleep(1)
        except Exception:
            continue
    return None, None

def extract_html(html: str) -> str:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml")
    for t in soup(["script", "style", "nav", "header", "footer"]):
        t.decompose()
    for b in soup.select(".ltx_bibliography, .ltx_appendix, .ltx_page_footer, .ar5iv-footer, .ltx_role_affiliation"):
        b.decompose()
    art = soup.find("article") or soup.find("div", class_="ltx_page_content") or soup.body
    text = art.get_text(" ", strip=True) if art else ""
    return re.sub(r"\s+", " ", text)

def full_text(arxiv_id: str):
    """HTML-first structured (prose + linearized tables), PDF fallback. Returns (prose, tables, source)."""
    html, src = fetch_html(arxiv_id)
    if html:
        try:
            prose, tables = extract_html_structured(html)
            if len(prose) > 2000:
                return prose, tables, src
        except Exception:
            pass
    return extract_text(fetch_pdf(arxiv_id)), [], "pdf"

def deep_layer_for(arxiv_id: str):
    cj, cv = os.path.join(CACHE, f"{arxiv_id}.chunks.json"), os.path.join(CACHE, f"{arxiv_id}.vecs.npy")
    if os.path.exists(cj) and os.path.exists(cv):
        return json.load(open(cj)), np.load(cv)
    prose, tables, src = full_text(arxiv_id)
    chunks = chunk_text(prose) + ["[TABLE] " + t for t in tables]
    if not chunks:
        return [], np.zeros((0, 2560), dtype=np.float32)
    vecs = _norm(_embed(chunks))
    json.dump(chunks, open(cj, "w")); np.save(cv, vecs)
    open(os.path.join(CACHE, f"{arxiv_id}.src"), "w").write(src)
    return chunks, vecs

def build_deep_layer(arxiv_ids):
    layer = {}
    for aid in [a for a in dict.fromkeys(arxiv_ids) if a]:
        try:
            layer[aid] = deep_layer_for(aid)
        except Exception as e:
            print(f"  [warn] {aid}: {str(e)[:80]}")
    return layer

def ground(claim: str, layer, k=6):
    qv = _norm(_embed([claim], is_query=True))[0]
    hits = []
    for aid, (chunks, vecs) in layer.items():
        if len(chunks) == 0:
            continue
        sims = vecs @ qv
        for i in np.argsort(-sims)[:2]:
            hits.append({"arxiv_id": aid, "score": float(sims[i]), "passage": chunks[i]})
    hits.sort(key=lambda h: -h["score"])
    return hits[:k]

def literature_context(topic: str, claim: str, k_papers=6, k_passages=5):
    """Select papers, deep-read, ground `claim`. Returns dict or None."""
    papers = select_papers(topic, rows=k_papers)
    if not papers:
        return None
    by_arxiv = {p["arxiv"]: p for p in papers if p.get("arxiv")}
    layer = build_deep_layer(list(by_arxiv))
    hits = ground(claim, layer, k=k_passages)
    cited, lines = [], []
    for h in hits:
        p = by_arxiv.get(h["arxiv_id"], {}); key = cite_key(p)
        if key not in [c[0] for c in cited]:
            cited.append((key, p))
        lines.append(f'[{key}] "{h["passage"][:300].strip()}"')
    return {"papers": papers, "passages": hits, "refs": [p["bibcode"] for p in papers],
            "cite_block": "\n".join(lines), "ref_list": [f"[{k}] {format_ref(p)}" for k, p in cited]}

if __name__ == "__main__":
    import sys
    topic = sys.argv[1] if len(sys.argv) > 1 else "star-forming main sequence of galaxies"
    claim = sys.argv[2] if len(sys.argv) > 2 else "The slope of the star-forming main sequence flattens at high stellar mass."
    ctx = literature_context(topic, claim, k_papers=5, k_passages=4)
    if not ctx:
        print("no papers"); raise SystemExit
    print(f"selected {len(ctx['papers'])} papers; {len(ctx['passages'])} grounded passages\n")
    print("GROUNDED PASSAGES:\n" + ctx["cite_block"][:1200])
    print("\nREFERENCES:\n" + "\n".join(ctx["ref_list"]))
