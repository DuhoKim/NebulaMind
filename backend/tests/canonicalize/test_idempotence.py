import pytest
from app.services.content_canonicalizer import canonicalize

def test_canonicalize_idempotency():
    inputs = [
        "Let \(M_{\text{vir}}\) be the mass.",
        "Equation: \[ \delta \rho / \rho \]",
        "The virial temperature is T_vir and radius is R_e.",
        "The density is ρ_SFR at the center.",
        "An _orphan_ word should be escaped.",
        "Math $T_vir$ and bare T_vir",
        "The mass of the cluster is 10¹² solar masses.",
        "Let's check 10⁻⁵ or delta rho / rho ~ 10⁻⁵",
        "The stellar mass is M★ and gas mass is M☉.",
        "A composite break like $10^{11}$·⁸ should be merged."
    ]

    for text in inputs:
        res1 = canonicalize(text)
        res2 = canonicalize(res1.new_content)
        assert res1.new_content == res2.new_content
        assert res2.changes["latex_paren"] == 0
        assert res2.changes["num_sup"] == 0
        assert res2.changes["symbol"] == 0
        assert res2.changes["bare_sub"] == 0
        assert res2.changes["orphan_us"] == 0
        assert res2.changes["composite"] == 0
        assert res2.invariants_ok is True
