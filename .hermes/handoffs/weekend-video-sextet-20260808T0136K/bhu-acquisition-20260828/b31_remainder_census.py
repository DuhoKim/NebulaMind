#!/usr/bin/env python3
"""B31 -- census of the 20 unflagged readable papers the miss-rate sample did NOT draw.

WHY. b29's random sample of 11 found two to three papers meeting the obstruction rule while filed
CONSISTENCY-ONLY. That is a measured leak, not a suspicion. THE OTHER 20 HAVE NEVER BEEN CHECKED FOR
OBSTRUCTION CONTENT. This is a census of the remainder, so there is no sampling statistic to compute
-- only reading.

THE PATTERN IS DELIBERATELY WIDER THAN THE ONE THAT FAILED. My b29 triage reported "0
impossibility-word hits" for entry 5, whose central result is that a matching CANNOT BE SMOOTH,
because my pattern contained neither "not smooth" nor "can only". That was the seventh false absence
from a narrow pattern in this lane. The pattern below adds the constructions that failure exposed.

THIS FILE TRIAGES. It does not classify and it moves no tier. Every hit needs reading, and the rule
is the one preregistered in b28.
"""
import re, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__))
D=os.path.abspath(os.path.join(_HERE,".."))
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

FRAME=[5,7,8,9,10,11,12,21,23,24,26,27,31,36,37,38,39,40,41,43,44,45,46,49,51,52,53,54,55,56,57]
SAMPLED=[5,7,10,24,27,36,37,40,46,49,56]
REMAIN=sorted(set(FRAME)-set(SAMPLED))
print("="*98); print("B31 -- census of the unsampled remainder"); print("="*98)
print(f"\n  frame {len(FRAME)}   sampled {len(SAMPLED)}   remainder {len(REMAIN)}")
print(f"  {REMAIN}")
chk("ARITHMETIC: the remainder is exactly the frame minus the preregistered sample, with no "
    "quiet additions or drops",
    len(REMAIN)==20 and not (set(REMAIN)&set(SAMPLED)) and set(REMAIN)|set(SAMPLED)==set(FRAME),
    "20 papers. A census of these plus the 11 already read covers every unflagged readable paper")

# widened -- each addition is a construction that defeated the earlier pattern
IMPOSS = (r"cannot be both|cannot be\b|can not be\b|can only be\b|can only occur|is not smooth|"
          r"not smooth|does not yield|no .{0,30}(?:can|exists?)\b|impossible|impossibility|"
          r"obstruct\w*|must give up|prevents?\b|forbidden|rules? out|ruled out|excluded|"
          r"if and only if|no solution|cannot exist|never .{0,20}(?:exists?|occurs?)")
def load(rel):
    p=os.path.join(D,rel)
    if p.endswith(".pdf"):
        import fitz; d=fitz.open(p); return " ".join(" ".join(pg.get_text() for pg in d).split())
    return " ".join(open(p,errors="ignore").read().split())

T=open(os.path.join(D,"bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")).read()
cut=T.find("## Ranked:")
st=[(m.start(),int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ",T[:cut],re.M)]
bl={n:T[p:(st[i+1][0] if i+1<len(st) else cut)] for i,(p,n) in enumerate(st)}
def norm(x): return re.sub(r"[^a-z0-9]","",x.lower())
CH=("skip to main content","sign up for alerts","close banner","privacy policy")
RL=("[google scholar]","[crossref]","[scilit]")
cache={}
for dp,_,fn in os.walk(D):
    for f in fn:
        if f.endswith((".txt",".pdf")):
            p=os.path.join(dp,f)
            try:
                if p.endswith(".pdf"):
                    import fitz; d=fitz.open(p); cache[p]=" ".join(" ".join(pg.get_text() for pg in d).split())
                else: cache[p]=" ".join(open(p,errors="ignore").read().split())
            except Exception: pass
MAPPED={41:"2007.11556_clean.txt"}
print("\n  triage -- hits are CANDIDATES for reading, not findings")
print(f"  {'entry':>5}  {'hits':>4}  file")
rows=[]
for n in REMAIN:
    tm=re.search(r'[“"]([^”"]{8,140})[.”"]', bl[n].split("\n")[0])
    k=norm(tm.group(1))[:60] if tm else None
    best=None
    for p,full in cache.items():
        h=" ".join(full[:6000].split())
        if sum(1 for c in CH if c in h.lower())>=2 or sum(1 for c in RL if c in h.lower())>=2: continue
        if (k and k in norm(h) and len(full)>=3000) or os.path.basename(p)==MAPPED.get(n):
            if best is None or len(full)>len(cache[best]): best=p
    if not best: rows.append((n,-1,"NO FILE")); continue
    hits=len(re.findall(IMPOSS,cache[best],re.I))
    rows.append((n,hits,os.path.basename(best)))
for n,h,f in sorted(rows,key=lambda r:-r[1]):
    print(f"  {n:>5}  {h:>4}  {f[:52]}")
top=[r for r in rows if r[1]>=12]
chk("MEASURED: the widened pattern separates the remainder rather than flagging all or none",
    0 < len(top) < len(REMAIN),
    f"{len(top)} of {len(REMAIN)} carry 12+ impossibility constructions. The threshold is a "
    f"READING ORDER, not a verdict -- b29 proved a low count can hide a real obstruction (entry 5 "
    f"scored ZERO on the narrow pattern and was one)")
print(f"""
  READ FIRST: {[n for n,_,_ in sorted(top,key=lambda r:-r[1])]}

  ABSENCE CLAIM, to the lane's standard.
    PATTERN: the widened impossibility set above, counted per paper.
    ONE CLASS IT WOULD MISS: a paper stating its no-go only in symbols or in a theorem environment
      whose prose carries none of these words -- exactly how entry 5 escaped the narrow pattern.
    WHAT WAS DONE: the count is used ONLY to order reading, never to exclude. Every one of the 20
      is to be read regardless of its score, and a zero-hit paper is not thereby cleared.
""")
n_=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n_}/{len(checks)} passed")
sys.exit(0 if n_==len(checks) else 1)
