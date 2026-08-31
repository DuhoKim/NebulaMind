#!/usr/bin/env python3
"""stratum_index_producer — Row D2 (slot BS-SI, class E), REQUIRED build item
(GPT56-V100 F3; producer created by the principal's strata-option-A ruling,
2026-08-30). Runs the TWO committee architectures' outputs into the per-object HC
stratum index — machine-committee state × |χ| tertile, both axes χ-derived by the
ruling — and writes the SEALED artifact via Row B with its receipt.

CLASS-E DISCIPLINE, structural: the artifact fills at P2–P3 and its schema is
written when the slot fills (SCHEMA-PENDING). Until a schema commitment exists,
produce() REFUSES — there is no tag to seal under and no artifact may be emitted,
which is the draft's own blocking clause for BS-2f's allocation and BS-8p. The
fixtures pass an explicitly TEST-marked schema commitment; the real one arrives at
slot-fill and its digest binds into the receipt.

THE TYPED/CAPABILITY BARRIER is this row's load-bearing clause: the sealed artifact
is consumable by Row F's allocation constructor (`allocate_handcheck`) ONLY.
consume() refuses every other consumer, and the positions-only guard refuses any
calibration-bound row that carries a stratum field — the stratum index may reach
the allocation and may NEVER reach `calibration_bins()`.

DECLARED CONVENTIONS (bound into the artifact, recomputed by the verifier —
committed here so they cannot be shopped at P2):
- committee state: the two architectures' handedness calls, each in {"S","Z"};
  equal-S → AGREE-S, equal-Z → AGREE-Z, unequal → DISAGREE; any other call value
  refuses (closed set).
- |χ| tertile: rank thirds over the input set sorted by (chi_abs, object_id) —
  the stable tie rule; sizes n//3 + (1 if tertile_index < n % 3 else 0), lowest
  tertiles absorbing the remainder first; labels T1 (lowest) / T2 / T3.
- the stratum key is (state, tertile): 3 × 3 = 9, matching v9's frozen
  N_HC_STRATA = 9.
- seal bytes: the schema commitment's tag + the canonical JSON of the sorted
  per-object rows plus the convention block; receipt = sha256 over the seal
  bytes."""
import hashlib
import json
import sys

STATES = ("AGREE-S", "AGREE-Z", "DISAGREE")
TERTILES = ("T1", "T2", "T3")
CONSUMER = "allocate_handcheck"


class StratumRefusal(ValueError):
    def __init__(self, code, msg):
        self.code = code
        super().__init__(f"{code}: {msg}")


def _r(code, msg):
    raise StratumRefusal(code, msg)


def _canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False)


def committee_state(call_a, call_b):
    for c in (call_a, call_b):
        if c not in ("S", "Z"):
            _r("CALL-OUT-OF-SET", f"handedness call {c!r} outside {{S, Z}}")
    if call_a == call_b:
        return "AGREE-S" if call_a == "S" else "AGREE-Z"
    return "DISAGREE"


def tertiles(objects):
    """objects: list of (object_id, chi_abs). Returns {object_id: tertile} under
    the declared rank rule. Refuses on duplicate ids, non-finite or negative
    |χ|, or fewer than 3 objects (no thirds of fewer)."""
    ids = [o for o, _ in objects]
    if len(set(ids)) != len(ids):
        _r("DUPLICATE-OBJECT", "an object appears twice in the tertile input")
    if len(objects) < 3:
        _r("TOO-FEW-OBJECTS", f"{len(objects)} objects cannot form tertiles")
    for o, c in objects:
        if not (type(c) in (int, float) and c == c and c >= 0
                and c != float("inf")):
            _r("CHI-OUT-OF-RANGE", f"|chi| for {o!r} is not a finite non-negative "
                                   "number")
    ranked = sorted(objects, key=lambda t: (t[1], str(t[0])))
    n = len(ranked)
    sizes = [n // 3 + (1 if i < n % 3 else 0) for i in range(3)]
    out = {}
    k = 0
    for t_i, size in enumerate(sizes):
        for _ in range(size):
            out[ranked[k][0]] = TERTILES[t_i]
            k += 1
    return out


def build_index(committee_calls, chi_rows):
    """committee_calls: {object_id: (call_a, call_b)}; chi_rows: list of
    (object_id, chi_abs) from Row D's receipts. The two inputs must cover the
    SAME object set — a missing or extra object refuses."""
    if set(committee_calls) != {o for o, _ in chi_rows}:
        _r("OBJECT-SET-MISMATCH",
           "committee outputs and Row D receipts cover different objects")
    ters = tertiles(chi_rows)
    rows = []
    for oid in sorted(committee_calls, key=str):
        a, b = committee_calls[oid]
        rows.append({"object_id": oid, "state": committee_state(a, b),
                     "tertile": ters[oid]})
    counts = {}
    for r in rows:
        key = f"{r['state']}|{r['tertile']}"
        counts[key] = counts.get(key, 0) + 1
    return {"rows": rows, "stratum_counts": counts,
            "convention": {"tie_rule": "(chi_abs, object_id) stable sort",
                           "remainder_rule": "lowest tertiles first",
                           "states": list(STATES), "tertiles": list(TERTILES)}}


class SealedStratumIndex:
    """The typed artifact. Only consume(artifact, CONSUMER) opens it — the
    capability barrier the row's load-bearing clause demands."""

    def __init__(self, seal_bytes, receipt):
        self._seal_bytes = seal_bytes
        self.receipt = receipt


def produce(committee_calls, chi_rows, schema_commit, row_b_write):
    """The one emission path: refuses without a schema commitment (SCHEMA-PENDING),
    seals under the commitment's tag, writes VIA ROW B, returns (artifact,
    receipt, chain_position). There is no unsealed return."""
    if schema_commit is None:
        _r("SCHEMA-PENDING",
           "the BS-SI schema is written when the slot fills at P2–P3; no "
           "stratum-index artifact may be emitted before it — this refusal IS "
           "the draft's blocking clause for BS-2f's allocation and BS-8p")
    for f in ("tag", "schema_digest"):
        if f not in schema_commit:
            _r("SCHEMA-COMMIT-MALFORMED", f"schema commitment missing {f}")
    if not callable(row_b_write):
        _r("ROW-B-REQUIRED",
           "the artifact is written via Row B or not at all")
    index = build_index(committee_calls, chi_rows)
    body = {"index": index, "schema_digest": schema_commit["schema_digest"]}
    seal = (b"NMPR1:" + schema_commit["tag"].encode() + b":"
            + _canon(body).encode())
    receipt = hashlib.sha256(seal).hexdigest()
    pos = row_b_write(seal)
    return SealedStratumIndex(seal, receipt), receipt, pos


def consume(artifact, consumer):
    """The capability barrier: Row F's allocation constructor only."""
    if type(artifact) is not SealedStratumIndex:
        _r("NOT-A-SEALED-INDEX", "consume() takes the sealed artifact, exactly")
    if consumer != CONSUMER:
        _r("CONSUMER-BARRIER",
           f"the stratum index is consumable by {CONSUMER} ONLY; {consumer!r} "
           "may not open it — and calibration_bins() may never")
    return artifact._seal_bytes


def positions_only_guard(rows):
    """BS-2f's boundary recomputation is POSITIONS-ONLY: any row carrying a
    stratum-bearing field refuses as contamination (the third required fixture)."""
    forbidden = {"state", "tertile", "stratum", "stratum_counts"}
    for i, r in enumerate(rows):
        hit = forbidden & set(r)
        if hit:
            _r("STRATUM-CONTAMINATION",
               f"row {i} carries {sorted(hit)} — the stratum index may never "
               "reach calibration_bins()")
    return True


# ------------------------------------------------------------------ fixtures
def fixtures():
    f = []
    total = 0
    T = {"tag": "stratum-index-TEST", "schema_digest": "5" * 64}
    calls = {"a": ("S", "S"), "b": ("Z", "Z"), "c": ("S", "Z"),
             "d": ("Z", "S"), "e": ("S", "S"), "g": ("Z", "Z")}
    chis = [("a", 0.1), ("b", 0.5), ("c", 0.9), ("d", 0.2), ("e", 0.6),
            ("g", 1.1)]
    writes = []

    def wb(b):
        writes.append(b)
        return len(writes) - 1

    def expect(code, thunk):
        nonlocal total
        total += 1
        try:
            thunk()
        except StratumRefusal as e:
            if e.code != code:
                f.append(f"[{code}] refused with {e.code}")
            return
        except Exception as e:
            f.append(f"[{code}] non-refusal {type(e).__name__}: {e}")
            return
        f.append(f"[{code}] accepted")

    total += 1
    art, receipt, pos = produce(calls, chis, T, wb)
    if hashlib.sha256(writes[pos]).hexdigest() != receipt:
        f.append("receipt does not bind the Row B bytes")
    total += 1
    art2, receipt2, _ = produce(calls, chis, T, wb)
    if receipt2 != receipt:
        f.append("same inputs, different receipts — sealing not deterministic")
    total += 1
    if consume(art, CONSUMER) != writes[pos]:
        f.append("legitimate consumer got different bytes than Row B holds")
    expect("CONSUMER-BARRIER", lambda: consume(art, "calibration_bins"))
    expect("CONSUMER-BARRIER", lambda: consume(art, "bs8p"))
    expect("NOT-A-SEALED-INDEX", lambda: consume({"seal": b"x"}, CONSUMER))
    expect("SCHEMA-PENDING", lambda: produce(calls, chis, None, wb))
    expect("SCHEMA-COMMIT-MALFORMED",
           lambda: produce(calls, chis, {"tag": "x"}, wb))
    expect("ROW-B-REQUIRED", lambda: produce(calls, chis, T, None))
    expect("CALL-OUT-OF-SET",
           lambda: build_index({"a": ("S", "M"), "b": ("S", "S"),
                                "c": ("Z", "Z")},
                               [("a", 0.1), ("b", 0.2), ("c", 0.3)]))
    expect("OBJECT-SET-MISMATCH",
           lambda: build_index(dict(calls, extra=("S", "S")), chis))
    expect("DUPLICATE-OBJECT",
           lambda: tertiles([("a", 0.1), ("a", 0.2), ("b", 0.3)]))
    expect("TOO-FEW-OBJECTS", lambda: tertiles([("a", 0.1), ("b", 0.2)]))
    expect("CHI-OUT-OF-RANGE", lambda: tertiles([("a", -0.1), ("b", 0.2),
                                                 ("c", 0.3)]))
    expect("CHI-OUT-OF-RANGE", lambda: tertiles([("a", float("nan")),
                                                 ("b", 0.2), ("c", 0.3)]))
    # declared tertile rule: 6 objects → sizes 2/2/2 in (chi, id) order
    total += 1
    ters = tertiles(chis)
    if [ters[o] for o in ("a", "d", "b", "e", "c", "g")] != \
            ["T1", "T1", "T2", "T2", "T3", "T3"]:
        f.append(f"tertile rule drifted: {ters}")
    # remainder rule: 7 objects → 3/2/2, lowest first; tie broken by object_id
    total += 1
    t7 = tertiles(chis + [("h", 0.5)])
    if sum(1 for v in t7.values() if v == "T1") != 3:
        f.append("remainder did not go to the lowest tertile")
    if t7["b"] != "T1" or t7["h"] != "T2":
        # 0.5 tie: 'b' < 'h' lexically, so b takes rank 2 (absorbed by the
        # 3-member lowest tertile) and h takes rank 3 (T2) — the tie rule split
        f.append(f"tie rule drifted: b={t7['b']}, h={t7['h']}")
    # committee-state axis
    total += 1
    if (committee_state("S", "S"), committee_state("Z", "Z"),
            committee_state("S", "Z")) != ("AGREE-S", "AGREE-Z", "DISAGREE"):
        f.append("committee state mapping drifted")
    # nine possible strata, counts partition the objects
    total += 1
    idx = build_index(calls, chis)
    if sum(idx["stratum_counts"].values()) != len(chis):
        f.append("stratum counts do not partition the object set")
    # positions-only guard: clean rows pass, contaminated rows refuse
    total += 1
    positions_only_guard([{"object_id": "a", "position": 1,
                           "accept_flag": True}])
    expect("STRATUM-CONTAMINATION",
           lambda: positions_only_guard([{"object_id": "a", "position": 1,
                                          "tertile": "T1"}]))
    expect("STRATUM-CONTAMINATION",
           lambda: positions_only_guard([{"object_id": "a", "position": 1,
                                          "state": "AGREE-S"}]))
    return f, total


if __name__ == "__main__":
    fails, total = fixtures()
    for x in fails:
        print("FIXTURE FAIL:", x)
    print(f"stratum index producer fixtures: {total - len(fails)}/{total} green")
    sys.exit(1 if fails else 0)
