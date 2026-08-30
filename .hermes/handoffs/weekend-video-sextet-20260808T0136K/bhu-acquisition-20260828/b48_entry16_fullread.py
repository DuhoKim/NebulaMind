#!/usr/bin/env python3
"""B48 -- entry 16 read in full under the census rule (the VERSION OF RECORD, acquired via
Duho's connected Chrome -- SCOAP3 gold OA, CC-BY).

THE READ: all 11 born-digital pages of Pourhassan, "Multiversal entropy and information
conservation in black hole nucleated baby universes", NPB 1020 (2025) 117160 -- Secs. 1-6 +
references [1]-[54] -- via the clean text companion (pourhassan_2025_npb1020_clean.txt).
This is the ONLY entry in the corpus read from its published version of record rather than a
preprint or scan. BYLINE CORRECTION recorded on pinning: single-author (Behnam Pourhassan);
the record's "et al." was wrong.

RULE, unchanged from b28: does the paper PROVE that no member of a specified class of models
can satisfy a specified conjunction of conditions -- refutable by counterexample, not by
measurement?

VERDICT (mine, to the gate): NOT AN OBSTRUCTION -- a conjecture-stack PROPOSAL; triage's
PROSPECT tier is CONFIRMED by the source, not changed. GATED 2026-08-30: AGATE_B48
ENTRY16_CONFIRMED_PROSPECT / CGATE_B48 ENTRY16_NARROWED (four repairs applied: the et-al
heading, the stale NOT-YET-READ state -- the THIRD stale-state catch today -- the
inherited-vs-locally-reconstructed threshold wording, and the paper's own eq-(19) arithmetic
flaw recorded). Inventory:
  Sec. 2  reviews Garriga-Vilenkin-Zhang bubble dynamics (its ref [18]): the junction relation
          (eq 1), effective potential (eqs 2-5), M_cr (eqs 6-7) -- INHERITED threshold, the
          paper says "Following [18]" and derives nothing new here; super/subcritical defined
          causally (wormhole-to-inflating-interior vs collapse).
  Sec. 3  the proposal: S_total = S_BH + S_ent, S_ent ~ alpha log N; landscape N ~ 10^500 cut
          by CDL accessibility to S_ent^eff >~ 330. Conjecture-flagged in the paper's own
          verbs ("We conjecture", "We posit").
  Sec. 4  the "multiversal second law" (eq 26) and a multiversal Page bound (eq 33) --
          proposed, not derived from established physics.
  Sec. 5  observational PROSPECTS, Table 1: GW echoes, a PBH mass-function feature near M_cr,
          entropy-bound deviations -- NO thresholds, numbers, or datasets; "may hint", "could
          serve". Exactly the PROSPECT class shape.
  No falsifier, no no-member theorem anywhere.

CROSS-LINKS source-owned: ref [19] = entry 50; ref [41] = entry 14; ref [40] = the
Sato-Sasaki-Kodama-Maeda wormhole paper (entry 47's programme); ref [43] = entry 15; ref [36]
= Abedi-Dykaar-Afshordi (entry 44's co-author). The corpus's modern continuation.
"""
import re, os, hashlib
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
PDF = os.path.join(ROOT, "bhu-reading-20260823/sources/pourhassan_2025_npb1020_117160_scoap3.pdf")
TXT = os.path.join(ROOT, "bhu-reading-20260823/sources/pourhassan_2025_npb1020_clean.txt")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B48 -- entry 16 full read (the SCOAP3 version of record)"); print("=" * 98)

raw = open(PDF, "rb").read()
chk("PIN: VoR present, PDF magic, sha256 2d11feddb342...",
    raw[:4] == b"%PDF" and hashlib.sha256(raw).hexdigest().startswith("2d11feddb342"))
S = " ".join(open(TXT, errors="ignore").read().split())
chk("TEXT COMPANION: headered as the VoR extraction with the PDF as pin of record",
    S.startswith("[TEXT EXTRACTION") and "pin of record" in S)
chk("IDENTITY LANDMARKS: title, the single author, journal id, CC-BY/SCOAP3 lines",
    "Multiversal entropy and information conservation" in S and "Behnam Pourhassan" in S
    and "117160" in S and "Funded by SCOAP" in S and "CC BY" in S)
chk("PROPOSAL LANDMARKS: the conjecture verbs, the entropy formula pieces, the multiversal "
    "second law, and the inherited threshold are all in the source",
    "We conjecture" in S and "We posit" in S and "multiversal" in S.lower()
    and "Following [18]" in S.replace("Following the treatment in [18]", "Following [18]")
    and "supercritical" in S)
chk("PROSPECT LANDMARKS: the channels are named without calibration -- Table 1, echoes, PBH "
    "mass function; and the hedging verbs are present",
    "Gravitational Wave Echoes" in S and "Primordial Black Hole Mass Function" in S
    and "may hint" in S)
chk("CROSS-LINK LANDMARKS: all five relational links -- entries 50, 14, 15's papers, the Sato "
    "programme, and the Afshordi echo paper (CGATE_B48: ref [36] was omitted; the pointless "
    "self-replace removed)",
    "Is it possible to create a universe in the laboratory by quantum tunneling?" in S
    and "Black holes as possible sources of closed and semiclosed worlds" in S
    and "Universe generation from black hole interiors" in S
    and "Creation of wormholes by" in S
    and "Echoes from the abyss" in S)
B = open(BIB).read()
cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b16 = " ".join(blocks[16].split())
chk("RECORD: entry 16 carries the VoR pin, the byline correction, the read confirmation, the "
    "inherited-threshold note, and the cross-links",
    "2d11feddb342" in b16 and "SINGLE-AUTHOR" in b16
    and "CONFIRMED BY THE FULL READ 2026-08-30 (b48" in b16
    and "LOCAL heuristic" in b16 and "ref. [19] = entry 50" in b16
    # CGATE_B48's four repairs, asserted in their repaired state:
    and "heading corrected from" in b16
    and "superseded" in b16
    and "internal arithmetic flaw" in b16)
m = re.search(r"Testability: \*\*([A-Z-]+)\*\*", blocks[16])
chk("TIER UNCHANGED: entry 16 remains PROSPECT (triage label now source-confirmed)",
    m is not None and m.group(1) == "PROSPECT")
obs = set()
for n, b in blocks.items():
    mm = re.search(r"Testability: \*\*([A-Z-]+)\*\*", b)
    if mm and mm.group(1) == "THEORETICAL-OBSTRUCTION": obs.add(n)
chk("OBSTRUCTION SET CURRENT: {22, 5, 48} -- entry 16's round changed nothing",
    obs == {22, 5, 48})

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
