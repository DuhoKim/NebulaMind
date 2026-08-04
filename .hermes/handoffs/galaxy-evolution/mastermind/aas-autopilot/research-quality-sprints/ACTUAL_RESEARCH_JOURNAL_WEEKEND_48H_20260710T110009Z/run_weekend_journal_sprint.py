#!/usr/bin/env python3
"""Local-only 48-hour NebulaMind weekend journal-paper sprint orchestrator.

The orchestrator is intentionally conservative:
- writes only under the sprint directory or the active candidate copy
- never mutates the seed package
- separates integrity blockers from journal-quality gaps
- uses read-only reviewer lanes before a single candidate-local writer lane
- treats compilation logs and provenance receipts as first-class state
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Callable

SPRINT = Path(__file__).resolve().parent
SPRINT_ID = SPRINT.name
AUTO = SPRINT.parents[1]
REPO = AUTO.parents[4]

SEED_PACKAGE = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/"
    "research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/"
    "candidates/cycle_49_package"
)

DEFAULT_DURATION_SECONDS = 172800
DEFAULT_MAX_CYCLES = 24
DEFAULT_SLOT_SECONDS = 7200
HEARTBEAT_SECONDS = 60
REPORT_MAX_BYTES = 240_000
REPORT_MIN_BYTES = 180
PROVIDER_TIMEOUT_SECONDS = 75 * 60
INTEGRATOR_TIMEOUT_SECONDS = 60 * 60
ANALYST_TIMEOUT_SECONDS = 45 * 60

FLAGSHIP_DIR = Path("flagship_rp1")
SUPPLEMENT_DIR = Path("supplementary_denominator_atlas")
FLAGSHIP_TEX = FLAGSHIP_DIR / "aastex/rp1_flagship_polished.tex"
SUPPLEMENT_TEX = SUPPLEMENT_DIR / "aastex/supplementary_denominator_atlas.tex"
TEX_RELATIVES = [FLAGSHIP_TEX, SUPPLEMENT_TEX]
CANDIDATE_TOP_DIRS = [FLAGSHIP_DIR, SUPPLEMENT_DIR, Path("provenance"), Path("analysis_extensions")]

PHASES = [
    "baseline referee",
    "real-data feasibility",
    "methods",
    "statistics/robustness",
    "tables/figures",
    "literature",
    "introduction",
    "results",
    "discussion",
    "limitations",
    "supplement",
    "reproducibility",
    "referee 1",
    "data audit",
    "TeX/layout",
    "citations",
    "abstract/title",
    "journal style",
    "adversarial claims",
    "coherence",
    "reanalysis",
    "referee 2",
    "final revision",
    "final dossier",
]
MILESTONE_CYCLES = {1, 4, 8, 12, 16, 20, 24}
ANALYST_PHASES = {"real-data feasibility", "statistics/robustness", "tables/figures", "data audit", "reanalysis"}

LOW_USAGE_WORKHORSES = {
    "director_science": "AGY Gemini 3.1 Pro (Low)",
    "literature": "AGY Gemini 3.1 Pro (Low)",
    "fact_check": "AGY Gemini 3.5 Flash (Low)",
    "codex_repro_tex": "Codex gpt-5.4-mini",
    "codex_milestone": "Codex gpt-5.5",
}

SAFETY_LOCKS = [
    "Work only inside this local sprint directory and active candidate copies.",
    "No public/static replacement, DB/API/wiki/trust writes, deploy/restart, git writes, cron, billing/OAuth/account/credentials, browser automation, or external submission.",
    "No Claude API.",
    "No credentials, token, cookie, or account reads.",
    "No automatic execution of untrusted scripts outside the Codex sandbox.",
]

REAL_DATA_RULES = [
    "No mock, synthetic, placeholder, toy, or invented data.",
    "No invented numbers, citations, source identifiers, sample sizes, table values, or figure values.",
    "Every new measured result must trace to an existing real file and provenance receipt.",
    "Public literature can support interpretation but cannot become a measured project result.",
    "Keep RP-1 association-only unless real local evidence justifies stronger wording.",
]

NUMERIC_INVARIANTS = ["8,146", "-1.309", "[-1.334,-1.283]", "249,917", "60,000", "24.0"]
WORKFLOW_PHRASES = [
    "mock data",
    "synthetic data",
    "placeholder data",
    "toy data",
    "invented",
    "not measured here",
    "needs real data",
]
BAD_DATA_USE_PATTERNS = [
    r"\b(?:use|used|using|based on|generated|created|filled|substituted)\b[^.\n]{0,80}\b(?:mock|synthetic|fake|placeholder|toy) data\b",
    r"\b(?:mock|synthetic|fake|placeholder|toy) data\b[^.\n]{0,80}\b(?:result|sample|catalog|catalogue|table|measurement|analysis)\b",
]

STOP_REQUESTED = False


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_utc(value: str) -> dt.datetime:
    return dt.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_text(path: Path, text: str) -> None:
    assert_inside_sprint(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def append_text(path: Path, text: str) -> None:
    assert_inside_sprint(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(text)


def read_text(path: Path, limit: int | None = None) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""
    if limit is not None and len(text) > limit:
        return text[:limit] + "\n[TRUNCATED]\n"
    return text


def assert_inside_sprint(path: Path) -> None:
    resolved = path.resolve()
    sprint = SPRINT.resolve()
    if resolved != sprint and sprint not in resolved.parents:
        raise ValueError(f"Refusing to write outside sprint root: {path}")


def is_live_pid(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def refuse_if_running() -> None:
    pid_path = SPRINT / "RUNNING.pid"
    if not pid_path.exists():
        return
    try:
        pid = int(pid_path.read_text().strip())
    except ValueError:
        return
    if pid != os.getpid() and is_live_pid(pid):
        raise RuntimeError(f"Another live sprint process is already running: pid {pid}")


def command_exists(name: str) -> bool:
    return shutil.which(name) is not None


def status_update(**kwargs: Any) -> None:
    path = SPRINT / "SPRINT_STATUS.json"
    current: dict[str, Any] = {}
    if path.exists():
        try:
            current = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            current = {}
    current.update(kwargs)
    current["updated_utc"] = utc_now()
    write_text(path, json.dumps(current, indent=2, sort_keys=True) + "\n")


def ledger(line: str) -> None:
    append_text(SPRINT / "SPRINT_LEDGER.md", f"- {utc_now()} {line}\n")


def strip_tex_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        escaped = False
        out = []
        for ch in line:
            if ch == "%" and not escaped:
                break
            out.append(ch)
            escaped = ch == "\\" and not escaped
        lines.append("".join(out))
    return "\n".join(lines)


def tex_to_words(text: str) -> list[str]:
    text = strip_tex_comments(text)
    text = re.sub(r"\\begin\{[^}]+\}|\\end\{[^}]+\}", " ", text)
    text = re.sub(r"\\[a-zA-Z]+(?:\[[^\]]*\])?(?:\{[^{}]*\})?", " ", text)
    text = re.sub(r"[$_^{}&#~]", " ", text)
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9.'+-]*", text)


def env_body(text: str, name: str) -> str:
    m = re.search(rf"\\begin\{{{re.escape(name)}\}}(.*?)\\end\{{{re.escape(name)}\}}", text, re.S)
    return m.group(1) if m else ""


def journal_metrics(flagship_text: str, supplement_text: str) -> dict[str, Any]:
    main_words = len(tex_to_words(flagship_text))
    abstract_words = len(tex_to_words(env_body(flagship_text, "abstract")))
    supplement_words = len(tex_to_words(supplement_text))
    combined = flagship_text + "\n" + supplement_text
    citation_keys: set[str] = set()
    for match in re.finditer(r"\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}", combined):
        citation_keys.update(k.strip() for k in match.group(1).split(",") if k.strip())
    reference_keys = set(re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", combined))
    reference_keys.update(re.findall(r"@(?:article|book|misc|inproceedings|phdthesis|techreport)\{([^,]+),", combined, re.I))
    displayed_equations = (
        len(re.findall(r"\\begin\{(?:equation|align|eqnarray|multline|gather)\*?\}", flagship_text))
        + len(re.findall(r"\\\[", flagship_text))
    )
    quantitative_prior_work = bool(
        re.search(r"(?is)(prior work|previous work|published|literature).{0,240}[-+]?\d", flagship_text)
        or re.search(r"(?is)[-+]?\d.{0,240}(prior work|previous work|published|literature)", flagship_text)
    )
    metrics = {
        "flagship_words_approx": main_words,
        "abstract_words_approx": abstract_words,
        "supplement_words_approx": supplement_words,
        "section_count": len(re.findall(r"\\section\*?\{", flagship_text)),
        "equation_count": displayed_equations,
        "table_count": len(re.findall(r"\\begin\{(?:deluxetable|table)\*?\}", flagship_text)),
        "figure_count": len(re.findall(r"\\begin\{figure\*?\}", flagship_text)),
        "citation_command_count": len(re.findall(r"\\cite\w*(?:\[[^\]]*\])*\{", flagship_text)),
        "citation_key_count": len(citation_keys),
        "reference_key_count": len(reference_keys),
        "quantitative_prior_work_comparison_present": quantitative_prior_work,
        "workflow_phrase_scan": {p: len(re.findall(re.escape(p), combined, re.I)) for p in WORKFLOW_PHRASES},
        "bad_data_use_hits": [
            re.sub(r"\s+", " ", match.group(0)).strip()
            for pattern in BAD_DATA_USE_PATTERNS
            for match in re.finditer(pattern, combined, re.I)
        ][:30],
        "numeric_invariants_missing": [x for x in NUMERIC_INVARIANTS if x not in flagship_text],
    }
    return metrics


def classify_quality_blockers(metrics: dict[str, Any]) -> list[str]:
    blockers = []
    if not 5000 <= metrics["flagship_words_approx"] <= 8000:
        blockers.append("flagship main text outside 5000-8000 target")
    if not 200 <= metrics["abstract_words_approx"] <= 350:
        blockers.append("abstract outside 200-350 target")
    if metrics["citation_key_count"] < 20:
        blockers.append("fewer than 20 contextual citation keys")
    if metrics["equation_count"] < 2:
        blockers.append("fewer than 2 displayed equations")
    if metrics["table_count"] < 3:
        blockers.append("fewer than 3 real-data-derived tables")
    if metrics["figure_count"] < 2:
        blockers.append("fewer than 2 figures")
    if not metrics["quantitative_prior_work_comparison_present"]:
        blockers.append("missing explicit quantitative comparison to prior work")
    if metrics["supplement_words_approx"] < 4000:
        blockers.append("supplement below 4000-word target")
    if any(metrics.get("workflow_phrase_scan", {}).values()):
        blockers.append("workflow/operator safety prose remains in manuscript")
    return blockers


def classify_integrity_blockers(metrics: dict[str, Any], compile_audit: dict[str, Any], provenance: dict[str, Any]) -> list[str]:
    blockers = []
    if not compile_audit.get("build_ok"):
        blockers.append("strict compile failed")
    if compile_audit.get("fatal_errors") or compile_audit.get("missing_includes"):
        blockers.append("fatal TeX errors or missing includes")
    if compile_audit.get("undefined_citations") or compile_audit.get("undefined_references"):
        blockers.append("undefined citations or references")
    if compile_audit.get("writer_scope_violations"):
        blockers.append("candidate writer attempted out-of-scope changes")
    if metrics.get("numeric_invariants_missing"):
        blockers.append("numeric invariants missing")
    if provenance.get("new_result_without_provenance"):
        blockers.append("new measured result lacks source custody")
    if provenance.get("custody_errors"):
        blockers.append("candidate source custody receipt is stale or invalid")
    if metrics.get("bad_data_use_hits"):
        blockers.append("forbidden use of mock/synthetic/placeholder/toy data")
    return sorted(set(blockers))


def should_copy_file(rel: Path) -> bool:
    parts = set(rel.parts)
    name = rel.name
    lower = name.lower()
    if name.startswith("CYCLE_") or name.startswith("FINAL_") or name in {"SPRINT_STATUS.json", "RUNNING.pid", "INPUTS.json"}:
        return False
    if any(part in {"logs", "__pycache__", ".git", ".pytest_cache"} for part in parts):
        return False
    if re.search(r"(receipt|handoff|ledger|audit|summary|status)", lower) and lower.endswith((".md", ".json", ".csv", ".log")):
        return False
    stale_suffixes = {".aux", ".log", ".out", ".bbl", ".blg", ".toc", ".fls", ".fdb_latexmk", ".synctex.gz"}
    if any(lower.endswith(s) for s in stale_suffixes):
        return False
    if lower.endswith(".pdf") and "figures" not in parts:
        return False
    return True


def clean_candidate_copy(source: Path, dest: Path) -> list[dict[str, Any]]:
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    copied: list[dict[str, Any]] = []
    for top in CANDIDATE_TOP_DIRS:
        src_top = source / top
        if not src_top.exists():
            continue
        for src in sorted(p for p in src_top.rglob("*") if p.is_file()):
            rel = src.relative_to(source)
            if not should_copy_file(rel):
                continue
            dst = dest / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            copied.append({"path": str(rel), "bytes": dst.stat().st_size, "sha256": sha256(dst)})
    return copied


def inventory_real_data() -> dict[str, Any]:
    roots = [AUTO / "runs"]
    files = []
    for root in roots:
        if root.exists():
            for path in sorted(root.rglob("*")):
                if path.suffix.lower() not in {".csv", ".json"} or not path.is_file():
                    continue
                rec: dict[str, Any] = {
                    "path": str(path),
                    "bytes": path.stat().st_size,
                    "sha256": sha256(path),
                    "kind": path.suffix.lower().lstrip("."),
                }
                if path.suffix.lower() == ".csv":
                    try:
                        with path.open(newline="", encoding="utf-8", errors="replace") as f:
                            rec["rows_approx"] = max(0, sum(1 for _ in f) - 1)
                    except OSError as exc:
                        rec["error"] = str(exc)
                files.append(rec)
    return {"created_utc": utc_now(), "roots": [str(r) for r in roots], "files": files, "counts": {"csv_json": len(files)}}


def write_inputs(seed: Path, copied_seed_files: list[dict[str, Any]], inventory: dict[str, Any]) -> None:
    data = {
        "sprint_id": SPRINT_ID,
        "sprint_root": str(SPRINT),
        "seed_package": str(seed),
        "seed_hashes": copied_seed_files,
        "real_data_inventory": inventory,
        "models": LOW_USAGE_WORKHORSES,
        "safety_locks": SAFETY_LOCKS,
        "real_data_rules": REAL_DATA_RULES,
    }
    write_text(SPRINT / "INPUTS.json", json.dumps(data, indent=2, sort_keys=True) + "\n")


def write_candidate_provenance(candidate: Path, seed: Path, copied_seed_files: list[dict[str, Any]], inventory: dict[str, Any]) -> None:
    """Package source custody beside the manuscripts without copying or mutating source data."""
    data = {
        "marker": "NEBULAMIND_REAL_DATA_SOURCE_CUSTODY_V1",
        "created_utc": utc_now(),
        "seed_package": str(seed),
        "candidate": str(candidate),
        "seed_hashes": copied_seed_files,
        "real_data_inventory": inventory,
        "no_mock_or_synthetic_data": True,
        "source_data_copied": False,
        "source_data_mutated": False,
    }
    write_text(candidate / "provenance" / "REAL_DATA_SOURCE_CUSTODY.json", json.dumps(data, indent=2, sort_keys=True) + "\n")
    refresh_candidate_custody(candidate)


def refresh_candidate_custody(candidate: Path) -> None:
    """Bind the custody receipt to the active candidate and current manuscript hashes."""
    receipt = candidate / "provenance" / "REAL_DATA_SOURCE_CUSTODY.json"
    if not receipt.exists():
        raise RuntimeError(f"Missing candidate custody receipt: {receipt}")
    data = json.loads(receipt.read_text(encoding="utf-8"))
    data["candidate"] = str(candidate)
    data["updated_utc"] = utc_now()
    data["active_candidate_hashes"] = {
        str(rel): {
            "bytes": (candidate / rel).stat().st_size,
            "sha256": sha256(candidate / rel),
        }
        for rel in TEX_RELATIVES
        if (candidate / rel).is_file()
    }
    write_text(receipt, json.dumps(data, indent=2, sort_keys=True) + "\n")


def validate_report(path: Path, min_bytes: int = REPORT_MIN_BYTES, max_bytes: int = REPORT_MAX_BYTES) -> tuple[bool, list[str]]:
    reasons = []
    if not path.exists():
        return False, ["missing report"]
    size = path.stat().st_size
    text = read_text(path, limit=max_bytes + 32)
    if size < min_bytes:
        reasons.append(f"tiny report: {size} bytes")
    if size > max_bytes:
        reasons.append(f"oversized report: {size} bytes")
    if "[TRUNCATED]" in text:
        reasons.append("report contains [TRUNCATED]")
    if not re.search(r"JOURNAL_LEVEL_PASS\s*:\s*(YES|NO)", text, re.I):
        reasons.append("missing JOURNAL_LEVEL_PASS verdict")
    return not reasons, reasons


def cap_file(path: Path, max_bytes: int = REPORT_MAX_BYTES) -> None:
    if not path.exists() or path.stat().st_size <= max_bytes:
        return
    data = path.read_bytes()[:max_bytes]
    path.write_bytes(data + b"\n[TRUNCATED]\n")


def base_prompt(phase: str, candidate: Path) -> str:
    return f"""Phase: {phase}
Sprint: {SPRINT_ID}
Candidate root: {candidate}

Safety locks:
{chr(10).join('- ' + x for x in SAFETY_LOCKS)}

Real-data rules:
{chr(10).join('- ' + x for x in REAL_DATA_RULES)}

Required review behavior:
- Inspect {candidate / 'provenance/REAL_DATA_SOURCE_CUSTODY.json'} before declaring provenance absent; it inventories real source paths, hashes, and row counts without copying the source data.
- Demand concrete section-level improvements for the flagship and supplement.
- Provide real source identifiers for literature suggestions: DOI, arXiv, ADS bibcode, URL, journal volume/page, or explicit "unverified / do not integrate".
- Preserve exact numeric invariants and association-only boundaries.
- Separate integrity blockers from journal-quality blockers.
- End with exactly one verdict line: JOURNAL_LEVEL_PASS: YES or JOURNAL_LEVEL_PASS: NO.
"""


def reviewer_specs(phase: str, candidate: Path) -> list[dict[str, Any]]:
    prompt = base_prompt(phase, candidate)
    return [
        {
            "name": "director_science",
            "report": SPRINT / "lanes/director_science" / f"{phase_slug(phase)}.md",
            "raw": SPRINT / "logs" / f"{phase_slug(phase)}_director_science.raw.log",
            "cmd": ["agy", "--model", "Gemini 3.1 Pro (Low)", "--mode", "plan", "--print", prompt + "\nRole: director/science referee."],
        },
        {
            "name": "literature",
            "report": SPRINT / "lanes/literature" / f"{phase_slug(phase)}.md",
            "raw": SPRINT / "logs" / f"{phase_slug(phase)}_literature.raw.log",
            "cmd": ["agy", "--model", "Gemini 3.1 Pro (Low)", "--mode", "plan", "--print", prompt + "\nRole: literature/source referee."],
        },
        {
            "name": "fact_check",
            "report": SPRINT / "lanes/fact_check" / f"{phase_slug(phase)}.md",
            "raw": SPRINT / "logs" / f"{phase_slug(phase)}_fact_check.raw.log",
            "cmd": ["agy", "--model", "Gemini 3.5 Flash (Low)", "--mode", "plan", "--print", prompt + "\nRole: fact-check and overclaim referee."],
        },
        {
            "name": "codex_repro_tex",
            "report": SPRINT / "lanes/codex_repro_tex" / f"{phase_slug(phase)}.md",
            "raw": SPRINT / "logs" / f"{phase_slug(phase)}_codex_repro_tex.raw.log",
            "cmd": [
                "codex",
                "exec",
                "-m",
                "gpt-5.4-mini",
                "--sandbox",
                "read-only",
                "--cd",
                str(candidate),
                "--output-last-message",
                str(SPRINT / "lanes/codex_repro_tex" / f"{phase_slug(phase)}.md"),
                prompt + "\nRole: reproducibility, provenance, and TeX referee.",
            ],
        },
    ]


def phase_slug(phase: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", phase.lower()).strip("_")


def run_command(cmd: list[str], raw_log: Path, cwd: Path, timeout: int) -> dict[str, Any]:
    raw_log.parent.mkdir(parents=True, exist_ok=True)
    start = time.time()
    if not command_exists(cmd[0]):
        write_text(raw_log, f"[MISSING COMMAND] {cmd[0]}\n")
        return {"exit_code": 127, "elapsed_s": 0.0, "missing_command": cmd[0]}
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            env={**os.environ, "NO_COLOR": "1", "CLICOLOR": "0"},
        )
        output = proc.stdout or ""
        code = proc.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        output = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        output += f"\n[TIMEOUT after {timeout}s]\n"
        code = 124
        timed_out = True
    write_text(raw_log, output)
    return {"exit_code": code, "elapsed_s": round(time.time() - start, 1), "timed_out": timed_out}


def file_manifest(root: Path) -> dict[Path, str]:
    if not root.exists():
        return {}
    return {p.relative_to(root): sha256(p) for p in root.rglob("*") if p.is_file()}


def path_is_allowed(rel: Path, allowed_files: set[Path], allowed_dirs: set[Path]) -> bool:
    return rel in allowed_files or any(rel == directory or directory in rel.parents for directory in allowed_dirs)


def revert_outside_writer_scope(
    candidate: Path,
    backup: Path,
    allowed_files: set[Path],
    allowed_dirs: set[Path],
) -> list[str]:
    before = file_manifest(backup)
    after = file_manifest(candidate)
    violations: list[str] = []
    for rel in sorted(set(before) | set(after), key=str):
        if path_is_allowed(rel, allowed_files, allowed_dirs) or before.get(rel) == after.get(rel):
            continue
        violations.append(str(rel))
        original = backup / rel
        current = candidate / rel
        if original.exists():
            current.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(original, current)
        elif current.exists():
            current.unlink()
    return violations


def writer_scope_backup(candidate: Path, cycle: int, role: str) -> Path:
    backup = SPRINT / "scope_snapshots" / f"cycle_{cycle:02d}_{role}"
    if backup.exists():
        shutil.rmtree(backup)
    shutil.copytree(candidate, backup)
    return backup


def run_reviewer(spec: dict[str, Any], candidate: Path) -> dict[str, Any]:
    result = run_command(spec["cmd"], spec["raw"], candidate, PROVIDER_TIMEOUT_SECONDS)
    if spec["cmd"][0] == "agy":
        text = read_text(spec["raw"])
        if len(text.encode("utf-8")) > REPORT_MAX_BYTES:
            text = text.encode("utf-8")[:REPORT_MAX_BYTES].decode("utf-8", errors="replace") + "\n[TRUNCATED]\n"
        write_text(spec["report"], text)
    cap_file(spec["report"])
    ok, reasons = validate_report(spec["report"])
    result.update({"name": spec["name"], "report": str(spec["report"]), "valid_report": ok, "report_reject_reasons": reasons})
    return result


def run_reviewers(phase: str, candidate: Path) -> list[dict[str, Any]]:
    import concurrent.futures

    specs = reviewer_specs(phase, candidate)
    for spec in specs:
        spec["report"].parent.mkdir(parents=True, exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        return list(ex.map(lambda s: run_reviewer(s, candidate), specs))


def analyst_prompt(phase: str, candidate: Path) -> str:
    return base_prompt(phase, candidate) + f"""
Role: candidate-only real-data analyst.
You may read existing real SDSS CSV/JSON artifacts under {AUTO / 'runs'}.
You may write only under {candidate / 'analysis_extensions'} and candidate-local derived tables/figures/scripts/provenance.
No mock/synthetic/toy data. Do not run untrusted scripts outside the Codex sandbox.
"""


def run_optional_analyst(phase: str, cycle: int, candidate: Path) -> dict[str, Any] | None:
    if phase not in ANALYST_PHASES:
        return None
    report = SPRINT / "lanes/analyst" / f"{cycle:02d}_{phase_slug(phase)}.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    raw = SPRINT / "logs" / f"{cycle:02d}_{phase_slug(phase)}_analyst.raw.log"
    prompt = analyst_prompt(phase, candidate)
    cmd = [
        "codex",
        "exec",
        "-m",
        "gpt-5.4-mini",
        "--sandbox",
        "workspace-write",
        "--cd",
        str(candidate),
        "--output-last-message",
        str(report),
        prompt,
    ]
    backup = writer_scope_backup(candidate, cycle, "analyst")
    result = run_command(cmd, raw, candidate, ANALYST_TIMEOUT_SECONDS)
    violations = revert_outside_writer_scope(candidate, backup, set(), {Path("analysis_extensions")})
    shutil.rmtree(backup)
    ok, reasons = validate_report(report, min_bytes=120)
    result.update({
        "name": "real_data_analyst",
        "report": str(report),
        "valid_report": ok,
        "report_reject_reasons": reasons,
        "writer_scope_violations_reverted": violations,
    })
    return result


def integrator_prompt(phase: str, cycle: int, candidate: Path, reports: list[Path]) -> str:
    report_text = []
    for path in reports:
        report_text.append(f"\n\n===== {path.name} =====\n{read_text(path, 40_000)}")
    allowed = "\n".join(f"- {candidate / rel}" for rel in TEX_RELATIVES)
    return base_prompt(phase, candidate) + f"""
Role: single manuscript integrator for cycle {cycle}.

You may edit only:
{allowed}
- candidate-local analysis artifacts under {candidate / 'analysis_extensions'} when needed for provenance references.

The real-data analyst and integrator must not overlap; analyst has already finished or was skipped.
Return a concise final response through the CLI output; do not create a separate response file in the candidate.
Do not add padding merely to hit word/count targets. Refuse absent measurements instead of inventing them.

Reviewer reports:
{''.join(report_text)}
"""


def run_integrator(phase: str, cycle: int, candidate: Path, reviewer_results: list[dict[str, Any]], analyst_result: dict[str, Any] | None) -> dict[str, Any]:
    reports = [Path(r["report"]) for r in reviewer_results if r.get("valid_report")]
    if analyst_result and analyst_result.get("valid_report"):
        reports.append(Path(analyst_result["report"]))
    if len(reports) < 2:
        return {
            "name": "integrator",
            "exit_code": 126,
            "valid_report": False,
            "report_reject_reasons": ["fewer than two valid reviewer reports; blind integration refused"],
            "writer_scope_violations_reverted": [],
        }
    model = "gpt-5.5" if cycle in MILESTONE_CYCLES else "gpt-5.4-mini"
    report = SPRINT / "lanes/integrator" / f"{cycle:02d}_{phase_slug(phase)}.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    raw = SPRINT / "logs" / f"{cycle:02d}_{phase_slug(phase)}_integrator.raw.log"
    cmd = [
        "codex",
        "exec",
        "-m",
        model,
        "--sandbox",
        "workspace-write",
        "--cd",
        str(candidate),
        "--output-last-message",
        str(report),
        integrator_prompt(phase, cycle, candidate, reports),
    ]
    backup = writer_scope_backup(candidate, cycle, "integrator")
    result = run_command(cmd, raw, candidate, INTEGRATOR_TIMEOUT_SECONDS)
    violations = revert_outside_writer_scope(
        candidate,
        backup,
        set(TEX_RELATIVES),
        {Path("analysis_extensions")},
    )
    shutil.rmtree(backup)
    ok, reasons = validate_report(report, min_bytes=120)
    result.update({
        "name": "integrator",
        "model": model,
        "report": str(report),
        "valid_report": ok,
        "report_reject_reasons": reasons,
        "writer_scope_violations_reverted": violations,
    })
    return result


def cleanup_tex_outputs(tex: Path) -> None:
    for suffix in [".aux", ".log", ".out", ".bbl", ".blg", ".toc"]:
        stale = tex.with_suffix(suffix)
        if stale.exists():
            stale.unlink()


def parse_compile_log(log_text: str) -> dict[str, Any]:
    lower = log_text.lower()
    return {
        "fatal_errors": re.findall(r"(?im)^(?:! .*|.*fatal error.*|.*emergency stop.*|.*halted.*)$", log_text),
        "undefined_citations": re.findall(r"(?i)(?:undefined citation|citation .* undefined|there were undefined references)", log_text),
        "undefined_references": re.findall(r"(?i)(?:reference .* undefined|undefined references)", log_text),
        "missing_includes": re.findall(r"(?i)(?:file .* not found|no such file or directory|could not find include)", log_text),
        "aastex_deprecations": re.findall(r"(?i)(?:deprecated|obsolete).{0,120}(?:aastex|aas|deluxetable)?", log_text),
        "overfull_box_count": len(re.findall(r"Overfull \\[hv]box", log_text)),
        "underfull_box_count": len(re.findall(r"Underfull \\[hv]box", log_text)),
        "has_fatal_marker": any(x in lower for x in ["fatal error", "emergency stop", "halted on"]),
    }


def strict_compile_one(tex: Path) -> dict[str, Any]:
    cleanup_tex_outputs(tex)
    pdf = tex.with_suffix(".pdf")
    if pdf.exists():
        pdf.unlink()
    log_path = tex.with_suffix(".strict_compile.log")
    if not command_exists("tectonic"):
        write_text(log_path, "tectonic not found\n")
        parsed = parse_compile_log("tectonic not found\n")
        return {"tex": str(tex), "build_ok": False, "clean_ok": False, "returncode": 127, "pdf": str(pdf), "log": str(log_path), **parsed}
    cmd = ["tectonic", "--keep-logs", "--print", "--reruns", "1", "--color", "never", tex.name]
    try:
        proc = subprocess.run(cmd, cwd=str(tex.parent), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=600)
        output = proc.stdout or ""
        rc = proc.returncode
    except subprocess.TimeoutExpired as exc:
        output = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        output += "\n[TIMEOUT]\n"
        rc = 124
    write_text(log_path, output)
    final_tex_log = tex.with_suffix(".log")
    final_log_text = read_text(final_tex_log) if final_tex_log.exists() else output
    parsed = parse_compile_log(final_log_text)
    pdf_ok = pdf.exists() and pdf.stat().st_size > 1000 and pdf.open("rb").read(4) == b"%PDF"
    build_ok = rc == 0 and pdf_ok
    clean_ok = (
        build_ok
        and not parsed["fatal_errors"]
        and not parsed["undefined_citations"]
        and not parsed["undefined_references"]
        and not parsed["missing_includes"]
        and not parsed["aastex_deprecations"]
        and parsed["overfull_box_count"] == 0
        and parsed["underfull_box_count"] == 0
    )
    return {
        "tex": str(tex),
        "pdf": str(pdf),
        "log": str(log_path),
        "final_tex_log": str(final_tex_log) if final_tex_log.exists() else None,
        "returncode": rc,
        "build_ok": build_ok,
        "clean_ok": clean_ok,
        "pdf_bytes": pdf.stat().st_size if pdf.exists() else 0,
        "pdf_sha256": sha256(pdf) if pdf.exists() else None,
        **parsed,
    }


def strict_compile(candidate: Path) -> dict[str, Any]:
    results = [strict_compile_one(candidate / rel) for rel in TEX_RELATIVES]
    return {
        "results": results,
        "build_ok": all(r["build_ok"] for r in results),
        "clean_ok": all(r["clean_ok"] for r in results),
        "fatal_errors": [x for r in results for x in r["fatal_errors"]],
        "missing_includes": [x for r in results for x in r["missing_includes"]],
        "undefined_citations": [x for r in results for x in r["undefined_citations"]],
        "undefined_references": [x for r in results for x in r["undefined_references"]],
        "aastex_deprecations": [x for r in results for x in r["aastex_deprecations"]],
        "overfull_box_count": sum(r["overfull_box_count"] for r in results),
        "underfull_box_count": sum(r["underfull_box_count"] for r in results),
    }


def scan_provenance(candidate: Path) -> dict[str, Any]:
    analysis_root = candidate / "analysis_extensions"
    analysis_files = [p for p in analysis_root.rglob("*") if p.is_file()] if analysis_root.exists() else []
    provenance_files = [p for p in analysis_files if "provenance" in p.name.lower()]
    custody_receipt = candidate / "provenance" / "REAL_DATA_SOURCE_CUSTODY.json"
    custody_errors: list[str] = []
    custody: dict[str, Any] = {}
    if not custody_receipt.exists():
        custody_errors.append("missing REAL_DATA_SOURCE_CUSTODY.json")
    else:
        try:
            custody = json.loads(custody_receipt.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            custody_errors.append(f"invalid custody receipt: {exc}")
        if custody and custody.get("marker") != "NEBULAMIND_REAL_DATA_SOURCE_CUSTODY_V1":
            custody_errors.append("invalid custody marker")
        if custody and custody.get("candidate") != str(candidate):
            custody_errors.append("custody candidate path is stale")
        active_hashes = custody.get("active_candidate_hashes", {}) if custody else {}
        for rel in TEX_RELATIVES:
            path = candidate / rel
            record = active_hashes.get(str(rel), {})
            if not path.is_file() or record.get("sha256") != (sha256(path) if path.is_file() else None):
                custody_errors.append(f"active manuscript hash mismatch: {rel}")
    return {
        "analysis_files": [str(p) for p in analysis_files],
        "provenance_files": [str(p) for p in provenance_files if p.is_file()],
        "new_result_without_provenance": bool(analysis_files and not provenance_files),
        "custody_receipt": str(custody_receipt),
        "custody_errors": custody_errors,
        "custody_valid": not custody_errors,
    }


def audit_candidate(cycle: int, phase: str, candidate: Path, compile_audit: dict[str, Any]) -> dict[str, Any]:
    flagship = read_text(candidate / FLAGSHIP_TEX)
    supplement = read_text(candidate / SUPPLEMENT_TEX)
    metrics = journal_metrics(flagship, supplement)
    provenance = scan_provenance(candidate)
    quality_blockers = classify_quality_blockers(metrics)
    if not compile_audit.get("clean_ok"):
        quality_blockers.append(
            "strict compile warning-clean gate not met "
            f"(overfull={compile_audit.get('overfull_box_count', 0)}, "
            f"underfull={compile_audit.get('underfull_box_count', 0)}, "
            f"deprecations={len(compile_audit.get('aastex_deprecations', []))})"
        )
    integrity_blockers = classify_integrity_blockers(metrics, compile_audit, provenance)
    audit = {
        "marker": "WEEKEND_JOURNAL_QUALITY_AUDIT_V1",
        "cycle": cycle,
        "phase": phase,
        "candidate": str(candidate),
        "created_utc": utc_now(),
        "metrics": metrics,
        "compile": compile_audit,
        "provenance": provenance,
        "integrity_blockers": integrity_blockers,
        "quality_blockers": quality_blockers,
        "fatal_failures": len(integrity_blockers),
        "compile_ok": [bool(result.get("build_ok")) for result in compile_audit.get("results", [])],
        "compile_results": [{"ok": bool(result.get("build_ok"))} for result in compile_audit.get("results", [])],
        "figures": metrics["figure_count"],
        "figure_count": metrics["figure_count"],
    }
    write_text(candidate / f"CYCLE_{cycle:02d}_{phase_slug(phase)}_AUDIT.json", json.dumps(audit, indent=2, sort_keys=True) + "\n")
    append_word_count_ledger(audit)
    return audit


def append_word_count_ledger(audit: dict[str, Any]) -> None:
    path = SPRINT / "WORD_COUNT_LEDGER.csv"
    new = not path.exists()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new:
            writer.writerow(["utc", "cycle", "phase", "candidate", "flagship_words", "abstract_words", "supplement_words", "citations", "equations", "tables", "figures", "integrity_blockers", "quality_blockers"])
        m = audit["metrics"]
        writer.writerow([
            utc_now(),
            audit["cycle"],
            audit["phase"],
            audit["candidate"],
            m["flagship_words_approx"],
            m["abstract_words_approx"],
            m["supplement_words_approx"],
            m["citation_key_count"],
            m["equation_count"],
            m["table_count"],
            m["figure_count"],
            "; ".join(audit["integrity_blockers"]),
            "; ".join(audit["quality_blockers"]),
        ])


def post_fix_referee(phase: str, cycle: int, candidate: Path) -> dict[str, Any] | None:
    if cycle not in MILESTONE_CYCLES:
        return None
    prompt = base_prompt(phase, candidate) + "\nRole: independent read-only post-fix referee. Do not edit files."
    report = SPRINT / "lanes/post_fix_referee" / f"{cycle:02d}_{phase_slug(phase)}.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    raw = SPRINT / "logs" / f"{cycle:02d}_{phase_slug(phase)}_post_fix_referee.raw.log"
    cmd = ["codex", "exec", "-m", "gpt-5.5", "--sandbox", "read-only", "--cd", str(candidate), "--output-last-message", str(report), prompt]
    result = run_command(cmd, raw, candidate, PROVIDER_TIMEOUT_SECONDS)
    ok, reasons = validate_report(report, min_bytes=120)
    result.update({"name": "post_fix_referee", "model": "gpt-5.5", "report": str(report), "valid_report": ok, "report_reject_reasons": reasons})
    return result


def write_phase_brief(cycle: int, phase: str, candidate: Path) -> None:
    brief = base_prompt(phase, candidate)
    write_text(SPRINT / "briefs" / f"{cycle:02d}_{phase_slug(phase)}.md", brief)


def initialize_sprint(seed: Path) -> tuple[Path, list[dict[str, Any]], dict[str, Any]]:
    for d in ["briefs", "candidates", "lanes", "logs", "promotion_packet"]:
        (SPRINT / d).mkdir(parents=True, exist_ok=True)
    inventory = inventory_real_data()
    seed_candidate = SPRINT / "candidates" / "seed_clean_package"
    copied = clean_candidate_copy(seed, seed_candidate)
    write_inputs(seed, copied, inventory)
    write_candidate_provenance(seed_candidate, seed, copied, inventory)
    write_text(SPRINT / "SPRINT_BOARD.md", "\n".join([
        f"# {SPRINT_ID}",
        "",
        "Local-only 48-hour journal-paper sprint.",
        "",
        "## Phase Slots",
        *[f"{i + 1}. {p}" for i, p in enumerate(PHASES)],
        "",
        "## Safety Locks",
        *[f"- {x}" for x in SAFETY_LOCKS],
        "",
        "## Real-Data Rules",
        *[f"- {x}" for x in REAL_DATA_RULES],
    ]) + "\n")
    return seed_candidate, copied, inventory


def run_cycle(cycle: int, phase: str, source: Path) -> tuple[Path, dict[str, Any]]:
    candidate = SPRINT / "candidates" / f"cycle_{cycle:02d}_package"
    clean_candidate_copy(source, candidate)
    refresh_candidate_custody(candidate)
    write_phase_brief(cycle, phase, candidate)
    status_update(state="running", phase=phase, cycle=cycle, current_lane="reviewers", latest_candidate=str(candidate))
    reviewer_results = run_reviewers(phase, candidate)
    status_update(current_lane="real_data_analyst" if phase in ANALYST_PHASES else "integrator")
    analyst_result = run_optional_analyst(phase, cycle, candidate)
    status_update(current_lane="integrator")
    integrator_result = run_integrator(phase, cycle, candidate, reviewer_results, analyst_result)
    refresh_candidate_custody(candidate)
    status_update(current_lane="strict_compile_audit")
    compile_audit = strict_compile(candidate)
    scope_violations = []
    if analyst_result:
        scope_violations.extend(analyst_result.get("writer_scope_violations_reverted", []))
    scope_violations.extend(integrator_result.get("writer_scope_violations_reverted", []))
    compile_audit["writer_scope_violations"] = sorted(set(scope_violations))
    audit = audit_candidate(cycle, phase, candidate, compile_audit)
    invalid_lanes = [r.get("name", "unknown") for r in reviewer_results if not r.get("valid_report")]
    if analyst_result and not analyst_result.get("valid_report"):
        invalid_lanes.append("real_data_analyst")
    if not integrator_result.get("valid_report"):
        invalid_lanes.append("integrator")
    if invalid_lanes:
        audit["quality_blockers"].append("invalid or missing lane outputs: " + ", ".join(sorted(set(invalid_lanes))))
        write_text(candidate / f"CYCLE_{cycle:02d}_{phase_slug(phase)}_AUDIT.json", json.dumps(audit, indent=2, sort_keys=True) + "\n")
    referee_result = post_fix_referee(phase, cycle, candidate)
    summary = {
        "cycle": cycle,
        "phase": phase,
        "candidate": str(candidate),
        "reviewers": reviewer_results,
        "analyst": analyst_result,
        "integrator": integrator_result,
        "compile_audit": compile_audit,
        "audit": audit,
        "post_fix_referee": referee_result,
        "finished_utc": utc_now(),
    }
    write_text(candidate / f"CYCLE_{cycle:02d}_{phase_slug(phase)}_SUMMARY.json", json.dumps(summary, indent=2, sort_keys=True) + "\n")
    ledger(f"cycle {cycle:02d} phase={phase} integrity={len(audit['integrity_blockers'])} quality={len(audit['quality_blockers'])}")
    return candidate, summary


def heartbeat_sleep_until(deadline: float, status_base: dict[str, Any]) -> None:
    while time.time() < deadline and not STOP_REQUESTED:
        remaining = max(0, int(deadline - time.time()))
        status_update(state="waiting_next_phase", heartbeat_utc=utc_now(), seconds_to_next_slot=remaining, **status_base)
        time.sleep(min(HEARTBEAT_SECONDS, remaining, 5 if remaining < HEARTBEAT_SECONDS else HEARTBEAT_SECONDS))


def write_final_handoff(cycles: list[dict[str, Any]], latest: Path | None, last_clean: Path | None, started_utc: str, target_end_utc: str) -> None:
    packet = {
        "sprint_id": SPRINT_ID,
        "started_utc": started_utc,
        "target_end_utc": target_end_utc,
        "finished_utc": utc_now(),
        "cycles_completed": len(cycles),
        "latest_candidate": str(latest) if latest else None,
        "last_clean_candidate": str(last_clean) if last_clean else None,
        "no_apply": True,
        "cycles": cycles,
    }
    write_text(SPRINT / "FINAL_HANDOFF.json", json.dumps(packet, indent=2, sort_keys=True) + "\n")
    lines = [
        f"# Final Handoff: {SPRINT_ID}",
        "",
        f"- Started UTC: {started_utc}",
        f"- Target end UTC: {target_end_utc}",
        f"- Finished UTC: {utc_now()}",
        f"- Cycles completed: {len(cycles)}",
        f"- Latest candidate: `{latest}`" if latest else "- Latest candidate: none",
        f"- Last clean candidate: `{last_clean}`" if last_clean else "- Last clean candidate: none",
        "",
        "## No-Apply Promotion Packet",
        "",
        "No public replacement, git write, deployment, DB/API/wiki/trust mutation, or external submission was performed.",
    ]
    if latest:
        lines.extend(["", "## Candidate Files"])
        for rel in TEX_RELATIVES:
            path = latest / rel
            lines.append(f"- `{path}` exists={path.exists()} sha256={sha256(path) if path.exists() else None}")
    write_text(SPRINT / "FINAL_HANDOFF.md", "\n".join(lines) + "\n")
    write_text(SPRINT / "promotion_packet" / "NO_APPLY_PROMOTION_PACKET.md", "\n".join(lines) + "\n")


def signal_handler(signum: int, _frame: Any) -> None:
    global STOP_REQUESTED
    STOP_REQUESTED = True
    status_update(state="stopping", stop_signal=signum)
    ledger(f"stop requested signal={signum}")


def preflight(seed: Path, max_cycles: int, duration_seconds: int, slot_seconds: int) -> dict[str, Any]:
    result = {
        "sprint_id": SPRINT_ID,
        "sprint_root": str(SPRINT),
        "seed_package": str(seed),
        "seed_exists": seed.exists(),
        "duration_seconds": duration_seconds,
        "max_cycles": max_cycles,
        "slot_seconds": slot_seconds,
        "phase_count": len(PHASES),
        "commands": {name: command_exists(name) for name in ["agy", "codex", "tectonic"]},
        "would_call_providers": False,
        "models": LOW_USAGE_WORKHORSES,
    }
    write_text(SPRINT / "PREFLIGHT.json", json.dumps(result, indent=2, sort_keys=True) + "\n")
    status_update(state="preflight_complete", pid=os.getpid(), phase=None, cycle=0, cycles_completed=0, progress_percent=0, current_lane="preflight")
    return result


def require_runtime_prerequisites(seed: Path) -> None:
    missing = [name for name in ["agy", "codex", "tectonic"] if not command_exists(name)]
    if not seed.exists():
        raise RuntimeError(f"Missing seed package: {seed}")
    if missing:
        raise RuntimeError("Missing required commands: " + ", ".join(missing))


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preflight", action="store_true", help="initialize/validate source/tools/models without provider calls")
    parser.add_argument("--duration-seconds", type=int, default=DEFAULT_DURATION_SECONDS)
    parser.add_argument("--max-cycles", type=int, default=DEFAULT_MAX_CYCLES)
    parser.add_argument("--slot-seconds", type=int, default=DEFAULT_SLOT_SECONDS)
    parser.add_argument("--seed-package", type=Path, default=SEED_PACKAGE, help=argparse.SUPPRESS)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    SPRINT.mkdir(parents=True, exist_ok=True)
    if args.preflight:
        preflight(args.seed_package, args.max_cycles, args.duration_seconds, args.slot_seconds)
        return 0

    refuse_if_running()
    require_runtime_prerequisites(args.seed_package)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    started_utc = utc_now()
    started_ts = time.time()
    target_end = time.time() + args.duration_seconds
    target_end_utc = dt.datetime.fromtimestamp(target_end, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    write_text(SPRINT / "RUNNING.pid", f"{os.getpid()}\n")
    latest, copied, inventory = initialize_sprint(args.seed_package)
    last_clean = latest
    write_inputs(args.seed_package, copied, inventory)
    cycles: list[dict[str, Any]] = []
    status_update(
        state="running",
        pid=os.getpid(),
        phase=PHASES[0],
        cycle=0,
        started_utc=started_utc,
        target_end_utc=target_end_utc,
        current_lane="initialized",
        latest_candidate=str(latest),
        last_clean_candidate=str(last_clean),
        latest_audit=None,
        cycles_completed=0,
        progress_percent=0,
    )
    ledger("sprint started")

    final_state = "completed"
    try:
        for idx, phase in enumerate(PHASES[: args.max_cycles], start=1):
            if STOP_REQUESTED or time.time() >= target_end:
                break
            slot_deadline = parse_utc(started_utc).timestamp() + idx * args.slot_seconds
            source = last_clean if last_clean else latest
            candidate, summary = run_cycle(idx, phase, source)
            cycles.append(summary)
            latest = candidate
            audit = summary["audit"]
            if audit["integrity_blockers"]:
                ledger(f"cycle {idx:02d}: integrity fatal; next cycle will restart from last clean candidate")
            else:
                last_clean = candidate
            progress = min(100, round(100 * (min(time.time(), target_end) - started_ts) / max(1, args.duration_seconds), 2))
            status_update(
                state="between_cycles",
                phase=phase,
                cycle=idx,
                current_lane="waiting_or_next",
                latest_candidate=str(latest),
                last_clean_candidate=str(last_clean) if last_clean else None,
                latest_audit=str(candidate / f"CYCLE_{idx:02d}_{phase_slug(phase)}_AUDIT.json"),
                cycles_completed=len(cycles),
                progress_percent=progress,
            )
            if time.time() < slot_deadline:
                heartbeat_sleep_until(slot_deadline, {"phase": phase, "cycle": idx, "cycles_completed": len(cycles)})
    except Exception as exc:
        final_state = "failed"
        status_update(state="failed", error=f"{type(exc).__name__}: {exc}")
        ledger(f"sprint failed: {type(exc).__name__}: {exc}")
        raise
    finally:
        state = "stopped" if STOP_REQUESTED else final_state
        write_final_handoff(cycles, latest, last_clean, started_utc, target_end_utc)
        status_update(
            state=state,
            phase=cycles[-1]["phase"] if cycles else None,
            cycle=len(cycles),
            current_lane="final_handoff",
            latest_candidate=str(latest) if latest else None,
            last_clean_candidate=str(last_clean) if last_clean else None,
            cycles_completed=len(cycles),
            progress_percent=100 if state == "completed" else None,
        )
        pid_path = SPRINT / "RUNNING.pid"
        if pid_path.exists():
            pid_path.unlink()
        ledger(f"sprint {state}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
