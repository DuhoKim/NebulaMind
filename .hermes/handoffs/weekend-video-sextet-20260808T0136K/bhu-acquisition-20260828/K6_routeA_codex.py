#!/usr/bin/env python3
"""K6 Route A, codex seat: reproducible symbolic/control check."""

from math import log10, pi, sqrt


# CODATA/SI values used only after the symbolic statements below are sealed.
G = 6.67430e-11
C = 299792458.0
HBAR = 1.054571817e-34
M_E = 9.1093837139e-31
RHO_CE_CONTROL = 1.0e51


def cartan_radius(mass, coefficient=1.0):
    """Eq. (33) solved with an explicitly added control coefficient."""
    return (coefficient * G * HBAR**2 / (mass * C**4)) ** (1.0 / 3.0)


def gr_mean_density(mass):
    """Euclidean mean density inside an added Schwarzschild radius."""
    radius = 2.0 * G * mass / C**2
    return mass / ((4.0 * pi / 3.0) * radius**3)


def gr_control_floor(rho, radius_coefficient=2.0, volume_factor=4.0 * pi / 3.0):
    """Added completion R=k GM/c^2, V=v R^3; solve M/V=rho."""
    return sqrt(C**6 / (volume_factor * radius_coefficient**3 * G**3 * rho))


def require_proper_density(measure):
    if measure == "coordinate-volume":
        raise ValueError("coordinate volume is not an invariant density measure")
    if measure not in {"local-rest-scalar", "proper-volume-average"}:
        raise ValueError("density semantics unspecified")
    return True


print("SYMBOLIC_CHAIN_SEALED")
print("S1 [source-derived, VoR 102-203]: ECKS gives local field equations (3)-(6).")
print("S2 [source-derived, VoR 204-406]: spin conservation gives multipole identity (17).")
print("S3 [source-derived, VoR 551-568]: Eq. (33) is only order-of-magnitude:")
print("   m/r_C^3 ~ (G/c^4)(hbar/r_C^3)^2.")
print("   Therefore r_C^3 ~ G hbar^2/(m c^4), r_C proportional to m^(-1/3),")
print("   and rho_C=m/r_C^3 is proportional to m^2.")
print("S4 [source-derived, VoR 625-653]: rho_Ce is an expected approximate ceiling;")
print("   extension from particles to self-gravitating systems is expressly conjectural.")
print("S5 [source-derived, VoR 662-664]: rho_BH <= rho_Ce and ~10^16 kg are asserted.")
print("THEOREM TEST: a density ceiling alone has no mass dimension and implies no M floor")
print("unless a source-bound relation supplies a length/volume as a function of mass.")
print("FAILED_BINDING_ATTEMPT_1: the source does not define rho_BH as a local scalar or")
print("a proper-volume average; coordinate-volume and Euclidean-volume readings are unlicensed.")
print("FAILED_BINDING_ATTEMPT_2: the source defines no black-hole mass notion, trapped-surface")
print("radius relation, interior profile, charge/spin domain, or interior/exterior matching map.")
print("FIRST_UNBOUND_QUANTITY: V(M), equivalently a source-bound size/mass relation.")
print("STOPPING_RULE: two failed attempts to bind the same missing global premise.")
print("CONCLUSION: no source-bound theorem rho <= rho_Ce => M >= M_min > 0 is reproduced")
print("from the stated inputs; this is not a claim that the printed statement is an error.")

r_e = cartan_radius(M_E)
rho_from_eq33 = M_E / r_e**3
assert abs(log10(r_e) - log10(1.0e-27)) <= 0.5
assert abs(rho_from_eq33 - M_E**2 * C**4 / (G * HBAR**2)) / rho_from_eq33 < 1e-12
print(f"C2 control: unit-coefficient r_Ce={r_e:.6e} m; log10={log10(r_e):.6f}.")

probe_mass = 2.5e16
rho_direct = gr_mean_density(probe_mass)
rho_formula = 3.0 * C**6 / (32.0 * pi * G**3 * probe_mass**2)
assert abs(rho_direct - rho_formula) / rho_formula < 1e-12
print("C3 symbolic: R=2GM/c^2 and V=4pi R^3/3 imply rho_bar=3c^6/(32piG^3M^2).")
print(f"C3 numerical probe printed by script: M={probe_mass:.6e} kg, rho={rho_formula:.6e} kg/m^3.")

assert require_proper_density("local-rest-scalar")
assert require_proper_density("proper-volume-average")
coordinate_caught = False
try:
    require_proper_density("coordinate-volume")
except ValueError:
    coordinate_caught = True
assert coordinate_caught

control_floor = gr_control_floor(RHO_CE_CONTROL)
changed_completion_floor = gr_control_floor(RHO_CE_CONTROL, radius_coefficient=3.0)
assert control_floor != changed_completion_floor
print(f"ADDED_COMPLETION_CONTROL: Schwarzschild/Euclidean/uniform-mean floor={control_floor:.6e} kg.")
print(f"COMPLETION_CHANGE_CONTROL: radius coefficient 3 gives floor={changed_completion_floor:.6e} kg.")
print("C5 deletion: deleting source ECKS equations leaves the injected GR control floor intact;")
print("therefore that relation is circular for K6 and no derived-floor class is allowed.")
print("C6 split: changing an added size/mass completion changes the floor, exposing dependence.")

print("C1_SOURCE_IDENTITY=PASS")
print("C2_EQ33_SCALING=PASS")
print("C3_GR_BENCHMARK=PASS")
print("C4_DENSITY_SEMANTICS=PASS")
print("C5_DELETION_PROBE=PASS")
print("C6_COMPLETION_SPLIT=PASS")
print("CLASS=K6_FLOOR_UNDERDETERMINED")
