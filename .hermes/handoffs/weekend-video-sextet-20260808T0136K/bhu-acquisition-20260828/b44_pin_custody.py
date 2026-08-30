#!/usr/bin/env python3
"""B44 -- pin custody: every artifact the record cites must actually be IN the repository.

THE DEFECT (register 1ah). The shared .gitignore takes the whole .hermes tree and re-admits by
extension (.md .json .txt .html .yaml .yml .py .tex) -- NOT .pdf. So every PDF pin the record
cites was silently ignored: present on this disk, absent from every fresh clone. NINE pins were
disk-only when this control was built (2026-08-30), including:
  - entry 44's arXiv PDF from THIS MORNING's "two-artifact repair" (d551b99e4) -- the commit
    shipped the sweep and the record, and git dropped the artifact itself;
  - entry 57's ARMA paper -- the source both B32 seats read "in full, all 39 PDF pages";
  - entry 49's Blau-Guendelman-Guth, entry 6's Smolin 1992, entry 31's Smolin 2004, the
    Rothman-Ellis pair, Smoller-Temple 2000, and entry 32's new ADS scan.
All nine were force-added (git add -f, targeted -- the shared ignore rule stays untouched
because other lanes depend on it) in the same commit as this control.

DISCOVERY HONESTY. Found while pinning entry 32's scan (the fresh pin's check-ignore hit).
The first sweep pattern -- backticked ../-relative paths -- caught 6 pins and MISSED the class
of bare backticked filenames; widening to all backticked artifact filenames caught 17 and still
missed the class cited WITHOUT backticks (entry 44's `1309.1487.pdf` -- verified untracked by
direct git ls-files, not by the pattern). This control therefore takes BOTH routes: the
backticked-filename sweep AND an explicit list of known non-backticked pins. One class it still
misses: an artifact cited by prose description with no filename at all; nothing mechanical can
enumerate those, and the reading notes are the fallback.

RULE: for every cited artifact filename that exists anywhere in the handoff tree, at least one
on-disk copy must be git-tracked. (Basename collisions across dirs are resolved permissively --
ANY tracked copy passes -- and that weakness is stated here rather than hidden.)
"""
import re, os, subprocess
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))          # the handoff tree
REPO = os.path.abspath(os.path.join(ROOT, "../.."))        # repo root
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B44 -- pin custody: cited artifacts must survive a fresh clone"); print("=" * 98)

T = open(BIB).read()
cited = sorted(set(os.path.basename(m.group(1)) for m in
                   re.finditer(r"`([^`\s]+?\.(?:pdf|txt|html|json|tex))`", T)))
cited = [b for b in cited if "*" not in b]                  # prose globs are not filenames
KNOWN_UNBACKTICKED = ["1309.1487.pdf"]                      # entry 44's pin, cited in prose
for b in KNOWN_UNBACKTICKED:
    if b not in cited: cited.append(b)

idx = {}
for root, dirs, files in os.walk(ROOT):
    if "venv" in root or "node_modules" in root: continue
    for f in files:
        idx.setdefault(f, []).append(os.path.join(root, f))

missing_disk, untracked, tracked = [], [], 0
for b in sorted(cited):
    hits = idx.get(b, [])
    if not hits:
        missing_disk.append(b); continue
    if any(subprocess.run(["git", "-C", REPO, "ls-files", "--error-unmatch", os.path.relpath(h, REPO)],
                          capture_output=True).returncode == 0 for h in hits):
        tracked += 1
    else:
        untracked.append(b)

print(f"\n  cited artifact filenames : {len(cited)} (backticked sweep + {len(KNOWN_UNBACKTICKED)} known prose-cited)")
print(f"  tracked                  : {tracked}")
print(f"  missing on disk          : {missing_disk if missing_disk else 'none'}")
print(f"  on disk but untracked    : {untracked if untracked else 'none'}")

chk("CUSTODY: every cited artifact that exists on disk is git-tracked -- the nine disk-only "
    "pins of 2026-08-30 are in the repository",
    untracked == [] and tracked == len(cited) - len(missing_disk) and tracked >= 17)
chk("DISK: no cited artifact is missing from the tree entirely",
    missing_disk == [])

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
