"""Fast intent classifier — no LLM in hot path."""
from dataclasses import dataclass

ASTRO_KEYWORDS = frozenset("""
galaxy star stellar neutron pulsar magnetar supernova quasar black hole
dark matter energy cosmos universe inflation big bang hubble gravity
gravitational wave exoplanet planet asteroid comet orbit telescope
redshift blueshift parsec light year astronomy astrophysics nebula
cluster mass luminosity singularity event horizon hawking radiation
accretion disk agn solar magnetic plasma corona cmb baryon boson
spacetime quantum white dwarf binary merger lensing reionization
""".split())

OFF_TOPIC_CUES = frozenset("""
recipe cook food restaurant movie film music sport football basketball
weather stock crypto bitcoin nft politics election president country
""".split())


@dataclass
class IntentResult:
    topic: str       # "astronomy" | "off_topic"
    mode: str        # "definitional" | "explanatory" | "comparative" | "refuse" | "general"
    confidence: float


def classify_intent(question: str) -> IntentResult:
    q = question.lower().strip()
    words = set(q.split())

    if any(w in q for w in OFF_TOPIC_CUES) and not any(w in q for w in ASTRO_KEYWORDS):
        return IntentResult(topic="off_topic", mode="refuse", confidence=0.9)

    has_astro = any(w in q for w in ASTRO_KEYWORDS)
    if not has_astro:
        # Borderline — could still be astronomy phrased differently
        return IntentResult(topic="off_topic", mode="refuse", confidence=0.6)

    if any(phrase in q for phrase in ["what is", "define", "meaning", "what are"]):
        return IntentResult(topic="astronomy", mode="definitional", confidence=0.85)
    if any(phrase in q for phrase in ["how does", "how do", "why does", "why do", "explain", "how is"]):
        return IntentResult(topic="astronomy", mode="explanatory", confidence=0.85)
    if any(phrase in q for phrase in ["versus", " vs ", "compare", "debate", "difference", "controversy"]):
        return IntentResult(topic="astronomy", mode="comparative", confidence=0.85)

    return IntentResult(topic="astronomy", mode="general", confidence=0.7)
