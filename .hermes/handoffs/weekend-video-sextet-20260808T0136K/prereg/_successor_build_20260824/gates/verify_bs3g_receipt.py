#!/usr/bin/env python3
"""Independent, fixture-only verifier for the strict twenty-field BS-3g receipt."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import types
from decimal import Decimal
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent.parent
REF, RUN = BASE / "ref", BASE / "run"
sys.path[:0] = [str(BASE / "gates"), str(RUN), str(REF)]
import replay_harness as rh  # noqa: E402
from receipt_strict import receipt_strict, schema_entry_digest  # noqa: E402

PINS = {
    "kernel_sha256": (REF / "gain_gradient_kernel.py", "10dd6f62074f30a3d98ff3838c98463eb2574e99012b6db00d8454b1f25978ab"),
    "estimator_sha256": (REF / "gain_gradient_estimator.py", "e227029713396a920f76d33eed2383339dd0e566e1cdbb6818092ec4403727fd"),
    "verifier_sha256": (BASE / "gates" / "verify_mu_gamma.py", "e33d9275d80787437429af7aa5989f3b886a8d1a477eddd55459e2270e046d04"),
}
CELL_TOKENS = {"REPRODUCED-LONGO", "REJECTED-AT-LONGO-AMPLITUDE", "INCONCLUSIVE"}


class VerificationRefusal(RuntimeError):
    pass


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                      allow_nan=False).encode()


def decstr(x):
    s = format(x, "f").rstrip("0").rstrip(".")
    return s if s and s != "-0" else "0"


def unique(pattern, text, name):
    hits = re.findall(pattern, text)
    if not hits or len(set(hits)) != 1:
        raise VerificationRefusal(f"missing/ambiguous ruling for {name}: {sorted(set(hits))}")
    return hits[0]


def rules():
    d = (REF / "DRAW_MECHANICS_COMMIT_20260830.md").read_text()
    g = (BASE / "GAMMA_RATIFICATION_20260830.md").read_text()
    m = (BASE / "OPEN_QUESTION_GAIN_SIGN_MAPPING.md").read_text()
    c = (BASE / "MAPPING_CONFIRMATION_RULING_20260831.md").read_text()
    v = (BASE / "PREREG_SUCCESSOR_DRAFT_V136_20260903.md").read_text()
    nd = int(unique(r"`n_draws` \| \*\*(\d+)\*\*", d, "n_draws"))
    seed = int(unique(r"`draw_master_seed` \| \*\*(\d+)\*\*", d, "seed"))
    gen = unique(r"`draw_generator_id` \| \*\*`([^`]+)`\*\*", d, "generator")
    ns = int(unique(r"`n_steps` \| \*\*(\d+)\*\*", d, "n_steps"))
    gamma = Decimal(unique(r"That number is now ratified: \*\*Γ = ([0-9.]+)\*\*", g, "Gamma"))
    npv = int(unique(r"PRODUCTION permutation contract — `n_perm = ([0-9,]+)`", v, "n_perm").replace(",", ""))
    required = (("COMMON RANDOM", d), ("ZERO-BASED", d), ("option A", m),
                ("WORST CASE OVER DRAWS", m), ('option (b), "real gate"',
                 (BASE / "OPEN_QUESTION_T_COMPLETENESS.md").read_text()),
                ('a₀ = cal["a_hat"]', c), ("mean of the mask's c values", c),
                ("[0.5 + 1e-9, 1.0]", c), ("per-bin-means cal′", c))
    for phrase, source in required:
        if phrase not in source:
            raise VerificationRefusal(f"required ruling phrase absent: {phrase}")
    step = Decimal(2) * gamma / Decimal(ns)
    grid = [-gamma + Decimal(j) * step for j in range(ns + 1)]
    j0 = ns // 2
    if ns % 2 or decstr(grid[j0]) != "0":
        raise VerificationRefusal("non-canonical baseline")
    return nd, seed, gen, ns, gamma, step, grid, j0, npv


def mask_digest(mask):
    rec = {"scope": "FROZEN-FIXTURE", "kind": mask.kind,
           "brickid": mask.brickid.tolist(), "objid": mask.objid.tolist(),
           "c": [float(x).hex() for x in mask.c], "s": [int(x) for x in mask.s],
           "bin": mask.bin.tolist(), "accept": mask.accept.tolist(),
           "boundaries": None if mask.boundaries is None else
           [float(x).hex() for x in mask.boundaries]}
    return hashlib.sha256(canon(rec)).hexdigest()


def cal_digest(cal):
    rec = {k: ([float(x).hex() for x in np.asarray(v).reshape(-1)]
               if isinstance(v, np.ndarray) else float(v).hex()) for k, v in sorted(cal.items())}
    return hashlib.sha256(canon({"scope": "FROZEN-FIXTURE", "calibration": rec})).hexdigest()


def recompute(progress=False):
    nd, seed, gen, ns, gamma, step, grid, j0, n_perm = rules()
    for field, (path, expected) in PINS.items():
        if sha(path) != expected:
            raise VerificationRefusal(f"{field} pinned bytes moved")
    buffers = rh._read_and_verify()
    mods, saved = rh._compile_in_order(buffers)
    v9, gcp = mods["successor_ref_v9"], mods["gain_counterfactual_path"]
    try:
        v9.require_environment()
        mbuf, mpath, _ = buffers["gain_mapping_a"]
        mm = types.ModuleType("gain_mapping_a_independent_verifier")
        mm.__file__, mm._V9 = str(mpath), v9
        exec(compile(mbuf, str(mpath), "exec", dont_inherit=True, optimize=0), mm.__dict__)
        mm._V9 = v9
        mask, _ = gcp._fixture()
        if type(mask) is not v9.FixtureMask:
            raise VerificationRefusal("mask is not exact loaded FixtureMask type")
        cal = gcp._CAL
        ep = PINS["estimator_sha256"][0]
        ens = {"__name__": "gain_gradient_estimator_independent", "__file__": str(ep)}
        exec(compile(ep.read_bytes(), str(ep), "exec", dont_inherit=True, optimize=0), ens)
        cb = [float(mask.c[mask.bin == b].mean()) for b in range(v9.N_CAL_BINS)]
        est, bad = ens["estimate_gamma"](cal["a_b"], cal["cov_a"], cb)
        if bad or est is None:
            raise VerificationRefusal(f"estimator refusal: {bad}")
        kp = PINS["kernel_sha256"][0]
        kns = {"__name__": "gain_gradient_kernel_independent", "__file__": str(kp)}
        exec(compile(kp.read_bytes(), str(kp), "exec", dont_inherit=True, optimize=0), kns)
        if not np.isfinite(kns["kernel"](np.asarray(cal["a_b"])[mask.bin], mask.c)):
            raise VerificationRefusal("kernel returned non-finite")
        rh._JOURNAL.events.clear(); rh._JOURNAL.active = True
        matrix, memo = [], {}
        for i in range(nd):
            mapper = mm.make_mapping(i)
            row = []
            for gd in grid:
                gf = float(gd)
                sp, cp = mapper(gf, mask, cal)
                key = (sp.tobytes(), canon({k: np.asarray(v).tolist()
                       if isinstance(v, np.ndarray) else v for k, v in cp.items()}))
                if key not in memo:
                    result = gcp.evaluate_at(gf, mask, cal, mapper, stage=v9.STAGE_C,
                                             prefix=11, trial=3, n_perm=n_perm)
                    if result["verdict"] not in CELL_TOKENS:
                        raise VerificationRefusal("cell outside closed verdict vocabulary")
                    memo[key] = result["verdict"]
                row.append(memo[key])
            matrix.append(row)
            if progress:
                print(f"verify draw {i + 1}/{nd}", file=sys.stderr, flush=True)
        rh._JOURNAL.active = False
        stray, native = rh._census(rh._JOURNAL.events,
                                   {x[0] for x in rh.MANIFEST} |
                                   {"successor_ref_v9", "gain_counterfactual_path",
                                    "gain_mapping_a", "gain_gradient_estimator",
                                    "gain_gradient_kernel"})
        if stray or native:
            raise VerificationRefusal(f"load census mismatch: {stray}, {native}")
        for name, (_buf, path, got) in buffers.items():
            if sha(path) != got:
                raise VerificationRefusal(f"post-replay root mismatch: {name}")
        manifest = [decstr(x) for x in grid]
        baselines = [row[j0] for row in matrix]
        held = all(cell == row[j0] for row in matrix for cell in row)
        return {
            "mask_sha256": mask_digest(mask), "calibration_sha256": cal_digest(cal),
            "perturbation_manifest_sha256": hashlib.sha256("\n".join(manifest).encode()).hexdigest(),
            **{field: expected for field, (_path, expected) in PINS.items()},
            "mapping_id": mm.MAPPING_ID, "gamma_hat": est["gamma_hat"],
            "sigma_gamma": est["sigma_gamma"], "gamma_bound": decstr(gamma),
            "invariance_outcome": "HELD" if held else "FAILED",
            "n_perturbations": len(grid), "n_draws": len(matrix),
            "draw_generator_id": gen, "draw_master_seed": seed,
            "draw_verdict_digest": hashlib.sha256(
                "\n".join(c for row in matrix for c in row).encode()).hexdigest(),
            "baseline_verdict": baselines[0] if len(set(baselines)) == 1 else "PER-DRAW",
            "delta_gamma_max": decstr(step),
            "counterfactual_path_sha256": buffers["gain_counterfactual_path"][2],
            "replay_harness_sha256": sha(BASE / "gates" / "replay_harness.py"),
        }
    finally:
        rh._JOURNAL.active = False
        if saved is not None: sys.modules["successor_ref_v9"] = saved
        else: sys.modules.pop("successor_ref_v9", None)


def verify(path, progress=False):
    try:
        supplied = json.loads(path.read_text(), parse_constant=lambda x: (_ for _ in ()).throw(
            VerificationRefusal(f"non-finite JSON constant {x}")))
    except (OSError, json.JSONDecodeError) as e:
        raise VerificationRefusal(f"candidate unreadable: {e}") from e
    if schema_entry_digest("BS-3g") != "eb8589f5f70656b16dc8ba16e7d78677a0ab0da7b92cb54eddd22fef14e20102":
        raise VerificationRefusal("BS3G-V1 entry digest moved")
    if not isinstance(supplied, dict) or not isinstance(supplied.get("body"), dict):
        raise VerificationRefusal("candidate is not a strict receipt envelope")
    rebuilt = receipt_strict("BS-3g", supplied["body"])
    if rebuilt != supplied:
        raise VerificationRefusal("strict envelope/body digest mismatch")
    expected = recompute(progress)
    disagreements = [k for k in expected if supplied["body"].get(k) != expected[k]]
    if disagreements:
        raise VerificationRefusal(f"receipt field disagreement: {disagreements}")
    print(f"BS-3g receipt verifier: 20/20 fields PASS; outcome {expected['invariance_outcome']}")
    return expected


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate", type=Path)
    ap.add_argument("--progress", action="store_true")
    a = ap.parse_args()
    verify(a.candidate, a.progress)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except VerificationRefusal as e:
        print(f"REFUSED: {e}", file=sys.stderr)
        raise SystemExit(2)
