#!/usr/bin/env python3
"""R4 — the accreted mass, settled against Tauris et al. 2017 (ApJ 846, 170).

BLR's Phys.Rept. 462 proviso claims 0.1-0.2 Msun is deposited on the first-born NS
during the He red giant phase. Tauris et al. 2017 -- the DNS-formation authority
Ferdman et al. 2020 cite -- budget it phase by phase, verbatim:

  common envelope  : "we take Delta M_NS = 0.01 Msun as a reasonable estimate for the
                      upper limit of the amount of mass accreted by a NS during a CE
                      phase"  (MacLeod & Ramirez-Ruiz's <0.1 Msun is argued to be an
                      overestimate, with observational support from four DNS systems)
  wind accretion   : "Delta M_NS < 4e-4 Msun when integrating throughout the
                      wind-accretion phase of the NS-helium star binaries"
  Case BB RLO      : "Delta M_NS = 5e-5 - 3e-3 Msun" for binaries leading to DNS
"""
import math

PHASES = {"common envelope (upper limit)": 0.01,
          "wind accretion":                4e-4,
          "Case BB RLO (max)":             3e-3}
total = sum(PHASES.values())
for k, v in PHASES.items():
    print(f"  {k:32} {v:.4f} Msun")
print(f"  {'TOTAL (all phases, each at max)':32} {total:.4f} Msun")
print(f"  BLR proviso claims               0.1000 - 0.2000 Msun"
      f"   -> overstated by {0.1/total:.0f}x to {0.2/total:.0f}x\n")

mA, sA, mB, sB = 1.599, 0.008, 1.290, 0.008     # 2026 A&A update
dm, sig = mA - mB, math.hypot(sA, sB)
for name, dep in (("BLR proviso 0.2", 0.2), ("BLR proviso 0.1", 0.1),
                  ("Tauris budget", total), ("no deposit", 0.0)):
    ceil = 0.04 * mB + dep
    print(f"  ceiling under {name:18} = {ceil:.3f} Msun | excess {dm-ceil:+.3f} = {(dm-ceil)/sig:5.1f} sigma")
