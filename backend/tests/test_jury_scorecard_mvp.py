import pytest
from app.services.jury_scorecard import JurorScorecard, PolicySpec, aggregate_scorecards, ConsensusScorecard

class DummyProfile:
    def __init__(self, tier, domain, reliability, calibration=1.0):
        self.tier_weight = tier
        self.domain_weight = domain
        self.reliability_weight = reliability
        self.calibration_temperature = calibration

def test_aggregate_scorecards_basic():
    jurors = [
        JurorScorecard(agent_id=1, verdict="SUPPORTS", R=1.0, E=0.8, M=0.9, C=1.0),
        JurorScorecard(agent_id=2, verdict="SUPPORTS", R=0.9, E=0.7, M=0.8, C=0.66),
        JurorScorecard(agent_id=3, verdict="ABSTAIN", R=0.5, E=0.0, M=0.5, C=0.33),
    ]
    policy = PolicySpec(support_threshold=0.65)
    profiles = {
        1: DummyProfile(1.0, 1.0, 0.9),  # raw weight = 0.9
        2: DummyProfile(0.7, 0.85, 0.8), # raw weight = 0.476
        3: DummyProfile(0.4, 0.7, 0.6),   # raw weight = 0.168
    }
    
    consensus = aggregate_scorecards(jurors, policy, profiles)
    
    assert consensus.stance in ("supports", "neutral", "refutes")
    assert 0.0 <= consensus.relevance <= 1.0
    assert -1.0 <= consensus.entailment <= 1.0
    assert 0.0 <= consensus.rigor <= 1.0
    assert 0.0 <= consensus.quality <= 1.0
