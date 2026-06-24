from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_repo_file(path: str) -> str:
    return (REPO_ROOT / path).read_text()


def test_active_evidence_vote_writers_are_canonical_service_only():
    active_paths = [
        "app/agent_loop/tasks.py",
        "app/agent_loop/citation_context/miner.py",
        "app/agent_loop/citation_context/dynamic_miner.py",
        "scripts/targeted_ads_miner.py",
    ]

    for path in active_paths:
        source = read_repo_file(path)
        assert "EvidenceVote(" not in source
        assert "db.add(EvidenceVote" not in source

    service_source = read_repo_file("app/services/trust_mutation.py")
    assert "EvidenceVote(" in service_source


def test_sanctioned_task_paths_use_trust_mutation_service():
    source = read_repo_file("app/agent_loop/tasks.py")

    assert "TrustMutationService.create_or_update_evidence_vote" in source
    assert 'trigger="stance_jury"' in source
    assert 'trigger="jury_single"' in source
    assert 'voter_type="jury"' in source
    assert "recalculate=False" in source
    assert "TrustMutationService.recalculate_evidence_trust" in source


def test_source_finding_paths_are_fenced_as_provisional_no_vote():
    miner_source = read_repo_file("app/agent_loop/citation_context/miner.py")
    dynamic_source = read_repo_file("app/agent_loop/citation_context/dynamic_miner.py")
    targeted_source = read_repo_file("scripts/targeted_ads_miner.py")

    assert "ccm_evidence_inserted_provisional_no_vote" in miner_source
    assert "dccm_evidence_inserted_provisional_no_vote" in dynamic_source
    assert "targeted_ads_evidence_inserted_provisional_no_vote" in targeted_source
    assert "does\nnot create authoritative EvidenceVote rows" in targeted_source
