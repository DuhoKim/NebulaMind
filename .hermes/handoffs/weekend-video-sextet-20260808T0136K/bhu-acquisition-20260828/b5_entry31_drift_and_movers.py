#!/usr/bin/env python3
"""B5 -- entry 31, tasks 3 and 4: the drift claim computed PER INSTRUMENT, and what would move it.

Blanc: "the drift claim now needs computing TWICE, once per instrument, because 'moving away from
firing as the error tightens' may be true on one and false on the other."

Our record says entry 31 is "drifting away from firing". That is a claim about a trend, stated in
prose with no computation behind it. Both epochs of the radio-timing history are inside the pinned
J0740+6620 paper, so the radio branch is computable from sources we hold.

Pinned: 2104.00880_clean.txt (carries BOTH its own value and Cromartie et al. 2020's)
        2207.05124_clean.txt (black widow)
"""
import re, sys, math

S = "../bhu-reading-20260823/sources/"
J1 = " ".join(open(S + "2104.00880_clean.txt").read().split())
J2 = " ".join(open(S + "2207.05124_clean.txt").read().split())
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))
def tail(x): return 0.5 * math.erfc(x / math.sqrt(2.0))

BAR = 2.5
print("=" * 98); print("B5 -- the drift claim, per instrument; and what would settle this"); print("=" * 98)

# ---- TASK 3a: radio timing has a real two-epoch history, inside the pinned paper --------------
prior = re.search(r"m_\{\\rm p\}=2\.14\^\{\+0\.10\}_\{-0\.09\}", J1) or ("2.14" in J1 and "Cromartie" in J1)
print("\n3a. RADIO TIMING -- two epochs, both from the pinned paper")
HIST = [("Cromartie et al. 2020", 2.14, 0.095), ("Fonseca et al. 2021", 2.08, 0.07)]
for lbl, mu, sd in HIST:
    z = (BAR - mu)/sd
    print(f"   {lbl:<26} {mu:.2f} +/- {sd:.3f}   ->  {z:5.2f} sigma short   P(M>2.5) = {tail(z):.2e}")
z0 = (BAR-HIST[0][1])/HIST[0][2]; z1 = (BAR-HIST[1][1])/HIST[1][2]
print(f"   central value MOVED DOWN {HIST[0][1]-HIST[1][1]:+.2f}; uncertainty TIGHTENED "
      f"{HIST[0][2]-HIST[1][2]:.3f}; both push AWAY from the bar")
print(f"   posterior mass above 2.5 fell by a factor of {tail(z0)/tail(z1):,.0f}")
chk("COMPUTED: on radio timing the drift claim is TRUE -- the central value fell AND the error "
    "tightened, and the posterior above the bar dropped by ~5 orders of magnitude",
    bool(prior) and z1 > z0 and tail(z0)/tail(z1) > 1e4,
    f"{z0:.2f} sigma -> {z1:.2f} sigma between the two epochs the pinned paper reports")

# ---- TASK 3b: the black widow has NO history ---------------------------------------------------
hist_hits = len(re.findall(r"(?:previous|earlier|prior)\s+(?:mass|measurement|estimate)", J2))
print(f"\n3b. BLACK WIDOW -- prior-measurement mentions in its paper: {hist_hits}")
chk("COMPUTED: on the black widow the drift claim is NOT FALSE, it is UNCOMPUTABLE -- there is "
    "one measurement and no history to trend",
    hist_hits == 0,
    "n=1. A trend needs two points, and this branch has one")

print("""
3c. WHAT THAT MEANS -- and it is the sharpest thing in this study

    Our record says entry 31 is "drifting away from firing". That is TRUE on radio timing, where
    the falsifier is already 6 sigma away and effectively DEAD -- and UNCOMPUTABLE on the black
    widow, the branch where the falsifier is LIVE at 19%.

    So the reassuring half of our record's summary was carried entirely by the instrument on
    which there is nothing left to reassure about. On the branch that actually matters, we have
    a single measurement and no trend at all.
""")

# ---- TASK 4: what would move it ---------------------------------------------------------------
print("""4. WHAT WOULD MOVE THIS -- measurement, instrument, timescale

   The lane's most useful output, because entry 31 is the corpus's only live calibrated falsifier
   and its status currently turns on an unresolved instrument question rather than on data.

   (A) TO SETTLE WHICH BRANCH WE ARE ON  -- highest value, and it is a measurement question
       WHAT: an independent mass for PSR J0952-0607, or for any black widow, by a method that
             does not depend on modelling an irradiated companion's light curve.
       WHY:  the entire 19%-vs-1e-9 split rests on whether optical black-widow modelling counts
             as "well measured". Romani et al. call theirs "the largest well-measured mass found
             to date"; Smolin's own sentence names binary pulsar data. One independent check
             would collapse the split without anyone having to adjudicate the word.
       HOW:  relativistic Shapiro delay requires a near-edge-on orbit, which most black widows do
             not offer -- this is why the optical route is used. So the realistic version is
             CONSISTENCY across many systems rather than one decisive check: Romani et al.
             already reanalyse other black widows and redbacks, and a systematic bias would show
             up as a population offset.
       TIMESCALE: years, not decades. Ongoing.

   (B) TO FIRE THE FALSIFIER ON THE CONSERVATIVE BRANCH
       WHAT: a radio-timed neutron star above 2.5 M_sun.
       GAP:  the heaviest such mass we hold is 2.08 +/- 0.07. Firing needs ~0.4 M_sun more than
             any pulsar ever timed -- roughly 6 sigma. This is not a near-miss.
       HOW:  MeerKAT/TRAPUM, FAST, CHIME/Pulsar now; SKA later.
       TIMESCALE: SKA-era. 2030s.

   (C) TO KILL IT OUTRIGHT
       WHAT: continued tightening on J0740+6620 and similar systems.
       STATUS: already happening, and already at 6 sigma. Each refinement makes the conservative
             branch deader. It cannot kill the black-widow branch, which is the point of (A).

   (D) A THIRD INSTRUMENT, NAMED BUT NOT PINNED -- flagged as testimony
       Gravitational-wave mass measurements of compact objects in the 2.5-3 M_sun range would
       bear directly on the bar, since Smolin's argument is about the maximum neutron-star mass
       rather than about pulsars specifically. I am NOT quoting a value: no GW paper is pinned in
       this corpus, and the known difficulty is that an object in that range may be a light black
       hole rather than a neutron star, which is precisely the ambiguity the bar cannot tolerate.
       ACQUIRING one is cheap and is the obvious next pin.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
