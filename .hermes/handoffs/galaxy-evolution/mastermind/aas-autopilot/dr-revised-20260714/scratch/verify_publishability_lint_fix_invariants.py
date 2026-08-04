import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714")
LINTER = Path("/Users/duhokim/NebulaMind/NebulaMind/tools/ge_tex_publishability_lint.py")
ROUND1 = BASE / "round1"
ROUND2 = BASE / "round2"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cited_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for match in re.finditer(r"\\cite[a-zA-Z*]*(?:\[[^]]*\])*(?:\{([^}]+)\})", text):
        keys.update(key.strip() for key in match.group(1).split(",") if key.strip())
    return keys


def bib_lines(text: str) -> dict[str, str]:
    result = {}
    for line in text.splitlines():
        match = re.search(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", line)
        if match:
            result[match.group(1)] = line
    return result


def normalize_measurement_line(line: str) -> str:
    line = line.replace(r"$\geq$", ">=").replace(r"$\leq$", "<=")
    line = line.replace(r"\geq", ">=").replace(r"\leq", "<=")
    return re.sub(r"\s+", " ", line).strip()


def measurement_numeric_lines(text: str) -> list[str]:
    start_marker = r"\section{Shared parent sample and selection function}"
    start = text.index(start_marker)
    end = text.index(r"\begin{figure", start)
    return [normalize_measurement_line(line) for line in text[start:end].splitlines() if re.search(r"\d", line)]


def extract_prompt_candidate(number: int) -> str:
    paper_id = f"paper_{number:02d}"
    path = ROUND1 / "dr-review-prompts" / f"{paper_id}_round1_review_dr_research_prompt.md"
    text = path.read_text()
    begin = f"----- BEGIN ROUND1 TEX {paper_id} -----\n"
    end = f"\n----- END ROUND1 TEX {paper_id} -----"
    if begin not in text or end not in text:
        raise RuntimeError(f"candidate markers absent for {paper_id}")
    return text.split(begin, 1)[1].split(end, 1)[0]


def normalized_subsequence(required: list[str], observed: list[str]) -> bool:
    cursor = 0
    for line in observed:
        if cursor < len(required) and line == required[cursor]:
            cursor += 1
    return cursor == len(required)


def compile_receipt(round_name: str) -> dict:
    name = "ROUND1_TECTONIC_BUILDS.json" if round_name == "round1" else "ROUND2_TECTONIC_BUILDS.json"
    return json.loads((BASE / round_name / "receipts" / name).read_text())


def verify_compile_rows(round_name: str, expected_count: int) -> tuple[bool, list[dict]]:
    receipt = compile_receipt(round_name)
    rows = []
    for build in receipt["builds"]:
        source = Path(build["source_tex"])
        pdf = Path(build["pdf"])
        log = Path(build["log"])
        row = {
            "paper_id": build["paper_id"],
            "source_hash_match": source.is_file() and sha(source) == build["source_tex_sha256"],
            "pdf_hash_match": pdf.is_file() and sha(pdf) == build["pdf_sha256"],
            "pdf_size_match": pdf.is_file() and pdf.stat().st_size == build["pdf_size"],
            "log_exists": log.is_file(),
            "exit_code": build["exit_code"],
            "compile_clean": build["compile_clean"],
            "undefined_citation_warning": build["undefined_citation_warning"],
            "undefined_reference_warning": build["undefined_reference_warning"],
        }
        row["pass"] = all((row["source_hash_match"], row["pdf_hash_match"], row["pdf_size_match"], row["log_exists"], row["exit_code"] == 0, row["compile_clean"], not row["undefined_citation_warning"], not row["undefined_reference_warning"]))
        rows.append(row)
    return len(rows) == expected_count and all(row["pass"] for row in rows), rows


def main() -> None:
    baseline_round1_validation = ROUND1 / "receipts" / "ROUND1_VALIDATION.json"
    baseline_round2_validation = ROUND2 / "receipts" / "ROUND2_VALIDATION.json"
    baseline_r1 = json.loads(baseline_round1_validation.read_text())
    baseline_r2 = json.loads(baseline_round2_validation.read_text())
    if baseline_r1.get("status") != "PASS" or baseline_r2.get("status") != "PASS":
        raise RuntimeError("pre-lint baseline validation receipts are not PASS")

    round1_rows = []
    pre_round1_text = {}
    for number in range(1, 10):
        paper_id = f"paper_{number:02d}"
        before = extract_prompt_candidate(number)
        after_path = ROUND1 / f"{paper_id}_r1.tex"
        after = after_path.read_text()
        pre_round1_text[number] = before
        before_cites = cited_keys(before)
        after_cites = cited_keys(after)
        before_bib = bib_lines(before)
        after_bib = bib_lines(after)
        before_measurements = measurement_numeric_lines(before)
        after_measurements = measurement_numeric_lines(after)
        retained_bib_lines_unchanged = all(after_bib[key] == before_bib[key] for key in after_bib if key in before_bib)
        row = {
            "paper_id": paper_id,
            "before_candidate_sha256": sha(ROUND1 / "dr-review-prompts" / f"{paper_id}_round1_review_dr_research_prompt.md"),
            "after_tex_sha256": sha(after_path),
            "citation_key_set_unchanged": before_cites == after_cites,
            "citation_key_count": len(after_cites),
            "bibliography_is_exactly_cited_keys": set(after_bib) == after_cites,
            "retained_bibliography_lines_unchanged": retained_bib_lines_unchanged,
            "removed_bibliography_keys": sorted(set(before_bib) - set(after_bib)),
            "added_bibliography_keys": sorted(set(after_bib) - set(before_bib)),
            "measured_numeric_line_count": len(before_measurements),
            "measured_numeric_lines_preserved_after_operator_normalization": normalized_subsequence(before_measurements, after_measurements),
            "documentclass_aastex702": after.startswith(r"\documentclass[twocolumn]{aastex702}"),
            "workflow_phrase_absent": "No public page" not in after,
            "bibliography_width_99": r"\begin{thebibliography}{99}" in after,
        }
        row["pass"] = all((row["citation_key_set_unchanged"], row["bibliography_is_exactly_cited_keys"], row["retained_bibliography_lines_unchanged"], not row["added_bibliography_keys"], row["measured_numeric_lines_preserved_after_operator_normalization"], row["documentclass_aastex702"], row["workflow_phrase_absent"], row["bibliography_width_99"]))
        round1_rows.append(row)

    expected_round2_delta = {
        1: ({"zibetti2026", "demellos2024", "gatto2025"}, set()),
        2: ({"goubert2024corr", "nandi2025", "okane2024", "sampaio2024"}, set()),
        9: ({"nanni2023imanga", "hirschmann2023", "vijayan2023"}, {"imanga2023"}),
    }
    round2_rows = []
    for number in (1, 2, 9):
        paper_id = f"paper_{number:02d}"
        before = pre_round1_text[number]
        source_current = (ROUND1 / f"{paper_id}_r1.tex").read_text()
        output_path = ROUND2 / f"{paper_id}_r2.tex"
        output = output_path.read_text()
        output_cites = cited_keys(output)
        source_cites = cited_keys(source_current)
        adds, removes = expected_round2_delta[number]
        expected_cites = (source_cites - removes) | adds
        output_bib = bib_lines(output)
        original_measurements = measurement_numeric_lines(before)
        output_measurements = measurement_numeric_lines(output)
        row = {
            "paper_id": paper_id,
            "after_tex_sha256": sha(output_path),
            "citation_delta_matches_preverified_round2_sources": output_cites == expected_cites,
            "added_citation_keys": sorted(output_cites - source_cites),
            "removed_or_corrected_citation_keys": sorted(source_cites - output_cites),
            "bibliography_is_exactly_cited_keys": set(output_bib) == output_cites,
            "measured_numeric_line_count": len(original_measurements),
            "measured_numeric_lines_preserved_after_operator_normalization": normalized_subsequence(original_measurements, output_measurements),
            "documentclass_aastex702": output.startswith(r"\documentclass[twocolumn]{aastex702}"),
            "workflow_phrase_absent": "No public page" not in output,
            "bibliography_width_99": r"\begin{thebibliography}{99}" in output,
        }
        row["pass"] = all((row["citation_delta_matches_preverified_round2_sources"], row["bibliography_is_exactly_cited_keys"], row["measured_numeric_lines_preserved_after_operator_normalization"], row["documentclass_aastex702"], row["workflow_phrase_absent"], row["bibliography_width_99"]))
        round2_rows.append(row)

    paths = [ROUND1 / f"paper_{i:02d}_r1.tex" for i in range(1, 10)] + [ROUND2 / f"paper_{i:02d}_r2.tex" for i in (1, 2, 9)]
    lint = subprocess.run(["python3", str(LINTER), "--json", *map(str, paths)], capture_output=True, text=True, check=False)
    lint_json = json.loads(lint.stdout)
    compile_r1_pass, compile_r1_rows = verify_compile_rows("round1", 9)
    compile_r2_pass, compile_r2_rows = verify_compile_rows("round2", 3)

    stale_receipts = {}
    for round_name in ("round1", "round2"):
        receipt_path = BASE / round_name / "receipts" / "WONE_PUBLISHABILITY_LINT_FIX.json"
        receipt = json.loads(receipt_path.read_text())
        rows = []
        for filename, record in sorted(receipt.items()):
            current = BASE / round_name / filename
            rows.append({"file": filename, "recorded_intermediate_post_sha256": record["post_sha256"], "current_final_sha256": sha(current), "matches_final": record["post_sha256"] == sha(current)})
        stale_receipts[round_name] = {"path": str(receipt_path), "sha256": sha(receipt_path), "status": "INTERMEDIATE_HASH_RECEIPT_SUPERSEDED_BY_THIS_VERIFICATION", "rows": rows}

    generated = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    common = {
        "status": "PASS" if all(row["pass"] for row in round1_rows + round2_rows) and lint.returncode == 0 and lint_json == {"error_count": 0, "finding_count": 0, "findings": [], "tex_file_count": 12, "warning_count": 0} and compile_r1_pass and compile_r2_pass else "FAIL",
        "generated_utc": generated,
        "scope": "local account-free verification of WonE publishability-lint fixes",
        "baseline_round1_validation": {"path": str(baseline_round1_validation), "sha256": sha(baseline_round1_validation), "status": baseline_r1["status"]},
        "baseline_round2_validation": {"path": str(baseline_round2_validation), "sha256": sha(baseline_round2_validation), "status": baseline_r2["status"]},
        "normalization_boundary": "Only TeX operator spelling is normalized: $\\geq$ or \\geq -> >= and $\\leq$ or \\leq -> <=. Numeric tokens and all other line content remain exact.",
        "lint": {"exit_code": lint.returncode, **lint_json},
        "compile_round1_pass": compile_r1_pass,
        "compile_round2_pass": compile_r2_pass,
        "round1": round1_rows,
        "round2": round2_rows,
        "compile_round1": compile_r1_rows,
        "compile_round2": compile_r2_rows,
        "stale_intermediate_wone_hash_receipts": stale_receipts,
        "safety": {"browser_or_account_touched": False, "broker_touched": False, "publish_commit_push_performed": False, "database_or_wiki_touched": False},
    }
    for round_name in ("round1", "round2"):
        output = BASE / round_name / "receipts" / "TORI_PUBLISHABILITY_LINT_FIX_VERIFICATION.json"
        output.write_text(json.dumps(common, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": common["status"], "lint": common["lint"], "round1_pass": all(row["pass"] for row in round1_rows), "round2_pass": all(row["pass"] for row in round2_rows), "compile_round1_pass": compile_r1_pass, "compile_round2_pass": compile_r2_pass}, sort_keys=True))
    raise SystemExit(0 if common["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
