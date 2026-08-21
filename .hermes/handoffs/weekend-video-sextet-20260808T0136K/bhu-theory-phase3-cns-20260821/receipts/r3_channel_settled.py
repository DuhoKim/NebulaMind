#!/usr/bin/env python3
"""R3 — the He-star channel applies to J1913+1102, so the proviso is live.

Ferdman et al. 2020 (Nature 583, 211; arXiv:2007.04175), verbatim: J1913+1102 belongs to a
population "e.g. PSRs J0737-3039A/B and J1756-2251" whose path has "the second-formed NS
... born as a result of an envelope-stripped helium star progenitor"; and the pulsar "was
the first-formed neutron star ... subsequently recycled by accretion of matter from the
progenitor to the second NS".  Those are the two systems BLR's Phys.Rept. 462 Sec 3.2
proviso is written for, and the same mechanism.
"""
import math

CEIL_FRAC = 0.04                      # derived in R2 (10% He-burning window / 2.5)
CASES = {
    "Ferdman+2020 (Nature 583, 211)":      (1.62,  0.03,  1.27,  0.03),
    "2026 A&A update (arXiv:2606.19276)":  (1.599, 0.008, 1.290, 0.008),
}
print(f"{'measurement':38} {'deposit':>8} {'ceiling':>9} {'obs dM':>16} {'excess':>9} {'sigma':>7}")
for name, (mA, sA, mB, sB) in CASES.items():
    dm, sig = mA - mB, math.hypot(sA, sB)
    for dep in (0.0, 0.2):
        ceil = CEIL_FRAC * mB + dep
        exc = dm - ceil
        print(f"{name:38} {dep:8.1f} {ceil:9.3f} {dm:9.3f}+/-{sig:.3f} {exc:9.3f} {exc/sig:7.1f}")
print("\nDirection check (the proviso predicts the FIRST-BORN is the heavier one):")
print("  Ferdman: pulsar = first-formed, recycled by accretion, 1.62 Msun;")
print("           companion = second-formed NS, 1.27 Msun.  Heavier = first-born -> MATCHES.")
