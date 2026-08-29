#!/usr/bin/env python3
"""GAIN COUNTERFACTUAL PATH — option (b): move A and p together, through production.

The principal ruled the sensitivity-gradient control a "real gate" (2026-08-29), which selects
option (b): freeze an executable joint counterfactual path that maps each allowed gain perturbation
through accepted signs, calibration and the production permutation record. Option (a) — hold the
observed p fixed and vary only the amplitude — is dead, and this module must not quietly reintroduce
it.

Why the joint path is the whole point
-------------------------------------
My earlier reduction argued production `p` is a monotone function of `|A|`, so the p gates could be
folded into A-breakpoints. Both seats refuted it, and GPT56 supplied a counterexample rather than an
argument: two accepted-sign vectors on the same geometry with the SAME raw slope, hence the same A,
but exact one-sided p of 1.0 and 0.9. `p(A)` is not single-valued at fixed geometry and fixed
calibration, because production permutes the accepted-sign vector and `perm_sigma_exact` reads the
variance of `s`. A gain gradient moves the sign multiset, so it moves the null.

So there is no scalar `p_of_A` to insert. The only sound path is to carry a counterfactual sign
vector all the way through the real machinery:

    gamma  ->  s'  ->  perm_record(mask.with_signs(s'))  ->  (beta', p', sigma_beta')
                 \\
                  ->  cal'                               ->  _decide_from(...)  ->  verdict'

`perm_record` returns beta, the null, p and sigma together from the same s', so A and p cannot drift
apart the way an assumed reduction lets them.

WHAT THIS MODULE DELIBERATELY DOES NOT CONTAIN
----------------------------------------------
**The mapping gamma -> s' is NOT here, and must not be added without preregistering it.** What
counterfactual sign vector a given gain gradient produces is a modelling assumption about the
instrument, not an implementation detail, and I flagged it as needing preregistration before this
build was authorised. Choosing it quietly on the way to building the path is the exact failure the
standing orders name.

Therefore this module **refuses to run without an explicitly supplied mapping**. There is no default,
no fallback, and no "reasonable" identity. `evaluate_path` raises `MappingNotFrozen` if none is
given. The self-test supplies a mapping named `_TEST_ONLY_*` whose only purpose is to exercise
plumbing; it is not a candidate model and is not preregistered.
"""

import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import successor_ref_v9 as v9  # noqa: E402  the FROZEN production reference; never modified

CODES = {
    "P01": "no counterfactual mapping was supplied — the module refuses a default",
    "P02": "the mapping returned a sign vector of the wrong length",
    "P03": "the mapping returned values that are not exactly +1 or -1",
    "P04": "the mapping returned a non-finite value",
    "P05": "the mapping returned a degenerate sign vector (no variance) — production would raise",
    "P06": "the gain grid is empty, non-finite, or not sorted",
    "P07": "the calibration the mapping returned is missing a key production reads",
    "P08": "the production permutation record raised on the counterfactual signs",
    "P09": "the decision helper raised on the counterfactual inputs",
}


class MappingNotFrozen(RuntimeError):
    """Raised when no mapping is supplied. Deliberately not catchable by a bare default."""


class PathRefusal(RuntimeError):
    def __init__(self, code, msg):
        super().__init__(f"[{code}] {CODES[code]}: {msg}")
        self.code = code


# The keys `_decide_from` reads on each adjudicated path. Checked before use so a missing key is a
# named refusal rather than a KeyError three frames down.
_CAL_KEYS_SCALAR = ("a_hat", "sigma_a", "a_lb")
_CAL_KEYS_PROFILE = ("a_b", "a_lb_b", "cov_a")


def _check_signs(s, n):
    a = np.asarray(s)
    if a.shape != (n,):
        raise PathRefusal("P02", f"expected shape ({n},), got {a.shape}")
    if not np.isfinite(a).all():
        raise PathRefusal("P04", "counterfactual sign vector contains a non-finite value")
    if not np.isin(a, (-1.0, 1.0)).all():
        bad = sorted(set(np.asarray(a).ravel().tolist()) - {-1.0, 1.0})[:4]
        raise PathRefusal("P03", f"values outside {{-1,+1}}: {bad}")
    if float(np.var(a)) <= 0.0:
        raise PathRefusal("P05", "all signs identical — perm_sigma_exact would raise")
    return np.asarray(a, dtype=np.float64)


def _check_cal(cal):
    if not isinstance(cal, dict):
        raise PathRefusal("P07", f"calibration is {type(cal).__name__}, not a dict")
    try:
        path = v9.adjudicate_path(cal)
    except Exception as e:
        raise PathRefusal("P07", f"adjudicate_path refused: {type(e).__name__}: {e}")
    need = _CAL_KEYS_SCALAR if path == "SCALAR" else _CAL_KEYS_PROFILE
    missing = [k for k in need if k not in cal]
    if missing:
        raise PathRefusal("P07", f"{path} path needs {missing}")
    return path


def _check_grid(gammas):
    g = np.asarray(gammas, dtype=np.float64)
    if g.size == 0:
        raise PathRefusal("P06", "empty gain grid")
    if not np.isfinite(g).all():
        raise PathRefusal("P06", "non-finite gamma in the grid")
    if not np.all(np.diff(g) >= 0):
        raise PathRefusal("P06", "gain grid is not sorted ascending")
    return g


def evaluate_at(gamma, mask, cal, mapping, *, stage, prefix, trial, n_perm):
    """One point of the joint path. Returns the production verdict dict, plus gamma.

    Every step runs the real v9 function. Nothing is approximated and no p is held fixed.
    """
    if mapping is None:
        raise MappingNotFrozen(
            "[P01] " + CODES["P01"] + " — gamma -> s' is a modelling assumption that must be "
            "preregistered before it is used; see OPEN_QUESTION_GAIN_SIGN_MAPPING.md")

    s_prime, cal_prime = mapping(gamma, mask, cal)
    s_prime = _check_signs(s_prime, mask.n)
    cal_prime = cal if cal_prime is None else cal_prime
    _check_cal(cal_prime)

    m = mask.with_signs(s_prime)
    try:
        beta, _null, p, sigma_beta = v9.perm_record(m, stage, prefix, trial, n_perm=n_perm)
    except Exception as e:
        raise PathRefusal("P08", f"gamma={gamma!r}: {type(e).__name__}: {e}")
    try:
        out = v9._decide_from(beta, p, sigma_beta, m, cal_prime)
    except Exception as e:
        raise PathRefusal("P09", f"gamma={gamma!r}: {type(e).__name__}: {e}")
    out["gamma"] = float(gamma)
    return out


def evaluate_path(gammas, mask, cal, mapping=None, *, stage, prefix, trial, n_perm=2000):
    """Evaluate the whole allowed perturbation set. Refuses rather than defaulting."""
    g = _check_grid(gammas)
    return [evaluate_at(x, mask, cal, mapping, stage=stage, prefix=prefix,
                        trial=trial, n_perm=n_perm) for x in g]


def invariance(results):
    """The gate: does the verdict survive every allowed perturbation?

    Reports the flip explicitly. A control that says only PASS/FAIL hides which perturbation broke
    it, and the whole value of the joint path is knowing where the verdict turns over.
    """
    verdicts = {r["verdict"] for r in results}
    if len(verdicts) == 1:
        return {"invariant": True, "verdict": results[0]["verdict"], "n": len(results),
                "flips": []}
    flips = [(results[i - 1]["gamma"], results[i]["gamma"],
              results[i - 1]["verdict"], results[i]["verdict"])
             for i in range(1, len(results)) if results[i]["verdict"] != results[i - 1]["verdict"]]
    return {"invariant": False, "verdict": None, "n": len(results),
            "verdicts": sorted(verdicts), "flips": flips}


# ---------------------------------------------------------------------------
# Self-test. The mapping below is PLUMBING ONLY.
# ---------------------------------------------------------------------------

def _fixture(n=240, seed=7):
    rng = np.random.default_rng(seed)
    c = np.linspace(-0.98, 0.98, n)
    s = np.where(rng.random(n) < (1.0 + 0.10 * c) / 2.0, 1.0, -1.0)
    if float(np.var(s)) <= 0:                      # degenerate draw would refuse downstream
        s[0] = -s[0]
    bid = np.arange(n, dtype=np.int64)
    bnd = v9.calibration_bins(c)                   # the production cos-theta tertiles
    return v9.FixtureMask(bid, bid, c, s, bin_label=v9.assign_bins(c, bnd)), s


def _TEST_ONLY_flip_fraction_mapping(gamma, mask, cal):
    """NOT A MODEL. NOT PREREGISTERED. Exercises the plumbing only.

    Deterministically flips a gamma-dependent share of signs so that downstream quantities actually
    move and the controls have something to bite on. It encodes no claim whatever about what a gain
    gradient does to handedness, and must never be promoted to a default.
    """
    s = np.array(mask.s, dtype=np.float64, copy=True)
    k = int(abs(gamma) * len(s))
    if k:
        idx = np.argsort(mask.c)[:k] if gamma < 0 else np.argsort(-mask.c)[:k]
        s[idx] = -s[idx]
    if float(np.var(s)) <= 0.0:
        s[0] = -s[0]
    return s, None


_CAL = {"a_hat": 0.88, "sigma_a": 0.02, "a_lb": 0.86,
        "a_b": np.full(3, 0.88), "a_lb_b": np.full(3, 0.86),
        "cov_a": np.eye(3) * 4e-4}


def self_test():
    mask, _ = _fixture()
    fails = []
    ST = dict(stage=v9.STAGE_C, prefix=11, trial=3, n_perm=400)

    # 1 — the refusal that matters most: no mapping, no run, no default.
    try:
        evaluate_at(0.0, mask, _CAL, None, **ST)
        fails.append("P01: a missing mapping did NOT refuse")
    except MappingNotFrozen:
        pass
    except Exception as e:
        fails.append(f"P01: wrong exception {type(e).__name__}")

    # 2 — the joint path runs end-to-end through production.
    try:
        res = evaluate_path([-0.2, -0.1, 0.0, 0.1, 0.2], mask, _CAL,
                            _TEST_ONLY_flip_fraction_mapping, **ST)
        if len(res) != 5:
            fails.append("path: wrong result count")
        if not all(np.isfinite([r["p"] for r in res])):
            fails.append("path: non-finite p")
        # The refuted reduction claimed p follows |A|. Show they move independently here.
        if len({(round(r["A_L"], 12), round(r["p"], 12)) for r in res}) < 2:
            fails.append("path: nothing moved — the mapping is not exercising the machinery")
    except Exception as e:
        fails.append(f"path raised {type(e).__name__}: {e}")

    # 3 — domain controls. Each asserts its OWN code, not that 'something refused'.
    bad = (
        ("P02", lambda g, m, c: (np.ones(m.n - 1), None)),
        ("P03", lambda g, m, c: (np.full(m.n, 0.5), None)),
        ("P04", lambda g, m, c: (np.full(m.n, np.nan), None)),
        ("P05", lambda g, m, c: (np.ones(m.n), None)),
        ("P07", lambda g, m, c: (m.s, {"a_hat": 0.88})),   # missing a_lb_b/a_b
    )
    for code, mp in bad:
        try:
            evaluate_at(0.0, mask, _CAL, mp, **ST)
            fails.append(f"{code}: did not refuse")
        except PathRefusal as e:
            if e.code != code:
                fails.append(f"{code}: refused as {e.code} instead")
        except Exception as e:
            fails.append(f"{code}: raised {type(e).__name__} rather than refusing")

    for code, grid in (("P06", []), ("P06", [0.1, np.nan]), ("P06", [0.2, 0.1])):
        try:
            evaluate_path(grid, mask, _CAL, _TEST_ONLY_flip_fraction_mapping, **ST)
            fails.append(f"{code}: grid {grid} did not refuse")
        except PathRefusal as e:
            if e.code != code:
                fails.append(f"{code}: refused as {e.code}")

    # 4 — invariance reports WHERE it flips, not merely that it did.
    a = [{"verdict": "INCONCLUSIVE", "gamma": 0.0}, {"verdict": "INCONCLUSIVE", "gamma": 0.1}]
    if not invariance(a)["invariant"]:
        fails.append("invariance: constant verdicts reported as flipping")
    b = [{"verdict": "INCONCLUSIVE", "gamma": 0.0}, {"verdict": "REPRODUCED-LONGO", "gamma": 0.1}]
    r = invariance(b)
    if r["invariant"] or r["flips"] != [(0.0, 0.1, "INCONCLUSIVE", "REPRODUCED-LONGO")]:
        fails.append("invariance: flip not located")

    # 4b — the two codes that wrap PRODUCTION failures. These were reported as "unexercised
    # (reachable only from production internals)" when this module shipped, which is an honest
    # label for an uncontrolled branch but still an uncontrolled branch. Both are reachable and
    # both now have a control asserting their own code.
    good = lambda g, m, c: (np.array(m.s, dtype=np.float64, copy=True), None)
    try:
        # perm_record refuses a FixtureMask under STAGE_REAL BY TYPE - a real production guard.
        evaluate_at(0.0, mask, _CAL, good, stage=v9.STAGE_REAL, prefix=11, trial=3, n_perm=200)
        fails.append("P08: production refusal did not surface")
    except PathRefusal as e:
        if e.code != "P08":
            fails.append(f"P08: refused as {e.code}")
    except Exception as e:
        fails.append(f"P08: raised {type(e).__name__} rather than refusing")

    # _decide_from on the PROFILE path indexes a_b by mask.bin; a short a_b is a production error.
    _SHORT = {"a_hat": 0.88, "a_b": np.array([0.95, 0.80]),
              "a_lb_b": np.full(2, 0.86), "cov_a": np.eye(2) * 4e-4}
    try:
        evaluate_at(0.0, mask, _CAL, lambda g, m, c: (good(g, m, c)[0], _SHORT), **ST)
        fails.append("P09: production refusal did not surface")
    except PathRefusal as e:
        if e.code != "P09":
            fails.append(f"P09: refused as {e.code}")
    except Exception as e:
        fails.append(f"P09: raised {type(e).__name__} rather than refusing")

    # 5 — no code may be unexercised; an unclaimed code is an uncontrolled branch.
    exercised = {"P01", "P02", "P03", "P04", "P05", "P06", "P07", "P08", "P09"}
    unexercised = set(CODES) - exercised
    for f in fails:
        print(f"  FAIL {f}")
    print(f"  self-test: {len(CODES)} codes, {len(unexercised)} unexercised"
          + (f" ({sorted(unexercised)})" if unexercised else " — every code has a control")
          + f", {len(fails)} failure(s)")
    print("  NOTE: the mapping used above is _TEST_ONLY_ plumbing. gamma -> s' is UNFROZEN and "
          "must be preregistered before this path can gate anything.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv[1:] else
             (print(__doc__.strip().split("\n")[0]), 2)[1])
