import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Literal

from sqlalchemy.orm import Session

from app.models.agent import Agent
from app.models.claim import Claim, Evidence, EvidenceVote

logger = logging.getLogger(__name__)

VoteDuplicateMode = Literal["reject", "update"]


class TrustMutationError(Exception):
    def __init__(self, status_code: int, detail: str):
        super().__init__(detail)
        self.status_code = status_code
        self.detail = detail


@dataclass(frozen=True)
class EvidenceVoteMutationResult:
    vote: EvidenceVote
    created: bool


@dataclass(frozen=True)
class EvidencePromotionResult:
    evidence: Evidence
    promoted: bool
    old_status: str
    old_level: str | None
    old_score: float
    new_level: str
    new_score: float

    @property
    def score_delta(self) -> float:
        return self.new_score - self.old_score


class TrustMutationService:
    VALID_VOTE_VALUES = {-1, 0, 1}

    @classmethod
    def validate_vote_value(cls, value: int) -> int:
        if isinstance(value, bool):
            raise TrustMutationError(422, "value must be -1, 0, or 1")
        if value not in cls.VALID_VOTE_VALUES:
            raise TrustMutationError(422, "value must be -1, 0, or 1")
        return value

    @classmethod
    def create_or_update_evidence_vote(
        cls,
        db: Session,
        *,
        evidence_id: int,
        actor_agent: Agent,
        value: int,
        reason: str | None = None,
        task_id: int | None = None,
        trigger: str,
        duplicate_mode: VoteDuplicateMode = "reject",
        voter_type: str | None = None,
        weight: float | None = None,
        recalculate: bool = True,
        recalc_actor_agent_id: int | None = None,
    ) -> EvidenceVoteMutationResult:
        if not actor_agent or actor_agent.id is None:
            raise TrustMutationError(401, "Authenticated agent required")
        value = cls.validate_vote_value(value)

        evidence = db.query(Evidence).filter(Evidence.id == evidence_id).first()
        if not evidence:
            raise TrustMutationError(404, "Evidence not found")

        vote = (
            db.query(EvidenceVote)
            .filter_by(evidence_id=evidence_id, agent_id=actor_agent.id)
            .first()
        )
        created = vote is None
        if vote and duplicate_mode == "reject":
            raise TrustMutationError(409, "Already voted on this evidence")
        if not vote:
            vote = EvidenceVote(evidence_id=evidence_id, agent_id=actor_agent.id)
            db.add(vote)

        vote.value = value
        vote.weight = float(actor_agent.reputation if weight is None else weight)
        vote.voter_type = voter_type or ("external_agent" if actor_agent.endpoint_url else "agent")
        vote.reason = (reason or "")[:500]
        db.flush()

        if recalculate:
            cls.recalculate_evidence_trust(
                db,
                evidence=evidence,
                trigger=trigger,
                actor_agent_id=(
                    actor_agent.id if recalc_actor_agent_id is None else recalc_actor_agent_id
                ),
            )
        logger.info(
            "trust_mutation_evidence_vote %s",
            {
                "evidence_id": evidence_id,
                "claim_id": evidence.claim_id,
                "task_id": task_id,
                "actor_agent_id": actor_agent.id,
                "value": value,
                "voter_type": vote.voter_type,
                "created": created,
                "duplicate_mode": duplicate_mode,
                "trigger": trigger,
            },
        )
        return EvidenceVoteMutationResult(vote=vote, created=created)

    @classmethod
    def recalculate_evidence_trust(
        cls,
        db: Session,
        *,
        evidence: Evidence,
        trigger: str,
        actor_agent_id: int | None = None,
    ) -> tuple[str, float]:
        from app.services.trust_calculation import recalculate_trust_v2

        return recalculate_trust_v2(
            evidence.claim_id,
            db,
            trigger=trigger,
            actor_agent_id=actor_agent_id,
        )

    @classmethod
    def recalculate_sentence_trust(
        cls,
        db: Session,
        *,
        page_version_id: int,
        sentence_index: int,
        sentence_hash: str,
    ):
        # Keep this lazy to avoid importing the sentence model from the claim/evidence mutation module at import time.
        from app.services.sentence_trust import recalculate_sentence_trust

        return recalculate_sentence_trust(
            db,
            page_version_id=page_version_id,
            sentence_index=sentence_index,
            sentence_hash=sentence_hash,
        )

    @classmethod
    def promote_evidence(
        cls,
        db: Session,
        *,
        evidence_id: int,
        actor_agent: Agent | None = None,
        trigger: str = "evidence_promoted",
    ) -> EvidencePromotionResult:
        if actor_agent is not None and actor_agent.id is None:
            raise TrustMutationError(401, "Authenticated agent required")

        evidence = db.query(Evidence).filter(Evidence.id == evidence_id).first()
        if not evidence:
            raise TrustMutationError(404, "Evidence not found")

        claim = db.query(Claim).filter(Claim.id == evidence.claim_id).first()
        old_status = evidence.status or "active"
        old_level = claim.trust_level if claim else None
        old_score = float((claim.trust_score if claim else 0.0) or 0.0)

        if old_status == "active":
            return EvidencePromotionResult(
                evidence=evidence,
                promoted=False,
                old_status=old_status,
                old_level=old_level,
                old_score=old_score,
                new_level=old_level or "unverified",
                new_score=old_score,
            )
        if old_status != "provisional":
            raise TrustMutationError(422, "Evidence status must be provisional or active")

        evidence.status = "active"
        if evidence.verified_at is None:
            evidence.verified_at = datetime.utcnow()
        db.flush()

        new_level, new_score = cls.recalculate_evidence_trust(
            db,
            evidence=evidence,
            trigger=trigger,
            actor_agent_id=actor_agent.id if actor_agent else None,
        )
        db.flush()
        logger.info(
            "trust_mutation_evidence_promoted %s",
            {
                "evidence_id": evidence.id,
                "claim_id": evidence.claim_id,
                "old_status": old_status,
                "new_status": evidence.status,
                "old_level": old_level,
                "new_level": new_level,
                "actor_agent_id": actor_agent.id if actor_agent else None,
                "trigger": trigger,
            },
        )
        return EvidencePromotionResult(
            evidence=evidence,
            promoted=True,
            old_status=old_status,
            old_level=old_level,
            old_score=old_score,
            new_level=new_level,
            new_score=new_score,
        )
