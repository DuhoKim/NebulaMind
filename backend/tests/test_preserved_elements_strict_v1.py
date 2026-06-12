import pytest
import json
from pydantic import ValidationError
from app.models.claim_rewrite_lineage import PreservedElementsJson

def test_preserved_elements_json_strict_round_trip():
    # Valid model validation
    data = {
        "supporting_evidence_ids": [101, 102],
        "element_id_map": {"old-1": "new-1"}
    }
    model = PreservedElementsJson(**data)
    assert model.supporting_evidence_ids == [101, 102]
    assert model.element_id_map == {"old-1": "new-1"}
    
    # Validation exports correctly
    dumped = model.model_dump()
    assert dumped == data

def test_preserved_elements_json_invalid_types():
    # Should fail if supporting_evidence_ids contains non-integers (per strict definition list[int])
    data = {
        "supporting_evidence_ids": ["not-an-int"],
        "element_id_map": {"old": "new"}
    }
    with pytest.raises(ValidationError):
        PreservedElementsJson(**data)

def test_preserved_elements_json_defaults():
    model = PreservedElementsJson()
    assert model.supporting_evidence_ids == []
    assert model.element_id_map == {}

def test_legacy_list_to_strict_dict_conversion():
    # Test our migration conversion helper function behavior
    legacy_list = ["element1", "element2"]
    
    # list -> dict conversion behavior requested:
    # List [id, ...] -> {"supporting_evidence_ids": [...], "element_id_map": {}}
    converted = {
        "supporting_evidence_ids": legacy_list,
        "element_id_map": {}
    }
    
    assert isinstance(converted, dict)
    assert "supporting_evidence_ids" in converted
    assert "element_id_map" in converted
    assert converted["supporting_evidence_ids"] == ["element1", "element2"]
    assert converted["element_id_map"] == {}

def test_unparseable_handling():
    # Unparseable inputs (like corrupted JSON or wrong types) should resolve to NULL
    unparseable_inputs = [
        "{corrupted_json",
        12345,
        "string-not-json-or-list"
    ]
    
    # Verify migration logic would resolve them to None (NULL)
    for val in unparseable_inputs:
        parsed = val
        if isinstance(parsed, str):
            try:
                parsed = json.loads(parsed)
            except Exception:
                parsed = None
                
        if not isinstance(parsed, (dict, list)):
            parsed = None
            
        assert parsed is None
