"""Deterministic selection from three digest-pinned ASCII ID lists.

All inputs contain one canonical nonnegative decimal GZ1_OBJID per line.
Eligibility must be strictly ascending; exclusion/failed lists are unordered sets.
Empty files represent empty sets. A final newline is optional.
"""

import hashlib
from pathlib import Path
import re


def _read_ids(path, expected, name, ascending=False):
    if not isinstance(expected, str) or re.fullmatch(r"[0-9a-fA-F]{64}", expected) is None:
        raise ValueError(f"{name}: malformed expected SHA256")
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != expected.lower():
        raise ValueError(f"{name}: SHA256 mismatch: expected {expected.lower()}, got {digest}")
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeDecodeError as exc:
        raise ValueError(f"{name}: malformed ASCII ID file") from exc
    ids = []
    for line_number, line in enumerate(lines, 1):
        if re.fullmatch(r"0|[1-9][0-9]*", line) is None:
            raise ValueError(f"{name}: malformed GZ1_OBJID on line {line_number}")
        objid = int(line)
        if ascending and ids and objid <= ids[-1]:
            raise ValueError(f"{name}: IDs must be ascending without duplicates (line {line_number})")
        ids.append(objid)
    return ids, digest


def select(eligible_ids_path, eligible_sha256, exclusion_path, exclusion_sha256,
           failed_set_path, failed_sha256, seed_hex,
           sizes=(400, 200, 2000)):
    """Return ordered splits, normalized seed, verified digests and input/split counts.

    Counts include unique exclusion/failed nonmembers of eligibility; these are
    retained history, not input errors.
    Draw exactly the requested sizes or raise with the split's shortfall in
    the eligible population after exclusions and earlier split allocations.
    """
    eligible, eligible_digest = _read_ids(eligible_ids_path, eligible_sha256, "eligible", True)
    excluded, exclusion_digest = _read_ids(exclusion_path, exclusion_sha256, "exclusion")
    failed, failed_digest = _read_ids(failed_set_path, failed_sha256, "failed")
    if not isinstance(seed_hex, str) or re.fullmatch(r"[0-9a-fA-F]{64}", seed_hex) is None:
        raise ValueError("seed_hex must contain exactly 64 hexadecimal characters")
    seed = seed_hex.lower()
    if len(sizes) != 3 or any(type(n) is not int or n < 0 for n in sizes):
        raise ValueError("sizes must be three nonnegative integers")
    excluded, failed = set(excluded), set(failed)
    overlap = excluded & failed
    if overlap:
        raise ValueError("exclusion/failed overlap: " + ", ".join(map(str, sorted(overlap))))
    eligible_set = set(eligible)
    # Historical lists are global; eligibility is already renderability-qualified.
    exclusion_nonmembers = len(excluded - eligible_set)
    failed_nonmembers = len(failed - eligible_set)
    survivors = [objid for objid in eligible if objid not in excluded | failed]

    def rank(objid):
        digest = hashlib.sha256(f"{seed}||{objid}".encode("ascii")).digest()
        return int.from_bytes(digest, "big") % (2 ** 32), objid

    survivors.sort(key=rank)
    names = ("tuning", "holdout", "validation")
    result = {}
    offset = 0
    for name, size in zip(names, sizes):
        available = len(survivors) - offset
        if available < size:
            raise ValueError(f"{name} draw size shortfall: {size - available} "
                             f"(eligible population after exclusions {len(survivors)}, "
                             f"remaining {available}, requested {size})")
        result[name] = survivors[offset:offset + size]
        offset += size
    result["seed"] = seed
    result["digests"] = {"eligible": eligible_digest, "exclusion": exclusion_digest,
                         "failed": failed_digest}
    result["counts"] = {"eligible": len(eligible), "exclusion": len(excluded),
                        "failed": len(failed), "removed": len(eligible) - len(survivors),
                        "survivors": len(survivors),
                        "exclusion_nonmembers": exclusion_nonmembers,
                        "failed_nonmembers": failed_nonmembers,
                        **{name: len(result[name]) for name in names}}
    return result
