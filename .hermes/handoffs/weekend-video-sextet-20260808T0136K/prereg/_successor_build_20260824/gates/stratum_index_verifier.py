#!/usr/bin/env python3
"""stratum_index_verifier — the INDEPENDENT half of Row D2 (slot BS-SI): recomputes
the per-object HC stratum index from Row D's receipts (per-object |χ|) and the two
committee architectures' outputs, and refuses any mismatch with the sealed artifact.

INDEPENDENCE IS THE DESIGN, SAID PLAINLY: this file deliberately does NOT import the
producer's build_index — the one place a second implementation is the point, because
an imported recomputation reproduces the producer's own bug and certifies it
(common-mode failure), while a divergent independent derivation surfaces as
INDEX-MISMATCH. The conventions both files implement are FROZEN in both docstrings
(stable (chi_abs, object_id) tie rule, lowest-tertiles-first remainder, the
AGREE-S/AGREE-Z/DISAGREE state map, rows sorted by str(object_id)); if the two
implementations ever disagree, the refusal fires and the divergence is the finding.

The verifier runs AT EMISSION (Row D2 writes "sealed, independently verified");
the downstream capability barrier — allocate_handcheck ONLY — governs consumption
and lives with the producer's consume()."""
import hashlib
import json
import sys

STATES = ("AGREE-S", "AGREE-Z", "DISAGREE")
TERTILES = ("T1", "T2", "T3")


class StratumVerifyRefusal(ValueError):
    def __init__(self, code, msg):
        self.code = code
        super().__init__(f"{code}: {msg}")


def _r(code, msg):
    raise StratumVerifyRefusal(code, msg)


def _canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False)


def _own_state(a, b):
    # independent derivation, not an import
    if a not in ("S", "Z") or b not in ("S", "Z"):
        _r("CALL-OUT-OF-SET", f"({a!r}, {b!r})")
    if a != b:
        return "DISAGREE"
    return {"S": "AGREE-S", "Z": "AGREE-Z"}[a]


def _own_tertiles(chi_rows):
    ids = [o for o, _ in chi_rows]
    if len(set(ids)) != len(ids):
        _r("DUPLICATE-OBJECT", "duplicate object in Row D receipts")
    if len(chi_rows) < 3:
        _r("TOO-FEW-OBJECTS", str(len(chi_rows)))
    for o, c in chi_rows:
        if not (type(c) in (int, float) and c == c and 0 <= c < float("inf")):
            _r("CHI-OUT-OF-RANGE", repr(o))
    order = sorted(chi_rows, key=lambda t: (t[1], str(t[0])))
    n = len(order)
    out = {}
    i = 0
    for t_idx in range(3):
        take = n // 3 + (1 if t_idx < n % 3 else 0)
        for _ in range(take):
            out[order[i][0]] = TERTILES[t_idx]
            i += 1
    return out


def recompute_index(committee_calls, chi_rows):
    if set(committee_calls) != {o for o, _ in chi_rows}:
        _r("OBJECT-SET-MISMATCH",
           "committee outputs and Row D receipts cover different objects")
    ters = _own_tertiles(chi_rows)
    rows = [{"object_id": oid,
             "state": _own_state(*committee_calls[oid]),
             "tertile": ters[oid]}
            for oid in sorted(committee_calls, key=str)]
    counts = {}
    for r in rows:
        k = f"{r['state']}|{r['tertile']}"
        counts[k] = counts.get(k, 0) + 1
    return {"rows": rows, "stratum_counts": counts,
            "convention": {"tie_rule": "(chi_abs, object_id) stable sort",
                           "remainder_rule": "lowest tertiles first",
                           "states": list(STATES), "tertiles": list(TERTILES)}}


def verify_stratum_index(seal_bytes, receipt, committee_calls, chi_rows,
                         schema_commit):
    """The full check: seal framing under the schema commitment's tag, the schema
    digest binding, the sha256 receipt, and the byte-for-byte comparison of the
    sealed index against this file's OWN recomputation from the raw inputs."""
    if type(seal_bytes) is not bytes:
        _r("SEAL-MALFORMED", "seal must be bytes, exactly")
    for f in ("tag", "schema_digest"):
        if f not in (schema_commit or {}):
            _r("SCHEMA-COMMIT-MALFORMED", f"missing {f}")
    want_prefix = b"NMPR1:" + schema_commit["tag"].encode() + b":"
    if not seal_bytes.startswith(want_prefix):
        _r("SEAL-TAG-MISMATCH",
           f"seal does not open with {want_prefix!r}")
    if hashlib.sha256(seal_bytes).hexdigest() != receipt:
        _r("RECEIPT-MISMATCH",
           "the presented receipt does not bind these seal bytes")
    try:
        body = json.loads(seal_bytes[len(want_prefix):].decode("utf-8"))
    except Exception as e:
        _r("SEAL-MALFORMED", f"body does not parse: {e}")
    if type(body) is not dict or set(body) != {"index", "schema_digest"}:
        _r("SEAL-MALFORMED", "body fields are not exactly {index, schema_digest}")
    if body["schema_digest"] != schema_commit["schema_digest"]:
        _r("SCHEMA-DIGEST-MISMATCH",
           "the sealed schema digest is not the committed one")
    recomputed = recompute_index(committee_calls, chi_rows)
    if _canon(recomputed) != _canon(body["index"]):
        _r("INDEX-MISMATCH",
           "the sealed index does not equal the independent recomputation from "
           "Row D's receipts and the committee outputs")
    return True


# ------------------------------------------------------------------ fixtures
def fixtures():
    import stratum_index_producer as sip  # test-artifact generation ONLY
    f = []
    total = 0
    T = {"tag": "stratum-index-TEST", "schema_digest": "5" * 64}
    calls = {"a": ("S", "S"), "b": ("Z", "Z"), "c": ("S", "Z"),
             "d": ("Z", "S"), "e": ("S", "S"), "g": ("Z", "Z")}
    chis = [("a", 0.1), ("b", 0.5), ("c", 0.9), ("d", 0.2), ("e", 0.6),
            ("g", 1.1)]
    writes = []
    art, receipt, _ = sip.produce(calls, chis, T, lambda b: writes.append(b))
    seal = writes[0]

    def expect(code, thunk):
        nonlocal total
        total += 1
        try:
            thunk()
        except StratumVerifyRefusal as e:
            if e.code != code:
                f.append(f"[{code}] refused with {e.code}")
            return
        except Exception as e:
            f.append(f"[{code}] non-refusal {type(e).__name__}: {e}")
            return
        f.append(f"[{code}] accepted")

    total += 1
    try:
        verify_stratum_index(seal, receipt, calls, chis, T)
    except Exception as e:
        f.append(f"[clean verify] refused: {e}")

    # the item's required fixture: INDEX MISMATCH REFUSED — flip one sealed state
    tampered = seal.replace(b'"state":"AGREE-S"', b'"state":"AGREE-Z"', 1)
    expect("RECEIPT-MISMATCH",
           lambda: verify_stratum_index(tampered, receipt, calls, chis, T))
    t_receipt = hashlib.sha256(tampered).hexdigest()
    expect("INDEX-MISMATCH",
           lambda: verify_stratum_index(tampered, t_receipt, calls, chis, T))
    # divergent INPUTS against an honest seal also refuse
    calls2 = dict(calls, a=("Z", "Z"))
    expect("INDEX-MISMATCH",
           lambda: verify_stratum_index(seal, receipt, calls2, chis, T))
    chis2 = [("a", 2.0)] + chis[1:]
    expect("INDEX-MISMATCH",
           lambda: verify_stratum_index(seal, receipt, calls, chis2, T))
    expect("SEAL-TAG-MISMATCH",
           lambda: verify_stratum_index(seal, receipt, calls, chis,
                                        {"tag": "other",
                                         "schema_digest": "5" * 64}))
    expect("SCHEMA-DIGEST-MISMATCH",
           lambda: verify_stratum_index(seal, receipt, calls, chis,
                                        {"tag": "stratum-index-TEST",
                                         "schema_digest": "6" * 64}))
    expect("RECEIPT-MISMATCH",
           lambda: verify_stratum_index(seal, "0" * 64, calls, chis, T))
    expect("SEAL-MALFORMED",
           lambda: verify_stratum_index("not-bytes", receipt, calls, chis, T))
    bad = b"NMPR1:stratum-index-TEST:{not json"
    expect("SEAL-MALFORMED",
           lambda: verify_stratum_index(bad, hashlib.sha256(bad).hexdigest(),
                                        calls, chis, T))
    expect("OBJECT-SET-MISMATCH",
           lambda: recompute_index(dict(calls, extra=("S", "S")), chis))
    # cross-implementation agreement: the two independent derivations agree on
    # the clean input (their divergence anywhere is the refusal working)
    total += 1
    if _canon(recompute_index(calls, chis)) != \
            _canon(sip.build_index(calls, chis)):
        f.append("independent recomputation diverges from the producer on "
                 "clean input — one implementation has drifted")
    return f, total


if __name__ == "__main__":
    fails, total = fixtures()
    for x in fails:
        print("FIXTURE FAIL:", x)
    print(f"stratum index verifier fixtures: {total - len(fails)}/{total} green")
    sys.exit(1 if fails else 0)
