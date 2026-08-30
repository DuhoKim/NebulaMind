#!/usr/bin/env python3
"""B41 -- coverage proof for the census, ordered by Duho's 2026-08-30 directive (via Blanc):
"read the unflagged remainder".

V2, REPAIRED AFTER CGATE_B41 (COVERAGE_REFUTED_ENTRY38_UNRECEIPTED). V1's defect: it bound
{38,57} to b33's retrospective sentence "38 and 57 were done in b32's" -- circular testimony,
not a receipt. The B32 record is asymmetric: both seats read entry 57 in full ("all 39 PDF
pages"); neither recorded a full read of entry 38. V1's demonstrated coverage was therefore
38/39. The repairs, all from CGATE_B41's required list:
  1. entry 38 read in full under the b28 rule (b43, 2026-08-30) -- its own batch row here;
  2. {57} bound to CGATE_B32's explicit full-read statement, not b33's comment;
  3. every batch bound to its OWN gate verdict (first-line token + full-read phrase), not just
     the batch script's self-description;
  4. flags 6/22/25 bound to their actual adjudication artifacts, not just declared FROZEN;
  5. live_flags == FROZEN_FLAGS equality, not subset;
  6. the miss rate labelled PAPER-TIER, with claim-level sensitivity stated as NOT MEASURED.

WHAT THIS PROVES AND WHAT IT DOESN'T. The union arithmetic and bindings prove every readable
BHU paper has a receipted read-plus-adjudication under the one preregistered rule. The
obstruction ground truth is parsed from the bibliography's CURRENT Testability labels -- the
output of the gated census plus Duho's rulings -- so the miss rate is measured against the
corpus's adjudicated record, not against independent re-derivation. The 12-paper not-located
list is bound to the wrap-up's record; "all paywalled" is that round's testimony, not re-checked
here.
"""
import re, os, random
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")
SRC = os.path.join(ROOT, "bhu-reading-20260823/sources/")
MAP = os.path.join(ROOT, "bhu-theory-phase6-curvature-20260827/ENTRY_SOURCE_MAP.md")
NOTES = os.path.join(ROOT, "bhu-reading-20260823/READING_NOTES_01.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

def txt(name): return open(os.path.join(_HERE, name)).read()
def token(name): return txt(name).splitlines()[0].strip()

print("=" * 98); print("B41 v2 -- census coverage: computed, receipted, both directions"); print("=" * 98)

# --- the corpus partition ------------------------------------------------------------------------
SUPPORT = {29, 30, 32, 33, 34, 35, 58}
BHU = set(range(1, 59)) - SUPPORT
NOT_LOCATED = {1, 2, 3, 4, 13, 14, 16, 18, 42, 47, 48, 50}
chk("BOUND: the not-located list is the wrap-up's, verbatim (that round's record; login-gated)",
    "1, 2, 3, 4, 13, 14, 16, 18, 42, 47, 48, 50" in txt("WRAP_UP_20260830_OVERNIGHT.md"))
READABLE = BHU - NOT_LOCATED
chk("PARTITION: 51 BHU papers = 39 readable + 12 not-located, disjoint",
    len(BHU) == 51 and len(READABLE) == 39 and not (READABLE & NOT_LOCATED))

# --- the screen's flags: recomputed live, EQUALITY, each bound to its adjudication artifact ------
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
chk("FLAGS RECOMPUTED, EQUALITY: the live screen over the mapped corpus flags exactly b28's "
    "frozen set -- a new flag or a lost flag goes red here",
    live_flags == FROZEN_FLAGS and "FLAGGED={22,25,6}" in txt("b28_missrate_draw.py"),
    f"live: {sorted(live_flags)}")
chk("FLAG 6 RECEIPTED: full read in the reading notes (batch 9) and the paper-level "
    "false-positive ruling in b25's gated convention dispute",
    "# Batch 9 — entry 6" in open(NOTES).read()
    and os.path.exists(os.path.join(_HERE, "AGATE_B25_VERDICT.md")))
chk("FLAG 22 RECEIPTED: CGATE_B24 read the complete pinned source; entry 22 is the gated "
    "true positive",
    "I read the complete pinned source" in txt("CGATE_B24_VERDICT.md")
    and token("CGATE_B24_VERDICT.md") == "SCOPE_NARROWED_COUNT_AND_CELL")
chk("FLAG 25 RECEIPTED: b25 re-runs the criterion and both B25 gates ruled on it",
    token("AGATE_B25_VERDICT.md") == "PRECISION_REFUTED_ARTEFACT_AND_HONESTY"
    and token("CGATE_B25_VERDICT.md") == "PRECISION_NARROWED_CURRENT_SUBSET_ONLY")

# --- the preregistered sample: re-drawn from the committed seed ----------------------------------
SEED = "5d5a2454e54b7638401428bfc58d3a4cdd87a8ad"
B28_READABLE = [5,7,8,9,10,11,12,21,22,23,24,25,26,27,31,36,37,38,39,40,41,43,44,45,46,49,51,52,53,54,55,56,57,6]
chk("BOUND: b28's frame list occurs verbatim in b28's committed text",
    "READABLE=[5,7,8,9,10,11,12,21,22,23,24,25,26,27,31,36,37,38,39,40,41,43,44,45,46,49,51,52,53,54,55,56,57,6]"
    in txt("b28_missrate_draw.py"))
SAMPLE = set(sorted(random.Random(int(SEED[:15], 16)).sample(sorted(set(B28_READABLE) - FROZEN_FLAGS), 11)))
chk("RE-DRAWN: the committed seed reproduces the 11-paper sample",
    SAMPLE == {5, 7, 10, 24, 27, 36, 37, 40, 46, 49, 56})

# --- the census batches: each bound to its script AND its own gate verdict -----------------------
# (set, batch artifact, fragment in it, verdict artifact, expected first-line token, read phrase)
BATCHES = {
    "b32 gate-read":  ({57}, "CGATE_B32_VERDICT.md", "all 39 PDF pages",
                       "CGATE_B32_VERDICT.md", "CANDIDATE_NARROWED_ENTRY57_NOT_PROOF_OWNER", "all 39 PDF pages"),
    "b33 batch 2":    ({8, 43, 55}, "b33_census_batch2.py", "entries 8, 43, 55",
                       "CGATE_B33_VERDICT.md", "BATCH2_CONFIRMED", "in full"),
    "b34 batch 3":    ({51, 31, 12}, "b34_census_batch3.py", "entries 51, 31, 12",
                       "CGATE_B34_VERDICT.md", "BATCH3_REFUTED_ENTRY51_TIER_AND_DRAW", "in full"),
    "b36 batch 4":    ({39, 21, 11}, "b36_census_batch4.py", "entries 39, 21, 11",
                       "CGATE_B36_VERDICT.md", "BATCH4_NARROWED_DRAW_PROVEN_NOT_BLINDNESS", "in full"),
    "b37 closer":     ({9, 23, 26, 41, 44, 45, 52, 53, 54}, "b37_census_final.py", "[9,23,26,41,44,45,52,53,54]",
                       "CGATE_B37_VERDICT.md", "CENSUS_REFUTED_ENTRIES52_AND53", "in full"),
    "b38 acquisitions": ({15, 17, 20, 28}, "b38_acquisitions_batch.py", "entries 15, 17, 20, 28",
                       "CGATE_B38_VERDICT.md", "ACQ_NARROWED_entry20_identity_and_owned_subresults", "in full"),
    "b39 entry 19":   ({19}, "b39_entry19.py", "entry 19 acquired",
                       "CGATE_B39_VERDICT.md", "E19_NARROWED_DERIVED_SUBCASE_AND_ABRIDGED_CAPTURE", "in full"),
    "b43 entry 38":   ({38}, "b43_entry38_fullread.py", "all 3262 lines sequentially",
                       "b43_entry38_fullread.py", None, "read IN FULL under the census rule"),
}
ok = True
for name, (s, art, frag, vart, vtok, vphrase) in BATCHES.items():
    t = txt(art); v = txt(vart)
    row = frag in t and vphrase in v and (vtok is None or token(vart) == vtok)
    if not row: print(f"      BINDING FAILED: {name}")
    ok = ok and row
chk("BOUND: every batch's set is bound to its committed artifact AND its own gate verdict "
    "(token + read phrase); entry 38 to b43, entry 57 to CGATE_B32's own words -- b33's "
    "retrospective comment is no longer load-bearing", ok,
    "b43's gate verdicts land separately; its READ is the receipt bound here")
batch_union = set().union(*(s for s, *_ in BATCHES.values()))

# --- the coverage claim, both directions ---------------------------------------------------------
covered = FROZEN_FLAGS | SAMPLE | batch_union
missing = sorted(READABLE - covered)
extra   = sorted(covered - READABLE)
print(f"\n  readable corpus      : {len(READABLE)}")
print(f"  flags hand-checked   : {sorted(FROZEN_FLAGS)}   (receipted above)")
print(f"  preregistered sample : {sorted(SAMPLE)}")
print(f"  census batches       : {len(batch_union)} papers in {len(BATCHES)} receipted rows")
print(f"  UNION                : {len(covered)}   missing: {missing}   outside corpus: {extra}")
chk("COVERAGE: every readable BHU paper has a receipted read under the b28 rule; nothing "
    "adjudicated is outside the corpus", missing == [] and extra == [],
    "v1 could not say this -- entry 38's receipt did not exist; b43 is it")
remainder = READABLE - FROZEN_FLAGS - SAMPLE
chk("REMAINDER: the unflagged-unsampled remainder is exactly the batch union, 25 papers",
    remainder == batch_union and len(remainder) == 25)

# --- how many belonged: parsed from the bibliography's current adjudicated labels ----------------
T = open(BIB).read(); cut = T.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", T[:cut], re.M)]
blocks = {n: T[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
obs = set()
for n, b in blocks.items():
    m = re.search(r"Testability: \*\*([A-Z-]+)\*\*", b)
    if m and m.group(1) == "THEORETICAL-OBSTRUCTION": obs.add(n)
print(f"\n  paper-level THEORETICAL-OBSTRUCTION entries (current adjudicated labels): {sorted(obs)}")
chk("PARSED: the readable corpus holds exactly two paper-level obstructions, 22 and 5",
    obs == {22, 5} and obs <= READABLE)

# --- the measured number, honestly labelled ------------------------------------------------------
hits = sorted(obs & FROZEN_FLAGS); missed = sorted(obs - FROZEN_FLAGS)
print(f"\n  PAPER-TIER miss rate on the receipted census : {len(missed)} of {len(obs)} "
      f"(hit {hits}, missed {missed})")
print(f"  PAPER-TIER precision                          : {len(hits)} of {len(FROZEN_FLAGS)} flags")
print("  CLAIM-LEVEL sensitivity                       : NOT MEASURED. The record carries")
print("  claim-level exclusions in at least entries 25, 37, 38, 51, 52, 53, 57 -- the screen")
print("  flagged only 25 of those. A claim-level rate needs its own frozen ground-truth table")
print("  and a multiple-claims-per-paper rule; this file does not supply one.")
chk("MEASURED (paper-tier only): miss rate 1 of 2 -- the screen missed entry 5, found only by "
    "full read; precision 1 of 3 flags",
    hits == [22] and missed == [5] and len(FROZEN_FLAGS) == 3,
    "the number question 1's record says nobody had measured -- now measured over a census "
    "receipted paper-by-paper")

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
