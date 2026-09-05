#!/usr/bin/env python3
# C2 census builder — R3D kimi seat, 2026-09-05.
# Reads the four pinned manifest sources, prints for each:
#   PART 1: complete extracted text with stable line numbers (blank lines marked)
#   PART 2: disposition of every non-blank line (INCLUDED row / excluded under a
#           predeclared reason code / DUPLICATE naming the covering row)
#   PART 3: reconciliation line (non-blank lines == assigned dispositions)
#   PART 4: full list of numbered/displayed equations, each its own census row
#   plus the eleven-term search output (convenience only, per §2c).
# Disposition tables are authored by the seat in census_tables.py.
import os, sys, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from census_tables import SOURCES, ROWS, EQLIST

BASE = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K"
OUT = os.path.join(BASE, "bhu-acquisition-20260828", "R3D_RUN_kimi_20260905")
TERMS = ["core", "scale", "density", "mass", "mass function", "radius",
         "horizon", "matching", "surface", "regular", "de Sitter"]

CODE_NAME = {"INC": "INCLUDED", "WB": "WRONG_BRANCH", "DEF": "DEFINITION_ONLY",
             "NOM": "NO_MASS_OR_SIZE_CONTENT", "DUP": "DUPLICATE"}

def sha256(b):
    return hashlib.sha256(b).hexdigest()

def build(entry):
    src = SOURCES[entry]
    path = os.path.join(BASE, src["rel"])
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8", errors="replace")
    # stable line numbering: split on \n; a trailing newline produces a final empty field
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]  # conventional final newline: not a line of its own
    n = len(lines)
    nonblank = [i + 1 for i, ln in enumerate(lines) if ln.strip() != ""]
    rows = ROWS[entry]
    # assign dispositions
    disp = {}
    errors = []
    for (lo, hi, code, rid, demo) in rows:
        if code not in CODE_NAME:
            errors.append(f"bad code {code} in row {rid}")
        for ln in range(lo, hi + 1):
            if ln > n:
                errors.append(f"row {rid} covers line {ln} beyond EOF ({n})")
                continue
            if lines[ln - 1].strip() == "":
                continue  # blank lines carry no disposition
            if ln in disp:
                errors.append(f"line {ln} covered twice (rows {disp[ln][0]} and {rid})")
            disp[ln] = (rid, code, demo, lo, hi)
    for ln in nonblank:
        if ln not in disp:
            errors.append(f"line {ln} (non-blank) has NO disposition: {lines[ln-1]!r:.80}")
    # equation list check: every eq row's covering block exists
    out = []
    out.append(f"C2 CENSUS — manifest entry {entry}: {src['paper']}")
    out.append(f"source path (relative to protocol): {src['rel']}")
    out.append(f"absolute path: {path}")
    out.append(f"sha256 of raw bytes (computed this run): {sha256(raw)}")
    out.append(f"pinned sha256 (§2a):                    {src['sha']}")
    out.append(f"match: {sha256(raw) == src['sha']}")
    out.append("")
    out.append("CONVENTIONS (stated so the second seat applies the same rule):")
    out.append(" - Every non-blank line is assigned exactly one disposition. Blank lines are")
    out.append("   printed in PART 1 marked BLANK and carry no disposition.")
    out.append(" - An equation and its defining/context lines form one bounded block; the")
    out.append("   block's line range is printed. Within a range, each non-blank line is")
    out.append("   individually assigned that row's disposition (see PART 2).")
    out.append(" - INCLUDED = the line asserts (or forms part of) a relation, condition or")
    out.append("   property bearing on core scale, density, mass, mass function, radius,")
    out.append("   horizon, matching surface, regularity, or the de Sitter limit.")
    out.append(" - WRONG_BRANCH = the line asserts such a relation for a DIFFERENT")
    out.append("   construction than the Dymnikova regular-core metrics (demonstrated by")
    out.append("   the quoted branch marker in the source text).")
    out.append(" - NO_MASS_OR_SIZE_CONTENT = the line asserts no such relation (headers,")
    out.append("   furniture, history, motivation, roadmap, bibliographic citations — a")
    out.append("   citation identifies an external work and asserts no relation here).")
    out.append(" - DEFINITION_ONLY = pure notation/definition with no relational content.")
    out.append(" - DUPLICATE = repeated text; the covering row is named.")
    out.append(" - The eleven terms are printed as a convenience search only; no row is")
    out.append("   justified by them.")
    out.append("")
    out.append("=" * 78)
    out.append("PART 1 — COMPLETE EXTRACTED TEXT WITH STABLE LINE NUMBERS")
    out.append("=" * 78)
    for i, ln in enumerate(lines):
        tag = "" if ln.strip() else "   [BLANK]"
        out.append(f"{i+1:>5}| {ln}{tag}")
    out.append("")
    out.append("=" * 78)
    out.append("PART 2 — DISPOSITION OF EVERY NON-BLANK LINE")
    out.append("=" * 78)
    seen_demo = set()
    for ln in nonblank:
        rid, code, demo, lo, hi = disp[ln]
        first = "  <-- " + (f"row {rid} [{CODE_NAME[code]}] (lines {lo}-{hi}): {demo}" if ln == lo else "")
        if ln == lo and rid in seen_demo:
            first = f"  <-- row {rid} (continued)"
        if ln == lo:
            seen_demo.add(rid)
        out.append(f"{ln:>5}| {rid:<9} {CODE_NAME[code]:<24}{first}")
    out.append("")
    out.append("=" * 78)
    out.append("PART 3 — RECONCILIATION")
    out.append("=" * 78)
    out.append(f"non-blank line count      : {len(nonblank)}")
    out.append(f"assigned disposition count: {len(disp)}")
    out.append(f"equal: {len(nonblank) == len(disp)}")
    out.append("")
    out.append("=" * 78)
    out.append("PART 4 — FULL EQUATION LIST (each numbered/displayed equation its own row)")
    out.append("=" * 78)
    for (eqlab, loc, cover, note) in EQLIST[entry]:
        out.append(f"  eq {eqlab:<10} lines {loc:<12} census row {cover:<9} {note}")
    out.append("")
    out.append("=" * 78)
    out.append("ELEVEN-TERM SEARCH (convenience only; not the enumeration key)")
    out.append("=" * 78)
    low = [ln.lower() for ln in lines]
    for t in TERMS:
        hits = [i + 1 for i, ln in enumerate(low) if t.lower() in ln and lines[i].strip()]
        out.append(f"  term {t!r:<16}: {len(hits)} lines: {hits[:60]}{' ...' if len(hits) > 60 else ''}")
    out.append("")
    if errors:
        out.append("!!! TABLE ERRORS:")
        out.extend("  " + e for e in errors)
    return "\n".join(out) + "\n", errors, len(nonblank), len(disp)

def main():
    allerr = {}
    for entry in ["18", "19", "20", "55"]:
        text, errors, nnb, ndisp = build(entry)
        fn = os.path.join(OUT, f"C2_census_entry{entry}.txt")
        with open(fn, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"entry {entry}: non-blank={nnb} dispositions={ndisp} errors={len(errors)} -> {fn}")
        if errors:
            allerr[entry] = errors
    if allerr:
        for e, errs in allerr.items():
            print(f"--- entry {e} errors (first 40):")
            for x in errs[:40]:
                print("   ", x)
        sys.exit(1)
    print("RECONCILIATION OK for all four sources.")

if __name__ == "__main__":
    main()
