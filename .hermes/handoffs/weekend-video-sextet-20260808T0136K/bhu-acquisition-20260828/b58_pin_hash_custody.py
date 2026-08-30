#!/usr/bin/env python3
"""B58 -- pin HASH custody: every sha256 the record cites corresponds to a real on-disk source file
whose content actually hashes to it. Self-computing (no seat gate: a hash is a deterministic
function of bytes).

COMPLEMENTS b44. b44 proves every cited artifact FILENAME exists on disk and is git-tracked (defect
1ah -- pins dropped by the .pdf gitignore). It does NOT check that the file's CONTENT matches the
cited hash -- a pin could be present and tracked yet silently corrupted, truncated, or replaced.
This closes that gap: for every distinct sha256 prefix cited in the record, some file in the pinned
source dirs must hash to it.

DRIFT NOTE: Elsevier stamps a per-download timestamp, so a *re-downloaded* VoR/erratum/SCOAP3 PDF
would hash differently (register: content verified by identity+numbers, not stable byte hash). The
committed/pinned copies match their recorded hash and are not re-downloaded in place, so they pass;
this check verifies the pinned copy, which is the durable artifact. A genuine MISMATCH here (a
non-drift file whose bytes no longer match the record) would be real corruption -- a finding.
"""
import re, os, hashlib
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")
SRC_DIRS = [os.path.join(ROOT, "bhu-reading-20260823/sources"),
            os.path.join(ROOT, "bhu-theory-phase3-cns-20260821/sources")]

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B58 -- pin hash custody: cited sha256 must match real file bytes"); print("=" * 98)

# distinct sha prefixes cited in the record (>=8 hex to stay collision-safe over a ~40-file corpus)
T = open(BIB).read()
prefixes = sorted(set(m.group(1).lower() for m in re.finditer(r"sha256\s*`?([0-9a-fA-F]{8,})", T)))

# hash every file in the pinned source dirs once
disk = []
for d in SRC_DIRS:
    if not os.path.isdir(d): continue
    for f in sorted(os.listdir(d)):
        p = os.path.join(d, f)
        if os.path.isfile(p):
            disk.append((f, hashlib.sha256(open(p, "rb").read()).hexdigest()))

unmatched = [pref for pref in prefixes if not any(h.startswith(pref) for _, h in disk)]
chk(f"HASH CUSTODY: all {len(prefixes)} distinct sha256 prefixes cited in the record hash-match a "
    "real file in the pinned source dirs (content integrity, not just presence)",
    unmatched == [], f"UNMATCHED (possible corruption/replacement): {unmatched}" if unmatched else "")

# spot-report the load-bearing acquired pins so the receipt names them
KEY = {"747bce6d54d4": "entry51 Poplawski PLB690 VoR", "dafedba1ce9e": "entry51 2013 erratum",
       "573ff9751cec": "entry48 Farhi-Guth KEK scan", "54269cc6f8e6": "entry22 Crossref receipt",
       "5bf7c92ddc47": "entry58 Longo abs", "2d11feddb342": "entry16 Pourhassan SCOAP3"}
present = {k: any(h.startswith(k) for _, h in disk) for k in KEY}
chk("LOAD-BEARING PINS INTACT: the acquired-this-cycle pins (entries 51/48/22/58/16) each hash-match",
    all(present.values()), f"missing: {[KEY[k] for k, v in present.items() if not v]}")

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(prefixes)} prefixes over {len(disk)} pinned files; "
      f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
