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
