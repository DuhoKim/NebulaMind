#!/usr/bin/env python3
"""B10 -- what would move entry 31, recomputed under the METHOD-AGNOSTIC criterion.

The original "what would move it" was written under the instrument framing both seats refuted, and
now sits below the SUPERSEDED marker. Under the corrected criterion the question is not "which
instrument counts" but:

    IS ANY OBJECT ABOVE 2.5 M_sun SECURELY A NEUTRON STAR?

That changes what would move it, so this recomputes it. Arithmetic only where arithmetic applies;
the rest is named as judgement.
"""
import math, sys
def tail(z): return 0.5*math.erfc(z/math.sqrt(2.0))
BAR, MU, SD = 2.5, 2.35, 0.11
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*96); print("B10 -- what would move entry 31, under the corrected criterion"); print("="*96)

print(f"\n1. WHERE J0952 SITS NOW: {MU} +/- {SD}  ->  {(BAR-MU)/SD:.2f} sigma, P(M>2.5) = {tail((BAR-MU)/SD):.1%}")

print("\n2. WHAT PRECISION ALONE CAN DO -- holding the central value at 2.35")
print(f"   {'sigma':>8} {'z to bar':>10} {'P(M>2.5)':>10}")
for sd in (0.11, 0.08, 0.05, 0.03):
    z=(BAR-MU)/sd; print(f"   {sd:>8.2f} {z:>10.2f} {tail(z):>10.2%}")
sd_3sig = (BAR-MU)/3.0
chk("COMPUTED: tightening alone cannot fire this -- at a fixed central value of 2.35 more "
    "precision only drives the bar further away",
    tail((BAR-MU)/0.03) < tail((BAR-MU)/0.11),
    f"to put the bar at 3 sigma the uncertainty must fall to {sd_3sig:.3f}; every improvement in "
    f"precision at 2.35 makes firing LESS likely, not more")

print("\n3. WHAT WOULD ACTUALLY FIRE IT -- the central value has to move")
print(f"   {'central':>9} {'at sd=0.11':>12} {'at sd=0.05':>12}")
for mu in (2.35, 2.45, 2.55, 2.65):
    print(f"   {mu:>9.2f} {tail((BAR-mu)/0.11):>12.1%} {tail((BAR-mu)/0.05):>12.1%}")
chk("COMPUTED: firing requires a central value at or above the bar, not a smaller error bar",
    tail((BAR-2.55)/0.05) > 0.8,
    "at 2.55 +/- 0.05 the posterior above 2.5 is >80%; at 2.35 no attainable precision gets there")

print("""
4. SO WHAT WOULD MOVE IT -- under the method-agnostic criterion

   THE QUESTION IS NO LONGER "which instrument counts". It is: IS ANY OBJECT ABOVE 2.5 SECURELY
   A NEUTRON STAR? Three routes, ranked by what they could actually settle.

   (A) RESOLVE GW190814'S IDENTITY -- highest value, and possibly unresolvable for that event.
       Its secondary is the only known object whose mass estimate sits at the bar. If it is a
       neutron star, the bar is met on the paper's own terms. The discovery paper declines to say,
       and for a single event with no electromagnetic counterpart and no measurable tidal
       signature there may be no way to say. WHAT WOULD SETTLE IT: a comparable event WITH a tidal
       deformability measurement or an EM counterpart. Instrument: LIGO/Virgo/KAGRA at O5
       sensitivity. Timescale: this decade, and it depends on a rare event occurring.

   (B) A NEW OBJECT ABOVE 2.5 WITH SECURE IDENTIFICATION. On the arithmetic above, this is the
       ONLY route that fires the falsifier: the central value must move, not the error bar.
       Instruments: MeerKAT/TRAPUM, FAST, CHIME now; SKA in the 2030s for pulsars. Note the gap --
       the heaviest securely-identified neutron star we hold is 2.35, so this needs +0.15 or more
       with the identification intact.

   (C) POPULATION-LEVEL M_TOV CONSTRAINTS. Nathanail 2021 already gives 2.210 +0.116 -0.123 (2s),
       which puts the bar above its interval. Tightening that constrains the falsifier without
       finding any single object -- and it is the route most likely to move first, because it
       improves with every binary neutron-star merger rather than requiring a rare heavy one.

   AND THE 1.5 BAR IS ALREADY PASSED. Smolin's conditional threshold -- "any value higher than
   this would be troubling", crediting Bethe-Brown -- was exceeded years ago by every measurement
   here. Nothing needs to move for that. It is the 2.5 bar alone that remains unmet.

5. WHAT THIS SECTION DOES NOT DO

   The arithmetic covers only the J0952 posterior under a Gaussian approximation. It says nothing
   about whether 2.35 is CORRECT -- that is a question about optical heating models, not about
   sigma. And routes (A) and (C) depend on rates of astrophysical events, which nothing here
   estimates. Named because the first version of this study asserted timescales it had not
   computed.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
