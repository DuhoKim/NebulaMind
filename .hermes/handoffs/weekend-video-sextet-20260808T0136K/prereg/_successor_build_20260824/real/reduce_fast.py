#!/usr/bin/env python3
"""Removal pass equivalent to the frozen local_pass's removal loop, done in O(n) per scan.

Identity used: for weighted SSE with S1 = sum n_i c_i, S2 = sum n_i c_i^2, N = sum n_i,
    SSE            = S2 - S1^2 / N
    SSE without j  = (S2 - n_j c_j^2) - (S1 - n_j c_j)^2 / (N - n_j)
so an entire removal scan costs one vector pass instead of |S| full recomputations.
Agreement with the frozen local_pass is proven on random small cases before production use.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ref"))
import successor_ref_v4 as R


def sse_without(n, c, S1, S2, N):
    Nj = N - n
    with np.errstate(invalid="ignore", divide="ignore"):
        out = (S2 - n * c * c) - (S1 - n * c) ** 2 / Nj
    return np.where(Nj > 0, out, 0.0)


def reduce_removals(brickid, c, n_ret, target):
    """Frozen sequence: cut the greedy order at the smallest prefix reaching `target`, THEN
    remove. (An earlier version reduced from the whole ordered set and disagreed with the
    frozen local_pass on 1 of 30 random cases — the prefix cut is part of the rule, not an
    optimisation.) Removal rule: ascending removal-loss, ties by brickid; remove the first
    whose removal keeps L >= target; repeat until none applies."""
    bid = np.asarray(brickid, dtype=np.int64)
    cc = np.asarray(c, dtype=np.float64)
    nn = np.asarray(n_ret, dtype=np.float64)
    pool = [k for k in range(len(bid)) if nn[k] > 0]
    csum_N = np.cumsum(nn); csum_1 = np.cumsum(nn * cc); csum_2 = np.cumsum(nn * cc * cc)
    with np.errstate(invalid="ignore", divide="ignore"):
        Lpref = np.where(csum_N > 0, csum_2 - csum_1 ** 2 / csum_N, 0.0)
    hit = np.nonzero(Lpref >= target)[0]
    if hit.size == 0:
        raise RuntimeError("greedy order never reaches the target on retained counts")
    cut = int(hit[0]) + 1
    keep = np.zeros(len(bid), dtype=bool)
    keep[:cut] = True
    removed = []
    while True:
        n, cv, b = nn[keep], cc[keep], bid[keep]
        N = float(n.sum()); S1 = float((n * cv).sum()); S2 = float((n * cv * cv).sum())
        L = S2 - S1 * S1 / N
        cand = sse_without(n, cv, S1, S2, N)
        loss = L - cand
        legal = cand >= target
        if not legal.any():
            # No single removal is legal. The FROZEN local_pass does not stop here: it tries
            # every accepted brick swapped for every unaccepted positive-count brick, in
            # ascending brickid order, and commits the first swap after which a removal
            # becomes legal. (Round 8, codex: omitting this phase is not equivalent -- their
            # trial-47 counterexample gets 6 bricks from the frozen rule and 7 from
            # removal-only. 30 random cases never fired a swap.)
            moved = _swap_then_remove(bid, cc, nn, keep, target, pool)
            if moved is None:
                return keep, L, removed
            keep, rm = moved
            removed.append(rm)
            continue
        idx = np.nonzero(legal)[0]
        pick = idx[np.lexsort((b[idx], loss[idx]))[0]]      # ascending loss, then brickid
        gpos = np.nonzero(keep)[0][pick]
        keep[gpos] = False
        removed.append(int(bid[gpos]))


def _swap_then_remove(bid, cc, nn, keep, target, pool):
    """One frozen swap move: accepted i (ascending brickid) x unaccepted positive j (ascending
    brickid); commit the first (i, j) whose swap keeps L >= target AND after which some
    removal is legal. Vectorised over j; returns (new_keep, removed_brickid) or None."""
    acc = np.nonzero(keep)[0]
    unacc = np.array([k for k in pool if not keep[k]], dtype=np.int64)
    if unacc.size == 0:
        return None
    n_a, c_a = nn[keep], cc[keep]
    N = float(n_a.sum()); S1 = float((n_a * c_a).sum()); S2 = float((n_a * c_a * c_a).sum())
    nj, cj = nn[unacc], cc[unacc]
    for i in acc[np.argsort(bid[acc], kind="stable")]:
        ni, ci = float(nn[i]), float(cc[i])
        N1, A1, B1 = N - ni, S1 - ni * ci, S2 - ni * ci * ci      # after removing i
        Nn, An, Bn = N1 + nj, A1 + nj * cj, B1 + nj * cj * cj     # after adding each j
        with np.errstate(invalid="ignore", divide="ignore"):
            Lsw = np.where(Nn > 0, Bn - An * An / Nn, -np.inf)
        ok_j = np.nonzero(Lsw >= target)[0]
        if ok_j.size == 0:
            continue
        for j in ok_j[np.argsort(bid[unacc[ok_j]], kind="stable")]:
            k2 = keep.copy(); k2[i] = False; k2[unacc[j]] = True
            n2, c2 = nn[k2], cc[k2]
            N2 = float(n2.sum()); P1 = float((n2 * c2).sum()); P2 = float((n2 * c2 * c2).sum())
            cand2 = sse_without(n2, c2, P1, P2, N2)
            legal2 = cand2 >= target
            if not legal2.any():
                continue
            L2 = P2 - P1 * P1 / N2
            loss2 = L2 - cand2
            b2 = bid[k2]
            idx2 = np.nonzero(legal2)[0]
            pick2 = idx2[np.lexsort((b2[idx2], loss2[idx2]))[0]]
            gpos2 = np.nonzero(k2)[0][pick2]
            k2[gpos2] = False
            return k2, int(bid[gpos2])
    return None


def prove_agreement(trials=30, seed=11):
    rng = np.random.default_rng(seed)
    checked = 0
    for t in range(trials):
        n = int(rng.integers(18, 26))                        # above N_EXACT: heuristic branch
        bid = np.arange(200, 200 + n, dtype=np.int64)
        c = np.round(rng.uniform(-1, 1, n), 3)
        nraw = rng.integers(1, 40, n).astype(np.int64)
        nret = R.retained_counts(nraw)
        if (nret > 0).sum() < 5:
            continue
        order, _ = R.greedy_ledger(bid, c, nraw)
        full = R.sse(nret, c)
        target = 0.55 * full
        try:
            ref_sel, ref_L = R.local_pass(bid, c, nraw, nret, order, target)
        except RuntimeError:
            continue
        keep, L, _rm = reduce_removals(bid[order], c[order], nret[order], target)
        fast_set = sorted(int(x) for x in bid[order][keep])
        ref_set = sorted(int(bid[i]) for i in ref_sel)
        if fast_set != ref_set:
            raise AssertionError(f"trial {t}: fast {fast_set} != frozen {ref_set}")
        checked += 1
    return checked


if __name__ == "__main__":
    print(f"removal pass agrees with the frozen local_pass on {prove_agreement()} random cases")
