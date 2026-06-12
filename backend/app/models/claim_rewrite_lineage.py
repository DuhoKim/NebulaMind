from __future__ import annotations

from pydantic import BaseModel, Field

class PreservedElementsJson(BaseModel):
    """
    Strict schema for the `preserved_elements_json` field in the
    `claim_rewrite_lineage` table.
    """
    supporting_evidence_ids: list[int] = Field(default_factory=list)
    element_id_map: dict[str, str] = Field(default_factory=dict)
