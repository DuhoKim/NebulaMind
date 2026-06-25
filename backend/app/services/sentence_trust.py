from __future__ import annotations

from typing import TypedDict

from sqlalchemy.orm import Session

from app.config import settings
from app.models.sentence_trust import SentenceTrust, SentenceVote


class SentenceTrustProjection(TypedDict):
    vote_count: int
    settled_votes: int
    contested_votes: int
    settled_share: float
    trust_score: float
    trust_level: str
    tone_tier: str
    single_source: bool
    contested_veto: bool
    tier2_density: float
    tone_distribution: dict[str, int]
    tone_distribution_4: dict[str, int] | None


def _sentence_tone_tier(settled_votes: int, contested_votes: int) -> str:
    if not settled_votes and not contested_votes:
        return "mixed"
    if settled_votes and contested_votes:
        return "mixed"
    if contested_votes:
        return "contested"
    return "settled"


def _sentence_trust_level(settled_votes: int, contested_votes: int, distinct_sources: int) -> tuple[str, bool, bool]:
    single_source = distinct_sources <= 1 and (settled_votes + contested_votes) > 0
    # The votes fed here are assumed to have passed the stance/relevance gate;
    # the matcher slice remains responsible for rejecting adjacent-but-irrelevant dissent.
    contested_veto = distinct_sources >= 2 and contested_votes >= 2
    if distinct_sources <= 1:
        return "unverified", single_source, contested_veto
    if contested_votes > settled_votes:
        return "challenged", single_source, contested_veto
    if contested_veto:
        return "debated", single_source, contested_veto
    if settled_votes >= 3 and contested_votes == 0:
        return "consensus", single_source, contested_veto
    if contested_votes > 0:
        return "debated", single_source, contested_veto
    if settled_votes > 0:
        return "accepted", single_source, contested_veto
    return "unverified", single_source, contested_veto


def project_sentence_trust(
    *,
    settled_votes: int,
    contested_votes: int,
    distinct_sources: int | None = None,
) -> SentenceTrustProjection:
    """Project sentence trust fields without touching the database.

    The Page57/Page58 dry-run path needs the exact same vote-count, tiering,
    and score semantics as the production `sentence_votes` -> `sentence_trust`
    writer. Keep that contract here so dry-run artifacts cannot drift from the
    eventual persisted aggregate.
    """
    if settled_votes < 0 or contested_votes < 0:
        raise ValueError("sentence vote counts must be non-negative")
    vote_total = settled_votes + contested_votes
    if distinct_sources is None:
        distinct_sources = vote_total
    if distinct_sources < 0:
        raise ValueError("distinct_sources must be non-negative")
    if vote_total == 0 and distinct_sources:
        raise ValueError("distinct_sources must be 0 when sentence vote counts are 0")
    if vote_total > 0 and distinct_sources == 0:
        raise ValueError("distinct_sources must be positive when sentence vote counts are non-zero")
    if distinct_sources > vote_total:
        raise ValueError("distinct_sources cannot exceed total sentence votes")

    settled_share = (settled_votes / vote_total) if vote_total else 0.0
    raw_evidence = ((settled_votes - contested_votes) / vote_total) if vote_total else 0.0
    trust_score = settings.TRUST_W_EVIDENCE * raw_evidence
    trust_level, single_source, contested_veto = _sentence_trust_level(
        settled_votes,
        contested_votes,
        distinct_sources,
    )
    tone_tier = _sentence_tone_tier(settled_votes, contested_votes)
    return {
        "vote_count": distinct_sources,
        "settled_votes": settled_votes,
        "contested_votes": contested_votes,
        "settled_share": settled_share,
        "trust_score": trust_score,
        "trust_level": trust_level,
        "tone_tier": tone_tier,
        "single_source": single_source,
        "contested_veto": contested_veto,
        "tier2_density": 0.0,
        "tone_distribution": {"settled": settled_votes, "contested": contested_votes},
        "tone_distribution_4": None,
    }



def recalculate_sentence_trust(
    db: Session,
    *,
    page_version_id: int,
    sentence_index: int,
    sentence_hash: str,
) -> SentenceTrust:
    """Roll per-paper sentence votes into the sentence_trust aggregate row.

    This is the sentence-level analogue of the claim evidence trust adapter: one
    paper casts at most one vote per sentence through the SentenceVote uniqueness
    guard, and this deterministic rollup writes only the aggregate row for that
    sentence/version.
    """
    votes = (
        db.query(SentenceVote)
        .filter(
            SentenceVote.page_version_id == page_version_id,
            SentenceVote.sentence_index == sentence_index,
            SentenceVote.sentence_hash == sentence_hash,
        )
        .all()
    )
    settled_votes = sum(1 for vote in votes if vote.value > 0)
    contested_votes = sum(1 for vote in votes if vote.value < 0)
    distinct_sources = len({vote.arxiv_id for vote in votes})
    projection = project_sentence_trust(
        settled_votes=settled_votes,
        contested_votes=contested_votes,
        distinct_sources=distinct_sources,
    )

    row = (
        db.query(SentenceTrust)
        .filter(
            SentenceTrust.page_version_id == page_version_id,
            SentenceTrust.sentence_index == sentence_index,
        )
        .first()
    )
    if row is None:
        row = SentenceTrust(page_version_id=page_version_id, sentence_index=sentence_index)
        db.add(row)

    row.sentence_hash = sentence_hash
    row.tone_tier = projection["tone_tier"]
    row.vote_count = projection["vote_count"]
    row.settled_votes = projection["settled_votes"]
    row.contested_votes = projection["contested_votes"]
    row.settled_share = projection["settled_share"]
    row.trust_score = projection["trust_score"]
    row.trust_level = projection["trust_level"]
    row.single_source = projection["single_source"]
    row.contested_veto = projection["contested_veto"]
    row.tier2_density = projection["tier2_density"]
    row.tone_distribution = projection["tone_distribution"]
    row.tone_distribution_4 = projection["tone_distribution_4"]
    db.flush()
    return row
