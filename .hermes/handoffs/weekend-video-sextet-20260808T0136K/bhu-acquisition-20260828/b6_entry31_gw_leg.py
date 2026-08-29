#!/usr/bin/env python3
"""B6 -- entry 31, option (D): the gravitational-wave leg, pinned.

I named this in b5 as "cheap and the obvious next pin" and quoted no value because nothing was
pinned. Blanc: do it, pin what the paper claims about the NATURE of the object rather than just
the mass, and treat the classification contest AS the finding rather than something to resolve.

Three sources pinned today:
  2006.12611  GW190814 discovery (LIGO/Virgo)
  2007.10999  On the maximum mass of neutron stars and GW190814
  2101.01735  GW170817 and GW190814: tension on the maximum mass

WHY THIS BEARS ON ENTRY 31 AT ALL. Smolin's argument is about the MAXIMUM NEUTRON STAR MASS, not
about pulsars specifically. Any instrument that measures that maximum is on-bar. Gravitational
waves supply two such instruments, and they do not agree with each other or with radio timing.
"""
import re, sys, math

S = "../bhu-reading-20260823/sources/"
GW  = " ".join(open(S + "2006.12611_clean.txt").read().split())
TEN = " ".join(open(S + "2101.01735_clean.txt").read().split())
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

BAR = 2.5
print("=" * 98); print("B6 -- the gravitational-wave leg: an object AT the bar whose nature is contested"); print("=" * 98)

# ---- 1. the object, and what the discovery paper says it IS ----------------------------------
mass_rng = "2.50 – 2.67" in GW or "2.50-2.67" in GW.replace(" ", "")
either_or = "either the lightest black hole or the heaviest neutron star" in GW
print("\n1. THE OBJECT, AND ITS CONTESTED NATURE -- both from the discovery paper")
print("   secondary mass: 2.50 - 2.67 Msun (90% credible)")
print('   nature:  "either the lightest black hole or the heaviest neutron star ever discovered')
print('            in a double compact-object system"')
chk("QUOTED: the discovery paper's ENTIRE 90% credible interval for the secondary lies AT OR "
    "ABOVE Smolin's 2.5 Msun bar",
    mass_rng,
    "2.50-2.67. Not near the bar -- the whole interval is on or past it")
chk("QUOTED: and the discovery paper DECLINES to classify the object, which is exactly the "
    "ambiguity the bar cannot tolerate",
    either_or,
    "Blanc's caution was to pin what the paper claims about the NATURE, not just the mass. It "
    "claims 'either ... or'. That refusal is the finding, not an obstacle to one")

# ---- 2. the conditional that decides it ------------------------------------------------------
cond = "requiring" in TEN and "if the secondary was a" in TEN
print("\n2. THE CONDITIONAL, from the tension paper")
print("   'GW170817 suggesting that M_TOV <~ 2.3 Msun, and GW190814 requiring M_TOV >~ 2.5 Msun")
print("    IF THE SECONDARY WAS A (non- or slowly rotating) NEUTRON STAR at merger'")
chk("QUOTED: the literature states the conditional explicitly -- GW190814 forces M_TOV above "
    "Smolin's bar IF and ONLY IF the secondary was a neutron star",
    cond,
    "so Smolin's falsifier fires on this instrument exactly when the classification goes one way")

# ---- 3. and the same paper's own preferred value points the other way -------------------------
tov = re.search(r"M_\{\{\}_\{\\rm TOV\}\}=2\.210\^\{\+0\.116\}_\{-0\.123\}", TEN) or ("2.210" in TEN and "0.116" in TEN)
LO, HI = 2.210 - 0.123, 2.210 + 0.116
print(f"\n3. THE TENSION PAPER'S OWN M_TOV, from GW170817")
print(f"   M_TOV = 2.210 +0.116 -0.123 Msun, quoted by the authors as a 2-sigma range")
print(f"   => 2-sigma interval [{LO:.3f}, {HI:.3f}]   Smolin's bar 2.5 lies {'INSIDE' if LO<=BAR<=HI else 'OUTSIDE (above)'}")
chk("COMPUTED: Smolin's 2.5 Msun bar lies ABOVE the tension paper's own 2-sigma interval for the "
    "maximum neutron-star mass",
    tov and BAR > HI,
    f"2.5 vs an upper 2-sigma edge of {HI:.3f} -- on THIS instrument the bar is excluded, which "
    f"is the same direction radio timing points and the opposite of what GW190814 would imply")

print("""
4. FOUR INSTRUMENTS, THREE ANSWERS -- and they are not independent

   +---------------------------------------+--------------------------+------------------------+
   | instrument                            | value                    | Smolin's 2.5 bar       |
   +---------------------------------------+--------------------------+------------------------+
   | radio timing, J0740+6620              | 2.08 +/- 0.07            | 6.0 sigma away: DEAD   |
   | M_TOV from GW170817 (tension paper)   | 2.210 +0.116 -0.123 (2s) | ABOVE the interval:    |
   |                                       |                          | EXCLUDED               |
   | black widow optical, J0952-0607       | 2.35 +/- 0.17            | 0.88 sigma: LIVE, 19%  |
   | GW190814 secondary, IF a neutron star | 2.50 - 2.67 (90%)        | entire interval AT OR  |
   |                                       |                          | ABOVE: FIRES           |
   +---------------------------------------+--------------------------+------------------------+

   The two GW-derived routes point in OPPOSITE directions, and the tension paper says so in its
   own title. Its preferred M_TOV excludes the bar; the event it is named after would force the
   bar to be exceeded, but only under a classification the discovery paper refuses to make.

5. WHAT THIS DOES TO THE ENTRY-31 FINDING

   b5 reported a two-branch instrument split. That was already the right shape and it is now
   WORSE than reported: the split is four-way, and one branch does not merely leave the falsifier
   live -- it FIRES it, on a 90% interval lying entirely at or above the bar.

   Nothing here resolves anything, and it is not supposed to. What it establishes is that entry
   31's status is even less a fact about the universe than b5 said. Whether the corpus's only
   live falsifier has already fired turns on whether one object 241 Mpc away was a neutron star
   or a black hole -- a question its discoverers explicitly declined to answer.

6. WHAT I AM NOT DOING

   Not resolving the classification. The discovery paper declines it, the tension paper treats it
   as an open conditional, and Blanc's instruction was to treat the contest as the finding.
   Not adopting M_TOV = 2.21 as OUR value either -- it is one analysis of one event, and the
   corpus now holds three GW papers that disagree about what the same data imply.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
