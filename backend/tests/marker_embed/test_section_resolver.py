"""Tests for section_resolver.py — fuzzy section matching and excluded sections."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.agent_loop.marker_embed.section_resolver import (
    parse_sections,
    resolve_section,
    EXCLUDED_SECTIONS,
)

_SAMPLE_CONTENT = """\
# Galaxy Evolution

## Overview & Historical Context

The Milky Way is a typical spiral galaxy in the local universe.

## Quenching Mechanisms

AGN feedback and environmental quenching are the primary drivers of star formation cessation.

### AGN Feedback: Radiative and Kinetic Modes

Radiative mode AGN feedback heats the surrounding gas and suppresses cooling.

## Open Questions & Future Directions

Many open questions remain about the precise mechanisms of quenching at high redshift.
"""


def test_parse_sections_finds_h2():
    sections = parse_sections(_SAMPLE_CONTENT)
    titles = [s.title for s in sections]
    assert "Overview & Historical Context" in titles
    assert "Quenching Mechanisms" in titles
    assert "Open Questions & Future Directions" in titles


def test_parse_sections_excludes_h3():
    sections = parse_sections(_SAMPLE_CONTENT)
    titles = [s.title for s in sections]
    assert "AGN Feedback: Radiative and Kinetic Modes" not in titles


def test_parse_sections_body_content():
    sections = parse_sections(_SAMPLE_CONTENT)
    quench = next(s for s in sections if s.title == "Quenching Mechanisms")
    assert "AGN feedback" in quench.body


def test_resolve_section_exact():
    sections = parse_sections(_SAMPLE_CONTENT)
    result = resolve_section("Quenching Mechanisms", sections)
    assert result is not None
    assert result.title == "Quenching Mechanisms"


def test_resolve_section_exact_overview():
    sections = parse_sections(_SAMPLE_CONTENT)
    result = resolve_section("Overview & Historical Context", sections)
    assert result is not None
    assert "Milky Way" in result.body


def test_resolve_section_excluded():
    sections = parse_sections(_SAMPLE_CONTENT)
    result = resolve_section("Open Questions & Future Directions", sections)
    assert result is None


def test_resolve_section_excluded_constant():
    assert "Open Questions & Future Directions" in EXCLUDED_SECTIONS


def test_resolve_section_fuzzy_match():
    """Slightly misspelled section name should still resolve via Jaccard."""
    sections = parse_sections(_SAMPLE_CONTENT)
    result = resolve_section("Quenching Mechanism", sections)  # missing 's'
    assert result is not None
    assert result.title == "Quenching Mechanisms"


def test_resolve_section_no_match_returns_none():
    sections = parse_sections(_SAMPLE_CONTENT)
    result = resolve_section("Completely Unrelated Topic About Cats", sections)
    assert result is None


def test_resolve_section_char_start():
    sections = parse_sections(_SAMPLE_CONTENT)
    overview = next(s for s in sections if s.title == "Overview & Historical Context")
    assert overview.char_start > 0
    assert _SAMPLE_CONTENT[overview.char_start : overview.char_start + 2] == "##"
