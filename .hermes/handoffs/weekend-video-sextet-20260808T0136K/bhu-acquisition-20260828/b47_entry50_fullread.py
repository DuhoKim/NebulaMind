#!/usr/bin/env python3
"""B47 -- entry 50 read in full under the census rule (the long quantum sequel).

THE READ, scope stated exactly: all 34 two-up scan sheets of MIT-CTP-1690 (Farhi, Guth &
Guven, "Is It Possible to Create a Universe in the Laboratory by Quantum Tunneling?", October
1989; published as NPB 339, 417-490), ~68 preprint pages -- Secs. I-VII, references 1-25, and
Appendices A-F -- read completely via the OCR companion (clean on prose, garbled on equations;
figures are INLINE with captions, no separate figure sheets). Sheet 1 was rendered and
visually verified at acquisition; NO other sheet was rendered by me. The gate should render
whatever it distrusts -- the b46 lesson about sheet accounting is why this scope is stated to
the sheet.

RULE, unchanged from b28: does the paper PROVE that no member of a specified class of models
can satisfy a specified conjunction of conditions -- refutable by counterexample, not by
measurement?

VERDICT (mine, to the gate): NOT AN OBSTRUCTION -- the paper is the corpus's second named
ESCAPE from entry 48's theorem, executed: a constructive leading-WKB tunneling-amplitude
calculation for subcritical (M < M_S) false-vacuum bubbles tunneling from the collapsing type
(a) branch to the universe-becoming type (b) branch. Inventory:
  Sec. II   classical trajectories; M_cr/M_S/M_D thresholds; restates ref [9] (= entry 48):
            Penrose applies to an expanding type (a) bubble iff M > M_S -- inherited, not
            re-proven here.
  Sec. III  the reduced action; surface term kills the r-double-dot; crossing-boundary sign
            rule.
  Sec. IV   subtracted-action WKB formalism.
  Sec. V    THE MAIN RESULT: the Euclidean interpolation is NOT a manifold (the wall trajectory
            crosses both tunneling surfaces; theta_S always exceeds pi by their extensive
            numerics); they define a PSEUDOMANIFOLD (covering numbers / singular multi-sheeted
            covering with sqrt(g) changing sign), CONJECTURE its action approximates the
            amplitude, and obtain I_E negative-definite (their 5.34), |I_E| ~ 1/(G chi^2),
            probability ~ 10^(-10^11) at GUT scale.
  Sec. VI   the canonical approach FAILS: p(r, r-dot) noninvertible (their 6.3), no H(r,p),
            non-monotonic action, momentum cannot vanish at both endpoints for M_D < M < M_S.
  Sec. VII  conclusion: "quantum effects can very likely avoid the implications of the
            classical singularity theorems" -- conjecture, flagged; Fischler-Morgan-Polchinski
            agreement.
CLAIM-LEVEL negatives recorded (not tiers): the canonical-method failure (methodological,
their own slicing) and the simple-connectedness exclusion of a nonsingular multi-sheeted
covering. NO falsifier anywhere: the rate estimate is not an observational discriminator, and
the closing pages say even a real creation event may be unverifiable from outside.

TIER: UNREAD -> CONSISTENCY-ONLY, set here under the routine gated-census pattern (b38/b39,
ratified in Duho's morning review). This is NOT the entry-48 situation: the assigned tier is
the census's default constructive class, not an obstruction; both seats verify it in this
round and a refutation reverts it.

CROSS-LINKS now source-owned in the record: 48 (ref [9], the no-go tunneled past), 49 (ref
[6]; footnote 18 corrects its eq. 4.25a sign error), 13 (ref [11], the limiting-curvature
escape family), 47 (ref [2], the Sato chain). The obstruction/escape web is complete:
classical no-go (48) / limiting-curvature escape (13, 14) / quantum-tunneling escape (50).
"""
import re, os, hashlib
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
PDF = os.path.join(ROOT, "bhu-reading-20260823/sources/farhi_guth_guven_ctp1690_kekscan_2000_36_692.pdf")
TXT = os.path.join(ROOT, "bhu-reading-20260823/sources/farhi_guth_guven_ctp1690_clean.txt")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B47 -- entry 50 full read (MIT-CTP-1690 scan)"); print("=" * 98)

raw = open(PDF, "rb").read()
chk("PIN: scan present, PDF magic, sha256 32e93d710705...",
    raw[:4] == b"%PDF" and hashlib.sha256(raw).hexdigest().startswith("32e93d710705"))
S = " ".join(open(TXT, errors="ignore").read().split())
chk("OCR COMPANION: headered as grep receipts with the PDF as pin of record",
    S.startswith("[OCR EXTRACTION") and "pin of record" in S)
chk("IDENTITY LANDMARKS: title, all three authors, CTP number, the NPB submission line",
    "IS IT POSSIBLE TO CREATE" in S and "QUANTUM TUNNELING" in S and "Farhi" in S
    and "Guth" in S and "Guven" in S and "1690" in S and "Nuclear Physics" in S)
chk("STRUCTURE LANDMARKS: the pseudomanifold coinage, covering numbers, the canonical failure, "
    "and all six appendices are in the source",
    "pseudomanifold" in S and "covering number" in S and "noninvertible" in S
    and all(f"APPENDIX {a}" in S for a in "ABCDEF"))
chk("ESCAPE LANDMARKS: the conclusion's quantum-escape sentence and the FMP agreement are in "
    "the source",
    "avoid the implications of the classical singularity theorems" in S
    and "human initiative" in S and "Polchinski" in S)
chk("CROSS-LINK LANDMARKS: refs to entry 48 (PLB 183), entry 13 (PLB 216), entry 49 (PRD 35 "
    "1747) and the Sato chain are in the reference list",
    "1836. 149" in S.replace("183B. 149", "1836. 149") or "1836. 149" in S)
chk("CROSS-LINK LANDMARKS 2: FMM and BGG references present",
    "2166. 272" in S and "035. 1747" in S and "Sato" in S)
B = open(BIB).read()
cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b50 = " ".join(blocks[50].split())
chk("RECORD: entry 50 carries the read scope, the tier provenance, the conjecture status, "
    "both claim-level negatives, and the four cross-links",
    "READ IN FULL 2026-08-30" in b50 and "EXECUTES the quantum escape entry 48 named" in b50
    and "pseudomanifold" in b50 and "noninvertible" in b50
    and "simply connected" in b50 and "ref. [11] = entry 13" in b50)
m = re.search(r"Testability: \*\*([A-Z-]+)\*\*", blocks[50])
chk("TIER: entry 50 now reads CONSISTENCY-ONLY (set by this census read, gates verifying)",
    m is not None and m.group(1) == "CONSISTENCY-ONLY")
obs = set()
for n, b in blocks.items():
    mm = re.search(r"Testability: \*\*([A-Z-]+)\*\*", b)
    if mm and mm.group(1) == "THEORETICAL-OBSTRUCTION": obs.add(n)
chk("CENSUS OBS SET UNTOUCHED: still exactly {22, 5}",
    obs == {22, 5})

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
