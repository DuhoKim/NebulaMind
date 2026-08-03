import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from app.agent_loop import frontier_ranking



def _write_delta(engine: Path, rows: list[dict]) -> None:
    delta = engine / "delta"
    delta.mkdir(parents=True, exist_ok=True)
    (delta / "new_papers.jsonl").write_text(
        "".join(json.dumps(row) + "\n" for row in rows),
        encoding="utf-8",
    )
    (delta / "new_labels.json").write_text(
        json.dumps({row["arxiv_id"]: row["cluster"] for row in rows}),
        encoding="utf-8",
    )
    (delta / "new_emb.f32").write_bytes(
        b"\0" * len(rows) * frontier_ranking.EMBEDDING_DIM * 4
    )


def _write_engine_scripts(engine: Path) -> None:
    for name in ("ingest_incremental.py", "rerank_incremental.py", "gen_frontiers_data.py"):
        (engine / name).write_text("# test fixture\n", encoding="utf-8")


def _completed(stdout: str = "ok") -> SimpleNamespace:
    return SimpleNamespace(returncode=0, stdout=stdout, stderr="")


def test_frontier_cli_exposes_daily_ingest_and_weekly_staging_only(monkeypatch, capsys):
    calls = []
    monkeypatch.setattr(
        frontier_ranking,
        "run_daily_frontier_ingest",
        lambda *, limit: calls.append(("daily", limit)) or {"status": "finished"},
    )
    monkeypatch.setattr(
        frontier_ranking,
        "run_weekly_frontier_rerank",
        lambda: calls.append(("weekly", None)) or {
            "status": "finished",
            "live_frontend_updated": False,
        },
    )

    assert frontier_ranking.main(["daily", "--limit", "100"]) == 0
    assert frontier_ranking.main(["weekly"]) == 0
    assert calls == [("daily", 100), ("weekly", None)]
    assert '"live_frontend_updated": false' in capsys.readouterr().out


def test_daily_frontier_ingest_appends_aligned_delta_and_writes_receipt(tmp_path):
    engine = tmp_path / "engine"
    engine.mkdir()
    _write_engine_scripts(engine)
    _write_delta(
        engine,
        [{"arxiv_id": "2607.10000", "cluster": 41, "submitted": "2026-07-22"}],
    )

    def fake_runner(command, *, cwd, timeout, env):
        assert command[-1] == "75"
        assert cwd == engine
        rows = [
            {"arxiv_id": "2607.10000", "cluster": 41, "submitted": "2026-07-22"},
            {"arxiv_id": "2607.20000", "cluster": 54, "submitted": "2026-07-23"},
        ]
        _write_delta(engine, rows)
        return _completed("ingested 1 new papers | assigned 1 | noise/novel 0 | drift-far 0")

    result = frontier_ranking.run_daily_frontier_ingest(
        limit=75,
        engine_dir=engine,
        process_runner=fake_runner,
        now=lambda: "2026-07-23T08:00:00Z",
    )

    assert result["status"] == "finished"
    assert result["before"]["papers"] == 1
    assert result["after"]["papers"] == 2
    assert result["added_papers"] == 1
    assert result["automatic_wiki_integration"] is False
    assert result["live_frontend_updated"] is False
    receipt = Path(result["receipt"])
    assert receipt.exists()
    assert json.loads(receipt.read_text())["added_papers"] == 1


def test_daily_frontier_ingest_refuses_misaligned_existing_store(tmp_path):
    engine = tmp_path / "engine"
    engine.mkdir()
    _write_engine_scripts(engine)
    _write_delta(
        engine,
        [{"arxiv_id": "2607.10000", "cluster": 41, "submitted": "2026-07-22"}],
    )
    (engine / "delta/new_emb.f32").write_bytes(b"broken")

    with pytest.raises(frontier_ranking.FrontierStoreInvariantError, match="embedding bytes"):
        frontier_ranking.run_daily_frontier_ingest(
            engine_dir=engine,
            process_runner=lambda *args, **kwargs: pytest.fail("runner should not execute"),
        )


def test_weekly_rerank_snapshots_previous_state_and_never_writes_live_frontend(tmp_path):
    engine = tmp_path / "engine"
    engine.mkdir()
    _write_engine_scripts(engine)
    _write_delta(
        engine,
        [
            {"arxiv_id": "2607.10000", "cluster": 41, "submitted": "2026-07-22"},
            {"arxiv_id": "2607.20000", "cluster": 54, "submitted": "2026-07-23"},
        ],
    )
    constants = {"a_half": 12.16, "tension_min": 0.026, "tension_max": 0.434, "growth_min": 0.074, "growth_max": 0.458}
    base = {
        "v1_constants": constants,
        "clusters": [
            {"cluster": 41, "tractable": 1, "score_v1": 0.8},
            {"cluster": 54, "tractable": 1, "score_v1": 0.7},
        ],
    }
    previous = {
        **base,
        "constants_frozen": True,
        "rank_comparison": {"reranked_as_of": "2026-07-20", "cumulative_delta_papers": 1},
    }
    (engine / "frontier_map_v3.json").write_text(json.dumps(base), encoding="utf-8")
    previous_path = engine / "frontier_map_v3_reranked.json"
    previous_path.write_text(json.dumps(previous), encoding="utf-8")
    staging = engine / "frontiersData.v3.staging.ts"
    staging.write_text("old staging", encoding="utf-8")
    live = tmp_path / "frontiersData.ts"
    live.write_text("live must not change", encoding="utf-8")
    live_hash = hashlib.sha256(live.read_bytes()).hexdigest()
    calls = []

    def fake_runner(command, *, cwd, timeout, env):
        calls.append(Path(command[1]).name)
        if Path(command[1]).name == "rerank_incremental.py":
            current = {
                **base,
                "clusters": [
                    {"cluster": 41, "tractable": 1, "score_v1": 0.8},
                    {"cluster": 54, "tractable": 1, "score_v1": 0.9},
                ],
                "constants_frozen": True,
                "rank_comparison": {
                    "baseline_as_of": "2026-07-20",
                    "reranked_as_of": "2026-07-23",
                    "delta_papers": 1,
                    "assigned_papers": 1,
                    "cumulative_delta_papers": 2,
                    "cumulative_assigned_papers": 2,
                },
                "rank_movements": {
                    "54": {"cluster": 54, "previousRank": 2, "currentRank": 1, "delta": 1, "deltaPapers": 1},
                    "41": {"cluster": 41, "previousRank": 1, "currentRank": 2, "delta": -1, "deltaPapers": 0},
                },
            }
            previous_path.write_text(json.dumps(current), encoding="utf-8")
        else:
            staging.write_text(
                "export const FRONTIER_RANKING_UPDATE = {};\n"
                "export const FRONTIER_RANK_MOVEMENT = {};\n",
                encoding="utf-8",
            )
        return _completed()

    result = frontier_ranking.run_weekly_frontier_rerank(
        engine_dir=engine,
        live_frontiers_path=live,
        process_runner=fake_runner,
        now=lambda: "2026-07-23T09:00:00Z",
    )

    assert calls == ["rerank_incremental.py", "gen_frontiers_data.py"]
    assert result["status"] == "finished"
    assert result["movement_count"] == 2
    assert result["live_frontend_updated"] is False
    assert hashlib.sha256(live.read_bytes()).hexdigest() == live_hash
    assert Path(result["previous_snapshot"]).exists()
    assert "FRONTIER_RANK_MOVEMENT" in Path(result["staging_path"]).read_text()
    assert Path(result["receipt"]).exists()


def test_weekly_rerank_preserves_staging_when_no_new_papers(tmp_path):
    engine = tmp_path / "engine"
    engine.mkdir()
    _write_engine_scripts(engine)
    rows = [
        {"arxiv_id": "2607.10000", "cluster": 41, "submitted": "2026-07-22"}
    ]
    _write_delta(engine, rows)
    constants = {"a_half": 12.16}
    base = {"v1_constants": constants, "clusters": []}
    reranked = {
        **base,
        "constants_frozen": True,
        "rank_comparison": {
            "reranked_as_of": "2026-07-23",
            "cumulative_delta_papers": 1,
        },
        "rank_movements": {},
    }
    (engine / "frontier_map_v3.json").write_text(json.dumps(base), encoding="utf-8")
    (engine / "frontier_map_v3_reranked.json").write_text(
        json.dumps(reranked), encoding="utf-8"
    )
    staging = engine / "frontiersData.v3.staging.ts"
    staging.write_text(
        "export const FRONTIER_RANKING_UPDATE = {};\n"
        "export const FRONTIER_RANK_MOVEMENT = {};\n",
        encoding="utf-8",
    )
    live = tmp_path / "frontiersData.ts"
    live.write_text("live must not change", encoding="utf-8")

    result = frontier_ranking.run_weekly_frontier_rerank(
        engine_dir=engine,
        live_frontiers_path=live,
        process_runner=lambda *args, **kwargs: pytest.fail("runner should not execute"),
        now=lambda: "2026-07-23T10:00:00Z",
    )

    assert result["status"] == "skipped_no_new_papers"
    assert result["previous_snapshot"] is None
    assert "FRONTIER_RANK_MOVEMENT" in staging.read_text()
    assert live.read_text() == "live must not change"
    assert Path(result["receipt"]).exists()
