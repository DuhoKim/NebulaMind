"""Composite quality scorer — §1.2 formula.

v4 (2026-05-12): rubric_to_utility() deprecated — use
`app.agent_loop.autowiki.judge.compute_utility(judge_dims, python_dims)`.
The composite formula `compute_quality(h_struct, utility)` is unchanged.
"""


def rubric_to_utility(rubric: dict) -> float:
    """DEPRECATED in v4. Use judge.compute_utility() instead.

    This stub raises so any forgotten caller fails loudly. The v4 scoring
    pipeline is hybrid (5 Python dims + 5 judge dims) and cannot be
    summarized by the v3 5-key integer rubric. See docs/autowiki_loop_v1.md
    §13 for the migration."""
    raise RuntimeError(
        "scorer.rubric_to_utility() is deprecated (v3). "
        "Use judge.compute_utility(judge_dims, python_dims) instead — see §13."
    )


def compute_quality(h_struct: float, utility: float) -> float:
    """§1.2: quality = 0.35 * h_struct/100 + 0.65 * utility/10
    Returns value in [0, 1]."""
    return round(0.35 * (h_struct / 100.0) + 0.65 * (utility / 10.0), 4)
