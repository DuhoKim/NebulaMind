#!/usr/bin/env python3
"""Four-hour local-only Galaxy Evolution wiki quality sprint.

Uses low-usage subscription-backed lanes where available:
- AGY/Antigravity Gemini 3.1 Pro (Low): Hwao-style wiki direction / topic strategy
- AGY/Antigravity Gemini 3.5 Flash (Low): Goru-style mechanical/content gap review
- Codex gpt-5.4-mini: Kun-style schema, citation, and reproducibility review
- Codex gpt-5.4-mini: local candidate integrator that prints revised Markdown only

Hard safety boundaries:
- Writes only under this sprint root.
- Does not edit product/wiki source files, public static roots, DB/API, page_versions,
  live wiki pages, trust/evidence, deploy/restart, git, cron, browser, credentials,
  billing/account/API/OAuth/GCP, or external submissions.
"""
from __future__ import annotations

import datetime as dt
import html
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
SPRINT_ROOT = Path(__file__).resolve().parent
INPUTS = SPRINT_ROOT / "inputs"
LANES = SPRINT_ROOT / "lane-reports"
CANDIDATES = SPRINT_ROOT / "candidates"
LOGS = SPRINT_ROOT / "logs"
STATUS = SPRINT_ROOT / "WIKI_SPRINT_STATUS.json"
LEDGER = SPRINT_ROOT / "WIKI_SPRINT_LEDGER.md"
BOARD = SPRINT_ROOT / "WIKI_SPRINT_BOARD.md"
FINAL = SPRINT_ROOT / "FINAL_HANDOFF.md"
MARKER = "WIKI_QUALITY_SPRINT_20260709T024308Z"

# 4 hours from process start unless WIKI_SPRINT_DURATION_SECONDS overrides.
DURATION_SECONDS = int(os.environ.get("WIKI_SPRINT_DURATION_SECONDS", "14400"))
MAX_CYCLES = int(os.environ.get("WIKI_SPRINT_MAX_CYCLES", "8"))
CYCLE_PAUSE_SECONDS = int(os.environ.get("WIKI_SPRINT_CYCLE_PAUSE_SECONDS", "600"))

SOURCE_FILES = {
    "wiki_content_contract": REPO / "docs" / "wiki_content_contract_v1.md",
    "wiki_schema": REPO / "wiki_schema.md",
    "galaxy_wiki_current_draft": REPO / "frontend" / "public" / "agent-reports" / "wiki-method-results" / "galaxy-evolution" / "source-first-paper-adjudication" / "galaxy-evolution-same-format-draft.md",
    "research_topics_current": REPO / "frontend" / "public" / "agent-reports" / "wiki-method-results" / "galaxy-evolution" / "source-first-paper-adjudication" / "research-topics-from-wiki-20260708T090359Z" / "research-topics-from-wiki-20260708T090359Z.md",
    "live_dom_snapshot": REPO / "docs" / "step9f_visible_content_prose_exact_diff_packet_20260704T022950Z" / "execution_results" / "20260704T062110Z" / "dom" / "wiki_galaxy_evolution_curl.html",
    "rp1_flagship_tex": REPO / ".hermes" / "handoffs" / "galaxy-evolution" / "mastermind" / "aas-autopilot" / "integration-runs" / "INTEGRATED_9_PAPERS_20260709T012051Z" / "decision-package" / "RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z" / "flagship_rp1" / "aastex" / "rp1_flagship_polished.tex",
    "rp1_package_audit": REPO / ".hermes" / "handoffs" / "galaxy-evolution" / "mastermind" / "aas-autopilot" / "integration-runs" / "INTEGRATED_9_PAPERS_20260709T012051Z" / "decision-package" / "RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z" / "PACKAGE_AUDIT.md",
}

SAFETY_LINES = [
    "local sprint/candidate artifacts only",
    "no DB/SQL/page_versions/API/wiki publish/trust recompute",
    "no public PDF/static wiki replacement or live roots",
    "no deploy/restart/service mutation",
    "no git commit/push/merge/rebase/reset",
    "no cron/background scheduler creation",
    "no billing/account/GCP/API-key/OAuth/token/credential reads or changes",
    "no browser automation or external submission",
]


def utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


def iso(ts: dt.datetime | None = None) -> str:
    return (ts or utcnow()).isoformat().replace("+00:00", "Z")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def append(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as fh:
        fh.write(text)


def read(path: Path, limit: int | None = None) -> str:
    text = path.read_text(errors="replace") if path.exists() else f"[MISSING: {path}]"
    if limit and len(text) > limit:
        return text[:limit] + f"\n\n[TRUNCATED at {limit} chars from {path}]"
    return text


def status_update(**kwargs: Any) -> None:
    data: Dict[str, Any] = {}
    if STATUS.exists():
        try:
            data = json.loads(STATUS.read_text())
        except Exception:
            data = {}
    data.update(kwargs)
    data["updated_utc"] = iso()
    write_text(STATUS, json.dumps(data, indent=2, sort_keys=True) + "\n")


def init_dirs() -> None:
    for d in [INPUTS, LANES, CANDIDATES, LOGS]:
        d.mkdir(parents=True, exist_ok=True)


def copy_inputs() -> None:
    manifest = {}
    for name, src in SOURCE_FILES.items():
        dst = INPUTS / f"{name}{src.suffix or '.txt'}"
        if src.exists():
            shutil.copy2(src, dst)
            manifest[name] = {"source": str(src), "copy": str(dst), "exists": True, "size": src.stat().st_size}
        else:
            write_text(dst, f"MISSING SOURCE: {src}\n")
            manifest[name] = {"source": str(src), "copy": str(dst), "exists": False, "size": 0}
    write_text(INPUTS / "INPUT_MANIFEST.json", json.dumps(manifest, indent=2, sort_keys=True) + "\n")


def rp1_facts() -> str:
    return """Latest local RP-1 paper facts available for wiki-quality review only (not product evidence until later approval):
- RP-1 is the local flagship short-paper candidate from the AAS sprint.
- Broad optical BPT AGN vs matched star-forming controls in a capped SDSS DR17 optical emission-line denominator.
- Matched pairs: 8,146.
- Median delta log sSFR: -1.309 dex.
- Bootstrap interval: [-1.334, -1.283] dex.
- Cache: 60,000 rows sampled/capped from a strict public four-line S/N>=3 parent of 249,917 rows, coverage 24.0%.
- Guardrail: association only; not causal AGN feedback, not a claim of physical quenching, and not representative of the whole SDSS galaxy population.
- The other eight SDSS pilot papers are supplementary denominator/proxy atlas material, not standalone causal-feedback papers.
"""


def base_context(wiki_path: Path, topics_path: Path) -> str:
    return textwrap.dedent(f"""
    Marker: {MARKER}

    Task: improve the Galaxy Evolution wiki and research-topic development locally.

    Safety boundary:
    - {'; '.join(SAFETY_LINES)}.
    - Outputs are advisory/candidate-only under {SPRINT_ROOT}.
    - Do not instruct live wiki publish or product DB writes.

    Current target files copied into this sprint:
    - Wiki content contract: {INPUTS / 'wiki_content_contract.md'}
    - Wiki schema: {INPUTS / 'wiki_schema.md'}
    - Current Galaxy Evolution same-format draft: {wiki_path}
    - Current research-topic proposal page: {topics_path}
    - RP-1 local AAS facts/audit are local support material only.

    Wiki content contract excerpt:
    {read(INPUTS / 'wiki_content_contract.md', 4000)}

    RP-1 local paper facts:
    {rp1_facts()}

    Current Galaxy Evolution wiki candidate markdown:
    {read(wiki_path, 18000)}

    Current research topics markdown:
    {read(topics_path, 12000)}
    """).strip()


def run_command(name: str, command: List[str], timeout: int, cwd: Path = REPO) -> Tuple[int, str, str, float]:
    start = time.time()
    try:
        cp = subprocess.run(command, cwd=str(cwd), text=True, capture_output=True, timeout=timeout)
        return cp.returncode, cp.stdout, cp.stderr, time.time() - start
    except subprocess.TimeoutExpired as exc:
        raw_out = exc.stdout
        raw_err = exc.stderr
        out = raw_out if isinstance(raw_out, str) else (raw_out or b"").decode(errors="replace")
        err = raw_err if isinstance(raw_err, str) else (raw_err or b"").decode(errors="replace")
        return 124, out, err + f"\n[TIMEOUT after {timeout}s]", time.time() - start
    except Exception as exc:
        return 127, "", repr(exc), time.time() - start


def run_many(cycle_dir: Path, jobs: List[Tuple[str, List[str], int]]) -> Dict[str, Dict[str, Any]]:
    # Keep implementation simple and deterministic; launch concurrently to avoid serial waiting.
    procs = []
    for name, command, timeout in jobs:
        start = time.time()
        proc = subprocess.Popen(command, cwd=str(REPO), text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        procs.append((name, command, timeout, start, proc))
    results: Dict[str, Dict[str, Any]] = {}
    for name, command, timeout, start, proc in procs:
        try:
            out, err = proc.communicate(timeout=timeout)
            rc = proc.returncode
        except subprocess.TimeoutExpired:
            proc.kill()
            out, err = proc.communicate()
            rc = 124
            err = (err or "") + f"\n[TIMEOUT after {timeout}s]"
        elapsed = time.time() - start
        safe_name = name.replace("/", "_")
        write_text(cycle_dir / f"{safe_name}.stdout.md", out or "")
        write_text(cycle_dir / f"{safe_name}.stderr.log", err or "")
        results[name] = {"returncode": rc, "elapsed_seconds": round(elapsed, 1), "stdout": str(cycle_dir / f"{safe_name}.stdout.md"), "stderr": str(cycle_dir / f"{safe_name}.stderr.log"), "command": command[:4]}
    return results


def mechanical_audit(text: str, topics: str) -> Dict[str, Any]:
    combined = text + "\n" + topics
    headings = re.findall(r"^##+\s+(.+)$", text, re.M)
    required_present = [h for h in ["Overview", "Current Research", "Open Questions", "See Also", "References"] if any(h.lower() in x.lower() for x in headings)]
    claim_open = len(re.findall(r"<!--claim:", text))
    claim_close = len(re.findall(r"<!--/claim:", text))
    cite_count = len(re.findall(r"<!--cite:", text))
    forbidden = []
    for token in ["<span", "</span", "<sub", "<sup", "&gt;", "&lt;", "&amp;", "\\sim", "\\approx", "\\pm"]:
        if token in combined:
            forbidden.append(token)
    overclaim_patterns = [
        r"AGN feedback quenches galaxies",
        r"proves? that AGN",
        r"causal AGN feedback",
        r"universal quenching",
        r"all active nuclei",
    ]
    overclaim_hits = []
    for pat in overclaim_patterns:
        if re.search(pat, combined, re.I):
            overclaim_hits.append(pat)
    rp1_number_hits = {num: (num in combined) for num in ["8,146", "-1.309", "-1.334", "-1.283", "60,000", "249,917", "24.0%"]}
    return {
        "marker": f"{MARKER}_MECHANICAL_AUDIT",
        "headings": headings,
        "required_schema_headings_present_by_name": required_present,
        "claim_markers": {"open": claim_open, "close": claim_close, "balanced": claim_open == claim_close},
        "cite_count": cite_count,
        "forbidden_contract_tokens": forbidden,
        "overclaim_pattern_hits": overclaim_hits,
        "rp1_number_presence": rp1_number_hits,
        "fatal_failures": [
            msg for msg in [
                "unbalanced claim markers" if claim_open != claim_close else "",
                "forbidden stored-content tokens present" if forbidden else "",
            ] if msg
        ],
    }


def simple_md_to_html(title: str, body: str, marker: str) -> str:
    # Minimal local preview only; not a renderer contract for product wiki.
    lines = []
    for raw in body.splitlines():
        if raw.startswith("# "):
            lines.append(f"<h1>{html.escape(raw[2:].strip())}</h1>")
        elif raw.startswith("## "):
            lines.append(f"<h2>{html.escape(raw[3:].strip())}</h2>")
        elif raw.startswith("### "):
            lines.append(f"<h3>{html.escape(raw[4:].strip())}</h3>")
        elif raw.startswith("- "):
            lines.append(f"<p>• {html.escape(raw[2:].strip())}</p>")
        elif raw.strip() == "":
            lines.append("")
        else:
            lines.append(f"<p>{html.escape(raw)}</p>")
    return "\n".join([
        "<!doctype html><meta charset='utf-8'>",
        f"<title>{html.escape(title)}</title>",
        "<style>body{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif;max-width:980px;margin:40px auto;padding:0 24px;line-height:1.6;background:#0f172a;color:#e5edf7}h1,h2,h3{color:#fff}p{color:#cbd5e1}code{color:#93c5fd}</style>",
        f"<!-- {marker} -->",
        *lines,
    ])


def extract_between(text: str, start: str, end: str) -> str | None:
    if start not in text or end not in text:
        return None
    chunk = text.split(start, 1)[1].split(end, 1)[0]
    return chunk.strip().strip("`").strip()


def seed_improvement(wiki_md: str, topics_md: str) -> Tuple[str, str]:
    # Deterministic quality nudge so every cycle produces an actual local candidate even if model output is delayed.
    rp1_para = (
        "\n\nA useful next denominator-controlled test now comes from the local SDSS DR17 optical-emission-line pilot. "
        "In that local draft, broad BPT-selected optical AGN hosts are compared with mass-redshift matched star-forming controls, "
        "yielding 8,146 matched pairs and a median $\\Delta\\log\\mathrm{sSFR}$ of -1.309 dex with bootstrap interval [-1.334, -1.283]. "
        "Because the analysis uses a 60,000-row capped cache covering 24.0% of a strict 249,917-row four-line S/N>=3 parent, "
        "it should be framed as an association and denominator-design result, not as a causal proof of AGN quenching."
    )
    if "8,146 matched pairs" not in wiki_md and "## Observational Evidence & Surveys" in wiki_md:
        wiki_md = wiki_md.replace("## Synthesis & Open Tensions", rp1_para + "\n\n## Synthesis & Open Tensions")
    if "P0 — Denominator-controlled optical AGN associations" not in topics_md:
        insert = """
## P0 — Denominator-controlled optical AGN associations in SDSS

**Hypothesis / objective.** Broad optical BPT AGN classifications identify host populations with lower catalog sSFR than carefully matched star-forming controls, but the observed offset must be separated from selection-function and denominator effects before it is interpreted as feedback.

**Prior evidence and constraints.** The local RP-1 SDSS pilot reports 8,146 matched AGN/control pairs and a median $\\Delta\\log\\mathrm{sSFR}$ of -1.309 dex, with bootstrap interval [-1.334, -1.283]. The same pilot is explicitly capped at 60,000 cached rows, covering 24.0% of the strict 249,917-row four-line S/N>=3 parent.

**Remaining uncertainty.** The offset may combine physical regulation, host selection, emission-line detectability, catalog SFR systematics, and denominator construction.

**Survey/data plan.** Rebuild the denominator with full SDSS DR17 access, then compare BPT, WISE, radio, X-ray, and morphology-selected AGN hosts across mass, redshift, environment, dust, and aperture controls.

**Analysis/test and decision criterion.** Treat the optical result as a reproducibility and association baseline. A feedback interpretation only becomes credible if multi-wavelength AGN indicators, gas-reservoir changes, and time-scale diagnostics remain coherent after denominator and selection-function stress tests.

**Limitations and wording guardrails.** This proposal must not say the SDSS pilot proves causal AGN feedback or universal quenching; it motivates a stricter denominator-controlled research programme.
""".strip()
        topics_md = topics_md.replace("3 proposal-style research programmes.", "4 proposal-style research programmes.\n\n" + insert)
    return wiki_md, topics_md


def run_cycle(cycle: int, previous_wiki: Path, previous_topics: Path) -> Path:
    cycle_dir = CANDIDATES / f"cycle_{cycle:02d}"
    cycle_dir.mkdir(parents=True, exist_ok=True)
    lane_dir = LANES / f"cycle_{cycle:02d}"
    lane_dir.mkdir(parents=True, exist_ok=True)

    current_wiki = cycle_dir / "galaxy-evolution-wiki-candidate.md"
    current_topics = cycle_dir / "research-topics-candidate.md"
    wiki_md, topics_md = seed_improvement(read(previous_wiki), read(previous_topics))
    write_text(current_wiki, wiki_md)
    write_text(current_topics, topics_md)

    ctx = base_context(current_wiki, current_topics)

    hwao_prompt = ctx + textwrap.dedent(f"""

    You are the Hwao-style wiki director lane for cycle {cycle}.
    Return a concise but substantive review with marker HWAO_WIKI_DIRECTOR_CYCLE_{cycle:02d}.
    Focus on: (1) research-topic strategy, (2) whether the Galaxy Evolution page advances the physical story,
    (3) how RP-1 should or should not influence the wiki, (4) highest-value next revisions.
    Keep causal guardrails strict and preserve source-first / prose-first workflow.
    Output only a report; do not claim to edit or publish anything.
    End with a safety ledger.
    """)
    goru_prompt = ctx + textwrap.dedent(f"""

    You are the Goru mechanical wiki-review lane for cycle {cycle}.
    Return marker GORU_WIKI_MECHANICAL_CYCLE_{cycle:02d}.
    Check section coverage, duplicate/redundant prose, jargonic phrasing, missing denominator/selection caveats,
    forbidden wiki-content-contract issues, missing research-topic decision criteria, and places where the proposal page needs clearer observables.
    Output exact ranked findings and safe local edit suggestions only.
    End with a safety ledger.
    """)
    kun_prompt = textwrap.dedent(f"""
    You are the Codex/Kun schema and reproducibility review lane for a local wiki sprint.
    Inspect these files read-only:
    - {current_wiki}
    - {current_topics}
    - {INPUTS / 'wiki_content_contract.md'}
    - {INPUTS / 'wiki_schema.md'}
    - {INPUTS / 'rp1_package_audit.md'}

    Return marker CODEX_KUN_WIKI_REVIEW_CYCLE_{cycle:02d}.
    Check markdown/schema/content-contract issues, citation/claim marker balance, RP-1 number consistency,
    overclaim risk, and whether research-topic proposals are actionable.
    Do not edit files. Do not run git writes, DB/API/wiki publish, deploy, restart, browser, or credential reads.
    End with safety ledger.
    """)

    jobs = [
        ("hwao_agy_director", ["agy", "--model", "Gemini 3.1 Pro (Low)", "--mode", "plan", "--print", hwao_prompt], 900),
        ("goru_agy_mechanical", ["agy", "--model", "Gemini 3.5 Flash (Low)", "--mode", "plan", "--print", goru_prompt], 720),
        ("kun_codex_review", ["codex", "exec", "-m", "gpt-5.4-mini", "--sandbox", "read-only", "--cd", str(REPO), kun_prompt], 900),
    ]
    append(LEDGER, f"\n- {iso()} cycle {cycle}: launching Hwao/Goru/Kun low-usage review lanes.\n")
    results = run_many(lane_dir, jobs)
    write_text(lane_dir / "LANE_RESULTS.json", json.dumps(results, indent=2, sort_keys=True) + "\n")

    report_summaries = []
    for name in ["hwao_agy_director", "goru_agy_mechanical", "kun_codex_review"]:
        report_summaries.append(f"\n## {name}\n" + read(lane_dir / f"{name}.stdout.md", 8000))

    integrator_prompt = textwrap.dedent(f"""
    You are the local-only wiki candidate integrator for cycle {cycle}.

    Hard boundaries:
    - Do not edit files directly; return text only.
    - Do not publish, write DB/API/page_versions, deploy/restart, run git writes, use browser, read credentials, or call billing/account/OAuth/API-key surfaces.
    - Output is candidate-only and will be saved under {cycle_dir}.

    Goal: improve the Galaxy Evolution wiki candidate and research-topic page so they support research-topic development.

    Requirements:
    - Preserve # Galaxy Evolution title and same-format narrative style.
    - Keep claim/cite markers balanced; do not invent new product evidence IDs.
    - RP-1 may be mentioned only as local pilot motivation/association/denominator design, not as a live product evidence source and not as causal proof.
    - Make research topics more actionable: clear hypothesis, observables, denominator/control plan, decision criterion, and limitations.
    - Reduce jargon where possible without flattening science.

    Current wiki candidate:
    {read(current_wiki, 18000)}

    Current research topics candidate:
    {read(current_topics, 12000)}

    Lane reports:
    {''.join(report_summaries)}

    Return exactly two Markdown blocks using these markers:
    BEGIN_GALAXY_WIKI_CANDIDATE
    <full revised Galaxy Evolution wiki candidate markdown>
    END_GALAXY_WIKI_CANDIDATE

    BEGIN_RESEARCH_TOPICS_CANDIDATE
    <full revised research topics markdown>
    END_RESEARCH_TOPICS_CANDIDATE
    """)
    append(LEDGER, f"- {iso()} cycle {cycle}: launching Codex mini integrator for local candidates.\n")
    rc, out, err, elapsed = run_command(
        "codex_integrator",
        ["codex", "exec", "-m", "gpt-5.4-mini", "--sandbox", "read-only", "--cd", str(REPO), integrator_prompt],
        1200,
    )
    write_text(lane_dir / "codex_integrator.stdout.md", out)
    write_text(lane_dir / "codex_integrator.stderr.log", err)
    integration_meta = {"returncode": rc, "elapsed_seconds": round(elapsed, 1), "stdout": str(lane_dir / "codex_integrator.stdout.md"), "stderr": str(lane_dir / "codex_integrator.stderr.log")}
    write_text(lane_dir / "INTEGRATOR_RESULT.json", json.dumps(integration_meta, indent=2, sort_keys=True) + "\n")

    wiki_block = extract_between(out, "BEGIN_GALAXY_WIKI_CANDIDATE", "END_GALAXY_WIKI_CANDIDATE")
    topics_block = extract_between(out, "BEGIN_RESEARCH_TOPICS_CANDIDATE", "END_RESEARCH_TOPICS_CANDIDATE")
    if wiki_block and len(wiki_block) > 2000:
        write_text(current_wiki, wiki_block + "\n")
    if topics_block and len(topics_block) > 1000:
        write_text(current_topics, topics_block + "\n")

    audit = mechanical_audit(read(current_wiki), read(current_topics))
    write_text(cycle_dir / "WIKI_QUALITY_AUDIT.json", json.dumps(audit, indent=2, sort_keys=True) + "\n")
    audit_md = [f"# Wiki quality audit cycle {cycle}", "", f"Marker: `{MARKER}_AUDIT_CYCLE_{cycle:02d}`", "", f"Fatal failures: {len(audit['fatal_failures'])}", "", "## Checks", f"- claim markers balanced: {audit['claim_markers']['balanced']}", f"- cite markers: {audit['cite_count']}", f"- forbidden contract tokens: {audit['forbidden_contract_tokens']}", f"- overclaim pattern hits: {audit['overclaim_pattern_hits']}", f"- RP-1 number presence: {audit['rp1_number_presence']}"]
    write_text(cycle_dir / "WIKI_QUALITY_AUDIT.md", "\n".join(audit_md) + "\n")
    write_text(cycle_dir / "galaxy-evolution-wiki-candidate.html", simple_md_to_html("Galaxy Evolution wiki candidate", read(current_wiki), f"{MARKER}_WIKI_HTML_CYCLE_{cycle:02d}"))
    write_text(cycle_dir / "research-topics-candidate.html", simple_md_to_html("Galaxy Evolution research topics candidate", read(current_topics), f"{MARKER}_TOPICS_HTML_CYCLE_{cycle:02d}"))

    append(LEDGER, f"- {iso()} cycle {cycle}: candidate/audit written; fatal failures={len(audit['fatal_failures'])}; candidate={cycle_dir}.\n")
    status_update(state="cycle_complete", cycle=cycle, cycles_completed=cycle, latest_candidate=str(cycle_dir), latest_audit=str(cycle_dir / "WIKI_QUALITY_AUDIT.md"))
    return cycle_dir


def write_board(start: dt.datetime, end: dt.datetime) -> None:
    content = f"""# Galaxy Evolution wiki quality sprint

Marker: `{MARKER}`

Started: {iso(start)}
Target end: {iso(end)}
Duration: about {DURATION_SECONDS // 3600} hours

## Why this exists

The wiki is important for developing research topics. This sprint asks low-usage lanes to keep improving the local Galaxy Evolution wiki candidate and research-topic proposal page while the paper sprint continues.

## Lanes

- Hwao-style director: `agy`, Gemini 3.1 Pro (Low), research-topic strategy and wiki direction.
- Goru mechanical reviewer: `agy`, Gemini 3.5 Flash (Low), contract/schema/gap checks.
- Kun reviewer: `codex exec`, gpt-5.4-mini, schema/reproducibility/overclaim checks.
- Integrator: `codex exec`, gpt-5.4-mini, writes candidate Markdown only under this sprint root.
- Tori/Hermes: orchestrator, receipt verifier, dashboard feed updater, no live publish.

## Target inputs

- `{SOURCE_FILES['galaxy_wiki_current_draft']}`
- `{SOURCE_FILES['research_topics_current']}`
- `{SOURCE_FILES['wiki_content_contract']}`
- `{SOURCE_FILES['wiki_schema']}`
- RP-1 local flagship paper package, as motivation/denominator context only.

## Safety

""" + "\n".join(f"- {x}" for x in SAFETY_LINES) + "\n"
    write_text(BOARD, content)


def final_handoff(start: dt.datetime, end: dt.datetime, latest: Path | None, cycles_completed: int) -> None:
    content = f"""# Wiki quality sprint handoff

Marker: `{MARKER}_FINAL_HANDOFF`

Started: {iso(start)}
Ended/status time: {iso()}
Target end: {iso(end)}
Cycles completed: {cycles_completed}
Latest candidate: `{latest or ''}`

## Outputs

- Board: `{BOARD}`
- Ledger: `{LEDGER}`
- Status JSON: `{STATUS}`
- Lane reports: `{LANES}`
- Candidates: `{CANDIDATES}`

## Safety ledger

""" + "\n".join(f"- {x}: 0 / not touched" for x in SAFETY_LINES[1:]) + "\n"
    write_text(FINAL, content)


def main() -> int:
    start = utcnow()
    end = start + dt.timedelta(seconds=DURATION_SECONDS)
    init_dirs()
    copy_inputs()
    write_board(start, end)
    append(LEDGER, f"# Wiki quality sprint ledger\n\nMarker: `{MARKER}`\n\n- {iso(start)} sprint started; pid={os.getpid()}; target_end={iso(end)}.\n")
    status_update(
        marker=MARKER,
        pid=os.getpid(),
        state="starting",
        started_utc=iso(start),
        target_end_utc=iso(end),
        duration_seconds=DURATION_SECONDS,
        max_cycles=MAX_CYCLES,
        board=str(BOARD),
        ledger=str(LEDGER),
        safety=SAFETY_LINES,
        lanes=["agy Gemini 3.1 Pro Low", "agy Gemini 3.5 Flash Low", "codex gpt-5.4-mini review", "codex gpt-5.4-mini integrator"],
    )

    previous_wiki = INPUTS / "galaxy_wiki_current_draft.md"
    previous_topics = INPUTS / "research_topics_current.md"
    latest: Path | None = None
    cycles_completed = 0

    for cycle in range(1, MAX_CYCLES + 1):
        if utcnow() >= end:
            break
        status_update(state="cycle_running", cycle=cycle, candidate=str(CANDIDATES / f"cycle_{cycle:02d}"), cycles_completed=cycles_completed)
        latest = run_cycle(cycle, previous_wiki, previous_topics)
        cycles_completed = cycle
        previous_wiki = latest / "galaxy-evolution-wiki-candidate.md"
        previous_topics = latest / "research-topics-candidate.md"
        remaining = (end - utcnow()).total_seconds()
        if cycle >= MAX_CYCLES or remaining <= 300:
            break
        sleep_for = min(CYCLE_PAUSE_SECONDS, max(0, int(remaining - 300)))
        status_update(state="between_cycles", cycle=cycle, cycles_completed=cycles_completed, next_cycle_after_seconds=sleep_for, latest_candidate=str(latest))
        append(LEDGER, f"- {iso()} cycle {cycle}: sleeping {sleep_for}s before next low-usage pass.\n")
        time.sleep(sleep_for)

    final_handoff(start, end, latest, cycles_completed)
    status_update(state="completed", cycles_completed=cycles_completed, latest_candidate=str(latest or ""), final_handoff=str(FINAL))
    append(LEDGER, f"- {iso()} sprint completed; cycles_completed={cycles_completed}; final={FINAL}.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
