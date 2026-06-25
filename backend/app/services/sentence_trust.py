from __future__ import annotations

from sqlalchemy.orm import Session

from app.config import settings
from app.models.sentence_trust import SentenceTrust, SentenceVote


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
    vote_count = settled_votes + contested_votes
    distinct_sources = len({vote.arxiv_id for vote in votes})
    settled_share = (settled_votes / vote_count) if vote_count else 0.0
    raw_evidence = ((settled_votes - contested_votes) / vote_count) if vote_count else 0.0
    trust_score = settings.TRUST_W_EVIDENCE * raw_evidence
    trust_level, single_source, contested_veto = _sentence_trust_level(
        settled_votes,
        contested_votes,
        distinct_sources,
    )
    tone_tier = _sentence_tone_tier(settled_votes, contested_votes)

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
    row.tone_tier = tone_tier
    row.vote_count = vote_count
    row.settled_votes = settled_votes
    row.contested_votes = contested_votes
    row.settled_share = settled_share
    row.trust_score = trust_score
    row.trust_level = trust_level
    row.single_source = single_source
    row.contested_veto = contested_veto
    row.tier2_density = 0.0
    row.tone_distribution = {"settled": settled_votes, "contested": contested_votes}
    row.tone_distribution_4 = None
    db.flush()
    return row
