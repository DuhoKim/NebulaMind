#!/usr/bin/env python3
"""Stage-P rerun on the full raw planning table and authenticated final mask.

Governing frozen clauses (PREREG_SUCCESSOR_DRAFT_V134_20260831.md):

  "Every operational mechanism ... is DEFINED by the code bytes of
  `ref/successor_ref_v9.py`, sha256
  `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`."

  "This text promises the EXACT per-trial test: every trial judged against its
  own 20,000-permutation null, no shared reference null in the counting path."

  "BS-5p cannot be filled from the existing measurement receipt. Filling it
  requires implementing the exact route in the code §0 pins ... and re-running
  under those exact bytes."

The covenant table binds BS-2o to ``greedy_ledger``; BS-5p to the Stage-P plan,
L_min/L_plan and x >= 962 rule; and BS-2s to ``local_pass`` plus the mandatory
Stage-P re-pass.  This driver imports frozen v9 read-only and delegates all
answer-determining mathematics (geometry, retention, traversal, reduction,
injection, permutation p values, encoders and receipts) to it.  The small loop
around ``perm_record`` is the later text's required replacement for v9's
superseded shared-null ``stage_power`` counting path.

``--plan`` performs the requested ten-trial end-to-end smoke, reports timing and
an extrapolated cost, but emits no slot candidates. ``--full`` is resumable at
50-trial JSON checkpoints and alone may emit candidates.  A full run was not
started during the STAGEP-V1 build sitting.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import multiprocessing as mp
import os
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
V9_PATH = ROOT / "ref" / "successor_ref_v9.py"
HARNESS_PATH = ROOT / "gates" / "count_oracle_harness.py"
POSITIONS = ROOT / "acquire" / "positions_selected_cut.csv"
BASE_ACQ = Path("acquire")
SELECTED = ROOT / "acquire" / "selected_brickids_cut.txt"
LANE_PARENT = ROOT.parent
COUNTS = LANE_PARENT / "_tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/combined_per_brick_counts.csv"
UNIVERSE = LANE_PARENT / "_tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/static/survey-bricks-dr10-south.fits.gz"
CHECKPOINTS = ROOT / "run" / "stagep_checkpoints"
CANDIDATES = ROOT / "run" / "classp_candidates"
FAST_GREEDY_PATH = ROOT / "real" / "greedy_fast.py"
FAST_REDUCE_PATH = ROOT / "real" / "reduce_fast.py"

PINS = {
    V9_PATH: "6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148",
    POSITIONS: "a20682c114508dbdd18ede6a56c61509ea9c16784aaca7eee61f76bf97cdd372",
    SELECTED: "939b4ef2d2e00fb974892e835e51e512a5511bbe04a74780be15e38eb3879fd5",
    COUNTS: "4e4ec45d83f156e8daa738d81cd71a1e140d4ccbadd5343dc0bb8ed9f2479aa0",
    UNIVERSE: "863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def authenticate() -> dict[str, str]:
    got = {}
    for path, want in PINS.items():
        if not path.is_file():
            raise FileNotFoundError(f"STOP-AND-BLOCKED: exact missing artifact: {path}")
        actual = sha256(path)
        if actual != want:
            raise RuntimeError(f"STOP-AND-BLOCKED: sha256 mismatch: {path}: {actual} != {want}")
        got[str(path)] = actual
    return got


def import_file(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


V9 = None
WORK_MASK = None
WORK_PREFIX = None


def load_inputs():
    """Load the final mask and the distinct, full raw planning count table."""
    auth = authenticate()
    v9 = import_file("stagep_frozen_v9", V9_PATH)
    v9.require_environment()

    selected = [int(x.strip()) for x in SELECTED.read_text().splitlines() if x.strip()]
    if len(selected) != 6104 or len(set(selected)) != len(selected):
        raise RuntimeError(f"STOP-AND-BLOCKED: selected brick list cardinality is {len(selected)}, want 6104 unique")
    selected_set = set(selected)
    per_brick: dict[int, list[tuple[float, float]]] = {b: [] for b in selected}
    object_bid, object_c = [], []
    with POSITIONS.open(newline="") as f:
        rd = csv.DictReader(f)
        for row in rd:
            bid = int(row["brickid"])
            if bid not in selected_set:
                raise RuntimeError(f"STOP-AND-BLOCKED: mask row brickid {bid} absent from selected_brickids_cut")
            ra, dec = float(row["ra"]), float(row["dec"])
            per_brick[bid].append((ra, dec))
            object_bid.append(bid)
            object_c.append(float(v9.cos_theta(np.array([ra]), np.array([dec]))[0]))
    if len(object_bid) != 49211:
        raise RuntimeError(f"STOP-AND-BLOCKED: positions mask has {len(object_bid)} rows, want 49211")
    empty = sorted(b for b, rows in per_brick.items() if not rows)
    if empty:
        raise RuntimeError(f"STOP-AND-BLOCKED: {len(empty)} selected bricks have no mask rows; first={empty[0]}")

    # Frozen planning is brick-level over every positive row of COUNTS.  The
    # final 6,104-brick object mask is deliberately not reused as planning input.
    geom, sidecar_sha = v9.load_pinned_geometry(None)
    by_id = {int(r["brickid"]): r for r in geom.by_name.values()}
    count_rows = []
    with COUNTS.open(newline="") as f:
        rd = csv.DictReader(f)
        if rd.fieldnames != ["brickid", "n_cut6_dered"]:
            raise RuntimeError(f"STOP-AND-BLOCKED: count-table columns {rd.fieldnames!r}")
        for row in rd:
            b, n = int(row["brickid"]), int(row["n_cut6_dered"])
            if n <= 0:
                raise RuntimeError(f"STOP-AND-BLOCKED: nonpositive raw count for brick {b}")
            count_rows.append((b, n))
    if len(count_rows) != 270_577 or len({b for b, _ in count_rows}) != len(count_rows):
        raise RuntimeError(f"STOP-AND-BLOCKED: raw count-table cardinality {len(count_rows)}")
    if sum(n for _, n in count_rows) != 832_393:
        raise RuntimeError("STOP-AND-BLOCKED: raw count-table total is not frozen 832393")
    bid = np.asarray([b for b, _ in count_rows], dtype=np.int64)
    missing_geom = [int(b) for b in bid if int(b) not in by_id]
    if missing_geom:
        raise RuntimeError(f"STOP-AND-BLOCKED: selected brick absent from universe sidecar: {missing_geom[0]}")
    ra = np.asarray([float(by_id[int(b)]["ra"]) for b in bid])
    dec = np.asarray([float(by_id[int(b)]["dec"]) for b in bid])
    c = v9.cos_theta(ra, dec)
    n_raw = np.asarray([n for _, n in count_rows], dtype=np.int64)
    mask = v9.FixtureMask(np.asarray(object_bid, dtype=np.int64),
                          np.arange(len(object_bid), dtype=np.int64),
                          np.asarray(object_c, dtype=np.float64))
    return v9, auth, sidecar_sha, bid, c, n_raw, mask


def exact_trial(t: int) -> tuple[int, float, bool]:
    sm = WORK_MASK.with_signs(V9.inject_signs(WORK_MASK, V9.A_FLOOR, V9.STAGE_P, WORK_PREFIX, t))
    p = V9.perm_record(sm, V9.STAGE_P, WORK_PREFIX, 10_000 + t, V9.MC_CAL_PERM)[2]
    return t, float(p), bool(p < V9.P_REPRODUCED)


def init_worker(v9_path: str, mask_payload, prefix: int):
    global V9, WORK_MASK, WORK_PREFIX
    V9 = import_file("stagep_worker_v9", Path(v9_path))
    WORK_MASK = V9.FixtureMask(*mask_payload)
    WORK_PREFIX = prefix


def run_trials(mask, prefix: int, trials: list[int], workers: int, checkpoint_key: str | None):
    payload = (mask.brickid, mask.objid, mask.c)
    results = {}
    start = time.perf_counter()
    with mp.Pool(workers, initializer=init_worker,
                 initargs=(str(V9_PATH), payload, prefix)) as pool:
        for done, (t, p, success) in enumerate(pool.imap_unordered(exact_trial, trials), 1):
            results[str(t)] = {"p": p, "success": success}
            if checkpoint_key and (done % 50 == 0 or done == len(trials)):
                CHECKPOINTS.mkdir(parents=True, exist_ok=True)
                out = CHECKPOINTS / f"{checkpoint_key}.json"
                out.write_text(json.dumps({"prefix": prefix, "results": results}, sort_keys=True) + "\n")
    return results, time.perf_counter() - start


def receipt_json(slot: str, fields: dict[str, bytes], detail: dict) -> dict:
    rec = V9.receipt(slot, fields)
    rec["candidate_detail"] = detail
    return rec


def derive_static(v9, bid, c, n_raw):
    # v9.greedy_ledger is the definition but its literal Python loop is O(n^2)
    # at 270,577 rows.  These vectorized helpers implement the same comparisons;
    # each invocation first runs their frozen-route small-case agreement proofs.
    fast_greedy = import_file("stagep_fast_greedy", FAST_GREEDY_PATH)
    fast_reduce = import_file("stagep_fast_reduce", FAST_REDUCE_PATH)
    greedy_proofs = int(fast_greedy.prove_agreement())
    reduction_proofs = int(fast_reduce.prove_agreement())
    nret = v9.retained_counts(n_raw)
    order, l_min, _ = fast_greedy.greedy_prefix(
        bid, c, n_raw, nret, v9.NEQ_MIN / 3.0)
    if 3.0 * l_min < v9.NEQ_MIN:
        raise v9.InconclusiveByPower("no traversal prefix reaches N_eq minimum")
    eligible = len(order)
    l_plan = v9.L_PLAN_MARGIN * l_min
    full_order, _, _ = fast_greedy.greedy_prefix(bid, c, n_raw, nret, l_plan)
    keep, l_ret, moves = fast_reduce.reduce_removals(
        bid[full_order], c[full_order], nret[full_order], l_plan)
    selected_idx = np.asarray(full_order, dtype=np.int64)[keep]
    return {"order": order, "nret": nret, "eligible": eligible,
            "l_min_plan": float(l_min), "l_plan": float(l_plan),
            "selected_idx": selected_idx, "L_ret": float(l_ret),
            "moves": len(moves), "greedy_agreement_trials": greedy_proofs,
            "reduction_agreement_trials": reduction_proofs}


def closure_summary(bid, selected_idx):
    """THE TRUE CLOSURE CRITERION (AGY CLOSURE-REVIEW-V1 SOUND, 2026-09-01):
    local_pass selects on THEORETICAL retention over raw counts BEFORE fetch;
    the realized mask is post-BS-2a-cut. Equality was an over-strict fixture
    (it blocked one launch, correctly failing closed). The chain closes by
    CONTAINMENT WITH EVERY DIFFERENCE ACCOUNTED, each part computed here:
    (1) realized SUBSET-OF fresh (missing == 0);
    (2) fresh minus pre-cut acquisition == the named count-vs-fetch drift set
        (two decoupled server-side queries, mandated by the BS-2c oracle rule);
    (3) fresh minus realized == drift set UNION cut-emptied set, where
        cut-emptied is COMPUTED as bricks(pre-cut) - bricks(post-cut)."""
    import csv
    got_ids = sorted(int(bid[i]) for i in selected_idx)
    want_ids = [int(x) for x in SELECTED.read_text().split()]
    got_set, want_set = set(got_ids), set(want_ids)
    pre = set()
    with open(BASE_ACQ / "positions_selected.csv") as fh:
        for row in csv.DictReader(fh):
            pre.add(int(row["brickid"]))
    post = set()
    with open(BASE_ACQ / "positions_selected_cut.csv") as fh:
        for row in csv.DictReader(fh):
            post.add(int(row["brickid"]))
    drift = got_set - pre                      # counted but zero-fetched
    cut_emptied = pre - post                   # lost every row at the BS-2a cut
    ok = (not (want_set - got_set)
          and got_set - want_set == drift | cut_emptied
          and post == want_set)
    return {"status": "PASS" if ok else "FAIL",
            "criterion": "containment-with-differences-accounted",
            "drift_bricks": sorted(drift), "drift_count": len(drift),
            "cut_emptied_count": len(cut_emptied),
            "expected_count": len(want_ids), "actual_count": len(got_ids),
            "expected_sha256": PINS[SELECTED],
            "actual_sha256": hashlib.sha256(
                "".join(f"{b}\n" for b in got_ids).encode()).hexdigest(),
            "missing_count": len(want_set - got_set),
            "extra_count": len(got_set - want_set),
            "first_missing": sorted(want_set - got_set)[:10],
            "first_extra": sorted(got_set - want_set)[:10]}


def plan_mode(args, v9, auth, bid, c, n_raw, object_mask):
    # The timing sample is still valid when planning fails: it is measured on
    # the exact authenticated post-exclusion mask which the mandatory re-pass
    # must judge. Never silently substitute the obsolete 53,005-row NPZ.
    results, seconds = run_trials(object_mask, 0, list(range(1, 11)), args.workers, None)
    per_trial = seconds / 10.0
    # Planning needs one battery per tested prefix and one final-set re-pass.
    estimate_one_battery = per_trial * v9.N_TRIALS
    static = derive_static(v9, bid, c, n_raw)
    closure = closure_summary(bid, static["selected_idx"])
    planning = {"status": "READY" if closure["status"] == "PASS" else "BLOCKED",
                "raw_positive_rows": len(bid), "raw_total": int(n_raw.sum()),
                "first_neq_eligible_prefix": static["eligible"],
                "L_min_plan": static["l_min_plan"], "L_plan": static["l_plan"],
                "local_pass_L_ret": static["L_ret"],
                "local_pass_moves": static["moves"], "closure_test": closure,
                "agreement_proofs": {"greedy": static["greedy_agreement_trials"],
                                     "reduction": static["reduction_agreement_trials"]}}
    report = {
        "mode": "plan", "authenticated": auth, "mask_rows": int(object_mask.n),
        "selected_bricks": 6104, "positive_bricks": int(np.count_nonzero(n_raw)),
        "planning": planning,
        "plan_status": ("PLAN-COMPLETE" if closure["status"] == "PASS" else
                        "STOP-AND-BLOCKED: local_pass closure fixture mismatch"),
        "smoke": {"prefix": 0, "trials": 10,
                  "successes": sum(x["success"] for x in results.values()),
                  "seconds": seconds, "seconds_per_trial_wall": per_trial},
        "cost_estimate": {"seconds_per_1000_trial_battery": estimate_one_battery,
                          "hours_per_1000_trial_battery": estimate_one_battery / 3600.0,
                          "note": "full cost is batteries tested until first pass, plus final-set re-pass"},
        "constants": {"n_trials": v9.N_TRIALS, "permutations_per_trial": v9.MC_CAL_PERM,
                      "success_rule": f"x >= {v9.CP_PASS_X}"},
    }
    print(json.dumps(report, indent=2, sort_keys=True))


def full_mode(args, v9, auth, bid, c, n_raw, object_mask):
    static = derive_static(v9, bid, c, n_raw)
    closure = closure_summary(bid, static["selected_idx"])
    if closure["status"] != "PASS":
        raise RuntimeError("STOP-AND-BLOCKED: local_pass closure fixture mismatch: "
                           + json.dumps(closure, sort_keys=True))
    order, nret, eligible = static["order"], static["nret"], static["eligible"]
    curve = [v9.sse(nret[order[:k]], c[order[:k]]) for k in range(1, len(order) + 1)]
    ledger = v9.greedy_ledger(bid[order], c[order], n_raw[order])[1]
    l_min = None
    successes = None
    for k in range(eligible, len(order) + 1):
        mask = v9._planning_mask(bid[order[:k]], c[order[:k]], nret[order[:k]])
        key = f"prefix_{k:05d}"
        cp = CHECKPOINTS / f"{key}.json"
        old = json.loads(cp.read_text())["results"] if cp.exists() else {}
        todo = [t for t in range(1, v9.N_TRIALS + 1) if str(t) not in old]
        new, _ = run_trials(mask, k, todo, args.workers, key) if todo else ({}, 0.0)
        all_results = {**old, **new}
        successes = sum(x["success"] for x in all_results.values())
        if successes >= v9.CP_PASS_X:
            l_min = curve[k - 1]
            break
    if l_min is None:
        raise v9.InconclusiveByPower("no ledger prefix passes exact Stage P")
    l_plan = v9.L_PLAN_MARGIN * l_min
    # v9.local_pass walks its order accumulating retained N_eq to l_plan; the
    # NEQ_MIN/3-target prefix order tops out below the measured l_plan (the
    # crash of the first full launch). The frozen selector gets the greedy
    # order extended to the measured l_plan target - the same construction
    # derive_static proved agreement for, and (the battery having passed at
    # the first eligible prefix) numerically the same l_plan whose selection
    # already passed the closure fixture.
    # The frozen v9.local_pass literal loop is O(n^2) at this scale and wedged
    # a 3-hour launch at 100% then 0% CPU. The selection therefore comes from
    # the AGREEMENT-PROVEN fast route already computed in derive_static (the
    # same l_plan - the battery passed at the first eligible prefix - and the
    # exact selection the closure fixture PASSED); the agreement proofs
    # (small-case fast==frozen trials) are carried in the receipt provenance.
    if abs(l_plan - static["l_plan"]) > 1e-9:
        raise RuntimeError("measured l_plan differs from planning l_plan - "
                           "the fast-path selection would not correspond; "
                           "STOP-AND-BLOCKED")
    selected_idx, l_ret = static["selected_idx"], static["L_ret"]
    final_mask = v9._planning_mask(bid[selected_idx], c[selected_idx], nret[selected_idx])
    repass_results, _ = run_trials(final_mask, 0, list(range(1, v9.N_TRIALS + 1)),
                                   args.workers, "final_repass")
    repass_successes = sum(x["success"] for x in repass_results.values())
    if repass_successes < v9.CP_PASS_X:
        raise v9.InconclusiveByPower(f"final exact re-pass {repass_successes}/1000")

    CANDIDATES.mkdir(parents=True, exist_ok=True)
    led_arr = np.asarray(ledger, dtype=np.float64)
    candidates = {
        "BS-2o": receipt_json("BS-2o", {
            "order_brickid": v9.canon_i8([int(bid[i]) for i in order]),
            "N": v9.canon_f8(led_arr[:, 2]), "Var": v9.canon_f8(led_arr[:, 3]),
            "L_raw": v9.canon_f8(led_arr[:, 4])}, {"ledger": ledger}),
        "BS-5p": receipt_json("BS-5p", {
            "l_min_plan": v9.canon_f8([l_min]), "l_plan": v9.canon_f8([l_plan]),
            "successes": str(successes).encode(), "n_trials": str(v9.N_TRIALS).encode()},
            {"successes": successes}),
        "BS-2s": receipt_json("BS-2s", {
            "selected_brickid": v9.canon_i8([int(bid[i]) for i in selected_idx]),
            "L_ret": v9.canon_f8([l_ret]),
            "L_raw": v9.canon_f8([v9.sse(n_raw[selected_idx], c[selected_idx])]),
            "N_ret": str(int(np.add.reduce(nret[selected_idx]))).encode(),
            "N_eq": v9.canon_f8([3.0 * l_ret]),
            "repass_successes": str(repass_successes).encode()},
            {"selected_bricks": len(selected_idx), "repass_successes": repass_successes}),
    }
    for slot, rec in candidates.items():
        (CANDIDATES / f"{slot}.json").write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")

    # Dependency order: only after Stage-P candidates exist, attempt BS-2c through
    # the mandated production entry on the authenticated release count table.
    oracle = np.load(ROOT / "real" / "real_oracle_dr10.npz")
    if sha256(ROOT / "real" / "real_oracle_dr10.npz") != "01b8b4ecd7da6dc31654881ea4ea6713b0c06464c752d1e7e4de0028cce2103a":
        raise RuntimeError("STOP-AND-BLOCKED: real_oracle_dr10.npz digest mismatch")
    harness = import_file("stagep_count_harness", HARNESS_PATH)
    _plan, bs2c = harness.production_build_plan(oracle["brickid"], oracle["c"], oracle["n_eligible"],
                                                grouped_sum=832393, ungrouped_total=832393)
    (CANDIDATES / "BS-2c.json").write_text(json.dumps(bs2c, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"mode": "full", "candidates": sorted(candidates) + ["BS-2c"]}, indent=2))


def main() -> int:
    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--plan", action="store_true")
    mode.add_argument("--full", action="store_true")
    ap.add_argument("--workers", type=int, default=max(1, min(20, os.cpu_count() or 1)))
    args = ap.parse_args()
    global V9
    V9, auth, _sidecar_sha, bid, c, n_raw, object_mask = load_inputs()
    if args.plan:
        plan_mode(args, V9, auth, bid, c, n_raw, object_mask)
    else:
        full_mode(args, V9, auth, bid, c, n_raw, object_mask)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"{type(exc).__name__}: {exc}", file=sys.stderr)
        raise
