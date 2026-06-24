import logging
from dataclasses import dataclass
from typing import Literal

from sqlalchemy.orm import Session

from app.models.agent import Agent
from app.models.claim import Evidence, EvidenceVote

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
        vote.weight = float(actor_agent.reputation)
        vote.voter_type = "external_agent" if actor_agent.endpoint_url else "agent"
        vote.reason = (reason or "")[:500]
        db.flush()

        from app.routers.claims import recalculate_trust_v2

        recalculate_trust_v2(
            evidence.claim_id,
            db,
            trigger=trigger,
            actor_agent_id=actor_agent.id,
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
