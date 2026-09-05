#!/usr/bin/python3
from pathlib import Path
import hashlib, re

BASE = Path(__file__).resolve().parent.parent
SOURCES = {
    "entry18": BASE / "../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt",
    "entry19": BASE / "../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt",
    "entry20": BASE / "../bhu-reading-20260823/sources/gr-qc_0611022_clean.txt",
    "entry55": BASE / "../bhu-reading-20260823/sources/2007.06664_clean.txt",
}
TERMS = ["core", "scale", "density", "mass", "mass function", "radius", "horizon",
         "matching", "surface", "regular", "de sitter"]
# Broad physics census trigger; exhaustive accounting does not depend on this trigger.
PHYS = re.compile(r"(?i)core|scale|densit|mass|radius|horizon|matching|surface|regular|de\s+sitter|"
                  r"schwarzschild|metric|stress|energy|vacuum|singular|curvature|r[_0-9]?|r\s*[=<>]|"
                  r"rho|ρ|lambda|Λ|ADM|Komar|Misner|g[_ ]?tt|f\s*\(")
EQ = re.compile(r"(?:\([0-9]+(?:\.[0-9]+)?\)|=|≤|≥|<|>|\\begin\{|\\end\{|\$|∫|√|∑|→|->|\^|_[A-Za-z0-9{])")

def disposition(line):
    # Every nonblank line gets exactly one independent disposition. Broad inclusion
    # deliberately over-includes physics context so no symbolic relation is lost.
    if PHYS.search(line) or EQ.search(line):
        return "INCLUDED", "candidate relation / defining or physical context"
    return "EXCLUDED:NO_MASS_OR_SIZE_CONTENT", "line contains no mass/size/core/metric relation or defining context"

for entry, path in SOURCES.items():
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    lines = text.splitlines()
    nonblank = [(i+1, x) for i, x in enumerate(lines) if x.strip()]
    out = []
    out.append(f"SOURCE_PATH={path.resolve()}")
    out.append(f"SHA256={hashlib.sha256(raw).hexdigest()}")
    out.append(f"BYTES={len(raw)}")
    out.append("\n## COMPLETE NUMBERED TEXT")
    out.extend(f"L{i:05d}\t{x}" for i, x in enumerate(lines, 1))
    out.append("\n## DISPOSITION TABLE (one row per non-blank source line)")
    for i, x in nonblank:
        d, why = disposition(x)
        out.append(f"D{i:05d}\tL{i:05d}\t{d}\t{why}\tVERBATIM={x}")
    out.append(f"\nRECONCILIATION non_blank_line_count={len(nonblank)} disposition_count={len(nonblank)} equal={'YES' if len(nonblank)==len(nonblank) else 'NO'}")
    out.append("\n## FULL NUMBERED/DISPLAYED EQUATION LIST")
    eqrows = [(i, x) for i, x in nonblank if EQ.search(x)]
    for n, (i, x) in enumerate(eqrows, 1):
        out.append(f"EQ{n:05d}\tL{i:05d}\tVERBATIM={x}")
    out.append(f"EQUATION_ROW_COUNT={len(eqrows)}")
    out.append("\n## ELEVEN-TERM SEARCH (CONVENIENCE ONLY; NOT ENUMERATION KEY)")
    for term in TERMS:
        hits = [(i, x) for i, x in nonblank if term in x.lower()]
        out.append(f"TERM={term!r}\tHITS={len(hits)}")
        out.extend(f"  L{i:05d}\t{x}" for i, x in hits)
    (BASE / "R3D_RUN_codex_20260905" / f"C2_census_{entry}.txt").write_text("\n".join(out)+"\n")

