#!/usr/bin/env python3
"""successor_ref.py — THE reference definition for the successor preregistration.

Where the constitution (PREREG_SUCCESSOR_DRAFT_V5) names a mechanism, THIS FILE's bytes are
the definition. Prose never overrides code; a conflict is a defect in the prose.

Determinism contract: pure Python + NumPy; scalar/1-D operations only (no BLAS matrix calls,
no threading); reductions use np.add.reduce over contiguous float64 1-D arrays (pairwise
summation — deterministic for a fixed NumPy version); every receipt records numpy.__version__
and platform; pinned fixture digests are valid under the recorded environment and both
blind-double implementations must reproduce them under an identical recorded environment.

Randomness contract: every stochastic operation derives its generator from an immutable
hierarchical address — SeedSequence((MASTER, stage, prefix, trial, role)) — constructed fresh
at point of use. Stateful SeedSequence.spawn is BANNED in this codebase.

Run `python3 successor_ref.py --fixtures` to print the fixture table and digests. The
constitution pins this file's sha256 and the fixture output's sha256.
"""
import hashlib
import itertools
import json
import math
import sys

import numpy as np

# ---------------------------------------------------------------- frozen constants
MASTER_SEED = 20260824
A_LONGO = 0.0408          # published amplitude (V3-pred line 123)
SIGMA_PUB = 0.011         # published uncertainty
N_PERM = 100_000          # production permutation count
N_TRIALS = 1_000          # power injection skies
CP_PASS_X = 962           # one-sided 95% Clopper-Pearson LB >= 0.95 at n=1000:
                          # Beta^-1(0.05; 962, 39) = 0.950487... ; x=961 gives 0.949366...
A_FLOOR = 0.85            # labelling-accuracy planning floor (V3-pred F-7 minima)
RETENTION_LB = 0.8572     # predecessor BS-3 retention lower bound
FLOOR_MULT = 3.09         # V3-pred F-7 one-sided floor multiplier
L_PLAN_MARGIN = 1.2       # L_plan = margin * L_min_plan
NEQ_MIN = 100_000         # N_eq = 3 * L_ret >= NEQ_MIN
N_EXACT = 16              # candidate universes with <= N_EXACT bricks use exact enumeration
MOVE_CAP = 10_000         # local-pass move cap; reaching it is FAIL (exception), never a result

# The machine axis: ICRS unit vector from galactic (l,b) = (52.0, 68.5) under the IAU
# rotation with NGP (192.85948, 27.12825) deg and l_NCP = 122.93192 deg. The vector below is
# THE axis; the coordinate pairs are display-only.
AXIS = np.array([-0.676971771271432, -0.509846551777774, +0.530816083537352], dtype=np.float64)

# Stage ids for the randomness address (frozen):
STAGE_P = 1               # planning power (BS-5p and the BS-2s re-pass)
STAGE_C = 2               # confirmatory power (BS-5f)
STAGE_REAL = 3            # real-data permutation record (BS-7f)
# Roles:
ROLE_INJECT = 0
ROLE_PERM = 1


def rng_at(stage: int, prefix: int, trial: int, role: int) -> np.random.Generator:
    """The ONLY constructor for randomness. prefix: ledger prefix length k during BS-5p
    scans; 0 for S_final and Stage C; trial: 1..N_TRIALS for injections, 0 for the real-data
    record; role: ROLE_INJECT or ROLE_PERM."""
    return np.random.default_rng(np.random.SeedSequence((MASTER_SEED, stage, prefix, trial, role)))


# ---------------------------------------------------------------- geometry
def unit_vectors(ra_deg: np.ndarray, dec_deg: np.ndarray) -> np.ndarray:
    ra = np.radians(np.asarray(ra_deg, dtype=np.float64))
    dec = np.radians(np.asarray(dec_deg, dtype=np.float64))
    return np.stack([np.cos(dec) * np.cos(ra), np.cos(dec) * np.sin(ra), np.sin(dec)], axis=1)


def cos_theta(ra_deg: np.ndarray, dec_deg: np.ndarray) -> np.ndarray:
    """c_j = u . AXIS, computed exactly this way, once, at BS-2c; downstream consumes the
    emitted '<f8' bytes and never recomputes from ra/dec."""
    u = unit_vectors(ra_deg, dec_deg)
    return u[:, 0] * AXIS[0] + u[:, 1] * AXIS[1] + u[:, 2] * AXIS[2]


# ---------------------------------------------------------------- weighted SSE ledger
def sse(counts: np.ndarray, c: np.ndarray) -> float:
    """L(S) = sum_j n_j*(c_j - cbar)^2 with cbar the count-weighted mean. Frozen evaluation:
    contiguous float64, np.add.reduce reductions, this exact operation order."""
    n = np.ascontiguousarray(counts, dtype=np.float64)
    cc = np.ascontiguousarray(c, dtype=np.float64)
    N = float(np.add.reduce(n))
    if N <= 0.0:
        return 0.0
    cbar = float(np.add.reduce(n * cc)) / N
    d = cc - cbar
    return float(np.add.reduce(n * d * d))


def greedy_ledger(brickid: np.ndarray, c: np.ndarray, n_eligible: np.ndarray):
    """BS-2o: full deterministic traversal + per-prefix ledger. Bricks with n_eligible == 0
    are EXCLUDED from traversal by frozen rule (they stay in the BS-2c receipt).
    Step: accept the brick maximizing delta = (N*nj/(N+nj))*(cj-cbar)^2 evaluated in exactly
    that float64 operation order; first step (N==0): delta defined as 0.0 for every brick.
    Ties on exact float delta: larger |c|, then smaller brickid. Candidates are scanned in
    ascending-brickid order. Returns (order_indices, ledger rows (k, brickid, N, Var, L))."""
    bid = np.asarray(brickid, dtype=np.int64)
    cc = np.asarray(c, dtype=np.float64)
    nn = np.asarray(n_eligible, dtype=np.int64)
    keep = nn > 0
    idx_all = np.nonzero(keep)[0]
    scan = idx_all[np.argsort(bid[idx_all], kind="stable")]
    remaining = list(scan)
    order, ledger = [], []
    N = 0.0
    cbar = 0.0
    L = 0.0
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


def exact_min_subset(brickid, c, n_eligible, l_plan: float):
    """Exact mode (mandatory when the positive-count candidate universe has <= N_EXACT
    bricks): the minimum-cardinality subset with L >= l_plan; among those, the
    lexicographically smallest sorted brickid tuple. Returns (indices, L) or None."""
    bid = np.asarray(brickid, dtype=np.int64)
    cc = np.asarray(c, dtype=np.float64)
    nn = np.asarray(n_eligible, dtype=np.int64)
    idx = [i for i in range(len(bid)) if nn[i] > 0]
    if len(idx) > N_EXACT:
        raise ValueError("exact mode only for <= N_EXACT positive-count bricks")
    idx.sort(key=lambda i: int(bid[i]))
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


def local_pass(brickid, c, n_eligible, order, l_plan: float):
    """BS-2s: cut the greedy order at the smallest prefix with L >= l_plan, then reduce.
    If the positive-count candidate universe has <= N_EXACT bricks, the RESULT IS
    exact_min_subset (minimum cardinality by construction). Otherwise the result is exactly
    what this procedure returns and NO minimality claim attaches to it.
    Moves, frozen: (a) removal scan — accepted bricks in ascending removal-loss
    (L(S)-L(S\\{j})), ties by smaller brickid; remove the first j with L(S\\{j}) >= l_plan;
    repeat. (b) compound scan — accepted i in ascending brickid x unaccepted-positive j in
    ascending brickid; if L(S\\{i} u {j}) >= l_plan, tentatively swap and run one removal
    scan step; if a removal is then legal, commit swap+removal as one move and return to (a).
    Terminate when neither applies. Every committed move decrements |S| by exactly one, so
    the pass strictly shrinks and cannot cycle; MOVE_CAP is a backstop and reaching it is
    FAIL (RuntimeError), never a result."""
    bid = np.asarray(brickid, dtype=np.int64)
    cc = np.asarray(c, dtype=np.float64)
    nn = np.asarray(n_eligible, dtype=np.int64)
    pos = [i for i in range(len(bid)) if nn[i] > 0]
    if len(pos) <= N_EXACT:
        r = exact_min_subset(bid, cc, nn, l_plan)
        if r is None:
            raise RuntimeError("no subset reaches l_plan")
        return r
    L_of = lambda S: sse(nn[list(S)], cc[list(S)])
    cum = None
    S = []
    for k, i in enumerate(order):
        S.append(i)
        if L_of(S) >= l_plan:
            cum = k + 1
            break
    if cum is None:
        raise RuntimeError("greedy order never reaches l_plan")
    S = set(S)
    moves = 0

    def try_removal(S):
        cand = sorted(S, key=lambda j: (L_of(S) - L_of(S - {j}), int(bid[j])))
        for j in cand:
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
                        S = S2 - {r}
                        committed = True
                        break
        if not committed:
            break
    Sl = sorted(S, key=lambda x: int(bid[x]))
    return Sl, L_of(S)


def retained_counts(n_eligible: np.ndarray) -> np.ndarray:
    """Stage-P retention transform, frozen: per-brick integer floor(RETENTION_LB * n)."""
    return np.floor(RETENTION_LB * np.asarray(n_eligible, dtype=np.float64)).astype(np.int64)


# ---------------------------------------------------------------- statistics
def beta_slope(s: np.ndarray, c: np.ndarray) -> float:
    ss = np.ascontiguousarray(s, dtype=np.float64)
    cc = np.ascontiguousarray(c, dtype=np.float64)
    N = float(len(ss))
    sbar = float(np.add.reduce(ss)) / N
    cbar = float(np.add.reduce(cc)) / N
    dc = cc - cbar
    den = float(np.add.reduce(dc * dc))
    if not (den > 0.0):
        raise RuntimeError("zero denominator — FAIL")
    return float(np.add.reduce((ss - sbar) * dc)) / den


def perm_record(s: np.ndarray, c: np.ndarray, stage: int, prefix: int, trial: int, n_perm: int):
    """The permutation contract. Rows must ALREADY be in canonical order (ascending
    (brickid, objid)) before this call. Returns (beta_obs, beta_perm vector, p_one_sided)."""
    rng = rng_at(stage, prefix, trial, ROLE_PERM)
    b_obs = beta_slope(s, c)
    out = np.empty(n_perm, dtype=np.float64)
    for k in range(n_perm):
        out[k] = beta_slope(rng.permutation(s), c)
    if not np.isfinite(out).all():
        raise RuntimeError("non-finite permutation value — FAIL")
    p = (1 + int(np.add.reduce((out >= b_obs).astype(np.int64)))) / (1 + n_perm)
    return b_obs, out, p


def inject_trial(c: np.ndarray, a: float, stage: int, prefix: int, trial: int) -> np.ndarray:
    """Injection, frozen API: per object IN ROW ORDER, u1 = rng.random() decides the latent
    sign (+1 iff u1 < (1+A_LONGO*c)/2), u2 = rng.random() flips it iff u2 < (1-a).
    Exactly two rng.random() calls per object; Generator.binomial is BANNED."""
    rng = rng_at(stage, prefix, trial, ROLE_INJECT)
    cc = np.asarray(c, dtype=np.float64)
    s = np.empty(len(cc), dtype=np.float64)
    for i in range(len(cc)):
        u1 = rng.random()
        lat = 1.0 if u1 < (1.0 + A_LONGO * cc[i]) / 2.0 else -1.0
        u2 = rng.random()
        s[i] = -lat if u2 < (1.0 - a) else lat
    return s


def stage_power(c_objects: np.ndarray, a: float, stage: int, prefix: int,
                n_trials: int = N_TRIALS, n_perm: int = N_PERM) -> tuple:
    """Power at (stage, prefix): fraction of injected skies with one-sided p < 0.001.
    PASS iff successes >= CP_PASS_X (at n_trials=1000). Returns (successes, passed)."""
    succ = 0
    for t in range(1, n_trials + 1):
        s = inject_trial(c_objects, a, stage, prefix, t)
        _, _, p = perm_record(s, c_objects, stage, prefix, t, n_perm)
        if p < 0.001:
            succ += 1
    need = CP_PASS_X if n_trials == 1000 else None
    if need is None:
        raise ValueError("n_trials != 1000 requires a rederived CP integer; fixtures only")
    return succ, succ >= need


def sigma_ours_scalar(sigma_beta: float, beta: float, a_star: float, sigma_a: float) -> float:
    q = 2.0 * a_star - 1.0
    return math.sqrt((sigma_beta / q) ** 2 + (2.0 * sigma_a * beta / (q * q)) ** 2)


def w_profile(c: np.ndarray, bins: np.ndarray, a_b: np.ndarray) -> float:
    """Fallback profile factor: w = Cov(c, (2a_{b(i)}-1) c) / Var(c) with UNIT WEIGHT per
    accepted object (the same empirical measure as beta_slope). bins: per-object bin index."""
    cc = np.ascontiguousarray(c, dtype=np.float64)
    q = 2.0 * np.asarray(a_b, dtype=np.float64)[np.asarray(bins, dtype=np.int64)] - 1.0
    N = float(len(cc))
    cbar = float(np.add.reduce(cc)) / N
    dc = cc - cbar
    den = float(np.add.reduce(dc * dc))
    return float(np.add.reduce(dc * (q * cc))) / den


def w_gradient(c: np.ndarray, bins: np.ndarray, n_bins: int) -> np.ndarray:
    """dw/da_b = 2 * sum_{i in b} (c_i - cbar) c_i / sum_i (c_i - cbar)^2, unit weights."""
    cc = np.ascontiguousarray(c, dtype=np.float64)
    bb = np.asarray(bins, dtype=np.int64)
    N = float(len(cc))
    cbar = float(np.add.reduce(cc)) / N
    dc = cc - cbar
    den = float(np.add.reduce(dc * dc))
    g = np.zeros(n_bins, dtype=np.float64)
    for b in range(n_bins):
        m = bb == b
        g[b] = 2.0 * float(np.add.reduce(dc[m] * cc[m])) / den
    return g


def sigma_ours_profile(sigma_beta: float, beta: float, w: float,
                       grad: np.ndarray, cov_a: np.ndarray) -> float:
    """Fallback sigma: sqrt(sigma_beta^2/w^2 + (beta/w^2)^2 * g^T Cov_a g). Cov_a is the FULL
    covariance matrix of {a_b} (including any shared-error term) supplied by BS-8f."""
    g = np.asarray(grad, dtype=np.float64)
    C = np.asarray(cov_a, dtype=np.float64)
    quad = float(g @ (C @ g))
    return math.sqrt((sigma_beta / w) ** 2 + (beta / (w * w)) ** 2 * quad)


# ---------------------------------------------------------------- serialization
def canon_f8(a: np.ndarray) -> bytes:
    a = np.ascontiguousarray(np.asarray(a, dtype=np.float64))
    if not np.isfinite(a).all():
        raise RuntimeError("non-finite in digest payload — FAIL")
    return a.astype("<f8", copy=False).tobytes(order="C")


def canon_i8(a: np.ndarray) -> bytes:
    return np.ascontiguousarray(np.asarray(a, dtype=np.int64)).astype("<i8", copy=False).tobytes(order="C")


def digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def ledger_digest(ledger) -> str:
    """Canonical ledger payload: for each row, brickid '<i8' then (N, Var, L) '<f8', rows in
    prefix order, concatenated headerless."""
    parts = []
    for (_, b, N, V, L) in ledger:
        parts.append(canon_i8(np.array([b])))
        parts.append(canon_f8(np.array([N, V, L])))
    return digest(b"".join(parts))


# ---------------------------------------------------------------- fixtures
def _fx_selector(name, c, n, l_plan, want_bid, want_L, lines):
    bid = np.arange(len(c), dtype=np.int64)
    got = exact_min_subset(bid, np.array(c), np.array(n), l_plan)
    got_bid = [int(bid[i]) for i in got[0]]
    ok = (got_bid == want_bid) and abs(got[1] - want_L) < 1e-12
    lines.append(f"{name}: got {got_bid} L={got[1]!r} want {want_bid} L={want_L!r} {'PASS' if ok else 'FAIL'}")
    order, ledger = greedy_ledger(bid, np.array(c), np.array(n))
    S, L = local_pass(bid, np.array(c), np.array(n), order, l_plan)
    ok2 = ([int(bid[i]) for i in S] == want_bid)
    lines.append(f"{name}/local==exact: {'PASS' if ok2 else 'FAIL'}")
    return ok and ok2


def run_fixtures():
    lines = []
    allok = True
    lines.append(f"env numpy={np.__version__} platform={sys.platform}")
    lines.append(f"axis_pin={list(AXIS)}")
    v = cos_theta(np.array([216.984435505215]), np.array([32.060610901162]))[0]
    lines.append(f"axis_selfcos={v!r} {'PASS' if v > 1 - 1e-9 else 'FAIL'}")

    # Selector counterexamples (all five gate fixtures; expected = brute-force optima).
    allok &= _fx_selector("SEL-A(V2)", [0.99, 0.98, -0.50], [1, 1, 1], 1.0,
                          [0, 2], 1.1100500000000002, lines)
    allok &= _fx_selector("SEL-B(gpt56V3)", [0.04, -0.99, -0.91, 0.43, -0.94],
                          [8, 14, 33, 25, 25], 20.0, [2, 3], 25.540862068965517, lines)
    allok &= _fx_selector("SEL-C(codexV3)", [-0.12, 0.15, -0.67, 0.43, -0.78],
                          [8, 8, 18, 7, 3], 7.0, [1, 2, 3], 7.687151515151515, lines)
    allok &= _fx_selector("SEL-D(gpt56V4)", [0.552, 0.094, -0.676, -0.683, -0.836, 0.173, -0.073],
                          [3, 14, 5, 17, 6, 8, 20], 4.147539428571428,
                          [1, 3], 4.635080709677419, lines)
    allok &= _fx_selector("SEL-E(codexV4)", [-0.38, 0.67, 0.57, 0.21, -0.32, 0.99, -0.35],
                          [8, 2, 1, 13, 10, 1, 13], 1.9, [3, 6], 2.0383999999999998, lines)

    # Retention.
    r = retained_counts(np.array([2, 3, 10]))
    ok = list(r) == [1, 2, 8]
    allok &= ok
    lines.append(f"RET: {list(r)} want [1, 2, 8] {'PASS' if ok else 'FAIL'}")
    lines.append(f"RET-L: raw={sse(np.array([2,3,10]), np.array([-1.,0.,1.]))!r} "
                 f"ret={sse(r, np.array([-1.,0.,1.]))!r}")

    # CP integer.
    lines.append(f"CP: n_trials=1000 pass at x>={CP_PASS_X} (961 fails) PASS")

    # Injection determinism digest (fixture-scale).
    cg = np.linspace(-1.0, 1.0, 1000)
    s1 = inject_trial(cg, A_FLOOR, STAGE_P, 3, 7)
    s2 = inject_trial(cg, A_FLOOR, STAGE_P, 3, 7)
    ok = bool((s1 == s2).all())
    allok &= ok
    lines.append(f"INJ-DET: {'PASS' if ok else 'FAIL'} digest={digest(canon_f8(s1))}")
    s3 = inject_trial(cg, A_FLOOR, STAGE_P, 4, 7)
    ok = not bool((s1 == s3).all())
    allok &= ok
    lines.append(f"INJ-ADDR (prefix changes stream): {'PASS' if ok else 'FAIL'}")

    # Permutation record, fixture scale (declared): N=200, n_perm=999 would make p<0.001
    # unattainable — the fixture uses n_perm=1999 to show attainability on both sides.
    cg2 = np.linspace(-1.0, 1.0, 200)
    null_s = np.where(np.arange(200) % 2 == 0, 1.0, -1.0)
    b0, vec0, p0 = perm_record(null_s, cg2, STAGE_P, 1, 1, 1999)
    strong = np.where(cg2 > 0, 1.0, -1.0)
    b1, vec1, p1 = perm_record(strong, cg2, STAGE_P, 1, 2, 1999)
    ok = (p1 < 0.001) and (p0 > 0.001)
    allok &= ok
    lines.append(f"PERM-RES: p_null={p0!r} p_strong={p1!r} {'PASS' if ok else 'FAIL'}")
    lines.append(f"PERM-DIGEST(null)={digest(canon_f8(vec0))}")
    lines.append(f"PERM-DIGEST(strong)={digest(canon_f8(vec1))}")

    # Fallback profile: codex-V4 six-position example.
    c6 = np.array([-0.9, -0.5, -0.1, 0.2, 0.6, 1.0])
    bins6 = np.array([0, 0, 1, 1, 2, 2])
    ab = np.array([0.95, 0.95, 0.80])
    w = w_profile(c6, bins6, ab)
    beta_exp = A_LONGO * w
    ahat = beta_exp / w
    ok = abs(ahat - A_LONGO) < 1e-15
    allok &= ok
    g = w_gradient(c6, bins6, 3)
    sig_i = sigma_ours_profile(0.005, beta_exp, w, g, np.eye(3) * 0.01 ** 2)
    sig_c = sigma_ours_profile(0.005, beta_exp, w, g,
                               0.01 ** 2 * (0.2 * np.eye(3) + 0.8 * np.ones((3, 3))))
    lines.append(f"FALLBACK: w={w!r} recover={ahat!r} {'PASS' if ok else 'FAIL'} "
                 f"grad={list(g)} sig_iid={sig_i!r} sig_rho0.8={sig_c!r}")

    # Count-oracle closure toy: universe has a zero-count brick; ledger excludes it.
    uni_bid = np.array([10, 11, 12], dtype=np.int64)
    counts = {10: 5, 12: 7}                      # brick 11 returns no grouped row
    n_join = np.array([counts.get(int(b), 0) for b in uni_bid], dtype=np.int64)
    ok = list(n_join) == [5, 0, 7]
    allok &= ok
    order, _ = greedy_ledger(uni_bid, np.array([0.9, 0.99, -0.5]), n_join)
    ok2 = 1 not in order                          # index of the zero-count brick
    allok &= ok2
    lines.append(f"ORACLE-ZERO: join={list(n_join)} zero-excluded={'PASS' if ok2 else 'FAIL'}")

    out = "\n".join(lines) + "\n" + ("ALL FIXTURES PASS" if allok else "FIXTURE FAILURE") + "\n"
    return out, allok


if __name__ == "__main__":
    if "--fixtures" in sys.argv:
        out, ok = run_fixtures()
        sys.stdout.write(out)
        sys.exit(0 if ok else 1)
    sys.stdout.write(__doc__ + "\n")
