#!/usr/bin/env python3
"""Strict successor receipt envelope.

Frozen V134 quotation: ``SLOT_SCHEMA['BS-3g'] is exactly these twenty fields,
no more and no fewer: mask_sha256 · calibration_sha256 ·
perturbation_manifest_sha256 · kernel_sha256 · estimator_sha256 ·
verifier_sha256 · mapping_id · gamma_hat · sigma_gamma · gamma_bound ·
invariance_outcome · n_perturbations · n_draws · draw_generator_id ·
draw_master_seed · draw_verdict_digest · baseline_verdict · delta_gamma_max ·
counterfactual_path_sha256 · replay_harness_sha256.``

This layer deliberately carries no frozen-v9 slot.  It returns an envelope; it
does not write one to a receipt store.
"""
import hashlib
import json
from pathlib import Path

SLOT_SCHEMA_SUCCESSOR = {
    # V136 fills BS-2a as design identities only.  The later BS-2f execution
    # receipt, not this envelope, carries the realised catalogue partition.
    "BS-2a": (
        "quality_gate_sha256", "flux_ivar_r_gt", "psfsize_r_lt",
        "nobs_r_ge", "evidence_schema_digest", "verifier_digest",
        "classification",
    ),
    # Frozen V134 §7/§11 requires the BS-2v canonical authenticated receipt to
    # bind exactly these converter-produced fields.  Closure is recomputed by
    # gates/bs2v_void_converter.py rather than accepted as producer testimony.
    "BS-2v": (
        "registry_digest", "converter_sha256", "normative_ids",
        "exercised_ids", "per_id", "classifications",
    ),
    "BS-3g": (
        "mask_sha256", "calibration_sha256", "perturbation_manifest_sha256",
        "kernel_sha256", "estimator_sha256", "verifier_sha256", "mapping_id",
        "gamma_hat", "sigma_gamma", "gamma_bound", "invariance_outcome",
        "n_perturbations", "n_draws", "draw_generator_id", "draw_master_seed",
        "draw_verdict_digest", "baseline_verdict", "delta_gamma_max",
        "counterfactual_path_sha256", "replay_harness_sha256",
    )
}

SCHEMA_IDS = {
    "BS-2a": "BS2A-V1",
    "BS-2v": "BS2V-V1",
    "BS-3g": "BS3G-V1",
}

CODES = {
    "RS01": "slot is outside the successor schema",
    "RS02": "receipt contains an empty payload",
    "RS03": "receipt field set is missing required fields",
    "RS04": "receipt field set contains extra fields",
    "RS05": "pinned successor schema entry changed",
}


class ReceiptRefusal(RuntimeError):
    def __init__(self, code, detail):
        self.code = code
        super().__init__(f"[{code}] {CODES[code]}: {detail}")


def _canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def schema_entry_digest(slot):
    """Digest one canonical successor schema entry, including field order."""
    if slot not in SLOT_SCHEMA_SUCCESSOR:
        raise ReceiptRefusal("RS01", repr(slot))
    entry = {"slot": slot, "schema": SCHEMA_IDS[slot],
             "fields": list(SLOT_SCHEMA_SUCCESSOR[slot])}
    return hashlib.sha256(_canonical(entry)).hexdigest()


def schema_entry_digests():
    """Return per-entry digests for every successor-layer schema."""
    return {slot: schema_entry_digest(slot) for slot in SLOT_SCHEMA_SUCCESSOR}


def assert_entries_preserved(pinned):
    """Refuse if any pinned successor-layer entry is absent or changed."""
    for slot, digest in pinned.items():
        if slot not in SLOT_SCHEMA_SUCCESSOR:
            raise ReceiptRefusal("RS05", f"{slot!r} is absent")
        actual = schema_entry_digest(slot)
        if actual != digest:
            raise ReceiptRefusal(
                "RS05", f"{slot!r}: pinned {digest}, actual {actual}")


def receipt_strict(slot, fields):
    """Validate exactness and digest a canonical-JSON successor envelope."""
    if slot not in SLOT_SCHEMA_SUCCESSOR:
        raise ReceiptRefusal("RS01", repr(slot))
    want = set(SLOT_SCHEMA_SUCCESSOR[slot])
    got = set(fields)
    empty = sorted(k for k, v in fields.items() if v is None or v == "" or v == b"")
    if empty:
        raise ReceiptRefusal("RS02", repr(empty))
    missing, extra = sorted(want - got), sorted(got - want)
    if missing:
        raise ReceiptRefusal("RS03", repr(missing))
    if extra:
        raise ReceiptRefusal("RS04", repr(extra))
    body = {k: fields[k] for k in SLOT_SCHEMA_SUCCESSOR[slot]}
    body_sha = hashlib.sha256(_canonical(body)).hexdigest()
    core = {"slot": slot, "schema": SCHEMA_IDS[slot], "body": body,
            "body_sha256": body_sha}
    return {**core, "envelope_sha256": hashlib.sha256(_canonical(core)).hexdigest()}


def _fields():
    return {k: (i + 1) for i, k in enumerate(SLOT_SCHEMA_SUCCESSOR["BS-3g"])}


def fixtures():
    passed = 0
    f = _fields()
    r = receipt_strict("BS-3g", f)
    assert r["slot"] == "BS-3g"; passed += 1
    for code, slot, body in (
        ("RS03", "BS-3g", {k: v for k, v in f.items() if k != "mask_sha256"}),
        ("RS04", "BS-3g", {**f, "extra": 1}),
        ("RS02", "BS-3g", {**f, "mapping_id": ""}),
        ("RS01", "BS-7p", f),
    ):
        try:
            receipt_strict(slot, body)
            raise AssertionError(f"{code} did not refuse")
        except ReceiptRefusal as e:
            assert e.code == code, (code, e.code)
        passed += 1
    assert receipt_strict("BS-3g", f) == receipt_strict("BS-3g", dict(reversed(list(f.items()))))
    passed += 1
    candidate_dir = Path(__file__).resolve().parent / "classp_candidates"
    v_candidate = json.loads((candidate_dir / "BS-2v.json").read_text())
    assert receipt_strict("BS-2v", v_candidate["body"]) == v_candidate
    passed += 1
    a_candidate = json.loads((candidate_dir / "BS-2a.json").read_text())
    assert receipt_strict("BS-2a", a_candidate["body"]) == a_candidate
    passed += 1
    pinned = schema_entry_digests()
    noop_namespace = {"__name__": "receipt_strict_noop",
                      "__file__": str(Path(__file__).resolve())}
    source = Path(__file__).read_text() + "\n# no-op file edit\n"
    exec(compile(source, __file__, "exec"), noop_namespace)
    assert noop_namespace["schema_entry_digests"]() == pinned
    passed += 1
    original = SLOT_SCHEMA_SUCCESSOR["BS-2v"]
    try:
        SLOT_SCHEMA_SUCCESSOR["BS-2v"] = original + ("mutated_field",)
        try:
            assert_entries_preserved({"BS-2v": pinned["BS-2v"]})
            raise AssertionError("mutated BS2V-V1 entry did not refuse")
        except ReceiptRefusal as e:
            assert e.code == "RS05" and "BS-2v" in str(e)
    finally:
        SLOT_SCHEMA_SUCCESSOR["BS-2v"] = original
    passed += 1
    return passed


if __name__ == "__main__":
    n = fixtures()
    print(f"receipt_strict fixtures: {n}/{n} PASS")
