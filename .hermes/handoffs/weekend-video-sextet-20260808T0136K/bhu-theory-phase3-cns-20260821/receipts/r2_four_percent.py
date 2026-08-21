#!/usr/bin/env python3
"""R2 — where the 4% comes from, and what the source's own proviso does to it.

Source: Brown, Lee & Rho, Phys. Rept. 462 (2008) 1 (arXiv:0708.3137), Sec. 3.2 —
the paper the PRL falsifier imports its double-NS limb from.
"""
import math

# --- 1. The 4% itself -------------------------------------------------------
# Sec 3.2: "Helium burning takes up 10% of the star lifetime ... To go from
# lifetimes to masses one must divide by about 2.5, so the two giant progenitors
# must be within 4% of each other in mass."
dtau_over_tau = 0.10
exponent      = 2.5           # tau ~ M/L, L ~ M^3.5  =>  tau ~ M^-2.5
dM_over_M     = dtau_over_tau / exponent
print(f"1. derived threshold      : {dM_over_M:.1%}   (paper: 4%)  -> {'CHECK' if abs(dM_over_M-0.04)<1e-9 else 'MISMATCH'}")

# --- 2. The proviso, which the same section QUANTIFIES ------------------------
# "During the helium burning red giant, ~0.1 to 0.2 Msun can be deposited on the
#  first born neutron star ... in addition to the possible ~4% difference"
m_lower = 1.290               # J1913+1102 B, Msun  (2026 A&A update)
m_upper = 1.599               # J1913+1102 A
sig     = math.hypot(0.008, 0.008)
dm_obs  = m_upper - m_lower

for deposit in (0.0, 0.1, 0.2):
    ceiling = 0.04 * m_lower + deposit
    excess  = dm_obs - ceiling
    print(f"2. deposit {deposit:.1f} Msun -> ceiling {ceiling:.3f} Msun | "
          f"observed {dm_obs:.3f} +/- {sig:.3f} | excess {excess:+.3f} = {excess/sig:5.1f} sigma")

# --- 3. What the adjudication reported ---------------------------------------
frac = dm_obs / m_lower
print(f"\n3. bare fractional asymmetry: {frac:.1%} vs a bare 4% threshold "
      f"-> ({frac-0.04:.3f}/{sig/m_lower:.4f}) = {(frac-0.04)/(sig/m_lower):.0f} sigma  "
      f"[the ~21 sigma figure in the 2026-08-17 adjudication]")
print("   Same data, same verdict direction. The margin is what changes, and only")
print("   IF J1913+1102 shares the He-red-giant channel the proviso is stated for.")
