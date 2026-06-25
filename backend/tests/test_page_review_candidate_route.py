from pathlib import Path
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.main import app
from app.routers import admin_page_review
from app.services.page_review_candidate_registry import (
    EXPECTED_MARKER_IDS,
    _forbidden_scan,
    _parse_marker_checks,
    sha256_text,
)


def _candidate_with_markers() -> str:
    return "\n\n".join(
        f"<!--claim:{claim_id}-->claim {claim_id} body<!--/claim:{claim_id}-->"
        for claim_id in EXPECTED_MARKER_IDS
    )


def test_page_review_marker_bijection_passes_for_v3_live_ids():
    result = _parse_marker_checks(_candidate_with_markers())
    assert result["status"] == "PASS"
    assert result["open_ids"] == EXPECTED_MARKER_IDS
    assert result["close_ids"] == EXPECTED_MARKER_IDS
    assert result["extra_ids"] == []
    assert result["missing_ids"] == []


def test_page_review_marker_bijection_rejects_extra_or_repeated_ids():
    body = _candidate_with_markers()
    body += "\n<!--claim:580001-->synthetic<!--/claim:580001-->"
    body += "\n<!--claim:2905-->duplicate<!--/claim:2905-->"
    result = _parse_marker_checks(body)
    assert result["status"] == "FAIL"
    assert 580001 in result["extra_ids"]
    assert result["once_each"] is False


def test_page_review_forbidden_token_scan_negative_fixture():
    result = _forbidden_scan("This has cand:123 and [reported] and display_trust.")
    assert result["status"] == "FAIL"
    assert result["hits"]["cand:"] is True
    assert result["hits"]["[reported]"] is True
    assert result["hits"]["display_trust"] is True


def test_page_review_sha256_helper_matches_known_value():
    assert sha256_text("page57-review") == "2ebafff8895ad18946a35ccff27f6f923b95c448cc99ac463931befae7813d06"


def test_page_review_get_route_is_read_only(monkeypatch):
    monkeypatch.setenv("PAGE_REVIEW_TOKEN", "test-review-token")

    def fake_builder(page_id, candidate_id, db):
        assert page_id == 57
        assert candidate_id == "v3-max-papers"
        return {
            "read_only": True,
            "write_paths_reachable": False,
            "route_guarantee": "GET-only artifact review route",
            "review_status": "REVIEWABLE",
            "candidate": {"id": candidate_id, "page_id": page_id, "sha256": "abc", "markdown": ""},
            "checks": {"apply_gate": {"allowed_to_apply": False}},
            "evidence_panels": [],
        }

    monkeypatch.setattr(admin_page_review, "build_page_review_candidate_response", fake_builder)
    client = TestClient(app)
    unauthenticated = client.get("/api/admin/page-review/page/57/candidates/v3-max-papers")
    assert unauthenticated.status_code == 401

    invalid = client.get(
        "/api/admin/page-review/page/57/candidates/v3-max-papers",
        headers={"X-Page-Review-Token": "wrong-token"},
    )
    assert invalid.status_code == 403

    response = client.get(
        "/api/admin/page-review/page/57/candidates/v3-max-papers",
        headers={"X-Page-Review-Token": "test-review-token"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["read_only"] is True
    assert payload["write_paths_reachable"] is False
    assert payload["checks"]["apply_gate"]["allowed_to_apply"] is False

    not_allowed = client.post("/api/admin/page-review/page/57/candidates/v3-max-papers")
    assert not_allowed.status_code == 405
