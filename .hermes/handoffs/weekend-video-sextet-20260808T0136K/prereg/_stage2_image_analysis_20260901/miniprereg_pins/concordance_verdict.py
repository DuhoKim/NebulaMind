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
  prereg_sha256, sample_manifest_sha256, brick_manifest_sha256,
  instrument_sha256, journal_head_sha256: lowercase SHA-256 hex strings
  objects: array of objects, each with exactly
      gz1_objid: non-negative JSON integer
      gz_label: +1 or -1
      machine_sign: +1 or -1

The objects array is the frozen eligible pair set, one row per unique
GZ1_OBJID. Its machine_sign values are the sealed repeated-measurement outputs.
Every key is mandatory. Extra keys, duplicate IDs, booleans used as integers,
missing values, malformed JSON, and any non-finite number fail closed to
DATA-INTEGRITY-FAIL. The program writes exactly one canonical JSON verdict
block plus LF, with the closed field set in preregistration section 16.7.

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
    "prereg_sha256", "sample_manifest_sha256", "brick_manifest_sha256",
    "instrument_sha256", "journal_head_sha256",
}
ALLOWED_ROW = {"gz1_objid", "gz_label", "machine_sign"}
DIGEST_KEYS = (
    "prereg_sha256", "sample_manifest_sha256", "brick_manifest_sha256",
    "instrument_sha256", "journal_head_sha256",
)
VERDICT_KEYS = {
    "schema_version", "verdict", "n_map", "k_map_raw_same", "p_map",
    "mapping", "mapping_strength", "n_est", "k_agree", "p_agree",
    "wilson95_low", "wilson95_high", "q_disagree", "q_wilson95_low",
    "q_wilson95_high", "robustness", *DIGEST_KEYS,
}
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


def _block(answer="DATA-INTEGRITY-FAIL", digests=None):
    block = {key: None for key in VERDICT_KEYS}
    block["schema_version"] = "GZ-TIERC-VERDICT-1"
    block["verdict"] = answer
    if digests is not None:
        for key in DIGEST_KEYS:
            block[key] = digests[key]
    return block


def _terminal(block, answer):
    block["verdict"] = answer
    return block


def verdict(doc):
    if not isinstance(doc, dict) or set(doc) != ALLOWED_TOP or not _finite_tree(doc):
        return _block()
    bool_keys = ALLOWED_TOP - {"objects", *DIGEST_KEYS}
    if any(type(doc[k]) is not bool for k in bool_keys):
        return _block()
    if type(doc["objects"]) is not list:
        return _block()
    if any(type(doc[k]) is not str or len(doc[k]) != 64 or
           any(c not in "0123456789abcdef" for c in doc[k]) for k in DIGEST_KEYS):
        return _block()

    block = _block(digests=doc)

    # §13 precedence, including all pre-computation gates represented here.
    if doc["blind_violation"]:
        return _terminal(block, "VOID-BLIND-VIOLATION")
    if not doc["completeness_pass"]:
        return _terminal(block, "COMPLETENESS-FAIL")
    if not doc["data_integrity_pass"]:
        return block
    if not doc["instrument_integrity_pass"]:
        return _terminal(block, "INSTRUMENT-INTEGRITY-FAIL")
    if doc["wrong_parity"]:
        return _terminal(block, "WRONG-PARITY-REFUSAL")
    if not doc["absolute_anchor_pass"]:
        return _terminal(block, "ABSOLUTE-ANCHOR-FAIL")

    rows = []
    seen = set()
    for row in doc["objects"]:
        if not isinstance(row, dict) or set(row) != ALLOWED_ROW:
            return _block(digests=doc)
        objid = row["gz1_objid"]
        if type(objid) is not int or objid < 0 or objid in seen:
            return _block(digests=doc)
        if type(row["gz_label"]) is not int or row["gz_label"] not in (-1, 1):
            return _block(digests=doc)
        if type(row["machine_sign"]) is not int or row["machine_sign"] not in (-1, 1):
            return _terminal(block, "MEASUREMENT-FAIL")
        seen.add(objid)
        rows.append((objid, row["gz_label"], row["machine_sign"], _split(objid)))

    n_map = sum(split == "map" for _, _, _, split in rows)
    n_est = len(rows) - n_map
    block["n_map"] = n_map
    block["n_est"] = n_est
    if n_map < N_MAP_MIN or n_est < N_EST_MIN:
        return _terminal(block, "INSUFFICIENT-SAMPLE")
    if not doc["measurement_pass"]:
        return _terminal(block, "MEASUREMENT-FAIL")
    if not doc["deterministic_pass"]:
        return _terminal(block, "NONDETERMINISTIC-INSTRUMENT")

    map_rows = [(g, m) for _, g, m, split in rows if split == "map"]
    k_map_raw_same = sum(g == m for g, m in map_rows)
    p_map = k_map_raw_same / n_map
    d_map = abs(2.0 * p_map - 1.0)
    block.update(k_map_raw_same=k_map_raw_same, p_map=p_map,
                 mapping_strength=d_map)
    if d_map < MAPPING_MARGIN:
        return _terminal(block, "UNDETERMINED-SIGN")
    orientation = 1 if p_map > 0.5 else -1
    block["mapping"] = "SAME" if orientation == 1 else "INVERTED"

    est_rows = [(g, m) for _, g, m, split in rows if split == "est"]
    k_agree = sum(m == orientation * g for g, m in est_rows)
    p_hat = k_agree / n_est

    # §12 estimand and Wilson calculation populate the closed verdict block.
    z2 = WILSON_Z * WILSON_Z
    center = (p_hat + z2 / (2.0 * n_est)) / (1.0 + z2 / n_est)
    half = WILSON_Z / (1.0 + z2 / n_est) * math.sqrt(
        p_hat * (1.0 - p_hat) / n_est + z2 / (4.0 * n_est * n_est)
    )
    low = center - half
    high = center + half
    q_hat = 1.0 - p_hat
    robustness = abs(2.0 * p_hat - 1.0)
    computed = (low, high, q_hat, robustness)
    if not all(math.isfinite(x) for x in computed):
        return _block(digests=doc)
    block.update(k_agree=k_agree, p_agree=p_hat, wilson95_low=low,
                 wilson95_high=high, q_disagree=q_hat,
                 q_wilson95_low=1.0 - high, q_wilson95_high=1.0 - low,
                 robustness=robustness)
    if p_hat >= CONCORDANT_MIN:
        return _terminal(block, "CONCORDANT")
    if p_hat <= DISCORDANT_MAX:
        return _terminal(block, "DISCORDANT")
    return _terminal(block, "INTERMEDIATE-CONCORDANCE")


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
        answer = _block()
    sys.stdout.write(json.dumps(answer, sort_keys=True, separators=(",", ":"),
                                allow_nan=False) + "\n")


if __name__ == "__main__":
    main()
