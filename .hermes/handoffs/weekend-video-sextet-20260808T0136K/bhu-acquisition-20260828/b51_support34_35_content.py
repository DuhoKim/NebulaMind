#!/usr/bin/env python3
"""B51 -- support-layer content verification, entries 34 (Ferdman) and 35 (Tauris): the
measurement spine of the neutron-star falsifiers. Self-computing string-presence checks (no seat
gate; the finding is "is the load-bearing claim in the pinned source", deterministic).

ENTRY 34 = Ferdman et al., "Asymmetric mass ratios for bright double neutron-star mergers",
Nature 583 (2020), pinned `ferdman2020_clean.txt`. Both load-bearing claims CONFIRMED verbatim:
the masses 1.62 ± 0.03 / 1.27 ± 0.03 M_sun and PSR J1913+1102's helium-star / ultra-stripped
formation channel. Source-accurate; no over-attribution.

ENTRY 35 = Tauris et al., "Formation of double neutron star systems", ApJ 846 (2017), pinned
`tauris2017_clean.txt`. FINDING (the sweep's first derived-vs-quoted distinction): Tauris
supplies the FORMATION FRAMEWORK and per-phase accretion physics (Case BB, recycling,
hypercritical/Eddington accretion -- all present). But the record's ΔM_NS ≈ 0.0134 M_sun TOTAL
is NOT a verbatim Tauris number -- it is the auditor's per-phase SUM, derived and DOUBLE-GATED in
Phase 3 Track B (GATE_B_VERDICT + XGATE_B_VERDICT). The record now says so explicitly (per the
describe-vs-compute discipline: a computed number is labelled computed, not quoted). No
discrepancy: Tauris backs the framework; the number is the gated derivation FROM it.
"""
import re, os
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
P3 = os.path.join(ROOT, "bhu-theory-phase3-cns-20260821")
FERD = os.path.join(P3, "sources/ferdman2020_clean.txt")
TAUR = os.path.join(P3, "sources/tauris2017_clean.txt")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B51 -- support entries 34 & 35 content bound to source"); print("=" * 98)

F = " ".join(open(FERD, errors="ignore").read().split())
chk("ENTRY 34 IDENTITY: pinned source is Ferdman's asymmetric-mass DNS paper",
    "Asymmetric" in F.replace("asymmetric", "Asymmetric") and "J1913" in F)
chk("ENTRY 34 CLAIM 1: the masses 1.62 ± 0.03 and 1.27 ± 0.03 M_sun are verbatim in the source",
    "1.62 ± 0.03" in F and "1.27 ± 0.03" in F)
chk("ENTRY 34 CLAIM 2: the helium-star / ultra-stripped formation channel is in the source",
    "helium star" in F and "Ultra-stripped" in F.replace("ultra-stripped", "Ultra-stripped"))

Tt = " ".join(open(TAUR, errors="ignore").read().split())
chk("ENTRY 35 FRAMEWORK: Tauris supplies the DNS-formation accretion physics (Case BB, "
    "recycling, hypercritical/Eddington) -- the machinery the 0.0134 sum is built from",
    "Case BB" in Tt and "recycl" in Tt and ("hypercritical" in Tt or "Eddington" in Tt))
chk("ENTRY 35 DERIVED-NOT-QUOTED: 0.0134 does NOT appear verbatim in the Tauris source -- "
    "confirming it is the auditor's derived total, not a Tauris quote",
    "0.0134" not in Tt)
chk("ENTRY 35 DERIVATION RECEIPTED: the 0.0134 total is double-gated in Phase 3 Track B",
    os.path.exists(os.path.join(P3, "GATE_B_VERDICT.md"))
    and os.path.exists(os.path.join(P3, "XGATE_B_VERDICT.md"))
    and "0.0134" in open(os.path.join(P3, "TRACK_B_INTERIM_FINDING.md"), errors="ignore").read())

B = open(BIB).read()
cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b34 = " ".join(blocks[34].split()); b35 = " ".join(blocks[35].split())
chk("RECORD 34: attributes 1.62/1.27 ± 0.03 and the He-star channel -- both source-confirmed above",
    "1.62/1.27" in b34 and "He-star" in b34)
chk("RECORD 35: now states the 0.0134 total is DERIVED (not a Tauris quote) and Track-B gated",
    "NOT a verbatim Tauris number" in b35 and "DOUBLE-GATED in Phase 3 Track B" in b35)

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
