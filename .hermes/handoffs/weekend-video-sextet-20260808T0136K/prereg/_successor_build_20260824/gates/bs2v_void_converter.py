#!/usr/bin/env python3
"""bs2v_void_converter — §11 build item ("`VOID` conversion", a pre-BS-6
dependency): the converter that handles EVERY enumerated void antecedent, its
canonical authenticated receipt, and the gate that compares the converter's
emitted and exercised IDs against the pinned §7.1 registry's contents — missing,
duplicate, extra, or non-VOID conversion for any ID fails the gate.

THE REGISTRY IS NOT DUPLICATED HERE. The canonical closed antecedent registry IS
§7.1's row table, extracted and digested through the ONE shipped tool
(tools/void_registry.py's extract/canonical/digest) — a second registry in this
file would be the divergent-copy defect, and the §7.1 checker already proves the
table well-formed and NAME-complete. The converter is total over exactly that
closed set: every enumerated ID converts to the VOID result class carrying its
registry row (source, phase, failure effect) verbatim; an ID outside the set
refuses. The receipt schema is the item's own list, verbatim fields:
(registry_digest, converter_sha256, normative_ids ordered, exercised_ids,
per_id rows, result classifications) — closure is RECOMPUTED by the gate from
those fields, never asserted by the producer.

The receipt's domain tag uses an explicitly TEST-scoped token pattern pending
BS-2k's kind provisioning, the same discipline as the BS-SI schema commitment."""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/tools")
import void_registry as vr  # noqa: E402

RECEIPT_TAG = "bs2v-receipt-TEST"  # real token binds at BS-2k provisioning


class VoidConvertRefusal(ValueError):
    def __init__(self, code, msg):
        self.code = code
        super().__init__(f"{code}: {msg}")


def _r(code, msg):
    raise VoidConvertRefusal(code, msg)


def _canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False)


def latest_draft(base=HERE.parent):
    ds = []
    for p in base.glob("PREREG_SUCCESSOR_DRAFT_V*_2026*.md"):
        m = re.search(r"_V(\d+)_", p.name)
        if m:
            ds.append((int(m.group(1)), p))
    if not ds:
        _r("NO-DRAFT", "no draft found")
    return sorted(ds)[-1][1]


def load_registry(draft_text):
    rows = vr.extract(draft_text)
    if not rows:
        _r("REGISTRY-ABSENT", "§7.1 holds no rows")
    ids = [r[0] for r in rows]
    if len(set(ids)) != len(ids):
        _r("REGISTRY-DUPLICATE", "duplicate antecedent ID in §7.1")
    return {r[0]: {"id": r[0], "source": r[1], "phase": r[2],
                   "failure_effect": r[3]} for r in rows}, ids


def convert(antecedent_id, registry):
    """Total over the closed set, refusing outside it: every enumerated VOID
    antecedent converts to the VOID result class carrying its registry row."""
    if antecedent_id not in registry:
        _r("UNKNOWN-ANTECEDENT",
           f"{antecedent_id!r} is not in the §7.1 closed registry")
    row = registry[antecedent_id]
    if row["failure_effect"] != "VOID":
        _r("NON-VOID-EFFECT",
           f"{antecedent_id} carries effect {row['failure_effect']!r}; the "
           "converter emits VOID conversions only")
    return {"classification": "VOID", "id": row["id"], "source": row["source"],
            "phase": row["phase"], "failure_effect": row["failure_effect"]}


def exercise_all(registry, ids):
    return [convert(i, registry) for i in ids]


def build_receipt(draft_text):
    """The canonical authenticated receipt: the item's fields verbatim, sha-bound
    under the domain tag. Closure facts are the gate's to recompute."""
    registry, ids = load_registry(draft_text)
    conversions = exercise_all(registry, ids)
    body = {
        "registry_digest": vr.digest(vr.extract(draft_text)),
        "converter_sha256": hashlib.sha256(
            Path(__file__).read_bytes()).hexdigest(),
        "normative_ids": ids,
        "exercised_ids": [c["id"] for c in conversions],
        "per_id": {c["id"]: {"source": c["source"], "phase": c["phase"],
                             "failure_effect": c["failure_effect"]}
                   for c in conversions},
        "classifications": {c["id"]: c["classification"] for c in conversions},
    }
    seal = b"NMPR1:" + RECEIPT_TAG.encode() + b":" + _canon(body).encode()
    return body, hashlib.sha256(seal).hexdigest()


def gate(body, receipt_sha, draft_text):
    """Recomputes everything: authentication, the pinned §7.1 digest, ID closure
    both ways, uniqueness, per-ID row equality, all-VOID classification.
    Missing, duplicate, extra, or non-VOID conversion for any ID fails."""
    seal = b"NMPR1:" + RECEIPT_TAG.encode() + b":" + _canon(body).encode()
    if hashlib.sha256(seal).hexdigest() != receipt_sha:
        _r("RECEIPT-UNAUTHENTICATED",
           "the receipt sha does not bind these bytes")
    rows = vr.extract(draft_text)
    if body["registry_digest"] != vr.digest(rows):
        _r("REGISTRY-DIGEST-MISMATCH",
           "the receipt's registry digest is not the pinned §7.1 digest")
    want_ids = [r[0] for r in rows]
    if body["normative_ids"] != want_ids:
        _r("NORMATIVE-IDS-DRIFT",
           "the receipt's ordered normative IDs are not §7.1's rows in "
           "document order")
    ex = body["exercised_ids"]
    if len(set(ex)) != len(ex):
        _r("EXERCISED-DUPLICATE", "an ID was exercised twice in one receipt")
    missing = set(want_ids) - set(ex)
    if missing:
        _r("EXERCISED-MISSING", f"unexercised antecedents: {sorted(missing)[:4]}")
    extra = set(ex) - set(want_ids)
    if extra:
        _r("EXERCISED-EXTRA", f"alien antecedents: {sorted(extra)[:4]}")
    reg = {r[0]: r for r in rows}
    for i in want_ids:
        want = {"source": reg[i][1], "phase": reg[i][2],
                "failure_effect": reg[i][3]}
        if body["per_id"].get(i) != want:
            _r("PER-ID-ROW-DRIFT", f"{i}: receipt row differs from §7.1")
        if body["classifications"].get(i) != "VOID":
            _r("NON-VOID-CONVERSION",
               f"{i} classified {body['classifications'].get(i)!r}")
    return True


# ------------------------------------------------------------------ fixtures
def fixtures():
    f = []
    total = 0
    text = latest_draft().read_text()

    def expect(code, thunk):
        nonlocal total
        total += 1
        try:
            thunk()
        except VoidConvertRefusal as e:
            if e.code != code:
                f.append(f"[{code}] refused with {e.code}")
            return
        except Exception as e:
            f.append(f"[{code}] non-refusal {type(e).__name__}: {e}")
            return
        f.append(f"[{code}] accepted")

    registry, ids = load_registry(text)
    total += 1
    conv = exercise_all(registry, ids)
    if len(conv) != len(ids) or any(c["classification"] != "VOID" for c in conv):
        f.append("full exercise did not convert every enumerated antecedent")
    expect("UNKNOWN-ANTECEDENT", lambda: convert("VOID-99-ALIEN", registry))

    body, sha = build_receipt(text)
    total += 1
    gate(body, sha, text)
    total += 1
    b2, s2 = build_receipt(text)
    if s2 != sha:
        f.append("same draft, different receipt shas — not deterministic")

    def mut(**kw):
        b = json.loads(json.dumps(body))
        b.update(kw)
        seal = b"NMPR1:" + RECEIPT_TAG.encode() + b":" + _canon(b).encode()
        return b, hashlib.sha256(seal).hexdigest()

    expect("RECEIPT-UNAUTHENTICATED", lambda: gate(body, "0" * 64, text))
    expect("REGISTRY-DIGEST-MISMATCH",
           lambda: gate(*mut(registry_digest="1" * 64), text))
    expect("NORMATIVE-IDS-DRIFT",
           lambda: gate(*mut(normative_ids=list(reversed(body["normative_ids"]))),
                        text))
    expect("EXERCISED-MISSING",
           lambda: gate(*mut(exercised_ids=body["exercised_ids"][:-1]), text))
    expect("EXERCISED-EXTRA",
           lambda: gate(*mut(exercised_ids=body["exercised_ids"]
                             + ["VOID-99-ALIEN"]), text))
    expect("EXERCISED-DUPLICATE",
           lambda: gate(*mut(exercised_ids=body["exercised_ids"]
                             + [body["exercised_ids"][0]]), text))
    pid = json.loads(json.dumps(body["per_id"]))
    first = body["normative_ids"][0]
    pid[first]["phase"] = "Never"
    expect("PER-ID-ROW-DRIFT", lambda: gate(*mut(per_id=pid), text))
    cls = dict(body["classifications"])
    cls[first] = "HALT"
    expect("NON-VOID-CONVERSION", lambda: gate(*mut(classifications=cls), text))
    return f, total


if __name__ == "__main__":
    fails, total = fixtures()
    for x in fails:
        print("FIXTURE FAIL:", x)
    print(f"bs2v void converter fixtures: {total - len(fails)}/{total} green")
    sys.exit(1 if fails else 0)
