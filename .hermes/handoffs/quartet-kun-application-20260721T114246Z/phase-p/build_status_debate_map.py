#!/usr/bin/env python3
"""Build the docs-only status/debate map v1 from Claim Ledger Contract v1.

G6 gate (docs-only). Pure function of Contract v1: reads the frozen 16-entry
ledger, the 4-axis seed, and the stance matrix, and emits
status_debate_map_v1.json. Writes NOTHING except that one JSON file. No DB, no
git, no network, no product mutation, no prose. Contract v1 is read-only.

Derivation rules (from STATUS_DEBATE_MAP_GATE_PROPOSAL.md §6):
  1. Axis membership = seed axes + three links-justified G6-A attachments.
  2. Axis status  = a certainty_level enum value (off-enum seed strings mapped).
  3. counterevidence[] = every member entry's links of type
     contradicts/qualifies/same_axis, with backing span_ids from the stance
     matrix (contradicts->contradicts spans, qualifies->qualifies spans,
     same_axis->[] positional).
  4. epistemic_caps[] = member entries with epistemic_type single_case/simulation.
  5. reader_guard = copied verbatim from the seed.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

CONTRACT = Path(__file__).resolve().parents[4] / "docs" / "claim_ledger_contract_v1_agn_20260703T0830Z"
LEDGER = CONTRACT / "artifacts" / "claim_status_ledger.jsonl"
SEED = CONTRACT / "artifacts" / "status_debate_map_seed.json"
STANCE = CONTRACT / "artifacts" / "claim_source_stance_matrix.jsonl"
OUT = Path(__file__).resolve().parent / "status_debate_map_v1.json"

# G6-B: seed status strings that are not in the certainty_level enum -> nearest enum.
STATUS_ENUM_FIX = {"widely_supported_scoped": "widely_supported"}

# G6-A: the three orphaned entries, attached by their OWN ledger links (not by guess).
#   axis -> [(entry_id, justifying_link_type, justifying_target)]
ATTACHMENTS = {
    "mechanism": [
        ("clc_agn_008_star_formation_driven_outflow_counter", "contradicts", "clc_agn_001_ejective_mechanism_selected_systems"),
        ("clc_agn_006_central_kpc_depletion_local_qualifier", "same_axis", "clc_agn_001_ejective_mechanism_selected_systems"),
    ],
    "dominance_debate": [
        ("clc_agn_005_gas_retention_low_sfe_qualifier", "qualifies", "clc_agn2299_003_dominance_debate"),
    ],
}

CE_LINK_TYPES = {"contradicts", "qualifies", "same_axis"}
CAP_CEILINGS = {"single_case": "shows_can_occur", "simulation": "in_model_only"}


def load_jsonl(p: Path) -> list[dict]:
    return [json.loads(line) for line in p.read_text().splitlines() if line.strip()]


def main() -> None:
    ledger = {e["entry_id"]: e for e in load_jsonl(LEDGER)}
    seed = json.loads(SEED.read_text())
    stance_rows = load_jsonl(STANCE)

    # span_ids per (entry_id, stance) from the stance matrix
    spans_by_entry_stance: dict[tuple[str, str], list[str]] = {}
    for r in stance_rows:
        spans_by_entry_stance.setdefault((r["entry_id"], r["stance"]), []).append(r["span_id"])

    axes_out = []
    for seed_axis in seed["axes"]:
        name = seed_axis["axis"]
        members = list(seed_axis["ledger_entries"])
        # G6-A attachments
        for entry_id, _lt, _tgt in ATTACHMENTS.get(name, []):
            if entry_id not in members:
                members.append(entry_id)

        # G6-B status reconciliation to certainty_level enum
        raw_status = seed_axis["status"]
        status = STATUS_ENUM_FIX.get(raw_status, raw_status)

        # G6-C structured counterevidence from member entries' links
        counterevidence = []
        for entry_id in members:
            entry = ledger[entry_id]
            for link in entry.get("links", []):
                lt = link.get("type")
                if lt not in CE_LINK_TYPES:
                    continue
                if lt == "same_axis":
                    span_ids = []
                else:  # contradicts / qualifies -> the entry's spans of that stance
                    span_ids = sorted(spans_by_entry_stance.get((entry_id, lt), []))
                counterevidence.append({
                    "entry_id": entry_id,
                    "relation": lt,
                    "target_entry_id": link.get("entry_id"),
                    "span_ids": span_ids,
                })

        # epistemic caps from member entries
        epistemic_caps = []
        for entry_id in members:
            et = ledger[entry_id].get("epistemic_type")
            if et in CAP_CEILINGS:
                epistemic_caps.append({
                    "entry_id": entry_id,
                    "cap": et,
                    "ceiling_modality": CAP_CEILINGS[et],
                })

        axes_out.append({
            "axis": name,
            "status": status,
            "status_seed_original": raw_status if raw_status != status else None,
            "member_entries": members,
            "counterevidence": counterevidence,
            "epistemic_caps": epistemic_caps,
            "reader_guard": seed_axis["reader_guard"],  # verbatim
        })

    referenced = sorted({e for ax in axes_out for e in ax["member_entries"]})
    unmapped = sorted(set(ledger) - set(referenced))

    doc = {
        "marker": "CLAIM_STATUS_DEBATE_MAP_V1_AGN_20260722",
        "as_of": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "boundary": "Docs-only status/debate map over Contract v1; prose remains blocked; no product mutation.",
        "source_contract": "claim_ledger_contract_v1_agn_20260703T0830Z",
        "derived_from_seed": "artifacts/status_debate_map_seed.json",
        "vocabulary_bridge": {
            "note": "Backend _STATUS_SEMANTIC_CAPS reconciliation, documentation only — no code change in this gate.",
            "mixed_debated": {"ledger": "modality value + certainty_level actively_debated", "backend_cap": "debated", "overlap": "exact"},
            "model_bounded": {"ledger": "no direct value; nearest = modality in_model_only / reported_only, certainty_level contradicted_or_model_dependent", "backend_cap": "reported", "overlap": "none — naming mismatch flagged"},
        },
        "axes": axes_out,
        "coverage": {
            "entry_count": len(ledger),
            "entries_referenced": len(referenced),
            "unmapped": unmapped,
        },
    }
    # drop null status_seed_original for cleanliness
    for ax in doc["axes"]:
        if ax["status_seed_original"] is None:
            del ax["status_seed_original"]

    OUT.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"wrote {OUT}")
    print(f"axes={len(axes_out)} entries_referenced={len(referenced)}/{len(ledger)} unmapped={unmapped}")


if __name__ == "__main__":
    main()
