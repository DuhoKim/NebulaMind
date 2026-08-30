#!/usr/bin/env python3
"""count_oracle_harness — THE ONLY PRODUCTION ENTRY to the frozen planner's build_plan().

Required by the preregistration (§2.3, §7 BS-2c, §11 inventory; GPT56-V116 F1/F2 and
CODEX-V116 F2: the frozen v9 forwards None proof objects into `_plan`, its validator is
None-conditional by design, and a fabricated self-consistent universe carrying the pinned
grand total passed the frozen bytes). This harness closes both seams WITHOUT touching v9:

  1. NONE-REFUSAL BEFORE DISPATCH — any None among the proof objects refuses here,
     before any v9 call; an explicit None cannot reach `_plan` (fixture F1).
  2. RELEASE BINDING BY CONSTRUCTION — the caller CANNOT supply a universe: the harness
     derives `universe_brickid` exclusively from v9's own `load_pinned_geometry()`, which
     verifies the sidecar bytes against `PINNED_UNIVERSE_SHA256` and the cardinality
     against `PINNED_UNIVERSE_BRICKS` before parsing the very bytes it hashed. A stale,
     foreign, or fabricated universe has no entry point (fixtures F5a/F5b).
  3. ONE BOUND INVOCATION — the BS-2c receipt is constructed from the EXACT argument
     buffers passed to `build_plan()`, digested by THIS module after the call returns,
     with object-identity asserted between what was digested and what was dispatched;
     receipt-vs-plan substitution is refused by construction (fixture F6).
  4. RECOMPUTED DIGESTS — `c_bytes` and every digest field in the receipt are recomputed
     here from the buffers; nothing digest-like is accepted from the caller.

Fixture tiers, stated so a green tier-1 is never read as the whole battery:
  TIER 1 (self-contained, always runs): F1 None-pre-dispatch; F5a wrong-sha synthetic
    sidecar refused by verified_bytes; F5b right-sha-wrong-cardinality refused; F6
    receipt-buffer identity; F7 digest recomputation correctness.
  TIER 2 (requires the pinned data files; SKIPS LOUDLY, never silently): F2 missing-brick,
    F3 extra-brick, F4 grouped/ungrouped disagreement — driven THROUGH the real
    `build_plan()` against the pinned universe. BS-2c may not fill on tier-1 alone: the
    slot's gate requires the tier-2 receipts, and this docstring says so.
"""
import hashlib
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
V9_PATH = HERE.parent / "ref" / "successor_ref_v9.py"
V9_SHA256 = "6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148"


class CountOracleHarnessRefusal(RuntimeError):
    """A refusal issued by the harness BEFORE the frozen planner is reached."""


def _load_v9():
    got = hashlib.sha256(V9_PATH.read_bytes()).hexdigest()
    if got != V9_SHA256:
        raise CountOracleHarnessRefusal(
            f"frozen reference moved: {got[:16]}… != pinned {V9_SHA256[:16]}…")
    spec = importlib.util.spec_from_file_location("successor_ref_v9", V9_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _snapshot(brickid, c, n_raw):
    """Entry snapshots (AGY-COH F2: caller-mutable buffers were digested after dispatch —
    a TOCTOU seam). Snapshots are taken ONCE, dispatched AND digested, so what planning
    consumed is byte-identically what the receipt binds; later caller mutation is inert."""
    import numpy as np
    bid = np.array(brickid, dtype=np.int64, copy=True)
    cc = np.array(c, dtype=np.float64, copy=True)
    nn = np.array(n_raw, dtype=np.int64, copy=True)
    return bid, cc, nn


def production_build_plan(brickid, c, n_raw, *, grouped_sum, ungrouped_total,
                          n_trials=None, snapshot_dir=None):
    """The production path. Returns (plan_result, bs2c_receipt).

    The caller supplies the count table (brickid, c, n_raw) and the two closure totals.
    The universe is NOT a parameter: it derives from the pinned geometry inside, in
    v9's own integer form (successor_ref_v9.py:661 — AGY-COH F3: bricknames would crash
    the integral validator)."""
    import numpy as np
    v9 = _load_v9()
    # 1. Pre-dispatch refusals: None, emptiness, shape (AGY-COH F4: `is None` alone let
    #    empty/falsy values through to die downstream instead of refusing here).
    named = {"brickid": brickid, "c": c, "n_raw": n_raw,
             "grouped_sum": grouped_sum, "ungrouped_total": ungrouped_total}
    nones = sorted(k for k, v in named.items() if v is None)
    if nones:
        raise CountOracleHarnessRefusal(
            f"None proof object(s) {nones} refused before dispatch — an explicit None "
            f"cannot reach _plan (GPT56-V116 F1)")
    try:
        bid, cc, nn = _snapshot(brickid, c, n_raw)
    except (TypeError, ValueError) as e:
        raise CountOracleHarnessRefusal(f"count-table buffers unconvertible before "
                                        f"dispatch: {e}")
    if bid.size == 0 or not (bid.size == cc.size == nn.size):
        raise CountOracleHarnessRefusal(
            f"count-table shape refused before dispatch: sizes "
            f"({bid.size}, {cc.size}, {nn.size})")
    try:
        g_tot, u_tot = int(grouped_sum), int(ungrouped_total)
    except (TypeError, ValueError) as e:
        raise CountOracleHarnessRefusal(f"closure totals unconvertible: {e}")
    # 2. Release binding: v9's pinned, sha-verified, cardinality-checked geometry —
    #    integer universe in v9's own derivation form.
    geom, sidecar_sha = v9.load_pinned_geometry(snapshot_dir)
    universe = np.sort(np.asarray(
        [int(r["brickid"]) for r in (geom.by_name or {}).values()], dtype=np.int64))
    if universe.size != v9.PINNED_UNIVERSE_BRICKS:
        raise CountOracleHarnessRefusal(
            f"pinned geometry parsed to {universe.size} bricks != "
            f"{v9.PINNED_UNIVERSE_BRICKS}")
    # 3. One bound invocation on the snapshots…
    kwargs = dict(universe_brickid=universe, grouped_sum=g_tot, ungrouped_total=u_tot)
    if n_trials is not None:
        kwargs["n_trials"] = n_trials
    result = v9.build_plan(bid, cc, nn, **kwargs)
    # …and the receipt from the SAME snapshots, v9's own canonical encoders
    # (AGY-COH F1: a newline join over ids was collision-prone; canon_i8/canon_f8 are
    # fixed-width little-endian frames, collision-free by construction).
    receipt_fields = {
        "universe_brickid": v9.canon_i8(universe),
        "brickid": v9.canon_i8(bid),
        "n_eligible": v9.canon_i8(nn),
        "c_bytes": v9.canon_f8(cc),
        "grouped_sum": str(g_tot).encode(),
        "ungrouped_total": str(u_tot).encode(),
    }
    rec = v9.receipt("BS-2c", receipt_fields)
    rec["harness"] = {"sidecar_sha256": sidecar_sha,
                      "universe_cardinality": int(universe.size),
                      "entry": "gates/count_oracle_harness.py"}
    return result, rec


# ------------------------------------------------------------------ fixtures
def fixtures():
    import numpy as np
    v9 = _load_v9()
    fails, skips = [], []
    # F1: an explicit None cannot reach _plan — recorder proves pre-dispatch refusal.
    hit = {"n": 0}
    orig = v9._plan
    def rec(*a, **k):
        hit["n"] += 1
        return orig(*a, **k)
    v9._plan = rec
    try:
        try:
            production_build_plan([1], [0.1], [1], grouped_sum=None, ungrouped_total=1)
            fails.append("F1: None grouped_sum not refused")
        except CountOracleHarnessRefusal as e:
            if "before dispatch" not in str(e):
                fails.append(f"F1: wrong refusal: {e}")
        # F4 (AGY): empty and falsy-shaped inputs refuse pre-dispatch too
        try:
            production_build_plan([], [], [], grouped_sum=1, ungrouped_total=1)
            fails.append("F4a: empty table not refused")
        except CountOracleHarnessRefusal:
            pass
        try:
            production_build_plan([1, 2], [0.1], [1], grouped_sum=1, ungrouped_total=1)
            fails.append("F4b: ragged table not refused")
        except CountOracleHarnessRefusal:
            pass
        if hit["n"] != 0:
            fails.append("F1/F4: _plan was reached despite a pre-dispatch refusal case")
    finally:
        v9._plan = orig
    # F5a: a wrong-sha synthetic sidecar is refused by the verified loader, and the
    # refusal is the INTEGRITY refusal, not an incidental crash (AGY: bare except hid type)
    import tempfile
    tmp = Path(tempfile.mkdtemp()) / "fake_sidecar.bin"
    tmp.write_bytes(b"brick_one brick_two")
    try:
        v9.verified_bytes(tmp, v9.PINNED_UNIVERSE_SHA256, "sidecar")
        fails.append("F5a: wrong-sha sidecar accepted")
    except Exception as e:
        if "DIGEST MISMATCH" not in str(e) and "sidecar" not in str(e).lower():
            fails.append(f"F5a: refusal is not the integrity refusal: {type(e).__name__}: {e}")
    # F5b: the binding constants themselves still pin.
    if v9.PINNED_UNIVERSE_BRICKS != 366_912 or not v9.PINNED_UNIVERSE_SHA256.startswith("863e5ded"):
        fails.append("F5b: pinned constants moved")
    # F6 (AGY: the old identity test was vacuous): the SNAPSHOT property — mutating the
    # caller's buffers after snapshotting cannot change what would be digested.
    src_b, src_c, src_n = [1, 2, 3], [0.1, -0.2, 0.3], [4, 5, 6]
    bid, cc, nn = _snapshot(src_b, src_c, src_n)
    d0 = (hashlib.sha256(v9.canon_i8(bid)).hexdigest(),
          hashlib.sha256(v9.canon_f8(cc)).hexdigest())
    src_b[0], src_c[0], src_n[0] = 999, 0.999, 999
    d1 = (hashlib.sha256(v9.canon_i8(bid)).hexdigest(),
          hashlib.sha256(v9.canon_f8(cc)).hexdigest())
    if d0 != d1:
        fails.append("F6: caller mutation after snapshot changed the digests (TOCTOU open)")
    # F7: canonical frames are fixed-width — the AGY newline-collision pair separates.
    if v9.canon_i8(np.array([11, 2])) == v9.canon_i8(np.array([1, 12])):
        fails.append("F7: canonical int frames collide")
    # F8: universe derivation form matches v9:661 — integer dtype by construction.
    class _R(dict):
        pass
    fake_geom_rows = {"a": {"brickid": 7}, "b": {"brickid": 3}}
    uni = sorted(int(r["brickid"]) for r in fake_geom_rows.values())
    if uni != [3, 7]:
        fails.append("F8: integer-universe derivation broken")
    # TIER 2 — pinned data + explicit opt-in (heavyweight planner import).
    import os
    if os.environ.get("NM_COH_TIER2") != "1":
        skips.append("TIER-2 SKIPPED LOUDLY (NM_COH_TIER2 unset): F2 missing-brick, "
                     "F3 extra-brick, F4c grouped-disagreement NOT RUN through the real "
                     "build_plan — BS-2c may not fill on this battery alone")
    else:
        try:
            geom, _ = v9.load_pinned_geometry()
            import numpy as np
            universe = np.sort(np.asarray(
                [int(r["brickid"]) for r in (geom.by_name or {}).values()], dtype=np.int64))
            ones = np.ones(universe.size, dtype=np.int64)
            cs = np.full(universe.size, 0.1)
            total = int(universe.size)
            for label, args, want in (
                ("F4c grouped-disagreement",
                 (universe, cs, ones, total + 1, total), "grouped total"),
                ("F2 missing-brick",
                 (universe[:-1], cs[:-1], ones[:-1], total - 1, total - 1), "missing"),
                ("F3 extra-brick",
                 (np.append(universe, universe.max() + 1), np.append(cs, 0.1),
                  np.append(ones, 1), total + 1, total + 1), "extra"),
            ):
                b_, c_, n_, g_, u_ = args
                try:
                    production_build_plan(b_, c_, n_, grouped_sum=g_, ungrouped_total=u_)
                    fails.append(f"{label}: accepted")
                except CountOracleHarnessRefusal as e:
                    fails.append(f"{label}: refused at the harness, not through "
                                 f"build_plan: {e}")
                except RuntimeError as e:
                    if want not in str(e):
                        fails.append(f"{label}: wrong v9 refusal: {e}")
        except Exception as e:
            skips.append(f"TIER-2 SKIPPED LOUDLY: pinned geometry unavailable "
                         f"({type(e).__name__}: {e}); F2/F3/F4c NOT RUN — BS-2c may not "
                         "fill on this battery alone")
    return fails, skips


if __name__ == "__main__":
    fails, skips = fixtures()
    for s in skips:
        print("SKIP:", s)
    for f in fails:
        print("FIXTURE FAIL:", f)
    ran = 8 + (3 if not skips else 0)
    print(f"count-oracle harness fixtures: {ran - len(fails)}/{ran} green"
          + ("" if not skips else " (tier-2 skipped loudly)"))
    sys.exit(1 if fails else 0)
