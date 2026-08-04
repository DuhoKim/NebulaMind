#!/usr/bin/env python3
"""Build a lane-local Wave-3 citation-placement/source-grounding packet.

Network scope: public arXiv REST API and optional public Semantic Scholar Graph API.
Write scope: lanes/literature only.
"""
from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TIMESTAMP = "20260708T233709Z"
ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature")
RAW = ROOT / "raw_payloads" / TIMESTAMP
RAW.mkdir(parents=True, exist_ok=True)
(ROOT / "ticks").mkdir(parents=True, exist_ok=True)

# These are papers already visible in the Wave-3 lane-local drafts plus a few
# targeted guardrail additions.  Every source is public arXiv-resolvable.
SOURCES = [
    # M1 RP-1: SDSS optical AGN/sSFR matched-control pilot
    {
        "key": "abdurrouf2022_sdss_dr17",
        "arxiv": "2112.02026",
        "papers": ["m1_rp1_sdss_agn_sfr", "m2_p3_feedback_transition_mass", "m3_p1_multiphase_census"],
        "placement": "Data/sample provenance for SDSS DR17; cite wherever the public SDSS release is named.",
        "relevance": "Grounds the survey release used by the cached DR17 optical-denominator analysis.",
        "support_class": "supports_actual_method_or_data_provenance",
    },
    {
        "key": "brinchmann2004_physical_properties",
        "arxiv": "astro-ph/0311060",
        "papers": ["m1_rp1_sdss_agn_sfr"],
        "placement": "Data/sample and Discussion paragraphs on catalog stellar mass and SFR/sSFR estimator assumptions.",
        "relevance": "Documents SDSS low-redshift physical-property/SFR context; helps keep the RP-1 offset framed as a catalog-sSFR association.",
        "support_class": "supports_actual_method_or_data_provenance",
    },
    {
        "key": "kewley2006_agn_classification",
        "arxiv": "astro-ph/0605681",
        "papers": ["m1_rp1_sdss_agn_sfr"],
        "placement": "Classification and Discussion guardrail after broad BPT-AGN definition.",
        "relevance": "Explains AGN host classification and Seyfert/LINER branches; supports subclass/retired-ionization caveats, not the feedback conclusion.",
        "support_class": "supports_actual_method_guardrail",
    },
    {
        "key": "stasinska2015_retired_not_forgotten",
        "arxiv": "1501.03812",
        "papers": ["m1_rp1_sdss_agn_sfr"],
        "placement": "Discussion caveat on LINER-like or retired-galaxy ionization contaminating broad BPT-AGN labels.",
        "relevance": "Direct guardrail for interpreting optical line-ratio AGN in low-sSFR systems; it weakens causal language rather than supporting it.",
        "support_class": "supports_interpretation_guardrail",
    },
    {
        "key": "stasinska2008_retired_mimic_active",
        "arxiv": "0809.1341",
        "papers": ["m1_rp1_sdss_agn_sfr"],
        "placement": "Optional added citation beside the retired/LINER caution if the manuscript needs a more explicit retired-galaxy anchor.",
        "relevance": "Motivates not treating all AGN-looking line ratios as accreting AGN feedback signatures.",
        "support_class": "supports_interpretation_guardrail",
    },
    {
        "key": "lamassa2013_sf_agn_connection",
        "arxiv": "1302.2631",
        "papers": ["m1_rp1_sdss_agn_sfr"],
        "placement": "Introduction as motivation for a low-redshift AGN--star-formation association test.",
        "relevance": "Useful context for RP-1, but does not validate the cached SDSS result or causal feedback.",
        "support_class": "motivates_future_or_context_only",
    },
    # M2 P3: mass transition / low-sSFR and optical AGN incidence
    {
        "key": "kauffmann2003_stellar_masses",
        "arxiv": "astro-ph/0204055",
        "papers": ["m2_p3_feedback_transition_mass"],
        "placement": "Scope/source grounding for the SDSS stellar-mass axis and catalog physical-property context.",
        "relevance": "Supports use of stellar mass as an empirical axis in the SDSS denominator; not a feedback-regime proof.",
        "support_class": "supports_actual_method_or_data_provenance",
    },
    {
        "key": "kauffmann2003_sfh_structure_mass",
        "arxiv": "astro-ph/0205070",
        "papers": ["m2_p3_feedback_transition_mass"],
        "placement": "Scope/source grounding where the manuscript motivates stellar mass and structure as transition variables.",
        "relevance": "Anchors the mass/structure dependence of low-redshift galaxy star-formation histories; motivates but does not prove the physical transition.",
        "support_class": "motivates_context_and_guardrail",
    },
    {
        "key": "baldry2004_bimodal_colour",
        "arxiv": "astro-ph/0309710",
        "papers": ["m2_p3_feedback_transition_mass"],
        "placement": "Introduction/source grounding for bimodality/transition framing.",
        "relevance": "Motivates mass-binned low-sSFR/colour-transition diagnostics; not evidence for AGN causality.",
        "support_class": "motivates_context_only",
    },
    {
        "key": "peng2010_mass_environment_i",
        "arxiv": "1003.4747",
        "papers": ["m2_p3_feedback_transition_mass"],
        "placement": "Interpretation guard separating mass and environment quenching channels.",
        "relevance": "Supports caution that mass-linked and environmental effects must be decomposed before attributing the SDSS mass vector to AGN feedback.",
        "support_class": "supports_interpretation_guardrail",
    },
    {
        "key": "peng2012_mass_environment_ii_satellite_quenching",
        "arxiv": "1106.2546",
        "papers": ["m2_p3_feedback_transition_mass"],
        "placement": "Future-data/interpretation guard for central-satellite and environment separation.",
        "relevance": "Shows why a transition-mass claim needs central/satellite/environment labels; motivates future data only for this pilot.",
        "support_class": "motivates_future_data_only",
    },
    {
        "key": "dekel2006_bimodality_shock_heating",
        "arxiv": "astro-ph/0412300",
        "papers": ["m2_p3_feedback_transition_mass"],
        "placement": "Interpretation guard where halo shock/hot-mode language appears.",
        "relevance": "Motivates a halo-scale physical mechanism that the current SDSS optical table cannot test directly.",
        "support_class": "motivates_future_data_only",
    },
    {
        "key": "bluck2023_bh_mass_quenching_signature",
        "arxiv": "2301.03677",
        "papers": ["m2_p3_feedback_transition_mass"],
        "placement": "Future-data paragraph requiring black-hole mass or velocity-dispersion information.",
        "relevance": "Supports the manuscript guard that optical AGN incidence is not a substitute for black-hole-mass or accretion-history information.",
        "support_class": "motivates_future_data_only",
    },
    {
        "key": "piotrowska2021_integrated_agn_feedback",
        "arxiv": "2112.07672",
        "papers": ["m2_p3_feedback_transition_mass"],
        "placement": "Optional future-data/interpretation citation for integrated AGN-feedback tests in central galaxies.",
        "relevance": "Useful as a comparator for a later physical-transition analysis; does not support the current optical-denominator result by itself.",
        "support_class": "motivates_future_data_only",
    },
    # M3 P1: common-denominator optical tracer census
    {
        "key": "veilleux2005_galactic_winds_review",
        "arxiv": None,
        "doi": "10.1146/annurev.astro.43.072103.150610",
        "papers": ["m3_p1_multiphase_census"],
        "placement": "Scope/source grounding for why real outflow census work is multiphase/kinematic.",
        "relevance": "Review-level anchor for physical wind observables; motivates future data rather than validating SDSS optical thresholds.",
        "support_class": "motivates_future_data_only",
    },
    {
        "key": "rupke2018_galactic_winds_review",
        "arxiv": "1812.05184",
        "papers": ["m3_p1_multiphase_census"],
        "placement": "Scope/source grounding beside Veilleux review; clarifies that tracer prevalence needs phase/kinematic definitions.",
        "relevance": "Review anchor for wind observations; supports interpretation guard, not the current SDSS prevalence as outflows.",
        "support_class": "supports_interpretation_guardrail",
    },
    {
        "key": "cicone2014_molecular_outflows",
        "arxiv": "1311.2595",
        "papers": ["m3_p1_multiphase_census"],
        "placement": "Future-data paragraph requiring molecular gas measurements.",
        "relevance": "Concrete molecular-outflow anchor showing what the current SDSS optical table lacks.",
        "support_class": "motivates_future_data_only",
    },
    {
        "key": "fiore2017_agn_wind_scaling",
        "arxiv": "1702.04507",
        "papers": ["m3_p1_multiphase_census"],
        "placement": "Future-data paragraph on wind scalings, velocities, and energetics.",
        "relevance": "Motivates comparing wind quantities across phases; not evidence that SDSS line-ratio flags are outflows.",
        "support_class": "motivates_future_data_only",
    },
    {
        "key": "feruglio2015_multiphase_mrk231",
        "arxiv": "1503.01481",
        "papers": ["m3_p1_multiphase_census"],
        "placement": "Future-data paragraph or caveat that single-object multiphase detections are physics anchors, not denominator prevalence.",
        "relevance": "Illustrates multiphase measurements beyond SDSS optical ratios; should not be used as a population prevalence anchor.",
        "support_class": "motivates_future_data_only",
    },
    {
        "key": "woo2016_prevalence_type2_agn_outflows",
        "arxiv": "1511.05142",
        "papers": ["m3_p1_multiphase_census"],
        "placement": "Cautionary prevalence/context citation for ionized-gas outflows in Type 2 AGN.",
        "relevance": "Relevant to future denominator design; its sample/selection should not be merged with the cached SDSS optical threshold fractions.",
        "support_class": "motivates_future_data_only",
    },
    {
        "key": "bae2018_neutral_ionized_independence",
        "arxiv": "1712.08944",
        "papers": ["m3_p1_multiphase_census"],
        "placement": "Future-data paragraph requiring separate neutral and ionized outflow measurements.",
        "relevance": "Directly supports the guardrail that one phase/tracer cannot stand in for a multiphase census.",
        "support_class": "supports_interpretation_guardrail",
    },
]

LOCAL_INPUTS_READ = [
    "OVERNIGHT_BRIEF.md",
    "SWARM_BOARD.md",
    "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/aastex/sdss_agn_sfr_pilot_aas.tex",
    "runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_aas.tex",
    "runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_aas.tex",
    "lanes/lana/revision-drafts/m1_rp1_sdss_agn_sfr/aastex/sdss_agn_sfr_pilot_lana_control_baseline_20260708T204532Z.tex",
    "lanes/lana/revision-drafts/m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_lana_claim_contract_20260708T204532Z.tex",
    "lanes/lana/revision-drafts/m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_lana_threshold_contract_20260708T204532Z.tex",
    "topic pages/current+backup under frontend/public/agent-reports/wiki-method-results/galaxy-evolution/",
]


def fetch(url: str, *, data: bytes | None = None, headers: dict[str, str] | None = None, timeout: int = 60) -> tuple[int, bytes, dict[str, str]]:
    req = urllib.request.Request(url, data=data, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read(), dict(resp.headers)
    except urllib.error.HTTPError as e:
        return e.code, e.read(), dict(e.headers)


def arxiv_id_list(ids: list[str]) -> dict[str, Any]:
    if not ids:
        return {"status": "not_requested", "entries": {}}
    query = ",".join(urllib.parse.quote(i, safe="/") for i in ids)
    url = f"https://export.arxiv.org/api/query?id_list={query}&max_results={len(ids)+5}"
    status, body, headers = fetch(url)
    (RAW / "wave3_citation_placement_arxiv_id_list.xml").write_bytes(body)
    (RAW / "wave3_citation_placement_arxiv_status.json").write_text(json.dumps({"url": url, "status": status, "headers_subset": {k: headers.get(k) for k in ["date", "content-type"]}}, indent=2) + "\n")
    entries: dict[str, Any] = {}
    if status != 200:
        return {"status": status, "entries": entries}
    root = ET.fromstring(body)
    ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    for e in root.findall("a:entry", ns):
        entry_id = e.findtext("a:id", namespaces=ns) or ""
        arxiv_versioned = entry_id.split("/abs/")[-1]
        if not arxiv_versioned:
            continue
        base = arxiv_versioned
        if "v" in base and base.rsplit("v", 1)[-1].isdigit():
            base = base.rsplit("v", 1)[0]
        title = " ".join((e.findtext("a:title", namespaces=ns) or "").split())
        summary = " ".join((e.findtext("a:summary", namespaces=ns) or "").split())
        published = (e.findtext("a:published", namespaces=ns) or "")[:10]
        updated = (e.findtext("a:updated", namespaces=ns) or "")[:10]
        authors = [a.findtext("a:name", namespaces=ns) for a in e.findall("a:author", ns)]
        cats = [c.attrib.get("term") for c in e.findall("a:category", ns)]
        primary = e.find("arxiv:primary_category", ns)
        doi_el = e.find("arxiv:doi", ns)
        rec = {
            "arxiv_id": base,
            "arxiv_versioned_id": arxiv_versioned,
            "arxiv_url": f"https://arxiv.org/abs/{arxiv_versioned}",
            "arxiv_pdf_url": f"https://arxiv.org/pdf/{arxiv_versioned}",
            "title": title,
            "authors": authors,
            "year": int(published[:4]) if published[:4].isdigit() else None,
            "published": published,
            "updated": updated,
            "summary": summary,
            "categories": cats,
            "primary_category": primary.attrib.get("term") if primary is not None else None,
            "arxiv_doi": doi_el.text.strip() if doi_el is not None and doi_el.text else None,
        }
        entries[base] = rec
    return {"status": status, "entries": entries}


def semantic_scholar_batch(source_ids: list[str], doi_ids: list[str]) -> dict[str, Any]:
    ids = [f"arXiv:{x}" for x in source_ids] + [f"DOI:{d}" for d in doi_ids]
    if not ids:
        return {"status": "not_requested", "records_by_id": {}}
    url = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,authors,year,venue,publicationVenue,externalIds,citationCount,referenceCount,abstract,url,publicationDate"
    payload = json.dumps({"ids": ids}).encode()
    headers = {"Content-Type": "application/json"}
    attempts = []
    final_status = None
    final_body: bytes | None = None
    for wait in [0, 15, 45]:
        if wait:
            time.sleep(wait)
        status, body, resp_headers = fetch(url, data=payload, headers=headers)
        attempts.append({"status": status, "wait_before_seconds": wait, "headers_subset": {k: resp_headers.get(k) for k in ["date", "content-type", "x-ratelimit-limit", "x-ratelimit-remaining"]}})
        final_status = status
        final_body = body
        if status == 200:
            break
        if status not in (429, 500, 502, 503, 504):
            break
    assert final_body is not None
    (RAW / "wave3_citation_placement_semantic_scholar_batch_raw.json").write_bytes(final_body)
    (RAW / "wave3_citation_placement_semantic_scholar_status.json").write_text(json.dumps({"url": url, "ids": ids, "attempts": attempts, "final_status": final_status}, indent=2) + "\n")
    records_by_id: dict[str, Any] = {}
    if final_status == 200:
        try:
            rows = json.loads(final_body.decode())
            for id_, row in zip(ids, rows):
                records_by_id[id_] = row
        except Exception as exc:  # preserve body already saved
            records_by_id["_parse_error"] = str(exc)
    return {"status": final_status, "records_by_id": records_by_id, "attempts": attempts}


def first_author_short(authors: list[str]) -> str:
    if not authors:
        return "unknown authors"
    if len(authors) == 1:
        return authors[0]
    if len(authors) == 2:
        return f"{authors[0]} and {authors[1]}"
    return f"{authors[0]} et al."


def main() -> int:
    arxiv_ids = [s["arxiv"] for s in SOURCES if s.get("arxiv")]
    doi_ids = [s["doi"] for s in SOURCES if s.get("doi")]
    arxiv_result = arxiv_id_list(arxiv_ids)
    s2_result = semantic_scholar_batch(arxiv_ids, doi_ids)

    records = []
    for src in SOURCES:
        arxiv_meta = None
        if src.get("arxiv"):
            arxiv_meta = arxiv_result["entries"].get(src["arxiv"])
        s2_meta = None
        s2_lookup_ids = []
        if src.get("arxiv"):
            s2_lookup_ids.append(f"arXiv:{src['arxiv']}")
        if src.get("doi"):
            s2_lookup_ids.append(f"DOI:{src['doi']}")
        for sid in s2_lookup_ids:
            row = s2_result["records_by_id"].get(sid)
            if row:
                s2_meta = row
                break
        # Prefer arXiv title/author strings when available; Semantic Scholar is
        # retained for DOI/URL/year/citation enrichment but can duplicate or
        # mangle long author lists in some astronomy records.
        title = (arxiv_meta or {}).get("title") or (s2_meta or {}).get("title") or src["key"]
        authors = (arxiv_meta or {}).get("authors") or [a.get("name") for a in (s2_meta or {}).get("authors", []) if a.get("name")] or []
        year = (s2_meta or {}).get("year") or (arxiv_meta or {}).get("year")
        external = (s2_meta or {}).get("externalIds") or {}
        doi = src.get("doi") or external.get("DOI") or (arxiv_meta or {}).get("arxiv_doi")
        arxiv_versioned = (arxiv_meta or {}).get("arxiv_versioned_id")
        arxiv_url = (arxiv_meta or {}).get("arxiv_url")
        if src.get("arxiv") and not arxiv_url:
            arxiv_url = f"https://arxiv.org/abs/{src['arxiv']}"
        rec = {
            "record_key": src["key"],
            "associated_papers": src["papers"],
            "title": title,
            "year": year,
            "authors": authors,
            "author_short": first_author_short(authors),
            "arxiv_id_requested": src.get("arxiv"),
            "arxiv_versioned_id": arxiv_versioned,
            "arxiv_url": arxiv_url,
            "arxiv_pdf_url": (arxiv_meta or {}).get("arxiv_pdf_url"),
            "semantic_scholar_url": (s2_meta or {}).get("url"),
            "doi": doi,
            "doi_url": f"https://doi.org/{doi}" if doi else None,
            "publication_date": (s2_meta or {}).get("publicationDate") or (arxiv_meta or {}).get("published"),
            "venue": (s2_meta or {}).get("venue"),
            "citation_count_semantic_scholar": (s2_meta or {}).get("citationCount"),
            "reference_count_semantic_scholar": (s2_meta or {}).get("referenceCount"),
            "placement": src["placement"],
            "why_relevant": src["relevance"],
            "support_class": src["support_class"],
            "supports_actual_result_interpretation": src["support_class"].startswith("supports_actual"),
            "supports_only_future_data_or_context": "future" in src["support_class"] or "context" in src["support_class"] or "guardrail" in src["support_class"],
            "source_provenance": {
                "arxiv_api": bool(arxiv_meta),
                "semantic_scholar_api": bool(s2_meta),
                "semantic_scholar_status": s2_result["status"],
            },
        }
        records.append(rec)

    jsonl_path = ROOT / f"literature_sources_wave3_citation_placement_{TIMESTAMP}.jsonl"
    with jsonl_path.open("w") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + "\n")

    by_paper = defaultdict(list)
    for rec in records:
        for paper in rec["associated_papers"]:
            by_paper[paper].append(rec)
    paper_counts = {k: len(v) for k, v in sorted(by_paper.items())}
    support_counts = Counter(rec["support_class"] for rec in records)
    duplicate_keys = [k for k, n in Counter(rec["record_key"] for rec in records).items() if n > 1]
    summary = {
        "timestamp": TIMESTAMP,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "lane": "literature/source-grounding",
        "selected_papers": sorted(by_paper.keys()),
        "record_count": len(records),
        "paper_record_counts": paper_counts,
        "support_class_counts": dict(sorted(support_counts.items())),
        "duplicate_record_keys": duplicate_keys,
        "raw_payload_dir": str(RAW),
        "jsonl_path": str(jsonl_path),
        "semantic_scholar_status": s2_result["status"],
        "semantic_scholar_attempts": s2_result["attempts"],
        "arxiv_status": arxiv_result["status"],
        "safety_ledger": {
            "credentials_used": False,
            "public_network_sources_only": True,
            "writes_limited_to_literature_lane": True,
            "db_api_page_versions_wiki_publish_live_deploy_restart_git_cron_billing_oauth_external_submission": False,
        },
        "local_inputs_read_before_packet": LOCAL_INPUTS_READ,
    }
    summary_path = ROOT / f"literature_summary_wave3_citation_placement_{TIMESTAMP}.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True) + "\n")

    report_path = ROOT / f"literature_citation_placement_wave3_{TIMESTAMP}.md"
    lines = []
    lines.append(f"# Literature/source grounding Wave-3 citation placement — {TIMESTAMP}")
    lines.append("")
    lines.append("Marker: `LITERATURE_WAVE3_CITATION_PLACEMENT_20260708T233709Z`")
    lines.append("")
    lines.append("Scope: lane-local source grounding for M1 RP-1, M2 P3, and M3 P1. No manuscript/public/page/API/database/git/deploy changes.")
    lines.append("")
    lines.append("## Inputs checked")
    for item in LOCAL_INPUTS_READ:
        lines.append(f"- `{item}`")
    lines.append("")
    lines.append("## API/artifact summary")
    lines.append(f"- Public arXiv records requested: {len(arxiv_ids)}; arXiv status: `{arxiv_result['status']}`.")
    lines.append(f"- Public Semantic Scholar batch status: `{s2_result['status']}` (raw/status saved even if rate-limited).")
    lines.append(f"- JSONL records: {len(records)}; duplicate record keys: {duplicate_keys or 'none'}.")
    lines.append(f"- Raw payloads: `{RAW}`")
    lines.append(f"- JSONL: `{jsonl_path}`")
    lines.append(f"- Summary JSON: `{summary_path}`")
    lines.append("")
    for paper in ["m1_rp1_sdss_agn_sfr", "m2_p3_feedback_transition_mass", "m3_p1_multiphase_census"]:
        lines.append(f"## {paper}")
        for rec in by_paper[paper]:
            urls = []
            if rec.get("arxiv_url"):
                urls.append(f"arXiv: {rec['arxiv_url']}")
            if rec.get("semantic_scholar_url"):
                urls.append(f"Semantic Scholar: {rec['semantic_scholar_url']}")
            if rec.get("doi_url"):
                urls.append(f"DOI: {rec['doi_url']}")
            url_text = "; ".join(urls) if urls else "URL unavailable from public APIs"
            authors_text = ", ".join(rec["authors"][:6]) + (", et al." if len(rec["authors"]) > 6 else "") if rec["authors"] else "authors unavailable"
            lines.append(f"- **{rec['title']}** ({rec.get('year') or 'year unavailable'}; {authors_text}).")
            lines.append(f"  - URLs: {url_text}")
            lines.append(f"  - Placement: {rec['placement']}")
            lines.append(f"  - Relevance: {rec['why_relevant']}")
            if rec["support_class"] in {"supports_actual_method_or_data_provenance", "supports_actual_method_guardrail"}:
                lines.append("  - Use class: supports the actual SDSS method/data provenance or method guardrail; it still does not make the pilot causal.")
            else:
                lines.append("  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.")
        lines.append("")
    lines.append("## Integration guidance")
    lines.append("- M1 RP-1 is strengthened by keeping SDSS DR17/MPA-JHU/BPT method citations adjacent to the method and retired/LINER citations adjacent to the caveat; LaMassa is only motivation.")
    lines.append("- M2 P3 should keep the mass-vector result separate from physical transition claims: Kauffmann/Baldry support the empirical axes, while Peng/Dekel/Bluck/Piotrowska motivate variables missing from this pilot.")
    lines.append("- M3 P1 should use the wind/outflow sources to say what a real multiphase census needs; none converts SDSS optical threshold fractions into outflow incidence.")
    lines.append("")
    lines.append("## Safety")
    lines.append("No credentials used. No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/cron/billing/OAuth/external submission changes. Writes were limited to this literature lane plus the separately authorized ledger append.")
    report_path.write_text("\n".join(lines) + "\n")

    tick_path = ROOT / "ticks" / f"LITERATURE_TICK_WAVE3_CITATION_PLACEMENT_{TIMESTAMP}.md"
    tick_lines = [
        f"# Literature tick — {TIMESTAMP}",
        "",
        "Completed Wave-3 citation-placement/source-grounding packet for M1 RP-1, M2 P3, and M3 P1.",
        f"Report: `{report_path}`",
        f"JSONL: `{jsonl_path}`",
        f"Summary: `{summary_path}`",
        f"Records: {len(records)}; paper counts: {paper_counts}; duplicate keys: {duplicate_keys or 'none'}.",
        "Safety: no credentials; no DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/cron/billing/OAuth/external submission changes.",
    ]
    tick_path.write_text("\n".join(tick_lines) + "\n")

    print(json.dumps({"report_path": str(report_path), "jsonl_path": str(jsonl_path), "summary_path": str(summary_path), "tick_path": str(tick_path), "record_count": len(records), "paper_counts": paper_counts, "semantic_scholar_status": s2_result["status"], "arxiv_status": arxiv_result["status"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
