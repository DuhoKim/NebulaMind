"""Scheduled staging-only frontier intake and ranking tasks.

These tasks keep the immutable full-cluster snapshot separate from the incremental
arXiv delta. Daily work appends embeddings and cluster assignments to ``delta/``.
Weekly work snapshots the prior rerank, recomputes against frozen normalization
constants, and generates only ``frontiersData.v3.staging.ts``. Nothing here writes
the live frontend or any wiki/database table.
"""

from __future__ import annotations

import datetime as dt
import argparse
import fcntl
import hashlib
import json
import os
import re
from contextlib import contextmanager
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Callable

from celery import shared_task

EMBEDDING_DIM = 2560
DAILY_TIMEOUT_SECONDS = 1200
WEEKLY_TIMEOUT_SECONDS = 300
_ENGINE_RELATIVE_PATH = Path(
    ".hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718"
)


class FrontierPipelineError(RuntimeError):
    """Base error for frontier staging automation."""


class FrontierPipelineBusy(FrontierPipelineError):
    """Raised when another frontier intake/rerank process owns the shared lock."""


class FrontierStoreInvariantError(FrontierPipelineError):
    """Raised when delta files or generated ranking artifacts are inconsistent."""


def _default_engine_dir() -> Path:
    configured = os.getenv("NEBULAMIND_FRONTIER_ENGINE_DIR")
    if configured:
        return Path(configured).expanduser().resolve()
    return (Path(__file__).parents[3] / _ENGINE_RELATIVE_PATH).resolve()


def _default_live_frontiers_path() -> Path:
    return (
        Path(__file__).parents[3]
        / "frontend/src/app/lab/frontiersData.ts"
    ).resolve()


def _utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _timestamp_slug(value: str) -> str:
    return value.replace("-", "").replace(":", "")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _atomic_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


@contextmanager
def _exclusive_pipeline_lock(engine_dir: Path):
    lock_path = engine_dir / ".frontier_pipeline.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+") as handle:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise FrontierPipelineBusy(
                f"frontier pipeline already running: {lock_path}"
            ) from exc
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def _read_json_lines(path: Path) -> list[dict]:
    rows = []
    if not path.exists():
        return rows
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise FrontierStoreInvariantError(
                f"invalid JSONL at {path}:{line_number}: {exc}"
            ) from exc
        if not isinstance(row, dict) or not row.get("arxiv_id"):
            raise FrontierStoreInvariantError(
                f"invalid paper record at {path}:{line_number}"
            )
        rows.append(row)
    return rows


def inspect_delta_store(engine_dir: Path) -> dict:
    delta_dir = engine_dir / "delta"
    papers_path = delta_dir / "new_papers.jsonl"
    labels_path = delta_dir / "new_labels.json"
    embeddings_path = delta_dir / "new_emb.f32"

    papers = _read_json_lines(papers_path)
    paper_ids = [str(row["arxiv_id"]) for row in papers]
    if len(paper_ids) != len(set(paper_ids)):
        raise FrontierStoreInvariantError("delta store contains duplicate arXiv IDs")

    if labels_path.exists():
        try:
            labels = json.loads(labels_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise FrontierStoreInvariantError(f"invalid label index: {exc}") from exc
    else:
        labels = {}
    if not isinstance(labels, dict):
        raise FrontierStoreInvariantError("label index must be a JSON object")
    if set(labels) != set(paper_ids):
        raise FrontierStoreInvariantError(
            f"label IDs do not match paper IDs: labels={len(labels)} papers={len(paper_ids)}"
        )

    embedding_bytes = embeddings_path.stat().st_size if embeddings_path.exists() else 0
    expected_embedding_bytes = len(papers) * EMBEDDING_DIM * 4
    if embedding_bytes != expected_embedding_bytes:
        raise FrontierStoreInvariantError(
            "embedding bytes do not match paper count: "
            f"actual={embedding_bytes} expected={expected_embedding_bytes}"
        )

    assigned = sum(1 for row in papers if int(row.get("cluster", -1)) != -1)
    submitted = sorted(
        str(row["submitted"])[:10] for row in papers if row.get("submitted")
    )
    return {
        "papers": len(papers),
        "labels": len(labels),
        "embedding_bytes": embedding_bytes,
        "assigned": assigned,
        "novel_or_noise": len(papers) - assigned,
        "submitted_from": submitted[0] if submitted else None,
        "submitted_to": submitted[-1] if submitted else None,
    }


def _run_process(
    command: list[str],
    *,
    cwd: Path,
    timeout: int,
    env: dict[str, str],
):
    completed = subprocess.run(
        command,
        cwd=cwd,
        timeout=timeout,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout or "no process output")[-4000:]
        raise FrontierPipelineError(
            f"{Path(command[1]).name} failed with exit {completed.returncode}: {detail}"
        )
    return completed


def _require_files(engine_dir: Path, names: tuple[str, ...]) -> None:
    missing = [name for name in names if not (engine_dir / name).is_file()]
    if missing:
        raise FrontierPipelineError(
            f"frontier engine missing required files: {', '.join(missing)}"
        )


def _receipt_path(engine_dir: Path, lane: str, now_value: str) -> Path:
    return engine_dir / "receipts" / f"{lane}_{_timestamp_slug(now_value)}.json"


def run_daily_frontier_ingest(
    *,
    limit: int = 100,
    engine_dir: Path | None = None,
    process_runner: Callable = _run_process,
    now: Callable[[], str] = _utc_now,
) -> dict:
    engine = (engine_dir or _default_engine_dir()).resolve()
    _require_files(engine, ("ingest_incremental.py",))
    if not 1 <= int(limit) <= 500:
        raise ValueError("frontier daily ingest limit must be between 1 and 500")

    with _exclusive_pipeline_lock(engine):
        before = inspect_delta_store(engine)
        environment = dict(os.environ)
        environment["NEBULAMIND_FRONTIER_LOCK_HELD"] = "1"
        completed = process_runner(
            [sys.executable, str(engine / "ingest_incremental.py"), str(int(limit))],
            cwd=engine,
            timeout=DAILY_TIMEOUT_SECONDS,
            env=environment,
        )
        after = inspect_delta_store(engine)
        added = after["papers"] - before["papers"]
        if added < 0:
            raise FrontierStoreInvariantError(
                f"daily ingest removed papers: before={before['papers']} after={after['papers']}"
            )
        now_value = now()
        receipt = _receipt_path(engine, "daily_frontier_ingest", now_value)
        result = {
            "status": "finished",
            "lane": "daily_frontier_ingest",
            "generated_at": now_value,
            "before": before,
            "after": after,
            "added_papers": added,
            "automatic_wiki_integration": False,
            "live_frontend_updated": False,
            "stdout_tail": (completed.stdout or "")[-2000:],
            "receipt": str(receipt),
        }
        _atomic_json(receipt, result)
        return result


def _snapshot_previous_rerank(engine: Path, previous_path: Path) -> Path:
    digest = _sha256(previous_path)
    snapshot = engine / "snapshots" / f"frontier_map_v3_reranked_{digest[:16]}.json"
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    if not snapshot.exists():
        temporary = snapshot.with_name(f".{snapshot.name}.{os.getpid()}.tmp")
        shutil.copyfile(previous_path, temporary)
        os.replace(temporary, snapshot)
    return snapshot


def _previous_delta_count(document: dict) -> int:
    comparison = document.get("rank_comparison") or {}
    for key in ("cumulative_delta_papers", "delta_papers"):
        value = comparison.get(key)
        if isinstance(value, int) and value >= 0:
            return value
    match = re.search(
        r"base \+ delta \((\d+) arXiv preprints",
        str(document.get("reranked_over", "")),
    )
    return int(match.group(1)) if match else 0


def _validate_rerank(engine: Path) -> tuple[dict, dict]:
    base = json.loads((engine / "frontier_map_v3.json").read_text(encoding="utf-8"))
    reranked = json.loads(
        (engine / "frontier_map_v3_reranked.json").read_text(encoding="utf-8")
    )
    if reranked.get("constants_frozen") is not True:
        raise FrontierStoreInvariantError("rerank did not declare constants_frozen=true")
    if reranked.get("v1_constants") != base.get("v1_constants"):
        raise FrontierStoreInvariantError("rerank changed frozen v1 constants")
    comparison = reranked.get("rank_comparison")
    movements = reranked.get("rank_movements")
    if not isinstance(comparison, dict):
        raise FrontierStoreInvariantError("rerank is missing rank_comparison metadata")
    if not isinstance(movements, dict):
        raise FrontierStoreInvariantError("rerank is missing rank_movements metadata")
    return comparison, movements


def run_weekly_frontier_rerank(
    *,
    engine_dir: Path | None = None,
    live_frontiers_path: Path | None = None,
    process_runner: Callable = _run_process,
    now: Callable[[], str] = _utc_now,
) -> dict:
    engine = (engine_dir or _default_engine_dir()).resolve()
    live_path = (live_frontiers_path or _default_live_frontiers_path()).resolve()
    _require_files(
        engine,
        (
            "rerank_incremental.py",
            "gen_frontiers_data.py",
            "frontier_map_v3.json",
            "frontier_map_v3_reranked.json",
        ),
    )
    if not live_path.is_file():
        raise FrontierPipelineError(f"live frontier data file is missing: {live_path}")

    with _exclusive_pipeline_lock(engine):
        delta_state = inspect_delta_store(engine)
        previous_path = engine / "frontier_map_v3_reranked.json"
        previous_document = json.loads(previous_path.read_text(encoding="utf-8"))
        previous_delta_count = _previous_delta_count(previous_document)
        if previous_delta_count > delta_state["papers"]:
            raise FrontierStoreInvariantError(
                "prior rerank contains more delta papers than the current store: "
                f"prior={previous_delta_count} current={delta_state['papers']}"
            )
        staging_path = engine / "frontiersData.v3.staging.ts"
        staging_ready = staging_path.is_file() and all(
            marker in staging_path.read_text(encoding="utf-8")
            for marker in ("FRONTIER_RANKING_UPDATE", "FRONTIER_RANK_MOVEMENT")
        )
        if previous_delta_count == delta_state["papers"] and staging_ready:
            live_hash = _sha256(live_path)
            now_value = now()
            receipt = _receipt_path(engine, "weekly_frontier_rerank", now_value)
            result = {
                "status": "skipped_no_new_papers",
                "lane": "weekly_frontier_rerank",
                "generated_at": now_value,
                "comparison": previous_document.get("rank_comparison") or {},
                "movement_count": 0,
                "previous_snapshot": None,
                "staging_path": str(staging_path),
                "staging_sha256": _sha256(staging_path),
                "live_frontend_sha256": live_hash,
                "live_frontend_updated": False,
                "automatic_wiki_integration": False,
                "receipt": str(receipt),
            }
            _atomic_json(receipt, result)
            return result
        previous_snapshot = _snapshot_previous_rerank(engine, previous_path)
        live_hash_before = _sha256(live_path)
        environment = dict(os.environ)
        environment["NEBULAMIND_FRONTIER_LOCK_HELD"] = "1"

        rerank_result = process_runner(
            [sys.executable, str(engine / "rerank_incremental.py")],
            cwd=engine,
            timeout=WEEKLY_TIMEOUT_SECONDS,
            env=environment,
        )
        comparison, movements = _validate_rerank(engine)
        generator_result = process_runner(
            [sys.executable, str(engine / "gen_frontiers_data.py")],
            cwd=engine,
            timeout=WEEKLY_TIMEOUT_SECONDS,
            env=environment,
        )

        staging_path = engine / "frontiersData.v3.staging.ts"
        if not staging_path.is_file() or staging_path.stat().st_size == 0:
            raise FrontierStoreInvariantError("frontier generator did not produce staging data")
        staging_source = staging_path.read_text(encoding="utf-8")
        if (
            "FRONTIER_RANKING_UPDATE" not in staging_source
            or "FRONTIER_RANK_MOVEMENT" not in staging_source
        ):
            raise FrontierStoreInvariantError(
                "staging data is missing rank update or movement exports"
            )
        live_hash_after = _sha256(live_path)
        if live_hash_after != live_hash_before:
            raise FrontierStoreInvariantError(
                "weekly staging task modified the live frontend data file"
            )

        now_value = now()
        receipt = _receipt_path(engine, "weekly_frontier_rerank", now_value)
        result = {
            "status": "finished",
            "lane": "weekly_frontier_rerank",
            "generated_at": now_value,
            "comparison": comparison,
            "movement_count": len(movements),
            "previous_snapshot": str(previous_snapshot),
            "staging_path": str(staging_path),
            "staging_sha256": _sha256(staging_path),
            "live_frontend_sha256": live_hash_after,
            "live_frontend_updated": False,
            "automatic_wiki_integration": False,
            "rerank_stdout_tail": (rerank_result.stdout or "")[-2000:],
            "generator_stdout_tail": (generator_result.stdout or "")[-2000:],
            "receipt": str(receipt),
        }
        _atomic_json(receipt, result)
        return result


@shared_task(name="app.agent_loop.frontier_ranking.ingest_daily")
def ingest_daily(limit: int = 100):
    return run_daily_frontier_ingest(limit=limit)


@shared_task(name="app.agent_loop.frontier_ranking.rerank_weekly")
def rerank_weekly():
    return run_weekly_frontier_rerank()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the staging-only frontier pipeline")
    subparsers = parser.add_subparsers(dest="lane", required=True)
    daily_parser = subparsers.add_parser("daily", help="ingest recent GA/CO papers")
    daily_parser.add_argument("--limit", type=int, default=100)
    subparsers.add_parser("weekly", help="rerank and generate staging data")
    args = parser.parse_args(argv)
    if args.lane == "daily":
        result = run_daily_frontier_ingest(limit=args.limit)
    else:
        result = run_weekly_frontier_rerank()
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
