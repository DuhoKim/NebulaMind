#!/usr/bin/env python3
"""C3: where the model's only NUMBER comes from, and whether the chain that produced it
is self-consistent.

The chain (target = Gaztanaga, Kumar, Pradhan & Gabler, PRD 111 103537):

    Omega_k ceiling (0.07 +- 0.02)   Eq.27
      <- chi_*  = 15.93 +- 2.22 Gpc  Eq.26
      <- theta_cut = 65.9 +- 9.2 deg Eq.25   [Camacho-Quevedo & Gaztanaga 2022]
      <- with chi_CMB = 13.8 Gpc     Eq.24   "for Omega_Lambda ~ 0.7 and H0 ~ 70"

Two questions, both computed here:
  A. PROVENANCE -- is the anchoring measurement independent of the target's own authors?
  B. SELF-CONSISTENCY -- Eq.24 is a FLAT-geometry relation, and the source paper states its
     conversion assumes flat geometry. The target then uses the result to predict NON-zero
     curvature. Does that assumption survive at the curvature the model itself predicts?
"""
import math, sys

checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

# ---------------------------------------------------------------- A. provenance
TARGET_AUTHORS = ["Gaztanaga", "Sravan Kumar", "Pradhan", "Gabler"]
CHAIN = {   # citation -> author surnames, from the target's own reference list
    "Camacho-Quevedo & Gaztanaga 2022 (JCAP 04 044) -- SOURCE OF theta_cut":
        ["Camacho-Quevedo", "Gaztanaga"],
    "Gaztanaga & Camacho-Quevedo 2022 (PLB 835 137468)":
        ["Gaztanaga", "Camacho-Quevedo"],
    "Fosalba & Gaztanaga 2021 (MNRAS 504 5840)":
        ["Fosalba", "Gaztanaga"],
    "Efstathiou 2003 (MNRAS 343 L95) -- the one INDEPENDENT citation":
        ["Efstathiou"],
}
print("=" * 92)
print("A. PROVENANCE of the chain that fixes the model's only number")
print("=" * 92)
shared = {}
for cite, authors in CHAIN.items():
    ov = sorted(set(authors) & set(TARGET_AUTHORS))
    shared[cite] = ov
    print(f"  {cite}")
    print(f"     authors: {', '.join(authors)}")
    print(f"     shares with target: {', '.join(ov) if ov else 'NONE'}")

anchor = [c for c in CHAIN if "SOURCE OF theta_cut" in c][0]
chk("the measurement that fixes theta_cut shares an author with the target",
    len(shared[anchor]) > 0, f"shared: {', '.join(shared[anchor])}")
chk("EVERY supporting citation for the cutoff is co-authored by the target's lead author",
    all(shared[c] for c in CHAIN if "INDEPENDENT" not in c),
    "3 of 3 cutoff citations carry Gaztanaga")
indep = [c for c in CHAIN if "INDEPENDENT" in c][0]
chk("the sole independent citation shares NO author",
    not shared[indep], "Efstathiou 2003 is genuinely independent of the target")

print("""
  But note what the independent one contains. Efstathiou 2003, verbatim from its abstract:
    'Here we SPECULATE that the low quadrupole amplitude is associated with spatial curvature.
     We show that positively curved models are consistent with the WMAP data and that the
     quadrupole amplitude can be reproduced if the primordial spectrum truncates on scales
     comparable to the curvature scale.'
  It gives NO numerical scale. It cannot corroborate 15.93 +- 2.22 Gpc; it corroborates the
  IDEA. The target's wording ('agrees with a previous independent way of modeling the low
  quadrupole') is accurate as written -- it claims agreement of approach, not of number.

  And what the anchoring measurement says about itself, verbatim:
    'We present the FIRST measurement of the homogeneity index ... This finding is AT ODDS
     with the LambdaCDM prediction ... Such ANOMALY is consistent with the well known low
     quadrupole amplitude'
  So the model's only number rests on a single unreplicated measurement that its own authors
  describe as anomalous.
""")

# ------------------------------------------------- B. is the flat conversion self-consistent?
# Camacho-Quevedo & Gaztanaga, verbatim: "ASSUMING TRANSLATION INVARIANCE (AND FLAT GEOMETRY)
# we can convert the isotropy scale theta_H into a (comoving) homogeneity scale".
# The target then feeds that into Eq.27 to predict Omega_k != 0.
C = 299792.458          # km/s
Z_CMB = 1090.0
H0, OM = 70.0, 0.30     # the target's own stated values for Eq.24

def comoving_chi(Ok, n=200000):
    """radial comoving distance to z_CMB, in Gpc, for curvature Ok."""
    OL = 1.0 - OM - Ok
    dz = Z_CMB / n
    s = 0.0
    for i in range(n):
        z = (i + 0.5) * dz
        E = math.sqrt(OM*(1+z)**3 + Ok*(1+z)**2 + OL)
        s += dz / E
    return (C / H0) * s / 1000.0        # Mpc -> Gpc

def transverse(Ok, chi):
    """comoving TRANSVERSE distance S_k(chi): what an angle actually subtends."""
    if abs(Ok) < 1e-12:
        return chi
    R = (C / H0) / math.sqrt(abs(Ok)) / 1000.0
    return R*math.sin(chi/R) if Ok < 0 else R*math.sinh(chi/R)

print("=" * 92)
print("B. SELF-CONSISTENCY of the flat-geometry conversion")
print("=" * 92)
chi_flat = comoving_chi(0.0)
print(f"  flat geometry:      chi_CMB = {chi_flat:.3f} Gpc   (target's Eq.24 states ~13.8 Gpc)")
chk("the flat calculation reproduces the target's own stated chi_CMB -- positive control",
    abs(chi_flat - 13.8) < 0.6, f"computed {chi_flat:.3f} vs stated 13.8 Gpc")

THETA = 65.9 * math.pi / 180.0
chi_star_flat = THETA * chi_flat
print(f"  chi_* from Eq.24:   theta_cut x chi_CMB = {chi_star_flat:.3f} Gpc   "
      f"(target's Eq.26 states 15.93 Gpc)")
chk("and reproduces the target's chi_* to within its own quoted uncertainty",
    abs(chi_star_flat - 15.93) < 2.22, f"computed {chi_star_flat:.3f} vs stated 15.93 +- 2.22")

print(f"\n  Now redo it AT THE CURVATURE THE MODEL PREDICTS, using the transverse distance:")
print(f"  {'Omega_k':>9} {'chi_CMB':>10} {'S_k(chi)':>10} {'chi_* implied':>15} {'shift vs flat':>15}")
rows = []
for Ok in (0.0, -0.02, -0.05, -0.07, -0.09):
    ch = comoving_chi(Ok)
    Sk = transverse(Ok, ch)
    cs = THETA * Sk
    rows.append((Ok, cs))
    print(f"  {Ok:+9.2f} {ch:10.3f} {Sk:10.3f} {cs:15.3f} {100*(cs-chi_star_flat)/chi_star_flat:+14.1f}%")

worst = max(abs(cs - chi_star_flat) / chi_star_flat for _, cs in rows)
chk("the flat assumption is NOT benign at the curvature the model itself predicts",
    worst > 0.05, f"chi_* shifts by up to {100*worst:.1f}% across the model's own allowed band")
band = [cs for Ok, cs in rows if Ok <= -0.05]
chk("and the shift is comparable to the quoted uncertainty on chi_*, so it is not negligible",
    abs(band[0] - chi_star_flat) > 0.5 * 2.22,
    f"shift at Omega_k=-0.05 is {abs(band[0]-chi_star_flat):.2f} Gpc vs quoted +-2.22 Gpc")

print("""
  READING. Eq.24 is a flat-space relation and the source paper says its conversion assumes
  flat geometry. The target uses the output to predict NON-zero curvature without redoing the
  conversion at that curvature. The table shows the assumption is not free: inside the model's
  own allowed band the implied chi_* moves by an amount comparable to its quoted error bar.

  This is NOT a demonstration that the number is wrong. It is a demonstration that the number
  is not self-consistent as derived, and that the target does not check it. A first-order
  treatment might well survive; the point is that the check is absent, and the direction of
  the shift is not obviously favourable.

  GATE RESPONSE -- BOTH seats returned PASS_C3 independently, on different engines:
  CGATE_C3_VERDICT.md (codex gpt-5.5) and AGATE_C3_VERDICT.md (agy, Gemini 3.1 Pro).
  Neither broke point 1, and both gave the same reason independently. Agy states it most
  directly: "In a curved FLRW spacetime, the proper comoving arc length of an angle theta on
  a sphere of radial coordinate chi is precisely s = S_k(chi) theta. The form using a bare
  chi instead of S_k(chi) is strictly a flat-space Euclidean relation."
  Refinements adopted:

  (i) The S_k correction stands, and the gate supplied the reason more sharply than I did:
      the last-scattering two-sphere has radius S_k(chi_radial), NOT the radial geodesic
      distance. So the correction applies whether chi_* is read as a transverse separation or
      as an arc on that sphere. The only escape would be to redefine the target's chi_CMB as
      the transverse/areal coordinate -- but the target states it as the comoving radial
      distance for a FLAT fiducial, and imports Eq.24 from a source that says its conversion
      assumes flat geometry.

  (ii) THE LARGE-ANGLE POINT IS WITHDRAWN as a defect. I raised 65.9 deg = 1.15 rad against the
      small-angle form and explicitly declined to claim it; the gate resolved it against me.
      The 2022 measurement is genuinely angular at the measurement stage (pixel pair counts,
      exact 1-cos(theta) solid angle), and reading the scale as an ARC on the last-scattering
      sphere makes arc = theta * D_M exact. The chord would be ~5.4% smaller, but chord is not
      what is meant. Phrase it "arc, not chord" -- there is no small-angle error here.

  (iii) Provenance wording: the gate ruled it fair ONLY if stated narrowly. It is a
      single-point numerical dependency and a disclosure gap. It is NOT an allegation of
      misconduct, and nothing here should be read as one. Self-citation is ordinary practice;
      a first measurement has to be someone's.
""")
np_ = sum(1 for _, ok, _ in checks if ok)
print(f"SELF-CHECKS: {np_}/{len(checks)} passed")
sys.exit(0 if np_ == len(checks) else 1)
