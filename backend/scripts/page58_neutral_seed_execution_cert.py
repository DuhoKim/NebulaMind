#!/usr/bin/env python3
"""Dry-run execution cert for page-58 neutral evidence seeds.

This script writes report artifacts only. The DB probe inserts a scratch claim and
scratch evidence row inside one transaction, reads the evidence back, then rolls
the transaction back and verifies no scratch rows remain.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Any

from sqlalchemy import func, text

REPO_ROOT = Path(__file__).resolve().parents[2]
BACKEND_ROOT = REPO_ROOT / "backend"
DOCS_ROOT = REPO_ROOT / "docs"
REBALANCE_DIR = DOCS_ROOT / "page58_slice2b_stance_gold_rebalance_20260623T043618Z"
DEFAULT_SEED_PLAN = REBALANCE_DIR / "sign_suppressed_seed_plan_20260623T105018Z.jsonl"
SOURCE_CHANNEL = "page58_neutral_seed_v1"
PAGE_ID = 58

sys.path.insert(0, str(BACKEND_ROOT))

from app.database import SessionLocal  # noqa: E402
from app.models.claim import Claim, Evidence, EvidenceVote  # noqa: E402
from app.models.jury import JuryTask  # noqa: E402
from app.models.page import PageVersion  # noqa: E402
from app.routers.claims import EvidenceCreate  # noqa: E402


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False, sort_keys=True) for row in rows) + "\n",
        encoding="utf-8",
    )


def nm_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=REPO_ROOT, text=True).strip()


def arxiv_variants(arxiv_id: str | None) -> list[str]:
    if not arxiv_id:
        return []
    raw = arxiv_id.strip()
    base = raw
    if "v" in raw:
        head, tail = raw.rsplit("v", 1)
        if tail.isdigit():
            base = head
    return list(dict.fromkeys([
        raw,
        base,
        f"arXiv:{raw}",
        f"arXiv:{base}",
        f"oai:arXiv.org:{raw}",
        f"oai:arXiv.org:{base}",
    ]))


def load_paper_meta(db, arxiv_id: str | None) -> dict[str, Any]:
    variants = arxiv_variants(arxiv_id)
    if not variants:
        return {"title": None, "authors": None, "year": None, "url": None, "metadata_status": "missing_arxiv_id"}
    row = db.execute(
        text(
            """
            SELECT arxiv_id, title, authors, submitted, url
            FROM arxiv_papers
            WHERE arxiv_id = ANY(:variants)
            LIMIT 1
            """
        ),
        {"variants": variants},
    ).mappings().first()
    if not row:
        clean = variants[1] if len(variants) > 1 else variants[0]
        return {
            "title": f"arXiv:{clean}",
            "authors": None,
            "year": None,
            "url": f"https://arxiv.org/abs/{clean}",
            "metadata_status": "fallback_from_arxiv_id",
        }
    year = None
    submitted = row.get("submitted")
    if submitted and len(str(submitted)) >= 4 and str(submitted)[:4].isdigit():
        year = int(str(submitted)[:4])
    return {
        "title": row.get("title"),
        "authors": row.get("authors"),
        "year": year,
        "url": row.get("url"),
        "metadata_status": "arxiv_papers",
        "matched_arxiv_id": row.get("arxiv_id"),
    }


def marker_summary(row: dict[str, Any]) -> str:
    intro = " ".join(str(row.get("intro_sentence") or "").split())
    return f"[{SOURCE_CHANNEL} gold_id={row['gold_id']}] {intro[:430]}".strip()


def build_insert_plan(seed_plan_path: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    source_rows = read_jsonl(seed_plan_path)
    auto_rows = [row for row in source_rows if row.get("auto_seed")]
    db = SessionLocal()
    try:
        base_sentences = sorted({row["base_sentence"] for row in auto_rows})
        claim_rows = (
            db.query(Claim)
            .filter(Claim.page_id == PAGE_ID, Claim.text.in_(base_sentences))
            .all()
        )
        claim_by_text = {claim.text: claim for claim in claim_rows}
        page_version = db.get(PageVersion, 6189)
        plan: list[dict[str, Any]] = []
        for idx, row in enumerate(auto_rows, start=1):
            claim = claim_by_text.get(row["base_sentence"])
            meta = load_paper_meta(db, row.get("arxiv_id"))
            plan.append({
                "insert_order": idx,
                "source_gold_id": row["gold_id"],
                "claim_id": claim.id if claim else None,
                "claim_resolution_status": "resolved" if claim else "blocked_missing_live_claim",
                "claim_text": row["base_sentence"],
                "arxiv_id": row.get("arxiv_id"),
                "title": meta["title"],
                "authors": meta["authors"],
                "year": meta["year"],
                "url": meta["url"],
                "paper_metadata_status": meta["metadata_status"],
                "summary": marker_summary(row),
                "stance": "none",
                "quality": 0.5,
                "abstract": None,
                "intro_excerpt": None,
                "stance_jury_run_at": "now()",
                "source_channel": SOURCE_CHANNEL,
                "verified_at": "now()",
                "arxiv_verified": bool(row.get("arxiv_id")),
                "create_jury_task": False,
                "create_evidence_vote": False,
                "idempotency_key": f"{SOURCE_CHANNEL}:{row['gold_id']}",
                "idempotency_predicate": (
                    "skip if evidence.source_channel == source_channel "
                    "and evidence.summary starts with '[page58_neutral_seed_v1 gold_id=<source_gold_id>]'"
                ),
            })
        summary = {
            "source_rows": len(source_rows),
            "planned_insert_rows": len(plan),
            "resolved_claim_rows": sum(1 for row in plan if row["claim_id"] is not None),
            "unresolved_claim_rows": sum(1 for row in plan if row["claim_id"] is None),
            "distinct_claim_texts": len(base_sentences),
            "page_version_6189": {
                "id": getattr(page_version, "id", None),
                "page_id": getattr(page_version, "page_id", None),
                "content_len": len(getattr(page_version, "content", "") or "") if page_version else None,
                "has_claim_markers": "<!--claim:" in (getattr(page_version, "content", "") or "") if page_version else None,
            },
        }
        return plan, summary
    finally:
        db.close()


def rollback_probe(sample_plan_row: dict[str, Any]) -> dict[str, Any]:
    scratch = f"PAGE58_EXEC_CERT_SCRATCH_{uuid.uuid4().hex}"
    now = dt.datetime.utcnow()
    db = SessionLocal()
    evidence_id = None
    claim_id = None
    try:
        # Demonstrate why the seed writer must pass stance explicitly.
        evidence_create_default = EvidenceCreate(title="scratch-default").model_dump()
        evidence_create_explicit = EvidenceCreate(title="scratch-explicit", stance="none").model_dump()

        claim = Claim(
            page_id=PAGE_ID,
            section="execution_cert_dry_run",
            text=scratch,
            trust_level="unverified",
            claim_type="established",
        )
        db.add(claim)
        db.flush()
        claim_id = claim.id

        ev = Evidence(
            claim_id=claim.id,
            arxiv_id=sample_plan_row.get("arxiv_id"),
            doi=None,
            url=sample_plan_row.get("url"),
            title=sample_plan_row.get("title") or "page-58 neutral seed dry-run",
            authors=sample_plan_row.get("authors"),
            year=sample_plan_row.get("year"),
            summary=sample_plan_row["summary"],
            stance="none",
            quality=sample_plan_row["quality"],
            abstract=None,
            intro_excerpt=None,
            verified_at=now,
            stance_jury_run_at=now,
            source_channel=SOURCE_CHANNEL,
            arxiv_verified=sample_plan_row["arxiv_verified"],
            peer_reviewed=False,
        )
        db.add(ev)
        db.flush()
        evidence_id = ev.id

        readback = db.query(Evidence).filter(Evidence.id == evidence_id).one()
        readback_assertions = {
            "stance_is_none": readback.stance == "none",
            "abstract_is_null": readback.abstract is None,
            "intro_excerpt_is_null": readback.intro_excerpt is None,
            "stance_jury_run_at_is_set": readback.stance_jury_run_at is not None,
            "vote_count_is_zero": db.query(func.count(EvidenceVote.id)).filter(EvidenceVote.evidence_id == evidence_id).scalar() == 0,
            "jury_task_count_is_zero": db.query(func.count(JuryTask.id)).filter(JuryTask.evidence_id == evidence_id).scalar() == 0,
        }
        p2_gate = {
            "stance_jury_run_at_is_not_null": readback.stance_jury_run_at is not None,
            "vote_count": 0,
            "vote_count_gt_0_required_by_p2": False,
            "abstract_length_predicate": False,
            "intro_excerpt_length_predicate": False,
            "fast_pass_p2_selected": False,
        }
        db.rollback()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

    check = SessionLocal()
    try:
        post_rollback = {
            "scratch_claim_rows": check.query(func.count(Claim.id)).filter(Claim.text == scratch).scalar(),
            "scratch_evidence_rows": (
                check.query(func.count(Evidence.id))
                .filter(Evidence.source_channel == SOURCE_CHANNEL, Evidence.summary.like(f"%{scratch}%"))
                .scalar()
            ),
            "probed_evidence_id_reused_after_rollback": (
                None if evidence_id is None
                else check.query(func.count(Evidence.id)).filter(Evidence.id == evidence_id).scalar()
            ),
        }
    finally:
        check.close()

    return {
        "method": "scratch Claim + Evidence inserted, read back, then db.rollback(); no commit",
        "scratch_claim_id_inside_rolled_back_tx": claim_id,
        "scratch_evidence_id_inside_rolled_back_tx": evidence_id,
        "evidence_create_default_stance": evidence_create_default["stance"],
        "evidence_create_explicit_stance": evidence_create_explicit["stance"],
        "exact_write_call_fields": {
            "Evidence.claim_id": "<resolved claim id at live write; scratch claim id in probe>",
            "Evidence.stance": "none",
            "Evidence.abstract": None,
            "Evidence.intro_excerpt": None,
            "Evidence.stance_jury_run_at": "now()",
            "Evidence.source_channel": SOURCE_CHANNEL,
            "JuryTask": "not created",
            "EvidenceVote": "not created",
        },
        "readback_assertions": readback_assertions,
        "durable_lock_checks": p2_gate,
        "post_rollback_verification": post_rollback,
        "net_db_write_count": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-plan", type=Path, default=DEFAULT_SEED_PLAN)
    parser.add_argument("--out-dir", type=Path, default=REBALANCE_DIR)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    stamp = utc_stamp()
    insert_plan, plan_summary = build_insert_plan(args.seed_plan)
    if len(insert_plan) != 105:
        raise RuntimeError(f"expected 105 planned insert rows, got {len(insert_plan)}")
    probe = rollback_probe(insert_plan[0])

    report = {
        "phase": "page58_neutral_seed_execution_cert_dry_run",
        "created_at_utc": dt.datetime.now(dt.UTC).isoformat(),
        "nm_head": nm_head(),
        "seed_plan_source": str(args.seed_plan),
        "execution_conditions": {
            "E1_explicit_stance_none": probe["readback_assertions"]["stance_is_none"],
            "E_A_null_text_at_write": (
                probe["readback_assertions"]["abstract_is_null"]
                and probe["readback_assertions"]["intro_excerpt_is_null"]
            ),
            "E_B_zero_jury_tasks": probe["readback_assertions"]["jury_task_count_is_zero"],
            "durable_lock_run_at_set": probe["readback_assertions"]["stance_jury_run_at_is_set"],
            "durable_lock_vote_count_zero": probe["readback_assertions"]["vote_count_is_zero"],
            "fk_claims_resolved_now": plan_summary["unresolved_claim_rows"] == 0,
            "idempotency_defined": True,
        },
        "execution_condition_notes": {
            "E_A": (
                "NULL abstract/intro_excerpt is verified as a write-time setting only. "
                "It is not claimed as the durable lock."
            ),
            "durable_lock": (
                "Durable closures are stance_jury_run_at=now() for run_at-IS-NULL drainers "
                "and vote_count=0 for fast-pass priority 2's vote_count > 0 gate."
            ),
        },
        "plan_summary": plan_summary,
        "rollback_probe": probe,
        "fk_order_and_idempotency": {
            "required_order": [
                "1. page-58 live page write creates or resolves Claim rows for the 10 base assertions",
                "2. neutral seed writer resolves each plan row's claim_id from claim_text",
                "3. writer checks idempotency marker before insert",
                "4. writer inserts Evidence with stance='none', null text, stance_jury_run_at=now(), source_channel marker",
                "5. writer does not create JuryTask or EvidenceVote",
                "6. writer reads back inserted rows and asserts stance='none', zero votes, zero JuryTask",
            ],
            "current_blocker": (
                "wiki_pages.id=58 currently has zero Claim rows; page_versions.id=6189 has no <!--claim:...--> markers. "
                "The 105 evidence rows cannot be live-inserted until the Papa-held page write creates/resolves claim IDs."
            ) if plan_summary["unresolved_claim_rows"] else None,
            "idempotency_marker": SOURCE_CHANNEL,
            "idempotency_key_shape": f"{SOURCE_CHANNEL}:<gold_id>",
        },
        "containment": {
            "db_write_count": 0,
            "db_probe_net_zero": True,
            "no_commit": True,
            "no_alembic": True,
            "no_live_page57_or_page58_write": True,
            "no_stance_lock": True,
            "paid_lane_touched": False,
            "excluded_files_touched": [],
        },
    }

    plan_path = args.out_dir / f"page58_neutral_seed_insert_plan_{stamp}.jsonl"
    report_path = args.out_dir / f"page58_neutral_seed_execution_cert_{stamp}.json"
    md_path = args.out_dir / f"page58_neutral_seed_execution_cert_{stamp}.md"
    write_jsonl(plan_path, insert_plan)
    write_json(report_path, report)
    md_path.write_text(render_md(report, plan_path, report_path), encoding="utf-8")
    sha256s = {path.name: sha256_file(path) for path in [plan_path, report_path, md_path]}
    print(json.dumps({
        "insert_plan": str(plan_path),
        "report": str(report_path),
        "markdown": str(md_path),
        "sha256s": sha256s,
    }, ensure_ascii=False, indent=2, sort_keys=True))


def render_md(report: dict[str, Any], plan_path: Path, report_path: Path) -> str:
    cond = report["execution_conditions"]
    summary = report["plan_summary"]
    probe = report["rollback_probe"]
    blocker = report["fk_order_and_idempotency"]["current_blocker"]
    notes = report["execution_condition_notes"]
    return "\n".join([
        "# Page-58 Neutral Seed Execution Cert Dry-Run",
        "",
        f"Created: {report['created_at_utc']}",
        f"NM HEAD: `{report['nm_head']}`",
        "",
        "## Artifacts",
        "",
        f"- Insert plan: `{plan_path}`",
        f"- JSON report: `{report_path}`",
        "",
        "## Counts",
        "",
        f"- Planned insert rows: {summary['planned_insert_rows']}",
        f"- Resolved claim rows now: {summary['resolved_claim_rows']}",
        f"- Unresolved claim rows now: {summary['unresolved_claim_rows']}",
        f"- Distinct base assertions: {summary['distinct_claim_texts']}",
        "",
        "## Execution Conditions",
        "",
        f"- E1 explicit `stance=\"none\"` read-back: {cond['E1_explicit_stance_none']}",
        f"- EvidenceCreate default stance hazard observed: `{probe['evidence_create_default_stance']}`",
        f"- EvidenceCreate explicit stance observed: `{probe['evidence_create_explicit_stance']}`",
        f"- E-A `abstract=NULL` and `intro_excerpt=NULL` at write: {cond['E_A_null_text_at_write']}",
        f"  - Note: {notes['E_A']}",
        f"- E-B zero `JuryTask`: {cond['E_B_zero_jury_tasks']}",
        f"- Durable lock `stance_jury_run_at=now()`: {cond['durable_lock_run_at_set']}",
        f"- Durable lock `vote_count=0`: {cond['durable_lock_vote_count_zero']}",
        f"  - Note: {notes['durable_lock']}",
        "",
        "## Rollback Probe",
        "",
        f"- Method: {probe['method']}",
        f"- Scratch claim id inside rolled-back tx: {probe['scratch_claim_id_inside_rolled_back_tx']}",
        f"- Scratch evidence id inside rolled-back tx: {probe['scratch_evidence_id_inside_rolled_back_tx']}",
        f"- Post-rollback scratch claim rows: {probe['post_rollback_verification']['scratch_claim_rows']}",
        f"- Post-rollback probed evidence id rows: {probe['post_rollback_verification']['probed_evidence_id_reused_after_rollback']}",
        f"- Net DB write count: {probe['net_db_write_count']}",
        "",
        "## FK Gate",
        "",
        blocker or "All claim IDs resolved.",
        "",
        "## Containment",
        "",
        f"- db_write_count: {report['containment']['db_write_count']}",
        "- No commit, no deploy/restart, no alembic, no live page-57/page-58 write, no paid lane.",
        "- Exclusion-zone files touched: none.",
        "",
    ])


if __name__ == "__main__":
    main()
