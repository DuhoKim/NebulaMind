#!/usr/bin/env python3
"""B41 -- coverage proof for the census, ordered by Duho's 2026-08-30 directive (via Blanc):
"read the unflagged remainder".

V5, AFTER CGATE_B41V4 (B41V4_REFUTED_B37_REFRESHER_BINDINGS). AGATE_B41V4 confirmed v4 --
including calling the A5/B17 bindings "correct" when they were existence-only (`("f.md","")`
rows skip the substring test via `if frag`); CGATE caught that, plus that entries 23 and 54 had
NO bound prior artifact at all. The one-seat-does-the-work pattern, recorded again. V5's
repairs, from CGATE_B41V4's required list:
  16. Four explicit refresher chains for B37's refreshed entries, each binding: the entry's own
      refresher line in CGATE_B37 (the reread declaration), the actual prior artifact, its
      token, and a content fragment proving that artifact engages the right source. The
      strengths are printed, not implied: none of the four prior artifacts contains a scoped
      "read in full" sentence of its own -- the full-source testimony for 26/44 lives in
      CGATE_B37's words ("my full-source A5/B17 adjudication"); entry 23's prior (CGATE_A10)
      rules on its cutoff claim; entry 54's prior (AGATE_B15) is SUBJECT-matched only -- it
      audits the curvature claim against Planck 1807.06209 and never names entry 54.
  17. Flag 6 binds the notes' read phrase ("read at last"), not just the reclassification
      headline.

V4, AFTER CGATE_B41V3 (B41V3_REFUTED_RECEIPT_BINDINGS). The substantive numbers survived that
gate -- 39/39, paper-tier miss rate 1 of 2, precision 1 of 3, claim-level unmeasured -- but the
closer itself was refuted because green predicates validated loosely combined strings where
their labels claimed bound facts. V4's repairs, all from that verdict's required list:
  9.  B37's four refreshed prior receipts (23, 26, 44, 54) are now individually bound to the
      verdict's refresher lines and to the earlier full-source gate artifacts it names
      (CGATE_A5, CGATE_B17); the five fresh reads are bound per-entry, not by a floating
      "in full".
  10. B43's row binds CGATE_B43 (token + "in full and sequentially") AND AGATE_B43 (token +
      "full sequential read") -- both landed; "lands separately" is no longer an excuse.
  11. The eleven-paper sample is receipt-bound to CGATE_B29's sentence "I re-read all eleven
      sampled papers from their pinned full texts" + token, not just re-drawn.
  12. Every batch row requires each member's "entry N" to appear in its bound receipt document
      (B39's verdict names the paper, not the number -- bound via "Dymnikova" + the capture
      sentence, stated here).
  13. Flag 6 binds the notes' reclassification headline; flag 25 binds CGATE_B25's entry-25
      ruling sentences, not just first-line tokens.
  14. The COVERAGE check's label now separates the RECORD-level conclusion (the artifacts
      support 39/39) from the SCRIPT-level one (these predicates bind those artifacts; they
      still cannot certify human reading, only the signed record of it).
  15. The two claim-level lists in the metrics prose are labelled as two distinct observations.

V3's repairs (kept): entry-5 double miss computed live (pool-external file scanned, criterion
(0,0,0), would not flag even in-pool); entry 6's pre-rule basis disclosed; pool boundary
printed; live==frozen equality. V2's repairs (kept): b43 receipt for entry 38; {57} bound to
CGATE_B32's own words. V1's sin: binding {38,57} to b33's retrospective comment.
SEAT SPLITS, both resolved: on {38,57} (AGATE blessed, CGATE refuted) -- b43 receipts entry 38
either way; on the miss-rate presentation (AGATE would print a claim-level 1-of-6, CGATE
refuses a metric without a frozen denominator) -- this file follows CGATE's rule and prints
both seats' observations, labelled, below.

WHAT THIS PROVES AND WHAT IT DOESN'T. The union arithmetic plus per-entry receipt bindings
prove: the committed record contains, for every readable BHU paper, a read-and-adjudication
receipt (unflagged papers under the b28 rule; flags via their own artifacts; entry 6's
predates the rule -- disclosed). Phrase bindings certify the RECORD, not the reading act.
The obstruction ground truth is the bibliography's CURRENT Testability labels -- the gated
census's output plus Duho's rulings -- not independent re-derivation. The 12-paper not-located
list is bound to the wrap-up's record; "all paywalled" is that round's testimony.
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

print("=" * 98); print("B41 v4 -- census coverage: per-entry receipt bindings"); print("=" * 98)

# --- the corpus partition ------------------------------------------------------------------------
SUPPORT = {29, 30, 32, 33, 34, 35, 58}
BHU = set(range(1, 59)) - SUPPORT
NOT_LOCATED = {1, 2, 3, 4, 13, 14, 16, 18, 42, 47, 48, 50}
chk("BOUND: the not-located list is the wrap-up's, verbatim (that round's record; login-gated)",
    "1, 2, 3, 4, 13, 14, 16, 18, 42, 47, 48, 50" in txt("WRAP_UP_20260830_OVERNIGHT.md"))
READABLE = BHU - NOT_LOCATED
chk("PARTITION: 51 BHU papers = 39 readable + 12 not-located, disjoint",
    len(BHU) == 51 and len(READABLE) == 39 and not (READABLE & NOT_LOCATED))

# --- the screen's flags: recomputed live over ITS OWN POOL, equality ----------------------------
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
chk("FLAGS RECOMPUTED, EQUALITY over the stated pool (mapped bhu-reading *_clean.txt -- the "
    "boundary is part of the finding): exactly b28's frozen set",
    live_flags == FROZEN_FLAGS and "FLAGGED={22,25,6}" in txt("b28_missrate_draw.py"),
    f"live: {sorted(live_flags)}")
E5 = os.path.join(ROOT, "reviews/bhu-citation-custody-evidence-20260811/arxiv-1412.0105v1.txt")
t5 = " ".join(open(E5, errors="ignore").read().split())
c5 = (len(re.findall(IMPOSSIBILITY, t5)), len(re.findall(DOMAIN, t5)), len(re.findall(REFUTABLE, t5)))
print(f"      entry 5 counterfactual: pool-external file scanned separately -> counts {c5} "
      f"vs threshold (5,2,2) -> would NOT have flagged")
chk("ENTRY 5 DOUBLE MISS: its text was never in the screen's pool, AND the criterion scores it "
    "(0,0,0) -- it hides from the vocabulary even in-pool",
    os.path.exists(E5) and "Pathria" in t5 and c5 == (0, 0, 0) and not is_obstruction(t5))
_notes = open(NOTES).read()
chk("FLAG 6 RECEIPTED, per-fact: the notes' batch-9 section carries the read phrase AND the "
    "reclassification headline; date 2026-08-23 predates the b28 rule -- disclosed",
    "# Batch 9 — entry 6" in _notes
    and "reclassed QUALITATIVE-DIRECTIONAL" in _notes
    and "read at last" in _notes)
chk("FLAG 22 RECEIPTED: CGATE_B24 read the complete pinned source; the gated true positive",
    "I read the complete pinned source" in txt("CGATE_B24_VERDICT.md")
    and token("CGATE_B24_VERDICT.md") == "SCOPE_NARROWED_COUNT_AND_CELL")
chk("FLAG 25 RECEIPTED, per-fact: CGATE_B25 rules on entry 25 itself -- the arguable local "
    "no-go acknowledged, the flag rejected under the paper-level convention",
    "arguable local no-go inside entry 25" in txt("CGATE_B25_VERDICT.md")
    and "does not make B1's flag correct under the current primary-paper classification"
        in txt("CGATE_B25_VERDICT.md")
    and token("AGATE_B25_VERDICT.md") == "PRECISION_REFUTED_ARTEFACT_AND_HONESTY"
    and token("CGATE_B25_VERDICT.md") == "PRECISION_NARROWED_CURRENT_SUBSET_ONLY")

# --- the preregistered sample: re-drawn AND receipt-bound ---------------------------------------
SEED = "5d5a2454e54b7638401428bfc58d3a4cdd87a8ad"
B28_READABLE = [5,7,8,9,10,11,12,21,22,23,24,25,26,27,31,36,37,38,39,40,41,43,44,45,46,49,51,52,53,54,55,56,57,6]
chk("BOUND: b28's frame list occurs verbatim in b28's committed text",
    "READABLE=[5,7,8,9,10,11,12,21,22,23,24,25,26,27,31,36,37,38,39,40,41,43,44,45,46,49,51,52,53,54,55,56,57,6]"
    in txt("b28_missrate_draw.py"))
SAMPLE = set(sorted(random.Random(int(SEED[:15], 16)).sample(sorted(set(B28_READABLE) - FROZEN_FLAGS), 11)))
chk("RE-DRAWN: the committed seed reproduces the 11-paper sample",
    SAMPLE == {5, 7, 10, 24, 27, 36, 37, 40, 46, 49, 56})

# --- receipt engine: every row = (set, requirements ALL-of, token checks) -----------------------
# a requirement is (file, fragment); every member's "entry N" must appear in the row's receipt
# document unless the row names an explicit alternative identity fragment (B39: "Dymnikova").
ROWS = {
    "b29 sample": (SAMPLE, "CGATE_B29_VERDICT.md",
        [("CGATE_B29_VERDICT.md", "I re-read all eleven sampled papers from their pinned full texts"),
         ("CGATE_B29_VERDICT.md", "| entry | independent verdict | source-level reason |")],
        [("CGATE_B29_VERDICT.md", "MISSRATE_REFUTED_THREE_MISSES_IN_SAMPLE")], "TABLE"),
    "b32 gate-read": ({57}, "CGATE_B32_VERDICT.md",
        [("CGATE_B32_VERDICT.md", "all 39 PDF pages")],
        [("CGATE_B32_VERDICT.md", "CANDIDATE_NARROWED_ENTRY57_NOT_PROOF_OWNER")], None),
    "b33 batch 2": ({8, 43, 55}, "CGATE_B33_VERDICT.md",
        [("b33_census_batch2.py", "entries 8, 43, 55"),
         ("CGATE_B33_VERDICT.md", "all three papers in full")],
        [("CGATE_B33_VERDICT.md", "BATCH2_CONFIRMED")], None),
    "b34 batch 3": ({51, 31, 12}, "CGATE_B34_VERDICT.md",
        [("b34_census_batch3.py", "entries 51, 31, 12"),
         ("CGATE_B34_VERDICT.md", "I read all three pinned papers in full")],
        [("CGATE_B34_VERDICT.md", "BATCH3_REFUTED_ENTRY51_TIER_AND_DRAW")], None),
    "b36 batch 4": ({39, 21, 11}, "CGATE_B36_VERDICT.md",
        [("b36_census_batch4.py", "entries 39, 21, 11"),
         ("CGATE_B36_VERDICT.md", "I read all three pinned papers in full")],
        [("CGATE_B36_VERDICT.md", "BATCH4_NARROWED_DRAW_PROVEN_NOT_BLINDNESS")], None),
    "b37 closer (5 fresh + 4 refreshed)": ({9, 23, 26, 41, 44, 45, 52, 53, 54}, "CGATE_B37_VERDICT.md",
        [("b37_census_final.py", "[9,23,26,41,44,45,52,53,54]"),
         ("CGATE_B37_VERDICT.md", "I read these five required sources in full for this gate"),
         ("CGATE_B37_VERDICT.md", "For the permitted refresher set, I re-read the decisive sections"),
         # entry 23's chain: refresher line + prior artifact ruling on 23's claim, with token
         ("CGATE_B37_VERDICT.md", "current source abstract, derivation, and Discussion/Conclusions"),
         ("CGATE_A10_VERDICT.md", "Do not promote entry 23"),
         # entry 26's chain: B37's full-source testimony + the A5 gate on entry 26
         ("CGATE_B37_VERDICT.md", "plus my full-source A5 adjudication"),
         ("CGATE_A5_VERDICT.md", "Gaztanaga, entry 26"),
         # entry 44's chain: B37's full-source testimony + B17's source-engaged content
         ("CGATE_B37_VERDICT.md", "my full-source B17 adjudication"),
         ("CGATE_B17_VERDICT.md", "(5.1) imports an observational DGP constraint"),
         # entry 54's chain: refresher line + subject-matched prior (does NOT name entry 54)
         ("CGATE_B37_VERDICT.md", "the full-source B15 curvature adjudication"),
         ("AGATE_B15_VERDICT.md", "Planck 2018 VI (1807.06209)")],
        [("CGATE_B37_VERDICT.md", "CENSUS_REFUTED_ENTRIES52_AND53"),
         ("CGATE_A10_VERDICT.md", "HOLD_UNCALIBRATED_CUTOFF"),
         ("CGATE_A5_VERDICT.md", "AUDIT_CONFIRMED_TIER_ONLY"),
         ("CGATE_B17_VERDICT.md", "AUDIT_REFUTED_MISSED_EQ5_1_AND_TIER"),
         ("AGATE_B15_VERDICT.md", "CONTRAST_REFUTED_NAIVE_STATISTICS")], None),
    "b38 acquisitions": ({15, 17, 20, 28}, "CGATE_B38_VERDICT.md",
        [("b38_acquisitions_batch.py", "entries 15, 17, 20, 28"),
         ("CGATE_B38_VERDICT.md", "I read all four pinned texts in full")],
        [("CGATE_B38_VERDICT.md", "ACQ_NARROWED_entry20_identity_and_owned_subresults")], None),
    "b39 entry 19": ({19}, "CGATE_B39_VERDICT.md",
        [("b39_entry19.py", "entry 19 acquired"),
         ("CGATE_B39_VERDICT.md", "pinned capture in full")],
        [("CGATE_B39_VERDICT.md", "E19_NARROWED_DERIVED_SUBCASE_AND_ABRIDGED_CAPTURE")],
        "Dymnikova"),
    "b43 entry 38 (both gates landed)": ({38}, "CGATE_B43_VERDICT.md",
        [("b43_entry38_fullread.py", "all 3262 lines sequentially"),
         ("CGATE_B43_VERDICT.md", "in full and sequentially"),
         ("AGATE_B43_VERDICT.md", "full sequential read")],
        [("CGATE_B43_VERDICT.md", "ENTRY38_NARROWED_THEOREM8_STATEMENT_AND_SCOPE"),
         ("AGATE_B43_VERDICT.md", "ENTRY38_CONFIRMED_NOT_OBSTRUCTION")], None),
}
all_ok = True
for name, (s, receipt_doc, reqs, toks, alt_id) in ROWS.items():
    row_ok = all(frag in txt(f) for f, frag in reqs if frag) \
         and all(os.path.exists(os.path.join(_HERE, f)) for f, _ in reqs) \
         and all(token(f) == t for f, t in toks)
    rd = txt(receipt_doc)
    if alt_id is None:
        ids_ok = all(f"entry {n}" in rd for n in s)
    elif alt_id == "TABLE":   # per-entry verdict table rows: "| N | **verdict** | reason |"
        ids_ok = all(f"| {n} |" in rd for n in s)
    else:
        ids_ok = alt_id in rd
    if not (row_ok and ids_ok):
        print(f"      BINDING FAILED: {name}  (reqs={row_ok}, ids={ids_ok})")
    all_ok = all_ok and row_ok and ids_ok
print("      B37 refresher strengths, printed not implied: 23 -> CGATE_A10 rules on its cutoff")
print("      claim; 26 -> CGATE_A5 is its own gate ('Gaztanaga, entry 26'); 44 -> CGATE_B17")
print("      engages the source's equations; 54 -> AGATE_B15 is SUBJECT-matched only (audits")
print("      the curvature claim against Planck, never names entry 54). None of the four prior")
print("      artifacts contains its own 'read in full' sentence; the full-source testimony for")
print("      26/44 is CGATE_B37's, and B37's decisive-section rereads are the read declaration")
print("      for all four.")
chk("RECEIPTS, per-entry: every row's requirements hold AND every member is named in its "
    "receipt document ('entry N', per-entry table rows for b29, or the stated identity "
    "fragment for b39) AND every verdict token matches -- B37's four refresher chains are "
    "individually bound with strengths printed above",
    all_ok)
batch_union = set().union(*(s for s, *_ in ROWS.values()))

# --- the coverage claim, both directions ---------------------------------------------------------
covered = FROZEN_FLAGS | batch_union          # SAMPLE rides inside ROWS now, receipt-bound
missing = sorted(READABLE - covered)
extra   = sorted(covered - READABLE)
print(f"\n  readable corpus      : {len(READABLE)}")
print(f"  flags hand-checked   : {sorted(FROZEN_FLAGS)}   (receipted above)")
print(f"  receipted rows       : {len(batch_union)} papers in {len(ROWS)} rows (sample + batches)")
print(f"  UNION                : {len(covered)}   missing: {missing}   outside corpus: {extra}")
chk("COVERAGE -- record-level: the bound artifacts contain a read-and-adjudication receipt for "
    "every readable BHU paper. Script-level: these predicates bind those artifacts' sentences "
    "and tokens; they certify the RECORD of reading, not the act",
    missing == [] and extra == [])
remainder = READABLE - FROZEN_FLAGS - SAMPLE
chk("REMAINDER: the unflagged-unsampled remainder is exactly the batch rows minus the sample, "
    "25 papers",
    remainder == (batch_union - SAMPLE) and len(remainder) == 25)

# --- how many belonged: parsed from the bibliography's current adjudicated labels ----------------
T = open(BIB).read(); cut = T.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", T[:cut], re.M)]
blocks = {n: T[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
obs = set()
for n, b in blocks.items():
    m = re.search(r"Testability: \*\*([A-Z-]+)\*\*", b)
    if m and m.group(1) == "THEORETICAL-OBSTRUCTION": obs.add(n)
print(f"\n  paper-level THEORETICAL-OBSTRUCTION entries (current adjudicated labels): {sorted(obs)}")
chk("PARSED: the CLOSED-CENSUS FRAME (readable-39) holds exactly two paper-level obstructions, "
    "22 and 5; entry 48 -- tiered 2026-08-30 under question 8, AFTER this census closed and "
    "OUTSIDE its frame (it was not-located then) -- is asserted separately",
    (obs & READABLE) == {22, 5} and obs == {22, 5, 48})

# --- the measured numbers, honestly labelled -----------------------------------------------------
obs_frame = obs & READABLE      # the closed census frame; entry 48 was tiered POST-census,
                                # outside this frame, and was never in the screen's pool
hits = sorted(obs_frame & FROZEN_FLAGS); missed = sorted(obs_frame - FROZEN_FLAGS)
print(f"\n  (entry 48, tiered 2026-08-30 at question 8, sits OUTSIDE this closed frame and")
print(f"  outside the screen's pool -- it is not a screen hit or miss; the frame metrics stand.)")
print(f"\n  PAPER-TIER miss rate, CLOSED READABLE-39 FRAME : {len(missed)} of {len(obs_frame)} "
      f"(hit {hits}, missed {missed})")
print(f"  PAPER-TIER precision                          : {len(hits)} of {len(FROZEN_FLAGS)} flags")
print(f"  entry 5's miss is a DOUBLE miss               : never in the pool, and (0,0,0) on the")
print(f"  vocabulary -- see the counterfactual above.")
print("  CLAIM-LEVEL sensitivity                       : NOT MEASURED as a metric (CGATE's rule:")
print("  no denominator without a frozen claim table). Two DISTINCT observations, labelled:")
print("    (i) records observation: entries 25, 37, 38, 51, 52, 53, 57 carry derived claim-level")
print("        exclusions in their prose; the screen flagged only 25 of those seven;")
print("    (ii) AGATE_B41's proposed paper list: 'caught 22; missed 5, 37, 51, 52, 53' -- a")
print("        different set (paper-level truth plus four claim-level carriers), kept as its")
print("        seat's stated position, not adopted as a denominator.")
chk("MEASURED (paper-tier, closed readable-39 frame): miss rate 1 of 2 -- the screen missed "
    "entry 5, found only by full read; precision 1 of 3 flags. The printed denominator is now "
    "BOUND (CGATE_Q8's catch: the output printed len(obs)=3 while this predicate said 2)",
    hits == [22] and missed == [5] and len(FROZEN_FLAGS) == 3 and len(obs_frame) == 2,
    "the number question 1's record says nobody had measured -- now measured over a census "
    "receipted paper-by-paper")

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
