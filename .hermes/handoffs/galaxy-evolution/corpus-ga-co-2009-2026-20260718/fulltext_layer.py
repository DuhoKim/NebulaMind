#!/usr/bin/env python3
"""On-demand full-text grounding layer (Astro-Note style, scoped per study).

Given the papers a study leans on (bibcodes or arXiv ids), this:
  fetch arXiv PDF (cached) -> extract text -> chunk -> embed (qwen3-embedding-4b) -> cache,
then ground(claim) returns the top passages that support/refute a claim, with their source paper.

Only the working set of a study is ever fetched, so a 50-paper deep-read is ~minutes, not the
~week it would take to vectorize all 120k full texts. Cached per paper, so it is reused across studies.
"""
import json, os, re, time, urllib.request
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "corpus_ga_co_2009_2026.jsonl")
CACHE = os.path.join(HERE, "fulltext_cache")
OLLAMA = "http://localhost:11434/api/embed"
MODEL = "qwen3-embedding:4b"
UA = "NebulaMind-AI-Scientist/1.0 (research; contact duhokim81@gmail.com)"
ARX = re.compile(r"(?:arXiv:)?(\d{4}\.\d{4,5})", re.I)
GROUND_INSTR = "Instruct: Given a scientific claim or question, retrieve the passage that best supports, refutes, or answers it\nQuery: "
os.makedirs(CACHE, exist_ok=True)

# ---------- bibcode -> arXiv id ----------
_MAP = None
def bibcode_to_arxiv(bibcode: str):
    global _MAP
    if _MAP is None:
        _MAP = {}
        for ln in open(CORPUS):
            d = json.loads(ln)
            for s in (d.get("identifier") or []):
                m = ARX.search(str(s))
                if m:
                    _MAP[d["bibcode"]] = m.group(1); break
    return _MAP.get(bibcode)

def to_arxiv_ids(refs):
    """refs: list of arXiv ids and/or bibcodes -> list of arXiv ids (deduped, order-preserved)."""
    out = []
    for r in refs:
        m = ARX.search(str(r))
        aid = m.group(1) if m else bibcode_to_arxiv(r)
        if aid and aid not in out:
            out.append(aid)
    return out

# ---------- fetch + extract ----------
def fetch_pdf(arxiv_id: str) -> bytes:
    path = os.path.join(CACHE, f"{arxiv_id}.pdf")
    if os.path.exists(path):
        return open(path, "rb").read()
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        data = r.read()
    open(path, "wb").write(data)
    time.sleep(3)  # arXiv politeness
    return data

def extract_text(pdf_bytes: bytes) -> str:
    import fitz
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    parts = [p.get_text("text") for p in doc]
    doc.close()
    text = "\n".join(parts)
    # cut the bibliography (we ground on the science, not the reference list)
    cut = re.search(r"\n\s*(References|Bibliography|REFERENCES)\s*\n", text)
    if cut and cut.start() > 0.4 * len(text):
        text = text[:cut.start()]
    text = re.sub(r"-\n(\w)", r"\1", text)      # de-hyphenate line breaks
    text = re.sub(r"[ \t]+", " ", text)
    return text

def chunk_text(text: str, target=1400, overlap_paras=1):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if len(p.strip()) > 60]
    chunks, cur, prev = [], "", []
    for p in paras:
        if len(cur) + len(p) > target and cur:
            chunks.append(cur.strip())
            cur = " ".join(prev[-overlap_paras:]) + " " if prev else ""
        cur += p + "\n\n"; prev.append(p)
    if len(cur.strip()) > 120:
        chunks.append(cur.strip())
    return [c[:2000] for c in chunks]

# ---------- embed ----------
def _embed(texts, is_query=False):
    payload = [(GROUND_INSTR + t if is_query else t) for t in texts]
    body = json.dumps({"model": MODEL, "input": payload}).encode()
    req = urllib.request.Request(OLLAMA, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return np.array(json.loads(r.read().decode())["embeddings"], dtype=np.float32)

def _norm(M):
    return M / (np.linalg.norm(M, axis=1, keepdims=True) + 1e-9)

# ---------- deep layer (cached per paper) ----------
def deep_layer_for(arxiv_id: str):
    cj = os.path.join(CACHE, f"{arxiv_id}.chunks.json")
    cv = os.path.join(CACHE, f"{arxiv_id}.vecs.npy")
    if os.path.exists(cj) and os.path.exists(cv):
        return json.load(open(cj)), np.load(cv)
    text = extract_text(fetch_pdf(arxiv_id))
    chunks = chunk_text(text)
    if not chunks:
        return [], np.zeros((0, 2560), dtype=np.float32)
    vecs = _norm(_embed(chunks))
    json.dump(chunks, open(cj, "w"))
    np.save(cv, vecs)
    return chunks, vecs

def build_deep_layer(refs):
    """Fetch/chunk/embed the working set. Returns {arxiv_id: (chunks, vecs)}."""
    layer = {}
    for aid in to_arxiv_ids(refs):
        try:
            layer[aid] = deep_layer_for(aid)
        except Exception as e:
            print(f"  [warn] {aid}: {str(e)[:80]}")
    return layer

# ---------- grounding ----------
def ground(claim: str, layer, k=6):
    """Return top-k passages across the working set that best support/refute/answer the claim."""
    qv = _norm(_embed([claim], is_query=True))[0]
    hits = []
    for aid, (chunks, vecs) in layer.items():
        if len(chunks) == 0: continue
        sims = vecs @ qv
        for i in np.argsort(-sims)[:3]:
            hits.append({"arxiv_id": aid, "score": float(sims[i]), "passage": chunks[i]})
    hits.sort(key=lambda h: -h["score"])
    return hits[:k]

# ---------- study entry point (what the research pipeline calls) ----------
def ground_study(paper_refs, claims, k=6):
    """paper_refs: bibcodes/arXiv ids the study retrieved. claims: list of statements to ground.
    Returns {claim: [ {arxiv_id, score, passage}, ... ]}. Builds+caches the deep layer once."""
    layer = build_deep_layer(paper_refs)
    n_chunks = sum(len(c) for c, _ in layer.values())
    print(f"  deep layer: {len(layer)} papers, {n_chunks} chunks")
    return {c: ground(c, layer, k) for c in claims}

if __name__ == "__main__":
    import sys
    # demo: ground two claims against a couple of real galaxy-evolution papers
    refs = sys.argv[1:] or ["1809.05548", "1707.03395"]  # IllustrisTNG public data release, EAGLE-ish
    claims = ["The stellar mass function of galaxies declines steeply at the high-mass end.",
              "IllustrisTNG reproduces the observed galaxy color bimodality."]
    res = ground_study(refs, claims, k=4)
    for claim, hits in res.items():
        print("\n### CLAIM:", claim)
        for h in hits:
            print(f"  [{h['score']:.3f}] {h['arxiv_id']}: {h['passage'][:180].strip()}...")
