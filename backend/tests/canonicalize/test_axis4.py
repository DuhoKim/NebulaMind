import pytest
from app.services.content_canonicalizer import canonicalize

def test_unicode_exponents():
    res = canonicalize("The mass of the cluster is 10¹² solar masses.")
    assert res.new_content == "The mass of the cluster is $10^{12}$ solar masses."
    assert res.changes["num_sup"] == 1

    res = canonicalize("Let's check 10⁻⁵ or delta rho / rho ~ 10⁻⁵")
    assert res.new_content == "Let's check $10^{-5}$ or delta rho / rho ~ $10^{-5}$"
    assert res.changes["num_sup"] == 2

def test_star_sun_symbols():
    res = canonicalize("The stellar mass is M★ and gas mass is M☉.")
    assert res.new_content == "The stellar mass is $M_\\star$ and gas mass is $M_\\odot$."
    assert res.changes["symbol"] == 2

def test_composite_breaks():
    res = canonicalize("A composite break like $10^{11}$·⁸ should be merged.")
    assert res.new_content == "A composite break like $10^{11}.8$ should be merged."
    assert res.changes["composite"] == 1

    res = canonicalize("Cloud growth scales as $t_{\\text{cool}}$⁻¹.")
    assert res.new_content == "Cloud growth scales as $t_{\\text{cool}}^{-1}$."
    assert res.changes["composite"] == 1

def test_legacy_html_math_fragments():
    res = canonicalize("*M*<sub>⋆</sub> > 10<sup>10.5</sup> *M*<sub>⊙</sub> yr⁻¹")
    assert res.new_content == "$M_{\\star}$ > $10^{10.5}$ $M_{\\odot}$ $yr^{-1}$"
    assert res.invariants_ok

def test_unit_and_chemical_scripts():
    res = canonicalize("Use 250 W/m², 0.5 pc/cm³, H₂, and 4πΣ².")
    assert res.new_content == "Use 250 W/$m^{2}$, 0.5 pc/$cm^{3}$, $H_{2}$, and 4$\\pi\\Sigma^{2}$."
    assert res.invariants_ok
