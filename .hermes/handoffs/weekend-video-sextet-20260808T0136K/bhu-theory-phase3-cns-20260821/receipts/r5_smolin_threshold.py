#!/usr/bin/env python3
"""R5 — the heaviest measured neutron stars against SMOLIN's own stated threshold.

Smolin, astro-ph/9712189 (preprint; context-only under the published-base-layer rule),
abstract and Sec 5, verbatim: "the observation of a pulsar with mass greater than
2.5 Msun would cleanly refute the theory."  Sec 2 adds the weaker form: "if one is
completely confident of Bethe and Brown's upper limit of 1.5, any value higher than
this would be troubling."

Masses as ledgered in the 2026-08-17 C08 adjudication (measurement classes preserved).
"""
SMOLIN_CLEAN = 2.5
BLR_SAFE     = 2.0

STARS = [  # name, mass, 1-sigma, class
    ("PSR J0740+6620", 2.08, 0.07, "timing (qualifying)"),
    ("PSR J1614-2230", 1.928, 0.017, "timing (qualifying)"),
    ("PSR J1913+1102 A", 1.599, 0.008, "timing (qualifying)"),
    ("PSR J0952-0607", 2.35, 0.17, "light-curve (EXCLUDED class)"),
]
print(f"{'star':20} {'mass':>14} {'vs 2.5 (Smolin)':>18} {'vs 2.0 (BLR)':>15}  class")
for n, m, s, c in STARS:
    d25 = (m - SMOLIN_CLEAN) / s
    d20 = (m - BLR_SAFE) / s
    print(f"{n:20} {m:6.3f}+/-{s:5.3f} {d25:+17.1f}s {d20:+14.1f}s  {c}")
print()
print(f"Nothing reaches Smolin's 2.5 Msun. The heaviest QUALIFYING star is 2.08 +/- 0.07,")
print(f"which is {(2.5-2.08)/0.07:.1f} sigma BELOW his stated clean-refutation threshold.")
print("Even the excluded-class J0952-0607 at 2.35 +/- 0.17 sits below it.")
