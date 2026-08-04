#!/usr/bin/env python3
"""Continuation actual-data-only journal-paper quality sprint for NebulaMind Galaxy Evolution papers.

This orchestrator relaunches the prior paper/research autopilot pattern with low-usage
provider lanes. It writes only under this sprint directory and candidate copies of the
local manuscript package. It never touches public pages, live roots, product DB/API,
git history, deployment, billing/account settings, cron, or external submission systems.

Research/data rule: no mock, synthetic, fake, placeholder, or toy data may be introduced.
New quantitative claims must come from the real local SDSS artifacts inventoried here or
from a cited public source with URL/DOI/arXiv/ADS metadata. If a needed datum is absent,
the lane must write "not measured here" / "needs real data" instead of filling it in.
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
import time
from pathlib import Path
from typing import Any, Dict, List, Tuple

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTO = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
SOURCE_PACKAGE = Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package')
INTEGRATED_ROOT = AUTO / "integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z"
OVERNIGHT_ROOT = AUTO / "overnight-9-papers-20260708"
SPRINT_ID = "ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z"
SPRINT = AUTO / "research-quality-sprints" / SPRINT_ID

DURATION_SECONDS = int(os.environ.get("NEBULAMIND_ACTUAL_RESEARCH_SPRINT_SECONDS", str(8 * 60 * 60)))
MAX_CYCLES = int(os.environ.get("NEBULAMIND_ACTUAL_RESEARCH_SPRINT_MAX_CYCLES", "6"))
MIN_REMAINING_FOR_NEW_CYCLE = 40 * 60
PER_LANE_TIMEOUT = 75 * 60
INTEGRATOR_TIMEOUT = 60 * 60

FLAGSHIP_REL = Path("flagship_rp1/aastex/rp1_flagship_polished.tex")
SUPPLEMENT_REL = Path("supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex")

LOCKS = [
    "write only under this sprint directory and candidate copies",
    "no public pages, public PDF replacement, or live/static root edits",
    "no product DB, SQL, /api/pages, page_versions, wiki publish, trust recompute, or data mutation",
    "no deploy/restart",
    "no git commit/push/merge/rebase/history rewrite",
    "no cron creation/update",
    "no billing/cloud/OAuth/API-key/account changes and no credential/token/cookie reads",
    "no external manuscript submission",
]

REAL_DATA_POLICY = [
    "Never use mock, synthetic, fake, placeholder, or toy data.",
    "Do not invent numeric values, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, or figure results.",
    "New quantitative claims must be traceable to the real local SDSS artifacts inventoried by this sprint or to a cited public source with URL/DOI/arXiv/ADS metadata.",
    "If a value is not present in the local real-data inventory or a cited public source, write 'not measured here' or 'needs real data'.",
    "Literature-only sources may motivate future work; they do not become measured NebulaMind results.",
    "The RP-1 flagship remains an optical SDSS/BPT association pilot unless real additional observables are supplied.",
]

REQUIRED_FLAGSHIP_PHRASES = ["association", "not a causal", "capped", "non-random", "8,146", "-1.309"]
REQUIRED_SUPPLEMENT_PHRASES = ["denominator/proxy", "radio", "X-ray", "CO/HI", "not as independent causal"]
NUMERIC_INVARIANTS = ["8,146", "-1.309", "[-1.334,-1.283]", "249,917", "60,000", "24.0"]
BAD_DATA_USE_PATTERNS = [
    r"\b(?:use|used|using|based on|generated|created|filled|substituted)\b[^.\n]{0,80}\b(?:mock|synthetic|fake|placeholder|toy) data\b",
    r"\b(?:mock|synthetic|fake|placeholder|toy) data\b[^.\n]{0,80}\b(?:result|sample|catalog|catalogue|table|measurement|analysis)\b",
]


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def kst_now() -> str:
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S KST")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def append(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(text)


def read_text(path: Path, limit: int | None = None) -> str:
    if not path.exists():
        return f"[MISSING: {path}]"
    text = path.read_text(errors="replace")
    if limit and len(text) > limit:
        return text[:limit] + f"\n\n[TRUNCATED at {limit} chars from {path}]\n"
    return text


def sha256(path: Path) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def command_exists(name: str) -> bool:
    return shutil.which(name) is not None


def ledger(line: str) -> None:
    append(SPRINT / "SPRINT_LEDGER.md", f"- {utc_now()} / {kst_now()} — {line}\n")


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


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(SPRINT))
    except Exception:
        return str(path)


def csv_row_count(path: Path) -> int | None:
    try:
        with path.open("rb") as f:
            count = sum(1 for _ in f)
        return max(0, count - 1)
    except Exception:
        return None


def compact_ws(text: str, limit: int = 900) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        return text[:limit] + " ..."
    return text


def extract_tex_summary(path: Path) -> Dict[str, Any]:
    text = read_text(path, 250000)
    title_m = re.search(r"\\title(?:\[[^\]]*\])?\{(.+?)\}", text, flags=re.S)
    abstract_m = re.search(r"\\begin\{abstract\}(.+?)\\end\{abstract\}", text, flags=re.S)
    return {
        "path": str(path),
        "bytes": path.stat().st_size if path.exists() else 0,
        "sha256": sha256(path),
        "title": compact_ws(title_m.group(1), 220) if title_m else "[title not found]",
        "abstract": compact_ws(abstract_m.group(1), 1200) if abstract_m else "[abstract not found]",
    }


def integrated_tex_files() -> List[Path]:
    if not INTEGRATED_ROOT.exists():
        return []
    return sorted(INTEGRATED_ROOT.glob("[0-9][0-9]_*/aastex/*_integrated.tex"))


def build_real_data_inventory(cycle: int | None = None) -> Dict[str, Any]:
    csv_roots = [
        AUTO / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data",
        OVERNIGHT_ROOT / "lanes/goru/tables",
    ]
    json_roots = [
        AUTO / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z",
        AUTO / "runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
        OVERNIGHT_ROOT / "lanes/goru/artifacts",
        OVERNIGHT_ROOT / "lanes/tori",
        INTEGRATED_ROOT,
        SOURCE_PACKAGE,
    ]
    csvs = []
    for root in csv_roots:
        if root.exists():
            for p in sorted(root.rglob("*.csv"))[:200]:
                csvs.append({"path": str(p), "rows": csv_row_count(p), "bytes": p.stat().st_size, "sha256": sha256(p)})
    jsons = []
    for root in json_roots:
        if root.exists():
            for p in sorted(root.rglob("*.json"))[:400]:
                rec: Dict[str, Any] = {"path": str(p), "bytes": p.stat().st_size, "sha256": sha256(p), "parse_ok": False}
                try:
                    val = json.loads(p.read_text(errors="replace"))
                    rec["parse_ok"] = True
                    if isinstance(val, dict):
                        rec["top_keys"] = list(val.keys())[:20]
                    elif isinstance(val, list):
                        rec["list_len"] = len(val)
                except Exception as exc:
                    rec["error"] = f"{type(exc).__name__}: {exc}"
                jsons.append(rec)
    texs = [extract_tex_summary(p) for p in integrated_tex_files()]
    pdfs = []
    for root in [SOURCE_PACKAGE, INTEGRATED_ROOT]:
        if root.exists():
            for p in sorted(root.rglob("*.pdf"))[:120]:
                header = ""
                try:
                    header = p.open("rb").read(4).decode(errors="replace")
                except Exception:
                    pass
                pdfs.append({"path": str(p), "bytes": p.stat().st_size, "header": header, "sha256": sha256(p)})
    inventory = {
        "sprint_id": SPRINT_ID,
        "cycle": cycle,
        "created_utc": utc_now(),
        "real_data_policy": REAL_DATA_POLICY,
        "source_package": str(SOURCE_PACKAGE),
        "integrated_root": str(INTEGRATED_ROOT),
        "overnight_root": str(OVERNIGHT_ROOT),
        "csv_files": csvs,
        "json_files": jsons,
        "integrated_tex_summaries": texs,
        "pdf_files": pdfs,
        "counts": {"csv_files": len(csvs), "json_files": len(jsons), "integrated_tex_files": len(texs), "pdf_files": len(pdfs)},
    }
    out = SPRINT / "real-data-inventory"
    name = "REAL_DATA_INVENTORY_INITIAL" if cycle is None else f"REAL_DATA_INVENTORY_CYCLE_{cycle:02d}"
    write_text(out / f"{name}.json", json.dumps(inventory, indent=2, sort_keys=True))
    md = [
        f"# Real data inventory {name}",
        "",
        f"Marker: `{name}`",
        f"Created UTC: {inventory['created_utc']}",
        "",
        "## Hard rule",
        *[f"- {x}" for x in REAL_DATA_POLICY],
        "",
        "## Counts",
        f"- CSV real-data files inventoried: {len(csvs)}",
        f"- JSON/result/provenance files inventoried: {len(jsons)}",
        f"- integrated AASTeX drafts summarized: {len(texs)}",
        f"- PDFs hashed: {len(pdfs)}",
        "",
        "## Key CSV receipts",
    ]
    for rec in csvs[:40]:
        md.append(f"- `{rec['path']}` rows={rec['rows']} bytes={rec['bytes']} sha256={rec['sha256']}")
    md += ["", "## Integrated draft summaries"]
    for rec in texs:
        md.append(f"- `{rec['path']}` — {rec['title']}")
    write_text(out / f"{name}.md", "\n".join(md) + "\n")
    return inventory


def prepare_static_files(start_utc: str, end_utc: str) -> None:
    for d in ["briefs", "lanes/hwao", "lanes/gemini_deep_research", "lanes/gemini_source_factcheck", "lanes/codex_kun", "lanes/goru_real_data", "lanes/integrator", "candidates", "logs", "real-data-inventory"]:
        (SPRINT / d).mkdir(parents=True, exist_ok=True)
    board = [
        "# Actual-data-only journal-paper quality sprint",
        "",
        f"Marker: `{SPRINT_ID}`",
        f"Start UTC: {start_utc}",
        f"Target end UTC: {end_utc}",
        f"Start KST: {kst_now()}",
        "",
        "## User directive",
        "Relaunch the autopilots that worked on actual research and journal-paper writing; enhance paper quality using low-usage provider lanes such as Gemini/Gemini-web/deep-research style. For research, never use mock data; use real data only.",
        "",
        "## Source package",
        f"Primary candidate source: `{SOURCE_PACKAGE}`",
        f"Integrated nine-paper context: `{INTEGRATED_ROOT}`",
        f"Overnight lane artifacts: `{OVERNIGHT_ROOT}`",
        "",
        "## Lane roles",
        "- Hwao/Fable director lane: Gemini 3.1 Pro Low via AGY; publication triage and paper-by-paper priority.",
        "- Gemini deep-research lane: Gemini 3.1 Pro Low via AGY; web/deep-research-style literature/source gap work with URLs/DOIs/arXiv/ADS only.",
        "- Gemini source fact-check lane: Gemini 3.5 Flash Low via AGY; citation-role and overclaim checks.",
        "- Kun/Codex lane: gpt-5.4-mini read-only reproducibility, TeX, and data-provenance audit.",
        "- Goru mechanical lane: local Python real-data inventory, hashes, row counts, no-mock scan, compile receipts.",
        "- Tori integrator lane: candidate-copy-only TeX integration; no public/live/git/DB/deploy side effects.",
        "",
        "## Real-data-only policy",
        *[f"- {x}" for x in REAL_DATA_POLICY],
        "",
        "## Safety locks",
        *[f"- {x}" for x in LOCKS],
    ]
    write_text(SPRINT / "SPRINT_BOARD.md", "\n".join(board) + "\n")
    write_text(SPRINT / "INPUTS.json", json.dumps({
        "sprint_id": SPRINT_ID,
        "source_package": str(SOURCE_PACKAGE),
        "integrated_root": str(INTEGRATED_ROOT),
        "overnight_root": str(OVERNIGHT_ROOT),
        "real_data_policy": REAL_DATA_POLICY,
        "safety_locks": LOCKS,
        "start_utc": start_utc,
        "target_end_utc": end_utc,
    }, indent=2, sort_keys=True))
    build_real_data_inventory(None)


def run_cmd(label: str, args: List[str], out_path: Path, timeout_s: int, cwd: Path = REPO) -> Dict[str, Any]:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    started = utc_now()
    append(out_path, f"# {label}\nStarted UTC: {started}\nCWD: {cwd}\nCommand head: {args[:8]}\n\n")
    if args and not command_exists(args[0]):
        output = f"[MISSING COMMAND] {args[0]}\n"
        append(out_path, output)
        return {"label": label, "exit_code": 127, "elapsed_s": 0, "timed_out": False, "started_utc": started, "finished_utc": utc_now(), "output_path": str(out_path), "missing_command": args[0]}
    env = os.environ.copy()
    env.setdefault("NO_COLOR", "1")
    env.setdefault("CLICOLOR", "0")
    t0 = time.time()
    try:
        proc = subprocess.run(args, cwd=str(cwd), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout_s, env=env)
        output = proc.stdout or ""
        rc = proc.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        raw = exc.stdout
        if isinstance(raw, bytes):
            output = raw.decode(errors="replace")
        elif isinstance(raw, str):
            output = raw
        else:
            output = ""
        output += f"\n\n[TIMEOUT after {timeout_s}s]\n"
        rc = 124
        timed_out = True
    except Exception as exc:
        output = f"[EXCEPTION] {type(exc).__name__}: {exc}\n"
        rc = 125
        timed_out = False
    elapsed = time.time() - t0
    append(out_path, output)
    append(out_path, f"\n\n# command_result\nexit_code={rc}\nelapsed_s={elapsed:.1f}\ntimed_out={timed_out}\nfinished_utc={utc_now()}\n")
    return {"label": label, "exit_code": rc, "elapsed_s": round(elapsed, 1), "timed_out": timed_out, "started_utc": started, "finished_utc": utc_now(), "output_path": str(out_path)}


def make_context(candidate: Path, cycle: int, inventory: Dict[str, Any]) -> str:
    tex_summaries = inventory.get("integrated_tex_summaries", [])
    summary_lines = []
    for rec in tex_summaries:
        summary_lines.append(f"- {rec.get('title')}\n  path: {rec.get('path')}\n  abstract: {rec.get('abstract')}")
    flagship = candidate / FLAGSHIP_REL
    supplement = candidate / SUPPLEMENT_REL
    pieces = [
        f"Sprint: {SPRINT_ID} cycle {cycle}",
        "",
        "REAL-DATA-ONLY POLICY:",
        "\n".join(f"- {x}" for x in REAL_DATA_POLICY),
        "",
        "SAFETY LOCKS:",
        "\n".join(f"- {x}" for x in LOCKS),
        "",
        f"Primary candidate package: {candidate}",
        f"Flagship TeX: {flagship}",
        f"Supplement TeX: {supplement}",
        f"Integrated nine-paper context root: {INTEGRATED_ROOT}",
        "",
        "REAL-DATA INVENTORY COUNTS:",
        json.dumps(inventory.get("counts", {}), indent=2),
        "",
        "INTEGRATED DRAFT SUMMARIES:",
        "\n".join(summary_lines)[:14000],
        "",
        "FLAGSHIP EXCERPT:",
        read_text(flagship, 18000),
        "",
        "SUPPLEMENT EXCERPT:",
        read_text(supplement, 22000),
    ]
    return "\n".join(pieces)


def make_hwao_prompt(cycle: int, candidate: Path, inventory: Dict[str, Any]) -> str:
    return f"""You are Hwao/Fable, director for the NebulaMind actual-data journal-paper quality sprint.

Task: produce a paper-quality triage plan for this cycle. Work in read-only review mode.

Output marker: ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_{cycle:02d}

Required output:
- publication-readiness verdict for the RP-1 flagship and the supplementary denominator/proxy atlas
- top 12 concrete quality improvements, ranked by scientific value
- what can be improved now using real local SDSS data already inventoried
- what requires new real data and therefore must not be written as a result yet
- exact guidance for the integrator: safe wording/citation changes only
- a no-mock-data receipt and safety ledger

Hard rules:
- Never use or propose mock/synthetic/fake/placeholder/toy data.
- Do not invent numbers, sample sizes, citations, URLs, DOIs, arXiv IDs, or ADS bibcodes.
- Preserve the association-only boundary for RP-1 unless a real added dataset justifies more.
- Read-only: do not edit files, publish, deploy, write DB/API/wiki/git/cron, or touch public/live roots.

Context follows:
{make_context(candidate, cycle, inventory)}
"""


def make_deep_research_prompt(cycle: int, candidate: Path, inventory: Dict[str, Any]) -> str:
    return f"""You are the Gemini deep-research-style lane for NebulaMind Galaxy Evolution papers.

Use low-usage Gemini/deep-research/web abilities if available, but operate as read-only. Your job is source-grounded literature and paper-quality research, not file editing.

Output marker: ACTUAL_RESEARCH_GEMINI_DEEP_RESEARCH_CYCLE_{cycle:02d}

Required output:
1. A source-grounded literature/source packet for improving the RP-1 flagship and supplement.
2. Every new source must include at least one of: URL, DOI, arXiv ID, ADS bibcode, journal volume/page, or another checkable public identifier.
3. Classify each source role: actual method support, interpretation caveat, future-data motivation, or not usable.
4. Identify missing real observables: radio, X-ray, CO/HI, morphology, environment/halo, outflow, AGN luminosity/duty cycle, simulations as published comparison data only. Do not write them as measured results unless real data are present.
5. Provide exact safe wording improvements and citation insertion suggestions.
6. End with a no-mock-data receipt and safety ledger.

Hard real-data rule:
- Never introduce mock, synthetic, fake, placeholder, or toy data.
- If you cannot verify a source or datum, mark it "unverified / do not integrate".
- Literature can motivate future work; it cannot create a NebulaMind measured result.

Read-only safety: do not edit files; do not request credentials; do not publish/deploy/commit/restart/write DB/API/wiki/trust/cron/billing/account settings.

Context follows:
{make_context(candidate, cycle, inventory)}
"""


def make_factcheck_prompt(cycle: int, candidate: Path, inventory: Dict[str, Any]) -> str:
    return f"""You are the Gemini source-factcheck lane for a real-data-only astronomy manuscript sprint.

Output marker: ACTUAL_RESEARCH_GEMINI_SOURCE_FACTCHECK_CYCLE_{cycle:02d}

Review the package for overclaims, citation-role errors, and any accidental use of non-real data.

Required output:
- blocker/major/minor issue list
- quote risky sentence or section and propose safer wording
- flag any place where radio/X-ray/CO/HI/outflow/simulation literature is treated as measured data instead of future-observable motivation
- flag any claim that needs real data not currently inventoried
- list source/citation suggestions only if you can provide checkable identifiers
- explicit statement: no mock/synthetic/fake/placeholder/toy data accepted
- safety ledger

Read-only; no edits or side effects.

Context follows:
{make_context(candidate, cycle, inventory)}
"""


def make_codex_review_prompt(cycle: int, candidate: Path, inventory: Dict[str, Any]) -> str:
    inv_path = SPRINT / "real-data-inventory" / f"REAL_DATA_INVENTORY_CYCLE_{cycle:02d}.json"
    return f"""Review this local manuscript package in read-only mode.

Output marker: ACTUAL_RESEARCH_CODEX_KUN_REVIEW_CYCLE_{cycle:02d}

You are Kun/Codex: reproducibility, TeX, provenance, and no-mock-data audit.

Read only these roots unless needed for harmless metadata checks:
- candidate package: {candidate}
- real-data inventory: {inv_path}
- integrated context: {INTEGRATED_ROOT}
- original real-data runs: {AUTO / 'runs'}

Tasks:
- inspect TeX/prose for compile risks and journal-paper weaknesses
- verify that numeric claims remain traceable to real local files or cited public sources
- check core invariants: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage
- scan for forbidden use of mock/synthetic/fake/placeholder/toy data
- recommend safe candidate-only edits for the integrator

Forbidden: file edits, public/live edits, DB/API/wiki/trust/deploy/git/cron/billing/OAuth/account changes, external submission, credential reads.
"""


def find_bad_data_use(text: str) -> List[str]:
    hits: List[str] = []
    for pat in BAD_DATA_USE_PATTERNS:
        for m in re.finditer(pat, text, flags=re.I):
            hits.append(compact_ws(m.group(0), 260))
    return hits[:30]


def goru_real_data_report(cycle: int, candidate: Path, inventory: Dict[str, Any], out_path: Path) -> Dict[str, Any]:
    ftxt = read_text(candidate / FLAGSHIP_REL)
    stxt = read_text(candidate / SUPPLEMENT_REL)
    report = {
        "cycle": cycle,
        "candidate": str(candidate),
        "created_utc": utc_now(),
        "real_data_inventory_counts": inventory.get("counts", {}),
        "flagship_required_missing": [p for p in REQUIRED_FLAGSHIP_PHRASES if p not in ftxt],
        "supplement_required_missing": [p for p in REQUIRED_SUPPLEMENT_PHRASES if p not in stxt],
        "numeric_invariants_missing_flagship": [p for p in NUMERIC_INVARIANTS if p not in ftxt],
        "bad_mock_or_synthetic_data_use_flagship": find_bad_data_use(ftxt),
        "bad_mock_or_synthetic_data_use_supplement": find_bad_data_use(stxt),
        "pdfs": [],
        "figures": [],
    }
    for p in [candidate / "flagship_rp1/aastex/rp1_flagship_polished.pdf", candidate / "supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf"]:
        header = ""
        if p.exists():
            try:
                header = p.open("rb").read(4).decode(errors="replace")
            except Exception:
                pass
        report["pdfs"].append({"path": str(p), "exists": p.exists(), "bytes": p.stat().st_size if p.exists() else 0, "header": header, "sha256": sha256(p)})
    for root in [candidate / "flagship_rp1/figures", candidate / "supplementary_denominator_atlas/figures"]:
        if root.exists():
            for p in sorted(root.glob("*.pdf")):
                report["figures"].append({"path": str(p), "bytes": p.stat().st_size, "sha256": sha256(p)})
    write_text(out_path.with_suffix(".json"), json.dumps(report, indent=2, sort_keys=True))
    md = [
        f"# Goru real-data/no-mock report cycle {cycle}",
        "",
        f"Marker: `ACTUAL_RESEARCH_GORU_REAL_DATA_REPORT_CYCLE_{cycle:02d}`",
        f"Created UTC: {report['created_utc']}",
        "",
        "## Real-data inventory counts",
        f"- {report['real_data_inventory_counts']}",
        "",
        "## Missing guards",
        f"- flagship required phrases missing: {report['flagship_required_missing']}",
        f"- supplement required phrases missing: {report['supplement_required_missing']}",
        f"- flagship numeric invariants missing: {report['numeric_invariants_missing_flagship']}",
        "",
        "## Forbidden mock/synthetic data-use scan",
        f"- flagship hits: {report['bad_mock_or_synthetic_data_use_flagship']}",
        f"- supplement hits: {report['bad_mock_or_synthetic_data_use_supplement']}",
        "",
        "## PDF receipts before integration/compile",
    ]
    for rec in report["pdfs"]:
        md.append(f"- `{rec['path']}` exists={rec['exists']} bytes={rec['bytes']} header={rec['header']} sha256={rec['sha256']}")
    md += ["", "## Policy", *[f"- {x}" for x in REAL_DATA_POLICY], "", "## Safety", *[f"- {x}" for x in LOCKS]]
    write_text(out_path, "\n".join(md) + "\n")
    return report


def make_integrator_prompt(cycle: int, candidate: Path, report_paths: List[Path]) -> str:
    reports = []
    for p in report_paths:
        reports.append(f"\n\n===== REPORT {p} =====\n" + read_text(p, 26000))
    return f"""You are the Tori/Codex candidate-copy-only manuscript integrator for actual-data journal-paper quality cycle {cycle}.

Working root: {candidate}

You may edit ONLY these two candidate-copy TeX files:
- {candidate / FLAGSHIP_REL}
- {candidate / SUPPLEMENT_REL}

You may write a concise response file:
- {candidate / f'CYCLE_{cycle:02d}_ACTUAL_RESEARCH_RESPONSE.md'}

Hard real-data-only rules:
- NEVER introduce mock, synthetic, fake, placeholder, or toy data.
- Do not invent any number, sample size, table value, figure result, citation, URL, DOI, arXiv ID, or ADS bibcode.
- You may add a new citation only if a review report gives checkable bibliographic metadata OR it already exists in the manuscript/package.
- You may not add new quantitative claims unless the value appears in the local real-data inventory or reports with a source path.
- If a requested improvement needs absent data, write it as a limitation/future real-data requirement, not as a result.

Forbidden side effects:
- Do not edit outside the candidate root.
- Do not touch public pages, live roots, DB/API/wiki/trust/deploy/git/cron/billing/OAuth/account settings, or external submission systems.
- Do not change numeric invariants, figure paths, or core association-only claim boundaries unless correcting a typo with cited proof.

Allowed and desired:
- Improve journal-paper prose, abstract, introduction, limitations, source-role clarity, and conclusion.
- Strengthen real-data provenance and no-mock/no-placeholder wording where appropriate.
- Keep RP-1 as an optical BPT/sSFR association pilot and the supplement as a denominator/proxy atlas.
- Separate actual method/data citations from future-observable literature.
- Keep TeX compilable.
- Write CYCLE_{cycle:02d}_ACTUAL_RESEARCH_RESPONSE.md explaining exactly what changed, what was refused, and why.

Review reports follow:
{''.join(reports)}
"""


def compile_tex(tex: Path) -> Dict[str, Any]:
    pdf = tex.with_suffix(".pdf")
    log = tex.with_suffix(".actual_research.compile.log")
    if pdf.exists():
        try:
            pdf.unlink()
        except Exception:
            pass
    if not command_exists("tectonic"):
        write_text(log, "tectonic not found\n")
        return {"tex": str(tex), "pdf": str(pdf), "ok": False, "reason": "tectonic not found", "log": str(log)}
    try:
        proc = subprocess.run(["tectonic", tex.name], cwd=str(tex.parent), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=10 * 60)
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


def audit_candidate(cycle: int, candidate: Path, compile_results: List[Dict[str, Any]], goru_report: Dict[str, Any]) -> Dict[str, Any]:
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
        "bad_mock_or_synthetic_data_use_flagship": find_bad_data_use(ftxt),
        "bad_mock_or_synthetic_data_use_supplement": find_bad_data_use(stxt),
        "goru_preintegrator_report": goru_report,
        "fatal_failures": [],
    }
    for cr in compile_results:
        if not cr.get("ok"):
            audit["fatal_failures"].append({"compile_failure": cr})
    for key in ["flagship_required_missing", "supplement_required_missing", "numeric_invariants_missing_flagship", "bad_mock_or_synthetic_data_use_flagship", "bad_mock_or_synthetic_data_use_supplement"]:
        if audit[key]:
            audit["fatal_failures"].append({key: audit[key]})
    write_text(candidate / f"CYCLE_{cycle:02d}_ACTUAL_RESEARCH_AUDIT.json", json.dumps(audit, indent=2, sort_keys=True))
    md = [
        f"# Cycle {cycle} actual-research audit",
        "",
        f"Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_{cycle:02d}`",
        f"Audit UTC: {audit['audit_utc']}",
        "",
        "## Compile results",
    ]
    for cr in compile_results:
        md.append(f"- `{Path(cr['tex']).name}` ok={cr.get('ok')} bytes={cr.get('pdf_bytes')} sha256={cr.get('sha256')} bad_markers={cr.get('bad_markers')}")
    md += [
        "",
        "## Guards",
        f"- flagship missing required phrases: {audit['flagship_required_missing']}",
        f"- supplement missing required phrases: {audit['supplement_required_missing']}",
        f"- flagship missing numeric invariants: {audit['numeric_invariants_missing_flagship']}",
        f"- forbidden mock/synthetic data-use hits flagship: {audit['bad_mock_or_synthetic_data_use_flagship']}",
        f"- forbidden mock/synthetic data-use hits supplement: {audit['bad_mock_or_synthetic_data_use_supplement']}",
        "",
        f"Fatal failures: {len(audit['fatal_failures'])}",
        "",
        "## Real-data policy",
        *[f"- {x}" for x in REAL_DATA_POLICY],
    ]
    write_text(candidate / f"CYCLE_{cycle:02d}_ACTUAL_RESEARCH_AUDIT.md", "\n".join(md) + "\n")
    return audit


def run_cycle(cycle: int, source_for_copy: Path, hard_end: float) -> Tuple[Path, Dict[str, Any]]:
    candidate = SPRINT / "candidates" / f"cycle_{cycle:02d}_package"
    if candidate.exists():
        shutil.rmtree(candidate)
    shutil.copytree(source_for_copy, candidate)
    ledger(f"cycle {cycle}: candidate copied from {source_for_copy} to {candidate}")
    update_status(state="cycle_running", cycle=cycle, candidate=str(candidate))

    inventory = build_real_data_inventory(cycle)
    hwao_prompt = make_hwao_prompt(cycle, candidate, inventory)
    deep_prompt = make_deep_research_prompt(cycle, candidate, inventory)
    fact_prompt = make_factcheck_prompt(cycle, candidate, inventory)
    codex_prompt = make_codex_review_prompt(cycle, candidate, inventory)
    write_text(SPRINT / "briefs" / f"cycle_{cycle:02d}_hwao_director_prompt.md", hwao_prompt)
    write_text(SPRINT / "briefs" / f"cycle_{cycle:02d}_gemini_deep_research_prompt.md", deep_prompt)
    write_text(SPRINT / "briefs" / f"cycle_{cycle:02d}_gemini_source_factcheck_prompt.md", fact_prompt)
    write_text(SPRINT / "briefs" / f"cycle_{cycle:02d}_codex_kun_prompt.md", codex_prompt)

    report_paths = [
        SPRINT / "lanes/hwao" / f"ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_{cycle:02d}.md",
        SPRINT / "lanes/gemini_deep_research" / f"ACTUAL_RESEARCH_GEMINI_DEEP_RESEARCH_CYCLE_{cycle:02d}.md",
        SPRINT / "lanes/gemini_source_factcheck" / f"ACTUAL_RESEARCH_GEMINI_SOURCE_FACTCHECK_CYCLE_{cycle:02d}.md",
        SPRINT / "lanes/codex_kun" / f"ACTUAL_RESEARCH_CODEX_KUN_REVIEW_CYCLE_{cycle:02d}.md",
        SPRINT / "lanes/goru_real_data" / f"ACTUAL_RESEARCH_GORU_REAL_DATA_REPORT_CYCLE_{cycle:02d}.md",
    ]
    remaining = lambda: min(PER_LANE_TIMEOUT, int(max(60, hard_end - time.time())))
    lane_results: List[Dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        futures = [
            ex.submit(run_cmd, f"hwao-agy-low-cycle-{cycle}", ["agy", "--model", "Gemini 3.1 Pro (Low)", "--mode", "plan", "--print-timeout", "75m0s", "--print", hwao_prompt], report_paths[0], remaining(), REPO),
            ex.submit(run_cmd, f"gemini-deep-research-low-cycle-{cycle}", ["agy", "--model", "Gemini 3.1 Pro (Low)", "--mode", "plan", "--print-timeout", "75m0s", "--print", deep_prompt], report_paths[1], remaining(), REPO),
            ex.submit(run_cmd, f"gemini-source-factcheck-flash-low-cycle-{cycle}", ["agy", "--model", "Gemini 3.5 Flash (Low)", "--mode", "plan", "--print-timeout", "75m0s", "--print", fact_prompt], report_paths[2], remaining(), REPO),
            ex.submit(run_cmd, f"codex-kun-readonly-cycle-{cycle}", ["codex", "exec", "-m", "gpt-5.4-mini", "--sandbox", "read-only", "--cd", str(REPO), codex_prompt], report_paths[3], remaining(), REPO),
        ]
        for fut in futures:
            lane_results.append(fut.result())
    goru_report = goru_real_data_report(cycle, candidate, inventory, report_paths[4])
    ledger(f"cycle {cycle}: review lanes finished; exits={[r.get('exit_code') for r in lane_results]}; real-data csv={inventory.get('counts', {}).get('csv_files')} json={inventory.get('counts', {}).get('json_files')}")

    integ_prompt = make_integrator_prompt(cycle, candidate, report_paths)
    write_text(SPRINT / "briefs" / f"cycle_{cycle:02d}_integrator_prompt.md", integ_prompt)
    integ_result = run_cmd(
        f"codex-integrator-actual-research-cycle-{cycle}",
        ["codex", "exec", "-m", "gpt-5.4-mini", "--sandbox", "workspace-write", "--cd", str(candidate), "--skip-git-repo-check", integ_prompt],
        SPRINT / "lanes/integrator" / f"INTEGRATOR_ACTUAL_RESEARCH_CYCLE_{cycle:02d}.log",
        min(INTEGRATOR_TIMEOUT, int(max(60, hard_end - time.time()))),
        candidate,
    )
    ledger(f"cycle {cycle}: integrator finished exit={integ_result.get('exit_code')}")

    compile_results = [compile_tex(candidate / FLAGSHIP_REL), compile_tex(candidate / SUPPLEMENT_REL)]
    audit = audit_candidate(cycle, candidate, compile_results, goru_report)
    summary = {"cycle": cycle, "candidate": str(candidate), "lane_results": lane_results, "integrator_result": integ_result, "audit": audit, "finished_utc": utc_now()}
    write_text(candidate / f"CYCLE_{cycle:02d}_ACTUAL_RESEARCH_SUMMARY.json", json.dumps(summary, indent=2, sort_keys=True))
    md = [
        f"# Actual-research cycle {cycle} summary",
        "",
        f"Marker: `ACTUAL_RESEARCH_CYCLE_SUMMARY_{cycle:02d}`",
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
        "",
        "## Real-data policy",
        *[f"- {x}" for x in REAL_DATA_POLICY],
        "",
        "## Safety",
        *[f"- {x}" for x in LOCKS],
    ]
    write_text(candidate / f"CYCLE_{cycle:02d}_ACTUAL_RESEARCH_SUMMARY.md", "\n".join(md) + "\n")
    ledger(f"cycle {cycle}: audit fatal_failures={len(audit['fatal_failures'])}; compile_ok={[r.get('ok') for r in compile_results]}")
    return candidate, summary


def write_final(cycles: List[Dict[str, Any]], latest: Path | None, start_utc: str, end_utc: str) -> None:
    final = {"sprint_id": SPRINT_ID, "started_utc": start_utc, "target_end_utc": end_utc, "finished_utc": utc_now(), "cycles_completed": len(cycles), "latest_candidate": str(latest) if latest else None, "real_data_policy": REAL_DATA_POLICY, "safety_locks": LOCKS, "cycles": cycles}
    write_text(SPRINT / "FINAL_ACTUAL_RESEARCH_JOURNAL_SPRINT_HANDOFF.json", json.dumps(final, indent=2, sort_keys=True))
    lines = [
        "# Actual-data journal-paper quality sprint final handoff",
        "",
        f"Marker: `{SPRINT_ID}_FINAL_HANDOFF`",
        f"Started UTC: {start_utc}",
        f"Target end UTC: {end_utc}",
        f"Finished UTC: {utc_now()}",
        f"Cycles completed: {len(cycles)}",
        "",
        "## Latest candidate",
        "",
        f"`{latest}`" if latest else "none",
        "",
    ]
    if latest:
        for p in [latest / FLAGSHIP_REL, latest / "flagship_rp1/aastex/rp1_flagship_polished.pdf", latest / SUPPLEMENT_REL, latest / "supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf"]:
            lines.append(f"- `{p}` exists={p.exists()} sha256={sha256(p) if p.exists() and p.is_file() else None}")
    lines += ["", "## Cycle receipts"]
    for c in cycles:
        audit = c.get("audit", {})
        lines.append(f"- cycle {c.get('cycle')}: candidate `{c.get('candidate')}` fatal_failures={len(audit.get('fatal_failures', []))}")
    lines += ["", "## Real-data-only policy", *[f"- {x}" for x in REAL_DATA_POLICY], "", "## Safety ledger", *[f"- {x}" for x in LOCKS], "", "No public replacement/publish was performed. Hwao/Lana/user review remains the next gate before any public update or submission."]
    write_text(SPRINT / "FINAL_ACTUAL_RESEARCH_JOURNAL_SPRINT_HANDOFF.md", "\n".join(lines) + "\n")
    update_status(state="completed", cycles_completed=len(cycles), latest_candidate=str(latest) if latest else None, final_handoff=str(SPRINT / "FINAL_ACTUAL_RESEARCH_JOURNAL_SPRINT_HANDOFF.md"))


def main() -> int:
    SPRINT.mkdir(parents=True, exist_ok=True)
    if not SOURCE_PACKAGE.exists():
        update_status(state="blocked_missing_source_package", source_package=str(SOURCE_PACKAGE))
        raise SystemExit(f"Missing source package: {SOURCE_PACKAGE}")
    start_utc = utc_now()
    hard_end = time.time() + DURATION_SECONDS
    end_utc = dt.datetime.fromtimestamp(hard_end, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    prepare_static_files(start_utc, end_utc)
    write_text(SPRINT / "RUNNING.pid", str(os.getpid()) + "\n")
    update_status(state="starting", pid=os.getpid(), started_utc=start_utc, target_end_utc=end_utc, source_package=str(SOURCE_PACKAGE), integrated_root=str(INTEGRATED_ROOT))
    ledger("sprint started")
    for cmd in ["agy", "codex", "tectonic"]:
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
            update_status(state="between_cycles", cycle=cycle, cycles_completed=len(cycles), latest_candidate=str(latest))
        except Exception as exc:
            ledger(f"cycle {cycle}: fatal orchestrator exception {type(exc).__name__}: {exc}")
            append(SPRINT / "logs/orchestrator_exceptions.log", f"{utc_now()} cycle {cycle}: {type(exc).__name__}: {exc}\n")
            update_status(state="cycle_exception", cycle=cycle, error=f"{type(exc).__name__}: {exc}")
        cycle += 1
    write_final(cycles, latest, start_utc, end_utc)
    ledger("sprint completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
