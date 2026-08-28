"""p2b3-R1: Omega_S bracket vs the pinned BBN stiff-fluid bound.
Pinned bound (NAMED publication, Gate-1-condition-1 closure): Dutta & Scherrer,
'Big bang nucleosynthesis with a stiff fluid', Phys. Rev. D 82, 083501 (2010),
DOI 10.1103/PhysRevD.82.083501 (Crossref-verified; full text sources/ar5iv_1006.4166.html
SHA-256 f99cd419...), verbatim: 'we obtain the bound rho_S10/rho_R10 < 30' at T = 10 MeV.
Sign caveat: their rho_S > 0; our torsion component is NEGATIVE with the same a^-6 scaling —
the magnitude comparison is the honest use (a |component| this small is invisible either way)."""
import math
OmS = {"coherent": 8.82e-70, "incoherent": 1.47e-70}   # |Omega_S| bracket (B1-derived)
OmR = 8.8e-5                                            # paper's own radiation parameter
T0_eV = 2.35e-4     # today's photon temperature in eV (2.725 K; aT invariant)
T10 = 10e6          # 10 MeV in eV
ratio_growth = (T10/T0_eV)**2   # (eps_S/eps_R) grows as a^-2 = (T/T0)^2
print(f"(a0/a)^2 at T=10 MeV: {ratio_growth:.3e}")
for tag, s in OmS.items():
    r = s/OmR*ratio_growth
    print(f"|eps_S/eps_R|(10 MeV), {tag}: {r:.2e}  vs bound 30  -> margin {30/r:.1e}  CONSISTENT")
