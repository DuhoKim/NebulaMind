from types import SimpleNamespace

from app.utils import novelty_screen


def idea(**overrides):
    base = {
        "id": 1,
        "survey_combo": "DESI+JWST",
        "question": "Does JWST morphology correlate with DESI environment?",
        "why_now": "JWST and DESI overlap is now public.",
        "approach": "Cross-match JWST NIRCam galaxies with DESI spectra.",
    }
    base.update(overrides)
    return SimpleNamespace(**base)


def test_entity_validation_rejects_known_confabulated_survey_name():
    result = novelty_screen.validate_entities(
        idea(approach="Use the DESI Legacy Survey of Space and Time catalog."),
        db=None,
        registry=set(novelty_screen.CONTROLLED_VOCAB),
    )

    assert not result.ok
    assert "DESI Legacy Survey of Space and Time" in result.offending_terms


def test_entity_validation_accepts_controlled_vocabulary_names():
    result = novelty_screen.validate_entities(
        idea(approach="Cross-match JWST NIRCam, DESI, ALMA, VLA, MeerKAT, and eROSITA."),
        db=None,
        registry=set(novelty_screen.CONTROLLED_VOCAB),
    )

    assert result.ok
    assert result.offending_terms == []


def test_aggregate_status_prefers_covered_over_partial():
    status, closest = novelty_screen.aggregate_status(
        {
            "paper_verdicts": [
                {"bibcode": "A", "verdict": "partial", "one_line_reason": "nearby"},
                {"bibcode": "B", "verdict": "covered", "one_line_reason": "same test"},
            ],
            "closest_prior_work": [
                {"bibcode": "A", "verdict": "partial", "one_line_reason": "nearby"},
                {"bibcode": "B", "verdict": "covered", "one_line_reason": "same test"},
            ],
        }
    )

    assert status == "covered"
    assert [row["bibcode"] for row in closest] == ["A", "B"]


def test_derive_factual_verified_from_coverage_status():
    assert novelty_screen.derive_factual_verified("screened_pass") is True
    assert novelty_screen.derive_factual_verified("partial") is True
    assert novelty_screen.derive_factual_verified("covered") is False
    assert novelty_screen.derive_factual_verified(None) is False
