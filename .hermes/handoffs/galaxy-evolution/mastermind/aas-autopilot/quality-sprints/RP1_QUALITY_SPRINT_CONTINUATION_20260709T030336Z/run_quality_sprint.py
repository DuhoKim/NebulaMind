#!/usr/bin/env python3
"""Four-hour local-only RP-1 paper quality sprint.

This orchestrator uses low-usage subscription-backed lanes where available:
- AGY/Antigravity Gemini 3.1 Pro (Low) for Hwao-style director review.
- AGY/Antigravity Gemini 3.5 Flash (Low) for Gemini/Goru deep-review-style critique.
- Codex gpt-5.4-mini for Kun-style reproducibility/prose/TeX critique and local candidate edits.
- Local Python mechanical audit for figures, phrases, TeX, and PDF receipts.

Safety: writes only under the sprint directory and candidate copies of the existing local package.
It does not touch public pages, live roots, DB/API/wiki/trust/deploy/git/cron/billing/OAuth,
or external submission systems.
"""
from __future__ import annotations

import concurrent.futures
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
from typing import Any, Dict, List, Tuple

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTOPILOT = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
SOURCE_RUN = AUTOPILOT / "quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z"
SOURCE_PACKAGE = SOURCE_RUN / "candidates/cycle_08_package"
SPRINT_ID = "RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z"
SPRINT = AUTOPILOT / "quality-sprints" / SPRINT_ID
DURATION_SECONDS = 4 * 60 * 60
TARGET_END_UTC = "2026-07-09T06:11:24Z"
MAX_CYCLES = 64
MIN_REMAINING_FOR_NEW_CYCLE = 20 * 60
PER_LANE_TIMEOUT = 45 * 60
INTEGRATOR_TIMEOUT = 55 * 60

FLAGSHIP_REL = Path("flagship_rp1/aastex/rp1_flagship_polished.tex")
SUPPLEMENT_REL = Path("supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex")

LOCKS = [
    "no public pages or live roots",
    "no public PDF replacement",
    "no database, SQL, /api/pages, page_versions, wiki publish, or trust recompute",
    "no deploy/restart",
    "no git commit/push/merge/rebase",
    "no cron creation/update",
    "no billing/cloud/OAuth/API-key/account changes",
    "no external manuscript submission",
    "no credential/token/cookie reads",
]

REQUIRED_FLAGSHIP_PHRASES = [
    "association",
    "not a causal",
    "capped",
    "non-random",
    "24.0",
    "S/N$\\geq10$",
]
REQUIRED_SUPPLEMENT_PHRASES = [
    "denominator/proxy",
    "not as independent causal",
    "radio",
    "X-ray",
    "CO/HI",
    "simulation",
]
NUMERIC_INVARIANTS = [
    "8,146",
    "-1.309",
    "[-1.334,-1.283]",
    "249,917",
    "60,000",
    "24.0",
]


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def kst_now() -> str:
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S KST")


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(SPRINT))
    except Exception:
        return str(p)


def sha256(path: Path) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text(path: Path, limit: int | None = None) -> str:
    if not path.exists():
        return f"[MISSING: {path}]"
    text = path.read_text(errors="replace")
    if limit and len(text) > limit:
        return text[:limit] + f"\n\n[TRUNCATED at {limit} chars from {path}]\n"
    return text


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def append(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(text)


def ledger(line: str) -> None:
    append(SPRINT / "SPRINT_LEDGER.md", f"- {utc_now()} / {kst_now()} — {line}\n")


def update_status(**kwargs: Any) -> None:
    status_path = SPRINT / "SPRINT_STATUS.json"
    current: Dict[str, Any] = {}
    if status_path.exists():
        try:
            current = json.loads(status_path.read_text())
        except Exception:
            current = {}
    current.update(kwargs)
    current["updated_utc"] = utc_now()
    write_text(status_path, json.dumps(current, indent=2, sort_keys=True))


def prepare_static_files(start_utc: str, end_utc: str) -> None:
    for d in ["briefs", "lanes/hwao", "lanes/gemini_deep", "lanes/codex_kun", "lanes/goru_mech", "lanes/integrator", "candidates", "logs"]:
        (SPRINT / d).mkdir(parents=True, exist_ok=True)
    board = f"""# RP-1 four-hour local quality sprint

Marker: `{SPRINT_ID}`

Start UTC: {start_utc}
Target end UTC: {end_utc}
Start KST: {kst_now()}
Duration: about 4 hours

## User directive

Let the autopilots that worked on the Galaxy Evolution papers keep working on the two-PDF package to increase quality, following Gemini/deep-research-style and/or Hwao review results, while leveraging low-usage models.

## Source package

`{SOURCE_PACKAGE}`

Inputs:

- polished RP-1 flagship paper
- supplementary denominator/proxy atlas
- package audit and final handoff

## Lane roles

- Hwao-style director lane: AGY/Antigravity `Gemini 3.1 Pro (Low)`, publication/readiness triage.
- Gemini/Goru deep-review-style lane: AGY/Antigravity `Gemini 3.5 Flash (Low)`, science guardrails, missing observables, citation-role critique.
- Codex/Kun lane: Codex `gpt-5.4-mini`, read-only reproducibility/prose/TeX critique and candidate-only integration edits.
- Goru mechanical lane: local Python checks for phrases, figures, PDFs, logs, and unchanged numeric invariants.
- Tori integrator lane: this orchestrator copies the package into cycle-local candidate directories, applies only local candidate edits, compiles, audits, and writes receipts.

## Single-writer rule

Reviewer lanes write reports only. The integrator lane may edit only candidate copies under this sprint directory. The original decision package and public-linked artifacts are not edited.

## Safety locks

""" + "\n".join(f"- {x}" for x in LOCKS) + "\n"
    write_text(SPRINT / "SPRINT_BOARD.md", board)
    write_text(SPRINT / "INPUTS.json", json.dumps({
        "sprint_id": SPRINT_ID,
        "source_package": str(SOURCE_PACKAGE),
        "source_run": str(SOURCE_RUN),
        "flagship_tex": str(SOURCE_PACKAGE / FLAGSHIP_REL),
        "supplement_tex": str(SOURCE_PACKAGE / SUPPLEMENT_REL),
        "safety_locks": LOCKS,
        "start_utc": start_utc,
        "target_end_utc": end_utc,
    }, indent=2, sort_keys=True))


def command_exists(name: str) -> bool:
    return shutil.which(name) is not None


def run_cmd(label: str, args: List[str], out_path: Path, timeout_s: int, cwd: Path = REPO) -> Dict[str, Any]:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    meta = {
        "label": label,
        "command_head": args[:5],
        "cwd": str(cwd),
        "started_utc": utc_now(),
        "timeout_s": timeout_s,
    }
    append(out_path, f"# {label}\nStarted UTC: {meta['started_utc']}\nCWD: {cwd}\n\n")
    env = os.environ.copy()
    env.setdefault("NO_COLOR", "1")
    env.setdefault("CLICOLOR", "0")
    t0 = time.time()
    try:
        proc = subprocess.run(
            args,
            cwd=str(cwd),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout_s,
            env=env,
        )
        output = proc.stdout or ""
        rc = proc.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        raw_timeout_output = exc.stdout
        if isinstance(raw_timeout_output, bytes):
            output = raw_timeout_output.decode(errors="replace")
        elif isinstance(raw_timeout_output, str):
            output = raw_timeout_output
        else:
            output = ""
        output += f"\n\n[TIMEOUT after {timeout_s}s]\n"
        rc = 124
        timed_out = True
    except Exception as exc:  # noqa: BLE001
        output = f"[EXCEPTION] {type(exc).__name__}: {exc}\n"
        rc = 125
        timed_out = False
    elapsed = time.time() - t0
    append(out_path, output)
    append(out_path, f"\n\n# command_result\nexit_code={rc}\nelapsed_s={elapsed:.1f}\ntimed_out={timed_out}\nfinished_utc={utc_now()}\n")
    meta.update({"exit_code": rc, "elapsed_s": round(elapsed, 1), "timed_out": timed_out, "finished_utc": utc_now(), "output_path": str(out_path)})
    return meta


def make_snapshot(candidate: Path) -> str:
    pieces = []
    for name, path, limit in [
        ("FINAL_HANDOFF", candidate / "FINAL_HANDOFF.md", 9000),
        ("PACKAGE_AUDIT", candidate / "PACKAGE_AUDIT.md", 3000),
        ("FLAGSHIP_TEX", candidate / FLAGSHIP_REL, 22000),
        ("SUPPLEMENT_TEX", candidate / SUPPLEMENT_REL, 30000),
    ]:
        pieces.append(f"\n\n===== {name}: {path} =====\n" + read_text(path, limit))
    return "".join(pieces)


def make_hwao_prompt(cycle: int, candidate: Path) -> str:
    return f"""You are the Hwao/Fable director lane for NebulaMind paper quality work.

Task: Review the current local two-PDF Galaxy Evolution package and produce a prioritized quality plan for the next integrator pass.

Cycle: {cycle}
Candidate root: {candidate}

Safety: read-only review. Do not edit files. Do not request credentials. Do not publish, deploy, commit, restart, write DB/API/wiki, or touch public pages. Treat this as local manuscript review only.

Output requirements:
- Start with marker `HWAO_QUALITY_REVIEW_CYCLE_{cycle:02d}`.
- Give a publication-readiness verdict for RP-1 and for the supplement.
- List the top 10 concrete improvements, ranked by effect on scientific quality.
- Separate "must fix before public", "nice local polish", and "needs new data".
- Preserve the association-only claim boundary and the numeric results.
- Tell the integrator exactly what wording/section changes are safe.
- End with a safety ledger.

Important science boundary:
RP-1 may claim an optical BPT classification association with catalog sSFR in a capped SDSS denominator. It must not claim causal AGN feedback, molecular gas depletion, radio-mode maintenance heating, outflow escape/recycling, or simulation validation.

Local package snapshot follows. Use it as evidence; do not invent data.
{make_snapshot(candidate)}
"""


def make_gemini_prompt(cycle: int, candidate: Path) -> str:
    return f"""You are the Gemini/Goru deep-review-style lane for a local astronomy manuscript quality sprint.

Task: Act like a skeptical deep research reviewer, but use only the provided local package text. Identify overclaims, missing observables, citation-role problems, weak caveats, and places where a reader could mistake denominator/proxy notes for physical results.

Cycle: {cycle}
Candidate root: {candidate}

Safety: read-only review. No file edits, no web/API/cloud/billing/account changes, no public publishing, no git. Output only a Markdown report.

Output requirements:
- Start with marker `GEMINI_AGY_DEEP_REVIEW_CYCLE_{cycle:02d}`.
- Give issue severity: blocker / major / minor / optional.
- For each issue, quote or paraphrase the risky sentence and propose safer replacement wording.
- Flag any citations that are being used as method support when they should only be future-data motivation.
- Flag any missing-data claims that need radio, X-ray, CO/HI, resolved outflow, halo/group, morphology, or simulation mocks.
- Rank concrete integrator actions.
- End with safety ledger.

Local package snapshot follows. Use it as evidence; do not invent data.
{make_snapshot(candidate)}
"""


def make_codex_review_prompt(cycle: int, candidate: Path) -> str:
    return f"""Review this local manuscript package in read-only mode.

You are the Codex/Kun reproducibility and TeX/prose lane. Inspect only local files under:
{candidate}

Core files:
- {candidate / FLAGSHIP_REL}
- {candidate / SUPPLEMENT_REL}
- {candidate / 'PACKAGE_AUDIT.md'}
- {candidate / 'FINAL_HANDOFF.md'}

Safety:
- Do not edit files in this review lane.
- Do not run git write commands, deploy, restart, publish, call APIs, read credentials, or touch public/live roots.
- You may read files and run harmless read-only commands if needed.

Output requirements:
- Start with marker CODEX_KUN_REVIEW_CYCLE_{cycle:02d}.
- Report TeX, compile, figure, and reproducibility risks.
- Check for numeric consistency: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage.
- Identify wording that could break the association-only guardrail.
- Give exact safe edit recommendations for the integrator.
- End with safety ledger.
"""


def mechanical_report(cycle: int, candidate: Path, out_path: Path) -> Dict[str, Any]:
    flagship = candidate / FLAGSHIP_REL
    supplement = candidate / SUPPLEMENT_REL
    ftxt = read_text(flagship)
    stxt = read_text(supplement)
    reports: Dict[str, Any] = {
        "cycle": cycle,
        "candidate": str(candidate),
        "flagship_exists": flagship.exists(),
        "supplement_exists": supplement.exists(),
        "flagship_required_missing": [p for p in REQUIRED_FLAGSHIP_PHRASES if p not in ftxt],
        "supplement_required_missing": [p for p in REQUIRED_SUPPLEMENT_PHRASES if p not in stxt],
        "numeric_invariants_missing_flagship": [p for p in NUMERIC_INVARIANTS if p not in ftxt],
        "flagship_includegraphics": ftxt.count("\\includegraphics"),
        "supplement_includegraphics": stxt.count("\\includegraphics"),
        "flagship_caption_count": ftxt.count("\\caption"),
        "supplement_caption_count": stxt.count("\\caption"),
        "suspicious_claims_flagship": [],
        "suspicious_claims_supplement": [],
        "figures": [],
        "pdfs": [],
    }
    suspicious = [
        r"causal AGN feedback",
        r"proves? quenching",
        r"maintenance heating measurement",
        r"outflow escape",
        r"simulation validation/rejection",
        r"molecular gas depletion",
    ]
    for pat in suspicious:
        if re.search(pat, ftxt, flags=re.I):
            reports["suspicious_claims_flagship"].append(pat)
        if re.search(pat, stxt, flags=re.I):
            reports["suspicious_claims_supplement"].append(pat)
    for fig in list((candidate / "flagship_rp1/figures").glob("*.pdf")) + list((candidate / "supplementary_denominator_atlas/figures").glob("*.pdf")):
        reports["figures"].append({"path": str(fig), "bytes": fig.stat().st_size, "sha256": sha256(fig)})
    for pdf in [
        candidate / "flagship_rp1/aastex/rp1_flagship_polished.pdf",
        candidate / "supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf",
    ]:
        header = ""
        if pdf.exists():
            header = pdf.open("rb").read(4).decode(errors="replace")
        reports["pdfs"].append({"path": str(pdf), "exists": pdf.exists(), "bytes": pdf.stat().st_size if pdf.exists() else 0, "header": header, "sha256": sha256(pdf)})
    md = [
        f"# Goru mechanical report cycle {cycle}",
        "",
        f"Marker: `GORU_MECHANICAL_REPORT_CYCLE_{cycle:02d}`",
        "",
        "## Counts",
        f"- flagship includegraphics: {reports['flagship_includegraphics']}",
        f"- supplement includegraphics: {reports['supplement_includegraphics']}",
        f"- flagship captions: {reports['flagship_caption_count']}",
        f"- supplement captions: {reports['supplement_caption_count']}",
        f"- figures found: {len(reports['figures'])}",
        "",
        "## Missing required phrases",
        f"- flagship: {reports['flagship_required_missing']}",
        f"- supplement: {reports['supplement_required_missing']}",
        "",
        "## Missing numeric invariants in flagship",
        f"- {reports['numeric_invariants_missing_flagship']}",
        "",
        "## Suspicious claim phrase scan",
        f"- flagship: {reports['suspicious_claims_flagship']}",
        f"- supplement: {reports['suspicious_claims_supplement']}",
        "",
        "## PDF receipts",
    ]
    for p in reports["pdfs"]:
        md.append(f"- {p['path']} exists={p['exists']} bytes={p['bytes']} header={p['header']} sha256={p['sha256']}")
    md += ["", "## Safety", *[f"- {x}" for x in LOCKS]]
    write_text(out_path, "\n".join(md) + "\n")
    write_text(out_path.with_suffix(".json"), json.dumps(reports, indent=2, sort_keys=True))
    return reports


def compile_tex(tex: Path) -> Dict[str, Any]:
    pdf = tex.with_suffix(".pdf")
    log = tex.with_suffix(".quality.compile.log")
    if pdf.exists():
        try:
            pdf.unlink()
        except Exception:
            pass
    if not command_exists("tectonic"):
        write_text(log, "tectonic not found\n")
        return {"tex": str(tex), "pdf": str(pdf), "ok": False, "reason": "tectonic not found", "log": str(log)}
    proc = subprocess.run(["tectonic", tex.name], cwd=str(tex.parent), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=10 * 60)
    write_text(log, proc.stdout or "")
    header = ""
    if pdf.exists():
        header = pdf.open("rb").read(4).decode(errors="replace")
    bad_markers = []
    low = (proc.stdout or "").lower()
    for marker in ["error", "fatal", "halted", "emergency stop"]:
        if marker in low:
            bad_markers.append(marker)
    return {
        "tex": str(tex),
        "pdf": str(pdf),
        "ok": proc.returncode == 0 and pdf.exists() and header == "%PDF" and not bad_markers,
        "returncode": proc.returncode,
        "header": header,
        "pdf_bytes": pdf.stat().st_size if pdf.exists() else 0,
        "sha256": sha256(pdf),
        "log": str(log),
        "bad_markers": bad_markers,
    }


def audit_candidate(cycle: int, candidate: Path, compile_results: List[Dict[str, Any]]) -> Dict[str, Any]:
    ftxt = read_text(candidate / FLAGSHIP_REL)
    stxt = read_text(candidate / SUPPLEMENT_REL)
    audit = {
        "cycle": cycle,
        "candidate": str(candidate),
        "audit_utc": utc_now(),
        "compile_results": compile_results,
        "flagship_required_missing": [p for p in REQUIRED_FLAGSHIP_PHRASES if p not in ftxt],
        "supplement_required_missing": [p for p in REQUIRED_SUPPLEMENT_PHRASES if p not in stxt],
        "numeric_invariants_missing_flagship": [p for p in NUMERIC_INVARIANTS if p not in ftxt],
        "figures": [],
        "fatal_failures": [],
    }
    for fig in list((candidate / "flagship_rp1/figures").glob("*.pdf")) + list((candidate / "supplementary_denominator_atlas/figures").glob("*.pdf")):
        audit["figures"].append({"path": str(fig), "bytes": fig.stat().st_size, "sha256": sha256(fig)})
    for cr in compile_results:
        if not cr.get("ok"):
            audit["fatal_failures"].append(cr)
    if audit["flagship_required_missing"]:
        audit["fatal_failures"].append({"missing_flagship_phrases": audit["flagship_required_missing"]})
    if audit["supplement_required_missing"]:
        audit["fatal_failures"].append({"missing_supplement_phrases": audit["supplement_required_missing"]})
    if audit["numeric_invariants_missing_flagship"]:
        audit["fatal_failures"].append({"missing_numeric_invariants": audit["numeric_invariants_missing_flagship"]})
    write_text(candidate / f"CYCLE_{cycle:02d}_QUALITY_AUDIT.json", json.dumps(audit, indent=2, sort_keys=True))
    md = [
        f"# Cycle {cycle} quality audit",
        "",
        f"Marker: `QUALITY_CYCLE_AUDIT_{cycle:02d}`",
        f"Audit UTC: {audit['audit_utc']}",
        "",
        "## Compile results",
    ]
    for cr in compile_results:
        md.append(f"- {Path(cr['tex']).name}: ok={cr.get('ok')} bytes={cr.get('pdf_bytes')} sha256={cr.get('sha256')} bad_markers={cr.get('bad_markers')}")
    md += [
        "",
        "## Phrase/numeric guards",
        f"- flagship missing required phrases: {audit['flagship_required_missing']}",
        f"- supplement missing required phrases: {audit['supplement_required_missing']}",
        f"- flagship missing numeric invariants: {audit['numeric_invariants_missing_flagship']}",
        "",
        f"Fatal failures: {len(audit['fatal_failures'])}",
    ]
    write_text(candidate / f"CYCLE_{cycle:02d}_QUALITY_AUDIT.md", "\n".join(md) + "\n")
    return audit


def make_integrator_prompt(cycle: int, candidate: Path, report_paths: List[Path]) -> str:
    reports = []
    for p in report_paths:
        reports.append(f"\n\n===== REPORT {p} =====\n" + read_text(p, 22000))
    return f"""You are the Tori/Codex local manuscript integrator for quality cycle {cycle}.

You may edit ONLY these candidate-copy TeX files:
- {candidate / FLAGSHIP_REL}
- {candidate / SUPPLEMENT_REL}

You may also write a concise Markdown response here:
- {candidate / f'CYCLE_{cycle:02d}_REVIEW_RESPONSE.md'}

Forbidden:
- Do not edit the original source package outside this candidate root.
- Do not edit public pages, live roots, DB/API/wiki/trust/deploy/git/cron/billing/OAuth/account settings, or external submission systems.
- Do not change numeric results, table numbers, figure paths, or core claims.
- Do not invent new data or new citations.
- Do not turn denominator/proxy notes into causal physical-feedback claims.

Allowed and desired:
- Apply safe wording improvements from the review reports.
- Improve abstract/intro/conclusion clarity.
- Strengthen association-only and capped-cache caveats.
- Make the supplement read like a coherent atlas rather than eight papers.
- Clarify citation-role separation: SDSS/BPT/catalog for actual methods; radio/X-ray/CO/HI/outflow/simulation papers as future-data motivation.
- Keep TeX compilable.
- Write CYCLE_{cycle:02d}_REVIEW_RESPONSE.md summarizing exactly what you changed and what you refused as needing new data.

Review reports follow.
{''.join(reports)}
"""


def make_fix_prompt(cycle: int, candidate: Path) -> str:
    logs = []
    for p in candidate.glob("*/aastex/*.quality.compile.log"):
        logs.append(f"\n\n===== COMPILE LOG {p} =====\n" + read_text(p, 12000))
    return f"""Fix TeX compile errors only for quality cycle {cycle}.

Edit only:
- {candidate / FLAGSHIP_REL}
- {candidate / SUPPLEMENT_REL}

Do not change numbers, claims, figure paths, citations, or safety wording except as needed for valid TeX escaping. Do not touch public/live/git/DB/deploy/cron/account systems.

Compile logs:
{''.join(logs)}
"""


def run_cycle(cycle: int, source_for_copy: Path, hard_end: float) -> Tuple[Path, Dict[str, Any]]:
    candidate = SPRINT / "candidates" / f"cycle_{cycle:02d}_package"
    if candidate.exists():
        shutil.rmtree(candidate)
    shutil.copytree(source_for_copy, candidate)
    ledger(f"cycle {cycle}: candidate copied from {source_for_copy} to {candidate}")
    update_status(state="cycle_running", cycle=cycle, candidate=str(candidate))

    # Write lane prompts.
    hwao_prompt = make_hwao_prompt(cycle, candidate)
    gemini_prompt = make_gemini_prompt(cycle, candidate)
    codex_prompt = make_codex_review_prompt(cycle, candidate)
    write_text(SPRINT / "briefs" / f"cycle_{cycle:02d}_hwao_prompt.md", hwao_prompt)
    write_text(SPRINT / "briefs" / f"cycle_{cycle:02d}_gemini_agy_prompt.md", gemini_prompt)
    write_text(SPRINT / "briefs" / f"cycle_{cycle:02d}_codex_kun_prompt.md", codex_prompt)

    lane_jobs = []
    report_paths = [
        SPRINT / "lanes/hwao" / f"HWAO_QUALITY_REVIEW_CYCLE_{cycle:02d}.md",
        SPRINT / "lanes/gemini_deep" / f"GEMINI_AGY_DEEP_REVIEW_CYCLE_{cycle:02d}.md",
        SPRINT / "lanes/codex_kun" / f"CODEX_KUN_REVIEW_CYCLE_{cycle:02d}.md",
        SPRINT / "lanes/goru_mech" / f"GORU_MECHANICAL_REPORT_CYCLE_{cycle:02d}.md",
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        lane_jobs.append(ex.submit(run_cmd, f"hwao-agy-cycle-{cycle}", ["agy", "--model", "Gemini 3.1 Pro (Low)", "--mode", "plan", "--print", hwao_prompt], report_paths[0], min(PER_LANE_TIMEOUT, int(max(60, hard_end - time.time()))), REPO))
        lane_jobs.append(ex.submit(run_cmd, f"gemini-agy-deep-cycle-{cycle}", ["agy", "--model", "Gemini 3.5 Flash (Low)", "--mode", "plan", "--print", gemini_prompt], report_paths[1], min(PER_LANE_TIMEOUT, int(max(60, hard_end - time.time()))), REPO))
        lane_jobs.append(ex.submit(run_cmd, f"codex-kun-cycle-{cycle}", ["codex", "exec", "-m", "gpt-5.4-mini", "--sandbox", "read-only", "--cd", str(REPO), codex_prompt], report_paths[2], min(PER_LANE_TIMEOUT, int(max(60, hard_end - time.time()))), REPO))
        lane_results = [f.result() for f in lane_jobs]

    mech = mechanical_report(cycle, candidate, report_paths[3])
    ledger(f"cycle {cycle}: review lanes finished; lane exits {[r.get('exit_code') for r in lane_results]}; mechanical figures={len(mech.get('figures', []))}")

    integrator_prompt = make_integrator_prompt(cycle, candidate, report_paths)
    write_text(SPRINT / "briefs" / f"cycle_{cycle:02d}_integrator_prompt.md", integrator_prompt)
    integ_report = SPRINT / "lanes/integrator" / f"INTEGRATOR_APPLY_CYCLE_{cycle:02d}.log"
    integ_result = run_cmd(
        f"codex-integrator-cycle-{cycle}",
        ["codex", "exec", "-m", "gpt-5.4-mini", "--sandbox", "workspace-write", "--cd", str(REPO), integrator_prompt],
        integ_report,
        min(INTEGRATOR_TIMEOUT, int(max(60, hard_end - time.time()))),
        REPO,
    )
    ledger(f"cycle {cycle}: integrator finished exit={integ_result.get('exit_code')}")

    compile_results = [compile_tex(candidate / FLAGSHIP_REL), compile_tex(candidate / SUPPLEMENT_REL)]
    if any(not r.get("ok") for r in compile_results) and time.time() + 10 * 60 < hard_end:
        ledger(f"cycle {cycle}: compile failed; running one TeX fix pass")
        fix_prompt = make_fix_prompt(cycle, candidate)
        write_text(SPRINT / "briefs" / f"cycle_{cycle:02d}_tex_fix_prompt.md", fix_prompt)
        run_cmd(
            f"codex-tex-fix-cycle-{cycle}",
            ["codex", "exec", "-m", "gpt-5.4-mini", "--sandbox", "workspace-write", "--cd", str(REPO), fix_prompt],
            SPRINT / "lanes/integrator" / f"TEX_FIX_CYCLE_{cycle:02d}.log",
            min(20 * 60, int(max(60, hard_end - time.time()))),
            REPO,
        )
        compile_results = [compile_tex(candidate / FLAGSHIP_REL), compile_tex(candidate / SUPPLEMENT_REL)]

    audit = audit_candidate(cycle, candidate, compile_results)
    summary = {
        "cycle": cycle,
        "candidate": str(candidate),
        "lane_results": lane_results,
        "integrator_result": integ_result,
        "audit": audit,
        "finished_utc": utc_now(),
    }
    write_text(candidate / f"CYCLE_{cycle:02d}_SUMMARY.json", json.dumps(summary, indent=2, sort_keys=True))
    md = [
        f"# Quality cycle {cycle} summary",
        "",
        f"Marker: `QUALITY_CYCLE_SUMMARY_{cycle:02d}`",
        f"Candidate: `{candidate}`",
        "",
        "## Lane exits",
    ]
    for r in lane_results:
        md.append(f"- {r['label']}: exit={r.get('exit_code')} elapsed={r.get('elapsed_s')}s output={r.get('output_path')}")
    md += [
        f"- integrator: exit={integ_result.get('exit_code')} elapsed={integ_result.get('elapsed_s')}s output={integ_result.get('output_path')}",
        "",
        "## Audit",
        f"- fatal_failures: {len(audit['fatal_failures'])}",
        f"- compile ok: {[r.get('ok') for r in compile_results]}",
        f"- figures: {len(audit['figures'])}",
        "",
        "## Safety",
        *[f"- {x}" for x in LOCKS],
    ]
    write_text(candidate / f"CYCLE_{cycle:02d}_SUMMARY.md", "\n".join(md) + "\n")
    ledger(f"cycle {cycle}: audit fatal_failures={len(audit['fatal_failures'])}; compile_ok={[r.get('ok') for r in compile_results]}")
    return candidate, summary


def write_final(cycles: List[Dict[str, Any]], latest_candidate: Path | None, start_utc: str, end_utc: str) -> None:
    final = {
        "sprint_id": SPRINT_ID,
        "started_utc": start_utc,
        "target_end_utc": end_utc,
        "finished_utc": utc_now(),
        "cycles_completed": len(cycles),
        "latest_candidate": str(latest_candidate) if latest_candidate else None,
        "safety_locks": LOCKS,
        "cycles": cycles,
    }
    write_text(SPRINT / "FINAL_QUALITY_SPRINT_HANDOFF.json", json.dumps(final, indent=2, sort_keys=True))
    lines = [
        "# RP-1 quality sprint final handoff",
        "",
        f"Marker: `{SPRINT_ID}_FINAL_HANDOFF`",
        f"Started UTC: {start_utc}",
        f"Target end UTC: {end_utc}",
        f"Finished UTC: {utc_now()}",
        f"Cycles completed: {len(cycles)}",
        "",
        "## Latest candidate",
        "",
        f"`{latest_candidate}`" if latest_candidate else "none",
        "",
    ]
    if latest_candidate:
        for p in [
            latest_candidate / "flagship_rp1/aastex/rp1_flagship_polished.pdf",
            latest_candidate / "supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf",
            latest_candidate / FLAGSHIP_REL,
            latest_candidate / SUPPLEMENT_REL,
        ]:
            lines.append(f"- `{p}` exists={p.exists()} sha256={sha256(p) if p.exists() and p.is_file() else None}")
    lines += [
        "",
        "## Cycle receipts",
    ]
    for c in cycles:
        audit = c.get("audit", {})
        lines.append(f"- cycle {c.get('cycle')}: candidate `{c.get('candidate')}` fatal_failures={len(audit.get('fatal_failures', []))}")
    lines += [
        "",
        "## Safety ledger",
        *[f"- {x}" for x in LOCKS],
        "",
        "No public replacement/publish was performed. Human/Hwao/Lana review remains the next gate before any public update.",
    ]
    write_text(SPRINT / "FINAL_QUALITY_SPRINT_HANDOFF.md", "\n".join(lines) + "\n")
    update_status(state="completed", cycles_completed=len(cycles), latest_candidate=str(latest_candidate) if latest_candidate else None, final_handoff=str(SPRINT / "FINAL_QUALITY_SPRINT_HANDOFF.md"))


def main() -> int:
    SPRINT.mkdir(parents=True, exist_ok=True)
    start = time.time()
    target_dt = dt.datetime.fromisoformat(TARGET_END_UTC.replace("Z", "+00:00"))
    hard_end = target_dt.timestamp()
    if hard_end <= start + 10 * 60:
        hard_end = start + DURATION_SECONDS
    start_utc = utc_now()
    end_utc = dt.datetime.fromtimestamp(hard_end, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    prepare_static_files(start_utc, end_utc)
    write_text(SPRINT / "RUNNING.pid", str(os.getpid()) + "\n")
    update_status(state="starting", pid=os.getpid(), started_utc=start_utc, target_end_utc=end_utc, source_package=str(SOURCE_PACKAGE))
    ledger("sprint started")

    for cmd in ["agy", "codex"]:
        if not command_exists(cmd):
            ledger(f"missing command: {cmd}")
    cycles: List[Dict[str, Any]] = []
    latest: Path | None = None
    source_for_copy = SOURCE_PACKAGE

    cycle = 1
    while cycle <= MAX_CYCLES and time.time() + MIN_REMAINING_FOR_NEW_CYCLE < hard_end:
        try:
            latest, summary = run_cycle(cycle, source_for_copy, hard_end)
            cycles.append(summary)
            source_for_copy = latest
        except Exception as exc:  # noqa: BLE001
            ledger(f"cycle {cycle}: fatal orchestrator exception {type(exc).__name__}: {exc}")
            append(SPRINT / "logs/orchestrator_exceptions.log", f"{utc_now()} cycle {cycle}: {type(exc).__name__}: {exc}\n")
        cycle += 1
        update_status(state="between_cycles", cycle=cycle - 1, cycles_completed=len(cycles), latest_candidate=str(latest) if latest else None)

    write_final(cycles, latest, start_utc, end_utc)
    ledger("sprint completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
