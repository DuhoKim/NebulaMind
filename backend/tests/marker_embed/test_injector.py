"""Tests for injector.py — every §3.3 deny-list case."""
import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.agent_loop.marker_embed.injector import (
    inject_markers,
    strip_markers,
    InjectionCandidate,
)


def _cand(claim_id: int, sentence: str, span: str, confidence: float = 0.85) -> InjectionCandidate:
    return InjectionCandidate(
        claim_id=claim_id,
        chosen_sentence=sentence,
        span=span,
        confidence=confidence,
        judge_agreement=0.9,
    )


# ── strip_markers (idempotency) ────────────────────────────────────────────────

def test_strip_markers_removes_existing():
    content = "Before <!--claim:1-->the span<!--/claim:1--> after."
    result = strip_markers(content)
    assert "<!--claim:1-->" not in result
    assert "the span" in result


def test_strip_markers_idempotent():
    content = "Plain text without markers."
    assert strip_markers(content) == content


# ── Basic injection ────────────────────────────────────────────────────────────

def test_basic_injection():
    content = "Galaxy formation depends on dark matter halos. Stars form in molecular clouds."
    sentence = "Galaxy formation depends on dark matter halos."
    span = "dark matter halos"
    result = inject_markers(content, [_cand(42, sentence, span)])
    assert "<!--claim:42-->dark matter halos<!--/claim:42-->" in result.content
    assert result.injected_count == 1
    assert not result.validation_errors


def test_injection_validation_open_close_match():
    content = "Quenching occurs via AGN feedback mechanisms in massive galaxies."
    sentence = "Quenching occurs via AGN feedback mechanisms in massive galaxies."
    span = "AGN feedback mechanisms"
    result = inject_markers(content, [_cand(7, sentence, span)])
    assert result.injected_count == 1
    assert not result.validation_errors


# ── Deny-list: forbidden injection sites ──────────────────────────────────────

def test_deny_heading_h2():
    content = "## AGN feedback drives quenching\n\nSome prose follows here."
    sentence = "## AGN feedback drives quenching"
    span = "AGN feedback drives quenching"
    result = inject_markers(content, [_cand(1, sentence, span)])
    assert result.skipped_unsafe == 1
    assert result.injected_count == 0


def test_deny_code_fence():
    content = "```\nAGN feedback is the mechanism\n```\n\nSome prose."
    sentence = "AGN feedback is the mechanism"
    span = "AGN feedback"
    result = inject_markers(content, [_cand(2, sentence, span)])
    # Span is inside code fence — should be unsafe
    assert result.skipped_unsafe == 1 or result.injected_count == 0


def test_deny_inline_code():
    content = "The `AGN feedback` model predicts quenching. Other content here."
    sentence = "The `AGN feedback` model predicts quenching."
    span = "AGN feedback"
    result = inject_markers(content, [_cand(3, sentence, span)])
    assert result.skipped_unsafe == 1
    assert result.injected_count == 0


def test_deny_link_text():
    content = "See [AGN feedback paper](https://example.com) for details."
    sentence = "See [AGN feedback paper](https://example.com) for details."
    span = "AGN feedback paper"
    result = inject_markers(content, [_cand(4, sentence, span)])
    assert result.skipped_unsafe == 1
    assert result.injected_count == 0


def test_deny_math_inline():
    content = "The relation $n_s = 0.9649 \\pm 0.0042$ constrains inflation models."
    sentence = "The relation $n_s = 0.9649 \\pm 0.0042$ constrains inflation models."
    span = "n_s = 0.9649"
    result = inject_markers(content, [_cand(5, sentence, span)])
    assert result.skipped_unsafe == 1
    assert result.injected_count == 0


def test_deny_bold_emphasis():
    content = "**Environmental quenching** is the dominant mechanism in clusters."
    sentence = "**Environmental quenching** is the dominant mechanism in clusters."
    span = "Environmental quenching"
    result = inject_markers(content, [_cand(6, sentence, span)])
    assert result.skipped_unsafe == 1
    assert result.injected_count == 0


def test_deny_preexisting_marker():
    content = "Stars form in <!--claim:99-->molecular clouds<!--/claim:99--> under gravity."
    sentence = "Stars form in molecular clouds under gravity."
    # After strip, the marker is removed, so this should succeed
    result = inject_markers(content, [_cand(100, sentence, "molecular clouds")])
    assert result.injected_count == 1
    assert "<!--claim:100-->molecular clouds<!--/claim:100-->" in result.content


# ── Ambiguity handling ────────────────────────────────────────────────────────

def test_ambiguous_span_falls_back_to_sentence():
    """A short repeated span falls back to the full chosen sentence."""
    content = (
        "AGN feedback suppresses star formation. "
        "Many studies confirm AGN feedback reduces gas accretion. "
        "In clusters, AGN feedback is particularly strong."
    )
    sentence = "Many studies confirm AGN feedback reduces gas accretion."
    span = "AGN feedback"  # appears 3 times in content
    result = inject_markers(content, [_cand(10, sentence, span)])
    assert result.injected_count == 1
    assert f"<!--claim:10-->{sentence}<!--/claim:10-->" in result.content
    assert result.skipped_ambiguous == 0


# ── Per-sentence deduplication ────────────────────────────────────────────────

def test_multi_claims_stack_per_sentence():
    """Two claims pointing to the same sentence share one grouped marker span."""
    content = "Environmental quenching dominates in dense cluster environments."
    sentence = "Environmental quenching dominates in dense cluster environments."
    cand_low = _cand(1, sentence, "Environmental quenching", confidence=0.72)
    cand_high = _cand(2, sentence, "cluster environments", confidence=0.91)
    result = inject_markers(content, [cand_low, cand_high])
    assert result.injected_count == 2
    assert f"<!--claim:1,2-->{sentence}<!--/claim:1,2-->" in result.content
    assert not result.validation_errors


# ── Reverse-order stability ────────────────────────────────────────────────────

def test_multiple_injections_stable():
    """Multiple injections in different sentences should all succeed."""
    content = (
        "Dark matter halos seed galaxy formation. "
        "Star formation rates decline at z < 2."
    )
    cands = [
        _cand(1, "Dark matter halos seed galaxy formation.", "Dark matter halos"),
        _cand(2, "Star formation rates decline at z < 2.", "Star formation rates"),
    ]
    result = inject_markers(content, cands)
    assert result.injected_count == 2
    assert "<!--claim:1-->Dark matter halos<!--/claim:1-->" in result.content
    assert "<!--claim:2-->Star formation rates<!--/claim:2-->" in result.content
    assert not result.validation_errors
