#!/usr/bin/env python3
"""Deep-Research-gated publishability loop for the 9 Galaxy Evolution PDFs.

Local/candidate-only. It never edits public roots, product DB/API/wiki/trust,
deploys/restarts, git history, cron, credentials, billing, or submission systems.

Loop contract:
1. Copy the integrated 9-paper source package into a cycle candidate.
2. Compile the 9 PDFs.
3. Ask the Gemini Deep Research lane for a strict all-9 publishability verdict.
4. If any paper fails, run a candidate-only integrator over the 9 TeX files.
5. Repeat from the resulting PDFs until Deep Research returns PASS or the bounded
   local run budget expires.
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
from typing import Any, Dict, List, Tuple

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTO = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
SOURCE_ROOT = AUTO / "integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z"
RUN_ID = os.environ.get("NEBULAMIND_PUBLISHABLE_9PDF_RUN_ID", "PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260710T000000Z")
RUN_ROOT = AUTO / "publishability-loops" / RUN_ID

MAX_CYCLES = int(os.environ.get("NEBULAMIND_PUBLISHABLE_9PDF_MAX_CYCLES", "30"))
MAX_SECONDS = int(os.environ.get("NEBULAMIND_PUBLISHABLE_9PDF_SECONDS", str(18 * 60 * 60)))
MIN_REMAINING_FOR_NEW_CYCLE = 35 * 60
REVIEW_TIMEOUT = int(os.environ.get("NEBULAMIND_PUBLISHABLE_9PDF_REVIEW_TIMEOUT", str(2 * 60 * 60)))
INTEGRATOR_TIMEOUT = int(os.environ.get("NEBULAMIND_PUBLISHABLE_9PDF_INTEGRATOR_TIMEOUT", str(90 * 60)))

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

REAL_DATA_RULES = [
    "Never introduce mock, synthetic, fake, placeholder, or toy data.",
    "Never invent numbers, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, figures, tables, or result values.",
    "New quantitative claims must be traceable to existing real local SDSS artifacts or checkable public sources.",
    "If a needed datum is absent, write 'not measured here' or 'requires future real data' instead of filling it in.",
    "For the 8 proxy/denominator papers, publishability means an honest observational data note, not a causal feedback result.",
]

SAFETY_LOCKS = [
    "write only under this publishability loop directory and copied candidate packages",
    "no public page or public-linked PDF replacement",
    "no product DB, SQL, /api/pages, page_versions, wiki publish, trust recompute, or data mutation",
    "no deploy/restart",
    "no git commit/push/merge/rebase/history rewrite",
    "no cron creation/update",
    "no billing/cloud/OAuth/API-key/account changes and no credential/token/cookie reads",
    "no external manuscript submission",
]


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def append(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(text)


def read_text(path: Path, limit: int | None = None) -> str:
    if not path.exists():
        return f"[MISSING {path}]"
    text = path.read_text(errors="replace")
    if limit is not None and len(text) > limit:
        return text[:limit] + f"\n[TRUNCATED at {limit} chars from {path}]\n"
    return text


def compact(text: str, limit: int = 900) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[:limit] + " ..."


def ledger(line: str) -> None:
    append(RUN_ROOT / "PUBLISHABILITY_LEDGER.md", f"- {utc_now()} — {line}\n")


def status(**kwargs: Any) -> None:
    path = RUN_ROOT / "PUBLISHABILITY_STATUS.json"
    data: Dict[str, Any] = {}
    if path.exists():
        try:
            data = json.loads(path.read_text())
        except Exception:
            data = {}
    data.update(kwargs)
    data["updated_utc"] = utc_now()
    write_text(path, json.dumps(data, indent=2, sort_keys=True))


def run_cmd(label: str, args: List[str], out_path: Path, timeout_s: int, cwd: Path) -> Dict[str, Any]:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    started = utc_now()
    append(out_path, f"# {label}\nStarted UTC: {started}\nCWD: {cwd}\nCommand head: {args[:8]}\n\n")
    t0 = time.time()
    env = os.environ.copy()
    env.setdefault("NO_COLOR", "1")
    env.setdefault("CLICOLOR", "0")
    try:
        proc = subprocess.run(args, cwd=str(cwd), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout_s, env=env)
        output = proc.stdout or ""
        rc = proc.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        raw = exc.stdout
        output = raw.decode(errors="replace") if isinstance(raw, bytes) else (raw or "")
        output += f"\n\n[TIMEOUT after {timeout_s}s]\n"
        rc = 124
        timed_out = True
    except Exception as exc:
        output = f"[EXCEPTION] {type(exc).__name__}: {exc}\n"
        rc = 125
        timed_out = False
    elapsed = round(time.time() - t0, 1)
    append(out_path, output)
    append(out_path, f"\n\n# command_result\nexit_code={rc}\nelapsed_s={elapsed}\ntimed_out={timed_out}\nfinished_utc={utc_now()}\n")
    return {"label": label, "exit_code": rc, "elapsed_s": elapsed, "timed_out": timed_out, "output_path": str(out_path)}


def paper_tex_paths(candidate: Path) -> List[Path]:
    paths: List[Path] = []
    for d in PAPER_DIRS:
        matches = sorted((candidate / d / "aastex").glob("*_integrated.tex"))
        if matches:
            paths.append(matches[0])
    return paths


def title_and_abstract(tex: Path) -> Dict[str, str]:
    text = read_text(tex, 80000)
    title = "[missing title]"
    abstract = "[missing abstract]"
    m = re.search(r"\\title(?:\[[^\]]*\])?\{(.+?)\}", text, re.S)
    if m:
        title = compact(m.group(1), 260)
    m = re.search(r"\\begin\{abstract\}(.+?)\\end\{abstract\}", text, re.S)
    if m:
        abstract = compact(m.group(1), 1200)
    return {"title": title, "abstract": abstract}


def compile_one(tex: Path) -> Dict[str, Any]:
    pdf = tex.with_suffix(".pdf")
    log = tex.with_suffix(".publishability.compile.log")
    if pdf.exists():
        pdf.unlink()
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
    fatal_markers = [m for m in ["error:", "fatal", "emergency stop", "halted"] if m in out.lower()]
    return {
        "tex": str(tex),
        "pdf": str(pdf),
        "ok": rc == 0 and pdf.exists() and header == "%PDF" and not fatal_markers,
        "returncode": rc,
        "pdf_bytes": pdf.stat().st_size if pdf.exists() else 0,
        "pdf_sha256": sha256(pdf) if pdf.exists() else None,
        "header": header,
        "log": str(log),
        "fatal_markers": fatal_markers,
    }


def compile_all(candidate: Path, cycle: int) -> List[Dict[str, Any]]:
    results = [compile_one(tex) for tex in paper_tex_paths(candidate)]
    write_text(candidate / f"CYCLE_{cycle:02d}_COMPILE_RECEIPT.json", json.dumps(results, indent=2, sort_keys=True))
    lines = [f"# Cycle {cycle} compile receipt", "", f"Created UTC: {utc_now()}", ""]
    for r in results:
        lines.append(f"- `{Path(r['tex']).parent.parent.name}` ok={r['ok']} bytes={r['pdf_bytes']} sha256={r['pdf_sha256']} markers={r['fatal_markers']}")
    write_text(candidate / f"CYCLE_{cycle:02d}_COMPILE_RECEIPT.md", "\n".join(lines) + "\n")
    return results


def forbidden_data_hits(candidate: Path) -> List[Dict[str, str]]:
    pats = [
        re.compile(r"\b(?:mock|synthetic|fake|placeholder|toy) data\b", re.I),
        re.compile(r"\b(?:invented|fabricated) (?:number|citation|data|result)s?\b", re.I),
    ]
    hits: List[Dict[str, str]] = []
    for tex in paper_tex_paths(candidate):
        text = read_text(tex)
        for pat in pats:
            for m in pat.finditer(text):
                snip = compact(text[max(0, m.start() - 120):m.end() + 160], 300)
                # Allow explicit prohibitions/safety statements, but still surface them for reviewer context.
                hits.append({"tex": str(tex), "pattern": pat.pattern, "snippet": snip})
    return hits[:100]


def build_candidate(source: Path, cycle: int) -> Path:
    candidate = RUN_ROOT / "candidates" / f"cycle_{cycle:02d}_nine_papers"
    if candidate.exists():
        shutil.rmtree(candidate)
    candidate.mkdir(parents=True, exist_ok=True)
    for d in PAPER_DIRS:
        shutil.copytree(source / d, candidate / d)
    write_text(candidate / "SOURCE_COPY.json", json.dumps({"cycle": cycle, "source": str(source), "copied_utc": utc_now(), "paper_dirs": PAPER_DIRS}, indent=2))
    return candidate


def summarize_candidate(candidate: Path, compile_results: List[Dict[str, Any]], cycle: int) -> str:
    pieces = [
        f"Candidate root: {candidate}",
        f"Cycle: {cycle}",
        "",
        "Safety locks:",
        "\n".join(f"- {x}" for x in SAFETY_LOCKS),
        "",
        "Real-data rules:",
        "\n".join(f"- {x}" for x in REAL_DATA_RULES),
        "",
        "Compiled PDF receipts:",
        json.dumps(compile_results, indent=2)[:12000],
        "",
        "Papers:",
    ]
    for i, tex in enumerate(paper_tex_paths(candidate), 1):
        meta = title_and_abstract(tex)
        pieces.append(f"{i}. slug={tex.parent.parent.name}\n   tex={tex}\n   pdf={tex.with_suffix('.pdf')}\n   title={meta['title']}\n   abstract={meta['abstract']}\n")
    pieces.append("\nCurrent key excerpts:")
    for tex in paper_tex_paths(candidate):
        pieces.append(f"\n===== {tex.parent.parent.name} {tex.name} =====\n" + read_text(tex, 6500))
    return "\n".join(pieces)


def deep_research_prompt(candidate: Path, compile_results: List[Dict[str, Any]], cycle: int, previous_review: str | None = None) -> str:
    prev = f"\nPrevious Deep Research review to re-check after integration:\n{previous_review[:20000]}\n" if previous_review else ""
    return f"""You are the Gemini Deep Research publication gate for the NebulaMind Galaxy Evolution 9-PDF package.

Use deep-research-style source scrutiny and astronomy-journal standards. Work strictly read-only.

Output marker: PUBLISHABLE_9PDF_GEMINI_DEEP_RESEARCH_CYCLE_{cycle:02d}

FIRST LINE MUST BE EXACTLY ONE OF:
DEEP_RESEARCH_PASS: YES
DEEP_RESEARCH_PASS: NO

Pass only if ALL NINE compiled PDFs are publishable as honest AAS-style draft papers/data notes, with no blocker or major issue remaining. For the 8 non-flagship papers, accept them as publishable only if they are clearly framed as selection-aware SDSS observational denominator/proxy data notes, not as causal feedback papers. Do not require impossible new radio/X-ray/CO/HI/morphology/environment/outflow/simulation data for pass; require that absent data are honestly described as future real-data requirements.

Required review output after the first line:
1. Per-paper verdict for all 9 papers: PASS/FAIL plus blocker/major/minor issues.
2. Exact issue text and exact safe replacement guidance where possible.
3. Citation/source audit: any citation that is wrong, unverifiable, or role-misclassified.
4. Real-data audit: confirm no mock/synthetic/fake/placeholder/toy data and no invented values.
5. Publishability action list ranked by severity.
6. Safety ledger: read-only, no files edited, no public roots, no DB/API/wiki/trust/deploy/git/cron/billing/OAuth/submission.

Hard rules:
- Never invent citations, identifiers, numbers, sample sizes, or facts.
- If a source/data value is not verifiable from the manuscript or known public metadata, mark it unverified/do-not-integrate.
- Keep RP-1 association-only; keep the 8 proxy papers honest denominator/proxy/data-note drafts.
- Review the local TeX/PDF paths in the candidate package if available; they are local candidate artifacts, not public products.
{prev}

Context follows:
{summarize_candidate(candidate, compile_results, cycle)}
"""


def parse_pass(review_text: str) -> bool:
    for line in review_text.splitlines()[:20]:
        m = re.match(r"\s*DEEP_RESEARCH_PASS:\s*(YES|NO)\s*$", line, re.I)
        if m:
            return m.group(1).upper() == "YES"
    return False


def integrator_prompt(candidate: Path, cycle: int, review_text: str, compile_results: List[Dict[str, Any]]) -> str:
    tex_list = "\n".join(f"- {p}" for p in paper_tex_paths(candidate))
    return f"""You are the candidate-only integrator for the NebulaMind Galaxy Evolution 9-PDF publishability loop.

Working root: {candidate}
Output marker: PUBLISHABLE_9PDF_INTEGRATOR_CYCLE_{cycle:02d}

You may edit ONLY these 9 local candidate TeX files:
{tex_list}

You may write only this response file:
- {candidate / f'CYCLE_{cycle:02d}_INTEGRATOR_RESPONSE.md'}

Goal: address the Gemini Deep Research publication-gate issues so the next review can pass all 9 PDFs.

Required safe transformations:
- Remove process/meta wording like "local-only integration", "No public page", "generated by autopilot", or "not part of this run" from abstracts/results/conclusions unless it belongs in a brief reproducibility note.
- Convert each paper into an AAS-style draft/data note: scientific abstract, purpose, data/selection, result, limitations, reproducibility/data availability, conclusion.
- Preserve exact measured numbers and denominators; do not invent new values.
- Preserve the RP-1 association-only boundary.
- For papers 2-9, frame them as honest SDSS optical denominator/proxy observational notes, not causal physical-feedback claims.
- Keep absent radio/X-ray/CO/HI/morphology/environment/outflow/simulation data as future real-data requirements.
- Keep all TeX compilable; do not change figure paths unless absolutely required and already present.
- Add or alter citations only if already present in the file/package or provided by Gemini with checkable identifier. Do not invent bibitems.

Forbidden:
- No edits outside {candidate}.
- No public/live roots, no DB/API/wiki/trust/deploy/git/cron/billing/OAuth/submission.
- No credential reads.
- No mock/synthetic/fake/placeholder/toy data.

Compile receipt before integration:
{json.dumps(compile_results, indent=2)[:12000]}

Gemini Deep Research review to fix:
{review_text[:65000]}
"""


def audit_cycle(candidate: Path, cycle: int, compile_results: List[Dict[str, Any]], review_text: str, passed: bool) -> Dict[str, Any]:
    hits = forbidden_data_hits(candidate)
    audit = {
        "cycle": cycle,
        "candidate": str(candidate),
        "created_utc": utc_now(),
        "deep_research_pass": passed,
        "compile_all_ok": len(compile_results) == 9 and all(r.get("ok") for r in compile_results),
        "compile_results": compile_results,
        "forbidden_data_hits": hits,
        "fatal_failures": [],
    }
    if not audit["compile_all_ok"]:
        audit["fatal_failures"].append("compile_not_all_ok")
    # Hits are surfaced but not automatically fatal because explicit safety statements often contain those words.
    if "DEEP_RESEARCH_PASS: YES" not in review_text.splitlines()[:5] and passed:
        audit["fatal_failures"].append("pass_parse_inconsistent")
    write_text(candidate / f"CYCLE_{cycle:02d}_PUBLISHABILITY_AUDIT.json", json.dumps(audit, indent=2, sort_keys=True))
    md = [f"# Cycle {cycle} publishability audit", "", f"Deep Research pass: {passed}", f"Compile all ok: {audit['compile_all_ok']}", f"Forbidden-data wording hits surfaced: {len(hits)}", f"Fatal failures: {audit['fatal_failures']}", "", "## Safety", *[f"- {x}" for x in SAFETY_LOCKS]]
    write_text(candidate / f"CYCLE_{cycle:02d}_PUBLISHABILITY_AUDIT.md", "\n".join(md) + "\n")
    return audit


def write_final(cycles: List[Dict[str, Any]], latest: Path | None, passed: bool) -> None:
    final = {
        "run_id": RUN_ID,
        "finished_utc": utc_now(),
        "passed": passed,
        "latest_candidate": str(latest) if latest else None,
        "cycles": cycles,
        "safety_locks": SAFETY_LOCKS,
    }
    write_text(RUN_ROOT / "FINAL_PUBLISHABILITY_HANDOFF.json", json.dumps(final, indent=2, sort_keys=True))
    lines = [
        "# 9-PDF Deep Research publishability loop final handoff",
        "",
        f"Run ID: `{RUN_ID}`",
        f"Finished UTC: {utc_now()}",
        f"Deep Research pass achieved: {passed}",
        f"Latest candidate: `{latest}`" if latest else "Latest candidate: none",
        "",
        "## Cycles",
    ]
    for c in cycles:
        lines.append(f"- cycle {c.get('cycle')}: pass={c.get('deep_research_pass')} candidate=`{c.get('candidate')}` review=`{c.get('review_path')}`")
    if latest:
        lines += ["", "## Latest PDFs"]
        for tex in paper_tex_paths(latest):
            pdf = tex.with_suffix(".pdf")
            lines.append(f"- `{pdf}` exists={pdf.exists()} sha256={sha256(pdf) if pdf.exists() else None}")
    lines += ["", "## Safety", *[f"- {x}" for x in SAFETY_LOCKS], "", "No public PDF replacement/publish or external submission was performed."]
    write_text(RUN_ROOT / "FINAL_PUBLISHABILITY_HANDOFF.md", "\n".join(lines) + "\n")
    status(state="completed_pass" if passed else "completed_no_pass", passed=passed, latest_candidate=str(latest) if latest else None, final_handoff=str(RUN_ROOT / "FINAL_PUBLISHABILITY_HANDOFF.md"), cycles_completed=len(cycles))


def main() -> int:
    RUN_ROOT.mkdir(parents=True, exist_ok=True)
    write_text(RUN_ROOT / "RUNNING.pid", str(os.getpid()) + "\n")
    start = utc_now()
    end_ts = time.time() + MAX_SECONDS
    status(state="starting", pid=os.getpid(), started_utc=start, source_root=str(SOURCE_ROOT), max_cycles=MAX_CYCLES, max_seconds=MAX_SECONDS)
    ledger("publishability loop started")
    write_text(RUN_ROOT / "OPERATING_CONTRACT.md", "\n".join(["# Operating contract", "", "## Real-data rules", *[f"- {x}" for x in REAL_DATA_RULES], "", "## Safety locks", *[f"- {x}" for x in SAFETY_LOCKS]]) + "\n")

    source = SOURCE_ROOT
    cycles: List[Dict[str, Any]] = []
    latest: Path | None = None
    previous_review: str | None = None
    passed = False

    for cycle in range(1, MAX_CYCLES + 1):
        if time.time() + MIN_REMAINING_FOR_NEW_CYCLE >= end_ts:
            ledger(f"stopping before cycle {cycle}: not enough bounded runtime remaining")
            break
        candidate = build_candidate(source, cycle)
        latest = candidate
        status(state="cycle_running", cycle=cycle, candidate=str(candidate), cycles_completed=len(cycles))
        ledger(f"cycle {cycle}: candidate copied from {source} to {candidate}")

        compile_results = compile_all(candidate, cycle)
        ledger(f"cycle {cycle}: compiled {sum(1 for r in compile_results if r.get('ok'))}/{len(compile_results)} PDFs")

        review_prompt = deep_research_prompt(candidate, compile_results, cycle, previous_review)
        review_prompt_path = RUN_ROOT / "briefs" / f"cycle_{cycle:02d}_gemini_deep_research_prompt.md"
        write_text(review_prompt_path, review_prompt)
        review_path = RUN_ROOT / "lanes/gemini_deep_research" / f"PUBLISHABLE_9PDF_GEMINI_DEEP_RESEARCH_CYCLE_{cycle:02d}.md"
        review_result = run_cmd(
            f"gemini-deep-research-publishability-cycle-{cycle}",
            ["agy", "--model", "Gemini 3.1 Pro (High)", "--mode", "plan", "--print-timeout", "120m0s", "--print", review_prompt],
            review_path,
            min(REVIEW_TIMEOUT, int(max(60, end_ts - time.time()))),
            REPO,
        )
        review_text = read_text(review_path)
        previous_review = review_text
        passed = parse_pass(review_text)
        audit = audit_cycle(candidate, cycle, compile_results, review_text, passed)
        cycles.append({"cycle": cycle, "candidate": str(candidate), "review_path": str(review_path), "review_result": review_result, "deep_research_pass": passed, "audit": audit})
        ledger(f"cycle {cycle}: Gemini Deep Research pass={passed} exit={review_result.get('exit_code')}")
        if passed:
            break

        integ_prompt = integrator_prompt(candidate, cycle, review_text, compile_results)
        write_text(RUN_ROOT / "briefs" / f"cycle_{cycle:02d}_integrator_prompt.md", integ_prompt)
        integ_path = RUN_ROOT / "lanes/integrator" / f"PUBLISHABLE_9PDF_INTEGRATOR_CYCLE_{cycle:02d}.log"
        integ_result = run_cmd(
            f"codex-integrator-publishable-9pdf-cycle-{cycle}",
            ["codex", "exec", "-m", "gpt-5.4-mini", "--sandbox", "workspace-write", "--cd", str(candidate), "--skip-git-repo-check", integ_prompt],
            integ_path,
            min(INTEGRATOR_TIMEOUT, int(max(60, end_ts - time.time()))),
            candidate,
        )
        cycles[-1]["integrator_result"] = integ_result
        ledger(f"cycle {cycle}: integrator exit={integ_result.get('exit_code')}")
        # Use the edited candidate as the source for the next Deep Research review.
        source = candidate
        status(state="between_cycles", cycle=cycle, candidate=str(candidate), cycles_completed=len(cycles), latest_review=str(review_path), latest_integrator=str(integ_path), latest_pass=passed)

    write_final(cycles, latest, passed)
    ledger(f"publishability loop completed pass={passed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
