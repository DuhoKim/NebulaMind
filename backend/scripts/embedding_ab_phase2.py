#!/usr/bin/env python3
"""Shadow-only embedding A/B Phase 2 harness.

This script intentionally does not write production tables, change routing, or
start background jobs. Outputs are JSON/Markdown artifacts under logs/workspace.
"""

from __future__ import annotations

import argparse
import asyncio
import datetime as dt
import hashlib
import json
import math
import os
import random
import re
import statistics
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import httpx
import numpy as np
from sqlalchemy import text

from app.database import engine


OLLAMA_BASE = os.getenv("EMBED_AB_OLLAMA_BASE", "http://127.0.0.1:11434")
OLLAMA_V1_BASE = os.getenv("EMBED_AB_OLLAMA_V1_BASE", "http://127.0.0.1:11434/v1")
LOG_DIR = Path("/Users/duhokim/NebulaMind/logs")
WORKSPACE_DIR = Path("/Users/duhokim/.openclaw/workspace")
RANDOM_SEED = 20260523

QWEN_PREFIX_V1 = (
    "Instruct: Given an astronomy wiki claim, retrieve peer-reviewed paper evidence "
    "that supports or challenges the claim.\nQuery: "
)
QWEN_PREFIX_V2 = (
    "Instruct: Retrieve the specific astronomy paper abstract that directly supports "
    "or challenges this wiki claim. Prefer same-subfield evidence over broad topical overlap.\nQuery: "
)

MODELS: dict[str, dict[str, Any]] = {
    "nomic": {"ollama": "nomic-embed-text:v1.5", "dim": 768, "prefix": ""},
    "qwen06": {"ollama": "qwen3-embedding:0.6b", "dim": 1024, "prefix": QWEN_PREFIX_V1},
    "qwen4b": {"ollama": "qwen3-embedding:4b", "dim": 2560, "prefix": QWEN_PREFIX_V1},
    "qwen06_retrieval_prefix_v2": {
        "ollama": "qwen3-embedding:0.6b",
        "dim": 1024,
        "prefix": QWEN_PREFIX_V2,
    },
}

STOP = {
    "the", "and", "for", "with", "that", "this", "from", "into", "onto", "are", "was", "were",
    "been", "being", "have", "has", "had", "not", "but", "its", "their", "they", "them", "these",
    "those", "between", "within", "across", "through", "using", "used", "use", "than", "then",
    "galaxy", "galaxies", "astronomy", "wiki", "claim", "evidence", "paper", "abstract",
}


def stamp() -> str:
    return dt.datetime.now().strftime("%Y%m%d_%H%M")


def iso_now() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def sha(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def toks(value: str) -> list[str]:
    return [
        t
        for t in re.findall(r"[a-z0-9]+", (value or "").lower())
        if len(t) > 2 and t not in STOP
    ]


def doc_text(row: dict[str, Any]) -> str:
    parts = [row.get("title") or ""]
    if row.get("year") or row.get("submitted"):
        parts.append(f"Date: {row.get('year') or row.get('submitted')}")
    if row.get("abstract"):
        parts.append(row["abstract"])
    if row.get("summary") or row.get("abstract_summary"):
        parts.append("Summary: " + (row.get("summary") or row.get("abstract_summary") or ""))
    return "\n\n".join(p for p in parts if p)


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    denom = float(np.linalg.norm(a) * np.linalg.norm(b))
    return 0.0 if denom == 0.0 else float(np.dot(a, b) / denom)


def percentile(values: list[float], p: float) -> float | None:
    if not values:
        return None
    if len(values) == 1:
        return values[0]
    values = sorted(values)
    idx = (len(values) - 1) * p
    lo = math.floor(idx)
    hi = math.ceil(idx)
    if lo == hi:
        return values[lo]
    return values[lo] * (hi - idx) + values[hi] * (idx - lo)


def memory_snapshot() -> dict[str, Any]:
    try:
        r = httpx.get(f"{OLLAMA_BASE}/api/ps", timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


def embed(client: httpx.Client, model: str, prompt: str, keep_alive: str = "30m") -> list[float]:
    last: Exception | None = None
    body = {"model": model, "prompt": prompt[:3000], "keep_alive": keep_alive}
    for attempt in range(4):
        try:
            r = client.post(f"{OLLAMA_BASE}/api/embeddings", json=body, timeout=240)
            r.raise_for_status()
            vec = r.json().get("embedding")
            if not isinstance(vec, list) or not vec:
                raise RuntimeError("empty embedding")
            return [float(x) for x in vec]
        except Exception as exc:
            last = exc
            time.sleep(2 + attempt * 3)
    raise RuntimeError(f"embedding failed model={model} len={len(prompt)} sha={sha(prompt)[:12]} err={last}")


def fetch_slice_a(limit: int = 1000, cap_per_page: int = 40) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    pub = "(e.peer_reviewed=true or e.doi is not null or e.ads_bibcode is not null or e.journal_ref is not null)"
    tiers = [
        (
            "A0",
            f"e.stance='supports' and c.trust_level in ('accepted','consensus') "
            f"and e.abstract is not null and length(e.abstract)>=300 and {pub} "
            "and coalesce(v.pos_w,0)>=3 and coalesce(v.neg_n,0)=0",
        ),
        (
            "A1",
            f"e.stance='supports' and c.trust_level in ('accepted','consensus','debated') "
            f"and e.abstract is not null and length(e.abstract)>=300 and {pub} "
            "and coalesce(v.pos_w,0)>=3 and coalesce(v.neg_n,0)=0",
        ),
        (
            "A2",
            f"e.stance='supports' and c.trust_level in ('accepted','consensus','debated') "
            f"and e.abstract is not null and length(e.abstract)>=300 and {pub} "
            "and coalesce(v.pos_w,0)>=2 and coalesce(v.neg_n,0)=0",
        ),
        (
            "A3",
            f"e.stance='supports' and c.trust_level in ('accepted','consensus','debated') "
            f"and e.abstract is not null and length(e.abstract)>=300 and {pub} "
            "and coalesce(v.neg_n,0)=0 and "
            "(coalesce(v.pos_w,0)>=2 or (coalesce(v.pos_w,0)=0 and e.quality>=0.70 and e.source_channel is not null))",
        ),
    ]
    base = """
        FROM claims c
        JOIN evidence e ON e.claim_id = c.id
        JOIN wiki_pages wp ON wp.id = c.page_id
        LEFT JOIN (
            SELECT evidence_id,
                   SUM(CASE WHEN value > 0 THEN COALESCE(weight, 1.0) ELSE 0 END) AS pos_w,
                   SUM(CASE WHEN value < 0 THEN 1 ELSE 0 END) AS neg_n,
                   COUNT(*) AS vote_count
            FROM evidence_votes GROUP BY evidence_id
        ) v ON v.evidence_id = e.id
    """
    selected: list[dict[str, Any]] = []
    seen_pairs: set[tuple[int, int]] = set()
    seen_evidence: set[int] = set()
    per_page: Counter[str] = Counter()
    tier_counts: dict[str, int] = {}
    rng = random.Random(RANDOM_SEED)

    with engine.connect() as conn:
        for tier, where in tiers:
            rows = [
                dict(r._mapping)
                for r in conn.execute(
                    text(
                        f"""
                        SELECT c.id AS claim_id, c.text AS claim_text, c.trust_level, c.page_id,
                               wp.slug AS page_slug, wp.title AS page_title,
                               e.id AS evidence_id, e.title, e.abstract, e.summary, e.year,
                               e.quality, e.source_channel, e.doi, e.ads_bibcode, e.journal_ref,
                               e.peer_reviewed, COALESCE(v.pos_w,0) AS pos_weight,
                               COALESCE(v.neg_n,0) AS neg_votes, COALESCE(v.vote_count,0) AS vote_count
                        {base}
                        WHERE {where}
                        """
                    )
                ).fetchall()
            ]
            tier_counts[tier] = len(rows)
            rows.sort(key=lambda r: (r["page_slug"], r["claim_id"], r["evidence_id"]))
            rng.shuffle(rows)
            for row in rows:
                pair_key = (int(row["claim_id"]), int(row["evidence_id"]))
                if pair_key in seen_pairs:
                    continue
                if tier != "A0" and int(row["evidence_id"]) in seen_evidence:
                    continue
                if tier != "A0" and per_page[row["page_slug"]] >= cap_per_page:
                    continue
                row["slice"] = "A"
                row["tier"] = tier
                row["query_id"] = f"a:c:{row['claim_id']}"
                row["doc_id"] = f"e:{row['evidence_id']}"
                row["pair_id"] = f"{row['query_id']}|{row['doc_id']}"
                row["doc_text"] = doc_text(row)
                selected.append(row)
                seen_pairs.add(pair_key)
                seen_evidence.add(int(row["evidence_id"]))
                per_page[row["page_slug"]] += 1
                if len(selected) >= limit:
                    break
            if len(selected) >= limit:
                break
    meta = {
        "target": limit,
        "selected_count": len(selected),
        "tier_candidate_counts": tier_counts,
        "selected_by_tier": dict(Counter(r["tier"] for r in selected)),
        "selected_by_page": dict(sorted(per_page.items())),
        "cap_per_page": cap_per_page,
        "a0_subset_count": sum(1 for r in selected if r["tier"] == "A0"),
    }
    return selected, meta


class BM25:
    def __init__(self, docs: list[tuple[str, str]]):
        self.docs = docs
        self.tokens = [toks(text_value) for _, text_value in docs]
        self.counters = [Counter(ts) for ts in self.tokens]
        self.lengths = [len(ts) for ts in self.tokens]
        self.avgdl = sum(self.lengths) / max(1, len(self.lengths))
        df: Counter[str] = Counter()
        for ts in self.tokens:
            df.update(set(ts))
        n = max(1, len(docs))
        self.idf = {t: math.log((n - c + 0.5) / (c + 0.5) + 1.0) for t, c in df.items()}

    def score(self, query: str, idx: int) -> float:
        q = toks(query)
        c = self.counters[idx]
        length = self.lengths[idx] or 1
        k1 = 1.2
        b = 0.75
        total = 0.0
        for t in q:
            f = c.get(t, 0)
            if f:
                total += self.idf.get(t, 0.0) * f * (k1 + 1.0) / (f + k1 * (1 - b + b * length / self.avgdl))
        return total

    def top(self, query: str, k: int, exclude: set[str] | None = None) -> list[tuple[str, float]]:
        exclude = exclude or set()
        scored = []
        for i, (doc_id, _) in enumerate(self.docs):
            if doc_id in exclude:
                continue
            scored.append((doc_id, self.score(query, i)))
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:k]


def atom_score(client: httpx.Client, claim: str, abstract: str) -> float:
    prompt = (
        f"Claim: {claim[:300]}\n\nEvidence abstract: {abstract[:700]}\n\n"
        "Does this evidence directly support the claim with specific findings? "
        "Reply with a decimal number 0.00-1.00 only (e.g. 0.82)."
    )
    try:
        r = client.post(
            f"{OLLAMA_V1_BASE}/chat/completions",
            json={
                "model": "vanta-research/atom-astronomy-7b",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.0,
                "options": {"num_ctx": 8192},
                "keep_alive": "30m",
            },
            timeout=30,
        )
        r.raise_for_status()
        content = r.json()["choices"][0]["message"]["content"].strip()
        m = re.search(r"([01]\.\d+|\d+)", content)
        return min(1.0, float(m.group(1))) if m else 0.0
    except Exception:
        return 0.0


def atom_label(client: httpx.Client, claim: str, title: str, abstract: str) -> tuple[str, str]:
    prompt = (
        "Classify whether the paper directly supports the claim. Be conservative: "
        "shared topic words are not enough. A direct support label requires the abstract "
        "to state findings, measurements, simulations, or constraints that answer the claim.\n\n"
        f"Claim: {claim[:450]}\n\n"
        f"Paper title: {title[:220]}\n\n"
        f"Abstract: {abstract[:900]}\n\n"
        "Return one line only in this format:\n"
        "label=<strict_support|adjacent_support|neutral_or_unclear>; reason=<12 words max>"
    )
    try:
        r = client.post(
            f"{OLLAMA_V1_BASE}/chat/completions",
            json={
                "model": "vanta-research/atom-astronomy-7b",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.0,
                "options": {"num_ctx": 8192},
                "keep_alive": "30m",
            },
            timeout=45,
        )
        r.raise_for_status()
        content = r.json()["choices"][0]["message"]["content"].strip()
        label_match = re.search(r"(strict_support|adjacent_support|neutral_or_unclear)", content)
        label = label_match.group(1) if label_match else "neutral_or_unclear"
        return label, content[:180]
    except Exception as exc:
        return "neutral_or_unclear", f"label_error: {exc}"


def build_galaxy_fixture(out_path: Path, target_max: int = 250) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    with engine.connect() as conn:
        claims = [
            dict(r._mapping)
            for r in conn.execute(
                text(
                    """
                    SELECT id AS claim_id, text AS claim_text
                    FROM claims
                    WHERE page_id = 57 AND text IS NOT NULL AND length(text) >= 80
                    ORDER BY id
                    """
                )
            ).fetchall()
        ]
        papers = [
            dict(r._mapping)
            for r in conn.execute(
                text(
                    """
                    SELECT arxiv_id, title, abstract, abstract_summary, submitted, category, url
                    FROM arxiv_papers
                    WHERE related_pages::text ILIKE '%galaxy-evolution%'
                      AND abstract IS NOT NULL AND length(abstract) >= 300
                    ORDER BY submitted DESC, arxiv_id
                    """
                )
            ).fetchall()
        ]

    bm25 = BM25([(f"g:{p['arxiv_id']}", doc_text(p)) for p in papers])
    paper_by_doc = {f"g:{p['arxiv_id']}": p for p in papers}
    proposed: list[tuple[float, dict[str, Any], dict[str, Any]]] = []
    for claim in claims:
        for doc_id, score_value in bm25.top(claim["claim_text"], 3):
            proposed.append((score_value, claim, paper_by_doc[doc_id]))
    proposed.sort(key=lambda item: item[0], reverse=True)

    fixture: list[dict[str, Any]] = []
    seen: set[tuple[int, str]] = set()
    with httpx.Client() as client:
        for bm25_score, claim, paper in proposed:
            key = (int(claim["claim_id"]), str(paper["arxiv_id"]))
            if key in seen:
                continue
            seen.add(key)
            score_value = atom_score(client, claim["claim_text"], paper["abstract"])
            claim_terms = set(toks(claim["claim_text"]))
            doc_terms = set(toks((paper["title"] or "") + " " + (paper["abstract"] or "")))
            key_overlap = len(claim_terms & doc_terms) / max(1, len(claim_terms))
            if score_value >= 0.90 and key_overlap >= 0.20:
                label = "strict_support"
            elif score_value >= 0.50:
                label = "adjacent_support"
            else:
                label = "neutral_or_unclear"
            fixture.append(
                {
                    "slice": "B",
                    "query_id": f"g:c:{claim['claim_id']}",
                    "doc_id": f"g:{paper['arxiv_id']}",
                    "pair_id": f"g:c:{claim['claim_id']}|g:{paper['arxiv_id']}",
                    "claim_id": int(claim["claim_id"]),
                    "claim_text": claim["claim_text"],
                    "arxiv_id": paper["arxiv_id"],
                    "title": paper["title"],
                    "abstract": paper["abstract"],
                    "abstract_summary": paper.get("abstract_summary"),
                    "submitted": paper.get("submitted"),
                    "category": paper.get("category"),
                    "page_slug": "galaxy-evolution",
                    "bm25_score": bm25_score,
                    "atom_score": score_value,
                    "claim_key_overlap": key_overlap,
                    "label": label,
                    "doc_text": doc_text(paper),
                }
            )
            strict_count = sum(1 for x in fixture if x["label"] == "strict_support")
            if len(fixture) >= target_max and strict_count >= 100:
                break

    meta = {
        "page_id": 57,
        "claims_available": len(claims),
        "candidate_papers_available": len(papers),
        "fixture_count": len(fixture),
        "label_counts": dict(Counter(x["label"] for x in fixture)),
        "label_method": (
            "BM25 top-3 proposal plus conservative local Atom-7B score and lexical key-overlap gate. "
            "strict_support requires Atom score >=0.90 and claim-key overlap >=0.20; adjacent_support "
            "requires Atom score >=0.50. This demotes all prior low-confidence Atom-only strict labels "
            "below 0.90 and rows without enough claim-specific term overlap."
        ),
    }
    out_path.write_text(json.dumps({"generated_at": iso_now(), "meta": meta, "items": fixture}, indent=2), encoding="utf-8")
    return fixture, meta


def fetch_evidence_pool() -> list[dict[str, Any]]:
    with engine.connect() as conn:
        return [
            dict(r._mapping)
            for r in conn.execute(
                text(
                    """
                    SELECT e.id AS evidence_id, e.claim_id, c.page_id, wp.slug AS page_slug, wp.title AS page_title,
                           e.title, e.abstract, e.summary, e.year, e.stance
                    FROM evidence e
                    JOIN claims c ON c.id = e.claim_id
                    JOIN wiki_pages wp ON wp.id = c.page_id
                    WHERE e.abstract IS NOT NULL AND length(e.abstract) >= 300
                    """
                )
            ).fetchall()
        ]


def build_pre_nomic_hard_candidates(slice_a: list[dict[str, Any]]) -> tuple[dict[str, list[str]], dict[str, dict[str, Any]], dict[str, Any]]:
    pool = fetch_evidence_pool()
    docs: dict[str, dict[str, Any]] = {}
    by_page: defaultdict[int, list[dict[str, Any]]] = defaultdict(list)
    for row in pool:
        row["doc_id"] = f"e:{row['evidence_id']}"
        row["doc_text"] = doc_text(row)
        docs[row["doc_id"]] = row
        by_page[int(row["page_id"])].append(row)
    bm25 = BM25([(doc_id, row["doc_text"]) for doc_id, row in docs.items()])

    page_by_query = {r["query_id"]: int(r["page_id"]) for r in slice_a}
    claim_by_query = {r["query_id"]: int(r["claim_id"]) for r in slice_a}
    gold_docs_by_query: defaultdict[str, set[str]] = defaultdict(set)
    for row in slice_a:
        gold_docs_by_query[row["query_id"]].add(row["doc_id"])
    query_text = {r["query_id"]: r["claim_text"] for r in slice_a}
    candidates: dict[str, list[str]] = {}
    rng = random.Random(RANDOM_SEED)

    for pair in slice_a:
        qid = pair["query_id"]
        pair_id = pair["pair_id"]
        excluded_gold = gold_docs_by_query[qid]
        page_id = page_by_query[qid]
        claim_id = claim_by_query[qid]
        selected: list[str] = []
        same = [r["doc_id"] for r in by_page[page_id] if int(r["claim_id"]) != claim_id and r["doc_id"] not in excluded_gold]
        rng.shuffle(same)
        selected.extend(same[:30])
        # Neighbor pages: lexical title overlap or same first broad page token, deterministic fallback to adjacent page ids.
        page_title_tokens = set(toks(next(r["page_title"] for r in slice_a if r["query_id"] == qid)))
        neighbor_rows = [
            r for r in pool
            if int(r["page_id"]) != page_id
            and (page_title_tokens & set(toks(r["page_title"])))
            and r["doc_id"] not in excluded_gold
        ]
        if len(neighbor_rows) < 30:
            neighbor_rows.extend([r for r in pool if abs(int(r["page_id"]) - page_id) <= 2 and int(r["page_id"]) != page_id])
        rng.shuffle(neighbor_rows)
        selected.extend([r["doc_id"] for r in neighbor_rows[:30] if r["doc_id"] not in excluded_gold])
        selected.extend([doc_id for doc_id, _ in bm25.top(query_text[qid], 30, exclude=excluded_gold)])
        dedup: list[str] = []
        seen: set[str] = set()
        for doc_id in selected:
            if doc_id not in excluded_gold and doc_id not in seen:
                seen.add(doc_id)
                dedup.append(doc_id)
        candidates[pair_id] = dedup
    sizes = [len(v) for v in candidates.values()]
    unique_queries = {r["query_id"] for r in slice_a}
    multi_gold_queries = sum(1 for docs_for_query in gold_docs_by_query.values() if len(docs_for_query) > 1)
    meta = {
        "gold_pairs": len(candidates),
        "unique_queries": len(unique_queries),
        "multi_gold_queries": multi_gold_queries,
        "max_gold_docs_per_query": max((len(v) for v in gold_docs_by_query.values()), default=0),
        "pre_nomic_negative_size": {
            "min": min(sizes) if sizes else 0,
            "median": statistics.median(sizes) if sizes else 0,
            "max": max(sizes) if sizes else 0,
        },
        "evidence_pool_size": len(pool),
    }
    return candidates, docs, meta


def embed_all(
    pairs: list[dict[str, Any]],
    docs: dict[str, dict[str, Any]],
    models: list[str],
) -> tuple[dict[str, dict[str, np.ndarray]], dict[str, dict[str, np.ndarray]], dict[str, Any]]:
    queries = {p["query_id"]: p["claim_text"] for p in pairs}
    timings: dict[str, Any] = {}
    qvecs: dict[str, dict[str, np.ndarray]] = {m: {} for m in models}
    dvecs: dict[str, dict[str, np.ndarray]] = {m: {} for m in models}
    with httpx.Client() as client:
        for model_key in models:
            spec = MODELS[model_key]
            before = memory_snapshot()
            print(json.dumps({"event": "embedding_model_start", "model": model_key, "ollama": spec["ollama"]}), flush=True)
            q_start = time.perf_counter()
            for qid, qtext in queries.items():
                vec = embed(client, spec["ollama"], spec["prefix"] + qtext)
                if len(vec) != spec["dim"]:
                    raise RuntimeError(f"{model_key} query dim {len(vec)} != {spec['dim']}")
                qvecs[model_key][qid] = np.array(vec, dtype=np.float32)
            q_seconds = time.perf_counter() - q_start
            d_start = time.perf_counter()
            # Prefix variant reuses qwen06 document vectors because only query instruction changes.
            if model_key == "qwen06_retrieval_prefix_v2" and "qwen06" in dvecs and dvecs["qwen06"]:
                dvecs[model_key] = dvecs["qwen06"]
                d_seconds = 0.0
            else:
                for doc_id, row in docs.items():
                    vec = embed(client, spec["ollama"], row["doc_text"])
                    if len(vec) != spec["dim"]:
                        raise RuntimeError(f"{model_key} doc dim {len(vec)} != {spec['dim']}")
                    dvecs[model_key][doc_id] = np.array(vec, dtype=np.float32)
                d_seconds = time.perf_counter() - d_start
            after = memory_snapshot()
            timings[model_key] = {
                "model": spec["ollama"],
                "query_count": len(queries),
                "doc_count": len(docs) if d_seconds else 0,
                "query_seconds": q_seconds,
                "doc_seconds": d_seconds,
                "query_seconds_per_1000": q_seconds / max(1, len(queries)) * 1000,
                "doc_seconds_per_1000": d_seconds / max(1, len(docs)) * 1000 if d_seconds else 0.0,
                "memory_before": before,
                "memory_after": after,
            }
    return qvecs, dvecs, timings


def add_nomic_neighbors(
    slice_a: list[dict[str, Any]],
    candidates: dict[str, list[str]],
    docs: dict[str, dict[str, Any]],
    qvecs: dict[str, dict[str, np.ndarray]],
    dvecs: dict[str, dict[str, np.ndarray]],
) -> tuple[dict[str, list[str]], dict[str, Any]]:
    doc_ids = list(docs.keys())
    gold_docs_by_query: defaultdict[str, set[str]] = defaultdict(set)
    for pair in slice_a:
        gold_docs_by_query[pair["query_id"]].add(pair["doc_id"])
    for pair in slice_a:
        qid = pair["query_id"]
        pair_id = pair["pair_id"]
        gold = pair["doc_id"]
        excluded_gold = gold_docs_by_query[qid]
        ranked = [
            (doc_id, cosine(qvecs["nomic"][qid], dvecs["nomic"][doc_id]))
            for doc_id in doc_ids
            if doc_id not in excluded_gold
        ]
        ranked.sort(key=lambda x: x[1], reverse=True)
        merged = list(candidates.get(pair_id, [])) + [doc_id for doc_id, _ in ranked[:30]]
        dedup: list[str] = []
        seen: set[str] = set()
        for doc_id in merged:
            if doc_id not in excluded_gold and doc_id not in seen:
                seen.add(doc_id)
                dedup.append(doc_id)
        candidates[pair_id] = dedup
    sizes = [len(v) for v in candidates.values()]
    included_pairs = [pair for pair in slice_a if len(candidates.get(pair["pair_id"], [])) >= 20]
    return candidates, {
        "gold_pairs": len(candidates),
        "unique_queries": len({p["query_id"] for p in slice_a}),
        "candidate_size": {
            "min": min(sizes) if sizes else 0,
            "median": statistics.median(sizes) if sizes else 0,
            "max": max(sizes) if sizes else 0,
        },
        "included_gold_pairs": len(included_pairs),
        "included_unique_queries": len({p["query_id"] for p in included_pairs}),
        "excluded_lt20_negatives": sum(1 for v in candidates.values() if len(v) < 20),
    }


def rank(query_vec: np.ndarray, doc_vecs: dict[str, np.ndarray], candidate_ids: list[str]) -> list[str]:
    scored = [(doc_id, cosine(query_vec, doc_vecs[doc_id])) for doc_id in candidate_ids if doc_id in doc_vecs]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [doc_id for doc_id, _ in scored]


def metric_from_ranks(ranks: list[int | None], missing_rank: int) -> dict[str, Any]:
    n = len(ranks)
    if n == 0:
        return {"n": 0, "recall_at_1": 0, "recall_at_5": 0, "recall_at_10": 0, "mrr_at_10": 0, "median_rank": None}
    valid = [r for r in ranks if r is not None]
    return {
        "n": n,
        "recall_at_1": sum(1 for r in valid if r <= 1) / n,
        "recall_at_5": sum(1 for r in valid if r <= 5) / n,
        "recall_at_10": sum(1 for r in valid if r <= 10) / n,
        "mrr_at_10": sum(1.0 / r for r in valid if r <= 10) / n,
        "median_rank": float(np.median([r if r is not None else missing_rank for r in ranks])),
    }


def score_slices(
    slice_a: list[dict[str, Any]],
    galaxy: list[dict[str, Any]],
    hard_candidates: dict[str, list[str]],
    docs: dict[str, dict[str, Any]],
    qvecs: dict[str, dict[str, np.ndarray]],
    dvecs: dict[str, dict[str, np.ndarray]],
    models: list[str],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    metrics: dict[str, Any] = {m: {} for m in models}
    examples: list[dict[str, Any]] = []
    a_docs = sorted({p["doc_id"] for p in slice_a})
    a0 = [p for p in slice_a if p["tier"] == "A0"]
    a0_docs = sorted({p["doc_id"] for p in a0})
    galaxy_strict = [p for p in galaxy if p["label"] == "strict_support"]
    galaxy_relaxed = [p for p in galaxy if p["label"] in ("strict_support", "adjacent_support")]
    galaxy_docs = sorted({p["doc_id"] for p in galaxy})

    rank_cache: dict[tuple[str, str, str], int | None] = {}
    for model in models:
        for name, pairs, candidates in [
            ("slice_a_combined_global", slice_a, a_docs),
            ("slice_a_a0_global", a0, a_docs),
            ("slice_a_a0_vs_a0_global", a0, a0_docs),
            ("galaxy_strict_global", galaxy_strict, galaxy_docs),
            ("galaxy_relaxed_global", galaxy_relaxed, galaxy_docs),
        ]:
            ranks = []
            for p in pairs:
                ranked = rank(qvecs[model][p["query_id"]], dvecs[model], candidates)
                gold = p["doc_id"]
                r = ranked.index(gold) + 1 if gold in ranked else None
                ranks.append(r)
                rank_cache[(model, name, p["query_id"] + "|" + gold)] = r
            metrics[model][name] = metric_from_ranks(ranks, len(candidates) + 1)

        hard_pairs = [p for p in slice_a if len(hard_candidates.get(p["pair_id"], [])) >= 20]
        hard_ranks = []
        for p in hard_pairs:
            candidates = [p["doc_id"]] + hard_candidates[p["pair_id"]]
            ranked = rank(qvecs[model][p["query_id"]], dvecs[model], candidates)
            r = ranked.index(p["doc_id"]) + 1 if p["doc_id"] in ranked else None
            hard_ranks.append(r)
            rank_cache[(model, "slice_c_hard_negative", p["query_id"] + "|" + p["doc_id"])] = r
        metrics[model]["slice_c_hard_negative"] = metric_from_ranks(hard_ranks, 122)

    for p in slice_a[:]:
        key = p["query_id"] + "|" + p["doc_id"]
        n_rank = rank_cache.get(("nomic", "slice_c_hard_negative", key))
        for model in [m for m in models if m != "nomic"]:
            m_rank = rank_cache.get((model, "slice_c_hard_negative", key))
            if n_rank and m_rank and abs(n_rank - m_rank) >= 20:
                examples.append(
                    {
                        "slice": "C",
                        "model": model,
                        "direction": "qwen_win" if m_rank < n_rank else "qwen_loss",
                        "page_slug": p["page_slug"],
                        "claim_id": p["claim_id"],
                        "doc_id": p["doc_id"],
                        "claim": p["claim_text"][:220],
                        "title": p["title"][:160],
                        "nomic_rank": n_rank,
                        "model_rank": m_rank,
                    }
                )
    examples.sort(key=lambda x: abs(x["nomic_rank"] - x["model_rank"]), reverse=True)
    return metrics, examples[:40]


async def latency_one(client: httpx.AsyncClient, model: str, prompt: str, keep_alive: str) -> tuple[float, bool]:
    start = time.perf_counter()
    try:
        r = await client.post(
            f"{OLLAMA_BASE}/api/embeddings",
            json={"model": model, "prompt": prompt[:1200], "keep_alive": keep_alive},
            timeout=60,
        )
        r.raise_for_status()
        ok = bool(r.json().get("embedding"))
    except Exception:
        ok = False
    return (time.perf_counter() - start) * 1000.0, ok


async def latency_run_model(model_key: str, queries: list[str], concurrency: int, cold: bool) -> dict[str, Any]:
    spec = MODELS[model_key]
    keep_alive = "0s" if cold else "30m"
    sem = asyncio.Semaphore(concurrency)
    async with httpx.AsyncClient() as client:
        async def task(q: str) -> tuple[float, bool]:
            async with sem:
                return await latency_one(client, spec["ollama"], spec["prefix"] + q, keep_alive)
        results = await asyncio.gather(*(task(q) for q in queries))
    lat = [x for x, ok in results if ok]
    errors = sum(1 for _, ok in results if not ok)
    return {
        "model": spec["ollama"],
        "mode": "cold_keep_alive_0s" if cold else "hot_keep_alive_30m",
        "concurrency": concurrency,
        "count": len(results),
        "errors": errors,
        "p50_ms": percentile(lat, 0.50),
        "p90_ms": percentile(lat, 0.90),
        "p95_ms": percentile(lat, 0.95),
        "p99_ms": percentile(lat, 0.99),
    }


def latency_benchmark(models: list[str], queries: list[str]) -> dict[str, Any]:
    selected = queries[:200]
    out: dict[str, Any] = {}
    for model in models:
        out[model] = {}
        for cold in [False, True]:
            for conc in [1, 2, 4]:
                key = f"{'cold' if cold else 'hot'}_c{conc}"
                out[model][key] = asyncio.run(latency_run_model(model, selected, conc, cold))
                print(json.dumps({"event": "latency_done", "model": model, "case": key, "p95": out[model][key]["p95_ms"], "errors": out[model][key]["errors"]}), flush=True)
    return out


def rel(new: float, base: float) -> float | None:
    return None if base == 0 else (new - base) / base


def pass_fail(metrics: dict[str, Any], latency: dict[str, Any], timings: dict[str, Any], galaxy_meta: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    n = metrics["nomic"]
    n_hot = latency["nomic"]["hot_c1"]["p95_ms"] or 0
    for model in [m for m in metrics if m != "nomic"]:
        m = metrics[model]
        hard_abs_vs_q06 = None
        galaxy_abs_vs_q06 = None
        if model == "qwen4b" and "qwen06" in metrics:
            hard_abs_vs_q06 = m["slice_c_hard_negative"]["recall_at_10"] - metrics["qwen06"]["slice_c_hard_negative"]["recall_at_10"]
            galaxy_abs_vs_q06 = m["galaxy_strict_global"]["recall_at_10"] - metrics["qwen06"]["galaxy_strict_global"]["recall_at_10"]
        hot_p95 = latency[model]["hot_c1"]["p95_ms"]
        offline_ratio = (
            (timings[model]["query_seconds_per_1000"] + timings[model]["doc_seconds_per_1000"])
            / max(0.001, timings["nomic"]["query_seconds_per_1000"] + timings["nomic"]["doc_seconds_per_1000"])
        )
        out[model] = {
            "galaxy_coverage_gate": galaxy_meta["label_counts"].get("strict_support", 0) >= 100,
            "global_a_combined_r10_relative": rel(m["slice_a_combined_global"]["recall_at_10"], n["slice_a_combined_global"]["recall_at_10"]),
            "global_a0_r10_relative": rel(m["slice_a_a0_global"]["recall_at_10"], n["slice_a_a0_global"]["recall_at_10"]),
            "global_a0_vs_a0_r10_relative": rel(m["slice_a_a0_vs_a0_global"]["recall_at_10"], n["slice_a_a0_vs_a0_global"]["recall_at_10"]),
            "hard_r10_relative": rel(m["slice_c_hard_negative"]["recall_at_10"], n["slice_c_hard_negative"]["recall_at_10"]),
            "hard_mrr_relative": rel(m["slice_c_hard_negative"]["mrr_at_10"], n["slice_c_hard_negative"]["mrr_at_10"]),
            "galaxy_strict_r10_relative": rel(m["galaxy_strict_global"]["recall_at_10"], n["galaxy_strict_global"]["recall_at_10"]),
            "hot_p95_ms": hot_p95,
            "hot_p95_ratio_vs_nomic": (hot_p95 / n_hot) if hot_p95 and n_hot else None,
            "offline_ratio_vs_nomic": offline_ratio,
            "qwen4b_hard_abs_vs_qwen06": hard_abs_vs_q06,
            "qwen4b_galaxy_abs_vs_qwen06": galaxy_abs_vs_q06,
        }
        if model.startswith("qwen06"):
            out[model]["passes_summary"] = (
                out[model]["galaxy_coverage_gate"]
                and (out[model]["global_a_combined_r10_relative"] or 0) >= 0.15
                and (out[model]["global_a0_r10_relative"] or 0) >= 0.08
                and (out[model]["hard_r10_relative"] or 0) >= 0.10
                and (out[model]["hard_mrr_relative"] or 0) >= 0.05
                and (out[model]["galaxy_strict_r10_relative"] or 0) >= 0.10
                and offline_ratio <= 2.5
                and (out[model]["hot_p95_ratio_vs_nomic"] or 999) <= 2.0
            )
        elif model == "qwen4b":
            out[model]["passes_summary"] = (
                out[model]["galaxy_coverage_gate"]
                and (out[model]["global_a_combined_r10_relative"] or 0) >= 0.18
                and (hard_abs_vs_q06 or -1) >= 0.03
                and (galaxy_abs_vs_q06 or -1) >= 0.03
                and offline_ratio <= 7.5
                and hot_p95 is not None
                and hot_p95 <= 700
                and (out[model]["hot_p95_ratio_vs_nomic"] or 999) <= 3.0
            )
    return out


def write_report(report: dict[str, Any], path: Path) -> None:
    lines = [
        "# Embeddings A/B Phase 2 Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "## Gate Summary",
        "",
        f"- Slice A selected pairs: {report['slice_a']['selected_count']}",
        f"- Galaxy strict_support labels: {report['galaxy']['label_counts'].get('strict_support', 0)}",
        f"- Galaxy coverage gate: {'PASS' if report['galaxy']['label_counts'].get('strict_support', 0) >= 100 else 'FAIL'}",
        f"- Hard-negative included gold pairs: {report['slice_c']['included_gold_pairs']}",
        f"- Hard-negative included unique queries: {report['slice_c']['included_unique_queries']}",
        f"- Hard-negative candidate size median: {report['slice_c']['candidate_size']['median']}",
        "",
        "## Pass/Fail",
        "",
    ]
    for model, row in report["pass_fail"].items():
        lines.append(f"- {model}: {'PASS' if row['passes_summary'] else 'FAIL'}")
    lines.extend(["", "## Slice A Counts", "", f"- Tiers selected: {report['slice_a']['selected_by_tier']}"])
    lines.extend(["", "## Metrics", ""])
    for model, scopes in report["metrics"].items():
        lines.append(f"### {model}")
        for scope, m in scopes.items():
            lines.append(
                f"- {scope}: R@1={m['recall_at_1']:.3f}, R@5={m['recall_at_5']:.3f}, "
                f"R@10={m['recall_at_10']:.3f}, MRR@10={m['mrr_at_10']:.3f}, median={m['median_rank']}"
            )
        t = report["timings"][model]
        lines.append(
            f"- Runtime: query {t['query_seconds_per_1000']:.1f}s/1k, doc {t['doc_seconds_per_1000']:.1f}s/1k"
        )
        if report.get("latency"):
            lines.append(f"- Hot c1 p95: {report['latency'][model]['hot_c1']['p95_ms']}")
        else:
            lines.append("- Hot c1 p95: skipped")
        lines.append("")
    lines.extend(["## Threshold Details", ""])
    for model, row in report["pass_fail"].items():
        lines.append(f"- {model}: `{json.dumps(row, sort_keys=True)}`")
    lines.extend(["", "## Qualitative Examples", ""])
    for ex in report["qualitative_examples"][:20]:
        lines.append(
            f"- {ex['direction']} {ex['model']} {ex['page_slug']}: nomic rank {ex['nomic_rank']} "
            f"vs model rank {ex['model_rank']} — {ex['claim']} / {ex['title']}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit-a", type=int, default=1000)
    parser.add_argument("--models", nargs="+", default=list(MODELS))
    parser.add_argument("--skip-latency", action="store_true")
    args = parser.parse_args()

    run_stamp = stamp()
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    json_out = LOG_DIR / f"embedding_ab_phase2b_{run_stamp}.json"
    galaxy_out = LOG_DIR / f"embedding_ab_phase2b_galaxy_fixture_{run_stamp}.json"
    md_out = WORKSPACE_DIR / f"Report_Embeddings_AB_Phase2b_{dt.datetime.now().date().isoformat()}.md"

    started = time.perf_counter()
    slice_a, slice_a_meta = fetch_slice_a(limit=args.limit_a)
    galaxy, galaxy_meta = build_galaxy_fixture(galaxy_out)
    print(json.dumps({"event": "slice_builders_done", "slice_a": slice_a_meta, "galaxy": galaxy_meta, "galaxy_fixture": str(galaxy_out)}), flush=True)
    if galaxy_meta["label_counts"].get("strict_support", 0) < 100:
        report = {
            "generated_at": iso_now(),
            "elapsed_seconds": time.perf_counter() - started,
            "status": "blocked_galaxy_coverage",
            "slice_a": slice_a_meta,
            "galaxy": galaxy_meta,
            "galaxy_fixture": str(galaxy_out),
            "message": "Galaxy strict_support count below 100; per design, stop and escalate.",
        }
        json_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
        md_out.write_text(
            "# Embeddings A/B Phase 2 Report\n\n"
            f"Generated: {report['generated_at']}\n\n"
            "Status: BLOCKED - galaxy coverage gate failed.\n\n"
            f"Strict support labels: {galaxy_meta['label_counts'].get('strict_support', 0)}\n"
            f"Fixture: `{galaxy_out}`\n",
            encoding="utf-8",
        )
        print(json.dumps({"event": "blocked_galaxy_coverage", "json_out": str(json_out), "md_out": str(md_out)}), flush=True)
        return

    hard_pre, evidence_docs, hard_pre_meta = build_pre_nomic_hard_candidates(slice_a)
    docs: dict[str, dict[str, Any]] = {}
    for p in slice_a:
        docs[p["doc_id"]] = p
    for doc_id in {d for values in hard_pre.values() for d in values}:
        if doc_id in evidence_docs:
            docs[doc_id] = evidence_docs[doc_id]
    for g in galaxy:
        docs[g["doc_id"]] = g

    all_pairs = slice_a + galaxy
    qvecs, dvecs, timings = embed_all(all_pairs, docs, args.models)
    hard_final, hard_meta = add_nomic_neighbors(slice_a, hard_pre, docs, qvecs, dvecs)
    print(json.dumps({"event": "corpus_embedded", "timings": timings, "slice_c": hard_meta}), flush=True)

    metrics, examples = score_slices(slice_a, galaxy, hard_final, docs, qvecs, dvecs, args.models)
    latency = {} if args.skip_latency else latency_benchmark(args.models, [p["claim_text"] for p in slice_a[:200]])
    print(json.dumps({"event": "latency_benchmark_complete", "skip": args.skip_latency}), flush=True)
    verdicts = pass_fail(metrics, latency, timings, galaxy_meta) if latency else {}

    report = {
        "generated_at": iso_now(),
        "elapsed_seconds": time.perf_counter() - started,
        "status": "complete",
        "models": {k: MODELS[k] for k in args.models},
        "slice_a": slice_a_meta,
        "galaxy": galaxy_meta,
        "galaxy_fixture": str(galaxy_out),
        "slice_c_pre_nomic": hard_pre_meta,
        "slice_c": hard_meta,
        "timings": timings,
        "metrics": metrics,
        "latency": latency,
        "pass_fail": verdicts,
        "qualitative_examples": examples,
    }
    json_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    write_report(report, md_out)
    print(json.dumps({"event": "report_done", "json_out": str(json_out), "md_out": str(md_out), "pass_fail": verdicts}), flush=True)


if __name__ == "__main__":
    main()
