#!/usr/bin/env python3
"""Shadow-only embedding A/B harness for NebulaMind Phase 1."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import os
import random
import time
from collections import defaultdict
from pathlib import Path
from typing import Any

import httpx
import numpy as np
from sqlalchemy import text

from app.database import engine


OLLAMA_BASE = os.getenv("EMBED_AB_OLLAMA_BASE", "http://127.0.0.1:11434")
MODELS = {
    "nomic": {"ollama": "nomic-embed-text:v1.5", "dim": 768, "query_prefix": False},
    "qwen06": {"ollama": "qwen3-embedding:0.6b", "dim": 1024, "query_prefix": True},
    "qwen4b": {"ollama": "qwen3-embedding:4b", "dim": 2560, "query_prefix": True},
}
QWEN_QUERY_INSTRUCTION = (
    "Instruct: Given an astronomy wiki claim, retrieve peer-reviewed paper evidence "
    "that supports or challenges the claim.\nQuery: "
)
RANDOM_SEED = 20260523


def now_stamp() -> str:
    return dt.datetime.now().strftime("%Y%m%d_%H%M")


def sha(text_value: str) -> str:
    return hashlib.sha256(text_value.encode("utf-8")).hexdigest()


def vector_literal(vec: list[float]) -> list[float]:
    return [float(x) for x in vec]


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    denom = float(np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0.0:
        return 0.0
    return float(np.dot(a, b) / denom)


def embed(client: httpx.Client, model: str, prompt: str) -> list[float]:
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            response = client.post(
                f"{OLLAMA_BASE}/api/embeddings",
                json={"model": model, "prompt": prompt[:3000], "keep_alive": "30m"},
                timeout=240,
            )
            response.raise_for_status()
            break
        except Exception as exc:
            last_error = exc
            time.sleep(2 + attempt * 4)
    else:
        raise RuntimeError(
            f"embedding failed for {model}: len={len(prompt)} sha={sha(prompt)[:12]} err={last_error}"
        ) from last_error
    vec = response.json().get("embedding")
    if not isinstance(vec, list) or not vec:
        raise RuntimeError(f"empty embedding from {model}")
    return [float(x) for x in vec]


def create_shadow_table() -> dict[str, Any]:
    """Create the shadow table. Use arrays if pgvector is unavailable."""
    with engine.begin() as conn:
        has_vector = bool(
            conn.execute(
                text("select 1 from pg_available_extensions where name='vector'")
            ).first()
        )
        if has_vector:
            conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
            conn.execute(text("DROP TABLE IF EXISTS embedding_ab_items"))
            conn.execute(
                text(
                    """
                    CREATE TABLE embedding_ab_items (
                        id BIGSERIAL PRIMARY KEY,
                        item_kind TEXT NOT NULL,
                        item_id INTEGER NOT NULL,
                        text_hash TEXT NOT NULL,
                        text_content TEXT NOT NULL,
                        nomic_embedding vector(768),
                        qwen06_embedding vector(1024),
                        qwen4b_embedding vector(2560),
                        created_at TIMESTAMP DEFAULT now(),
                        UNIQUE (item_kind, item_id, text_hash)
                    )
                    """
                )
            )
            storage = "pgvector"
        else:
            conn.execute(text("DROP TABLE IF EXISTS embedding_ab_items"))
            conn.execute(
                text(
                    """
                    CREATE TABLE embedding_ab_items (
                        id BIGSERIAL PRIMARY KEY,
                        item_kind TEXT NOT NULL,
                        item_id INTEGER NOT NULL,
                        text_hash TEXT NOT NULL,
                        text_content TEXT NOT NULL,
                        nomic_embedding DOUBLE PRECISION[],
                        qwen06_embedding DOUBLE PRECISION[],
                        qwen4b_embedding DOUBLE PRECISION[],
                        created_at TIMESTAMP DEFAULT now(),
                        UNIQUE (item_kind, item_id, text_hash),
                        CONSTRAINT embedding_ab_nomic_dim CHECK (
                            nomic_embedding IS NULL OR array_length(nomic_embedding, 1) = 768
                        ),
                        CONSTRAINT embedding_ab_qwen06_dim CHECK (
                            qwen06_embedding IS NULL OR array_length(qwen06_embedding, 1) = 1024
                        ),
                        CONSTRAINT embedding_ab_qwen4b_dim CHECK (
                            qwen4b_embedding IS NULL OR array_length(qwen4b_embedding, 1) = 2560
                        )
                    )
                    """
                )
            )
            storage = "double precision arrays; pgvector extension not installed"
    return {"storage": storage, "pgvector_available": has_vector}


def run_preflight() -> dict[str, Any]:
    sample_query = "Massive galaxies formed most of their stars earlier than low-mass galaxies."
    prefixed = QWEN_QUERY_INSTRUCTION + sample_query
    unsupported_field_result: dict[str, Any] | None = None
    with httpx.Client() as client:
        plain_vec = embed(client, MODELS["qwen06"]["ollama"], sample_query)
        prefixed_vec = embed(client, MODELS["qwen06"]["ollama"], prefixed)
        try:
            response = client.post(
                f"{OLLAMA_BASE}/api/embeddings",
                json={
                    "model": MODELS["qwen06"]["ollama"],
                    "prompt": sample_query,
                    "instruction": QWEN_QUERY_INSTRUCTION.strip(),
                },
                timeout=180,
            )
            field_vec = response.json().get("embedding") if response.headers.get("content-type", "").startswith("application/json") else None
            unsupported_field_result = {
                "status_code": response.status_code,
                "returned_embedding": bool(field_vec),
                "cosine_vs_plain": cosine(np.array(plain_vec), np.array(field_vec)) if field_vec else None,
            }
        except Exception as exc:
            unsupported_field_result = {"error": str(exc)}
    similarity = cosine(np.array(plain_vec), np.array(prefixed_vec))
    return {
        "ollama_base": OLLAMA_BASE,
        "model": MODELS["qwen06"]["ollama"],
        "plain_dim": len(plain_vec),
        "prefixed_dim": len(prefixed_vec),
        "plain_vs_prefixed_cosine": similarity,
        "separate_instruction_field_probe": unsupported_field_result,
        "decision": "use inline instruction prefix for qwen query embeddings",
        "instruction_prefix": QWEN_QUERY_INSTRUCTION,
    }


def fetch_eval_pairs(limit: int = 200, max_per_page: int = 20) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    sql = text(
        """
        WITH vote_rollup AS (
            SELECT evidence_id,
                   SUM(CASE WHEN value > 0 THEN COALESCE(weight, 1.0) ELSE 0 END) AS pos_weight,
                   SUM(CASE WHEN value < 0 THEN 1 ELSE 0 END) AS neg_votes,
                   COUNT(*) AS vote_count,
                   COUNT(*) FILTER (WHERE voter_type = 'human') AS human_votes,
                   COUNT(*) FILTER (WHERE voter_type <> 'human') AS agent_votes
            FROM evidence_votes
            GROUP BY evidence_id
        )
        SELECT c.id AS claim_id, c.text AS claim_text, c.trust_level, c.page_id,
               wp.slug AS page_slug, wp.title AS page_title,
               e.id AS evidence_id, e.title, e.abstract, e.summary, e.year,
               e.doi, e.ads_bibcode, e.journal_ref, e.peer_reviewed,
               COALESCE(v.pos_weight, 0) AS pos_weight,
               COALESCE(v.neg_votes, 0) AS neg_votes,
               COALESCE(v.vote_count, 0) AS vote_count,
               COALESCE(v.human_votes, 0) AS human_votes,
               COALESCE(v.agent_votes, 0) AS agent_votes
        FROM claims c
        JOIN evidence e ON e.claim_id = c.id
        JOIN wiki_pages wp ON wp.id = c.page_id
        LEFT JOIN vote_rollup v ON v.evidence_id = e.id
        WHERE e.stance = 'supports'
          AND c.trust_level IN ('accepted', 'consensus')
          AND e.abstract IS NOT NULL
          AND length(e.abstract) >= 300
          AND (e.peer_reviewed = true OR e.doi IS NOT NULL OR e.ads_bibcode IS NOT NULL OR e.journal_ref IS NOT NULL)
          AND COALESCE(v.pos_weight, 0) >= 3
          AND COALESCE(v.neg_votes, 0) = 0
        ORDER BY
          CASE WHEN wp.slug = 'galaxy-evolution' THEN 0
               WHEN wp.slug IN ('galaxy-formation', 'galaxy-clusters') THEN 1
               ELSE 2 END,
          wp.slug,
          c.id,
          e.id
        """
    )
    selected: list[dict[str, Any]] = []
    per_page: defaultdict[str, int] = defaultdict(int)
    with engine.connect() as conn:
        rows = [dict(r._mapping) for r in conn.execute(sql).fetchall()]
        galaxy_evolution_available = sum(1 for r in rows if r["page_slug"] == "galaxy-evolution")
        for row in rows:
            if per_page[row["page_slug"]] >= max_per_page:
                continue
            selected.append(row)
            per_page[row["page_slug"]] += 1
            if len(selected) >= limit:
                break
    meta = {
        "strict_candidate_count": len(rows),
        "selected_count": len(selected),
        "max_per_page": max_per_page,
        "per_page": dict(per_page),
        "galaxy_evolution_available": galaxy_evolution_available,
        "galaxy_evolution_selected": sum(1 for r in selected if r["page_slug"] == "galaxy-evolution"),
        "galaxy_related_selected": sum(
            1 for r in selected if r["page_slug"] in {"galaxy-formation", "galaxy-clusters"}
        ),
    }
    if len(selected) < 100:
        raise RuntimeError(f"only {len(selected)} strict eval rows available; need at least 100")
    return selected, meta


def evidence_doc(row: dict[str, Any]) -> str:
    parts = [row.get("title") or ""]
    if row.get("year"):
        parts.append(f"Year: {row['year']}")
    if row.get("abstract"):
        parts.append(row["abstract"])
    if row.get("summary"):
        parts.append("Summary: " + row["summary"])
    return "\n\n".join(p for p in parts if p)


def fetch_hard_negative_docs(pairs: list[dict[str, Any]], per_query: int = 30) -> tuple[dict[int, list[int]], dict[int, str]]:
    by_page_claims: dict[int, set[int]] = defaultdict(set)
    gold_by_claim: dict[int, set[int]] = defaultdict(set)
    for pair in pairs:
        by_page_claims[int(pair["page_id"])].add(int(pair["claim_id"]))
        gold_by_claim[int(pair["claim_id"])].add(int(pair["evidence_id"]))

    rng = random.Random(RANDOM_SEED)
    hard_scope: dict[int, list[int]] = {}
    doc_texts: dict[int, str] = {}
    with engine.connect() as conn:
        for page_id, claim_ids in by_page_claims.items():
            rows = [
                dict(r._mapping)
                for r in conn.execute(
                    text(
                        """
                        SELECT e.id AS evidence_id, e.title, e.abstract, e.summary, e.year, e.claim_id
                        FROM evidence e
                        JOIN claims c ON c.id = e.claim_id
                        WHERE c.page_id = :page_id
                          AND e.abstract IS NOT NULL
                          AND length(e.abstract) >= 300
                        """
                    ),
                    {"page_id": page_id},
                ).fetchall()
            ]
            for claim_id in claim_ids:
                candidates = [
                    int(r["evidence_id"])
                    for r in rows
                    if int(r["claim_id"]) != claim_id and int(r["evidence_id"]) not in gold_by_claim[claim_id]
                ]
                rng.shuffle(candidates)
                hard_scope[claim_id] = candidates[:per_query]
                for evidence_id in hard_scope[claim_id]:
                    row = next(r for r in rows if int(r["evidence_id"]) == evidence_id)
                    doc_texts[evidence_id] = evidence_doc(row)
    for pair in pairs:
        doc_texts[int(pair["evidence_id"])] = evidence_doc(pair)
    return hard_scope, doc_texts


def upsert_item(
    conn: Any,
    kind: str,
    item_id: int,
    content: str,
    column: str,
    vec: list[float],
) -> None:
    conn.execute(
        text(
            f"""
            INSERT INTO embedding_ab_items (item_kind, item_id, text_hash, text_content, {column})
            VALUES (:kind, :item_id, :text_hash, :content, :vec)
            ON CONFLICT (item_kind, item_id, text_hash)
            DO UPDATE SET {column} = EXCLUDED.{column}
            """
        ),
        {
            "kind": kind,
            "item_id": item_id,
            "text_hash": sha(content),
            "content": content,
            "vec": vector_literal(vec),
        },
    )


def embed_corpus(
    pairs: list[dict[str, Any]],
    doc_texts: dict[int, str],
    models: list[str],
) -> tuple[dict[str, dict[int, np.ndarray]], dict[str, dict[int, np.ndarray]], dict[str, Any]]:
    claim_texts = {int(p["claim_id"]): p["claim_text"] for p in pairs}
    timings: dict[str, Any] = {}
    query_vectors: dict[str, dict[int, np.ndarray]] = {m: {} for m in models}
    doc_vectors: dict[str, dict[int, np.ndarray]] = {m: {} for m in models}
    with httpx.Client() as client:
        for key in models:
            spec = MODELS[key]
            start = time.perf_counter()
            count = 0
            print(json.dumps({"event": "embedding_model_start", "model": key, "ollama": spec["ollama"]}), flush=True)
            with engine.begin() as conn:
                for claim_id, claim_text in claim_texts.items():
                    prompt = QWEN_QUERY_INSTRUCTION + claim_text if spec["query_prefix"] else claim_text
                    vec = embed(client, spec["ollama"], prompt)
                    if len(vec) != spec["dim"]:
                        raise RuntimeError(f"{key} claim dim mismatch: {len(vec)} != {spec['dim']}")
                    query_vectors[key][claim_id] = np.array(vec, dtype=np.float32)
                    upsert_item(conn, "claim", claim_id, claim_text, f"{key}_embedding", vec)
                    count += 1
                for evidence_id, doc in doc_texts.items():
                    vec = embed(client, spec["ollama"], doc)
                    if len(vec) != spec["dim"]:
                        raise RuntimeError(f"{key} doc dim mismatch: {len(vec)} != {spec['dim']}")
                    doc_vectors[key][evidence_id] = np.array(vec, dtype=np.float32)
                    upsert_item(conn, "evidence", evidence_id, doc, f"{key}_embedding", vec)
                    count += 1
            elapsed = time.perf_counter() - start
            timings[key] = {
                "model": spec["ollama"],
                "embedding_count": count,
                "seconds": elapsed,
                "seconds_per_1000_embeddings": elapsed / count * 1000 if count else None,
            }
    return query_vectors, doc_vectors, timings


def rank_for_scope(query_vec: np.ndarray, doc_vecs: dict[int, np.ndarray], candidate_ids: list[int]) -> list[int]:
    scored = [
        (evidence_id, cosine(query_vec, doc_vecs[evidence_id]))
        for evidence_id in candidate_ids
        if evidence_id in doc_vecs
    ]
    scored.sort(key=lambda item: item[1], reverse=True)
    return [evidence_id for evidence_id, _ in scored]


def score(
    pairs: list[dict[str, Any]],
    hard_scope: dict[int, list[int]],
    query_vectors: dict[str, dict[int, np.ndarray]],
    doc_vectors: dict[str, dict[int, np.ndarray]],
    models: list[str],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    global_docs = sorted({int(p["evidence_id"]) for p in pairs})
    metrics: dict[str, Any] = {}
    qualitative: list[dict[str, Any]] = []
    ranks_by_model_scope: dict[tuple[str, str], list[int | None]] = {}
    for model in models:
        for scope_name in ["global", "same_page_hard_negative"]:
            ranks: list[int | None] = []
            for pair in pairs:
                claim_id = int(pair["claim_id"])
                gold_id = int(pair["evidence_id"])
                candidate_ids = global_docs
                if scope_name == "same_page_hard_negative":
                    candidate_ids = [gold_id] + hard_scope.get(claim_id, [])
                ranked = rank_for_scope(query_vectors[model][claim_id], doc_vectors[model], candidate_ids)
                rank = ranked.index(gold_id) + 1 if gold_id in ranked else None
                ranks.append(rank)
            ranks_by_model_scope[(model, scope_name)] = ranks
            valid = [r for r in ranks if r is not None]
            n = len(ranks)
            metrics.setdefault(model, {})[scope_name] = {
                "n": n,
                "recall_at_1": sum(1 for r in valid if r <= 1) / n,
                "recall_at_5": sum(1 for r in valid if r <= 5) / n,
                "recall_at_10": sum(1 for r in valid if r <= 10) / n,
                "mrr_at_10": sum((1 / r) for r in valid if r <= 10) / n,
                "median_rank": float(np.median([r if r is not None else len(global_docs) + 1 for r in ranks])),
            }

    for idx, pair in enumerate(pairs):
        nomic_rank = ranks_by_model_scope[("nomic", "global")][idx]
        for qwen in [m for m in models if m.startswith("qwen")]:
            qwen_rank = ranks_by_model_scope[(qwen, "global")][idx]
            if nomic_rank and qwen_rank and abs(nomic_rank - qwen_rank) >= 20:
                qualitative.append(
                    {
                        "model": qwen,
                        "direction": "qwen_win" if qwen_rank < nomic_rank else "qwen_loss",
                        "claim_id": int(pair["claim_id"]),
                        "evidence_id": int(pair["evidence_id"]),
                        "page_slug": pair["page_slug"],
                        "claim": pair["claim_text"][:240],
                        "evidence_title": pair["title"][:180],
                        "nomic_global_rank": nomic_rank,
                        "qwen_global_rank": qwen_rank,
                    }
                )
    qualitative.sort(key=lambda x: abs(x["nomic_global_rank"] - x["qwen_global_rank"]), reverse=True)
    return metrics, qualitative[:30]


def pass_fail(metrics: dict[str, Any], timings: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    nomic_global = metrics["nomic"]["global"]
    nomic_hard = metrics["nomic"]["same_page_hard_negative"]
    nomic_runtime = timings["nomic"]["seconds_per_1000_embeddings"]
    for model in ["qwen06", "qwen4b"]:
        global_r10 = metrics[model]["global"]["recall_at_10"]
        hard_r10 = metrics[model]["same_page_hard_negative"]["recall_at_10"]
        mrr = metrics[model]["global"]["mrr_at_10"]
        runtime = timings[model]["seconds_per_1000_embeddings"]
        rel_global = (global_r10 - nomic_global["recall_at_10"]) / nomic_global["recall_at_10"] if nomic_global["recall_at_10"] else None
        rel_hard = (hard_r10 - nomic_hard["recall_at_10"]) / nomic_hard["recall_at_10"] if nomic_hard["recall_at_10"] else None
        rel_mrr = (mrr - nomic_global["mrr_at_10"]) / nomic_global["mrr_at_10"] if nomic_global["mrr_at_10"] else None
        runtime_ratio = runtime / nomic_runtime if nomic_runtime else None
        if model == "qwen06":
            passed = (
                rel_global is not None
                and rel_hard is not None
                and rel_mrr is not None
                and runtime_ratio is not None
                and rel_global >= 0.08
                and rel_hard >= 0.05
                and rel_mrr >= -0.02
                and runtime_ratio <= 2.0
            )
        else:
            passed = rel_global is not None and rel_global >= 0.12
        result[model] = {
            "passed_threshold": passed,
            "relative_global_recall_at_10": rel_global,
            "relative_hard_recall_at_10": rel_hard,
            "relative_global_mrr_at_10": rel_mrr,
            "runtime_ratio_vs_nomic": runtime_ratio,
        }
    return result


def write_markdown(report: dict[str, Any], path: Path) -> None:
    lines = [
        "# Embeddings A/B Phase 1 Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "## Verdict",
        "",
    ]
    for model, verdict in report["pass_fail"].items():
        lines.append(f"- {model}: {'PASS' if verdict['passed_threshold'] else 'FAIL'}")
    lines.extend(
        [
            "",
            "Promotion remains Papa's decision. This run did not modify production routing.",
            "",
            "## Pre-flight",
            "",
            f"- Decision: {report['preflight']['decision']}",
            f"- Plain vs prefixed query cosine: {report['preflight']['plain_vs_prefixed_cosine']:.6f}",
            f"- Shadow storage: {report['shadow_table']['storage']}",
            "",
            "## Eval Set",
            "",
            f"- Selected pairs: {report['eval_set']['selected_count']}",
            f"- Strict candidates available: {report['eval_set']['strict_candidate_count']}",
            f"- Galaxy Evolution rows available: {report['eval_set']['galaxy_evolution_available']}",
            f"- Galaxy-related selected: {report['eval_set']['galaxy_related_selected']}",
            "",
            "## Metrics",
            "",
        ]
    )
    for model, scopes in report["metrics"].items():
        lines.append(f"### {model} ({MODELS[model]['ollama']})")
        for scope, values in scopes.items():
            lines.append(
                "- "
                f"{scope}: R@1={values['recall_at_1']:.3f}, "
                f"R@5={values['recall_at_5']:.3f}, "
                f"R@10={values['recall_at_10']:.3f}, "
                f"MRR@10={values['mrr_at_10']:.3f}, "
                f"median_rank={values['median_rank']:.1f}"
            )
        t = report["timings"][model]
        lines.append(f"- Runtime: {t['seconds']:.1f}s total, {t['seconds_per_1000_embeddings']:.1f}s / 1k embeddings")
        lines.append("")
    lines.extend(["## Threshold Details", ""])
    for model, values in report["pass_fail"].items():
        lines.append(
            f"- {model}: global R@10 rel={values['relative_global_recall_at_10']:.3f}, "
            f"hard R@10 rel={values['relative_hard_recall_at_10']:.3f}, "
            f"MRR rel={values['relative_global_mrr_at_10']:.3f}, "
            f"runtime ratio={values['runtime_ratio_vs_nomic']:.2f}"
        )
    lines.extend(["", "## Qualitative Notes", ""])
    if report["qualitative_examples"]:
        for ex in report["qualitative_examples"][:12]:
            lines.append(
                f"- {ex['direction']} {ex['model']} on {ex['page_slug']}: "
                f"nomic rank {ex['nomic_global_rank']} vs qwen rank {ex['qwen_global_rank']} — "
                f"{ex['claim']} / {ex['evidence_title']}"
            )
    else:
        lines.append("- No large rank swings found under the configured qualitative threshold.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=200)
    parser.add_argument("--models", nargs="+", default=["nomic", "qwen06", "qwen4b"])
    parser.add_argument("--json-out", default="")
    parser.add_argument("--md-out", default="/Users/duhokim/.openclaw/workspace/Report_Embeddings_AB_Phase1_2026-05-23.md")
    args = parser.parse_args()

    started = time.perf_counter()
    stamp = now_stamp()
    json_out = Path(args.json_out or f"/Users/duhokim/NebulaMind/logs/embedding_ab_phase1_{stamp}.json")
    json_out.parent.mkdir(parents=True, exist_ok=True)

    preflight = run_preflight()
    print(json.dumps({"event": "preflight_done", "preflight": preflight}), flush=True)
    shadow = create_shadow_table()
    print(json.dumps({"event": "shadow_table_done", "shadow_table": shadow}), flush=True)
    pairs, eval_meta = fetch_eval_pairs(limit=args.limit)
    hard_scope, doc_texts = fetch_hard_negative_docs(pairs)
    hard_counts = [len(v) for v in hard_scope.values()]
    eval_meta["hard_negative"] = {
        "queries": len(hard_counts),
        "min": min(hard_counts) if hard_counts else 0,
        "median": float(np.median(hard_counts)) if hard_counts else 0,
        "max": max(hard_counts) if hard_counts else 0,
        "unique_docs_embedded": len(doc_texts),
    }
    print(json.dumps({"event": "eval_set_done", "eval_set": eval_meta}), flush=True)

    query_vectors, doc_vectors, timings = embed_corpus(pairs, doc_texts, args.models)
    print(json.dumps({"event": "harness_embeddings_done", "timings": timings}), flush=True)
    metrics, qualitative = score(pairs, hard_scope, query_vectors, doc_vectors, args.models)
    verdicts = pass_fail(metrics, timings)

    report = {
        "generated_at": dt.datetime.now().isoformat(),
        "elapsed_seconds": time.perf_counter() - started,
        "preflight": preflight,
        "shadow_table": shadow,
        "eval_set": eval_meta,
        "models": {k: MODELS[k] for k in args.models},
        "timings": timings,
        "metrics": metrics,
        "pass_fail": verdicts,
        "qualitative_examples": qualitative,
    }
    json_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    md_out = Path(args.md_out)
    write_markdown(report, md_out)
    print(json.dumps({"event": "report_done", "json_out": str(json_out), "md_out": str(md_out)}), flush=True)


if __name__ == "__main__":
    main()
