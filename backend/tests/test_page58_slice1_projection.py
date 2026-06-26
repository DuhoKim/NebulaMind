import argparse
import json

from app.services.sentence_trust import project_sentence_trust
from scripts import page58_sentence_vote_staking_dry_run as slice1
from scripts.page58_sentence_vote_staking_dry_run import rollup, write_report


def test_slice1_rollup_skips_seed_duplicate_paper_stakes():
    base_rows = [
        {
            "page_version_id": 6197,
            "sentence_index": 4,
            "sentence_hash": "hash-4",
            "sentence_text": "Seed sentence with existing paper provenance.",
            "trust_level": "accepted",
            "settled_votes": 2,
            "contested_votes": 0,
            "existing_arxiv_ids": ["2401.00001", "2401.00002"],
        }
    ]
    votes = [
        {
            "sentence_index": 4,
            "arxiv_id": "2401.00001",
            "tone_tier": "accepted",
            "tone_confidence": 0.95,
        },
        {
            "sentence_index": 4,
            "arxiv_id": "2401.00003",
            "tone_tier": "accepted",
            "tone_confidence": 0.93,
        },
    ]

    row = rollup(base_rows, votes, tau_vote=0.70)[0]
    expected = project_sentence_trust(
        settled_votes=3,
        contested_votes=0,
        distinct_sources=3,
    )

    assert row["new_pro_votes"] == 1
    assert row["new_con_votes"] == 0
    assert row["seed_duplicate_stakes_skipped"] == 1
    assert row["would_be_settled_votes"] == expected["settled_votes"]
    assert row["would_be_contested_votes"] == expected["contested_votes"]
    assert row["would_be_vote_count"] == expected["vote_count"]
    assert row["would_be_trust_level"] == expected["trust_level"]
    assert row["single_source"] is expected["single_source"]
    assert row["contested_veto"] is expected["contested_veto"]


def test_slice1_rollup_preserves_seed_duplicate_skip_when_dropping_con_votes():
    base_rows = [
        {
            "page_version_id": 6197,
            "sentence_index": 5,
            "sentence_hash": "hash-5",
            "sentence_text": "Seed sentence with a debated baseline.",
            "trust_level": "debated",
            "settled_votes": 2,
            "contested_votes": 1,
            "existing_arxiv_ids": ["2401.01001", "2401.01002", "2401.01003"],
        }
    ]
    votes = [
        {
            "sentence_index": 5,
            "arxiv_id": "2401.01003",
            "tone_tier": "challenged",
            "tone_confidence": 0.96,
        },
        {
            "sentence_index": 5,
            "arxiv_id": "2401.01004",
            "tone_tier": "challenged",
            "tone_confidence": 0.96,
        },
    ]

    row = rollup(base_rows, votes, tau_vote=0.70, drop_con=True)[0]
    expected = project_sentence_trust(
        settled_votes=2,
        contested_votes=1,
        distinct_sources=3,
    )

    assert row["new_pro_votes"] == 0
    assert row["new_con_votes"] == 0
    assert row["seed_duplicate_stakes_skipped"] == 1
    assert row["would_be_contested_votes"] == expected["contested_votes"]
    assert row["would_be_vote_count"] == expected["vote_count"]
    assert row["would_be_trust_level"] == expected["trust_level"]


def test_slice1_summary_counts_include_seed_duplicate_skip_total():
    counts = slice1.summarize_rollup_counts([
        {"new_pro_votes": 1, "new_con_votes": 0, "refine_tally": 2, "seed_duplicate_stakes_skipped": 3},
        {"new_pro_votes": 0, "new_con_votes": 1, "refine_tally": 0, "seed_duplicate_stakes_skipped": 4},
    ])

    assert counts == {
        "new_votes": 2,
        "new_pro_votes": 1,
        "new_con_votes": 1,
        "refine_tally": 2,
        "seed_duplicate_stakes_skipped": 7,
    }


def test_slice1_git_head_observed_is_best_effort(monkeypatch):
    def raise_after_expensive_dry_run(*_args, **_kwargs):
        raise FileNotFoundError("git unavailable")

    monkeypatch.setattr(slice1.subprocess, "check_output", raise_after_expensive_dry_run)

    assert slice1.observed_git_head() == "unknown"


def test_slice1_report_surfaces_seed_duplicate_skip_count(tmp_path):
    summary = {
        "ratios": {
            "intros_staked": "1/2",
            "intros_no_op": "1/2",
            "intros_no_match_emergent_pool": "0/2",
            "finding_sentences_kept": "2/3",
            "finding_sentences_filtered": "1/3",
            "provenance_coverage": "1/1",
            "settled_share": "3/3",
        },
        "sensitivity": {
            "trust_tier_changes_if_con_votes_dropped": "0/1",
            "trust_tier_changes_if_tau_vote_minus_0_10": "0/1",
            "trust_tier_changes_if_tau_vote_plus_0_10": "0/1",
        },
        "timings": {"total_seconds": 0.01},
        "counts": {"seed_duplicate_stakes_skipped": 2, "checkpoint_files_written": 4},
        "progress": {"progress_log": "progress.jsonl", "checkpoint_dir": "checkpoints"},
        "db_write_count": 0,
        "no_apply": True,
        "local_only": True,
        "paid_lane_touched": False,
        "claude_p_used": False,
    }
    trust_rows = [
        {
            "sentence_index": 4,
            "sentence_text": "Seed sentence.",
            "new_pro_votes": 1,
            "new_con_votes": 0,
            "seed_duplicate_stakes_skipped": 2,
            "refine_tally": 0,
            "no_op_tally": 0,
            "would_be_trust_level": "consensus",
            "would_be_tone_tier": "settled",
            "baseline_trust_level": "accepted",
            "settled_share": 1.0,
            "single_source": False,
            "contested_veto": False,
        }
    ]
    path = tmp_path / "REPORT.md"

    write_report(path, summary, trust_rows)

    report = path.read_text(encoding="utf-8")
    assert "- Seed duplicate stakes skipped: 2." in report
    assert "seed duplicate stakes skipped 2" in report
    assert "- Progress log: progress.jsonl" in report
    assert "- Checkpoint directory: checkpoints" in report
    assert "- Checkpoint files written before final report: 4" in report


def test_slice1_progress_event_appends_jsonl_and_prints_operator_line(tmp_path, capsys):
    event = slice1.record_progress(
        tmp_path,
        "claim_filter_intro",
        "running",
        processed_intros=3,
        total_intros=10,
        no_apply=True,
        db_write_count=0,
    )

    lines = (tmp_path / "progress.jsonl").read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1
    persisted = json.loads(lines[0])
    assert persisted["stage"] == "claim_filter_intro"
    assert persisted["status"] == "running"
    assert persisted["processed_intros"] == 3
    assert persisted["total_intros"] == 10
    assert persisted["no_apply"] is True
    assert persisted["db_write_count"] == 0
    assert persisted["created_at"] == event["created_at"]
    stderr = capsys.readouterr().err
    assert "PAGE58_PROGRESS" in stderr
    assert "claim_filter_intro" in stderr


def test_slice1_run_writes_operator_checkpoints_before_final_artifacts(tmp_path, monkeypatch):
    base_rows = [
        {
            "page_version_id": 6189,
            "sentence_index": 0,
            "sentence_hash": "hash-0",
            "sentence_text": "AGN feedback heats gas and can suppress star formation in galaxies.",
            "trust_level": "debated",
            "settled_votes": 2,
            "contested_votes": 1,
            "existing_arxiv_ids": ["2401.00001"],
        }
    ]
    intros = [
        {
            "arxiv_id": "2401.99999",
            "intro_text": "We find that AGN feedback heats circumgalactic gas and suppresses star formation in massive galaxies.",
            "source": "test",
            "fetched_at": "2026-06-26T00:00:00Z",
        }
    ]
    meta = {"page": {"id": 58, "slug": "galaxy-evolution-v2"}, "page_version": {"id": 6189, "version_num": 1}}

    monkeypatch.setattr(slice1, "load_base_and_intros", lambda limit: (base_rows, intros, meta))
    monkeypatch.setattr(slice1, "embed_texts", lambda texts, timeout=180: [[1.0, 0.0] for _ in texts])
    monkeypatch.setattr(
        slice1,
        "atom_claim_filter",
        lambda sentences, timeout: [
            {
                "sentence": sentences[0],
                "finding": True,
                "confidence": 0.91,
                "source": "test_claim_filter",
                "reason": "test",
            }
        ],
    )
    monkeypatch.setattr(
        slice1,
        "tone_gate_predictions",
        lambda pairs, timeout: [
            {
                **pairs[0],
                "tone_tier": "accepted",
                "tone_confidence": 0.95,
            }
        ],
    )

    summary = slice1.run(
        argparse.Namespace(
            no_apply=True,
            limit_intros=1,
            tau_rel=0.55,
            tau_vote=0.70,
            model_timeout=1,
            out_dir=tmp_path,
        )
    )

    progress = [json.loads(line) for line in (tmp_path / "progress.jsonl").read_text(encoding="utf-8").splitlines()]
    stages = [event["stage"] for event in progress]
    assert stages[0] == "start"
    assert "load_base_and_intros" in stages
    assert "claim_filter_intro" in stages
    assert "claim_filter_done" in stages
    assert "embedding_match_done" in stages
    assert "tone_gate_done" in stages
    assert stages[-1] == "final_artifacts_done"
    assert all(event["no_apply"] is True for event in progress)
    assert all(event["db_write_count"] == 0 for event in progress)

    checkpoint_dir = tmp_path / "checkpoints"
    assert json.loads((checkpoint_dir / "load_base_and_intros.json").read_text(encoding="utf-8"))["input_intros"] == 1
    assert json.loads((checkpoint_dir / "claim_filter.json").read_text(encoding="utf-8"))["finding_sentences"] == 1
    assert (checkpoint_dir / "candidate_pairs.jsonl").read_text(encoding="utf-8").strip()
    assert (checkpoint_dir / "tone_gate_predictions.jsonl").read_text(encoding="utf-8").strip()
    assert summary["progress"]["progress_log"].endswith("progress.jsonl")
    assert summary["progress"]["checkpoint_dir"].endswith("checkpoints")
    assert summary["counts"]["checkpoint_files_written"] >= 4
