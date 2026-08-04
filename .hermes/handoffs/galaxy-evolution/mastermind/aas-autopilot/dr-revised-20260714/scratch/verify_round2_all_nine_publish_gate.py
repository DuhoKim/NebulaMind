import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader

BASE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714")
ROUND1 = BASE / "round1"
ROUND2 = BASE / "round2"
BUILD = ROUND2 / "build"
RECEIPTS = ROUND2 / "receipts"
CLASS = BASE.parent / "latex-publishability-repair" / "aastex7_style_stage" / "aastex702.cls"
LINTER = Path("/Users/duhokim/NebulaMind/NebulaMind/tools/ge_tex_publishability_lint.py")
ROUND1_BUILDS = ROUND1 / "receipts" / "ROUND1_TECTONIC_BUILDS.json"
LINT_RECONCILIATION = RECEIPTS / "TORI_PUBLISHABILITY_LINT_FIX_VERIFICATION.json"
FINAL_VALIDATION = RECEIPTS / "ALL_NINE_VALIDATION_FINAL.json"
ALL9_RECEIPT = RECEIPTS / "ALL_9_VERIFIED.json"
ALL9_MARKDOWN = RECEIPTS / "ALL_9_VERIFIED.md"
PAPERS = tuple(range(1, 10))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def measured_numeric_lines(text):
    start = text.index(r"\section{Shared parent sample and selection function}")
    end = text.index(r"\begin{figure", start)
    return [line for line in text[start:end].splitlines() if re.search(r"\d", line)]


def citation_keys(text):
    keys = []
    for match in re.finditer(r"\\cite[a-zA-Z*]*(?:\[[^]]*\])*\{([^}]+)\}", text):
        keys.extend(key.strip() for key in match.group(1).split(",") if key.strip())
    return keys


def bibliography_keys(text):
    return re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", text)


def run_lint(paths):
    command = ["python3", str(LINTER), "--json", *[str(path) for path in paths]]
    completed = subprocess.run(command, text=True, capture_output=True, timeout=180)
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        payload = {
            "error_count": -1,
            "warning_count": -1,
            "finding_count": -1,
            "findings": [],
            "parse_error": completed.stdout,
        }
    return command, completed, payload


def compile_paper(paper_id, tex_path, figure_source, temp_root):
    work_root = temp_root / paper_id
    aastex = work_root / "aastex"
    aastex.mkdir(parents=True)
    shutil.copy2(tex_path, aastex / tex_path.name)
    shutil.copy2(CLASS, aastex / CLASS.name)
    (work_root / "figures").symlink_to(figure_source, target_is_directory=True)

    command = [
        "tectonic",
        "--keep-logs",
        "--outdir",
        str(BUILD),
        tex_path.name,
    ]
    before_hash = sha(tex_path)
    completed = subprocess.run(command, cwd=aastex, text=True, capture_output=True, timeout=300)
    after_hash = sha(tex_path)
    stdout_log = BUILD / f"{paper_id}.tectonic.stdout.log"
    combined = (
        "$ " + " ".join(command) + "\n\n"
        "--- STDOUT ---\n" + completed.stdout + "\n"
        "--- STDERR ---\n" + completed.stderr
    )
    stdout_log.write_text(combined)

    pdf_path = BUILD / f"{paper_id}_r2.pdf"
    tectonic_log = BUILD / f"{paper_id}_r2.log"
    pdf_exists = pdf_path.is_file()
    page_count = len(PdfReader(str(pdf_path)).pages) if pdf_exists else 0
    log_text = tectonic_log.read_text(errors="replace") if tectonic_log.is_file() else ""
    scan_text = combined + "\n" + log_text
    undefined_citation = bool(re.search(r"(?i)(undefined citations?|citation[^\n]*undefined)", scan_text))
    undefined_reference = bool(re.search(r"(?i)(undefined references?|reference[^\n]*undefined)", scan_text))
    fatal_error = bool(re.search(r"(?im)^error:", scan_text))
    passed = (
        completed.returncode == 0
        and pdf_exists
        and tectonic_log.is_file()
        and page_count > 0
        and before_hash == after_hash
        and not undefined_citation
        and not undefined_reference
        and not fatal_error
    )
    return {
        "command": command,
        "exit_code": completed.returncode,
        "source_unchanged_by_compile": before_hash == after_hash,
        "source_sha256_before": before_hash,
        "source_sha256_after": after_hash,
        "stdout_log": str(stdout_log),
        "stdout_log_sha256": sha(stdout_log),
        "tectonic_log": str(tectonic_log),
        "tectonic_log_sha256": sha(tectonic_log) if tectonic_log.is_file() else None,
        "pdf": str(pdf_path),
        "pdf_exists": pdf_exists,
        "pdf_sha256": sha(pdf_path) if pdf_exists else None,
        "pdf_bytes": pdf_path.stat().st_size if pdf_exists else 0,
        "pdf_pages": page_count,
        "exactly_three_pages": page_count == 3,
        "undefined_citation_warning": undefined_citation,
        "undefined_reference_warning": undefined_reference,
        "fatal_error": fatal_error,
        "pass": passed,
    }


def receipt_hash_reconciliation(paper_id, source_receipt, output_hash, lint_rows, lint_receipt_hash):
    recorded = source_receipt.get("output_tex_sha256")
    if recorded == output_hash:
        return {
            "required": False,
            "source_receipt_output_hash_matches_current": True,
            "pass": True,
        }
    matches = [row for row in lint_rows if row.get("paper_id") == paper_id]
    passed = len(matches) == 1 and matches[0].get("pass") is True and matches[0].get("after_tex_sha256") == output_hash
    return {
        "required": True,
        "source_receipt_output_hash_matches_current": False,
        "reconciliation_receipt": str(LINT_RECONCILIATION),
        "reconciliation_receipt_sha256": lint_receipt_hash,
        "reconciliation_row": matches[0] if len(matches) == 1 else None,
        "reason": "authorized publishability-only repair superseded the earlier per-paper output hash",
        "pass": passed,
    }


def main():
    BUILD.mkdir(parents=True, exist_ok=True)
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    figures_payload = json.loads(ROUND1_BUILDS.read_text())
    figure_sources = {row["paper_id"]: Path(row["figure_source"]) for row in figures_payload["builds"]}
    lint_reconciliation = json.loads(LINT_RECONCILIATION.read_text())
    lint_rows = lint_reconciliation.get("round2", [])
    lint_receipt_hash = sha(LINT_RECONCILIATION)

    tex_paths = [ROUND2 / f"paper_{number:02d}_r2.tex" for number in PAPERS]
    aggregate_command, aggregate_completed, aggregate_lint = run_lint(tex_paths)
    aggregate_lint_log = BUILD / "ALL_9.publishability_lint.json"
    aggregate_lint_log.write_text(json.dumps({
        "command": aggregate_command,
        "exit_code": aggregate_completed.returncode,
        **aggregate_lint,
    }, indent=2, sort_keys=True) + "\n")

    rows = []
    with tempfile.TemporaryDirectory(prefix="wone-round2-all9-") as temp_name:
        temp_root = Path(temp_name)
        for number, output_path in zip(PAPERS, tex_paths):
            paper_id = f"paper_{number:02d}"
            source_path = ROUND1 / f"{paper_id}_r1.tex"
            source_receipt_path = RECEIPTS / f"{paper_id}_sources.json"
            source_receipt = json.loads(source_receipt_path.read_text())
            source_text = source_path.read_text()
            output_text = output_path.read_text()
            source_lines = measured_numeric_lines(source_text)
            output_lines = measured_numeric_lines(output_text)
            source_numeric_tokens = re.findall(r"(?<![A-Za-z])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", "\n".join(source_lines))
            output_numeric_tokens = re.findall(r"(?<![A-Za-z])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", "\n".join(output_lines))
            cites = citation_keys(output_text)
            bibitems = bibliography_keys(output_text)
            cite_set = set(cites)
            bib_set = set(bibitems)
            citation_pass = len(bibitems) == len(bib_set) and cite_set == bib_set
            invariant_pass = source_lines == output_lines and source_numeric_tokens == output_numeric_tokens

            lint_command, lint_completed, lint_payload = run_lint([output_path])
            lint_log = BUILD / f"{paper_id}.publishability_lint.json"
            lint_log.write_text(json.dumps({
                "command": lint_command,
                "exit_code": lint_completed.returncode,
                **lint_payload,
            }, indent=2, sort_keys=True) + "\n")
            lint_pass = (
                lint_completed.returncode == 0
                and lint_payload.get("error_count") == 0
                and lint_payload.get("warning_count") == 0
                and lint_payload.get("finding_count") == 0
            )

            compile_result = compile_paper(paper_id, output_path, figure_sources[paper_id], temp_root)
            output_hash = sha(output_path)
            hash_reconciliation = receipt_hash_reconciliation(
                paper_id, source_receipt, output_hash, lint_rows, lint_receipt_hash
            )
            row = {
                "paper_id": paper_id,
                "round1_source": str(source_path),
                "round1_source_sha256": sha(source_path),
                "round2_source": str(output_path),
                "round2_source_sha256": output_hash,
                "source_receipt": str(source_receipt_path),
                "source_receipt_sha256": sha(source_receipt_path),
                "source_receipt_hash_reconciliation": hash_reconciliation,
                "measured_invariant_line_count": len(source_lines),
                "measured_invariant_lines_exact": source_lines == output_lines,
                "measured_numeric_tokens_exact": source_numeric_tokens == output_numeric_tokens,
                "measured_invariants_pass": invariant_pass,
                "citation_occurrence_count": len(cites),
                "citation_key_count": len(cite_set),
                "bibliography_key_count": len(bibitems),
                "duplicate_bibliography_keys": sorted({key for key in bibitems if bibitems.count(key) > 1}),
                "missing_bibliography_keys": sorted(cite_set - bib_set),
                "unused_bibliography_keys": sorted(bib_set - cite_set),
                "citations_bibliography_one_to_one": citation_pass,
                "lint": {
                    "command": lint_command,
                    "exit_code": lint_completed.returncode,
                    "error_count": lint_payload.get("error_count"),
                    "warning_count": lint_payload.get("warning_count"),
                    "finding_count": lint_payload.get("finding_count"),
                    "log": str(lint_log),
                    "log_sha256": sha(lint_log),
                    "pass": lint_pass,
                },
                "compile": compile_result,
            }
            row["pass"] = (
                invariant_pass
                and citation_pass
                and lint_pass
                and compile_result["pass"]
                and hash_reconciliation["pass"]
            )
            rows.append(row)

    aggregate_lint_pass = (
        aggregate_completed.returncode == 0
        and aggregate_lint.get("error_count") == 0
        and aggregate_lint.get("warning_count") == 0
        and aggregate_lint.get("finding_count") == 0
        and aggregate_lint.get("tex_file_count") == 9
    )
    priority_rows = [row for row in rows if row["paper_id"] in {"paper_06", "paper_07", "paper_08"}]
    priority_pass = (
        len(priority_rows) == 3
        and all(row["pass"] for row in priority_rows)
        and all(row["compile"]["exactly_three_pages"] for row in priority_rows)
    )
    all_pass = aggregate_lint_pass and len(rows) == 9 and all(row["pass"] for row in rows) and priority_pass
    receipt = {
        "generated_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "status": "PASS" if all_pass else "HOLD",
        "all_valid": all_pass,
        "paper_count": len(rows),
        "pdf_count": sum(1 for row in rows if row["compile"]["pdf_exists"]),
        "exact_three_page_pdf_count": sum(1 for row in rows if row["compile"]["exactly_three_pages"]),
        "aggregate_publishability_lint": {
            "command": aggregate_command,
            "exit_code": aggregate_completed.returncode,
            "error_count": aggregate_lint.get("error_count"),
            "warning_count": aggregate_lint.get("warning_count"),
            "finding_count": aggregate_lint.get("finding_count"),
            "tex_file_count": aggregate_lint.get("tex_file_count"),
            "log": str(aggregate_lint_log),
            "log_sha256": sha(aggregate_lint_log),
            "pass": aggregate_lint_pass,
        },
        "priority_new_papers_06_08_pass": priority_pass,
        "priority_new_papers_06_08_exact_three_page_count": sum(
            1 for row in priority_rows if row["compile"]["exactly_three_pages"]
        ),
        "papers": rows,
        "safety": {
            "account_free": True,
            "browser_or_account_touched": False,
            "broker_touched": False,
            "network_used": False,
            "database_or_wiki_touched": False,
            "manuscript_content_changed_by_validator": False,
            "publish_commit_push_performed": False,
        },
        "publish_gate": {
            "validation_blocker_cleared": all_pass,
            "publish_performed": False,
            "next_action": "HOLD for Duho publish gate" if all_pass else "HOLD; repair exact validation failures before publication",
        },
    }
    content = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    FINAL_VALIDATION.write_text(content)
    ALL9_RECEIPT.write_text(content)
    markdown = [
        "# ALL-9-VERIFIED — round-2 publish gate",
        "",
        f"Status: `{'PASS' if all_pass else 'HOLD'}`",
        f"Generated UTC: `{receipt['generated_utc']}`",
        f"PDFs built: `{receipt['pdf_count']}/9`",
        f"Exactly three pages: `{receipt['exact_three_page_pdf_count']}/9`",
        f"Priority papers 06/07/08 exactly three pages: `{receipt['priority_new_papers_06_08_exact_three_page_count']}/3`",
        f"Aggregate publishability lint: `{aggregate_lint.get('error_count')} errors / {aggregate_lint.get('warning_count')} warnings`",
        f"Papers 06/07/08: `{'PASS' if receipt['priority_new_papers_06_08_pass'] else 'HOLD'}`",
        "",
        "No publication, commit, push, browser/account, broker, DB, or wiki action was performed.",
        "Next action: HOLD for Duho publish gate.",
        "",
    ]
    ALL9_MARKDOWN.write_text("\n".join(markdown))
    print(json.dumps({
        "status": receipt["status"],
        "pdf_count": receipt["pdf_count"],
        "exact_three_page_pdf_count": receipt["exact_three_page_pdf_count"],
        "lint_errors": aggregate_lint.get("error_count"),
        "lint_warnings": aggregate_lint.get("warning_count"),
        "priority_new_papers_06_08_pass": receipt["priority_new_papers_06_08_pass"],
        "receipt": str(ALL9_RECEIPT),
        "receipt_sha256": sha(ALL9_RECEIPT),
        "validation": str(FINAL_VALIDATION),
        "validation_sha256": sha(FINAL_VALIDATION),
        "markdown": str(ALL9_MARKDOWN),
        "markdown_sha256": sha(ALL9_MARKDOWN),
    }, sort_keys=True))
    raise SystemExit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
