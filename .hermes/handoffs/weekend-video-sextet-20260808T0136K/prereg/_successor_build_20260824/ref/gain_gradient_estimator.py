#!/usr/bin/env python3
"""BS-3 side: the sensitivity-gradient estimator. The GLS/delta-method contract, as code.

WHAT THIS IS
------------
`GAIN_GRADIENT_CONTROL_DESIGN_20260828.md` §3 named a three-point GLS slope, a normalisation and a
delta-method propagation in prose. Both referee seats found that prose is not a contract: no solver,
no conditioning rule, no refusal for a singular covariance, and no Jacobian. This module is that
contract, written so a later operator has nothing left to choose.

THE NORMALISATION DEFECT THIS FIXES
-----------------------------------
The bias equation is derived for the UNCENTRED model

    g(c) = g0 * (1 + gamma * c)

in which the regression INTERCEPT is `g0` and the slope is `g0*gamma`. §3 then estimated
`gamma_hat = slope / mean(g_hat)`. Those are different quantities: the count-weighted sample mean is
`g0*(1 + gamma*mean(c))`, so the statistic actually defined was

    slope / mean(g) = gamma / (1 + gamma*mean(c))

On the frozen retained geometry `mean(c) = -0.158387518`, so a true `gamma = +0.2` came out as
`+0.20654`, and `gamma = +0.5` as `+0.54300` (GPT56-GAINV3-1, CODEX-GAINV3-1). That is the same
class of error as the v2 blocker — a quantity specified in one place and estimated in another — one
layer further in.

**Here `gamma_hat = slope / INTERCEPT`, both from the same GLS fit, with their joint covariance
propagated by an explicit Jacobian.** `self_test()` asserts the recovery is exact on a noiseless
fixture AND that the old sample-mean normalisation would have been wrong, so the defect cannot
return silently.

WHAT IS AND IS NOT CLAIMED
--------------------------
This estimates the first-order gradient of the accepted-sign gain along `cos theta` from three
positional bins. It does not measure `mu`, does not bound routes (a) or (c) of the instrument
description's §2.3, does not address curvature, and does not close conditional independence.
`gamma_hat` is UNMEASURED: this module defines how it would be computed, not what it is.
"""
from __future__ import annotations

import sys

import numpy as np

# ── Frozen. Changing any of these is a contract change. ─────────────────────────────────────────
N_BINS = 3
COND_MAX = 1.0e12          # covariance condition-number ceiling; above it the solve is refused
DESIGN_COND_MAX = 1.0e10   # whitened normal-matrix ceiling; near-coincident bin centres refuse
INTERCEPT_K = 3.0          # |intercept| must exceed this many standard errors, or gamma is undefined
A_LO, A_HI = 0.5, 1.0      # v9's own accuracy domain (`inject_signs`, v9:1207)

CODES = {
    "G01": "an input is not finite",
    "G02": "the covariance is not symmetric",
    "G03": "the covariance is rank-deficient; no generalised inverse is substituted",
    "G04": "the covariance is worse-conditioned than the frozen ceiling",
    "G05": "the design matrix is rank-deficient; the bin centres do not span a slope",
    "G06": "the fitted intercept is not distinguishable from zero, so slope/intercept is undefined",
    "G07": "a bin accuracy is outside v9's (0.5, 1.0] domain",
    "G08": "a deterministic numerical linear-algebra failure was caught",
    "G09": "a bin centre is outside the physical cos(theta) range [-1, 1]",
}


def _codes(reasons):
    return {r[1:4] for r in reasons if len(r) > 4 and r[0] == "[" and r[4] == "]"}


def estimate_gamma(a_hat, cov_a, c_bar):
    """Return (result, refusals).

    `result` is None whenever `refusals` is non-empty — there is no partial answer. On success it is
    a dict of exactly the receipt fields.
    """
    bad: list[str] = []

    def refuse(code, msg):
        bad.append(f"[{code}] {msg}")

    a = np.asarray(a_hat, dtype=np.float64)
    S_a = np.asarray(cov_a, dtype=np.float64)
    c = np.asarray(c_bar, dtype=np.float64)

    if a.shape != (N_BINS,) or c.shape != (N_BINS,) or S_a.shape != (N_BINS, N_BINS):
        refuse("G01", f"shapes {a.shape}, {S_a.shape}, {c.shape} != ({N_BINS},), "
                      f"({N_BINS},{N_BINS}), ({N_BINS},)")
        return None, bad
    if not (np.isfinite(a).all() and np.isfinite(S_a).all() and np.isfinite(c).all()):
        refuse("G01", "a_hat, cov_a or c_bar carries a non-finite value")
        return None, bad
    if c.min() < -1.0 or c.max() > 1.0:
        refuse("G09", f"c_bar range [{c.min():.6f}, {c.max():.6f}] outside the physical [-1, 1]")
    if a.min() <= A_LO or a.max() > A_HI:
        refuse("G07", f"accuracy range [{a.min():.6f}, {a.max():.6f}] outside ({A_LO}, {A_HI}]")
    if not np.allclose(S_a, S_a.T, rtol=0.0, atol=1e-15):
        refuse("G02", "cov_a is not symmetric")
    if bad:
        return None, bad

    # g = 2a - 1, so Cov(g) = 4 Cov(a). The estimator consumes the gain, not the accuracy.
    g = 2.0 * a - 1.0
    S = 4.0 * S_a
    # Finite inputs do not imply finite derived algebra in float64: cov_a = diag(1e308) is finite
    # and 4*cov_a is not. Checked AFTER the scaling, not before (CODEX-GAINV4-2).
    if not np.isfinite(S).all():
        refuse("G01", "cov_a is finite but 4*cov_a overflows; the scaled covariance is not finite")
        return None, bad

    # Rank and conditioning BEFORE any inverse. A singular covariance is refused outright: no
    # pseudo-inverse is substituted, because the choice of generalised inverse would itself be an
    # unpinned degree of freedom (GPT56-GAINV3-2).
    w = np.linalg.eigvalsh(S)
    if w.min() <= 0.0:
        refuse("G03", f"cov_g eigenvalues {np.round(w, 18).tolist()} — not positive definite")
        return None, bad
    cond = float(w.max() / w.min())
    if cond > COND_MAX:
        refuse("G04", f"cov_g condition number {cond:.3e} > frozen ceiling {COND_MAX:.1e}")
        return None, bad

    # Design matrix for the UNCENTRED model: g_b = theta0 + theta1 * c_b, so theta0 IS g0 and
    # theta1 IS g0*gamma. gamma = theta1/theta0 by construction, which is the gamma the bias
    # equation uses.
    X = np.column_stack([np.ones(N_BINS), c])
    if np.linalg.matrix_rank(X) < 2:
        refuse("G05", f"design matrix rank {np.linalg.matrix_rank(X)} < 2; c_bar = {c.tolist()}")
        return None, bad

    # GLS by Cholesky solve rather than an explicit inverse. matrix_rank(X) == 2 is NOT sufficient:
    # bin centres separated by 1e-8 are formally rank 2 and still make XtX singular
    # (GPT56-GAINV4-2). Condition the whitened normal matrix, and wrap every numpy.linalg call so a
    # deterministic failure becomes a refusal rather than an exception escaping the API.
    try:
        L = np.linalg.cholesky(S)
        Xw = np.linalg.solve(L, X)
        gw = np.linalg.solve(L, g)
        XtX = Xw.T @ Xw
        wx = np.linalg.eigvalsh(XtX)
        if wx.min() <= 0.0 or float(wx.max() / wx.min()) > DESIGN_COND_MAX:
            refuse("G05", f"whitened normal matrix condition "
                          f"{float(wx.max() / max(wx.min(), 1e-300)):.3e} > {DESIGN_COND_MAX:.1e}; "
                          f"bin centres {c.tolist()} do not span a slope")
            return None, bad
        theta = np.linalg.solve(XtX, Xw.T @ gw)
        cov_theta = np.linalg.solve(XtX, np.eye(2))
    except np.linalg.LinAlgError as e:
        refuse("G08", f"numerical linear algebra failed: {e}")
        return None, bad

    g0, g1 = float(theta[0]), float(theta[1])
    se_g0 = float(np.sqrt(max(cov_theta[0, 0], 0.0)))
    if abs(g0) <= INTERCEPT_K * se_g0 or g0 == 0.0:
        refuse("G06", f"intercept {g0:.6e} within {INTERCEPT_K} se ({se_g0:.6e}) of zero")
        return None, bad

    gamma = g1 / g0
    # Delta method, Jacobian written out: d(g1/g0)/dg0 = -g1/g0^2, d(g1/g0)/dg1 = 1/g0.
    J = np.array([-g1 / (g0 * g0), 1.0 / g0], dtype=np.float64)
    var_gamma = float(J @ cov_theta @ J)
    if not np.isfinite(gamma) or not np.isfinite(var_gamma) or var_gamma < 0.0:
        refuse("G08", f"gamma {gamma!r} or var {var_gamma!r} not finite/non-negative")
        return None, bad

    return {
        "g_hat": g.tolist(),
        "cov_g": S.tolist(),
        "c_bar": c.tolist(),
        "intercept_g0": g0,
        "slope_g1": g1,
        "cov_theta": cov_theta.tolist(),
        "cond_cov_g": cond,
        "gamma_hat": gamma,
        "sigma_gamma": float(np.sqrt(var_gamma)),
        "jacobian": J.tolist(),
    }, []


# ── Fixtures. Every refusal must prove it can fire, and the normalisation must prove it is fixed. ─

# v4 declared G08 "unreachable by construction" and exempted it from coverage. BOTH SEATS BROKE
# THAT, and they were right: finite inputs do not imply finite derived algebra in float64. The
# exemption is withdrawn and G08 now carries a real control - a denormal covariance passes G01 and
# G03 and then fails inside the solve. Nothing here is exempt from coverage any more.
UNREACHABLE: set[str] = set()   # G08 is reachable and controlled; the exemption is withdrawn


def REFUSAL_CONTROLS(a_ok, S_ok, c_ok):
    return [
        ("non-finite input", (a_ok, np.full((3, 3), np.nan).tolist(), c_ok), {"G01"}),
        ("asymmetric cov", (a_ok, [[1e-6, 1e-7, 0], [0, 1e-6, 0], [0, 0, 1e-6]], c_ok), {"G02"}),
        ("rank-0 cov", (a_ok, np.zeros((3, 3)).tolist(), c_ok), {"G03"}),
        ("rank-1 cov", (a_ok, (np.ones((3, 3)) * 1e-6).tolist(), c_ok), {"G03"}),
        ("near-singular cov", (a_ok, (np.diag([1e-6, 1e-6, 1e-19])).tolist(), c_ok), {"G04"}),
        ("degenerate c_bar", (a_ok, S_ok, [0.1, 0.1, 0.1]), {"G05"}),
        ("accuracy out of domain", ([0.4, 0.8, 0.9], S_ok, c_ok), {"G07"}),
        # GPT56-GAINV4-2: formally rank-2 but numerically singular.
        ("near-coincident bin centres",
         ([0.8, 0.81, 0.82], np.diag([1e-20, 1e-20, 1e-20]).tolist(),
          [1 - 2e-8, 1 - 1e-8, 1.0]), {"G05"}),
        # G08 IS reachable: a denormal covariance survives G01/G03 and fails inside the solve.
        # The v4 "unreachable by construction" exemption was wrong and both seats said so.
        ("denormal covariance",
         ([0.8, 0.8, 0.8], np.diag([5e-324, 5e-324, 5e-324]).tolist(), [-0.9, 0.0, 0.9]),
         {"G08"}),
        # CODEX-GAINV4-2: finite cov_a whose 4x scaling overflows.
        ("cov overflows on scaling",
         ([0.8, 0.8, 0.8], np.diag([1e308, 1e308, 1e308]).tolist(), [-0.9, 0.0, 0.9]), {"G01"}),
        # CODEX-GAINV4-2: bin means of cos(theta) must lie in [-1, 1].
        ("bin centre out of range", (a_ok, S_ok, [-2.0, 0.0, 2.0]), {"G09"}),
    ]

C_BAR_REF = [-0.94001065, -0.453413185, 0.918326918]   # the real retained-sample bin centres
MEAN_C_REF = -0.158387518                              # count-weighted mean over the same sample


def _noiseless(gamma, g0=0.80, cov_scale=1e-6):
    """Exact g_b = g0(1 + gamma c_b), with a well-conditioned diagonal covariance."""
    c = np.array(C_BAR_REF)
    g = g0 * (1.0 + gamma * c)
    a = (1.0 + g) / 2.0
    return a.tolist(), (np.eye(N_BINS) * cov_scale).tolist(), C_BAR_REF


def self_test() -> int:
    print("gain-gradient estimator self-test")
    fails = []

    # 1. Recovery: the estimator must return the gamma that generated the data.
    #    g0 is chosen per case to keep accuracy inside v9's (0.5, 1.0] domain: since
    #    a = (1 + g0(1 + gamma*c))/2 and c is in [-1, 1], the domain requires |gamma| <= 1/g0 - 1.
    #    A case that violates it is a fixture bug, not a physics result — the same trap that made
    #    verify_mu_gamma.py report a false mismatch.
    for gamma, g0 in ((0.0, 0.80), (0.2, 0.80), (-0.2, 0.80), (0.5, 0.60), (-0.5, 0.60)):
        assert abs(gamma) <= 1.0 / g0 - 1.0 + 1e-12, f"fixture out of domain: gamma={gamma} g0={g0}"
        res, bad = estimate_gamma(*_noiseless(gamma, g0=g0))
        ok = res is not None and abs(res["gamma_hat"] - gamma) < 1e-9
        shown = f"{res['gamma_hat']:+.12f}" if res else f"REFUSED {sorted(_codes(bad))}"
        print(f"  {'OK  ' if ok else 'FAIL'} recovers gamma = {gamma:+.2f} (g0={g0}): {shown}")
        if not ok:
            fails.append(f"recovery {gamma}")

    # 2. Regression control for the defect itself: the OLD sample-mean normalisation must differ
    #    from the fixed one, and must differ by the predicted amount. If this ever stops firing,
    #    the normalisation has silently reverted.
    for gamma, g0 in ((0.2, 0.80), (-0.2, 0.80), (0.5, 0.60)):
        res, bad = estimate_gamma(*_noiseless(gamma, g0=g0))
        if res is None:
            print(f"  FAIL regression control gamma={gamma}: REFUSED {sorted(_codes(bad))}")
            fails.append(f"regression control {gamma}")
            continue
        old = res["slope_g1"] / float(np.mean(res["g_hat"]))
        predicted_old = gamma / (1.0 + gamma * np.mean(C_BAR_REF))
        differs = abs(old - res["gamma_hat"]) > 1e-6
        matches = abs(old - predicted_old) < 1e-6
        ok = differs and matches
        print(f"  {'OK  ' if ok else 'FAIL'} old sample-mean normalisation for gamma={gamma:+.2f} "
              f"gives {old:+.9f}, fixed gives {res['gamma_hat']:+.9f} (differ: {differs})")
        if not ok:
            fails.append(f"regression control {gamma}")

    # 3. Every refusal fires, with its exact code set.
    a_ok, S_ok, c_ok = _noiseless(0.2)
    controls = list(REFUSAL_CONTROLS(a_ok, S_ok, c_ok)) + [
        ("non-finite input", (a_ok, np.full((3, 3), np.nan).tolist(), c_ok), {"G01"}),
        ("asymmetric cov", (a_ok, [[1e-6, 1e-7, 0], [0, 1e-6, 0], [0, 0, 1e-6]], c_ok), {"G02"}),
        ("rank-0 cov", (a_ok, np.zeros((3, 3)).tolist(), c_ok), {"G03"}),
        ("rank-1 cov", (a_ok, (np.ones((3, 3)) * 1e-6).tolist(), c_ok), {"G03"}),
        ("near-singular cov", (a_ok, (np.diag([1e-6, 1e-6, 1e-19])).tolist(), c_ok), {"G04"}),
        ("degenerate c_bar", (a_ok, S_ok, [0.1, 0.1, 0.1]), {"G05"}),
    ]
    for name, args, expect in controls:
        res, bad = estimate_gamma(*args)
        got = _codes(bad)
        ok = got == expect and res is None
        print(f"  {'OK  ' if ok else 'FAIL'} {name}: {sorted(got) or 'ACCEPTED'}"
              f"{'' if ok else f' — expected {sorted(expect)}'}")
        if not ok:
            fails.append(name)

    # 4. G06: an intercept indistinguishable from zero. g0 -> 0 with a wide covariance.
    c = np.array(C_BAR_REF)
    g = 1e-9 * (1.0 + 0.2 * c)
    res, bad = estimate_gamma(((1.0 + g) / 2.0).tolist(), (np.eye(3) * 1e-4).tolist(), C_BAR_REF)
    ok = res is None and _codes(bad) == {"G06"}
    print(f"  {'OK  ' if ok else 'FAIL'} intercept at zero: {sorted(_codes(bad)) or 'ACCEPTED'}")
    if not ok:
        fails.append("G06")

    # 5. Coverage, COMPUTED from the controls that ran, with the exemption named.
    exercised = set().union(*(e for _, _, e in controls)) | {"G06"}
    orphans = set(CODES) - exercised - UNREACHABLE
    if orphans:
        print(f"  FAIL codes with no control and no exemption: {sorted(orphans)}")
        fails.append("coverage")
    else:
        print(f"  OK   {len(exercised)} of {len(CODES)} codes exercised by a control; "
              f"{sorted(UNREACHABLE)} declared unreachable by construction, not counted as covered")

    print(f"  self-test: {len(fails)} failure(s)")
    return 1 if fails else 0


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    res, bad = estimate_gamma(*_noiseless(0.2))
    print("reference fit on the noiseless gamma=+0.2 fixture:")
    for k in ("intercept_g0", "slope_g1", "gamma_hat", "sigma_gamma", "cond_cov_g"):
        print(f"  {k:<14} {res[k]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
