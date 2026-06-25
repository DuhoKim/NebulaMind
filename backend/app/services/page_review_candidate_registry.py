from __future__ import annotations

import csv
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.claim import Claim, Evidence
from app.models.page import WikiPage, PageVersion
from app.services.content_canonicalizer import canonicalize


EXPECTED_MARKER_IDS = list(range(2905, 2927))
FORBIDDEN_TOKENS = [
    "cand:",
    "580",
    "[consensus]",
    "[debated]",
    "[reported]",
    "[unverified]",
    "[accepted]",
    "[background]",
    "display_trust",
    "tier_override",
    "staging",
    "static-preview wrapper",
    "wrapper artifacts",
]


@dataclass(frozen=True)
class CandidateRegistryEntry:
    candidate_id: str
    page_id: int
    label: str
    packet_path: Path
    expected_candidate_sha256: str
    preimage_page57_sha256: str
    preimage_page57_page_version_id: int
    preimage_page57_version_num: int
    page58_sha256: str
    evidence_count: int
    evidence_max_id: int
    page_versions_count: int
    page_versions_max_id: int


V3_MAX_PAPERS = CandidateRegistryEntry(
    candidate_id="v3-max-papers",
    page_id=57,
    label="Page57 synthesis v3 max papers",
    packet_path=Path(
        "/Users/duhokim/.openclaw/workspace/galaxy_evolution_v2/"
        "page57_synthesis_integration_packet_v3_max_papers_rebased_20260621T071140Z"
    ),
    expected_candidate_sha256="07f8d96919ea13ff0a313102a1861f5c10e8a2401d99302122512c987ce5f289",
    preimage_page57_sha256="44bea6c9454299fb5e5b9cc4791e8e0bbf36f7f15b24e1f1e5f469a8904a2aa0",
    preimage_page57_page_version_id=6196,
    preimage_page57_version_num=1707,
    page58_sha256="ef652c9692a2bb6d647bd7e7af1b1fce7ba0a115b07baf96d75ec3e6dae1593b",
    evidence_count=11675,
    evidence_max_id=27096,
    page_versions_count=5779,
    page_versions_max_id=6196,
)

REGISTRY: dict[tuple[int, str], CandidateRegistryEntry] = {
    (V3_MAX_PAPERS.page_id, V3_MAX_PAPERS.candidate_id): V3_MAX_PAPERS,
}


def get_candidate_registry_entry(page_id: int, candidate_id: str) -> CandidateRegistryEntry | None:
    return REGISTRY.get((page_id, candidate_id))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _candidate_files(entry: CandidateRegistryEntry) -> dict[str, Path]:
    packet = entry.packet_path
    return {
        "candidate": packet / "page57_synthesis_candidate.md",
        "validation": packet / "VALIDATION_REPORT.json",
        "apply_gate": packet / "APPLY_GATE.json",
        "live_baseline": packet / "LIVE_BASELINE.json",
        "traceability": packet / "PROSE_TRACEABILITY_MAP.json",
        "section_claim_map": packet / "SECTION_CLAIM_MAP.tsv",
        "integration_map": packet / "ORIGINAL_PAPER_INTEGRATION_MAP.json",
        "disposition_table": packet / "ORIGINAL_PAPER_DISPOSITION_TABLE.tsv",
        "coherence": packet / "COHERENCE_GUARD_DECISIONS.md",
        "artifact_hashes": packet / "ARTIFACT_HASHES.json",
    }


def _parse_section_claim_map(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return [dict(row) for row in csv.DictReader(fh, delimiter="\t")]


def _parse_marker_checks(candidate: str) -> dict[str, Any]:
    opens = [int(x) for x in re.findall(r"<!--\s*claim:(\d+)\s*-->", candidate)]
    closes = [int(x) for x in re.findall(r"<!--\s*/claim:(\d+)\s*-->", candidate)]
    expected = set(EXPECTED_MARKER_IDS)
    visible = set(opens + closes)
    return {
        "status": (
            "PASS"
            if set(opens) == expected
            and set(closes) == expected
            and opens == closes
            and len(opens) == len(EXPECTED_MARKER_IDS)
            and all(opens.count(cid) == 1 for cid in EXPECTED_MARKER_IDS)
            else "FAIL"
        ),
        "open_ids": opens,
        "close_ids": closes,
        "expected_ids": EXPECTED_MARKER_IDS,
        "missing_ids": sorted(expected - visible),
        "extra_ids": sorted(visible - expected),
        "open_close_all_match": opens == closes,
        "once_each": all(opens.count(cid) == 1 for cid in EXPECTED_MARKER_IDS),
    }


def _forbidden_scan(candidate: str) -> dict[str, Any]:
    hits = {token: (token in candidate) for token in FORBIDDEN_TOKENS}
    return {"status": "PASS" if not any(hits.values()) else "FAIL", "hits": hits}


def _canonicalizer_check(candidate: str) -> dict[str, Any]:
    try:
        result = canonicalize(candidate)
        return {
            "status": "PASS" if result.invariants_ok else "FAIL",
            "available": True,
            "invariants_ok": result.invariants_ok,
            "violations": result.violations or [],
            "content_changed": result.new_content != candidate,
            "new_content_sha256": sha256_text(result.new_content),
            "changes": result.changes,
        }
    except Exception as exc:
        return {
            "status": "NOT_FULLY_HARD_GATED",
            "available": False,
            "reason": f"{type(exc).__name__}: {exc}",
        }


def _page_state(db: Session, page_id: int) -> dict[str, Any]:
    page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
    if not page:
        return {"exists": False, "page_id": page_id}
    latest = (
        db.query(PageVersion)
        .filter(PageVersion.page_id == page_id)
        .order_by(PageVersion.version_num.desc())
        .first()
    )
    content = page.content or ""
    return {
        "exists": True,
        "page_id": page_id,
        "title": page.title,
        "sha256": sha256_text(content),
        "bytes": len(content.encode("utf-8")),
        "chars": len(content),
        "latest_page_version_id": latest.id if latest else None,
        "latest_version_num": latest.version_num if latest else None,
    }


def _live_drift(entry: CandidateRegistryEntry, db: Session) -> dict[str, Any]:
    page57 = _page_state(db, 57)
    page58 = _page_state(db, 58)
    evidence_count, evidence_max_id = db.query(func.count(Evidence.id), func.max(Evidence.id)).one()
    page_versions_count, page_versions_max_id = db.query(func.count(PageVersion.id), func.max(PageVersion.id)).one()
    candidate_is_live = page57.get("sha256") == entry.expected_candidate_sha256
    checks = {
        "candidate_is_live": candidate_is_live,
        "page57_sha256": page57.get("sha256") == entry.preimage_page57_sha256,
        "page57_page_version_id": page57.get("latest_page_version_id") == entry.preimage_page57_page_version_id,
        "page57_version_num": page57.get("latest_version_num") == entry.preimage_page57_version_num,
        "page58_sha256": page58.get("sha256") == entry.page58_sha256,
        "evidence_count": evidence_count == entry.evidence_count,
        "evidence_max_id": evidence_max_id == entry.evidence_max_id,
        "page_versions_count": page_versions_count == entry.page_versions_count,
        "page_versions_max_id": page_versions_max_id == entry.page_versions_max_id,
    }
    if candidate_is_live:
        status = "APPLIED"
    elif all(value for key, value in checks.items() if key != "candidate_is_live"):
        status = "CURRENT"
    else:
        status = "STALE_PREIMAGE"
    return {
        "status": status,
        "checks": checks,
        "current": {
            "page57": page57,
            "page58": page58,
            "evidence": {"count": evidence_count, "max_id": evidence_max_id},
            "page_versions": {"count": page_versions_count, "max_id": page_versions_max_id},
        },
        "pinned": {
            "page57": {
                "sha256": entry.preimage_page57_sha256,
                "latest_page_version_id": entry.preimage_page57_page_version_id,
                "latest_version_num": entry.preimage_page57_version_num,
            },
            "page58": {"sha256": entry.page58_sha256},
            "evidence": {"count": entry.evidence_count, "max_id": entry.evidence_max_id},
            "page_versions": {"count": entry.page_versions_count, "max_id": entry.page_versions_max_id},
        },
    }


def _query_claims_and_evidence(db: Session) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    claims = (
        db.query(Claim)
        .filter(Claim.id.in_(EXPECTED_MARKER_IDS))
        .order_by(Claim.id)
        .all()
    )
    claim_by_id = {claim.id: claim for claim in claims}
    for claim_id in EXPECTED_MARKER_IDS:
        claim = claim_by_id.get(claim_id)
        if not claim:
            rows.append({"claim_id": claim_id, "missing": True, "evidence": []})
            continue
        evidence_rows = db.query(Evidence).filter(Evidence.claim_id == claim_id).order_by(Evidence.id).all()
        rows.append(
            {
                "claim_id": claim_id,
                "missing": False,
                "text": claim.text,
                "trust_level": claim.trust_level,
                "trust_score": claim.trust_score,
                "section": claim.section,
                "order_idx": claim.order_idx,
                "evidence": [
                    {
                        "id": evidence.id,
                        "title": evidence.title,
                        "arxiv_id": evidence.arxiv_id,
                        "url": evidence.url,
                        "authors": evidence.authors,
                        "year": evidence.year,
                        "summary": evidence.summary,
                        "stance": evidence.stance,
                        "relevance": evidence.relevance,
                        "entailment": evidence.entailment,
                        "rigor": evidence.rigor,
                        "confidence": evidence.confidence,
                        "quality_v2": evidence.quality if evidence.consensus_scorecard_id is not None else None,
                    }
                    for evidence in evidence_rows
                ],
                "total_elements": 0,
            }
        )
    return rows


def build_page_review_candidate_response(page_id: int, candidate_id: str, db: Session) -> dict[str, Any] | None:
    entry = get_candidate_registry_entry(page_id, candidate_id)
    if not entry:
        return None

    files = _candidate_files(entry)
    missing_files = [name for name, path in files.items() if not path.exists()]
    candidate = files["candidate"].read_text(encoding="utf-8")
    computed_sha = sha256_text(candidate)
    hash_check = {
        "status": "PASS" if computed_sha == entry.expected_candidate_sha256 else "FAIL",
        "computed_sha256": computed_sha,
        "expected_sha256": entry.expected_candidate_sha256,
    }
    marker_check = _parse_marker_checks(candidate)
    forbidden_check = _forbidden_scan(candidate)
    canonicalizer_check = _canonicalizer_check(candidate)
    drift = _live_drift(entry, db)

    validation = _read_json(files["validation"]) if files["validation"].exists() else {}
    apply_gate = _read_json(files["apply_gate"]) if files["apply_gate"].exists() else {}
    traceability = _read_json(files["traceability"]) if files["traceability"].exists() else {}
    integration = _read_json(files["integration_map"]) if files["integration_map"].exists() else {}

    hard_checks_pass = all(
        check.get("status") == "PASS"
        for check in [hash_check, marker_check, forbidden_check, canonicalizer_check]
    )
    review_status = "REVIEWABLE" if hard_checks_pass and drift["status"] == "CURRENT" else drift["status"]
    if hard_checks_pass and drift["status"] == "APPLIED":
        review_status = "APPLIED"
    if not hard_checks_pass:
        review_status = "NOT_REVIEWABLE"

    return {
        "read_only": True,
        "write_paths_reachable": False,
        "route_guarantee": "GET-only artifact review route; no apply endpoint, no mutation handler, no write dependency.",
        "access_control": {
            "current_mode": "unauthenticated_local_preview",
            "compatibility_note": "Matches existing local admin preview surfaces.",
            "public_exposure_recommendation": (
                "Do not expose this route on the public internet without a gate. "
                "Use VPN/Tailscale-only access, HTTP basic auth at the reverse proxy, "
                "or a short-lived signed review token before managed/public rollout. "
                "Prefer X-Page-Review-Token over query tokens because URLs can leak "
                "through browser history, logs, and referrers."
            ),
        },
        "review_status": review_status,
        "candidate": {
            "id": entry.candidate_id,
            "page_id": entry.page_id,
            "label": entry.label,
            "artifact_ref": entry.packet_path.name,
            "markdown": candidate,
            "sha256": computed_sha,
            "bytes": len(candidate.encode("utf-8")),
            "chars": len(candidate),
        },
        "registry": {
            "expected_candidate_sha256": entry.expected_candidate_sha256,
            "expected_markers": EXPECTED_MARKER_IDS,
            "preimage_page57_sha256": entry.preimage_page57_sha256,
            "preimage_page57_page_version_id": entry.preimage_page57_page_version_id,
            "preimage_page57_version_num": entry.preimage_page57_version_num,
            "page58_sha256": entry.page58_sha256,
            "evidence": {"count": entry.evidence_count, "max_id": entry.evidence_max_id},
            "page_versions": {"count": entry.page_versions_count, "max_id": entry.page_versions_max_id},
        },
        "checks": {
            "missing_files": missing_files,
            "candidate_hash": hash_check,
            "marker_bijection": marker_check,
            "forbidden_tokens": forbidden_check,
            "canonicalizer": canonicalizer_check,
            "live_drift": drift,
            "apply_gate": {
                "status": "ALREADY_APPLIED" if drift["status"] == "APPLIED" else apply_gate.get("status"),
                "allowed_to_apply": False,
                "packet_allowed_to_apply": bool(apply_gate.get("allowed_to_apply", False)),
            },
        },
        "packet": {
            "validation": validation,
            "apply_gate": apply_gate,
            "live_baseline": _read_json(files["live_baseline"]) if files["live_baseline"].exists() else {},
            "traceability": traceability,
            "section_claim_map": _parse_section_claim_map(files["section_claim_map"]),
            "integration": integration,
            "coherence_guard_decisions": files["coherence"].read_text(encoding="utf-8") if files["coherence"].exists() else "",
        },
        "traceability_summary": {
            "paragraph_count": traceability.get("paragraph_count"),
            "entries_with_original_context": sum(
                1 for item in traceability.get("entries", []) if item.get("omitted_survivor_context_ids")
            ),
            "integrated_rows": integration.get("counts", {}).get("integrated_total_v3"),
            "considered_rows": integration.get("counts", {}).get("total_original_survivor_rows_considered"),
            "newly_integrated": integration.get("counts", {}).get("newly_integrated_v3"),
            "excluded_or_held": integration.get("counts", {}).get("excluded_or_held_total"),
        },
        "evidence_panels": _query_claims_and_evidence(db),
    }
