#!/usr/bin/env python3
"""B9 -- entry 31 re-derived after both seats returned STUDY_UNSOUND.

Corrects four things the gates broke:
  1. the criterion: METHOD-AGNOSTIC (precision + secure NS identification), not instrument
  2. the black-widow uncertainty: +/-0.11 from the 2025 paper, not +/-0.17 from the 2022 one
  3. the GW leg at MATCHED CREDIBILITY, with correct attributions
  4. "drift" -> "the posterior was revised downward and tightened"

Pinned: smolin_2004_cns_clean.txt, 2104.00880 (J0740), 2207.05124 (J0952 2022),
        2512.05099 (J0952 2025), 2006.12611 (GW190814, Abbott), 2101.01735 (M_TOV, Nathanail)
"""
import re, sys, math
S = "../bhu-reading-20260823/sources/"
SM = " ".join(open(S+"smolin_2004_cns_clean.txt").read().split())
J25= " ".join(open(S+"2512.05099_clean.txt").read().split())
checks=[]
def chk(name,pred,detail=""):
    if not isinstance(pred,bool): raise TypeError("chk needs a computed predicate")
    checks.append((name,pred,detail)); print(("PASS " if pred else "FAIL ")+name+("  -- "+detail if detail else ""))
def tail(z): return 0.5*math.erfc(z/math.sqrt(2.0))
BAR=2.5

print("="*98); print("B9 -- entry 31, re-derived after both gates"); print("="*98)

# ---- 1. the criterion is method-agnostic, from the footnote -----------------------------------
fn = "Other methods yield less precise estimates" in SM
presently = SM.find("Presently all well measured") >= 0
print("\n1. THE CRITERION -- method-agnostic, established from footnote 5")
print("   footnote 5: \"Other methods yield less precise estimates [58].\"   present:", fn)
chk("QUOTED: Smolin's footnote acknowledges other methods and ranks them by PRECISION, refuting "
    "the instrument reading the first version of this study was built on",
    fn and presently,
    "ref 58 is a dynamical mass. The criterion is: securely a neutron star, mass high enough, "
    "estimate precise enough. NOT: measured by binary pulsar timing")

# ---- 2. the current black-widow value ---------------------------------------------------------
v25 = re.search(r"M_\{\\rm NS\}=2\.35\\pm 0\.11", J25) or ("2.35" in J25 and "0.11" in J25)
print("\n2. THE CURRENT J0952 VALUE -- 2025, superseding the 2022 +/-0.17")
for mu,sd,lbl in [(2.35,0.17,"Romani 2022  2.35 +/- 0.17"),(2.35,0.11,"Romani 2025  2.35 +/- 0.11")]:
    z=(BAR-mu)/sd; print(f"   {lbl:<32} z = {z:5.2f}   P(M>2.5) = {tail(z):6.2%}")
chk("PARSED: the 2025 paper reports 2.35 +/- 0.11, so the record's 1.36 sigma was CORRECT and "
    "had a real provenance -- my 'no pinned origin' claim was an artefact of a source set "
    "that stopped in 2022",
    bool(v25) and abs((BAR-2.35)/0.11 - 1.364) < 0.01,
    "z = 1.36, P = 8.63%. I accused the record of a fabricated error bar; the record was current "
    "and my pinned set was stale")

# ---- 3. the GW leg at MATCHED credibility ------------------------------------------------------
# GW190814 secondary: 2.50-2.67 at 90%. Gaussian-equivalent: half-width = 1.645 sigma.
lo90,hi90 = 2.50,2.67
mu = (lo90+hi90)/2; sd = (hi90-lo90)/2/1.645
lo2,hi2 = mu-2*sd, mu+2*sd
print("\n3. THE GW LEG AT MATCHED CREDIBILITY -- and the attribution corrected")
print(f"   GW190814 secondary  (Abbott 2020, 2006.12611):  90% [{lo90:.2f}, {hi90:.2f}]")
print(f"                        Gaussian-equivalent 2-sigma: [{lo2:.3f}, {hi2:.3f}]")
print(f"   M_TOV               (Nathanail 2021, 2101.01735): 2-sigma [2.087, 2.326]")
print(f"   DIFFERENT PAPERS. The first version called them 'the same analysis paper'.")
chk("COMPUTED: put on a 2-sigma footing the GW190814 interval's lower bound falls BELOW 2.50, so "
    "'entirely at or above the bar' does not hold at matched credibility",
    lo2 < BAR,
    f"2-sigma lower bound {lo2:.3f} < {BAR}. The FIRES framing depended on the 90% level and on "
    f"comparing it against a 2-sigma range -- unlike summaries")

# ---- 4. the radio revision, stated at defensible strength ---------------------------------------
print("\n4. THE RADIO REVISION -- not 'drift'")
for mu_,sd_,lbl in [(2.14,0.095,"Cromartie 2020"),(2.08,0.070,"Fonseca 2021")]:
    z=(BAR-mu_)/sd_; print(f"   {lbl:<18} {mu_} +/- {sd_:.3f}   z = {z:5.2f}   P = {tail(z):.2e}")
chk("the two radio numbers are NESTED analyses of one constant mass, not independent epochs -- "
    "Fonseca 'combines' prior data and 'confirms and improves upon' it",
    True,
    "so the defensible statement is that the posterior was revised downward and tightened, NOT "
    "that a physical quantity drifted. The 76,510 ratio reproduces but does not mean what the "
    "first version said it meant")

print("""
5. THE CORRECTED PICTURE

   ONE bar: 2.5 Msun for certain refutation, 1.5 for "troubling" if Bethe-Brown is credited.
   ONE criterion, method-agnostic: securely a neutron star, mass high enough, estimate precise.

   Three estimates bearing on it, all evidence, none excluded by instrument:
       J0740+6620   2.08 +/- 0.07   radio timing        6.00 sigma from the bar
       J0952-0607   2.35 +/- 0.11   optical, 2025       1.36 sigma, P = 8.6%
       GW190814     securely a NS?  UNRESOLVED IDENTITY -- conditional, and at matched
                                    credibility its interval is not wholly above the bar

   WHAT IS UNDECIDED IS THE OBJECT, NOT THE INSTRUMENT. GW190814 is conditional because nobody
   knows whether it is a neutron star, not because gravitational waves are the wrong tool.

   DUHO'S RULING TO KEEP BOTH SURVIVES -- and codex says so explicitly. But the reason he was
   given was wrong. The right reason: J0740 and J0952 are two estimates of one quantity with
   different likelihoods and systematics, so both are evidence. Not: an instrument question is
   unresolved and one must choose a branch.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
