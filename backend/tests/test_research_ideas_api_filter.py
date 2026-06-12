from datetime import datetime, timezone
from types import SimpleNamespace

from app.routers import research_ideas


def row(**overrides):
    base = {
        "id": 7,
        "page_id": 57,
        "survey_combo": "DESI+JWST",
        "question": "Question?",
        "why_now": "Now.",
        "approach": "Do it.",
        "systematics_json": [],
        "novelty": 0.8,
        "feasibility": 0.7,
        "status": "draft",
        "model_chain": "test",
        "saved_by_papa": False,
        "seeded": False,
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
        "last_seen_at": datetime.now(timezone.utc),
        "factual_verified": False,
        "factual_verified_at": None,
        "factual_verification_notes": {"papers_checked": 20},
        "coverage_status": None,
        "closest_prior_work": None,
        "coverage_checked_at": None,
    }
    base.update(overrides)
    return SimpleNamespace(**base)


def test_idea_dict_marks_null_coverage_as_unverified_badge():
    payload = research_ideas._idea_to_dict(row())

    assert payload["factual_verified"] is False
    assert payload["display_badge"] == "unverified"


def test_idea_dict_derives_factual_verified_for_partial():
    payload = research_ideas._idea_to_dict(
        row(
            coverage_status="partial",
            closest_prior_work=[{"bibcode": "2024ApJ...1A", "verdict": "partial"}],
            coverage_checked_at=datetime.now(timezone.utc),
        )
    )

    assert payload["factual_verified"] is True
    assert payload["display_badge"] is None
    assert payload["closest_prior_work"][0]["bibcode"] == "2024ApJ...1A"


def test_page_filter_excludes_screened_fail_by_default():
    clause = research_ideas._screening_filter(include_covered=False)

    assert "screened_pass" in clause
    assert "partial" in clause
    assert "failed_entity" not in clause
    assert "coverage_status IS NULL" in clause
