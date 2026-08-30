#!/usr/bin/env python3
"""gain_mapping_a — THE EXECUTABLE MAPPING A, the artifact whose absence kept
`mapping_id = MAPPING-NOT-PREREGISTERED` and blocked BS-3g -> BS-6 (CODEX-V112 F7).

THE RULED MODEL (principal, 2026-08-29, OPEN_QUESTION_GAIN_SIGN_MAPPING.md — option A):
position-dependent accuracy  a_gamma(c) = a0 + gamma * (c - c_bar),  signs REDRAWN under
it, the same shape production already uses in `inject_signs`; reduced to one verdict by
WORST CASE OVER DRAWS.

THE COMMITTED DRAW MECHANICS (ref/DRAW_MECHANICS_COMMIT_20260830.md, incl. Amendments 1-2):
  n_draws = 99 · master seed 20260830 · numpy default_rng over
  SeedSequence(20260830).spawn(99)[i], ZERO-BASED i in [0, 98] · COMMON RANDOM variates —
  one uniform stream per draw across every gamma, so a flip is the gradient's doing · the
  grid is the caller's ratified 51-point manifest (gamma_25 = 0 exactly).

WHAT THIS MODULE FIXES BY CONSTRUCTION, stated so the referee attacks the right things:
  * a0 = float(cal["a_hat"]) — the measured accuracy is the intercept; c_bar = mean(mask.c).
  * The per-draw uniforms are materialized ONCE per (draw, n) in production CONSUMPTION
    ORDER — object k uses u[2k] for the latent and u[2k+1] for the flip, exactly
    `inject_signs`' two sequential rng.random() calls per object — and CACHED, so every
    gamma of one draw sees identical variates (CRN as committed).
  * PHYSICAL CLAMP, a modelling choice said plainly: a_gamma(c) is clipped into
    [0.5 + 1e-9, 1.0]. Production's inject_signs REFUSES accuracy outside (0.5, 1]; the
    counterfactual's contract is a VERDICT at every ratified gamma, not a crash, and the
    ratified range was chosen so the calibration gate (not an exception) is what reacts
    to steep gradients. The clip fraction per call is exposed in `last_diagnostics`.
  * cal' carries the SAME PERTURBATION the signs saw: per-bin a_b' = clip(mean of
    a_gamma over the bin's objects); each bin's measured margin is preserved
    (a_lb_b' = a_b' - (a_b - a_lb_b)); a_hat'/a_lb' likewise; sigma_a and cov_a
    unchanged — the hypothesis moves the accuracy field, not the measurement noise.
  * No degeneracy patching: a variance-zero redraw is left for the path checker's P05,
    never silently repaired (the _TEST_ONLY mapping's s[0] flip is exactly what this
    module must NOT do).

MAPPING IDENTITY: MAPPING_ID below + this file's sha256 (pinned at gate time). The module
refuses spawn addressing outside [0, 98] and refuses a mask whose size changes mid-draw
(that would break CRN).
"""
import hashlib
import sys
from pathlib import Path

import numpy as np

MAPPING_ID = "MAPPING-A-CRN-PCG64-20260830-v1"
MASTER_SEED = 20260830
N_DRAWS = 99
A_CLIP_LO = 0.5 + 1e-9
A_CLIP_HI = 1.0

HERE = Path(__file__).resolve().parent
_V9 = None


def _v9():
    global _V9
    if _V9 is None:
        import importlib.util
        p = HERE / "successor_ref_v9.py"
        spec = importlib.util.spec_from_file_location("successor_ref_v9", p)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        _V9 = m
    return _V9


class MappingA:
    """One committed draw's mapping callback: mapping(gamma, mask, cal) -> (s', cal')."""

    def __init__(self, draw_index):
        if not (0 <= int(draw_index) < N_DRAWS):
            raise RuntimeError(
                f"draw index {draw_index} outside the committed zero-based [0, {N_DRAWS - 1}]")
        self.draw_index = int(draw_index)
        self._u = None
        self._n = None
        self.last_diagnostics = None

    def _uniforms(self, n):
        if self._u is None:
            child = np.random.SeedSequence(MASTER_SEED).spawn(N_DRAWS)[self.draw_index]
            rng = np.random.default_rng(child)
            self._u = rng.random(2 * n)
            self._n = n
        if self._n != n:
            raise RuntimeError(
                f"mask size changed within draw {self.draw_index} ({self._n} -> {n}) — "
                "common-random variates would be broken; one MappingA instance serves one "
                "mask population")
        return self._u

    def __call__(self, gamma, mask, cal):
        v9 = _v9()
        n = int(mask.n)
        u = self._uniforms(n)
        c = np.asarray(mask.c, dtype=np.float64)
        a0 = float(cal["a_hat"])
        c_bar = float(c.mean())
        a_raw = a0 + float(gamma) * (c - c_bar)
        a_g = np.clip(a_raw, A_CLIP_LO, A_CLIP_HI)
        clip_frac = float(np.mean(a_raw != a_g))
        u_lat = u[0::2]
        u_flip = u[1::2]
        lat = np.where(u_lat < (1.0 + v9.A_LONGO * c) / 2.0, 1.0, -1.0)
        s_prime = np.where(u_flip < (1.0 - a_g), -lat, lat)
        # cal' — the same perturbation, bin-aggregated, margins preserved
        cal_p = dict(cal)
        bins = np.asarray(mask.bin)
        a_b = np.asarray(cal["a_b"], dtype=np.float64)
        a_lb_b = np.asarray(cal["a_lb_b"], dtype=np.float64)
        a_b_p = np.empty_like(a_b)
        for b in range(a_b.shape[0]):
            sel = bins == b
            a_b_p[b] = float(np.clip(a_g[sel].mean(), A_CLIP_LO, A_CLIP_HI)) if sel.any() \
                else a_b[b]
        cal_p["a_b"] = a_b_p
        cal_p["a_lb_b"] = a_b_p - (a_b - a_lb_b)
        a_hat_p = float(np.clip(a_g.mean(), A_CLIP_LO, A_CLIP_HI))
        cal_p["a_hat"] = a_hat_p
        cal_p["a_lb"] = a_hat_p - (float(cal["a_hat"]) - float(cal["a_lb"]))
        self.last_diagnostics = {"gamma": float(gamma), "clip_fraction": clip_frac,
                                 "a_hat_prime": a_hat_p, "draw": self.draw_index}
        return s_prime, cal_p


def make_mapping(draw_index):
    return MappingA(draw_index)


# ------------------------------------------------------------------ self-test
def self_test():
    fails = []
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "gain_counterfactual_path", HERE / "gain_counterfactual_path.py")
    gcp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gcp)
    mask, _ = gcp._fixture()
    cal = dict(gcp._CAL)
    # 1. CRN: one draw, two gammas — identical uniforms, deterministic reconstruction
    m0 = make_mapping(0)
    s_a, _ = m0(0.10, mask, cal)
    u_first = m0._u.copy()
    s_b, _ = m0(-0.10, mask, cal)
    if not np.array_equal(m0._u, u_first):
        fails.append("CRN broken: uniforms changed across gammas within one draw")
    m0b = make_mapping(0)
    s_a2, _ = m0b(0.10, mask, cal)
    if not np.array_equal(s_a, s_a2):
        fails.append("determinism broken: draw 0 reconstructed differently")
    # 2. distinct draws use distinct streams
    m1 = make_mapping(1)
    m1(0.10, mask, cal)
    if np.array_equal(u_first, m1._u):
        fails.append("draw 1 shares draw 0's stream")
    # 3. zero-based addressing bounds
    try:
        make_mapping(N_DRAWS)
        fails.append("draw index 99 accepted (one-based ghost)")
    except RuntimeError:
        pass
    make_mapping(0)  # child 0 in use — the Amendment-1 correction
    # 4. sign-vector contract
    if not set(np.unique(s_a)).issubset({-1.0, 1.0}):
        fails.append("s' contains values other than ±1")
    # 5. gamma=0 uses a0 exactly (no perturbation): equals an a0-flat redraw
    mz = make_mapping(3)
    s_z, cal_z = mz(0.0, mask, cal)
    a_flat = np.full(mask.n, float(cal["a_hat"]))
    u = mz._u
    lat = np.where(u[0::2] < (1.0 + _v9().A_LONGO * np.asarray(mask.c)) / 2.0, 1.0, -1.0)
    exp = np.where(u[1::2] < (1.0 - a_flat), -lat, lat)
    if not np.array_equal(s_z, exp):
        fails.append("gamma=0 does not reduce to the flat-a0 redraw")
    # 6. clamp behaviour at extreme gamma is clipped, reported, and in-range
    mx = make_mapping(5)
    s_x, cal_x = mx(5.0, mask, cal)
    if mx.last_diagnostics["clip_fraction"] <= 0.0:
        fails.append("extreme gamma reported no clipping")
    if not (A_CLIP_LO <= cal_x["a_hat"] <= A_CLIP_HI):
        fails.append("cal' a_hat escaped the physical clamp")
    # 7. CRN-size guard
    class FakeMask:  # minimal duck type
        n = mask.n + 1
        c = np.zeros(mask.n + 1)
        bin = np.zeros(mask.n + 1, dtype=int)
    try:
        m0(0.05, FakeMask(), cal)
        fails.append("mask-size drift within a draw accepted")
    except RuntimeError:
        pass
    # 8. THE REAL PATH CONSUMES IT: evaluate_at with this mapping runs v9 end to end
    try:
        out = gcp.evaluate_at(0.0, mask, cal, make_mapping(7),
                              stage=1, prefix=1, trial=1, n_perm=400)
        if "gamma" not in out:
            fails.append("path integration returned no verdict dict")
    except Exception as e:
        fails.append(f"path integration failed: {type(e).__name__}: {e}")
    return fails


if __name__ == "__main__":
    f = self_test()
    for x in f:
        print("SELF-TEST FAIL:", x)
    print(f"gain_mapping_a self-test: {8 - len(f)}/8 green — {MAPPING_ID}")
    sys.exit(1 if f else 0)
