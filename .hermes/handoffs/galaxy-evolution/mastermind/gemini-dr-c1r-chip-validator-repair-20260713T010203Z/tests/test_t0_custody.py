from __future__ import annotations

import hashlib
import json
from pathlib import Path


PACKET = Path(__file__).resolve().parents[1]
SEALED = PACKET.parent / "gemini-dr-revised-canary-20260712T045317Z"
FIXTURES = PACKET / "fixtures"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_t0_sealed_inputs_and_fixture_copies_are_immutable() -> None:
    expected = {
        SEALED / "runs/c1r/rendered_body.html": "78ed129c47daf9300d9ed319aa1ffe95bbb0d1810a223733afaf48c4372f2bbc",
        SEALED / "runs/c1r/body.md": "8a130c5a6fc1b1f5d534888d3fb20806230b8b4c7737cb00f9bfb18ad0d6bc00",
        SEALED / "runs/c1r/structured_capture.json": "2d10e34a46c609b713d980ded746c8bf4f1214ea7213603535cd3c7e271ec468",
        SEALED / "runs/c1r/validator_result.json": "34f525a58b1c71d237b1723fc42bfab5acfaf631e9b25175a703462e108c91f4",
        SEALED / "runs/c1r/prompt_submitted.md": "fffac44fbf6e9abe3afb1f8f34f3a9e3e7688991f319c4927459fb29ac00e1ef",
        SEALED / "validator/structured_capture.js": "ca23943a5068289b4893e60ed2153a54a87f60b380c451c1d26565546984a0c8",
        SEALED / "validator/validator.py": "67aa2a2d904a18a5ede42c93e33c22091797d55f042ae61fee732ad259cc5f5f",
    }
    assert {str(path): digest(path) for path in expected} == {
        str(path): value for path, value in expected.items()
    }

    manifest = json.loads((FIXTURES / "GORU_FIXTURE_MANIFEST.json").read_text())
    assert manifest
    for entry in manifest:
        source = PACKET / entry["source_path"]
        copied = PACKET / entry["copied_path"]
        assert digest(source) == entry["source_sha256"]
        assert digest(copied) == entry["copied_sha256"]
        assert source.read_bytes() == copied.read_bytes()
        assert entry["byte_identical"] is True


def test_t0_goru_invalid_evidence_is_preserved_and_superseded() -> None:
    assert digest(FIXTURES / "EXPECTED_DOM_FACTS_GORU_INVALID.json") == "1924a8d5dcbeb5bd8572296c8897cd0a9e65569d42a9fa3aa04977cd550030f9"
    assert digest(FIXTURES / "CORRUPTED_HTML_MANIFEST_GORU_INVALID.json") == "ce388944ad852fff16d060b1c23d918c1b83c18aa6b0b36268e37c84a0b98fb3"
    assert not (PACKET / "GORU_FIXTURE_MANIFEST.json").exists()
    adjudication = (PACKET / "HWAO_GORU_FIXTURE_ADJUDICATION.md").read_text()
    assert adjudication.rstrip().endswith("HWAO_GORU_FIXTURE_SUPERSEDE_APPROVED_20260713T010203Z")


def test_t0_regenerated_facts_match_published_census() -> None:
    facts = json.loads((FIXTURES / "EXPECTED_DOM_FACTS_V2.json").read_text())
    assert facts["input_sha256"] == "78ed129c47daf9300d9ed319aa1ffe95bbb0d1810a223733afaf48c4372f2bbc"
    assert facts["counts"] == {
        "chips_total": 108,
        "chips_by_region": {"S1": 40, "S2": 8, "S3": 3, "S4": 9, "S5": 2, "ledger": 46},
        "anchors_total": 46,
        "anchors_inside_td": 0,
        "ledger_pairs": 46,
        "ledger_unique_indices": 37,
        "ledger_mapping_conflicts": 0,
        "blank_short_names": 46,
        "duplicate_rows": 9,
    }
    assert [row["citation_chips"] for row in facts["S2"]] == [[27], [28], [10], [11], [15], [20], [30], [30]]
    assert facts["S5"] == [
        {**facts["S5"][0], "unit": "GAP1", "chips": [30], "has_token": False},
        {**facts["S5"][1], "unit": "GAP2", "chips": [], "has_token": True},
        {**facts["S5"][2], "unit": "GAP3", "chips": [36], "has_token": False},
        {**facts["S5"][3], "unit": "GAP4", "chips": [], "has_token": True},
    ]
    assert facts["orphan_indices"] == [2, 5, 8, 9, 13, 16, 18, 23, 24, 29, 31, 33]

    corrupted = json.loads((FIXTURES / "CORRUPTED_HTML_MANIFEST_V2.json").read_text())
    assert corrupted["verification_passed"] is True
    assert list(corrupted["conflicts"]) == ["10"]
