"""Claim-level TF-IDF retrieval for grounded chat."""
from __future__ import annotations
import math
import re
from dataclasses import dataclass, field
from collections import Counter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

# Re-use stopwords from arxiv_classifier
_STOPWORDS = frozenset("""
a about above after against all also am an and any are as at be because
been before being below between both but by can cannot could did do does
doing down during each few for from further get had has have having he her
here him his how i if in into is it its itself let me more most my no nor
not of off on once only or other our out over own same she should so some
such than that the their them then there these they this those through to
too under until up very was we were what when where which while who with
would you your
""".split())

ASTRO_KEYWORDS = frozenset("""
galaxy galaxies star stars stellar neutron pulsar magnetar supernova
supernovae quasar black hole holes dark matter energy cosmos cosmology
universe inflation big bang cmbr cmb hubble gravity gravitational wave
exoplanet planet asteroid comet orbit telescope spectra spectral redshift
blueshift parsec lightyear astronomy astrophysics nebula cluster mass
luminosity magnitude photon electron proton baryon fermion boson
spacetime relativity quantum singularity event horizon hawking radiation
accretion disk jet agn solar wind magnetic field plasma corona
""".split())


@dataclass
class GroundedEvidence:
    arxiv_id: str | None
    doi: str | None
    title: str
    authors: str | None
    year: int | None
    abstract_excerpt: str
    quality: float
    n_jury_votes: int
    stance: str


@dataclass
class GroundedClaim:
    claim_id: int
    claim_text: str
    section: str
    page_title: str
    page_slug: str
    trust_level: str
    trust_score: float
    evidence: list[GroundedEvidence]
    relevance: float
    n_jury_votes: int


# Module-level cache
_cache: dict = {"idf": {}, "vectors": {}, "claim_ids": [], "version": 0}


def _tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[a-z]{3,}", text.lower())
    return [t for t in tokens if t not in _STOPWORDS]


def _build_index(db) -> tuple[dict, dict, list[int]]:
    """Build TF-IDF index over all non-unverified claims."""
    from app.models.claim import Claim
    claims = db.query(Claim).filter(
        Claim.trust_level.in_(["accepted", "consensus", "debated", "challenged"])
    ).all()

    doc_tokens: dict[int, list[str]] = {}
    for c in claims:
        tokens = _tokenize(c.text)
        doc_tokens[c.id] = tokens

    N = len(claims) or 1
    df: Counter = Counter()
    for tokens in doc_tokens.values():
        df.update(set(tokens))

    idf = {t: math.log((N + 1) / (cnt + 1)) + 1.0 for t, cnt in df.items()}

    vectors: dict[int, dict[str, float]] = {}
    for cid, tokens in doc_tokens.items():
        tf = Counter(tokens)
        n = sum(tf.values()) or 1
        vectors[cid] = {t: (tf[t] / n) * idf.get(t, 1.0) for t in tf}

    claim_ids = [c.id for c in claims]
    return idf, vectors, claim_ids


def _cosine(a: dict, b: dict) -> float:
    if not a or not b:
        return 0.0
    dot = sum(a[k] * b[k] for k in a if k in b)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


def _ensure_index(db) -> None:
    if not _cache["idf"]:
        idf, vectors, claim_ids = _build_index(db)
        _cache["idf"] = idf
        _cache["vectors"] = vectors
        _cache["claim_ids"] = claim_ids


def retrieve_grounding(question: str, db, top_k: int = 8) -> list[GroundedClaim]:
    """Return top_k claims most relevant to the question, with evidence preloaded."""
    from app.models.claim import Claim, Evidence, EvidenceVote
    from app.models.page import WikiPage
    from sqlalchemy import func

    _ensure_index(db)
    idf = _cache["idf"]
    vectors = _cache["vectors"]

    q_tokens = _tokenize(question)
    q_tf = Counter(q_tokens)
    q_n = sum(q_tf.values()) or 1
    q_vec = {t: (q_tf[t] / q_n) * idf.get(t, 1.0) for t in q_tf if t in idf}

    if not q_vec:
        return []

    # Score all claims
    scored = [(cid, _cosine(q_vec, vec)) for cid, vec in vectors.items()]
    scored.sort(key=lambda x: -x[1])

    out = []
    for cid, sim in scored[:top_k * 2]:
        if sim < 0.08:
            break

        claim = db.query(Claim).filter(Claim.id == cid).first()
        if not claim:
            continue

        evidence = (
            db.query(Evidence)
            .filter(Evidence.claim_id == cid, Evidence.quality >= 0.40)
            .order_by(Evidence.quality.desc())
            .limit(3).all()
        )
        if not evidence:
            continue

        ev_ids = [e.id for e in evidence]
        n_votes = db.query(func.count(EvidenceVote.id)).filter(
            EvidenceVote.evidence_id.in_(ev_ids)
        ).scalar() or 0

        page = db.query(WikiPage).filter(WikiPage.id == claim.page_id).first()

        grounded_ev = [
            GroundedEvidence(
                arxiv_id=e.arxiv_id,
                doi=e.doi,
                title=e.title or "",
                authors=e.authors,
                year=e.year,
                abstract_excerpt=(e.abstract or "")[:200],
                quality=e.quality or 0.5,
                n_jury_votes=n_votes,
                stance=e.stance,
            )
            for e in evidence
        ]

        out.append(GroundedClaim(
            claim_id=cid,
            claim_text=claim.text,
            section=claim.section or "",
            page_title=page.title if page else "",
            page_slug=page.slug if page else "",
            trust_level=claim.trust_level,
            trust_score=claim.trust_score or 0.0,
            evidence=grounded_ev,
            relevance=sim,
            n_jury_votes=n_votes,
        ))

        if len(out) >= top_k:
            break

    return out


def invalidate_index() -> None:
    """Call after claim inserts/updates to force re-build."""
    _cache["idf"] = {}
    _cache["vectors"] = {}
    _cache["claim_ids"] = []
