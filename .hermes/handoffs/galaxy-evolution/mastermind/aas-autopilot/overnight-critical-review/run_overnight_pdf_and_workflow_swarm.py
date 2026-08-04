#!/usr/bin/env python3
"""Overnight Galaxy Evolution PDF + workflow scrutiny swarm.

Local/artifact-only swarm for about 10 hours.

Scope:
- Critically review current public-linked PDFs, local publishable candidate PDFs,
  research-topic manuscripts, and manuscript-generation system artifacts.
- Feed review findings into candidate-copy PDF-writing cycles.
- Run a separate workflow-scrutiny lane on the wiki -> research topic -> PDF
  system and write improvement reports.

Safety locks:
- No public-linked PDF replacement.
- No public/live root edits.
- No DB/API/wiki/trust writes.
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
from typing import Any, Dict, Iterable, List, Optional, Tuple

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTO = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
INTEGRATED_ROOT = AUTO / "integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z"
PUBLISHABLE_ROOT = AUTO / "publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers"
PUBLISHABLE_HANDOFF = AUTO / "publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/FINAL_POST_FIX_HANDOFF.md"
ACTIVE_SPRINT = AUTO / "research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z"
PUBLIC_WIKI_ROOT = REPO / "frontend/public/agent-reports/wiki-method-results/galaxy-evolution"
LIVE_PUBLIC_WIKI_ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution")
IDEAS_CLIENT = REPO / "frontend/src/app/ideas/IdeasIndexClient.tsx"
LIVE_IDEAS_CLIENT = Path("/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/ideas/IdeasIndexClient.tsx")

RUN_ID = os.environ.get("NEBULAMIND_OVERNIGHT_REVIEW_RUN_ID") or "OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_" + dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUN_ROOT = AUTO / "overnight-critical-review" / RUN_ID
WINDOW_SECONDS = int(os.environ.get("NEBULAMIND_OVERNIGHT_REVIEW_SECONDS", str(10 * 60 * 60)))
MAX_CYCLES = int(os.environ.get("NEBULAMIND_OVERNIGHT_REVIEW_MAX_CYCLES", "20"))
MIN_REMAINING_SECONDS = int(os.environ.get("NEBULAMIND_OVERNIGHT_MIN_REMAINING", str(35 * 60)))
LANE_TIMEOUT = int(os.environ.get("NEBULAMIND_OVERNIGHT_LANE_TIMEOUT", str(80 * 60)))
INTEGRATOR_TIMEOUT = int(os.environ.get("NEBULAMIND_OVERNIGHT_INTEGRATOR_TIMEOUT", str(80 * 60)))
SLEEP_BETWEEN_CYCLES = int(os.environ.get("NEBULAMIND_OVERNIGHT_SLEEP_BETWEEN_CYCLES", str(8 * 60)))

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
    "write only under this overnight run root and its copied candidate packages",
    "review lanes write reports only; only the candidate-copy integrator edits candidate-copy TeX",
    "no public-linked PDF replacement",
    "no public/live frontend or static root edits",
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
    "Every quantitative claim must trace to real local artifacts or checkable public sources.",
    "Absent data must be written as absent/future real-data requirements, not inferred as results.",
    "RP-1 stays association-only; papers 2-9 stay SDSS optical denominator/proxy data notes unless new real data are inventoried.",
]

LANES = [
    {
        "name": "hwao_director",
        "provider": "agy",
        "model": "Gemini 3.1 Pro (Low)",
        "role": "Hwao/Fable director: prioritize paper-quality work, decide what should feed writer pilots, and keep scope honest.",
        "frequency": 1,
    },
    {
        "name": "gemini_deep_pdf_critic",
        "provider": "agy",
        "model": "Gemini 3.1 Pro (High)",
        "role": "Gemini Deep Research critic: strict astronomy/AAS-style review of all 9 PDFs and research-topic manuscripts.",
        "frequency": 1,
    },
    {
        "name": "gemini_flash_factcheck",
        "provider": "agy",
        "model": "Gemini 3.5 Flash (Low)",
        "role": "Goru/Gemini low-usage fact-check: citation display, source-role, no-overclaim, and missing-observable scan.",
        "frequency": 1,
    },
    {
        "name": "gptoss_skeptic",
        "provider": "agy",
        "model": "GPT-OSS 120B (Medium)",
        "role": "Low-usage local/open model skeptic: adversarial read for unclear logic, structure, and workflow risk.",
        "frequency": 1,
    },
    {
        "name": "claude_lana_manuscript",
        "provider": "agy",
        "model": "Claude Sonnet 4.6 (Thinking)",
        "role": "Lana-style manuscript reviewer: polish priorities, journal-readiness, reader experience, and exact safe rewrites.",
        "frequency": 2,
    },
    {
        "name": "codex_kun_repro",
        "provider": "codex",
        "model": "gpt-5.4-mini",
        "role": "Kun/Codex read-only reproducibility, TeX, provenance, and no-mock-data audit.",
        "frequency": 1,
    },
    {
        "name": "workflow_scrutiny",
        "provider": "agy",
        "model": "Gemini 3.5 Flash (Medium)",
        "role": "Independent workflow auditor: scrutinize wiki -> topics -> manuscript/PDF -> public-link pipeline and propose system improvements.",
        "frequency": 1,
    },
]


def utc() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def kst_from_utc(ts: Optional[dt.datetime] = None) -> str:
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
    append(RUN_ROOT / "OVERNIGHT_LEDGER.md", f"- {utc()} / {kst_from_utc()} — {line}\n")


def status(**kwargs: Any) -> None:
    path = RUN_ROOT / "OVERNIGHT_STATUS.json"
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


def title_abs(tex: Path) -> Dict[str, str]:
    text = read_text(tex, 100000)
    title = "[missing title]"
    abstract = "[missing abstract]"
    m = re.search(r"\\title(?:\[[^\]]*\])?\{(.+?)\}", text, re.S)
    if m:
        title = compact(m.group(1), 280)
    m = re.search(r"\\begin\{abstract\}(.+?)\\end\{abstract\}", text, re.S)
    if m:
        abstract = compact(m.group(1), 1100)
    return {"title": title, "abstract": abstract}


def copy_candidate(source: Path, cycle: int) -> Path:
    dest = RUN_ROOT / "candidates" / f"cycle_{cycle:02d}_nine_papers"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True, exist_ok=True)
    for d in PAPER_DIRS:
        shutil.copytree(source / d, dest / d)
    write_text(dest / "SOURCE_COPY.json", json.dumps({"source": str(source), "cycle": cycle, "copied_utc": utc(), "paper_dirs": PAPER_DIRS}, indent=2))
    return dest


def compile_one(tex: Path) -> Dict[str, Any]:
    pdf = tex.with_suffix(".pdf")
    log = tex.with_suffix(".overnight.compile.log")
    try:
        proc = subprocess.run(["tectonic", tex.name], cwd=str(tex.parent), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=12 * 60)
        out = proc.stdout or ""
        rc = proc.returncode
    except Exception as exc:
        out = f"[EXCEPTION] {type(exc).__name__}: {exc}\n"
        rc = 125
    write_text(log, out)
    header = ""
    if pdf.exists():
        try:
            header = pdf.open("rb").read(4).decode(errors="replace")
        except Exception:
            header = ""
    fatal = [m for m in ["error:", "fatal", "emergency stop", "halted"] if m in out.lower()]
    return {"tex": str(tex), "pdf": str(pdf), "ok": rc == 0 and pdf.exists() and header == "%PDF" and not fatal, "returncode": rc, "pdf_bytes": pdf.stat().st_size if pdf.exists() else 0, "pdf_sha256": sha256(pdf) if pdf.exists() else None, "header": header, "fatal_markers": fatal, "log": str(log)}


def compile_all(candidate: Path, cycle: int, label: str = "compile") -> List[Dict[str, Any]]:
    results = [compile_one(tex) for tex in paper_tex_paths(candidate)]
    receipt = candidate / f"CYCLE_{cycle:02d}_{label.upper()}_RECEIPT.json"
    write_text(receipt, json.dumps({"created_utc": utc(), "label": label, "all_ok": len(results) == 9 and all(r["ok"] for r in results), "results": results}, indent=2, sort_keys=True))
    lines = [f"# Cycle {cycle} {label} receipt", "", f"created_utc: {utc()}", ""]
    for r in results:
        lines.append(f"- `{Path(r['tex']).parent.parent.name}` ok={r['ok']} bytes={r['pdf_bytes']} sha256={r['pdf_sha256']}")
    write_text(candidate / f"CYCLE_{cycle:02d}_{label.upper()}_RECEIPT.md", "\n".join(lines) + "\n")
    return results


def deterministic_inventory(candidate: Path, cycle: int) -> Dict[str, Any]:
    public_pdfs = []
    for root in [PUBLIC_WIKI_ROOT, LIVE_PUBLIC_WIKI_ROOT]:
        if root.exists():
            for p in sorted(root.glob("*/research-topics-from-wiki-20260708T090359Z/*.pdf")):
                public_pdfs.append({"path": str(p), "bytes": p.stat().st_size, "sha256": sha256(p)})
    candidate_papers = []
    for tex in paper_tex_paths(candidate):
        meta = title_abs(tex)
        pdf = tex.with_suffix(".pdf")
        candidate_papers.append({"slug": tex.parent.parent.name, "tex": str(tex), "pdf": str(pdf), "title": meta["title"], "abstract": meta["abstract"], "tex_sha256": sha256(tex), "pdf_sha256": sha256(pdf), "pdf_bytes": pdf.stat().st_size if pdf.exists() else 0})
    workflow_files = [str(p) for p in [IDEAS_CLIENT, LIVE_IDEAS_CLIENT, PUBLISHABLE_HANDOFF, ACTIVE_SPRINT / "SPRINT_STATUS.json", ACTIVE_SPRINT / "SPRINT_BOARD.md"] if p.exists()]
    inv = {"cycle": cycle, "created_utc": utc(), "candidate": str(candidate), "candidate_papers": candidate_papers, "public_research_topic_pdfs": public_pdfs, "workflow_files": workflow_files, "safety_locks": SAFETY_LOCKS, "real_data_rules": REAL_DATA_RULES}
    write_text(RUN_ROOT / "inventories" / f"CYCLE_{cycle:02d}_INVENTORY.json", json.dumps(inv, indent=2, sort_keys=True))
    md = [f"# Cycle {cycle} deterministic inventory", "", f"created_utc: {utc()}", "", "## Candidate papers"]
    for p in candidate_papers:
        md.append(f"- `{p['slug']}` pdf_bytes={p['pdf_bytes']} pdf_sha256={p['pdf_sha256']} title={p['title']}")
    md += ["", "## Public research-topic PDFs"]
    for p in public_pdfs:
        md.append(f"- `{p['path']}` bytes={p['bytes']} sha256={p['sha256']}")
    write_text(RUN_ROOT / "inventories" / f"CYCLE_{cycle:02d}_INVENTORY.md", "\n".join(md) + "\n")
    return inv


def base_context(candidate: Path, cycle: int, compile_results: List[Dict[str, Any]], inventory: Dict[str, Any], previous_feed: Optional[Path]) -> str:
    parts = [
        f"Run root: {RUN_ROOT}",
        f"Cycle: {cycle}",
        f"Candidate package: {candidate}",
        f"Source publishable handoff: {PUBLISHABLE_HANDOFF}",
        f"Integrated 9-paper root: {INTEGRATED_ROOT}",
        f"Active pre-existing PDF-writing sprint (do not interfere): {ACTIVE_SPRINT}",
        f"Public wiki/PDF root (read-only): {PUBLIC_WIKI_ROOT}",
        f"Live public wiki/PDF root (read-only): {LIVE_PUBLIC_WIKI_ROOT}",
        "",
        "User overnight directive: critically review current PDFs and research-topic manuscripts, feed findings into PDF-writing pilots, and separately scrutinize the wiki-to-PDF workflow/system for improvement. Work about 10 hours using available/low-usage models.",
        "",
        "Safety locks:",
        "\n".join(f"- {x}" for x in SAFETY_LOCKS),
        "",
        "Real-data rules:",
        "\n".join(f"- {x}" for x in REAL_DATA_RULES),
        "",
        "Compile receipt summary:",
        json.dumps(compile_results, indent=2)[:10000],
        "",
        "Deterministic inventory summary:",
        json.dumps({"candidate_papers": inventory.get("candidate_papers", []), "public_pdf_count": len(inventory.get("public_research_topic_pdfs", [])), "workflow_files": inventory.get("workflow_files", [])}, indent=2)[:12000],
        "",
        "Candidate paper summaries:",
    ]
    for tex in paper_tex_paths(candidate):
        meta = title_abs(tex)
        parts.append(f"- slug={tex.parent.parent.name}\n  tex={tex}\n  pdf={tex.with_suffix('.pdf')}\n  title={meta['title']}\n  abstract={meta['abstract']}")
    if previous_feed and previous_feed.exists():
        parts.append("\nPrevious feed packet for continuity:\n" + read_text(previous_feed, 16000))
    parts.append("\nRelevant handoff excerpts:\n" + read_text(PUBLISHABLE_HANDOFF, 12000))
    return "\n".join(parts)


def lane_prompt(lane: Dict[str, str], candidate: Path, cycle: int, compile_results: List[Dict[str, Any]], inventory: Dict[str, Any], previous_feed: Optional[Path]) -> str:
    context = base_context(candidate, cycle, compile_results, inventory, previous_feed)
    marker = f"OVERNIGHT_{lane['name'].upper()}_CYCLE_{cycle:02d}"
    if lane["name"] == "workflow_scrutiny":
        task = """Scrutinize the overall NebulaMind Galaxy Evolution workflow from method wiki / research-topic pages to manuscript PDFs and current public linking. Inspect the named files/roots if your tool environment allows. Focus on system/process improvements: source-of-truth drift, stale public PDFs versus local candidates, topic-to-PDF mapping, review gates, audit receipts, no-mock-data enforcement, PDF publishability gates, frontend linking, handoff naming, and morning operations. Produce a concrete improvement report with prioritized fixes and no implementation beyond the report."""
    else:
        task = """Critically review the 9 current candidate PDFs/manuscript TeX files and the public-linked research-topic manuscripts. Find the highest-value issues that should feed the candidate-copy PDF-writing pilot: overclaims, missing caveats, weak abstracts, confusing conclusion/limitations wording, citation role errors, stale public-vs-local mismatch, poor reader flow, figure/table/caption problems, and reproducibility risks. Give exact safe rewrite guidance where possible, but do not edit files."""
    return f"""{lane['role']}

Output marker: {marker}

Work mode: artifact-only, read-only lane. Do not edit files. Do not publish. Do not call or request credentials.

{task}

Required output sections:
1. {marker} status: PASS/ISSUES_FOUND/BLOCKED.
2. Files/paths actually inspected or, if not inspectable, paths used from context.
3. Ranked findings, with severity: blocker/major/minor/improvement.
4. Exact feed for PDF-writing pilot: concrete TeX-level edits or section rewrite instructions, preserving measured values and real-data boundaries.
5. Real-data/source/citation audit notes.
6. Workflow/system notes if relevant.
7. Safety ledger confirming no edits/public/db/deploy/git/cron/billing/OAuth/submission.

{context}
"""


def run_model_lane(lane: Dict[str, Any], candidate: Path, cycle: int, compile_results: List[Dict[str, Any]], inventory: Dict[str, Any], previous_feed: Optional[Path], remaining: int) -> Dict[str, Any]:
    prompt = lane_prompt(lane, candidate, cycle, compile_results, inventory, previous_feed)
    brief_path = RUN_ROOT / "briefs" / f"cycle_{cycle:02d}_{lane['name']}.md"
    write_text(brief_path, prompt)
    out_path = RUN_ROOT / "lanes" / lane["name"] / f"{lane['name'].upper()}_CYCLE_{cycle:02d}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    timeout = max(60, min(LANE_TIMEOUT, remaining))
    started = time.time()
    out_path.write_text(f"# {lane['name']} cycle {cycle}\nStarted UTC: {utc()}\nModel: {lane['model']}\nProvider: {lane['provider']}\nBrief: {brief_path}\n\n")
    if lane["provider"] == "agy":
        cmd = ["agy", "--model", lane["model"], "--mode", "plan", "--print-timeout", f"{max(5, timeout // 60)}m0s", "--print", prompt]
        cwd = REPO
    elif lane["provider"] == "codex":
        cmd = ["codex", "exec", "-m", lane["model"], "--sandbox", "read-only", "--cd", str(REPO), prompt]
        cwd = REPO
    else:
        cmd = ["true"]
        cwd = REPO
    try:
        proc = subprocess.run(cmd, cwd=str(cwd), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
        text = proc.stdout or ""
        rc = proc.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        raw = exc.stdout
        text = raw.decode(errors="replace") if isinstance(raw, bytes) else (raw or "")
        text += f"\n\n[TIMEOUT after {timeout}s]\n"
        rc = 124
        timed_out = True
    except Exception as exc:
        text = f"[EXCEPTION] {type(exc).__name__}: {exc}\n"
        rc = 125
        timed_out = False
    with out_path.open("a") as f:
        f.write(text)
        f.write(f"\n\n# command_result\nexit_code={rc}\nelapsed_s={round(time.time()-started,1)}\ntimed_out={timed_out}\nfinished_utc={utc()}\n")
    return {"lane": lane["name"], "model": lane["model"], "provider": lane["provider"], "exit_code": rc, "timed_out": timed_out, "output_path": str(out_path), "brief_path": str(brief_path), "elapsed_s": round(time.time() - started, 1)}


def run_lanes(candidate: Path, cycle: int, compile_results: List[Dict[str, Any]], inventory: Dict[str, Any], previous_feed: Optional[Path], end_ts: float) -> List[Dict[str, Any]]:
    active = [lane for lane in LANES if cycle % int(lane.get("frequency", 1)) == 0]
    remaining = max(60, int(end_ts - time.time()))
    results: List[Dict[str, Any]] = []
    # Limit concurrency so existing autopilots are not starved; still keeps multiple lanes active.
    with cf.ThreadPoolExecutor(max_workers=min(4, len(active))) as ex:
        futs = [ex.submit(run_model_lane, lane, candidate, cycle, compile_results, inventory, previous_feed, remaining) for lane in active]
        for fut in cf.as_completed(futs):
            results.append(fut.result())
    write_text(RUN_ROOT / "lane-results" / f"CYCLE_{cycle:02d}_LANE_RESULTS.json", json.dumps(results, indent=2, sort_keys=True))
    return sorted(results, key=lambda r: r["lane"])


def collect_lane_texts(lane_results: List[Dict[str, Any]], limit_each: int = 250000) -> str:
    chunks = []
    for r in lane_results:
        p = Path(r["output_path"])
        text = read_text(p, limit_each)
        if "[TRUNCATED" in text:
            raise RuntimeError(f"lane report was truncated before feed assembly: {p}")
        chunks.append(f"\n===== {r['lane']} ({r['model']}) exit={r['exit_code']} =====\n" + text)
    return "\n".join(chunks)


def create_feed_packet(candidate: Path, cycle: int, lane_results: List[Dict[str, Any]], compile_results: List[Dict[str, Any]], inventory: Dict[str, Any]) -> Path:
    feed = RUN_ROOT / "feeds" / f"PDF_WRITING_FEED_CYCLE_{cycle:02d}.md"
    lines = [
        f"# PDF-writing feed cycle {cycle}",
        "",
        f"created_utc: {utc()}",
        f"candidate: `{candidate}`",
        "",
        "## Purpose",
        "This packet feeds critical review findings into the local candidate-copy PDF-writing pilot. It is not a public publish/replace instruction.",
        "",
        "## Safety locks",
        *[f"- {x}" for x in SAFETY_LOCKS],
        "",
        "## Compile status before writing",
    ]
    for r in compile_results:
        lines.append(f"- `{Path(r['tex']).parent.parent.name}` ok={r['ok']} bytes={r['pdf_bytes']} sha256={r['pdf_sha256']}")
    lines += ["", "## Lane outputs to integrate", collect_lane_texts(lane_results, 250000)]
    write_text(feed, "\n".join(lines) + "\n")
    return feed


def integrator_prompt(candidate: Path, cycle: int, feed: Path, compile_results: List[Dict[str, Any]]) -> str:
    tex_paths = paper_tex_paths(candidate)
    tex_list = "\n".join(f"- {p}" for p in tex_paths)
    return f"""You are the overnight candidate-copy PDF-writing integrator for NebulaMind Galaxy Evolution.

Output marker: OVERNIGHT_PDF_WRITER_INTEGRATOR_CYCLE_{cycle:02d}

Working root: {candidate}

You may edit ONLY these 9 candidate-copy TeX files:
{tex_list}

You may write/update ONLY this response file under the same candidate root:
- {candidate / f'CYCLE_{cycle:02d}_OVERNIGHT_INTEGRATOR_RESPONSE.md'}

Use this feed packet from reviewer lanes:
{feed}

Goal: improve the candidate PDFs/manuscripts based on critical reviews while preserving publishability and real-data integrity.

Mandatory rules:
- Candidate-copy only. Do not edit public roots, live roots, original integrated root, active sprint root, or repository source files.
- Preserve all measured values unless the feed points to a traceable real-data source proving a correction.
- Do not invent numbers, citations, URLs, DOI, arXiv, ADS, figure/table values, or new data.
- Keep RP-1 association-only; keep papers 2-9 as honest SDSS optical denominator/proxy data notes.
- Absent radio/X-ray/CO/HI/morphology/environment/outflow/simulation data stay as future real-data requirements.
- Prefer exact safe prose/citation-role/abstract/conclusion/limitation improvements over broad rewrites.
- Keep TeX compilable and existing figure paths intact.
- No public PDF replacement, DB/API/wiki/trust, deploy/restart, git, cron, billing/OAuth, credentials, or external submission.

Compile status before integration:
{json.dumps(compile_results, indent=2)[:12000]}

Feed packet content:
{read_text(feed, 65000)}
"""


def run_integrator(candidate: Path, cycle: int, feed: Path, compile_results: List[Dict[str, Any]], end_ts: float) -> Dict[str, Any]:
    prompt = integrator_prompt(candidate, cycle, feed, compile_results)
    brief = RUN_ROOT / "briefs" / f"cycle_{cycle:02d}_integrator.md"
    write_text(brief, prompt)
    out = RUN_ROOT / "lanes" / "integrator" / f"OVERNIGHT_PDF_WRITER_INTEGRATOR_CYCLE_{cycle:02d}.log"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"# integrator cycle {cycle}\nStarted UTC: {utc()}\nBrief: {brief}\n\n")
    timeout = max(60, min(INTEGRATOR_TIMEOUT, int(end_ts - time.time())))
    cmd = ["codex", "exec", "-m", "gpt-5.4-mini", "--sandbox", "workspace-write", "--cd", str(candidate), "--skip-git-repo-check", prompt]
    started = time.time()
    try:
        proc = subprocess.run(cmd, cwd=str(candidate), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
        text = proc.stdout or ""
        rc = proc.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        raw = exc.stdout
        text = raw.decode(errors="replace") if isinstance(raw, bytes) else (raw or "")
        text += f"\n\n[TIMEOUT after {timeout}s]\n"
        rc = 124
        timed_out = True
    except Exception as exc:
        text = f"[EXCEPTION] {type(exc).__name__}: {exc}\n"
        rc = 125
        timed_out = False
    with out.open("a") as f:
        f.write(text)
        f.write(f"\n\n# command_result\nexit_code={rc}\nelapsed_s={round(time.time()-started,1)}\ntimed_out={timed_out}\nfinished_utc={utc()}\n")
    return {"lane": "integrator", "model": "gpt-5.4-mini", "provider": "codex", "exit_code": rc, "timed_out": timed_out, "output_path": str(out), "brief_path": str(brief), "elapsed_s": round(time.time() - started, 1)}


def audit_candidate(candidate: Path, cycle: int, compile_results: List[Dict[str, Any]]) -> Dict[str, Any]:
    forbidden_patterns = [re.compile(r"\b(mock|synthetic|fake|placeholder|toy) data\b", re.I), re.compile(r"\b(invented|fabricated) (number|citation|data|result)s?\b", re.I)]
    hits: List[Dict[str, str]] = []
    for tex in paper_tex_paths(candidate):
        text = read_text(tex)
        for pat in forbidden_patterns:
            for m in pat.finditer(text):
                snip = compact(text[max(0, m.start() - 150): m.end() + 200], 400)
                hits.append({"tex": str(tex), "pattern": pat.pattern, "snippet": snip})
    audit = {"cycle": cycle, "created_utc": utc(), "candidate": str(candidate), "compile_all_ok": len(compile_results) == 9 and all(r["ok"] for r in compile_results), "compile_results": compile_results, "forbidden_wording_hits": hits[:100], "fatal_failures": []}
    if not audit["compile_all_ok"]:
        audit["fatal_failures"].append("compile_not_all_ok")
    write_text(candidate / f"CYCLE_{cycle:02d}_OVERNIGHT_AUDIT.json", json.dumps(audit, indent=2, sort_keys=True))
    md = [f"# Cycle {cycle} overnight audit", "", f"created_utc: {utc()}", f"compile_all_ok: {audit['compile_all_ok']}", f"fatal_failures: {audit['fatal_failures']}", f"forbidden_wording_hits_surfacd: {len(hits)}", "", "## Safety", *[f"- {x}" for x in SAFETY_LOCKS]]
    write_text(candidate / f"CYCLE_{cycle:02d}_OVERNIGHT_AUDIT.md", "\n".join(md) + "\n")
    return audit


def final_workflow_report(cycles: List[Dict[str, Any]], latest_candidate: Optional[Path]) -> None:
    workflow_outputs = []
    for p in sorted((RUN_ROOT / "lanes/workflow_scrutiny").glob("*.md")):
        text = read_text(p, 250000)
        if "[TRUNCATED" in text:
            raise RuntimeError(f"workflow lane report was truncated before final report synthesis: {p}")
        workflow_outputs.append(f"\n===== {p.name} =====\n" + text)
    prompt = f"""You are Hwao/Tori synthesizing the overnight workflow-scrutiny outputs into a practical system-improvement report.

Output marker: OVERNIGHT_WORKFLOW_SYSTEM_IMPROVEMENT_FINAL

Write a concise but actionable report to improve the NebulaMind Galaxy Evolution pipeline from method wiki / research-topic pages to manuscript PDFs/public PDF links/current autopilot system.

Use only the artifacts below. Do not invent facts. Do not recommend DB/deploy/git/public replacement without explicit approval gates.

Run root: {RUN_ROOT}
Latest candidate: {latest_candidate}
Cycles: {json.dumps(cycles, indent=2)[:20000]}
Safety locks: {SAFETY_LOCKS}

Workflow lane outputs:
{''.join(workflow_outputs)[:250000]}
"""
    brief = RUN_ROOT / "briefs" / "FINAL_WORKFLOW_REPORT_PROMPT.md"
    write_text(brief, prompt)
    out = RUN_ROOT / "workflow" / "WORKFLOW_SYSTEM_IMPROVEMENT_REPORT.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"# workflow system improvement final\nStarted UTC: {utc()}\nBrief: {brief}\n\n")
    try:
        proc = subprocess.run(["agy", "--model", "Gemini 3.1 Pro (Low)", "--mode", "plan", "--print-timeout", "30m0s", "--print", prompt], cwd=str(REPO), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=35 * 60)
        text = proc.stdout or ""
        rc = proc.returncode
    except Exception as exc:
        text = f"[EXCEPTION] {type(exc).__name__}: {exc}\n"
        rc = 125
    with out.open("a") as f:
        f.write(text)
        f.write(f"\n\n# command_result\nexit_code={rc}\nfinished_utc={utc()}\n")


def write_board(start_dt: dt.datetime, end_dt: dt.datetime) -> None:
    lines = [
        "# Overnight PDF review + workflow scrutiny swarm",
        "",
        f"Run ID: `{RUN_ID}`",
        f"Run root: `{RUN_ROOT}`",
        f"Start UTC: {start_dt.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"Target end UTC: {end_dt.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"Start KST: {kst_from_utc(start_dt)}",
        f"Target end KST: {kst_from_utc(end_dt)}",
        "",
        "## User directive",
        "Critically review current PDFs and research-topic manuscripts, feed review output into PDF-writing pilots, and have another autopilot scrutinize the wiki-to-PDF/current workflow system for improvements. Work overnight for about 10 hours and use available/low-usage models.",
        "",
        "## Inputs",
        f"- Local publishable candidate: `{PUBLISHABLE_ROOT}`",
        f"- Publishability handoff: `{PUBLISHABLE_HANDOFF}`",
        f"- Integrated 9-paper root: `{INTEGRATED_ROOT}`",
        f"- Active existing sprint (left running, not interfered with): `{ACTIVE_SPRINT}`",
        f"- Public-linked PDFs root (read-only): `{PUBLIC_WIKI_ROOT}`",
        f"- Live public PDFs root (read-only): `{LIVE_PUBLIC_WIKI_ROOT}`",
        "",
        "## Lanes",
    ]
    for lane in LANES:
        lines.append(f"- `{lane['name']}` — {lane['model']} — {lane['role']}")
    lines += ["", "## Safety locks", *[f"- {x}" for x in SAFETY_LOCKS], "", "## Real-data rules", *[f"- {x}" for x in REAL_DATA_RULES]]
    write_text(RUN_ROOT / "OVERNIGHT_BOARD.md", "\n".join(lines) + "\n")
    write_text(RUN_ROOT / "INPUTS.json", json.dumps({"run_id": RUN_ID, "start_utc": start_dt.strftime('%Y-%m-%dT%H:%M:%SZ'), "target_end_utc": end_dt.strftime('%Y-%m-%dT%H:%M:%SZ'), "publishable_root": str(PUBLISHABLE_ROOT), "publishability_handoff": str(PUBLISHABLE_HANDOFF), "integrated_root": str(INTEGRATED_ROOT), "active_sprint": str(ACTIVE_SPRINT), "public_wiki_root": str(PUBLIC_WIKI_ROOT), "live_public_wiki_root": str(LIVE_PUBLIC_WIKI_ROOT), "lanes": LANES, "safety_locks": SAFETY_LOCKS, "real_data_rules": REAL_DATA_RULES}, indent=2, sort_keys=True))


def update_latest_run_symlink() -> None:
    latest = RUN_ROOT.parent / "latest_run"
    try:
        if latest.is_symlink() or latest.exists():
            latest.unlink()
        latest.symlink_to(RUN_ROOT, target_is_directory=True)
        ledger(f"updated latest_run symlink -> {RUN_ROOT}")
    except Exception as exc:
        ledger(f"latest_run symlink update failed: {type(exc).__name__}: {exc}")


def final_handoff(cycles: List[Dict[str, Any]], latest_candidate: Optional[Path], passed_compile: bool) -> None:
    data = {"run_id": RUN_ID, "finished_utc": utc(), "latest_candidate": str(latest_candidate) if latest_candidate else None, "cycles": cycles, "passed_compile": passed_compile, "safety_locks": SAFETY_LOCKS}
    write_text(RUN_ROOT / "FINAL_OVERNIGHT_HANDOFF.json", json.dumps(data, indent=2, sort_keys=True))
    lines = [
        "# Overnight PDF review + workflow scrutiny final handoff",
        "",
        f"Run ID: `{RUN_ID}`",
        f"Finished UTC: {utc()}",
        f"Latest candidate: `{latest_candidate}`" if latest_candidate else "Latest candidate: none",
        f"Latest compile all ok: {passed_compile}",
        "",
        "## Cycles",
    ]
    for c in cycles:
        lines.append(f"- cycle {c.get('cycle')}: candidate=`{c.get('candidate')}` lanes={len(c.get('lane_results', []))} integrator_exit={c.get('integrator_result', {}).get('exit_code')} compile_after_ok={c.get('compile_after_ok')} feed=`{c.get('feed')}`")
    if latest_candidate:
        lines += ["", "## Latest PDFs"]
        for tex in paper_tex_paths(latest_candidate):
            pdf = tex.with_suffix(".pdf")
            lines.append(f"- `{pdf}` exists={pdf.exists()} sha256={sha256(pdf) if pdf.exists() else None}")
    lines += ["", "## Workflow report", f"- `{RUN_ROOT / 'workflow/WORKFLOW_SYSTEM_IMPROVEMENT_REPORT.md'}`", "", "## Safety", *[f"- {x}" for x in SAFETY_LOCKS], "", "No public replacement/publish/submission was performed."]
    write_text(RUN_ROOT / "FINAL_OVERNIGHT_HANDOFF.md", "\n".join(lines) + "\n")
    update_latest_run_symlink()
    status(state="completed", latest_candidate=str(latest_candidate) if latest_candidate else None, cycles_completed=len(cycles), final_handoff=str(RUN_ROOT / "FINAL_OVERNIGHT_HANDOFF.md"), workflow_report=str(RUN_ROOT / "workflow/WORKFLOW_SYSTEM_IMPROVEMENT_REPORT.md"), latest_compile_all_ok=passed_compile)


def main() -> int:
    RUN_ROOT.mkdir(parents=True, exist_ok=True)
    start_dt = dt.datetime.now(dt.timezone.utc)
    end_dt = start_dt + dt.timedelta(seconds=WINDOW_SECONDS)
    end_ts = time.time() + WINDOW_SECONDS
    write_text(RUN_ROOT / "RUNNING.pid", str(os.getpid()) + "\n")
    write_board(start_dt, end_dt)
    status(state="starting", pid=os.getpid(), started_utc=start_dt.strftime("%Y-%m-%dT%H:%M:%SZ"), target_end_utc=end_dt.strftime("%Y-%m-%dT%H:%M:%SZ"), run_root=str(RUN_ROOT), source_candidate=str(PUBLISHABLE_ROOT), active_sprint=str(ACTIVE_SPRINT))
    ledger("overnight PDF review + workflow scrutiny swarm started")

    source = PUBLISHABLE_ROOT if PUBLISHABLE_ROOT.exists() else INTEGRATED_ROOT
    previous_feed: Optional[Path] = None
    latest_candidate: Optional[Path] = None
    cycles: List[Dict[str, Any]] = []
    latest_compile_ok = False

    for cycle in range(1, MAX_CYCLES + 1):
        if time.time() + MIN_REMAINING_SECONDS >= end_ts:
            ledger(f"stopping before cycle {cycle}: less than minimum remaining window")
            break
        candidate = copy_candidate(source, cycle)
        latest_candidate = candidate
        status(state="cycle_running", cycle=cycle, candidate=str(candidate), cycles_completed=len(cycles))
        ledger(f"cycle {cycle}: copied candidate from {source} to {candidate}")

        compile_before = compile_all(candidate, cycle, "before")
        latest_compile_ok = len(compile_before) == 9 and all(r["ok"] for r in compile_before)
        ledger(f"cycle {cycle}: compile-before {sum(1 for r in compile_before if r['ok'])}/{len(compile_before)} ok")

        inventory = deterministic_inventory(candidate, cycle)
        lane_results = run_lanes(candidate, cycle, compile_before, inventory, previous_feed, end_ts)
        ledger(f"cycle {cycle}: lane reports finished ({len(lane_results)} lanes)")

        feed = create_feed_packet(candidate, cycle, lane_results, compile_before, inventory)
        previous_feed = feed
        ledger(f"cycle {cycle}: feed packet written {feed}")

        integrator_result = run_integrator(candidate, cycle, feed, compile_before, end_ts)
        ledger(f"cycle {cycle}: integrator finished exit={integrator_result.get('exit_code')}")

        compile_after = compile_all(candidate, cycle, "after")
        latest_compile_ok = len(compile_after) == 9 and all(r["ok"] for r in compile_after)
        audit = audit_candidate(candidate, cycle, compile_after)
        ledger(f"cycle {cycle}: compile-after {sum(1 for r in compile_after if r['ok'])}/{len(compile_after)} ok fatal={audit.get('fatal_failures')}")

        cycle_record = {"cycle": cycle, "candidate": str(candidate), "feed": str(feed), "lane_results": lane_results, "integrator_result": integrator_result, "compile_after_ok": latest_compile_ok, "audit": audit, "finished_utc": utc()}
        cycles.append(cycle_record)
        write_text(RUN_ROOT / "cycle-records" / f"CYCLE_{cycle:02d}_RECORD.json", json.dumps(cycle_record, indent=2, sort_keys=True))
        status(state="between_cycles", cycle=cycle, candidate=str(candidate), latest_feed=str(feed), cycles_completed=len(cycles), latest_compile_all_ok=latest_compile_ok)

        source = candidate
        if time.time() + MIN_REMAINING_SECONDS >= end_ts:
            break
        # Brief pause keeps the overnight swarm from hammering every provider continuously.
        sleep_for = min(SLEEP_BETWEEN_CYCLES, max(0, int(end_ts - time.time() - MIN_REMAINING_SECONDS)))
        if sleep_for > 0:
            ledger(f"cycle {cycle}: sleeping {sleep_for}s before next cycle")
            time.sleep(sleep_for)

    try:
        final_workflow_report(cycles, latest_candidate)
    except Exception as exc:
        write_text(RUN_ROOT / "workflow" / "WORKFLOW_SYSTEM_IMPROVEMENT_REPORT.md", f"# workflow report failed\n\n{type(exc).__name__}: {exc}\n")
    final_handoff(cycles, latest_candidate, latest_compile_ok)
    ledger("overnight swarm completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
