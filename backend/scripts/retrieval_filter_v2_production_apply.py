#!/usr/bin/env python3
"""Production apply for retrieval-filter v2/v2.1 element rows.

This script is intentionally narrow: it writes retrieval-filter element rows
for the configured three galaxy-evolution v2 sections, creates a new
arxiv_wiki_feed_runs row, and never touches promoter or validator state.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from sqlalchemy import create_engine, text

from app.config import settings
WORK_ROOT = Path("/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2")
LIVE_CONFIG = BACKEND_ROOT / "config" / "page_retrieval_calibration.galaxy-evolution.v2.yaml"
ROLLBACK_COPY = (
    WORK_ROOT
    / "retrieval_filter_v2_1_apply_validator_dryrun_20260527T001425Z"
    / "rollback_page_retrieval_calibration.galaxy-evolution.v2.yaml"
)
V2_1_VARIANT = (
    WORK_ROOT
    / "retrieval_filter_v2_brk_trim_dryrun_20260527T001157Z"
    / "page_retrieval_calibration.galaxy-evolution.v2_1.yaml"
)
V2_1_PROJECTION = (
    WORK_ROOT
    / "retrieval_filter_v2_brk_trim_dryrun_20260527T001157Z"
    / "v2_1_projection_rows.jsonl"
)
BACKUP_DIR = Path("/Users/duhokim/NebulaMind/backups")
PG_DUMP = Path("/opt/homebrew/Cellar/libpq/18.4/bin/pg_dump")

TARGET_SECTIONS = ("feedback_outflows", "high_z_sf", "env_quenching")
EXPECTED = {
    "feedback_outflows": {"rows": 148, "brk": 38},
    "high_z_sf": {"rows": 183, "brk": 32},
    "env_quenching": {"rows": 95, "brk": 36},
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def claim_id_from_element(element_id: str) -> int:
    match = re.match(r"claim-(\d+)-", str(element_id or ""))
    if not match:
        raise ValueError(f"Cannot parse claim_id from {element_id!r}")
    return int(match.group(1))


def pg_dump_backup(path: Path) -> None:
    backup_env = dict(os.environ)
    backup_env.setdefault("PGPASSWORD", "nebula")
    subprocess.run(
        [
            str(PG_DUMP),
            "-h",
            "localhost",
            "-U",
            "nebula",
            "-d",
            "nebulamind",
            "-Fc",
            "-f",
            str(path),
        ],
        check=True,
        env=backup_env,
    )
    path.chmod(0o600)


def ensure_config_state(artifact_dir: Path) -> dict[str, Any]:
    live_sha = sha256(LIVE_CONFIG)
    v2_1_sha = sha256(V2_1_VARIANT)
    rollback_sha = sha256(ROLLBACK_COPY)

    shutil.copy2(LIVE_CONFIG, artifact_dir / "pre_apply_live_config_snapshot.yaml")
    shutil.copy2(V2_1_VARIANT, artifact_dir / "v2_1_variant_snapshot.yaml")
    shutil.copy2(ROLLBACK_COPY, artifact_dir / "rollback_copy_snapshot.yaml")

    if live_sha == v2_1_sha:
        action = "live already swapped to v2.1, skipping swap step"
    elif live_sha == rollback_sha:
        shutil.copy2(V2_1_VARIANT, LIVE_CONFIG)
        action = "live matched rollback copy, swapped to v2.1 variant"
        live_sha = sha256(LIVE_CONFIG)
    else:
        raise RuntimeError(
            "unknown live config state: "
            f"live_sha={live_sha} v2_1_variant_sha={v2_1_sha} rollback_copy_sha={rollback_sha}"
        )

    shutil.copy2(LIVE_CONFIG, artifact_dir / "post_preflight_live_config_snapshot.yaml")
    return {
        "live_sha": live_sha,
        "v2_1_variant_sha": v2_1_sha,
        "rollback_copy_sha": rollback_sha,
        "action": action,
    }


def create_rows(
    rows_to_insert: list[dict[str, Any]],
    paper_map: dict[str, Any],
    run_id: int,
    *,
    page_id: int,
    page_slug: str,
) -> list[dict[str, Any]]:
    insert_rows = []
    for row in rows_to_insert:
        arxiv_id = str(row.get("paper_id") or "")
        paper_meta = paper_map.get(arxiv_id)
        if isinstance(paper_meta, dict):
            arxiv_paper_id = paper_meta.get("id")
            paper_title = paper_meta.get("title")
            paper_abstract = paper_meta.get("abstract")
        else:
            arxiv_paper_id = paper_meta
            paper_title = None
            paper_abstract = None
        row_payload = dict(row)
        if paper_title and not row_payload.get("paper_title_snapshot"):
            row_payload["paper_title_snapshot"] = paper_title
        if paper_abstract and not row_payload.get("paper_abstract_snapshot"):
            row_payload["paper_abstract_snapshot"] = paper_abstract
        decision = row["v2_1_decision"]
        routes_to_validator = bool(row.get("retrieval_routes_to_validator", decision == "keep"))
        validator_enqueue_policy = row.get("validator_enqueue_policy") or (
            "audit_only" if decision == "boundary_review_keep" else "enqueue"
        )
        validator_status = "pending" if routes_to_validator else "audit_only"
        insert_rows.append(
            {
                "run_id": run_id,
                "page_id": page_id,
                "page_slug": page_slug,
                "section": row["section"],
                "claim_id": claim_id_from_element(row["element_id"]),
                "element_id": row["element_id"],
                "arxiv_paper_id": arxiv_paper_id,
                "arxiv_id": arxiv_id,
                "retrieval_filter_version": "v2.1",
                "retrieval_filter_decision": decision,
                "boundary_review_reason": row.get("prior_boundary_reason")
                if decision == "boundary_review_keep"
                else None,
                "boundary_review_policy": (
                    f"{row['section']}_boundary_review_v2_1_brk_trim_20260527"
                    if decision == "boundary_review_keep"
                    else None
                ),
                "boundary_review_features": json.dumps(
                    {
                        "source_projection_run_key": "retrieval_filter_v2_brk_trim_dryrun_20260527T001157Z",
                        "prior_v2_decision": row.get("prior_v2_decision"),
                        "prior_boundary_reason": row.get("prior_boundary_reason"),
                        "v2_1_trim_reason": row.get("v2_1_trim_reason"),
                        "final_score": row.get("final_score"),
                        "validator_enqueue_policy": validator_enqueue_policy,
                        "validator_enqueue_reason": row.get("validator_enqueue_reason"),
                        "brk_usage": row.get("brk_usage"),
                    }
                ),
                "would_be_promotion_authority": False,
                "retrieval_routes_to_validator": routes_to_validator,
                "validator_status": validator_status,
                "validator_priority": 0 if decision == "boundary_review_keep" else 50,
                "label": row.get("label"),
                "final_score": row.get("final_score"),
                "combined_score": row.get("combined_score"),
                "context_score": row.get("context_score"),
                "positive_score": row.get("positive_score"),
                "tags": json.dumps(row.get("tags") or []),
                "drop_reasons": json.dumps(row.get("drop_reasons") or []),
                "row_payload": json.dumps(row_payload),
            }
        )
    return insert_rows


def write_summary(path: Path, payload: dict[str, Any], wall_seconds: float) -> None:
    lines = [
        "# Retrieval Filter v2 Production Apply",
        "",
        f"- Run key: `{payload['run_key']}`",
        f"- New DB run id: `{payload.get('new_db_run_id')}`",
        f"- Backup: `{payload['backup_path']}`",
        f"- Backup size: `{payload['backup_size_bytes']}` bytes",
        f"- Status: `{payload['status']}`",
        f"- Total wall time: `{wall_seconds:.2f}s`",
        f"- Config preflight: `{payload['config_preflight']['action']}`",
        "",
        "| Section | Rows | BRK | Recall | Off-domain |",
        "|---|---:|---:|---:|---:|",
    ]
    for section in TARGET_SECTIONS:
        metrics = payload.get("per_section", {}).get(section, {})
        lines.append(
            f"| `{section}` | {metrics.get('rows')} | {metrics.get('brk')} | "
            f"{metrics.get('citable_recall')} | {metrics.get('off_domain_share')} |"
        )
    lines += [
        "",
        f"- v1 regression clean: `{payload.get('v1_regression_clean')}`",
        f"- db_run_id=3 unmutated: `{payload.get('db_run_id_3_unmutated')}`",
        f"- pytest passed: `{payload.get('pytest_passed')}`",
        f"- promoter changes: `{payload.get('promoter_changes')}`",
    ]
    if payload.get("failing_check"):
        lines.append(f"- Failing check: `{payload['failing_check']}`")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True)
    parser.add_argument("--run-key", default=f"retrieval_filter_v2_production_apply_{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}")
    parser.add_argument("--artifact-dir")
    args = parser.parse_args()

    started = time.monotonic()
    global LIVE_CONFIG
    LIVE_CONFIG = BACKEND_ROOT / "config" / f"page_retrieval_calibration.{args.slug}.v2.yaml"
    run_key = args.run_key
    artifact_dir = Path(args.artifact_dir) if args.artifact_dir else WORK_ROOT / run_key
    artifact_dir.mkdir(parents=True, exist_ok=True)
    backup_path = BACKUP_DIR / f"nebulamind_pre_{run_key}.dump"
    summary_path = artifact_dir / "SUMMARY.md"

    payload: dict[str, Any] = {
        "run_key": run_key,
        "artifact_dir": str(artifact_dir),
        "summary_path": str(summary_path),
        "backup_path": str(backup_path),
        "status": "aborted",
        "new_db_run_id": None,
        "v1_regression_clean": None,
        "db_run_id_3_unmutated": None,
        "pytest_passed": None,
        "promoter_changes": False,
    }

    try:
        pg_dump_backup(backup_path)
        payload["backup_size_bytes"] = backup_path.stat().st_size
        payload["backup_sha256"] = sha256(backup_path)
        payload["config_preflight"] = ensure_config_state(artifact_dir)

        rows_all = read_jsonl(V2_1_PROJECTION)
        rows_to_insert = [
            row
            for row in rows_all
            if row.get("section") in TARGET_SECTIONS and row.get("v2_1_decision") != "drop"
        ]
        projection_counts = Counter(row["section"] for row in rows_to_insert)
        projection_brk = Counter(
            row["section"] for row in rows_to_insert if row.get("v2_1_decision") == "boundary_review_keep"
        )
        for section, expected in EXPECTED.items():
            if projection_counts[section] != expected["rows"] or projection_brk[section] != expected["brk"]:
                raise RuntimeError(f"projection mismatch for {section}")

        engine = create_engine(settings.DATABASE_URL)
        code_version = (
            subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=BACKEND_ROOT,
                text=True,
                capture_output=True,
                check=False,
            ).stdout.strip()
            or "unknown"
        )

        with engine.begin() as conn:
            page = conn.execute(
                text("SELECT id, slug FROM wiki_pages WHERE slug = :slug"),
                {"slug": args.slug},
            ).mappings().first()
            if not page:
                raise RuntimeError(f"unknown wiki page slug: {args.slug}")

            run3_before = conn.execute(
                text("SELECT id, run_key, status FROM arxiv_wiki_feed_runs WHERE id=3")
            ).mappings().one()
            v1_before = conn.execute(
                text(
                    """
                    SELECT section, element_id, arxiv_id, retrieval_filter_decision,
                           boundary_review_reason, row_payload::text
                    FROM retrieval_filter_element_rows
                    WHERE run_id=3 AND section IN ('size_evolution','shmr_halo_quenching')
                    ORDER BY section, element_id, arxiv_id
                    """
                )
            ).fetchall()

            run_id = conn.execute(
                text(
                    """
                    INSERT INTO arxiv_wiki_feed_runs
                        (run_key, page_id, page_slug, run_scope, paper_query, candidate_params,
                         validator_params, status, created_by, code_version, report_path, notes)
                    VALUES
                        (:run_key, :page_id, :page_slug, 'retrieval_filter_v2_production_apply',
                         CAST(:paper_query AS jsonb), CAST(:candidate_params AS jsonb),
                         CAST(:validator_params AS jsonb), 'production_v2_1_element_rows_applied',
                         'tori', :code_version, :report_path,
                         'v2.1 production apply; retrieval-filter rows only; no promoter or validator changes')
                    RETURNING id
                    """
                ),
                {
                    "run_key": run_key,
                    "page_id": page["id"],
                    "page_slug": page["slug"],
                    "paper_query": json.dumps({"sections": list(TARGET_SECTIONS)}),
                    "candidate_params": json.dumps(
                        {
                            "config_path": str(LIVE_CONFIG),
                            "config_sha256": sha256(LIVE_CONFIG),
                            "projection_path": str(V2_1_PROJECTION),
                            "expected_counts": EXPECTED,
                            "backup_path": str(backup_path),
                            "backup_sha256": payload["backup_sha256"],
                        }
                    ),
                    "validator_params": json.dumps({"promoter_changes": False, "validator_write": False}),
                    "code_version": code_version,
                    "report_path": str(summary_path),
                },
            ).scalar_one()

            arxiv_ids = sorted(
                {str(row.get("paper_id") or "") for row in rows_to_insert if str(row.get("paper_id") or "")}
            )
            paper_rows = conn.execute(
                text("SELECT arxiv_id, id, title, abstract FROM arxiv_papers WHERE arxiv_id = ANY(:ids)"),
                {"ids": arxiv_ids},
            ).fetchall()
            paper_map = {
                row.arxiv_id: {"id": row.id, "title": row.title, "abstract": row.abstract}
                for row in paper_rows
            }

            conn.execute(
                text(
                    """
                    INSERT INTO retrieval_filter_element_rows
                        (run_id, page_id, page_slug, section, claim_id, element_id,
                         arxiv_paper_id, arxiv_id, retrieval_filter_version,
                         retrieval_filter_decision, boundary_review_reason,
                         boundary_review_policy, boundary_review_features,
                         would_be_promotion_authority, retrieval_routes_to_validator,
                         validator_status, validator_priority, label, final_score,
                         combined_score, context_score, positive_score, tags,
                         drop_reasons, row_payload)
                    VALUES
                        (:run_id, :page_id, :page_slug, :section, :claim_id, :element_id,
                         :arxiv_paper_id, :arxiv_id, :retrieval_filter_version,
                         :retrieval_filter_decision, :boundary_review_reason,
                         :boundary_review_policy, CAST(:boundary_review_features AS jsonb),
                         :would_be_promotion_authority, :retrieval_routes_to_validator,
                         :validator_status, :validator_priority, :label, :final_score,
                         :combined_score, :context_score, :positive_score, CAST(:tags AS jsonb),
                         CAST(:drop_reasons AS jsonb), CAST(:row_payload AS jsonb))
                    """
                ),
                create_rows(rows_to_insert, paper_map, run_id, page_id=page["id"], page_slug=page["slug"]),
            )

            actual_rows = conn.execute(
                text(
                    """
                    SELECT section, count(*) AS rows,
                           count(*) FILTER (WHERE retrieval_filter_decision='boundary_review_keep') AS brk,
                           count(*) FILTER (WHERE retrieval_routes_to_validator) AS validator_enqueue,
                           count(*) FILTER (WHERE label='citable') AS citable,
                           count(*) FILTER (WHERE label='off_domain') AS off_domain,
                           count(*) FILTER (WHERE would_be_promotion_authority) AS promo_true
                    FROM retrieval_filter_element_rows
                    WHERE run_id=:run_id
                    GROUP BY section
                    """
                ),
                {"run_id": run_id},
            ).mappings().all()
            actual_by_section = {row["section"]: dict(row) for row in actual_rows}
            for section, expected in EXPECTED.items():
                actual = actual_by_section.get(section)
                if not actual or actual["rows"] != expected["rows"] or actual["brk"] != expected["brk"]:
                    raise RuntimeError(f"post-write count mismatch for {section}: {actual}")
                if actual["promo_true"] != 0:
                    raise RuntimeError(f"promotion-authority row found for {section}")
                expected_validator_enqueue = actual["rows"] - actual["brk"]
                if actual["validator_enqueue"] != expected_validator_enqueue:
                    raise RuntimeError(
                        f"validator enqueue mismatch for {section}: "
                        f"{actual['validator_enqueue']} != {expected_validator_enqueue}"
                    )

            accidental = sorted(set(actual_by_section) - set(TARGET_SECTIONS))
            if accidental:
                raise RuntimeError(f"accidental sections touched: {accidental}")

            run3_after = conn.execute(
                text("SELECT id, run_key, status FROM arxiv_wiki_feed_runs WHERE id=3")
            ).mappings().one()
            v1_after = conn.execute(
                text(
                    """
                    SELECT section, element_id, arxiv_id, retrieval_filter_decision,
                           boundary_review_reason, row_payload::text
                    FROM retrieval_filter_element_rows
                    WHERE run_id=3 AND section IN ('size_evolution','shmr_halo_quenching')
                    ORDER BY section, element_id, arxiv_id
                    """
                )
            ).fetchall()
            payload["db_run_id_3_unmutated"] = (
                dict(run3_before) == dict(run3_after)
                and run3_after["run_key"] == "retrieval_filter_v1_partial_ship_20260526T232205Z"
                and run3_after["status"] == "production_partial_shipped"
            )
            payload["v1_regression_clean"] = v1_before == v1_after
            if not payload["db_run_id_3_unmutated"] or not payload["v1_regression_clean"]:
                raise RuntimeError("v1 regression or run_id=3 mutation check failed")

            conn.execute(text("UPDATE arxiv_wiki_feed_runs SET finished_at=now() WHERE id=:id"), {"id": run_id})

        per_section = {}
        for section in TARGET_SECTIONS:
            kept = [row for row in rows_to_insert if row["section"] == section]
            all_section = [row for row in rows_all if row["section"] == section]
            total_citable = sum(1 for row in all_section if row.get("label") == "citable")
            kept_citable = sum(1 for row in kept if row.get("label") == "citable")
            off_domain = sum(1 for row in kept if row.get("label") == "off_domain")
            brk = sum(1 for row in kept if row.get("v2_1_decision") == "boundary_review_keep")
            per_section[section] = {
                "rows": len(kept),
                "brk": brk,
                "citable_recall": round(kept_citable / total_citable, 6) if total_citable else None,
                "off_domain_share": round(off_domain / len(kept), 6) if kept else None,
            }

        payload["new_db_run_id"] = run_id
        payload["per_section"] = per_section
        payload["status"] = "success"
    except Exception as exc:
        payload["failing_check"] = str(exc)
    finally:
        wall_seconds = time.monotonic() - started
        if payload["status"] == "success":
            test_result = subprocess.run(
                [str(BACKEND_ROOT / ".venv/bin/python"), "-m", "pytest", "tests/test_retrieval_filter_v2.py", "-q"],
                cwd=BACKEND_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            payload["pytest_passed"] = test_result.returncode == 0
            (artifact_dir / "pytest_retrieval_filter_v2.txt").write_text(
                test_result.stdout + test_result.stderr, encoding="utf-8"
            )
            if not payload["pytest_passed"]:
                payload["status"] = "aborted"
                payload["failing_check"] = "post-apply pytest failed"
        write_summary(summary_path, payload, wall_seconds)
        (artifact_dir / "result.json").write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["status"] == "success" else 1


if __name__ == "__main__":
    raise SystemExit(main())
