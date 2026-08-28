#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import os
import re
import sys

HERE = Path(__file__).resolve().parent
SOURCE = Path(os.environ.get("MZR_FROZEN_SOURCE_DIR", HERE / "frozen_sources/pass7"))
storyboard_path = Path(os.environ.get("MZR_STORYBOARD_PATH", HERE / "STORYBOARD_CANDIDATE.json"))
storyboard = json.loads(storyboard_path.read_text())
beats = storyboard["beats"]
citation_ledger = json.loads((HERE / "citation_ledger.json").read_text())
approved_contract = json.loads((HERE / "qa/APPROVED_STORYBOARD_CONTRACT.json").read_text())
source_manifest = json.loads((SOURCE / "MANIFEST.json").read_text())


def file_sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


snapshot_manifest_path = HERE / "MANIFEST.json"
snapshot_manifest_authentication: dict[str, object] = {
    "manifest_present": snapshot_manifest_path.exists(),
    "external_manifest_digest_required": True,
}
if snapshot_manifest_path.exists():
    snapshot_manifest = json.loads(snapshot_manifest_path.read_text())
    snapshot_entries = {entry["path"]: entry for entry in snapshot_manifest.get("files", [])}
    approval_entry = snapshot_entries.get("qa/APPROVED_STORYBOARD_CONTRACT.json")
    validator_entry = snapshot_entries.get("validate_proposal.py")
    storyboard_entry = snapshot_entries.get("STORYBOARD_CANDIDATE.json")
    snapshot_manifest_authentication.update({
        "approval_entry_present": approval_entry is not None,
        "approval_hash_matches": approval_entry is not None
        and approval_entry["sha256"] == file_sha256(HERE / "qa/APPROVED_STORYBOARD_CONTRACT.json"),
        "validator_entry_present": validator_entry is not None,
        "validator_hash_matches": validator_entry is not None
        and validator_entry["sha256"] == file_sha256(HERE / "validate_proposal.py"),
        "storyboard_entry_present": storyboard_entry is not None,
        "storyboard_hash_matches": storyboard_entry is not None
        and storyboard_entry["sha256"] == file_sha256(HERE / "STORYBOARD_CANDIDATE.json"),
    })
    snapshot_manifest_authentication["verdict"] = "PASS" if all(
        value for key, value in snapshot_manifest_authentication.items()
        if key not in {"manifest_present", "external_manifest_digest_required", "verdict"}
    ) else "FAIL"
else:
    snapshot_manifest_authentication["verdict"] = "NOT_APPLICABLE_UNSEALED_LIVE_LANE"


source_manifest_checks = {
    entry["file"]: (SOURCE / entry["file"]).exists()
    and file_sha256(SOURCE / entry["file"]) == entry["sha256"]
    and (SOURCE / entry["file"]).stat().st_size == entry["bytes"]
    for entry in source_manifest["files"]
}

errors = []
if len(source_manifest_checks) != 8 or not all(source_manifest_checks.values()):
    errors.append(f"self-contained source freeze failed: {[name for name, value in source_manifest_checks.items() if not value]}")
if len(beats) != 10:
    errors.append(f"expected 10 beats, found {len(beats)}")
if any(not b.get("visual_action") for b in beats):
    errors.append("every beat must have one visual action")
if any(not b.get("display_citation") for b in beats):
    errors.append("every beat must have an audience display citation")
if any("/" in b["display_citation"] or ".json" in b["display_citation"] or ".md" in b["display_citation"] for b in beats):
    errors.append("display citations expose internal paths or filenames")
if any(not b.get("on_screen_copy") for b in beats):
    errors.append("every beat must have explicit on_screen_copy")
if snapshot_manifest_authentication["verdict"] == "FAIL":
    errors.append("snapshot manifest authentication failed: approved contract, validator, or storyboard is not pinned to the current immutable manifest")

audience_contract = storyboard.get("audience_copy_contract", {})
if audience_contract.get("visible_fields") != ["on_screen_copy", "display_citation"]:
    errors.append("audience-copy visible-field contract is missing or changed")
if audience_contract.get("status") != "STATIC_STORYBOARD_PROPOSAL_ONLY_NOT_A_CANDIDATE":
    errors.append("audience-copy proposal-only status is missing or changed")
required_stage_labels = {
    "T1 ENUMERATION",
    "T1 RETRIEVAL-INSTRUMENT CHECK",
    "T1 RECORDED CHARACTERIZATION",
    "T2 CONTRACT STATUS · APPLICATION NOT COMPLETED",
}
if set(audience_contract.get("required_stage_labels", [])) != required_stage_labels:
    errors.append("required T1/T2 audience-stage labels are missing or changed")

motion_contract = audience_contract.get("scientific_presentation_motion_contract", {})
maximum_state_seconds = motion_contract.get("maximum_unchanged_evidence_state_seconds")
minimum_states = motion_contract.get("minimum_reveal_states_per_beat")
motion_checks = {}
global_change_times = []
declared_clause_ids = set()
mapped_clause_ids = set()
cursor = 0.0
noop_pattern = re.compile(r"\b(hold|retain|standalone section divider)\b", re.IGNORECASE)


def normalized_words(text):
    return " ".join(re.findall(r"[\w]+", text.lower()))


for beat in beats:
    states = beat.get("timed_reveal_states", [])
    times = [state.get("at_seconds") for state in states]
    duration = float(beat["proposed_seconds"])
    gaps = [b - a for a, b in zip(times, times[1:])] + ([duration - times[-1]] if times else [])
    clauses = beat.get("narration_clauses", [])
    clause_ids = {clause.get("clause_id") for clause in clauses}
    declared_clause_ids.update(clause_ids)
    narration_normalized = normalized_words(beat["narration"])
    clauses_are_verbatim_subsequences = all(
        bool(clause.get("text")) and normalized_words(clause["text"]) in narration_normalized
        for clause in clauses
    )
    state_schema_pass = all(
        set(state) == {"state_id", "at_seconds", "operation", "evidence_delta", "clause_ids", "visible_change"}
        and state["operation"] in {"reveal", "transform"}
        and bool(state["evidence_delta"])
        and bool(state["visible_change"])
        and bool(state["clause_ids"])
        and set(state["clause_ids"]).issubset(clause_ids)
        and not noop_pattern.search(state["visible_change"] + " " + state["evidence_delta"])
        for state in states
    )
    for state in states:
        mapped_clause_ids.update(state.get("clause_ids", []))
        if state.get("operation") in {"reveal", "transform"} and state.get("evidence_delta"):
            global_change_times.append(cursor + float(state["at_seconds"]))
    motion_checks[beat["id"]] = {
        "state_count": len(states),
        "starts_at_zero": bool(times) and times[0] == 0.0,
        "strictly_increasing_and_within_beat": bool(times) and times == sorted(set(times)) and times[-1] < duration,
        "all_states_are_structured_semantic_changes": state_schema_pass,
        "narration_clause_count": len(clauses),
        "clauses_are_verbatim_subsequences": clauses_are_verbatim_subsequences,
        "all_beat_clauses_mapped": clause_ids == {cid for state in states for cid in state.get("clause_ids", [])},
        "maximum_state_gap_seconds": max(gaps) if gaps else None,
        "raw_within_beat_gap_pass": bool(gaps) and maximum_state_seconds == 3.0 and max(gaps) <= maximum_state_seconds,
        "minimum_state_count_pass": minimum_states == 2 and len(states) >= minimum_states,
    }
    cursor += duration

semantic_global_gaps = [b - a for a, b in zip(global_change_times, global_change_times[1:])]
if global_change_times:
    semantic_global_gaps.append(cursor - global_change_times[-1])
global_motion_checks = {
    "first_change_at_zero": bool(global_change_times) and global_change_times[0] == 0.0,
    "global_times_strictly_increasing": global_change_times == sorted(set(global_change_times)),
    "maximum_semantic_gap_seconds": max(semantic_global_gaps) if semantic_global_gaps else None,
    "maximum_semantic_gap_pass": bool(semantic_global_gaps) and maximum_state_seconds == 3.0 and max(semantic_global_gaps) <= maximum_state_seconds,
    "all_declared_clauses_mapped": bool(declared_clause_ids) and declared_clause_ids == mapped_clause_ids,
}
motion_gate_pass = all(
    all(value for key, value in checks.items() if key not in {"state_count", "maximum_state_gap_seconds"})
    for checks in motion_checks.values()
) and all(value for key, value in global_motion_checks.items() if key != "maximum_semantic_gap_seconds")
if not motion_gate_pass:
    failed_beats = [beat for beat, checks in motion_checks.items() if not all(value for key, value in checks.items() if key not in {"state_count", "maximum_state_gap_seconds"})]
    failed_global = [key for key, value in global_motion_checks.items() if key != "maximum_semantic_gap_seconds" and not value]
    errors.append(f"scientific-presentation motion contract failed: beats={failed_beats}; global={failed_global}")

continuity_contract = audience_contract.get("scientific_state_continuity_contract", {})
handoffs = [beat.get("state_handoff", {}) for beat in beats]
handoff_chain = [handoffs[index]["exit_state_id"] == handoffs[index + 1]["entry_state_id"] for index in range(len(handoffs) - 1)] if all(handoffs) else []
continuity_checks = {
    "all_beats_declare_handoff": all(
        set(handoff) == {"entry_state_id", "exit_state_id", "persistent_layers", "retire_after_exit"}
        and bool(handoff["entry_state_id"])
        and bool(handoff["exit_state_id"])
        and bool(handoff["persistent_layers"])
        and isinstance(handoff["retire_after_exit"], list)
        for handoff in handoffs
    ),
    "cross_beat_state_ids_match": len(handoff_chain) == 9 and all(handoff_chain),
    "full_frame_scientific_resets_prohibited": continuity_contract.get("full_frame_scientific_resets") == "PROHIBITED",
    "scope_layers_persist_every_beat": all(
        "not-an-MZR" in " ".join(handoff["persistent_layers"])
        and "single-table/no-crossmatch" in " ".join(handoff["persistent_layers"])
        for handoff in handoffs
    ),
    "main_spine_persists_after_construction": beats[5]["timed_reveal_states"][0]["evidence_delta"] == "new direct 157-to-T2 eligibility-gate path"
        and all(
            "178→−21→157→T2 main spine" in handoffs[index]["persistent_layers"]
            for index in range(6, 10)
        ),
    "62_parent_and_boundary_persist_after_side_branch": all(
        all(token in " ".join(handoffs[index]["persistent_layers"]) for token in ["62", "157", "boundary"])
        for index in range(6, 10)
    ),
    "qualified_close_inherits_required_layers": all(
        token in " ".join(handoffs[-1]["persistent_layers"])
        for token in ["178→−21→157→T2 main spine", "62-of-157", "application-not-completed/no-count", "not-an-MZR", "single-table/no-crossmatch"]
    ),
    "encoded_continuity_regate_required": "CUT-BOUNDARY CONTINUITY" in continuity_contract.get("future_encoded_gate", ""),
}
continuity_gate_pass = all(continuity_checks.values())
if not continuity_gate_pass:
    errors.append(f"scientific-state continuity contract failed: {[key for key, value in continuity_checks.items() if not value]}")


def visible_strings(value):
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [text for item in value for text in visible_strings(item)]
    if isinstance(value, dict):
        return [text for item in value.values() for text in visible_strings(item)]
    return []


def canonical_sha256(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(payload).hexdigest()


audience_projection = "\n".join(
    text
    for beat in beats
    for text in visible_strings({"on_screen_copy": beat["on_screen_copy"], "display_citation": beat["display_citation"]})
)
prohibited_audience = audience_contract.get("prohibited_audience_tokens", [])
found_prohibited_audience = [token for token in prohibited_audience if token.lower() in audience_projection.lower()]
if found_prohibited_audience:
    errors.append(f"prohibited audience-copy tokens: {found_prohibited_audience}")

used_display_citations = [beat["display_citation"] for beat in beats]
registered_display_citations = set(citation_ledger.get("display_citations", []))
citation_identity_checks = {
    "all_display_citations_registered_exactly": bool(registered_display_citations) and all(citation in registered_display_citations for citation in used_display_citations),
    "count_ledger_precondition_unsatisfied": citation_ledger.get("internal_count_ledger_publication_state") == "NOT_AUDIENCE_REACHABLE · PUBLICATION PRECONDITION UNSATISFIED",
    "external_source_urls_present": len(citation_ledger.get("sources", [])) == 2 and all(source.get("url", "").startswith("https://") for source in citation_ledger["sources"]),
}
if not all(citation_identity_checks.values()):
    errors.append(f"citation identity checks failed: {[key for key, value in citation_identity_checks.items() if not value]}")

audience_semantics = [
    {
        "id": beat["id"],
        "narration": beat["narration"],
        "on_screen_copy": beat["on_screen_copy"],
        "display_citation": beat["display_citation"],
    }
    for beat in beats
]
build_semantics = [
    {
        "id": beat["id"],
        "visual_action": beat["visual_action"],
        "narration_clauses": beat["narration_clauses"],
        "timed_reveal_states": beat["timed_reveal_states"],
        "state_handoff": beat["state_handoff"],
    }
    for beat in beats
]
approved_contract_checks = {
    "storyboard_version_exact": storyboard.get("storyboard_version") == approved_contract["storyboard_version"] == "pass7-distinct-example-clock-v8",
    "canonical_storyboard_exact": canonical_sha256(storyboard) == approved_contract["canonical_storyboard_sha256"],
    "canonical_audience_semantics_exact": canonical_sha256(audience_semantics) == approved_contract["canonical_audience_semantics_sha256"],
    "canonical_build_semantics_exact": canonical_sha256(build_semantics) == approved_contract["canonical_build_semantics_sha256"],
    "contract_counts_exact": (
        len(beats),
        len(audience_semantics),
        sum(len(beat["timed_reveal_states"]) for beat in beats),
        sum(len(beat["narration_clauses"]) for beat in beats),
    ) == (
        approved_contract["beat_count"],
        approved_contract["narration_count"],
        approved_contract["structured_state_count"],
        approved_contract["declared_clause_count"],
    ),
    "build_directions_prohibit_static_hold_language": all(
        not re.search(r"\bhold\b|static prose|unchanged for the entire beat", beat["visual_action"], re.IGNORECASE)
        for beat in beats
    ),
    "self_contained_source_manifest_exact": file_sha256(SOURCE / "MANIFEST.json") == approved_contract["source_freeze_manifest_sha256"],
    "snapshot_manifest_authenticates_contract_storyboard_and_validator": snapshot_manifest_authentication["verdict"] in {"PASS", "NOT_APPLICABLE_UNSEALED_LIVE_LANE"},
    "b09_four_examples_are_distinct_from_persistent_taxonomy_labels": [
        state["evidence_delta"] for state in beats[8]["timed_reveal_states"][1:]
    ] == [
        "Galactic Cartesian height example under the persistent symbol-and-meaning group",
        "stellar-grid model-metal-fraction example under the persistent symbol-and-meaning group",
        "stellar gravitational-redshift example under the persistent target-domain group",
        "gravitational-redshift-velocity example completes the second recorded-example pair",
    ],
    "b09_not_t2_clause_mapped_by_stage_transition": beats[8]["timed_reveal_states"][0]["clause_ids"] == ["b09_c01", "b09_c03"],
    "external_manifest_declared_as_trust_anchor": approved_contract.get("trust_anchor") == "EXTERNALLY_SUPPLIED_IMMUTABLE_SNAPSHOT_MANIFEST_SHA256"
        and approved_contract.get("co_located_hashes_independent_trust_anchor") is False
        and approved_contract.get("snapshot_manifest_authentication_required") is True,
    "contract_publication_closed": approved_contract["publication_gate"] == "CLOSED",
}
if not all(approved_contract_checks.values()):
    errors.append(f"approved storyboard contract failed: {[key for key, value in approved_contract_checks.items() if not value]}")

narration = " ".join(b["narration"] for b in beats)
word_count = len(re.findall(r"\b[\w–-]+\b", narration))
total_seconds = sum(float(b["proposed_seconds"]) for b in beats)
delivered_wpm = word_count / total_seconds * 60

required = [
    "178 candidate tables",
    "21 tables",
    "19 on redshift",
    "2 on abundance",
    "leaving 157",
    "62 of those 157",
    "T2 still applies to all 157",
    "All seven pinned recall members returned",
    "none of the three controls appeared",
    "validate retrieval, not precision",
    "symbol-and-meaning collisions",
    "target-domain mismatches",
    "not T2 rulings",
    "twelve decoys and three anchors",
    "eligibility application is not completed",
    "no eligible-table count",
]
missing = [p for p in required if p not in narration]
if missing:
    errors.append(f"missing required narration phrases: {missing}")

forbidden_affirmative = [
    "62 eligible",
    "measured the mass-metallicity relation",
    "the archive cannot do it",
    "precision check passed",
]
found_forbidden = [p for p in forbidden_affirmative if p.lower() in narration.lower()]
if found_forbidden:
    errors.append(f"forbidden affirmative claims: {found_forbidden}")

visual_actions = " ".join(b["visual_action"] for b in beats)
final_states = beats[-1]["timed_reveal_states"]
final_sequence_checks = {
    "state_ids": [state["state_id"] for state in final_states] == ["b10_s01", "b10_s02", "b10_s03", "b10_s04"],
    "times": [state["at_seconds"] for state in final_states] == [0.0, 3.0, 6.0, 8.0],
    "operations": [state["operation"] for state in final_states] == ["reveal", "reveal", "reveal", "transform"],
    "ordered_deltas": all(
        token in final_states[index]["evidence_delta"]
        for index, token in enumerate(["reportable-now", "pending", "no-count gate", "qualified close"])
    ),
}
visual_semantics = {
    "opening_single_table_metadata_reach": "A single-table metadata census" in audience_projection and "metadata-reachable columns" in audience_projection,
    "single_table_crossmatch_boundary": "CROSS-TABLE JOINS AND CROSSMATCHES NOT ASSESSED" in audience_projection,
    "direct_157_to_T2": "Connect 157 directly to T2" in visual_actions and "T2 STILL APPLIES TO ALL 157" in audience_projection,
    "62_side_check": "62 OF 157 RECORDED DESCRIPTIONS MATCHED" in audience_projection and "NOT AN ELIGIBILITY FILTER" in audience_projection,
    "qualified_T2_status": "APPLICATION NOT COMPLETED · NO ELIGIBLE-TABLE COUNT" in audience_projection,
    "precision_taxonomy_split": "SYMBOL / MEANING COLLISION" in audience_projection and "TARGET-DOMAIN MISMATCH" in audience_projection,
    "examples_not_T2_rulings": "RECORDED EXAMPLES · NOT T2 RULINGS" in audience_projection,
    "reportable_now_pending_close": all(
        phrase in audience_projection
        for phrase in [
            "Reportable now versus pending",
            "T2 APPLICATION TO ALL 157 TABLES",
            "ELIGIBLE-TABLE COUNT",
            "ANY METALLICITY OR MZR MEASUREMENT",
            "SINGLE-TABLE METADATA CENSUS · NOT AN MZR MEASUREMENT",
        ]
    ),
    "no_carrying_measurement_overstatement": "catalogues carrying gas-phase" not in audience_projection.lower() and "carry all three axes" not in audience_projection.lower(),
    "all_target_concepts_are_search_axes": all(
        phrase in audience_projection.lower() and phrase in narration.lower()
        for phrase in ["abundance-search", "mass-search", "redshift-search"]
    ) and "stellar-mass, and redshift-search" not in audience_projection.lower(),
    "vocabulary_presence_not_evidence": "FROZEN VOCABULARY REGEX PRESENCE · NOT ADJUDICATED GAS-PHASE EVIDENCE" in audience_projection and "explicit gas-phase evidence" not in audience_projection.lower(),
    "T1_T2_stage_provenance": all(
        phrase in audience_projection
        for phrase in [
            "T1 ENUMERATION",
            "T1 RETRIEVAL-INSTRUMENT CHECK · 3 CONTROLS",
            "T1 RECORDED CHARACTERIZATION · NOT T2 RULINGS",
            "T2 CONTRACT STATUS · APPLICATION NOT COMPLETED",
        ]
    ),
    "balanced_T2_contract_design_provenance": "T2 CONTRACT DESIGN · 12 DECOYS + 3 ANCHORS · NOT ELIGIBILITY RESULTS" in audience_projection,
    "audience_reachable_count_ledger_precondition": "AUDIENCE-REACHABLE METHODS AND COUNT LEDGER BEFORE PUBLIC RELEASE" in audience_contract.get("publication_precondition", ""),
    "scientific_presentation_motion_contract": maximum_state_seconds == 3.0 and minimum_states == 2 and motion_gate_pass,
    "no_standalone_section_divider_holds": "NO STANDALONE SECTION-DIVIDER HOLDS" in motion_contract.get("section_divider_policy", ""),
    "final_reportable_pending_reveal_sequence": all(final_sequence_checks.values()),
    "scientific_state_continuity_contract": continuity_gate_pass,
    "no_full_frame_scientific_resets": continuity_checks["full_frame_scientific_resets_prohibited"],
    "cross_beat_state_handoffs_match": continuity_checks["cross_beat_state_ids_match"],
    "main_spine_and_62_parent_continuity": continuity_checks["main_spine_persists_after_construction"] and continuity_checks["62_parent_and_boundary_persist_after_side_branch"],
}
if not all(visual_semantics.values()):
    errors.append(f"visual semantics failed: {[k for k, v in visual_semantics.items() if not v]}")

# Exact source checks.
findings = (SOURCE / "T1_FINDINGS.md").read_text()
manifest = json.loads((SOURCE / "T1_MZR_MANIFEST.json").read_text())
gas = json.loads((SOURCE / "T1E_GASPHASE_COUNT.json").read_text())
t2_freeze_record = (SOURCE / "FREEZE_RECORD_T2.md").read_text()
source_checks = {
    "manifest_done": manifest["status"] == "DONE",
    "funnel": (manifest["n_candidates_pre_filter"], len(manifest["dropped_candidates"]), manifest["n_candidates"]) == (178, 21, 157),
    "drop_split": (
        sum("redshift" in d["axes_emptied_by_modifier_filter"] for d in manifest["dropped_candidates"]),
        sum("abundance" in d["axes_emptied_by_modifier_filter"] for d in manifest["dropped_candidates"]),
    ) == (19, 2),
    "gas_vocabulary": (gas["count"], gas["of_candidates"]) == (62, 157),
    "gas_not_ruling": all(
        phrase in gas["this_is_not_a_ruling"]
        for phrase in ["vocabulary presence", "not an E1-E4 verdict", "T2 rules eligibility"]
    ),
    "recall_control": (sum(manifest["recall_members_returned"].values()), sum(manifest["controls_appearing"].values())) == (7, 0),
    "axis_totals_in_findings": all(token in findings for token in ["5,393", "5,568", "+175", "6,118", "6,206", "+88", "6,667", "6,687", "+20"]),
    "T1_controls_distinct_from_complete_T2_contract_controls": "0/3 controls appeared" in findings and "12 decoys + 3 anchors" in t2_freeze_record,
}
if not all(source_checks.values()):
    errors.append(f"source checks failed: {[k for k, v in source_checks.items() if not v]}")

axis_rows = {
    axis: {
        "ucd": int(ucd.replace(",", "")),
        "plus_name": int(plus_name.replace(",", "")),
        "gain": int(gain),
    }
    for axis, ucd, plus_name, gain in re.findall(
        r"\| (abundance|mass|redshift) \| ([\d,]+) \| ([\d,]+) \| \+(\d+)",
        findings,
    )
}
expected_axis_cards = [
    f"{axis.upper()} SEARCH · UCD {values['ucd']:,} · UCD + NAME {values['plus_name']:,} · GAIN +{values['gain']} TABLES"
    for axis, values in axis_rows.items()
]
pre_filter = manifest["n_candidates_pre_filter"]
post_filter = manifest["n_candidates"]
dropped = len(manifest["dropped_candidates"])
redshift_drops = sum("redshift" in item["axes_emptied_by_modifier_filter"] for item in manifest["dropped_candidates"])
abundance_drops = sum("abundance" in item["axes_emptied_by_modifier_filter"] for item in manifest["dropped_candidates"])
gas_count = gas["count"]
gas_parent = gas["of_candidates"]
expected_b03_narration = (
    f"UCD plus name matching reached {axis_rows['abundance']['plus_name']:,} tables on the abundance-search axis, "
    f"{axis_rows['mass']['plus_name']:,} on mass-search, and {axis_rows['redshift']['plus_name']:,} on redshift-search; "
    f"name matching added {axis_rows['abundance']['gain']}, {axis_rows['mass']['gain']}, and {axis_rows['redshift']['gain']}."
)
expected_b05_narration = (
    f"Modifier columns then emptied a required search axis in {dropped} tables: {redshift_drops} on redshift-search and "
    f"{abundance_drops} on abundance-search, leaving {post_filter} recorded candidates."
)
expected_b06_narration = (
    f"As a side check, a frozen term regex matched {gas_count} of those {gas_parent} recorded descriptions; "
    f"it is not an eligibility filter, and T2 still applies to all {post_filter}."
)
source_render_bindings = {
    "b01_all_axes_exhaustively_qualified": beats[0]["narration"] == "This VizieR metadata census asks which single tables intersect the abundance-search, mass-search, and redshift-search axes."
        and beats[0]["on_screen_copy"]["body"] == "Which VizieR single tables have metadata-reachable columns on the abundance-search, mass-search, and redshift-search axes?",
    "b01_visual_action_matches_progressive_states": beats[0]["visual_action"] == "Open on one archive-table icon with the T1 stage label. Reveal ABUNDANCE SEARCH, MASS SEARCH, and REDSHIFT SEARCH rails one at a time; merge all three into the single-table intersection; then reveal and lock the persistent METADATA CENSUS — NOT AN MZR MEASUREMENT badge and SINGLE-TABLE METADATA INTERSECTION — CROSS-TABLE JOINS AND CROSSMATCHES NOT ASSESSED subtitle."
        and [state["evidence_delta"] for state in beats[0]["timed_reveal_states"]] == [
            "archive-table icon and T1 stage label",
            "abundance-search metadata rail",
            "mass-search metadata rail",
            "redshift-search rail and three-axis merge",
            "not-an-MZR and single-table/no-crossmatch badges",
        ],
    "b02_retrieval_channels_exactly_bound": beats[1]["narration"] == "The search combined semantic UCD tags with column-name variants, and each frozen query returned exactly its pre-counted rows."
        and beats[1]["on_screen_copy"] == {
            "stage": "T1 ENUMERATION",
            "heading": "Two retrieval channels",
            "channels": ["SEMANTIC UCD TAGS", "COLUMN-NAME VARIANTS"],
            "status": "FROZEN QUERIES · ZERO CHANNEL FAILURES",
        },
    "b03_axis_cards_exactly_source_bound": beats[2]["on_screen_copy"]["cards"] == expected_axis_cards,
    "b03_narration_exactly_source_bound": beats[2]["narration"] == expected_b03_narration,
    "b04_intersection_exactly_source_bound": beats[3]["on_screen_copy"]["main"] == f"{pre_filter} SINGLE TABLES"
        and beats[3]["narration"] == f"The three axis lists intersected at {pre_filter} candidate tables.",
    "b05_funnel_exactly_source_bound": beats[4]["on_screen_copy"]["main"] == f"{pre_filter} − {dropped} = {post_filter} RECORDED CANDIDATE TABLES"
        and beats[4]["on_screen_copy"]["redshift_drop"].startswith(f"{redshift_drops} · REDSHIFT-SEARCH AXIS EMPTIED")
        and beats[4]["on_screen_copy"]["abundance_drop"].startswith(f"{abundance_drops} · ABUNDANCE-SEARCH AXIS EMPTIED")
        and beats[4]["narration"] == expected_b05_narration
        and beats[4]["state_handoff"]["exit_state_id"] == "funnel_178_21_157"
        and beats[4]["timed_reveal_states"][-1]["evidence_delta"] == "157 post-filter result node"
        and beats[4]["timed_reveal_states"][-1]["visible_change"] == "Reveal 157 RECORDED CANDIDATE TABLES as the post-filter result.",
    "b06_vocabulary_topology_exactly_source_bound": beats[5]["on_screen_copy"]["main"] == f"{gas_count} OF {gas_parent} RECORDED DESCRIPTIONS MATCHED"
        and beats[5]["on_screen_copy"]["meaning"] == "FROZEN VOCABULARY REGEX PRESENCE · NOT ADJUDICATED GAS-PHASE EVIDENCE"
        and beats[5]["on_screen_copy"]["boundary"] == f"SIDE CHECK ONLY · NOT AN ELIGIBILITY FILTER · T2 STILL APPLIES TO ALL {post_filter}"
        and beats[5]["narration"] == expected_b06_narration
        and beats[5]["state_handoff"]["entry_state_id"] == "funnel_178_21_157"
        and beats[5]["timed_reveal_states"][0]["evidence_delta"] == "new direct 157-to-T2 eligibility-gate path"
        and beats[5]["timed_reveal_states"][0]["visible_change"] == "Extend the completed 178→−21→157 spine by revealing the direct 157-to-T2 eligibility-gate path.",
    "b07_retrieval_metrics_exactly_source_bound": beats[6]["on_screen_copy"]["recall"] == f"RECALL {sum(manifest['recall_members_returned'].values())}/7"
        and beats[6]["on_screen_copy"]["controls"] == f"CONTROLS APPEARING {sum(manifest['controls_appearing'].values())}/3"
        and beats[6]["narration"] == "All seven pinned recall members returned, while none of the three controls appeared."
        and beats[6]["on_screen_copy"] == {
            "stage": "T1 RETRIEVAL-INSTRUMENT CHECK · 3 CONTROLS",
            "heading": "Retrieval instrument check",
            "recall": "RECALL 7/7",
            "controls": "CONTROLS APPEARING 0/3",
        },
    "b08_precision_limit_exactly_source_bound": beats[7]["narration"] == "Those checks validate retrieval, not precision: the frozen controls did not cover the dominant precision-contamination mode."
        and beats[7]["on_screen_copy"] == {
            "stage": "T1 RETRIEVAL-INSTRUMENT CHECK · 3 CONTROLS",
            "retrieval_status": "RETRIEVAL CHECK PASSED",
            "precision_status": "PRECISION NOT CERTIFIED",
            "coverage_limit": "FROZEN CONTROLS DID NOT COVER THE DOMINANT PRECISION-CONTAMINATION MODE",
            "taxonomy_preview": ["SYMBOL / MEANING COLLISION", "TARGET-DOMAIN MISMATCH"],
            "boundary": "RECORDED EXAMPLES · NOT T2 RULINGS",
        },
    "b08_semantic_state_progression_exact": [state["evidence_delta"] for state in beats[7]["timed_reveal_states"]] == [
        "retrieval-check status becomes explicitly passed",
        "distinct precision-not-certified status",
        "frozen-control coverage limitation",
        "two named precision-failure taxonomy groups",
        "recorded-examples not-T2-rulings boundary",
    ],
    "b09_precision_examples_exactly_source_bound": beats[8]["narration"] == "Recorded examples separate symbol-and-meaning collisions—Galactic height and model-grid metal fraction—from target-domain mismatches: stellar gravitational redshift and gravitational-redshift velocity. They are not T2 rulings."
        and beats[8]["on_screen_copy"] == {
            "stage": "T1 RECORDED CHARACTERIZATION · NOT T2 RULINGS",
            "heading": "RECORDED EXAMPLES · NOT T2 RULINGS",
            "symbol_or_meaning_collision": {
                "label": "SYMBOL / MEANING COLLISION",
                "examples": ["GALACTIC CARTESIAN HEIGHT", "STELLAR-GRID METAL FRACTION · MODEL Z"],
            },
            "target_domain_mismatch": {
                "label": "TARGET-DOMAIN MISMATCH",
                "examples": ["STELLAR GRAVITATIONAL REDSHIFT", "GRAVITATIONAL-REDSHIFT VELOCITY"],
            },
        },
    "b10_reportable_pending_exactly_bound": beats[9]["on_screen_copy"]["reportable_now"] == [
        "T1 METADATA-ENUMERATION COUNTS",
        f"{pre_filter} − {dropped} = {post_filter} RECORDED CANDIDATE TABLES",
        f"{gas_count}/{gas_parent} DESCRIPTION-TERM SIDE CHECK",
        "RECALL 7/7 · CONTROLS 0/3 · PRECISION NOT CERTIFIED",
        "T2 RULE CONTRACT FROZEN",
        "T2 CONTRACT DESIGN · 12 DECOYS + 3 ANCHORS · NOT ELIGIBILITY RESULTS",
    ] and beats[9]["on_screen_copy"]["pending"] == [
        f"T2 APPLICATION TO ALL {post_filter} TABLES",
        "ELIGIBLE-TABLE COUNT",
        "ANY METALLICITY OR MZR MEASUREMENT",
    ] and beats[9]["on_screen_copy"]["gate"] == "APPLICATION NOT COMPLETED · NO ELIGIBLE-TABLE COUNT"
 and beats[9]["on_screen_copy"]["close"] == "SINGLE-TABLE METADATA CENSUS · NOT AN MZR MEASUREMENT"
 and beats[9]["narration"] == "The T2 rule contract was frozen after seven gate rounds over twelve decoys and three anchors, but the 157-table eligibility application is not completed, so no eligible-table count or metallicity measurement is reportable yet.",
 }
if not all(source_render_bindings.values()):
    errors.append(f"source-to-render binding failed: {[key for key, value in source_render_bindings.items() if not value]}")

result = {
    "verdict": "PASS" if not errors else "FAIL",
    "beat_count": len(beats),
    "word_count": word_count,
    "planned_seconds": total_seconds,
    "planned_delivered_wpm": round(delivered_wpm, 1),
    "source_checks": source_checks,
    "self_contained_source_freeze": {
        "manifest_sha256": file_sha256(SOURCE / "MANIFEST.json"),
        "file_checks": source_manifest_checks,
        "verdict": "PASS" if len(source_manifest_checks) == 8 and all(source_manifest_checks.values()) else "FAIL",
    },
    "source_render_bindings": source_render_bindings,
    "citation_identity_checks": citation_identity_checks,
    "approved_storyboard_contract_checks": approved_contract_checks,
    "snapshot_manifest_authentication": snapshot_manifest_authentication,
    "display_citations_internal_path_free": not any("display citations expose" in e for e in errors),
    "audience_copy_contract": {
        "projection_sha256": hashlib.sha256(audience_projection.encode()).hexdigest(),
        "prohibited_tokens_found": found_prohibited_audience,
        "all_beats_have_explicit_copy": all(bool(b.get("on_screen_copy")) for b in beats),
    },
    "required_phrase_check": {"missing": missing},
    "forbidden_claim_check": {"found": found_forbidden},
    "visual_semantics": visual_semantics,
    "motion_contract": {
        "maximum_unchanged_evidence_state_seconds": maximum_state_seconds,
        "minimum_reveal_states_per_beat": minimum_states,
        "per_beat": motion_checks,
        "global_change_times_seconds": global_change_times,
        "semantic_global_gaps_seconds": semantic_global_gaps,
        "global_checks": global_motion_checks,
        "verdict": "PASS" if motion_gate_pass else "FAIL",
    },
    "continuity_contract": {
        "per_beat": {beat["id"]: beat["state_handoff"] for beat in beats},
        "handoff_chain": handoff_chain,
        "checks": continuity_checks,
        "verdict": "PASS" if continuity_gate_pass else "FAIL",
    },
    "final_sequence_checks": final_sequence_checks,
    "errors": errors,
    "scope": "proposal validation only; no audio or encoded-candidate claim"
}
out = HERE / "qa/proposal_validation.json"
if "--check" not in sys.argv:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
raise SystemExit(0 if not errors else 1)
