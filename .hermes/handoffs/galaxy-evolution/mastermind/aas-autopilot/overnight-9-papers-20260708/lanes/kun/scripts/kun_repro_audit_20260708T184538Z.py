#!/usr/bin/env python3
"""Kun reproducibility/integrity audit for the overnight 9-paper AAS swarm.

Read-mostly audit over aas-autopilot artifacts. This script writes only Kun
lane-local report/JSON artifacts and deliberately avoids rerunning manuscript
or data generators that would race other lanes or overwrite run products.
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
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

TS = "20260708T184538Z"
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
SCRIPT_PATH = KUN / "scripts" / f"kun_repro_audit_{TS}.py"
BRIEF = OVERNIGHT / "OVERNIGHT_BRIEF.md"
SWARM_BOARD = OVERNIGHT / "SWARM_BOARD.md"
LEDGER = OVERNIGHT / "OVERNIGHT_LEDGER.md"
BATCH_MANIFEST = BATCH_RUN / "ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json"
PUBLIC_APPLY = AUTOPILOT / "ALL_TOPICS_PDF_LINK_APPLY_20260708T130505Z.json"
QUALITY_INVENTORY = OVERNIGHT / "artifacts/quality_inventory_20260708T132720Z.json"
SELECTION_MANIFEST = OVERNIGHT / "lanes/tori/selection-function-attrition/20260708T155514Z/selection_function_attrition_artifact_manifest_20260708T155514Z.json"

PRIMARY_PDF_NAMES = {
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

FATAL_LOG_RE = re.compile(
    r"fatal error|! LaTeX Error|Emergency stop|Undefined control sequence|No pages of output|Traceback|Tectonic failed|failed for|ERROR:",
    re.IGNORECASE,
)
WARNING_RE = re.compile(r"warning", re.IGNORECASE)

PATH_KEYS = {
    "path", "pdf", "compiled_pdf", "draft_pdf", "figure_pdf", "tex", "draft_tex",
    "source_tex", "source_json", "compile_log", "changes_md", "summary_json",
    "tick_report_md", "inventory_csv", "regression_sensitivity_csv",
    "alternate_bin_target_vector_csv", "paper_table_candidates_csv",
    "topic_bootstrap_summary_csv", "coefficient_figure",
}
SHA_KEYS = ("sha256", "pdf_sha256")
BYTE_KEYS = ("bytes", "pdf_bytes")


def inside(path: Path, root: Path) -> bool:
    try:
        p = str(path.resolve())
        r = str(root.resolve())
    except Exception:
        p = str(path)
        r = str(root)
    return p == r or p.startswith(r + os.sep)


def assert_kun_write(path: Path) -> None:
    if not inside(path, KUN):
        raise RuntimeError(f"refusing non-Kun-lane write: {path}")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO))
    except Exception:
        return str(path)


def sha256(path: Path) -> Optional[str]:
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


def read_text(path: Path) -> str:
    if not path.exists() or not path.is_file():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def safe_json(path: Path) -> Any:
    if not path.exists() or not path.is_file():
        return {"__missing__": True}
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except Exception as exc:
        return {"__parse_error__": str(exc)}


def json_ok(data: Any) -> bool:
    return not (isinstance(data, dict) and (data.get("__missing__") or data.get("__parse_error__")))


def normalize_path(value: Any, base: Optional[Path] = None) -> Optional[Path]:
    if value is None or value == "":
        return None
    if not isinstance(value, (str, os.PathLike)):
        return None
    s = str(value)
    if "\n" in s or "\r" in s or len(s) > 600:
        return None
    # Avoid treating arbitrary prose as a path.
    if not any(token in s for token in ["/", ".pdf", ".tex", ".json", ".csv", ".md", ".log", ".png", ".py", ".sh", ".sql"]):
        return None
    p = Path(s)
    if p.is_absolute():
        return p
    if s.startswith(".hermes/"):
        return REPO / p
    if s.startswith("runs/"):
        return AUTOPILOT / p
    if s.startswith(("lanes/", "ticks/", "artifacts/", "visible-panes/", "scripts/")):
        return OVERNIGHT / p
    if base is not None:
        return base / p
    return AUTOPILOT / p


def count_csv_rows(path: Path) -> Dict[str, Any]:
    rec: Dict[str, Any] = {
        "path": str(path),
        "relative_path": rel(path),
        "exists": path.exists(),
        "bytes": path.stat().st_size if path.exists() else None,
        "sha256": sha256(path) if path.exists() else None,
        "rows": None,
        "columns": None,
    }
    if not path.exists() or not path.is_file():
        return rec
    rows = 0
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration:
            header = []
        for _ in reader:
            rows += 1
    rec["rows"] = rows
    rec["columns"] = header
    return rec


def add_expected(
    expected: Dict[str, Dict[str, Any]],
    path: Optional[Path],
    source: str,
    sha_value: Optional[Any] = None,
    bytes_value: Optional[Any] = None,
    kind: str = "artifact",
) -> None:
    if path is None:
        return
    key = str(path)
    rec = expected.setdefault(key, {"sources": [], "sha256": None, "bytes": None, "conflicts": [], "kind": kind})
    rec["sources"].append(source)
    if sha_value:
        if rec["sha256"] and rec["sha256"] != sha_value:
            rec["conflicts"].append({"field": "sha256", "old": rec["sha256"], "new": sha_value, "source": source})
        else:
            rec["sha256"] = str(sha_value)
    if bytes_value is not None:
        try:
            b = int(bytes_value)
        except Exception:
            b = None
        if b is not None:
            if rec["bytes"] is not None and rec["bytes"] != b:
                rec["conflicts"].append({"field": "bytes", "old": rec["bytes"], "new": b, "source": source})
            else:
                rec["bytes"] = b


def primary_paths_from_manifests(batch: Any) -> Dict[str, Path]:
    out = {"sdss_agn_sfr_pilot_aas.pdf": FIRST_RUN / "aastex/sdss_agn_sfr_pilot_aas.pdf"}
    if isinstance(batch, dict):
        for item in batch.get("topics", []):
            if isinstance(item, dict) and item.get("pdf_name") and item.get("pdf"):
                p = normalize_path(item.get("pdf"))
                if p is not None:
                    out[str(item["pdf_name"])] = p
    return out


def collect_expected_from_manifest_dict(expected: Dict[str, Dict[str, Any]], data: Any, source: str, base: Optional[Path]) -> None:
    """Conservative recursive path extraction for lane manifests.

    Important: many lane manifest rows contain one manuscript PDF hash plus
    additional paths (source_json, changes_md, figure_pdf). Do not attach that
    manuscript hash to every sibling path; attach hashes only to explicit
    artifact `path` rows or manuscript-PDF keys.
    """
    if isinstance(data, dict):
        sha_value = next((data.get(k) for k in SHA_KEYS if data.get(k)), None)
        bytes_value = next((data.get(k) for k in BYTE_KEYS if data.get(k) is not None), None)
        for key, value in data.items():
            is_path_key = key in PATH_KEYS or key.endswith("_path") or key.endswith("_pdf") or key.endswith("_csv") or key.endswith("_json") or key.endswith("_md") or key.endswith("_log") or key.endswith("_tex")
            if is_path_key:
                p = normalize_path(value, base=base)
                if p is not None and (inside(p, AUTOPILOT) or inside(p, REPO)):
                    hash_for_path = None
                    bytes_for_path = None
                    if key == "path" and sha_value:
                        # Artifact manifests/inventories usually store path+sha in the same row.
                        hash_for_path = sha_value
                        bytes_for_path = bytes_value
                    elif key in {"pdf", "compiled_pdf", "draft_pdf"} and sha_value:
                        # Lane manuscript manifests store pdf/pdf_sha256/pdf_bytes in one dict.
                        hash_for_path = sha_value
                        bytes_for_path = bytes_value
                    add_expected(expected, p, source, hash_for_path, bytes_for_path)
            collect_expected_from_manifest_dict(expected, value, source, base)
    elif isinstance(data, list):
        for item in data:
            collect_expected_from_manifest_dict(expected, item, source, base)


def collect_inventory_csvs(expected: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    inventories = sorted([p for p in AUTOPILOT.rglob("*.csv") if "inventory" in p.name.lower()])
    rows: List[Dict[str, Any]] = []
    for inv in inventories:
        parsed = 0
        added = 0
        if inv.exists():
            with inv.open(newline="", encoding="utf-8", errors="replace") as handle:
                reader = csv.DictReader(handle)
                for row in reader:
                    parsed += 1
                    path_value = row.get("path") or row.get("artifact") or row.get("file")
                    p = normalize_path(path_value)
                    if p is None:
                        continue
                    add_expected(
                        expected,
                        p,
                        inv.name,
                        row.get("sha256") or None,
                        row.get("bytes") or None,
                        kind="inventory_row",
                    )
                    added += 1
        rows.append({"path": str(inv), "relative_path": rel(inv), "rows_seen": parsed, "expected_rows_added": added})
    return rows


def build_expected_artifacts() -> Tuple[Dict[str, Dict[str, Any]], Dict[str, Any]]:
    expected: Dict[str, Dict[str, Any]] = {}
    details: Dict[str, Any] = {}
    batch = safe_json(BATCH_MANIFEST)
    public = safe_json(PUBLIC_APPLY)
    details["batch_manifest_json_ok"] = json_ok(batch)
    details["public_apply_json_ok"] = json_ok(public)
    primary_by_name = primary_paths_from_manifests(batch)

    # Primary/batch expected PDFs and declared support files.
    if isinstance(batch, dict):
        for item in batch.get("topics", []):
            if isinstance(item, dict):
                add_expected(expected, normalize_path(item.get("pdf")), BATCH_MANIFEST.name, item.get("pdf_sha256"), item.get("pdf_bytes"), "batch_pdf")
                for k in ["tex", "compile_log", "figure_pdf"]:
                    add_expected(expected, normalize_path(item.get(k)), BATCH_MANIFEST.name, None, None, k)

    if isinstance(public, dict):
        for name, rec in (public.get("pdf_hashes") or {}).items():
            if isinstance(rec, dict):
                add_expected(expected, primary_by_name.get(name), PUBLIC_APPLY.name, rec.get("sha256"), rec.get("bytes"), "public_apply_pdf")

    # First run primary PDF is in public receipt; add its TeX/log/figures for existence.
    add_expected(expected, FIRST_RUN / "aastex/sdss_agn_sfr_pilot_aas.pdf", "first_run_primary", None, None, "primary_pdf")
    add_expected(expected, FIRST_RUN / "aastex/sdss_agn_sfr_pilot_aas.tex", "first_run_primary", None, None, "primary_tex")
    add_expected(expected, FIRST_RUN / "aastex/compile.log", "first_run_primary", None, None, "primary_compile_log")

    # Lane-local manifests/receipts.
    manifest_paths = sorted([p for p in AUTOPILOT.rglob("*.json") if "manifest" in p.name.lower() or p in {BATCH_MANIFEST, PUBLIC_APPLY}])
    lane_manifest_count = 0
    for manifest in manifest_paths:
        data = safe_json(manifest)
        if inside(manifest, OVERNIGHT / "lanes") or manifest in {BATCH_MANIFEST, PUBLIC_APPLY}:
            lane_manifest_count += 1
            collect_expected_from_manifest_dict(expected, data, manifest.name, manifest.parent)

    # Tori selection raw payloads are declared by count rather than all hashes.
    selection = safe_json(SELECTION_MANIFEST)
    raw_dir = SELECTION_MANIFEST.parent / "raw_sdss_payloads"
    details["selection_manifest_json_ok"] = json_ok(selection)
    details["selection_raw_payload_count_json_expected"] = selection.get("raw_payload_count_json") if isinstance(selection, dict) else None
    details["selection_raw_payload_count_sql_expected"] = selection.get("raw_payload_count_sql") if isinstance(selection, dict) else None
    details["selection_raw_payload_count_json_actual"] = len(list(raw_dir.glob("*.json"))) if raw_dir.exists() else 0
    details["selection_raw_payload_count_sql_actual"] = len(list(raw_dir.glob("*.sql"))) if raw_dir.exists() else 0

    inventory_rows = collect_inventory_csvs(expected)
    details["manifest_like_json_count"] = len(manifest_paths)
    details["manifest_like_json_ok_count"] = sum(1 for p in manifest_paths if json_ok(safe_json(p)))
    details["lane_manifest_like_processed_count"] = lane_manifest_count
    details["inventory_csvs"] = inventory_rows
    return expected, details


def is_compileish_log(path: Path, text: str) -> bool:
    if path.name == "compile.log" or path.name.startswith("compile_"):
        return True
    if "revision-drafts" in str(path) and path.suffix == ".log":
        return True
    if "Output written on" in text and ".pdf" in text:
        return True
    if "Running xdvipdfmx" in text or ("Writing `" in text and ".pdf`" in text):
        return True
    return False


def log_checks(log_paths: List[Path]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for p in log_paths:
        text = read_text(p)
        fatal = FATAL_LOG_RE.findall(text)
        out.append({
            "path": str(p),
            "relative_path": rel(p),
            "exists": p.exists(),
            "bytes": p.stat().st_size if p.exists() else None,
            "sha256": sha256(p) if p.exists() else None,
            "compileish": is_compileish_log(p, text),
            "fatal_marker_count": len(fatal),
            "fatal_markers": fatal[:12],
            "warning_marker_count": len(WARNING_RE.findall(text)),
            "tail_preview": re.sub(r"\s+", " ", text[-500:]).strip(),
        })
    return out


def bash_syntax_ok(path: Path) -> Tuple[Optional[bool], Optional[str]]:
    bash = shutil.which("bash") or "/bin/bash"
    try:
        proc = subprocess.run([bash, "-n", str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=20)
        return proc.returncode == 0, (proc.stderr.strip() or proc.stdout.strip() or None)
    except Exception as exc:
        return False, str(exc)


def script_checks(script_paths: List[Path]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for p in script_paths:
        text = read_text(p)
        rec: Dict[str, Any] = {
            "path": str(p),
            "relative_path": rel(p),
            "exists": p.exists(),
            "bytes": p.stat().st_size if p.exists() else None,
            "sha256": sha256(p) if p.exists() else None,
            "shebang": text.splitlines()[0] if text.startswith("#!") else None,
            "syntax_ok": None,
            "syntax_error": None,
            "has_absolute_repo_path": str(REPO) in text,
            "has_hardcoded_timestamp": bool(re.search(r"20\d{6}T\d{6}Z", text)),
            "write_tokens_seen": [tok for tok in ["write_text", "to_csv", "fig.savefig", "mkdir", "subprocess.run", "urlopen", "SDSS.query_sql", "open("] if tok in text],
            "network_or_external_notes": [],
            "self_containment_notes": [],
        }
        if p.suffix == ".py":
            try:
                ast.parse(text, filename=str(p))
                rec["syntax_ok"] = True
            except SyntaxError as exc:
                rec["syntax_ok"] = False
                rec["syntax_error"] = f"{exc.lineno}:{exc.offset} {exc.msg}"
        elif p.suffix == ".sh":
            ok, err = bash_syntax_ok(p)
            rec["syntax_ok"] = ok
            rec["syntax_error"] = err
        if "astroquery" in text or "SDSS.query_sql" in text:
            rec["network_or_external_notes"].append("May query public SDSS via astroquery if cache is absent.")
        if "urlopen" in text or "SkyServerWS" in text:
            rec["network_or_external_notes"].append("Uses public SDSS SkyServer HTTP requests.")
        if "semantic" in text.lower() or "arxiv" in text.lower() or "requests" in text:
            rec["network_or_external_notes"].append("May use public literature/web metadata endpoints when run.")
        if "claude" in text or "codex" in text:
            rec["network_or_external_notes"].append("Can invoke external AI CLI in visible read-only pane loop.")
        if str(REPO) in text:
            rec["self_containment_notes"].append("Uses absolute /Users/duhokim repo paths; reproducible on this host, not relocatable without edits.")
        if "analysis_sample_bpt.csv" in text:
            rec["self_containment_notes"].append("Requires cached SDSS analysis_sample_bpt.csv unless RP-1 generator is rerun.")
        if "tectonic" in text:
            rec["self_containment_notes"].append("Requires tectonic/LaTeX and class resolution.")
        if any(pkg in text for pkg in ["pandas", "numpy", "matplotlib", "scipy", "astroquery"]):
            rec["self_containment_notes"].append("Requires Python scientific/literature stack for that lane.")
        out.append(rec)
    return out


def pdf_checks(pdf_paths: List[Path], expected: Dict[str, Dict[str, Any]], primary_paths: Iterable[Path]) -> List[Dict[str, Any]]:
    primary_set = {str(p) for p in primary_paths}
    rows: List[Dict[str, Any]] = []
    for p in pdf_paths:
        exp = expected.get(str(p), {})
        actual_sha = sha256(p)
        actual_bytes = p.stat().st_size if p.exists() else None
        rows.append({
            "path": str(p),
            "relative_path": rel(p),
            "exists": p.exists(),
            "bytes": actual_bytes,
            "sha256": actual_sha,
            "starts_with_pdf_magic": pdf_magic_ok(p),
            "is_primary_linked_manuscript_pdf": str(p) in primary_set,
            "is_lane_local_pdf": inside(p, OVERNIGHT / "lanes"),
            "is_figure_pdf": ("/figures/" in str(p)) or ("_figure" in p.name) or p.name.startswith("figure"),
            "expected_sources": exp.get("sources", []),
            "expected_sha256": exp.get("sha256"),
            "expected_bytes": exp.get("bytes"),
            "expected_conflicts": exp.get("conflicts", []),
            "matches_expected_sha256": actual_sha == exp.get("sha256") if exp.get("sha256") else None,
            "matches_expected_bytes": actual_bytes == exp.get("bytes") if exp.get("bytes") is not None else None,
        })
    return rows


def json_inventory(json_paths: List[Path]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for p in json_paths:
        data = safe_json(p)
        rows.append({
            "path": str(p),
            "relative_path": rel(p),
            "exists": p.exists(),
            "bytes": p.stat().st_size if p.exists() else None,
            "sha256": sha256(p) if p.exists() else None,
            "json_ok": json_ok(data),
            "parse_error": data.get("__parse_error__") if isinstance(data, dict) else None,
            "top_level_type": type(data).__name__,
            "top_level_keys": sorted(list(data.keys()))[:40] if isinstance(data, dict) and json_ok(data) else None,
        })
    return rows


def analysis_result_checks() -> List[Dict[str, Any]]:
    paths = [FIRST_RUN / "analysis_results.json"] + sorted(BATCH_RUN.glob("*/analysis_results.json"))
    rows: List[Dict[str, Any]] = []
    for p in paths:
        data = safe_json(p)
        guard = ""
        if isinstance(data, dict):
            guard = str(data.get("interpretation_guard") or data.get("safety") or data.get("proxy_guard") or data.get("scope_guard") or "")
        rows.append({
            "path": str(p),
            "relative_path": rel(p),
            "exists": p.exists(),
            "json_ok": json_ok(data),
            "run_id": data.get("run_id") if isinstance(data, dict) else None,
            "slug": data.get("slug") if isinstance(data, dict) else None,
            "sample_rows_or_analysis_rows": data.get("sample_rows", data.get("analysis_rows")) if isinstance(data, dict) else None,
            "source_sample": data.get("source_sample") if isinstance(data, dict) else None,
            "has_interpretation_guard_or_safety": bool(guard),
            "guard_text": guard[:300],
        })
    return rows


def expected_artifact_rows(expected: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for pstr, exp in sorted(expected.items()):
        p = Path(pstr)
        actual_sha = sha256(p) if p.exists() else None
        actual_bytes = p.stat().st_size if p.exists() else None
        rows.append({
            "path": pstr,
            "relative_path": rel(p),
            "exists": p.exists(),
            "kind": exp.get("kind"),
            "sources": exp.get("sources", []),
            "expected_sha256": exp.get("sha256"),
            "actual_sha256": actual_sha,
            "expected_bytes": exp.get("bytes"),
            "actual_bytes": actual_bytes,
            "matches_sha256": actual_sha == exp.get("sha256") if exp.get("sha256") else None,
            "matches_bytes": actual_bytes == exp.get("bytes") if exp.get("bytes") is not None else None,
            "conflicts": exp.get("conflicts", []),
        })
    return rows


def goru_summary_checks() -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for p in sorted((OVERNIGHT / "lanes/goru/artifacts").glob("goru_*_20260708T*.json")):
        data = safe_json(p)
        outputs = data.get("outputs", {}) if isinstance(data, dict) else {}
        missing = []
        measured_rows: Dict[str, Optional[int]] = {}
        for key, value in outputs.items():
            op = normalize_path(value)
            if op is None or not op.exists():
                missing.append(str(value))
            elif op.suffix.lower() == ".csv":
                measured_rows[key] = count_csv_rows(op).get("rows")
        rows.append({
            "path": str(p),
            "relative_path": rel(p),
            "json_ok": json_ok(data),
            "marker": data.get("marker") if isinstance(data, dict) else None,
            "output_count": len(outputs),
            "missing_output_count": len(missing),
            "missing_outputs": missing,
            "row_counts_declared": data.get("row_counts") if isinstance(data, dict) else None,
            "csv_rows_measured": measured_rows,
        })
    return rows


def process_scan() -> Dict[str, Any]:
    patterns = [
        "tectonic", "run_sdss_agn_sfr_pilot.py", "run_remaining_topic_pilots.py",
        "selection_attrition", "goru_stratified_bpt_robustness", "goru_regression_bin_sensitivity",
        "goru_actual_data_robustness", "lana_", "tori_wave2_result_table_drafts",
        "rp1_robustness_selection_revision",
    ]
    try:
        output = subprocess.check_output(["ps", "-axo", "pid=,command="], text=True, stderr=subprocess.DEVNULL)
    except Exception as exc:
        return {"ok": False, "error": str(exc), "matching_processes": []}
    hits: List[Dict[str, str]] = []
    self_pid = os.getpid()
    for line in output.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        parts = stripped.split(maxsplit=1)
        pid_s = parts[0]
        command = parts[1] if len(parts) > 1 else ""
        try:
            if int(pid_s) == self_pid:
                continue
        except Exception:
            pass
        if any(pat in command for pat in patterns):
            hits.append({"pid": pid_s, "command": command})
    return {"ok": True, "matching_processes": hits}


def dependency_checks() -> Dict[str, Any]:
    packages = ["numpy", "pandas", "matplotlib", "scipy", "astroquery"]
    return {
        "executables": {name: shutil.which(name) for name in ["python3", "python", "tectonic", "shasum", "pdfinfo", "bash"]},
        "python_executable": sys.executable,
        "python_version": sys.version.split()[0],
        "python_packages_find_spec": {name: importlib.util.find_spec(name) is not None for name in packages},
    }


def exact_repro_commands() -> List[str]:
    return [
        "cd /Users/duhokim/NebulaMind/NebulaMind",
        "# RP-1 full local rerun; uses cached CSV if present, may query public SDSS if cache is absent, overwrites run-local artifacts",
        "bash .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/run_full_sdss_agn_sfr_pilot.sh",
        "",
        "# Remaining 8 active topic pilots; requires cached RP-1 analysis_sample_bpt.csv and overwrites batch run-local artifacts",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/run_remaining_topic_pilots.py > .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z.batch.log 2>&1",
        "",
        "# Hash-check the 9 public-linked manuscript PDFs without writing artifacts",
        "shasum -a 256 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/aastex/sdss_agn_sfr_pilot_aas.pdf",
        "shasum -a 256 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/*/aastex/*_aas.pdf",
        "",
        "# Lane-local overnight generators; run only in lane scopes because they write lane artifacts",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/scripts/build_quality_inventory_20260708T132720Z.py",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/scripts/goru_actual_data_robustness_20260708T141459Z.py",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/scripts/goru_stratified_bpt_robustness_20260708T162615Z.py",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/scripts/goru_regression_bin_sensitivity_20260708T183643Z.py",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/scripts/selection_attrition_tick_v2.py  # public SDSS COUNT queries; writes Tori lane artifacts",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/scripts/tori_wave2_result_table_drafts_20260708T143512Z.py",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/scripts/rp1_robustness_selection_revision_20260708T181833Z.py",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/lana/scripts/lana_wave1_selection_definition_cleanup_20260708T182812Z.py",
        "",
        "# Re-run this Kun read-mostly integrity audit (writes only Kun lane report/JSON)",
        f"python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/kun/scripts/kun_repro_audit_{TS}.py",
    ]


def render_markdown(out: Dict[str, Any]) -> str:
    c = out["summary_counts"]
    deps = out["dependency_checks"]
    exp = out["expected_artifacts"]
    mc = out["manifest_checks"]
    lines: List[str] = []
    lines.append(f"# Kun reproducibility tick — {TS}")
    lines.append("")
    lines.append(f"Marker: `{MARKER}`")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append("Read the overnight brief, swarm board, ledger, all manifest-like JSON, compile/run logs, scripts, PDFs, analysis JSON, and sample-provenance files under `aas-autopilot`. I did not rerun manuscript/data generators or compilers; this tick ran only the Kun-local audit script to avoid lane races and non-Kun writes.")
    lines.append("")
    lines.append("## Race/process check")
    hits = out["process_scan"].get("matching_processes", [])
    if hits:
        lines.append(f"- Potential active generator/TeX/lane processes observed: {len(hits)}; generator reruns avoided.")
        for hit in hits[:8]:
            lines.append(f"  - PID {hit.get('pid')}: `{hit.get('command')}`")
    else:
        lines.append("- No active `tectonic`, manuscript-generator, selection-attrition, Goru robustness, Lana revision, or Tori revision process was seen at scan time.")
    lines.append("")
    lines.append("## Artifact integrity results")
    lines.append("")
    lines.append(f"- PDFs under aas-autopilot: {c['pdf_total']} total; {c['pdf_magic_ok']} start with `%PDF-`; {c['pdf_expected_count']} have expected SHA/byte checks; expected mismatches: {c['pdf_expected_mismatches']}.")
    lines.append(f"- Primary 9 public-linked manuscript PDFs: {c['primary_pdf_count']} checked; expected-hash/byte mismatches: {c['primary_pdf_mismatches']}.")
    lines.append(f"- Lane-local expected PDFs: {c['lane_expected_pdf_count']} checked; mismatches: {c['lane_expected_pdf_mismatches']}.")
    lines.append(f"- Logs under aas-autopilot: {c['log_total']} checked; compile-ish logs: {c['compileish_log_total']}; compile-ish fatal-marker files: {c['compileish_logs_with_fatal_markers']}; all-log fatal-marker files: {c['log_files_with_fatal_markers']}.")
    lines.append(f"- Manifest/receipt/inventory expected artifacts: {c['expected_artifact_count']} checked; missing/hash/byte/conflict rows: {c['expected_artifact_mismatch_count']}.")
    lines.append(f"- Manifest-like JSON files: {mc['manifest_like_json_count']} checked, {mc['manifest_like_json_ok_count']} parse OK.")
    lines.append(f"- Selection-function raw payload counts: SQL {mc['selection_raw_payload_count_sql_actual']}/{mc['selection_raw_payload_count_sql_expected']}, JSON {mc['selection_raw_payload_count_json_actual']}/{mc['selection_raw_payload_count_json_expected']}.")
    lines.append(f"- Goru summary JSONs checked: {c['goru_summary_count']}; missing declared Goru outputs: {c['goru_missing_outputs']}.")
    lines.append(f"- Quality inventory summary remains: `{out['quality_inventory_summary']}`.")
    lines.append("")
    lines.append("## Data/sample provenance")
    lines.append("")
    for key, rec in out["data_provenance"].items():
        lines.append(f"- {key}: exists={rec.get('exists')} rows={rec.get('rows')} bytes={rec.get('bytes')} sha256=`{rec.get('sha256')}`")
    lines.append(f"- Analysis JSON files: {c['analysis_json_count']} checked, {c['analysis_json_ok']} parse OK, {c['analysis_json_with_guard']} with explicit guard/safety text.")
    lines.append("")
    lines.append("## Script/self-containment checks")
    lines.append("")
    lines.append(f"- Scripts checked: {c['script_total']} (`*.py`/`*.sh`); syntax OK: {c['script_syntax_ok']}; failures: {c['script_syntax_bad']}.")
    lines.append(f"- Scripts with absolute repo paths: {c['scripts_with_absolute_repo_path']}; with public-network/external notes: {c['scripts_with_network_or_external_notes']}.")
    lines.append(f"- Executables: python3=`{deps['executables'].get('python3')}`, running Python=`{deps['python_executable']}` {deps['python_version']}, tectonic=`{deps['executables'].get('tectonic')}`, shasum=`{deps['executables'].get('shasum')}`, pdfinfo=`{deps['executables'].get('pdfinfo')}`.")
    lines.append(f"- Python package availability by `importlib.util.find_spec`: `{deps['python_packages_find_spec']}`.")
    lines.append("- Reproducibility note: scripts are self-contained for this host but not fully relocatable because many use absolute `/Users/duhokim/...` paths; some public SDSS/literature scripts may use network if caches are absent.")
    lines.append("")
    lines.append("## Exact local repro commands")
    lines.append("")
    lines.append("```bash")
    lines.extend(out["exact_repro_commands"])
    lines.append("```")
    lines.append("")
    lines.append("## Blocker notes")
    lines.append("")
    if out["blockers"]:
        for blocker in out["blockers"]:
            lines.append(f"- BLOCKER: {blocker}")
    else:
        lines.append("- No artifact-integrity blocker found: PDF magic/hash checks, manifests/receipts/inventories, compile logs, scripts, analysis JSON, and sample provenance are internally consistent for preserved artifacts.")
    if c["log_files_with_fatal_markers"] and not c["compileish_logs_with_fatal_markers"]:
        lines.append("- Non-blocker: fatal markers, if any, are confined to non-compile miscellaneous logs/stderr rather than manuscript compile logs.")
    lines.append("- Non-blocker: `pdfinfo` may be unavailable, so PDF page counts are not a gate; binary magic and SHA256/byte checks are the integrity checks.")
    lines.append("- Non-blocker: lane-local revisions are compiled/hashed but are not integrated into public-linked manuscripts/PDFs; integration remains a separate Hwao/Tori/user-approved gate.")
    lines.append("- Non-blocker: exact PDF SHA can change on recompilation due to TeX/PDF metadata; source/data/figure inputs remain the stable reproducibility basis.")
    lines.append("")
    lines.append("## Safety")
    lines.append("")
    lines.append("No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git, billing, OAuth, external submission, or new cron jobs were touched. This audit wrote only Kun-lane report/JSON files; the required one-line `OVERNIGHT_LEDGER.md` append is separate.")
    lines.append("")
    lines.append(f"JSON summary: `{SUMMARY}`")
    return "\n".join(lines) + "\n"


def main() -> None:
    for d in [REPORT.parent, SUMMARY.parent, SCRIPT_PATH.parent]:
        assert_kun_write(d)
        d.mkdir(parents=True, exist_ok=True)

    for p in [BRIEF, SWARM_BOARD, LEDGER]:
        if not p.exists():
            raise RuntimeError(f"required read-first file missing: {p}")

    batch = safe_json(BATCH_MANIFEST)
    primary_by_name = primary_paths_from_manifests(batch)
    primary_paths = [p for name, p in primary_by_name.items() if name in PRIMARY_PDF_NAMES]
    expected, manifest_details = build_expected_artifacts()

    pdf_paths = sorted(AUTOPILOT.rglob("*.pdf"))
    log_paths = sorted(AUTOPILOT.rglob("*.log"))
    script_paths = sorted(AUTOPILOT.rglob("*.py")) + sorted(AUTOPILOT.rglob("*.sh"))
    json_paths = sorted(AUTOPILOT.rglob("*.json"))

    pdf_rows = pdf_checks(pdf_paths, expected, primary_paths)
    log_rows = log_checks(log_paths)
    script_rows = script_checks(script_paths)
    json_rows = json_inventory(json_paths)
    expected_rows = expected_artifact_rows(expected)
    analyses = analysis_result_checks()
    goru_rows = goru_summary_checks()
    deps = dependency_checks()
    proc = process_scan()

    data_paths = {
        "sdss_query_sql": FIRST_RUN / "data/query.sql",
        "raw_sdss_csv": FIRST_RUN / "data/sdss_dr17_emission_line_sample.csv",
        "analysis_sample_bpt_csv": FIRST_RUN / "data/analysis_sample_bpt.csv",
        "matched_agn_sf_pairs_csv": FIRST_RUN / "data/matched_agn_sf_pairs.csv",
        "batch_source_csv": normalize_path(batch.get("source_csv")) if isinstance(batch, dict) else None,
    }
    data_provenance: Dict[str, Any] = {}
    for key, p in data_paths.items():
        if p is None:
            data_provenance[key] = {"path": None, "relative_path": None, "exists": False, "bytes": None, "sha256": None, "rows": None}
        elif p.suffix.lower() == ".csv":
            data_provenance[key] = count_csv_rows(p)
        else:
            data_provenance[key] = {"path": str(p), "relative_path": rel(p), "exists": p.exists(), "bytes": p.stat().st_size if p.exists() else None, "sha256": sha256(p) if p.exists() else None, "rows": None}

    quality = safe_json(QUALITY_INVENTORY)
    quality_summary = quality.get("summary") if isinstance(quality, dict) else None

    pdf_expected_rows = [r for r in pdf_rows if r["expected_sha256"]]
    pdf_expected_mismatches = [r for r in pdf_expected_rows if r["matches_expected_sha256"] is False or r["matches_expected_bytes"] is False or r["expected_conflicts"]]
    primary_pdf_rows = [r for r in pdf_rows if r["is_primary_linked_manuscript_pdf"]]
    primary_mismatches = [r for r in primary_pdf_rows if r["matches_expected_sha256"] is False or r["matches_expected_bytes"] is False]
    lane_expected_pdf_rows = [r for r in pdf_expected_rows if r["is_lane_local_pdf"]]
    lane_expected_pdf_mismatches = [r for r in lane_expected_pdf_rows if r["matches_expected_sha256"] is False or r["matches_expected_bytes"] is False]
    pdf_magic_bad = [r for r in pdf_rows if not r["starts_with_pdf_magic"]]
    log_bad = [r for r in log_rows if r["fatal_marker_count"]]
    compileish_logs = [r for r in log_rows if r["compileish"]]
    compileish_bad = [r for r in compileish_logs if r["fatal_marker_count"]]
    script_bad = [r for r in script_rows if r["syntax_ok"] is False]
    json_bad = [r for r in json_rows if not r["json_ok"]]
    expected_mismatches = [r for r in expected_rows if (not r["exists"]) or r["matches_sha256"] is False or r["matches_bytes"] is False or r["conflicts"]]
    analysis_ok = [r for r in analyses if r["json_ok"]]
    analysis_guard = [r for r in analyses if r["has_interpretation_guard_or_safety"]]
    goru_missing = sum(r["missing_output_count"] for r in goru_rows)

    blockers: List[str] = []
    if pdf_magic_bad:
        blockers.append(f"{len(pdf_magic_bad)} PDF(s) do not start with %PDF magic")
    if pdf_expected_mismatches:
        blockers.append(f"{len(pdf_expected_mismatches)} expected PDF(s) mismatch recorded SHA/bytes")
    if expected_mismatches:
        blockers.append(f"{len(expected_mismatches)} expected manifest/receipt/inventory artifact row(s) missing or hash/byte/conflict mismatched")
    if compileish_bad:
        blockers.append(f"{len(compileish_bad)} compile-ish log file(s) contain fatal/traceback/LaTeX-error markers")
    if len(primary_pdf_rows) != 9:
        blockers.append(f"Primary public-linked manuscript PDF count is {len(primary_pdf_rows)}, expected 9")
    if isinstance(batch, dict) and len(batch.get("topics", [])) != 8:
        blockers.append(f"Batch manifest topic count is {len(batch.get('topics', []))}, expected 8")
    if script_bad:
        blockers.append(f"{len(script_bad)} script(s) failed syntax checks")
    if json_bad:
        blockers.append(f"{len(json_bad)} JSON file(s) failed parse")
    if len(analyses) != 9 or len(analysis_ok) != 9:
        blockers.append(f"Analysis JSON parse count is {len(analysis_ok)}/{len(analyses)}, expected 9/9")
    if data_provenance["analysis_sample_bpt_csv"].get("rows") != 60000:
        blockers.append(f"analysis_sample_bpt_csv rows={data_provenance['analysis_sample_bpt_csv'].get('rows')}, expected 60000")
    if data_provenance["matched_agn_sf_pairs_csv"].get("rows") != 8146:
        blockers.append(f"matched_agn_sf_pairs_csv rows={data_provenance['matched_agn_sf_pairs_csv'].get('rows')}, expected 8146")
    if manifest_details["selection_raw_payload_count_json_expected"] != manifest_details["selection_raw_payload_count_json_actual"]:
        blockers.append("Selection raw JSON payload count mismatch expected=%s actual=%s" % (manifest_details["selection_raw_payload_count_json_expected"], manifest_details["selection_raw_payload_count_json_actual"]))
    if manifest_details["selection_raw_payload_count_sql_expected"] != manifest_details["selection_raw_payload_count_sql_actual"]:
        blockers.append("Selection raw SQL payload count mismatch expected=%s actual=%s" % (manifest_details["selection_raw_payload_count_sql_expected"], manifest_details["selection_raw_payload_count_sql_actual"]))
    if goru_missing:
        blockers.append(f"{goru_missing} declared Goru output(s) missing")

    summary_counts = {
        "pdf_total": len(pdf_rows),
        "pdf_magic_ok": sum(1 for r in pdf_rows if r["starts_with_pdf_magic"]),
        "pdf_expected_count": len(pdf_expected_rows),
        "pdf_expected_mismatches": len(pdf_expected_mismatches),
        "primary_pdf_count": len(primary_pdf_rows),
        "primary_pdf_mismatches": len(primary_mismatches),
        "lane_expected_pdf_count": len(lane_expected_pdf_rows),
        "lane_expected_pdf_mismatches": len(lane_expected_pdf_mismatches),
        "log_total": len(log_rows),
        "compileish_log_total": len(compileish_logs),
        "compileish_logs_with_fatal_markers": len(compileish_bad),
        "log_files_with_fatal_markers": len(log_bad),
        "script_total": len(script_rows),
        "script_syntax_ok": sum(1 for r in script_rows if r["syntax_ok"] is True),
        "script_syntax_bad": len(script_bad),
        "scripts_with_absolute_repo_path": sum(1 for r in script_rows if r["has_absolute_repo_path"]),
        "scripts_with_network_or_external_notes": sum(1 for r in script_rows if r["network_or_external_notes"]),
        "json_total": len(json_rows),
        "json_ok": sum(1 for r in json_rows if r["json_ok"]),
        "json_bad": len(json_bad),
        "expected_artifact_count": len(expected_rows),
        "expected_artifact_mismatch_count": len(expected_mismatches),
        "analysis_json_count": len(analyses),
        "analysis_json_ok": len(analysis_ok),
        "analysis_json_with_guard": len(analysis_guard),
        "goru_summary_count": len(goru_rows),
        "goru_missing_outputs": goru_missing,
        "blocking_failure_count": len(blockers),
    }

    out: Dict[str, Any] = {
        "marker": MARKER,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Kun reproducibility/integrity audit over existing aas-autopilot artifacts; no generator/compiler reruns outside Kun lane.",
        "paths_read_first": [str(BRIEF), str(SWARM_BOARD), str(LEDGER)],
        "summary_counts": summary_counts,
        "blockers": blockers,
        "process_scan": proc,
        "dependency_checks": deps,
        "manifest_checks": manifest_details,
        "quality_inventory_summary": quality_summary,
        "data_provenance": data_provenance,
        "analysis_results": analyses,
        "goru_summaries": goru_rows,
        "json_inventory_summary": {"json_total": len(json_rows), "json_ok": sum(1 for r in json_rows if r["json_ok"]), "json_bad": len(json_bad)},
        "expected_artifacts": {"rows": expected_rows, "mismatches": expected_mismatches[:50]},
        "pdfs": pdf_rows,
        "logs": log_rows,
        "scripts": script_rows,
        "exact_repro_commands": exact_repro_commands(),
        "safety": "No public pages/live roots/product DB/API/pages/page_versions/trust/deploy/restart/git/billing/OAuth/external submission/new cron jobs touched. Writes are under Kun lane only; a separate one-line ledger append is required by the user instruction.",
    }

    assert_kun_write(SUMMARY)
    assert_kun_write(REPORT)
    SUMMARY.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    REPORT.write_text(render_markdown(out), encoding="utf-8")
    print(json.dumps({
        "ok": True,
        "marker": MARKER,
        "report": str(REPORT),
        "summary": str(SUMMARY),
        "summary_counts": summary_counts,
        "blockers": blockers,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
