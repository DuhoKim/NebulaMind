#!/usr/bin/env python3
"""B41 -- coverage proof for the census, ordered by Duho's 2026-08-30 directive (via Blanc):
"read the unflagged remainder".

THE DIRECTIVE ARRIVED AFTER THE WORK. The census batches (b29 sample, b32 gate-reads, b33, b34,
b36, b37, b38, b39) already read the unflagged remainder under the same logic Duho now ratifies
("then look harder with more entries", his question-3 precedent). But "already done" is testimony
until the set arithmetic is computed. This file computes it: the union of every adjudicated set
is compared against the readable corpus, both directions, and the final report numbers (how many
read / how many belonged / measured screen miss rate) are derived here, not quoted.

PROVENANCE RULE. Each adjudicated set is re-declared below AND bound to its committed artifact by
an exact-substring assertion against that artifact's text, so a silent edit of either side goes
red. The b28 sample is not even re-declared -- it is RE-DRAWN from the committed seed. The
obstruction set is parsed from the bibliography's Testability lines, not recalled.

SCOPE HONESTY. "Adjudicated" here means paper-level reading under b28's one preregistered rule
(prove no member of a stated class satisfies a stated conjunction, refutable by counterexample).
The three screen flags were hand-checked earlier under the same question (b25 records the
convention dispute on entry 25). Claim-level exclusions inside constructive papers (37, 51,
52/53, 57, 38 s4) are recorded in prose per CGATE_B30 s5 and are NOT counted as paper-level
membership here.
"""
import re, os, random
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")
SRC = os.path.join(ROOT, "bhu-reading-20260823/sources/")
MAP = os.path.join(ROOT, "bhu-theory-phase6-curvature-20260827/ENTRY_SOURCE_MAP.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

def txt(name): return open(os.path.join(_HERE, name)).read()

print("=" * 98); print("B41 -- census coverage: computed, not asserted"); print("=" * 98)

# --- the corpus partition ------------------------------------------------------------------------
SUPPORT = {29, 30, 32, 33, 34, 35, 58}                  # measurement/support entries, not BHU papers
BHU = set(range(1, 59)) - SUPPORT                       # 51 BHU papers
NOT_LOCATED = {1, 2, 3, 4, 13, 14, 16, 18, 42, 47, 48, 50}
chk("BOUND: the not-located list is the wrap-up's, verbatim",
    "1, 2, 3, 4, 13, 14, 16, 18, 42, 47, 48, 50" in txt("WRAP_UP_20260830_OVERNIGHT.md"),
    "12 papers, all paywalled, waiting on Duho's institutional login")
READABLE = BHU - NOT_LOCATED
chk("PARTITION: 51 BHU papers = 39 readable + 12 not-located, disjoint",
    len(BHU) == 51 and len(READABLE) == 39 and not (READABLE & NOT_LOCATED))

# --- the screen's flags: recomputed live (b25's verbatim criterion + map parse) ------------------
IMPOSSIBILITY = r"cannot be both|cannot be\b|can not be\b|does not yield|no .{0,30}(?:can|exists?)\b|impossible|obstruct\w*|must give up|prevents?\b"
DOMAIN        = r"[Cc]onsider a .{0,80}(?:spacetime|metric|parent|class|solution)|[Aa]ssume that|under the (?:same )?assumptions?|hypothes[ei]s"
REFUTABLE     = r"escape|evasion|requires? an? (?:additional|extra)|must give up at least one|unless"
def is_obstruction(T):
    return (len(re.findall(IMPOSSIBILITY, T)) >= 5 and len(re.findall(DOMAIN, T)) >= 2
            and len(re.findall(REFUTABLE, T)) >= 2)
f2e = {}
for line in open(MAP).read().splitlines():
    if not line.startswith("|"): continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 3: continue
    nums = re.findall(r"\d{1,2}", cells[0].replace("~", ""))
    if not nums: continue
    for m in re.finditer(r"`([^`]+)`", line):
        base = os.path.basename(m.group(1))
        stem = re.sub(r"^arxiv_|_clean\.txt$|\.txt$", "", base)
        f2e.setdefault(stem, nums[-1])
live_flags = set()
for f in sorted(os.listdir(SRC)):
    if not f.endswith("_clean.txt"): continue
    stem = f[: -len("_clean.txt")]
    if stem in f2e and is_obstruction(" ".join(open(SRC + f, errors="ignore").read().split())):
        live_flags.add(int(f2e[stem]))
FROZEN_FLAGS = {22, 25, 6}
chk("BOUND: b28 froze the same flag set this run recomputes",
    "FLAGGED={22,25,6}" in txt("b28_missrate_draw.py") and FROZEN_FLAGS <= live_flags,
    f"live corpus flags today: {sorted(live_flags)}")

# --- the preregistered sample: re-drawn from the committed seed, not re-declared -----------------
SEED = "5d5a2454e54b7638401428bfc58d3a4cdd87a8ad"
B28_READABLE = [5,7,8,9,10,11,12,21,22,23,24,25,26,27,31,36,37,38,39,40,41,43,44,45,46,49,51,52,53,54,55,56,57,6]
chk("BOUND: b28's frame list occurs verbatim in b28's committed text",
    "READABLE=[5,7,8,9,10,11,12,21,22,23,24,25,26,27,31,36,37,38,39,40,41,43,44,45,46,49,51,52,53,54,55,56,57,6]"
    in txt("b28_missrate_draw.py"))
SAMPLE = set(sorted(random.Random(int(SEED[:15], 16)).sample(sorted(set(B28_READABLE) - FROZEN_FLAGS), 11)))
chk("RE-DRAWN: the committed seed reproduces the 11-paper sample",
    SAMPLE == {5, 7, 10, 24, 27, 36, 37, 40, 46, 49, 56})

# --- the census batches: each set bound to its committed artifact --------------------------------
BATCHES = {
    "b32 gate-reads": ({38, 57}, "b33_census_batch2.py", "38 and 57 were done in b32's"),
    "b33 batch 2":    ({8, 43, 55}, "b33_census_batch2.py", "entries 8, 43, 55"),
    "b34 batch 3":    ({51, 31, 12}, "b34_census_batch3.py", "entries 51, 31, 12"),
    "b36 batch 4":    ({39, 21, 11}, "b36_census_batch4.py", "entries 39, 21, 11"),
    "b37 closer":     ({9, 23, 26, 41, 44, 45, 52, 53, 54}, "b37_census_final.py", "[9,23,26,41,44,45,52,53,54]"),
    "b38 acquisitions": ({15, 17, 20, 28}, "b38_acquisitions_batch.py", "entries 15, 17, 20, 28"),
    "b39 entry 19":   ({19}, "b39_entry19.py", "entry 19 acquired"),
}
bound = all(frag in txt(art) for _, (s, art, frag) in BATCHES.items())
chk("BOUND: every batch set's members occur verbatim in that batch's committed artifact", bound)
batch_union = set().union(*(s for s, _, _ in BATCHES.values()))

# --- the coverage claim, both directions ---------------------------------------------------------
covered = FROZEN_FLAGS | SAMPLE | batch_union
missing = sorted(READABLE - covered)
extra   = sorted(covered - READABLE)
print(f"\n  readable corpus      : {len(READABLE)}")
print(f"  flags hand-checked   : {sorted(FROZEN_FLAGS)}")
print(f"  preregistered sample : {sorted(SAMPLE)}")
print(f"  census batches       : {len(batch_union)} papers in {len(BATCHES)} artifacts")
print(f"  UNION                : {len(covered)}   missing from union: {missing}   outside corpus: {extra}")
chk("COVERAGE: every readable BHU paper is adjudicated; nothing adjudicated is outside the corpus",
    missing == [] and extra == [],
    "the unflagged remainder Duho ordered read IS read -- this is the set arithmetic, not a memory")
remainder = READABLE - FROZEN_FLAGS - SAMPLE
chk("REMAINDER: the unflagged-unsampled remainder is exactly the batch union, 25 papers",
    remainder == batch_union and len(remainder) == 25)

# --- how many belonged: parsed from the bibliography, not recalled -------------------------------
T = open(BIB).read(); cut = T.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", T[:cut], re.M)]
blocks = {n: T[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
obs = set()
for n, b in blocks.items():
    m = re.search(r"Testability: \*\*([A-Z-]+)\*\*", b)
    if m and m.group(1) == "THEORETICAL-OBSTRUCTION": obs.add(n)
print(f"\n  paper-level THEORETICAL-OBSTRUCTION entries (parsed from Testability lines): {sorted(obs)}")
chk("PARSED: the readable corpus holds exactly two paper-level obstructions, 22 and 5",
    obs == {22, 5} and obs <= READABLE)

# --- the number nobody had measured: the screen's miss rate on adjudicated ground truth ----------
hits = sorted(obs & FROZEN_FLAGS); missed = sorted(obs - FROZEN_FLAGS)
print(f"\n  screen hit rate on adjudicated obstructions : {len(hits)} of {len(obs)} (hit {hits}, missed {missed})")
print(f"  screen precision at paper level             : {len(hits)} of {len(FROZEN_FLAGS)} flags")
chk("MEASURED: miss rate 1 of 2 -- the screen missed entry 5, found only by full read; "
    "precision 1 of 3 flags",
    hits == [22] and missed == [5] and len(FROZEN_FLAGS) == 3,
    "the number question 1's record says nobody had measured, now measured over a FULL census")

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
