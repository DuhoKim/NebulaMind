import math
from dataclasses import dataclass, field
from typing import Dict, List, Any

@dataclass
class JurorScorecard:
    agent_id: int
    verdict: str  # "SUPPORTS", "REFUTES", "ABSTAIN", or "ERROR"
    R: float  # Relevance (0.0 to 1.0)
    E: float  # Entailment (-1.0 to 1.0)
    M: float  # Rigor (0.0 to 1.0)
    C: float  # Confidence (0.0 to 1.0)
    quoted_sentence: str | None = None

@dataclass
class ConsensusScorecard:
    relevance: float
    entailment: float
    rigor: float
    confidence: float
    stance: str  # "supports", "refutes", "neutral"
    quality: float  # quality_v2
    var_entailment: float
    weights: dict[int, float]
    jurors: list[JurorScorecard]

    @classmethod
    def empty(cls, reason: str) -> "ConsensusScorecard":
        return cls(
            relevance=0.0,
            entailment=0.0,
            rigor=0.0,
            confidence=0.0,
            stance="neutral",
            quality=0.0,
            var_entailment=0.0,
            weights={},
            jurors=[],
        )

@dataclass
class PolicySpec:
    support_threshold: float = 0.65
    refute_threshold: float = 0.65
    abstain_band: list[float] = field(default_factory=lambda: [0.35, 0.65])
    min_quoted_sentence_chars: int = 25

def aggregate_scorecards(
    jurors: list[JurorScorecard],
    policy: PolicySpec,
    profiles: dict[int, Any]  # dict of agent_id -> JuryAgentProfile
) -> ConsensusScorecard:
    valid = [j for j in jurors if j.verdict != "ERROR"]
    if not valid:
        return ConsensusScorecard.empty(reason="no_jurors")

    raw_w = {}
    for j in valid:
        profile = profiles.get(j.agent_id)
        if profile is not None:
            raw_w[j.agent_id] = float(profile.tier_weight * profile.domain_weight * profile.reliability_weight)
        else:
            # default weights
            raw_w[j.agent_id] = 0.7 * 0.85 * 0.6

    total_raw_w = sum(raw_w.values()) or 1.0
    w = {aid: val / total_raw_w for aid, val in raw_w.items()}

    c_sum = sum(w[j.agent_id] * j.C for j in valid)
    if c_sum == 0:
        return ConsensusScorecard.empty(reason="zero_confidence")

    R_bar = sum(w[j.agent_id] * j.C * j.R for j in valid) / c_sum
    E_bar = sum(w[j.agent_id] * j.C * j.E for j in valid) / c_sum
    M_bar = sum(w[j.agent_id] * j.C * j.M for j in valid) / c_sum

    C_mean = sum(j.C for j in valid) / len(valid)
    var_E = sum(w[j.agent_id] * (j.E - E_bar) ** 2 for j in valid)
    CON = C_mean * (1.0 - math.sqrt(max(0.0, min(1.0, var_E))))

    if E_bar >= policy.support_threshold and CON >= 0.50:
        stance = "supports"
    elif E_bar <= -policy.refute_threshold and CON >= 0.50:
        stance = "refutes"
    else:
        stance = "neutral"

    quality_v2 = 0.35 * R_bar + 0.40 * abs(E_bar) + 0.15 * M_bar + 0.10 * CON

    return ConsensusScorecard(
        relevance=R_bar,
        entailment=E_bar,
        rigor=M_bar,
        confidence=CON,
        stance=stance,
        quality=quality_v2,
        var_entailment=var_E,
        weights=w,
        jurors=valid,
    )
