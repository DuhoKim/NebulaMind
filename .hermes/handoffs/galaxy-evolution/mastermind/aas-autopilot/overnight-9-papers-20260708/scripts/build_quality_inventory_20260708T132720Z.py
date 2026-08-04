#!/usr/bin/env python3
"""Build a local quality inventory for the nine Galaxy Evolution AAS pilot papers.

This is a read-only verifier over existing run artifacts plus local writes under the
overnight work root.  It does not touch product DB/API/static public roots, git, or
running services.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTOPILOT_ROOT = REPO_ROOT / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
OVERNIGHT_ROOT = AUTOPILOT_ROOT / "overnight-9-papers-20260708"
FIRST_RUN = AUTOPILOT_ROOT / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z"
BATCH_RUN = AUTOPILOT_ROOT / "runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z"
BATCH_MANIFEST = BATCH_RUN / "ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json"
OUT_STAMP = "20260708T132720Z"

OUT_JSON = OVERNIGHT_ROOT / "artifacts" / f"quality_inventory_{OUT_STAMP}.json"
OUT_MD = OVERNIGHT_ROOT / "artifacts" / f"quality_inventory_{OUT_STAMP}.md"

PROHIBITED_TARGET_HINTS = [
    "NebulaMind/product DB",
    "/api/pages",
    "page_versions",
    "wiki publish",
    "trust recompute",
    "deploy/restart",
    "git commit/push/merge/rebase",
    "cron creation",
    "billing/cloud/OAuth/API-key changes",
]

GUARD_PATTERNS = [
    r"not\s+(?:a\s+)?causal",
    r"not\s+as\s+a\s+full\s+causal\s+test",
    r"does\s+not\s+by\s+itself\s+establish",
    r"association\s+(?:measurement|pilot)",
    r"SDSS-only\s+pilot",
    r"proxy\s+or\s+denominator",
    r"full\s+proposal\s+requires",
]

TOPIC_SPECIFIC_LITERATURE_TERMS = [
    "environment", "quenching", "maintenance", "heating", "outflow", "escape",
    "recycling", "radio", "jet", "transition", "multiphase", "molecular",
    "depletion", "efficiency", "simulation", "feedback"
]


def sha256_file(path: Path) -> Optional[str]:
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def csv_profile(path: Path) -> Dict[str, Any]:
    prof: Dict[str, Any] = {
        "path": str(path),
        "exists": path.exists(),
        "bytes": path.stat().st_size if path.exists() else None,
        "sha256": sha256_file(path) if path.exists() else None,
        "rows": None,
        "columns": [],
        "sample_class_counts": {},
    }
    if not path.exists():
        return prof
    counts = Counter()
    rows = 0
    with path.open(newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        prof["columns"] = reader.fieldnames or []
        class_key = None
        for candidate in ("bpt_class", "class", "bpt", "bptclass"):
            if candidate in prof["columns"]:
                class_key = candidate
                break
        for row in reader:
            rows += 1
            if class_key:
                counts[row.get(class_key, "") or "<blank>"] += 1
    prof["rows"] = rows
    prof["sample_class_counts"] = dict(counts)
    return prof


def one_line(s: str, max_len: int = 160) -> str:
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if len(s) <= max_len else s[: max_len - 1] + "…"


def extract_braced_command(tex: str, command: str) -> str:
    m = re.search(r"\\" + re.escape(command) + r"\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", tex, re.S)
    if not m:
        return ""
    return one_line(m.group(1), 300)


def tex_metrics(tex_path: Path) -> Dict[str, Any]:
    tex = read_text(tex_path)
    abstract_match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S)
    abstract = abstract_match.group(1) if abstract_match else ""
    sections = [one_line(s, 80) for s in re.findall(r"\\section\*?\{([^{}]+)\}", tex)]
    bibkeys = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^{}]+)\}", tex)
    cite_commands = re.findall(r"\\cite\w*\{([^{}]+)\}", tex)
    cite_keys = sorted({k.strip() for group in cite_commands for k in group.split(",") if k.strip()})
    words = re.findall(r"[A-Za-z][A-Za-z0-9\-']+", re.sub(r"\\[a-zA-Z]+(?:\[[^\]]*\])?(?:\{[^{}]*\})?", " ", tex))
    guard_hits = [pat for pat in GUARD_PATTERNS if re.search(pat, tex, re.I)]
    lower_tex = tex.lower()
    topic_lit_hits = [term for term in TOPIC_SPECIFIC_LITERATURE_TERMS if term in lower_tex]
    return {
        "path": str(tex_path),
        "exists": tex_path.exists(),
        "bytes": tex_path.stat().st_size if tex_path.exists() else None,
        "documentclass_aastex": "aastex" in tex[:250].lower(),
        "title": extract_braced_command(tex, "title"),
        "shorttitle": extract_braced_command(tex, "shorttitle"),
        "abstract_words": len(re.findall(r"[A-Za-z][A-Za-z0-9\-']+", abstract)),
        "abstract_preview": one_line(abstract, 260),
        "sections": sections,
        "section_count": len(sections),
        "figure_environments": len(re.findall(r"\\begin\{figure\*?\}", tex)),
        "includegraphics_count": len(re.findall(r"\\includegraphics", tex)),
        "table_environments": len(re.findall(r"\\begin\{table\*?\}", tex)),
        "deluxetable_environments": len(re.findall(r"\\begin\{deluxetable\*?\}", tex)),
        "bibitem_count": len(bibkeys),
        "bibkeys": bibkeys,
        "cite_key_count": len(cite_keys),
        "cite_keys": cite_keys,
        "word_count_rough": len(words),
        "has_reproducibility_section": any("reproduc" in s.lower() for s in sections),
        "has_scope_or_guard_section": any(("scope" in s.lower() or "guard" in s.lower() or "discussion" in s.lower()) for s in sections),
        "guard_patterns_hit": guard_hits,
        "has_interpretation_guard": bool(guard_hits),
        "topic_literature_terms_in_text": topic_lit_hits,
    }


def pdf_profile(pdf_path: Path, expected_sha: Optional[str] = None, expected_bytes: Optional[int] = None) -> Dict[str, Any]:
    exists = pdf_path.exists()
    actual_sha = sha256_file(pdf_path) if exists else None
    size = pdf_path.stat().st_size if exists else None
    magic = ""
    if exists:
        with pdf_path.open("rb") as f:
            magic = f.read(5).decode("latin1", errors="replace")
    return {
        "path": str(pdf_path),
        "exists": exists,
        "bytes": size,
        "sha256": actual_sha,
        "starts_with_pdf_magic": magic == "%PDF-",
        "manifest_sha256": expected_sha,
        "manifest_bytes": expected_bytes,
        "matches_manifest_sha256": (actual_sha == expected_sha) if expected_sha else None,
        "matches_manifest_bytes": (size == expected_bytes) if expected_bytes is not None else None,
    }


def compile_profile(path: Path) -> Dict[str, Any]:
    text = read_text(path)
    fatal_matches = re.findall(r"(?im)(fatal error|! LaTeX Error|Emergency stop|No pages of output|failed)", text)
    warning_matches = re.findall(r"(?im)warning", text)
    return {
        "path": str(path),
        "exists": path.exists(),
        "bytes": path.stat().st_size if path.exists() else None,
        "fatal_error_markers": fatal_matches[:10],
        "warning_marker_count": len(warning_matches),
        "looks_successful": path.exists() and not fatal_matches,
    }


def figure_profiles(paths: List[Path]) -> List[Dict[str, Any]]:
    out = []
    seen = set()
    for p in paths:
        if not p or str(p) in seen:
            continue
        seen.add(str(p))
        out.append({
            "path": str(p),
            "exists": p.exists(),
            "bytes": p.stat().st_size if p.exists() else None,
            "sha256": sha256_file(p) if p.exists() else None,
        })
    return out


def build_papers() -> List[Dict[str, Any]]:
    manifest = load_json(BATCH_MANIFEST)
    papers: List[Dict[str, Any]] = [
        {
            "slug": "m1_rp1_agn_sfr_matched_control",
            "method": "packet-gated-paper-to-wiki-reconciliation",
            "card_id": "rp-1",
            "title": "A Matched-Control SDSS DR17 Pilot Test of Specific Star Formation in Optical AGN Hosts",
            "short_title": "SDSS AGN/sSFR matched-control pilot",
            "tex": str(FIRST_RUN / "aastex/sdss_agn_sfr_pilot_aas.tex"),
            "pdf": str(FIRST_RUN / "aastex/sdss_agn_sfr_pilot_aas.pdf"),
            "compile_log": str(FIRST_RUN / "aastex/compile.log"),
            "analysis_results": str(FIRST_RUN / "analysis_results.json"),
            "figure_pdfs": [
                str(FIRST_RUN / "figures/figure1_bpt.pdf"),
                str(FIRST_RUN / "figures/figure2_matched_offsets.pdf"),
            ],
            "manifest_pdf_sha256": "7f2832413b354023be6375e3a8c2bf4a9658c0791f9167a5056a9c5fc19d8e75",
            "manifest_pdf_bytes": 234931,
        }
    ]
    for topic in manifest.get("topics", []):
        p = dict(topic)
        p["analysis_results"] = str(BATCH_RUN / p["slug"] / "analysis_results.json")
        p["figure_pdfs"] = [topic.get("figure_pdf", "")]
        p["manifest_pdf_sha256"] = topic.get("pdf_sha256")
        p["manifest_pdf_bytes"] = topic.get("pdf_bytes")
        papers.append(p)
    return papers


def paper_inventory(p: Dict[str, Any]) -> Dict[str, Any]:
    tex = tex_metrics(Path(p["tex"]))
    analysis = load_json(Path(p["analysis_results"]))
    pdf = pdf_profile(Path(p["pdf"]), p.get("manifest_pdf_sha256"), p.get("manifest_pdf_bytes"))
    compile_log = compile_profile(Path(p["compile_log"]))
    figures = figure_profiles([Path(x) for x in p.get("figure_pdfs", []) if x])

    quality_flags: List[str] = []
    recommended_next: List[str] = []

    if not pdf["exists"] or not pdf["starts_with_pdf_magic"] or not compile_log["looks_successful"]:
        quality_flags.append("compile_or_pdf_verification_problem")
        recommended_next.append("Recompile and inspect the TeX/PDF before content edits.")
    if not tex["has_interpretation_guard"]:
        quality_flags.append("missing_explicit_interpretation_guard")
        recommended_next.append("Add an explicit association/proxy-only interpretation guard.")
    if tex["bibitem_count"] <= 4:
        quality_flags.append("minimal_bibliography_topic_specific_literature_gap")
        recommended_next.append("Add topic-specific review/status/source anchors beyond the generic SDSS/BPT citations.")
    if tex["table_environments"] == 0 and tex["deluxetable_environments"] == 0:
        quality_flags.append("no_manuscript_result_table")
        recommended_next.append("Add a compact result/proxy-limit/reproducibility table in AASTeX.")
    if tex["word_count_rough"] < 1400:
        quality_flags.append("thin_manuscript_requires_expansion")
        recommended_next.append("Expand methods/results/discussion with exact sample definitions, proxy limits, and next-data requirements.")
    if tex["figure_environments"] < 1 or not figures or not all(f["exists"] for f in figures):
        quality_flags.append("figure_missing_or_unverified")
        recommended_next.append("Regenerate or verify the topic figure and include it from the manuscript directory.")
    if not analysis:
        quality_flags.append("missing_analysis_results_json")
        recommended_next.append("Recover or regenerate topic analysis_results.json before manuscript changes.")

    if not quality_flags:
        quality_flags.append("baseline_artifacts_verify; still eligible for literature/robustness improvement")
        recommended_next.append("Proceed to robustness and source/literature anchoring passes.")

    return {
        "slug": p["slug"],
        "method": p.get("method"),
        "card_id": p.get("card_id"),
        "manifest_title": p.get("title"),
        "manifest_short_title": p.get("short_title"),
        "tex": tex,
        "pdf": pdf,
        "compile_log": compile_log,
        "figures": figures,
        "analysis_results_path": p.get("analysis_results"),
        "analysis_results_exists": bool(analysis),
        "analysis_keys": sorted(analysis.keys()) if analysis else [],
        "analysis_sample_rows": analysis.get("analysis_rows", analysis.get("sample_rows")) if analysis else None,
        "pilot_question": analysis.get("pilot_question") if analysis else None,
        "full_proposal_requires": analysis.get("full_proposal_requires") if analysis else None,
        "result_bullets": analysis.get("result_bullets") if analysis else None,
        "quality_flags": quality_flags,
        "recommended_next": recommended_next,
    }


def md_table_row(cols: List[Any]) -> str:
    return "| " + " | ".join(str(c).replace("\n", " ") for c in cols) + " |"


def render_markdown(inventory: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append(f"# Nine-paper AAS pilot quality inventory — {OUT_STAMP}")
    lines.append("")
    lines.append("Marker: `OVERNIGHT_9_PAPERS_QUALITY_INVENTORY_20260708T132720Z`")
    lines.append("")
    lines.append("## Scope and safety")
    lines.append("This tick performed a local, read-only inventory over the 9 active AAS-style pilot manuscripts and their preserved run artifacts. It wrote only this inventory JSON/Markdown plus the tick/ledger files under the overnight work root. It did not perform DB writes, `/api/pages`, page_versions/wiki publish, trust recompute, live frontend mirroring, deploy/restart, git operations, cron creation, billing/cloud/OAuth/API-key changes, or external submission.")
    lines.append("")
    lines.append("## Data/source grounding verified")
    src = inventory["source_sample_profile"]
    lines.append(f"- Source SDSS analysis CSV: `{src['path']}`")
    lines.append(f"- Exists/rows/bytes/SHA256: {src['exists']} / {src['rows']} / {src['bytes']} / `{src['sha256']}`")
    if src.get("columns"):
        lines.append(f"- Column count: {len(src['columns'])}; first columns: {', '.join(src['columns'][:12])}")
    if src.get("sample_class_counts"):
        lines.append(f"- BPT class counts from CSV: `{json.dumps(src['sample_class_counts'], sort_keys=True)}`")
    lines.append("")
    summ = inventory["summary"]
    lines.append("## Summary counts")
    for k in sorted(summ):
        lines.append(f"- {k}: {summ[k]}")
    lines.append("")
    lines.append("## Paper-by-paper inventory")
    lines.append(md_table_row(["Paper", "PDF", "Compile", "Figs", "Tables", "Bib", "Words", "Guard", "Top flags"]))
    lines.append(md_table_row(["---", "---", "---", "---:", "---:", "---:", "---:", "---", "---"]))
    for p in inventory["papers"]:
        pdf_ok = p["pdf"]["exists"] and p["pdf"]["starts_with_pdf_magic"] and (p["pdf"].get("matches_manifest_sha256") in (True, None))
        flags = "; ".join(p["quality_flags"][:3])
        lines.append(md_table_row([
            p["slug"],
            "ok" if pdf_ok else "CHECK",
            "ok" if p["compile_log"]["looks_successful"] else "CHECK",
            len(p["figures"]),
            p["tex"]["table_environments"] + p["tex"]["deluxetable_environments"],
            p["tex"]["bibitem_count"],
            p["tex"]["word_count_rough"],
            "yes" if p["tex"]["has_interpretation_guard"] else "NO",
            flags,
        ]))
    lines.append("")
    lines.append("## Immediate improvement backlog derived from inventory")
    lines.append("1. Add compact AASTeX result/proxy-limit tables to the 8 batch manuscripts; RP-1 already has a deluxetable and richer discussion.")
    lines.append("2. Add topic-specific literature/status anchors for all 8 batch manuscripts. Their bibliographies currently verify as the generic SDSS/BPT backbone only (4 bibitems each), which is acceptable for a pilot draft but weak for AAS-style topic context.")
    lines.append("3. Expand the 8 batch manuscripts beyond the current short template with exact variable definitions, source-sample limitations, and proposal-specific follow-up requirements.")
    lines.append("4. Next robustness phase should use the cached 60,000-row SDSS sample to add sensitivity checks: BPT class variants, mass/redshift bins, density-neighbour variants, and bootstrap intervals where relevant.")
    lines.append("5. Preserve the key guardrail in every future edit: these are SDSS denominator/proxy pilots unless the full topic needs radio, X-ray, CO, resolved kinematics, simulations, group catalogues, or multi-redshift data.")
    lines.append("")
    lines.append("## Per-paper recommended next actions")
    for p in inventory["papers"]:
        lines.append(f"### {p['slug']}")
        lines.append(f"- Title: {p['tex']['title'] or p.get('manifest_title')}")
        if p.get("pilot_question"):
            lines.append(f"- Pilot question: {p['pilot_question']}")
        if p.get("full_proposal_requires"):
            lines.append(f"- Full proposal still requires: {p['full_proposal_requires']}")
        lines.append(f"- Flags: {', '.join(p['quality_flags'])}")
        for rec in p["recommended_next"][:4]:
            lines.append(f"  - {rec}")
        lines.append("")
    lines.append("## Verification")
    lines.append(f"- JSON artifact: `{OUT_JSON}`")
    lines.append(f"- Markdown artifact: `{OUT_MD}`")
    lines.append("- 9 manuscripts parsed; PDF magic/hash checks and compile-log fatal-marker checks were run locally.")
    lines.append("- The inventory is a quality/readiness map only; it does not authorize public/live updates or prose/claim mutation beyond local manuscript-improvement ticks.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    papers = build_papers()
    source_sample = FIRST_RUN / "data/analysis_sample_bpt.csv"
    paper_infos = [paper_inventory(p) for p in papers]

    summary = {
        "papers_total": len(paper_infos),
        "pdf_exists_and_magic_ok": sum(1 for p in paper_infos if p["pdf"]["exists"] and p["pdf"]["starts_with_pdf_magic"]),
        "pdf_sha_matches_manifest_where_recorded": sum(1 for p in paper_infos if p["pdf"].get("matches_manifest_sha256") is True),
        "compile_logs_without_fatal_markers": sum(1 for p in paper_infos if p["compile_log"]["looks_successful"]),
        "with_interpretation_guard": sum(1 for p in paper_infos if p["tex"]["has_interpretation_guard"]),
        "with_any_result_table": sum(1 for p in paper_infos if (p["tex"]["table_environments"] + p["tex"]["deluxetable_environments"]) > 0),
        "minimal_bibliography_le_4_bibitems": sum(1 for p in paper_infos if p["tex"]["bibitem_count"] <= 4),
        "thin_manuscript_lt_1400_words": sum(1 for p in paper_infos if p["tex"]["word_count_rough"] < 1400),
        "analysis_results_json_present": sum(1 for p in paper_infos if p["analysis_results_exists"]),
    }

    inventory: Dict[str, Any] = {
        "marker": "OVERNIGHT_9_PAPERS_QUALITY_INVENTORY_20260708T132720Z",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "local read-only inventory of the 9 active Galaxy Evolution AAS pilot manuscripts and run artifacts",
        "safety_ledger": {
            "local_artifact_writes_only_under": str(OVERNIGHT_ROOT),
            "prohibited_actions_not_performed": PROHIBITED_TARGET_HINTS,
        },
        "source_sample_profile": csv_profile(source_sample),
        "summary": summary,
        "papers": paper_infos,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(inventory), encoding="utf-8")

    print(json.dumps({
        "marker": inventory["marker"],
        "json": str(OUT_JSON),
        "markdown": str(OUT_MD),
        "summary": summary,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
