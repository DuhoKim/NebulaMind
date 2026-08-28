#!/usr/bin/env python3
"""C5: audit of entry 7's FALSIFIED adjudication -- the worked example the whole
CALIBRATED-FALSIFIER tier is defined by.

Target: Brown, Lee & Rho, "Kaon Condensation, Black Holes, and Cosmological Natural
Selection", PRL 101, 091101 (2008), with Publisher's Note PRL 101, 119901.
Pinned locally: reviews/_tori_bhu_reverify_sources_20260811/aps_vor_10.1103_PhysRevLett.101.091101_layout.txt
                brown-erratum.txt

Our record says: "already adjudicated in our record -- falsified via limb 2 (the 'simply
falsify' limb of the source's own disjunction)".

This file tests whether the source licenses that, and whether the resulting record is
internally consistent with today's entry 31 ruling.

DISCLOSURE: I am the interested party twice over. My entry 31 tiebreak leaned on entry 7 as
the fired contrast case, and the entry 54 demotion applied this morning used entry 7 as the
worked example of what CALIBRATED-FALSIFIER means. If entry 7 is misread, both inherit it.
"""
import sys

checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

# ---- the three statements, verbatim from the APS version of record -----------------
STATEMENTS = [
    ("ABSTRACT (l.16-19)", "disjunction",
     "a massive neutron star with mass M >~ 2Msun would put in SERIOUS DOUBT **OR** SIMPLY "
     "FALSIFY the following chain of predictions: (1) a nearly vanishing vector meson mass at "
     "chiral restoration, (2) kaon condensation at n ~ 3n0, (3) the Brown-Bethe maximum "
     "neutron-star mass Mmax ~ 1.5Msun, and (4) Smolin's 'cosmological natural selection'.",
     True),    # mentions CNS
    ("BODY (l.43-45)", "unambiguous falsification",
     "'Find a neutron star of mass >~ 2Msun, whether in binary or otherwise, then IT FALSIFIES "
     "the VM of HLS theory, which in turn FALSIFIES the kaon condensation at 3n0.'",
     False),   # does NOT mention CNS
    ("CLOSING (l.233-236)", "serious obstacle",
     "A firm observation of any type of a neutron star whose mass is greater than Mmax^BB, or "
     "to be safe >~2Msun, would PRESENT A SERIOUS OBSTACLE to the BB and CNS scenarios.",
     True),    # mentions CNS
]

print("=" * 100)
print("C5 -- what the source actually says, at three places, at three strengths")
print("=" * 100)
for where, strength, text, mentions_cns in STATEMENTS:
    print(f"\n  {where}  [{strength}]  CNS named: {'YES' if mentions_cns else 'NO'}")
    for i in range(0, len(text), 92):
        print(f"    {text[i:i+92]}")

strong = [s for s in STATEMENTS if s[1] == "unambiguous falsification"]
chk("the ONE unambiguous 'falsifies' statement does NOT name CNS -- it stops at kaon condensation",
    all(not s[3] for s in strong),
    "body chain is: heavy NS -> falsifies VM of HLS -> falsifies kaon condensation at 3n0")
chk("both places that DO name CNS use weaker language than 'falsifies'",
    all(s[1] != "unambiguous falsification" for s in STATEMENTS if s[3]),
    "abstract offers 'serious doubt OR simply falsify'; the closing says 'serious obstacle'")
chk("the authors' own CLOSING verdict on CNS is the weakest of the three",
    STATEMENTS[2][1] == "serious obstacle",
    "'would present a serious obstacle to the BB and CNS scenarios' -- their conclusion, own voice")

# ---- the internal contradiction this exposes ---------------------------------------
print("\n" + "=" * 100)
print("The contradiction between entry 7 as recorded and entry 31 as ruled today")
print("=" * 100)
HEAVIEST = 2.35            # PSR J0952-0607, +-0.11
OBSERVED_ABOVE_2 = [1.97, 2.08, 2.35]
E7_THRESHOLD = 2.0         # ">~ 2 Msun", per abstract + Publisher's Note on the relation sign
E31_THRESHOLD = 2.5        # Smolin's own "certainly" bar, upheld LIVE_CALIBRATED today

e7_fired_for_cns = any(m >= E7_THRESHOLD for m in OBSERVED_ABOVE_2)
e31_fired_for_cns = HEAVIEST >= E31_THRESHOLD
print(f"  entry 7  as recorded: CNS falsified at M >~ {E7_THRESHOLD} Msun  -> observed "
      f"{max(OBSERVED_ABOVE_2)} Msun -> CNS {'DEAD' if e7_fired_for_cns else 'live'}")
print(f"  entry 31 as ruled:    CNS refuted   at M >= {E31_THRESHOLD} Msun  -> observed "
      f"{HEAVIEST} Msun -> CNS {'DEAD' if e31_fired_for_cns else 'LIVE'}")
chk("the two records give OPPOSITE answers about the same theory on the same evidence",
    e7_fired_for_cns != e31_fired_for_cns,
    "entry 7 says CNS died years ago; entry 31 says CNS is live and 1.36 sigma short")
chk("and if entry 7's strong reading were right, today's entry 31 ruling would be MOOT",
    e7_fired_for_cns,
    "there would be no live falsifier to uphold -- CNS would already be dead")

print("""
RESOLUTION, and it is the same distinction the entry 31 tiebreak upheld this morning

  The strong falsification language in this paper attaches to the NUCLEAR-PHYSICS chain --
  vector manifestation of HLS, then kaon condensation at 3n0. That is the INSTRUMENT.
  The cosmological element, CNS, is never the object of the word "falsifies" anywhere in the
  paper. It gets "serious doubt" (abstract, limb 1) and "a serious obstacle" (closing).

  So: the >~2 Msun observations fired the INSTRUMENT limb, exactly as the body says without
  hedging. They did not fire CNS. CNS dies at Smolin's own 2.5 Msun bar, which is unreached.

  Under the WEAK reading, entry 7 and entry 31 are consistent.
  Under the STRONG reading as currently recorded, they contradict each other outright.
  Coherence of the record therefore favours the weak reading -- and so does the fact that the
  authors, writing in their own voice in their own conclusion, chose "serious obstacle".

  PROPOSED, not applied -- the bibliography is Blanc's:
    entry 7 record should read FIRED AS TO THE BROWN-BETHE INSTRUMENT CHAIN, with CNS left at
    "a serious obstacle" in the source's own words, NOT falsified.

GATE RESULT -- both seats UPHOLD_WEAK, and both corrected my emphasis
  AGATE_ENTRY7_VERDICT.md (agy, Gemini 3.1 Pro) and CGATE_ENTRY7_VERDICT.md (codex gpt-5.5),
  independently, fresh context. Neither found the instrument/theory split imported: agy calls it
  "authored by Brown, Lee, and Rho, not retroactively imported"; codex calls it "present in this
  paper's own text". Both declined to resolve the contradiction by overturning entry 31.

  CORRECTION TO MY OWN ARGUMENT. I leaned on the body's SILENCE about CNS as the load-bearing
  evidence. Codex found the pattern repeats in two places I had not read, and says so directly:
  the ruling "rests on the whole textual pattern, not silence alone".
    - lines 51-55: a neutron star appreciably exceeding the Brown-Bethe maximum "would COUNT
      AGAINST the CNS scenario" -- softer language again, which I missed.
    - lines 260-270: a different CCS/gravitational-wave route "would FALSIFY the BB scenario and
      PUT IN DOUBT the CNS theory" -- the same split, stated a third time.
  So the paper reserves unqualified "falsify" for the nuclear mechanism and weaker language for
  CNS at least FOUR times, not the two I found. My case was right and under-evidenced; the
  silence argument was doing work the explicit passages should have been doing.

TIER QUESTION (Duho's third)

  Entry 7 (fired) and entry 31 (unfired) currently carry the IDENTICAL label
  CALIBRATED-FALSIFIER. The tier encodes calibration but not status, while every tally
  statement we make turns on how many are LIVE. That is a defect in the scheme, not in either
  entry. A fired/unfired axis is needed, or the tally has to be stated separately every time --
  as I have had to do three times today.

  RESOLVED BY THE GATE, and better than I put it: do NOT strip calibration from entry 7. Codex:
  "It is not inherently wrong for Entry 7 and Entry 31 to share CALIBRATED-FALSIFIER if both are
  author-stated observational tests with numerical thresholds. It is a record-keeping defect if
  the tier is then used in tallies without a LIVE / FIRED / DEMOTED status field."
  Proposed representation, both seats concurring:
    entry 7  = CALIBRATED-FALSIFIER / FIRED as to the instrument chain / CNS seriously obstructed
    entry 31 = CALIBRATED-FALSIFIER / LIVE

THRESHOLD (Duho's second)

  Survives as printed: M >~ 2 Msun. Publisher's Note PRL 101, 119901 exists precisely to fix a
  relation-sign misprint: "a tagging error causing a relation sign misprint in the abstract.
  The second line of the abstract should read as '...mass M >~ 2Msun would...'". Our record's
  note on this is correct.
""")
np_ = sum(1 for _, ok, _ in checks if ok)
print(f"SELF-CHECKS: {np_}/{len(checks)} passed")
sys.exit(0 if np_ == len(checks) else 1)
