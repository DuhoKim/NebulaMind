#!/usr/bin/env python3
"""R3I validator (black-hole referent census). Usage: r3i_validate.py <referent_ledger.json> <sources_dir>
Ledger: {"records":[{"text_file","referent","quotation","source_line","secondary":[...]}]}. Referent set (alphabetical):
COSMOLOGICAL_INTERIOR | REGULAR_CORE | SINGULAR_HORIZON | UNDECLARED. UNDECLARED needs no quotation; every other referent needs a
quotation that is a verbatim (normalised) substring of the cited line of the named file. Prints C1_SOURCE_IDENTITY and exits 1 on FAIL."""
import sys, json, pathlib
from r3_controls_lib import normalise, chk, token, finish
REF = {"COSMOLOGICAL_INTERIOR", "REGULAR_CORE", "SINGULAR_HORIZON", "UNDECLARED"}
def main(ledger, sources):
    L = json.load(open(ledger)); ok_all = True
    for rec in L["records"]:
        f = pathlib.Path(sources) / rec["text_file"]; ref = rec.get("referent")
        if ref not in REF: chk(f"{rec['text_file']}: referent {ref!r} in set", False); ok_all = False; continue
        if ref == "UNDECLARED":
            chk(f"{rec['text_file']}: UNDECLARED carries no quotation", not rec.get("quotation")); ok_all &= not rec.get("quotation"); continue
        if not f.exists(): chk(f"{rec['text_file']}: file exists", False); ok_all = False; continue
        lines = f.read_text(encoding="utf-8", errors="replace").split("\n"); ln = rec.get("source_line", 0)
        raw = lines[ln-1] if 0 < ln <= len(lines) else ""
        ok = bool(rec.get("quotation")) and normalise(rec["quotation"]) in normalise(raw)
        chk(f"{rec['text_file']} L{ln} {ref}: quotation is a verbatim substring", ok); ok_all &= ok
    token("C1_SOURCE_IDENTITY", ok_all)
if __name__ == "__main__":
    if len(sys.argv) != 3: print(__doc__); sys.exit(2)
    main(sys.argv[1], sys.argv[2]); finish()
