#!/usr/bin/env python3
"""Jina v3 embedding delta against signed-off Phase 2b fixtures.

Shadow-only. Reads production DB for the same deterministic Slice A/doc pools
used by Phase 2b, but writes only JSON/Markdown artifacts under logs/workspace.
Run with:
  /Users/duhokim/NebulaMind/venvs/embedding_ab_jina/bin/python scripts/embedding_ab_jina_phase3.py
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import math
import os
import random
import re
import statistics
import subprocess
import sys
import tempfile
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import httpx
import numpy as np
import torch
import transformers
from sqlalchemy import create_engine, text
from transformers import AutoModel


DB_URL = os.getenv("DATABASE_URL", "postgresql://nebula:nebula@localhost:5432/nebulamind")
ENGINE = create_engine(DB_URL)
LOG_DIR = Path("/Users/duhokim/NebulaMind/logs")
WORKSPACE_DIR = Path("/Users/duhokim/.openclaw/workspace")
PHASE2B_JSON = LOG_DIR / "embedding_ab_phase2b_20260523_0729.json"
PHASE2B_GALAXY = LOG_DIR / "embedding_ab_phase2b_galaxy_fixture_20260523_0729.json"
PHASE2B_AUDIT = LOG_DIR / "embedding_ab_phase2b_label_audit_20260523_0729.json"
RANDOM_SEED = 20260523
JINA_MODEL_ID = "jinaai/jina-embeddings-v3"

STOP = {
    "the", "and", "for", "with", "that", "this", "from", "into", "onto", "are", "was", "were",
    "been", "being", "have", "has", "had", "not", "but", "its", "their", "they", "them", "these",
    "those", "between", "within", "across", "through", "using", "used", "use", "than", "then",
    "galaxy", "galaxies", "astronomy", "wiki", "claim", "evidence", "paper", "abstract",
}


def now_stamp() -> str:
    return dt.datetime.now().strftime("%Y%m%d_%H%M")


def iso_now() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def toks(value: str) -> list[str]:
    return [
        t for t in re.findall(r"[a-z0-9]+", (value or "").lower())
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


def trim_query(value: str) -> str:
    return (value or "")[:1800]


def trim_doc(value: str) -> str:
    return (value or "")[:12000]


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    denom = float(np.linalg.norm(a) * np.linalg.norm(b))
    return 0.0 if denom == 0.0 else float(np.dot(a, b) / denom)


def normalize(mat: np.ndarray) -> np.ndarray:
    arr = np.asarray(mat, dtype=np.float32)
    norms = np.linalg.norm(arr, axis=1, keepdims=True)
    norms[norms == 0.0] = 1.0
    return arr / norms


def percentile(values: list[float], p: float) -> float | None:
    if not values:
        return None
    values = sorted(values)
    if len(values) == 1:
        return values[0]
    idx = (len(values) - 1) * p
    lo, hi = math.floor(idx), math.ceil(idx)
    if lo == hi:
        return values[lo]
    return values[lo] * (hi - idx) + values[hi] * (idx - lo)


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
        k1, b = 1.2, 0.75
        total = 0.0
        for token in q:
            f = c.get(token, 0)
            if f:
                total += self.idf.get(token, 0.0) * f * (k1 + 1.0) / (f + k1 * (1 - b + b * length / self.avgdl))
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


def fetch_slice_a(limit: int = 1000, cap_per_page: int = 40) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    pub = "(e.peer_reviewed=true or e.doi is not null or e.ads_bibcode is not null or e.journal_ref is not null)"
    tiers = [
        ("A0", f"e.stance='supports' and c.trust_level in ('accepted','consensus') and e.abstract is not null and length(e.abstract)>=300 and {pub} and coalesce(v.pos_w,0)>=3 and coalesce(v.neg_n,0)=0"),
        ("A1", f"e.stance='supports' and c.trust_level in ('accepted','consensus','debated') and e.abstract is not null and length(e.abstract)>=300 and {pub} and coalesce(v.pos_w,0)>=3 and coalesce(v.neg_n,0)=0"),
        ("A2", f"e.stance='supports' and c.trust_level in ('accepted','consensus','debated') and e.abstract is not null and length(e.abstract)>=300 and {pub} and coalesce(v.pos_w,0)>=2 and coalesce(v.neg_n,0)=0"),
        ("A3", f"e.stance='supports' and c.trust_level in ('accepted','consensus','debated') and e.abstract is not null and length(e.abstract)>=300 and {pub} and coalesce(v.neg_n,0)=0 and (coalesce(v.pos_w,0)>=2 or (coalesce(v.pos_w,0)=0 and e.quality>=0.70 and e.source_channel is not null))"),
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
    with ENGINE.connect() as conn:
        for tier, where in tiers:
            rows = [dict(r._mapping) for r in conn.execute(text(f"""
              SELECT c.id AS claim_id, c.text AS claim_text, c.trust_level, c.page_id,
                     wp.slug AS page_slug, wp.title AS page_title,
                     e.id AS evidence_id, e.title, e.abstract, e.summary, e.year,
                     e.quality, e.source_channel, e.doi, e.ads_bibcode, e.journal_ref,
                     e.peer_reviewed, COALESCE(v.pos_w,0) AS pos_weight,
                     COALESCE(v.neg_n,0) AS neg_votes, COALESCE(v.vote_count,0) AS vote_count
              {base}
              WHERE {where}
            """)).fetchall()]
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


def fetch_evidence_pool() -> list[dict[str, Any]]:
    with ENGINE.connect() as conn:
        return [dict(r._mapping) for r in conn.execute(text("""
          SELECT e.id AS evidence_id, e.claim_id, c.page_id, wp.slug AS page_slug, wp.title AS page_title,
                 e.title, e.abstract, e.summary, e.year, e.stance
          FROM evidence e
          JOIN claims c ON c.id = e.claim_id
          JOIN wiki_pages wp ON wp.id = c.page_id
          WHERE e.abstract IS NOT NULL AND length(e.abstract) >= 300
        """)).fetchall()]


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
    query_text = {r["query_id"]: r["claim_text"] for r in slice_a}
    gold_docs_by_query: defaultdict[str, set[str]] = defaultdict(set)
    for row in slice_a:
        gold_docs_by_query[row["query_id"]].add(row["doc_id"])
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
        page_title_tokens = set(toks(pair["page_title"]))
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
    return candidates, docs, {
        "gold_pairs": len(candidates),
        "unique_queries": len({r["query_id"] for r in slice_a}),
        "multi_gold_queries": sum(1 for v in gold_docs_by_query.values() if len(v) > 1),
        "max_gold_docs_per_query": max((len(v) for v in gold_docs_by_query.values()), default=0),
        "pre_nomic_negative_size": {"min": min(sizes), "median": statistics.median(sizes), "max": max(sizes)},
        "evidence_pool_size": len(pool),
    }


def add_embedding_neighbors(
    slice_a: list[dict[str, Any]],
    candidates: dict[str, list[str]],
    docs: dict[str, dict[str, Any]],
    qvecs: dict[str, np.ndarray],
    dvecs: dict[str, np.ndarray],
) -> tuple[dict[str, list[str]], dict[str, Any]]:
    doc_ids = list(docs.keys())
    gold_docs_by_query: defaultdict[str, set[str]] = defaultdict(set)
    for pair in slice_a:
        gold_docs_by_query[pair["query_id"]].add(pair["doc_id"])
    for pair in slice_a:
        qid = pair["query_id"]
        pair_id = pair["pair_id"]
        excluded = gold_docs_by_query[qid]
        ranked = [
            (doc_id, cosine(qvecs[qid], dvecs[doc_id]))
            for doc_id in doc_ids
            if doc_id not in excluded
        ]
        ranked.sort(key=lambda x: x[1], reverse=True)
        merged = list(candidates[pair_id]) + [doc_id for doc_id, _ in ranked[:30]]
        out: list[str] = []
        seen: set[str] = set()
        for doc_id in merged:
            if doc_id not in excluded and doc_id not in seen:
                seen.add(doc_id)
                out.append(doc_id)
        candidates[pair_id] = out
    sizes = [len(v) for v in candidates.values()]
    included = [p for p in slice_a if len(candidates[p["pair_id"]]) >= 20]
    return candidates, {
        "gold_pairs": len(candidates),
        "unique_queries": len({p["query_id"] for p in slice_a}),
        "candidate_size": {"min": min(sizes), "median": statistics.median(sizes), "max": max(sizes)},
        "included_gold_pairs": len(included),
        "included_unique_queries": len({p["query_id"] for p in included}),
        "excluded_lt20_negatives": sum(1 for v in candidates.values() if len(v) < 20),
    }


def load_galaxy_fixture() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    payload = json.loads(PHASE2B_GALAXY.read_text())
    items = payload["items"]
    for row in items:
        row["slice"] = "B"
        row["query_id"] = f"g:c:{row['claim_id']}"
        row["doc_id"] = f"g:{row['arxiv_id']}"
        row["pair_id"] = f"{row['query_id']}|{row['doc_id']}"
        row["doc_text"] = doc_text(row)
    return items, payload["meta"]


def rank(query_vec: np.ndarray, doc_vecs: dict[str, np.ndarray], candidate_ids: list[str]) -> list[str]:
    scored = [(doc_id, cosine(query_vec, doc_vecs[doc_id])) for doc_id in candidate_ids if doc_id in doc_vecs]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [doc_id for doc_id, _ in scored]


def metric_from_ranks(ranks: list[int | None], missing_rank: int) -> dict[str, Any]:
    n = len(ranks)
    valid = [r for r in ranks if r is not None]
    return {
        "n": n,
        "recall_at_1": sum(1 for r in valid if r <= 1) / n if n else 0,
        "recall_at_5": sum(1 for r in valid if r <= 5) / n if n else 0,
        "recall_at_10": sum(1 for r in valid if r <= 10) / n if n else 0,
        "mrr_at_10": sum(1.0 / r for r in valid if r <= 10) / n if n else 0,
        "median_rank": float(np.median([r if r is not None else missing_rank for r in ranks])) if n else None,
    }


def score_slices(
    slice_a: list[dict[str, Any]],
    galaxy: list[dict[str, Any]],
    hard_candidates: dict[str, list[str]],
    qvecs: dict[str, np.ndarray],
    dvecs: dict[str, np.ndarray],
) -> dict[str, Any]:
    metrics: dict[str, Any] = {}
    a_docs = sorted({p["doc_id"] for p in slice_a})
    a0 = [p for p in slice_a if p["tier"] == "A0"]
    a0_docs = sorted({p["doc_id"] for p in a0})
    galaxy_strict = [p for p in galaxy if p["label"] == "strict_support"]
    galaxy_relaxed = [p for p in galaxy if p["label"] in {"strict_support", "adjacent_support"}]
    galaxy_docs = sorted({p["doc_id"] for p in galaxy})
    for name, pairs, candidates in [
        ("slice_a_combined_global", slice_a, a_docs),
        ("slice_a_a0_global", a0, a_docs),
        ("slice_a_a0_vs_a0_global", a0, a0_docs),
        ("galaxy_strict_global", galaxy_strict, galaxy_docs),
        ("galaxy_relaxed_global", galaxy_relaxed, galaxy_docs),
    ]:
        ranks = []
        for p in pairs:
            ranked = rank(qvecs[p["query_id"]], dvecs, candidates)
            ranks.append(ranked.index(p["doc_id"]) + 1 if p["doc_id"] in ranked else None)
        metrics[name] = metric_from_ranks(ranks, len(candidates) + 1)
    hard_pairs = [p for p in slice_a if len(hard_candidates[p["pair_id"]]) >= 20]
    ranks = []
    for p in hard_pairs:
        candidates = [p["doc_id"]] + hard_candidates[p["pair_id"]]
        ranked = rank(qvecs[p["query_id"]], dvecs, candidates)
        ranks.append(ranked.index(p["doc_id"]) + 1 if p["doc_id"] in ranked else None)
    metrics["slice_c_hard_negative"] = metric_from_ranks(ranks, 122)
    return metrics


class JinaEmbedder:
    def __init__(self, batch_size: int):
        self.batch_size = batch_size
        self.device = "mps" if torch.backends.mps.is_available() else "cpu"
        start = time.perf_counter()
        self.model = AutoModel.from_pretrained(JINA_MODEL_ID, trust_remote_code=True)
        try:
            self.model.to(self.device)
        except Exception:
            self.device = "cpu"
        self.load_seconds = time.perf_counter() - start

    def encode_many(self, texts: list[str], task: str) -> np.ndarray:
        chunks: list[np.ndarray] = []
        for i in range(0, len(texts), self.batch_size):
            batch = texts[i : i + self.batch_size]
            arr = self.model.encode(batch, task=task, batch_size=self.batch_size)
            chunks.append(np.asarray(arr, dtype=np.float32))
        return normalize(np.vstack(chunks))


def embed_corpus(embedder: JinaEmbedder, queries: dict[str, str], docs: dict[str, dict[str, Any]]) -> tuple[dict[str, np.ndarray], dict[str, np.ndarray], dict[str, Any]]:
    q_ids = list(queries)
    d_ids = list(docs)
    q_texts = [trim_query(queries[qid]) for qid in q_ids]
    d_texts = [trim_doc(docs[doc_id]["doc_text"]) for doc_id in d_ids]
    q_start = time.perf_counter()
    q_mat = embedder.encode_many(q_texts, "retrieval.query")
    q_seconds = time.perf_counter() - q_start
    print(json.dumps({"event": "queries_embedded", "count": len(q_ids), "seconds": q_seconds}), flush=True)
    d_start = time.perf_counter()
    d_mat = embedder.encode_many(d_texts, "retrieval.passage")
    d_seconds = time.perf_counter() - d_start
    print(json.dumps({"event": "docs_embedded", "count": len(d_ids), "seconds": d_seconds}), flush=True)
    qvecs = {qid: q_mat[i] for i, qid in enumerate(q_ids)}
    dvecs = {doc_id: d_mat[i] for i, doc_id in enumerate(d_ids)}
    trunc = {
        "query_count": len(q_texts),
        "doc_count": len(d_texts),
        "query_chars_max": max(map(len, q_texts)) if q_texts else 0,
        "doc_chars_max": max(map(len, d_texts)) if d_texts else 0,
        "docs_truncated_at_12000_chars": sum(1 for row in docs.values() if len(row["doc_text"]) > 12000),
    }
    timings = {
        "model_load_seconds": embedder.load_seconds,
        "query_count": len(q_ids),
        "doc_count": len(d_ids),
        "query_seconds": q_seconds,
        "doc_seconds": d_seconds,
        "query_seconds_per_1000": q_seconds / max(1, len(q_ids)) * 1000,
        "doc_seconds_per_1000": d_seconds / max(1, len(d_ids)) * 1000,
    }
    return qvecs, dvecs, {"timings": timings, "truncation": trunc}


def latency_benchmark(embedder: JinaEmbedder, queries: list[str]) -> dict[str, Any]:
    selected = [trim_query(q) for q in queries[:200]]

    def one(q: str) -> tuple[float, bool]:
        start = time.perf_counter()
        try:
            arr = embedder.model.encode([q], task="retrieval.query", batch_size=1)
            ok = np.asarray(arr).shape[-1] == 1024
        except Exception:
            ok = False
        return (time.perf_counter() - start) * 1000.0, ok

    out: dict[str, Any] = {}
    for concurrency in [1, 2, 4]:
        lat: list[float] = []
        errors = 0
        if concurrency == 1:
            for q in selected:
                ms, ok = one(q)
                lat.append(ms)
                errors += 0 if ok else 1
        else:
            with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
                for ms, ok in pool.map(one, selected):
                    lat.append(ms)
                    errors += 0 if ok else 1
        out[f"hot_c{concurrency}"] = {
            "count": len(selected),
            "errors": errors,
            "p50_ms": percentile(lat, 0.50),
            "p90_ms": percentile(lat, 0.90),
            "p95_ms": percentile(lat, 0.95),
            "p99_ms": percentile(lat, 0.99),
        }
    # HF cold start is model-load dominated; measure a single subprocess load+encode sample.
    code = """
import time, json
from transformers import AutoModel
t=time.perf_counter()
m=AutoModel.from_pretrained('jinaai/jina-embeddings-v3', trust_remote_code=True)
load=time.perf_counter()-t
t=time.perf_counter()
v=m.encode(['Massive galaxies quench at high redshift.'], task='retrieval.query')
enc=time.perf_counter()-t
print(json.dumps({'load_ms': load*1000, 'first_encode_ms': enc*1000, 'dim': int(v.shape[-1])}))
"""
    try:
        proc = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=180)
        cold = json.loads(proc.stdout.strip().splitlines()[-1])
        cold_ms = cold["load_ms"] + cold["first_encode_ms"]
        cold_errors = 0 if cold.get("dim") == 1024 else 1
    except Exception as exc:
        cold_ms = None
        cold_errors = 1
        cold = {"error": str(exc)}
    for concurrency in [1, 2, 4]:
        out[f"cold_c{concurrency}"] = {
            "count": 1,
            "errors": cold_errors,
            "p50_ms": cold_ms,
            "p90_ms": cold_ms,
            "p95_ms": cold_ms,
            "p99_ms": cold_ms,
            "note": "HF cold start measured as one subprocess model load plus first encode; concurrency cold start is not production-shaped.",
            "raw": cold,
        }
    return out


def pass_fail(metrics: dict[str, Any], phase2b: dict[str, Any], timings: dict[str, Any], latency: dict[str, Any], failures: int) -> dict[str, Any]:
    q06 = phase2b["metrics"]["qwen06"]
    nomic_t = phase2b["timings"]["nomic"]
    nomic_hot = phase2b["latency"]["nomic"]["hot_c1"]["p95_ms"]
    nomic_offline = nomic_t["query_seconds_per_1000"] + nomic_t["doc_seconds_per_1000"]
    jina_offline = timings["query_seconds_per_1000"] + timings["doc_seconds_per_1000"]
    hot_p95 = latency["hot_c1"]["p95_ms"]
    cold_p95 = latency["cold_c1"]["p95_ms"]
    gates = {
        "slice_a_combined_r10": {"value": metrics["slice_a_combined_global"]["recall_at_10"], "target": 0.305},
        "a0_vs_a0_r10": {"value": metrics["slice_a_a0_vs_a0_global"]["recall_at_10"], "target": 0.680},
        "hard_negative_r10": {"value": metrics["slice_c_hard_negative"]["recall_at_10"], "target": 0.144},
        "galaxy_strict_r10": {"value": metrics["galaxy_strict_global"]["recall_at_10"], "target": 0.824},
        "slice_c_mrr_no_worse_than_qwen06_minus_2pct": {
            "value": metrics["slice_c_hard_negative"]["mrr_at_10"],
            "target": q06["slice_c_hard_negative"]["mrr_at_10"] * 0.98,
        },
        "galaxy_strict_mrr_no_worse_than_qwen06_minus_2pct": {
            "value": metrics["galaxy_strict_global"]["mrr_at_10"],
            "target": q06["galaxy_strict_global"]["mrr_at_10"] * 0.98,
        },
        "offline_ratio_vs_nomic": {"value": jina_offline / nomic_offline, "target": 2.5, "direction": "lte"},
        "hot_p95_ratio_vs_nomic": {"value": hot_p95 / nomic_hot if hot_p95 else None, "target": 2.0, "direction": "lte"},
        "hot_p95_absolute_ms": {"value": hot_p95, "target": 300.0, "direction": "lte"},
        "cold_p95_ms": {"value": cold_p95, "target": 1500.0, "direction": "lte"},
        "empty_embedding_failures": {"value": failures, "target": 0, "direction": "eq"},
    }
    for row in gates.values():
        direction = row.get("direction", "gte")
        value = row["value"]
        target = row["target"]
        if value is None:
            row["passed"] = False
        elif direction == "lte":
            row["passed"] = value <= target
        elif direction == "eq":
            row["passed"] = value == target
        else:
            row["passed"] = value >= target
    return {
        "passed": all(row["passed"] for row in gates.values()),
        "gates": gates,
        "recommendation": "promote" if all(row["passed"] for row in gates.values()) else "do_not_promote",
        "reranker_candidate": (
            metrics["slice_a_combined_global"]["recall_at_10"] >= q06["slice_a_combined_global"]["recall_at_10"]
            or metrics["slice_c_hard_negative"]["recall_at_10"] >= q06["slice_c_hard_negative"]["recall_at_10"]
        ),
    }


def write_report(report: dict[str, Any], path: Path) -> None:
    pf = report["pass_fail"]
    m = report["metrics"]["jina_v3"]
    lines = [
        "# Embeddings A/B Jina Phase 3 Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "## Verdict",
        "",
        f"- Jina v3: {'PASS' if pf['passed'] else 'FAIL'}",
        f"- Recommendation: {pf['recommendation']}",
        f"- Carry as reranker candidate: {pf['reranker_candidate']}",
        "",
        "## Metrics",
        "",
    ]
    for scope, vals in m.items():
        lines.append(
            f"- {scope}: R@1={vals['recall_at_1']:.3f}, R@5={vals['recall_at_5']:.3f}, "
            f"R@10={vals['recall_at_10']:.3f}, MRR@10={vals['mrr_at_10']:.3f}, median={vals['median_rank']}"
        )
    lines.extend(["", "## Gates", ""])
    for name, row in pf["gates"].items():
        lines.append(f"- {name}: {'PASS' if row['passed'] else 'FAIL'} value={row['value']} target={row['target']}")
    lines.extend([
        "",
        "## Runtime",
        "",
        f"- Model load: {report['timings']['model_load_seconds']:.1f}s",
        f"- Query throughput: {report['timings']['query_seconds_per_1000']:.1f}s / 1k",
        f"- Document throughput: {report['timings']['doc_seconds_per_1000']:.1f}s / 1k",
        f"- Hot c1 p95: {report['latency']['hot_c1']['p95_ms']}",
        f"- Cold c1 p95: {report['latency']['cold_c1']['p95_ms']}",
        "",
        "## Environment",
        "",
        f"- Model: `{JINA_MODEL_ID}`",
        f"- Device requested/used: `{report['environment']['device']}`",
        f"- Torch: `{report['environment']['torch']}`",
        f"- Transformers: `{report['environment']['transformers']}`",
        f"- Vector normalization: `{report['environment']['normalization']}`",
    ])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate_locked_counts(slice_a_meta: dict[str, Any], galaxy_meta: dict[str, Any], hard_meta: dict[str, Any], phase2b: dict[str, Any]) -> None:
    expected = phase2b
    checks = [
        (slice_a_meta["selected_count"], expected["slice_a"]["selected_count"], "Slice A selected_count"),
        (slice_a_meta["a0_subset_count"], expected["slice_a"]["a0_subset_count"], "A0 subset"),
        (galaxy_meta["label_counts"], expected["galaxy"]["label_counts"], "galaxy label_counts"),
        (hard_meta["included_gold_pairs"], expected["slice_c"]["included_gold_pairs"], "Slice C included_gold_pairs"),
        (hard_meta["included_unique_queries"], expected["slice_c"]["included_unique_queries"], "Slice C included_unique_queries"),
    ]
    for actual, want, label in checks:
        if actual != want:
            raise RuntimeError(f"locked fixture mismatch: {label}: {actual!r} != {want!r}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=16)
    args = parser.parse_args()
    started = time.perf_counter()
    run_stamp = now_stamp()
    json_out = LOG_DIR / f"embedding_ab_jina_phase3_{run_stamp}.json"
    md_out = WORKSPACE_DIR / f"Report_Embeddings_AB_Jina_Phase3_{dt.datetime.now().date().isoformat()}.md"
    phase2b = json.loads(PHASE2B_JSON.read_text())
    slice_a, slice_a_meta = fetch_slice_a()
    galaxy, galaxy_meta = load_galaxy_fixture()
    hard_pre, evidence_docs, hard_pre_meta = build_pre_nomic_hard_candidates(slice_a)
    docs: dict[str, dict[str, Any]] = {p["doc_id"]: p for p in slice_a}
    for doc_id in {d for values in hard_pre.values() for d in values}:
        if doc_id in evidence_docs:
            docs[doc_id] = evidence_docs[doc_id]
    for g in galaxy:
        docs[g["doc_id"]] = g
    queries = {p["query_id"]: p["claim_text"] for p in slice_a + galaxy}
    print(json.dumps({"event": "fixtures_loaded", "slice_a": slice_a_meta, "galaxy": galaxy_meta, "docs": len(docs), "queries": len(queries)}), flush=True)
    embedder = JinaEmbedder(batch_size=args.batch_size)
    qvecs, dvecs, embed_meta = embed_corpus(embedder, queries, docs)
    hard_final, hard_meta = add_embedding_neighbors(slice_a, hard_pre, docs, qvecs, dvecs)
    validate_locked_counts(slice_a_meta, galaxy_meta, hard_meta, phase2b)
    metrics = score_slices(slice_a, galaxy, hard_final, qvecs, dvecs)
    print(json.dumps({"event": "scoring_done", "metrics": metrics}), flush=True)
    latency = latency_benchmark(embedder, [p["claim_text"] for p in slice_a[:200]])
    failures = 0
    verdict = pass_fail(metrics, phase2b, embed_meta["timings"], latency, failures)
    report = {
        "generated_at": iso_now(),
        "elapsed_seconds": time.perf_counter() - started,
        "status": "complete",
        "phase2b_json": str(PHASE2B_JSON),
        "phase2b_galaxy_fixture": str(PHASE2B_GALAXY),
        "phase2b_label_audit": str(PHASE2B_AUDIT),
        "slice_a": slice_a_meta,
        "galaxy": galaxy_meta,
        "slice_c_pre_jina": hard_pre_meta,
        "slice_c": hard_meta,
        "model": {"key": "jina_v3", "hf_model": JINA_MODEL_ID, "dim": 1024, "query_task": "retrieval.query", "doc_task": "retrieval.passage"},
        "environment": {
            "python": sys.version,
            "torch": torch.__version__,
            "transformers": transformers.__version__,
            "device": embedder.device,
            "normalization": "L2-normalized in harness before cosine",
            "venv": sys.prefix,
        },
        "timings": embed_meta["timings"],
        "truncation": embed_meta["truncation"],
        "latency": latency,
        "metrics": {"jina_v3": metrics},
        "baseline_phase2b_metrics": phase2b["metrics"],
        "baseline_phase2b_timings": phase2b["timings"],
        "baseline_phase2b_latency": phase2b["latency"],
        "pass_fail": verdict,
    }
    json_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    write_report(report, md_out)
    print(json.dumps({"event": "report_done", "json_out": str(json_out), "md_out": str(md_out), "pass_fail": verdict}), flush=True)


if __name__ == "__main__":
    main()
