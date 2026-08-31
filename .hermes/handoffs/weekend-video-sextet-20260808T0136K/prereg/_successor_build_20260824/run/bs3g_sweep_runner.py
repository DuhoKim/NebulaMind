#!/usr/bin/env python3
"""BS-3g sweep owner.  Production is 99x51; --selfcheck is only 2x5.

No receipt is written unless the real sealed mask, calibration, and measured
gamma pair all materialize.  In this build lane they do not; BLK codes name
the absent frozen inputs rather than replacing them with fixtures.
"""
import argparse
import hashlib
import json
import sys
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
sys.path[:0] = [str(HERE), str(BASE / "ref")]
from receipt_strict import ReceiptRefusal, receipt_strict  # noqa: E402

GAMMA = Decimal("0.25")
N_STEPS = 50
J0 = 25
N_DRAWS = 99
N_PERM = 200
MAPPING_ID = "MAPPING-A-CRN-PCG64-20260830-v1"
DRAW_GENERATOR_ID = "numpy-1.26.4-PCG64-default_rng"
DRAW_MASTER_SEED = 20260830

CODES = {
    "BR01": "gamma=0 baseline is not adjudicated",
    "BR02": "counterfactual cell refused outside the calibration boundary",
    "BR03": "receipt was not accepted by receipt_strict",
    "BLK01": "sealed 49,211-row BS-2f mask is absent",
    "BLK02": "real BS-8f calibration record is absent",
    "BLK03": "gamma_hat and sigma_gamma are unmeasured and have no authorized placeholder",
}


class RunnerRefusal(RuntimeError):
    def __init__(self, code, detail=""):
        self.code = code
        super().__init__(f"[{code}] {CODES[code]}" + (f": {detail}" if detail else ""))


def grid():
    return [(Decimal(j - J0) * GAMMA / Decimal(J0)) for j in range(N_STEPS + 1)]


def manifest_bytes(values):
    return "\n".join(format(x, "f").rstrip("0").rstrip(".") if x else "0"
                     for x in values).encode("utf-8")


def matrix_digest(matrix):
    b = json.dumps(matrix, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(b).hexdigest()


def reduce_row(row, zero_index):
    base = row[zero_index]
    if not isinstance(base, str) or not base.startswith("V:"):
        raise RunnerRefusal("BR01", repr(base))
    flips = sum(x.startswith("V:") and x != base for x in row)
    # INCAL is the admissibility boundary and is never counted as a flip.
    for x in row:
        if not (isinstance(x, str) and (x.startswith("V:") or x == "INCAL")):
            raise RunnerRefusal("BR02", repr(x))
    return base[2:], flips


def _candidate_skeleton():
    h = "0" * 64
    return {
        "mask_sha256": h, "calibration_sha256": h,
        "perturbation_manifest_sha256": h, "kernel_sha256": h,
        "estimator_sha256": h, "verifier_sha256": h, "mapping_id": MAPPING_ID,
        "gamma_hat": 0.1, "sigma_gamma": 0.01, "gamma_bound": 0.25,
        "invariance_outcome": "HELD", "n_perturbations": 51, "n_draws": 99,
        "draw_generator_id": DRAW_GENERATOR_ID, "draw_master_seed": DRAW_MASTER_SEED,
        "draw_verdict_digest": h, "baseline_verdict": "INCONCLUSIVE",
        "delta_gamma_max": 0.01, "counterfactual_path_sha256": h,
        "replay_harness_sha256": h,
    }


def fixtures():
    n = 0
    g = grid()
    assert len(g) == 51 and g[J0] == 0 and g[0] == -GAMMA and g[-1] == GAMMA; n += 1
    assert manifest_bytes(g).splitlines()[J0] == b"0"; n += 1
    base, flips = reduce_row(["V:INCONCLUSIVE", "INCAL", "V:INCONCLUSIVE"], 0)
    assert base == "INCONCLUSIVE" and flips == 0; n += 1
    _, flips = reduce_row(["V:INCONCLUSIVE", "V:REPRODUCED-LONGO"], 0)
    assert flips == 1; n += 1
    for code, row in (("BR01", ["INCAL"]), ("BR02", ["V:INCONCLUSIVE", "BOGUS"])):
        try:
            reduce_row(row, 0)
            raise AssertionError(f"{code} did not refuse")
        except RunnerRefusal as e:
            assert e.code == code
        n += 1
    try:
        env = receipt_strict("BS-3g", _candidate_skeleton())
        assert env["schema"] == "BS3G-V1"
    except ReceiptRefusal as e:
        raise RunnerRefusal("BR03", str(e))
    n += 1
    m = [["V:INCONCLUSIVE", "INCAL"], ["V:REPRODUCED-LONGO", "V:REPRODUCED-LONGO"]]
    assert matrix_digest(m) == matrix_digest(json.loads(json.dumps(m))); n += 1
    return n


def materialize_real_inputs():
    rec = json.loads((BASE / "acquire" / "positions_receipts.json").read_text())
    cut = BASE / "acquire" / "positions_selected_cut.csv"
    cut_rows = sum(1 for _ in cut.open()) - 1 if cut.exists() else 0
    raise RunnerRefusal(
        "BLK01", f"positions_receipts.json authenticates {rec.get('total_rows')} acquired "
        f"rows and the cut CSV contains {cut_rows} positions, but neither artifact carries "
        "the accepted signs, sealed boundaries, or BS-2f mask_digest needed to construct "
        "the frozen real mask")
    # These remain explicit guards if a future lane supplies the first artifact.
    raise RunnerRefusal("BLK02", "no a_hat/a_lb/per-bin/cov_a BS-8f artifact is on disk")


def selfcheck():
    n = fixtures()
    print(f"bs3g_sweep_runner fixtures: {n}/{n} PASS")
    try:
        materialize_real_inputs()
    except RunnerRefusal as e:
        print(f"SELFCHECK BLOCKED {e}")
        print("[BLK03] frozen V134 says gamma_hat/sigma_gamma are finite doubles and "
              "'gamma-hat remains unmeasured'; it gives no authorized placeholder")
        return 2
    raise RunnerRefusal("BLK03")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selfcheck", action="store_true")
    args = ap.parse_args()
    if not args.selfcheck:
        print("production 99x51 execution is prohibited in this build round; use --selfcheck",
              file=sys.stderr)
        return 2
    return selfcheck()


if __name__ == "__main__":
    raise SystemExit(main())
