#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind")
SOURCE = ROOT / ".hermes/handoffs/mzr-archive-census-20260805T1857K"
storyboard = json.loads((HERE / "STORYBOARD_CANDIDATE.json").read_text())
beats = storyboard["beats"]

errors = []
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
for beat in beats:
    states = beat.get("timed_reveal_states", [])
    times = [state.get("at_seconds") for state in states]
    duration = float(beat["proposed_seconds"])
    gaps = [b - a for a, b in zip(times, times[1:])] + ([duration - times[-1]] if times else [])
    motion_checks[beat["id"]] = {
        "state_count": len(states),
        "starts_at_zero": bool(times) and times[0] == 0.0,
        "strictly_increasing_and_within_beat": bool(times) and times == sorted(set(times)) and times[-1] < duration,
        "all_states_describe_visible_change": all(bool(state.get("visible_change")) for state in states),
        "maximum_state_gap_seconds": max(gaps) if gaps else None,
        "maximum_state_gap_pass": bool(gaps) and maximum_state_seconds == 4.0 and max(gaps) <= maximum_state_seconds,
        "minimum_state_count_pass": minimum_states == 2 and len(states) >= minimum_states,
    }
motion_gate_pass = all(
    all(value for key, value in checks.items() if key not in {"state_count", "maximum_state_gap_seconds"})
    for checks in motion_checks.values()
)
if not motion_gate_pass:
    errors.append(f"scientific-presentation motion contract failed: {[beat for beat, checks in motion_checks.items() if not all(value for key, value in checks.items() if key not in {'state_count', 'maximum_state_gap_seconds'})]}")


def visible_strings(value):
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [text for item in value for text in visible_strings(item)]
    if isinstance(value, dict):
        return [text for item in value.values() for text in visible_strings(item)]
    return []


audience_projection = "\n".join(
    text
    for beat in beats
    for text in visible_strings({"on_screen_copy": beat["on_screen_copy"], "display_citation": beat["display_citation"]})
)
prohibited_audience = audience_contract.get("prohibited_audience_tokens", [])
found_prohibited_audience = [token for token in prohibited_audience if token.lower() in audience_projection.lower()]
if found_prohibited_audience:
    errors.append(f"prohibited audience-copy tokens: {found_prohibited_audience}")

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
    "scientific_presentation_motion_contract": maximum_state_seconds == 4.0 and minimum_states == 2 and motion_gate_pass,
    "no_standalone_section_divider_holds": "NO STANDALONE SECTION-DIVIDER HOLDS" in motion_contract.get("section_divider_policy", ""),
    "final_reportable_pending_reveal_sequence": all(
        phrase in " ".join(state["visible_change"] for state in beats[-1]["timed_reveal_states"])
        for phrase in ["REPORTABLE NOW", "PENDING", "combined qualified summary"]
    ),
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

result = {
    "verdict": "PASS" if not errors else "FAIL",
    "beat_count": len(beats),
    "word_count": word_count,
    "planned_seconds": total_seconds,
    "planned_delivered_wpm": round(delivered_wpm, 1),
    "source_checks": source_checks,
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
        "verdict": "PASS" if motion_gate_pass else "FAIL",
    },
    "errors": errors,
    "scope": "proposal validation only; no audio or encoded-candidate claim"
}
out = HERE / "qa/proposal_validation.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
raise SystemExit(0 if not errors else 1)
