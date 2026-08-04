#!/usr/bin/env python3
"""Kun reproducibility/integrity tick for the overnight 9-paper AAS swarm.

This script performs a read-mostly audit over existing aas-autopilot artifacts and
writes only Kun lane-local report/summary artifacts. It deliberately does not
rerun manuscript generators, TeX compilers, public SDSS queries, public-page
updates, deploys, git operations, or cron creation.
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
from typing import Any, Dict, Iterable, List, Optional, Tuple

TS = "20260708T163511Z"
MARKER = "KUN_REPRO_AUDIT_%s" % TS
REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTOPILOT = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
RUNS = AUTOPILOT / "runs"
FIRST_RUN = RUNS / "SDSS_AGN_SFR_PILOT_20260708T122000Z"
BATCH_RUN = RUNS / "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z"
OVERNIGHT = AUTOPILOT / "overnight-9-papers-20260708"
KUN = OVERNIGHT / "lanes/kun"
REPORT = KUN / "ticks" / ("KUN_TICK_%s.md" % TS)
SUMMARY = KUN / "artifacts" / ("kun_repro_audit_%s.json" % TS)
SCRIPT_PATH = KUN / "scripts" / ("kun_repro_audit_%s.py" % TS)

BRIEF = OVERNIGHT / "OVERNIGHT_BRIEF.md"
SWARM_BOARD = OVERNIGHT / "SWARM_BOARD.md"
LEDGER = OVERNIGHT / "OVERNIGHT_LEDGER.md"
BATCH_MANIFEST = BATCH_RUN / "ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json"
PUBLIC_APPLY = AUTOPILOT / "ALL_TOPICS_PDF_LINK_APPLY_20260708T130505Z.json"
QUALITY_INVENTORY = OVERNIGHT / "artifacts/quality_inventory_20260708T132720Z.json"
LITERATURE_SUMMARY = OVERNIGHT / "lanes/literature/literature_summary_20260708T143233Z.json"

FATAL_LOG_RE = re.compile(
    r"fatal error|! LaTeX Error|Emergency stop|Undefined control sequence|No pages of output|Traceback|Tectonic failed|failed for|ERROR:",
    re.IGNORECASE,
)
WARN_RE = re.compile(r"warning", re.IGNORECASE)

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

PROHIBITED_ACTIONS = [
    "public pages/live roots",
    "product DB",
    "API/pages",
    "page_versions",
    "trust",
    "deploy/restart",
    "git",
    "billing/OAuth",
    "external submission",
    "new cron jobs",
]


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
        raise RuntimeError("refusing non-Kun-lane write: %s" % path)


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


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO))
    except Exception:
        return str(path)


def count_csv_rows(path: Path) -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "path": str(path),
        "relative_path": rel(path),
        "exists": path.exists(),
        "bytes": path.stat().st_size if path.exists() else None,
        "sha256": sha256(path) if path.exists() else None,
        "rows": None,
        "columns": None,
    }
    if not path.exists() or not path.is_file():
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


def normalize_path(value: Any, base: Optional[Path] = None) -> Optional[Path]:
    if value is None or value == "":
        return None
    p = Path(str(value))
    if p.is_absolute():
        return p
    s = str(value)
    if s.startswith("lanes/") or s.startswith("ticks/") or s.startswith("artifacts/") or s.startswith("visible-panes/"):
        return OVERNIGHT / p
    if s.startswith("runs/"):
        return AUTOPILOT / p
    if base is not None:
        return base / p
    return AUTOPILOT / p


def add_expected(expected: Dict[str, Dict[str, Any]], path: Optional[Path], source: str, sha_value: Optional[str], bytes_value: Optional[int]) -> None:
    if path is None:
        return
    key = str(path)
    rec = expected.setdefault(key, {"sources": [], "sha256": None, "bytes": None, "conflicts": []})
    rec["sources"].append(source)
    if sha_value:
        if rec["sha256"] and rec["sha256"] != sha_value:
            rec["conflicts"].append({"field": "sha256", "old": rec["sha256"], "new": sha_value, "source": source})
        else:
            rec["sha256"] = sha_value
    if bytes_value is not None:
        if rec["bytes"] is not None and rec["bytes"] != bytes_value:
            rec["conflicts"].append({"field": "bytes", "old": rec["bytes"], "new": bytes_value, "source": source})
        else:
            rec["bytes"] = bytes_value


def primary_pdf_paths_from_batch(batch: Any) -> Dict[str, Path]:
    paths: Dict[str, Path] = {
        "sdss_agn_sfr_pilot_aas.pdf": FIRST_RUN / "aastex/sdss_agn_sfr_pilot_aas.pdf"
    }
    if isinstance(batch, dict):
        for item in batch.get("topics", []):
            if isinstance(item, dict) and item.get("pdf_name") and item.get("pdf"):
                paths[item["pdf_name"]] = Path(item["pdf"])
    return paths


def build_expected_artifacts() -> Tuple[Dict[str, Dict[str, Any]], Dict[str, Any]]:
    expected: Dict[str, Dict[str, Any]] = {}
    details: Dict[str, Any] = {}

    batch = safe_json(BATCH_MANIFEST)
    details["batch_manifest_json_ok"] = json_ok(batch)
    primary_by_name = primary_pdf_paths_from_batch(batch)
    if isinstance(batch, dict):
        for item in batch.get("topics", []):
            if isinstance(item, dict):
                add_expected(
                    expected,
                    Path(item.get("pdf", "")),
                    "ALL_REMAINING_TOPIC_PILOTS_MANIFEST",
                    item.get("pdf_sha256"),
                    item.get("pdf_bytes"),
                )

    public = safe_json(PUBLIC_APPLY)
    details["public_apply_json_ok"] = json_ok(public)
    if isinstance(public, dict):
        for name, rec in (public.get("pdf_hashes") or {}).items():
            path = primary_by_name.get(name)
            add_expected(
                expected,
                path,
                "ALL_TOPICS_PDF_LINK_APPLY pdf_hashes",
                rec.get("sha256") if isinstance(rec, dict) else None,
                rec.get("bytes") if isinstance(rec, dict) else None,
            )

    lana_manifests = sorted((OVERNIGHT / "lanes/lana").glob("lana_revision_manifest_*.json"))
    lana_drafts = 0
    for manifest in lana_manifests:
        data = safe_json(manifest)
        if isinstance(data, dict):
            for item in data.get("drafts", []):
                if isinstance(item, dict):
                    lana_drafts += 1
                    add_expected(
                        expected,
                        normalize_path(item.get("compiled_pdf")),
                        manifest.name,
                        item.get("pdf_sha256"),
                        item.get("pdf_bytes"),
                    )
    details["lana_manifest_count"] = len(lana_manifests)
    details["lana_draft_count"] = lana_drafts

    tori_manifest = OVERNIGHT / "lanes/tori/wave2-result-table-drafts/20260708T143512Z/tori_wave2_result_table_manifest_20260708T143512Z.json"
    tori = safe_json(tori_manifest)
    tori_drafts = 0
    if isinstance(tori, dict):
        for item in tori.get("drafts", []):
            if isinstance(item, dict):
                tori_drafts += 1
                add_expected(
                    expected,
                    normalize_path(item.get("compiled_pdf")),
                    tori_manifest.name,
                    item.get("pdf_sha256"),
                    item.get("pdf_bytes"),
                )
    details["tori_wave2_manifest_json_ok"] = json_ok(tori)
    details["tori_wave2_draft_count"] = tori_drafts

    selection_manifest = OVERNIGHT / "lanes/tori/selection-function-attrition/20260708T155514Z/selection_function_attrition_artifact_manifest_20260708T155514Z.json"
    selection = safe_json(selection_manifest)
    selection_artifacts = 0
    if isinstance(selection, dict):
        for item in selection.get("artifacts", []):
            if isinstance(item, dict):
                selection_artifacts += 1
                add_expected(
                    expected,
                    normalize_path(item.get("path")),
                    selection_manifest.name,
                    item.get("sha256"),
                    item.get("bytes"),
                )
    details["selection_manifest_json_ok"] = json_ok(selection)
    details["selection_artifact_count"] = selection_artifacts
    details["selection_raw_payload_count_json_expected"] = selection.get("raw_payload_count_json") if isinstance(selection, dict) else None
    details["selection_raw_payload_count_sql_expected"] = selection.get("raw_payload_count_sql") if isinstance(selection, dict) else None

    return expected, details


def pdf_checks(pdf_paths: List[Path], expected: Dict[str, Dict[str, Any]], primary_paths: Iterable[Path]) -> List[Dict[str, Any]]:
    primary_set = set(str(p) for p in primary_paths)
    rows: List[Dict[str, Any]] = []
    for path in pdf_paths:
        exp = expected.get(str(path))
        actual_sha = sha256(path)
        actual_bytes = path.stat().st_size if path.exists() else None
        rows.append({
            "path": str(path),
            "relative_path": rel(path),
            "exists": path.exists(),
            "bytes": actual_bytes,
            "sha256": actual_sha,
            "starts_with_pdf_magic": pdf_magic_ok(path),
            "is_primary_linked_manuscript_pdf": str(path) in primary_set,
            "is_lane_local_pdf": inside(path, OVERNIGHT / "lanes"),
            "is_figure_pdf": ("/figures/" in str(path)) or ("_figure" in path.name) or path.name.startswith("figure"),
            "expected_sources": exp.get("sources") if exp else [],
            "expected_bytes": exp.get("bytes") if exp else None,
            "expected_sha256": exp.get("sha256") if exp else None,
            "expected_conflicts": exp.get("conflicts") if exp else [],
            "matches_expected_bytes": (actual_bytes == exp.get("bytes")) if exp and exp.get("bytes") is not None else None,
            "matches_expected_sha256": (actual_sha == exp.get("sha256")) if exp and exp.get("sha256") else None,
        })
    return rows


def is_compileish_log(path: Path, text: str) -> bool:
    if path.name == "compile.log":
        return True
    if "revision-drafts" in str(path) and path.suffix == ".log":
        return True
    if "Output written on" in text and (".pdf" in text or ".xdv" in text):
        return True
    if "Running xdvipdfmx" in text or "Writing `" in text and ".pdf`" in text:
        return True
    return False


def log_checks(log_paths: List[Path]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for path in log_paths:
        text = read_text(path)
        fatal = FATAL_LOG_RE.findall(text)
        rows.append({
            "path": str(path),
            "relative_path": rel(path),
            "exists": path.exists(),
            "bytes": path.stat().st_size if path.exists() else None,
            "sha256": sha256(path) if path.exists() else None,
            "compileish": is_compileish_log(path, text),
            "fatal_marker_count": len(fatal),
            "fatal_markers": fatal[:10],
            "warning_marker_count": len(WARN_RE.findall(text)),
            "tail_preview": re.sub(r"\s+", " ", text[-500:]).strip(),
        })
    return rows


def bash_syntax_ok(path: Path) -> Tuple[bool, Optional[str]]:
    bash = shutil.which("bash") or "/bin/bash"
    try:
        proc = subprocess.run([bash, "-n", str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=20)
        return proc.returncode == 0, (proc.stderr.strip() or proc.stdout.strip() or None)
    except Exception as exc:
        return False, str(exc)


def script_checks(paths: List[Path]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for path in paths:
        text = read_text(path)
        suffix = path.suffix.lower()
        rec: Dict[str, Any] = {
            "path": str(path),
            "relative_path": rel(path),
            "exists": path.exists(),
            "bytes": path.stat().st_size if path.exists() else None,
            "sha256": sha256(path) if path.exists() else None,
            "shebang": text.splitlines()[0] if text.startswith("#!") else None,
            "syntax_ok": None,
            "syntax_error": None,
            "has_absolute_repo_path": str(REPO) in text,
            "has_hardcoded_timestamp": bool(re.search(r"20\d{6}T\d{6}Z", text)),
            "write_tokens_seen": [tok for tok in ["write_text", "to_csv", "fig.savefig", "mkdir", "subprocess.run", "urlopen", "SDSS.query_sql"] if tok in text],
            "network_or_external_notes": [],
            "self_containment_notes": [],
        }
        if suffix == ".py" and path.exists():
            try:
                ast.parse(text, filename=str(path))
                rec["syntax_ok"] = True
            except SyntaxError as exc:
                rec["syntax_ok"] = False
                rec["syntax_error"] = "%s:%s %s" % (exc.lineno, exc.offset, exc.msg)
        elif suffix == ".sh" and path.exists():
            ok, err = bash_syntax_ok(path)
            rec["syntax_ok"] = ok
            rec["syntax_error"] = err
        if "astroquery" in text or "SDSS.query_sql" in text:
            rec["network_or_external_notes"].append("May query public SDSS via astroquery if cache is absent.")
        if "urlopen" in text or "SkyServerWS" in text:
            rec["network_or_external_notes"].append("Uses public SDSS SkyServer HTTP COUNT queries.")
        if "claude" in text or "codex" in text:
            rec["network_or_external_notes"].append("Can invoke external AI CLI in visible read-only pane loop.")
        if str(REPO) in text:
            rec["self_containment_notes"].append("Uses absolute /Users/duhokim repo paths; reproducible on this host, not relocatable without edits.")
        if "analysis_sample_bpt.csv" in text:
            rec["self_containment_notes"].append("Requires cached SDSS analysis_sample_bpt.csv unless the first RP-1 generator is run.")
        if "tectonic" in text:
            rec["self_containment_notes"].append("Requires tectonic and AASTeX class resolution.")
        if "pandas" in text:
            rec["self_containment_notes"].append("Requires Python scientific stack where used (pandas/numpy/scipy/matplotlib as applicable).")
        rows.append(rec)
    return rows


def json_inventory(json_paths: List[Path]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for path in json_paths:
        data = safe_json(path)
        rows.append({
            "path": str(path),
            "relative_path": rel(path),
            "exists": path.exists(),
            "bytes": path.stat().st_size if path.exists() else None,
            "sha256": sha256(path) if path.exists() else None,
            "json_ok": json_ok(data),
            "parse_error": data.get("__parse_error__") if isinstance(data, dict) else None,
            "top_level_type": type(data).__name__,
            "top_level_keys": sorted(list(data.keys()))[:30] if isinstance(data, dict) and json_ok(data) else None,
        })
    return rows


def manifest_checks(expected: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    batch = safe_json(BATCH_MANIFEST)
    public = safe_json(PUBLIC_APPLY)
    quality = safe_json(QUALITY_INVENTORY)
    literature = safe_json(LITERATURE_SUMMARY)

    batch_topics = batch.get("topics", []) if isinstance(batch, dict) else []
    batch_hash_mismatches: List[Dict[str, Any]] = []
    for item in batch_topics:
        if not isinstance(item, dict):
            continue
        p = Path(item.get("pdf", ""))
        if sha256(p) != item.get("pdf_sha256") or ((p.stat().st_size if p.exists() else None) != item.get("pdf_bytes")):
            batch_hash_mismatches.append({
                "slug": item.get("slug"),
                "pdf": str(p),
                "expected_sha256": item.get("pdf_sha256"),
                "actual_sha256": sha256(p),
                "expected_bytes": item.get("pdf_bytes"),
                "actual_bytes": p.stat().st_size if p.exists() else None,
            })

    expected_rows: List[Dict[str, Any]] = []
    for pstr, exp in expected.items():
        p = Path(pstr)
        actual_sha = sha256(p)
        actual_bytes = p.stat().st_size if p.exists() else None
        expected_rows.append({
            "path": pstr,
            "relative_path": rel(p),
            "sources": exp.get("sources", []),
            "exists": p.exists(),
            "expected_sha256": exp.get("sha256"),
            "actual_sha256": actual_sha,
            "expected_bytes": exp.get("bytes"),
            "actual_bytes": actual_bytes,
            "matches_sha256": actual_sha == exp.get("sha256") if exp.get("sha256") else None,
            "matches_bytes": actual_bytes == exp.get("bytes") if exp.get("bytes") is not None else None,
            "conflicts": exp.get("conflicts", []),
        })
    expected_mismatches = [r for r in expected_rows if r["exists"] is False or r["matches_sha256"] is False or r["matches_bytes"] is False or r["conflicts"]]

    selection_manifest_path = OVERNIGHT / "lanes/tori/selection-function-attrition/20260708T155514Z/selection_function_attrition_artifact_manifest_20260708T155514Z.json"
    selection = safe_json(selection_manifest_path)
    raw_dir = OVERNIGHT / "lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads"
    raw_json_paths = sorted(raw_dir.glob("*.json"))
    raw_sql_paths = sorted(raw_dir.glob("*.sql"))
    raw_json_ok_count = sum(1 for p in raw_json_paths if json_ok(safe_json(p)))

    goru_jsons = sorted((OVERNIGHT / "lanes/goru/artifacts").glob("goru_*_20260708T*.json"))
    goru_summaries: List[Dict[str, Any]] = []
    for gp in goru_jsons:
        data = safe_json(gp)
        outputs = data.get("outputs", {}) if isinstance(data, dict) else {}
        missing = []
        csv_rows: Dict[str, Any] = {}
        for key, value in outputs.items():
            op = normalize_path(value)
            if op is None or not op.exists():
                missing.append(str(value))
            elif str(op).endswith(".csv"):
                csv_rows[key] = count_csv_rows(op).get("rows")
        goru_summaries.append({
            "path": str(gp),
            "relative_path": rel(gp),
            "json_ok": json_ok(data),
            "marker": data.get("marker") if isinstance(data, dict) else None,
            "output_count": len(outputs),
            "missing_output_count": len(missing),
            "missing_outputs": missing,
            "row_counts_recorded": data.get("row_counts") if isinstance(data, dict) else None,
            "csv_rows_measured": csv_rows,
        })

    return {
        "batch_manifest_exists": BATCH_MANIFEST.exists(),
        "batch_topic_count": len(batch_topics),
        "batch_hash_mismatch_count": len(batch_hash_mismatches),
        "batch_hash_mismatches": batch_hash_mismatches,
        "public_apply_exists": PUBLIC_APPLY.exists(),
        "public_pdf_hash_count": len(public.get("pdf_hashes", {})) if isinstance(public, dict) else None,
        "public_errors": public.get("errors") if isinstance(public, dict) else None,
        "quality_inventory_exists": QUALITY_INVENTORY.exists(),
        "quality_inventory_summary": quality.get("summary") if isinstance(quality, dict) else None,
        "literature_summary_exists": LITERATURE_SUMMARY.exists(),
        "literature_summary_marker": literature.get("marker") if isinstance(literature, dict) else None,
        "expected_artifact_count": len(expected_rows),
        "expected_artifact_mismatch_count": len(expected_mismatches),
        "expected_artifact_mismatches": expected_mismatches,
        "selection_manifest_exists": selection_manifest_path.exists(),
        "selection_artifact_count": selection.get("artifact_count") if isinstance(selection, dict) else None,
        "selection_raw_payload_count_json_expected": selection.get("raw_payload_count_json") if isinstance(selection, dict) else None,
        "selection_raw_payload_count_sql_expected": selection.get("raw_payload_count_sql") if isinstance(selection, dict) else None,
        "selection_raw_payload_count_json_actual": len(raw_json_paths),
        "selection_raw_payload_count_sql_actual": len(raw_sql_paths),
        "selection_raw_payload_json_ok_count": raw_json_ok_count,
        "goru_summaries": goru_summaries,
    }


def analysis_result_checks() -> List[Dict[str, Any]]:
    paths = [FIRST_RUN / "analysis_results.json"] + sorted(BATCH_RUN.glob("*/analysis_results.json"))
    rows: List[Dict[str, Any]] = []
    for path in paths:
        data = safe_json(path)
        rec: Dict[str, Any] = {
            "path": str(path),
            "relative_path": rel(path),
            "exists": path.exists(),
            "json_ok": json_ok(data),
            "parse_error": data.get("__parse_error__") if isinstance(data, dict) else None,
            "run_id": data.get("run_id") if isinstance(data, dict) else None,
            "slug": data.get("slug") if isinstance(data, dict) else None,
            "sample_rows_or_analysis_rows": data.get("sample_rows", data.get("analysis_rows")) if isinstance(data, dict) else None,
            "source_sample": data.get("source_sample") if isinstance(data, dict) else None,
            "has_interpretation_guard_or_safety": False,
            "guard_text": None,
        }
        if isinstance(data, dict):
            guard = str(data.get("interpretation_guard") or data.get("safety") or data.get("proxy_guard") or "")
            rec["has_interpretation_guard_or_safety"] = bool(guard)
            rec["guard_text"] = guard[:260]
        rows.append(rec)
    return rows


def process_scan() -> Dict[str, Any]:
    patterns = [
        "tectonic",
        "run_sdss_agn_sfr_pilot.py",
        "run_remaining_topic_pilots.py",
        "selection_attrition",
        "goru_stratified_bpt_robustness",
        "goru_actual_data_robustness",
        "lana_revision",
        "tori_wave2_result_table_drafts",
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
        pid = parts[0]
        command = parts[1] if len(parts) > 1 else ""
        try:
            if int(pid) == self_pid:
                continue
        except Exception:
            pass
        if any(pattern in command for pattern in patterns):
            hits.append({"pid": pid, "command": command})
    return {"ok": True, "matching_processes": hits}


def dependency_checks() -> Dict[str, Any]:
    packages = ["numpy", "pandas", "matplotlib", "scipy", "astroquery"]
    return {
        "executables": {name: shutil.which(name) for name in ["python3", "python", "tectonic", "shasum", "pdfinfo", "bash"]},
        "python_version": subprocess.check_output([shutil.which("python3") or "python3", "--version"], text=True).strip(),
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
        "# Previously used overnight local generators; run only in their lane scopes because they write lane artifacts",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/scripts/build_quality_inventory_20260708T132720Z.py",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/scripts/goru_actual_data_robustness_20260708T141459Z.py",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/scripts/tori_wave2_result_table_drafts_20260708T143512Z.py",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/scripts/selection_attrition_tick_v2.py  # public SDSS COUNT queries; writes Tori lane artifacts",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/scripts/goru_stratified_bpt_robustness_20260708T162615Z.py",
        "",
        "# Re-run this Kun read-only integrity audit (writes only Kun lane report/JSON)",
        "python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/kun/scripts/kun_repro_audit_%s.py" % TS,
    ]


def render_markdown(summary: Dict[str, Any]) -> str:
    s = summary["summary_counts"]
    mc = summary["manifest_checks"]
    deps = summary["dependency_checks"]
    lines: List[str] = []
    lines.append("# Kun reproducibility tick — %s" % TS)
    lines.append("")
    lines.append("Marker: `%s`" % MARKER)
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append("Read the overnight brief, swarm board, ledger, manifest/receipt JSON, compile/run logs, scripts, PDFs, analysis JSON, and sample provenance under `aas-autopilot`. I did not rerun generators or compilers because that would write outside the Kun lane or risk racing lane-local manuscript work; this tick ran only this Kun-local audit script.")
    lines.append("")
    lines.append("## Race/process check")
    proc_hits = summary["process_scan"].get("matching_processes", [])
    if proc_hits:
        lines.append("- Potential active generator/TeX processes at scan time: %d; reruns avoided." % len(proc_hits))
        for hit in proc_hits[:8]:
            lines.append("  - PID %s: `%s`" % (hit.get("pid"), hit.get("command")))
    else:
        lines.append("- No active `tectonic`, manuscript-generator, selection-attrition, Goru robustness, Lana revision, or Tori wave2 generator process was seen at scan time.")
    lines.append("")
    lines.append("## Artifact integrity results")
    lines.append("")
    lines.append("- PDFs under aas-autopilot: %d total; %d start with `%%PDF-`; %d have recorded expected SHA/byte checks; expected mismatches: %d." % (s["pdf_total"], s["pdf_magic_ok"], s["pdf_expected_count"], s["pdf_expected_mismatches"]))
    lines.append("- Primary 9 public-linked manuscript PDFs: %d checked; expected-hash mismatches: %d." % (s["primary_pdf_count"], s["primary_pdf_mismatches"]))
    lines.append("- Lane-local revision PDFs with expected hashes (Lana/Tori): %d checked; mismatches: %d." % (s["lane_expected_pdf_count"], s["lane_expected_pdf_mismatches"]))
    lines.append("- `.log` files under aas-autopilot: %d checked; compile-ish logs: %d; compile-ish files with fatal markers: %d; all-log fatal-marker files: %d." % (s["log_total"], s["compileish_log_total"], s["compileish_logs_with_fatal_markers"], s["log_files_with_fatal_markers"]))
    lines.append("- Manifest/receipt expected artifacts: %d checked; mismatches/missing/conflicts: %d." % (mc["expected_artifact_count"], mc["expected_artifact_mismatch_count"]))
    lines.append("- Batch manifest topics: %s; batch PDF hash mismatches: %s. Public apply receipt hashes: %s, errors=%s." % (mc["batch_topic_count"], mc["batch_hash_mismatch_count"], mc["public_pdf_hash_count"], mc["public_errors"]))
    lines.append("- Tori selection-function manifest: artifact_count=%s; raw SQL/JSON actual=%s/%s; raw JSON parse-ok=%s." % (mc["selection_artifact_count"], mc["selection_raw_payload_count_sql_actual"], mc["selection_raw_payload_count_json_actual"], mc["selection_raw_payload_json_ok_count"]))
    goru_missing = sum(x["missing_output_count"] for x in mc["goru_summaries"])
    lines.append("- Goru summaries checked: %d; missing declared outputs: %d." % (len(mc["goru_summaries"]), goru_missing))
    lines.append("- Quality inventory summary still records: `%s`." % mc["quality_inventory_summary"])
    lines.append("")
    lines.append("## Data/sample provenance")
    lines.append("")
    for key, rec in summary["data_provenance"].items():
        lines.append("- %s: exists=%s rows=%s bytes=%s sha256=`%s`" % (key, rec.get("exists"), rec.get("rows"), rec.get("bytes"), rec.get("sha256")))
    lines.append("- Analysis JSON files: %d checked, %d parse OK, %d with explicit guard/safety text." % (s["analysis_json_count"], s["analysis_json_ok"], s["analysis_json_with_guard"]))
    lines.append("")
    lines.append("## Script/self-containment checks")
    lines.append("")
    lines.append("- Scripts checked: %d (`*.py`/`*.sh`); syntax/header OK: %d; failures: %d." % (s["script_total"], s["script_syntax_ok"], s["script_syntax_bad"]))
    lines.append("- Executables: python3=`%s` (%s), tectonic=`%s`, shasum=`%s`, pdfinfo=`%s`." % (deps["executables"].get("python3"), deps.get("python_version"), deps["executables"].get("tectonic"), deps["executables"].get("shasum"), deps["executables"].get("pdfinfo")))
    lines.append("- Python package availability by `importlib.util.find_spec`: `%s`." % deps["python_packages_find_spec"])
    lines.append("- Reproducibility notes: main scripts use absolute `/Users/duhokim/...` paths; several require cached SDSS CSVs, the scientific Python stack, and Tectonic; first/selection scripts may perform public SDSS network reads if rerun.")
    lines.append("")
    lines.append("## Exact local repro commands")
    lines.append("")
    lines.append("```bash")
    lines.extend(summary["exact_repro_commands"])
    lines.append("```")
    lines.append("")
    lines.append("## Blocker notes")
    lines.append("")
    if summary["blockers"]:
        for blocker in summary["blockers"]:
            lines.append("- BLOCKER: %s" % blocker)
    else:
        lines.append("- No artifact-integrity blocker found in this tick: PDF magic/hash checks, manifests/receipts, compile logs, scripts, analysis JSON, and sample provenance are internally consistent for the preserved artifacts.")
    lines.append("- Non-blocker: `pdfinfo` is not installed, so PDF page counts were not extracted; binary magic and SHA256 were verified instead.")
    lines.append("- Non-blocker: lane-local Lana/Tori drafts are compiled and hashed but are not integrated into the public-linked manuscripts/PDFs; integration remains a separate Hwao/Tori/user-approved gate.")
    lines.append("- Non-blocker: recompiled PDF SHA256 can change due to TeX/PDF metadata; source/data/figure artifacts remain the stable reproducibility basis.")
    lines.append("")
    lines.append("## Safety")
    lines.append("")
    lines.append("No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git, billing, OAuth, external submission, or new cron jobs were touched. This audit wrote only Kun-lane report/JSON files; the separate one-line `OVERNIGHT_LEDGER.md` append records the tick as requested.")
    lines.append("")
    lines.append("JSON summary: `%s`" % SUMMARY)
    return "\n".join(lines) + "\n"


def main() -> None:
    for output_dir in [REPORT.parent, SUMMARY.parent, SCRIPT_PATH.parent]:
        assert_kun_write(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    batch = safe_json(BATCH_MANIFEST)
    primary_by_name = primary_pdf_paths_from_batch(batch)
    primary_paths = [p for name, p in primary_by_name.items() if name in PRIMARY_PDF_NAMES]

    expected, expected_details = build_expected_artifacts()
    pdf_paths = sorted(AUTOPILOT.rglob("*.pdf"))
    log_paths = sorted(AUTOPILOT.rglob("*.log"))
    script_paths = sorted(AUTOPILOT.rglob("*.py")) + sorted(AUTOPILOT.rglob("*.sh"))
    json_paths = sorted(AUTOPILOT.rglob("*.json"))
    manifest_like_paths = [p for p in json_paths if "manifest" in p.name.lower() or p == PUBLIC_APPLY or p == BATCH_MANIFEST]

    pdf_rows = pdf_checks(pdf_paths, expected, primary_paths)
    log_rows = log_checks(log_paths)
    script_rows = script_checks(script_paths)
    json_rows = json_inventory(json_paths)
    manifest_json_rows = json_inventory(manifest_like_paths)
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
    data_provenance: Dict[str, Any] = {}
    for key, path in data_paths.items():
        if path.suffix.lower() == ".csv":
            data_provenance[key] = count_csv_rows(path)
        else:
            data_provenance[key] = {
                "path": str(path),
                "relative_path": rel(path),
                "exists": path.exists(),
                "bytes": path.stat().st_size if path.exists() else None,
                "sha256": sha256(path) if path.exists() else None,
                "rows": None,
            }

    expected_pdf_rows = [r for r in pdf_rows if r["expected_sha256"]]
    expected_mismatches = [r for r in expected_pdf_rows if r["matches_expected_sha256"] is False or r["matches_expected_bytes"] is False or r["expected_conflicts"]]
    primary_pdf_rows = [r for r in pdf_rows if r["is_primary_linked_manuscript_pdf"]]
    primary_mismatches = [r for r in primary_pdf_rows if r["matches_expected_sha256"] is False or r["matches_expected_bytes"] is False]
    lane_expected_pdf_rows = [r for r in expected_pdf_rows if r["is_lane_local_pdf"]]
    lane_expected_pdf_mismatches = [r for r in lane_expected_pdf_rows if r["matches_expected_sha256"] is False or r["matches_expected_bytes"] is False]
    pdf_magic_bad = [r for r in pdf_rows if not r["starts_with_pdf_magic"]]
    log_bad = [r for r in log_rows if r["fatal_marker_count"]]
    compileish_logs = [r for r in log_rows if r["compileish"]]
    compileish_bad = [r for r in compileish_logs if r["fatal_marker_count"]]
    script_bad = [r for r in script_rows if r["syntax_ok"] is False]
    analysis_ok = [r for r in analyses if r["json_ok"]]
    analysis_guard = [r for r in analyses if r["has_interpretation_guard_or_safety"]]

    blockers: List[str] = []
    if pdf_magic_bad:
        blockers.append("%d PDF(s) do not start with %%PDF magic" % len(pdf_magic_bad))
    if expected_mismatches:
        blockers.append("%d PDF(s) mismatch recorded expected SHA/bytes" % len(expected_mismatches))
    if manifest["expected_artifact_mismatch_count"]:
        blockers.append("%d expected manifest/receipt artifact(s) are missing or hash/byte mismatched" % manifest["expected_artifact_mismatch_count"])
    if compileish_bad:
        blockers.append("%d compile-ish log file(s) contain fatal/traceback/LaTeX-error markers" % len(compileish_bad))
    if len(primary_pdf_rows) != 9:
        blockers.append("Primary public-linked manuscript PDF count is %d, expected 9" % len(primary_pdf_rows))
    if manifest["batch_topic_count"] != 8:
        blockers.append("Batch manifest topic count is %s, expected 8" % manifest["batch_topic_count"])
    if script_bad:
        blockers.append("%d script(s) failed syntax/header checks" % len(script_bad))
    if len(analyses) != 9 or len(analysis_ok) != 9:
        blockers.append("Analysis JSON parse count is %d/%d, expected 9/9" % (len(analysis_ok), len(analyses)))
    for key in ["raw_sdss_csv", "analysis_sample_bpt_csv", "matched_agn_sf_pairs_csv"]:
        if not data_provenance[key].get("exists"):
            blockers.append("Missing source data artifact: %s" % key)
    if data_provenance["analysis_sample_bpt_csv"].get("rows") != 60000:
        blockers.append("analysis_sample_bpt_csv rows=%s, expected 60000" % data_provenance["analysis_sample_bpt_csv"].get("rows"))
    if manifest["selection_raw_payload_count_json_expected"] != manifest["selection_raw_payload_count_json_actual"]:
        blockers.append("Selection raw JSON payload count mismatch expected=%s actual=%s" % (manifest["selection_raw_payload_count_json_expected"], manifest["selection_raw_payload_count_json_actual"]))
    if manifest["selection_raw_payload_count_sql_expected"] != manifest["selection_raw_payload_count_sql_actual"]:
        blockers.append("Selection raw SQL payload count mismatch expected=%s actual=%s" % (manifest["selection_raw_payload_count_sql_expected"], manifest["selection_raw_payload_count_sql_actual"]))

    summary_counts = {
        "pdf_total": len(pdf_rows),
        "pdf_magic_ok": sum(1 for r in pdf_rows if r["starts_with_pdf_magic"]),
        "pdf_expected_count": len(expected_pdf_rows),
        "pdf_expected_mismatches": len(expected_mismatches),
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
        "json_total": len(json_rows),
        "json_ok": sum(1 for r in json_rows if r["json_ok"]),
        "manifest_like_json_count": len(manifest_json_rows),
        "manifest_like_json_ok": sum(1 for r in manifest_json_rows if r["json_ok"]),
        "analysis_json_count": len(analyses),
        "analysis_json_ok": len(analysis_ok),
        "analysis_json_with_guard": len(analysis_guard),
        "blocking_failure_count": len(blockers),
    }

    out: Dict[str, Any] = {
        "marker": MARKER,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Kun reproducibility/integrity audit over existing aas-autopilot artifacts; no generator recompiles/reruns outside Kun lane.",
        "paths_read_first": [str(BRIEF), str(SWARM_BOARD), str(LEDGER)],
        "summary_counts": summary_counts,
        "blockers": blockers,
        "process_scan": proc,
        "dependency_checks": deps,
        "expected_details": expected_details,
        "manifest_checks": manifest,
        "data_provenance": data_provenance,
        "analysis_results": analyses,
        "json_inventory_summary": {
            "json_total": len(json_rows),
            "json_ok": sum(1 for r in json_rows if r["json_ok"]),
            "manifest_like_json_count": len(manifest_json_rows),
            "manifest_like_json_ok": sum(1 for r in manifest_json_rows if r["json_ok"]),
        },
        "manifest_like_jsons": manifest_json_rows,
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
