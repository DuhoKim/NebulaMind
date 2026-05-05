"""Wiki page health score computation — 6 weighted dimensions."""
from __future__ import annotations
import json
import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.page import WikiPage

HEALTH_WEIGHTS = {
    "depth": 0.25,
    "freshness": 0.15,
    "balance": 0.10,
    "hero_richness": 0.10,
    "claim_density": 0.20,
    "sourcing": 0.20,
}

BAND_LABELS = {
    (80, 101): ("Excellent", "🟢"),
    (60, 80):  ("Good", "🔵"),
    (40, 60):  ("Fair", "🟡"),
    (20, 40):  ("Poor", "🟠"),
    (0, 20):   ("Critical", "🔴"),
}


def get_health_band(score: float) -> tuple[str, str]:
    for (lo, hi), (label, emoji) in BAND_LABELS.items():
        if lo <= score < hi:
            return label, emoji
    return "Critical", "🔴"


def compute_health_score(page, db) -> dict:
    """Compute 0-100 health score for a wiki page. Returns full breakdown."""
    from app.models.claim import Claim, Evidence
    from app.services.subtopic_maps import get_required_subtopics, is_subtopic_covered, coverage_ratio as _coverage_ratio
    from sqlalchemy import func

    # --- Dimension 1: Depth (subtopic coverage) ---
    claims = db.query(Claim).filter(Claim.page_id == page.id).all()
    claim_texts = [c.text for c in claims]
    depth_ratio, missing_list = _coverage_ratio(page.slug, claim_texts)
    required_subtopics = list(get_required_subtopics(page.slug).keys())
    depth = depth_ratio

    # --- Dimension 2: Freshness (recent evidence) ---
    current_year = datetime.datetime.utcnow().year
    cutoff_year = current_year - 2
    all_evidence = db.query(Evidence).join(
        Claim, Claim.id == Evidence.claim_id
    ).filter(Claim.page_id == page.id).all()
    if all_evidence:
        recent = sum(1 for e in all_evidence if e.year and e.year >= cutoff_year)
        freshness = min(1.0, (recent / len(all_evidence)) / 0.30)  # 30% recent = full score
    else:
        freshness = 0.0

    # --- Dimension 3: Balance (perspective coverage) ---
    perspective_keywords = {
        "observational": ["observed", "detection", "survey", "measurement", "telescope"],
        "theoretical": ["theory", "model", "simulation", "mechanism", "prediction"],
        "computational": ["simulation", "numerical", "code", "N-body", "SPH", "hydrodynamic"],
    }
    perspectives_present = set()
    for ev in all_evidence:
        text = ((ev.title or "") + " " + (ev.abstract or "")[:300]).lower()
        for persp, keywords in perspective_keywords.items():
            if any(kw in text for kw in keywords):
                perspectives_present.add(persp)
    balance = len(perspectives_present) / 3.0

    # --- Dimension 4: Hero richness ---
    hero_score = 0.0
    if page.hero_facts:
        try:
            facts = json.loads(page.hero_facts)
            if isinstance(facts, list) and facts:
                n_facts = len(facts)
                n_range = sum(1 for f in facts if f.get("kind") == "range")
                n_sourced = sum(1 for f in facts
                                if (f.get("source") or {}).get("tier") in ("authoritative", "claim"))
                hero_score = (
                    min(1.0, n_facts / 3.0) * 0.4 +
                    min(1.0, n_range) * 0.2 +
                    min(1.0, n_sourced / max(1, n_facts)) * 0.4
                )
        except Exception:
            pass

    # --- Dimension 5: Claim density ---
    claim_count = len(claims)
    claim_density = min(1.0, claim_count / 22.0)  # target 22

    # --- Dimension 6: Sourcing (% claims with quality evidence) ---
    if claim_count > 0:
        claims_with_ev = sum(
            1 for c in claims
            if db.query(func.count(Evidence.id)).filter(
                Evidence.claim_id == c.id,
                Evidence.quality >= 0.40,
            ).scalar() > 0
        )
        sourcing = claims_with_ev / claim_count
    else:
        sourcing = 0.0

    # --- Combine ---
    components = {
        "depth": round(depth, 3),
        "freshness": round(freshness, 3),
        "balance": round(balance, 3),
        "hero_richness": round(hero_score, 3),
        "claim_density": round(claim_density, 3),
        "sourcing": round(sourcing, 3),
    }
    score = 100 * sum(HEALTH_WEIGHTS[k] * v for k, v in components.items())
    score = round(score, 1)

    weakest = sorted(components, key=lambda k: components[k] * HEALTH_WEIGHTS[k])[:2]
    band_label, band_emoji = get_health_band(score)

    missing_subtopics = missing_list

    return {
        "score": score,
        "band": band_label,
        "emoji": band_emoji,
        "components": components,
        "weakest_dimensions": weakest,
        "missing_subtopics": missing_subtopics[:5],  # top 5 most critical
        "claim_count": claim_count,
        "evidence_count": len(all_evidence),
    }
