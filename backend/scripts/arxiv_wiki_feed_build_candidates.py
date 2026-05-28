#!/usr/bin/env python3
"""Build shadow arXiv -> claim candidates for a wiki page."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from sqlalchemy import text

from arxiv_wiki_feed_common import (
    artifact_dir,
    arxiv_url,
    bm25_score,
    build_idf,
    claim_key_overlap,
    clean_arxiv_id,
    code_version,
    cosine,
    db_engine,
    load_page_scope,
    paper_year,
    run_key,
    tfidf,
    tokenize,
    write_json,
    write_jsonl,
)


def build_candidates(args: argparse.Namespace) -> tuple[str, list[dict], dict]:
    scope = load_page_scope(args.page_slug, args.min_abstract_chars)
    page = scope["page"]
    claims = scope["claims"]
    papers = scope["papers"]
    duplicates = scope["duplicates"]

    claim_tokens = {c["id"]: tokenize(c["text"]) for c in claims}
    paper_tokens = {
        p["id"]: tokenize(" ".join([p.get("title") or "", p.get("abstract") or ""]))
        for p in papers
    }
    all_docs = list(claim_tokens.values()) + list(paper_tokens.values())
    idf = build_idf(all_docs)
    avg_claim_len = sum(len(v) for v in claim_tokens.values()) / max(1, len(claim_tokens))
    claim_vecs = {cid: tfidf(tokens, idf) for cid, tokens in claim_tokens.items()}
    paper_vecs = {pid: tfidf(tokens, idf) for pid, tokens in paper_tokens.items()}

    candidates_by_key: dict[tuple[int, str], dict] = {}
    per_claim_scores: dict[int, list[dict]] = defaultdict(list)

    for paper in papers:
        paper_id = paper["id"]
        clean_id = clean_arxiv_id(paper["arxiv_id"])
        if not clean_id:
            continue
        p_tokens = paper_tokens[paper_id]
        p_token_set = set(p_tokens)
        scored: list[dict] = []
        for claim in claims:
            c_tokens = claim_tokens[claim["id"]]
            overlap, matched = claim_key_overlap(c_tokens, p_token_set)
            if overlap < args.min_overlap:
                continue
            tfidf_score = cosine(paper_vecs[paper_id], claim_vecs[claim["id"]])
            bm25 = bm25_score(p_tokens, c_tokens, idf, avg_claim_len)
            row = {
                "claim": claim,
                "paper": paper,
                "bm25_score": round(bm25, 6),
                "tfidf_score": round(tfidf_score, 6),
                "claim_key_overlap": round(overlap, 6),
                "matched_terms": matched,
            }
            scored.append(row)
            per_claim_scores[claim["id"]].append(row)

        scored.sort(key=lambda r: (r["bm25_score"], r["tfidf_score"], r["claim_key_overlap"]), reverse=True)
        for rank, item in enumerate(scored[: args.top_k_per_paper], start=1):
            key = (item["claim"]["id"], clean_id)
            candidates_by_key[key] = make_candidate(page, item, rank, "related_pages_bm25", duplicates)

    existing_by_claim = defaultdict(int)
    for claim_id, _arxiv_id in candidates_by_key:
        existing_by_claim[claim_id] += 1

    for claim in claims:
        claim_id = claim["id"]
        if existing_by_claim[claim_id] >= args.reciprocal_k:
            continue
        scored = per_claim_scores.get(claim_id, [])
        scored.sort(key=lambda r: (r["bm25_score"], r["tfidf_score"], r["claim_key_overlap"]), reverse=True)
        for rank, item in enumerate(scored[: args.reciprocal_k], start=1):
            clean_id = clean_arxiv_id(item["paper"]["arxiv_id"])
            key = (claim_id, clean_id)
            if key not in candidates_by_key:
                candidates_by_key[key] = make_candidate(page, item, rank, "reciprocal_claim_topk", duplicates)

    candidates = list(candidates_by_key.values())
    candidates.sort(key=lambda r: (r["bm25_score"], r["tfidf_score"], r["claim_key_overlap"]), reverse=True)
    if args.max_candidates:
        candidates = candidates[: args.max_candidates]
    for idx, row in enumerate(candidates, start=1):
        row["global_rank"] = idx

    key = args.run_key or run_key(args.page_slug)
    meta = {
        "run_key": key,
        "page": page,
        "dry_run": args.dry_run,
        "code_version": code_version(),
        "params": {
            "top_k_per_paper": args.top_k_per_paper,
            "reciprocal_k": args.reciprocal_k,
            "min_abstract_chars": args.min_abstract_chars,
            "min_overlap": args.min_overlap,
            "max_candidates": args.max_candidates,
        },
        "counts": {
            "page_claims": len(claims),
            "eligible_papers": len(papers),
            "candidate_pairs": len(candidates),
            "distinct_claims": len({r["claim_id"] for r in candidates}),
            "duplicate_existing": sum(1 for r in candidates if r.get("duplicate_evidence_id")),
        },
    }
    return key, candidates, meta


def make_candidate(page: dict, item: dict, rank: int, source: str, duplicates: dict) -> dict:
    claim = item["claim"]
    paper = item["paper"]
    clean_id = clean_arxiv_id(paper["arxiv_id"])
    duplicate_id = duplicates.get((claim["id"], clean_id))
    status = "duplicate_existing" if duplicate_id else "shadow_proposed"
    return {
        "run_id": None,
        "page_id": page["id"],
        "page_slug": page["slug"],
        "claim_id": claim["id"],
        "claim_text_snapshot": claim["text"],
        "claim_section_snapshot": claim.get("section"),
        "arxiv_paper_id": paper["id"],
        "arxiv_id": clean_id,
        "paper_title_snapshot": paper["title"],
        "paper_abstract_snapshot": paper["abstract"],
        "paper_authors_snapshot": paper.get("authors"),
        "paper_year": paper_year(paper.get("submitted")),
        "paper_url": arxiv_url(clean_id, paper.get("url")),
        "candidate_rank": rank,
        "bm25_score": item["bm25_score"],
        "tfidf_score": item["tfidf_score"],
        "claim_key_overlap": item["claim_key_overlap"],
        "matched_terms": item["matched_terms"],
        "candidate_source": source,
        "status": status,
        "duplicate_evidence_id": duplicate_id,
    }


def write_shadow_rows(run_key_value: str, candidates: list[dict], meta: dict) -> int:
    engine = db_engine()
    with engine.begin() as conn:
        run_id = conn.execute(
            text(
                """
                INSERT INTO arxiv_wiki_feed_runs
                    (run_key, page_id, page_slug, run_scope, paper_query,
                     candidate_params, status, created_by, code_version, notes)
                VALUES
                    (:run_key, :page_id, :page_slug, 'single_page', CAST(:paper_query AS jsonb),
                     CAST(:candidate_params AS jsonb), 'started', 'tori', :code_version, :notes)
                RETURNING id
                """
            ),
            {
                "run_key": run_key_value,
                "page_id": meta["page"]["id"],
                "page_slug": meta["page"]["slug"],
                "paper_query": json.dumps({"related_pages": meta["page"]["slug"], "min_abstract_chars": meta["params"]["min_abstract_chars"]}),
                "candidate_params": json.dumps(meta["params"]),
                "code_version": meta["code_version"],
                "notes": "arxiv wiki feed v1 candidate build",
            },
        ).scalar_one()
        for row in candidates:
            row["run_id"] = run_id
            conn.execute(
                text(
                    """
                    INSERT INTO arxiv_wiki_evidence_candidates
                        (run_id, page_id, page_slug, claim_id, claim_text_snapshot,
                         claim_section_snapshot, arxiv_paper_id, arxiv_id, paper_title_snapshot,
                         paper_abstract_snapshot, paper_authors_snapshot, paper_year, paper_url,
                         candidate_rank, bm25_score, tfidf_score, claim_key_overlap,
                         matched_terms, candidate_source, status, duplicate_evidence_id)
                    VALUES
                        (:run_id, :page_id, :page_slug, :claim_id, :claim_text_snapshot,
                         :claim_section_snapshot, :arxiv_paper_id, :arxiv_id, :paper_title_snapshot,
                         :paper_abstract_snapshot, :paper_authors_snapshot, :paper_year, :paper_url,
                         :candidate_rank, :bm25_score, :tfidf_score, :claim_key_overlap,
                         CAST(:matched_terms AS jsonb), :candidate_source, :status, :duplicate_evidence_id)
                    ON CONFLICT (run_id, claim_id, arxiv_id) DO NOTHING
                    """
                ),
                {**row, "matched_terms": json.dumps(row["matched_terms"])},
            )
        conn.execute(
            text("UPDATE arxiv_wiki_feed_runs SET status='candidates_built' WHERE id=:run_id"),
            {"run_id": run_id},
        )
    return int(run_id)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--page-slug", required=True)
    parser.add_argument("--dry-run", action="store_true", help="write artifacts only; no DB shadow writes")
    parser.add_argument("--run-key")
    parser.add_argument("--top-k-per-paper", type=int, default=5)
    parser.add_argument("--reciprocal-k", type=int, default=3)
    parser.add_argument("--min-abstract-chars", type=int, default=300)
    parser.add_argument("--min-overlap", type=float, default=0.10)
    parser.add_argument("--max-candidates", type=int, default=0)
    args = parser.parse_args()

    key, candidates, meta = build_candidates(args)
    out_dir = artifact_dir(key)
    if not args.dry_run:
        meta["run_id"] = write_shadow_rows(key, candidates, meta)
        for row in candidates:
            row["run_id"] = meta["run_id"]
    else:
        meta["run_id"] = None

    candidates_path = out_dir / "candidates.jsonl"
    meta_path = out_dir / "build_candidates_meta.json"
    write_jsonl(candidates_path, candidates)
    write_json(meta_path, meta)

    print(json.dumps({"run_key": key, "candidates_path": str(candidates_path), "meta_path": str(meta_path), **meta["counts"]}, indent=2))


if __name__ == "__main__":
    main()
