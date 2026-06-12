import pytest
from app.services.content_canonicalizer import canonicalize

def test_latex_paren_delimiters():
    # Inline \(...\)
    res = canonicalize(r"Let \(M_{\text{vir}}\) be the mass.")
    assert res.new_content == r"Let $M_{\text{vir}}$ be the mass."
    assert res.changes["latex_paren"] == 1

    # Block \[...\]
    res = canonicalize(r"Equation: \[ \delta \rho / \rho \]")
    assert res.new_content == r"Equation: $$ \delta \rho / \rho $$"
    assert res.changes["latex_paren"] == 1

def test_bare_subscripts():
    res = canonicalize("The virial temperature is T_vir and radius is R_e.")
    assert res.new_content == "The virial temperature is $T_{\\text{vir}}$ and radius is $R_{\\text{e}}$."
    assert res.changes["bare_sub"] == 2

    # Verify Greek bare subscripts are also wrapped
    res = canonicalize("The density is ρ_SFR at the center.")
    assert res.new_content == "The density is $\\rho_{\\text{SFR}}$ at the center."
    assert res.changes["symbol"] == 1

def test_orphan_underscores():
    res = canonicalize("An _orphan_ word should be escaped.")
    assert res.new_content == "An \\_orphan\\_ word should be escaped."
    assert res.changes["orphan_us"] == 1

    # Protected underscore inside math
    res = canonicalize("Math $T_vir$ and bare T_vir")
    assert res.new_content == "Math $T_vir$ and bare $T_{\\text{vir}}$"

def test_legacy_cite_spans_become_markers():
    res = canonicalize('Fact <span data-cite-ids="12, 34">(Smith 2020)</span>.')
    assert res.new_content == "Fact <!--cite:12,34-->."
    assert res.changes["cite"] == 1
