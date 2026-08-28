#!/usr/bin/env python3
"""Step 1 of the sweep: mechanical screen for falsifier-shaped text in the 19 pinned entries.

PURPOSE. Three of three entries re-read today were OVERCLAIMS. That makes UNDERCLAIMS the blind
spot: a CONSISTENCY-ONLY entry that actually contains an author-stated number and threshold is a
live test we have been ignoring, and it is worth more than another demotion.

WHAT THIS IS. A lexical screen, nothing more. It finds sentences carrying BOTH a
falsification/prediction construction AND a quantity. That is the shape of "if X exceeds N, the
model is dead". It ranks entries by how many such sentences they contain.

WHAT THIS IS NOT. Evidence of anything. A paper can state a falsifier in words this screen
cannot see, and can trip the screen while claiming nothing. Its output is a READING ORDER for
Step 2, not a finding. Step 3's control sample exists precisely because this screen's silence
proves nothing -- the same defect as an abs() that cannot see a sign change.
"""
import os, re, json

LANE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(LANE, "..", "bhu-reading-20260823", "sources")
MAP = {
 "1111.1017_clean.txt":1, "smolin_1992_clean.txt":6, "smolin_2004_cns_clean.txt":31,
 "smoller_temple_2000_clean.txt":36, "0210105_clean.txt":37, "math-ph_0302036_clean.txt":38,
 "1105.6127_clean.txt":39, "2008.02136_clean.txt":40, "2007.11556_clean.txt":41,
 "2304.12018_clean.txt":43, "1309.1487_clean.txt":44, "2210.15186_clean.txt":45,
 "blau_guendelman_guth_1987_clean.txt":49, "0910.1181_clean.txt":51,
 "1808.08327_clean.txt":52, "1906.11824_clean.txt":53, "2505.23877_clean.txt":54,
 "2007.06664_clean.txt":55, "smoller_temple_1997_clean.txt":57,
}

# a claim-shaped construction ...
VERB = re.compile(r'\b(falsif\w*|refut\w*|rule[sd]? out|ruled out|exclud\w*|'
                  r'inconsistent with|would be (?:dead|wrong|excluded)|'
                  r'predict\w*|prediction|constrain\w*|upper (?:mass )?limit|'
                  r'lower bound|upper bound|threshold|smoking gun|test(?:able|s)?\b)', re.I)
# ... carrying a quantity
QUANT = re.compile(r'(\d+(?:\.\d+)?\s*(?:±|\+/-|\+-)\s*\d+(?:\.\d+)?'      # 2.35 +- 0.11
                   r'|\d+(?:\.\d+)?\s*(?:M_?\W?sun|M\W?⊙|solar mass|Gpc|Mpc|eV|sigma|σ|%)'
                   r'|[<>≲≳]\s*\d+(?:\.\d+)?'                              # > 2
                   r'|\b\d+(?:\.\d+)?\s*(?:times )?10\s*\^?\s*[-−]?\d+)', re.I)

def sentences(t):
    t = re.sub(r'\s+', ' ', t)
    return re.split(r'(?<=[.!?])\s+', t)

rows = []
detail = {}
for fn, entry in sorted(MAP.items(), key=lambda x: x[1]):
    p = os.path.join(SRC, fn)
    try:
        txt = open(p, errors="ignore").read()
    except OSError:
        continue
    sents = sentences(txt)
    hits = [s.strip() for s in sents if len(s) < 600 and VERB.search(s) and QUANT.search(s)]
    # de-duplicate near-identical lines (reference lists, repeated captions)
    seen, uniq = set(), []
    for h in hits:
        k = re.sub(r'[^a-z0-9]', '', h.lower())[:90]
        if k not in seen:
            seen.add(k); uniq.append(h)
    kw = len(sents)
    rows.append((entry, fn, len(uniq), kw, round(1000*len(uniq)/max(kw,1), 2)))
    detail[entry] = uniq

rows.sort(key=lambda r: (-r[2], r[0]))
print("=" * 100)
print("S1 — falsifier-shaped sentences per pinned entry (claim-verb AND quantity, deduped)")
print("=" * 100)
print(f"{'entry':>6} {'hits':>5} {'sents':>7} {'per-1k':>7}  file")
for e, fn, n, kw, dens in rows:
    print(f"{e:>6} {n:>5} {kw:>7} {dens:>7}  {fn}")

out = os.path.join(LANE, "s1_screen_hits.json")
json.dump({str(k): v for k, v in detail.items()}, open(out, "w"), indent=1)
print(f"\nfull hit text written to {os.path.basename(out)} "
      f"({sum(len(v) for v in detail.values())} sentences) — this is the Step 2 reading packet")

top = [r for r in rows if r[2] >= 5]
print(f"\n{len(top)} entries carry >=5 falsifier-shaped sentences.")
print("Screen output is a READING ORDER, not a finding. Entries scoring 0 are NOT cleared —")
print("they are exactly what the Step 3 control sample must include.")

# =====================================================================================
# NEGATIVE RESULT, recorded 2026-08-28. THIS SCREEN DOES NOT WORK ON THIS CORPUS.
# Do not use its ranking. Do not read its zeros as "no falsifier language".
#
# Diagnosis, measured rather than assumed:
#
# 1. SENTENCE SEGMENTATION FAILS. These clean texts carry "###" headers, affiliations and
#    equation fragments with almost no terminal punctuation. Splitting on [.!?] yields
#    multi-paragraph blobs -- the first "sentence" of entry 55 is the entire title +
#    affiliation block. The unit the screen counts is not a sentence.
#
# 2. THE CO-OCCURRENCE TEST IS THEREFORE MEANINGLESS. Measured on four files:
#       entry 55: VERB-matching chunks 63, QUANT-matching 25, BOTH 0
#       entry 41: VERB 1,  QUANT 9,  BOTH 0
#       entry 45: VERB 6,  QUANT 27, BOTH 0
#    Both regexes fire plentifully on their own; they simply never co-occur in whatever a
#    "chunk" happens to be. 14 zeros is an artefact of segmentation, not evidence of absence.
#
# 3. OCR MANGLING compounds it in the older scanned files. Smolin 2004's key falsifier line
#    renders as "SuMciently high is certainly 2:5M" -- ffi->M, decimal point->colon, Msun->M.
#    The regexes cannot match it. That is the single most falsifier-shaped sentence in the
#    entire corpus and the screen scored its file at 1.
#
# WHY IT IS BEING DROPPED RATHER THAN FIXED.
#    The screen existed to avoid reading 48 papers. Step 0 established the sweepable set is
#    19, not 48 -- four seat batches, entirely affordable. The screen now buys nothing and
#    costs a false-negative rate I would have to measure with a control sample. Dropping it
#    removes that whole apparatus: blind-classify all 19 and the screen's blind spot cannot
#    exist.
#
#    Had the sweepable set really been 48, the right move would have been to fix segmentation
#    (sliding character window, not sentences) and normalise the OCR first. Recorded in case
#    a future corpus is large enough to need it.
