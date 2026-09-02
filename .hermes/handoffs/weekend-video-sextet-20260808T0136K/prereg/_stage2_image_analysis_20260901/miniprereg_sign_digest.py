#!/usr/bin/env python3
"""Compute the §17.1-17.4 signing digest of a mini-prereg file.

Preimage = the file's bytes with the single `DUHO SIGNATURE:` line replaced by
exactly b"DUHO SIGNATURE:\n"; nothing else blanked or normalized. Refuses if the
file has CRLF, lacks a trailing LF, has no or several `DUHO SIGNATURE:` lines,
or (unless --allow-blank-utc) still has an empty `SIGNATURE UTC:` line.
Usage: python3 miniprereg_sign_digest.py MINI_PREREG_GZ_TIERC_DRAFT_V7_20260902.md
"""
import sys, hashlib
def main():
    allow_blank = "--allow-blank-utc" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(paths) != 1: sys.exit("usage: miniprereg_sign_digest.py <file> [--allow-blank-utc]")
    b = open(paths[0], "rb").read()
    if b"\r" in b: sys.exit("REFUSE: CR byte present; file must be LF-only (§17.2)")
    if not b.endswith(b"\n"): sys.exit("REFUSE: file must end in LF (§17.2)")
    lines = b.split(b"\n")
    sig = [i for i, l in enumerate(lines) if l.startswith(b"DUHO SIGNATURE:")]
    if len(sig) != 1: sys.exit(f"REFUSE: expected exactly one DUHO SIGNATURE: line, found {len(sig)}")
    utc = [l for l in lines if l.startswith(b"SIGNATURE UTC:")]
    if len(utc) != 1: sys.exit(f"REFUSE: expected exactly one SIGNATURE UTC: line, found {len(utc)}")
    if utc[0].strip() == b"SIGNATURE UTC:" and not allow_blank:
        sys.exit("REFUSE: SIGNATURE UTC: is blank; fill it first (§17.1) or pass --allow-blank-utc for a preview")
    lines[sig[0]] = b"DUHO SIGNATURE:"
    pre = b"\n".join(lines)
    print(hashlib.sha256(pre).hexdigest())
main()
