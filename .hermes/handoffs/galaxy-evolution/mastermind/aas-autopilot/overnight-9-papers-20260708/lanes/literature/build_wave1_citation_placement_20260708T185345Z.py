#!/usr/bin/env python3
"""Build a lane-local public-source citation-placement packet for Wave-1 papers.

No credentials. Public arXiv export API + one unauthenticated Semantic Scholar batch probe.
Writes only under the literature lane.
"""
from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

STAMP = "20260708T185345Z"
ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature")
RAW = ROOT / "raw_payloads" / STAMP
RAW.mkdir(parents=True, exist_ok=True)

PAPERS = {
    "m1_rp2_environment_quenching": {
        "label": "M1 RP-2 — SDSS density proxy for environmental quenching",
        "boundary": "actual cached-SDSS nearest-neighbour density versus catalog-sSFR quenching association; not halo/central-satellite causal environmental quenching",
    },
    "m1_rp3_maintenance_heating": {
        "label": "M1 RP-3 — optical-AGN denominator for maintenance-heating follow-up",
        "boundary": "actual optical BPT-AGN fractions in massive emission-line hosts; not jet power, cavity enthalpy, cooling balance, or duty cycle",
    },
    "m2_p1_outflow_escape_recycling": {
        "label": "M2 P1 — high-excitation optical-AGN denominator for outflow escape/recycling tests",
        "boundary": "actual high-excitation optical target denominator and sSFR contrast; not outflow velocity, escape speed, gas phase mass, or recycling fraction",
    },
}

# One record per paper-source placement. arxiv_id is the source key where available.
PLACEMENTS = [
    # M1 RP-2
    dict(paper="m1_rp2_environment_quenching", arxiv_id="2112.02026", bibkey="abdurrouf2022", role="actual_data_method", placement="Data/Selection: public SDSS DR17 provenance", support_class="supports_actual_method", relevance="DR17 release paper anchors the public survey release used by the cached SDSS pilot."),
    dict(paper="m1_rp2_environment_quenching", arxiv_id="astro-ph/0311060", bibkey="brinchmann2004", role="actual_data_method", placement="Data/Selection: catalog SFR/sSFR and value-added-property caveat", support_class="supports_actual_method", relevance="SDSS low-redshift physical-property/SFR context for catalog sSFR-based quenching flags."),
    dict(paper="m1_rp2_environment_quenching", arxiv_id="1003.4747", bibkey="peng2010", role="actual_result_context", placement="Introduction/Discussion: mass and environment as separable population axes", support_class="supports_scoped_result_interpretation", relevance="Mass/environment quenching framework helps interpret why a mass-redshift adjusted density-proxy diagnostic is meaningful."),
    dict(paper="m1_rp2_environment_quenching", arxiv_id="astro-ph/0607648", bibkey="baldry2006", role="actual_result_context", placement="Introduction/Discussion: local density and bimodality context", support_class="supports_scoped_result_interpretation", relevance="SDSS-like colour bimodality versus stellar mass and environment context; close to the paper's density-proxy/quenching association."),
    dict(paper="m1_rp2_environment_quenching", arxiv_id="1206.3571", bibkey="wetzel2013", role="future_data_guard", placement="Limitations/Future work: satellite histories, group catalogues, infall/preprocessing", support_class="motivates_future_data_only", relevance="Group/cluster satellite quenching-timescale work specifies missing central/satellite and infall information."),
    dict(paper="m1_rp2_environment_quenching", arxiv_id="2401.12953", bibkey="goubert2024", role="future_data_guard", placement="Limitations/Future work: model comparison and intrinsic/environment predictor separation", support_class="motivates_future_data_only", relevance="Recent SDSS-plus-simulation comparison frames environment and AGN feedback jointly, guarding against causal overclaim from one density proxy."),

    # M1 RP-3
    dict(paper="m1_rp3_maintenance_heating", arxiv_id="2112.02026", bibkey="abdurrouf2022", role="actual_data_method", placement="Data/Selection: public SDSS DR17 provenance", support_class="supports_actual_method", relevance="DR17 release paper anchors the public survey release for the optical denominator."),
    dict(paper="m1_rp3_maintenance_heating", arxiv_id="astro-ph/0506269", bibkey="best2005", role="target_stratification_context", placement="Introduction/Discussion: SDSS-to-radio demographic bridge for massive hosts", support_class="supports_scoped_target_stratification", relevance="SDSS radio-loud AGN demographics connect massive-host target selection to later radio-mode follow-up without measuring jet power here."),
    dict(paper="m1_rp3_maintenance_heating", arxiv_id="0709.2152", bibkey="mcnamara2007", role="future_data_guard", placement="Scope/Discussion: X-ray cavity, shock, hot-atmosphere heating observables missing from SDSS", support_class="motivates_future_data_only", relevance="Review anchor for hot-atmosphere heating tests; defines future calorimetric observables absent from the optical pilot."),
    dict(paper="m1_rp3_maintenance_heating", arxiv_id="1204.0006", bibkey="mcnamara2012", role="future_data_guard", placement="Scope/Discussion: mechanical feedback and heating-to-cooling measurement requirements", support_class="motivates_future_data_only", relevance="Mechanical-feedback review supports requiring jet/cavity power and cooling luminosity before maintenance-heating claims."),
    dict(paper="m1_rp3_maintenance_heating", arxiv_id="1403.4620", bibkey="heckmanbest2014", role="status_context", placement="Introduction: radiative-mode versus radio-mode AGN population context", support_class="status_motivation_only", relevance="Survey review helps separate optical/radiative and radio/mechanical AGN modes; not a measurement in the SDSS pilot."),
    dict(paper="m1_rp3_maintenance_heating", arxiv_id="2403.17145", bibkey="eckert2024", role="future_data_guard", placement="Future work: group/hot-gas regime for feedback energetics", support_class="motivates_future_data_only", relevance="Group-scale AGN-feedback status source identifying the hot-gas/group observations needed after the optical denominator."),

    # M2 P1
    dict(paper="m2_p1_outflow_escape_recycling", arxiv_id="2112.02026", bibkey="abdurrouf2022", role="actual_data_method", placement="Data/Selection: public SDSS DR17 provenance", support_class="supports_actual_method", relevance="DR17 release paper anchors the public survey release for the high-excitation optical target denominator."),
    dict(paper="m2_p1_outflow_escape_recycling", arxiv_id="astro-ph/0605681", bibkey="kewley2006", role="actual_data_method", placement="Data/Candidate definition: Seyfert/LINER/composite optical-classification caveats", support_class="supports_actual_method", relevance="Classification paper supports line-ratio guardrails for high-excitation optical AGN selection."),
    dict(paper="m2_p1_outflow_escape_recycling", arxiv_id="astro-ph/0504435", bibkey="veilleux2005", role="status_context", placement="Scope/Discussion: multiphase wind physics and diagnostic requirements", support_class="status_motivation_only", relevance="Galactic-winds review motivates why velocity, geometry, phase mass, and multiwavelength data are needed beyond SDSS line ratios."),
    dict(paper="m2_p1_outflow_escape_recycling", arxiv_id="1311.2595", bibkey="cicone2014", role="future_data_guard", placement="Future work: molecular outflow mass/rate follow-up", support_class="motivates_future_data_only", relevance="CO molecular-outflow work specifies a missing cold-gas phase and outflow-rate observable; not support for an SDSS escape fraction."),
    dict(paper="m2_p1_outflow_escape_recycling", arxiv_id="1702.04507", bibkey="fiore2017", role="future_data_guard", placement="Future work: wind scaling relations and kinetic-power measurements", support_class="motivates_future_data_only", relevance="Wind scaling-relations source motivates velocities/radii/phase masses and duty-cycle caution for future resolved follow-up."),
    dict(paper="m2_p1_outflow_escape_recycling", arxiv_id="1706.08987", bibkey="carniani2017", role="future_data_guard", placement="Future work: high-z molecular-reservoir disturbance as targeted-case motivation", support_class="motivates_future_data_only", relevance="Quasar molecular-gas reservoir paper motivates resolved gas follow-up but must not be used as denominator-wide escape/recycling evidence."),
    dict(paper="m2_p1_outflow_escape_recycling", arxiv_id="1204.4114", bibkey="fabian2012", role="status_context", placement="Discussion: broad AGN-feedback review with explicit overclaim guard", support_class="status_motivation_only", relevance="Review source frames AGN feedback evidence while the pilot remains an optical target baseline."),
]


def fetch_url(url: str, *, data: bytes | None = None, headers: dict | None = None, timeout: int = 45) -> tuple[int | None, bytes, str | None]:
    req = urllib.request.Request(url, data=data, headers=headers or {"User-Agent": "NebulaMind-literature-lane/1.0 (public metadata; no credentials)"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read(), None
    except urllib.error.HTTPError as e:
        try:
            body = e.read()
        except Exception:
            body = b""
        return e.code, body, str(e)
    except Exception as e:
        return None, b"", repr(e)


def parse_arxiv(xml_bytes: bytes) -> dict[str, dict]:
    ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(xml_bytes)
    out = {}
    for entry in root.findall("a:entry", ns):
        id_url = entry.findtext("a:id", default="", namespaces=ns).strip().replace("http://", "https://")
        raw_id = id_url.split("/abs/")[-1]
        base_id = re.sub(r"v\d+$", "", raw_id)
        title = " ".join((entry.findtext("a:title", default="", namespaces=ns) or "").split())
        summary = " ".join((entry.findtext("a:summary", default="", namespaces=ns) or "").split())
        authors = [a.findtext("a:name", default="", namespaces=ns).strip() for a in entry.findall("a:author", ns)]
        cats = [c.get("term") for c in entry.findall("a:category", ns)]
        pdf_url = None
        for link in entry.findall("a:link", ns):
            if link.get("title") == "pdf" or link.get("type") == "application/pdf":
                pdf_url = (link.get("href") or "").replace("http://", "https://")
        doi = None
        doi_el = entry.find("arxiv:doi", ns)
        if doi_el is not None and doi_el.text:
            doi = doi_el.text.strip()
        primary = entry.find("arxiv:primary_category", ns)
        out[base_id] = {
            "arxiv_api_id": raw_id,
            "arxiv_base_id": base_id,
            "abs_url": id_url,
            "pdf_url": pdf_url,
            "title": title,
            "authors": authors,
            "author_count": len(authors),
            "published": entry.findtext("a:published", default="", namespaces=ns),
            "updated": entry.findtext("a:updated", default="", namespaces=ns),
            "year": (entry.findtext("a:published", default="", namespaces=ns) or "")[:4],
            "doi": doi,
            "primary_category": primary.get("term") if primary is not None else None,
            "categories": cats,
            "abstract": summary,
        }
    return out


def arxiv_id_list_url(ids: list[str]) -> str:
    return "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": ",".join(ids), "max_results": str(len(ids))})

# Fetch raw arXiv XML per paper category, politely.
all_meta: dict[str, dict] = {}
status_by_paper = {}
for idx, (paper, _pdata) in enumerate(PAPERS.items()):
    ids = sorted({p["arxiv_id"] for p in PLACEMENTS if p["paper"] == paper})
    url = arxiv_id_list_url(ids)
    status, body, error = fetch_url(url)
    raw_path = RAW / f"{paper}_arxiv_id_list.xml"
    raw_path.write_bytes(body)
    status_by_paper[paper] = {"http_status": status, "error": error, "raw_path": str(raw_path), "requested_ids": ids, "url": url}
    if status == 200 and body:
        meta = parse_arxiv(body)
        all_meta.update(meta)
        status_by_paper[paper]["records_parsed"] = len(meta)
    else:
        status_by_paper[paper]["records_parsed"] = 0
    if idx < len(PAPERS) - 1:
        time.sleep(3.2)

# Semantic Scholar unauthenticated batch status probe; the output is enrichment only.
s2_ids = [f"arXiv:{aid}" for aid in sorted({p["arxiv_id"] for p in PLACEMENTS})]
s2_url = "https://api.semanticscholar.org/graph/v1/paper/batch?" + urllib.parse.urlencode({"fields": "title,authors,year,abstract,externalIds,publicationVenue,citationCount,isOpenAccess,openAccessPdf"})
s2_body = json.dumps({"ids": s2_ids}).encode("utf-8")
s2_status, s2_resp, s2_error = fetch_url(s2_url, data=s2_body, headers={"User-Agent": "NebulaMind-literature-lane/1.0 (public metadata; no credentials)", "Content-Type": "application/json"}, timeout=45)
(RAW / "semantic_scholar_batch_status.json").write_text(json.dumps({"http_status": s2_status, "error": s2_error, "request_ids": s2_ids, "response_text": s2_resp.decode("utf-8", "replace")[:200000]}, indent=2) + "\n")
s2_by_arxiv: dict[str, dict] = {}
if s2_status == 200 and s2_resp:
    try:
        s2_items = json.loads(s2_resp.decode("utf-8"))
        if isinstance(s2_items, list):
            for requested, item in zip(s2_ids, s2_items):
                base = requested.split("arXiv:", 1)[-1]
                if isinstance(item, dict):
                    ext = item.get("externalIds") or {}
                    arxiv_ext = ext.get("ArXiv") if isinstance(ext, dict) else None
                    s2_by_arxiv[str(arxiv_ext or base)] = item
    except Exception:
        s2_by_arxiv = {}

# Build JSONL association ledger.
jsonl_path = ROOT / f"literature_sources_wave1_citation_placement_{STAMP}.jsonl"
records: list[dict[str, object]] = []
for pl in PLACEMENTS:
    meta = all_meta.get(pl["arxiv_id"])
    rec: dict[str, object] = dict(pl)
    rec["paper_label"] = PAPERS[pl["paper"]]["label"]
    rec["paper_boundary"] = PAPERS[pl["paper"]]["boundary"]
    rec["source_key"] = f"arxiv:{pl['arxiv_id']}"
    rec["record_key"] = f"{pl['paper']}|arxiv:{pl['arxiv_id']}"
    if meta:
        rec.update({
            "title": meta["title"],
            "year": meta["year"],
            "authors": meta["authors"],
            "author_count": meta["author_count"],
            "exact_url": meta["abs_url"],
            "pdf_url": meta["pdf_url"],
            "doi": meta["doi"],
            "arxiv_api_id": meta["arxiv_api_id"],
            "arxiv_categories": meta["categories"],
            "metadata_source": "public_arxiv_export_api",
            "abstract_available": bool(meta.get("abstract")),
        })
    else:
        rec.update({
            "title": None,
            "year": None,
            "authors": [],
            "author_count": 0,
            "exact_url": f"https://arxiv.org/abs/{pl['arxiv_id']}",
            "pdf_url": f"https://arxiv.org/pdf/{pl['arxiv_id']}",
            "doi": None,
            "arxiv_api_id": None,
            "arxiv_categories": [],
            "metadata_source": "arxiv_lookup_missing",
            "abstract_available": False,
        })
    s2_item = s2_by_arxiv.get(pl["arxiv_id"])
    if s2_item:
        rec["semantic_scholar_year"] = s2_item.get("year")
        rec["semantic_scholar_citation_count"] = s2_item.get("citationCount")
        rec["semantic_scholar_title"] = s2_item.get("title")
        rec["publication_year_for_citation"] = s2_item.get("year") or rec.get("year")
    else:
        rec["semantic_scholar_year"] = None
        rec["semantic_scholar_citation_count"] = None
        rec["semantic_scholar_title"] = None
        rec["publication_year_for_citation"] = rec.get("year")
    records.append(rec)

with jsonl_path.open("w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + "\n")

# Summary JSON.
record_keys = [r["record_key"] for r in records]
source_keys = [r["source_key"] for r in records]
by_paper = defaultdict(list)
for r in records:
    by_paper[r["paper"]].append(r)
summary = {
    "marker": f"LITERATURE_WAVE1_CITATION_PLACEMENT_{STAMP}",
    "utc": STAMP,
    "scope": "citation-placement/source-grounding review for M1 RP-2, M1 RP-3, and M2 P1 after Lana selection-definition revisions",
    "records": len(records),
    "unique_sources": len(set(source_keys)),
    "duplicate_record_keys": [k for k, c in Counter(record_keys).items() if c > 1],
    "duplicate_source_keys_across_associations": {k: c for k, c in Counter(source_keys).items() if c > 1},
    "papers": {paper: {"label": PAPERS[paper]["label"], "records": len(rs), "support_class_counts": Counter(r["support_class"] for r in rs), "role_counts": Counter(r["role"] for r in rs)} for paper, rs in by_paper.items()},
    "metadata_availability": {
        "arxiv_metadata_found_records": sum(1 for r in records if r["metadata_source"] == "public_arxiv_export_api"),
        "semantic_scholar_found_records": sum(1 for r in records if r.get("semantic_scholar_title")),
        "abstract_available_records": sum(1 for r in records if r.get("abstract_available")),
        "doi_available_records": sum(1 for r in records if r.get("doi")),
        "author_year_available_records": sum(1 for r in records if r.get("year") and int(r.get("author_count", 0) or 0) > 0),
    },
    "arxiv_status_by_paper": status_by_paper,
    "semantic_scholar_batch_probe": {"http_status": s2_status, "error": s2_error, "raw_path": str(RAW / "semantic_scholar_batch_status.json"), "records_requested": len(s2_ids)},
    "artifact_paths": {
        "jsonl": str(jsonl_path),
        "summary_json": str(ROOT / f"literature_summary_wave1_citation_placement_{STAMP}.json"),
        "raw_payload_dir": str(RAW),
    },
    "safety_ledger": [
        "No credentials used; no ADS token/API-key access attempted.",
        "No manuscript/PDF/public page/live root/product DB/API/page_versions/trust/deploy/restart/git/billing/OAuth/cron/external-submission changes.",
        "This packet supports later local citation-integration review only; it does not authorize prose publication or public-linked PDF replacement.",
    ],
}
summary_path = ROOT / f"literature_summary_wave1_citation_placement_{STAMP}.json"
summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=lambda x: dict(x)) + "\n", encoding="utf-8")

# Compact Markdown report.
def short_authors(authors: list[str], max_names: int = 4) -> str:
    if not authors:
        return "authors unavailable"
    if len(authors) <= max_names:
        return ", ".join(authors)
    return ", ".join(authors[:max_names]) + f", et al. ({len(authors)} authors)"

md_path = ROOT / f"literature_citation_placement_wave1_{STAMP}.md"
lines = []
lines.append(f"# Literature/source grounding — Wave-1 citation placement review")
lines.append("")
lines.append(f"Marker: `LITERATURE_WAVE1_CITATION_PLACEMENT_{STAMP}`")
lines.append("")
lines.append("UTC: 2026-07-08T18:53:45Z  ")
lines.append("Local: 2026-07-09 03:53:45 KST")
lines.append("")
lines.append("## Scope and inputs read")
lines.append("")
lines.append("Focused on three Wave-1 papers after the Lana selection/definition cleanup: M1 RP-2, M1 RP-3, and M2 P1. Read the overnight brief, swarm board, ledger, current run-root manuscripts, current topic pages and backups, the Wave-1 literature packet, Hwao direction, and the Lana 20260708T182812Z revision drafts. This is a source-grounding/citation-placement packet only; no manuscript, PDF, public page, product DB/API, deploy, git, billing/OAuth, cron, or external submission change is authorized or performed.")
lines.append("")
lines.append("## Acquisition and mechanical checks")
lines.append("")
lines.append("- Public arXiv export API only for primary metadata; raw XML was preserved by paper under `raw_payloads/20260708T185345Z/`.")
lines.append(f"- Unauthenticated Semantic Scholar batch enrichment was attempted once; HTTP status: `{s2_status}`. It is enrichment only and not required for the conclusions.")
lines.append(f"- Association records: **{len(records)}** across **{len(set(source_keys))}** unique arXiv sources; duplicate record keys: **{summary['duplicate_record_keys']}**.")
lines.append(f"- arXiv metadata found for **{summary['metadata_availability']['arxiv_metadata_found_records']}/{len(records)}** association records; Semantic Scholar enrichment found **{summary['metadata_availability']['semantic_scholar_found_records']}/{len(records)}**; abstracts **{summary['metadata_availability']['abstract_available_records']}/{len(records)}**; DOI in arXiv record **{summary['metadata_availability']['doi_available_records']}/{len(records)}**; author/year **{summary['metadata_availability']['author_year_available_records']}/{len(records)}**.")
lines.append("")
lines.append("## Paper-specific placement rules")
for paper in PAPERS:
    lines.append("")
    lines.append(f"### {PAPERS[paper]['label']}")
    lines.append("")
    lines.append(f"Boundary: {PAPERS[paper]['boundary']}.")
    lines.append("")
    lines.append("| Priority | Source | Exact URL | Year / authors | Placement / relevance | Supports actual result, or only future data? |")
    lines.append("|---:|---|---|---|---|---|")
    for i, rec in enumerate([r for r in records if r["paper"] == paper], 1):
        source = str(rec.get("title") or rec["source_key"])
        exact = str(rec.get("exact_url") or f"https://arxiv.org/abs/{rec['arxiv_id']}")
        authors_obj = rec.get("authors", [])
        authors = authors_obj if isinstance(authors_obj, list) else []
        display_year = rec.get("publication_year_for_citation") or rec.get("year") or "year unavailable"
        ya = f"{display_year} — {short_authors([str(a) for a in authors])}"
        placement = f"{rec['placement']}; {rec['relevance']}"
        support = str(rec["support_class"]).replace("_", " ")
        lines.append(f"| {i} | {source} | {exact} | {ya} | {placement} | {support} |")
    lines.append("")
    if paper == "m1_rp2_environment_quenching":
        lines.append("Integration guard: cite Peng/Baldry as scoped context for the density-proxy association; keep Wetzel/Goubert in the missing-data paragraph requiring group/halo/central-satellite/model-comparison information.")
    elif paper == "m1_rp3_maintenance_heating":
        lines.append("Integration guard: use Best/Heckman-Best as target-stratification/status context, and McNamara/Nulsen/Eckert only to define the future X-ray/radio/hot-gas measurements; do not imply the optical BPT fraction measures heating balance.")
    else:
        lines.append("Integration guard: Kewley 2006 can support optical-classification caveats; wind/outflow papers belong in the required-follow-up paragraph and cannot support escape/recycling fractions from SDSS line ratios.")
lines.append("")
lines.append("## Later manuscript-integration checklist")
lines.append("")
lines.append("1. Current run-root Wave-1 manuscripts still have only the minimal York/BPT bibliography; the Lana drafts already contain the safer expanded citations. A later integration pass should migrate the citations with the same method/status/future-data separation, not just paste bibliography entries.")
lines.append("2. Preserve exact operational definitions before citations: RP-2 `specsfr_tot_p50 < -11.0` and 10th-neighbour density proxy; RP-3 `lgm_tot_p50 >= 10.8` and `specsfr_tot_p50 < -11.0`; M2 P1 BPT AGN plus `log([OIII]/Hb) > 0.25`.")
lines.append("3. Keep selection-function disclosure adjacent to all incidence language: 249,917 strict four-line S/N>=3 public rows, 60,000 cached rows, 24.0% coverage, `TOP 60000 ... ORDER BY specObjID`, and sSFR-dependent retention.")
lines.append("4. Treat this as local citation-integration readiness only. It does not authorize public prose/wiki changes, public-linked PDF replacement, DB/API writes, deploy, git, or external submission.")
lines.append("")
lines.append("## Artifact manifest")
lines.append("")
lines.append(f"- Markdown packet: `{md_path}`")
lines.append(f"- JSONL source/placement ledger: `{jsonl_path}`")
lines.append(f"- Summary JSON: `{summary_path}`")
for paper, st in status_by_paper.items():
    lines.append(f"- Raw arXiv XML for {paper}: `{st['raw_path']}`")
lines.append(f"- Semantic Scholar batch status: `{RAW / 'semantic_scholar_batch_status.json'}`")
lines.append("")
lines.append("## Safety ledger")
lines.append("")
for item in summary["safety_ledger"]:
    lines.append(f"- {item}")
lines.append("- No active execution phrase.")
lines.append("")
md_path.write_text("\n".join(lines), encoding="utf-8")

# Lane-local tick note.
tick_path = ROOT / "ticks" / f"LITERATURE_TICK_WAVE1_CITATION_PLACEMENT_{STAMP}.md"
tick_path.parent.mkdir(parents=True, exist_ok=True)
tick_path.write_text("\n".join([
    f"# Literature tick — Wave-1 citation placement {STAMP}",
    "",
    f"Wrote `{md_path.name}`, `{jsonl_path.name}`, `{summary_path.name}`, and raw public arXiv/Semantic-Scholar-status payloads under `raw_payloads/{STAMP}/`.",
    "Covered M1 RP-2, M1 RP-3, and M2 P1; separated actual-method/result-context citations from future-data-only physical-context citations.",
    "No credentials used. No public/live/product DB/API/page_versions/trust/deploy/restart/git/billing/OAuth/cron/external-submission changes. No active execution phrase.",
    "",
]), encoding="utf-8")

print(json.dumps({
    "marker": summary["marker"],
    "md_path": str(md_path),
    "jsonl_path": str(jsonl_path),
    "summary_path": str(summary_path),
    "tick_path": str(tick_path),
    "records": len(records),
    "unique_sources": len(set(source_keys)),
    "s2_status": s2_status,
    "duplicate_record_keys": summary["duplicate_record_keys"],
}, indent=2))
