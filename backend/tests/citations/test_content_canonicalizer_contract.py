from __future__ import annotations

from app.services.content_canonicalizer import canonicalize, verify_invariants


def test_unwraps_whole_page_markdown_fence_before_transforms() -> None:
    result = canonicalize("```markdown\n# Title\nThe value is H₀.\n```\n")

    assert result.changes["markdown_fence"] == 1
    assert "```" not in result.new_content
    assert "$H_{0}$" in result.new_content
    assert result.invariants_ok


def test_unwraps_unclosed_leading_markdown_fence() -> None:
    result = canonicalize("```md\n# Title\nThe radius is R_e.\n")

    assert result.changes["markdown_fence"] == 1
    assert result.new_content.startswith("# Title")
    assert "$R_{\\text{e}}$" in result.new_content
    assert result.invariants_ok


def test_non_markdown_leading_fence_is_quarantine_violation() -> None:
    content = '```json\n{"title": "Kuiper Belt"}\n```'

    result = canonicalize(content)

    assert result.changes["markdown_fence"] == 0
    assert "leading_code_fence" in (result.violations or [])
    assert not result.invariants_ok


def test_strips_nested_inline_math_inside_display_math() -> None:
    result = canonicalize("$$ds^2 = -(1 - $r_{\\text{s}}$/r)c^2dt^2$$")

    assert result.changes["nested_math"] == 2
    assert "$$ds^2 = -(1 - r_{\\text{s}}/r)c^2dt^2$$" in result.new_content
    assert "nested_math_delimiter" not in (result.violations or [])
    assert result.invariants_ok


def test_invariant_flags_remaining_nested_display_math_delimiters() -> None:
    violations = verify_invariants("$$x + $y$ = z$$")

    assert "nested_math_delimiter" in violations


def test_strips_author_year_parentheticals_before_invariant_check() -> None:
    result = canonicalize("This was measured previously (Smith et al. 2023) and refined (Johnson 2019).")

    assert result.changes["author_year_stripped"] == 2
    assert "(Smith et al. 2023)" not in result.new_content
    assert "(Johnson 2019)" not in result.new_content
    assert "author_year_parenthetical" not in (result.violations or [])
    assert result.invariants_ok


def test_strips_unknown_comments_but_keeps_registered_comments() -> None:
    result = canonicalize("A <!--cite:EVIDENCE_001--> B <!--debate:S0_production--> C <!--cite:42-->")

    assert result.changes["unknown_comments_stripped"] == 2
    assert "<!--cite:EVIDENCE_001-->" not in result.new_content
    assert "<!--debate:S0_production-->" not in result.new_content
    assert "<!--cite:42-->" in result.new_content
    assert not any(v.startswith("unknown_comment") for v in (result.violations or []))
    assert result.invariants_ok
