#!/usr/bin/env python3
"""Build a local-only crosswalk from historical research-topic candidates to the 9 active AAS pilot papers.

Safety: read-only inputs under frontend public report backups; writes only under the overnight autopilot root.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
OVERNIGHT_ROOT = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708"
FRONTEND_RT_ROOT = REPO / "frontend/public/agent-reports/wiki-method-results/galaxy-evolution"

METHODS = {
    "M1": {
        "method_dir": "packet-gated-paper-to-wiki-reconciliation",
        "label": "M1 / packet-gated-paper-to-wiki-reconciliation",
        "active_prefix": "m1",
    },
    "M2": {
        "method_dir": "source-first-paper-adjudication",
        "label": "M2 / source-first-paper-adjudication",
        "active_prefix": "m2",
    },
    "M3": {
        "method_dir": "debate-map-to-wiki-rebuild",
        "label": "M3 / debate-map-to-wiki-rebuild",
        "active_prefix": "m3",
    },
}

STAGES = {
    "active_current": "research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json",
    "historical_seed": "research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topic-map-20260708T090359Z.json",
    "pre_professional": "research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topic-map-20260708T090359Z.json",
}

# Active slugs are the nine public-card paper identities, not every historical candidate.
ACTIVE_SLUGS = {
    "M1:RP-1": "m1_rp1_sdss_agn_sfr",
    "M1:RP-2": "m1_rp2_environment_quenching",
    "M1:RP-3": "m1_rp3_maintenance_heating",
    "M2:P1": "m2_p1_outflow_escape_recycling",
    "M2:P2": "m2_p2_radio_jet_environment",
    "M2:P3": "m2_p3_feedback_transition_mass",
    "M3:P1": "m3_p1_multiphase_census",
    "M3:P2": "m3_p2_gas_depletion_efficiency",
    "M3:P3": "m3_p3_simulation_validation",
}

# Curated crosswalk from historical/pre-professional records to active papers or future extensions.
# The titles are verified mechanically from the source JSON files; this mapping supplies the judgment.
MAPPING: Dict[str, Dict[str, Any]] = {
    # M1 earliest seed topics.
    "M1|historical_seed|M1-RT-01": {
        "status": "PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION",
        "targets": ["m1_rp1_sdss_agn_sfr"],
        "future_extension": "Evidence-bearing audit for claim 2929 and controls beyond the SDSS optical association pilot.",
        "notes": "The active RP-1 paper covers the AGN/sSFR association part, not the full source-adjudication audit of attached evidence.",
    },
    "M1|historical_seed|M1-RT-02": {
        "status": "ACTIVE_PAPER",
        "targets": ["m1_rp2_environment_quenching"],
        "future_extension": "Group/halo central-satellite data and environment systematics needed before physical environmental-quenching claims.",
        "notes": "Directly became the density-proxy environmental-quenching pilot, with the SDSS proxy guardrail preserved.",
    },
    "M1|historical_seed|M1-RT-03": {
        "status": "ACTIVE_PAPER",
        "targets": ["m1_rp3_maintenance_heating"],
        "future_extension": "X-ray cavity/cooling luminosity plus radio duty-cycle data needed for real maintenance-heating tests.",
        "notes": "Directly became the optical-AGN denominator for maintenance-heating follow-up.",
    },
    "M1|historical_seed|M1-RT-04": {
        "status": "FUTURE_METHODS_EXTENSION",
        "targets": [],
        "future_extension": "Unbound-claim prioritization packet for 27 claims before any additional paper generation.",
        "notes": "Evidence-accounting topic; intentionally not an astrophysical AAS pilot paper.",
    },
    "M1|historical_seed|M1-RT-05": {
        "status": "FUTURE_METHODS_EXTENSION",
        "targets": [],
        "future_extension": "Evidence-empty section recovery plan with source requirements and no-prose gate.",
        "notes": "Narrative-only section repair remains a separate source/corpus task.",
    },
    "M1|historical_seed|M1-RT-06": {
        "status": "FUTURE_METHODS_EXTENSION",
        "targets": [],
        "future_extension": "Malformed-link and unresolved-title provenance repair audit.",
        "notes": "Data-quality/provenance repair, not a survey-analysis paper.",
    },
    "M1|historical_seed|M1-RT-07": {
        "status": "FUTURE_METHODS_EXTENSION",
        "targets": [],
        "future_extension": "Deduplicated source/paper count audit before trust promotion.",
        "notes": "Rows-vs-papers accounting remains a corpus/readiness check.",
    },
    "M1|historical_seed|M1-RT-08": {
        "status": "FUTURE_METHODS_EXTENSION",
        "targets": [],
        "future_extension": "Pre-registered evidence thresholds for upgrading AGN-feedback claim status.",
        "notes": "Acceptance criteria are a gate artifact, not a completed paper.",
    },
    # M1 journal/professional intermediate proposals.
    "M1|pre_professional|RP-1": {
        "status": "ACTIVE_PAPER",
        "targets": ["m1_rp1_sdss_agn_sfr"],
        "future_extension": "Causal test remains future; current RP-1 is association-only and needs morphology/environment/gas/duty-cycle controls.",
        "notes": "Current wording was demoted from causal test to observational constraints/SDSS association.",
    },
    "M1|pre_professional|RP-2": {
        "status": "ACTIVE_PAPER",
        "targets": ["m1_rp2_environment_quenching"],
        "future_extension": "Halo/group catalog and central-satellite follow-up.",
        "notes": "Narrowed to density-proxy pilot.",
    },
    "M1|pre_professional|RP-3": {
        "status": "ACTIVE_PAPER",
        "targets": ["m1_rp3_maintenance_heating"],
        "future_extension": "Observed heating-vs-cooling balance remains future X-ray/radio work.",
        "notes": "Narrowed to optical-AGN denominator in massive hosts.",
    },
    "M1|pre_professional|RP-4": {
        "status": "FUTURE_METHODS_EXTENSION",
        "targets": [],
        "future_extension": "Prioritized evidence-gap programme for narrative-only sections.",
        "notes": "Omitted from the active nine; should be a methods/source packet if resumed.",
    },
    "M1|pre_professional|RP-5": {
        "status": "FUTURE_METHODS_EXTENSION",
        "targets": [],
        "future_extension": "Evidence-accounting robustness appendix for row/paper/citation treatment.",
        "notes": "Guardrail for future papers, not an astrophysical pilot.",
    },
    "M1|pre_professional|RP-6": {
        "status": "FUTURE_METHODS_EXTENSION",
        "targets": [],
        "future_extension": "Pre-registered AGN-feedback acceptance criteria before any public claim upgrade.",
        "notes": "Useful gate artifact; not completed by the active nine.",
    },
    # M2 earliest seed topics.
    "M2|historical_seed|T1": {
        "status": "FUTURE_METHODS_EXTENSION",
        "targets": [],
        "future_extension": "Cite-unmatched evidence to product-citation mapping; would require separate DB/page gate before product use.",
        "notes": "Traceability task, not a physical paper.",
    },
    "M2|historical_seed|T2": {
        "status": "PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION",
        "targets": ["m2_p1_outflow_escape_recycling", "m1_rp1_sdss_agn_sfr"],
        "future_extension": "Full single-anchor sensitivity note for claim 2943 and independent primary outflow-support acquisition.",
        "notes": "Outflow permanence/recycling was folded into M2 P1; source-strength sensitivity remains future evidence work.",
    },
    "M2|historical_seed|T3": {
        "status": "PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION",
        "targets": ["m1_rp3_maintenance_heating"],
        "future_extension": "Real observational maintenance-heating path using X-ray cavities/cooling luminosity/radio duty cycles.",
        "notes": "Covered only as optical massive-host denominator; no heating measurement.",
    },
    "M2|historical_seed|T4": {
        "status": "ACTIVE_PAPER",
        "targets": ["m2_p2_radio_jet_environment"],
        "future_extension": "Radio/X-ray jet coupling data required for physical efficiency estimates.",
        "notes": "Became the radio-jet environment proposal, narrowed to SDSS environment proxy overnight.",
    },
    "M2|historical_seed|T5": {
        "status": "FUTURE_SCIENCE_EXTENSION",
        "targets": ["m3_p1_multiphase_census"],
        "future_extension": "M51-generalization sample with PHANGS/MUSE/ALMA-style resolved diagnostics.",
        "notes": "Only broadly adjacent to M3 P1; M51 representativeness was not completed by the active nine.",
    },
    "M2|historical_seed|T6": {
        "status": "FUTURE_SCIENCE_EXTENSION",
        "targets": [],
        "future_extension": "Positive/compressive AGN-feedback claim audit and multi-galaxy resolved sample.",
        "notes": "Not in the active nine; should remain a caution until additional evidence exists.",
    },
    "M2|historical_seed|T7": {
        "status": "FUTURE_METHODS_EXTENSION",
        "targets": [],
        "future_extension": "Rejected-position reconsideration criteria and audit trail.",
        "notes": "Source-status governance topic.",
    },
    "M2|historical_seed|T8": {
        "status": "ACTIVE_PAPER",
        "targets": ["m2_p3_feedback_transition_mass"],
        "future_extension": "Direct stellar/AGN feedback budget data, halo mass, gas fractions, and redshift evolution.",
        "notes": "Became the mass-transition optical incidence/quenching pilot.",
    },
    "M2|historical_seed|T9": {
        "status": "ACTIVE_PAPER",
        "targets": ["m2_p1_outflow_escape_recycling"],
        "future_extension": "Resolved outflow velocities, escape speeds, CGM/recycling tracers.",
        "notes": "Became the escape-versus-recycling denominator proposal, but remains SDSS optical denominator only.",
    },
    "M2|historical_seed|T10": {
        "status": "FUTURE_METHODS_EXTENSION",
        "targets": [],
        "future_extension": "Full-text verification priority queue for abstract-only rows.",
        "notes": "A source-verification gate, not an AAS pilot paper.",
    },
    # M2 journal/professional intermediate proposals.
    "M2|pre_professional|P1": {
        "status": "ACTIVE_PAPER",
        "targets": ["m2_p1_outflow_escape_recycling"],
        "future_extension": "Escape-fraction measurement needs outflow kinematics and halo potentials.",
        "notes": "Direct active proposal; current artifact is denominator only.",
    },
    "M2|pre_professional|P2": {
        "status": "PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION",
        "targets": ["m1_rp3_maintenance_heating"],
        "future_extension": "Cavity enthalpy versus cooling luminosity duty-cycle paper.",
        "notes": "Maintenance-heating theme appears in active M1 RP-3, but the observational X-ray/radio test is omitted from active SDSS-only artifacts.",
    },
    "M2|pre_professional|P3": {
        "status": "ACTIVE_PAPER",
        "targets": ["m2_p2_radio_jet_environment"],
        "future_extension": "Radio jet power and gas-work calorimetry.",
        "notes": "Direct active proposal, narrowed to optical AGN fraction versus density proxy.",
    },
    "M2|pre_professional|P4": {
        "status": "FUTURE_SCIENCE_EXTENSION",
        "targets": ["m3_p1_multiphase_census"],
        "future_extension": "Resolved nearby-galaxy positive/negative feedback frequency study.",
        "notes": "M51-specific/positive-feedback topic remains outside the active nine except as a caution.",
    },
    "M2|pre_professional|P5": {
        "status": "ACTIVE_PAPER",
        "targets": ["m2_p3_feedback_transition_mass"],
        "future_extension": "Full gas/halo/black-hole-mass transition analysis.",
        "notes": "Direct active mass-transition pilot.",
    },
    "M2|pre_professional|P6": {
        "status": "FUTURE_METHODS_EXTENSION",
        "targets": [],
        "future_extension": "Citation-linking/full-text/reconsideration methods programme.",
        "notes": "Omitted methods programme, not one of the nine cards.",
    },
    # M3 earliest seed topics.
    "M3|historical_seed|t1": {
        "status": "PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION",
        "targets": ["m3_p1_multiphase_census", "m2_p1_outflow_escape_recycling"],
        "future_extension": "Mechanism-versus-prevalence decomposition with true outflow/multiphase data.",
        "notes": "Folded into common-denominator/outflow denominator work; prevalence remains emission-line/optical conditional.",
    },
    "M3|historical_seed|t2": {
        "status": "ACTIVE_PAPER",
        "targets": ["m3_p1_multiphase_census"],
        "future_extension": "CO/HI/neutral/radio/X-ray matched denominators for a true multiphase census.",
        "notes": "Direct active census proposal, narrowed to optical tracer thresholds.",
    },
    "M3|historical_seed|t3": {
        "status": "PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION",
        "targets": ["m1_rp1_sdss_agn_sfr", "m2_p3_feedback_transition_mass"],
        "future_extension": "Causal dominance decomposition including black-hole mass, morphology, halo/environment, gas, and non-AGN quenching channels.",
        "notes": "Only association/transition proxies exist in current papers; causal dominance remains future.",
    },
    "M3|historical_seed|t4": {
        "status": "ACTIVE_PAPER",
        "targets": ["m3_p2_gas_depletion_efficiency"],
        "future_extension": "Molecular/atomic gas masses and depletion-time measurements.",
        "notes": "Direct active gas-reservoir proposal, narrowed to optical denominator/H-alpha proxy.",
    },
    "M3|historical_seed|t5": {
        "status": "PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION",
        "targets": ["m1_rp3_maintenance_heating"],
        "future_extension": "Maintenance/preventive-heating observational status paper with X-ray/radio hot-halo data.",
        "notes": "Appears only as massive-host optical-AGN denominator in the active nine.",
    },
    "M3|historical_seed|t6": {
        "status": "ACTIVE_PAPER",
        "targets": ["m3_p3_simulation_validation"],
        "future_extension": "Forward-modeled simulation mocks through SDSS/IFU/CO/radio/X-ray selection.",
        "notes": "Direct active target-vector proposal; no model ranking performed.",
    },
    "M3|historical_seed|t7": {
        "status": "FUTURE_GUARDRAIL_NOT_PAPER",
        "targets": ["m1_rp2_environment_quenching", "m2_p3_feedback_transition_mass"],
        "future_extension": "Completeness audit for non-AGN quenching channels before AGN dominance language.",
        "notes": "Travels as a guardrail; not a completed active paper.",
    },
    "M3|historical_seed|t8": {
        "status": "FUTURE_SCIENCE_EXTENSION",
        "targets": [],
        "future_extension": "Halo, morphology, chemical, and reionization coverage-gap papers/packets.",
        "notes": "Outside active consolidated card set.",
    },
    "M3|historical_seed|t9": {
        "status": "FUTURE_METHODS_EXTENSION",
        "targets": [],
        "future_extension": "Unmatched-ID and PENDING_RECHECK provenance repair.",
        "notes": "Methods/provenance task outside the active nine.",
    },
    # M3 journal/professional intermediate proposals.
    "M3|pre_professional|p1": {
        "status": "PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION",
        "targets": ["m1_rp1_sdss_agn_sfr", "m2_p3_feedback_transition_mass"],
        "future_extension": "Causal AGN quenching decomposition beyond SDSS association.",
        "notes": "Current active artifacts do not isolate causal AGN contribution.",
    },
    "M3|pre_professional|p2": {
        "status": "ACTIVE_PAPER",
        "targets": ["m3_p1_multiphase_census"],
        "future_extension": "Tracer-resolved multiphase data beyond optical lines.",
        "notes": "Direct active proposal, current version optical-only.",
    },
    "M3|pre_professional|p3": {
        "status": "ACTIVE_PAPER",
        "targets": ["m3_p2_gas_depletion_efficiency"],
        "future_extension": "Gas fraction and SFE require CO/HI/dust gas measurements.",
        "notes": "Direct active proposal, current version optical denominator/H-alpha proxy.",
    },
    "M3|pre_professional|p4": {
        "status": "PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION",
        "targets": ["m1_rp3_maintenance_heating"],
        "future_extension": "Maintenance-heating duty-cycle analysis with X-ray/radio data.",
        "notes": "Only indirectly represented by M1 RP-3 denominator.",
    },
    "M3|pre_professional|p5": {
        "status": "ACTIVE_PAPER",
        "targets": ["m3_p3_simulation_validation"],
        "future_extension": "Simulation mocks and model-comparison statistics.",
        "notes": "Direct active proposal, current version target vector only.",
    },
    "M3|pre_professional|p6": {
        "status": "FUTURE_SCIENCE_EXTENSION",
        "targets": [],
        "future_extension": "Multi-channel chemical/structural/high-redshift evidence rebalance.",
        "notes": "Outside the active nine; should become a separate corpus/status-map task if resumed.",
    },
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def get_items(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return list(data.get("proposals") or data.get("topics") or [])


def source_text(item: Dict[str, Any]) -> str:
    for key in ("question", "research_question", "hypothesis", "remaining_uncertainty", "why"):
        value = item.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main(argv: List[str]) -> int:
    if len(argv) > 1:
        ts = argv[1]
    else:
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    outdir = OVERNIGHT_ROOT / "lanes/tori/historical-topic-extension-map" / ts
    outdir.mkdir(parents=True, exist_ok=True)

    source_files: Dict[str, Dict[str, Any]] = {}
    records_by_stage: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    active_papers: List[Dict[str, Any]] = []
    historical_records: List[Dict[str, Any]] = []

    for method_id, method in METHODS.items():
        for stage, rel in STAGES.items():
            path = FRONTEND_RT_ROOT / method["method_dir"] / rel
            if not path.exists():
                raise FileNotFoundError(path)
            data = load_json(path)
            items = get_items(data)
            key = f"{method_id}|{stage}"
            source_files[key] = {
                "method": method_id,
                "stage": stage,
                "path": str(path),
                "sha256": sha256_file(path),
                "marker": data.get("marker"),
                "kind": data.get("kind"),
                "declared_count": data.get("proposal_count", data.get("topic_count")),
                "actual_count": len(items),
            }
            for item in items:
                item_id = str(item.get("id", "")).strip()
                title = str(item.get("title", "")).strip()
                if not item_id or not title:
                    raise ValueError(f"Missing id/title in {path}: {item}")
                base = {
                    "method": method_id,
                    "method_label": method["label"],
                    "stage": stage,
                    "source_key": f"{method_id}|{stage}|{item_id}",
                    "id": item_id,
                    "title": title,
                    "source_text": source_text(item),
                    "source_path": str(path),
                    "source_marker": data.get("marker"),
                }
                records_by_stage[stage].append(base)
                if stage == "active_current":
                    active_key = f"{method_id}:{item_id}"
                    slug = ACTIVE_SLUGS.get(active_key)
                    if not slug:
                        raise ValueError(f"Active key missing slug mapping: {active_key}")
                    active_papers.append({**base, "active_slug": slug})
                else:
                    mapping = MAPPING.get(base["source_key"])
                    if not mapping:
                        raise ValueError(f"No curated mapping for {base['source_key']} {title!r}")
                    for target in mapping.get("targets", []):
                        if target not in set(ACTIVE_SLUGS.values()):
                            raise ValueError(f"Unknown active target {target} for {base['source_key']}")
                    historical_records.append({
                        **base,
                        "mapping_status": mapping["status"],
                        "active_targets": mapping.get("targets", []),
                        "future_extension": mapping.get("future_extension", ""),
                        "notes": mapping.get("notes", ""),
                        "completed_by_active_9": mapping["status"] == "ACTIVE_PAPER",
                    })

    active_papers.sort(key=lambda r: (r["method"], r["id"]))
    historical_records.sort(key=lambda r: (r["method"], r["stage"], r["id"]))

    counts = {
        "active_current_records": len(active_papers),
        "historical_seed_records": len(records_by_stage["historical_seed"]),
        "pre_professional_records": len(records_by_stage["pre_professional"]),
        "mapped_historical_plus_preprofessional_records": len(historical_records),
        "by_mapping_status": dict(Counter(r["mapping_status"] for r in historical_records)),
        "by_method_and_status": {
            f"{method}|{status}": count
            for (method, status), count in Counter((r["method"], r["mapping_status"]) for r in historical_records).items()
        },
        "records_with_no_active_target": sum(1 for r in historical_records if not r["active_targets"]),
        "records_with_active_target_but_not_completed": sum(
            1 for r in historical_records if r["active_targets"] and r["mapping_status"] != "ACTIVE_PAPER"
        ),
    }

    validation = {
        "timestamp_utc": ts,
        "all_source_files_exist": all(Path(v["path"]).exists() for v in source_files.values()),
        "source_files_count": len(source_files),
        "active_slugs_expected": len(ACTIVE_SLUGS),
        "active_slugs_seen": len({r["active_slug"] for r in active_papers}),
        "active_slug_set_matches_expected": {r["active_slug"] for r in active_papers} == set(ACTIVE_SLUGS.values()),
        "curated_mapping_keys_expected": len(MAPPING),
        "curated_mapping_keys_used": len({r["source_key"] for r in historical_records}),
        "unused_mapping_keys": sorted(set(MAPPING) - {r["source_key"] for r in historical_records}),
        "unmapped_source_keys": sorted(
            {r["source_key"] for stage in ("historical_seed", "pre_professional") for r in records_by_stage[stage]}
            - set(MAPPING)
        ),
        "counts": counts,
        "safety": {
            "writes_only_under_overnight_root": str(outdir).startswith(str(OVERNIGHT_ROOT)),
            "public_frontend_files_modified": False,
            "db_api_page_versions_git_deploy_cron_billing_oauth_external_submission": False,
        },
    }

    if not validation["active_slug_set_matches_expected"]:
        raise SystemExit("Active slug set mismatch")
    if validation["unused_mapping_keys"] or validation["unmapped_source_keys"]:
        raise SystemExit("Mapping coverage mismatch")

    payload = {
        "marker": f"HISTORICAL_TOPIC_EXTENSION_MAP_{ts}",
        "generated_utc": ts,
        "purpose": "Local-only crosswalk of historical/pre-reduction research-topic candidates to the 9 active AAS-style pilot papers and future extension bins.",
        "scope_guard": "The active 9 papers cover the consolidated public cards only; omitted historical candidates remain future methods/science extensions and are not claimed completed.",
        "source_files": source_files,
        "counts": counts,
        "active_papers": active_papers,
        "historical_crosswalk": historical_records,
        "safety": validation["safety"],
    }

    json_path = outdir / f"historical_topic_extension_map_{ts}.json"
    csv_path = outdir / f"historical_topic_extension_map_{ts}.csv"
    md_path = outdir / f"HISTORICAL_TOPIC_EXTENSION_MAP_{ts}.md"
    validation_path = outdir / f"historical_topic_extension_validation_{ts}.json"
    manifest_path = outdir / f"historical_topic_extension_manifest_{ts}.json"

    write_json(json_path, payload)

    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        fieldnames = [
            "method", "stage", "id", "title", "mapping_status", "active_targets",
            "completed_by_active_9", "future_extension", "notes", "source_path", "source_marker",
        ]
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for r in historical_records:
            writer.writerow({
                "method": r["method"],
                "stage": r["stage"],
                "id": r["id"],
                "title": r["title"],
                "mapping_status": r["mapping_status"],
                "active_targets": ";".join(r["active_targets"]),
                "completed_by_active_9": str(r["completed_by_active_9"]).lower(),
                "future_extension": r["future_extension"],
                "notes": r["notes"],
                "source_path": r["source_path"],
                "source_marker": r["source_marker"],
            })

    status_counter = Counter(r["mapping_status"] for r in historical_records)
    method_counter = Counter(r["method"] for r in historical_records)
    future_only = [r for r in historical_records if not r["active_targets"] or r["mapping_status"].startswith("FUTURE")]
    partial = [r for r in historical_records if r["mapping_status"] == "PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION"]

    lines: List[str] = []
    lines += [
        f"# Historical topic extension map — {ts}",
        "",
        f"Marker: `HISTORICAL_TOPIC_EXTENSION_MAP_{ts}`",
        "",
        "## Purpose",
        "",
        "This local-only artifact maps pre-reduction / historical research-topic candidates to the 9 active Galaxy Evolution AAS-style pilot papers, and separates topics that remain future extensions. It is a scope-control artifact, not a new prose or claim-evidence packet.",
        "",
        "## Count summary",
        "",
        f"- Active current proposal-card papers parsed: **{counts['active_current_records']}**.",
        f"- Historical seed topics parsed: **{counts['historical_seed_records']}**.",
        f"- Pre-professional intermediate proposals parsed: **{counts['pre_professional_records']}**.",
        f"- Historical/intermediate records mapped: **{counts['mapped_historical_plus_preprofessional_records']}**.",
        f"- Records with no active-paper target: **{counts['records_with_no_active_target']}**.",
        f"- Records with active-paper adjacency but not completed by active 9: **{counts['records_with_active_target_but_not_completed']}**.",
        "",
        "Mapping-status counts:",
        "",
    ]
    for status, count in sorted(status_counter.items()):
        lines.append(f"- `{status}`: **{count}**")
    lines += ["", "Method counts:", ""]
    for method, count in sorted(method_counter.items()):
        lines.append(f"- `{method}`: **{count}** historical/intermediate records")

    lines += [
        "",
        "## Active 9 anchor set verified from current maps",
        "",
        "| Method | Active slug | ID | Current active title |",
        "|---|---|---|---|",
    ]
    for r in active_papers:
        lines.append(f"| {r['method']} | `{r['active_slug']}` | {r['id']} | {r['title']} |")

    lines += [
        "",
        "## Crosswalk",
        "",
        "| Source | Historical/intermediate title | Status | Active target(s) | Future-extension boundary |",
        "|---|---|---|---|---|",
    ]
    for r in historical_records:
        target = ", ".join(f"`{t}`" for t in r["active_targets"]) if r["active_targets"] else "—"
        source = f"{r['method']} {r['stage']} {r['id']}"
        lines.append(f"| {source} | {r['title']} | `{r['mapping_status']}` | {target} | {r['future_extension']} |")

    lines += [
        "",
        "## Future-only / not-completed queue",
        "",
        "These are the clearest omitted historical candidates. They should not be described as completed by the 9 overnight papers.",
        "",
        "| Source | Future queue item | Why not completed by active 9 |",
        "|---|---|---|",
    ]
    for r in future_only:
        lines.append(f"| {r['method']} {r['stage']} {r['id']} | {r['future_extension']} | {r['notes']} |")

    lines += [
        "",
        "## Partial-fold queue",
        "",
        "These topics have an active-paper adjacency but require a future artifact before the broader historical question can be claimed addressed.",
        "",
        "| Source | Active adjacency | Missing future work |",
        "|---|---|---|",
    ]
    for r in partial:
        target = ", ".join(f"`{t}`" for t in r["active_targets"])
        lines.append(f"| {r['method']} {r['stage']} {r['id']} | {target} | {r['future_extension']} |")

    lines += [
        "",
        "## Source grounding",
        "",
        "The map was built by parsing the current and backup JSON topic maps below; no new external literature or product database was queried.",
        "",
        "| Key | Marker | Count | SHA256 | Path |",
        "|---|---|---:|---|---|",
    ]
    for key, meta in sorted(source_files.items()):
        lines.append(f"| `{key}` | `{meta['marker']}` | {meta['actual_count']} | `{meta['sha256']}` | `{meta['path']}` |")

    lines += [
        "",
        "## Verification and safety",
        "",
        f"- Validation JSON: `{validation_path}`.",
        "- Active slug set matched the expected 9 active pilot-paper slugs.",
        "- Every historical/intermediate source record has exactly one curated mapping row.",
        "- Every active target named in the crosswalk is one of the verified active 9 slugs.",
        "- Writes were limited to the overnight work root; no public/static frontend files were modified by this tick.",
        "- No DB/API/page_versions/wiki publish/trust/deploy/restart/git/extra-cron/billing/OAuth/external-submission changes were performed.",
        "- No active execution phrase.",
        "",
    ]
    md_path.write_text("\n".join(lines), encoding="utf-8")

    # Write validation first, then manifest artifact hashes. Self-referential hashes are not
    # embedded in the file being hashed; consumers can compute the manifest hash externally.
    validation_final = {
        **validation,
        "artifact_hash_note": "Artifact hashes are recorded in the manifest. Self-referential hashes are intentionally not embedded in this validation file.",
    }
    write_json(validation_path, validation_final)

    artifact_meta = {}
    for p in [json_path, csv_path, md_path, validation_path]:
        artifact_meta[p.name] = {"path": str(p), "bytes": p.stat().st_size, "sha256": sha256_file(p)}
    manifest = {
        "marker": f"HISTORICAL_TOPIC_EXTENSION_MANIFEST_{ts}",
        "generated_utc": ts,
        "outdir": str(outdir),
        "artifacts": artifact_meta,
        "manifest_file": {
            "path": str(manifest_path),
            "bytes": None,
            "sha256_note": "Self-referential manifest SHA is not embedded; compute externally when needed.",
        },
        "validation": {
            "active_slug_set_matches_expected": validation["active_slug_set_matches_expected"],
            "unused_mapping_keys": validation["unused_mapping_keys"],
            "unmapped_source_keys": validation["unmapped_source_keys"],
            "counts": counts,
            "validation_sha256_final": artifact_meta[validation_path.name]["sha256"],
        },
        "safety": validation["safety"],
    }
    write_json(manifest_path, manifest)
    manifest["manifest_file"]["bytes"] = manifest_path.stat().st_size
    write_json(manifest_path, manifest)

    print(json.dumps({
        "ok": True,
        "timestamp_utc": ts,
        "outdir": str(outdir),
        "counts": counts,
        "artifacts": {k: v["path"] for k, v in artifact_meta.items()},
        "safety": validation["safety"],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
