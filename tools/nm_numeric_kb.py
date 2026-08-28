#!/usr/bin/env python3
"""Structured numeric-value KB — the matching layer for the expected-value gate.

For a paper, extract concrete measured/fitted NUMERIC RESULTS as structured tuples
  {quantity, value, uncertainty, units, context, calibration, arxiv, bibcode}
from its table + numeric chunks (LLM extraction). Cached per paper (kb_cache/<arxiv>.json), built
on-demand from a study's retrieved working set. lookup_expected() then matches a measured quantity to
stored tuples, so the gate compares against a STRUCTURED value (calibration-aware) instead of raw text.
"""
import json, os, re, urllib.request
import nm_fulltext_layer as ft

OLLAMA_GEN = "http://localhost:11434/api/generate"
def _judge(prompt, n=800, model="llama3.3:70b", temp=0.1):
    body = json.dumps({"model": model, "prompt": prompt, "stream": False,
                       "options": {"num_predict": n, "temperature": temp}}).encode()
    req = urllib.request.Request(OLLAMA_GEN, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return (json.loads(r.read().decode()).get("response") or "").strip()
_NUMK = re.compile(r"[-+]?\d+(?:\.\d+)?")
def _numeric_score(c):
    return len(_NUMK.findall(c)) + (5 if c.startswith("[TABLE]") else 0)

KB_CACHE = os.path.join(os.path.dirname(ft.CACHE), "kb_cache")
EXTRACT_MODEL = "llama3.3:70b"
os.makedirs(KB_CACHE, exist_ok=True)

def _parse_json_array(text):
    i, j = text.find("["), text.rfind("]")
    if i < 0 or j < 0 or j <= i:
        return []
    blob = text[i:j + 1]
    try:
        d = json.loads(blob)
        return d if isinstance(d, list) else []
    except Exception:
        # salvage line-by-line objects
        out = []
        for m in re.finditer(r"\{[^{}]*\}", blob):
            try: out.append(json.loads(m.group(0)))
            except Exception: pass
        return out

def extract_measurements(arxiv_id, bibcode=None, max_chunks=8):
    """Structured measured results for one paper (cached)."""
    cf = os.path.join(KB_CACHE, f"{arxiv_id}.json")
    if os.path.exists(cf):
        return json.load(open(cf))
    chunks, _ = ft.deep_layer_for(arxiv_id)
    if not chunks:
        json.dump([], open(cf, "w")); return []
    scored = sorted(chunks, key=lambda c: -_numeric_score(c))
    text = "\n\n".join(scored[:max_chunks])[:6500]
    prompt = (
        "You extract concrete NUMERIC RESULTS from an astronomy paper's passages and tables. Return a JSON "
        "array. Each element:\n"
        '{"quantity":"short name e.g. MZR turnover metallicity / main-sequence slope / SMF characteristic mass",'
        '"value": number or "a-b" range, "uncertainty":"+/- x or null", "units":"e.g. 12+log(O/H), dex, '
        'Mpc^-3, log Msun", "context":"redshift / mass range / sample", '
        '"calibration":"metallicity scale or fit method if relevant, else null"}\n'
        "Extract only real MEASURED or FITTED results (relation slopes, normalizations, turnover/characteristic "
        "values, number densities). Do NOT extract sample sizes, bin counts, or method knobs. If none, return [].\n\n"
        "PASSAGES/TABLES:\n" + text + "\n\nJSON array only:")
    out = _judge(prompt, n=900, model=EXTRACT_MODEL)
    tuples = _parse_json_array(out)
    for t in tuples:
        if isinstance(t, dict):
            t["arxiv"] = arxiv_id
            if bibcode: t["bibcode"] = bibcode
    tuples = [t for t in tuples if isinstance(t, dict) and t.get("quantity")]
    json.dump(tuples, open(cf, "w"), indent=1)
    return tuples

def kb_for_papers(papers):
    """Collect structured measurements from a study's retrieved working set (cached per paper)."""
    out = []
    for p in papers:
        aid = p.get("arxiv")
        if not aid:
            continue
        try:
            for t in extract_measurements(aid, p.get("bibcode")):
                t["_src"] = ft.cite_key(p)
                out.append(t)
        except Exception:
            pass
    return out

if __name__ == "__main__":
    import sys
    aid = sys.argv[1] if len(sys.argv) > 1 else "1404.7526"   # has the MZ Relation Fit table (Zo=9.102)
    ms = extract_measurements(aid)
    print(f"{aid}: extracted {len(ms)} measurements")
    for m in ms[:12]:
        print(f"  - {m.get('quantity')}: {m.get('value')} {m.get('units','')} "
              f"[{m.get('context','')}] calib={m.get('calibration')}")
