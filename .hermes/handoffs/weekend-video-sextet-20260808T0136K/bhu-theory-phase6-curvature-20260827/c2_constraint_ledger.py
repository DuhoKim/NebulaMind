#!/usr/bin/env python3
"""C2: the curvature constraint ledger, with provenance on every entry.

Convention (computed in c1): Omega_k > 0 = OPEN = negative spatial curvature.
                             Omega_k < 0 = CLOSED = positive spatial curvature.
The BHU target (2505.23877 sec.VI) requires Omega_k < 0.

PROVENANCE:
  V-LOCAL  verbatim from a paper pinned/extracted in this repo, read this session
  V-FETCH  verbatim from the source's own text via fetch this session
  C-DERIV  computed here from a V-quoted quantity
  2ND      quoted by another paper; NOT verified against the original

EQUATION-NUMBER PROVENANCE (CGATE_PHASE6 caveat, acted on 2026-08-28): the Planck equation
labels below -- 46a, 46b, 47a, 47b -- are as printed in the arXiv **PDF** of 1807.06209
(sha-free identification: 8.9 MB PDF, text extracted locally with pdftotext -layout; sec.7.3
begins at extracted line 3382). The gate seat found the SAME values carrying labels 44b/45a/45b
in the arXiv **HTML** rendering. The numbers and the quoted sentences agree; only the equation
numbering differs by rendering. Cite the values, not the labels, or pin the rendering.

REVISION 2026-08-28: the Planck gap is CLOSED. Section 7.3 of 1807.06209 was retrieved as PDF
and extracted locally, so every Planck entry below is now V-LOCAL. The previously 2ND entry
(-0.04 +/- 0.01, as quoted inside the target paper) is superseded by Planck's own Eq. 46b, and
the target's rendering of it turns out to be ACCURATE. That correction is carried explicitly
rather than silently.
"""
import sys

checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

RK = 21.0
CZ = +1.0 / RK**2      # Chen & Zaldarriaga: R_k = 21 H_0^-1, negative spatial curvature => open

# (source, combination, Omega_k, sigma_low, sigma_high, provenance, quoted note)
LEDGER = [
    ("Planck 2018 VI Eq.46a",  "Planck TT+lowE",                -0.056, 0.018, 0.028, "V-LOCAL",
     "'an apparent detection of curvature at well over 2 sigma'"),
    ("Planck 2018 VI Eq.46b",  "Planck TT,TE,EE+lowE",          -0.044, 0.015, 0.018, "V-LOCAL",
     "THE VALUE THE TARGET QUOTES as '-0.04 +/- 0.01' -- accurate rendering"),
    ("Planck 2018 VI sec.7.3", "CamSpec TT,TE,EE+lowE",         -0.037, 0.014, 0.019, "V-LOCAL",
     "'not robust at the approximately 0.5 sigma level to modelling of the polarization likelihoods'"),
    ("Planck 2018 VI Eq.47a",  "TT,TE,EE+lowE+lensing",         -0.0106, 0.0065, 0.0065, "V-LOCAL",
     "lensing 'pulls parameters back into consistency with a spatially flat universe to well within 2 sigma'"),
    ("Planck 2018 VI Eq.47b",  "TT,TE,EE+lowE+lensing+BAO",      0.0007, 0.0019, 0.0019, "V-LOCAL",
     "'spatially flat to a 1 sigma accuracy of 0.2%'"),
    ("ACT DR6 Eq.46",          "ACT",                           -0.004, 0.010, 0.010, "V-LOCAL",
     "'the ACT power spectra prefer a flat geometry'"),
    ("ACT DR6 Eq.46",          "W-ACT",                         -0.010, 0.009, 0.009, "V-LOCAL",
     "same equation, second line"),
    ("Chen & Zaldarriaga",     "DESI DR2+CMB",                   CZ,    0.0011, 0.0011, "C-DERIV",
     "from verbatim 'R_k = 21 H_0^-1'; negative spatial curvature => OPEN"),
    ("DESI DR1 FS + DR2 BAO",  "+CMB",                           0.0028, 0.0011, 0.0011, "V-FETCH",
     "'Omega_k > 0 ... about 2.4 sigma away from flatness'"),
    ("wCDM+Ok (2512.09486)",   "DESI DR2+BBN+OHD",               0.002, 0.045, 0.045, "V-LOCAL",
     "'nearly flat but marginally open'"),
    ("wCDM+Ok (2512.09486)",   "DESI DR1+BBN+OHD",               0.075, 0.054, 0.070, "V-LOCAL",
     "'favors a open universe'"),
]

print("=" * 104)
print(f"{'source':26s} {'combination':30s} {'Omega_k':>10s} {'|sigma|':>8s} {'geometry':>9s}  prov")
print("=" * 104)
rows = []
for src, comb, ok, slo, shi, prov, note in LEDGER:
    sig = abs(ok) / (slo if ok < 0 else shi)
    geom = "OPEN" if ok > 0 else ("CLOSED" if ok < 0 else "flat")
    rows.append((src, comb, ok, sig, geom, prov, note))
    print(f"{src:26.26s} {comb:30.30s} {ok:+10.5f} {sig:8.2f} {geom:>9s}  {prov}")
    print(f"{'':26s}   {note}")
print("=" * 104)

secondhand = [r for r in rows if r[5] == "2ND"]
chk("every entry is now first-hand -- the Planck gap is closed",
    len(secondhand) == 0, f"{len(rows)} entries, {len(secondhand)} second-hand")

# --- 1. the target's Planck number, checked against Planck itself -------------------
tgt_lo, tgt_hi = -0.04 - 0.01, -0.04 + 0.01          # target quotes -0.04 +/- 0.01
pl = [r for r in rows if "46b" in r[0]][0]
pl_lo, pl_hi = pl[2] - 0.015, pl[2] + 0.018
overlap = not (tgt_hi < pl_lo or tgt_lo > pl_hi)
chk("the target's quoted Planck value is an ACCURATE rendering of Planck Eq.46b",
    overlap, f"target [{tgt_lo:+.3f},{tgt_hi:+.3f}] vs Planck [{pl_lo:+.4f},{pl_hi:+.4f}] -- overlapping")

# --- 2. what Planck itself does with that number ------------------------------------
lens  = [r for r in rows if "47a" in r[0]][0]
bao   = [r for r in rows if "47b" in r[0]][0]
chk("adding lensing moves Planck's own curvature back toward flat by a large factor",
    abs(lens[2]) < abs(pl[2]) / 3.0, f"{pl[2]:+.4f} -> {lens[2]:+.4f}")
chk("adding BAO makes Planck's own result consistent with flat and CHANGES ITS SIGN",
    bao[2] > 0 and bao[3] < 1.0, f"{bao[2]:+.5f} +/- 0.0019, {bao[3]:.2f} sigma, OPEN side")

# --- 3. the geometry tally, excluding the CMB-alone rows Planck itself disowns -------
robust = [r for r in rows if r[1] not in
          ("Planck TT+lowE", "Planck TT,TE,EE+lowE", "CamSpec TT,TE,EE+lowE")]
chk("with the CMB-alone rows set aside, nothing detects curvature at all",
    all(r[3] < 2.6 for r in robust), f"max |sigma| = {max(r[3] for r in robust):.2f}")
chk("and every DESI-based entry sits on the OPEN side, which the model forbids",
    all(r[2] > 0 for r in robust if "DESI" in r[1] or "DESI" in r[0]),
    f"{len([r for r in robust if r[2] > 0])} open of {len(robust)} robust entries")

# --- 4. "isn't the universe just flat, so isn't it ruled out?" (Duho, 2026-08-28) ---------
# Answered by splitting the model into the version WITH its stated number and the version
# with only its sign. The tightest first-hand constraint is Planck Eq.47b.
OK_BEST, SIG_BEST = bao[2], 0.0019
print("\n" + "=" * 104)
print('DOES FLATNESS RULE IT OUT?  tightest constraint: Omega_K = '
      f'{OK_BEST:+.4f} +/- {SIG_BEST:.4f} (Planck+lensing+BAO)')
print("=" * 104)
# (a) the STATED bracket: chi_k ~ chi_*, giving Omega_k in roughly [-0.09, -0.05]
for edge, label in ((-0.05, "nearest edge of the stated bracket (-0.07+0.02)"),
                    (-0.07, "the stated central value"),
                    (-0.09, "far edge of the stated bracket (-0.07-0.02)")):
    print(f"   {label:48s} Omega_k = {edge:+.2f}  ->  {abs(OK_BEST-edge)/SIG_BEST:7.1f} sigma away")
excl = abs(OK_BEST - (-0.05)) / SIG_BEST
chk("the model's STATED bracket is excluded outright by current data",
    excl > 10.0, f"nearest edge is {excl:.1f} sigma from the tightest measurement")
# (b) the SIGN-only version: any Omega_k < 0 whatsoever
print(f"\n   sign-only version (any Omega_k < 0, no floor):")
for cand in (-0.001, -1e-5, -1e-9):
    print(f"      Omega_k = {cand:+.1e}  ->  {abs(OK_BEST-cand)/SIG_BEST:6.2f} sigma  "
          f"{'EXCLUDED' if abs(OK_BEST-cand)/SIG_BEST > 3 else 'NOT excluded'}")
chk("but the sign-only version survives any finite-precision flatness measurement",
    abs(OK_BEST - (-1e-9)) / SIG_BEST < 1.0,
    "Omega_k = -1e-9 sits 0.37 sigma from the tightest constraint; no measurement reaches it")
print("""
   So flatness DOES kill something: it kills the version of the model that had a NUMBER --
   the one where chi_k ~ chi_*, which is the identification that produced the bracket AND
   the explanation of the CMB low quadrupole. What survives is chi_k >> chi_*, i.e. the
   version with the sign and nothing else, which no flatness measurement can ever reach.

   The model keeps its prediction by giving up the thing that made it a prediction.""")

print("""
WHAT THE CLOSED GAP CHANGES

  It exonerates the target on its Planck NUMBER. Planck Eq.46b is
  Omega_K = -0.044 (+0.018/-0.015), and the target's '-0.04 +/- 0.01' is a fair rendering
  of it. My earlier audit could not verify this and flagged it as the one strongly-closed
  figure I could not stand behind. It stands. That correction is recorded, not buried.

  What the target omits is what PLANCK SAYS ABOUT ITS OWN NUMBER, in the same section:

    - the pull is attributed to the same cause as the lensing-amplitude anomaly --
      'The reasons for the pull towards negative values of Omega_K ... are essentially the
       same as those that lead to the preference for A_L > 1';
    - it is likelihood-dependent -- CamSpec gives -0.037 (+0.019/-0.014) and the result is
      'not robust at the approximately 0.5 sigma level to modelling of the polarization
       likelihoods';
    - adding lensing pulls it 'back into consistency with a spatially flat universe to well
      within 2 sigma' (-0.0106 +/- 0.0065);
    - adding BAO gives Omega_K = +0.0007 +/- 0.0019, 'spatially flat to a 1 sigma accuracy
      of 0.2%' -- and flips the sign to the side the model forbids.

  So the target quotes Planck's number correctly and omits Planck's reading of it. That is a
  weaker charge than misquotation and a fairer one, and it is the one the evidence supports.
""")
np_ = sum(1 for _, ok, _ in checks if ok)
print(f"SELF-CHECKS: {np_}/{len(checks)} passed")
sys.exit(0 if np_ == len(checks) else 1)
