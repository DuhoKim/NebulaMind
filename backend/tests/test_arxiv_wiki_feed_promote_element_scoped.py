import pytest
import json
import sys
from pathlib import Path
from unittest.mock import MagicMock
from sqlalchemy import text

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import scripts.arxiv_wiki_feed_promote as mod

class MockResult:
    def __init__(self, scalar=None, rows=None):
        self._scalar = scalar
        self._rows = rows or []

    def scalar(self):
        return self._scalar

    def scalar_one(self):
        return self._scalar

    def mappings(self):
        return self

    def first(self):
        return self._rows[0] if self._rows else None

    def all(self):
        return self._rows


class MockConn:
    def __init__(self, claims_db=None, lineage_db=None, evidence_db=None, links_db=None):
        self.claims_db = claims_db or {}
        self.lineage_db = lineage_db or []
        self.evidence_db = evidence_db or {}
        self.links_db = links_db or []
        self.inserted_evidence = []
        self.inserted_links = []
        self.inserted_runs = []
        self.inserted_candidates = []
        self.next_id = 1000

    def execute(self, statement, params=None):
        params = params or {}
        sql = str(statement).strip()

        # 1. SELECT id, page_id, rewrite_status FROM claims
        if "SELECT id, page_id, rewrite_status FROM claims WHERE id = :id" in sql or "SELECT id, rewrite_status FROM claims" in sql:
            claim_id = params.get("id")
            if claim_id in self.claims_db:
                row = self.claims_db[claim_id]
                return MockResult(rows=[{
                    "id": row.get("id"),
                    "page_id": row.get("page_id", 57),
                    "rewrite_status": row.get("rewrite_status")
                }])
            return MockResult(rows=[])

        # 1b. SELECT c.page_id, p.slug
        if "SELECT c.page_id, p.slug" in sql:
            claim_id = params.get("id")
            if claim_id in self.claims_db:
                row = self.claims_db[claim_id]
                return MockResult(rows=[{
                    "page_id": row.get("page_id", 57),
                    "slug": row.get("page_slug", "galaxy-evolution")
                }])
            return MockResult(rows=[])

        # 2. SELECT child_claim_id, preserved_elements_json FROM claim_rewrite_lineage
        if "SELECT child_claim_id, preserved_elements_json" in sql:
            parent_id = params.get("parent_id")
            matches = [
                {"child_claim_id": row["child_claim_id"], "preserved_elements_json": row["preserved_elements_json"]}
                for row in self.lineage_db if row["parent_claim_id"] == parent_id
            ]
            return MockResult(rows=matches)

        # 3. SELECT id FROM evidence
        if "SELECT id FROM evidence" in sql and "evidence_element_links" not in sql:
            claim_id = params.get("claim_id")
            arxiv_id = params.get("arxiv_id")
            match_key = (claim_id, arxiv_id)
            if match_key in self.evidence_db:
                return MockResult(scalar=self.evidence_db[match_key])
            return MockResult(scalar=None)

        # 4. SELECT id FROM evidence_element_links
        if "SELECT id FROM evidence_element_links" in sql:
            target_claim_id = params.get("target_claim_id")
            element_id = params.get("element_id")
            arxiv_id = params.get("arxiv_id")
            for link in self.links_db:
                if (link["target_claim_id"] == target_claim_id and 
                    link["element_id"] == element_id and 
                    link["arxiv_id"] == arxiv_id):
                    return MockResult(scalar=link["id"])
            return MockResult(scalar=None)

        # 8. INSERT INTO arxiv_wiki_evidence_candidates
        if "INSERT INTO arxiv_wiki_evidence_candidates" in sql:
            self.next_id += 1
            self.inserted_candidates.append({
                "id": self.next_id,
                "claim_id": params.get("claim_id")
            })
            return MockResult(scalar=self.next_id)

        # 6. INSERT INTO evidence_element_links
        if "INSERT INTO evidence_element_links" in sql:
            self.next_id += 1
            new_link = {
                "id": self.next_id,
                "evidence_id": params.get("evidence_id"),
                "source_claim_id": params.get("source_claim_id"),
                "target_claim_id": params.get("target_claim_id"),
                "element_id": params.get("element_id"),
                "arxiv_id": params.get("arxiv_id"),
            }
            self.inserted_links.append(new_link)
            self.links_db.append(new_link)
            return MockResult(scalar=self.next_id)

        # 7. INSERT INTO arxiv_wiki_feed_runs
        if "INSERT INTO arxiv_wiki_feed_runs" in sql:
            self.next_id += 1
            self.inserted_runs.append({
                "id": self.next_id,
                "run_key": params.get("run_key")
            })
            return MockResult(scalar=self.next_id)

        # 5. INSERT INTO evidence
        if "INSERT INTO evidence" in sql and "evidence_candidates" not in sql and "evidence_element_links" not in sql:
            self.next_id += 1
            self.inserted_evidence.append({
                "id": self.next_id,
                "claim_id": params.get("claim_id"),
                "arxiv_id": params.get("arxiv_id"),
            })
            self.evidence_db[(params.get("claim_id"), params.get("arxiv_id"))] = self.next_id
            return MockResult(scalar=self.next_id)

        return MockResult()


def test_resolve_target_claim_visible_source():
    claims = {
        100: {"id": 100, "rewrite_status": None},
    }
    conn = MockConn(claims_db=claims)
    target, status, reason = mod.resolve_target_claim(conn, 100, "elem-1")
    assert target == 100
    assert status == "self"
    assert reason is None


def test_resolve_target_claim_parent_replaced_single_child():
    claims = {
        100: {"id": 100, "rewrite_status": "parent_replaced"},
        201: {"id": 201, "rewrite_status": None},
    }
    lineage = [
        {"parent_claim_id": 100, "child_claim_id": 201, "preserved_elements_json": json.dumps({"supporting_evidence_ids": ["elem-1"]})}
    ]
    conn = MockConn(claims_db=claims, lineage_db=lineage)
    target, status, reason = mod.resolve_target_claim(conn, 100, "elem-1")
    assert target == 201
    assert status == "resolved"
    assert "Retargeted via lineage" in reason


def test_resolve_target_claim_parent_replaced_multiple_children_ambiguous():
    claims = {
        100: {"id": 100, "rewrite_status": "parent_replaced"},
        201: {"id": 201, "rewrite_status": None},
        202: {"id": 202, "rewrite_status": None},
    }
    lineage = [
        {"parent_claim_id": 100, "child_claim_id": 201, "preserved_elements_json": json.dumps({"supporting_evidence_ids": ["elem-1"]})},
        {"parent_claim_id": 100, "child_claim_id": 202, "preserved_elements_json": json.dumps({"supporting_evidence_ids": ["elem-1"]})},
    ]
    conn = MockConn(claims_db=claims, lineage_db=lineage)
    target, status, reason = mod.resolve_target_claim(conn, 100, "elem-1")
    assert target is None
    assert status == "ambiguous"
    assert "multiple visible matching" in reason


def test_resolve_target_claim_parent_replaced_no_match():
    claims = {
        100: {"id": 100, "rewrite_status": "parent_replaced"},
        201: {"id": 201, "rewrite_status": None},
    }
    lineage = [
        {"parent_claim_id": 100, "child_claim_id": 201, "preserved_elements_json": json.dumps({"supporting_evidence_ids": ["elem-2"]})}
    ]
    conn = MockConn(claims_db=claims, lineage_db=lineage)
    target, status, reason = mod.resolve_target_claim(conn, 100, "elem-1")
    assert target is None
    assert status == "not_found"
    assert "No visible child claim matches" in reason


def test_promote_element_scoped_dry_run():
    claims = {
        100: {"id": 100, "rewrite_status": None},
    }
    conn = MockConn(claims_db=claims)
    manifest = {
        "source_validator_path": "/tmp/validator.jsonl",
        "rows": [
            {
                "candidate": {
                    "claim_id": 100,
                    "element_id": "elem-1",
                    "page_id": 57,
                    "page_slug": "galaxy-evolution",
                    "arxiv_id": "2501.00001",
                    "status": "validated_ready",
                    "paper_title_snapshot": "Test Paper",
                }
            }
        ]
    }
    counters = mod.promote_element_scoped(manifest, conn, dry_run=True)
    assert counters["evidence_rows_inserted"] == 1
    assert counters["evidence_rows_reused"] == 0
    assert counters["element_links_inserted"] == 1
    assert counters["element_links_skipped_duplicate"] == 0
    assert counters["rewrite_resolution_skipped"] == 0
    assert counters["rewrite_resolution_failed"] == 0
    
    assert len(conn.inserted_evidence) == 0
    assert len(conn.inserted_links) == 0


def test_promote_element_scoped_real_apply_freezes_without_override(monkeypatch):
    monkeypatch.delenv(mod.MANUAL_PROMOTER_FREEZE_ENV, raising=False)
    conn = MockConn(claims_db={100: {"id": 100, "rewrite_status": None}})
    manifest = {
        "source_validator_path": "/tmp/validator.jsonl",
        "rows": [
            {
                "candidate": {
                    "claim_id": 100,
                    "element_id": "elem-1",
                    "page_id": 57,
                    "page_slug": "galaxy-evolution",
                    "arxiv_id": "2501.00001",
                    "status": "validated_ready",
                    "paper_title_snapshot": "Test Paper",
                }
            }
        ],
    }

    with pytest.raises(SystemExit, match="Evidence promotion is frozen"):
        mod.promote_element_scoped(manifest, conn, dry_run=False)

    assert len(conn.inserted_evidence) == 0
    assert len(conn.inserted_links) == 0


def test_promote_element_scoped_real_apply_and_idempotency(monkeypatch):
    monkeypatch.setenv(mod.MANUAL_PROMOTER_FREEZE_ENV, "1")
    claims = {
        100: {"id": 100, "rewrite_status": None},
    }
    conn = MockConn(claims_db=claims)
    manifest = {
        "source_validator_path": "/tmp/validator.jsonl",
        "rows": [
            {
                "candidate": {
                    "claim_id": 100,
                    "element_id": "elem-1",
                    "page_id": 57,
                    "page_slug": "galaxy-evolution",
                    "arxiv_id": "2501.00001",
                    "status": "validated_ready",
                    "paper_title_snapshot": "Test Paper",
                }
            }
        ]
    }
    
    counters_1 = mod.promote_element_scoped(manifest, conn, dry_run=False)
    assert counters_1["evidence_rows_inserted"] == 1
    assert counters_1["evidence_rows_reused"] == 0
    assert counters_1["element_links_inserted"] == 1
    assert counters_1["element_links_skipped_duplicate"] == 0
    
    assert len(conn.inserted_evidence) == 1
    assert len(conn.inserted_links) == 1

    counters_2 = mod.promote_element_scoped(manifest, conn, dry_run=False)
    assert counters_2["evidence_rows_inserted"] == 0
    assert counters_2["evidence_rows_reused"] == 1
    assert counters_2["element_links_inserted"] == 0
    assert counters_2["element_links_skipped_duplicate"] == 1
    
    assert len(conn.inserted_evidence) == 1
    assert len(conn.inserted_links) == 1
