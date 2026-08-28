#!/usr/bin/env python3
from copy import deepcopy
from pathlib import Path
import hashlib
import json
import os
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent.parent
VALIDATOR = HERE / "validate_proposal.py"
BASELINE = json.loads((HERE / "STORYBOARD_CANDIDATE.json").read_text())
RECEIPT = HERE / "qa/proposal_validation.json"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_case(name, story, expect_pass, expected_error_fragment=None):
    with tempfile.TemporaryDirectory(prefix="mzr-validator-") as directory:
        candidate = Path(directory) / "STORYBOARD_CANDIDATE.json"
        candidate.write_text(json.dumps(story, ensure_ascii=False, indent=2) + "\n")
        env = dict(os.environ, MZR_STORYBOARD_PATH=str(candidate))
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
