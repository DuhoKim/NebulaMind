#!/usr/bin/env python3
"""Offline builders for the 2026-09-01 unbuilt Class-P candidates.

This script reads only frozen lane artifacts.  It performs no transport, image
access, chi measurement, or store writes; its only outputs are candidate JSONs.
"""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "run" / "classp_candidates"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def emit(name, obj):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{name}.json").write_text(
        json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    )


def bs2v():
    conv = load("bs2v_void_converter", "gates/bs2v_void_converter.py")
    strict = load("receipt_strict", "run/receipt_strict.py")
    text = (ROOT / "PREREG_SUCCESSOR_DRAFT_V134_20260831.md").read_text()
    body, seal = conv.build_receipt(text)
    # First validate the converter's canonical authenticated body on its own
    # terms, then construct the required successor-layer SLOT RECEIPT.  Frozen
    # v9 is intentionally not used: BS-2v is absent from its SLOT_SCHEMA.
    assert conv.gate(body, seal, text)
    candidate = strict.receipt_strict("BS-2v", body)
    assert candidate == strict.receipt_strict("BS-2v", dict(reversed(list(body.items()))))
    assert conv.gate(candidate["body"], seal, text)
    emit("BS-2v", candidate)


def bs1b():
    v9 = load("successor_ref_v9", "ref/successor_ref_v9.py")
    cfg = v9.BRANCH_CONFIG["B_DR10_1"]
    provenance = {
        "branch": "B_DR10_1",
        "branch_config_sha256": v9.digest(json.dumps(cfg, sort_keys=True).encode()),
        "positions_query_sha256": sha("acquire/positions_query.adql"),
        "positions_receipts_sha256": sha("acquire/positions_receipts.json"),
        "positions_output_sha256": json.loads((ROOT / "acquire/positions_receipts.json").read_text())["output_sha256"],
        "quality_query_sha256": sha("acquire/quality_query.adql"),
        "quality_receipts_sha256": sha("acquire/quality_receipts.json"),
        "quality_output_sha256": json.loads((ROOT / "acquire/quality_receipts.json").read_text())["output_sha256"],
    }
    fields = {
        "photoz_product": cfg["photoz_product"].encode(),
        "columns": b"ls_id,release,brickid,objid,z_phot_median",
        "join_keys": b"ls_id,release,brickid,objid",
        "provenance": json.dumps(provenance, sort_keys=True, separators=(",", ":")).encode(),
    }
    candidate = v9.receipt("BS-1b", fields)
    candidate["fields"] = {k: v.decode() for k, v in fields.items()}
    emit("BS-1b", candidate)


if __name__ == "__main__":
    bs2v()
    bs1b()
