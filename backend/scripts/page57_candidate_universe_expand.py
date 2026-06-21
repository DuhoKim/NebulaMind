#!/usr/bin/env python3
"""Page 57 artifact-only candidate-universe expansion.

This script is Mode-1 safe: it reads the NebulaMind DB for claims, papers, and
existing candidate IDs, but writes only OpenClaw workspace artifacts. It never
inserts evidence candidates, Evidence rows, or promoter/apply state.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import math
import re
import sys
import time
from pathlib import Path
from typing import Any

from sqlalchemy import text

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from app.database import SessionLocal
from scripts.candidate_grounded_atom_backfill import (
    ATOM_MODEL,
    coverage_row,
    deterministic_anchors,
    semantic_support_features,
    sha_text,
    tokenize,
)
from scripts.page57_selection_atomization_recovery import (
    valid_ready,
    write_json,
    write_jsonl,
)
from scripts.arxiv_wiki_feed_v2_validate_elements import build_targeted_pairs_from_coverage_ready


PAGE_ID = 57
PAGE_SLUG = "galaxy-evolution"
ARTIFACT_ROOT = Path("/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2")
DEFAULT_SOURCE_ARTIFACT = (
    ARTIFACT_ROOT / "page57_selection_atomization_recovery_20260615T050418Z"
)
DEFAULT_ELEMENTS_PATH = DEFAULT_SOURCE_ARTIFACT / "atomization_manifest" / "elements_merged.jsonl"
DEFAULT_PREVIOUS_READY_PATH = DEFAULT_SOURCE_ARTIFACT / "validator_ready_rows_deduped.jsonl"
DEFAULT_APPROVED_CANDIDATE_UNIVERSE_ARTIFACT = (
    ARTIFACT_ROOT / "page57_candidate_universe_expand_20260615T061050Z"
)

ASTRO_TERMS = {
    "agn",
    "black",
    "bulge",
    "cluster",
    "clusters",
    "cosmic",
    "dark",
    "dwarf",
    "elliptical",
    "galaxies",
    "galaxy",
    "gas",
    "halo",
    "halos",
    "metallicity",
    "morphology",
    "quenching",
    "redshift",
    "spiral",
    "stellar",
    "starburst",
}
NUMBER_RE = re.compile(r"(?<![a-z0-9])(?:[<>~=]*\s*)?\d+(?:\.\d+)?(?:\s*[x×]\s*10\^?-?\d+)?", re.I)


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def clean_arxiv_id(value: Any) -> str:
    raw = str(value or "").strip()
    return raw.replace("oai:arXiv.org:", "").replace("arXiv:", "")


def paper_year(submitted: Any) -> int | None:
    match = re.search(r"(19|20)\d{2}", str(submitted or ""))
    return int(match.group(0)) if match else None


def extract_numbers(text_value: Any) -> set[str]:
    if not isinstance(text_value, str):
        text_value = json.dumps(text_value, ensure_ascii=False) if text_value is not None else ""
    return {re.sub(r"\s+", "", value.lower()) for value in NUMBER_RE.findall(text_value.lower())}


def load_claims(page_id: int = PAGE_ID) -> list[dict[str, Any]]:
    with SessionLocal() as db:
        rows = db.execute(
            text(
                """
                SELECT id, page_id, section, order_idx, text, trust_level, claim_type
                FROM claims
                WHERE page_id = :page_id
                ORDER BY order_idx NULLS LAST, id
                """
            ),
            {"page_id": page_id},
        ).mappings().all()
    return [dict(row) for row in rows]


def load_old_candidate_rows(page_id: int = PAGE_ID) -> list[dict[str, Any]]:
    with SessionLocal() as db:
        rows = db.execute(
            text(
                """
                SELECT id, run_id, claim_id, arxiv_id, arxiv_paper_id,
                       claim_text_snapshot, claim_section_snapshot,
                       paper_title_snapshot, paper_abstract_snapshot,
                       paper_authors_snapshot, paper_year, paper_url,
                       candidate_rank, bm25_score, tfidf_score,
                       claim_key_overlap, matched_terms, candidate_source,
                       status, duplicate_evidence_id
                FROM arxiv_wiki_evidence_candidates
                WHERE page_id = :page_id
                ORDER BY run_id, id
                """
            ),
            {"page_id": page_id},
        ).mappings().all()
    return [dict(row) for row in rows]


def load_source_papers(min_abstract_chars: int, limit: int | None = None) -> list[dict[str, Any]]:
    sql_limit = "LIMIT :limit_value" if limit else ""
    params: dict[str, Any] = {"min_abstract_chars": min_abstract_chars}
    if limit:
        params["limit_value"] = limit
    with SessionLocal() as db:
        rows = db.execute(
            text(
                f"""
                SELECT id, arxiv_id, title, authors, abstract, abstract_summary,
                       category, submitted, url, related_pages
                FROM arxiv_papers
                WHERE arxiv_id IS NOT NULL
                  AND title IS NOT NULL
                  AND length(coalesce(abstract, '')) >= :min_abstract_chars
                ORDER BY id
                {sql_limit}
                """
            ),
            params,
        ).mappings().all()
    return [dict(row) for row in rows]


def paper_tier(paper: dict[str, Any], old_arxiv_ids: set[str]) -> str:
    arxiv_id = clean_arxiv_id(paper.get("arxiv_id"))
    if arxiv_id in old_arxiv_ids:
        return "old_page57_candidate"
    related = str(paper.get("related_pages") or "").lower()
    if PAGE_SLUG in related or "galaxy" in related:
        return "related_pages_galaxy"
    category = str(paper.get("category") or "")
    if category == "astro-ph.GA":
        return "astro_ph_ga"
    blob_terms = tokenize(" ".join([str(paper.get("title") or ""), str(paper.get("abstract") or "")]))
    if blob_terms & ASTRO_TERMS:
        return "astro_lexical"
    return "eligible_arxiv_background"


def prepare_source_paper_pool(
    papers: list[dict[str, Any]],
    old_arxiv_ids: set[str],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    seen_ids: set[str] = set()
    pool: list[dict[str, Any]] = []
    for paper in papers:
        arxiv_id = clean_arxiv_id(paper.get("arxiv_id"))
        if not arxiv_id or arxiv_id in seen_ids:
            continue
        seen_ids.add(arxiv_id)
        title = str(paper.get("title") or "").strip()
        abstract = str(paper.get("abstract") or paper.get("abstract_summary") or "").strip()
        category = paper.get("category")
        tier = paper_tier(paper, old_arxiv_ids)
        pool.append(
            {
                "arxiv_paper_id": paper.get("id"),
                "arxiv_id": arxiv_id,
                "paper_title_snapshot": title,
                "paper_abstract_snapshot": abstract,
                "paper_authors_snapshot": paper.get("authors"),
                "paper_year": paper_year(paper.get("submitted")),
                "paper_url": f"https://arxiv.org/abs/{arxiv_id}",
                "category": category,
                "related_pages": paper.get("related_pages"),
                "source_paper_tier": tier,
                "old_db_candidate_arxiv": arxiv_id in old_arxiv_ids,
            }
        )
    tier_order = {
        "old_page57_candidate": 0,
        "related_pages_galaxy": 1,
        "astro_ph_ga": 2,
        "astro_lexical": 3,
        "eligible_arxiv_background": 4,
    }
    pool.sort(key=lambda row: (tier_order.get(row["source_paper_tier"], 9), row["arxiv_paper_id"] or 0))
    summary = {
        "source_paper_pool": len(pool),
        "distinct_arxiv_ids": len({row["arxiv_id"] for row in pool}),
        "old_db_arxiv_ids_in_pool": sum(1 for row in pool if row["old_db_candidate_arxiv"]),
        "new_arxiv_ids_vs_db": len({row["arxiv_id"] for row in pool} - old_arxiv_ids),
        "source_paper_tier_counts": dict(collections.Counter(row["source_paper_tier"] for row in pool)),
    }
    return pool, summary


def idf_for_docs(docs: list[set[str]]) -> dict[str, float]:
    doc_count = max(1, len(docs))
    df: collections.Counter[str] = collections.Counter()
    for doc in docs:
        df.update(doc)
    return {term: math.log((doc_count + 1) / (count + 0.5)) + 1.0 for term, count in df.items()}


def score_element_paper(
    element: dict[str, Any],
    claim: dict[str, Any],
    paper: dict[str, Any],
    *,
    element_terms: set[str],
    claim_terms: set[str],
    paper_terms: set[str],
    element_numbers: set[str],
    paper_numbers: set[str],
    idf: dict[str, float],
) -> dict[str, Any] | None:
    element_matches = element_terms & paper_terms
    claim_matches = claim_terms & paper_terms
    number_matches = element_numbers & paper_numbers
    if not (element_matches or claim_matches or number_matches):
        return None
    element_overlap = len(element_matches) / max(1, len(element_terms))
    claim_overlap = len(claim_matches) / max(1, len(claim_terms))
    idf_boost = sum(idf.get(term, 1.0) for term in element_matches) / max(1, len(element_terms))
    score = (
        2.2 * element_overlap
        + 0.55 * claim_overlap
        + 0.22 * min(1, len(number_matches))
        + 0.11 * min(1.0, idf_boost / 3.0)
        + (0.05 if not paper["old_db_candidate_arxiv"] else 0.0)
    )
    if element_matches & ASTRO_TERMS:
        score += 0.05
    return {
        "expansion_score": round(score, 6),
        "element_key_overlap": round(element_overlap, 6),
        "claim_key_overlap": round(claim_overlap, 6),
        "matched_terms": sorted(claim_matches)[:40],
        "element_matched_terms": sorted(element_matches)[:40],
        "element_matched_numbers": sorted(number_matches),
    }


def candidate_key_for(claim_id: int, element_id: str, arxiv_id: str) -> str:
    return sha_text(
        {
            "mode": "page57_candidate_universe_expand_v1",
            "claim_id": claim_id,
            "element_id": element_id,
            "arxiv_id": arxiv_id,
        }
    )


def build_candidate_universe(
    claims: list[dict[str, Any]],
    elements: list[dict[str, Any]],
    source_papers: list[dict[str, Any]],
    *,
    top_k_per_element: int,
    min_rows_per_claim: int,
) -> list[dict[str, Any]]:
    claims_by_id = {int(row["id"]): row for row in claims}
    paper_term_sets = {
        row["arxiv_id"]: tokenize(" ".join([row["paper_title_snapshot"], row["paper_abstract_snapshot"]]))
        for row in source_papers
    }
    paper_number_sets = {
        row["arxiv_id"]: extract_numbers(" ".join([row["paper_title_snapshot"], row["paper_abstract_snapshot"]]))
        for row in source_papers
    }
    idf = idf_for_docs(list(paper_term_sets.values()))
    rows_by_key: dict[tuple[int, str, str], dict[str, Any]] = {}
    per_claim_counts: collections.Counter[int] = collections.Counter()

    for index, element in enumerate(elements, 1):
        claim_id = int(element["claim_id"])
        claim = claims_by_id.get(claim_id)
        if not claim:
            continue
        element_text = str(element.get("text") or element.get("element_text") or "").strip()
        element_blob = " ".join(
            [
                element_text,
                json.dumps(element.get("normalized_subject"), ensure_ascii=False)
                if element.get("normalized_subject") is not None
                else "",
                json.dumps(element.get("normalized_mechanism"), ensure_ascii=False)
                if element.get("normalized_mechanism") is not None
                else "",
                json.dumps(element.get("quantity_or_range"), ensure_ascii=False)
                if element.get("quantity_or_range") is not None
                else "",
                json.dumps(element.get("redshift_or_environment"), ensure_ascii=False)
                if element.get("redshift_or_environment") is not None
                else "",
            ]
        )
        element_terms = tokenize(element_blob)
        element_numbers = extract_numbers(element_blob)
        claim_terms = tokenize(claim.get("text"))
        scored: list[dict[str, Any]] = []
        for paper in source_papers:
            arxiv_id = paper["arxiv_id"]
            features = score_element_paper(
                element,
                claim,
                paper,
                element_terms=element_terms,
                claim_terms=claim_terms,
                paper_terms=paper_term_sets[arxiv_id],
                element_numbers=element_numbers,
                paper_numbers=paper_number_sets[arxiv_id],
                idf=idf,
            )
            if not features:
                continue
            row = {
                "candidate_key": candidate_key_for(claim_id, str(element["element_id"]), arxiv_id),
                "retrieval_filter_run_id": 0,
                "page_id": PAGE_ID,
                "page_slug": PAGE_SLUG,
                "claim_id": claim_id,
                "element_id": element["element_id"],
                "element_index": int(element.get("element_index") or 0),
                "element_type": element.get("element_type"),
                "element_text": element_text,
                "required": bool(element.get("required")),
                "normalized_subject": element.get("normalized_subject"),
                "normalized_mechanism": element.get("normalized_mechanism"),
                "quantity_or_range": element.get("quantity_or_range"),
                "redshift_or_environment": element.get("redshift_or_environment"),
                "section": element.get("section") or claim.get("section"),
                "claim_text_snapshot": claim.get("text"),
                "claim_trust_level": claim.get("trust_level"),
                "claim_type": claim.get("claim_type"),
                "source_element_artifact": element.get("source_artifact"),
                "arxiv_id": arxiv_id,
                "arxiv_paper_id": paper.get("arxiv_paper_id"),
                "paper_title_snapshot": paper.get("paper_title_snapshot"),
                "paper_abstract_snapshot": paper.get("paper_abstract_snapshot"),
                "paper_authors_snapshot": paper.get("paper_authors_snapshot"),
                "paper_year": paper.get("paper_year"),
                "paper_url": paper.get("paper_url"),
                "paper_category": paper.get("category"),
                "source_paper_tier": paper.get("source_paper_tier"),
                "old_db_candidate_arxiv": bool(paper.get("old_db_candidate_arxiv")),
                "candidate_source": "page57_candidate_universe_expand_v1",
                "candidate_status": "artifact_only_expanded",
                "hydration_db_reads_used": False,
                "hydration_policy": "artifact_only_fail_closed",
                **features,
            }
            scored.append(row)
        scored.sort(
            key=lambda row: (
                float(row["expansion_score"]),
                float(row["element_key_overlap"]),
                not bool(row["old_db_candidate_arxiv"]),
                str(row["arxiv_id"]),
            ),
            reverse=True,
        )
        for row in scored[:top_k_per_element]:
            key = (int(row["claim_id"]), str(row["element_id"]), str(row["arxiv_id"]))
            rows_by_key[key] = row
            per_claim_counts[int(row["claim_id"])] += 1
        if index % 100 == 0 or index == len(elements):
            print(
                json.dumps(
                    {
                        "candidate_universe_elements_scored": index,
                        "elements_total": len(elements),
                        "candidate_rows": len(rows_by_key),
                    },
                    sort_keys=True,
                ),
                flush=True,
            )

    if min_rows_per_claim:
        by_claim_candidates: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
        for row in rows_by_key.values():
            by_claim_candidates[int(row["claim_id"])].append(row)
        for claim_id in sorted(claims_by_id):
            if len(by_claim_candidates.get(claim_id, [])) >= min_rows_per_claim:
                continue
            claim_elements = [row for row in elements if int(row["claim_id"]) == claim_id]
            for element in claim_elements:
                element_id = str(element["element_id"])
                existing_arxiv = {
                    key[2]
                    for key in rows_by_key
                    if key[0] == claim_id and key[1] == element_id
                }
                claim_rows = [
                    row
                    for row in rows_by_key.values()
                    if int(row["claim_id"]) == claim_id and str(row["arxiv_id"]) not in existing_arxiv
                ]
                claim_rows.sort(key=lambda row: float(row.get("expansion_score") or 0.0), reverse=True)
                for source_row in claim_rows[: max(0, min_rows_per_claim - len(by_claim_candidates.get(claim_id, [])))]:
                    cloned = dict(source_row)
                    cloned["element_id"] = element_id
                    cloned["element_index"] = int(element.get("element_index") or 0)
                    cloned["element_type"] = element.get("element_type")
                    cloned["element_text"] = str(element.get("text") or element.get("element_text") or "").strip()
                    cloned["candidate_key"] = candidate_key_for(claim_id, element_id, str(cloned["arxiv_id"]))
                    key = (claim_id, element_id, str(cloned["arxiv_id"]))
                    rows_by_key[key] = cloned
                    by_claim_candidates[claim_id].append(cloned)
                    if len(by_claim_candidates[claim_id]) >= min_rows_per_claim:
                        break
                if len(by_claim_candidates.get(claim_id, [])) >= min_rows_per_claim:
                    break

    rows = list(rows_by_key.values())
    rows.sort(
        key=lambda row: (
            int(row["claim_id"]),
            int(row.get("element_index") or 0),
            -float(row.get("expansion_score") or 0.0),
            str(row.get("arxiv_id") or ""),
        )
    )
    for rank, row in enumerate(rows, 1):
        row["candidate_universe_rank"] = rank
    return rows


def summarize_candidate_universe(rows: list[dict[str, Any]], old_arxiv_ids: set[str], source_summary: dict[str, Any]) -> dict[str, Any]:
    by_claim = collections.Counter(int(row["claim_id"]) for row in rows)
    arxiv_ids = {str(row["arxiv_id"]) for row in rows}
    return {
        **source_summary,
        "candidate_rows": len(rows),
        "distinct_claims_with_candidates": len(by_claim),
        "claims_with_ge5_candidate_rows": sum(1 for count in by_claim.values() if count >= 5),
        "distinct_candidate_arxiv_ids": len(arxiv_ids),
        "new_candidate_arxiv_ids_vs_db": len(arxiv_ids - old_arxiv_ids),
        "old_db_candidate_arxiv_ids_present": len(arxiv_ids & old_arxiv_ids),
        "candidate_source_counts": dict(collections.Counter(row.get("source_paper_tier") for row in rows)),
        "old_db_candidate_rows_in_universe": sum(1 for row in rows if row.get("old_db_candidate_arxiv")),
    }


def phase_a_gate(summary: dict[str, Any], *, source_pool_db_ceiling_documented: bool = False) -> list[str]:
    failures: list[str] = []
    if summary["source_paper_pool"] < 600 and not source_pool_db_ceiling_documented:
        failures.append("source_paper_pool_lt_600")
    if summary["candidate_rows"] < 12000:
        failures.append("candidate_rows_lt_12000")
    if summary["distinct_claims_with_candidates"] < 475:
        failures.append("distinct_claims_with_candidates_lt_475")
    if summary["claims_with_ge5_candidate_rows"] < 350:
        failures.append("claims_with_ge5_candidate_rows_lt_350")
    if summary["distinct_candidate_arxiv_ids"] < 500:
        failures.append("distinct_candidate_arxiv_ids_lt_500")
    if summary["new_candidate_arxiv_ids_vs_db"] < 300:
        failures.append("new_candidate_arxiv_ids_vs_db_lt_300")
    return failures


def row_quality_score(row: dict[str, Any]) -> float:
    anchors = row.get("deterministic_anchors") or {}
    terms = len(anchors.get("term_overlap") or [])
    numbers = len(anchors.get("number_overlap") or [])
    token_count = max(1, int(anchors.get("element_token_count") or 1))
    try:
        semantic = float(row.get("semantic_similarity") or 0.0)
    except (TypeError, ValueError):
        semantic = 0.0
    return round(
        float(row.get("expansion_score") or 0.0)
        + terms / token_count
        + 0.18 * min(1.0, numbers)
        + 0.35 * semantic
        + (0.08 if not row.get("old_db_candidate_arxiv") else 0.0),
        6,
    )


def order_selected_rows(rows: list[dict[str, Any]], previous_ready_claims: set[int]) -> list[dict[str, Any]]:
    def sort_key(row: dict[str, Any]) -> tuple[Any, ...]:
        return (
            int(row["claim_id"]) in previous_ready_claims,
            -float(row.get("selection_rank_score") or 0.0),
            -float(row.get("semantic_similarity") or 0.0),
            bool(row.get("old_db_candidate_arxiv")),
            str(row.get("arxiv_id") or ""),
            str(row.get("element_id") or ""),
        )

    by_claim: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
    for row in rows:
        by_claim[int(row["claim_id"])].append(row)
    for claim_rows in by_claim.values():
        claim_rows.sort(key=sort_key)
    claim_order = sorted(
        by_claim,
        key=lambda claim_id: (
            claim_id in previous_ready_claims,
            sort_key(by_claim[claim_id][0]),
            claim_id,
        ),
    )
    ordered: list[dict[str, Any]] = []
    depth = 0
    while True:
        added = False
        for claim_id in claim_order:
            claim_rows = by_claim[claim_id]
            if depth >= len(claim_rows):
                continue
            ordered.append({**claim_rows[depth], "selection_order_depth": depth + 1})
            added = True
        if not added:
            break
        depth += 1
    return ordered


def preflight_split(
    rows: list[dict[str, Any]],
    *,
    semantic_threshold: float,
    ollama_host: str,
    compute_semantic: bool,
    previous_ready_claims: set[int],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    selected: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    embedding_cache: dict[str, list[float]] = {}
    started = time.time()
    for index, source in enumerate(rows, 1):
        row = dict(source)
        if str(row.get("candidate_status") or "").lower() == "off_domain" or str(row.get("source_label") or "").lower() == "off_domain":
            row["selection_status"] = "excluded_off_domain"
            excluded.append(row)
            continue
        if str(row.get("retrieval_filter_decision") or "").lower() == "boundary_review_keep":
            row["selection_status"] = "audit_only_boundary_review_keep"
            excluded.append(row)
            continue
        anchors = deterministic_anchors(row)
        row["deterministic_anchors"] = anchors
        if not anchors.get("has_anchor_overlap"):
            row["selection_status"] = "excluded_anchor_overlap_missing"
            row["selection_rank_score"] = row_quality_score(row)
            excluded.append(row)
            continue
        if compute_semantic:
            row.update(semantic_support_features(row, semantic_threshold, ollama_host, embedding_cache))
            if row.get("coverage_candidate") is False:
                row["selection_status"] = "excluded_semantic_unsupported"
                row["selection_rank_score"] = row_quality_score(row)
                excluded.append(row)
                continue
        else:
            row.update(
                {
                    "coverage_candidate": None,
                    "semantic_similarity": None,
                    "semantic_similarity_threshold": semantic_threshold,
                    "semantic_support_status": "not_computed",
                    "semantic_support_error": None,
                }
            )
        entailment_decision = str(row.get("entailment_gate_decision") or "").lower()
        if entailment_decision == "no":
            row["selection_status"] = "excluded_entailment_rejected"
            row["selection_rank_score"] = row_quality_score(row)
            excluded.append(row)
            continue
        if entailment_decision == "error":
            row["selection_status"] = "excluded_entailment_error"
            row["selection_rank_score"] = row_quality_score(row)
            excluded.append(row)
            continue
        row["selection_status"] = "selected_for_atom_coverage"
        row["selection_rank_score"] = row_quality_score(row)
        selected.append(row)
        if index % 1000 == 0 or index == len(rows):
            print(
                json.dumps(
                    {
                        "preflight_rows": index,
                        "total_rows": len(rows),
                        "selected": len(selected),
                        "excluded": len(excluded),
                        "elapsed_seconds": round(time.time() - started, 1),
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
    return order_selected_rows(selected, previous_ready_claims), excluded


def summarize_preflight(selected: list[dict[str, Any]], excluded: list[dict[str, Any]], semantic_threshold: float, compute_semantic: bool) -> dict[str, Any]:
    status_counts = collections.Counter(row.get("selection_status") for row in selected + excluded)
    main_bad = [
        row
        for row in selected
        if row.get("selection_status") in {"audit_only_boundary_review_keep", "excluded_off_domain"}
    ]
    model_rows_anchor_missing = [
        row
        for row in selected
        if not (row.get("deterministic_anchors") or {}).get("has_anchor_overlap")
    ]
    return {
        "selected_queue_rows": len(selected),
        "selected_claims": len({int(row["claim_id"]) for row in selected}),
        "selected_arxiv_ids": len({str(row["arxiv_id"]) for row in selected}),
        "selection_status_counts": dict(status_counts),
        "excluded_anchor_overlap_missing": status_counts.get("excluded_anchor_overlap_missing", 0),
        "excluded_semantic_unsupported": status_counts.get("excluded_semantic_unsupported", 0),
        "excluded_entailment_rejected": status_counts.get("excluded_entailment_rejected", 0),
        "audit_only_boundary_review_keep": status_counts.get("audit_only_boundary_review_keep", 0),
        "excluded_off_domain": status_counts.get("excluded_off_domain", 0),
        "brk_or_off_domain_rows_in_main_queue": len(main_bad),
        "anchor_overlap_missing_model_rows": len(model_rows_anchor_missing),
        "anchor_overlap_missing_model_rate": round(len(model_rows_anchor_missing) / max(1, len(selected)), 6),
        "semantic_threshold": semantic_threshold,
        "semantic_computed": compute_semantic,
        "hydration_db_reads_used": False,
        "db_writes_used": False,
    }


def phase_b_gate(summary: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if summary["selected_queue_rows"] < 2500:
        failures.append("selected_queue_rows_lt_2500")
    if summary["selected_claims"] < 300:
        failures.append("selected_claims_lt_300")
    if summary["selected_arxiv_ids"] < 350:
        failures.append("selected_arxiv_ids_lt_350")
    if summary["anchor_overlap_missing_model_rows"] > 0:
        failures.append("anchor_overlap_missing_not_excluded_before_model")
    if summary["brk_or_off_domain_rows_in_main_queue"] > 0:
        failures.append("brk_or_off_domain_rows_in_main_queue")
    return failures


def previous_ready_claims(path: Path) -> set[int]:
    return {int(row["claim_id"]) for row in read_jsonl(path) if row.get("claim_id") is not None}


def choose_probe_rows(
    selected: list[dict[str, Any]],
    *,
    old_arxiv_ids: set[str],
    previous_ready: set[int],
    limit: int,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    used_keys: set[tuple[int, str, str]] = set()
    chosen: list[dict[str, Any]] = []
    buckets: collections.Counter[str] = collections.Counter()

    def key(row: dict[str, Any]) -> tuple[int, str, str]:
        return (int(row["claim_id"]), str(row["element_id"]), str(row["arxiv_id"]))

    def add(rows: list[dict[str, Any]], bucket: str, max_rows: int) -> None:
        for row in rows:
            if len(chosen) >= limit or buckets[bucket] >= max_rows:
                return
            row_key = key(row)
            if row_key in used_keys:
                continue
            chosen.append({**row, "probe_bucket": bucket})
            used_keys.add(row_key)
            buckets[bucket] += 1

    def one_per_claim(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
        by_claim: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
        for row in rows:
            by_claim[int(row["claim_id"])].append(row)
        ordered: list[dict[str, Any]] = []
        for claim_id in sorted(
            by_claim,
            key=lambda cid: (
                not any(str(row["arxiv_id"]) not in old_arxiv_ids for row in by_claim[cid]),
                -float(by_claim[cid][0].get("selection_rank_score") or 0.0),
                cid,
            ),
        ):
            by_claim[claim_id].sort(
                key=lambda row: (
                    bool(str(row["arxiv_id"]) in old_arxiv_ids),
                    -float(row.get("selection_rank_score") or 0.0),
                    -float(row.get("semantic_similarity") or 0.0),
                )
            )
            ordered.append(by_claim[claim_id][0])
        return ordered

    no_ready = [row for row in selected if int(row["claim_id"]) not in previous_ready]
    new_arxiv = [row for row in selected if str(row["arxiv_id"]) not in old_arxiv_ids]
    priority_trust = [
        row
        for row in no_ready
        if str(row.get("claim_trust_level") or "").lower() in {"accepted", "consensus", "challenged"}
    ]
    add(one_per_claim(no_ready), "no_previous_ready_claim_seed", min(320, limit))
    add(sorted(new_arxiv, key=lambda row: -float(row.get("selection_rank_score") or 0.0)), "new_arxiv_id_boost", min(160, limit))
    add(one_per_claim(priority_trust), "priority_trust_no_ready", min(100, limit))
    add(sorted(selected, key=lambda row: -float(row.get("selection_rank_score") or 0.0)), "quality_fill", limit)
    return chosen[:limit], {
        "probe_limit": limit,
        "probe_rows": len(chosen[:limit]),
        "probe_bucket_counts": dict(collections.Counter(row.get("probe_bucket") for row in chosen[:limit])),
        "probe_distinct_claims": len({int(row["claim_id"]) for row in chosen[:limit]}),
        "probe_distinct_arxiv_ids": len({str(row["arxiv_id"]) for row in chosen[:limit]}),
        "probe_new_arxiv_id_rows": sum(1 for row in chosen[:limit] if str(row["arxiv_id"]) not in old_arxiv_ids),
        "previous_ready_claims": len(previous_ready),
    }


def run_probe_coverage(
    probe_rows: list[dict[str, Any]],
    out_dir: Path,
    *,
    timeout: int,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    coverage_dir = out_dir / "coverage_probe_500"
    coverage_dir.mkdir(parents=True, exist_ok=True)
    coverage_path = coverage_dir / "coverage_rows.jsonl"
    if coverage_path.exists():
        coverage_path.unlink()
    coverage_rows: list[dict[str, Any]] = []
    started = time.time()
    with coverage_path.open("a", encoding="utf-8") as handle:
        for index, row in enumerate(probe_rows, 1):
            coverage = coverage_row(row, coverage_dir.name, ATOM_MODEL, timeout, use_model=True)
            coverage.update(
                {
                    "coverage_from_cache": False,
                    "probe_bucket": row.get("probe_bucket"),
                    "old_db_candidate_arxiv": row.get("old_db_candidate_arxiv"),
                    "selection_rank_score": row.get("selection_rank_score"),
                    "semantic_similarity": row.get("semantic_similarity"),
                    "expansion_score": row.get("expansion_score"),
                }
            )
            coverage_rows.append(coverage)
            handle.write(json.dumps(coverage, ensure_ascii=False, sort_keys=True) + "\n")
            if index % 25 == 0 or index == len(probe_rows):
                counts = collections.Counter(item.get("candidate_atom_coverage_status") for item in coverage_rows)
                print(
                    json.dumps(
                        {
                            "probe_coverage_rows": index,
                            "target": len(probe_rows),
                            "status_counts": dict(counts),
                            "elapsed_seconds": round(time.time() - started, 1),
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )
    ready_rows = [row for row in coverage_rows if valid_ready(row)]
    seen: set[tuple[Any, ...]] = set()
    deduped_ready: list[dict[str, Any]] = []
    for row in ready_rows:
        ready_key = (row.get("claim_id"), row.get("element_id"), row.get("arxiv_id"))
        if ready_key in seen:
            continue
        seen.add(ready_key)
        deduped_ready.append(row)
    write_jsonl(coverage_dir / "validator_ready_rows.jsonl", ready_rows)
    write_jsonl(coverage_dir / "validator_ready_rows_deduped.jsonl", deduped_ready)
    status_counts = collections.Counter(row.get("candidate_atom_coverage_status") for row in coverage_rows)
    summary = {
        "probe_rows": len(coverage_rows),
        "ready_rows": len(ready_rows),
        "valid_ready_rate": round(len(ready_rows) / max(1, len(coverage_rows)), 6),
        "unique_ready_tuples": len(deduped_ready),
        "distinct_ready_claims": len({int(row["claim_id"]) for row in ready_rows}),
        "ready_tuples_from_new_arxiv_ids": sum(1 for row in deduped_ready if not row.get("old_db_candidate_arxiv")),
        "retryable_rows": status_counts.get("error_retryable", 0),
        "retryable_error_rate": round(status_counts.get("error_retryable", 0) / max(1, len(coverage_rows)), 6),
        "status_counts": dict(status_counts),
        "hydration_db_reads_used": False,
        "db_reads_used_for_validator_hydration": False,
        "db_writes_used": False,
        "db_write_count": 0,
        "evidence_rows_written": 0,
        "promoter_run": False,
        "outputs": {
            "coverage_rows": str(coverage_path),
            "validator_ready_rows": str(coverage_dir / "validator_ready_rows.jsonl"),
            "validator_ready_rows_deduped": str(coverage_dir / "validator_ready_rows_deduped.jsonl"),
        },
    }
    write_json(coverage_dir / "coverage_summary.json", summary)
    return coverage_rows, summary


def phase_c_gate(summary: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if summary["valid_ready_rate"] < 0.08:
        failures.append("valid_ready_rate_lt_8pct")
    if summary["unique_ready_tuples"] < 40:
        failures.append("unique_ready_tuples_lt_40")
    if summary["distinct_ready_claims"] < 35:
        failures.append("distinct_ready_claims_lt_35")
    if summary["ready_tuples_from_new_arxiv_ids"] < 25:
        failures.append("ready_tuples_from_new_arxiv_ids_lt_25")
    if summary["retryable_error_rate"] > 0.02:
        failures.append("retryable_error_rate_gt_2pct")
    for field in ["hydration_db_reads_used", "db_reads_used_for_validator_hydration", "db_writes_used", "promoter_run"]:
        if summary.get(field):
            failures.append(f"{field}_not_false")
    if summary.get("evidence_rows_written") != 0 or summary.get("db_write_count") != 0:
        failures.append("mode1_safety_count_not_zero")
    return failures


def coverage_tuple_key(row: dict[str, Any]) -> tuple[int, str, str]:
    return (int(row["claim_id"]), str(row["element_id"]), str(row["arxiv_id"]))


def dedupe_valid_ready_rows(coverage_rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    ready_rows = [row for row in coverage_rows if valid_ready(row)]
    seen: set[tuple[int, str, str]] = set()
    deduped_ready: list[dict[str, Any]] = []
    for row in ready_rows:
        key = coverage_tuple_key(row)
        if key in seen:
            continue
        seen.add(key)
        deduped_ready.append(row)
    return ready_rows, deduped_ready


def summarize_full_coverage(coverage_rows: list[dict[str, Any]], deduped_ready: list[dict[str, Any]]) -> dict[str, Any]:
    ready_rows = [row for row in coverage_rows if valid_ready(row)]
    status_counts = collections.Counter(row.get("candidate_atom_coverage_status") for row in coverage_rows)
    return {
        "coverage_rows": len(coverage_rows),
        "valid_ready_rows": len(ready_rows),
        "valid_ready_rate": round(len(ready_rows) / max(1, len(coverage_rows)), 6),
        "unique_ready_tuples": len(deduped_ready),
        "distinct_ready_claims": len({int(row["claim_id"]) for row in ready_rows}),
        "ready_tuples_from_new_arxiv_ids": sum(1 for row in deduped_ready if not row.get("old_db_candidate_arxiv")),
        "retryable_rows": status_counts.get("error_retryable", 0),
        "retryable_error_rate": round(status_counts.get("error_retryable", 0) / max(1, len(coverage_rows)), 6),
        "status_counts": dict(status_counts),
        "hydration_db_reads_used": False,
        "db_reads_used_for_validator_hydration": False,
        "db_writes_used": False,
        "db_write_count": 0,
        "evidence_rows_written": 0,
        "promoter_run": False,
        "broad_validator_run": False,
        "db_candidate_insertion": False,
    }


def phase_d_gate(summary: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if summary["valid_ready_rows"] < 500:
        failures.append("valid_ready_rows_lt_500")
    if summary["unique_ready_tuples"] < 250:
        failures.append("unique_ready_tuples_lt_250")
    if summary["distinct_ready_claims"] < 100:
        failures.append("distinct_ready_claims_lt_100")
    if summary["ready_tuples_from_new_arxiv_ids"] < 100:
        failures.append("ready_tuples_from_new_arxiv_ids_lt_100")
    if summary["retryable_error_rate"] > 0.02:
        failures.append("retryable_error_rate_gt_2pct")
    for field in [
        "hydration_db_reads_used",
        "db_reads_used_for_validator_hydration",
        "db_writes_used",
        "promoter_run",
        "broad_validator_run",
        "db_candidate_insertion",
    ]:
        if summary.get(field):
            failures.append(f"{field}_not_false")
    if summary.get("evidence_rows_written") != 0 or summary.get("db_write_count") != 0:
        failures.append("mode1_safety_count_not_zero")
    return failures


def validator_build_pairs_gate(metrics: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if metrics.get("coverage_ready_input_rows") != metrics.get("targeted_pair_rows"):
        failures.append("coverage_ready_input_rows_ne_targeted_pair_rows")
    if metrics.get("hydration_missing_rows") != 0:
        failures.append("hydration_missing_rows_not_zero")
    if metrics.get("db_reads_used") is not False:
        failures.append("db_reads_used_not_false")
    if metrics.get("promotion_eligible") is not False:
        failures.append("promotion_eligible_not_false")
    return failures


def run_phase_d_full_coverage(args: argparse.Namespace) -> dict[str, Any]:
    approved_root = args.approved_artifact_root
    selected_path = approved_root / "coverage_selection_queue.jsonl"
    if not selected_path.exists():
        raise SystemExit(f"BLOCKED_PHASE_D_SELECTION_QUEUE_MISSING: {selected_path}")
    out_dir = args.phase_d_out_dir or approved_root / f"phase_d_full_expanded_mode1_{utc_stamp()}"
    out_dir.mkdir(parents=True, exist_ok=True)
    commands = [" ".join(sys.argv)]
    selected = read_jsonl(selected_path)
    rows_to_run = selected[: args.phase_d_limit] if args.phase_d_limit else selected
    coverage_path = out_dir / "coverage_rows.jsonl"
    existing_coverage = read_jsonl(coverage_path)
    coverage_by_tuple = {coverage_tuple_key(row): row for row in existing_coverage}

    if args.reuse_probe_coverage:
        probe_path = approved_root / "coverage_probe_500" / "coverage_rows.jsonl"
        for row in read_jsonl(probe_path):
            key = coverage_tuple_key(row)
            if key in coverage_by_tuple:
                continue
            coverage = {**row, "coverage_from_phase_c_probe_artifact": True}
            coverage_by_tuple[key] = coverage
            append_jsonl(coverage_path, coverage)

    started = time.time()
    completed_before = len(coverage_by_tuple)
    for index, row in enumerate(rows_to_run, 1):
        key = coverage_tuple_key(row)
        if key in coverage_by_tuple:
            continue
        coverage = coverage_row(row, out_dir.name, ATOM_MODEL, args.coverage_timeout, use_model=True)
        coverage.update(
            {
                "coverage_from_cache": False,
                "coverage_from_phase_c_probe_artifact": False,
                "old_db_candidate_arxiv": row.get("old_db_candidate_arxiv"),
                "selection_rank_score": row.get("selection_rank_score"),
                "semantic_similarity": row.get("semantic_similarity"),
                "expansion_score": row.get("expansion_score"),
                "hydration_db_reads_used": False,
                "hydration_policy": "artifact_only_fail_closed",
            }
        )
        coverage_by_tuple[key] = coverage
        append_jsonl(coverage_path, coverage)
        if index % 25 == 0 or index == len(rows_to_run):
            coverage_rows_so_far = list(coverage_by_tuple.values())
            ready_rows, deduped_ready = dedupe_valid_ready_rows(coverage_rows_so_far)
            counts = collections.Counter(item.get("candidate_atom_coverage_status") for item in coverage_rows_so_far)
            print(
                json.dumps(
                    {
                        "phase_d_selected_index": index,
                        "target": len(rows_to_run),
                        "coverage_rows": len(coverage_rows_so_far),
                        "valid_ready_rows": len(ready_rows),
                        "unique_ready_tuples": len(deduped_ready),
                        "distinct_ready_claims": len({int(item["claim_id"]) for item in ready_rows}),
                        "status_counts": dict(counts),
                        "elapsed_seconds": round(time.time() - started, 1),
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
        if args.phase_d_stop_after_success_gates:
            current_rows = list(coverage_by_tuple.values())
            _ready_so_far, deduped_so_far = dedupe_valid_ready_rows(current_rows)
            current_summary = summarize_full_coverage(current_rows, deduped_so_far)
            if not phase_d_gate(current_summary):
                print(
                    json.dumps(
                        {
                            "phase_d_stop_after_success_gates": True,
                            "phase_d_selected_index": index,
                            "coverage_rows": current_summary["coverage_rows"],
                            "valid_ready_rows": current_summary["valid_ready_rows"],
                            "unique_ready_tuples": current_summary["unique_ready_tuples"],
                            "distinct_ready_claims": current_summary["distinct_ready_claims"],
                            "ready_tuples_from_new_arxiv_ids": current_summary["ready_tuples_from_new_arxiv_ids"],
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )
                break

    coverage_rows = list(coverage_by_tuple.values())
    coverage_rows.sort(key=lambda row: (int(row["claim_id"]), str(row["element_id"]), str(row["arxiv_id"])))
    write_jsonl(coverage_path, coverage_rows)
    ready_rows, deduped_ready = dedupe_valid_ready_rows(coverage_rows)
    write_jsonl(out_dir / "validator_ready_rows.jsonl", ready_rows)
    write_jsonl(out_dir / "validator_ready_rows_deduped.jsonl", deduped_ready)
    coverage_summary = summarize_full_coverage(coverage_rows, deduped_ready)
    coverage_summary.update(
        {
            "approved_artifact_root": str(approved_root),
            "selection_queue_rows": len(selected),
            "phase_d_input_rows": len(rows_to_run),
            "completed_before_resume_or_probe_reuse": completed_before,
            "phase_c_probe_rows_reused": sum(1 for row in coverage_rows if row.get("coverage_from_phase_c_probe_artifact")),
            "outputs": {
                "coverage_rows": str(coverage_path),
                "validator_ready_rows": str(out_dir / "validator_ready_rows.jsonl"),
                "validator_ready_rows_deduped": str(out_dir / "validator_ready_rows_deduped.jsonl"),
            },
        }
    )
    coverage_summary["phase_d_gate_failures"] = phase_d_gate(coverage_summary)
    write_json(out_dir / "coverage_summary.json", coverage_summary)

    validator_metrics: dict[str, Any] | None = None
    validator_failures: list[str] = []
    validator_out_dir = out_dir / "validator_build_pairs_probe"
    if not coverage_summary["phase_d_gate_failures"]:
        build_targeted_pairs_from_coverage_ready(
            out_dir / "validator_ready_rows_deduped.jsonl",
            out_dir,
            validator_out_dir,
            require_hydrated=True,
        )
        validator_metrics = json.loads((validator_out_dir / "targeted_metrics.json").read_text(encoding="utf-8"))
        validator_failures = validator_build_pairs_gate(validator_metrics)
    else:
        validator_metrics = {"skipped": True, "reason": "phase_d_gate_failed"}

    summary = {
        "artifact_root": str(out_dir),
        "approved_input_artifact_root": str(approved_root),
        "created_at": dt.datetime.now(dt.UTC).isoformat(),
        "mode": "mode1_full_expanded_candidate_universe_coverage",
        "status": "ready" if not coverage_summary["phase_d_gate_failures"] and not validator_failures else "blocked",
        "changed_inputs": {
            "coverage_selection_queue": str(selected_path),
        },
        "full_run": coverage_summary,
        "validator_build_pairs_probe": validator_metrics,
        "gate_failures": coverage_summary["phase_d_gate_failures"] + validator_failures,
        "mode1_safety": {
            "evidence_rows_written": 0,
            "promoter_run": False,
            "broad_validator_run": False,
            "db_candidate_insertion": False,
            "hydration_db_reads_used": False,
            "db_reads_used_for_validator_hydration": False,
            "db_writes_used": False,
            "db_write_count": 0,
        },
        "next_step": "ready_for_broad_validator_approval",
        "outputs": {
            "coverage_rows": str(coverage_path),
            "validator_ready_rows": str(out_dir / "validator_ready_rows.jsonl"),
            "validator_ready_rows_deduped": str(out_dir / "validator_ready_rows_deduped.jsonl"),
            "coverage_summary": str(out_dir / "coverage_summary.json"),
            "validator_build_pairs_probe": str(validator_out_dir),
            "run_summary": str(out_dir / "phase_d_summary.json"),
            "run_commands": str(out_dir / "RUN_COMMANDS.md"),
            "report": str(out_dir / "REPORT.md"),
        },
    }
    if coverage_summary["phase_d_gate_failures"]:
        summary["next_step"] = "blocked_candidate_universe_expansion_not_enough_abstract_support"
    elif validator_failures:
        summary["next_step"] = "blocked_targeted_validator_build_pairs_probe"

    write_json(out_dir / "phase_d_summary.json", summary)
    phase_d_lines = [
        "# Page57 Full Expanded Mode 1",
        "",
        f"- Artifact root: `{out_dir}`",
        f"- Approved input: `{approved_root}`",
        f"- Status: `{summary['status']}`",
        f"- Next step: `{summary['next_step']}`",
        f"- Coverage rows: `{coverage_summary['coverage_rows']}`",
        f"- Valid ready rows: `{coverage_summary['valid_ready_rows']}`",
        f"- Unique ready tuples: `{coverage_summary['unique_ready_tuples']}`",
        f"- Distinct ready claims: `{coverage_summary['distinct_ready_claims']}`",
        f"- New-arXiv ready tuples: `{coverage_summary['ready_tuples_from_new_arxiv_ids']}`",
        f"- Retryable error rate: `{coverage_summary['retryable_error_rate']}`",
        "",
        "## Safety",
        "",
        "- Evidence rows written: `0`.",
        "- Promoter/apply run: `false`.",
        "- Broad validator run: `false`.",
        "- DB candidate insertion: `false`.",
        "- DB hydration reads: `false`.",
    ]
    if summary["gate_failures"]:
        phase_d_lines.extend(["", "## Gate Failures", ""])
        phase_d_lines.extend(f"- `{failure}`" for failure in summary["gate_failures"])
    (out_dir / "REPORT.md").write_text("\n".join(phase_d_lines) + "\n", encoding="utf-8")
    (out_dir / "RUN_COMMANDS.md").write_text("\n".join(f"- `{command}`" for command in commands) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    return summary


def write_run_docs(out_dir: Path, summary: dict[str, Any], commands: list[str]) -> None:
    preflight = summary.get("preflight") or {}
    probe = summary.get("probe_500") or {}
    lines = [
        "# Page57 Candidate Universe Recovery",
        "",
        f"- Artifact root: `{out_dir}`",
        f"- Status: `{summary['status']}`",
        f"- Next step: `{summary['next_step']}`",
        f"- Candidate rows: `{summary.get('candidate_universe', {}).get('candidate_rows')}`",
        f"- Distinct candidate claims: `{summary.get('candidate_universe', {}).get('distinct_claims_with_candidates')}`",
        f"- Distinct candidate arXiv IDs: `{summary.get('candidate_universe', {}).get('distinct_candidate_arxiv_ids')}`",
        f"- Selected preflight rows: `{preflight.get('selected_queue_rows')}`",
        f"- Probe rows: `{probe.get('probe_rows')}`",
        f"- Probe unique ready tuples: `{probe.get('unique_ready_tuples')}`",
        f"- Probe distinct ready claims: `{probe.get('distinct_ready_claims')}`",
        "",
        "## Safety",
        "",
        "- Evidence rows written: `0`.",
        "- Promoter/apply run: `false`.",
        "- Broad validator run: `false`.",
        "- DB candidate insertion: `false`.",
    ]
    if summary.get("gate_failures"):
        lines.extend(["", "## Gate Failures", ""])
        lines.extend(f"- `{failure}`" for failure in summary["gate_failures"])
    (out_dir / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out_dir / "RUN_COMMANDS.md").write_text("\n".join(f"- `{command}`" for command in commands) + "\n", encoding="utf-8")


def run(args: argparse.Namespace) -> dict[str, Any]:
    out_dir = args.out_dir or ARTIFACT_ROOT / f"page57_candidate_universe_expand_{utc_stamp()}"
    out_dir.mkdir(parents=True, exist_ok=True)
    commands = [" ".join(sys.argv)]
    claims = load_claims(args.page_id)
    elements = read_jsonl(args.elements_path)
    old_candidates = load_old_candidate_rows(args.page_id)
    old_arxiv_ids = {clean_arxiv_id(row.get("arxiv_id")) for row in old_candidates if clean_arxiv_id(row.get("arxiv_id"))}
    previous_ready = previous_ready_claims(args.previous_ready_path)
    raw_papers = load_source_papers(args.min_abstract_chars, args.source_paper_limit)
    source_papers, source_summary = prepare_source_paper_pool(raw_papers, old_arxiv_ids)
    write_jsonl(out_dir / "source_paper_pool.jsonl", source_papers)
    write_json(out_dir / "source_paper_pool_summary.json", source_summary)

    candidates = build_candidate_universe(
        claims,
        elements,
        source_papers,
        top_k_per_element=args.top_k_per_element,
        min_rows_per_claim=args.min_rows_per_claim,
    )
    write_jsonl(out_dir / "element_first_candidate_rows.jsonl", candidates)
    candidate_summary = summarize_candidate_universe(candidates, old_arxiv_ids, source_summary)
    candidate_summary.update(
        {
            "live_claims": len(claims),
            "atomized_elements_loaded": len(elements),
            "old_db_candidate_rows": len(old_candidates),
            "old_db_distinct_arxiv_ids": len(old_arxiv_ids),
            "phase_a_gate_failures": phase_a_gate(candidate_summary),
        }
    )
    write_json(out_dir / "candidate_universe_summary.json", candidate_summary)
    write_json(
        out_dir / "candidate_universe_deltas_vs_db.json",
        {
            "old_db_candidate_rows": len(old_candidates),
            "old_db_distinct_arxiv_ids": len(old_arxiv_ids),
            "expanded_candidate_rows": candidate_summary["candidate_rows"],
            "expanded_distinct_arxiv_ids": candidate_summary["distinct_candidate_arxiv_ids"],
            "new_candidate_arxiv_ids_vs_db": candidate_summary["new_candidate_arxiv_ids_vs_db"],
        },
    )
    write_jsonl(out_dir / "coverage_input_rows.jsonl", candidates)
    phase_a_failures = candidate_summary["phase_a_gate_failures"]
    summary: dict[str, Any] = {
        "artifact_root": str(out_dir),
        "created_at": dt.datetime.now(dt.UTC).isoformat(),
        "mode": "mode1_artifact_only_candidate_universe_recovery",
        "status": "blocked" if phase_a_failures else "running",
        "candidate_universe": candidate_summary,
        "preflight": None,
        "probe_500": None,
        "gate_failures": list(phase_a_failures),
        "mode1_safety": {
            "evidence_rows_written": 0,
            "promoter_run": False,
            "broad_validator_run": False,
            "db_candidate_insertion": False,
            "hydration_db_reads_used": False,
            "db_reads_used_for_validator_hydration": False,
            "db_writes_used": False,
            "db_write_count": 0,
        },
        "outputs": {
            "source_paper_pool": str(out_dir / "source_paper_pool.jsonl"),
            "candidate_rows": str(out_dir / "element_first_candidate_rows.jsonl"),
            "coverage_input_rows": str(out_dir / "coverage_input_rows.jsonl"),
            "coverage_selection_queue": str(out_dir / "coverage_selection_queue.jsonl"),
            "coverage_excluded_rows": str(out_dir / "coverage_excluded_rows.jsonl"),
            "report": str(out_dir / "REPORT.md"),
            "run_commands": str(out_dir / "RUN_COMMANDS.md"),
        },
    }
    if phase_a_failures:
        summary["next_step"] = "blocked_phase_a_gate"
        write_json(out_dir / "run_summary.json", summary)
        write_run_docs(out_dir, summary, commands)
        print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
        return summary

    selected, excluded = preflight_split(
        candidates,
        semantic_threshold=args.semantic_threshold,
        ollama_host=args.ollama_host,
        compute_semantic=not args.no_semantic,
        previous_ready_claims=previous_ready,
    )
    write_jsonl(out_dir / "coverage_selection_queue.jsonl", selected)
    write_jsonl(out_dir / "coverage_excluded_rows.jsonl", excluded)
    preflight_summary = summarize_preflight(selected, excluded, args.semantic_threshold, not args.no_semantic)
    preflight_summary["phase_b_gate_failures"] = phase_b_gate(preflight_summary)
    write_json(out_dir / "preflight_summary.json", preflight_summary)
    summary["preflight"] = preflight_summary
    phase_b_failures = preflight_summary["phase_b_gate_failures"]
    summary["gate_failures"].extend(phase_b_failures)
    if phase_b_failures:
        summary["status"] = "blocked"
        summary["next_step"] = "blocked_phase_b_gate"
        write_json(out_dir / "run_summary.json", summary)
        write_run_docs(out_dir, summary, commands)
        print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
        return summary

    probe_rows, probe_plan = choose_probe_rows(
        selected,
        old_arxiv_ids=old_arxiv_ids,
        previous_ready=previous_ready,
        limit=args.probe_limit,
    )
    write_jsonl(out_dir / "probe_500_input_rows.jsonl", probe_rows)
    write_json(out_dir / "probe_500_plan.json", probe_plan)
    if args.skip_phase_c:
        summary["status"] = "blocked"
        summary["next_step"] = "blocked_phase_c_skipped"
        summary["probe_500"] = {"skipped": True, **probe_plan}
        write_json(out_dir / "run_summary.json", summary)
        write_run_docs(out_dir, summary, commands)
        print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
        return summary

    _coverage_rows, probe_summary = run_probe_coverage(probe_rows, out_dir, timeout=args.coverage_timeout)
    probe_summary.update(probe_plan)
    probe_summary["phase_c_gate_failures"] = phase_c_gate(probe_summary)
    write_json(out_dir / "coverage_probe_500" / "coverage_summary.json", probe_summary)
    summary["probe_500"] = probe_summary
    summary["gate_failures"].extend(probe_summary["phase_c_gate_failures"])
    if probe_summary["phase_c_gate_failures"]:
        summary["status"] = "blocked"
        summary["next_step"] = "blocked_phase_c_gate"
    else:
        summary["status"] = "ready"
        summary["next_step"] = "ready_for_full_expanded_mode1"
    write_json(out_dir / "run_summary.json", summary)
    write_run_docs(out_dir, summary, commands)
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Page57 artifact-only candidate universe expansion")
    parser.add_argument("--phase-d-full", action="store_true", help="Run approved full expanded Mode 1 coverage from an existing Phase A/B/C artifact.")
    parser.add_argument("--approved-artifact-root", type=Path, default=DEFAULT_APPROVED_CANDIDATE_UNIVERSE_ARTIFACT)
    parser.add_argument("--phase-d-out-dir", type=Path)
    parser.add_argument("--phase-d-limit", type=int, default=0)
    parser.add_argument("--phase-d-stop-after-success-gates", action="store_true")
    parser.add_argument("--reuse-probe-coverage", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--page-id", type=int, default=PAGE_ID)
    parser.add_argument("--elements-path", type=Path, default=DEFAULT_ELEMENTS_PATH)
    parser.add_argument("--previous-ready-path", type=Path, default=DEFAULT_PREVIOUS_READY_PATH)
    parser.add_argument("--out-dir", type=Path)
    parser.add_argument("--min-abstract-chars", type=int, default=300)
    parser.add_argument("--source-paper-limit", type=int)
    parser.add_argument("--top-k-per-element", type=int, default=14)
    parser.add_argument("--min-rows-per-claim", type=int, default=5)
    parser.add_argument("--semantic-threshold", type=float, default=0.50)
    parser.add_argument("--ollama-host", default="http://localhost:11434")
    parser.add_argument("--no-semantic", action="store_true")
    parser.add_argument("--probe-limit", type=int, default=500)
    parser.add_argument("--coverage-timeout", type=int, default=180)
    parser.add_argument("--skip-phase-c", action="store_true")
    args = parser.parse_args()
    if args.phase_d_full:
        run_phase_d_full_coverage(args)
        return
    run(args)


if __name__ == "__main__":
    main()
