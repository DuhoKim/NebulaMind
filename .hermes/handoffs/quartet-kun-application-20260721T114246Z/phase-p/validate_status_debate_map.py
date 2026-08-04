#!/usr/bin/env python3
"""Validate status_debate_map_v1.json against Contract v1 (docs-only, read-only).

Enforces STATUS_DEBATE_MAP_GATE_PROPOSAL.md §8 acceptance:
  - coverage: entries_referenced == entry_count == 16, unmapped == []
  - enum conformance: axis.status in certainty_level; counterevidence.relation in
    {contradicts, qualifies, same_axis}; epistemic_caps.ceiling_modality in modality
  - provenance: every entry_id / target_entry_id resolves to a real ledger entry;
    every span_id resolves to a real stance-matrix span
  - counterevidence preserved: every ledger link of type contradicts/qualifies is
    present in some axis's counterevidence[] (nothing dropped)
  - safety: this validator writes ONE report file and nothing else; asserts the
    all-zero side-effect block.

Exit 0 on PASS, 1 on FAIL. Writes status_debate_map_v1_validation.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTRACT = HERE.parents[3] / "docs" / "claim_ledger_contract_v1_agn_20260703T0830Z"
MAP = HERE / "status_debate_map_v1.json"
LEDGER = CONTRACT / "artifacts" / "claim_status_ledger.jsonl"
STANCE = CONTRACT / "artifacts" / "claim_source_stance_matrix.jsonl"
ENUMS = CONTRACT / "artifacts" / "ledger_enums.json"
REPORT = HERE / "status_debate_map_v1_validation.json"

CE_RELATIONS = {"contradicts", "qualifies", "same_axis"}
PRESERVE_LINK_TYPES = {"contradicts", "qualifies"}


def load_jsonl(p: Path) -> list[dict]:
    return [json.loads(line) for line in p.read_text().splitlines() if line.strip()]


def main() -> int:
    doc = json.loads(MAP.read_text())
    ledger = {e["entry_id"]: e for e in load_jsonl(LEDGER)}
    stance_rows = load_jsonl(STANCE)
    enums = json.loads(ENUMS.read_text())
    certainty_enum = set(enums["certainty_level"])
    modality_enum = set(enums["modality"])
    valid_span_ids = {r["span_id"] for r in stance_rows}

    errors: list[str] = []

    # coverage
    referenced = sorted({e for ax in doc["axes"] for e in ax["member_entries"]})
    if doc["coverage"]["entry_count"] != len(ledger):
        errors.append(f"coverage.entry_count {doc['coverage']['entry_count']} != ledger {len(ledger)}")
    if len(referenced) != len(ledger):
        errors.append(f"entries_referenced {len(referenced)} != ledger {len(ledger)}")
    unmapped = sorted(set(ledger) - set(referenced))
    if unmapped:
        errors.append(f"unmapped entries: {unmapped}")

    # per-axis checks
    for ax in doc["axes"]:
        name = ax["axis"]
        if ax["status"] not in certainty_enum:
            errors.append(f"[{name}] status '{ax['status']}' not in certainty_level enum")
        for m in ax["member_entries"]:
            if m not in ledger:
                errors.append(f"[{name}] member_entry '{m}' not in ledger")
        for ce in ax["counterevidence"]:
            if ce["relation"] not in CE_RELATIONS:
                errors.append(f"[{name}] counterevidence.relation '{ce['relation']}' invalid")
            if ce["entry_id"] not in ledger:
                errors.append(f"[{name}] counterevidence.entry_id '{ce['entry_id']}' not in ledger")
            if ce.get("target_entry_id") and ce["target_entry_id"] not in ledger:
                errors.append(f"[{name}] counterevidence.target_entry_id '{ce['target_entry_id']}' not in ledger")
            for sid in ce.get("span_ids", []):
                if sid not in valid_span_ids:
                    errors.append(f"[{name}] span_id '{sid}' not in stance matrix")
        for cap in ax["epistemic_caps"]:
            if cap["entry_id"] not in ledger:
                errors.append(f"[{name}] epistemic_caps.entry_id '{cap['entry_id']}' not in ledger")
            if cap["ceiling_modality"] not in modality_enum:
                errors.append(f"[{name}] ceiling_modality '{cap['ceiling_modality']}' not in modality enum")

    # counterevidence preservation: every ledger contradicts/qualifies link present
    map_links = {(ce["entry_id"], ce["relation"], ce.get("target_entry_id"))
                 for ax in doc["axes"] for ce in ax["counterevidence"]}
    for eid, e in ledger.items():
        for link in e.get("links", []):
            if link.get("type") in PRESERVE_LINK_TYPES:
                key = (eid, link["type"], link.get("entry_id"))
                if key not in map_links:
                    errors.append(f"ledger link dropped: {key}")

    status = "PASS" if not errors else "FAIL"
    report = {
        "marker": "CLAIM_STATUS_DEBATE_MAP_V1_VALIDATION_20260722",
        "validates": "status_debate_map_v1.json",
        "source_contract": doc["source_contract"],
        "status": status,
        "counts": {
            "axes": len(doc["axes"]),
            "entry_count": len(ledger),
            "entries_referenced": len(referenced),
            "unmapped": len(unmapped),
            "counterevidence_items": sum(len(ax["counterevidence"]) for ax in doc["axes"]),
            "epistemic_caps": sum(len(ax["epistemic_caps"]) for ax in doc["axes"]),
        },
        "errors": errors,
        "safety": {
            "db_writes": 0, "sql_mutations": 0, "migrations": 0, "git_writes": 0,
            "deploy_restart": 0, "product_publish": 0, "galaxy_prose_draft": 0,
            "exact_diff_packet": 0, "secrets_access": 0, "network": 0,
            "files_written": 1,  # this report only
        },
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"{status}: {len(errors)} error(s). report -> {REPORT.name}")
    for e in errors:
        print("  -", e)
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
