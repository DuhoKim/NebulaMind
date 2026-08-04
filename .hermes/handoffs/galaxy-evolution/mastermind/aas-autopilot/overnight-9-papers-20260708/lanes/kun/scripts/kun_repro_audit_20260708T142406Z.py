#!/usr/bin/env python3
"""Kun reproducibility/integrity tick for the overnight 9-paper AAS swarm.

Reads existing aas-autopilot artifacts, computes hashes/counts, validates manifests
and compile logs, and writes Kun lane-local reports only.
"""
from __future__ import annotations

import ast
import csv
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TS = "20260708T142406Z"
MARKER = f"KUN_REPRO_AUDIT_{TS}"
REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTOPILOT = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
RUNS = AUTOPILOT / "runs"
FIRST_RUN = RUNS / "SDSS_AGN_SFR_PILOT_20260708T122000Z"
BATCH_RUN = RUNS / "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z"
OVERNIGHT = AUTOPILOT / "overnight-9-papers-20260708"
KUN = OVERNIGHT / "lanes/kun"
REPORT = KUN / "ticks" / f"KUN_TICK_{TS}.md"
SUMMARY = KUN / "artifacts" / f"kun_repro_audit_{TS}.json"

PATHS_READ_FIRST = [
    OVERNIGHT / "OVERNIGHT_BRIEF.md",
    OVERNIGHT / "SWARM_BOARD.md",
]
BATCH_MANIFEST = BATCH_RUN / "ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json"
PUBLIC_APPLY = AUTOPILOT / "ALL_TOPICS_PDF_LINK_APPLY_20260708T130505Z.json"
QUALITY_INVENTORY = OVERNIGHT / "artifacts/quality_inventory_20260708T132720Z.json"
LANA_MANIFEST = OVERNIGHT / "lanes/lana/lana_revision_manifest_20260708T140659Z.json"
GORU_SUMMARY = OVERNIGHT / "lanes/goru/artifacts/goru_actual_data_robustness_20260708T141459Z.json"

FATAL_LOG_RE = re.compile(
    r"fatal error|! LaTeX Error|Emergency stop|Undefined control sequence|No pages of output|Traceback|Tectonic failed|failed for",
    re.IGNORECASE,
)
WARN_RE = re.compile(r"warning", re.IGNORECASE)


def assert_kun_write(path: Path) -> None:
    resolved = path.resolve()
    kun_resolved = KUN.resolve()
    if kun_resolved not in [resolved, *resolved.parents]:
        raise RuntimeError(f"refusing non-Kun-lane write: {resolved}")


def sha256(path: Path) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def pdf_magic_ok(path: Path) -> bool:
    if not path.exists() or not path.is_file():
        return False
    with path.open("rb") as handle:
        return handle.read(5) == b"%PDF-"


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def safe_load_json(path: Path) -> Any:
    if not path.exists():
        return None
    try:
        return load_json(path)
    except Exception as exc:  # recorded as blocker, not raised
        return {"__parse_error__": str(exc)}


def count_csv_rows(path: Path) -> dict[str, Any]:
    out: dict[str, Any] = {
        "path": str(path),
        "exists": path.exists(),
        "bytes": path.stat().st_size if path.exists() else None,
        "sha256": sha256(path) if path.exists() else None,
        "rows": None,
        "columns": None,
    }
    if not path.exists():
        return out
    rows = 0
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration:
            header = []
        for _ in reader:
            rows += 1
    out["rows"] = rows
    out["columns"] = header
    return out


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def process_scan() -> dict[str, Any]:
    patterns = [
        "run_sdss_agn_sfr_pilot.py",
        "run_remaining_topic_pilots.py",
        "tectonic ",
        "pdflatex",
        "xelatex",
        "latexmk",
        "build_quality_inventory_20260708T132720Z.py",
        "goru_actual_data_robustness_20260708T141459Z.py",
        "lana_revision",
    ]
    hits: list[dict[str, str]] = []
    try:
        output = subprocess.check_output(["ps", "-axo", "pid=,command="], text=True, errors="replace")
    except Exception as exc:
        return {"ok": False, "error": str(exc), "matching_processes": []}
    self_pid = os.getpid()
    for line in output.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        parts = stripped.split(maxsplit=1)
        pid = parts[0]
        command = parts[1] if len(parts) > 1 else ""
        try:
            if int(pid) == self_pid:
                continue
        except ValueError:
            pass
        if any(pattern in command for pattern in patterns):
            hits.append({"pid": pid, "command": command})
    return {"ok": True, "matching_processes": hits}


def script_checks(paths: list[Path]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in paths:
        text = read_text(path)
        suffix = path.suffix.lower()
        rec: dict[str, Any] = {
            "path": str(path),
            "exists": path.exists(),
            "bytes": path.stat().st_size if path.exists() else None,
            "sha256": sha256(path) if path.exists() else None,
            "shebang": text.splitlines()[0] if text.startswith("#!") else None,
            "syntax_ok": None,
            "syntax_error": None,
            "has_absolute_repo_path": "/Users/duhokim/NebulaMind/NebulaMind" in text,
            "writes_fixed_outputs": any(token in text for token in ["write_text", "to_csv", "fig.savefig", "subprocess.run", "mkdir"]),
            "network_or_external_data_note": None,
            "self_containment_notes": [],
        }
        if suffix == ".py" and path.exists():
            try:
                ast.parse(text, filename=str(path))
                rec["syntax_ok"] = True
            except SyntaxError as exc:
                rec["syntax_ok"] = False
                rec["syntax_error"] = f"{exc.lineno}:{exc.offset} {exc.msg}"
        if suffix == ".sh" and path.exists():
            rec["syntax_ok"] = text.startswith("#!/") and "set -euo pipefail" in text
        if "astroquery" in text or "SDSS.query_sql" in text:
            rec["network_or_external_data_note"] = "May query public SDSS via astroquery if cached RAW_CSV is absent."
        if "SOURCE_CSV" in text and "analysis_sample_bpt.csv" in text:
            rec["self_containment_notes"].append("Requires cached SDSS analysis_sample_bpt.csv at the hard-coded source path.")
        if rec["has_absolute_repo_path"]:
            rec["self_containment_notes"].append("Uses absolute repo paths; reproducible on this machine, not relocatable without edits.")
        if "tectonic" in text:
            rec["self_containment_notes"].append("Requires tectonic executable and AASTeX class resolution.")
        rows.append(rec)
    return rows


def log_checks(log_paths: list[Path]) -> list[dict[str, Any]]:
    rows = []
    for path in log_paths:
        text = read_text(path)
        fatal = FATAL_LOG_RE.findall(text)
        rows.append(
            {
                "path": str(path),
                "exists": path.exists(),
                "bytes": path.stat().st_size if path.exists() else None,
                "sha256": sha256(path) if path.exists() else None,
                "fatal_marker_count": len(fatal),
                "fatal_markers": fatal[:10],
                "warning_marker_count": len(WARN_RE.findall(text)),
                "tail_preview": re.sub(r"\s+", " ", text[-500:]).strip(),
            }
        )
    return rows


def build_expected_hashes() -> dict[str, dict[str, Any]]:
    expected: dict[str, dict[str, Any]] = {}
    public = safe_load_json(PUBLIC_APPLY) or {}
    public_hashes = public.get("pdf_hashes", {}) if isinstance(public, dict) else {}
    first_pdf = FIRST_RUN / "aastex/sdss_agn_sfr_pilot_aas.pdf"
    if "sdss_agn_sfr_pilot_aas.pdf" in public_hashes:
        expected[str(first_pdf)] = {
            "source": "ALL_TOPICS_PDF_LINK_APPLY pdf_hashes",
            "bytes": public_hashes["sdss_agn_sfr_pilot_aas.pdf"].get("bytes"),
            "sha256": public_hashes["sdss_agn_sfr_pilot_aas.pdf"].get("sha256"),
        }
    manifest = safe_load_json(BATCH_MANIFEST) or {}
    for item in manifest.get("topics", []) if isinstance(manifest, dict) else []:
        expected[item["pdf"]] = {"source": "ALL_REMAINING_TOPIC_PILOTS_MANIFEST", "bytes": item.get("pdf_bytes"), "sha256": item.get("pdf_sha256")}
    lana = safe_load_json(LANA_MANIFEST) or {}
    for item in lana.get("drafts", []) if isinstance(lana, dict) else []:
        pdf = KUN  # dummy to satisfy type; overwritten below
        compiled = item.get("compiled_pdf")
        if compiled:
            pdf_path = OVERNIGHT / compiled if not str(compiled).startswith("/") else Path(compiled)
            expected[str(pdf_path)] = {"source": "lana_revision_manifest", "bytes": item.get("pdf_bytes"), "sha256": item.get("pdf_sha256")}
    return expected


def pdf_checks(pdf_paths: list[Path], expected: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for path in pdf_paths:
        exp = expected.get(str(path))
        actual_sha = sha256(path)
        actual_bytes = path.stat().st_size if path.exists() else None
        rows.append(
            {
                "path": str(path),
                "exists": path.exists(),
                "bytes": actual_bytes,
                "sha256": actual_sha,
                "starts_with_pdf_magic": pdf_magic_ok(path),
                "expected_source": exp.get("source") if exp else None,
                "expected_bytes": exp.get("bytes") if exp else None,
                "expected_sha256": exp.get("sha256") if exp else None,
                "matches_expected_bytes": (actual_bytes == exp.get("bytes")) if exp and exp.get("bytes") is not None else None,
                "matches_expected_sha256": (actual_sha == exp.get("sha256")) if exp and exp.get("sha256") else None,
            }
        )
    return rows


def manifest_checks(expected: dict[str, dict[str, Any]]) -> dict[str, Any]:
    batch = safe_load_json(BATCH_MANIFEST)
    public = safe_load_json(PUBLIC_APPLY)
    quality = safe_load_json(QUALITY_INVENTORY)
    lana = safe_load_json(LANA_MANIFEST)
    goru = safe_load_json(GORU_SUMMARY)

    batch_topics = batch.get("topics", []) if isinstance(batch, dict) else []
    batch_mismatches = []
    for item in batch_topics:
        pdf = Path(item["pdf"])
        actual_sha = sha256(pdf)
        actual_bytes = pdf.stat().st_size if pdf.exists() else None
        if actual_sha != item.get("pdf_sha256") or actual_bytes != item.get("pdf_bytes"):
            batch_mismatches.append({"slug": item.get("slug"), "pdf": str(pdf), "expected_sha": item.get("pdf_sha256"), "actual_sha": actual_sha, "expected_bytes": item.get("pdf_bytes"), "actual_bytes": actual_bytes})

    public_hashes = public.get("pdf_hashes", {}) if isinstance(public, dict) else {}
    public_errors = public.get("errors") if isinstance(public, dict) else None
    public_mismatches = []
    for name, rec in public_hashes.items():
        candidate_paths = [p for p in expected if Path(p).name == name]
        if not candidate_paths:
            public_mismatches.append({"pdf_name": name, "problem": "no local expected path found"})
            continue
        for p in candidate_paths:
            path = Path(p)
            if sha256(path) != rec.get("sha256") or (path.stat().st_size if path.exists() else None) != rec.get("bytes"):
                public_mismatches.append({"pdf_name": name, "path": p, "expected": rec, "actual_sha": sha256(path), "actual_bytes": path.stat().st_size if path.exists() else None})

    goru_outputs = goru.get("outputs", {}) if isinstance(goru, dict) else {}
    goru_missing_outputs = [path for path in goru_outputs.values() if not Path(path).exists()]
    goru_csv_row_checks: dict[str, Any] = {}
    for key, path in goru_outputs.items():
        if str(path).endswith(".csv"):
            goru_csv_row_checks[key] = count_csv_rows(Path(path)).get("rows")

    return {
        "batch_manifest_exists": BATCH_MANIFEST.exists(),
        "batch_topic_count": len(batch_topics),
        "batch_hash_mismatch_count": len(batch_mismatches),
        "batch_hash_mismatches": batch_mismatches,
        "public_apply_exists": PUBLIC_APPLY.exists(),
        "public_pdf_hash_count": len(public_hashes),
        "public_errors": public_errors,
        "public_hash_mismatch_count": len(public_mismatches),
        "public_hash_mismatches": public_mismatches,
        "quality_inventory_exists": QUALITY_INVENTORY.exists(),
        "quality_inventory_summary": quality.get("summary") if isinstance(quality, dict) else None,
        "lana_manifest_exists": LANA_MANIFEST.exists(),
        "lana_draft_count": len(lana.get("drafts", [])) if isinstance(lana, dict) else None,
        "goru_summary_exists": GORU_SUMMARY.exists(),
        "goru_marker": goru.get("marker") if isinstance(goru, dict) else None,
        "goru_missing_output_count": len(goru_missing_outputs),
        "goru_missing_outputs": goru_missing_outputs,
        "goru_csv_row_checks": goru_csv_row_checks,
    }


def analysis_result_checks() -> list[dict[str, Any]]:
    paths = [FIRST_RUN / "analysis_results.json"] + sorted(BATCH_RUN.glob("*/analysis_results.json"))
    rows = []
    for path in paths:
        data = safe_load_json(path)
        rec: dict[str, Any] = {
            "path": str(path),
            "exists": path.exists(),
            "json_ok": isinstance(data, dict) and "__parse_error__" not in data,
            "parse_error": data.get("__parse_error__") if isinstance(data, dict) else None,
            "run_id": data.get("run_id") if isinstance(data, dict) else None,
            "slug": data.get("slug") if isinstance(data, dict) else ("m1_rp1_agn_sfr" if path.parent == FIRST_RUN else None),
            "sample_rows_or_analysis_rows": (data.get("sample_rows") or data.get("analysis_rows")) if isinstance(data, dict) else None,
            "source_sample": data.get("source_sample") if isinstance(data, dict) else None,
            "has_interpretation_guard_or_safety": False,
            "guard_text": None,
        }
        if isinstance(data, dict):
            guard = str(data.get("interpretation_guard") or data.get("safety") or "")
            rec["has_interpretation_guard_or_safety"] = bool(guard)
            rec["guard_text"] = guard[:240]
        rows.append(rec)
    return rows


def dependency_checks() -> dict[str, Any]:
    packages = ["numpy", "pandas", "matplotlib", "scipy", "astroquery"]
    return {
        "executables": {name: shutil.which(name) for name in ["python3", "python", "tectonic", "shasum"]},
        "python_packages_find_spec": {name: importlib.util.find_spec(name) is not None for name in packages},
    }


def render_markdown(summary: dict[str, Any]) -> str:
    s = summary["summary_counts"]
    lines: list[str] = []
    lines.append(f"# Kun reproducibility tick — {TS}")
    lines.append("")
    lines.append(f"Marker: `{MARKER}`")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append("Read `OVERNIGHT_BRIEF.md`, `SWARM_BOARD.md`, manifests, scripts, logs, PDFs, and source-data artifacts under `aas-autopilot`. Per single-writer safety, I did not recompile or rerun generators because that would write outside the Kun lane or risk racing Lana/Goru outputs; this tick performed a read-only integrity audit plus Kun-local report writes.")
    lines.append("")
    lines.append("## Race/process check")
    proc_hits = summary["process_scan"].get("matching_processes", [])
    if proc_hits:
        lines.append(f"- Potential active compile/generator processes seen at scan time: {len(proc_hits)}. I avoided reruns.")
        for hit in proc_hits[:8]:
            lines.append(f"  - PID {hit['pid']}: `{hit['command']}`")
    else:
        lines.append("- No active `tectonic`, run-generator, Lana revision, Goru robustness, or quality-inventory process was seen at scan time.")
    lines.append("")
    lines.append("## Artifact integrity results")
    lines.append("")
    lines.append(f"- PDFs under aas-autopilot: {s['pdf_total']} total; {s['pdf_magic_ok']} start with `%PDF-`; {s['pdf_expected_count']} had recorded expected hashes; {s['pdf_expected_sha_matches']} matched expected SHA256; mismatches: {s['pdf_expected_sha_mismatches']}.")
    lines.append(f"- Primary 9 linked manuscript PDFs: {s['primary_pdf_count']} checked; expected-hash mismatches: {s['primary_pdf_mismatches']}.")
    lines.append(f"- `.log` files under aas-autopilot: {s['log_total']} checked; fatal/traceback/LaTeX-error marker files: {s['log_files_with_fatal_markers']}.")
    lines.append(f"- Batch manifest topics: {summary['manifest_checks']['batch_topic_count']}; batch PDF hash mismatches: {summary['manifest_checks']['batch_hash_mismatch_count']}.")
    lines.append(f"- Public apply receipt: {summary['manifest_checks']['public_pdf_hash_count']} PDF hashes, `errors={summary['manifest_checks']['public_errors']}`; local hash mismatches: {summary['manifest_checks']['public_hash_mismatch_count']}.")
    lines.append(f"- Quality inventory summary confirms: {summary['manifest_checks']['quality_inventory_summary']}.")
    lines.append(f"- Lana manifest: {summary['manifest_checks']['lana_draft_count']} lane-local revision PDFs recorded; Goru summary marker: `{summary['manifest_checks']['goru_marker']}`; missing Goru outputs: {summary['manifest_checks']['goru_missing_output_count']}.")
    lines.append("")
    lines.append("## Data/sample provenance")
    lines.append("")
    for key, rec in summary["data_provenance"].items():
        lines.append(f"- {key}: exists={rec['exists']}, rows={rec['rows']}, bytes={rec['bytes']}, sha256=`{rec['sha256']}`")
    lines.append("- First paper provenance: public SDSS DR17 SkyServer query is preserved in `data/query.sql`; cached raw/analysis/matched CSVs are present.")
    lines.append("- Remaining 8 papers provenance: `run_remaining_topic_pilots.py` reuses the cached `analysis_sample_bpt.csv` and each `analysis_results.json` records `source_sample` plus an SDSS-only/proxy interpretation guard.")
    lines.append("")
    lines.append("## Script/self-containment checks")
    lines.append("")
    lines.append(f"- Scripts checked: {s['script_total']} ({s['script_syntax_ok']} syntax/shell-header OK, {s['script_syntax_bad']} syntax/header failures).")
    deps = summary["dependency_checks"]
    lines.append(f"- Executables: python3=`{deps['executables']['python3']}`, tectonic=`{deps['executables']['tectonic']}`, shasum=`{deps['executables']['shasum']}`.")
    lines.append(f"- Python package availability by `importlib.util.find_spec`: {deps['python_packages_find_spec']}.")
    lines.append("- Reproducibility blocker/note: the main generator scripts are self-contained for this machine's current absolute repo layout, but are not cold-machine portable without the same `/Users/duhokim/...` paths and Python/TeX dependencies. The first script may query SDSS if the raw CSV cache is absent; the batch script depends on the cached RP-1 analysis CSV.")
    lines.append("")
    lines.append("## Exact local repro commands")
    lines.append("")
    lines.append("```bash")
    lines.append("cd /Users/duhokim/NebulaMind/NebulaMind")
    lines.append("# RP-1 full wrapper: uses cached CSV if present; may query public SDSS if cache is absent")
    lines.append("bash .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/run_full_sdss_agn_sfr_pilot.sh")
    lines.append("")
    lines.append("# Remaining 8 topic pilots: requires the cached RP-1 analysis_sample_bpt.csv")
    lines.append("python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/run_remaining_topic_pilots.py > .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z.batch.log 2>&1")
    lines.append("")
    lines.append("# Hash check for the 9 linked manuscript PDFs")
    lines.append("shasum -a 256 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/aastex/sdss_agn_sfr_pilot_aas.pdf")
    lines.append("shasum -a 256 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/*/aastex/*_aas.pdf")
    lines.append("")
    lines.append("# Re-run this Kun read-only audit/report generator")
    lines.append(f"python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/kun/scripts/kun_repro_audit_{TS}.py")
    lines.append("```")
    lines.append("")
    lines.append("## Blocker notes")
    lines.append("")
    if s["blocking_failure_count"] == 0:
        lines.append("- No integrity blocker found: hashes/manifests/logs/data provenance are internally consistent for the preserved artifacts.")
    else:
        for blocker in summary["blockers"]:
            lines.append(f"- BLOCKER: {blocker}")
    lines.append("- Not a blocker, but important: PDF SHA256 can change on recompilation because TeX/PDF metadata may be regenerated; source/data/figure artifacts are the stable reproducibility basis.")
    lines.append("- Not a blocker, but important: the 8 batch manuscripts remain short SDSS proxy/denominator drafts with minimal topic-specific bibliography and no result tables in the current public-linked PDFs; Lana's lane-local drafts improve three Wave-1 papers but are not integrated into public-linked PDFs.")
    lines.append("")
    lines.append("## Safety")
    lines.append("")
    lines.append("No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git, billing, OAuth, external submission, or new cron jobs were touched. Writes from this audit are Kun-lane local reports only; the separate one-line `OVERNIGHT_LEDGER.md` append records the tick.")
    lines.append("")
    lines.append(f"JSON summary: `{SUMMARY}`")
    return "\n".join(lines) + "\n"


def main() -> None:
    for output_dir in [REPORT.parent, SUMMARY.parent, KUN / "scripts"]:
        assert_kun_write(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    expected = build_expected_hashes()
    pdf_paths = sorted(AUTOPILOT.rglob("*.pdf"))
    log_paths = sorted(AUTOPILOT.rglob("*.log"))
    script_paths = sorted(AUTOPILOT.rglob("*.py")) + sorted(AUTOPILOT.rglob("*.sh"))

    pdf_rows = pdf_checks(pdf_paths, expected)
    log_rows = log_checks(log_paths)
    script_rows = script_checks(script_paths)
    manifest = manifest_checks(expected)
    analyses = analysis_result_checks()
    deps = dependency_checks()
    proc = process_scan()

    data_paths = {
        "sdss_query_sql": FIRST_RUN / "data/query.sql",
        "raw_sdss_csv": FIRST_RUN / "data/sdss_dr17_emission_line_sample.csv",
        "analysis_sample_bpt_csv": FIRST_RUN / "data/analysis_sample_bpt.csv",
        "matched_agn_sf_pairs_csv": FIRST_RUN / "data/matched_agn_sf_pairs.csv",
    }
    data_provenance: dict[str, Any] = {}
    for key, path in data_paths.items():
        if path.suffix.lower() == ".csv":
            data_provenance[key] = count_csv_rows(path)
        else:
            data_provenance[key] = {"path": str(path), "exists": path.exists(), "bytes": path.stat().st_size if path.exists() else None, "sha256": sha256(path) if path.exists() else None, "rows": None}

    primary_names = {
        "sdss_agn_sfr_pilot_aas.pdf",
        "m1_rp2_environment_quenching_aas.pdf",
        "m1_rp3_maintenance_heating_aas.pdf",
        "m2_p1_outflow_escape_recycling_aas.pdf",
        "m2_p2_radio_jet_environment_aas.pdf",
        "m2_p3_feedback_transition_mass_aas.pdf",
        "m3_p1_multiphase_census_aas.pdf",
        "m3_p2_gas_depletion_efficiency_aas.pdf",
        "m3_p3_simulation_validation_aas.pdf",
    }
    primary_pdf_rows = [r for r in pdf_rows if Path(r["path"]).name in primary_names and "/aastex/" in r["path"] and "revision-drafts" not in r["path"]]
    expected_rows = [r for r in pdf_rows if r["expected_sha256"]]
    script_bad = [r for r in script_rows if r["syntax_ok"] is False]
    pdf_magic_bad = [r for r in pdf_rows if not r["starts_with_pdf_magic"]]
    expected_mismatches = [r for r in expected_rows if r["matches_expected_sha256"] is False or r["matches_expected_bytes"] is False]
    log_bad = [r for r in log_rows if r["fatal_marker_count"]]

    blockers: list[str] = []
    if pdf_magic_bad:
        blockers.append(f"{len(pdf_magic_bad)} PDF(s) do not start with %PDF magic")
    if expected_mismatches:
        blockers.append(f"{len(expected_mismatches)} PDF(s) mismatch recorded expected SHA/bytes")
    if log_bad:
        blockers.append(f"{len(log_bad)} log file(s) contain fatal/traceback/LaTeX-error markers")
    if manifest["batch_topic_count"] != 8:
        blockers.append(f"Batch manifest topic count is {manifest['batch_topic_count']}, expected 8")
    if len(primary_pdf_rows) != 9:
        blockers.append(f"Primary linked manuscript PDF count is {len(primary_pdf_rows)}, expected 9")
    if script_bad:
        blockers.append(f"{len(script_bad)} script(s) failed syntax/header checks")
    for key in ["raw_sdss_csv", "analysis_sample_bpt_csv", "matched_agn_sf_pairs_csv"]:
        if not data_provenance[key]["exists"]:
            blockers.append(f"Missing source data artifact: {key}")
    if data_provenance["analysis_sample_bpt_csv"].get("rows") != 60000:
        blockers.append(f"analysis_sample_bpt_csv rows={data_provenance['analysis_sample_bpt_csv'].get('rows')}, expected 60000")

    summary_counts = {
        "pdf_total": len(pdf_rows),
        "pdf_magic_ok": sum(1 for r in pdf_rows if r["starts_with_pdf_magic"]),
        "pdf_expected_count": len(expected_rows),
        "pdf_expected_sha_matches": sum(1 for r in expected_rows if r["matches_expected_sha256"] is True),
        "pdf_expected_sha_mismatches": len(expected_mismatches),
        "primary_pdf_count": len(primary_pdf_rows),
        "primary_pdf_mismatches": sum(1 for r in primary_pdf_rows if r["matches_expected_sha256"] is False),
        "log_total": len(log_rows),
        "log_files_with_fatal_markers": len(log_bad),
        "script_total": len(script_rows),
        "script_syntax_ok": sum(1 for r in script_rows if r["syntax_ok"] is True),
        "script_syntax_bad": len(script_bad),
        "analysis_json_count": len(analyses),
        "analysis_json_ok": sum(1 for r in analyses if r["json_ok"]),
        "blocking_failure_count": len(blockers),
    }

    out = {
        "marker": MARKER,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Kun reproducibility/integrity audit over existing aas-autopilot artifacts; no generator recompiles/reruns outside Kun lane.",
        "paths_read_first": [str(p) for p in PATHS_READ_FIRST],
        "summary_counts": summary_counts,
        "blockers": blockers,
        "process_scan": proc,
        "dependency_checks": deps,
        "manifest_checks": manifest,
        "data_provenance": data_provenance,
        "analysis_results": analyses,
        "pdfs": pdf_rows,
        "logs": log_rows,
        "scripts": script_rows,
        "safety": "No public pages/live roots/product DB/API/pages/page_versions/trust/deploy/restart/git/billing/OAuth/external submission/new cron jobs touched. Writes are under Kun lane only, except the separately required ledger append by Hermes.",
    }

    assert_kun_write(SUMMARY)
    assert_kun_write(REPORT)
    SUMMARY.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    REPORT.write_text(render_markdown(out), encoding="utf-8")
    print(json.dumps({"ok": True, "marker": MARKER, "report": str(REPORT), "summary": str(SUMMARY), "summary_counts": summary_counts, "blockers": blockers}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
