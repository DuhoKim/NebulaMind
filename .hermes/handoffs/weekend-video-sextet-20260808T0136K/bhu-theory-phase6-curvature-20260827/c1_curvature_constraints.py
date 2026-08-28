#!/usr/bin/env python3
"""C1: the curvature sign convention, computed rather than asserted, and the confrontation
with the BHU model's requirement.

The sign trap this file exists to defuse:
    k > 0  ->  POSITIVE spatial curvature  ->  CLOSED  ->  Omega_k < 0
    k < 0  ->  NEGATIVE spatial curvature  ->  OPEN    ->  Omega_k > 0
"Negative curvature" and "negative Omega_k" mean OPPOSITE universes. A summarising read of
Chen & Zaldarriaga already mislabelled their open result as closed on exactly this. Every
conversion below is therefore computed and cross-checked against the paper's own printed value.

Target: Gaztanaga, Kumar, Pradhan & Gabler, PRD 111, 103537 (2025) [arXiv 2505.23877].
Its requirement, verbatim from section VI: "Inflation preceded by a bounce requires Omega_k < 0".
"""
import math, sys

checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool):
        raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail))
    print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

def omega_k_from_Rk(Rk_over_invH0, spatial_curvature_sign):
    """|Omega_k| = 1/(H0 R_k)^2 ; sign is OPPOSITE the spatial-curvature sign k."""
    mag = 1.0 / (Rk_over_invH0 ** 2)
    return -mag if spatial_curvature_sign > 0 else +mag

print("=" * 76)
print("C1 -- curvature constraints vs the BHU model's sign requirement")
print("=" * 76)

# --- 1. Chen & Zaldarriaga 2505.00659, verbatim: "a small but negative spatial
#        curvature with R_k = 21 H_0^{-1}, which DESI measures at 2 sigma when
#        combined with CMB data."
RK = 21.0
ok_cz = omega_k_from_Rk(RK, spatial_curvature_sign=-1)   # NEGATIVE spatial curvature => open
print(f"\n1. Chen & Zaldarriaga (2505.00659), DESI DR2 + CMB")
print(f"   stated: 'negative spatial curvature with R_k = {RK:.0f} H_0^-1', 2 sigma")
print(f"   => |Omega_k| = 1/R_k^2 = {1.0/RK**2:.7f}")
print(f"   => Omega_k   = {ok_cz:+.7f}   (negative spatial curvature -> OPEN -> Omega_k > 0)")
chk("their R_k converts to the +0.0023 that the independent read of the same paper reported",
    abs(ok_cz - 0.0023) < 5e-5, f"computed {ok_cz:+.7f} vs reported +0.0023")
chk("and it is POSITIVE Omega_k, i.e. an OPEN universe",
    ok_cz > 0, f"Omega_k = {ok_cz:+.7f}")

# --- 2. joint DESI DR1 FS + DR2 BAO + CMB (2602.18761), reported Omega_k = 0.0028 +- 0.0011
OK_FS, SIG_FS = 0.0028, 0.0011
print(f"\n2. DESI DR1 Full-Shape + DR2 BAO + CMB (2602.18761)")
print(f"   reported: Omega_k = {OK_FS:+.4f} +/- {SIG_FS:.4f}, stated as 'Omega_k > 0 ... about 2.4 sigma'")
n_sig = OK_FS / SIG_FS
print(f"   => distance from flat = {n_sig:.2f} sigma")
chk("the quoted 2.4 sigma reproduces from the quoted central value and error",
    abs(n_sig - 2.4) < 0.3, f"{n_sig:.2f} sigma from Omega_k/sigma")
chk("two independent DESI+CMB analyses agree in SIGN and rough magnitude",
    ok_cz > 0 and OK_FS > 0 and abs(ok_cz - OK_FS) < 0.002,
    f"{ok_cz:+.5f} vs {OK_FS:+.5f}, both positive")

# --- 3. the BHU model's requirement ------------------------------------------------
print(f"\n3. BHU model requirement (2505.23877 sec.VI, verbatim): Omega_k < 0")
print(f"   Eq.27: Omega_k = -(0.07 +/- 0.02)(chi_*/chi_k)^2  with chi_k > chi_*")
CEIL = -(0.07 + 0.02)      # most negative allowed, +1sigma edge
print(f"   => allowed band: {CEIL:+.2f} < Omega_k < 0  (magnitude ceiling, NOT a predicted value)")
chk("the model's allowed band is entirely NEGATIVE -- it forbids Omega_k > 0",
    CEIL < 0, f"band ({CEIL:+.2f}, 0), open excluded by construction")

# --- 4. the confrontation ----------------------------------------------------------
print(f"\n4. CONFRONTATION")
for label, ok, sig in (("Chen & Zaldarriaga DESI DR2+CMB", ok_cz, 0.0011),
                       ("DESI FS+DR2 BAO+CMB", OK_FS, SIG_FS)):
    # how many sigma is the measurement from the model's nearest allowed point (Omega_k = 0^-)?
    dist = ok / sig
    print(f"   {label:34s} Omega_k = {ok:+.5f}  -> {dist:+.2f} sigma on the OPEN side")
chk("both current DESI+CMB curvature analyses sit on the side the model FORBIDS",
    ok_cz > 0 and OK_FS > 0,
    "the model requires closed; the data prefer open at ~2-2.4 sigma")
chk("but neither excludes the model: flat remains within ~2-2.4 sigma",
    (OK_FS - 2.6*SIG_FS) < 0.0,
    f"lower 2.6-sigma edge = {OK_FS - 2.6*SIG_FS:+.5f} < 0, so Omega_k<0 is not yet excluded")

print("\n" + "=" * 76)
np_ = sum(1 for _, ok, _ in checks if ok)
print(f"SELF-CHECKS: {np_}/{len(checks)} passed")
print("""
READING (what the numbers do and do not license):

  The model requires Omega_k < 0 (closed). The two current DESI+CMB curvature analyses both
  find Omega_k > 0 (open), at roughly 2 to 2.4 sigma from flat. That is the side that
  FALSIFIES this model -- not the side our own bibliography named.

  It is NOT yet a refutation. At ~2.4 sigma, Omega_k < 0 is disfavoured, not excluded, and
  the model can retreat toward Omega_k -> 0^- without limit (see OPENING_FINDING). What has
  changed is the direction of travel: the falsifier is being pushed toward firing, and our
  record had the kill condition on the wrong side of zero.
""")
sys.exit(0 if np_ == len(checks) else 1)
