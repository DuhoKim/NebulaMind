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

WHY THE FIXTURES LOOK LIKE THIS
-------------------------------
Three guards written on 2026-08-28 reported "clean" while being unable to fail: a blockquote
exemption that voided a count check, a skipped branch that never examined the row most needing
examination, and a control battery covering five of six checks. All three were found by referees, not
by their author. So every check here ships a negative control, and `self_test()` asserts each one
fires. Silence is only evidence once a check has shown it can speak.
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
SCHEMA_VERSION = "bs2a/1"


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


def evidence_digest(evidence: list[dict]) -> str:
    """Canonical digest over the evidence, order-independent by construction."""
    # Length-prefixed, so no field value can forge a delimiter. "a|b" and "a","b" must not
    # collide, and with a bare "|" join they would (CODEX-BS2A-5).
    def enc(e):
        parts = [e["brickid"], e["objid"],
                 repr(float(e["flux_ivar_r"])), repr(float(e["psfsize_r"])),
                 repr(float(e["nobs_r"])), "1" if e["quality_pass"] else "0"]
        return "".join(f"{len(x)}:{x}" for x in parts)
    return hashlib.sha256("\n".join(sorted(enc(e) for e in evidence)).encode("utf-8")).hexdigest()


# ── The verifier. It must be able to reject. ────────────────────────────────────────────────────

def verify_receipt(receipt: dict, evidence: list[dict]) -> list[str]:
    """Return a list of refusal reasons. Empty means the receipt conforms.

    Recomputes rather than reads: every count and the evidence digest are derived here and compared,
    so a receipt cannot assert a number the evidence does not support.
    """
    bad: list[str] = []

    extra = set(receipt) - set(RECEIPT_FIELDS)
    missing = set(RECEIPT_FIELDS) - set(receipt)
    if missing:
        bad.append(f"receipt missing required fields: {sorted(missing)}")
    if extra:
        bad.append(f"receipt carries fields outside the schema: {sorted(extra)}")
    if bad:
        return bad

    if receipt["schema_version"] != SCHEMA_VERSION:
        bad.append(f"schema_version {receipt['schema_version']!r} != {SCHEMA_VERSION!r}")
    if receipt["quality_source_sha256"] != QUALITY_SHA256:
        bad.append("quality_source_sha256 does not match the frozen source digest")
    if receipt["parent_source_sha256"] != PARENT_SHA256:
        bad.append("parent_source_sha256 does not match the frozen parent digest")

    t = receipt.get("thresholds") or {}
    for name, want in (("flux_ivar_r_gt", T_FLUX_IVAR_R_GT),
                       ("psfsize_r_lt", T_PSFSIZE_R_LT),
                       ("nobs_r_ge", T_NOBS_R_GE)):
        if t.get(name) != want:
            bad.append(f"threshold {name}={t.get(name)!r} != frozen {want!r}")

    if list(receipt.get("join_keys") or []) != list(JOIN_KEYS):
        bad.append(f"join_keys {receipt.get('join_keys')!r} != {list(JOIN_KEYS)!r}")

    # EVERY row, not the first mismatch. The original broke out of this loop, so a clean row 0
    # let a later row carry chi_net straight through the schema that exists to stop it
    # (CODEX-BS2A-1). A check that inspects one element of a collection has not checked the
    # collection.
    off_schema = [i for i, e in enumerate(evidence) if set(e) != set(EVIDENCE_FIELDS)]
    if off_schema:
        i = off_schema[0]
        bad.append(f"{len(off_schema)} evidence row(s) off-schema; first at index {i}: "
                   f"{sorted(set(evidence[i]) ^ set(EVIDENCE_FIELDS))}")

    # PER ROW, not in aggregate. Totals can agree while individual rows lie in compensating
    # directions (CODEX-BS2A-2).
    disagree, nonfinite, nonbool = [], [], []
    for i, e in enumerate(evidence):
        try:
            f, ps, nb = float(e["flux_ivar_r"]), float(e["psfsize_r"]), float(e["nobs_r"])
        except (KeyError, TypeError, ValueError):
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
        bad.append(f"{len(nonfinite)} evidence row(s) carry missing or non-finite quality values; "
                   f"first index {nonfinite[0]}")
    if nonbool:
        bad.append(f"{len(nonbool)} evidence row(s) have non-boolean quality_pass; "
                   f"first index {nonbool[0]}")
    if disagree:
        bad.append(f"{len(disagree)} evidence row(s) assert a quality_pass the predicate does not "
                   f"support; first index {disagree[0]}")

    # Closure, IN THE VERIFIER. The builder enforced these, but a hand-made receipt/evidence pair
    # never goes through the builder (CODEX-BS2A-3).
    if receipt["n_parent"] != PARENT_ROWS:
        bad.append(f"n_parent {receipt['n_parent']} != frozen parent identity {PARENT_ROWS}")
    if receipt["n_joined"] != receipt["n_parent"]:
        bad.append(f"n_joined {receipt['n_joined']} != n_parent {receipt['n_parent']}: "
                   f"the join is not total over the parent")
    keys = [(e.get("brickid"), e.get("objid")) for e in evidence]
    if len(set(keys)) != len(keys):
        bad.append(f"evidence is not one-to-one on {JOIN_KEYS}: "
                   f"{len(keys) - len(set(keys))} duplicate key(s)")

    recomputed = sum(1 for e in evidence
                     if type(e.get("quality_pass")) is bool and e["quality_pass"])
    if recomputed != receipt["n_retained"]:
        bad.append(f"n_retained {receipt['n_retained']} but evidence carries {recomputed}")
    if receipt["n_joined"] != len(evidence):
        bad.append(f"n_joined {receipt['n_joined']} but evidence holds {len(evidence)}")
    if receipt["n_retained"] + receipt["n_excluded"] != receipt["n_joined"]:
        bad.append("n_retained + n_excluded != n_joined")
    if receipt["evidence_sha256"] != evidence_digest(evidence):
        bad.append("evidence_sha256 does not match the evidence it accompanies")

    return bad


# ── Negative controls. Every check above must prove it can fail. ────────────────────────────────

def _sample_evidence():
    """A fixture at the REAL parent size, not a miniature of it.

    The first version used four rows, so the parent-identity check (n_parent == 65,060) failed on
    the fixture itself and the partition control then refused for the wrong reason. The tempting fix
    is to relax the check when running against a fixture — which is precisely how a fixture ends up
    exercising a different code path from production, and how a gate certifies something it never
    tested. Generating 65,060 rows costs nothing and keeps one path.

    Four rows carry the interesting cases; the remainder are uniform passes.
    """
    rows = [
        {"brickid": "1", "objid": "1", "flux_ivar_r": 50.0, "psfsize_r": 1.2, "nobs_r": 5.0,
         "quality_pass": True},
        {"brickid": "1", "objid": "2", "flux_ivar_r": 2.0, "psfsize_r": 1.2, "nobs_r": 5.0,
         "quality_pass": False},
        {"brickid": "2", "objid": "1", "flux_ivar_r": 50.0, "psfsize_r": 1.9, "nobs_r": 5.0,
         "quality_pass": False},
        {"brickid": "2", "objid": "2", "flux_ivar_r": 50.0, "psfsize_r": 1.2, "nobs_r": 1.0,
         "quality_pass": False},
    ]
    for i in range(PARENT_ROWS - len(rows)):
        rows.append({"brickid": "9", "objid": str(i), "flux_ivar_r": 50.0, "psfsize_r": 1.2,
                     "nobs_r": 5.0, "quality_pass": True})
    retained = sum(1 for r in rows if r["quality_pass"])
    r = {
        "schema_version": SCHEMA_VERSION,
        "quality_source_sha256": QUALITY_SHA256,
        "parent_source_sha256": PARENT_SHA256,
        "thresholds": {"flux_ivar_r_gt": T_FLUX_IVAR_R_GT,
                       "psfsize_r_lt": T_PSFSIZE_R_LT,
                       "nobs_r_ge": T_NOBS_R_GE},
        "join_keys": list(JOIN_KEYS),
        "n_parent": PARENT_ROWS, "n_joined": len(rows),
        "n_retained": retained, "n_excluded": len(rows) - retained,
        "evidence_sha256": evidence_digest(rows),
    }
    return rows, r


def _c_threshold(rec, ev):
    rec["thresholds"]["psfsize_r_lt"] = 2.0
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


def _c_parent_rows(rec, ev):
    rec["n_parent"] = PARENT_ROWS - 1
    return rec, ev


def _c_count(rec, ev):
    """Inflate n_retained AND keep the partition summing, so only the count check can catch it.

    The original moved n_retained alone, which the partition-sum branch caught — so deleting the
    count check left the control still firing, for the wrong reason (CODEX-BS2A-4).
    """
    rec["n_retained"] += 2
    rec["n_excluded"] -= 2
    return rec, ev


def _c_joined(rec, ev):
    rec["n_joined"] += 1
    rec["n_excluded"] += 1
    return rec, ev


def _c_partition(rec, ev):
    """Break ONLY the sum. Moving n_joined too let the join-totality check fire first, so the
    control passed while proving nothing about the partition branch — the same wrong-reason pass
    CODEX found in the original battery, reintroduced by my own repair of it."""
    rec["n_excluded"] += 5
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
    ev[1]["quality_pass"] = True
    rec["n_retained"] += 1
    rec["n_excluded"] -= 1
    rec["evidence_sha256"] = evidence_digest(ev)
    return rec, ev


def _c_nonbool(rec, ev):
    ev[0]["quality_pass"] = 1
    rec["evidence_sha256"] = evidence_digest(ev)
    return rec, ev


def _c_nonfinite(rec, ev):
    ev[0]["psfsize_r"] = float("nan")
    rec["evidence_sha256"] = evidence_digest(ev)
    return rec, ev


def _c_duplicate_key(rec, ev):
    ev[1]["brickid"], ev[1]["objid"] = ev[0]["brickid"], ev[0]["objid"]
    rec["evidence_sha256"] = evidence_digest(ev)
    return rec, ev


# (name, mutator, REQUIRED substring of the refusal). Asserting the *reason* is the whole point:
# checking only that "something refused" let a surviving guard mask a deleted one, which is how a
# control battery reported 7/0 with two checks removed (CODEX-BS2A-4).
CONTROLS = (
    ("threshold mutated",        _c_threshold,        "threshold psfsize_r_lt"),
    ("schema version wrong",     _c_schema_version,   "schema_version"),
    ("quality digest wrong",     _c_quality_digest,   "quality_source_sha256"),
    ("parent digest wrong",      _c_parent_digest,    "parent_source_sha256"),
    ("join keys wrong",          _c_join_keys,        "join_keys"),
    ("parent identity wrong",    _c_parent_rows,      "n_parent"),
    ("retained count inflated",  _c_count,            "n_retained"),
    ("joined count wrong",       _c_joined,           "n_joined"),
    ("partition does not sum",   _c_partition,        "n_retained + n_excluded"),
    ("evidence digest wrong",    _c_evidence_digest,  "evidence_sha256"),
    ("extra receipt field",      _c_extra_field,      "outside the schema"),
    ("missing receipt field",    _c_missing_field,    "missing required fields"),
    ("late row carries χ",       _c_evidence_shape,   "off-schema"),
    ("row contradicts predicate", _c_row_disagrees,   "the predicate does not"),
    ("non-boolean quality_pass", _c_nonbool,          "non-boolean"),
    ("non-finite quality value", _c_nonfinite,        "non-finite"),
    ("duplicate evidence key",   _c_duplicate_key,    "one-to-one"),
)


def self_test() -> int:
    """Each control must produce ITS OWN refusal reason, not merely some refusal."""
    ev, rec = _sample_evidence()
    base = verify_receipt(rec, ev)
    ok0 = not base
    print(f"  {'OK  ' if ok0 else 'FAIL'} conforming receipt verifies clean"
          f"{'' if ok0 else f' — unexpected: {base}'}")
    fails = [] if ok0 else ["baseline"]

    for name, mutate, expect in CONTROLS:
        ev2, rec2 = _sample_evidence()
        rec2, ev2 = mutate(rec2, ev2)
        out = verify_receipt(rec2, ev2)
        matched = [b for b in out if expect in b]
        ok = bool(matched)
        detail = (matched[0][:66] if ok
                  else (f"refused for the WRONG reason: {out[0][:52]}" if out
                        else "ACCEPTED, control is silent"))
        print(f"  {'OK  ' if ok else 'FAIL'} {name}: {detail}")
        if not ok:
            fails.append(name)

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
        return self_test()

    if not a.acquire:
        print("--acquire <dir> required (or --self-test)")
        return 1
    d = Path(a.acquire)
    ev, rec = build_evidence(d / "positions_selected.csv", d / "quality_selected.csv")
    bad = verify_receipt(rec, ev)
    print(json.dumps(rec, indent=2))
    print(f"  retained {rec['n_retained']:,} of {rec['n_joined']:,} "
          f"(expected {EXPECTED_RETAINED:,}) — {'MATCH' if rec['n_retained'] == EXPECTED_RETAINED else 'MISMATCH'}")
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
