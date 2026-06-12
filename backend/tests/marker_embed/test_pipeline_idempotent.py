"""Test that running the injector twice on the same content yields identical output."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.agent_loop.marker_embed.injector import (
    inject_markers,
    strip_markers,
    InjectionCandidate,
)


def _cand(claim_id: int, sentence: str, span: str) -> InjectionCandidate:
    return InjectionCandidate(
        claim_id=claim_id,
        chosen_sentence=sentence,
        span=span,
        confidence=0.85,
        judge_agreement=0.9,
    )


_CONTENT = """\
## Quenching Mechanisms

AGN feedback suppresses star formation in massive galaxies at high redshift.
Ram-pressure stripping removes cold gas from satellite galaxies in dense clusters.
Stellar feedback drives galactic winds that regulate the baryon cycle.
"""

_CANDIDATES = [
    _cand(1, "AGN feedback suppresses star formation in massive galaxies at high redshift.", "AGN feedback"),
    _cand(2, "Ram-pressure stripping removes cold gas from satellite galaxies in dense clusters.", "cold gas"),
    _cand(3, "Stellar feedback drives galactic winds that regulate the baryon cycle.", "galactic winds"),
]


def test_idempotent_double_run():
    """Running inject_markers twice produces the same result."""
    result1 = inject_markers(_CONTENT, _CANDIDATES)
    assert result1.injected_count == 3
    assert not result1.validation_errors

    # Second run on already-injected content
    result2 = inject_markers(result1.content, _CANDIDATES)
    assert result2.injected_count == result1.injected_count
    assert result2.content == result1.content


def test_strip_then_reinject():
    """Strip markers, then reinject — should yield the same marked content."""
    result1 = inject_markers(_CONTENT, _CANDIDATES)
    stripped = strip_markers(result1.content)

    # Stripped content should equal original
    assert stripped.strip() == _CONTENT.strip()

    result2 = inject_markers(stripped, _CANDIDATES)
    assert result2.content == result1.content
    assert result2.injected_count == result1.injected_count


def test_no_markers_after_strip():
    result = inject_markers(_CONTENT, _CANDIDATES)
    stripped = strip_markers(result.content)
    assert "<!--claim:" not in stripped
    assert "<!--/claim:" not in stripped


def test_marker_count_stable():
    """Injected marker count is stable across re-runs."""
    r1 = inject_markers(_CONTENT, _CANDIDATES)
    r2 = inject_markers(r1.content, _CANDIDATES)
    r3 = inject_markers(r2.content, _CANDIDATES)
    assert r1.injected_count == r2.injected_count == r3.injected_count
    assert r2.content == r3.content
