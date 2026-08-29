#!/usr/bin/env python3
"""B18 -- do other pinned SOURCES admit a prediction that observation already killed?

WHY. Entry 44's fired prediction was invisible at the bibliography level. It surfaced only because
the paper itself was read, and CGATE_Q3 named the resulting limit precisely: "I did not reread every
one of the 58 underlying papers ... I cannot prove that no source body contains an unrecorded fired
prediction." b14 swept the RECORD. This sweeps the SOURCES.

THE TELL, taken from the one confirmed case rather than invented: 1309.1487 says "the simple model
of cosmological perturbations, developed in Sec. 4 is already ruled out by cosmological observations
at >5 sigma level". Two features -- refutation language, and it points at the authors' OWN model.

THIS PRINTS CANDIDATES. It does not classify, and no tier moves on its output. Defect 1aa is a
reminder that an absence claim can satisfy this lane's full standard and still be false.
"""
import re, os, sys
S="../bhu-reading-20260823/sources/"
MAP="../bhu-theory-phase6-curvature-20260827/ENTRY_SOURCE_MAP.md"
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

# file -> entry, from the map
M=open(MAP).read()
f2e={}
# FIXED: the first version used an optional \d+ group before the capture, so "31" matched the
# optional group with "3" and captured "1". Every entry number was truncated -- entry 31 printed as
# 1, entry 44 as 4. Now: take the first cell, strip markup, and use its LAST number, which is the
# corrected value in rows written as "~~1~~ **46**".
for line in M.splitlines():
    if not line.startswith("|"): continue
    cells=[c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 3: continue
    nums=re.findall(r"\d{1,2}", cells[0].replace("~",""))
    fm=re.search(r"`([^`]+_clean\.txt)`", line)
    if nums and fm: f2e.setdefault(fm.group(1), nums[-1])
# ONLY sweep sources that are actually corpus entries. The first version swept everything in the
# directory, which includes Planck, DESI, GW and EOS papers pinned as RECEIPTS -- their "fails to
# match" language is about likelihood systematics, not a cosmology being falsified. 4 of the 8
# original hits were that.
files=sorted(f for f in os.listdir(S) if f.endswith("_clean.txt") and f in f2e)
unmapped=sorted(f for f in os.listdir(S) if f.endswith("_clean.txt") and f not in f2e)
print("="*98); print("B18 -- source-level sweep for self-admitted firings"); print("="*98)
print(f"\ncorpus-entry sources swept: {len(files)}   |   map pairs: {len(f2e)}   |   pinned-but-unmapped (receipts, not entries): {len(unmapped)}")
chk("PARSED: the map's entry numbers survive intact -- the known two-digit rows come back as 31 "
    "and 44, not as the truncated 1 and 4 the first version produced",
    f2e.get("smolin_2004_cns_clean.txt")=="31" and f2e.get("1309.1487_clean.txt")=="44",
    f"entry 31 -> {f2e.get('smolin_2004_cns_clean.txt')}, entry 44 -> {f2e.get('1309.1487_clean.txt')}. "
    f"The first version printed 1 and 4 and would have sent every candidate to the wrong entry")

REFUT = r"(ruled out|excluded by|is excluded|inconsistent with|in conflict with|" \
        r"disfavou?red|at odds with|contradicted by|does not agree with|fails to (?:repro|match|account))"
SELF  = r"(our|we |this model|the present model|the simple model|the model (?:developed|presented))"
OBS   = r"(observ|data|measure|experiment|Planck|WMAP|LIGO|CMB|survey)"
hits={}
for f in files:
    T=" ".join(open(S+f, errors="ignore").read().split())
    for m in re.finditer(REFUT, T, re.I):
        w=T[max(0,m.start()-260):m.start()+260]
        if re.search(SELF, w, re.I) and re.search(OBS, w, re.I):
            hits.setdefault(f, []).append(" ".join(w.split()))
print(f"\nsources with refutation language pointing at the authors' own model: {len(hits)} of {len(files)}")
print("-"*98)
for f in sorted(hits, key=lambda x: -len(hits[x])):
    e=f2e.get(f, "?")
    print(f"  entry {e:>3}  {f:<34} {len(hits[f]):>2} hit(s)")
print("-"*98)

ctrl="1309.1487_clean.txt"
chk("POSITIVE CONTROL: the one paper KNOWN to admit a firing is flagged by this pattern",
    ctrl in hits,
    "1309.1487 (entry 44) -- 'the simple model ... is already ruled out by cosmological "
    "observations at >5 sigma level'. If the probe missed it, nothing it reports about the others "
    "would mean anything")
chk("MEASURED: the probe separates the pinned set rather than flagging all of it or none",
    0 < len(hits) < len(files),
    f"{len(hits)} of {len(files)}. A probe returning everything or nothing is uninformative "
    f"whatever it prints")

print("\nCANDIDATES -- these are NOT findings. Each needs reading.")
for f in sorted(hits, key=lambda x: -len(hits[x])):
    if f==ctrl: continue
    e=f2e.get(f,"?")
    print(f"\n  ENTRY {e} -- {f}")
    print(f"    {hits[f][0][:300]}...")

print("""
ABSENCE CLAIM, to the lane's standard.

  PATTERN: refutation language within 260 characters of a first-person model reference AND an
    observational reference.

  ONE CLASS IT WOULD MISS -- and it is the large one: A PAPER WHOSE PREDICTION WAS KILLED LATER, BY
    DATA IT NEVER SAW. Such a paper says nothing self-critical; the firing lives in the literature
    that came after it. Entry 44 was found only because its authors were unusually candid, and
    candour is not a property this probe can require of anyone else.

  WHAT WAS DONE ABOUT THAT CLASS: it is NOT measured here, and pretending otherwise would repeat
    defect 1aa. What is measured is an upper bound on the work it would take -- the count of pinned
    sources carrying a sharp numeric prediction construct at all, printed below. Confronting each
    against current data is a per-paper job, not a pattern.
""")
PRED = r"(we predict|our model predicts|this predicts|prediction is|we find that .{0,40}=|" \
       r"is predicted to be)"
withpred=[f for f in files if re.search(PRED, " ".join(open(S+f,errors='ignore').read().split()), re.I)]
print(f"   pinned sources carrying a sharp-prediction construct: {len(withpred)} of {len(files)}")
print(f"   -> that is the upper bound on the silent-firing class, unmeasured and named as such")
chk("MEASURED: the size of the class this probe cannot see is bounded and printed, rather than "
    "left as a caveat with no number attached",
    len(withpred) > 0,
    f"{len(withpred)} sources would each need confronting against current data. Naming a blind "
    f"spot without sizing it is what made defect 1aa survive review")
n=sum(1 for _,o,_ in checks if o)
print(f"\nSELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
