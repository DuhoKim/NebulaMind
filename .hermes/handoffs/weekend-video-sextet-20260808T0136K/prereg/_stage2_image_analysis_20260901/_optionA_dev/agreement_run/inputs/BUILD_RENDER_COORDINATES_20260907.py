#!/Library/Developer/CommandLineTools/usr/bin/python3
"""Reproduce the permitted, label-free coordinate projection; never select.
Known numeric prefixes only; the label suffix is neither decoded nor emitted.
Existing output bytes are compared, never overwritten. No network or pixels.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shlex
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
INTERPRETER = "/Library/Developer/CommandLineTools/usr/bin/python3"
SOURCES = {
    "_optionA_dev/corpus_identity/guarded_pool.csv": "2cc94a29562270fcb5043f4ce942e303696f359b5fb0c59fdee48578ebb34155",
    "scratch/survey-bricks-dr9-north.fits.gz": "2edd5c295fdad26852c6f224a3ff023cff43dd0e03a53acd35b767e726ee72fb",
    "validation_bricks/_bricks_without_r_coverage.txt": "ba2eb9d16d0d1d47eef2e0d52497b56d44ac979ebe67dd54b33f57c117d7a2fe",
    "_optionA_dev/agreement_run/inputs/eligible_ids_20260907.txt": "15f34e4ef21b47a5393786a404ecc45aa07f347d548c4811fcc92932a258611d",
}
OUTPUT = HERE / "render_coordinates_20260907.json"
RECEIPT = HERE / "RENDER_COORDINATES_RECEIPT_20260907.md"

def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return h.hexdigest()

def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")

def project(path):
    with Path(path).open("rb") as stream:
        if stream.readline().rstrip(b"\r\n") != b"GZ1_OBJID,RA,DEC,G":
            raise ValueError("Unexpected coordinate source header")
        for raw in stream:
            fields = []
            for _ in range(3):
                field, comma, raw = raw.partition(b",")
                if not comma or not field or b'"' in field:
                    raise ValueError("Malformed numeric prefix")
                fields.append(field.decode("ascii"))
            del raw  # Do not decode, parse, log, or retain the label suffix.
            if not re.fullmatch(r"[1-9][0-9]*", fields[0]):
                raise ValueError("Noncanonical identity")
            ra, dec = float(fields[1]), float(fields[2])
            if not (math.isfinite(ra) and math.isfinite(dec) and
                    0 <= ra < 360 and -90 <= dec <= 90):
                raise ValueError("Coordinate range")
            yield int(fields[0]), ra, dec

def matching(ra, dec, ra1, ra2, dec1, dec2):
    import numpy as np
    return np.flatnonzero(
        np.where(ra1 <= ra2, (ra1 <= ra) & (ra < ra2),
                 (ra1 <= ra) | (ra < ra2)) & (dec1 <= dec) & (dec < dec2))

def build():
    if sys.executable != INTERPRETER or not sys.dont_write_bytecode or os.environ.get(
            "PYTHONPATH") != str(ROOT / "_optionA_dev/_venv_bls/lib/python3.9/site-packages"):
        raise RuntimeError("Use the pinned interpreter and documented environment")
    import numpy as np
    from astropy.io import fits
    import astropy
    observed = {p: digest(ROOT / p) for p in SOURCES}
    if observed != SOURCES:
        raise RuntimeError("Source digest mismatch")
    raw_ids = (ROOT / "_optionA_dev/agreement_run/inputs/eligible_ids_20260907.txt").read_bytes()
    lines = raw_ids.decode("ascii").splitlines()
    if any(not re.fullmatch(r"[1-9][0-9]*", v) for v in lines):
        raise ValueError("Eligible identity syntax")
    eligible = [int(v) for v in lines]
    if eligible != sorted(set(eligible)) or len(eligible) != 11837:
        raise ValueError("Eligible count/order/uniqueness")
    registry_rows = (ROOT / "validation_bricks/_bricks_without_r_coverage.txt").read_text("ascii").splitlines()
    if any(not re.fullmatch(r"[0-9]{4}[pm][0-9]{3}", v) for v in registry_rows):
        raise ValueError("Registry syntax")
    no_r = set(registry_rows)
    with fits.open(ROOT / "scratch/survey-bricks-dr9-north.fits.gz", memmap=False) as hdus:
        table = hdus[1].data
        names = [str(v).strip() for v in table["brickname"]]
        bounds = [np.asarray(table[c], dtype=np.float64).copy()
                  for c in ("ra1", "ra2", "dec1", "dec2")]
    if not all(np.isfinite(a).all() for a in bounds) or any(
            not re.fullmatch(r"[0-9]{4}[pm][0-9]{3}", v) for v in names):
        raise ValueError("Brick metadata syntax")
    seen, qualified, after_brick = set(), {}, 0
    for oid, ra, dec in project(ROOT / "_optionA_dev/corpus_identity/guarded_pool.csv"):
        if oid in seen:
            raise ValueError("Duplicate source identity")
        seen.add(oid)
        hits = matching(ra, dec, *bounds)
        if len(hits) > 1:
            raise ValueError("Ambiguous brick assignment")
        if not len(hits):
            continue
        after_brick += 1
        brick = names[int(hits[0])]
        if brick not in no_r:
            qualified[oid] = {"objid": oid, "ra": ra, "dec": dec, "brick": brick}
    if sorted(qualified) != eligible:
        raise ValueError("Derived membership differs from pinned eligible IDs")
    counts = {
        "survey_bricks": len(names), "no_r_rows": len(registry_rows), "no_r_unique": len(no_r),
        "coordinate_prefix_rows": len(seen), "unique_coordinate_ids": len(seen),
        "after_half_open_brick": after_brick, "without_brick": len(seen)-after_brick,
        "after_no_r": len(qualified), "removed_no_r": after_brick-len(qualified),
        "eligible_rows": len(eligible), "eligible_missing_coordinates": 0,
        "qualified_not_eligible": 0, "output_rows": len(eligible),
    }
    if (len(names), len(no_r), len(seen), after_brick, len(qualified)) != (93548, 4, 12054, 11841, 11837):
        raise ValueError("Pinned derivation counts changed")
    if {p: digest(ROOT / p) for p in SOURCES} != observed:
        raise RuntimeError("Inputs changed while producing coordinates")
    payload = canonical([qualified[oid] for oid in eligible])
    command = ('PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$PWD/_optionA_dev/_venv_bls/lib/python3.9/site-packages" '
               + INTERPRETER + " " + shlex.quote(str(Path(__file__).relative_to(ROOT))))
    fence = chr(96) * 3
    lines = [
        "# Render-coordinate derivation receipt — 2026-09-07", "",
        "Label-free authoring only. Numeric GZ1_OBJID/RA/DEC prefixes of the already pinned "
        "guarded pool supply positions; IDs and brick boundaries alone cannot supply galaxy positions. "
        "The source is hashed opaquely and its label suffix is never decoded, parsed, displayed or emitted. "
        "No pixels, failed-source CSV, historical V15–V34 file, ranking, seed, draw or access stage is read or run.", "",
        "Procedure: binary64 dec1 <= DEC < dec2; nonwrapping ra1 <= RA < ra2; "
        "wrapping RA >= ra1 OR RA < ra2. Multiple matches stop. Exclude no-r bricks, "
        "require exact equality with pinned eligible membership, then emit numeric ID order. "
        "No checksum/exposure lookup or historical exclusion subtraction.", "",
        "## Command", "", "Run from the lane root:", "", fence+"sh", command, fence, "",
        "Existing outputs are recomputed and byte-compared without overwriting. JSON bytes use sorted keys, "
        "compact separators, finite numbers, UTF-8 and one terminal LF; no timestamp enters the output.", "",
        "## Row counts", "", fence+"json", json.dumps(counts, indent=2, sort_keys=True), fence, "",
        "## Actual data-input pins", "", "| Path | SHA-256 |", "|---|---|",
    ]
    lines += ["| \x60%s\x60 | \x60%s\x60 |" % (p, h) for p, h in sorted(observed.items())]
    lines += [
        "", "## Producer, output and runtime", "",
        "Producer SHA-256: \x60%s\x60." % digest(Path(__file__)),
        "Coordinate JSON SHA-256: \x60%s\x60; bytes: %d." % (hashlib.sha256(payload).hexdigest(), len(payload)),
        "Interpreter: \x60%s\x60; SHA-256: \x60%s\x60." % (INTERPRETER, digest(INTERPRETER)),
        "Python %s; NumPy %s; Astropy %s." % (sys.version.split()[0], np.__version__, astropy.__version__),
        "Package files are covered by the separate runtime inventory, not claimed by the four-data-input table.",
        "Receipt full-byte SHA-256 is printed after creation and retained in the v42 report; no self-digest is invented.", "",
    ]
    return payload, "\n".join(lines).encode("utf-8"), counts

def main():
    payload, receipt, counts = build()
    targets = ((OUTPUT, payload), (RECEIPT, receipt))
    for path, data in targets:
        if path.exists() and path.read_bytes() != data:
            raise FileExistsError("Refusing to change existing output: " + str(path))
    for path, data in targets:
        if not path.exists():
            with path.open("xb") as stream:
                stream.write(data)
        print(json.dumps({"path": str(path.relative_to(ROOT)), "sha256": digest(path), "bytes": len(data)}))
    print(json.dumps(counts, sort_keys=True))

if __name__ == "__main__":
    main()
