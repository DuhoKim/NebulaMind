#!/usr/bin/env python3
"""Fixture-only BS-3g producer.  Never accepts paths, modules, or callbacks."""
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
REF = BASE / "ref"
RUN = BASE / "run"
sys.path[:0] = [str(BASE / "gates"), str(RUN), str(REF)]

import replay_harness as harness  # noqa: E402
from receipt_strict import receipt_strict, schema_entry_digest  # noqa: E402

DRAW_RULE = REF / "DRAW_MECHANICS_COMMIT_20260830.md"
GAMMA_RULE = BASE / "GAMMA_RATIFICATION_20260830.md"
MAP_RULE = BASE / "OPEN_QUESTION_GAIN_SIGN_MAPPING.md"
CONVENTION_RULE = BASE / "MAPPING_CONFIRMATION_RULING_20260831.md"
V136 = BASE / "PREREG_SUCCESSOR_DRAFT_V136_20260903.md"

PINNED = {
    "kernel": (REF / "gain_gradient_kernel.py", "10dd6f62074f30a3d98ff3838c98463eb2574e99012b6db00d8454b1f25978ab"),
    "estimator": (REF / "gain_gradient_estimator.py", "e227029713396a920f76d33eed2383339dd0e566e1cdbb6818092ec4403727fd"),
    "verifier": (BASE / "gates" / "verify_mu_gamma.py", "e33d9275d80787437429af7aa5989f3b886a8d1a477eddd55459e2270e046d04"),
}
NUMERIC_TOKENS = {"REPRODUCED-LONGO", "REJECTED-AT-LONGO-AMPLITUDE", "INCONCLUSIVE"}


class BS3GRefusal(RuntimeError):
    pass


def _path_outcome(exc, v9):
    """Convert only §5's typed pre-statistic halts; every other path error refuses."""
    cause = exc.__cause__ or exc.__context__
    if exc.code == "P07" and isinstance(cause, v9.InconclusiveByCalibration):
        return "INCONCLUSIVE-BY-CALIBRATION"
    if exc.code == "P07" and isinstance(cause, v9.InconclusiveByPower):
        return "INCONCLUSIVE-BY-POWER"
    raise exc


def _one(pattern: str, text: str, label: str) -> str:
    hits = re.findall(pattern, text)
    if not hits:
        raise BS3GRefusal(f"ruling value absent: {label}")
    if len(set(hits)) != 1:
        raise BS3GRefusal(f"ruling value ambiguous: {label}: {sorted(set(hits))}")
    return hits[0]


def ruled_values():
    d = DRAW_RULE.read_text()
    g = GAMMA_RULE.read_text()
    m = MAP_RULE.read_text()
    c = CONVENTION_RULE.read_text()
    v = V136.read_text()
    # Every number/token below is parsed from its ruling record, never duplicated here.
    n_draws = int(_one(r"`n_draws` \| \*\*(\d+)\*\*", d, "n_draws"))
    seed = int(_one(r"`draw_master_seed` \| \*\*(\d+)\*\*", d, "draw_master_seed"))
    generator = _one(r"`draw_generator_id` \| \*\*`([^`]+)`\*\*", d, "draw_generator_id")
    n_steps = int(_one(r"`n_steps` \| \*\*(\d+)\*\*", d, "n_steps"))
    gamma = Decimal(_one(r"That number is now ratified: \*\*Γ = ([0-9.]+)\*\*", g, "Gamma"))
    n_perm = int(_one(r"PRODUCTION permutation contract — `n_perm = ([0-9,]+)`", v, "n_perm").replace(",", ""))
    if "COMMON RANDOM" not in d or "ZERO-BASED" not in d:
        raise BS3GRefusal("ruling value absent: CRN or zero-based addressing")
    if "option A" not in m or "WORST CASE OVER DRAWS" not in m:
        raise BS3GRefusal("ruling value absent: mapping-A worst-case reduction")
    if 'option (b), "real gate"' not in (BASE / "OPEN_QUESTION_T_COMPLETENESS.md").read_text():
        raise BS3GRefusal("ruling value absent: option-(b) real gate")
    for phrase in ('a₀ = cal["a_hat"]', "mean of the mask's c values",
                   "[0.5 + 1e-9, 1.0]", "per-bin-means cal′"):
        if phrase not in c:
            raise BS3GRefusal(f"confirmed convention absent: {phrase}")
    delta = (Decimal(2) * gamma) / Decimal(n_steps)
    grid = [-gamma + Decimal(j) * delta for j in range(n_steps + 1)]
    j0 = n_steps // 2
    if n_steps % 2 or grid[j0] != 0:
        raise BS3GRefusal("derived grid has no canonical central zero")
    return {"n_draws": n_draws, "seed": seed, "generator": generator,
            "n_steps": n_steps, "gamma": gamma, "delta": delta, "grid": grid,
            "j0": j0, "n_perm": n_perm}


def canonical_decimal(x: Decimal) -> str:
    s = format(x, "f").rstrip("0").rstrip(".")
    return s if s and s != "-0" else "0"


def canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode()


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load():
    if sys.flags.optimize != 0 or sys.pycache_prefix is not None:
        raise BS3GRefusal("replay flags are not optimize=0 / pycache_prefix=None")
    buffers = harness._read_and_verify()
    mods, saved = harness._compile_in_order(buffers)
    v9, gcp = mods["successor_ref_v9"], mods["gain_counterfactual_path"]
    v9.require_environment()
    mbuf, mpath, _ = buffers["gain_mapping_a"]
    mapping = types.ModuleType("gain_mapping_a")
    mapping.__file__ = str(mpath)
    mapping._V9 = v9
    exec(compile(mbuf, str(mpath), "exec", dont_inherit=True, optimize=0), mapping.__dict__)
    mapping._V9 = v9
    return buffers, mods, mapping, saved


def _fixture_digest(mask) -> str:
    record = {"scope": "FROZEN-FIXTURE", "kind": mask.kind,
              "brickid": mask.brickid.tolist(), "objid": mask.objid.tolist(),
              "c": [float(x).hex() for x in mask.c], "s": [int(x) for x in mask.s],
              "bin": mask.bin.tolist(), "accept": mask.accept.tolist(),
              "boundaries": None if mask.boundaries is None else
              [float(x).hex() for x in mask.boundaries]}
    return hashlib.sha256(canonical(record)).hexdigest()


def _cal_digest(cal) -> str:
    record = {k: ([float(x).hex() for x in np.asarray(v).reshape(-1)]
                  if isinstance(v, np.ndarray) else float(v).hex())
              for k, v in sorted(cal.items())}
    return hashlib.sha256(canonical({"scope": "FROZEN-FIXTURE", "calibration": record})).hexdigest()


def compute_fields(progress=False, diagnostics=None):
    rv = ruled_values()
    for name, (path, want) in PINNED.items():
        if _sha(path) != want:
            raise BS3GRefusal(f"pinned {name} digest mismatch")
    buffers, mods, mapping, saved = _load()
    v9, gcp = mods["successor_ref_v9"], mods["gain_counterfactual_path"]
    try:
        mask, _ = gcp._fixture()
        if type(mask) is not v9.FixtureMask:
            raise BS3GRefusal("fixture mask is not type-exact")
        cal = gcp._CAL
        # The pinned estimator is loaded from its verified buffer and really executed.
        ep = PINNED["estimator"][0]
        ens = {"__name__": "gain_gradient_estimator", "__file__": str(ep)}
        exec(compile(ep.read_bytes(), str(ep), "exec", dont_inherit=True, optimize=0), ens)
        c_bar = [float(mask.c[mask.bin == b].mean()) for b in range(v9.N_CAL_BINS)]
        estimate, bad = ens["estimate_gamma"](cal["a_b"], cal["cov_a"], c_bar)
        if bad or estimate is None:
            raise BS3GRefusal(f"estimator refused fixture: {bad}")
        # Execute the pinned kernel's pure kernel function on the same fixture geometry.
        kp = PINNED["kernel"][0]
        kns = {"__name__": "gain_gradient_kernel", "__file__": str(kp)}
        exec(compile(kp.read_bytes(), str(kp), "exec", dont_inherit=True, optimize=0), kns)
        q = np.asarray(cal["a_b"])[mask.bin]
        kval = kns["kernel"](q, mask.c)
        if not np.isfinite(kval):
            raise BS3GRefusal("kernel returned non-finite fixture value")
        harness._JOURNAL.events.clear()
        harness._JOURNAL.active = True
        matrix = []
        cache = {}
        inconclusive_cells = []
        min_a_lb_b = float("inf")
        for i in range(rv["n_draws"]):
            mp = mapping.make_mapping(i)
            row = []
            for gd in rv["grid"]:
                gamma = float(gd)
                s_prime, cal_prime = mp(gamma, mask, cal)
                if isinstance(cal_prime, dict) and "a_lb_b" in cal_prime:
                    min_a_lb_b = min(min_a_lb_b, float(np.min(cal_prime["a_lb_b"])))
                key = (s_prime.tobytes(), canonical({k: (np.asarray(v).tolist()
                       if isinstance(v, np.ndarray) else v) for k, v in cal_prime.items()}))
                if key not in cache:
                    try:
                        out = gcp.evaluate_at(gamma, mask, cal, mp, stage=v9.STAGE_C,
                                              prefix=11, trial=3, n_perm=rv["n_perm"])
                    except gcp.PathRefusal as e:
                        cache[key] = _path_outcome(e, v9)
                    else:
                        if out["verdict"] not in NUMERIC_TOKENS:
                            raise BS3GRefusal(
                                f"non-production numeric verdict token: {out['verdict']!r}")
                        cache[key] = out["verdict"]
                token = cache[key]
                row.append(token)
                if token.startswith("INCONCLUSIVE-BY-"):
                    inconclusive_cells.append((i, len(row) - 1, canonical_decimal(gd), token))
            matrix.append(row)
            if progress:
                print(f"draw {i + 1}/{rv['n_draws']}", file=sys.stderr, flush=True)
        harness._JOURNAL.active = False
        stray, native = harness._census(harness._JOURNAL.events,
                                        {x[0] for x in harness.MANIFEST} |
                                        {"successor_ref_v9", "gain_counterfactual_path",
                                         "gain_mapping_a", "gain_gradient_estimator",
                                         "gain_gradient_kernel"})
        if stray or native:
            raise BS3GRefusal(f"loaded-object census refusal: {stray}, {native}")
        for name, (_buf, path, got) in buffers.items():
            if _sha(path) != got:
                raise BS3GRefusal(f"root changed after replay: {name}")
        manifest = [canonical_decimal(x) for x in rv["grid"]]
        verdict_bytes = "\n".join(x for row in matrix for x in row).encode()
        baselines = [row[rv["j0"]] for row in matrix]
        held = all(x == row[rv["j0"]] for row in matrix for x in row)
        if diagnostics is not None:
            diagnostics.update({
                "inconclusive_cells": inconclusive_cells,
                "inconclusive_count": len(inconclusive_cells),
                "total_cells": len(matrix) * len(manifest),
                "first_inconclusive": inconclusive_cells[0] if inconclusive_cells else None,
                "min_a_lb_b": min_a_lb_b,
            })
        fields = {
            "mask_sha256": _fixture_digest(mask), "calibration_sha256": _cal_digest(cal),
            "perturbation_manifest_sha256": hashlib.sha256("\n".join(manifest).encode()).hexdigest(),
            "kernel_sha256": PINNED["kernel"][1], "estimator_sha256": PINNED["estimator"][1],
            "verifier_sha256": PINNED["verifier"][1], "mapping_id": mapping.MAPPING_ID,
            "gamma_hat": estimate["gamma_hat"], "sigma_gamma": estimate["sigma_gamma"],
            "gamma_bound": canonical_decimal(rv["gamma"]),
            "invariance_outcome": "HELD" if held else "FAILED",
            "n_perturbations": len(manifest), "n_draws": len(matrix),
            "draw_generator_id": rv["generator"], "draw_master_seed": rv["seed"],
            "draw_verdict_digest": hashlib.sha256(verdict_bytes).hexdigest(),
            "baseline_verdict": baselines[0] if len(set(baselines)) == 1 else "PER-DRAW",
            "delta_gamma_max": canonical_decimal(rv["delta"]),
            "counterfactual_path_sha256": buffers["gain_counterfactual_path"][2],
            "replay_harness_sha256": _sha(BASE / "gates" / "replay_harness.py"),
        }
        if schema_entry_digest("BS-3g") != "eb8589f5f70656b16dc8ba16e7d78677a0ab0da7b92cb54eddd22fef14e20102":
            raise BS3GRefusal("BS3G-V1 schema entry digest mismatch")
        return fields
    finally:
        harness._JOURNAL.active = False
        if saved is not None:
            sys.modules["successor_ref_v9"] = saved
        else:
            sys.modules.pop("successor_ref_v9", None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    ap.add_argument("--progress", action="store_true")
    a = ap.parse_args()
    envelope = receipt_strict("BS-3g", compute_fields(a.progress))
    payload = json.dumps(envelope, sort_keys=True, indent=2, ensure_ascii=False,
                         allow_nan=False) + "\n"
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(payload)
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
