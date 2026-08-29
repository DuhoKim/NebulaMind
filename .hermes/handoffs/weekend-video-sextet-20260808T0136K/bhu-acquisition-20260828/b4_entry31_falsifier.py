#!/usr/bin/env python3
"""B4 -- entry 31 (Smolin 2004, Physica A 340, 705-713): the corpus's one live calibrated falsifier.

Duho redirected the lane here: 15 entries audited, 0 tiers moved, and only 3 of 51 papers are
calibrated falsifiers at all -- entry 7 has fired, entry 51 is explicitly not a direct BHU
falsifier, leaving exactly one live route. This is the worked example for the falsifier rule
adopted this morning, and the only entry where BOTH halves apply without me supplying anything:
Smolin states his own bar.

Pinned sources, all three:
  ../bhu-reading-20260823/sources/smolin_2004_cns_clean.txt   entry 31, the claim
  ../bhu-reading-20260823/sources/2104.00880_clean.txt        J0740+6620, radio timing + NICER
  ../bhu-reading-20260823/sources/2207.05124_clean.txt        J0952-0607, black widow, optical
The two measurement papers were acquired today; before that the measurement side of this
falsifier was entirely unpinned testimony.
"""
import re, sys, math

S = "../bhu-reading-20260823/sources/"
SM = " ".join(open(S + "smolin_2004_cns_clean.txt").read().split())
J1 = " ".join(open(S + "2104.00880_clean.txt").read().split())
J2 = " ".join(open(S + "2207.05124_clean.txt").read().split())
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

def erfc_tail(x):  # P(N(0,1) > x)
    return 0.5 * math.erfc(x / math.sqrt(2.0))

print("=" * 98); print("B4 -- entry 31: the bar from the source, the measurement from the source"); print("=" * 98)

# ---- 1. THE BAR, from Smolin's own words, WITH the qualifier our record omitted ---------------
# NOTE: a naive [^.]*\. sentence-splitter TRUNCATES here, because the sentence contains "1.5"
# and the splitter stops at that decimal point. The first run of this check FAILED for that
# reason and not because the qualifier was absent -- a parsing artefact masquerading as a finding.
# Captured by explicit length instead.
bar = re.search(r"SuMciently high is certainly 2:5M◦.{0,190}", SM)
premise = "Presently all well measured neutron star masses are from binary pulsar data and are all below 1:5M◦" in SM
print("\n1. THE BAR, QUOTED")
print("   " + (" ".join(bar.group(0).split()) if bar else "<< NOT FOUND >>"))
chk("QUOTED: Smolin states 2.5 Msun as 'certainly' sufficient to refute -- our record's bar is "
    "correct", bar is not None,
    "verified from the pinned Physica A text, not from our own note")
chk("QUOTED: and it is a GRADED bar our record never carried -- 'if one is completely confident "
    "of Bethe and Brown's upper limit of 1.5 solar masses, any value higher than THIS would be "
    "troubling'",
    bar is not None and "1.5 solar masses" in bar.group(0) and "troubling" in bar.group(0),
    "so there are TWO bars: 2.5 = certainly refuting, and 1.5 = 'troubling', conditional on "
    "accepting Bethe-Brown. Our record tracked only the higher one")

print("\n2. SMOLIN'S OWN STANDARD OF EVIDENCE, and his 2004 factual premise")
print("   \"Presently all well measured neutron star masses are from BINARY PULSAR DATA and are")
print("    all below 1.5 Msun.\"")
chk("QUOTED: Smolin names BINARY PULSAR DATA as what counts as well-measured, and states that in "
    "2004 all such masses were below 1.5 Msun",
    premise,
    "the first clause is a criterion we can apply; the second is a factual premise that has since "
    "been overturned by measurements of exactly the type he named")

# ---- 2. THE MEASUREMENTS, from the pinned papers ---------------------------------------------
m1 = re.search(r"m_\{\\rm p\}=2\.08\^\{\+0\.07\}_\{-0\.07\}", J1) or ("2.08" in J1 and "0.07" in J1)
m2 = re.search(r"M_\{\\rm NS\}=2\.35\\pm 0\.17", J2) or ("2.35" in J2 and "0.17" in J2)
print(f"\n3. THE MEASUREMENTS, PARSED FROM THE PINNED PAPERS")
print(f"   J0740+6620  2.08 +/- 0.07 Msun, relativistic Shapiro delay, GBT + CHIME  : {bool(m1)}")
print(f"   J0952-0607  2.35 +/- 0.17 Msun, Keck optical light curve + RVs           : {bool(m2)}")
chk("PARSED: both masses read from their own pinned papers rather than from our record",
    bool(m1) and bool(m2),
    "our record carried 2.35 +/- 0.11 for the black widow; the source says +/- 0.17, and the "
    "0.11 has no pinned origin in this corpus")

# ---- 3. THE ARITHMETIC, both instrument choices -----------------------------------------------
BAR = 2.5
CASES = [("J0740+6620  radio timing (Smolin's named standard)", 2.08, 0.07),
         ("J0952-0607  black widow, optical  [source value]",   2.35, 0.17),
         ("J0952-0607  black widow  [our record's tighter bar]", 2.35, 0.11)]
print(f"\n4. HOW FAR FROM THE 2.5 Msun BAR? (Gaussian posterior, one-sided)")
print(f"   {'measurement':<52} {'sigma short':>12} {'P(M > 2.5)':>12}")
res = {}
for lbl, mu, sd in CASES:
    z = (BAR - mu) / sd; p = erfc_tail(z); res[lbl] = (z, p)
    print(f"   {lbl:<52} {z:>12.2f} {p:>11.2%}")
z_timing = res[CASES[0][0]][0]; z_bw = res[CASES[1][0]][0]
chk("COMPUTED: the instrument choice changes this from a live test to a dead one -- 0.9 sigma "
    "versus 6.0 sigma from the same bar",
    z_timing > 5.0 and z_bw < 1.0,
    f"radio timing puts the bar {z_timing:.1f} sigma away (P = {res[CASES[0][0]][1]:.1e}); the "
    f"black widow puts it {z_bw:.2f} sigma away (P = {res[CASES[1][0]][1]:.1%}). Same bar, same "
    f"corpus, opposite conclusions")
chk("COMPUTED: our record's error bar materially overstates how close this is -- +/-0.11 gives "
    "1.36 sigma and 8.6%, the source's +/-0.17 gives 0.88 sigma and 19%",
    abs(res[CASES[2][0]][0] - 1.36) < 0.02 and abs(res[CASES[1][0]][0] - 0.88) < 0.02,
    "the tighter bar makes the falsifier look FURTHER from firing than the published uncertainty "
    "warrants -- our record was conservative in the wrong direction")

print("""
5. THE INSTRUMENT DECISION -- named, owned, per the rule Duho adopted this morning

   CHOSEN: PSR J0740+6620, 2.08 +/- 0.07, radio timing via relativistic Shapiro delay.
   CHOSEN BY: Tori, 2026-08-29. THIS IS OURS.
   WHY: Smolin's own paper names the standard -- "all well measured neutron star masses are from
   BINARY PULSAR DATA". J0740+6620 is binary pulsar timing. J0952-0607's mass comes from optical
   light-curve and radial-velocity modelling of an irradiated companion, which is a different and
   more model-dependent instrument; Romani et al. call it "the largest well-measured mass found
   to date", so the label is contested, not settled.

   AGAINST THIS CHOICE, stated because it is the strongest counter: Smolin's sentence describes
   the state of measurement in 2004, and may be a report rather than a criterion. Reading it as
   a permanent standard is my inference.

   CONSEQUENCE OF THE CHOICE: on radio timing the bar is 6.0 sigma away and this falsifier is
   effectively dead. On the black widow it is 0.88 sigma away and live at ~19%.

6. WHAT OUR RECORD GOT WRONG, AND IT IS NOT THE HEADLINE NUMBER

   The 2.5 bar is right. What is missing is that SMOLIN'S FACTUAL PREMISE IS NOW FALSE. He wrote
   that all well-measured neutron star masses were below 1.5 Msun, and attached a second,
   conditional bar to that figure: above 1.5 would be "troubling" if one credits Bethe-Brown.

   Both pinned measurements -- 2.08 by his own named instrument, and 2.35 by another -- exceed
   1.5 by a wide margin. The LOWER bar was passed years ago, by exactly the kind of data he named.
   Our record tracked only the 2.5 bar and so recorded this entry as "1.36 sigma short and
   drifting away", when the paper's own conditional threshold had already been comprehensively
   exceeded.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
