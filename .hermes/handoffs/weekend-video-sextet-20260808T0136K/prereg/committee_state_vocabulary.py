"""Frozen bijection between committee output and HC-1H input state names."""
from __future__ import annotations

COMMITTEE_STATES = ("AGREE_CONFIDENT", "DISAGREE", "LOW_CONFIDENCE")
HC1H_STATES = ("agree-confident", "disagree", "low-confidence")
COMMITTEE_TO_HC1H: dict[str, str] = dict(zip(COMMITTEE_STATES, HC1H_STATES))

if set(COMMITTEE_TO_HC1H) != set(COMMITTEE_STATES):
    raise RuntimeError("committee-state mapping is not total")
if len(set(COMMITTEE_TO_HC1H.values())) != len(COMMITTEE_TO_HC1H):
    raise RuntimeError("committee-state mapping is not injective")
if set(COMMITTEE_TO_HC1H.values()) != set(HC1H_STATES):
    raise RuntimeError("committee-state mapping does not cover HC-1H states")


def to_hc1h(state: str) -> str:
    try:
        return COMMITTEE_TO_HC1H[state]
    except KeyError as exc:
        raise ValueError(f"unknown committee state: {state!r}") from exc
