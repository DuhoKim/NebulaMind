#!/usr/bin/env python3
"""Dry-run-first runner for promoting provisional evidence.

By default this script only reports candidate rows. Pass --commit to activate the
matching provisional evidence rows and recalculate affected claim trust through
TrustMutationService.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.agent import Agent
from app.models.claim import Evidence
from app.services.trust_mutation import TrustMutationError, TrustMutationService

TRIGGER = "provisional_evidence_promotion_runner"


def _normalize_ids(evidence_ids: Iterable[int] | None) -> list[int]:
    if not evidence_ids:
        return []
    return sorted({int(evidence_id) for evidence_id in evidence_ids})


def find_promotion_candidates(
    db: Session,
    *,
    evidence_ids: Iterable[int] | None = None,
    claim_id: int | None = None,
    source_channel: str | None = None,
    limit: int = 50,
) -> list[Evidence]:
    """Return provisional evidence rows matching the operator filters."""
    query = db.query(Evidence).filter(Evidence.status == "provisional")
    ids = _normalize_ids(evidence_ids)
    if ids:
        query = query.filter(Evidence.id.in_(ids))
    if claim_id is not None:
        query = query.filter(Evidence.claim_id == claim_id)
    if source_channel:
        query = query.filter(Evidence.source_channel == source_channel)
    return list(query.order_by(Evidence.created_at, Evidence.id).limit(max(1, limit)).all())


def _candidate_payload(evidence: Evidence) -> dict:
    return {
        "evidence_id": evidence.id,
        "claim_id": evidence.claim_id,
        "title": evidence.title,
        "source_channel": evidence.source_channel,
        "old_status": evidence.status,
        "would_promote": evidence.status == "provisional",
    }


def run_promotion(
    db: Session,
    *,
    evidence_ids: Iterable[int] | None = None,
    claim_id: int | None = None,
    source_channel: str | None = None,
    limit: int = 50,
    commit: bool = False,
    actor_agent_id: int | None = None,
) -> dict:
    """Report or promote matching provisional evidence rows.

    The default dry-run mode is read-only. Commit mode mutates only evidence
    status/verified_at and trust recalculation side effects from the canonical
    TrustMutationService path.
    """
    actor: Agent | None = None
    if actor_agent_id is not None:
        actor = db.get(Agent, actor_agent_id)
        if actor is None:
            raise ValueError(f"actor agent not found: {actor_agent_id}")

    candidates = find_promotion_candidates(
        db,
        evidence_ids=evidence_ids,
        claim_id=claim_id,
        source_channel=source_channel,
        limit=limit,
    )
    sample: list[dict] = []
    promoted_count = 0

    if not commit:
        sample = [_candidate_payload(evidence) for evidence in candidates]
        return {
            "commit": False,
            "destructive_action": False,
            "candidate_count": len(candidates),
            "promoted_count": 0,
            "retention_policy": "not applicable; promotion activates rows and does not delete data",
            "sample": sample,
        }

    try:
        for evidence in candidates:
            before = _candidate_payload(evidence)
            result = TrustMutationService.promote_evidence(
                db,
                evidence_id=evidence.id,
                actor_agent=actor,
                trigger=TRIGGER,
            )
            promoted_count += int(result.promoted)
            sample.append({
                **before,
                "promoted": result.promoted,
                "status": result.evidence.status,
                "old_trust_level": result.old_level,
                "old_trust_score": result.old_score,
                "new_trust_level": result.new_level,
                "new_trust_score": result.new_score,
                "trust_score_delta": result.score_delta,
            })
        db.commit()
    except Exception:
        db.rollback()
        raise

    return {
        "commit": True,
        "destructive_action": False,
        "candidate_count": len(candidates),
        "promoted_count": promoted_count,
        "retention_policy": "not applicable; promotion activates rows and does not delete data",
        "sample": sample,
    }


def _print_text(report: dict) -> None:
    print(
        "commit={commit} destructive_action={destructive_action} "
        "candidate_count={candidate_count} promoted_count={promoted_count}".format(**report)
    )
    print(f"retention_policy={report['retention_policy']}")
    for row in report["sample"]:
        line = (
            "evidence_id={evidence_id} claim_id={claim_id} old_status={old_status} "
            "source_channel={source_channel} title={title!r}".format(**row)
        )
        if "old_trust_score" in row and "new_trust_score" in row:
            old_score = float(row.get("old_trust_score") or 0.0)
            new_score = float(row.get("new_trust_score") or 0.0)
            delta = float(row.get("trust_score_delta", new_score - old_score) or 0.0)
            line += f" trust_score={old_score:.3f}->{new_score:.3f} trust_score_delta={delta:+.3f}"
        print(line)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-id", type=int, action="append", dest="evidence_ids", help="Evidence ID to promote; repeatable")
    parser.add_argument("--claim-id", type=int, help="Restrict candidates to a claim")
    parser.add_argument("--source-channel", help="Restrict candidates to a source channel")
    parser.add_argument("--limit", type=int, default=50, help="Maximum candidates to inspect/promote")
    parser.add_argument("--actor-agent-id", type=int, help="Agent ID to record as the promotion actor")
    parser.add_argument("--commit", action="store_true", help="Actually promote rows; default is read-only dry-run")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    db = SessionLocal()
    try:
        report = run_promotion(
            db,
            evidence_ids=args.evidence_ids,
            claim_id=args.claim_id,
            source_channel=args.source_channel,
            limit=args.limit,
            commit=args.commit,
            actor_agent_id=args.actor_agent_id,
        )
    except (TrustMutationError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    finally:
        db.close()

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True, default=str))
    else:
        _print_text(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
