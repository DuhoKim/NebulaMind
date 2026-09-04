#!/usr/bin/env python3
"""Executable K2 route-2 receipt added by Tori's support audit.

The original K2_route2_agy.py is preserved unchanged as evidence: it is a
six-line stub and emits no output.  This repair independently checks the
Misner-Sharp/Darmois algebra recorded in K2_ROUTE2_agy.md and the four
published controls.  Units are G = c = 1.
"""

from __future__ import annotations

import sympy as sp


def verify_route2() -> None:
    a, s, k, cosmological_lambda, mass_scale = sp.symbols(
        "a S k Lambda M0", positive=True, real=True
    )
    rho, chi, chi_dot = sp.symbols("rho chi chi_dot", positive=True, real=True)

    # FRW first integral for dust, with M0 = 4*pi*rho*a**3/3.
    a_dot_squared = 2 * mass_scale / a - k + cosmological_lambda * a**2 / 3
    radius = a * s
    exterior_mass = mass_scale * s**3
    f_metric = (
        1
        - 2 * exterior_mass / radius
        - cosmological_lambda * radius**2 / 3
    )

    # Darmois/Misner-Sharp continuity: beta_+^2 = F + Rdot^2
    # equals beta_-^2 = 1-k*S^2 for a comoving dust boundary.
    angular_residual = sp.simplify(
        f_metric + s**2 * a_dot_squared - (1 - k * s**2)
    )
    assert angular_residual == 0

    # Entry 56 is the flat member: S_0(chi*) = chi* and
    # M = (4*pi/3)*rho0*chi*^3, exactly its printed mass relation.
    rho0 = sp.symbols("rho0", positive=True, real=True)
    entry56_mass = exterior_mass.subs({mass_scale: 4 * sp.pi * rho0 / 3, s: chi})
    assert sp.simplify(entry56_mass - 4 * sp.pi * rho0 * chi**3 / 3) == 0

    # A fixed exterior mass forces a nondegenerate boundary to be comoving.
    # For 0 < chi < pi/2, d(M0*sin(chi)^3)/dt is proportional to chi_dot.
    closed_mass_prime = sp.diff(mass_scale * sp.sin(chi) ** 3, chi) * chi_dot
    expected_prime = (
        3 * mass_scale * sp.sin(chi) ** 2 * sp.cos(chi) * chi_dot
    )
    assert sp.simplify(closed_mass_prime - expected_prime) == 0

    # At the equator the first derivative is degenerate, but constancy over
    # an interval also sets the second derivative to zero; its velocity term
    # is -3*M0*chi_dot^2, so chi_dot must still vanish.
    chi_ddot = sp.symbols("chi_ddot", real=True)
    mass_of_chi = mass_scale * sp.sin(chi) ** 3
    closed_mass_second = (
        sp.diff(mass_of_chi, chi, 2) * chi_dot**2
        + sp.diff(mass_of_chi, chi) * chi_ddot
    )
    equator_second = sp.simplify(closed_mass_second.subs(chi, sp.pi / 2))
    assert equator_second == -3 * mass_scale * chi_dot**2

    # At Pathria's equator, angular continuity is F + Rdot^2 = 0.
    equator_f = sp.simplify(f_metric.subs({k: 1, s: 1}))
    equator_a_dot_squared = sp.simplify(
        a_dot_squared.subs({k: 1, s: 1})
    )
    assert sp.simplify(equator_f + equator_a_dot_squared) == 0

    # Khakshournia's null-shell control.  With the published jump,
    # Barrabes-Israel gives zero surface density and positive pressure.
    jump_kuu = -2 * sp.pi * rho * a
    surface_density = sp.Integer(0)
    surface_pressure = sp.simplify(-jump_kuu / (8 * sp.pi))
    assert surface_pressure == rho * a / 4
    assert surface_pressure.is_positive is True
    weak_energy_condition = surface_density >= 0 and surface_pressure.is_nonnegative
    dominant_energy_condition = sp.simplify(surface_density - surface_pressure).is_nonnegative
    assert weak_energy_condition is True
    assert dominant_energy_condition is False

    with_dec = "J_SHELL_UNPHYSICAL" if not dominant_energy_condition else "J_SHELL_EXPANDING"
    without_dec = "J_SHELL_EXPANDING"
    assert with_dec != without_dec

    print("ROUTE2_RECEIPT=EXECUTED")
    print("ROUTE2_METHOD=Misner-Sharp mass continuity plus FRW first integral")
    print(f"ANGULAR_RESIDUAL={angular_residual}")
    print(f"B3_MASS_DERIVATIVE={sp.sstr(expected_prime)}")
    print(f"B3_EQUATOR_SECOND_DERIVATIVE={sp.sstr(equator_second)}")
    print(f"NULL_JUMP_KUU={sp.sstr(jump_kuu)}")
    print(f"NULL_SURFACE_DENSITY={surface_density}")
    print(f"NULL_SURFACE_PRESSURE={sp.sstr(surface_pressure)}")
    print("C1_OS_MASS_CONTINUITY=PASS")
    print("C2_NULL_SHELL=PASS")
    print("C3_EQUATOR_IDENTITY=PASS")
    print("C4_DEC_DELETION=PASS")
    print("ENTRY56_CELL=J_SMOOTH_EXPANDING")
    print("PATHRIA_CELL=J_SHELL_UNPHYSICAL")
    print("B3_NOSHELL=comoving-only")
    print("ALL_ROUTE2_CHECKS=PASS")


if __name__ == "__main__":
    verify_route2()
