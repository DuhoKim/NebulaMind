import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


def test_cli_emits_manual_review_json_for_clean_c1r(tmp_path):
    subprocess.run([sys.executable, str(ROOT / "fixtures" / "build_mocks.py")], check=True)
    output = tmp_path / "contract_check.json"
    completed = subprocess.run(
        [
            sys.executable,
            str(ROOT / "run_validator.py"),
            "--body",
            str(ROOT / "fixtures" / "clean_c1.md"),
            "--structured",
            str(ROOT / "fixtures" / "clean_c1_structured.json"),
            "--spec",
            str(ROOT / "contract_spec.json"),
            "--output",
            str(output),
        ],
        text=True,
        capture_output=True,
    )
    assert completed.returncode == 2
    result = json.loads(output.read_text())
    assert result["overall"] == "MANUAL_REVIEW_REQUIRED"
    assert not [finding for finding in result["findings"] if finding["status"] == "FAIL"]
