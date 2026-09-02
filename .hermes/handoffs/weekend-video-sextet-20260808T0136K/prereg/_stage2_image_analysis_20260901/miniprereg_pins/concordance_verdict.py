#!/usr/bin/env python3
"""Emit one GZ-TIERC-VERDICT-1 verdict from a sealed JSON input.

Input is one UTF-8 JSON object, read from the sole command-line path or stdin.
It has exactly these keys:

  blind_violation: boolean
  completeness_pass: boolean
  data_integrity_pass: boolean
  instrument_integrity_pass: boolean
  wrong_parity: boolean
  absolute_anchor_pass: boolean
  measurement_pass: boolean
  deterministic_pass: boolean
  objects: array of objects, each with exactly
      gz1_objid: non-negative JSON integer
      gz_label: +1 or -1
      machine_sign: +1 or -1

The objects array is the frozen eligible pair set, one row per unique
GZ1_OBJID. Its machine_sign values are the sealed repeated-measurement outputs.
Every key is mandatory. Extra keys, duplicate IDs, booleans used as integers,
missing values, malformed JSON, and any non-finite number fail closed to
DATA-INTEGRITY-FAIL. The program writes exactly one verdict token plus LF.

Split, mapping, sample-floor, estimand, and band constants are inline below.
Earlier failure flags are evaluated in section-13 precedence. A caller that
stopped before measurement still supplies the schema, using an empty objects
array; the applicable earlier failure flag then determines the verdict.
"""

import hashlib
import json
import math
import sys

ALLOWED_TOP = {
    "blind_violation", "completeness_pass", "data_integrity_pass",
    "instrument_integrity_pass", "wrong_parity", "absolute_anchor_pass",
    "measurement_pass", "deterministic_pass", "objects",
}
ALLOWED_ROW = {"gz1_objid", "gz_label", "machine_sign"}
N_MAP_MIN = 100
N_EST_MIN = 400
SPLIT_MODULUS = 5
MAP_RESIDUE = 0
MAPPING_MARGIN = 0.10
DISCORDANT_MAX = 0.30
CONCORDANT_MIN = 0.70
WILSON_Z = 1.959963984540054


def _finite_tree(value):
    if isinstance(value, float) and not math.isfinite(value):
        return False
    if isinstance(value, dict):
        return all(_finite_tree(k) and _finite_tree(v) for k, v in value.items())
    if isinstance(value, list):
        return all(_finite_tree(v) for v in value)
    return True


def _split(objid):
    # Exact §6 preimage: ASCII base-10, no sign, whitespace, or leading zero.
    preimage = str(objid).encode("ascii")
    digest_integer = int.from_bytes(hashlib.sha256(preimage).digest(), "big")
    return "map" if digest_integer % SPLIT_MODULUS == MAP_RESIDUE else "est"


def verdict(doc):
    if not isinstance(doc, dict) or set(doc) != ALLOWED_TOP or not _finite_tree(doc):
        return "DATA-INTEGRITY-FAIL"
    bool_keys = ALLOWED_TOP - {"objects"}
    if any(type(doc[k]) is not bool for k in bool_keys):
        return "DATA-INTEGRITY-FAIL"
    if type(doc["objects"]) is not list:
        return "DATA-INTEGRITY-FAIL"

    # §13 precedence, including all pre-computation gates represented here.
    if doc["blind_violation"]:
        return "VOID-BLIND-VIOLATION"
    if not doc["completeness_pass"]:
        return "COMPLETENESS-FAIL"
    if not doc["data_integrity_pass"]:
        return "DATA-INTEGRITY-FAIL"
    if not doc["instrument_integrity_pass"]:
        return "INSTRUMENT-INTEGRITY-FAIL"
    if doc["wrong_parity"]:
        return "WRONG-PARITY-REFUSAL"
    if not doc["absolute_anchor_pass"]:
        return "ABSOLUTE-ANCHOR-FAIL"

    rows = []
    seen = set()
    for row in doc["objects"]:
        if not isinstance(row, dict) or set(row) != ALLOWED_ROW:
            return "DATA-INTEGRITY-FAIL"
        objid = row["gz1_objid"]
        if type(objid) is not int or objid < 0 or objid in seen:
            return "DATA-INTEGRITY-FAIL"
        if type(row["gz_label"]) is not int or row["gz_label"] not in (-1, 1):
            return "DATA-INTEGRITY-FAIL"
        if type(row["machine_sign"]) is not int or row["machine_sign"] not in (-1, 1):
            return "MEASUREMENT-FAIL"
        seen.add(objid)
        rows.append((objid, row["gz_label"], row["machine_sign"], _split(objid)))

    n_map = sum(split == "map" for _, _, _, split in rows)
    n_est = len(rows) - n_map
    if n_map < N_MAP_MIN or n_est < N_EST_MIN:
        return "INSUFFICIENT-SAMPLE"
    if not doc["measurement_pass"]:
        return "MEASUREMENT-FAIL"
    if not doc["deterministic_pass"]:
        return "NONDETERMINISTIC-INSTRUMENT"

    map_rows = [(g, m) for _, g, m, split in rows if split == "map"]
    k_map_raw_same = sum(g == m for g, m in map_rows)
    p_map = k_map_raw_same / n_map
    d_map = abs(2.0 * p_map - 1.0)
    if d_map < MAPPING_MARGIN:
        return "UNDETERMINED-SIGN"
    orientation = 1 if p_map > 0.5 else -1

    est_rows = [(g, m) for _, g, m, split in rows if split == "est"]
    k_agree = sum(m == orientation * g for g, m in est_rows)
    p_hat = k_agree / n_est

    # §12 estimand and Wilson calculation are computed, even though only the
    # fixed §13 band token is emitted by this single-output program.
    z2 = WILSON_Z * WILSON_Z
    center = (p_hat + z2 / (2.0 * n_est)) / (1.0 + z2 / n_est)
    half = WILSON_Z / (1.0 + z2 / n_est) * math.sqrt(
        p_hat * (1.0 - p_hat) / n_est + z2 / (4.0 * n_est * n_est)
    )
    computed = (center - half, center + half, 1.0 - p_hat, abs(2.0 * p_hat - 1.0))
    if not all(math.isfinite(x) for x in computed):
        return "DATA-INTEGRITY-FAIL"
    if p_hat >= CONCORDANT_MIN:
        return "CONCORDANT"
    if p_hat <= DISCORDANT_MAX:
        return "DISCORDANT"
    return "INTERMEDIATE-CONCORDANCE"


def main():
    try:
        if len(sys.argv) > 2:
            raise ValueError("at most one input path")
        if len(sys.argv) == 2:
            with open(sys.argv[1], "r", encoding="utf-8") as handle:
                doc = json.load(handle)
        else:
            doc = json.load(sys.stdin)
        answer = verdict(doc)
    except Exception:
        answer = "DATA-INTEGRITY-FAIL"
    sys.stdout.write(answer + "\n")


if __name__ == "__main__":
    main()
