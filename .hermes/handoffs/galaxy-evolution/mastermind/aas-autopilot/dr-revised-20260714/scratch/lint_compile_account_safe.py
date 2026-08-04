import hashlib
import json
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
BASE = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714"
LINTER = REPO / "tools/ge_tex_publishability_lint.py"
TECTONIC = Path("/opt/homebrew/bin/tectonic")
ROUND1_INPUTS = json.loads((BASE / "round1/ROUND1_INPUTS.json").read_text())
SOURCE_FIGURES = {
    row["paper_id"]: Path(row["source_tex"]).parent.parent / "figures"
    for row in ROUND1_INPUTS["inputs"]
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_lint(round_name: str, tex_files: list[Path]) -> dict:
    cmd = ["python3", str(LINTER), "--json", *map(str, tex_files)]
    proc = subprocess.run(cmd, cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
    payload = json.loads(proc.stdout)
    payload["exit_code"] = proc.returncode
    payload["missing_bibitem_count"] = sum(row.get("code") == "missing_bibitem" for row in payload["findings"])
    payload["round"] = round_name
    return payload


def compile_one(round_name: str, paper_id: str, source: Path, figures: Path) -> dict:
    build_root = BASE / round_name / "build"
    layout = build_root / ".layouts" / paper_id
    aastex = layout / "aastex"
    figure_link = layout / "figures"
    if layout.exists():
        shutil.rmtree(layout)
    aastex.mkdir(parents=True, exist_ok=True)
    build_root.mkdir(parents=True, exist_ok=True)
    if not figures.is_dir():
        raise RuntimeError(f"{paper_id}: missing original figure directory {figures}")
    figure_link.symlink_to(figures, target_is_directory=True)
    local_tex = aastex / source.name
    shutil.copy2(source, local_tex)
    before_sha = sha(source)
    command = [str(TECTONIC), "--keep-logs", "--outdir", str(build_root), local_tex.name]
    proc = subprocess.run(command, cwd=aastex, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
    after_sha = sha(source)
    pdf = build_root / f"{source.stem}.pdf"
    tectonic_log = build_root / f"{paper_id}.tectonic.stdout.log"
    tectonic_log.write_text(proc.stdout)
    output_lower = proc.stdout.lower()
    row = {
        "paper_id": paper_id,
        "source_tex": str(source),
        "source_tex_sha256": before_sha,
        "source_unchanged_after_compile": before_sha == after_sha,
        "figure_source": str(figures),
        "tectonic_command": command,
        "exit_code": proc.returncode,
        "pdf": str(pdf),
        "pdf_exists": pdf.is_file(),
        "pdf_size": pdf.stat().st_size if pdf.is_file() else 0,
        "pdf_sha256": sha(pdf) if pdf.is_file() else None,
        "log": str(tectonic_log),
        "undefined_citation_warning": "citation" in output_lower and "undefined" in output_lower,
        "undefined_reference_warning": "reference" in output_lower and "undefined" in output_lower,
        "error_excerpt": "\n".join(proc.stdout.splitlines()[-30:]) if proc.returncode else "",
    }
    row["compile_clean"] = (
        row["exit_code"] == 0
        and row["pdf_exists"]
        and row["pdf_size"] > 1000
        and row["source_unchanged_after_compile"]
        and not row["undefined_citation_warning"]
    )
    return row


def process_round(round_name: str, numbers: tuple[int, ...]) -> dict:
    root = BASE / round_name
    tex_files = [root / f"paper_{number:02d}_{'r1' if round_name == 'round1' else 'r2'}.tex" for number in numbers]
    missing = [str(path) for path in tex_files if not path.is_file()]
    if missing:
        raise RuntimeError(f"missing TeX files: {missing}")
    lint = run_lint(round_name, tex_files)
    (root / "receipts").mkdir(parents=True, exist_ok=True)
    (root / "receipts" / f"{round_name.upper()}_PUBLISHABILITY_LINT.json").write_text(json.dumps(lint, indent=2, sort_keys=True) + "\n")
    builds = []
    for number, tex in zip(numbers, tex_files):
        paper_id = f"paper_{number:02d}"
        builds.append(compile_one(round_name, paper_id, tex, SOURCE_FIGURES[paper_id]))
    result = {
        "round": round_name,
        "generated_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "tectonic_available": TECTONIC.is_file(),
        "lint": {
            "tex_file_count": lint["tex_file_count"],
            "exit_code": lint["exit_code"],
            "error_count": lint["error_count"],
            "warning_count": lint["warning_count"],
            "missing_bibitem_count": lint["missing_bibitem_count"],
        },
        "builds": builds,
        "compile_clean_count": sum(row["compile_clean"] for row in builds),
        "all_compile_clean": all(row["compile_clean"] for row in builds),
        "dr_citation_errors_detected": lint["missing_bibitem_count"] > 0 or any(row["undefined_citation_warning"] for row in builds),
    }
    (root / "receipts" / f"{round_name.upper()}_TECTONIC_BUILDS.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def main() -> None:
    if not TECTONIC.is_file():
        raise RuntimeError(f"Tectonic unavailable: {TECTONIC}")
    round1 = process_round("round1", tuple(range(1, 10)))
    round2 = process_round("round2", (1, 2, 9))
    result = {"status": "PASS" if round1["all_compile_clean"] and round2["all_compile_clean"] and not round1["dr_citation_errors_detected"] and not round2["dr_citation_errors_detected"] else "FAIL", "round1": round1, "round2": round2}
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
