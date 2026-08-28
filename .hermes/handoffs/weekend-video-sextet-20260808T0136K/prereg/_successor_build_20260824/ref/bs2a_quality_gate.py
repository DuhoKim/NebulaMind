#!/usr/bin/env python3
"""BS-2a — the catalogue-quality exclusion predicate, its evidence schema, and its verifier.

WHAT THIS IS
------------
Candidate code for the next atomic revision. `successor_ref_v9.py` is FROZEN and this file does not
touch it. BS-2a is DESIGN, defined, UNFILLED in V29 §7; filling it needs exactly this: the frozen
predicate as code, an authenticated evidence schema, a verifier that can reject a non-conforming
receipt, and fixtures that prove each check can fail.

THE PREDICATE, from V29 §2.7(7) — absolute values, not percentiles
-----------------------------------------------------------------
    flux_ivar_r  >  8.4000532
    psfsize_r    <  1.5699703
    nobs_r       >= 3

A percentile is a function of whatever sample computes it; an absolute number is not. These were
derived once from the 65,060-object pre-cut sample and frozen before any image byte, which is what
makes the predicate preregistered rather than chosen.

WHAT IS AND IS NOT CLAIMED
--------------------------
These three columns were measured by the DESI survey before this study existed, so the predicate is
**outcome-blind with respect to this study's unobserved χ**: it cannot be tuned post hoc.

It is NOT claimed to be statistically independent of handedness. Both referee seats refuted that
argument on 2026-08-28: chronology establishes only that this study's later output did not *cause*
the earlier catalogue values. `corr(psfsize_r, cos θ) = +0.3659`, and the Longo hypothesis is that
handedness correlates with position on that axis. Whether the predicate is independent of handedness
*conditional on position* — the property the dipole estimator needs — is **not established**. This
module implements the predicate; it does not resolve that question, and no docstring here should be
read as resolving it.

WHAT THE VERIFIER BINDS, AND WHAT IT DOES NOT
---------------------------------------------
Round 2 found that a receipt could name the frozen parent while carrying evidence for a *different*
65,060 objects: cardinality and key uniqueness are not set equality. So the contract is now pinned to
three frozen commitments over the authenticated bytes — the parent key set (E20), the full evidence
(E23), and the retained count (E22). A hand-made receipt/evidence pair cannot satisfy those without
being the authenticated evidence.

This binds the receipt to specific bytes. It does not make the *predicate* independent of
handedness, and E23 matching is not evidence about the science — only about custody.

WHY THE CONTROLS LOOK LIKE THIS
-------------------------------
Round 1: controls asserted that *some* refusal fired, so a surviving guard masked a deleted one.
Round 2: controls asserted a refusal *substring*, and `n_parent`/`n_joined` occur in several
branches — so deleting any of three closure checks still left the battery green. Both defects are
the same shape: the control accepted a superset of what it meant.

So a control now declares the EXACT SET of refusal codes its mutation must produce. Deleting a check
removes a code from the set; adding a spurious refusal adds one; either way the set differs and the
control fails. `uncontrolled()` then computes which codes no control exercises, rather than a
comment claiming coverage.

The fixture is the real authenticated evidence, not a synthetic stand-in, so no check needs relaxing
for it and there is exactly one code path. `--self-test` therefore requires the source CSVs.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import stat
import sys
from pathlib import Path

# ── Frozen constants. Changing any of these is a threshold change and voids the run. ────────────
T_FLUX_IVAR_R_GT = 8.4000532
T_PSFSIZE_R_LT = 1.5699703
T_NOBS_R_GE = 3.0

QUALITY_SHA256 = "61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3"
PARENT_SHA256 = "425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831"
PARENT_ROWS = 65_060
EXPECTED_RETAINED = 49_211

# Commitments over the authenticated bytes, computed once from the sources above. These are what
# make membership — not merely cardinality — checkable by a standalone verifier.
PARENT_KEYSET_SHA256 = "550e50a8c6fbea2a72ac93597b8c0fbc6798fc78172a5056f10329d7dde93bd6"
EVIDENCE_SHA256 = "0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca"

JOIN_KEYS = ("brickid", "objid")
QUALITY_COLUMNS = ("flux_ivar_r", "psfsize_r", "nobs_r")

# The evidence schema. A receipt carrying anything else, or missing anything here, is rejected.
EVIDENCE_FIELDS = (
    "brickid", "objid",
    "flux_ivar_r", "psfsize_r", "nobs_r",
    "quality_pass",
)
RECEIPT_FIELDS = (
    "schema_version", "quality_source_sha256", "parent_source_sha256",
    "thresholds", "join_keys",
    "n_parent", "n_joined", "n_retained", "n_excluded",
    "evidence_sha256",
)
THRESHOLD_FIELDS = ("flux_ivar_r_gt", "psfsize_r_lt", "nobs_r_ge")
COUNT_FIELDS = ("n_parent", "n_joined", "n_retained", "n_excluded")
SCHEMA_VERSION = "bs2a/1"

# One code per invariant. A code is the check's identity; the prose after it may be reworded freely
# without weakening any control, which a substring match could never allow.
CODES = {
    "E01": "receipt is missing required fields",
    "E02": "receipt carries fields outside the schema",
    "E03": "schema_version is not the frozen version",
    "E04": "quality_source_sha256 is not the frozen source digest",
    "E05": "parent_source_sha256 is not the frozen parent digest",
    "E06": "thresholds is not an object holding exactly the three frozen names",
    "E07": "a threshold value differs from the frozen predicate",
    "E08": "join_keys is not the frozen key list",
    "E09": "an evidence row is off-schema",
    "E10": "an evidence row carries a missing or non-finite quality value",
    "E11": "an evidence row has a non-boolean quality_pass",
    "E12": "an evidence row asserts a quality_pass the predicate denies",
    "E13": "n_parent is not the frozen parent cardinality",
    "E14": "n_joined != n_parent; the join is not total over the parent",
    "E15": "evidence is not one-to-one on the join keys",
    "E16": "n_retained disagrees with the count recomputed from the evidence",
    "E17": "n_joined disagrees with the number of evidence rows",
    "E18": "n_retained + n_excluded != n_joined",
    "E19": "evidence_sha256 does not match the evidence it accompanies",
    "E20": "the evidence key set is not the frozen parent key set",
    "E21": "a count field is not a non-negative int",
    "E22": "n_retained is not the frozen retained count for this contract",
    "E23": "the evidence is not the frozen authenticated evidence",
    "E24": "an evidence row has a non-string join key",
    "E25": "receipt is not an object",
    "E26": "evidence is not a list of rows",
}


class QualityGateError(Exception):
    """Refusals name what failed. A refusal that cannot say why is not a refusal."""


# ── Reading, with the bytes bound to the digest that was verified ───────────────────────────────

def verified_bytes(path: Path, expect_sha256: str) -> bytes:
    """Read once, hash what was read, refuse on mismatch.

    Single open, O_NOFOLLOW, regular-file check, hash-as-read. Verifying a path and then re-opening
    it verifies nothing about the bytes actually consumed — the closure mechanism spent five gate
    rounds establishing that, and the same rule applies here.
    """
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | getattr(os, "O_NONBLOCK", 0))
    try:
        st = os.fstat(fd)
        if not stat.S_ISREG(st.st_mode):
            raise QualityGateError(f"{path} is not a regular file")
        h, chunks = hashlib.sha256(), []
        while True:
            b = os.read(fd, 1 << 20)
            if not b:
                break
            h.update(b)
            chunks.append(b)
    finally:
        os.close(fd)
    got = h.hexdigest()
    if got != expect_sha256:
        raise QualityGateError(
            f"{path.name} digest mismatch: expected {expect_sha256}, read {got}")
    return b"".join(chunks)


def _rows(raw: bytes):
    return list(csv.DictReader(io.StringIO(raw.decode("utf-8"))))


# ── The predicate ───────────────────────────────────────────────────────────────────────────────

def quality_pass(flux_ivar_r: float, psfsize_r: float, nobs_r: float) -> bool:
    """The frozen predicate. All three must hold."""
    return (flux_ivar_r > T_FLUX_IVAR_R_GT
            and psfsize_r < T_PSFSIZE_R_LT
            and nobs_r >= T_NOBS_R_GE)


def _key(row) -> tuple:
    return tuple(str(row[k]).strip() for k in JOIN_KEYS)


def build_evidence(parent_path: Path, quality_path: Path) -> tuple[list[dict], dict]:
    """Join parent to quality one-to-one, apply the predicate, return (evidence, receipt).

    The join is exact set equality on (brickid, objid). A parent row with no quality row, a quality
    row with no parent, or a duplicate on either side is a refusal — not a silent drop. Silent
    inner-join loss is exactly what the acceptance design forbids downstream, and it would be no
    more acceptable here.
    """
    parent = _rows(verified_bytes(parent_path, PARENT_SHA256))
    quality = _rows(verified_bytes(quality_path, QUALITY_SHA256))

    if len(parent) != PARENT_ROWS:
        raise QualityGateError(f"parent holds {len(parent)} rows, expected {PARENT_ROWS}")

    qmap: dict[tuple, dict] = {}
    for r in quality:
        k = _key(r)
        if k in qmap:
            raise QualityGateError(f"duplicate quality row for {JOIN_KEYS}={k}")
        qmap[k] = r

    pkeys = set()
    for r in parent:
        k = _key(r)
        if k in pkeys:
            raise QualityGateError(f"duplicate parent row for {JOIN_KEYS}={k}")
        pkeys.add(k)

    missing = pkeys - set(qmap)
    extra = set(qmap) - pkeys
    if missing:
        raise QualityGateError(f"{len(missing)} parent objects have no quality row; first={sorted(missing)[0]}")
    if extra:
        raise QualityGateError(f"{len(extra)} quality rows have no parent; first={sorted(extra)[0]}")

    evidence = []
    for r in parent:
        k = _key(r)
        q = qmap[k]
        vals = {c: float(q[c]) for c in QUALITY_COLUMNS}
        evidence.append({
            "brickid": k[0], "objid": k[1],
            **{c: vals[c] for c in QUALITY_COLUMNS},
            "quality_pass": quality_pass(**vals),
        })

    retained = sum(1 for e in evidence if e["quality_pass"])
    receipt = {
        "schema_version": SCHEMA_VERSION,
        "quality_source_sha256": QUALITY_SHA256,
        "parent_source_sha256": PARENT_SHA256,
        "thresholds": {
            "flux_ivar_r_gt": T_FLUX_IVAR_R_GT,
            "psfsize_r_lt": T_PSFSIZE_R_LT,
            "nobs_r_ge": T_NOBS_R_GE,
        },
        "join_keys": list(JOIN_KEYS),
        "n_parent": len(parent),
        "n_joined": len(evidence),
        "n_retained": retained,
        "n_excluded": len(evidence) - retained,
        "evidence_sha256": evidence_digest(evidence),
    }
    return evidence, receipt


def _enc(*parts) -> str:
    """Length-prefixed, so no field value can forge a delimiter. "a|b" and "a","b" must not
    collide, and with a bare "|" join they would (CODEX-BS2A-5).

    Coerces to str so that a non-string join key digests instead of raising. `len(12345)` is a
    TypeError, and a verifier that raises has not refused — E24 is what rejects the type.
    """
    return "".join(f"{len(s)}:{s}" for s in map(str, parts))


def evidence_digest(evidence: list[dict]) -> str:
    """Canonical digest over the evidence, order-independent by construction."""
    def enc(e):
        def num(k):
            try:
                return repr(float(e.get(k)))
            except (TypeError, ValueError, OverflowError):
                return "\x00missing"
        return _enc(e.get("brickid"), e.get("objid"),
                    num("flux_ivar_r"), num("psfsize_r"), num("nobs_r"),
                    "1" if e.get("quality_pass") else "0")
    return hashlib.sha256("\n".join(sorted(enc(e) for e in evidence)).encode("utf-8")).hexdigest()


def keyset_digest(evidence: list[dict]) -> str:
    """Canonical digest over the evidence key SET — membership, not cardinality.

    Round 2: both seats forged a key while preserving size, uniqueness, counts and the evidence
    digest, and the verifier accepted it. Counting 65,060 unique keys says nothing about *which*
    65,060 they are.
    """
    return hashlib.sha256("\n".join(sorted(
        _enc(str(e.get("brickid")), str(e.get("objid"))) for e in evidence)).encode("utf-8")).hexdigest()


# ── The verifier. It must be able to reject. ────────────────────────────────────────────────────

def verify_receipt(receipt: dict, evidence: list[dict]) -> list[str]:
    """Return a list of refusal reasons, each prefixed with its code. Empty means it conforms.

    Recomputes rather than reads: every count, both digests and the key set are derived here and
    compared, so a receipt cannot assert a number the evidence does not support, nor evidence the
    authenticated sources did not produce.
    """
    bad: list[str] = []

    def refuse(code: str, msg: str) -> None:
        bad.append(f"[{code}] {msg}")

    # The CONTAINERS first. Rounds 3 and 4 both found this class one level lower: a check guarded
    # its rows but not the thing holding them, so `set(receipt)` and `enumerate(evidence)` raised on
    # JSON-native null/number/bool input. The dict case is the sharp one — iterating a dict yields
    # its keys, so `off_schema` correctly flagged index 0, and then the line written to REPORT that
    # refusal did `evidence[i]` with i=0 and raised KeyError. The detector fired; the reporter
    # crashed. Nothing below may assume its container shape without this.
    receipt_ok = type(receipt) is dict
    evidence_ok = type(evidence) is list
    if not receipt_ok:
        refuse("E25", f"receipt is not an object: {type(receipt).__name__}")
    if not evidence_ok:
        refuse("E26", f"evidence is not a list of rows: {type(evidence).__name__}")
    # Keyed off the STRUCTURAL condition, not off `bad`. My first version of this guard returned on
    # `bad`, so deleting either refusal let execution fall through and the deletion was caught by a
    # traceback instead of by its control — the identical defect this module already fixed at the
    # receipt-field level, reintroduced by the repair for it. A control should catch, not a crash.
    if not (receipt_ok and evidence_ok):
        return bad

    extra = set(receipt) - set(RECEIPT_FIELDS)
    missing = set(RECEIPT_FIELDS) - set(receipt)
    if missing:
        refuse("E01", f"receipt missing required fields: {sorted(missing)}")
    if extra:
        refuse("E02", f"receipt carries fields outside the schema: {sorted(extra)}")
    # Return on the STRUCTURAL condition, not on `bad`. Keying the early return off the refusal
    # list couples it to E01/E02 still existing: with E01 deleted, a receipt missing a field ran on
    # into `receipt[...]` and raised KeyError, so the deletion was caught by a crash rather than by
    # its control. A verifier should refuse, not crash, and a control should catch, not a traceback.
    if missing or extra:
        return bad

    if type(receipt["schema_version"]) is not str or receipt["schema_version"] != SCHEMA_VERSION:
        refuse("E03", f"schema_version {receipt['schema_version']!r} != {SCHEMA_VERSION!r}")
    if type(receipt["quality_source_sha256"]) is not str or receipt["quality_source_sha256"] != QUALITY_SHA256:
        refuse("E04", "quality_source_sha256 does not match the frozen source digest")
    if type(receipt["parent_source_sha256"]) is not str or receipt["parent_source_sha256"] != PARENT_SHA256:
        refuse("E05", "parent_source_sha256 does not match the frozen parent digest")

    # The schema is closed RECURSIVELY. Closing only the outer keys let a receipt carry chi_net
    # inside `thresholds` — the one field the schema exists to exclude (round 2, both seats).
    t = receipt["thresholds"]
    if type(t) is not dict or set(t) != set(THRESHOLD_FIELDS):
        refuse("E06", f"thresholds must be an object with exactly {sorted(THRESHOLD_FIELDS)}, got "
                      f"{sorted(t) if type(t) is dict else type(t).__name__}")
    else:
        for name, want in zip(THRESHOLD_FIELDS, (T_FLUX_IVAR_R_GT, T_PSFSIZE_R_LT, T_NOBS_R_GE)):
            if type(t[name]) not in (int, float) or t[name] != want:
                refuse("E07", f"threshold {name}={t[name]!r} != frozen {want!r}")

    if (type(receipt["join_keys"]) is not list
            or any(type(k) is not str for k in receipt["join_keys"])
            or receipt["join_keys"] != list(JOIN_KEYS)):
        refuse("E08", f"join_keys {receipt['join_keys']!r} != {list(JOIN_KEYS)!r}")

    # A count field is a cardinality. `65060.0 == 65060` and `True == 1` in Python, so equality
    # alone accepts a float or a bool where a row count belongs (CODEX round 2, finding 4).
    mistyped = [f for f in COUNT_FIELDS
                if type(receipt[f]) is not int or receipt[f] < 0]
    if mistyped:
        refuse("E21", f"count field(s) not a non-negative int: "
                      f"{ {f: repr(receipt[f]) for f in mistyped} }")

    # EVERY row, not the first mismatch. The original broke out of this loop, so a clean row 0
    # let a later row carry chi_net straight through the schema that exists to stop it
    # (CODEX-BS2A-1). A check that inspects one element of a collection has not checked the
    # collection.
    off_schema = [i for i, e in enumerate(evidence)
                  if not isinstance(e, dict) or set(e) != set(EVIDENCE_FIELDS)]
    if off_schema:
        i = off_schema[0]
        shape = (sorted(set(evidence[i]) ^ set(EVIDENCE_FIELDS)) if isinstance(evidence[i], dict)
                 else type(evidence[i]).__name__)
        refuse("E09", f"{len(off_schema)} evidence row(s) off-schema; first at index {i}: {shape}")
        # Return on the STRUCTURAL condition, not on `bad`. A row that is not a well-formed dict
        # cannot be digested, and everything below assumes it can be: CODEX round 3 deleted one
        # required key from one row and `evidence_digest()` raised KeyError instead of refusing.
        # A verifier that raises has not refused. Keying this off `bad` would also make it vanish
        # if E09 were ever deleted — the same coupling already fixed at the receipt level.
        return bad

    # PER ROW, not in aggregate. Totals can agree while individual rows lie in compensating
    # directions (CODEX-BS2A-2).
    disagree, nonfinite, nonbool = [], [], []
    for i, e in enumerate(evidence):
        try:
            f, ps, nb = float(e["flux_ivar_r"]), float(e["psfsize_r"]), float(e["nobs_r"])
        except (KeyError, TypeError, ValueError, OverflowError):
            nonfinite.append(i)
            continue
        if not all(v == v and v not in (float("inf"), float("-inf")) for v in (f, ps, nb)):
            nonfinite.append(i)
            continue
        if type(e.get("quality_pass")) is not bool:
            nonbool.append(i)
            continue
        if e["quality_pass"] != quality_pass(f, ps, nb):
            disagree.append(i)
    if nonfinite:
        refuse("E10", f"{len(nonfinite)} evidence row(s) carry missing or non-finite quality "
                      f"values; first index {nonfinite[0]}")
    if nonbool:
        refuse("E11", f"{len(nonbool)} evidence row(s) have non-boolean quality_pass; "
                      f"first index {nonbool[0]}")
    if disagree:
        refuse("E12", f"{len(disagree)} evidence row(s) assert a quality_pass the predicate does "
                      f"not support; first index {disagree[0]}")

    # Closure, IN THE VERIFIER. The builder enforced these, but a hand-made receipt/evidence pair
    # never goes through the builder (CODEX-BS2A-3).
    if receipt["n_parent"] != PARENT_ROWS:
        refuse("E13", f"n_parent {receipt['n_parent']} != frozen parent identity {PARENT_ROWS}")
    if receipt["n_joined"] != receipt["n_parent"]:
        refuse("E14", f"n_joined {receipt['n_joined']} != n_parent {receipt['n_parent']}: "
                      f"the join is not total over the parent")
    mistyped_keys = [i for i, e in enumerate(evidence)
                     if type(e.get("brickid")) is not str or type(e.get("objid")) is not str]
    if mistyped_keys:
        refuse("E24", f"{len(mistyped_keys)} evidence row(s) have a non-string join key; "
                      f"first index {mistyped_keys[0]}")

    keys = [(e.get("brickid"), e.get("objid")) for e in evidence]
    if len(set(keys)) != len(keys):
        refuse("E15", f"evidence is not one-to-one on {JOIN_KEYS}: "
                      f"{len(keys) - len(set(keys))} duplicate key(s)")

    recomputed = sum(1 for e in evidence
                     if type(e.get("quality_pass")) is bool and e["quality_pass"])
    if recomputed != receipt["n_retained"]:
        refuse("E16", f"n_retained {receipt['n_retained']} but evidence carries {recomputed}")
    if receipt["n_joined"] != len(evidence):
        refuse("E17", f"n_joined {receipt['n_joined']} but evidence holds {len(evidence)}")
    if receipt["n_retained"] + receipt["n_excluded"] != receipt["n_joined"]:
        refuse("E18", "n_retained + n_excluded != n_joined")
    ed = evidence_digest(evidence)
    if type(receipt["evidence_sha256"]) is not str or receipt["evidence_sha256"] != ed:
        refuse("E19", "evidence_sha256 does not match the evidence it accompanies")

    # Membership and identity against the frozen commitments. Everything above this point is
    # satisfiable by a well-formed forgery; these three are not.
    if keyset_digest(evidence) != PARENT_KEYSET_SHA256:
        refuse("E20", "the evidence key set is not the frozen parent key set")
    if receipt["n_retained"] != EXPECTED_RETAINED:
        refuse("E22", f"n_retained {receipt['n_retained']} != frozen {EXPECTED_RETAINED} for this "
                      f"contract")
    if ed != EVIDENCE_SHA256:
        refuse("E23", "the evidence is not the frozen authenticated evidence")

    return bad


def codes_of(reasons: list[str]) -> set[str]:
    """The refusal codes present in a refusal list."""
    return {r[1:4] for r in reasons if len(r) > 4 and r[0] == "[" and r[4] == "]"}


# ── Negative controls. Every check above must prove it can fail, and fail alone. ─────────────────

def default_acquire_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "acquire"


def authenticated_fixture(acquire: Path) -> tuple[list[dict], dict]:
    """The fixture IS the authenticated evidence.

    Round 2, CODEX: the synthetic fixture used invented keys and bypassed `verified_bytes()` /
    `build_evidence()`, "and that difference matters precisely because the verifier accepts a false
    parent membership independently of the builder". The tempting fix — exempting the fixture from
    the frozen commitments — is how a fixture ends up exercising a different code path from
    production. So the fixture is the production output, and `--self-test` needs the sources.
    """
    return build_evidence(acquire / "positions_selected.csv", acquire / "quality_selected.csv")


def _c_threshold(rec, ev):
    rec["thresholds"]["psfsize_r_lt"] = 2.0
    return rec, ev


def _c_nested_chi(rec, ev):
    """χ inside `thresholds`. Outer-only closure accepted this (round 2, both seats)."""
    rec["thresholds"]["chi_net"] = 0.731
    return rec, ev


def _c_thresholds_not_dict(rec, ev):
    rec["thresholds"] = [T_FLUX_IVAR_R_GT, T_PSFSIZE_R_LT, T_NOBS_R_GE]
    return rec, ev


def _c_schema_version(rec, ev):
    rec["schema_version"] = "bs2a/0"
    return rec, ev


def _c_quality_digest(rec, ev):
    rec["quality_source_sha256"] = "0" * 64
    return rec, ev


def _c_parent_digest(rec, ev):
    rec["parent_source_sha256"] = "0" * 64
    return rec, ev


def _c_join_keys(rec, ev):
    rec["join_keys"] = ["ls_id"]
    return rec, ev


def _c_join_keys_tuple(rec, ev):
    rec["join_keys"] = tuple(JOIN_KEYS)
    return rec, ev


def _c_parent_rows(rec, ev):
    rec["n_parent"] = PARENT_ROWS - 1
    return rec, ev


def _c_count(rec, ev):
    """Inflate n_retained AND keep the partition summing, so the partition branch cannot mask it."""
    rec["n_retained"] += 2
    rec["n_excluded"] -= 2
    return rec, ev


def _c_joined(rec, ev):
    rec["n_joined"] += 1
    rec["n_excluded"] += 1
    return rec, ev


def _c_partition(rec, ev):
    """Break ONLY the sum, so the join-totality check cannot fire first and mask it."""
    rec["n_excluded"] += 5
    return rec, ev


def _c_float_counts(rec, ev):
    for f in COUNT_FIELDS:
        rec[f] = float(rec[f])
    return rec, ev


def _c_bool_count(rec, ev):
    rec["n_excluded"] = True
    return rec, ev


def _c_evidence_digest(rec, ev):
    rec["evidence_sha256"] = "0" * 64
    return rec, ev


def _c_extra_field(rec, ev):
    rec["confidence"] = 0.9
    return rec, ev


def _c_missing_field(rec, ev):
    del rec["join_keys"]
    return rec, ev


def _c_evidence_shape(rec, ev):
    """χ on a LATE row — the original put it on row 0, which a break-on-first check caught."""
    ev[-1]["chi_net"] = 0.7
    return rec, ev


def _c_row_disagrees(rec, ev):
    """A row asserting a quality_pass the predicate denies, with totals left consistent."""
    i = next(i for i, e in enumerate(ev) if not e["quality_pass"])
    ev[i]["quality_pass"] = True
    rec["n_retained"] += 1
    rec["n_excluded"] -= 1
    rec["evidence_sha256"] = evidence_digest(ev)
    return rec, ev


def _c_nonbool(rec, ev):
    i = next(i for i, e in enumerate(ev) if e["quality_pass"])
    ev[i]["quality_pass"] = 1
    rec["evidence_sha256"] = evidence_digest(ev)
    return rec, ev


def _c_nonfinite(rec, ev):
    i = next(i for i, e in enumerate(ev) if not e["quality_pass"])
    ev[i]["psfsize_r"] = float("nan")
    rec["evidence_sha256"] = evidence_digest(ev)
    return rec, ev


def _c_duplicate_key(rec, ev):
    ev[1]["brickid"], ev[1]["objid"] = ev[0]["brickid"], ev[0]["objid"]
    rec["evidence_sha256"] = evidence_digest(ev)
    return rec, ev


def _c_forged_parent_key(rec, ev):
    """Size, uniqueness, counts and the accompanying digest all preserved — only *which* object it
    is changes. Both seats got this accepted in round 2."""
    ev[2]["brickid"] = "FORGED_PARENT_MEMBER_NOT_IN_SOURCE"
    rec["evidence_sha256"] = evidence_digest(ev)
    return rec, ev


def _c_nonstring_key(rec, ev):
    """An int join key. Before E24 this raised TypeError out of `evidence_digest()` rather than
    refusing, and a verifier that raises has not refused."""
    ev[3]["brickid"] = 12345
    rec["evidence_sha256"] = evidence_digest(ev)
    return rec, ev


def _c_missing_row_key(rec, ev):
    """CODEX round 3: deleting one required key from one row raised KeyError out of
    evidence_digest() instead of refusing."""
    ev[0] = dict(ev[0])
    del ev[0]["flux_ivar_r"]
    return rec, ev


def _c_nondict_row(rec, ev):
    """A row that is not a dict at all — `set(e)` raised TypeError before E09 could record it."""
    ev[0] = None
    return rec, ev


class _LiarEq:
    """Compares equal to everything. GPT56 round 3 used this to bypass E03/E07/E19 and get an
    ACCEPT — worse than a raise, because it is silent."""
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    def __hash__(self): return 0
    def __repr__(self): return "<LiarEq>"


def _c_liar_schema(rec, ev):
    rec["schema_version"] = _LiarEq()
    return rec, ev


def _c_liar_threshold(rec, ev):
    rec["thresholds"]["psfsize_r_lt"] = _LiarEq()
    return rec, ev


def _c_liar_digest(rec, ev):
    rec["evidence_sha256"] = _LiarEq()
    return rec, ev


def _c_huge_value(rec, ev):
    """float(10**400) raises OverflowError, which was not in the caught tuple."""
    ev[0] = dict(ev[0])
    ev[0]["flux_ivar_r"] = 10 ** 400
    rec["evidence_sha256"] = evidence_digest(ev)   # isolate: E19 is not what this tests
    return rec, ev


def _c_receipt_not_dict(rec, ev):
    """JSON null in the receipt slot. `set(receipt)` raised TypeError (CODEX round 4)."""
    return None, ev


def _c_evidence_not_list(rec, ev):
    """JSON number in the evidence slot. `enumerate(evidence)` raised TypeError."""
    return rec, 42


def _c_evidence_is_dict(rec, ev):
    """The sharp one: off_schema flagged it, then the reporting line raised KeyError: 0."""
    return rec, {"a": 1}


def _c_all_pass(rec, ev):
    """GPT56's stronger round-2 forgery: a wholly foreign all-pass partition, internally consistent
    and honestly re-digested, which the verifier accepted while printing MISMATCH."""
    for e in ev:
        e["quality_pass"] = True
    rec["n_retained"] = len(ev)
    rec["n_excluded"] = 0
    rec["evidence_sha256"] = evidence_digest(ev)
    return rec, ev


# (name, mutator, the EXACT set of refusal codes the mutation must produce). Not a substring, not
# "some refusal": deleting a check drops its code from the set and the control fails; a spurious
# extra refusal also fails. Rounds 1 and 2 both fell to controls that accepted a superset.
CONTROLS = (
    ("threshold mutated",          _c_threshold,          {"E07"}),
    ("chi_net nested in thresholds", _c_nested_chi,       {"E06"}),
    ("thresholds not an object",   _c_thresholds_not_dict, {"E06"}),
    ("schema version wrong",       _c_schema_version,     {"E03"}),
    ("quality digest wrong",       _c_quality_digest,     {"E04"}),
    ("parent digest wrong",        _c_parent_digest,      {"E05"}),
    ("join keys wrong",            _c_join_keys,          {"E08"}),
    ("join keys not a list",       _c_join_keys_tuple,    {"E08"}),
    ("parent identity wrong",      _c_parent_rows,        {"E13", "E14"}),
    ("retained count inflated",    _c_count,              {"E16", "E22"}),
    ("joined count wrong",         _c_joined,             {"E14", "E17"}),
    ("partition does not sum",     _c_partition,          {"E18"}),
    ("float count fields",         _c_float_counts,       {"E21"}),
    ("boolean count field",        _c_bool_count,         {"E18", "E21"}),
    ("evidence digest wrong",      _c_evidence_digest,    {"E19"}),
    ("extra receipt field",        _c_extra_field,        {"E02"}),
    ("missing receipt field",      _c_missing_field,      {"E01"}),
    ("late row carries χ",         _c_evidence_shape,     {"E09"}),
    ("row missing a key",          _c_missing_row_key,    {"E09"}),
    ("row is not a dict",          _c_nondict_row,        {"E09"}),
    ("lying __eq__ schema",        _c_liar_schema,        {"E03"}),
    ("lying __eq__ threshold",     _c_liar_threshold,     {"E07"}),
    ("lying __eq__ digest",        _c_liar_digest,        {"E19"}),
    ("value overflows float",      _c_huge_value,         {"E10", "E23"}),
    ("receipt is not an object",   _c_receipt_not_dict,   {"E25"}),
    ("evidence is not a list",     _c_evidence_not_list,  {"E26"}),
    ("evidence is a dict",         _c_evidence_is_dict,   {"E26"}),
    ("row contradicts predicate",  _c_row_disagrees,      {"E12", "E22", "E23"}),
    # No E23: the digest encodes quality_pass by truthiness, so int 1 and True are the same bytes.
    # E11 is what catches it, and E16 follows because the recount excludes the non-bool row.
    ("non-boolean quality_pass",   _c_nonbool,            {"E11", "E16"}),
    ("non-finite quality value",   _c_nonfinite,          {"E10", "E23"}),
    ("duplicate evidence key",     _c_duplicate_key,      {"E15", "E20", "E23"}),
    ("forged parent member",       _c_forged_parent_key,  {"E20", "E23"}),
    ("non-string join key",        _c_nonstring_key,      {"E24", "E20", "E23"}),
    ("foreign all-pass partition", _c_all_pass,           {"E12", "E22", "E23"}),
)


def uncontrolled() -> set[str]:
    """Codes no control exercises. Computed from CONTROLS, so coverage cannot be merely claimed."""
    return set(CODES) - set().union(*(expect for _, _, expect in CONTROLS))


def self_test(acquire: Path | None = None) -> int:
    """Each control must produce EXACTLY its own refusal codes — no fewer, no more."""
    acquire = acquire or default_acquire_dir()
    if not (acquire / "positions_selected.csv").is_file():
        print(f"  FAIL sources not found under {acquire}; the fixture is the authenticated "
              f"evidence and cannot be synthesised")
        return 1

    ev0, rec0 = authenticated_fixture(acquire)

    def fresh():
        return [dict(e) for e in ev0], json.loads(json.dumps(rec0))

    base = verify_receipt(rec0, ev0)
    ok0 = not base
    print(f"  {'OK  ' if ok0 else 'FAIL'} authenticated receipt verifies clean"
          f"{'' if ok0 else f' — unexpected: {base}'}")
    fails = [] if ok0 else ["baseline"]

    for name, mutate, expect in CONTROLS:
        ev2, rec2 = fresh()
        rec2, ev2 = mutate(rec2, ev2)
        got = codes_of(verify_receipt(rec2, ev2))
        ok = got == expect
        if ok:
            detail = " ".join(sorted(got))
        else:
            detail = (f"expected {sorted(expect)}, got {sorted(got)}"
                      f" — missing {sorted(expect - got)}, spurious {sorted(got - expect)}")
        print(f"  {'OK  ' if ok else 'FAIL'} {name}: {detail}")
        if not ok:
            fails.append(name)

    orphans = uncontrolled()
    if orphans:
        print(f"  FAIL {len(orphans)} check(s) have no control: {sorted(orphans)}")
        fails.append("coverage")
    else:
        print(f"  OK   every one of {len(CODES)} checks is exercised by a control")

    print(f"  self-test: {len(CONTROLS)} controls, {len(fails)} failure(s)")
    return 1 if fails else 0


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--acquire", default="", help="directory holding the two source CSVs")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--emit", default="", help="write evidence+receipt JSON here")
    a = ap.parse_args()

    if a.self_test:
        print("bs2a quality-gate self-test")
        return self_test(Path(a.acquire) if a.acquire else None)

    if not a.acquire:
        print("--acquire <dir> required (or --self-test)")
        return 1
    d = Path(a.acquire)
    ev, rec = build_evidence(d / "positions_selected.csv", d / "quality_selected.csv")
    bad = verify_receipt(rec, ev)
    print(json.dumps(rec, indent=2))
    match = rec["n_retained"] == EXPECTED_RETAINED
    print(f"  retained {rec['n_retained']:,} of {rec['n_joined']:,} "
          f"(expected {EXPECTED_RETAINED:,}) — {'MATCH' if match else 'MISMATCH'}")
    if bad:
        for b in bad:
            print(f"  REFUSED: {b}")
        return 1
    if a.emit:
        Path(a.emit).write_text(json.dumps({"receipt": rec, "evidence": ev}, indent=1))
        print(f"  wrote {a.emit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
