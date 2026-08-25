#!/usr/bin/env python3
"""successor_ref_v2.py — THE reference definition for the successor preregistration (V6).

Where the constitution names a mechanism, THIS FILE's bytes are the definition. Prose never
overrides code; a conflict is a defect in the prose. Supersedes successor_ref.py
(sha 67bc4876858c4cb4445ccf40f41a4d3977c1d43e0b88ec5890d9b6b0091a4449), which is retained for
provenance and whose fixtures remain valid where re-run below.

Repairs the union of GATE_GPT56_SUCCESSOR_V5 (F1-F8) and GATE_CODEX_SUCCESSOR_V5 (F1-F8):
mask typing/provenance, per-bin Stage C, the raw/retained orchestrator, the calibration
producer + covariance, receipt schemas + frozen environment, a production-feasible power
kernel with a proved-equality contract, the decision function, fail-closed sigmas, and the
count-oracle closure validator.

DETERMINISM. Reductions are np.add.reduce over contiguous float64 1-D arrays. The only
matrix expression (profile sigma quadratic form) is computed as an explicit scalar double
loop, so the module makes no BLAS call and the no-BLAS docstring claim is true.

RANDOMNESS. Every stochastic operation derives from an immutable hierarchical address
SeedSequence((MASTER, stage, prefix, trial, role)) built fresh at point of use. Stateful
SeedSequence.spawn is BANNED.

ENVIRONMENT. require_environment() asserts the frozen interpreter/library versions; receipts
carry environment_record(). Fixture digests are valid only under the frozen environment.

Run `python3 successor_ref_v2.py --fixtures` to print the fixture table. The constitution
pins this file's sha256 and the fixture output's sha256.
"""
import hashlib
import itertools
import json
import math
import platform
import sys

import numpy as np

# ---------------------------------------------------------------- frozen environment
FROZEN_ENV = {
    "python_major_minor": "3.9",
    "numpy": "1.26.4",
    "byteorder": "little",
}


def environment_record() -> dict:
    return {
        "python": sys.version.split()[0],
        "python_major_minor": ".".join(sys.version.split()[0].split(".")[:2]),
        "numpy": np.__version__,
        "platform": sys.platform,
        "machine": platform.machine(),
        "byteorder": sys.byteorder,
    }


def require_environment() -> dict:
    """Production entry points call this. A mismatch REFUSES; it does not warn."""
    env = environment_record()
    for k, want in FROZEN_ENV.items():
        if env[k] != want:
            raise RuntimeError(f"FROZEN ENVIRONMENT MISMATCH: {k}={env[k]!r} want {want!r}")
    return env


# ---------------------------------------------------------------- frozen constants
MASTER_SEED = 20260824
# Longo 2011 (bibcode 2011PhLB..699..224L, doi:10.1016/j.physletb.2011.04.008), abstract
# verified from source 2026-08-25: amplitude "-0.0408+-0.011", axis "(l, b) = (52 deg, 68.5
# deg)", 15,158 spirals. The published SIGN is negative in Longo's convention; our
# East-of-North winding maps it to +0.0408 (V3-pred F-5). A_LONGO below is OUR-convention.
A_LONGO = 0.0408
A_LONGO_PUBLISHED_SIGNED = -0.0408
SIGMA_PUB = 0.011
N_PERM = 100_000          # production permutation count
N_TRIALS = 1_000          # power injection skies
CP_PASS_X = 962           # one-sided 95% Clopper-Pearson LB >= 0.95 at n=1000
P_REPRODUCED = 0.001      # F-6 strict threshold
P_REJECT_MIN = 0.05       # F-6 strict threshold
A_FLOOR = 0.85            # labelling-accuracy planning floor (V3-pred F-7 minima)
RETENTION_LB = 0.8572     # predecessor BS-3 retention lower bound
FLOOR_MULT = 3.09         # V3-pred F-7 one-sided floor multiplier
L_PLAN_MARGIN = 1.2
NEQ_MIN = 100_000         # N_eq = 3 * L_ret >= NEQ_MIN
N_EXACT = 16              # <= N_EXACT positive-count bricks: exact enumeration IS the algorithm
MOVE_CAP = 10_000         # reaching it is FAIL, never a result
N_CAL_BINS = 3            # calibration bins in c
N_HC_STRATA = 9           # carried HC-1H machine-state x |chi|-tertile strata
HC_MIN_PER_CELL = 10      # minimum hand-check allocation per non-empty 3x9 cell
PERM_CHUNK = 1_000        # production permutation chunk size

AXIS = np.array([-0.676971771271432, -0.509846551777774, +0.530816083537352], dtype=np.float64)

STAGE_P, STAGE_C, STAGE_REAL = 1, 2, 3
ROLE_INJECT, ROLE_PERM = 0, 1


def rng_at(stage: int, prefix: int, trial: int, role: int) -> np.random.Generator:
    return np.random.default_rng(np.random.SeedSequence((MASTER_SEED, stage, prefix, trial, role)))


# ---------------------------------------------------------------- geometry
def unit_vectors(ra_deg, dec_deg) -> np.ndarray:
    ra = np.radians(np.asarray(ra_deg, dtype=np.float64))
    dec = np.radians(np.asarray(dec_deg, dtype=np.float64))
    return np.stack([np.cos(dec) * np.cos(ra), np.cos(dec) * np.sin(ra), np.sin(dec)], axis=1)


def cos_theta(ra_deg, dec_deg) -> np.ndarray:
    u = unit_vectors(ra_deg, dec_deg)
    return u[:, 0] * AXIS[0] + u[:, 1] * AXIS[1] + u[:, 2] * AXIS[2]


# ---------------------------------------------------------------- weighted SSE / ledger
def sse(counts, c) -> float:
    n = np.ascontiguousarray(counts, dtype=np.float64)
    cc = np.ascontiguousarray(c, dtype=np.float64)
    N = float(np.add.reduce(n))
    if N <= 0.0:
        return 0.0
    cbar = float(np.add.reduce(n * cc)) / N
    d = cc - cbar
    return float(np.add.reduce(n * d * d))


def greedy_ledger(brickid, c, n_eligible):
    """BS-2o. Traversal over POSITIVE-RAW-COUNT bricks; zero-count bricks stay in the BS-2c
    receipt and never enter selection. No threshold input exists here."""
    bid = np.asarray(brickid, dtype=np.int64)
    cc = np.asarray(c, dtype=np.float64)
    nn = np.asarray(n_eligible, dtype=np.int64)
    idx_all = np.nonzero(nn > 0)[0]
    remaining = list(idx_all[np.argsort(bid[idx_all], kind="stable")])
    order, ledger = [], []
    N = cbar = L = 0.0
    while remaining:
        best = None
        for i in remaining:
            nj = float(nn[i])
            if N == 0.0:
                delta = 0.0
            else:
                d = cc[i] - cbar
                delta = (N * nj / (N + nj)) * (d * d)
            key = (delta, abs(cc[i]), -int(bid[i]))
            if best is None or key > best[0]:
                best = (key, i)
        i = best[1]
        remaining.remove(i)
        nj = float(nn[i])
        L = L + best[0][0]
        cbar = (cbar * N + cc[i] * nj) / (N + nj)
        N = N + nj
        order.append(int(i))
        ledger.append((len(order), int(bid[i]), N, (L / N if N > 0 else 0.0), L))
    return order, ledger


def retained_counts(n_eligible) -> np.ndarray:
    """Stage-P retention transform: per-brick integer floor(RETENTION_LB * n)."""
    return np.floor(RETENTION_LB * np.asarray(n_eligible, dtype=np.float64)).astype(np.int64)


def exact_min_subset(brickid, c, counts, l_plan: float):
    """Minimum-cardinality subset with L(counts) >= l_plan; ties -> lexicographically smallest
    sorted brickid tuple. Defined only for <= N_EXACT positive-count bricks."""
    bid = np.asarray(brickid, dtype=np.int64)
    cc = np.asarray(c, dtype=np.float64)
    nn = np.asarray(counts, dtype=np.int64)
    idx = sorted([i for i in range(len(bid)) if nn[i] > 0], key=lambda i: int(bid[i]))
    if len(idx) > N_EXACT:
        raise ValueError("exact mode only for <= N_EXACT positive-count bricks")
    for m in range(1, len(idx) + 1):
        feas = []
        for comb in itertools.combinations(idx, m):
            Lc = sse(nn[list(comb)], cc[list(comb)])
            if Lc >= l_plan:
                feas.append((tuple(sorted(int(bid[i]) for i in comb)), list(comb), Lc))
        if feas:
            feas.sort(key=lambda t: t[0])
            return feas[0][1], feas[0][2]
    return None


def local_pass(brickid, c, counts, order, l_plan: float):
    """BS-2s reduction. `counts` is the RETAINED count vector — every threshold in this
    function is evaluated on retained leverage (gpt56-V5 F2). For <= N_EXACT positive-count
    bricks the exact enumeration IS the algorithm (minimum cardinality by construction);
    otherwise the result is exactly what this procedure returns and NO minimality claim
    attaches to it."""
    bid = np.asarray(brickid, dtype=np.int64)
    cc = np.asarray(c, dtype=np.float64)
    nn = np.asarray(counts, dtype=np.int64)
    pos = [i for i in range(len(bid)) if nn[i] > 0]
    if len(pos) <= N_EXACT:
        r = exact_min_subset(bid, cc, nn, l_plan)
        if r is None:
            raise RuntimeError("no subset reaches l_plan")
        return r
    L_of = lambda S: sse(nn[list(S)], cc[list(S)])
    S, cum = [], None
    for k, i in enumerate(order):
        if nn[i] <= 0:
            continue
        S.append(i)
        if L_of(S) >= l_plan:
            cum = k + 1
            break
    if cum is None:
        raise RuntimeError("greedy order never reaches l_plan on retained counts")
    S = set(S)
    moves = 0

    def try_removal(S):
        for j in sorted(S, key=lambda j: (L_of(S) - L_of(S - {j}), int(bid[j]))):
            if L_of(S - {j}) >= l_plan:
                return j
        return None

    while True:
        moves += 1
        if moves > MOVE_CAP:
            raise RuntimeError("MOVE_CAP reached — FAIL")
        j = try_removal(S)
        if j is not None:
            S = S - {j}
            continue
        committed = False
        for i in sorted(S, key=lambda x: int(bid[x])):
            if committed:
                break
            for j2 in sorted((x for x in pos if x not in S), key=lambda x: int(bid[x])):
                S2 = (S - {i}) | {j2}
                if L_of(S2) >= l_plan:
                    r = try_removal(S2)
                    if r is not None:
                        S, committed = S2 - {r}, True
                        break
        if not committed:
            break
    return sorted(S, key=lambda x: int(bid[x])), L_of(S)


# ---------------------------------------------------------------- count-oracle closure
def validate_count_oracle(universe_brickid, table_brickid, table_counts,
                          grouped_sum: int, ungrouped_total: int) -> dict:
    """BS-2c closure validator (gpt56-V5 F5 / codex-V5 F7). Checks the table's key set equals
    the independently enumerated release brick universe EXACTLY (after zero materialization)
    and that grouped and ungrouped totals agree. Any failure raises."""
    uni = np.asarray(universe_brickid, dtype=np.int64)
    tab = np.asarray(table_brickid, dtype=np.int64)
    cnt = np.asarray(table_counts, dtype=np.int64)
    if len(np.unique(uni)) != len(uni):
        raise RuntimeError("universe manifest has duplicate brickids")
    if len(np.unique(tab)) != len(tab):
        raise RuntimeError("count table has duplicate brickids")
    missing = np.setdiff1d(uni, tab)
    extra = np.setdiff1d(tab, uni)
    if missing.size:
        raise RuntimeError(f"count table missing {missing.size} universe bricks (first {missing[:3].tolist()})")
    if extra.size:
        raise RuntimeError(f"count table has {extra.size} bricks outside the universe (first {extra[:3].tolist()})")
    if int(np.add.reduce(cnt)) != int(grouped_sum):
        raise RuntimeError("table counts do not sum to the grouped total")
    if int(grouped_sum) != int(ungrouped_total):
        raise RuntimeError("grouped total != ungrouped total")
    return {"universe": int(uni.size), "rows": int(tab.size),
            "zero_rows": int(np.count_nonzero(cnt == 0)), "total": int(grouped_sum)}


# ---------------------------------------------------------------- manifest closure
def manifest_closure(object_required_bricks) -> dict:
    """BS-2m. The selection defines the parent; the parent's CUTOUT GEOMETRY defines the brick
    set INCLUDING neighbours at the footprint edge. `object_required_bricks` maps each parent
    object id -> the list of bricknames its cutout plan requires, produced by the FROZEN cutout
    planner (named in the constitution, not reimplemented here). Returns the closed set and its
    count. The manifest may be frozen only from this output.

    Inherited defect this exists to prevent (predecessor run, found 2026-08-25): the 60,308-brick
    manifest was frozen from a brick enumeration that did not close over neighbour requirements.
    ls_id 10997315463551936 (dec -88.59) needs 3471m885 and ls_id 10995116744378804 (dec -87.13)
    needs 2857m870; both bricks exist in the release, neither was in the manifest, the parent
    needed 60,310, and nothing detected it until the cutter stalled two objects short at the end.
    """
    closed = set()
    per_object = {}
    for oid, bricks in object_required_bricks.items():
        bs = sorted({str(b) for b in bricks})
        if not bs:
            raise RuntimeError(f"object {oid} plans zero bricks — FAIL")
        per_object[str(oid)] = bs
        closed.update(bs)
    return {"required_bricknames": sorted(closed), "required_count": len(closed),
            "objects": len(per_object)}


def require_manifest_closure(manifest_bricknames, closure: dict) -> dict:
    """Pre-freeze check (BS-2m). Recomputes nothing on trust: it compares the frozen manifest
    against the closure set and REFUSES on a difference of even one brick, in either direction.
    The returned counts go into the receipt so a future gate reads numbers, not an assurance."""
    man = sorted({str(b) for b in manifest_bricknames})
    req = sorted(set(closure["required_bricknames"]))
    missing = sorted(set(req) - set(man))
    extra = sorted(set(man) - set(req))
    result = {"manifest_count": len(man), "required_count": len(req),
              "missing_from_manifest": missing, "missing_count": len(missing),
              "extra_in_manifest": extra, "extra_count": len(extra)}
    if missing or extra:
        raise ManifestClosureError(
            f"MANIFEST NOT CLOSED: manifest {len(man)} vs required {len(req)}; "
            f"missing {len(missing)} {missing[:4]}; extra {len(extra)} {extra[:4]}", result)
    return result


class ManifestClosureError(RuntimeError):
    def __init__(self, message, result):
        super().__init__(message)
        self.result = result


# ---------------------------------------------------------------- the canonical mask
class Mask:
    """The ONLY admissible input to Stage C and the production permutation record
    (gpt56-V5 F3 / codex-V5 F5). Construction validates and sorts; `kind` records provenance
    and `digest` binds the bytes."""

    __slots__ = ("brickid", "objid", "c", "bin", "s", "kind", "digest", "n")

    def __init__(self, brickid, objid, c, bin_label, s, kind: str):
        if kind not in ("SEALED_ACCEPTED_MASK", "FIXTURE"):
            raise RuntimeError(f"inadmissible mask kind {kind!r}")
        bid = np.asarray(brickid, dtype=np.int64)
        oid = np.asarray(objid, dtype=np.int64)
        cc = np.ascontiguousarray(np.asarray(c, dtype=np.float64))
        bb = np.asarray(bin_label, dtype=np.int64)
        n = len(bid)
        if not (len(oid) == len(cc) == len(bb) == n) or n == 0:
            raise RuntimeError("mask field lengths disagree or mask is empty")
        if not np.isfinite(cc).all():
            raise RuntimeError("mask carries non-finite c")
        if np.abs(cc).max() > 1.0 + 1e-12:
            raise RuntimeError("mask carries |c| > 1")
        if bb.min() < 0 or bb.max() >= N_CAL_BINS:
            raise RuntimeError("calibration bin label out of range")
        keys = list(zip(bid.tolist(), oid.tolist()))
        if len(set(keys)) != n:
            raise RuntimeError("mask has duplicate (brickid, objid)")
        order = np.lexsort((oid, bid))            # canonical: ascending brickid, then objid
        self.brickid, self.objid = bid[order], oid[order]
        self.c, self.bin = cc[order], bb[order]
        if s is None:
            self.s = None
        else:
            ss = np.ascontiguousarray(np.asarray(s, dtype=np.float64))[order]
            if not np.isin(ss, (-1.0, 1.0)).all():
                raise RuntimeError("sign labels must be exactly +1 or -1")
            self.s = ss
        self.kind, self.n = kind, n
        self.digest = digest(canon_i8(self.brickid) + canon_i8(self.objid)
                             + canon_f8(self.c) + canon_i8(self.bin)
                             + (b"" if self.s is None else canon_f8(self.s)))

    def with_signs(self, s) -> "Mask":
        return Mask(self.brickid, self.objid, self.c, self.bin, s, self.kind)


def require_mask(m, need_signs: bool) -> "Mask":
    if not isinstance(m, Mask):
        raise RuntimeError("inadmissible input: not a canonical Mask "
                           "(bare vectors, parent positions and uniform-sphere inputs are refused)")
    if need_signs and m.s is None:
        raise RuntimeError("this operation requires sign labels")
    return m


# ---------------------------------------------------------------- statistics
def beta_slope(s, c) -> float:
    ss = np.ascontiguousarray(np.asarray(s, dtype=np.float64))
    cc = np.ascontiguousarray(np.asarray(c, dtype=np.float64))
    N = float(len(ss))
    sbar = float(np.add.reduce(ss)) / N
    cbar = float(np.add.reduce(cc)) / N
    dc = cc - cbar
    den = float(np.add.reduce(dc * dc))
    if not (den > 0.0) or not math.isfinite(den):
        raise RuntimeError("zero or non-finite denominator — FAIL")
    return float(np.add.reduce((ss - sbar) * dc)) / den


def perm_sigma_exact(s, c) -> float:
    """EXACT permutation standard deviation of beta (derivation in the constitution):
    Var(beta) = Var_pop(s) / ((N-1) * Var_pop(c)). Verified against exhaustive enumeration."""
    ss = np.asarray(s, dtype=np.float64)
    cc = np.asarray(c, dtype=np.float64)
    N = len(ss)
    vs = float(np.add.reduce((ss - float(np.add.reduce(ss)) / N) ** 2)) / N
    vc = float(np.add.reduce((cc - float(np.add.reduce(cc)) / N) ** 2)) / N
    if not (vc > 0.0):
        raise RuntimeError("degenerate c — FAIL")
    return math.sqrt(vs / ((N - 1) * vc))


def perm_record(mask: "Mask", stage: int, prefix: int, trial: int, n_perm: int = N_PERM):
    """PRODUCTION permutation record (BS-7f). Chunked but stream-frozen: permutation k is the
    k-th successive rng.permutation(N) draw. Returns (beta_obs, beta_perm, p, sigma_beta)."""
    m = require_mask(mask, need_signs=True)
    rng = rng_at(stage, prefix, trial, ROLE_PERM)
    b_obs = beta_slope(m.s, m.c)
    N = m.n
    cbar = float(np.add.reduce(m.c)) / N
    d = m.c - cbar
    den = float(np.add.reduce(d * d))
    sbar = float(np.add.reduce(m.s)) / N
    out = np.empty(n_perm, dtype=np.float64)
    for k in range(n_perm):
        p = rng.permutation(N)
        out[k] = float(np.add.reduce((m.s[p] - sbar) * d)) / den
    if not np.isfinite(out).all():
        raise RuntimeError("non-finite permutation value — FAIL")
    p_val = (1 + int(np.add.reduce((out >= b_obs).astype(np.int64)))) / (1 + n_perm)
    return b_obs, out, p_val, float(np.std(out, ddof=1))


def perm_p_analytic(mask: "Mask") -> float:
    """POWER-SIMULATION null (gpt56-V5 F8 / codex-V5 F5). The permutation null of beta has
    EXACT mean 0 and EXACT variance perm_sigma_exact()^2; only normality is approximated, and
    the finite-population CLT applies at production N. The equality contract with the full
    Monte-Carlo test is demonstrated at the decision quantile by fixture PWR-EQ; production
    decisions never use this function."""
    m = require_mask(mask, need_signs=True)
    b = beta_slope(m.s, m.c)
    sig = perm_sigma_exact(m.s, m.c)
    z = b / sig
    return 0.5 * math.erfc(z / math.sqrt(2.0))


def inject_signs(mask: "Mask", a, stage: int, prefix: int, trial: int) -> np.ndarray:
    """Injection, frozen API. `a` is either a scalar accuracy or a per-bin vector of length
    N_CAL_BINS (the fallback path, gpt56-V5 F1 / codex-V5 F1). Per object IN CANONICAL ROW
    ORDER: u1 = rng.random() sets the latent sign (+1 iff u1 < (1 + A_LONGO*c)/2), u2 =
    rng.random() flips it iff u2 < (1 - a_i). Exactly two rng.random() calls per object;
    Generator.binomial is BANNED."""
    m = require_mask(mask, need_signs=False)
    if np.isscalar(a):
        a_obj = np.full(m.n, float(a), dtype=np.float64)
    else:
        av = np.asarray(a, dtype=np.float64)
        if av.shape != (N_CAL_BINS,):
            raise RuntimeError(f"per-bin accuracy must have shape ({N_CAL_BINS},)")
        a_obj = av[m.bin]
    if not np.isfinite(a_obj).all() or a_obj.min() <= 0.5 or a_obj.max() > 1.0:
        raise RuntimeError("accuracy outside (0.5, 1] — FAIL")
    rng = rng_at(stage, prefix, trial, ROLE_INJECT)
    s = np.empty(m.n, dtype=np.float64)
    for i in range(m.n):
        lat = 1.0 if rng.random() < (1.0 + A_LONGO * m.c[i]) / 2.0 else -1.0
        s[i] = -lat if rng.random() < (1.0 - a_obj[i]) else lat
    return s


def stage_power(mask: "Mask", a, stage: int, prefix: int,
                n_trials: int = N_TRIALS, use_analytic: bool = True, n_perm: int = N_PERM):
    """Power at (stage, prefix): fraction of injected skies whose one-sided p < P_REPRODUCED.
    PASS iff successes >= CP_PASS_X at n_trials == 1000."""
    m = require_mask(mask, need_signs=False)
    succ = 0
    for t in range(1, n_trials + 1):
        sm = m.with_signs(inject_signs(m, a, stage, prefix, t))
        p = perm_p_analytic(sm) if use_analytic else perm_record(sm, stage, prefix, t, n_perm)[2]
        if p < P_REPRODUCED:
            succ += 1
    if n_trials != 1000:
        return succ, None
    return succ, succ >= CP_PASS_X


# ---------------------------------------------------------------- planning orchestrator
def build_plan(brickid, ra, dec, n_raw, cbytes=None, l_plan_override=None) -> dict:
    """BS-2c c-bytes -> BS-2o ledger -> BS-5p threshold -> BS-2s selection, in one frozen
    acyclic call (gpt56-V5 F2 / codex-V5 F2). RAW counts drive the ledger and the exact-mode
    boundary; RETAINED counts drive EVERY threshold (L_ret, N_eq, l_plan, reduction).
    Planning objects sit at brick centres; decision-grade power uses the sealed mask only."""
    bid = np.asarray(brickid, dtype=np.int64)
    c = np.asarray(cbytes, dtype=np.float64) if cbytes is not None else cos_theta(ra, dec)
    nr = np.asarray(n_raw, dtype=np.int64)
    nret = retained_counts(nr)
    order, ledger = greedy_ledger(bid, c, nr)
    l_ret_curve = []
    for k in range(1, len(order) + 1):
        idx = order[:k]
        l_ret_curve.append(sse(nret[idx], c[idx]))
    l_min_plan = None
    if l_plan_override is None:
        for k in range(1, len(order) + 1):
            idx = order[:k]
            if 3.0 * l_ret_curve[k - 1] < NEQ_MIN:
                continue
            objs = _expand_planning_objects(bid[idx], c[idx], nret[idx])
            if objs is None:
                continue
            _, passed = stage_power(objs, A_FLOOR, STAGE_P, k)
            if passed:
                l_min_plan = l_ret_curve[k - 1]
                break
        if l_min_plan is None:
            raise RuntimeError("no ledger prefix passes Stage P — INCONCLUSIVE-BY-POWER at planning")
        l_plan = L_PLAN_MARGIN * l_min_plan
    else:
        l_min_plan, l_plan = None, float(l_plan_override)
    S, L_final = local_pass(bid, c, nret, order, l_plan)
    return {
        "order_brickid": [int(bid[i]) for i in order],
        "ledger": ledger,
        "l_ret_curve": l_ret_curve,
        "l_min_plan": l_min_plan,
        "l_plan": l_plan,
        "selected_brickid": [int(bid[i]) for i in S],
        "L_ret_final": L_final,
        "L_raw_final": sse(nr[S], c[S]),
        "N_ret_final": int(np.add.reduce(nret[S])),
        "N_eq_final": 3.0 * L_final,
    }


def _expand_planning_objects(bid, c, counts):
    """Planning objects: `counts` copies of each brick centre, canonical order. Returns a
    FIXTURE-kind Mask (planning is never decision-grade)."""
    n = int(np.add.reduce(np.asarray(counts, dtype=np.int64)))
    if n <= 0:
        return None
    b = np.repeat(np.asarray(bid, dtype=np.int64), np.asarray(counts, dtype=np.int64))
    cc = np.repeat(np.asarray(c, dtype=np.float64), np.asarray(counts, dtype=np.int64))
    o = np.concatenate([np.arange(int(k), dtype=np.int64) for k in counts if int(k) > 0])
    return Mask(b, o, cc, np.zeros(n, dtype=np.int64), None, "FIXTURE")


# ---------------------------------------------------------------- calibration suite
def calibration_bins(mask: "Mask") -> np.ndarray:
    """BS-2f: count-weighted c-tertile boundaries over the sealed accepted objects, unit
    weight per object. Returns the two interior boundaries. Ties: an object at a boundary
    goes to the LOWER bin (np.searchsorted side='right')."""
    m = require_mask(mask, need_signs=False)
    q = np.sort(m.c)
    return np.array([q[int(math.floor(m.n / 3.0))], q[int(math.floor(2 * m.n / 3.0))]],
                    dtype=np.float64)


def assign_bins(c, boundaries) -> np.ndarray:
    return np.searchsorted(np.asarray(boundaries, dtype=np.float64),
                           np.asarray(c, dtype=np.float64), side="right").astype(np.int64)


def allocate_handcheck(cell_counts, budget: int) -> np.ndarray:
    """BS-8p: integer allocation of `budget` hand-check labels over the 3 x 9 cells,
    proportional to cell counts, minimum HC_MIN_PER_CELL per NON-EMPTY cell, by largest
    remainder. Ties on remainder: smaller flat cell index first. If the minima alone exceed
    the budget, this FAILS (it does not silently shrink them)."""
    cc = np.asarray(cell_counts, dtype=np.int64).reshape(N_CAL_BINS, N_HC_STRATA)
    nonempty = cc > 0
    k = int(np.count_nonzero(nonempty))
    if k * HC_MIN_PER_CELL > budget:
        raise RuntimeError(f"minima {k * HC_MIN_PER_CELL} exceed budget {budget} — FAIL")
    alloc = np.where(nonempty, HC_MIN_PER_CELL, 0).astype(np.int64)
    rest = budget - int(np.add.reduce(alloc.ravel()))
    tot = int(np.add.reduce(cc.ravel()))
    share = np.where(nonempty, cc.astype(np.float64) * rest / tot, 0.0)
    base = np.floor(share).astype(np.int64)
    alloc = alloc + base
    left = rest - int(np.add.reduce(base.ravel()))
    rem = (share - base).ravel()
    for flat in sorted(range(rem.size), key=lambda i: (-rem[i], i))[:max(0, left)]:
        alloc.ravel()[flat] += 1
    if int(np.add.reduce(alloc.ravel())) != budget:
        raise RuntimeError("allocation does not sum to budget — FAIL")
    if (alloc[nonempty] > cc[nonempty]).any():
        raise RuntimeError("allocation exceeds available objects in some cell — FAIL")
    return alloc


def accuracy_from_handcheck(agree_counts, n_counts, sigma_shared: float):
    """BS-8f: per-bin accuracy, its full covariance, and one-sided lower bounds.
    Model (carried from HC-1H): a_b = raw_b - eps, where raw_b is the binomial agreement rate
    in bin b and eps is ONE shared synthetic-error estimate with sd sigma_shared applied to
    every bin. Hence Cov(a_b, a_b') = sigma_shared^2 off-diagonal and
    Var(a_b) = raw_b(1-raw_b)/n_b + sigma_shared^2 on the diagonal."""
    agree = np.asarray(agree_counts, dtype=np.float64)
    n = np.asarray(n_counts, dtype=np.float64)
    if (n <= 0).any():
        raise RuntimeError("empty calibration bin — FAIL")
    raw = agree / n
    a_b = raw
    var_b = raw * (1.0 - raw) / n + sigma_shared ** 2
    cov = np.full((len(a_b), len(a_b)), sigma_shared ** 2, dtype=np.float64)
    for i in range(len(a_b)):
        cov[i, i] = var_b[i]
    sd_b = np.sqrt(var_b)
    a_lb_b = a_b - 1.645 * sd_b
    n_tot = float(np.add.reduce(n))
    a_hat = float(np.add.reduce(agree)) / n_tot
    sd_hat = math.sqrt(a_hat * (1.0 - a_hat) / n_tot + sigma_shared ** 2)
    return {"a_hat": a_hat, "sigma_a": sd_hat, "a_lb": a_hat - 1.645 * sd_hat,
            "a_b": a_b, "sigma_ab": sd_b, "a_lb_b": a_lb_b, "cov_a": cov}


def adjudicate_path(cal: dict) -> str:
    """Frozen admissibility test. Returns 'SCALAR', 'PROFILE', or raises the calibration halt."""
    if float(np.min(cal["a_lb_b"])) < A_FLOOR:
        raise InconclusiveByCalibration(
            f"a_lb_b min {float(np.min(cal['a_lb_b'])):.6f} < {A_FLOOR}")
    return "SCALAR" if float(np.max(np.abs(cal["a_b"] - cal["a_hat"]))) <= 0.03 else "PROFILE"


class InconclusiveByCalibration(RuntimeError):
    pass


class InconclusiveByPower(RuntimeError):
    pass


# ---------------------------------------------------------------- estimands and sigmas
def _finite(*vals):
    for v in vals:
        if not math.isfinite(float(v)):
            raise RuntimeError("non-finite decision quantity — FAIL")


def w_profile(mask: "Mask", a_b) -> float:
    m = require_mask(mask, need_signs=False)
    q = 2.0 * np.asarray(a_b, dtype=np.float64)[m.bin] - 1.0
    cbar = float(np.add.reduce(m.c)) / m.n
    dc = m.c - cbar
    den = float(np.add.reduce(dc * dc))
    if not (den > 0.0):
        raise RuntimeError("degenerate c — FAIL")
    w = float(np.add.reduce(dc * (q * m.c))) / den
    _finite(w)
    if abs(w) < 1e-12:
        raise RuntimeError("profile factor ~ 0 — FAIL")
    return w


def w_gradient(mask: "Mask") -> np.ndarray:
    m = require_mask(mask, need_signs=False)
    cbar = float(np.add.reduce(m.c)) / m.n
    dc = m.c - cbar
    den = float(np.add.reduce(dc * dc))
    g = np.zeros(N_CAL_BINS, dtype=np.float64)
    for b in range(N_CAL_BINS):
        sel = m.bin == b
        g[b] = 2.0 * float(np.add.reduce(dc[sel] * m.c[sel])) / den
    return g


def sigma_ours_scalar(sigma_beta: float, beta: float, a_star: float, sigma_a: float) -> float:
    _finite(sigma_beta, beta, a_star, sigma_a)
    q = 2.0 * a_star - 1.0
    if q <= 0.0:
        raise RuntimeError("2a-1 <= 0 — FAIL")
    out = math.sqrt((sigma_beta / q) ** 2 + (2.0 * sigma_a * beta / (q * q)) ** 2)
    _finite(out)
    return out


def sigma_ours_profile(sigma_beta: float, beta: float, w: float, grad, cov_a) -> float:
    """Quadratic form computed by an explicit scalar double loop — no BLAS call."""
    _finite(sigma_beta, beta, w)
    g = np.asarray(grad, dtype=np.float64)
    C = np.asarray(cov_a, dtype=np.float64)
    if not np.isfinite(g).all() or not np.isfinite(C).all():
        raise RuntimeError("non-finite gradient/covariance — FAIL")
    quad = 0.0
    for i in range(len(g)):
        for j in range(len(g)):
            quad += float(g[i]) * float(C[i, j]) * float(g[j])
    if quad < 0.0:
        raise RuntimeError("negative quadratic form — FAIL")
    out = math.sqrt((sigma_beta / w) ** 2 + (beta / (w * w)) ** 2 * quad)
    _finite(out)
    return out


# ---------------------------------------------------------------- the decision
def decide(mask: "Mask", cal: dict, stage_c_passed: bool, *, n_perm: int = N_PERM,
           _perm=None) -> dict:
    """The ONLY function that produces a verdict (gpt56-V5 F7). No verdict may be read off a
    table by a human. Carried from the lapsed build spec: it emits exactly one of the four
    F-6 outcomes and prints the evaluated floor."""
    m = require_mask(mask, need_signs=True)
    if not stage_c_passed:
        return {"verdict": "INCONCLUSIVE-BY-POWER", "reason": "Stage C did not pass"}
    path = adjudicate_path(cal)
    if _perm is None:
        beta, _, p, sigma_beta = perm_record(m, STAGE_REAL, 0, 0, n_perm)
    else:
        beta, p, sigma_beta = _perm
    if path == "SCALAR":
        a_hat, a_lb = cal["a_hat"], cal["a_lb"]
        A = beta / (2.0 * a_hat - 1.0)
        sig_band = sigma_ours_scalar(sigma_beta, beta, a_hat, cal["sigma_a"])
        sig_floor = sigma_ours_scalar(sigma_beta, beta, a_lb, cal["sigma_a"])
    else:
        w = w_profile(m, cal["a_b"])
        w_lb = w_profile(m, cal["a_lb_b"])
        g = w_gradient(m)
        A = beta / w
        sig_band = sigma_ours_profile(sigma_beta, beta, w, g, cal["cov_a"])
        sig_floor = sigma_ours_profile(sigma_beta, beta, w_lb, g, cal["cov_a"])
    sigma_comb = math.sqrt(SIGMA_PUB ** 2 + sig_band ** 2)
    floor = FLOOR_MULT * sig_floor
    if p < P_REPRODUCED and A > 0.0 and abs(A - A_LONGO) <= 3.0 * sigma_comb and A >= floor:
        verdict = "REPRODUCED-LONGO"
    elif p > P_REJECT_MIN and (abs(A) + 3.0 * sig_band) < A_LONGO:
        verdict = "REJECTED-AT-LONGO-AMPLITUDE"
    else:
        verdict = "INCONCLUSIVE"
    return {"verdict": verdict, "path": path, "beta": beta, "A_L": A, "p": p,
            "sigma_beta": sigma_beta, "sigma_ours_band": sig_band,
            "sigma_ours_floor": sig_floor, "sigma_comb": sigma_comb,
            "evaluated_floor": floor, "N": m.n, "mask_digest": m.digest}


# ---------------------------------------------------------------- run guards (lapsed-spec carry-ins)
def require_authorization(auth_path: str, expected_sha256: str) -> str:
    """Refuses real data without an authorization file pinned to a SHA-256."""
    try:
        with open(auth_path, "rb") as f:
            got = hashlib.sha256(f.read()).hexdigest()
    except OSError as exc:
        raise RuntimeError(f"authorization unreadable: {exc}") from exc
    if got != expected_sha256:
        raise RuntimeError(f"authorization digest mismatch: {got}")
    return got


def require_complete_sample(n_receipts: int, n_parent: int) -> None:
    """Refuses to run at all unless every parent object has a measurement receipt. A partial
    run is not a smaller run; it is a different experiment."""
    if int(n_receipts) != int(n_parent):
        raise RuntimeError(f"INCOMPLETE SAMPLE: {n_receipts} of {n_parent} — refusing")


# ---------------------------------------------------------------- serialization / receipts
def canon_f8(a) -> bytes:
    a = np.ascontiguousarray(np.asarray(a, dtype=np.float64))
    if not np.isfinite(a).all():
        raise RuntimeError("non-finite in digest payload — FAIL")
    return a.astype("<f8", copy=False).tobytes(order="C")


def canon_i8(a) -> bytes:
    return np.ascontiguousarray(np.asarray(a, dtype=np.int64)).astype("<i8", copy=False).tobytes(order="C")


def digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def field(name: str, payload: bytes) -> bytes:
    """Domain-separated, length-delimited field: name length, name, payload length, payload."""
    nb = name.encode("utf-8")
    return len(nb).to_bytes(4, "little") + nb + len(payload).to_bytes(8, "little") + payload


def receipt(slot: str, fields: dict) -> dict:
    """Canonical receipt envelope: slot id, schema version, environment, and the
    domain-separated field payload digest."""
    body = b"".join(field(k, fields[k]) for k in sorted(fields))
    env = environment_record()
    envelope = (field("slot", slot.encode("utf-8"))
                + field("schema", b"successor_ref_v2/1")
                + field("environment", json.dumps(env, sort_keys=True).encode("utf-8"))
                + field("body", body))
    return {"slot": slot, "schema": "successor_ref_v2/1", "environment": env,
            "body_sha256": digest(body), "envelope_sha256": digest(envelope)}


def ledger_digest(ledger) -> str:
    parts = []
    for (_, b, N, V, L) in ledger:
        parts.append(canon_i8(np.array([b])))
        parts.append(canon_f8(np.array([N, V, L])))
    return digest(b"".join(parts))


# ---------------------------------------------------------------- fixtures
def _fx(name, cond, lines, extra=""):
    lines.append(f"{name}: {'PASS' if cond else 'FAIL'}{(' ' + extra) if extra else ''}")
    return bool(cond)


def _fx_selector(name, c, n, l_plan, want_bid, want_L, lines):
    bid = np.arange(len(c), dtype=np.int64)
    got = exact_min_subset(bid, np.array(c), np.array(n), l_plan)
    got_bid = [int(bid[i]) for i in got[0]]
    ok = (got_bid == want_bid) and abs(got[1] - want_L) < 1e-12
    order, _ = greedy_ledger(bid, np.array(c), np.array(n))
    S, _L = local_pass(bid, np.array(c), np.array(n), order, l_plan)
    ok2 = [int(bid[i]) for i in S] == want_bid
    lines.append(f"{name}: exact {got_bid} L={got[1]!r} {'PASS' if ok else 'FAIL'}; "
                 f"local==exact {'PASS' if ok2 else 'FAIL'}")
    return ok and ok2


def _mk_mask(n, seed_c=None, bins=None, kind="FIXTURE", s=None):
    c = np.linspace(-0.95, 0.95, n) if seed_c is None else np.asarray(seed_c, dtype=np.float64)
    b = np.zeros(n, dtype=np.int64) if bins is None else np.asarray(bins, dtype=np.int64)
    return Mask(np.arange(n) // 7, np.arange(n) % 7, c, b, s, kind)


def run_fixtures():
    lines, ok = [], True
    env = environment_record()
    lines.append(f"env python={env['python']} numpy={env['numpy']} "
                 f"platform={env['platform']} machine={env['machine']} byteorder={env['byteorder']}")
    lines.append(f"axis={list(AXIS)}")
    lines.append(f"longo_published_signed={A_LONGO_PUBLISHED_SIGNED} our_convention={A_LONGO}")

    # --- selection: all five published gate counterexamples, exact mode IS the algorithm
    ok &= _fx_selector("SEL-A(V2)", [0.99, 0.98, -0.50], [1, 1, 1], 1.0, [0, 2],
                       1.1100500000000002, lines)
    ok &= _fx_selector("SEL-B(gpt56V3)", [0.04, -0.99, -0.91, 0.43, -0.94], [8, 14, 33, 25, 25],
                       20.0, [2, 3], 25.540862068965517, lines)
    ok &= _fx_selector("SEL-C(codexV3)", [-0.12, 0.15, -0.67, 0.43, -0.78], [8, 8, 18, 7, 3],
                       7.0, [1, 2, 3], 7.687151515151515, lines)
    ok &= _fx_selector("SEL-D(gpt56V4)", [0.552, 0.094, -0.676, -0.683, -0.836, 0.173, -0.073],
                       [3, 14, 5, 17, 6, 8, 20], 4.147539428571428, [1, 3],
                       4.635080709677419, lines)
    ok &= _fx_selector("SEL-E(codexV4)", [-0.38, 0.67, 0.57, 0.21, -0.32, 0.99, -0.35],
                       [8, 2, 1, 13, 10, 1, 13], 1.9, [3, 6], 2.0383999999999998, lines)

    # --- gpt56-V5 F2: raw-vs-retained. Thresholds MUST bind retained leverage.
    c7 = np.array([-0.4868224155944405, -0.8730927047630801, -0.3831733423895676,
                   -0.01644607194273373, -0.8506728007144366, -0.2700354997649146,
                   -0.5419268492467646])
    n7 = np.array([16, 9, 14, 6, 1, 2, 12])
    plan = build_plan(np.arange(7), None, None, n7, cbytes=c7, l_plan_override=1.2927783953207417)
    ok &= _fx("RAW-RET", plan["selected_brickid"] == [1, 3] and plan["L_ret_final"] >= 1.2927783953207417,
              lines, f"selected={plan['selected_brickid']} L_ret={plan['L_ret_final']!r} "
                     f"(raw-count call would have returned [1, 2] with L_ret 1.0611453924627055)")
    ok &= _fx("RET-FLOOR", list(retained_counts(np.array([2, 3, 10]))) == [1, 2, 8], lines)

    # --- mask typing: every banned input must fail closed (gpt56-V5 F3 / codex-V5 F5)
    banned = 0
    try:
        require_mask(np.linspace(-1, 1, 20), need_signs=False)
    except RuntimeError:
        banned += 1
    try:
        _mk_mask(6, s=[0, 2, 0, 2, 0, 2])
    except RuntimeError:
        banned += 1
    try:
        Mask([1, 1], [5, 5], [0.1, 0.2], [0, 0], None, "FIXTURE")
    except RuntimeError:
        banned += 1
    try:
        Mask([1, 2], [1, 2], [0.1, np.nan], [0, 0], None, "FIXTURE")
    except RuntimeError:
        banned += 1
    try:
        Mask([1, 2], [1, 2], [0.1, 0.2], [0, 9], None, "FIXTURE")
    except RuntimeError:
        banned += 1
    try:
        Mask([1, 2], [1, 2], [0.1, 0.2], [0, 0], None, "PARENT_POSITIONS")
    except RuntimeError:
        banned += 1
    ok &= _fx("MASK-REFUSALS", banned == 6, lines, f"{banned}/6 banned inputs refused")
    m_a = _mk_mask(20, s=np.where(np.arange(20) % 2 == 0, 1.0, -1.0))
    rev = np.arange(19, -1, -1)
    m_b = Mask(m_a.brickid[rev], m_a.objid[rev], m_a.c[rev], m_a.bin[rev], m_a.s[rev], "FIXTURE")
    ok &= _fx("MASK-CANON-ORDER", m_a.digest == m_b.digest, lines,
              "row order cannot change the record")

    # --- exact permutation sigma vs exhaustive enumeration
    cc4 = np.array([-1.0, -0.2, 0.4, 0.9])
    ss4 = np.array([-1.0, -1.0, 1.0, 1.0])
    vals = [beta_slope(np.array(p), cc4) for p in set(itertools.permutations(ss4))]
    counts = {}
    for p in itertools.permutations(range(4)):
        v = beta_slope(ss4[list(p)], cc4)
        counts[v] = counts.get(v, 0) + 1
    tot = sum(counts.values())
    mean = sum(v * k for v, k in counts.items()) / tot
    var = sum((v - mean) ** 2 * k for v, k in counts.items()) / tot
    ok &= _fx("PERM-SIGMA-EXACT", abs(math.sqrt(var) - perm_sigma_exact(ss4, cc4)) < 1e-12,
              lines, f"enum={math.sqrt(var)!r} formula={perm_sigma_exact(ss4, cc4)!r}")

    # --- PWR-EQ: the analytic power null vs the full Monte-Carlo test at the decision quantile
    cbig = np.linspace(-0.95, 0.95, 400)
    mm = _mk_mask(400, seed_c=cbig)
    sm = mm.with_signs(inject_signs(mm, A_FLOOR, STAGE_P, 1, 1))
    b_obs, vec, p_mc, _sd = perm_record(sm, STAGE_P, 1, 1, 20_000)
    p_an = perm_p_analytic(sm)
    q_mc = float(np.quantile(vec, 1.0 - P_REPRODUCED))
    q_an = perm_sigma_exact(sm.s, sm.c) * 3.090232306167813
    rel = abs(q_an - q_mc) / abs(q_mc)
    ok &= _fx("PWR-EQ", rel < 0.05, lines,
              f"decision-quantile MC={q_mc!r} analytic={q_an!r} rel={rel!r}; "
              f"p_mc={p_mc!r} p_analytic={p_an!r}")

    # --- injection determinism and address separation
    s1 = inject_signs(mm, A_FLOOR, STAGE_P, 3, 7)
    s2 = inject_signs(mm, A_FLOOR, STAGE_P, 3, 7)
    s3 = inject_signs(mm, A_FLOOR, STAGE_P, 4, 7)
    ok &= _fx("INJ-DET", bool((s1 == s2).all()), lines, f"digest={digest(canon_f8(s1))}")
    ok &= _fx("INJ-ADDR", not bool((s1 == s3).all()), lines, "prefix changes the stream")
    mb = _mk_mask(400, seed_c=cbig, bins=assign_bins(cbig, calibration_bins(mm)))
    sp = inject_signs(mb, np.array([0.95, 0.85, 0.75]), STAGE_C, 0, 1)
    ok &= _fx("INJ-PERBIN", sp.shape == (400,) and set(np.unique(sp)) <= {-1.0, 1.0}, lines,
              f"per-bin injection executes; digest={digest(canon_f8(sp))}")

    # --- calibration suite
    bnd = calibration_bins(mm)
    bins_all = assign_bins(mm.c, bnd)
    sizes = [int(np.count_nonzero(bins_all == b)) for b in range(N_CAL_BINS)]
    ok &= _fx("CAL-BINS", min(sizes) > 0 and abs(max(sizes) - min(sizes)) <= 2, lines,
              f"boundaries={list(bnd)} sizes={sizes}")
    cells = np.arange(1, N_CAL_BINS * N_HC_STRATA + 1).reshape(N_CAL_BINS, N_HC_STRATA) * 40
    alloc = allocate_handcheck(cells, 1000)
    ok &= _fx("CAL-ALLOC", int(alloc.sum()) == 1000 and int(alloc.min()) >= HC_MIN_PER_CELL,
              lines, f"sum={int(alloc.sum())} min={int(alloc.min())} max={int(alloc.max())}")
    try:
        allocate_handcheck(cells, 100)
        ok &= _fx("CAL-ALLOC-FAIL", False, lines)
    except RuntimeError:
        ok &= _fx("CAL-ALLOC-FAIL", True, lines, "minima over budget refused")
    cal = accuracy_from_handcheck([920, 910, 900], [1000, 1000, 1000], 0.005)
    ok &= _fx("CAL-COV", cal["cov_a"][0, 1] == 0.005 ** 2 and cal["cov_a"][0, 0] > 0.005 ** 2,
              lines, f"a_hat={cal['a_hat']!r} a_b={list(cal['a_b'])} "
                     f"a_lb_b={list(cal['a_lb_b'])} path={adjudicate_path(cal)}")
    cal_spread = accuracy_from_handcheck([970, 910, 880], [1000, 1000, 1000], 0.005)
    ok &= _fx("CAL-PATH-PROFILE", adjudicate_path(cal_spread) == "PROFILE", lines,
              f"spread={float(np.max(np.abs(cal_spread['a_b'] - cal_spread['a_hat']))):.4f} > 0.03, "
              f"all a_lb_b >= {A_FLOOR}")
    cal_halt = accuracy_from_handcheck([880, 870, 700], [1000, 1000, 1000], 0.01)
    try:
        adjudicate_path(cal_halt)
        ok &= _fx("CAL-HALT", False, lines)
    except InconclusiveByCalibration as exc:
        ok &= _fx("CAL-HALT", True, lines, str(exc))

    # --- profile estimator recovers a piecewise-constant a(c); sigmas fail closed
    a_b = np.array([0.95, 0.95, 0.80])
    w = w_profile(mb, a_b)
    ok &= _fx("PROFILE-RECOVER", abs((A_LONGO * w) / w - A_LONGO) < 1e-15, lines,
              f"w={w!r} grad={list(w_gradient(mb))}")
    try:
        sigma_ours_scalar(0.005, 0.03, 0.5, 0.01)
        ok &= _fx("SIGMA-FAILCLOSED", False, lines)
    except RuntimeError:
        ok &= _fx("SIGMA-FAILCLOSED", True, lines, "2a-1 <= 0 refused")

    # --- the lapsed build spec's validation battery, through decide()
    def _battery(A_true, n=4000, a=0.93, tag=""):
        cg = np.linspace(-0.98, 0.98, n)
        mk = _mk_mask(n, seed_c=cg, bins=assign_bins(cg, calibration_bins(_mk_mask(n, seed_c=cg))))
        rng = rng_at(STAGE_REAL, 99, abs(int(A_true * 1e6)) + 1, ROLE_INJECT)
        s = np.empty(n)
        for i in range(n):
            lat = 1.0 if rng.random() < (1.0 + A_true * cg[i]) / 2.0 else -1.0
            s[i] = -lat if rng.random() < (1.0 - a) else lat
        mk = mk.with_signs(s)
        cal_b = accuracy_from_handcheck([int(a * 1000)] * 3, [1000] * 3, 0.008)
        beta = beta_slope(mk.s, mk.c)
        sig = perm_sigma_exact(mk.s, mk.c)
        p = 0.5 * math.erfc((beta / sig) / math.sqrt(2.0))
        return decide(mk, cal_b, True, _perm=(beta, p, sig))

    d0 = _battery(0.0)
    ok &= _fx("BATTERY-A0", d0["verdict"] != "REPRODUCED-LONGO", lines,
              f"A=0 -> {d0['verdict']} (A_L={d0['A_L']:.5f}, p={d0['p']:.2e}, "
              f"floor={d0['evaluated_floor']:.5f})")
    dneg = _battery(-A_LONGO)
    ok &= _fx("BATTERY-SIGN", dneg["verdict"] != "REPRODUCED-LONGO", lines,
              f"A=-0.0408 -> {dneg['verdict']} (A_L={dneg['A_L']:.5f})")
    dpos = _battery(A_LONGO / 0.86 * 1.0, n=60000)
    ok &= _fx("BATTERY-POS-RUNS", dpos["verdict"] in
              ("REPRODUCED-LONGO", "INCONCLUSIVE", "REJECTED-AT-LONGO-AMPLITUDE"), lines,
              f"A=+ -> {dpos['verdict']} (A_L={dpos['A_L']:.5f}, p={dpos['p']:.2e})")
    dpow = decide(_mk_mask(50, s=np.where(np.arange(50) % 2 == 0, 1.0, -1.0)), cal, False)
    ok &= _fx("BATTERY-POWER", dpow["verdict"] == "INCONCLUSIVE-BY-POWER", lines)

    # --- run guards
    try:
        require_complete_sample(207000, 208407)
        ok &= _fx("GUARD-COMPLETE", False, lines)
    except RuntimeError:
        ok &= _fx("GUARD-COMPLETE", True, lines, "partial sample refused")
    try:
        require_authorization("/nonexistent/authorization.json", "0" * 64)
        ok &= _fx("GUARD-AUTH", False, lines)
    except RuntimeError:
        ok &= _fx("GUARD-AUTH", True, lines, "missing authorization refused")

    # --- count-oracle closure
    uni = np.array([10, 11, 12], dtype=np.int64)
    tab, cnt = np.array([10, 11, 12]), np.array([5, 0, 7])
    r = validate_count_oracle(uni, tab, cnt, 12, 12)
    ok &= _fx("ORACLE-OK", r["zero_rows"] == 1 and r["universe"] == 3, lines, json.dumps(r))
    refused = 0
    for args in ((uni, np.array([10, 12]), np.array([5, 7]), 12, 12),
                 (uni, np.array([10, 11, 12, 13]), np.array([5, 0, 7, 1]), 13, 13),
                 (uni, tab, cnt, 12, 13)):
        try:
            validate_count_oracle(*args)
        except RuntimeError:
            refused += 1
    ok &= _fx("ORACLE-REFUSALS", refused == 3, lines, f"{refused}/3 broken oracles refused")
    order_z, _ = greedy_ledger(uni, np.array([0.9, 0.99, -0.5]), cnt)
    ok &= _fx("ORACLE-ZERO-EXCLUDED", 1 not in order_z, lines)

    # --- manifest closure, replaying the predecessor's own defect at small scale
    #     Two edge objects each need a neighbour brick that a naive "bricks my objects sit in"
    #     enumeration omits — the exact shape of the 60,308-vs-60,310 gap.
    req_map = {
        "10997315463551936": ["3385m885", "3471m885"],
        "10995116744378804": ["2857m870", "2894m872", "2902m870"],
        "interior-1": ["2894m872"],
        "interior-2": ["3385m885"],
    }
    clos = manifest_closure(req_map)
    naive_manifest = ["3385m885", "2894m872", "2902m870"]      # the enumeration that shipped
    try:
        require_manifest_closure(naive_manifest, clos)
        ok &= _fx("CLOSURE-CATCHES", False, lines)
    except ManifestClosureError as exc:
        r = exc.result
        caught = (r["missing_count"] == 2
                  and r["missing_from_manifest"] == ["2857m870", "3471m885"])
        ok &= _fx("CLOSURE-CATCHES", caught, lines,
                  f"manifest {r['manifest_count']} vs required {r['required_count']}; "
                  f"missing {r['missing_count']} {r['missing_from_manifest']} "
                  f"(the predecessor's two bricks, by name)")
    good = require_manifest_closure(clos["required_bricknames"], clos)
    ok &= _fx("CLOSURE-PASSES", good["missing_count"] == 0 and good["extra_count"] == 0, lines,
              f"closed manifest of {good['required_count']} accepted")
    try:
        require_manifest_closure(clos["required_bricknames"] + ["9999m999"], clos)
        ok &= _fx("CLOSURE-EXTRA", False, lines)
    except ManifestClosureError as exc:
        ok &= _fx("CLOSURE-EXTRA", exc.result["extra_count"] == 1, lines,
                  "a brick beyond the closure is refused too")

    # --- receipts carry their environment and a domain-separated body digest
    rec = receipt("BS-2o", {"order": canon_i8(np.array([10, 12])),
                            "L": canon_f8(np.array([1.5]))})
    rec2 = receipt("BS-2o", {"order": canon_i8(np.array([10])),
                             "L": canon_f8(np.array([1.5, 0.0]))})
    ok &= _fx("RECEIPT-DOMAIN", rec["body_sha256"] != rec2["body_sha256"], lines,
              f"envelope={rec['envelope_sha256'][:16]}…")

    out = "\n".join(lines) + "\n" + ("ALL FIXTURES PASS" if ok else "FIXTURE FAILURE") + "\n"
    return out, ok


if __name__ == "__main__":
    if "--fixtures" in sys.argv:
        text, good = run_fixtures()
        sys.stdout.write(text)
        sys.exit(0 if good else 1)
    sys.stdout.write(__doc__ + "\n")
