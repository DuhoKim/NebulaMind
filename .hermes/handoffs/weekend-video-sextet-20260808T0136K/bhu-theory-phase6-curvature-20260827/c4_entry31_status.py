#!/usr/bin/env python3
"""C4: how close is the family's one live calibrated falsifier to firing?

Entry 31 = Smolin 2004, Physica A 340 705-713. Section 4 sets TWO limbs:
  - "troubling" limb: Brown-Bethe M_max ~ 1.5 M_sun, valid only "if one is completely
    confident of Bethe and Brown's upper limit" -- our C08/Track C adjudicated that
    instrument BROKEN at >= 8 sigma, so this limb is dead as a calibration.
  - CLEAN limb, Smolin's own: "sufficiently high is certainly 2.5 M_sun".

Only the 2.5 limb still calibrates. This file computes how close it is.

Context: entry 7 (Brown/Lee/Rho 2008) is a calibrated falsifier that already FIRED at its
own >~ 2 M_sun threshold. Entry 54 was demoted 2026-08-28. So entry 31 is the family's
ONLY live calibrated falsifier -- a claim the requester got wrong in the opposite direction
earlier today and is now stating from the record.
"""
import math, sys

checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

def phi(z):
    """standard normal CDF via erf -- no scipy needed."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))

TROUBLING = 1.5      # Brown-Bethe instrument limb (broken)
CLEAN     = 2.5      # Smolin's own clean-refutation bar

# (label, mass, sigma, source)
MASSES = [
    ("PSR J1614-2230", 1.97, 0.04, "Demorest+ 2010, Nature 467 1081"),
    ("PSR J0740+6620", 2.08, 0.07, "Fonseca+ 2021, ApJL 915 L12"),
    ("PSR J0952-0607", 2.35, 0.17, "Romani+ 2022, arXiv 2207.05124"),
    ("PSR J0952-0607 (tightened)", 2.35, 0.11, "arXiv 2512.05099"),
]

print("=" * 96)
print("C4 -- entry 31 (Smolin 2004 CNS): distance from the author's own clean-refutation bar")
print("=" * 96)
print(f"  troubling limb (Brown-Bethe instrument, BROKEN >=8 sigma per C08): {TROUBLING} M_sun")
print(f"  clean limb (Smolin's own words, 'certainly'):                      {CLEAN} M_sun\n")
print(f"  {'pulsar':30s} {'mass':>14s} {'>1.5?':>7s} {'sigma to 2.5':>13s} {'P(M>2.5)':>10s}")
rows = []
for label, m, s, src in MASSES:
    z = (CLEAN - m) / s
    p_above = 1.0 - phi(z)
    rows.append((label, m, s, z, p_above))
    print(f"  {label:30s} {m:>7.2f} +-{s:<4.2f} {'yes' if m > TROUBLING else 'no':>7s} "
          f"{z:13.2f} {100*p_above:9.1f}%")
    print(f"  {'':30s}   {src}")

best = rows[-1]
chk("every measured mass exceeds the broken 1.5 limb -- that limb is long gone",
    all(m > TROUBLING for _, m, _, _, _ in rows),
    f"lightest listed is {min(m for _, m, _, _, _ in rows):.2f} M_sun")
chk("but NO measurement reaches Smolin's clean 2.5 bar",
    all(m < CLEAN for _, m, _, _, _ in rows),
    f"heaviest is {max(m for _, m, _, _, _ in rows):.2f} M_sun, below {CLEAN}")
chk("the falsifier is LIVE but close -- under 2 sigma from firing",
    1.0 < best[3] < 2.0, f"{best[3]:.2f} sigma short on the tightened measurement")
chk("and the posterior mass above the bar is already non-negligible",
    0.05 < best[4] < 0.20, f"P(M > 2.5) = {100*best[4]:.1f}% on a Gaussian posterior")
# CORRECTED 2026-08-28: I first asserted the opposite -- that tightening moved it CLOSER to
# firing -- and this check FAILED me. It was right. The central value held at 2.35 while the
# error shrank, so the fixed 2.5 bar is now MORE sigma away, not fewer. The measurement got
# more precise about NOT having reached the bar.
chk("tightening the error bar moved it FURTHER from firing in sigma terms",
    rows[-1][3] > rows[-2][3],
    f"sigma-to-bar went {rows[-2][3]:.2f} -> {rows[-1][3]:.2f} as the error shrank 0.17 -> 0.11; "
    f"posterior above the bar fell {100*rows[-2][4]:.1f}% -> {100*rows[-1][4]:.1f}%")

# what measurement would fire it?
print(f"\n  What would fire it: a well-measured neutron star at or above {CLEAN} M_sun.")
for sig in (0.10, 0.07, 0.05):
    need = CLEAN + 3.0*sig
    print(f"     at +-{sig:.2f} precision, a 3-sigma clean firing needs M >= {need:.2f} M_sun")

print("""
READING -- THE GATE SPLIT, AND WHAT THE PRIMARY TEXT SAYS

  Two seats, two answers, on ONE question: does the falsifier survive its broken instrument?
    CGATE_ENTRY31_VERDICT.md (codex)  LIVE_CALIBRATED       -- yes, narrowly
    AGATE_ENTRY31_VERDICT.md (agy)    DEMOTE_BROKEN_INSTRUMENT -- no, it is an unanchored number
  They AGREE on everything else: the 2.5 bar is unreached, footnote 6 does not demote, and CNS
  genuinely belongs in the family.

  Smolin section 4 appears to settle it, verbatim, and against the demote reading:

    "Bethe, Brown and collaborators claim that calculations show that mu < mu_c. BUT THEIR
     CALCULATIONS INVOLVE APPROXIMATIONS SUCH AS CHIRAL DYNAMICS AND MAY BE SUFFICIENTLY
     INACCURATE that in fact mu_c > mu. HOWEVER, WE CAN BE REASONABLY SURE OF THE EXISTENCE OF
     SUCH A CRITICAL VALUE mu_c. Then we may reason as follows... Therefore a single
     observation of a neutron star whose mass M was sufficiently high would show that
     mu > mu_c... Sufficiently high is certainly 2.5 M_sun"

  Smolin anticipates the instrument being wrong and builds the argument to survive it. The
  falsifier depends on the EXISTENCE of a critical mu_c, not on Bethe-Brown's VALUE for it.
  Breaking the 1.5 number therefore does not sever the link agy says it severs -- Smolin
  severed that dependence himself, in the same paragraph, before stating the 2.5 bar.

  I am the interested party here and will not call my own tie. Recorded for a third seat.

  TALLY, stated conditionally because it turns on the split:
    if LIVE_CALIBRATED stands -> the family has ONE live calibrated falsifier (entry 31)
    if DEMOTE stands          -> the family has ZERO
  Entry 7 fired; entry 54 demoted 2026-08-28. No other entry is calibrated.

  And my own error, kept in the artifact: I told Duho the tally was ZERO before any of this,
  by assuming entry 31 was the same bound that fired entry 7 -- without reading our own
  bibliography entry, which already recorded the separate 2.5 bar as unreached. If the ZERO
  reading now wins on agy's reasoning, it wins for a reason I did not have and had not thought of.
""")
np_ = sum(1 for _, ok, _ in checks if ok)
print(f"SELF-CHECKS: {np_}/{len(checks)} passed")
sys.exit(0 if np_ == len(checks) else 1)
