#!/usr/bin/env python3
"""Couple-hour Galaxy Evolution LaTeX + publishability repair sprint.

Local/artifact-only target: make the 9 Galaxy Evolution manuscript candidate
PDFs compile cleanly under a stricter LaTeX/log audit and improve publication
readiness. Reviewer lanes write reports; only the integrator edits copied TeX.

Safety locks:
- No public PDF replacement or public/live root edits.
- No DB/API/wiki/page_versions/trust writes.
- No deploy/restart.
- No git commit/push/merge/rebase.
- No cron changes.
- No billing/cloud/OAuth/account/credential actions.
- No external manuscript submission.
"""
from __future__ import annotations

import concurrent.futures as cf
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTO = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
OVERNIGHT_ROOT = AUTO / "overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z"
PUBLISHABLE_ROOT = AUTO / "publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers"
PUBLIC_PROMOTION_ROOT = AUTO / "public-promotions/PUBLIC_STATIC_PDF_PROMOTION_20260709T233457Z"
INTEGRATED_ROOT = AUTO / "integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z"

RUN_ID = os.environ.get("NEBULAMIND_LATEX_REPAIR_RUN_ID") or "LATEX_PUBLISHABILITY_REPAIR_" + dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUN_ROOT = AUTO / "latex-publishability-repair" / RUN_ID
SOURCE_OVERRIDE = os.environ.get("NEBULAMIND_LATEX_REPAIR_SOURCE")
WINDOW_SECONDS = int(os.environ.get("NEBULAMIND_LATEX_REPAIR_SECONDS", str(2 * 60 * 60)))
MAX_CYCLES = int(os.environ.get("NEBULAMIND_LATEX_REPAIR_MAX_CYCLES", "6"))
MIN_REMAINING_SECONDS = int(os.environ.get("NEBULAMIND_LATEX_REPAIR_MIN_REMAINING", str(18 * 60)))
LANE_TIMEOUT = int(os.environ.get("NEBULAMIND_LATEX_REPAIR_LANE_TIMEOUT", str(32 * 60)))
INTEGRATOR_TIMEOUT = int(os.environ.get("NEBULAMIND_LATEX_REPAIR_INTEGRATOR_TIMEOUT", str(38 * 60)))
SLEEP_BETWEEN_CYCLES = int(os.environ.get("NEBULAMIND_LATEX_REPAIR_SLEEP_BETWEEN_CYCLES", str(2 * 60)))
TEX_LINT_TOOL = REPO / "tools/ge_tex_publishability_lint.py"

PAPER_DIRS = [
    "01_m1_rp1_sdss_agn_sfr",
    "02_m1_rp2_environment_quenching",
    "03_m1_rp3_maintenance_heating",
    "04_m2_p1_outflow_escape_recycling",
    "05_m2_p2_radio_jet_environment",
    "06_m2_p3_feedback_transition_mass",
    "07_m3_p1_multiphase_census",
    "08_m3_p2_gas_depletion_efficiency",
    "09_m3_p3_simulation_validation",
]

SAFETY_LOCKS = [
    "write only under this repair run root and copied candidate packages",
    "review lanes write reports only; only the candidate-copy integrator edits candidate-copy TeX",
    "no public-linked PDF replacement or public/live static root edits",
    "no DB, SQL, /api/pages, page_versions, wiki publish, trust recompute, or data mutation",
    "no deploy/restart",
    "no git commit/push/merge/rebase/history rewrite",
    "no cron creation/update/removal",
    "no billing/cloud/OAuth/API-key/account changes and no credential/token/cookie reads",
    "no external manuscript submission",
]

REAL_DATA_RULES = [
    "Never use mock, synthetic, fake, placeholder, or toy data as manuscript evidence.",
    "Never invent numbers, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, figure results, or table values.",
    "Every quantitative claim must trace to real local artifacts or checkable public sources already in the package.",
    "Absent data must be written as absent/future real-data requirements, not inferred as results.",
    "RP-1 stays association-only; papers 2-9 stay SDSS optical denominator/proxy notes unless new real data are inventoried.",
]

# Focused lanes. They run in parallel and write reports only.
LANES = [
    {
        "name": "hwao_publishability_director",
        "provider": "agy",
        "model": "Gemini 3.1 Pro (Low)",
        "role": "Hwao/Fable director: triage why the papers still feel not publishable; prioritize exact blockers for the writer.",
        "frequency": 1,
    },
    {
        "name": "gemini_latex_layout_critic",
        "provider": "agy",
        "model": "Gemini 3.5 Flash (Low)",
        "role": "Goru/Gemini TeX critic: focus on LaTeX errors, warnings, overfull/underfull boxes, broken citations/references, figure/table layout, and exact safe TeX fixes.",
        "frequency": 1,
    },
    {
        "name": "gemini_publishability_critic",
        "provider": "agy",
        "model": "Gemini 3.1 Pro (High)",
        "role": "Gemini Deep manuscript critic: strict AAS-style publishability review and exact rewrite instructions, preserving real-data boundaries.",
        "frequency": 1,
    },
    {
        "name": "gptoss_skeptic",
        "provider": "agy",
        "model": "GPT-OSS 120B (Medium)",
        "role": "Low-usage skeptic: adversarial scan for remaining non-publishable structure, weak abstracts, unsupported claims, and reader-confusing language.",
        "frequency": 1,
    },
    {
        "name": "codex_kun_tex_repro",
        "provider": "codex",
        "model": "gpt-5.4-mini",
        "role": "Kun/Codex read-only TeX/reproducibility audit: inspect candidate TeX and strict compile audit; report exact blockers; no edits.",
        "frequency": 1,
    },
]

FATAL_PATTERNS = [
    "LaTeX Error",
    "! Undefined control sequence",
    "! Emergency stop",
    "Emergency stop",
    "Fatal error",
    "halted on potentially-recoverable error",
    "I couldn't open",
    "No pages of output",
]

WARNING_PATTERNS = [
    "Overfull \\hbox",
    "Underfull \\hbox",
    "undefined references",
    "Citation `",
    "undefined citation",
    "Package natbib Warning",
    "Missing character",
    "Rerun to get cross-references right",
]


def utc() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def kst(ts: Optional[dt.datetime] = None) -> str:
    ts = ts or dt.datetime.now(dt.timezone.utc)
    return ts.astimezone(dt.timezone(dt.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S KST")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def append(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(text)


def read_text(path: Path, limit: Optional[int] = None) -> str:
    if not path.exists():
        return f"[MISSING: {path}]"
    text = path.read_text(errors="replace")
    if limit is not None and len(text) > limit:
        return text[:limit] + f"\n[TRUNCATED at {limit} chars: {path}]\n"
    return text


def compact(text: str, limit: int = 900) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[:limit] + " ..."


def sha256(path: Path) -> Optional[str]:
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def ledger(line: str) -> None:
    append(RUN_ROOT / "REPAIR_LEDGER.md", f"- {utc()} / {kst()} — {line}\n")


def status(**kwargs: Any) -> None:
    path = RUN_ROOT / "REPAIR_STATUS.json"
    data: Dict[str, Any] = {}
    if path.exists():
        try:
            data = json.loads(path.read_text())
        except Exception:
            data = {}
    data.update(kwargs)
    data["updated_utc"] = utc()
    write_text(path, json.dumps(data, indent=2, sort_keys=True))


def paper_tex_paths(candidate: Path) -> List[Path]:
    out: List[Path] = []
    for d in PAPER_DIRS:
        aas = candidate / d / "aastex"
        matches = sorted(aas.glob("*_integrated.tex"))
        if matches:
            out.append(matches[0])
    return out


def title_abs_conclusion(tex: Path) -> Dict[str, str]:
    text = read_text(tex, 160000)
    title = "[missing title]"
    abstract = "[missing abstract]"
    conclusion = "[missing conclusion]"
    m = re.search(r"\\title(?:\[[^\]]*\])?\{(.+?)\}", text, re.S)
    if m:
        title = compact(m.group(1), 260)
    m = re.search(r"\\begin\{abstract\}(.+?)\\end\{abstract\}", text, re.S)
    if m:
        abstract = compact(m.group(1), 900)
    m = re.search(r"\\section\{Conclusion\}.*?\n(.+?)(?:\\acknowledgments|\\begin\{thebibliography\})", text, re.S)
    if m:
        conclusion = compact(m.group(1), 900)
    return {"title": title, "abstract": abstract, "conclusion": conclusion}


def latest_completed_overnight_candidate() -> Optional[Tuple[int, Path, Path]]:
    candidates: List[Tuple[int, Path, Path]] = []
    if not OVERNIGHT_ROOT.exists():
        return None
    for receipt in (OVERNIGHT_ROOT / "candidates").glob("cycle_*_nine_papers/CYCLE_*_AFTER_RECEIPT.json"):
        try:
            data = json.loads(receipt.read_text())
            cycle = int(receipt.parent.name.split("_")[1])
            if data.get("all_ok"):
                candidates.append((cycle, receipt.parent, receipt))
        except Exception:
            continue
    return max(candidates, key=lambda x: x[0]) if candidates else None


def choose_source() -> Tuple[Path, str]:
    if SOURCE_OVERRIDE:
        source = Path(SOURCE_OVERRIDE).expanduser()
        if not source.exists():
            raise FileNotFoundError(f"NEBULAMIND_LATEX_REPAIR_SOURCE does not exist: {source}")
        return source, "explicit NEBULAMIND_LATEX_REPAIR_SOURCE override"
    latest = latest_completed_overnight_candidate()
    if latest is not None:
        cycle, root, receipt = latest
        return root, f"latest completed overnight candidate cycle {cycle}: {receipt}"
    return PUBLISHABLE_ROOT, "fallback publishability-pass candidate"


def run_tex_lint(candidate: Path, cycle: int, label: str) -> Dict[str, Any]:
    json_path = candidate / f"CYCLE_{cycle:02d}_{label.upper()}_TEX_LINT.json"
    md_path = candidate / f"CYCLE_{cycle:02d}_{label.upper()}_TEX_LINT.md"
    if not TEX_LINT_TOOL.exists():
        result = {
            "candidate": str(candidate),
            "cycle": cycle,
            "label": label,
            "created_utc": utc(),
            "tool": str(TEX_LINT_TOOL),
            "returncode": 125,
            "error_count": 1,
            "warning_count": 0,
            "finding_count": 1,
            "findings": [{"severity": "error", "code": "missing_tex_lint_tool", "message": f"Missing TeX linter: {TEX_LINT_TOOL}"}],
        }
    else:
        proc = subprocess.run([sys.executable, str(TEX_LINT_TOOL), "--json", str(candidate)], cwd=str(REPO), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=5 * 60)
        try:
            result = json.loads(proc.stdout or "{}")
        except Exception:
            result = {"findings": [], "raw_output": proc.stdout or ""}
        result.update({"candidate": str(candidate), "cycle": cycle, "label": label, "created_utc": utc(), "tool": str(TEX_LINT_TOOL), "returncode": proc.returncode})
    write_text(json_path, json.dumps(result, indent=2, sort_keys=True))
    findings = result.get("findings", []) or []
    lines = [
        f"# TeX publishability lint {label} cycle {cycle}",
        "",
        f"returncode: {result.get('returncode')}",
        f"tex_file_count: {result.get('tex_file_count')}",
        f"finding_count: {result.get('finding_count', len(findings))}",
        f"error_count: {result.get('error_count')}",
        f"warning_count: {result.get('warning_count')}",
        "",
    ]
    for item in findings[:80]:
        lines.append(f"- {item.get('severity')} {item.get('code')} `{item.get('path')}:{item.get('line') or '?'}` — {item.get('message')}")
    write_text(md_path, "\n".join(lines) + "\n")
    return result


def copy_candidate(source: Path, cycle: int) -> Path:
    dest = RUN_ROOT / "candidates" / f"cycle_{cycle:02d}_nine_papers"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True, exist_ok=True)
    for d in PAPER_DIRS:
        shutil.copytree(source / d, dest / d)
    write_text(dest / "SOURCE_COPY.json", json.dumps({"source": str(source), "cycle": cycle, "copied_utc": utc(), "paper_dirs": PAPER_DIRS}, indent=2))
    return dest


def count_occurrences(text: str, needle: str) -> int:
    return text.lower().count(needle.lower())


def interesting_lines(text: str, patterns: List[str], max_lines: int = 30) -> List[str]:
    out: List[str] = []
    for i, line in enumerate(text.splitlines(), start=1):
        low = line.lower()
        if any(p.lower() in low for p in patterns):
            out.append(f"L{i}: {line[:260]}")
            if len(out) >= max_lines:
                break
    return out


def compile_one(tex: Path, label: str) -> Dict[str, Any]:
    pdf = tex.with_suffix(".pdf")
    log = tex.with_suffix(f".{label}.strict.log")
    # Remove stale output/logs that could mask a failed compile.
    for suffix in [".aux", ".bbl", ".bcf", ".blg", ".idx", ".log", ".out", ".run.xml", ".toc"]:
        stale = tex.with_suffix(suffix)
        if stale.exists():
            try:
                stale.unlink()
            except Exception:
                pass
    if pdf.exists():
        try:
            pdf.unlink()
        except Exception:
            pass
    cmd = ["tectonic", "--keep-logs", "--print", "--reruns", "1", "--color", "never", tex.name]
    try:
        proc = subprocess.run(cmd, cwd=str(tex.parent), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=10 * 60)
        out = proc.stdout or ""
        rc = proc.returncode
    except Exception as exc:
        out = f"[EXCEPTION] {type(exc).__name__}: {exc}\n"
        rc = 125
    write_text(log, out)
    transcript = tex.with_suffix(".log")
    analysis_text = transcript.read_text(errors="replace") if transcript.exists() else out
    header = ""
    if pdf.exists():
        try:
            header = pdf.open("rb").read(4).decode(errors="replace")
        except Exception:
            header = ""
    fatal_counts = {p: count_occurrences(analysis_text, p) for p in FATAL_PATTERNS}
    warning_counts = {p: count_occurrences(analysis_text, p) for p in WARNING_PATTERNS}
    fatal_hits = {k: v for k, v in fatal_counts.items() if v}
    warning_hits = {k: v for k, v in warning_counts.items() if v}
    layout_warning_count = warning_counts.get("Overfull \\hbox", 0) + warning_counts.get("Underfull \\hbox", 0)
    undefined_count = sum(warning_counts.get(p, 0) for p in ["undefined references", "Citation `", "undefined citation", "Package natbib Warning"])
    clean_ok = rc == 0 and pdf.exists() and header == "%PDF" and not fatal_hits and undefined_count == 0 and layout_warning_count == 0
    build_ok = rc == 0 and pdf.exists() and header == "%PDF" and not fatal_hits and undefined_count == 0
    return {
        "tex": str(tex),
        "pdf": str(pdf),
        "label": label,
        "command": cmd,
        "returncode": rc,
        "pdf_exists": pdf.exists(),
        "pdf_bytes": pdf.stat().st_size if pdf.exists() else 0,
        "pdf_sha256": sha256(pdf) if pdf.exists() else None,
        "header": header,
        "fatal_hits": fatal_hits,
        "warning_hits": warning_hits,
        "layout_warning_count": layout_warning_count,
        "undefined_count": undefined_count,
        "clean_ok": clean_ok,
        "build_ok": build_ok,
        "log": str(log),
        "transcript_log": str(transcript) if transcript.exists() else None,
        "interesting_log_lines": interesting_lines(analysis_text, FATAL_PATTERNS + WARNING_PATTERNS, 25),
    }


def compile_all(candidate: Path, cycle: int, label: str) -> List[Dict[str, Any]]:
    results = [compile_one(tex, label) for tex in paper_tex_paths(candidate)]
    all_build_ok = all(r["build_ok"] for r in results)
    all_clean_ok = all(r["clean_ok"] for r in results)
    total_layout = sum(int(r["layout_warning_count"]) for r in results)
    total_undefined = sum(int(r["undefined_count"]) for r in results)
    receipt = {
        "created_utc": utc(),
        "cycle": cycle,
        "label": label,
        "candidate": str(candidate),
        "all_build_ok": all_build_ok,
        "all_clean_ok": all_clean_ok,
        "total_layout_warning_count": total_layout,
        "total_undefined_count": total_undefined,
        "results": results,
    }
    write_text(candidate / f"CYCLE_{cycle:02d}_{label.upper()}_STRICT_LATEX_AUDIT.json", json.dumps(receipt, indent=2, sort_keys=True))
    lines = [f"# Strict LaTeX audit {label} cycle {cycle}", "", f"all_build_ok: {all_build_ok}", f"all_clean_ok: {all_clean_ok}", f"layout_warning_count: {total_layout}", f"undefined_count: {total_undefined}", ""]
    for r in results:
        lines.append(f"## {Path(r['tex']).name}")
        lines.append(f"- build_ok={r['build_ok']} clean_ok={r['clean_ok']} rc={r['returncode']} bytes={r['pdf_bytes']}")
        lines.append(f"- fatal_hits={r['fatal_hits']}")
        lines.append(f"- warning_hits={r['warning_hits']}")
        if r["interesting_log_lines"]:
            lines.append("- log lines:")
            for l in r["interesting_log_lines"][:12]:
                lines.append(f"  - {l}")
        lines.append("")
    write_text(candidate / f"CYCLE_{cycle:02d}_{label.upper()}_STRICT_LATEX_AUDIT.md", "\n".join(lines))
    return results


def candidate_digest(candidate: Path, before_results: List[Dict[str, Any]], cycle: int) -> str:
    parts = [f"Candidate: {candidate}", f"Cycle: {cycle}", "", "## Strict LaTeX audit", ""]
    for r in before_results:
        parts.append(f"- {Path(r['tex']).name}: build_ok={r['build_ok']} clean_ok={r['clean_ok']} rc={r['returncode']} layout_warnings={r['layout_warning_count']} undefined={r['undefined_count']} fatal={r['fatal_hits']}")
        for l in r.get("interesting_log_lines", [])[:6]:
            parts.append(f"  - {l}")
    parts.append("\n## Manuscript summaries")
    for tex in paper_tex_paths(candidate):
        ta = title_abs_conclusion(tex)
        parts.append(f"\n### {tex.relative_to(candidate)}\nTitle: {ta['title']}\nAbstract: {ta['abstract']}\nConclusion: {ta['conclusion']}")
    parts.append("\n## Existing context")
    parts.append("The previous overnight swarm improved candidate-copy manuscripts but user reports PDFs are still not publishable and some show LaTeX errors. Treat layout warnings, broken refs/citations, missing figures, and sloppy AAS presentation as real blockers to chase down in the copied TeX package.")
    return "\n".join(parts)


def lane_prompt(lane: Dict[str, Any], candidate: Path, before_results: List[Dict[str, Any]], cycle: int) -> str:
    marker = f"LATEX_REPAIR_{lane['name'].upper()}_CYCLE_{cycle:02d}"
    return f"""{lane['role']}

Output marker: {marker}

Work mode: artifact-only, read-only lane. Do not edit files. Do not publish. Do not call or request credentials.

The user reports that the current public PDFs are still not publishable and that some show LaTeX errors. Your job is to find exact high-value blockers and feed the candidate-copy writer. Focus first on strict LaTeX/log issues, then AAS publishability.

Required output sections:
1. {marker} status: PASS/ISSUES_FOUND/BLOCKED.
2. Files/paths actually inspected or, if not inspectable, paths used from context.
3. Strict LaTeX blockers: fatal errors, undefined refs/citations, missing figures, overfull/underfull box locations, package/layout problems.
4. Publishability blockers: overclaiming, weak abstract/conclusion, insufficient caveats, source-role/citation problems, poor figure/table captions, reader flow.
5. Exact feed for the writer: concrete TeX-level edits, by file/section/line when possible. Preserve all real measured values and real-data limits.
6. Safety ledger: no edits/public/db/deploy/git/cron/billing/OAuth/submission.

Run root: {RUN_ROOT}
Cycle: {cycle}
Candidate package: {candidate}
Integrated 9-paper root: {INTEGRATED_ROOT}
Public promotion receipt root: {PUBLIC_PROMOTION_ROOT}

Safety locks:
""" + "\n".join(f"- {x}" for x in SAFETY_LOCKS) + "\n\nReal-data rules:\n" + "\n".join(f"- {x}" for x in REAL_DATA_RULES) + "\n\nContext follows:\n" + candidate_digest(candidate, before_results, cycle)


def run_lane(lane: Dict[str, Any], candidate: Path, before_results: List[Dict[str, Any]], cycle: int) -> Tuple[str, int, Path]:
    out_dir = RUN_ROOT / "lanes" / lane["name"]
    out_dir.mkdir(parents=True, exist_ok=True)
    report = out_dir / f"{lane['name'].upper()}_CYCLE_{cycle:02d}.md"
    brief = RUN_ROOT / "briefs" / f"cycle_{cycle:02d}_{lane['name']}.md"
    prompt = lane_prompt(lane, candidate, before_results, cycle)
    write_text(brief, prompt)
    started = utc()
    if lane["provider"] == "agy":
        cmd = ["agy", "--model", lane["model"], "--mode", "plan", "--print-timeout", f"{max(5, LANE_TIMEOUT // 60)}m0s", "--print", prompt]
        cwd = str(REPO)
    elif lane["provider"] == "codex":
        cmd = ["codex", "exec", "-m", lane["model"], "--sandbox", "read-only", "--cd", str(REPO), prompt]
        cwd = str(REPO)
    else:
        raise ValueError(lane["provider"])
    try:
        proc = subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=LANE_TIMEOUT)
        output = proc.stdout or ""
        rc = proc.returncode
    except Exception as exc:
        output = f"[EXCEPTION] {type(exc).__name__}: {exc}\n"
        rc = 125
    write_text(report, f"# {lane['name']} cycle {cycle}\nStarted UTC: {started}\nFinished UTC: {utc()}\nModel: {lane['model']}\nProvider: {lane['provider']}\nBrief: {brief}\nExit: {rc}\n\n```text\n{output}\n```\n")
    return lane["name"], rc, report


def write_feed(candidate: Path, before_results: List[Dict[str, Any]], lane_reports: List[Tuple[str, int, Path]], cycle: int) -> Path:
    feed = RUN_ROOT / "feeds" / f"LATEX_REPAIR_FEED_CYCLE_{cycle:02d}.md"
    parts = [f"# LaTeX/publishability repair feed cycle {cycle}", "", f"created_utc: {utc()}", f"candidate: `{candidate}`", "", "## Purpose", "Feed strict LaTeX and publication-readiness findings into the candidate-copy writer. This is not a public publish/replace instruction.", "", "## Safety locks"]
    parts.extend(f"- {x}" for x in SAFETY_LOCKS)
    parts.append("\n## Strict compile status before writing")
    for r in before_results:
        parts.append(f"- `{Path(r['tex']).name}` build_ok={r['build_ok']} clean_ok={r['clean_ok']} layout_warnings={r['layout_warning_count']} undefined={r['undefined_count']} fatal={r['fatal_hits']} bytes={r['pdf_bytes']}")
        for l in r.get("interesting_log_lines", [])[:8]:
            parts.append(f"  - {l}")
    parts.append("\n## Lane outputs to integrate")
    for name, rc, path in lane_reports:
        parts.append(f"\n===== {name} exit={rc} =====\n")
        parts.append(read_text(path, 24000))
    write_text(feed, "\n".join(parts))
    return feed


def integrator_prompt(candidate: Path, feed: Path, before_results: List[Dict[str, Any]], cycle: int) -> str:
    tex_paths = paper_tex_paths(candidate)
    marker = f"LATEX_REPAIR_WRITER_INTEGRATOR_CYCLE_{cycle:02d}"
    return f"""You are the candidate-copy LaTeX and publishability repair integrator for NebulaMind Galaxy Evolution.

Output marker: {marker}

Working root: {candidate}

You may edit ONLY these 9 candidate-copy TeX files:
""" + "\n".join(f"- {p}" for p in tex_paths) + f"""

Hard stops:
- Do not edit files outside the listed TeX files.
- Do not alter measured numeric results unless the feed proves a direct typo in the text; preserve all real-data limits.
- Do not invent citations, numbers, URLs, DOIs, arXiv IDs, ADS bibcodes, data products, figures, or tables.
- Do not change public files, DB, wiki, git, credentials, or services.

User-reported problem: the PDFs are still not publishable and some show LaTeX errors. The strict audit treats these as blockers until fixed:
- compile/fatal errors;
- undefined references or citations;
- missing figures/includes;
- overfull/underfull box warnings when they reflect bad AAS layout;
- poor AAS manuscript structure or weak publishability language.

Repair priorities:
1. Fix true LaTeX/log blockers first.
2. Reduce or eliminate overfull/underfull box warnings without masking scientific problems. Use careful wording/line-break/table/citation cleanup; use global blunt formatting only if justified and safe.
3. Improve abstracts/conclusions/captions/limitations into professional AAS-style manuscript language.
4. Preserve all real-data caveats and association-only wording.
5. Leave a short `CYCLE_{cycle:02d}_INTEGRATOR_CHANGELOG.md` in the working root summarizing edits.

Strict compile audit before writer:
""" + "\n".join(f"- {Path(r['tex']).name}: build_ok={r['build_ok']} clean_ok={r['clean_ok']} layout_warnings={r['layout_warning_count']} undefined={r['undefined_count']} fatal={r['fatal_hits']}" for r in before_results) + f"""

Feed packet to integrate:
{read_text(feed, 46000)}
"""


def run_integrator(candidate: Path, feed: Path, before_results: List[Dict[str, Any]], cycle: int) -> Tuple[int, Path]:
    out_dir = RUN_ROOT / "lanes" / "writer_integrator"
    out_dir.mkdir(parents=True, exist_ok=True)
    report = out_dir / f"WRITER_INTEGRATOR_CYCLE_{cycle:02d}.log"
    prompt = integrator_prompt(candidate, feed, before_results, cycle)
    brief = RUN_ROOT / "briefs" / f"cycle_{cycle:02d}_writer_integrator.md"
    write_text(brief, prompt)
    cmd = ["codex", "exec", "-m", "gpt-5.4-mini", "--sandbox", "workspace-write", "--cd", str(candidate), "--skip-git-repo-check", prompt]
    try:
        proc = subprocess.run(cmd, cwd=str(candidate), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=INTEGRATOR_TIMEOUT)
        output = proc.stdout or ""
        rc = proc.returncode
    except Exception as exc:
        output = f"[EXCEPTION] {type(exc).__name__}: {exc}\n"
        rc = 125
    write_text(report, output)
    return rc, report


def write_board(start: dt.datetime, source: Path, source_note: str) -> None:
    lines = [
        "# Couple-hour LaTeX + publishability repair board",
        "",
        f"Run ID: `{RUN_ID}`",
        f"Run root: `{RUN_ROOT}`",
        f"Started UTC: {start.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"Target end UTC: {(start + dt.timedelta(seconds=WINDOW_SECONDS)).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"Source candidate: `{source}`",
        f"Source note: {source_note}",
        "",
        "## Mission",
        "Run autonomous pilots for about two hours to fix real LaTeX/log problems and improve AAS-style publishability in local candidate copies only.",
        "",
        "## Lanes",
    ]
    for lane in LANES:
        lines.append(f"- {lane['name']}: {lane['provider']} / {lane['model']} — {lane['role']}")
    lines.extend(["", "## Safety locks"])
    lines.extend(f"- {x}" for x in SAFETY_LOCKS)
    lines.extend(["", "## Real-data rules"])
    lines.extend(f"- {x}" for x in REAL_DATA_RULES)
    write_text(RUN_ROOT / "REPAIR_BOARD.md", "\n".join(lines) + "\n")


def final_handoff(start: dt.datetime, end: dt.datetime, cycles_completed: int, latest_candidate: Optional[Path], latest_after: Optional[List[Dict[str, Any]]]) -> None:
    lines = [
        "# Couple-hour LaTeX + publishability repair final handoff",
        "",
        f"Run ID: `{RUN_ID}`",
        f"Started UTC: {start.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"Finished UTC: {end.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"Cycles completed: {cycles_completed}",
        "",
        "## Latest candidate",
        f"`{latest_candidate}`" if latest_candidate else "[none]",
        "",
    ]
    if latest_after:
        all_build_ok = all(r["build_ok"] for r in latest_after)
        all_clean_ok = all(r["clean_ok"] for r in latest_after)
        lines.append(f"- all_build_ok: {all_build_ok}")
        lines.append(f"- all_clean_ok: {all_clean_ok}")
        lines.append(f"- total_layout_warning_count: {sum(int(r['layout_warning_count']) for r in latest_after)}")
        lines.append(f"- total_undefined_count: {sum(int(r['undefined_count']) for r in latest_after)}")
        for r in latest_after:
            lines.append(f"- `{Path(r['tex']).name}` build_ok={r['build_ok']} clean_ok={r['clean_ok']} layout_warnings={r['layout_warning_count']} undefined={r['undefined_count']} fatal={r['fatal_hits']} pdf={r['pdf']} sha256={r['pdf_sha256']}")
    lines.extend(["", "## Safety ledger"])
    lines.extend(f"- {x}" for x in SAFETY_LOCKS)
    lines.append("")
    lines.append("No public replacement/publish was performed by this sprint. Promote only after a separate verification/promotion gate.")
    write_text(RUN_ROOT / "FINAL_LATEX_REPAIR_HANDOFF.md", "\n".join(lines) + "\n")


def main() -> int:
    start = dt.datetime.now(dt.timezone.utc)
    end_target = start + dt.timedelta(seconds=WINDOW_SECONDS)
    RUN_ROOT.mkdir(parents=True, exist_ok=True)
    source, source_note = choose_source()
    write_board(start, source, source_note)
    write_text(RUN_ROOT / "RUNNING.pid", str(os.getpid()) + "\n")
    status(state="started", pid=os.getpid(), run_root=str(RUN_ROOT), started_utc=start.strftime("%Y-%m-%dT%H:%M:%SZ"), target_end_utc=end_target.strftime("%Y-%m-%dT%H:%M:%SZ"), source_candidate=str(source), source_note=source_note, cycle=0, cycles_completed=0)
    ledger(f"repair sprint started from {source} ({source_note})")

    current_source = source
    latest_candidate: Optional[Path] = None
    latest_after: Optional[List[Dict[str, Any]]] = None
    cycles_completed = 0

    for cycle in range(1, MAX_CYCLES + 1):
        remaining = (end_target - dt.datetime.now(dt.timezone.utc)).total_seconds()
        if remaining < MIN_REMAINING_SECONDS:
            ledger(f"stopping before cycle {cycle}; remaining {int(remaining)}s below threshold")
            break
        candidate = copy_candidate(current_source, cycle)
        latest_candidate = candidate
        status(state="cycle_running", cycle=cycle, cycles_completed=cycles_completed, candidate=str(candidate))
        ledger(f"cycle {cycle}: copied candidate from {current_source} to {candidate}")

        lint_before = run_tex_lint(candidate, cycle, "before")
        ledger(f"cycle {cycle}: tex lint-before errors={lint_before.get('error_count')} warnings={lint_before.get('warning_count')} findings={lint_before.get('finding_count')}")

        before = compile_all(candidate, cycle, "before")
        ledger(f"cycle {cycle}: strict compile-before build_ok={sum(1 for r in before if r['build_ok'])}/9 clean_ok={sum(1 for r in before if r['clean_ok'])}/9 layout_warnings={sum(int(r['layout_warning_count']) for r in before)} undefined={sum(int(r['undefined_count']) for r in before)}")

        lane_reports: List[Tuple[str, int, Path]] = []
        runnable = [lane for lane in LANES if (cycle - 1) % int(lane.get("frequency", 1)) == 0]
        with cf.ThreadPoolExecutor(max_workers=min(5, len(runnable))) as ex:
            futs = [ex.submit(run_lane, lane, candidate, before, cycle) for lane in runnable]
            for fut in cf.as_completed(futs):
                try:
                    lane_reports.append(fut.result())
                except Exception as exc:
                    err_path = RUN_ROOT / "lanes" / "exceptions" / f"cycle_{cycle:02d}_{len(lane_reports)}.md"
                    write_text(err_path, f"[EXCEPTION] {type(exc).__name__}: {exc}\n")
                    lane_reports.append(("exception", 125, err_path))
        lane_reports.sort(key=lambda x: x[0])
        ledger(f"cycle {cycle}: lane reports finished ({len(lane_reports)} lanes)")

        feed = write_feed(candidate, before, lane_reports, cycle)
        status(latest_feed=str(feed))
        ledger(f"cycle {cycle}: feed packet written {feed}")

        rc, integ_report = run_integrator(candidate, feed, before, cycle)
        ledger(f"cycle {cycle}: writer integrator finished exit={rc}")

        lint_after = run_tex_lint(candidate, cycle, "after")
        ledger(f"cycle {cycle}: tex lint-after errors={lint_after.get('error_count')} warnings={lint_after.get('warning_count')} findings={lint_after.get('finding_count')}")

        after = compile_all(candidate, cycle, "after")
        latest_after = after
        all_build_ok = all(r["build_ok"] for r in after)
        all_clean_ok = all(r["clean_ok"] for r in after)
        total_layout = sum(int(r["layout_warning_count"]) for r in after)
        total_undefined = sum(int(r["undefined_count"]) for r in after)
        ledger(f"cycle {cycle}: strict compile-after build_ok={sum(1 for r in after if r['build_ok'])}/9 clean_ok={sum(1 for r in after if r['clean_ok'])}/9 layout_warnings={total_layout} undefined={total_undefined}")
        cycles_completed = cycle
        status(state="between_cycles", cycle=cycle, cycles_completed=cycles_completed, candidate=str(candidate), latest_integrator_log=str(integ_report), latest_build_all_ok=all_build_ok, latest_clean_all_ok=all_clean_ok, latest_layout_warning_count=total_layout, latest_undefined_count=total_undefined, latest_lint_error_count=lint_after.get("error_count"), latest_lint_warning_count=lint_after.get("warning_count"))
        current_source = candidate

        if all_clean_ok:
            ledger(f"cycle {cycle}: strict LaTeX clean PASS achieved; stopping early")
            break

        remaining = (end_target - dt.datetime.now(dt.timezone.utc)).total_seconds()
        if remaining < MIN_REMAINING_SECONDS:
            ledger(f"cycle {cycle}: no enough time for another full cycle; stopping")
            break
        sleep_s = min(SLEEP_BETWEEN_CYCLES, max(0, int(remaining - MIN_REMAINING_SECONDS)))
        if sleep_s:
            ledger(f"cycle {cycle}: sleeping {sleep_s}s before next cycle")
            time.sleep(sleep_s)

    end = dt.datetime.now(dt.timezone.utc)
    final_handoff(start, end, cycles_completed, latest_candidate, latest_after)
    status(state="completed", cycles_completed=cycles_completed, final_handoff=str(RUN_ROOT / "FINAL_LATEX_REPAIR_HANDOFF.md"), latest_candidate=str(latest_candidate) if latest_candidate else None)
    ledger("repair sprint completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
