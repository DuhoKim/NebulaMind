#!/usr/bin/env python3
"""Gemini-reviewed publishability loop for the 9 Galaxy Evolution manuscript PDFs.

Local-only safety posture:
- Works only under this publishability sprint root.
- Copies the existing integrated 9-paper TeX/PDF package into candidate cycle dirs.
- Reviewer lanes write reports; Codex integrator edits only candidate-copy TeX files.
- No public PDF replacement, live root writes, DB/API/wiki/trust/deploy/restart, git, cron,
  billing/OAuth/account, credential reads, or external submission.

Pass condition:
- Gemini/AGY deep-research reviewer writes exactly: GEMINI_DEEP_RESEARCH_VERDICT: PASS
- all 9 candidate TeX files compile to PDFs with %PDF headers;
- no local fatal audit guards fire.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTO = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
SOURCE_INTEGRATED = AUTO / "integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z"
SPRINT_ID = "PUBLISHABLE_9PDFS_DEEP_RESEARCH_20260709T160700Z"
SPRINT = AUTO / "publishability-sprints" / SPRINT_ID
AGY = Path("/Users/duhokim/.local/bin/agy")
CODEX = Path("/Users/duhokim/.local/bin/codex")
TECTONIC = shutil.which("tectonic") or "/opt/homebrew/bin/tectonic"

MAX_CYCLES = int(os.environ.get("NEBULAMIND_9PDF_PUBLISHABILITY_MAX_CYCLES", "24"))
DURATION_SECONDS = int(os.environ.get("NEBULAMIND_9PDF_PUBLISHABILITY_SECONDS", str(8 * 60 * 60)))
REVIEW_TIMEOUT = int(os.environ.get("NEBULAMIND_9PDF_REVIEW_TIMEOUT", str(85 * 60)))
INTEGRATOR_TIMEOUT = int(os.environ.get("NEBULAMIND_9PDF_INTEGRATOR_TIMEOUT", str(90 * 60)))
MIN_REMAINING_SECONDS = 20 * 60

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

REAL_DATA_POLICY = [
    "Never use mock, synthetic, fake, placeholder, or toy data.",
    "Do not invent numeric values, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, or figure results.",
    "New quantitative claims must be traceable to real local SDSS artifacts already present in the package or to cited public sources with checkable metadata.",
    "If a value is absent, write 'not measured here' or 'needs real data' instead of filling it in.",
    "Literature may motivate future work; it does not become a measured NebulaMind result.",
]

SAFETY_LOCKS = [
    "write only under this publishability sprint root and candidate copies",
    "no public pages, public PDF replacement, or live/static root edits",
    "no product DB, SQL, /api/pages, page_versions, wiki publish, trust recompute, or data mutation",
    "no deploy/restart",
    "no git commit/push/merge/rebase/history rewrite",
    "no cron creation/update",
    "no billing/cloud/OAuth/API-key/account changes and no credential/token/cookie reads",
    "no external manuscript submission",
]

REQUIRED_SHARED_PHRASES = ["SDSS", "60,000", "249,917", "24.0", "selection", "not a", "future"]
PUBLISHABILITY_TERMS = ["draft", "local-only", "No public page", "No public-linked PDF was replaced", "resulting status"]
BAD_DATA_USE_PATTERNS = [
    r"\b(?:use|used|using|based on|generated|created|filled|substituted)\b[^.\n]{0,100}\b(?:mock|synthetic|fake|placeholder|toy) data\b",
    r"\b(?:mock|synthetic|fake|placeholder|toy) data\b[^.\n]{0,100}\b(?:result|sample|catalog|catalogue|table|measurement|analysis)\b",
]


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def kst_now() -> str:
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S KST")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def append_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(text)


def read_text(path: Path, limit: Optional[int] = None) -> str:
    if not path.exists():
        return f"[MISSING {path}]"
    text = path.read_text(errors="replace")
    if limit and len(text) > limit:
        return text[:limit] + f"\n\n[TRUNCATED at {limit} chars from {path}]\n"
    return text


def sha256(path: Path) -> Optional[str]:
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def ledger(line: str) -> None:
    append_text(SPRINT / "SPRINT_LEDGER.md", f"- {utc_now()} / {kst_now()} — {line}\n")


def update_status(**kwargs: Any) -> None:
    path = SPRINT / "SPRINT_STATUS.json"
    current: Dict[str, Any] = {}
    if path.exists():
        try:
            current = json.loads(path.read_text())
        except Exception:
            current = {}
    current.update(kwargs)
    current["updated_utc"] = utc_now()
    write_text(path, json.dumps(current, indent=2, sort_keys=True))


def paper_tex_paths(candidate: Path) -> List[Path]:
    paths: List[Path] = []
    for d in PAPER_DIRS:
        matches = sorted((candidate / d / "aastex").glob("*_integrated.tex"))
        if matches:
            paths.append(matches[0])
    return paths


def extract_summary(tex: Path) -> Dict[str, Any]:
    text = read_text(tex, 250000)
    title = re.search(r"\\title(?:\[[^\]]*\])?\{(.+?)\}", text, flags=re.S)
    abstract = re.search(r"\\begin\{abstract\}(.+?)\\end\{abstract\}", text, flags=re.S)
    sections = re.findall(r"\\section\{(.+?)\}", text)
    return {
        "tex": str(tex),
        "paper_dir": tex.parents[1].name,
        "bytes": tex.stat().st_size if tex.exists() else 0,
        "sha256": sha256(tex),
        "title": re.sub(r"\s+", " ", title.group(1)).strip() if title else "[missing title]",
        "abstract": re.sub(r"\s+", " ", abstract.group(1)).strip()[:2200] if abstract else "[missing abstract]",
        "sections": sections,
        "citep_count": text.count("\\citep"),
        "bibitem_count": text.count("\\bibitem"),
        "figure_count": text.count("\\begin{figure"),
    }


def copy_source_to_candidate(cycle: int, source: Path) -> Path:
    candidate = SPRINT / "candidates" / f"cycle_{cycle:02d}_9pdf_package"
    if candidate.exists():
        shutil.rmtree(candidate)
    candidate.mkdir(parents=True)
    for d in PAPER_DIRS:
        shutil.copytree(source / d, candidate / d)
    # keep a tiny provenance file, not the whole decision-package tree
    write_text(candidate / "CANDIDATE_PROVENANCE.md", f"# 9-PDF publishability candidate cycle {cycle}\n\nCopied from `{source}` at {utc_now()}.\n")
    return candidate


def build_inventory(cycle: int, candidate: Path) -> Dict[str, Any]:
    papers = [extract_summary(p) for p in paper_tex_paths(candidate)]
    pdfs = []
    for tex in paper_tex_paths(candidate):
        pdf = tex.with_suffix(".pdf")
        header = ""
        if pdf.exists():
            try:
                header = pdf.open("rb").read(4).decode(errors="replace")
            except Exception:
                pass
        pdfs.append({"pdf": str(pdf), "exists": pdf.exists(), "bytes": pdf.stat().st_size if pdf.exists() else 0, "header": header, "sha256": sha256(pdf)})
    inv = {
        "sprint_id": SPRINT_ID,
        "cycle": cycle,
        "created_utc": utc_now(),
        "candidate": str(candidate),
        "source_integrated": str(SOURCE_INTEGRATED),
        "real_data_policy": REAL_DATA_POLICY,
        "safety_locks": SAFETY_LOCKS,
        "papers": papers,
        "pdfs": pdfs,
        "counts": {"papers": len(papers), "pdfs": len(pdfs), "existing_pdfs": sum(1 for p in pdfs if p["exists"] and p["header"] == "%PDF")},
    }
    out = SPRINT / "inventories" / f"PUBLISHABILITY_INVENTORY_CYCLE_{cycle:02d}.json"
    write_text(out, json.dumps(inv, indent=2, sort_keys=True))
    md = [f"# 9-PDF publishability inventory cycle {cycle}", "", f"Candidate: `{candidate}`", "", "## Papers"]
    for p in papers:
        md.append(f"- `{p['paper_dir']}` — {p['title']} (bytes={p['bytes']}, citep={p['citep_count']}, bibitem={p['bibitem_count']}, figs={p['figure_count']})")
    md += ["", "## PDFs"]
    for p in pdfs:
        md.append(f"- `{p['pdf']}` exists={p['exists']} bytes={p['bytes']} header={p['header']} sha256={p['sha256']}")
    write_text(SPRINT / "inventories" / f"PUBLISHABILITY_INVENTORY_CYCLE_{cycle:02d}.md", "\n".join(md) + "\n")
    return inv


def prompt_context(candidate: Path) -> str:
    parts = []
    for tex in paper_tex_paths(candidate):
        text = read_text(tex, 30000)
        parts.append(f"\n\n===== {tex.parents[1].name} :: {tex.name} =====\n{text}")
    return "".join(parts)


def make_review_prompt(cycle: int, candidate: Path, inventory: Dict[str, Any]) -> str:
    summaries = json.dumps(inventory["papers"], indent=2)[:32000]
    return f"""You are Gemini Deep Research reviewer for a NebulaMind Galaxy Evolution 9-manuscript PDF publishability gate.

Output marker: GEMINI_DEEP_RESEARCH_9PDF_REVIEW_CYCLE_{cycle:02d}
Final required verdict line, exactly one of:
GEMINI_DEEP_RESEARCH_VERDICT: PASS
GEMINI_DEEP_RESEARCH_VERDICT: FAIL

Task: review the resulted 9 manuscript PDFs through their exact AASTeX sources and compile inventory. Decide whether all nine are publishable as honest AAS-style short manuscripts or short data/proxy notes. They do NOT need to prove causal AGN feedback. They DO need to be scientifically publishable within their actual SDSS-only evidence boundary.

Strict pass criteria:
1. All 9 papers have a credible research question, abstract, method/data section, result section, interpretation/limitations, conclusion, citations, and figure/caption discipline.
2. No paper overclaims causal feedback, gas depletion, jet power, outflow escape, physical halo environment, or simulation validation from SDSS optical proxies alone.
3. Numeric claims are internally consistent and traceable to existing local SDSS/cached/integrated artifacts or cited public sources. Do not ask for new invented numbers.
4. The eight weaker papers may pass only if framed as publishable SDSS DR17 optical denominator/proxy/data-note papers, not as completed physical-feedback tests.
5. Any impossible requirement must be classified as "requires new real data; do not write as result yet".
6. No mock/synthetic/fake/placeholder/toy data may be introduced.
7. All required improvements must be actionable edits to the candidate TeX files, unless genuinely requiring new real data.

Review output sections:
- one-line overall verdict and why;
- 9-row table: paper id, publishability state (PASS/FAIL), main blocker, required edit;
- top 20 concrete safe edits ranked by publication value;
- citations/source role fixes with real identifiers only if known; otherwise say needs bibliographic verification;
- overclaim/future-data boundary fixes;
- what the integrator should refuse because it requires new real data;
- no-mock/no-secret/no-publication safety receipt.

Candidate root: {candidate}
Inventory summaries:
{summaries}

Full AASTeX source follows. Review source text as the content of the generated PDFs:
{prompt_context(candidate)}
"""


def make_integrator_prompt(cycle: int, candidate: Path, review_path: Path, audit_path: Optional[Path]) -> str:
    texs = paper_tex_paths(candidate)
    allowed = "\n".join(f"- {p}" for p in texs)
    previous_audit = read_text(audit_path, 24000) if audit_path else "[no previous audit]"
    return f"""You are the candidate-copy-only integrator for NebulaMind's 9 Galaxy Evolution manuscript PDFs.

Cycle: {cycle}
Candidate root: {candidate}
Review report: {review_path}
Output marker in your report: PUBLISHABLE_9PDFS_INTEGRATOR_CYCLE_{cycle:02d}

You may edit ONLY these candidate-copy TeX files:
{allowed}

You may write a concise integration response here:
- {candidate / f'CYCLE_{cycle:02d}_INTEGRATOR_RESPONSE.md'}

Hard real-data-only rules:
- Never introduce mock, synthetic, fake, placeholder, or toy data.
- Do not invent any number, sample size, table value, figure result, citation, URL, DOI, arXiv ID, or ADS bibcode.
- You may add citations only if they are already in the paper, already in another candidate paper in this package, or the review report gives checkable bibliographic metadata. If unsure, state the need instead of adding a fake citation.
- Preserve all measured numeric values unless correcting a clear typo from existing local source context.
- If a requested improvement requires new real data, write it as a limitation/future-data requirement, not as a result.
- Do not promote the eight proxy papers into causal feedback papers; make them publishable honest SDSS denominator/proxy/data-note manuscripts.

Desired edits:
- Apply every safe, high-value edit from the Gemini Deep Research review.
- Remove unprofessional/local-process language from manuscript bodies where it hurts publishability (e.g. "autopilot", "No public page", "local-only integration") while preserving reproducibility and safety in candidate receipts, not the article prose.
- Ensure each paper has publishable title/abstract/purpose, clear data/method, narrow result, interpretation with limitations, conclusion, and clean bibliography.
- Keep the RP-1 flagship as association-only unless actual added data support more.
- Improve the 8 weaker manuscripts enough to be publishable as short data/proxy notes, or explicitly state in the response why a manuscript cannot be made publishable without new real data.
- Keep TeX compilable with Tectonic.

Forbidden side effects:
- no edits outside the candidate root;
- no public/live roots, DB/API/wiki/trust/deploy/restart/git/cron/billing/OAuth/account/credential/external submission changes.

Gemini Deep Research review follows:
{read_text(review_path, 70000)}

Previous local audit follows:
{previous_audit}
"""


def run_cmd(label: str, cmd: List[str], out: Path, timeout: int, cwd: Path) -> Dict[str, Any]:
    start = time.time()
    write_text(out, f"# {label}\nStarted UTC: {utc_now()}\nCWD: {cwd}\nCommand head: {cmd[:8]}\n\n")
    try:
        proc = subprocess.run(cmd, cwd=str(cwd), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
        output = proc.stdout or ""
        rc = proc.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        output = (exc.stdout or "") + f"\n[TIMEOUT after {timeout}s]\n"
        rc = 124
        timed_out = True
    except Exception as exc:
        output = f"[EXCEPTION] {type(exc).__name__}: {exc}\n"
        rc = 125
        timed_out = False
    append_text(out, output)
    append_text(out, f"\n# command_result\nexit_code={rc}\nelapsed_s={time.time()-start:.1f}\ntimed_out={timed_out}\nfinished_utc={utc_now()}\n")
    return {"label": label, "exit_code": rc, "timed_out": timed_out, "elapsed_s": round(time.time() - start, 1), "output_path": str(out)}


def run_deep_review(cycle: int, candidate: Path, inventory: Dict[str, Any], timeout: int) -> Dict[str, Any]:
    prompt = make_review_prompt(cycle, candidate, inventory)
    prompt_path = SPRINT / "briefs" / f"cycle_{cycle:02d}_gemini_deep_research_review_prompt.md"
    out_path = SPRINT / "lanes" / "gemini_deep_research" / f"GEMINI_DEEP_RESEARCH_9PDF_REVIEW_CYCLE_{cycle:02d}.md"
    write_text(prompt_path, prompt)
    cmd = [str(AGY), "--model", "Gemini 3.1 Pro (High)", "--mode", "plan", "--print-timeout", f"{max(10, timeout//60)}m0s", "--print", prompt]
    return run_cmd(f"gemini-deep-research-9pdf-cycle-{cycle}", cmd, out_path, timeout, REPO)


def verdict_from_report(path: Path) -> str:
    text = read_text(path)
    pass_pat = re.search(r"^\s*GEMINI_DEEP_RESEARCH_VERDICT:\s*PASS\s*$", text, flags=re.M)
    fail_pat = re.search(r"^\s*GEMINI_DEEP_RESEARCH_VERDICT:\s*FAIL\s*$", text, flags=re.M)
    if pass_pat:
        return "PASS"
    if fail_pat:
        return "FAIL"
    return "MISSING"


def find_bad_data_use(text: str) -> List[str]:
    hits = []
    for pat in BAD_DATA_USE_PATTERNS:
        hits.extend(m.group(0) for m in re.finditer(pat, text, flags=re.I))
    return hits[:20]


def compile_tex(tex: Path) -> Dict[str, Any]:
    pdf = tex.with_suffix(".pdf")
    log = tex.with_suffix(".publishability.compile.log")
    if pdf.exists():
        try:
            pdf.unlink()
        except Exception:
            pass
    try:
        proc = subprocess.run([TECTONIC, tex.name], cwd=str(tex.parent), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=12 * 60)
        output = proc.stdout or ""
        rc = proc.returncode
    except Exception as exc:
        output = f"[EXCEPTION] {type(exc).__name__}: {exc}\n"
        rc = 125
    write_text(log, output)
    header = ""
    if pdf.exists():
        try:
            header = pdf.open("rb").read(4).decode(errors="replace")
        except Exception:
            pass
    bad_markers = [m for m in ["fatal", "emergency stop", "halted"] if m in output.lower()]
    return {"tex": str(tex), "pdf": str(pdf), "ok": rc == 0 and pdf.exists() and header == "%PDF" and not bad_markers, "returncode": rc, "header": header, "pdf_bytes": pdf.stat().st_size if pdf.exists() else 0, "sha256": sha256(pdf), "log": str(log), "bad_markers": bad_markers}


def local_audit(cycle: int, candidate: Path, review_verdict: str, compile_results: List[Dict[str, Any]]) -> Dict[str, Any]:
    fatal: List[Any] = []
    paper_audits = []
    for tex in paper_tex_paths(candidate):
        text = read_text(tex)
        missing_shared = [p for p in REQUIRED_SHARED_PHRASES if p not in text]
        stale_publishability_terms = [p for p in PUBLISHABILITY_TERMS if p in text]
        bad_data = find_bad_data_use(text)
        paper_audits.append({"tex": str(tex), "missing_shared_guard_phrases": missing_shared, "stale_local_process_terms": stale_publishability_terms, "bad_mock_synthetic_data_use": bad_data})
        # local-process terms are quality warnings, not fatal by themselves; they are useful for the next Gemini/Codex cycle
        if missing_shared:
            fatal.append({"missing_shared_guard_phrases": {str(tex): missing_shared}})
        if bad_data:
            fatal.append({"bad_mock_synthetic_data_use": {str(tex): bad_data}})
    for cr in compile_results:
        if not cr.get("ok"):
            fatal.append({"compile_failure": cr})
    if len(compile_results) != 9:
        fatal.append({"wrong_compile_count": len(compile_results)})
    audit = {
        "cycle": cycle,
        "candidate": str(candidate),
        "created_utc": utc_now(),
        "review_verdict": review_verdict,
        "compile_results": compile_results,
        "paper_audits": paper_audits,
        "fatal_failures": fatal,
        "all_compile_ok": len(compile_results) == 9 and all(r.get("ok") for r in compile_results),
        "pass_gate": review_verdict == "PASS" and len(fatal) == 0 and len(compile_results) == 9 and all(r.get("ok") for r in compile_results),
    }
    write_text(candidate / f"CYCLE_{cycle:02d}_PUBLISHABILITY_AUDIT.json", json.dumps(audit, indent=2, sort_keys=True))
    md = [f"# Cycle {cycle} publishability audit", "", f"Marker: `PUBLISHABLE_9PDFS_AUDIT_CYCLE_{cycle:02d}`", f"Review verdict: `{review_verdict}`", f"Pass gate: `{audit['pass_gate']}`", "", "## Compile results"]
    for cr in compile_results:
        md.append(f"- `{Path(cr['tex']).parents[1].name}` ok={cr.get('ok')} bytes={cr.get('pdf_bytes')} sha256={cr.get('sha256')} bad={cr.get('bad_markers')}")
    md += ["", f"Fatal failures: {len(fatal)}", "", "## Paper warnings"]
    for pa in paper_audits:
        md.append(f"- `{Path(pa['tex']).parents[1].name}` missing_guards={pa['missing_shared_guard_phrases']} stale_terms={pa['stale_local_process_terms']} bad_data={pa['bad_mock_synthetic_data_use']}")
    write_text(candidate / f"CYCLE_{cycle:02d}_PUBLISHABILITY_AUDIT.md", "\n".join(md) + "\n")
    return audit


def run_integrator(cycle: int, candidate: Path, review_path: Path, audit_path: Optional[Path], timeout: int) -> Dict[str, Any]:
    prompt = make_integrator_prompt(cycle, candidate, review_path, audit_path)
    prompt_path = SPRINT / "briefs" / f"cycle_{cycle:02d}_codex_integrator_prompt.md"
    out_path = SPRINT / "lanes" / "integrator" / f"PUBLISHABLE_9PDFS_INTEGRATOR_CYCLE_{cycle:02d}.log"
    write_text(prompt_path, prompt)
    cmd = [str(CODEX), "exec", "-m", "gpt-5.4-mini", "--sandbox", "workspace-write", "--cd", str(candidate), "--skip-git-repo-check", prompt]
    return run_cmd(f"codex-integrator-9pdf-publishability-cycle-{cycle}", cmd, out_path, timeout, candidate)


def write_board(start_utc: str, target_end_utc: str) -> None:
    lines = [
        "# 9-PDF publishability + Gemini Deep Research loop",
        "",
        f"Marker: `{SPRINT_ID}`",
        f"Start UTC: {start_utc}",
        f"Target end UTC: {target_end_utc}",
        "",
        "## User directive",
        "Make the nine Galaxy Evolution manuscript PDFs publishable. Review resulted PDFs with a Gemini Deep Research reviewer and rerun research/revision cycles until the Deep Research pass gate is met or a hard real-data blocker remains.",
        "",
        "## Inputs",
        f"- integrated 9-paper source root: `{SOURCE_INTEGRATED}`",
        "",
        "## Pass gate",
        "- Gemini deep-research reviewer must output `GEMINI_DEEP_RESEARCH_VERDICT: PASS`.",
        "- All nine candidate TeX files must compile to PDFs with `%PDF` headers.",
        "- Local audit fatal count must be zero.",
        "",
        "## Safety locks",
        *[f"- {x}" for x in SAFETY_LOCKS],
        "",
        "## Real-data policy",
        *[f"- {x}" for x in REAL_DATA_POLICY],
    ]
    write_text(SPRINT / "SPRINT_BOARD.md", "\n".join(lines) + "\n")


def write_final(cycles: List[Dict[str, Any]], latest: Optional[Path], pass_candidate: Optional[Path], start_utc: str, target_end_utc: str) -> None:
    final = {
        "sprint_id": SPRINT_ID,
        "started_utc": start_utc,
        "target_end_utc": target_end_utc,
        "finished_utc": utc_now(),
        "cycles_completed": len(cycles),
        "latest_candidate": str(latest) if latest else None,
        "pass_candidate": str(pass_candidate) if pass_candidate else None,
        "passed": pass_candidate is not None,
        "cycles": cycles,
        "safety_locks": SAFETY_LOCKS,
        "real_data_policy": REAL_DATA_POLICY,
    }
    write_text(SPRINT / "FINAL_9PDF_PUBLISHABILITY_HANDOFF.json", json.dumps(final, indent=2, sort_keys=True))
    lines = [
        "# 9-PDF publishability loop final handoff",
        "",
        f"Marker: `{SPRINT_ID}_FINAL_HANDOFF`",
        f"Passed: `{pass_candidate is not None}`",
        f"Latest candidate: `{latest}`",
        f"Pass candidate: `{pass_candidate}`",
        f"Cycles completed: {len(cycles)}",
        "",
        "## Cycle summary",
    ]
    for c in cycles:
        lines.append(f"- cycle {c['cycle']}: verdict={c.get('review_verdict')} pass_gate={c.get('pass_gate')} candidate=`{c.get('candidate')}`")
    lines += ["", "## Safety", *[f"- {x}" for x in SAFETY_LOCKS]]
    write_text(SPRINT / "FINAL_9PDF_PUBLISHABILITY_HANDOFF.md", "\n".join(lines) + "\n")


def main() -> int:
    SPRINT.mkdir(parents=True, exist_ok=True)
    start_utc = utc_now()
    hard_end = time.time() + DURATION_SECONDS
    target_end_utc = dt.datetime.fromtimestamp(hard_end, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    write_board(start_utc, target_end_utc)
    update_status(state="running", pid=os.getpid(), started_utc=start_utc, target_end_utc=target_end_utc, source_integrated=str(SOURCE_INTEGRATED), max_cycles=MAX_CYCLES)
    ledger("sprint started")

    if not SOURCE_INTEGRATED.exists():
        update_status(state="blocked", blocker=f"missing source root {SOURCE_INTEGRATED}")
        ledger(f"BLOCKED missing source root {SOURCE_INTEGRATED}")
        return 2
    if not AGY.exists():
        update_status(state="blocked", blocker=f"missing agy CLI {AGY}")
        ledger(f"BLOCKED missing agy CLI {AGY}")
        return 2
    if not CODEX.exists():
        update_status(state="blocked", blocker=f"missing codex CLI {CODEX}")
        ledger(f"BLOCKED missing codex CLI {CODEX}")
        return 2

    cycles: List[Dict[str, Any]] = []
    source_for_copy = SOURCE_INTEGRATED
    latest: Optional[Path] = None
    pass_candidate: Optional[Path] = None
    previous_audit_path: Optional[Path] = None

    for cycle in range(1, MAX_CYCLES + 1):
        if time.time() + MIN_REMAINING_SECONDS > hard_end:
            ledger("stopping before next cycle: target window nearly exhausted")
            break
        candidate = copy_source_to_candidate(cycle, source_for_copy)
        latest = candidate
        update_status(state="cycle_running", cycle=cycle, candidate=str(candidate))
        ledger(f"cycle {cycle}: candidate copied from {source_for_copy} to {candidate}")

        inventory = build_inventory(cycle, candidate)
        ledger(f"cycle {cycle}: inventory papers={inventory['counts']['papers']} existing_pdfs={inventory['counts']['existing_pdfs']}")

        review_timeout = min(REVIEW_TIMEOUT, max(120, int(hard_end - time.time())))
        review_result = run_deep_review(cycle, candidate, inventory, review_timeout)
        review_path = Path(review_result["output_path"])
        review_verdict = verdict_from_report(review_path)
        ledger(f"cycle {cycle}: Gemini deep-research review exit={review_result.get('exit_code')} verdict={review_verdict}")

        compile_results = [compile_tex(tex) for tex in paper_tex_paths(candidate)]
        audit = local_audit(cycle, candidate, review_verdict, compile_results)
        previous_audit_path = candidate / f"CYCLE_{cycle:02d}_PUBLISHABILITY_AUDIT.md"
        summary = {"cycle": cycle, "candidate": str(candidate), "review_result": review_result, "review_verdict": review_verdict, "compile_ok": [r.get("ok") for r in compile_results], "pass_gate": audit["pass_gate"], "fatal_failures": len(audit["fatal_failures"]), "finished_review_utc": utc_now()}
        cycles.append(summary)
        write_text(candidate / f"CYCLE_{cycle:02d}_SUMMARY.json", json.dumps(summary, indent=2, sort_keys=True))
        write_text(candidate / f"CYCLE_{cycle:02d}_SUMMARY.md", f"# Cycle {cycle} summary\n\nMarker: `PUBLISHABLE_9PDFS_CYCLE_{cycle:02d}_SUMMARY`\n\n- verdict: `{review_verdict}`\n- pass_gate: `{audit['pass_gate']}`\n- fatal_failures: `{len(audit['fatal_failures'])}`\n- compile_ok: `{[r.get('ok') for r in compile_results]}`\n- candidate: `{candidate}`\n")
        update_status(cycles_completed=cycle - 1, latest_candidate=str(candidate), latest_review_verdict=review_verdict, latest_pass_gate=audit["pass_gate"])

        if audit["pass_gate"]:
            pass_candidate = candidate
            ledger(f"cycle {cycle}: PASS gate reached")
            update_status(state="passed", cycles_completed=cycle, pass_candidate=str(candidate), latest_candidate=str(candidate))
            break

        if time.time() + MIN_REMAINING_SECONDS > hard_end:
            ledger(f"cycle {cycle}: no time left for integrator/new cycle")
            break

        integ_timeout = min(INTEGRATOR_TIMEOUT, max(120, int(hard_end - time.time())))
        integ_result = run_integrator(cycle, candidate, review_path, previous_audit_path, integ_timeout)
        summary["integrator_result"] = integ_result
        write_text(candidate / f"CYCLE_{cycle:02d}_SUMMARY.json", json.dumps(summary, indent=2, sort_keys=True))
        ledger(f"cycle {cycle}: integrator exit={integ_result.get('exit_code')}; revised candidate will feed next cycle")
        source_for_copy = candidate
        update_status(cycles_completed=cycle, latest_candidate=str(candidate), latest_integrator_exit=integ_result.get("exit_code"))

    if pass_candidate is None:
        update_status(state="stopped_without_pass", cycles_completed=len(cycles), latest_candidate=str(latest) if latest else None)
        ledger("stopped without Gemini Deep Research PASS")
    write_final(cycles, latest, pass_candidate, start_utc, target_end_utc)
    return 0 if pass_candidate is not None else 3


if __name__ == "__main__":
    raise SystemExit(main())
