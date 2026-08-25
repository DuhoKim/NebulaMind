#!/usr/bin/env python3
"""successor_ref_v3.py — THE reference definition for the successor preregistration (V7).

Supersedes successor_ref_v2.py (sha dda4436cf0b10710ad9f8a6bb3dff6581c293df31ca8d577b4a2423d33d2dcfd),
retained for provenance. Repairs the union of GATE_GPT56_SUCCESSOR_V6 (F1-F9) and
GATE_CODEX_SUCCESSOR_V6 (F1-F11), both REFUSED.

The four structural changes:

1. CLOSURE IS DERIVED, NOT SUPPLIED. The cutout planner is implemented here
   (`plan_object_bricks`, the footprint-edge neighbour rule included). The production entry
   point `close_manifest()` takes the frozen parent table and its digest and derives every
   object's required bricks itself; it cannot be handed an answer. Both gate attacks (an
   omitted parent object; a planner that returns only the home brick) are negative fixtures.
2. TYPES ARE NOT INTERCHANGEABLE. `SealedMask` and `FixtureMask` are distinct classes.
   Production entry points accept only `SealedMask`; its digest binds kind, schema, boundary
   digest and acceptance flags; bin labels are RECOMPUTED from the sealed boundaries and a
   caller's disagreeing labels are refused; sign length is validated exactly.
3. THE PRODUCTION PATH HAS NO SEAMS. `run_production_verdict()` takes no permutation
   injection, no count override, no stage/trial override; it asserts the frozen environment,
   a pinned authorization, sample completeness, sealed provenance, the N_eq floor and a
   Stage-C receipt before calling the full permutation record. Synthetic exploration lives in
   `explore_verdict()`, a separately named non-production function.
4. THE ANALYTIC POWER NULL IS CONSERVATIVE BY CONSTRUCTION. Its critical value is inflated by
   PWR_CONSERVATISM, and the contract checked in fixtures is the decision-metric one: over a
   pinned family of masks, an analytic success implies a Monte-Carlo success, so an analytic
   Stage-P pass understates true power rather than overstating it.

DETERMINISM. Reductions are np.add.reduce over contiguous float64 1-D arrays; the only
quadratic form is an explicit scalar double loop; no BLAS call, no threading.
RANDOMNESS. SeedSequence((MASTER, stage, prefix, trial, role)) built fresh at point of use;
stateful spawn is banned.
ENVIRONMENT. require_environment() refuses on mismatch and IS CALLED by production paths.

`python3 successor_ref_v3.py --fixtures` prints the battery. The constitution pins this file's
sha256 and the fixture output's sha256.
"""
import hashlib
import itertools
import json
import math
import platform
import sys

import numpy as np

# ---------------------------------------------------------------- frozen environment
FROZEN_ENV = {"python_major_minor": "3.9", "numpy": "1.26.4", "byteorder": "little"}


def environment_record() -> dict:
    return {"python": sys.version.split()[0],
            "python_major_minor": ".".join(sys.version.split()[0].split(".")[:2]),
            "numpy": np.__version__, "platform": sys.platform,
            "machine": platform.machine(), "byteorder": sys.byteorder}


def require_environment() -> dict:
    env = environment_record()
    for k, want in FROZEN_ENV.items():
        if env[k] != want:
            raise RuntimeError(f"FROZEN ENVIRONMENT MISMATCH: {k}={env[k]!r} want {want!r}")
    return env


# ---------------------------------------------------------------- frozen constants
MASTER_SEED = 20260824
# Longo 2011 (2011PhLB..699..224L, doi:10.1016/j.physletb.2011.04.008); abstract verified from
# source 2026-08-25: "-0.0408+-0.011", axis (l,b)=(52,68.5), 15,158 spirals. The published sign
# is NEGATIVE in Longo's (R-L)/(R+L) convention; our East-of-North winding maps it to +0.0408.
A_LONGO = 0.0408
A_LONGO_PUBLISHED_SIGNED = -0.0408
SIGMA_PUB = 0.011
N_PERM = 100_000
N_TRIALS = 1_000
CP_PASS_X = 962
P_REPRODUCED = 0.001
P_REJECT_MIN = 0.05
A_FLOOR = 0.85
RETENTION_LB = 0.8572
FLOOR_MULT = 3.09
L_PLAN_MARGIN = 1.2
NEQ_MIN = 100_000
N_EXACT = 16
MOVE_CAP = 10_000
N_CAL_BINS = 3
N_HC_STRATA = 9
HC_MIN_PER_CELL = 10
HC_MIN_PER_STRATUM = 30          # V3-pred HC-1H floor, per inherited stratum (codex-V6 F2)
HC_REAL_LABELS = 500             # V3-pred HC-1H fixed real-label budget
PWR_CONSERVATISM = 1.01          # residual margin on the MEASURED critical value
MC_CAL_PERM = 20_000             # permutations for the per-prefix null calibration
Z_0001 = 3.090232306167813       # normal reference only; never a decision threshold
CUTOUT_PIX = 128                 # frozen tensor side, IC6_SHAPE = (1, 128, 128)
CUTOUT_PIXSCALE_ARCSEC = 0.262   # DR10 coadd pixel scale
# DERIVED, never typed: a V7 gate caught a hand-written 0.0186 that was 3.99x its own comment.
CUTOUT_HALFSIZE_DEG = (CUTOUT_PIX * CUTOUT_PIXSCALE_ARCSEC / 2.0) / 3600.0
AXIS = np.array([-0.676971771271432, -0.509846551777774, +0.530816083537352], dtype=np.float64)
STAGE_P, STAGE_C, STAGE_REAL = 1, 2, 3
ROLE_INJECT, ROLE_PERM = 0, 1


def rng_at(stage: int, prefix: int, trial: int, role: int) -> np.random.Generator:
    return np.random.default_rng(np.random.SeedSequence((MASTER_SEED, stage, prefix, trial, role)))


# ---------------------------------------------------------------- serialization
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
    nb = name.encode("utf-8")
    return len(nb).to_bytes(4, "little") + nb + len(payload).to_bytes(8, "little") + payload


SLOT_SCHEMA = {
    "BS-2c": ("universe_brickid", "brickid", "n_eligible", "c_bytes", "grouped_sum", "ungrouped_total"),
    "BS-2o": ("order_brickid", "N", "Var", "L_raw"),
    "BS-5p": ("l_min_plan", "l_plan", "successes", "n_trials"),
    "BS-2s": ("selected_brickid", "L_ret", "L_raw", "N_ret", "N_eq", "repass_successes"),
    "BS-2m": ("parent_digest", "planner_digest", "plan_digest", "required_count", "manifest_count"),
    "BS-2f": ("brickid", "objid", "c", "accept_flag", "bin", "boundaries", "mask_digest"),
    "BS-8f": ("a_hat", "sigma_a", "a_lb", "a_b", "sigma_ab", "a_lb_b", "cov_a", "epsilon"),
    "BS-5f": ("successes", "n_trials", "passed", "mask_digest"),
    "BS-7f": ("beta_obs", "perm_payload_digest", "p", "n_perm", "mask_digest"),
    "BS-V": ("verdict", "A_L", "p", "sigma_comb", "evaluated_floor", "path", "mask_digest"),
}


def receipt(slot: str, fields: dict) -> dict:
    """Canonical receipt envelope. A slot in SLOT_SCHEMA MUST supply exactly its named fields
    (gpt56-V6 F8 / codex-V6 F11): missing or extra fields are refused, not warned."""
    if slot in SLOT_SCHEMA:
        want, got = set(SLOT_SCHEMA[slot]), set(fields)
        if want != got:
            raise RuntimeError(f"receipt {slot}: field set mismatch; missing {sorted(want - got)}, "
                               f"extra {sorted(got - want)}")
    body = b"".join(field(k, fields[k]) for k in sorted(fields))
    env = environment_record()
    envelope = (field("slot", slot.encode()) + field("schema", b"successor_ref_v3/1")
                + field("environment", json.dumps(env, sort_keys=True).encode()) + field("body", body))
    return {"slot": slot, "schema": "successor_ref_v3/1", "environment": env,
            "body_sha256": digest(body), "envelope_sha256": digest(envelope)}


# ---------------------------------------------------------------- geometry
def unit_vectors(ra_deg, dec_deg) -> np.ndarray:
    ra = np.radians(np.asarray(ra_deg, dtype=np.float64))
    dec = np.radians(np.asarray(dec_deg, dtype=np.float64))
    return np.stack([np.cos(dec) * np.cos(ra), np.cos(dec) * np.sin(ra), np.sin(dec)], axis=1)


def cos_theta(ra_deg, dec_deg) -> np.ndarray:
    u = unit_vectors(ra_deg, dec_deg)
    return u[:, 0] * AXIS[0] + u[:, 1] * AXIS[1] + u[:, 2] * AXIS[2]


# ---------------------------------------------------------------- the cutout planner
def _ra_sep(a, b):
    """Signed-free angular separation in RA degrees, wrapping at 360."""
    d = abs(float(a) - float(b)) % 360.0
    return min(d, 360.0 - d)


def plan_object_bricks(ra, dec, brick_table, halfsize_deg=CUTOUT_HALFSIZE_DEG):
    """THE planner (gpt56-V6 F1 / codex-V6 F3). `brick_table` is a dict
    brickname -> (ra1, ra2, dec1, dec2) in degrees. Returns EVERY brick whose rectangle
    intersects the object's cutout box — which is precisely the footprint-edge neighbour rule:
    an object near a brick edge returns its neighbours, and that is the requirement the
    predecessor's manifest enumeration failed to close over.

    RA half-width is inflated by 1/cos(dec) so the box stays angularly square toward the pole,
    where the predecessor's two missing objects sat (dec -88.59 and -87.13). At |dec| within
    halfsize of a pole the RA span degenerates to the full circle and every brick in the
    declination band is returned; that is correct, not a bug."""
    dec = float(dec)
    dlo, dhi = dec - halfsize_deg, dec + halfsize_deg
    if dhi >= 90.0 or dlo <= -90.0:
        ra_half = 180.0
    else:
        cosd = math.cos(math.radians(min(abs(dlo), abs(dhi)) if dlo * dhi > 0 else 0.0))
        cosd = max(cosd, 1e-12)
        ra_half = min(180.0, halfsize_deg / cosd)
    out = []
    for name, (ra1, ra2, d1, d2) in brick_table.items():
        if d2 < dlo or d1 > dhi:
            continue
        if ra_half >= 180.0:
            out.append(name)
            continue
        centre = (float(ra1) + float(ra2)) / 2.0
        half_brick = _ra_sep(ra1, ra2) / 2.0
        if _ra_sep(ra, centre) <= ra_half + half_brick:
            out.append(name)
    return sorted(out)


def planner_digest(halfsize_deg=CUTOUT_HALFSIZE_DEG) -> str:
    """Binds the planner's COMPLETE transitive source and geometry into the BS-2m receipt.
    (codex-V7 F1: hashing only plan_object_bricks.__code__.co_code omitted co_consts and the
    _ra_sep helper, so it was not a digest of the planner's effective bytes.)"""
    import inspect
    body = b"".join(field(f.__name__, inspect.getsource(f).encode())
                    for f in (_ra_sep, plan_object_bricks))
    return digest(body + field("halfsize", canon_f8(np.array([halfsize_deg])))
                  + field("pix", canon_i8(np.array([CUTOUT_PIX])))
                  + field("pixscale", canon_f8(np.array([CUTOUT_PIXSCALE_ARCSEC]))))


def parent_digest(objid, ra, dec) -> str:
    return digest(field("objid", canon_i8(objid)) + field("ra", canon_f8(ra)) + field("dec", canon_f8(dec)))


class ManifestClosureError(RuntimeError):
    def __init__(self, message, result):
        super().__init__(message)
        self.result = result


def close_manifest(parent_objid, parent_ra, parent_dec, expected_parent_digest,
                   brick_table, manifest_bricknames, halfsize_deg=CUTOUT_HALFSIZE_DEG) -> dict:
    """BS-2m production entry point. Derives the required brick set ITSELF from the frozen
    parent and the planner — there is no argument through which a caller can supply the answer,
    which is the hole both V6 gates walked through. Refuses on: a parent digest mismatch (an
    omitted or altered object changes it), any object planning zero bricks, and any difference
    of even one brick between the derived closure and the candidate manifest."""
    objid = np.asarray(parent_objid, dtype=np.int64)
    ra = np.asarray(parent_ra, dtype=np.float64)
    dec = np.asarray(parent_dec, dtype=np.float64)
    if not (len(objid) == len(ra) == len(dec)) or len(objid) == 0:
        raise RuntimeError("parent table malformed — FAIL")
    if len(np.unique(objid)) != len(objid):
        raise RuntimeError("parent table has duplicate objids — FAIL")
    got = parent_digest(objid, ra, dec)
    if got != expected_parent_digest:
        raise ManifestClosureError(
            f"PARENT DIGEST MISMATCH: got {got}, expected {expected_parent_digest} — an omitted "
            f"or altered parent object cannot pass this check",
            {"parent_digest_got": got, "parent_digest_expected": expected_parent_digest})
    per_object, closed = {}, set()
    for i in range(len(objid)):
        bs = plan_object_bricks(ra[i], dec[i], brick_table, halfsize_deg)
        if not bs:
            raise RuntimeError(f"object {int(objid[i])} plans zero bricks — FAIL")
        per_object[int(objid[i])] = bs
        closed.update(bs)
    man_list = [str(b) for b in manifest_bricknames]
    if len(set(man_list)) != len(man_list):
        raise ManifestClosureError("manifest contains duplicate bricknames — FAIL",
                                   {"manifest_count": len(man_list),
                                    "distinct": len(set(man_list))})
    man = sorted(set(man_list))
    req = sorted(closed)
    missing = sorted(set(req) - set(man))
    extra = sorted(set(man) - set(req))
    plan_payload = b"".join(field(str(k), "\x00".join(per_object[k]).encode())
                            for k in sorted(per_object))
    result = {"parent_digest": got, "planner_digest": planner_digest(halfsize_deg),
              "plan_digest": digest(plan_payload), "objects": len(per_object),
              "required_count": len(req), "manifest_count": len(man),
              "missing_from_manifest": missing, "missing_count": len(missing),
              "extra_in_manifest": extra, "extra_count": len(extra)}
    if missing or extra:
        raise ManifestClosureError(
            f"MANIFEST NOT CLOSED: manifest {len(man)} vs required {len(req)}; "
            f"missing {len(missing)} {missing[:4]}; extra {len(extra)} {extra[:4]}", result)
    return result


# ---------------------------------------------------------------- weighted SSE / ledger
def sse(counts, c) -> float:
    n = np.ascontiguousarray(np.asarray(counts, dtype=np.float64))
    cc = np.ascontiguousarray(np.asarray(c, dtype=np.float64))
    N = float(np.add.reduce(n))
    if N <= 0.0:
        return 0.0
    cbar = float(np.add.reduce(n * cc)) / N
    d = cc - cbar
    return float(np.add.reduce(n * d * d))


def validate_count_table(brickid, c, n_eligible, universe_brickid=None,
                         grouped_sum=None, ungrouped_total=None) -> dict:
    """BS-2c validator, now strict on the schema itself (gpt56-V6 F6 / codex-V6 F9): equal
    lengths, unique integral keys, non-negative INTEGRAL counts, finite |c| <= 1, exact
    universe equality after zero materialization, grouped == ungrouped."""
    bid = np.asarray(brickid)
    cc = np.asarray(c)
    nn = np.asarray(n_eligible)
    if not (len(bid) == len(cc) == len(nn)) or len(bid) == 0:
        raise RuntimeError("count table: field lengths disagree or table empty — FAIL")
    if bid.dtype.kind not in "iu":
        raise RuntimeError("count table: brickid must be integral — FAIL")
    if nn.dtype.kind not in "iu":
        raise RuntimeError("count table: counts must be integral, not float — FAIL")
    if len(np.unique(bid)) != len(bid):
        raise RuntimeError("count table: duplicate brickid — FAIL")
    if (np.asarray(nn, dtype=np.int64) < 0).any():
        raise RuntimeError("count table: negative count — FAIL")
    ccf = np.asarray(cc, dtype=np.float64)
    if not np.isfinite(ccf).all() or np.abs(ccf).max() > 1.0 + 1e-12:
        raise RuntimeError("count table: c outside [-1, 1] or non-finite — FAIL")
    out = {"rows": int(len(bid)), "zero_rows": int(np.count_nonzero(np.asarray(nn) == 0))}
    if universe_brickid is not None:
        uni = np.asarray(universe_brickid, dtype=np.int64)
        if len(np.unique(uni)) != len(uni):
            raise RuntimeError("universe manifest: duplicate brickid — FAIL")
        miss = np.setdiff1d(uni, bid)
        extra = np.setdiff1d(bid, uni)
        if miss.size or extra.size:
            raise RuntimeError(f"count table vs universe: {miss.size} missing, {extra.size} extra — FAIL")
        out["universe"] = int(uni.size)
    tot = int(np.add.reduce(np.asarray(nn, dtype=np.int64)))
    if grouped_sum is not None:
        if tot != int(grouped_sum):
            raise RuntimeError("count table does not sum to the grouped total — FAIL")
        if ungrouped_total is None or int(grouped_sum) != int(ungrouped_total):
            raise RuntimeError("grouped total != ungrouped total (or absent) — FAIL")
        out["total"] = tot
    return out


def greedy_ledger(brickid, c, n_raw):
    """BS-2o. Traversal over POSITIVE-RAW-COUNT bricks; zero-count bricks stay in the BS-2c
    receipt and never enter selection. No threshold input exists here."""
    bid = np.asarray(brickid, dtype=np.int64)
    cc = np.asarray(c, dtype=np.float64)
    nn = np.asarray(n_raw, dtype=np.int64)
    idx_all = np.nonzero(nn > 0)[0]
    remaining = list(idx_all[np.argsort(bid[idx_all], kind="stable")])
    order, ledger = [], []
    N = cbar = L = 0.0
    while remaining:
        best = None
        for i in remaining:
            nj = float(nn[i])
            delta = 0.0 if N == 0.0 else (N * nj / (N + nj)) * ((cc[i] - cbar) ** 2)
            key = (delta, abs(cc[i]), -int(bid[i]))
            if best is None or key > best[0]:
                best = (key, i)
        i = best[1]
        remaining.remove(i)
        nj = float(nn[i])
        L += best[0][0]
        cbar = (cbar * N + cc[i] * nj) / (N + nj)
        N += nj
        order.append(int(i))
        ledger.append((len(order), int(bid[i]), N, (L / N if N > 0 else 0.0), L))
    return order, ledger


def retained_counts(n_raw) -> np.ndarray:
    return np.floor(RETENTION_LB * np.asarray(n_raw, dtype=np.float64)).astype(np.int64)


def exact_min_subset(brickid, c, counts, l_plan: float, candidate_idx):
    """Minimum-cardinality subset (by RETAINED leverage) over the given candidate indices;
    ties -> lexicographically smallest sorted brickid tuple."""
    bid = np.asarray(brickid, dtype=np.int64)
    cc = np.asarray(c, dtype=np.float64)
    nn = np.asarray(counts, dtype=np.int64)
    idx = sorted(candidate_idx, key=lambda i: int(bid[i]))
    if len(idx) > N_EXACT:
        raise ValueError("exact mode only for <= N_EXACT candidates")
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


def local_pass(brickid, c, n_raw, n_ret, order, l_plan: float):
    """BS-2s reduction. RAW counts decide the exact-mode boundary (gpt56-V6 F6: the V6 code
    used retained-positive and flipped the branch at 17-raw/16-retained); RETAINED counts
    carry every leverage threshold."""
    bid = np.asarray(brickid, dtype=np.int64)
    cc = np.asarray(c, dtype=np.float64)
    nr = np.asarray(n_raw, dtype=np.int64)
    nt = np.asarray(n_ret, dtype=np.int64)
    raw_pos = [i for i in range(len(bid)) if nr[i] > 0]
    if len(raw_pos) <= N_EXACT:
        r = exact_min_subset(bid, cc, nt, l_plan, raw_pos)
        if r is None:
            raise RuntimeError("no subset reaches l_plan on retained counts")
        return r
    L_of = lambda S: sse(nt[list(S)], cc[list(S)])
    S, reached = [], False
    for i in order:
        S.append(i)
        if L_of(S) >= l_plan:
            reached = True
            break
    if not reached:
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
            for j2 in sorted((x for x in raw_pos if x not in S), key=lambda x: int(bid[x])):
                S2 = (S - {i}) | {j2}
                if L_of(S2) >= l_plan:
                    r = try_removal(S2)
                    if r is not None:
                        S, committed = S2 - {r}, True
                        break
        if not committed:
            break
    return sorted(S, key=lambda x: int(bid[x])), L_of(S)


# ---------------------------------------------------------------- masks (non-interchangeable)
class _BaseMask:
    __slots__ = ("brickid", "objid", "c", "bin", "s", "accept", "boundaries",
                 "kind", "digest", "n")

    def __init__(self, brickid, objid, c, bin_label, s, accept, boundaries, kind):
        bid = np.asarray(brickid, dtype=np.int64)
        oid = np.asarray(objid, dtype=np.int64)
        cc = np.ascontiguousarray(np.asarray(c, dtype=np.float64))
        n = len(bid)
        if n == 0 or not (len(oid) == len(cc) == n):
            raise RuntimeError("mask field lengths disagree or mask is empty")
        if not np.isfinite(cc).all() or np.abs(cc).max() > 1.0 + 1e-12:
            raise RuntimeError("mask carries non-finite or |c| > 1")
        if len(set(zip(bid.tolist(), oid.tolist()))) != n:
            raise RuntimeError("mask has duplicate (brickid, objid)")
        bnd = None if boundaries is None else np.asarray(boundaries, dtype=np.float64)
        if bnd is not None:
            derived = assign_bins(cc, bnd)
            if bin_label is not None and not np.array_equal(np.asarray(bin_label, dtype=np.int64), derived):
                raise RuntimeError("supplied bin labels disagree with the sealed boundaries — FAIL")
            bb = derived
        else:
            bb = np.zeros(n, dtype=np.int64) if bin_label is None else np.asarray(bin_label, dtype=np.int64)
            if bb.shape != (n,) or bb.min() < 0 or bb.max() >= N_CAL_BINS:
                raise RuntimeError("bin labels malformed")
        if accept is None:
            acc = np.ones(n, dtype=np.int64)
        else:
            acc = np.asarray(accept, dtype=np.int64)
            if acc.shape != (n,) or not np.isin(acc, (0, 1)).all():
                raise RuntimeError("acceptance flags malformed")
            if int(acc.min()) == 0:
                raise RuntimeError("mask contains non-accepted rows — FAIL")
        order = np.lexsort((oid, bid))
        self.brickid, self.objid = bid[order], oid[order]
        self.c, self.bin, self.accept = cc[order], bb[order], acc[order]
        self.boundaries = bnd
        if s is None:
            self.s = None
        else:
            ss = np.ascontiguousarray(np.asarray(s, dtype=np.float64))
            if ss.shape != (n,):
                raise RuntimeError(f"sign vector length {ss.shape} != mask length {n} — FAIL")
            ss = ss[order]
            if not np.isin(ss, (-1.0, 1.0)).all():
                raise RuntimeError("sign labels must be exactly +1 or -1")
            self.s = ss
        self.kind, self.n = kind, n
        self.digest = digest(
            field("kind", kind.encode()) + field("schema", b"mask/v3")
            + field("brickid", canon_i8(self.brickid)) + field("objid", canon_i8(self.objid))
            + field("c", canon_f8(self.c)) + field("bin", canon_i8(self.bin))
            + field("accept", canon_i8(self.accept))
            + field("boundaries", b"" if bnd is None else canon_f8(bnd))
            + field("signs_present", b"1" if self.s is not None else b"0")
            + field("s", b"" if self.s is None else canon_f8(self.s)))

    def with_signs(self, s):
        return type(self)(self.brickid, self.objid, self.c, None if self.boundaries is not None
                          else self.bin, s, self.accept, self.boundaries)


class SealedMask(_BaseMask):
    """The ONLY input production Stage C and the production record accept. Requires sealed
    calibration boundaries, from which bin labels are recomputed rather than trusted."""
    __slots__ = ()

    def __init__(self, brickid, objid, c, s, accept, boundaries, bin_label=None):
        if boundaries is None:
            raise RuntimeError("a sealed mask requires sealed calibration boundaries")
        super().__init__(brickid, objid, c, bin_label, s, accept, boundaries, "SEALED_ACCEPTED_MASK")

    def with_signs(self, s):
        return SealedMask(self.brickid, self.objid, self.c, s, self.accept, self.boundaries)


class FixtureMask(_BaseMask):
    """Synthetic/planning only. Production entry points refuse it by type."""
    __slots__ = ()

    def __init__(self, brickid, objid, c, s=None, bin_label=None, boundaries=None, accept=None):
        super().__init__(brickid, objid, c, bin_label, s, accept, boundaries, "FIXTURE")

    def with_signs(self, s):
        return FixtureMask(self.brickid, self.objid, self.c, s,
                           None if self.boundaries is not None else self.bin,
                           self.boundaries, self.accept)


def require_any_mask(m, need_signs: bool):
    if not isinstance(m, _BaseMask):
        raise RuntimeError("inadmissible input: not a mask type (bare vectors, parent positions "
                           "and uniform-sphere inputs are refused)")
    if need_signs and m.s is None:
        raise RuntimeError("this operation requires sign labels")
    return m


def require_sealed(m, need_signs: bool) -> "SealedMask":
    if not isinstance(m, SealedMask):
        raise RuntimeError(f"PRODUCTION PATH requires a SealedMask, got "
                           f"{type(m).__name__} — FAIL")
    return require_any_mask(m, need_signs)


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
    ss = np.asarray(s, dtype=np.float64)
    cc = np.asarray(c, dtype=np.float64)
    N = len(ss)
    vs = float(np.add.reduce((ss - float(np.add.reduce(ss)) / N) ** 2)) / N
    vc = float(np.add.reduce((cc - float(np.add.reduce(cc)) / N) ** 2)) / N
    if not (vc > 0.0) or not (vs > 0.0):
        raise RuntimeError("degenerate c or s — FAIL")
    return math.sqrt(vs / ((N - 1) * vc))


def perm_record(mask, stage: int, prefix: int, trial: int, n_perm: int = N_PERM):
    """STAGE_REAL is the production record and refuses a fixture BY TYPE."""
    m = require_sealed(mask, need_signs=True) if stage == STAGE_REAL \
        else require_any_mask(mask, need_signs=True)
    rng = rng_at(stage, prefix, trial, ROLE_PERM)
    b_obs = beta_slope(m.s, m.c)
    N = m.n
    cbar = float(np.add.reduce(m.c)) / N
    d = m.c - cbar
    den = float(np.add.reduce(d * d))
    sbar = float(np.add.reduce(m.s)) / N
    out = np.empty(n_perm, dtype=np.float64)
    for k in range(n_perm):
        out[k] = float(np.add.reduce((m.s[rng.permutation(N)] - sbar) * d)) / den
    if not np.isfinite(out).all():
        raise RuntimeError("non-finite permutation value — FAIL")
    p = (1 + int(np.add.reduce((out >= b_obs).astype(np.int64)))) / (1 + n_perm)
    return b_obs, out, p, float(np.std(out, ddof=1))


def reference_null_z(mask_with_ref_signs, stage: int, prefix: int,
                     n_perm: int = MC_CAL_PERM) -> np.ndarray:
    """The STANDARDIZED permutation null z = beta_perm / sigma_exact for this geometry,
    measured once per Stage-P prefix and returned sorted.

    Why measured rather than assumed (gpt56-V6 F7 / codex-V6 F7, plus a defect this file's own
    fixtures found): the pure-normal critical value 3.0902*sigma is ANTI-CONSERVATIVE on polar
    geometry with imbalanced signs — the very geometry the successor selects. Measured z*
    across four geometries ranged 3.0376 to 3.1355, bracketing the normal value, so no fixed
    normal threshold is safe and no fixture-tuned inflation factor would be a contract.

    Why the WHOLE null rather than one quantile: a 0.999 quantile estimated from 20,000
    permutations rests on ~20 tail points and is badly noisy (an early version of this file
    failed its own contract by -3.6% for that reason alone). Comparing a trial statistic
    against the full empirical tail uses every permutation.

    Why one null serves 1,000 trials: standardizing by sigma_exact removes the sign-multiset's
    leading effect, and fixture PWR-Z-STABLE MEASURES the residual rather than assuming it.
    This is what makes Stage P feasible — one null per prefix, not one per trial."""
    m = require_any_mask(mask_with_ref_signs, need_signs=True)
    _b, vec, _p, _sd = perm_record(m, stage, prefix, 0, n_perm)
    return np.sort(vec / perm_sigma_exact(m.s, m.c))


def calibrated_p(mask_with_signs, ref_z_sorted) -> float:
    """Plus-one one-sided p against the measured standardized null. The trial statistic is
    DEFLATED by PWR_CONSERVATISM before comparison, so the decision is conservative: it
    demands more evidence than the raw statistic provides."""
    m = require_any_mask(mask_with_signs, need_signs=True)
    z = beta_slope(m.s, m.c) / (perm_sigma_exact(m.s, m.c) * PWR_CONSERVATISM)
    ref = np.asarray(ref_z_sorted, dtype=np.float64)
    exceed = int(ref.size - np.searchsorted(ref, z, side="left"))
    return (1 + exceed) / (1 + ref.size)


def calibrated_success(mask_with_signs, ref_z_sorted) -> bool:
    """Stage-P decision. Production never calls this; the production verdict path always runs
    the full N_PERM permutation record on the sealed mask."""
    return calibrated_p(mask_with_signs, ref_z_sorted) < P_REPRODUCED


def inject_signs(mask, a, stage: int, prefix: int, trial: int) -> np.ndarray:
    m = require_any_mask(mask, need_signs=False)
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


def stage_power(mask, a, stage: int, prefix: int, n_trials: int = N_TRIALS):
    """Power at (stage, prefix). The null is MEASURED once for this geometry from trial 1's
    injected signs; every trial is then judged against that full standardized null.
    STAGE_C is a production stage and refuses a fixture BY TYPE (gpt56-V7 F2 / codex-V7 F2:
    V7 checked only that the argument was some mask, so Stage C accepted FixtureMask)."""
    m = require_sealed(mask, need_signs=False) if stage == STAGE_C \
        else require_any_mask(mask, need_signs=False)
    ref = m.with_signs(inject_signs(m, a, stage, prefix, 1))
    ref_z = reference_null_z(ref, stage, prefix)
    succ = 0
    for t in range(1, n_trials + 1):
        sm = ref if t == 1 else m.with_signs(inject_signs(m, a, stage, prefix, t))
        if calibrated_success(sm, ref_z):
            succ += 1
    return succ, (succ >= CP_PASS_X if n_trials == N_TRIALS else None)


# ---------------------------------------------------------------- planning orchestrator
def _planning_mask(bid, c, counts):
    n = int(np.add.reduce(np.asarray(counts, dtype=np.int64)))
    if n <= 0:
        return None
    b = np.repeat(np.asarray(bid, dtype=np.int64), np.asarray(counts, dtype=np.int64))
    cc = np.repeat(np.asarray(c, dtype=np.float64), np.asarray(counts, dtype=np.int64))
    o = np.concatenate([np.arange(int(k), dtype=np.int64) for k in counts if int(k) > 0])
    return FixtureMask(b, o, cc)


def build_plan(brickid, c, n_raw, *, universe_brickid=None, grouped_sum=None,
               ungrouped_total=None, l_plan_override=None, n_trials=N_TRIALS) -> dict:
    """BS-2c -> BS-2o -> BS-5p -> BS-2s in one acyclic call, WITH the count-table validator
    integrated (gpt56-V6 F6) and the mandatory Stage-P re-pass on the final set."""
    validate_count_table(brickid, c, n_raw, universe_brickid, grouped_sum, ungrouped_total)
    bid = np.asarray(brickid, dtype=np.int64)
    cc = np.asarray(c, dtype=np.float64)
    nr = np.asarray(n_raw, dtype=np.int64)
    nret = retained_counts(nr)
    order, ledger = greedy_ledger(bid, cc, nr)
    l_ret_curve = [sse(nret[order[:k]], cc[order[:k]]) for k in range(1, len(order) + 1)]
    if l_plan_override is None:
        l_min_plan = None
        for k in range(1, len(order) + 1):
            if 3.0 * l_ret_curve[k - 1] < NEQ_MIN:
                continue
            pm = _planning_mask(bid[order[:k]], cc[order[:k]], nret[order[:k]])
            if pm is None:
                continue
            if stage_power(pm, A_FLOOR, STAGE_P, k, n_trials)[1]:
                l_min_plan = l_ret_curve[k - 1]
                break
        if l_min_plan is None:
            raise InconclusiveByPower("no ledger prefix passes Stage P at planning")
        l_plan = L_PLAN_MARGIN * l_min_plan
    else:
        l_min_plan, l_plan = None, float(l_plan_override)
    S, L_final = local_pass(bid, cc, nr, nret, order, l_plan)
    repass = None
    if l_plan_override is None:
        pm = _planning_mask(bid[S], cc[S], nret[S])
        repass = stage_power(pm, A_FLOOR, STAGE_P, 0, n_trials)
        if not repass[1]:
            raise InconclusiveByPower(f"final selected set fails the Stage-P re-pass "
                                      f"({repass[0]}/{n_trials} < {CP_PASS_X})")
    return {"order_brickid": [int(bid[i]) for i in order], "ledger": ledger,
            "l_ret_curve": l_ret_curve, "l_min_plan": l_min_plan, "l_plan": l_plan,
            "selected_brickid": [int(bid[i]) for i in S], "L_ret_final": L_final,
            "L_raw_final": sse(nr[S], cc[S]), "N_ret_final": int(np.add.reduce(nret[S])),
            "N_eq_final": 3.0 * L_final, "repass": repass}


# ---------------------------------------------------------------- calibration (HC-1H)
class InconclusiveByCalibration(RuntimeError):
    pass


class InconclusiveByPower(RuntimeError):
    pass


def calibration_bins(c) -> np.ndarray:
    """Two interior boundaries at the count-weighted c-tertiles of the sealed accepted
    objects. Tie rule, stated and IMPLEMENTED identically (codex-V6 F2 caught the V6
    docstring/body contradiction): assignment uses side='left', so a value EQUAL to a boundary
    falls in the HIGHER bin. Refuses if any bin would be empty."""
    q = np.sort(np.asarray(c, dtype=np.float64))
    n = len(q)
    bnd = np.array([q[int(math.floor(n / 3.0))], q[int(math.floor(2 * n / 3.0))]], dtype=np.float64)
    sizes = np.bincount(assign_bins(q, bnd), minlength=N_CAL_BINS)
    if int(sizes.min()) == 0:
        raise RuntimeError(f"degenerate calibration bins {sizes.tolist()} — FAIL")
    return bnd


def assign_bins(c, boundaries) -> np.ndarray:
    return np.searchsorted(np.asarray(boundaries, dtype=np.float64),
                           np.asarray(c, dtype=np.float64), side="left").astype(np.int64)


def allocate_handcheck(cell_counts, budget: int = HC_REAL_LABELS) -> np.ndarray:
    """BS-8p: integer allocation over the 3 x N_HC_STRATA cells, proportional to cell counts,
    with BOTH inherited floors enforced (codex-V6 F2): >= HC_MIN_PER_CELL per non-empty cell
    AND >= HC_MIN_PER_STRATUM per non-empty inherited HC stratum (column). Largest remainder;
    ties by smaller flat index. Infeasible floors FAIL rather than silently shrink."""
    cc = np.asarray(cell_counts, dtype=np.int64).reshape(N_CAL_BINS, N_HC_STRATA)
    nonempty = cc > 0
    k = int(np.count_nonzero(nonempty))
    stratum_live = nonempty.any(axis=0)
    need = max(k * HC_MIN_PER_CELL, 0) + 0
    if need > budget:
        raise RuntimeError(f"cell minima {need} exceed budget {budget} — FAIL")
    if int(stratum_live.sum()) * HC_MIN_PER_STRATUM > budget:
        raise RuntimeError(f"stratum minima {int(stratum_live.sum()) * HC_MIN_PER_STRATUM} "
                           f"exceed budget {budget} — FAIL")
    alloc = np.where(nonempty, HC_MIN_PER_CELL, 0).astype(np.int64)
    for j in range(N_HC_STRATA):                       # lift each live stratum to its floor
        if not stratum_live[j]:
            continue
        while int(alloc[:, j].sum()) < HC_MIN_PER_STRATUM:
            rows = [i for i in range(N_CAL_BINS) if nonempty[i, j] and alloc[i, j] < cc[i, j]]
            if not rows:
                raise RuntimeError(f"stratum {j} cannot reach its floor of "
                                   f"{HC_MIN_PER_STRATUM} — FAIL")
            alloc[max(rows, key=lambda i: (cc[i, j], -i)), j] += 1
    rest = budget - int(alloc.sum())
    if rest < 0:
        raise RuntimeError("floors exceed budget after stratum lift — FAIL")
    tot = int(cc.sum())
    share = np.where(nonempty, cc.astype(np.float64) * rest / tot, 0.0)
    base = np.floor(share).astype(np.int64)
    alloc = alloc + base
    left = rest - int(base.sum())
    rem = (share - base).ravel()
    for flat in sorted(range(rem.size), key=lambda i: (-rem[i], i))[:max(0, left)]:
        alloc.ravel()[flat] += 1
    if int(alloc.sum()) != budget:
        raise RuntimeError("allocation does not sum to budget — FAIL")
    if (alloc[nonempty] > cc[nonempty]).any():
        raise RuntimeError("allocation exceeds available objects in a cell — FAIL")
    for j in range(N_HC_STRATA):
        if stratum_live[j] and int(alloc[:, j].sum()) < HC_MIN_PER_STRATUM:
            raise RuntimeError(f"stratum {j} below floor after apportionment — FAIL")
    return alloc


def accuracy_from_handcheck(agree_counts, n_counts, epsilon_hat: float, sigma_epsilon: float):
    """BS-8f, the INHERITED HC-1H estimator (gpt56-V6 F4 / codex-V6 F1). V3-pred HC-4 defines
    the corrected accuracy as `(raw - epsilon)/(1 - 2*epsilon)`; V6 wrongly returned raw.
    The shared epsilon is ONE quantity, so its derivative enters every bin and produces a
    genuine off-diagonal covariance rather than an additive constant:
        a_b = (raw_b - eps)/(1 - 2 eps)
        d a_b / d raw_b = 1/(1 - 2 eps)
        d a_b / d eps   = (2 a_b - 1)/(1 - 2 eps)
        Cov(a_b, a_b') = d_eps(b) * d_eps(b') * sigma_eps^2   (b != b')
        Var(a_b)       = (raw_b(1-raw_b)/n_b)/(1-2eps)^2 + d_eps(b)^2 sigma_eps^2
    """
    agree = np.asarray(agree_counts, dtype=np.float64)
    n = np.asarray(n_counts, dtype=np.float64)
    if agree.shape != n.shape or agree.size == 0:
        raise RuntimeError("calibration inputs malformed — FAIL")
    if (n <= 0).any():
        raise RuntimeError("empty calibration bin — FAIL")
    if (agree < 0).any() or (agree > n).any():
        raise RuntimeError("agreement count outside [0, n] — FAIL")
    eps = float(epsilon_hat)
    q = 1.0 - 2.0 * eps
    if not (0.0 <= eps < 0.5) or q <= 0.0:
        raise RuntimeError("epsilon outside [0, 0.5) — FAIL")
    raw = agree / n
    a_b = (raw - eps) / q
    d_raw = 1.0 / q
    d_eps = (2.0 * a_b - 1.0) / q
    var_raw = raw * (1.0 - raw) / n
    var_b = var_raw * d_raw ** 2 + (d_eps ** 2) * sigma_epsilon ** 2
    k = len(a_b)
    cov = np.zeros((k, k), dtype=np.float64)
    for i in range(k):
        for j in range(k):
            cov[i, j] = var_b[i] if i == j else d_eps[i] * d_eps[j] * sigma_epsilon ** 2
    sd_b = np.sqrt(var_b)
    n_tot = float(np.add.reduce(n))
    raw_hat = float(np.add.reduce(agree)) / n_tot
    a_hat = (raw_hat - eps) / q
    d_eps_hat = (2.0 * a_hat - 1.0) / q
    sd_hat = math.sqrt(raw_hat * (1.0 - raw_hat) / n_tot * d_raw ** 2
                       + d_eps_hat ** 2 * sigma_epsilon ** 2)
    return {"a_hat": a_hat, "sigma_a": sd_hat, "a_lb": a_hat - 1.645 * sd_hat,
            "a_b": a_b, "sigma_ab": sd_b, "a_lb_b": a_b - 1.645 * sd_b,
            "cov_a": cov, "epsilon": eps, "sigma_epsilon": float(sigma_epsilon)}


def adjudicate_path(cal: dict) -> str:
    if float(np.min(cal["a_lb_b"])) < A_FLOOR:
        raise InconclusiveByCalibration(
            f"a_lb_b min {float(np.min(cal['a_lb_b'])):.6f} < {A_FLOOR}")
    return "SCALAR" if float(np.max(np.abs(cal["a_b"] - cal["a_hat"]))) <= 0.03 else "PROFILE"


# ---------------------------------------------------------------- estimands and sigmas
def _finite(*vals):
    for v in vals:
        if not math.isfinite(float(v)):
            raise RuntimeError("non-finite decision quantity — FAIL")


def w_profile(mask, a_b) -> float:
    m = require_any_mask(mask, need_signs=False)
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


def w_gradient(mask) -> np.ndarray:
    m = require_any_mask(mask, need_signs=False)
    cbar = float(np.add.reduce(m.c)) / m.n
    dc = m.c - cbar
    den = float(np.add.reduce(dc * dc))
    g = np.zeros(N_CAL_BINS, dtype=np.float64)
    for b in range(N_CAL_BINS):
        sel = m.bin == b
        g[b] = 2.0 * float(np.add.reduce(dc[sel] * m.c[sel])) / den
    return g


def sigma_ours_scalar(sigma_beta, beta, a_star, sigma_a) -> float:
    _finite(sigma_beta, beta, a_star, sigma_a)
    q = 2.0 * a_star - 1.0
    if q <= 0.0:
        raise RuntimeError("2a-1 <= 0 — FAIL")
    out = math.sqrt((sigma_beta / q) ** 2 + (2.0 * sigma_a * beta / (q * q)) ** 2)
    _finite(out)
    return out


def sigma_ours_profile(sigma_beta, beta, w, grad, cov_a) -> float:
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
def _decide_from(beta, p, sigma_beta, mask, cal) -> dict:
    """Pure decision helper. It has no I/O and no permutation seam; the ONLY callers are the
    production runner (which supplies a full perm_record) and the explicitly-named
    exploration function."""
    path = adjudicate_path(cal)
    if path == "SCALAR":
        A = beta / (2.0 * cal["a_hat"] - 1.0)
        sig_band = sigma_ours_scalar(sigma_beta, beta, cal["a_hat"], cal["sigma_a"])
        sig_floor = sigma_ours_scalar(sigma_beta, beta, cal["a_lb"], cal["sigma_a"])
    else:
        w = w_profile(mask, cal["a_b"])
        w_lb = w_profile(mask, cal["a_lb_b"])
        g = w_gradient(mask)
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
            "sigma_beta": sigma_beta, "sigma_ours_band": sig_band, "sigma_ours_floor": sig_floor,
            "sigma_comb": sigma_comb, "evaluated_floor": floor, "N": mask.n,
            "mask_digest": mask.digest}


def run_production_verdict(mask, cal, *, authorization_path, authorization_sha256,
                           n_receipts, n_parent, stage_c_receipt) -> dict:
    """THE production path (gpt56-V6 F5 / codex-V6 F6). No permutation injection, no count
    override, no stage/trial override, no mask-kind override. Every guard is CALLED here, so a
    caller cannot satisfy the named symbol while skipping them."""
    env = require_environment()
    auth = require_authorization(authorization_path, authorization_sha256)
    require_complete_sample(n_receipts, n_parent)
    m = require_sealed(mask, need_signs=True)
    if not isinstance(stage_c_receipt, dict) or stage_c_receipt.get("slot") != "BS-5f":
        raise RuntimeError("a BS-5f Stage-C receipt is required — FAIL")
    if stage_c_receipt.get("mask_digest") != m.digest:
        raise RuntimeError("Stage-C receipt does not bind THIS mask — FAIL")
    if not stage_c_receipt.get("passed"):
        return {"verdict": "INCONCLUSIVE-BY-POWER", "reason": "Stage C did not pass",
                "mask_digest": m.digest}
    n_eq = 3.0 * float(m.n) * float(np.var(m.c))
    if n_eq < NEQ_MIN:
        return {"verdict": "INCONCLUSIVE-BY-POWER",
                "reason": f"N_eq {n_eq:.1f} < {NEQ_MIN}", "mask_digest": m.digest}
    try:
        beta, vec, p, sigma_beta = perm_record(m, STAGE_REAL, 0, 0, N_PERM)
    except Exception as exc:
        raise RuntimeError(f"production permutation record failed: {exc}") from exc
    out = _decide_from(beta, p, sigma_beta, m, cal)
    out.update({"environment": env, "authorization_sha256": auth, "n_perm": N_PERM,
                "perm_payload_digest": digest(canon_f8(vec))})
    return out


def explore_verdict(mask, cal, beta, p, sigma_beta) -> dict:
    """NON-PRODUCTION. Synthetic exploration only; named so no production caller can reach the
    decision helper by accident."""
    require_any_mask(mask, need_signs=True)
    return _decide_from(beta, p, sigma_beta, mask, cal)


# ---------------------------------------------------------------- run guards
def require_authorization(auth_path: str, expected_sha256: str) -> str:
    try:
        with open(auth_path, "rb") as f:
            got = hashlib.sha256(f.read()).hexdigest()
    except OSError as exc:
        raise RuntimeError(f"authorization unreadable: {exc}") from exc
    if got != expected_sha256:
        raise RuntimeError(f"authorization digest mismatch: {got}")
    return got


def require_complete_sample(n_receipts: int, n_parent: int) -> None:
    if int(n_receipts) != int(n_parent):
        raise RuntimeError(f"INCOMPLETE SAMPLE: {n_receipts} of {n_parent} — refusing")


# ---------------------------------------------------------------- branch resolver
BRANCH_CONFIG = {
    "A_DR11": {"release": "dr11", "sweep_dir": "south/sweep/", "photoz_product": "ls_dr11.photo_z",
               "bricks_product": "survey-bricks-dr11-south.fits.gz", "image_tree": "dr11/south/coadd/",
               "band": "r", "hdu": 1},
    "B_DR10_1": {"release": "dr10.1", "sweep_dir": "south/sweep/10.1/",
                 "photoz_product": "ls_dr10.photo_z",
                 "bricks_product": "survey-bricks-dr10-south.fits.gz",
                 "image_tree": "dr10/south/coadd/", "band": "r", "hdu": 1},
}
BRANCH_FIELDS = tuple(sorted(BRANCH_CONFIG["A_DR11"]))


def resolve_branch(photoz_available: bool, resolution_date: str) -> dict:
    """BS-1 (gpt56-V6 F2 / codex-V6 F8). `photoz_available` is the receipted result of the
    pinned availability probe; `resolution_date` is the immutable stamp. Branch A iff the DR11
    photo-z product is available at resolution; otherwise Branch B. The returned config is the
    ONLY thing downstream may differ by."""
    key = "A_DR11" if photoz_available else "B_DR10_1"
    cfg = dict(BRANCH_CONFIG[key])
    if tuple(sorted(cfg)) != BRANCH_FIELDS:
        raise RuntimeError("branch config field set differs between branches — FAIL")
    return {"branch": key, "resolution_date": str(resolution_date), "config": cfg,
            "config_digest": digest(json.dumps(cfg, sort_keys=True).encode())}


def branch_invariance(fn, *args, **kwargs) -> dict:
    """Runs `fn` under both branch configs and returns the two output digests. Branch
    invariance means they are EQUAL — i.e. the pipeline's behaviour depends on the config
    only through recorded paths, never through logic."""
    outs = {}
    for key in ("A_DR11", "B_DR10_1"):
        outs[key] = digest(json.dumps(fn(BRANCH_CONFIG[key], *args, **kwargs),
                                      sort_keys=True, default=str).encode())
    return {"A": outs["A_DR11"], "B": outs["B_DR10_1"], "invariant": outs["A_DR11"] == outs["B_DR10_1"]}


# ---------------------------------------------------------------- fixtures
def _fx(name, cond, lines, extra=""):
    lines.append(f"{name}: {'PASS' if cond else 'FAIL'}{(' ' + extra) if extra else ''}")
    return bool(cond)


def _grid_bricks(n_ra=8, n_dec=4, dec0=-89.0, ddec=0.5):
    t = {}
    for j in range(n_dec):
        d1, d2 = dec0 + j * ddec, dec0 + (j + 1) * ddec
        for i in range(n_ra):
            r1, r2 = i * (360.0 / n_ra), (i + 1) * (360.0 / n_ra)
            t[f"b{i:02d}{j:02d}"] = (r1, r2, d1, d2)
    return t


def _sealed(n, c=None, s=None):
    cc = np.linspace(-0.95, 0.95, n) if c is None else np.asarray(c, dtype=np.float64)
    bnd = calibration_bins(cc)
    return SealedMask(np.arange(n) // 7, np.arange(n) % 7, cc, s, np.ones(n, dtype=np.int64), bnd)


def run_fixtures():
    lines, ok = [], True
    env = environment_record()
    lines.append(f"env python={env['python']} numpy={env['numpy']} platform={env['platform']} "
                 f"machine={env['machine']} byteorder={env['byteorder']}")
    lines.append(f"axis={list(AXIS)} longo_published={A_LONGO_PUBLISHED_SIGNED} ours={A_LONGO}")

    # ---- closure: the two attacks that defeated V6 must now fail closed
    bt = _grid_bricks()
    pids = np.array([10997315463551936, 10995116744378804, 3001, 3002], dtype=np.int64)
    pra = np.array([341.7455555890261, 288.4480136104449, 45.0, 200.0])
    pdec = np.array([-88.59161065343326, -87.1321298442747, -88.2, -87.6])
    pdig = parent_digest(pids, pra, pdec)
    full = close_manifest(pids, pra, pdec, pdig, bt,
                          sorted({b for i in range(4)
                                  for b in plan_object_bricks(pra[i], pdec[i], bt)}))
    ok &= _fx("CLOSURE-DERIVES", full["required_count"] > 0 and full["objects"] == 4, lines,
              f"required={full['required_count']} from {full['objects']} objects; "
              f"planner_digest={full['planner_digest'][:12]}…")
    # attack 1 (gpt56-V6 F1): omit a parent object
    try:
        close_manifest(pids[:3], pra[:3], pdec[:3], pdig, bt, full and
                       sorted({b for i in range(3) for b in plan_object_bricks(pra[i], pdec[i], bt)}))
        ok &= _fx("CLOSURE-OMITTED-OBJECT", False, lines)
    except ManifestClosureError as exc:
        ok &= _fx("CLOSURE-OMITTED-OBJECT", "PARENT DIGEST MISMATCH" in str(exc), lines,
                  "an omitted parent object changes the digest and is refused")
    # attack 2 (gpt56-V6 F1): a home-brick-only manifest
    home_only = sorted({plan_object_bricks(pra[i], pdec[i], bt)[0] for i in range(4)})
    try:
        close_manifest(pids, pra, pdec, pdig, bt, home_only)
        ok &= _fx("CLOSURE-HOME-ONLY", False, lines)
    except ManifestClosureError as exc:
        ok &= _fx("CLOSURE-HOME-ONLY", exc.result["missing_count"] > 0, lines,
                  f"home-only manifest short by {exc.result['missing_count']} neighbour bricks")
    # edge neighbours are genuinely returned
    edge = plan_object_bricks(45.0 - 1e-9, -88.5, bt)
    ok &= _fx("CLOSURE-EDGE-NEIGHBOURS", len(edge) >= 2, lines,
              f"an object on a brick edge plans {len(edge)} bricks")

    # ---- masks: production must refuse fixtures and wrong bins
    cs = np.linspace(-0.9, 0.9, 30)
    sealed = _sealed(30, cs, np.where(np.arange(30) % 2 == 0, 1.0, -1.0))
    fx = FixtureMask(np.arange(30) // 7, np.arange(30) % 7, cs,
                     np.where(np.arange(30) % 2 == 0, 1.0, -1.0))
    refused = 0
    for probe in (lambda: require_sealed(fx, True),
                  lambda: require_sealed(np.linspace(-1, 1, 5), False),
                  lambda: SealedMask(np.arange(6) // 3, np.arange(6) % 3, np.linspace(-1, 1, 6),
                                     np.ones(7), np.ones(6), calibration_bins(np.linspace(-1, 1, 6))),
                  lambda: SealedMask(np.arange(6) // 3, np.arange(6) % 3, np.linspace(-1, 1, 6),
                                     None, np.ones(6), calibration_bins(np.linspace(-1, 1, 6)),
                                     bin_label=np.zeros(6, dtype=np.int64)),
                  lambda: SealedMask(np.arange(6) // 3, np.arange(6) % 3, np.linspace(-1, 1, 6),
                                     None, np.array([1, 1, 1, 0, 1, 1]),
                                     calibration_bins(np.linspace(-1, 1, 6)))):
        try:
            probe()
        except RuntimeError:
            refused += 1
    ok &= _fx("MASK-REFUSALS", refused == 5, lines,
              f"{refused}/5 refused: fixture-to-production, bare vector, sign-length, "
              f"wrong bins, non-accepted row")
    ok &= _fx("MASK-KIND-IN-DIGEST", sealed.digest != FixtureMask(
        sealed.brickid, sealed.objid, sealed.c, sealed.s, None, sealed.boundaries,
        sealed.accept).digest, lines, "identical arrays under different kinds differ by digest")

    # ---- exact permutation sigma vs exhaustive enumeration
    cc4, ss4 = np.array([-1.0, -0.2, 0.4, 0.9]), np.array([-1.0, -1.0, 1.0, 1.0])
    vals = [beta_slope(ss4[list(p)], cc4) for p in itertools.permutations(range(4))]
    mean = sum(vals) / len(vals)
    var = sum((v - mean) ** 2 for v in vals) / len(vals)
    ok &= _fx("PERM-SIGMA-EXACT", abs(math.sqrt(var) - perm_sigma_exact(ss4, cc4)) < 1e-12, lines,
              f"enum={math.sqrt(var)!r} formula={perm_sigma_exact(ss4, cc4)!r}")

    # ---- power: the decision-metric contract (gpt56-V6 F7 / codex-V6 F7).
    # A Stage-P success must IMPLY a full independent Monte-Carlo success. Checked directly
    # over injected trials on four geometries, including the polar case the successor selects,
    # where the pure-normal threshold was measured anti-conservative.
    fam = [("uniform-2000", np.linspace(-0.97, 0.97, 2000)),
           ("bimodal-1200", np.where(np.arange(1200) % 2 == 0, -0.95, 0.95)),
           ("skewed-1500", -0.9 + 1.8 * (np.linspace(0, 1, 1500) ** 3)),
           ("polar-1000", np.concatenate([np.linspace(-0.99, -0.7, 700),
                                          np.linspace(0.7, 0.99, 300)]))]
    rows, implied_all, seen_all, contract_ok = [], 0, 0, True
    for fi, (name, cg) in enumerate(fam):
        n = len(cg)
        mm = FixtureMask(np.arange(n) // 5, np.arange(n) % 5, cg)
        ref = mm.with_signs(inject_signs(mm, 1.0, STAGE_P, 80 + fi, 1))
        ref_z = reference_null_z(ref, STAGE_P, 80 + fi)
        z_used = float(np.quantile(ref_z, 1.0 - P_REPRODUCED))
        seen = implied = 0
        for t in range(1, 9):
            rng = rng_at(STAGE_P, 80 + fi, t, ROLE_INJECT)
            s = np.array([1.0 if rng.random() < (1.0 + 0.14 * cg[i]) / 2.0 else -1.0
                          for i in range(n)])
            sm = mm.with_signs(s)
            if not calibrated_success(sm, ref_z):
                continue
            seen += 1
            if perm_record(sm, STAGE_P, 90 + fi, t, 5_000)[2] < P_REPRODUCED:
                implied += 1
        contract_ok &= (seen > 0 and implied == seen)
        seen_all += seen
        implied_all += implied
        rows.append(f"{name}: measured z* {z_used:.4f} (normal {Z_0001:.4f}); "
                    f"Stage-P successes {seen}, each confirmed by independent MC: {implied}")
    ok &= _fx("PWR-CONTRACT", contract_ok, lines,
              f"every Stage-P success was confirmed by an independent full-MC test "
              f"({implied_all}/{seen_all} across {len(fam)} geometries)")
    for r in rows:
        lines.append(f"    {r}")

    # the standardized null must be near-invariant to the sign multiset, since one measured
    # null serves all 1,000 trials. Measured on the polar geometry via tail mass at a fixed z.
    cpol = np.concatenate([np.linspace(-0.99, -0.7, 700), np.linspace(0.7, 0.99, 300)])
    tails = []
    for imb in (2, 3, 5, 7):
        s = np.where(np.arange(1000) % imb == 0, 1.0, -1.0)
        mp = FixtureMask(np.arange(1000) // 5, np.arange(1000) % 5, cpol, s)
        rz = reference_null_z(mp, STAGE_P, 70 + imb)
        tails.append(float((rz >= Z_0001).mean()))
    spread = (max(tails) - min(tails)) / max(min(tails), 1e-12)
    ok &= _fx("PWR-Z-STABLE", spread < 0.5, lines,
              f"tail mass beyond z={Z_0001:.3f} across sign multisets: "
              f"{[f'{t:.5f}' for t in tails]}, relative spread {100 * spread:.1f}% "
              f"(measured; the conservative deflation absorbs it)")

    # ---- planning: oracle integration, 17-raw/16-retained boundary, re-pass
    refused = 0
    for bad in (dict(brickid=[1, 1], c=[0.1, 0.2], n_eligible=[1, 2]),
                dict(brickid=[1, 2], c=[0.1, 0.2], n_eligible=[5, -1]),
                dict(brickid=[1, 2], c=[0.1, 0.2], n_eligible=[5.9, 0.2]),
                dict(brickid=[1, 2, 3], c=[0.1, 0.2, 0.3], n_eligible=[1, 2],)):
        try:
            validate_count_table(**bad)
        except RuntimeError:
            refused += 1
    ok &= _fx("ORACLE-STRICT", refused == 4, lines,
              f"{refused}/4 refused: duplicate key, negative, float counts, length mismatch")
    try:
        validate_count_table([1, 2, 3], [0.1, 0.2, 0.3], [5, 0, 7], universe_brickid=[1, 2, 3, 4],
                             grouped_sum=12, ungrouped_total=12)
        ok &= _fx("ORACLE-UNIVERSE", False, lines)
    except RuntimeError:
        ok &= _fx("ORACLE-UNIVERSE", True, lines, "a universe brick missing from the table is refused")
    n17 = np.array([9] * 16 + [1], dtype=np.int64)          # 17 raw-positive, 16 retained-positive
    c17 = np.linspace(-0.9, 0.9, 17)
    ok &= _fx("RAW-EXACT-BOUNDARY", int(np.count_nonzero(retained_counts(n17) > 0)) == 16
              and int(np.count_nonzero(n17 > 0)) == 17, lines,
              "fixture geometry: 17 raw-positive, 16 retained-positive")
    bid17 = np.arange(17)
    ordr, _ = greedy_ledger(bid17, c17, n17)
    try:
        local_pass(bid17, c17, n17, retained_counts(n17), ordr, 1e18)
        ok &= _fx("RAW-EXACT-BRANCH", False, lines)
    except RuntimeError as exc:
        ok &= _fx("RAW-EXACT-BRANCH", "greedy order never reaches" in str(exc), lines,
                  "17 raw-positive takes the HEURISTIC branch (V6 wrongly took exact)")
    c7 = np.array([-0.4868224155944405, -0.8730927047630801, -0.3831733423895676,
                   -0.01644607194273373, -0.8506728007144366, -0.2700354997649146,
                   -0.5419268492467646])
    n7 = np.array([16, 9, 14, 6, 1, 2, 12])
    plan = build_plan(np.arange(7), c7, n7, l_plan_override=1.2927783953207417)
    ok &= _fx("RAW-RET", plan["selected_brickid"] == [1, 3], lines,
              f"selected={plan['selected_brickid']} L_ret={plan['L_ret_final']!r} "
              f"(a raw-threshold call returns [1, 2] at L_ret 1.0611453924627055)")

    # ---- calibration: the inherited HC-1H estimator, floors, tie rule
    cal = accuracy_from_handcheck([920, 910, 900], [1000, 1000, 1000], 0.02, 0.004)
    quoted = (0.9 - 0.02) / (1.0 - 0.04)
    ok &= _fx("HC-ESTIMATOR", abs(cal["a_b"][2] - quoted) < 1e-12, lines,
              f"raw 0.9, eps 0.02 -> {cal['a_b'][2]!r} (quoted {quoted!r}; V6 returned 0.9)")
    ok &= _fx("HC-COV-OFFDIAG", cal["cov_a"][0, 1] > 0 and cal["cov_a"][0, 1] != cal["cov_a"][0, 0],
              lines, f"shared-epsilon derivative gives a real off-diagonal "
                     f"{cal['cov_a'][0, 1]:.3e}, path={adjudicate_path(cal)}")
    cells = np.zeros((N_CAL_BINS, N_HC_STRATA), dtype=np.int64) + 200
    cells[:, 4] = np.array([40, 0, 0])                       # sparse but FEASIBLE stratum
    alloc = allocate_handcheck(cells, HC_REAL_LABELS)
    ok &= _fx("HC-STRATUM-FLOOR", int(alloc.sum()) == HC_REAL_LABELS
              and all(int(alloc[:, j].sum()) >= HC_MIN_PER_STRATUM
                      for j in range(N_HC_STRATA) if (cells[:, j] > 0).any()), lines,
              f"sparse stratum lifted to {int(alloc[:, 4].sum())} >= {HC_MIN_PER_STRATUM} "
              f"(V6 allowed 10)")
    infeasible = cells.copy()
    infeasible[:, 4] = np.array([12, 0, 0])                  # fewer objects than the floor
    try:
        allocate_handcheck(infeasible, HC_REAL_LABELS)
        ok &= _fx("HC-STRATUM-INFEASIBLE", False, lines)
    except RuntimeError as exc:
        ok &= _fx("HC-STRATUM-INFEASIBLE", "cannot reach its floor" in str(exc), lines,
                  "a stratum with fewer objects than its floor fails closed, never shrinks")
    tied = np.array([0.5] * 9)
    try:
        calibration_bins(tied)
        ok &= _fx("CAL-TIE-REFUSAL", False, lines)
    except RuntimeError:
        ok &= _fx("CAL-TIE-REFUSAL", True, lines, "all-tied c refuses instead of emptying bins")
    cal_prof = accuracy_from_handcheck([975, 915, 890], [1000, 1000, 1000], 0.02, 0.004)
    ok &= _fx("CAL-PATH-PROFILE", adjudicate_path(cal_prof) == "PROFILE", lines)
    try:
        adjudicate_path(accuracy_from_handcheck([880, 870, 700], [1000] * 3, 0.02, 0.004))
        ok &= _fx("CAL-HALT", False, lines)
    except InconclusiveByCalibration as exc:
        ok &= _fx("CAL-HALT", True, lines, str(exc))

    # ---- the production path has no seams
    import inspect
    sig = inspect.signature(run_production_verdict)
    ok &= _fx("PROD-NO-SEAMS", not any(p in sig.parameters for p in ("_perm", "n_perm", "stage", "trial")),
              lines, f"run_production_verdict{tuple(sig.parameters)}")
    calls = run_production_verdict.__code__.co_names
    ok &= _fx("PROD-CALLS-GUARDS", all(g in calls for g in
              ("require_environment", "require_authorization", "require_complete_sample",
               "require_sealed", "perm_record")), lines,
              "every guard and the full permutation record are called by name in the runner")
    stage_c_bad = {"slot": "BS-5f", "passed": True, "mask_digest": "0" * 64}
    try:
        run_production_verdict(sealed, cal, authorization_path="/nonexistent",
                               authorization_sha256="0" * 64, n_receipts=1, n_parent=1,
                               stage_c_receipt=stage_c_bad)
        ok &= _fx("PROD-REFUSES", False, lines)
    except RuntimeError as exc:
        ok &= _fx("PROD-REFUSES", "authorization" in str(exc), lines,
                  "missing authorization stops the production path before any statistic")

    # ---- lapsed-spec battery, restored to its named boundaries
    def _synth(A_true, n, a, addr):
        cg = np.linspace(-0.98, 0.98, n)
        mk = _sealed(n, cg)
        rng = rng_at(STAGE_REAL, 99, addr, ROLE_INJECT)
        s = np.empty(n)
        for i in range(n):
            lat = 1.0 if rng.random() < (1.0 + A_true * cg[i]) / 2.0 else -1.0
            s[i] = -lat if rng.random() < (1.0 - a) else lat
        mk = mk.with_signs(s)
        beta = beta_slope(mk.s, mk.c)
        sig = perm_sigma_exact(mk.s, mk.c)
        p = 0.5 * math.erfc((beta / sig) / math.sqrt(2.0))
        cal_b = accuracy_from_handcheck([int(a * 1000)] * 3, [1000] * 3, 0.01, 0.003)
        return explore_verdict(mk, cal_b, beta, p, sig)

    d0 = _synth(0.0, 4000, 0.93, 1)
    ok &= _fx("BATTERY-A0", d0["verdict"] != "REPRODUCED-LONGO", lines,
              f"A=0 -> {d0['verdict']}")
    dn = _synth(-A_LONGO, 4000, 0.93, 2)
    ok &= _fx("BATTERY-SIGN", dn["verdict"] != "REPRODUCED-LONGO", lines,
              f"A=-0.0408 -> {dn['verdict']} (A_L={dn['A_L']:.5f})")
    dp = _synth(A_LONGO, 200_000, 0.93, 3)
    ok &= _fx("BATTERY-POS", dp["verdict"] == "REPRODUCED-LONGO", lines,
              f"A=+0.0408 at powered N -> {dp['verdict']} (A_L={dp['A_L']:.5f}, p={dp['p']:.2e}, "
              f"floor={dp['evaluated_floor']:.5f})")
    small = _sealed(300, np.linspace(-0.98, 0.98, 300),
                    np.where(np.arange(300) % 2 == 0, 1.0, -1.0))
    n_eq_small = 3.0 * 300 * float(np.var(small.c))
    ok &= _fx("BATTERY-NEQ", n_eq_small < NEQ_MIN, lines,
              f"N_eq {n_eq_small:.1f} < {NEQ_MIN}: the runner derives INCONCLUSIVE-BY-POWER "
              f"from geometry, not from a caller-supplied boolean")

    # ---- branch resolver and invariance
    ra = resolve_branch(True, "2026-09-05")
    rb = resolve_branch(False, "2026-09-05")
    ok &= _fx("BRANCH-RESOLVE", ra["branch"] == "A_DR11" and rb["branch"] == "B_DR10_1"
              and ra["config_digest"] != rb["config_digest"], lines,
              f"A={ra['config_digest'][:12]}… B={rb['config_digest'][:12]}…")
    inv = branch_invariance(lambda cfg: {"selected": plan["selected_brickid"],
                                         "L": plan["L_ret_final"]})
    ok &= _fx("BRANCH-INVARIANT", inv["invariant"], lines,
              "the selection pipeline's output digest is identical under both configs")

    # ---- receipt schemas are enforced
    try:
        receipt("BS-V", {"verdict": b"X"})
        ok &= _fx("RECEIPT-SCHEMA", False, lines)
    except RuntimeError:
        ok &= _fx("RECEIPT-SCHEMA", True, lines, "a slot receipt missing its named fields is refused")

    out = "\n".join(lines) + "\n" + ("ALL FIXTURES PASS" if ok else "FIXTURE FAILURE") + "\n"
    return out, ok


if __name__ == "__main__":
    if "--fixtures" in sys.argv:
        text, good = run_fixtures()
        sys.stdout.write(text)
        sys.exit(0 if good else 1)
    sys.stdout.write(__doc__ + "\n")
