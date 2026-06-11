"""Best-effort DB ledger for scheduled pipeline task executions."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from typing import Any

from sqlalchemy import text

from app.database import SessionLocal

log = logging.getLogger(__name__)


def _json_safe(value: Any) -> str | None:
    if value is None:
        return None
    try:
        return json.dumps(value, default=str)[:20_000]
    except Exception:
        return json.dumps({"repr": repr(value)[:2_000]})


def ensure_pipeline_runs_table(db) -> None:
    db.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS pipeline_runs (
                id SERIAL PRIMARY KEY,
                task_name VARCHAR(200) NOT NULL,
                task_id VARCHAR(80),
                schedule_name VARCHAR(120),
                status VARCHAR(20) NOT NULL DEFAULT 'running',
                started_at TIMESTAMP NOT NULL DEFAULT NOW(),
                finished_at TIMESTAMP,
                duration_ms INTEGER,
                args_json TEXT,
                kwargs_json TEXT,
                result_json TEXT,
                error_text TEXT
            )
            """
        )
    )
    db.execute(
        text(
            """
            CREATE INDEX IF NOT EXISTS idx_pipeline_runs_task_started
            ON pipeline_runs (task_name, started_at DESC)
            """
        )
    )
    db.execute(
        text(
            """
            CREATE UNIQUE INDEX IF NOT EXISTS idx_pipeline_runs_task_id
            ON pipeline_runs (task_id)
            WHERE task_id IS NOT NULL
            """
        )
    )


def start_pipeline_run(
    *,
    task_name: str,
    task_id: str | None,
    schedule_name: str | None = None,
    args: Any = None,
    kwargs: Any = None,
) -> int | None:
    db = SessionLocal()
    try:
        ensure_pipeline_runs_table(db)
        row = db.execute(
            text(
                """
                INSERT INTO pipeline_runs (
                    task_name, task_id, schedule_name, status, started_at,
                    args_json, kwargs_json
                )
                VALUES (
                    :task_name, :task_id, :schedule_name, 'running', NOW(),
                    :args_json, :kwargs_json
                )
                ON CONFLICT (task_id) WHERE task_id IS NOT NULL DO UPDATE
                SET status = 'running',
                    started_at = NOW(),
                    finished_at = NULL,
                    duration_ms = NULL,
                    error_text = NULL
                RETURNING id
                """
            ),
            {
                "task_name": task_name,
                "task_id": task_id,
                "schedule_name": schedule_name,
                "args_json": _json_safe(args),
                "kwargs_json": _json_safe(kwargs),
            },
        ).fetchone()
        db.commit()
        return int(row[0]) if row else None
    except Exception as exc:
        db.rollback()
        log.warning("pipeline run start failed for %s/%s: %s", task_name, task_id, exc)
        return None
    finally:
        db.close()


def finish_pipeline_run(
    *,
    run_id: int | None = None,
    task_id: str | None = None,
    status: str,
    result: Any = None,
    error: str | None = None,
) -> None:
    if run_id is None and not task_id:
        return
    db = SessionLocal()
    try:
        ensure_pipeline_runs_table(db)
        now = datetime.now(timezone.utc)
        if run_id is not None:
            row = db.execute(
                text("SELECT started_at FROM pipeline_runs WHERE id = :id"),
                {"id": run_id},
            ).fetchone()
            where_sql = "id = :id"
            params: dict[str, Any] = {"id": run_id}
        else:
            row = db.execute(
                text("SELECT started_at FROM pipeline_runs WHERE task_id = :task_id"),
                {"task_id": task_id},
            ).fetchone()
            where_sql = "task_id = :task_id"
            params = {"task_id": task_id}
        started_at = row[0] if row else None
        duration_ms = None
        if started_at is not None:
            if started_at.tzinfo is None:
                started_at = started_at.replace(tzinfo=timezone.utc)
            duration_ms = max(0, int((now - started_at).total_seconds() * 1000))
        params.update(
            {
                "status": status[:20],
                "duration_ms": duration_ms,
                "result_json": _json_safe(result),
                "error_text": error[:4000] if error else None,
            }
        )
        db.execute(
            text(
                f"""
                UPDATE pipeline_runs
                SET status = :status,
                    finished_at = NOW(),
                    duration_ms = :duration_ms,
                    result_json = :result_json,
                    error_text = :error_text
                WHERE {where_sql}
                """
            ),
            params,
        )
        db.commit()
    except Exception as exc:
        db.rollback()
        log.warning("pipeline run finish failed for %s/%s: %s", run_id, task_id, exc)
    finally:
        db.close()
