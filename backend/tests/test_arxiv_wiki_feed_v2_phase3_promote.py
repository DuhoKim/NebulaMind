import json
from pathlib import Path

import pytest

import scripts.arxiv_wiki_feed_v2_phase3_promote as mod


def label(**extra):
    base = {
        "claim_id": 101,
        "element_id": "claim-101-e01",
        "label": "citable",
        "paper_id": "2501.00001v1",
        "prompt_version": "phase2_prompt",
        "reason": "The abstract supports the element.",
        "section": "Source Section",
        "target_section": "env_quenching",
        "target_section_title": "Environmental quenching",
    }
    base.update(extra)
    return base


def page():
    return {"id": 57, "slug": "galaxy-evolution", "title": "Galaxy Evolution"}


def claim(claim_id=101, **extra):
    base = {
        "id": claim_id,
        "page_id": 57,
        "section": "Source Section",
        "order_idx": 1,
        "text": f"Claim {claim_id} text",
    }
    base.update(extra)
    return base


def paper(arxiv_id="2501.00001v1", paper_id=501, **extra):
    base = {
        "id": paper_id,
        "arxiv_id": arxiv_id,
        "title": f"Paper {arxiv_id}",
        "authors": "A. Author",
        "abstract": "This paper supports the element.",
        "abstract_summary": None,
        "submitted": "2025-01-01",
        "url": f"https://arxiv.org/abs/{arxiv_id}",
    }
    base.update(extra)
    return base


def manifest_for(rows, held_back=None, *, apply_requested=False, approved_by=None, min_rows=30, min_distinct_claims=15, override=None, tmp_path=Path("/tmp")):
    return mod.build_manifest(
        page_slug="galaxy-evolution",
        section="env_quenching",
        labels_path=tmp_path / "LABELS_AFTER_RETRY.jsonl",
        source_run_key="source_run",
        apply_requested=apply_requested,
        approved_by=approved_by,
        min_rows=min_rows,
        min_distinct_claims=min_distinct_claims,
        min_rows_override=override,
        source_channel=mod.DEFAULT_SOURCE_CHANNEL,
        rows=rows,
        held_back_rows=held_back or [],
        schema_drift=[],
        rollback_manifest_path=tmp_path / "rollback_manifest.json",
    )


def promotion_rows(*labels, existing=None):
    labels = list(labels)
    claim_ids = {int(row["claim_id"]) for row in labels}
    arxiv_ids = {mod.clean_arxiv_id(row["paper_id"]) for row in labels}
    claims = {claim_id: claim(claim_id) for claim_id in claim_ids}
    papers = {arxiv_id: paper(arxiv_id, 500 + index) for index, arxiv_id in enumerate(sorted(arxiv_ids), start=1)}
    enriched, drift = mod.enrich_labels(
        labels,
        page=page(),
        claims=claims,
        papers=papers,
        source_run_key="source_run",
        approved_by="HwaO",
        source_channel=mod.DEFAULT_SOURCE_CHANNEL,
    )
    assert drift == []
    return mod.collapse_promotion_units(enriched, existing or {})


def test_dry_run_manifest_shape_is_correct(tmp_path):
    rows, held = promotion_rows(label())
    manifest = manifest_for(rows, held, min_rows=1, min_distinct_claims=1, tmp_path=tmp_path)
    assert manifest["manifest_version"] == mod.MANIFEST_VERSION
    assert manifest["page_slug"] == "galaxy-evolution"
    assert manifest["target_section"] == "env_quenching"
    assert manifest["dry_run"] is True
    assert manifest["apply_requested"] is False
    assert manifest["gate_passes_counts"] is True
    assert manifest["validated_element_pair_count"] == 1
    assert manifest["distinct_claim_count"] == 1
    assert manifest["duplicate_existing_count"] == 0
    assert manifest["rollback_manifest_path"].endswith("rollback_manifest.json")
    row = manifest["rows"][0]
    assert row["proposed_source_channel"] == "arxiv_wiki_feed_v2_element"
    assert row["provenance"]["source"] == "arxiv_wiki_feed_v2_phase3"
    assert row["provenance"]["element_support"][0]["element_id"] == "claim-101-e01"


def test_gate_blocks_apply_when_count_low_without_override(tmp_path):
    rows, held = promotion_rows(label())
    manifest = manifest_for(rows, held, apply_requested=True, approved_by="Papa", min_rows=30, min_distinct_claims=1, tmp_path=tmp_path)
    assert manifest["gate_passes_counts"] is False
    with pytest.raises(SystemExit, match="count gate failed"):
        mod.require_apply_allowed(manifest)


def test_precision_gate_blocks_apply_below_095(tmp_path):
    rows, held = promotion_rows(label())
    manifest = mod.build_manifest(
        page_slug="galaxy-evolution",
        section="env_quenching",
        labels_path=tmp_path / "labels.jsonl",
        source_run_key="source_run",
        apply_requested=True,
        approved_by="Papa",
        min_rows=1,
        min_distinct_claims=1,
        min_rows_override=None,
        source_channel=mod.DEFAULT_SOURCE_CHANNEL,
        rows=rows,
        held_back_rows=held,
        schema_drift=[],
        rollback_manifest_path=tmp_path / "rollback_manifest.json",
        audited_strict_precision=0.94,
    )
    assert manifest["gate_passes_precision"] is False
    with pytest.raises(SystemExit, match="audited precision gate failed"):
        mod.require_apply_allowed(manifest)


def test_off_domain_gate_blocks_apply(tmp_path):
    rows, held = promotion_rows(label())
    manifest = mod.build_manifest(
        page_slug="galaxy-evolution",
        section="env_quenching",
        labels_path=tmp_path / "labels.jsonl",
        source_run_key="source_run",
        apply_requested=True,
        approved_by="Papa",
        min_rows=1,
        min_distinct_claims=1,
        min_rows_override=None,
        source_channel=mod.DEFAULT_SOURCE_CHANNEL,
        rows=rows,
        held_back_rows=held,
        schema_drift=[],
        rollback_manifest_path=tmp_path / "rollback_manifest.json",
        off_domain_promoted_count=1,
    )
    assert manifest["gate_passes_off_domain"] is False
    with pytest.raises(SystemExit, match="off-domain gate failed"):
        mod.require_apply_allowed(manifest)


def test_gate_allows_apply_when_min_rows_override_is_provided(tmp_path):
    rows, held = promotion_rows(label())
    manifest = manifest_for(
        rows,
        held,
        apply_requested=True,
        approved_by="Papa",
        min_rows=30,
        min_distinct_claims=1,
        override="Papa approved env_quenching below 30 rows",
        tmp_path=tmp_path,
    )
    assert manifest["gate_passes_counts"] is True
    mod.require_apply_allowed(manifest)


def test_duplicate_claim_paper_collapse_has_multi_element_provenance():
    rows, held = promotion_rows(
        label(element_id="claim-101-e01", reason="Supports element one."),
        label(element_id="claim-101-e02", reason="Supports element two."),
    )
    assert held == []
    assert len(rows) == 1
    row = rows[0]
    assert row["element_ids"] == ["claim-101-e01", "claim-101-e02"]
    assert len(row["provenance"]["element_support"]) == 2


def test_existing_action1_rows_are_left_untouched():
    existing = {
        (101, "2501.00001v1"): {
            "id": 9001,
            "claim_id": 101,
            "arxiv_id": "2501.00001v1",
            "source_channel": "arxiv_wiki_feed_v2_action1",
            "evidence_status": "production_active",
        }
    }
    rows, held = promotion_rows(label(), existing=existing)
    assert rows == []
    assert len(held) == 1
    assert held[0]["existing_evidence_id"] == 9001
    assert held[0]["existing_source_channel"] == "arxiv_wiki_feed_v2_action1"
    assert held[0]["held_back_reason"] == "existing_evidence_for_claim_arxiv"


class FakeResult:
    def __init__(self, scalar=None, rows=None):
        self.scalar = scalar
        self.rows = rows or []

    def scalar_one(self):
        return self.scalar

    def mappings(self):
        return self.rows


class FakeConn:
    def __init__(self, rollback_path: Path):
        self.rollback_path = rollback_path
        self.insert_seen = False
        self.next_id = 100
        self.sql = []

    def execute(self, statement, params=None):
        sql = str(statement)
        self.sql.append(sql)
        if "SELECT source_channel, count(*)" in sql:
            return FakeResult(rows=[{"source_channel": "arxiv_wiki_feed_v2_action1", "count": 20}])
        if "INSERT INTO" in sql and not self.insert_seen:
            self.insert_seen = True
            assert self.rollback_path.exists()
            payload = json.loads(self.rollback_path.read_text(encoding="utf-8"))
            assert payload["status"] == "prepared_before_db_inserts"
            assert payload["inserted_evidence_ids"] == []
        if "INSERT INTO arxiv_wiki_feed_runs" in sql:
            return FakeResult(scalar=11)
        if "INSERT INTO arxiv_wiki_evidence_candidates" in sql:
            self.next_id += 1
            return FakeResult(scalar=self.next_id)
        if "INSERT INTO evidence" in sql:
            self.next_id += 1
            return FakeResult(scalar=self.next_id)
        return FakeResult()


class FakeBegin:
    def __init__(self, conn):
        self.conn = conn

    def __enter__(self):
        return self.conn

    def __exit__(self, exc_type, exc, tb):
        return False


class FakeEngine:
    def __init__(self, conn):
        self.conn = conn

    def begin(self):
        return FakeBegin(self.conn)


def test_rollback_manifest_is_written_before_any_db_inserts_on_apply(tmp_path):
    rows, held = promotion_rows(label())
    manifest = manifest_for(
        rows,
        held,
        apply_requested=True,
        approved_by="Papa",
        min_rows=30,
        min_distinct_claims=1,
        override="approved small section",
        tmp_path=tmp_path,
    )
    rollback_path = tmp_path / "rollback_manifest.json"
    conn = FakeConn(rollback_path)
    inserted = mod.apply_manifest(
        manifest,
        source_channel=mod.DEFAULT_SOURCE_CHANNEL,
        rollback_path=rollback_path,
        engine=FakeEngine(conn),
    )
    assert inserted["feed_run_id"] == 11
    final_payload = json.loads(rollback_path.read_text(encoding="utf-8"))
    assert final_payload["status"] == "applied"
    assert final_payload["inserted_evidence_ids"]
    assert any("UPDATE arxiv_wiki_evidence_candidates" in sql for sql in conn.sql)
    assert any("'active'" in sql for sql in conn.sql)
