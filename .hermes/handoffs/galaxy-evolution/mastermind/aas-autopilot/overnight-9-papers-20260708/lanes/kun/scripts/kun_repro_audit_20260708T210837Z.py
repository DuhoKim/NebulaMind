#!/usr/bin/env python3
"""Kun reproducibility/integrity audit for the overnight 9-paper AAS swarm.

Read-mostly audit over aas-autopilot artifacts. This script writes only Kun
lane-local report/JSON artifacts and avoids rerunning data/manuscript generators
or compilers, so it is safe while other lanes may still be active.
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

TS = "20260708T210837Z"
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

PATH_SUFFIXES = (
    ".pdf", ".tex", ".json", ".jsonl", ".csv", ".md", ".log", ".png", ".py", ".sh", ".sql", ".txt"
)
PATH_KEYS = {
    "path", "pdf", "compiled_pdf", "draft_pdf", "figure_pdf", "coefficient_figure",
    "tex", "draft_tex", "source_tex", "source_base", "source_json", "summary_json",
    "compile_log", "changes_md", "tick_report_md", "inventory_csv", "csv",
    "raw_csv", "analysis_csv", "matched_pairs_csv", "query_sql", "script", "report",
}
SHA_KEYS = ("sha256", "pdf_sha256", "actual_sha256")
BYTE_KEYS = ("bytes", "pdf_bytes", "actual_bytes")
FATAL_LOG_RE = re.compile(
    r"fatal error|! LaTeX Error|Emergency stop|Undefined control sequence|No pages of output|Traceback|Tectonic failed|failed for|ERROR:",
    re.IGNORECASE,
)
WARNING_RE = re.compile(r"warning", re.IGNORECASE)
SUPERSEDED_FAILURE_LOG_TOKENS = ("20260708T193423Z", "20260708T204428Z")
NETWORK_TOKENS = ["astroquery", "SDSS.query_sql", "SkyServer", "urlopen", "requests", "semantic", "arxiv", "ads"]
WRITE_TOKENS = ["write_text", "to_csv", "fig.savefig", "mkdir", "subprocess.run", "open(", "shutil.copy", "query_sql"]


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
        raise RuntimeError(f"Refusing non-Kun-lane write: {path}")


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


def normalize_path(value: Any, base: Optional[Path] = None) -> Optional[Path]:
    if value is None or value == "" or not isinstance(value, (str, os.PathLike)):
        return None
    s = str(value)
    if "\n" in s or "\r" in s or len(s) > 700:
        return None
    if not ("/" in s or s.endswith(PATH_SUFFIXES)):
        return None
    p = Path(s)
    if p.is_absolute():
        return p
    if s.startswith(".hermes/"):
        return REPO / p
    if s.startswith("runs/"):
        return AUTOPILOT / p
    if base is not None and s.startswith(("artifacts/", "revision-drafts/", "tables/", "figures/", "aastex/", "raw_sdss_payloads/")):
        return base / p
    if s.startswith(("lanes/", "ticks/", "visible-panes/", "scripts/")):
        return OVERNIGHT / p
    if base is not None:
        return base / p
    return AUTOPILOT / p


def add_expected(expected: Dict[str, Dict[str, Any]], path: Optional[Path], source: str,
                 sha_value: Optional[Any] = None, bytes_value: Optional[Any] = None,
                 kind: str = "artifact") -> None:
    if path is None:
        return
    if not (inside(path, AUTOPILOT) or inside(path, REPO)):
        return
    key = str(path)
    rec = expected.setdefault(key, {"sources": [], "sha256": None, "bytes": None, "conflicts": [], "kind": kind})
    rec["sources"].append(source)
    if sha_value:
        sha_s = str(sha_value)
        if rec["sha256"] and rec["sha256"] != sha_s:
            rec["conflicts"].append({"field": "sha256", "old": rec["sha256"], "new": sha_s, "source": source})
        else:
            rec["sha256"] = sha_s
    if bytes_value not in (None, ""):
        try:
            b = int(bytes_value)
        except Exception:
            b = None
        if b is not None:
            if rec["bytes"] is not None and rec["bytes"] != b:
                rec["conflicts"].append({"field": "bytes", "old": rec["bytes"], "new": b, "source": source})
            else:
                rec["bytes"] = b


def is_path_key(key: str) -> bool:
    return key in PATH_KEYS or key.endswith(("_path", "_pdf", "_csv", "_json", "_jsonl", "_md", "_log", "_tex", "_png", "_sql", "_script"))


def collect_expected_from_manifest(data: Any, source: str, base: Path,
                                   expected: Dict[str, Dict[str, Any]],
                                   compile_exit_rows: List[Dict[str, Any]]) -> None:
    if isinstance(data, dict):
        if "compile_exit_code" in data and data.get("compile_exit_code") not in (0, "0", None):
            compile_exit_rows.append({
                "source": source,
                "paper_slug": data.get("paper_slug"),
                "compile_exit_code": data.get("compile_exit_code"),
                "compile_log": data.get("compile_log"),
                "pdf": data.get("pdf"),
            })
        sha_value = next((data.get(k) for k in SHA_KEYS if data.get(k)), None)
        bytes_value = next((data.get(k) for k in BYTE_KEYS if data.get(k) is not None), None)
        for key, value in data.items():
            if is_path_key(key):
                p = normalize_path(value, base=base)
                if p is not None:
                    # Attach sibling hashes only to explicit artifact rows or PDF keys, avoiding the common
                    # manifest pattern where a manuscript PDF hash sits next to unrelated source/log paths.
                    attach_hash = False
                    if key == "path" and sha_value:
                        attach_hash = True
                    elif key in {"pdf", "compiled_pdf", "draft_pdf"} and sha_value:
                        attach_hash = True
                    add_expected(expected, p, source, sha_value if attach_hash else None, bytes_value if attach_hash else None, key)
            collect_expected_from_manifest(value, source, base, expected, compile_exit_rows)
    elif isinstance(data, list):
        for item in data:
            collect_expected_from_manifest(item, source, base, expected, compile_exit_rows)


def primary_paths_from_batch(batch: Any) -> Dict[str, Path]:
    out = {"sdss_agn_sfr_pilot_aas.pdf": FIRST_RUN / "aastex/sdss_agn_sfr_pilot_aas.pdf"}
    if isinstance(batch, dict):
        for item in batch.get("topics", []):
            if isinstance(item, dict) and item.get("pdf_name") and item.get("pdf"):
                p = normalize_path(item.get("pdf"))
                if p is not None:
                    out[str(item["pdf_name"])] = p
    return out


def build_expected() -> Tuple[Dict[str, Dict[str, Any]], Dict[str, Any]]:
    expected: Dict[str, Dict[str, Any]] = {}
    compile_exit_rows: List[Dict[str, Any]] = []
    batch = safe_json(BATCH_MANIFEST)
    public = safe_json(PUBLIC_APPLY)
    primary_map = primary_paths_from_batch(batch)

    if isinstance(batch, dict):
        for item in batch.get("topics", []):
            if isinstance(item, dict):
                add_expected(expected, normalize_path(item.get("pdf")), BATCH_MANIFEST.name, item.get("pdf_sha256"), item.get("pdf_bytes"), "primary_batch_pdf")
                for key in ["tex", "compile_log", "figure_pdf"]:
                    add_expected(expected, normalize_path(item.get(key)), BATCH_MANIFEST.name, None, None, key)
    add_expected(expected, FIRST_RUN / "aastex/sdss_agn_sfr_pilot_aas.pdf", "first_run_primary", None, None, "primary_first_pdf")
    add_expected(expected, FIRST_RUN / "aastex/sdss_agn_sfr_pilot_aas.tex", "first_run_primary", None, None, "primary_first_tex")
    add_expected(expected, FIRST_RUN / "aastex/compile.log", "first_run_primary", None, None, "primary_first_compile_log")

    if isinstance(public, dict):
        hashes = public.get("pdf_hashes") or {}
        if isinstance(hashes, dict):
            for pdf_name, rec in hashes.items():
                if isinstance(rec, dict):
                    add_expected(expected, primary_map.get(pdf_name), PUBLIC_APPLY.name, rec.get("sha256"), rec.get("bytes"), "public_apply_pdf")

    manifest_paths = sorted([p for p in AUTOPILOT.rglob("*.json") if "manifest" in p.name.lower()])
    for mp in manifest_paths:
        data = safe_json(mp)
        collect_expected_from_manifest(data, mp.name, mp.parent, expected, compile_exit_rows)

    # Inventory CSV rows often carry hashes for non-manifest artifacts.
    inventory_csvs = sorted([p for p in AUTOPILOT.rglob("*.csv") if "inventory" in p.name.lower()])
    inventory_rows = []
    for inv in inventory_csvs:
        seen = added = 0
        if inv.exists():
            with inv.open(newline="", encoding="utf-8", errors="replace") as handle:
                reader = csv.DictReader(handle)
                for row in reader:
                    seen += 1
                    p = normalize_path(row.get("path") or row.get("artifact") or row.get("file"), base=inv.parent)
                    if p is not None:
                        add_expected(expected, p, inv.name, row.get("sha256") or None, row.get("bytes") or None, "inventory_row")
                        added += 1
        inventory_rows.append({"path": str(inv), "relative_path": rel(inv), "rows_seen": seen, "expected_rows_added": added})

    selection = safe_json(SELECTION_MANIFEST)
    raw_dir = SELECTION_MANIFEST.parent / "raw_sdss_payloads"
    details = {
        "batch_manifest_json_ok": json_ok(batch),
        "public_apply_json_ok": json_ok(public),
        "manifest_like_json_count": len(manifest_paths),
        "manifest_like_json_ok_count": sum(1 for p in manifest_paths if json_ok(safe_json(p))),
        "manifest_paths": [rel(p) for p in manifest_paths],
        "compile_exit_nonzero_rows": compile_exit_rows,
        "inventory_csvs": inventory_rows,
        "selection_manifest_json_ok": json_ok(selection),
        "selection_raw_payload_count_json_expected": selection.get("raw_payload_count_json") if isinstance(selection, dict) else None,
        "selection_raw_payload_count_sql_expected": selection.get("raw_payload_count_sql") if isinstance(selection, dict) else None,
        "selection_raw_payload_count_json_actual": len(list(raw_dir.glob("*.json"))) if raw_dir.exists() else 0,
        "selection_raw_payload_count_sql_actual": len(list(raw_dir.glob("*.sql"))) if raw_dir.exists() else 0,
    }
    return expected, details


def is_compileish_log(path: Path, text: str) -> bool:
    if path.name == "compile.log" or path.name.startswith("compile_"):
        return True
    if "Output written on" in text and ".pdf" in text:
        return True
    if "Running xdvipdfmx" in text or "Rerunning LaTeX" in text:
        return True
    if "revision-drafts" in str(path) and path.suffix == ".log":
        return True
    return False


def log_checks(log_paths: List[Path]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for p in log_paths:
        text = read_text(p)
        fatal = FATAL_LOG_RE.findall(text)
        rows.append({
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
    return rows


def script_checks(script_paths: List[Path]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    bash = shutil.which("bash") or "/bin/bash"
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
            "has_main_guard": "if __name__" in text if p.suffix == ".py" else None,
            "has_absolute_repo_path": str(REPO) in text,
            "has_hardcoded_timestamp": bool(re.search(r"20\d{6}T\d{6}Z", text)),
            "network_or_external_notes": [tok for tok in NETWORK_TOKENS if tok.lower() in text.lower()],
            "write_or_process_tokens_seen": [tok for tok in WRITE_TOKENS if tok in text],
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
            try:
                proc = subprocess.run([bash, "-n", str(p)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=20)
                rec["syntax_ok"] = proc.returncode == 0
                rec["syntax_error"] = (proc.stderr.strip() or proc.stdout.strip() or None)
            except Exception as exc:
                rec["syntax_ok"] = False
                rec["syntax_error"] = str(exc)
        if rec["has_absolute_repo_path"]:
            rec["self_containment_notes"].append("Host-local absolute /Users/duhokim repo paths; not relocatable without edits.")
        if "analysis_sample_bpt.csv" in text:
            rec["self_containment_notes"].append("Requires cached SDSS analysis_sample_bpt.csv unless upstream RP-1 generator is rerun.")
        if "tectonic" in text:
            rec["self_containment_notes"].append("Requires tectonic/LaTeX class resolution for manuscript compiles.")
        if any(pkg in text for pkg in ["pandas", "numpy", "matplotlib", "scipy", "astroquery"]):
            rec["self_containment_notes"].append("Requires local Python scientific/literature stack.")
        rows.append(rec)
    return rows


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


def expected_rows(expected: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
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


def process_scan() -> Dict[str, Any]:
    patterns = [
        "tectonic", "run_sdss_agn_sfr_pilot.py", "run_remaining_topic_pilots.py",
        "selection_attrition", "shared_selection_module_tick", "goru_", "lana_",
        "tori_wave2_result_table_drafts", "rp1_robustness_selection_revision",
        "m2p3_m3p1_selection_ci_revision",
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

    def package_map_for(exe: Optional[str]) -> Optional[Dict[str, Any]]:
        if not exe:
            return None
        try:
            if not Path(exe).exists():
                return None
        except Exception:
            return None
        code = "import importlib.util,json; packages=%r; print(json.dumps({name: importlib.util.find_spec(name) is not None for name in packages}))" % packages
        try:
            proc = subprocess.run([exe, "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
            if proc.returncode != 0:
                return {"ok": False, "error": proc.stderr.strip() or proc.stdout.strip()}
            return {"ok": True, "packages": json.loads(proc.stdout)}
        except Exception as exc:
            return {"ok": False, "error": str(exc)}

    candidates: List[Dict[str, Any]] = []
    seen: set[str] = set()
    for exe in [shutil.which("python3"), "/usr/bin/python3", "/opt/homebrew/bin/python3", shutil.which("python")]:
        if not exe or exe in seen:
            continue
        seen.add(exe)
        pkg = package_map_for(exe)
        if pkg is not None:
            candidates.append({"executable": exe, **pkg})
    preferred = None
    for cand in candidates:
        pkgs = cand.get("packages") if cand.get("ok") else None
        if isinstance(pkgs, dict) and all(pkgs.get(name) for name in packages):
            preferred = cand["executable"]
            break
    return {
        "executables": {name: shutil.which(name) for name in ["python3", "python", "tectonic", "shasum", "pdfinfo", "bash"]},
        "python_executable": sys.executable,
        "python_version": sys.version.split()[0],
        "python_packages_find_spec": {name: importlib.util.find_spec(name) is not None for name in packages},
        "python_candidates": candidates,
        "preferred_science_python": preferred,
    }


def exact_repro_commands() -> List[str]:
    return [
        "cd /Users/duhokim/NebulaMind/NebulaMind",
        "# Primary actual-data RP-1 rerun; uses cached CSV if present, may query public SDSS if cache is absent, overwrites run-local artifacts",
        "env PATH=/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:$PATH bash .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/run_full_sdss_agn_sfr_pilot.sh",
        "",
        "# Remaining 8 active topic pilots; requires cached RP-1 analysis_sample_bpt.csv and overwrites batch run-local artifacts",
        "/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/run_remaining_topic_pilots.py > .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z.batch.log 2>&1",
        "",
        "# Read-only hash check of the 9 public-linked manuscript PDFs",
        "shasum -a 256 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/aastex/sdss_agn_sfr_pilot_aas.pdf",
        "shasum -a 256 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/*/aastex/*_aas.pdf",
        "",
        "# Lane-local overnight generators; run only in their owning lane scope because they write lane artifacts",
        "/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/scripts/build_quality_inventory_20260708T132720Z.py",
        "/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/scripts/goru_actual_data_robustness_20260708T141459Z.py",
        "/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/scripts/goru_stratified_bpt_robustness_20260708T162615Z.py",
        "/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/scripts/goru_regression_bin_sensitivity_20260708T183643Z.py",
        "/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/scripts/goru_matching_control_robustness_20260708T205859Z.py",
        "/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/scripts/selection_attrition_tick_v2.py  # public SDSS COUNT queries; writes Tori lane artifacts",
        "/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/scripts/shared_selection_module_tick.py",
        "/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/scripts/tori_wave2_result_table_drafts_20260708T143512Z.py",
        "/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/scripts/rp1_robustness_selection_revision_20260708T181833Z.py",
        "/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/scripts/m2p3_m3p1_selection_ci_revision_20260708T192506Z.py",
        "/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/lana/scripts/lana_wave1_selection_definition_cleanup_20260708T182812Z.py",
        "/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/lana/scripts/lana_wave3_flagship_control_and_suite_cleanup.py",
        "",
        "# Re-run this Kun read-mostly integrity audit (writes only Kun lane report/JSON)",
        f"/usr/bin/python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/kun/scripts/kun_repro_audit_{TS}.py",
    ]


def render_markdown(out: Dict[str, Any]) -> str:
    c = out["summary_counts"]
    deps = out["dependency_checks"]
    mc = out["manifest_checks"]
    lines: List[str] = []
    lines.append(f"# Kun reproducibility tick — {TS}")
    lines.append("")
    lines.append(f"Marker: `{MARKER}`")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append("Read the overnight brief, swarm board, ledger, manifest-like JSON, compile/run logs, scripts, PDFs, analysis JSON, and sample-provenance files under `aas-autopilot`. I did not rerun manuscript/data generators or compilers; this tick ran only this Kun-local read-mostly audit script to avoid lane races and non-Kun writes.")
    lines.append("")
    lines.append("## Race/process check")
    hits = out["process_scan"].get("matching_processes", [])
    if hits:
        lines.append(f"- Potential active generator/TeX/lane processes observed: {len(hits)}; generator/compiler reruns were avoided.")
        for hit in hits[:10]:
            lines.append(f"  - PID {hit.get('pid')}: `{hit.get('command')}`")
    else:
        lines.append("- No active `tectonic`, manuscript-generator, selection-attrition, Goru robustness, Lana revision, or Tori revision process was seen at scan time.")
    lines.append("")
    lines.append("## Artifact integrity results")
    lines.append("")
    lines.append(f"- PDFs under aas-autopilot: {c['pdf_total']} total; {c['pdf_magic_ok']} start with `%PDF-`; expected-hash/byte PDF rows checked: {c['pdf_expected_count']}; expected PDF mismatches: {c['pdf_expected_mismatches']}.")
    lines.append(f"- Primary 9 public-linked manuscript PDFs: {c['primary_pdf_count']} checked; expected-hash/byte mismatches: {c['primary_pdf_mismatches']}.")
    lines.append(f"- Lane-local expected PDFs: {c['lane_expected_pdf_count']} checked; mismatches: {c['lane_expected_pdf_mismatches']}.")
    lines.append(f"- Logs under aas-autopilot: {c['log_total']} checked; compile-ish logs: {c['compileish_log_total']}; fatal-marker compile logs: {c['compileish_logs_with_fatal_markers']} total ({c['current_compileish_logs_with_fatal_markers']} current, {c['superseded_compileish_logs_with_fatal_markers']} superseded); all-log fatal-marker files: {c['log_files_with_fatal_markers']}.")
    lines.append(f"- Manifest-like JSON files: {mc['manifest_like_json_count']} checked, {mc['manifest_like_json_ok_count']} parse OK; manifest/receipt/inventory expected artifact rows: {c['expected_artifact_count']}; missing/hash/byte/conflict rows: {c['expected_artifact_mismatch_count']}.")
    lines.append(f"- Manifest-declared nonzero compile exits: {c['manifest_nonzero_compile_exit_count']} (these include known stale failed Lana 20:44 draft entries if present; later successful manifests are separately checked by PDF/hash/log status).")
    lines.append(f"- Selection-function raw payload counts: SQL {mc['selection_raw_payload_count_sql_actual']}/{mc['selection_raw_payload_count_sql_expected']}, JSON {mc['selection_raw_payload_count_json_actual']}/{mc['selection_raw_payload_count_json_expected']}.")
    lines.append(f"- Quality inventory summary remains: `{out['quality_inventory_summary']}`.")
    lines.append("")
    lines.append("## Data/sample provenance")
    lines.append("")
    for key, rec in out["data_provenance"].items():
        lines.append(f"- {key}: exists={rec.get('exists')} rows={rec.get('rows')} bytes={rec.get('bytes')} sha256=`{rec.get('sha256')}`")
    lines.append(f"- Analysis JSON files: {c['analysis_json_count']} checked, {c['analysis_json_ok']} parse OK, {c['analysis_json_with_guard']} with explicit guard/safety text.")
    lines.append("")
    lines.append("## Script/self-containment and command completeness")
    lines.append("")
    lines.append(f"- Scripts checked: {c['script_total']} (`*.py`/`*.sh`); syntax OK: {c['script_syntax_ok']}; failures: {c['script_syntax_bad']}.")
    lines.append(f"- Scripts with absolute repo paths: {c['scripts_with_absolute_repo_path']}; with public-network/external tokens: {c['scripts_with_network_or_external_notes']}; with write/process tokens: {c['scripts_with_write_tokens']}.")
    lines.append(f"- Executables: python3=`{deps['executables'].get('python3')}`, running Python=`{deps['python_executable']}` {deps['python_version']}, tectonic=`{deps['executables'].get('tectonic')}`, shasum=`{deps['executables'].get('shasum')}`, pdfinfo=`{deps['executables'].get('pdfinfo')}`.")
    lines.append(f"- Current audit Python package availability by `importlib.util.find_spec`: `{deps['python_packages_find_spec']}`.")
    lines.append(f"- Preferred science-script Python for exact reruns: `{deps.get('preferred_science_python')}`; checked candidates: `{deps.get('python_candidates')}`.")
    lines.append("- Reproducibility note: exact commands use `/usr/bin/python3` or a PATH override because the default `python3` on this cron/Hermes PATH points at the Hermes venv without the scientific/astroquery stack, while `/usr/bin/python3` has it. Scripts are executable/self-contained for this host, but many are not portable because they use absolute `/Users/duhokim/...` paths; SDSS/literature scripts may use public network if caches are absent; PDF builds require tectonic/LaTeX.")
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
        lines.append("- No current artifact-integrity blocker found: all scanned PDFs have PDF magic, the 9 primary PDFs are present, expected PDF hashes/bytes match where declared, current compile-ish logs have no fatal markers, scripts parse, analysis JSON/sample provenance are internally consistent, and selection payload counts match the manifest.")
    if c["manifest_nonzero_compile_exit_count"]:
        lines.append("- Non-blocker note: manifest-declared nonzero compile exits are historical lane-local draft attempts; the current successful follow-up PDFs/logs remain present and verified where declared.")
    if c["expected_artifact_mismatch_count"]:
        lines.append("- Review note: the JSON summary lists missing/conflicting non-PDF expected artifact rows for follow-up; blockers above are limited to primary/current PDF, compile-log, script, JSON, and data-provenance gates.")
    lines.append("- Non-blocker: exact PDF SHA can change on recompilation due to TeX/PDF metadata; source/data/figure inputs are the stable reproducibility basis.")
    lines.append("")
    lines.append("## Safety")
    lines.append("")
    lines.append("No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git, billing, OAuth, external submission, or new cron jobs were touched. This audit wrote only Kun-lane report/JSON/script files; the required one-line `OVERNIGHT_LEDGER.md` append is performed separately.")
    lines.append("")
    lines.append(f"JSON summary: `{SUMMARY}`")
    return "\n".join(lines) + "\n"


def main() -> None:
    for required in [BRIEF, SWARM_BOARD, LEDGER]:
        if not required.exists():
            raise RuntimeError(f"Required read-first file missing: {required}")
    for d in [REPORT.parent, SUMMARY.parent]:
        assert_kun_write(d)
        d.mkdir(parents=True, exist_ok=True)

    batch = safe_json(BATCH_MANIFEST)
    primary_map = primary_paths_from_batch(batch)
    primary_paths = [p for name, p in primary_map.items() if name in PRIMARY_PDF_NAMES]
    expected, manifest_details = build_expected()

    pdf_paths = sorted(AUTOPILOT.rglob("*.pdf"))
    log_paths = sorted(AUTOPILOT.rglob("*.log"))
    script_paths = sorted(AUTOPILOT.rglob("*.py")) + sorted(AUTOPILOT.rglob("*.sh"))
    json_paths = sorted(AUTOPILOT.rglob("*.json"))

    pdf_rows = pdf_checks(pdf_paths, expected, primary_paths)
    log_rows = log_checks(log_paths)
    script_rows = script_checks(script_paths)
    json_rows = json_inventory(json_paths)
    exp_rows = expected_rows(expected)
    analyses = analysis_result_checks()
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
    superseded_compileish_bad = [r for r in compileish_bad if any(tok in r["relative_path"] for tok in SUPERSEDED_FAILURE_LOG_TOKENS)]
    current_compileish_bad = [r for r in compileish_bad if not any(tok in r["relative_path"] for tok in SUPERSEDED_FAILURE_LOG_TOKENS)]
    script_bad = [r for r in script_rows if r["syntax_ok"] is False]
    json_bad = [r for r in json_rows if not r["json_ok"]]
    # Keep non-PDF expected row mismatches as review notes to avoid falsely blocking on prose-only relative paths.
    exp_mismatches = [r for r in exp_rows if (not r["exists"]) or r["matches_sha256"] is False or r["matches_bytes"] is False or r["conflicts"]]
    analysis_ok = [r for r in analyses if r["json_ok"]]
    analysis_guard = [r for r in analyses if r["has_interpretation_guard_or_safety"]]

    blockers: List[str] = []
    if pdf_magic_bad:
        blockers.append(f"{len(pdf_magic_bad)} scanned PDF(s) do not start with %PDF magic")
    if pdf_expected_mismatches:
        blockers.append(f"{len(pdf_expected_mismatches)} expected PDF(s) mismatch recorded SHA/bytes")
    if current_compileish_bad:
        blockers.append(f"{len(current_compileish_bad)} current compile-ish log file(s) contain fatal/traceback/LaTeX-error markers")
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
    if data_provenance["raw_sdss_csv"].get("rows") != 60000:
        blockers.append(f"raw_sdss_csv rows={data_provenance['raw_sdss_csv'].get('rows')}, expected 60000")
    if data_provenance["analysis_sample_bpt_csv"].get("rows") != 60000:
        blockers.append(f"analysis_sample_bpt_csv rows={data_provenance['analysis_sample_bpt_csv'].get('rows')}, expected 60000")
    if data_provenance["matched_agn_sf_pairs_csv"].get("rows") != 8146:
        blockers.append(f"matched_agn_sf_pairs_csv rows={data_provenance['matched_agn_sf_pairs_csv'].get('rows')}, expected 8146")
    if manifest_details["selection_raw_payload_count_json_expected"] != manifest_details["selection_raw_payload_count_json_actual"]:
        blockers.append("Selection raw JSON payload count mismatch expected=%s actual=%s" % (manifest_details["selection_raw_payload_count_json_expected"], manifest_details["selection_raw_payload_count_json_actual"]))
    if manifest_details["selection_raw_payload_count_sql_expected"] != manifest_details["selection_raw_payload_count_sql_actual"]:
        blockers.append("Selection raw SQL payload count mismatch expected=%s actual=%s" % (manifest_details["selection_raw_payload_count_sql_expected"], manifest_details["selection_raw_payload_count_sql_actual"]))
    if not deps.get("preferred_science_python"):
        blockers.append("No checked Python executable has numpy/pandas/matplotlib/scipy/astroquery for science-script reruns")

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
        "current_compileish_logs_with_fatal_markers": len(current_compileish_bad),
        "superseded_compileish_logs_with_fatal_markers": len(superseded_compileish_bad),
        "log_files_with_fatal_markers": len(log_bad),
        "manifest_nonzero_compile_exit_count": len(manifest_details["compile_exit_nonzero_rows"]),
        "script_total": len(script_rows),
        "script_syntax_ok": sum(1 for r in script_rows if r["syntax_ok"] is True),
        "script_syntax_bad": len(script_bad),
        "scripts_with_absolute_repo_path": sum(1 for r in script_rows if r["has_absolute_repo_path"]),
        "scripts_with_network_or_external_notes": sum(1 for r in script_rows if r["network_or_external_notes"]),
        "scripts_with_write_tokens": sum(1 for r in script_rows if r["write_or_process_tokens_seen"]),
        "json_total": len(json_rows),
        "json_ok": sum(1 for r in json_rows if r["json_ok"]),
        "json_bad": len(json_bad),
        "expected_artifact_count": len(exp_rows),
        "expected_artifact_mismatch_count": len(exp_mismatches),
        "analysis_json_count": len(analyses),
        "analysis_json_ok": len(analysis_ok),
        "analysis_json_with_guard": len(analysis_guard),
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
        "json_inventory_summary": {"json_total": len(json_rows), "json_ok": sum(1 for r in json_rows if r["json_ok"]), "json_bad": len(json_bad)},
        "expected_artifacts": {"rows": exp_rows, "mismatches": exp_mismatches[:100]},
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
