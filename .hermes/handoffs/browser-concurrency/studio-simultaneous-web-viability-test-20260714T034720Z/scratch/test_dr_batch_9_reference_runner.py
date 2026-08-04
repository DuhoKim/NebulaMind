import hashlib
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import dr_batch_9_reference_runner as runner


def test_discovers_exact_ordered_manifest_and_output_names():
    specs = runner.discover_prompts()
    assert [item["paper_id"] for item in specs] == [f"paper_{index:02d}" for index in range(1, 10)]
    assert specs[0]["prompt_file_sha256"] == "bf0e95d7891257bcfe2485cff8125dc7530c6f1c92cc7356533cf5c0102ffcb6"
    assert specs[-1]["prompt_file_sha256"] == "717d6ba9891c1bf30d29dd01ba8486a2877c9e3a142f1cba2ae5b3bbd0b15e51"
    for item in specs:
        assert Path(item["packet_path"]).name.startswith(item["paper_id"] + "_")
        assert Path(item["packet_path"]).name.endswith("_dr_packet.md")
        assert Path(item["metadata_path"]).name.endswith("_dr_packet.metadata.json")
        assert item["prompt_chars"] > 5000
        assert len(item["prompt_sha256"]) == 64


def test_write_guard_allows_only_reference_md_json_under_packet_root():
    runner.assert_allowed_write(runner.PACKET_DIR / "paper_01_test_dr_packet.md")
    runner.assert_allowed_write(runner.PACKET_DIR / "paper_01_test_dr_packet.metadata.json")
    with pytest.raises(RuntimeError):
        runner.assert_allowed_write(runner.BATCH_ROOT / "candidate.tex")
    with pytest.raises(RuntimeError):
        runner.assert_allowed_write(runner.PACKET_DIR / "candidate.tex")
    with pytest.raises(RuntimeError):
        runner.assert_allowed_write(Path("/tmp/outside.md"))


def test_output_scan_detects_four_section_contract_and_sources():
    sample = """Section 1 - Source-Grounded Literature Packet
Source 1: Example et al. (2024)
Identifier: 10.1234/example.1 arXiv: 2401.12345
Role: method-support
Stance / Rationale: useful.
Section 2 - Missing Real Observables Assessment
Section 3 - Wording Improvements and Citation Insertions
Section 4 - No-Mock-Data Receipt and Safety Ledger
No mock or synthetic data.
"""
    scan = runner.output_scan(sample)
    assert all(scan[f"section_{index}_present"] for index in range(1, 5))
    assert scan["source_blocks"] == 1
    assert scan["identifier_fields"] == 1
    assert scan["role_fields"] == 1
    assert scan["stance_rationale_fields"] == 1
    assert scan["no_mock_receipt_present"] is True
    assert "2401.12345" in scan["arxiv_like_ids"]


def test_source_filter_and_normalization():
    assert runner.keep_source({"href": "https://arxiv.org/abs/2401.12345", "label": "paper"})
    assert not runner.keep_source({"href": "https://gemini.google.com/app/abc", "label": "chat"})
    assert runner.normalized("a\n  b\t c") == "a b c"


def test_saved_result_identity_requires_exact_hash_and_length():
    report = "terminal sourced report"
    digest = hashlib.sha256(report.encode()).hexdigest()
    assert runner.result_text_identity(report, digest, len(report))
    assert not runner.result_text_identity(report + " drift", digest, len(report))
    assert not runner.result_text_identity(report, "0" * 64, len(report))


def test_post_delete_stale_row_requires_settlement_reload():
    old = "/app/owned"
    assert runner.needs_deletion_settlement_reload("/app", old, 1)
    assert not runner.needs_deletion_settlement_reload("/app", old, 0)
    assert not runner.needs_deletion_settlement_reload(old, old, 1)
