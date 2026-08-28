#!/usr/bin/env python3
"""A14 -- audit the three RANDOMLY DRAWN entries. Selection-bias control for the sweep's null.

Draw recorded in _random_draw.json, seeded from the git HEAD sha at draw time
(e515f24656..., fixed by history before the draw), so the entries could not be chosen after
seeing them. Pool: 20 pinned + unaudited. Drawn: 24, 36, 40.

Naming follows the a11 rule: a presence test is named as a presence test; an absence or a count
carries a caveat naming what it would miss.

Sources under ../bhu-reading-20260823/sources/.
"""
import re, sys, json

SRC = "../bhu-reading-20260823/sources/"
DOC = {24: "2104.00521_clean.txt", 36: "smoller_temple_2000_clean.txt", 40: "2008.02136_clean.txt"}
TXT = {e: " ".join(open(SRC + f).read().split()) for e, f in DOC.items()}
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

print("=" * 96); print("A14 -- the three randomly drawn entries"); print("=" * 96)
d = json.load(open("_random_draw.json"))
print(f"\nseed {d['seed_hex'][:16]}...  pool {len(d['pool'])}  drawn {d['drawn']}")

# ---- COUNTED: numeric content across the three ---------------------------------------------
SCI = r"\d+(?:\.\d+)?\s*×\s*10\s*[−-]?\s*\d+|\d(?:\.\d+)?\s*\\times\s*10\^?\{?-?\d"
counts = {e: len(re.findall(SCI, T)) for e, T in TXT.items()}
print(f"\n1. COUNTED: scientific-notation values per entry   {counts}")
chk("COUNTED: only entry 36 carries substantial numeric content; 24 and 40 carry none",
    counts[24] == 0 and counts[40] == 0 and counts[36] > 15,
    "so 36 is the only one of the three that could hide a calibrated threshold")

# ---- entry 24 --------------------------------------------------------------------------------
agrees = "agrees with the black hole universe predictions" in TXT[24]
print(f"\n2. ENTRY 24 -- 'A Peek Outside Our Universe' (tier: QUALITATIVE-DIRECTIONAL)")
print(f"   QUOTED: CMB fossil-record analysis 'agrees with the black hole universe")
print(f"   predictions but challenges our understanding...'          present: {agrees}")
chk("QUOTED: entry 24's CMB claim is stated as AGREEMENT, not as a threshold that could fail",
    agrees and counts[24] == 0,
    "'agrees with' + zero numeric values = consistency language; tier CONFIRMED")

# ---- entry 36 -- the only real candidate in the draw ----------------------------------------
bounds = "upper and lower bounds on the shock position at the present time" in TXT[36]
freeparam = "the value of the scale factor R" in TXT[36] and "at which we start the shock" in TXT[36]
hubble = "comparable to the Hubble distance" in TXT[36]
print(f"\n3. ENTRY 36 -- Smoller-Temple 2000, 'Cosmology with a Shock-Wave' (tier: CONSISTENCY-ONLY)")
print(f"   QUOTED: derives 'upper and lower bounds on the shock position' .. {bounds}")
print(f"   QUOTED: the shock distance is 'comparable to the Hubble distance' {hubble}")
print(f"   QUOTED: the upper bound depends on R*, the free scale factor")
print(f"           'at which we start the shock-wave'                       {freeparam}")
chk("QUOTED: entry 36 derives numeric BOUNDS, but places the shock at or beyond the Hubble "
    "distance and leaves the upper bound dependent on a free starting parameter R*",
    bounds and hubble and freeparam,
    "36 h0/H0 <= r <= (36 h0/H0) sqrt(1 + 2.5 R*) at T0=2.7K -- a derived number describing "
    "something at or past the horizon, with a free parameter in the range. Tier CONFIRMED.")

# ---- entry 40 --------------------------------------------------------------------------------
unobs = "could not be observed outside the black hole because of the infinite redshift at the horizon" in TXT[40]
print(f"\n4. ENTRY 40 -- 'Gravitational collapse of a fluid with torsion' (tier: CONSISTENCY-ONLY)")
print(f"   QUOTED: 'its formation and subsequent dynamics could not be observed")
print(f"   outside the black hole because of the infinite redshift'   present: {unobs}")
chk("QUOTED: entry 40 explicitly states its object cannot be observed from outside",
    unobs and counts[40] == 0,
    "like entry 8, this is CONSISTENCY-ONLY in the strong sense -- it asserts unobservability "
    "rather than merely omitting a test")

print("""
5. RESULT OF THE CONTROL

   THREE DRAWN AT RANDOM, THREE TIERS UNCHANGED. The pattern did not break.

   Running total: 12 hand-picked + 3 random = 15 entries examined, 15 tiers unchanged, across
   three author lines (Gaztanaga, Poplawski, Smoller-Temple) and three frameworks.

   The draw did what it was for. My selection rule braided (A) "highest prior of concealing a
   testable claim" with (B) availability and ease of checking, and I could not separate them by
   introspection. A random draw returning the same answer means the null is not an artefact of
   (B). It is a property of the pinned corpus.

   ENTRY 36 IS THE INSTRUCTIVE ONE. It is the only draw with real numeric content -- 21
   scientific-notation values, and genuine derived bounds calibrated to the measured H0 and T0.
   On a shallow read it looks exactly like a concealed calibrated falsifier. It is not, for two
   independent reasons: the predicted object sits at or beyond the Hubble distance, and the
   upper bound carries a free parameter. That is the same shape found in the hand-picked set --
   a real number that cannot fail -- reached this time without my choosing the paper.

6. WHAT THIS CONTROL DOES NOT ESTABLISH

   The pool is not random. All 20 candidates were PINNED, and pinning followed the bibliography's
   ranked list. The 19 unpinned entries -- disproportionately paywalled and low audit-worthiness
   -- had no chance of being drawn. And n = 3 cannot prove a pattern; it can only fail to break
   one, which is what it did.

7. A DEFECT IN MY OWN SCREEN, caught before it mattered

   The screening pass counted 16 "sigma" matches in entry 36 and I nearly read them as statistical
   significances. They are the equation-of-state parameter sigma in p = sigma*rho. The regex was
   named for one thing and matched another -- the same name/predicate defect, in a script written
   within an hour of my adopting a rule against it. Recorded because it shows the rule needs to be
   applied at write time, not audited in afterwards.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
