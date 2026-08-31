#!/usr/bin/env python3
"""bs2f_boundary_verifier — §11 build item ("BS-2f boundary recomputation
verifier"): recomputes `calibration_bins()` over the FULL sealed accepted-partition
positions and refuses unless the sealed boundaries equal the recomputation EXACTLY.
It certifies THE ARTIFACT, not the process (§6.3): the receipt binds the sealed
bytes and the input digest, never an account of how they were produced.

The recomputation runs the FROZEN v9 — loaded through the replay harness's shipped
verified loader (_read_and_verify + _compile_in_order, restore mirrored from
replay_machinery_proof), never a second implementation and never an unverified
import: the boundary math that certifies is byte-for-byte the pinned math.

The positions-only law rides here too: the input surface is positions and
acceptance flags — any row carrying a stratum-bearing field refuses through the
ONE shipped guard (stratum_index_producer.positions_only_guard), because the
stratum index may reach the allocation and may NEVER reach calibration_bins().

The crash-vs-refuse law (AGY ENV-V3 F4's class, applied at build time): v9's
degenerate-bins RuntimeError surfaces as a REFUSAL code, and malformed inputs
refuse with typed codes — a verifier that crashes certifies nothing and blocks
nothing."""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import replay_harness as rh  # noqa: E402
import stratum_index_producer as sip  # noqa: E402


class BoundaryRefusal(ValueError):
    def __init__(self, code, msg):
        self.code = code
        super().__init__(f"{code}: {msg}")


def _r(code, msg):
    raise BoundaryRefusal(code, msg)


def _canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False)


def _load_v9():
    buffers = rh._read_and_verify()
    mods, saved = rh._compile_in_order(buffers)
    return (mods["successor_ref_v9"], saved,
            buffers["successor_ref_v9"][2])


def _restore(saved):
    if saved is not None:
        sys.modules["successor_ref_v9"] = saved
    else:
        sys.modules.pop("successor_ref_v9", None)


def verify_boundaries(sealed_boundaries, c_positions, rows=None):
    """The one entry: type-exact inputs, the positions-only guard, the frozen-v9
    recomputation, the exact byte comparison, the artifact-bound receipt."""
    if type(sealed_boundaries) is not np.ndarray:
        _r("SEAL-TYPE", "sealed boundaries must be an ndarray, exactly")
    if sealed_boundaries.dtype != np.dtype("<f8") or \
            sealed_boundaries.shape != (2,):
        _r("SEAL-TYPE",
           f"sealed boundaries are {sealed_boundaries.dtype}/"
           f"{sealed_boundaries.shape}; the artifact is two float64 interior "
           "boundaries")
    if type(c_positions) is not np.ndarray:
        _r("POSITIONS-TYPE", "positions must be an ndarray, exactly")
    if c_positions.dtype != np.dtype("<f8") or c_positions.ndim != 1:
        _r("POSITIONS-TYPE",
           f"positions are {c_positions.dtype}/ndim{c_positions.ndim}; the "
           "sealed accepted-partition positions are one float64 vector")
    if len(c_positions) < 3:
        _r("POSITIONS-EMPTY",
           f"{len(c_positions)} positions cannot span three calibration bins")
    if rows is not None:
        try:
            sip.positions_only_guard(rows)
        except sip.StratumRefusal as e:
            _r(e.code, str(e))
    v9, saved, v9_sha = _load_v9()
    try:
        try:
            recomputed = v9.calibration_bins(c_positions)
        except RuntimeError as e:
            _r("DEGENERATE-BINS", f"the frozen recomputation refuses: {e}")
        if recomputed.tobytes() != sealed_boundaries.tobytes():
            _r("BOUNDARY-MISMATCH",
               f"sealed {sealed_boundaries.tolist()} != recomputed "
               f"{recomputed.tolist()} over the full sealed positions")
    finally:
        _restore(saved)
    positions_digest = hashlib.sha256(c_positions.tobytes()).hexdigest()
    artifact_digest = hashlib.sha256(
        b"NMPR1:freeze-body:" + _canon({
            "boundaries_hex": sealed_boundaries.tobytes().hex(),
            "positions_digest": positions_digest,
        }).encode()).hexdigest()
    return {
        "verdict": "CERTIFIED",
        "artifact_digest": artifact_digest,
        "positions_digest": positions_digest,
        "v9_sha256": v9_sha,
        "verifier_sha256": hashlib.sha256(
            Path(__file__).read_bytes()).hexdigest(),
    }


# ------------------------------------------------------------------ fixtures
def fixtures():
    f = []
    total = 0

    def expect(code, thunk):
        nonlocal total
        total += 1
        try:
            thunk()
        except BoundaryRefusal as e:
            if e.code != code:
                f.append(f"[{code}] refused with {e.code}")
            return
        except Exception as e:
            f.append(f"[{code}] non-refusal {type(e).__name__}: {e}")
            return
        f.append(f"[{code}] accepted")

    c = np.arange(9, dtype="<f8") / 10.0
    v9, saved, v9_sha = _load_v9()
    try:
        sealed = v9.calibration_bins(c).copy()
    finally:
        _restore(saved)

    total += 1
    r1 = verify_boundaries(sealed, c)
    if r1["verdict"] != "CERTIFIED" or r1["v9_sha256"] != v9_sha:
        f.append("clean certification failed or wrong v9 identity")
    total += 1
    r2 = verify_boundaries(sealed, c)
    if r1["artifact_digest"] != r2["artifact_digest"]:
        f.append("same artifact, different digests — not deterministic")
    total += 1
    c2 = np.arange(12, dtype="<f8") / 10.0
    v9b, savedb, _ = _load_v9()
    try:
        sealed2 = v9b.calibration_bins(c2).copy()
    finally:
        _restore(savedb)
    r3 = verify_boundaries(sealed2, c2)
    if r3["artifact_digest"] == r1["artifact_digest"]:
        f.append("different inputs, same artifact digest — binding failed")

    bad = sealed.copy()
    bad[0] += 1e-9
    expect("BOUNDARY-MISMATCH", lambda: verify_boundaries(bad, c))
    expect("SEAL-TYPE", lambda: verify_boundaries(sealed.tolist(), c))
    expect("SEAL-TYPE",
           lambda: verify_boundaries(sealed.astype("<f4"), c))
    expect("SEAL-TYPE",
           lambda: verify_boundaries(np.zeros(3, dtype="<f8"), c))
    expect("POSITIONS-TYPE", lambda: verify_boundaries(sealed, c.tolist()))
    expect("POSITIONS-TYPE",
           lambda: verify_boundaries(sealed, c.astype("<f4")))
    expect("POSITIONS-EMPTY",
           lambda: verify_boundaries(sealed, np.zeros(2, dtype="<f8")))
    expect("DEGENERATE-BINS",
           lambda: verify_boundaries(sealed, np.full(9, 0.5, dtype="<f8")))
    expect("STRATUM-CONTAMINATION",
           lambda: verify_boundaries(sealed, c,
                                     rows=[{"object_id": "a", "position": 1,
                                            "tertile": "T1"}]))
    total += 1
    verify_boundaries(sealed, c,
                      rows=[{"object_id": "a", "position": 1,
                             "accept_flag": True}])
    return f, total


if __name__ == "__main__":
    fails, total = fixtures()
    for x in fails:
        print("FIXTURE FAIL:", x)
    print(f"bs2f boundary verifier fixtures: {total - len(fails)}/{total} green")
    sys.exit(1 if fails else 0)
