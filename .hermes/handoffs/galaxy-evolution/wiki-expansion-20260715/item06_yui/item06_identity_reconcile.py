#!/usr/bin/env python3
"""Reconcile item-06 composite identifiers against pinned public metadata.

Inputs are local custody artifacts. This script performs no network operations.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


def load_membership_module(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("item06_membership", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def normalized_doi(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = value.strip().lower()
    cleaned = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", cleaned)
    return cleaned or None


def normalized_arxiv(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = value.strip().lower()
    cleaned = re.sub(r"^arxiv:", "", cleaned)
    return cleaned or None


def author_matches(raw_author: str, semantic_authors: list[dict[str, Any]]) -> bool:
    if not semantic_authors:
        return False
    raw_surname = re.sub(r"[^a-z]", "", raw_author.split(",", 1)[0].lower())
    semantic_name = re.sub(r"[^a-z]", "", semantic_authors[0].get("name", "").lower())
    semantic_last = re.sub(
        r"[^a-z]", "", semantic_authors[0].get("name", "").split()[-1].lower()
    )
    return bool(
        raw_surname
        and semantic_name
        and (raw_surname in semantic_name or semantic_last in raw_surname)
    )


def crossref_author_matches(
    raw_author: str, crossref_authors: list[dict[str, Any]]
) -> bool:
    if not crossref_authors:
        return False
    raw_surname = re.sub(r"[^a-z]", "", raw_author.split(",", 1)[0].lower())
    family = re.sub(r"[^a-z]", "", crossref_authors[0].get("family", "").lower())
    return bool(raw_surname and family and (family in raw_surname or raw_surname in family))


def crossref_year(message: dict[str, Any]) -> int | None:
    for field in ("published-print", "published-online", "published", "issued"):
        parts = (message.get(field) or {}).get("date-parts") or []
        if parts and parts[0]:
            return parts[0][0]
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--membership-script", type=Path, required=True)
    parser.add_argument("--raw", type=Path, required=True)
    parser.add_argument("--membership-scan", type=Path, required=True)
    parser.add_argument("--semantic-request", type=Path, required=True)
    parser.add_argument("--semantic-response", type=Path, required=True)
    parser.add_argument("--semantic-doi-map", type=Path, required=True)
    parser.add_argument("--semantic-doi-response", type=Path, required=True)
    parser.add_argument("--crossref-doi-records", type=Path, required=True)
    parser.add_argument("--arxiv-corrections", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    membership_module = load_membership_module(args.membership_script)
    raw_rows = membership_module.parse_raw_rows(
        args.raw.read_text(encoding="utf-8")
    )
    membership_scan = json.loads(args.membership_scan.read_text(encoding="utf-8"))
    membership_by_key = {
        result["key"]: result for result in membership_scan["results"]
    }
    request = json.loads(args.semantic_request.read_text(encoding="utf-8"))
    response = json.loads(args.semantic_response.read_text(encoding="utf-8"))
    doi_map = json.loads(args.semantic_doi_map.read_text(encoding="utf-8"))
    doi_response = json.loads(args.semantic_doi_response.read_text(encoding="utf-8"))
    if len(doi_map["keys"]) != len(doi_response):
        raise ValueError("Semantic Scholar DOI response length does not match map")
    doi_by_key = dict(zip(doi_map["keys"], doi_response))
    crossref_capture = json.loads(
        args.crossref_doi_records.read_text(encoding="utf-8")
    )
    crossref_by_key = crossref_capture["results"]
    correction_capture = json.loads(
        args.arxiv_corrections.read_text(encoding="utf-8")
    )
    corrections_by_key = correction_capture["results"]

    expected_ids = [
        "ARXIV:" + raw_rows[key]["arxiv"] for key in sorted(raw_rows)
    ]
    if request["ids"] != expected_ids:
        raise ValueError("Semantic Scholar request order does not match raw source rows")
    if len(response) != len(expected_ids):
        raise ValueError("Semantic Scholar response length does not match request")

    results: list[dict[str, Any]] = []
    for key, arxiv_semantic in zip(sorted(raw_rows), response):
        raw = raw_rows[key]
        membership = membership_by_key[key]
        membership_ok = membership["status"] == "EXACT_BIBLIOGRAPHY_MEMBER"
        has_raw_doi = raw["doi"].lower() != "none"
        semantic = doi_by_key.get(key) if has_raw_doi else arxiv_semantic
        metadata_basis = "DOI" if has_raw_doi else "RAW_ARXIV"
        correction = corrections_by_key.get(key)

        if correction:
            metadata_basis = "PINNED_ARXIV_CORRECTION"
            corrected_title = correction.get("citation_title") or ""
            title_similarity = SequenceMatcher(
                None,
                normalized_title(raw["title"]),
                normalized_title(corrected_title),
            ).ratio()
            raw_title_matches = title_similarity >= 0.9
            corrected_year_text = correction.get("citation_date") or ""
            corrected_year = (
                int(corrected_year_text[:4])
                if re.match(r"^\d{4}", corrected_year_text)
                else None
            )
            corrected_doi = normalized_doi(correction.get("expected_related_doi"))
            related_dois = {
                normalized_doi(value)
                for value in correction.get("citation_doi_values") or []
            }
            corrected_arxiv = normalized_arxiv(correction.get("arxiv_id"))
            meta_arxiv = normalized_arxiv(correction.get("citation_arxiv_id"))
            corrected_authors = [
                {"name": name} for name in correction.get("citation_authors") or []
            ]
            checks = {
                "review_bibliography_member": membership_ok,
                "pinned_arxiv_page_http_200": correction.get("http_status") == 200,
                "corrected_title_match": raw_title_matches,
                "corrected_first_author_match": author_matches(
                    raw["author"], corrected_authors
                ),
                "publication_or_preprint_year_match": (
                    isinstance(corrected_year, int)
                    and abs(corrected_year - raw["year"]) <= 1
                ),
                "corrected_arxiv_matches_page_metadata": corrected_arxiv == meta_arxiv,
                "corrected_doi_matches_page_metadata": corrected_doi in related_dois,
                "ads_tuple_matches_review_bibliography": membership_ok,
            }
            canonical_doi = corrected_doi
            canonical_arxiv = corrected_arxiv
            semantic_identity = {
                "basis": "PINNED_ARXIV_ABSTRACT_PAGE",
                "title": corrected_title,
                "year": corrected_year,
                "first_author": (correction.get("citation_authors") or [None])[0],
                "doi": corrected_doi,
                "arxiv": corrected_arxiv,
                "url": correction.get("url"),
                "saved_html_sha256": correction.get("saved_html_sha256"),
            }
        elif has_raw_doi:
            crossref_capture_row = crossref_by_key.get(key) or {}
            crossref_message = (
                (crossref_capture_row.get("response") or {}).get("message")
                if crossref_capture_row.get("http_status") == 200
                else None
            )
            external = (semantic or {}).get("externalIds") or {}
            semantic_doi = normalized_doi(external.get("DOI"))
            semantic_arxiv = normalized_arxiv(external.get("ArXiv"))
            raw_doi = normalized_doi(raw["doi"])
            ads_volume, ads_qualifier, ads_page = membership_module.ads_volume_page(
                raw["ads"]
            )
            if crossref_message:
                crossref_doi = normalized_doi(crossref_message.get("DOI"))
                crossref_volume = re.sub(
                    r"[^0-9]", "", str(crossref_message.get("volume") or "")
                ).lstrip("0")
                crossref_page = re.sub(
                    r"[^a-zA-Z0-9]",
                    "",
                    str(crossref_message.get("page") or "").split("-", 1)[0],
                ).upper()
                expected_pages = {ads_page.upper()}
                if ads_qualifier:
                    expected_pages.add((ads_qualifier + ads_page).upper())
                tuple_ok = bool(
                    ads_volume
                    and crossref_volume == ads_volume.lstrip("0")
                    and crossref_page in expected_pages
                )
                year = crossref_year(crossref_message)
                year_ok = isinstance(year, int) and abs(year - raw["year"]) <= 1
                first_author_ok = crossref_author_matches(
                    raw["author"], crossref_message.get("author") or []
                )
                crossref_title = (crossref_message.get("title") or [""])[0]
                title_similarity = SequenceMatcher(
                    None,
                    normalized_title(raw["title"]),
                    normalized_title(crossref_title),
                ).ratio()
                raw_title_matches = title_similarity >= 0.8
                doi_ok = raw_doi == crossref_doi == semantic_doi
                arxiv_ok = bool(semantic_arxiv and semantic_doi == crossref_doi)
                canonical_doi = crossref_doi
                canonical_arxiv = semantic_arxiv
                semantic_identity = {
                    "basis": "CROSSREF_DOI_PLUS_SEMANTIC_SCHOLAR_EXTERNAL_IDS",
                    "title": crossref_title,
                    "year": year,
                    "first_author": (crossref_message.get("author") or [{}])[0].get("family"),
                    "venue": (crossref_message.get("container-title") or [None])[0],
                    "volume": crossref_message.get("volume"),
                    "page": crossref_message.get("page"),
                    "doi": crossref_doi,
                    "semantic_scholar_external_ids": external,
                }
            else:
                title_similarity = 0.0
                raw_title_matches = False
                tuple_ok = year_ok = first_author_ok = doi_ok = arxiv_ok = False
                canonical_doi = None
                canonical_arxiv = None
                semantic_identity = None
            checks = {
                "review_bibliography_member": membership_ok,
                "crossref_doi_record_present": crossref_message is not None,
                "crossref_publication_year_match": year_ok,
                "crossref_first_author_match": first_author_ok,
                "crossref_volume_page_or_title_matches_ads_identity": (
                    tuple_ok or raw_title_matches
                ),
                "doi_matches_crossref_and_semantic_scholar": doi_ok,
                "arxiv_supplied_by_same_doi_record": arxiv_ok,
                "ads_tuple_matches_review_bibliography": membership_ok,
            }
        elif semantic is None:
            checks = {
                "review_bibliography_member": membership_ok,
                "public_metadata_record_present": False,
                "title_match": False,
                "year_match": False,
                "first_author_match": False,
                "arxiv_match": False,
                "doi_match_or_publicly_supplied": False,
                "ads_tuple_matches_review_bibliography": membership_ok,
            }
            semantic_identity = None
            title_similarity = 0.0
            raw_title_matches = False
            canonical_doi = None
            canonical_arxiv = None
        else:
            external = semantic.get("externalIds") or {}
            semantic_title = semantic.get("title") or ""
            title_similarity = SequenceMatcher(
                None,
                normalized_title(raw["title"]),
                normalized_title(semantic_title),
            ).ratio()
            semantic_doi = normalized_doi(external.get("DOI"))
            raw_arxiv = normalized_arxiv(raw["arxiv"])
            semantic_arxiv = normalized_arxiv(external.get("ArXiv"))
            doi_ok = semantic_doi is not None
            arxiv_ok = raw_arxiv == semantic_arxiv
            year_ok = semantic.get("year") == raw["year"]
            raw_title_matches = title_similarity >= 0.9
            checks = {
                "review_bibliography_member": membership_ok,
                "public_metadata_record_present": True,
                "title_match": raw_title_matches,
                "publication_or_preprint_year_match": year_ok,
                "first_author_match": author_matches(raw["author"], semantic.get("authors") or []),
                "arxiv_match": arxiv_ok,
                "doi_match_or_publicly_supplied": doi_ok,
                "ads_tuple_matches_review_bibliography": membership_ok,
            }
            canonical_doi = semantic_doi
            canonical_arxiv = semantic_arxiv
            semantic_identity = {
                "basis": "SEMANTIC_SCHOLAR_RAW_ARXIV",
                "paper_id": semantic.get("paperId"),
                "title": semantic_title,
                "year": semantic.get("year"),
                "first_author": (semantic.get("authors") or [{}])[0].get("name"),
                "venue": semantic.get("venue"),
                "journal": semantic.get("journal"),
                "external_ids": external,
                "url": semantic.get("url"),
            }

        if not membership_ok:
            disposition = "QUARANTINE_NOT_EXACT_REVIEW_BIBLIOGRAPHY_MEMBER"
        elif all(checks.values()):
            disposition = "USABLE_COMPOSITE_VERIFIED"
        else:
            disposition = "HOLD_COMPOSITE_VERIFICATION_FAILED"

        results.append(
            {
                "key": key,
                "disposition": disposition,
                "raw_identity": {
                    field: raw[field]
                    for field in (
                        "author",
                        "year",
                        "journal",
                        "title",
                        "doi",
                        "arxiv",
                        "ads",
                        "role",
                        "review_locator",
                    )
                },
                "membership_status": membership["status"],
                "metadata_basis": metadata_basis,
                "exact_bibliography_entries": membership["exact_bibliography_entries"],
                "semantic_scholar_identity": semantic_identity,
                "title_similarity": round(title_similarity, 6),
                "raw_title_matches_public_record": raw_title_matches,
                "canonical_doi": canonical_doi,
                "canonical_arxiv": canonical_arxiv,
                "checks": checks,
            }
        )

    dispositions = sorted({result["disposition"] for result in results})
    report = {
        "schema_version": 1,
        "status": "COMPOSITE_IDENTITY_RECONCILIATION",
        "source_count": len(results),
        "disposition_counts": {
            disposition: sum(
                result["disposition"] == disposition for result in results
            )
            for disposition in dispositions
        },
        "results": results,
        "safety": {
            "network_operations_performed_by_this_script": 0,
            "browser_or_account_action": False,
            "live_wiki_db_trust_write": False,
            "deploy_restart": False,
            "git_write": False,
            "publication": False,
            "other_agents_used_after_owner_redirect": False,
        },
    }
    args.output.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
