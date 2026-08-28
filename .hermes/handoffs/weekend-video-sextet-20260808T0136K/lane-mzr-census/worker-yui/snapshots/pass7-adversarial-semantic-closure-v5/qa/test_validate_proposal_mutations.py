#!/usr/bin/env python3
from copy import deepcopy
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent.parent
VALIDATOR = HERE / "validate_proposal.py"
BASELINE = json.loads((HERE / "STORYBOARD_CANDIDATE.json").read_text())
RECEIPT = HERE / "qa/proposal_validation.json"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_case(name, story, expect_pass, expected_error_fragment=None, source_mutation=None):
    with tempfile.TemporaryDirectory(prefix="mzr-validator-") as directory:
        candidate = Path(directory) / "STORYBOARD_CANDIDATE.json"
        candidate.write_text(json.dumps(story, ensure_ascii=False, indent=2) + "\n")
        env = dict(os.environ, MZR_STORYBOARD_PATH=str(candidate))
        if source_mutation:
            source_copy = Path(directory) / "frozen_sources"
            shutil.copytree(HERE / "frozen_sources/pass7", source_copy)
            target = source_copy / source_mutation
            target.chmod(0o644)
            target.write_text(target.read_text() + "\nTAMPERED\n")
            env["MZR_FROZEN_SOURCE_DIR"] = str(source_copy)
        completed = subprocess.run(
            ["python3", str(VALIDATOR), "--check"],
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        result = json.loads(completed.stdout)
        passed = completed.returncode == 0 and result["verdict"] == "PASS"
        diagnostic_ok = expected_error_fragment is None or any(
            expected_error_fragment in error for error in result["errors"]
        )
        return {
            "name": name,
            "expected_pass": expect_pass,
            "actual_pass": passed,
            "diagnostic_ok": diagnostic_ok,
            "errors": result["errors"],
            "test_pass": passed == expect_pass and diagnostic_ok,
        }


receipt_hash_before = sha256(RECEIPT) if RECEIPT.exists() else None
cases = [run_case("baseline", BASELINE, True)]

mutant = deepcopy(BASELINE)
mutant["beats"][4]["on_screen_copy"]["main"] = "999 − 99 = 900 RECORDED CANDIDATE TABLES"
mutant["beats"][4]["on_screen_copy"]["redshift_drop"] = "98 · REDSHIFT AXIS EMPTIED"
mutant["beats"][4]["on_screen_copy"]["abundance_drop"] = "1 · ABUNDANCE AXIS EMPTIED"
cases.append(run_case("fabricated_funnel", mutant, False, "source-to-render binding failed"))

mutant = deepcopy(BASELINE)
mutant["beats"][2]["on_screen_copy"]["cards"] = [
    "ABUNDANCE SEARCH · UCD 9,999 · UCD + NAME 9,999 · GAIN +900 TABLES",
    "MASS SEARCH · UCD 9,998 · UCD + NAME 9,998 · GAIN +800 TABLES",
    "REDSHIFT SEARCH · UCD 9,997 · UCD + NAME 9,997 · GAIN +700 TABLES",
]
cases.append(run_case("fabricated_axis_counts", mutant, False, "source-to-render binding failed"))

mutant = deepcopy(BASELINE)
mutant["beats"][0]["on_screen_copy"]["body"] = mutant["beats"][0]["on_screen_copy"]["body"].replace("mass-search", "STELLAR MASS")
cases.append(run_case("partial_axis_dequalification", mutant, False, "source-to-render binding failed"))

mutant = deepcopy(BASELINE)
mutant["beats"][1]["timed_reveal_states"][0]["evidence_delta"] = "standalone section divider"
mutant["beats"][1]["timed_reveal_states"][0]["visible_change"] = "Show a standalone section divider only."
cases.append(run_case("standalone_divider", mutant, False, "scientific-presentation motion contract failed"))

mutant = deepcopy(BASELINE)
mutant["beats"][6]["timed_reveal_states"][-1]["evidence_delta"] = "scorecards retained"
mutant["beats"][6]["timed_reveal_states"][-1]["visible_change"] = "Hold both scorecards unchanged."
cases.append(run_case("semantic_hold_false_change", mutant, False, "scientific-presentation motion contract failed"))

mutant = deepcopy(BASELINE)
mutant["beats"][9]["timed_reveal_states"] = [
    mutant["beats"][9]["timed_reveal_states"][0],
    mutant["beats"][9]["timed_reveal_states"][3],
    mutant["beats"][9]["timed_reveal_states"][1],
    mutant["beats"][9]["timed_reveal_states"][2],
]
cases.append(run_case("reordered_final_sequence", mutant, False, "scientific-presentation motion contract failed"))

mutant = deepcopy(BASELINE)
mutant["beats"][0]["display_citation"] = "Fabricated Unregistered Count Source 2099"
cases.append(run_case("fabricated_citation", mutant, False, "citation identity checks failed"))

mutant = deepcopy(BASELINE)
for state in mutant["beats"][9]["timed_reveal_states"]:
    state["clause_ids"] = [clause_id for clause_id in state["clause_ids"] if clause_id != "b10_c03"]
cases.append(run_case("unmapped_narration_clause", mutant, False, "scientific-presentation motion contract failed"))

mutant = deepcopy(BASELINE)
mutant["beats"][1]["narration"] = "Each frozen query returned nine million rows, proving physical measurements."
mutant["beats"][1]["narration_clauses"] = [{"clause_id": "b02_c01", "text": mutant["beats"][1]["narration"]}]
for state in mutant["beats"][1]["timed_reveal_states"]:
    state["clause_ids"] = ["b02_c01"]
cases.append(run_case("fabricated_unbound_narration", mutant, False, "approved storyboard contract failed"))

mutant = deepcopy(BASELINE)
mutant["beats"][7]["on_screen_copy"]["limit"] = "PRECISION CERTIFIED"
cases.append(run_case("fabricated_precision_screen", mutant, False, "approved storyboard contract failed"))

mutant = deepcopy(BASELINE)
mutant["beats"][8]["on_screen_copy"]["symbol_meaning_collision_examples"] = ["CERTIFIED T2 ELIGIBLE TABLE"]
cases.append(run_case("fabricated_precision_example", mutant, False, "approved storyboard contract failed"))

mutant = deepcopy(BASELINE)
mutant["beats"][4]["visual_action"] = "Hold a static prose card unchanged for the entire beat."
cases.append(run_case("contradictory_static_build_direction", mutant, False, "approved storyboard contract failed"))

mutant = deepcopy(BASELINE)
mutant["beats"][7]["timed_reveal_states"].pop(3)
cases.append(run_case("state_count_reduced_45_to_44", mutant, False))

mutant = deepcopy(BASELINE)
mutant["beats"][7]["timed_reveal_states"][1]["at_seconds"] = 3.5
cases.append(run_case("semantic_gap_increased_to_3_5_seconds", mutant, False))

mutant = deepcopy(BASELINE)
mutant["beats"][7]["timed_reveal_states"][3]["evidence_delta"] = "decorative dot"
mutant["beats"][7]["timed_reveal_states"][3]["visible_change"] = "Reveal one decorative dot."
cases.append(run_case("decorative_state_substitution", mutant, False))

mutant = deepcopy(BASELINE)
mutant["beats"][5]["visual_action"] += " Full-frame reset; hide the 157 parent and T2 path."
mutant["beats"][5]["timed_reveal_states"][0]["visible_change"] = "Full-frame reset; show isolated giant 62."
cases.append(run_case("hidden_full_frame_reset", mutant, False))

mutant = deepcopy(BASELINE)
mutant["beats"][7]["on_screen_copy"]["stage"] = "T2 ELIGIBILITY RESULTS · APPLICATION COMPLETED"
cases.append(run_case("false_completed_T2_stage", mutant, False))

mutant = deepcopy(BASELINE)
mutant["beats"][7]["on_screen_copy"]["false_extra"] = "62 ELIGIBLE TABLES · T2 PASSED"
cases.append(run_case("extra_62_eligible_claim", mutant, False))

mutant = deepcopy(BASELINE)
mutant["beats"][0]["display_citation"], mutant["beats"][9]["display_citation"] = mutant["beats"][9]["display_citation"], mutant["beats"][0]["display_citation"]
cases.append(run_case("beat_citations_swapped", mutant, False))

mutant = deepcopy(BASELINE)
mutant["beats"][7]["narration_clauses"].pop()
cases.append(run_case("clause_count_reduced_21_to_20", mutant, False))

mutant = deepcopy(BASELINE)
for state in mutant["beats"][5]["timed_reveal_states"]:
    state["clause_ids"] = ["b06_c02"] if state["clause_ids"] == ["b06_c01"] else ["b06_c01"]
cases.append(run_case("semantically_unrelated_clause_mappings_swapped", mutant, False))

mutant = deepcopy(BASELINE)
mutant["beats"][2]["on_screen_copy"]["heading"] = "THREE ADJUDICATED PHYSICAL MEASUREMENTS"
cases.append(run_case("adjudicated_measurements_heading", mutant, False))

mutant = deepcopy(BASELINE)
mutant["beats"][5]["visual_action"] += " Route only 62 into T2."
cases.append(run_case("contradictory_route_only_62_direction", mutant, False))

mutant = deepcopy(BASELINE)
mutant["beats"][9]["on_screen_copy"]["false_extra"] = "12 DECOYS ALONE ARE THE COMPLETE T2 CONTROLS"
cases.append(run_case("incomplete_T2_controls_claim", mutant, False))

cases.append(run_case("tampered_self_contained_source", BASELINE, False, "self-contained source freeze failed", source_mutation="T1_FINDINGS.md"))

receipt_hash_after = sha256(RECEIPT) if RECEIPT.exists() else None
result = {
    "verdict": "PASS" if all(case["test_pass"] for case in cases) and receipt_hash_before == receipt_hash_after else "FAIL",
    "cases": cases,
    "baseline_receipt_hash_before": receipt_hash_before,
    "baseline_receipt_hash_after": receipt_hash_after,
    "check_mode_did_not_write": receipt_hash_before == receipt_hash_after,
}
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["verdict"] == "PASS" else 1)
