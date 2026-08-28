#!/usr/bin/env python3
"""Quality gates for the research pipeline — grounded in retrieved evidence, not model memory.

  novelty_gate            : before greenlight — has this exact measurement been done? -> NOVEL / PIVOT / ABORT
  expected_value_gate     : after result     — does it agree/contradict/trivially-repeat the literature? -> CONSISTENT / TENSION / CONTRADICTS / CIRCULAR
  citation_entailment_gate: in review        — is every [Key] citation actually supported by its cited paper?

Each gate retrieves real papers from the 120k, deep-reads them (HTML-first), and asks an LLM judge to
decide FROM the quoted passages. Ungrounded judgment is unreliable (it flip-flops); grounding fixes that.
"""
import json, re, time, urllib.request
import numpy as np
import nm_fulltext_layer as ft

JUDGE_MODEL = "llama3.3:70b"
OLLAMA_GEN = "http://localhost:11434/api/generate"

def _judge(prompt, n=500, model=JUDGE_MODEL, temp=0.15):
    body = json.dumps({"model": model, "prompt": prompt, "stream": False,
                       "options": {"num_predict": n, "temperature": temp}}).encode()
    req = urllib.request.Request(OLLAMA_GEN, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        j = json.loads(r.read().decode())
    return (j.get("response") or j.get("thinking") or "").strip()

def _verdict(text, options, default):
    """Take the LAST VERDICT: X in the text (after chain-of-thought)."""
    found = default
    for m in re.finditer(r"VERDICT:\s*([A-Z\-]+)", text, re.I):
        v = m.group(1).upper()
        if v in options:
            found = v
    return found

def _evidence(query, claim, k_papers=6, k_deep=5, k_pass=6):
    papers = ft.local_select_papers(query, rows=k_papers)
    by_arxiv = {p["arxiv"]: p for p in papers if p.get("arxiv")}
    layer = ft.build_deep_layer(list(by_arxiv)[:k_deep])
    hits = ft.ground(claim, layer, k=k_pass)
    lines = []
    for h in hits:
        p = by_arxiv.get(h["arxiv_id"], {})
        lines.append(f'[{ft.cite_key(p)}] (sim {p.get("score",0):.2f}) "{h["passage"][:280].strip()}"')
    return papers, hits, "\n".join(lines)


# ---- numeric-targeted retrieval: surface passages that actually contain the value ----
_NUM = re.compile(r"[-+]?\d+(?:\.\d+)?(?:\s*[x*]\s*10\^?[-+]?\d+)?")
_UNIT = re.compile(r"\b(dex|M_?\u2609|M\u2609|Msun|Mpc\^?-?3|Mpc|kpc|mag|Gyr|Myr|Z_?\u2609|slope|normalization|normalisation|scatter|log\s*\(?O/H\)?|10\^)\b", re.I)

def _numeric_score(chunk):
    return len(_NUM.findall(chunk)) + 2 * len(_UNIT.findall(chunk))

def _numeric_ground(query, layer, k=7):
    qv = ft._norm(ft._embed([query], is_query=True))[0]
    cand = []
    for aid, (chunks, vecs) in layer.items():
        if len(chunks) == 0:
            continue
        sims = vecs @ qv
        for i in np.argsort(-sims)[:6]:               # top semantic chunks per paper
            ns = _numeric_score(chunks[i])
            cand.append((float(sims[i]) + 0.03 * min(ns, 12), aid, chunks[i], ns))
    cand.sort(key=lambda x: -x[0])
    withnum = [c for c in cand if c[3] >= 2]          # prefer chunks that actually contain numbers
    return (withnum or cand)[:k]

# ---------------- Gate 1: novelty ----------------
def novelty_gate(topic, method, planned):
    papers, hits, evid = _evidence(f"{topic} {method} {planned}", planned)
    top_sim = papers[0]["score"] if papers else 0.0
    prompt = (
        "You are a rigorous astronomy referee deciding if a PROPOSED study is genuinely NEW or already done.\n"
        f"PROPOSED: topic={topic}; method={method}; measurement={planned}.\n\n"
        "REAL PRIOR LITERATURE retrieved from the corpus (passages quoted from the papers):\n" + evid + "\n\n"
        "Reason step by step ONLY from these passages: does any paper already report THIS measurement "
        "(same quantity, comparable data / redshift / selection)? Be strict — reproducing a well-known "
        "relation with default data is NOT novel.\n"
        "Finish with a final line, EXACTLY one of:\n"
        "VERDICT: NOVEL   -- not done as proposed\n"
        "VERDICT: PIVOT   -- done, but a specific change (redshift / dataset / selection) would be new; name it\n"
        "VERDICT: ABORT   -- thoroughly done, no useful pivot\n"
    )
    out = _judge(prompt, n=600)
    v = _verdict(out, {"NOVEL", "PIVOT", "ABORT"}, "PIVOT")
    # hard prior: a near-duplicate top hit strongly implies not-novel
    if top_sim >= 0.85 and v == "NOVEL":
        v = "PIVOT"
    return {"gate": "novelty", "verdict": v, "top_similarity": round(float(top_sim), 3),
            "reason": out.strip()[-700:], "papers": papers}

# ---------------- Gate 2: expected value (can KILL) ----------------
def expected_value_gate(topic, result_summary):
    import nm_numeric_kb as kb
    papers = ft.local_select_papers(f"{topic} {result_summary}", rows=7)
    tuples = kb.kb_for_papers(papers)                     # structured (quantity,value,units,calib) from working set
    if not tuples:
        return {"gate": "expected_value", "verdict": "INSUFFICIENT", "kill": False, "n_values": 0,
                "reason": "no structured measurements could be extracted from the retrieved papers", "papers": papers}
    tbl = "\n".join(
        f"- {t.get('quantity')}: {t.get('value')} {t.get('units','')} [{t.get('context','')}] "
        f"calib={t.get('calibration')} [{t.get('_src','?')}]" for t in tuples[:45])
    prompt = (
        "You are a rigorous referee comparing a COMPUTED RESULT to STRUCTURED expected values extracted from the "
        "literature.\n"
        f"RESULT (measured): {result_summary}\n\n"
        "EXPECTED VALUES from the literature  (quantity: value units [context] calib [source]):\n" + tbl + "\n\n"
        "Step 1 - MATCH: which listed value(s) are for the SAME quantity as the measured result? If none match, "
        "say NO MATCH.\n"
        "Step 2 - COMPARE, minding units and CALIBRATION. Different metallicity scales legitimately differ by "
        "~0.2-0.7 dex; a scale offset is TENSION, not an error.\n"
        "Finish with a final line EXACTLY one of:\n"
        "VERDICT: CONSISTENT   -- agrees with the matched expected value\n"
        "VERDICT: TENSION      -- differs in an interesting/calibration way\n"
        "VERDICT: CONTRADICTS  -- differs far beyond any calibration offset (likely a pipeline error; KILL)\n"
        "VERDICT: CIRCULAR     -- trivially reproduces a known value, no new information\n"
        "VERDICT: INSUFFICIENT -- NO listed quantity matches the measured one\n"
    )
    out = _judge(prompt, n=600)
    v = _verdict(out, {"CONSISTENT", "TENSION", "CONTRADICTS", "CIRCULAR", "INSUFFICIENT"}, "INSUFFICIENT")
    return {"gate": "expected_value", "verdict": v, "kill": v == "CONTRADICTS",
            "n_values": len(tuples), "reason": out.strip()[-800:], "papers": papers}

# ---------------- Gate 3: citation entailment ----------------
_CITE = re.compile(r"\[([A-Za-z][A-Za-z\-]+\d{4})\]")
def _entail(sent, passage):
    jp = ("Does the PASSAGE support the CLAIM (the same specific fact, not merely the same topic)? "
          "Answer SUPPORTED or UNSUPPORTED, then one short reason.\n"
          f"CLAIM: {sent}\nPASSAGE: {passage[:600]}")
    return _judge(jp, n=100).upper()
def _refute(sent, passage):
    jp = ("You are a skeptical referee TRYING TO REFUTE a citation. Give the strongest reason the PASSAGE does "
          "NOT fully support the CLAIM (different quantity, missing specifics, over-generalization, only "
          "topically related). Answer SUPPORTED only if it genuinely and specifically backs the claim; otherwise "
          "UNSUPPORTED. Default to UNSUPPORTED when uncertain.\n"
          f"CLAIM: {sent}\nPASSAGE: {passage[:600]}")
    return _judge(jp, n=110).upper()

def citation_entailment_gate(body, papers, adversarial=True):
    """Verify each [Key] against its source. A citation is SUPPORTED only if it survives BOTH a direct
    entailment check AND an adversarial refute pass (guards against the judge rubber-stamping paraphrase)."""
    keymap = {ft.cite_key(p): p for p in papers if p.get("arxiv")}
    layers = {}; results = []
    for sent in re.split(r"(?<=[.!?])\s+", body):
        for key in set(_CITE.findall(sent)):
            p = keymap.get(key)
            if not p:
                results.append({"key": key, "sentence": sent.strip()[:180], "supported": False,
                                "passage": "", "reason": "cited key not in the retrieved set - possibly fabricated"})
                continue
            aid = p["arxiv"]
            if aid not in layers:
                try: layers[aid] = ft.deep_layer_for(aid)
                except Exception: layers[aid] = ([], np.zeros((0, 2560), np.float32))
            chunks, vecs = layers[aid]
            if len(chunks) == 0:
                results.append({"key": key, "sentence": sent.strip()[:180], "supported": None,
                                "passage": "", "reason": "no full text available to verify"})
                continue
            qv = ft._norm(ft._embed([sent], is_query=True))[0]
            passage = chunks[int(np.argmax(vecs @ qv))]
            direct = _entail(sent.strip(), passage)
            sup = ("UNSUPPORTED" not in direct) and ("SUPPORTED" in direct)
            adv = None
            if adversarial and sup:                          # only re-examine the ones it approved
                ref = _refute(sent.strip(), passage)
                adv = ("UNSUPPORTED" not in ref) and ("SUPPORTED" in ref)
                sup = sup and adv                            # must survive the refute pass
            results.append({"key": key, "sentence": sent.strip()[:180], "supported": sup,
                            "adversarial_ok": adv, "passage": passage[:300], "reason": direct[:150]})
    unsupported = [r for r in results if r.get("supported") is False]
    passed = [r for r in results if r.get("supported") is True]
    spot = passed[0] if passed else None                     # spot-audit: surface a PASSED cite for a human
    return {"gate": "citation_entailment", "checked": len(results), "adversarial": adversarial,
            "n_unsupported": len(unsupported), "unsupported": unsupported,
            "spot_audit": ({"key": spot["key"], "sentence": spot["sentence"], "passage": spot["passage"]} if spot else None),
            "all": results}

if __name__ == "__main__":
    import sys
    which = sys.argv[1] if len(sys.argv) > 1 else "novelty"
    if which == "novelty":
        r = novelty_gate("mass-metallicity relation", "mass-metallicity",
                          "the z=0 stellar mass-metallicity relation of star-forming galaxies in SDSS")
        print(json.dumps({k: v for k, v in r.items() if k != "papers"}, indent=2)[:1400])
    elif which == "expected":
        r = expected_value_gate("star-forming main sequence",
                                "SDSS z=0 main sequence: log SFR at logM=10 is +0.04 dex")
        print(json.dumps({k: v for k, v in r.items() if k != "papers"}, indent=2)[:1400])
