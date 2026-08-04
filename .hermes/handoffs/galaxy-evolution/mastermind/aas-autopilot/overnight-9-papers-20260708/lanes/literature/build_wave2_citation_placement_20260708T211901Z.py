#!/usr/bin/env python3
"""Build Wave-2 citation-placement/source-grounding packet from public arXiv and Semantic Scholar.

No credentials; writes only under lanes/literature/.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

TS = "20260708T211901Z"
UTC_ISO = "2026-07-08T21:19:01Z"
LOCAL = "2026-07-09 06:19:01 KST"
ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708")
LANE = ROOT / "lanes" / "literature"
RAW = LANE / "raw_payloads" / TS
RAW.mkdir(parents=True, exist_ok=True)

ARXIV_API = "https://export.arxiv.org/api/query"
S2_BATCH = "https://api.semanticscholar.org/graph/v1/paper/batch"
UA = "NebulaMind literature lane (public metadata; no credentials; contact: local cron)"

# Role labels are deliberately conservative: actual_method can support the SDSS optical
# pilot method/denominator; scoped_interpretation supports cautious context; future_data
# and future_model motivate the missing follow-up only.
PAPERS = [
    {
        "slug": "m2_p2_radio_jet_environment",
        "title": "M2 P2 — environment proxy for optical AGN in massive hosts",
        "boundary": "Actual cached-SDSS result: BPT optical-AGN fraction versus internal nearest-neighbour density proxy in massive hosts; no radio jet power, hot-gas, cavity, or coupling-efficiency measurement.",
        "integration_guard": "Use radio/X-ray/group sources to define the required follow-up observables; the result sentence must remain an optical-AGN/environment denominator statement.",
        "sources": [
            {
                "arxiv_id": "2112.02026",
                "role": "actual_method",
                "placement": "Data/Selection: public SDSS DR17 provenance for the optical emission-line parent sample.",
                "relevance": "Anchors the public survey release used by the cached SDSS denominator.",
                "support": "supports actual method",
            },
            {
                "arxiv_id": "astro-ph/0605681",
                "role": "actual_method",
                "placement": "Data/Definitions: optical AGN host/classification context and BPT-class caveats.",
                "relevance": "Supports why the manuscript must describe BPT labels as optical classification proxies, not feedback measurements.",
                "support": "supports actual method",
            },
            {
                "arxiv_id": "astro-ph/0506269",
                "role": "scoped_interpretation",
                "placement": "Introduction/Discussion: massive-host radio-loud AGN demographic bridge.",
                "relevance": "Connects massive-host SDSS demographics to later radio-mode/maintenance follow-up while keeping the current sample optical-only.",
                "support": "supports scoped target stratification",
            },
            {
                "arxiv_id": "2009.11175",
                "role": "future_data",
                "placement": "Discussion/Future observables: young radio-galaxy outflows and efficiency language.",
                "relevance": "Shows what kind of radio/kinematic data would be needed before discussing coupling efficiency.",
                "support": "motivates future data only",
            },
            {
                "arxiv_id": "0709.2152",
                "role": "future_data",
                "placement": "Limitations/Future work: hot-atmosphere heating, cavities, shocks, and cooling balance.",
                "relevance": "Defines missing X-ray/hot-gas energetics that SDSS optical line ratios do not measure.",
                "support": "motivates future data only",
            },
            {
                "arxiv_id": "2403.17145",
                "role": "future_data",
                "placement": "Limitations/Future work: group-scale gas and AGN-feedback testbed.",
                "relevance": "Motivates environment/group observations needed after the internal-density proxy.",
                "support": "motivates future data only",
            },
        ],
    },
    {
        "slug": "m3_p2_gas_depletion_efficiency",
        "title": "M3 P2 — optical denominator for gas-fraction versus efficiency tests",
        "boundary": "Actual cached-SDSS result: massive low-sSFR four-line optical denominator and H-alpha proxy baseline; no CO/HI/dust gas masses, gas fractions, depletion times, or SFE measurement.",
        "integration_guard": "Cite gas-survey papers only around the missing CO/HI/dust data requirement and the depletion-time/SFE wording guard.",
        "sources": [
            {
                "arxiv_id": "2112.02026",
                "role": "actual_method",
                "placement": "Data/Selection: public SDSS DR17 provenance for the optical denominator.",
                "relevance": "Anchors the survey release for the four-line emission sample and cached follow-up denominator.",
                "support": "supports actual method",
            },
            {
                "arxiv_id": "astro-ph/0311060",
                "role": "actual_method",
                "placement": "Data/Definitions: SDSS physical-property, SFR, and catalog-sSFR context.",
                "relevance": "Supports the catalog sSFR/H-alpha-property caveats in the optical-only manuscript.",
                "support": "supports actual method",
            },
            {
                "arxiv_id": "1103.1642",
                "role": "future_data",
                "placement": "Discussion/Future data: COLD GASS molecular-gas survey anchor for massive nearby galaxies.",
                "relevance": "Specifies the H2/HI/stellar measurements needed before gas-fraction statements.",
                "support": "motivates future data only",
            },
            {
                "arxiv_id": "1104.0019",
                "role": "future_data",
                "placement": "Discussion/Future data: depletion-timescale and non-universality guard.",
                "relevance": "Directly supports the warning that depletion time is a molecular-gas-plus-SFR quantity, not an SDSS four-line quantity.",
                "support": "motivates future data only",
            },
            {
                "arxiv_id": "1710.02157",
                "role": "future_data",
                "placement": "Discussion/Future data: xCOLD GASS complete CO legacy-survey anchor.",
                "relevance": "Motivates the required CO follow-up denominator for molecular gas and depletion-time work.",
                "support": "motivates future data only",
            },
            {
                "arxiv_id": "1802.02373",
                "role": "future_data",
                "placement": "Discussion/Future data: xGASS HI+H2 scaling and molecular-to-atomic gas ratio context.",
                "relevance": "Motivates separating gas availability from SFE with cold-gas data rather than optical H-alpha alone.",
                "support": "motivates future data only",
            },
        ],
    },
    {
        "slug": "m3_p3_simulation_validation",
        "title": "M3 P3 — SDSS target vector for feedback-model validation",
        "boundary": "Actual cached-SDSS result: observed 15-cell mass-redshift target vector from the four-line optical sample; no simulation mock was generated or compared.",
        "integration_guard": "Simulation papers can motivate future forward modelling only; do not cite them as if the SDSS vector validates, rejects, ranks, or falsifies any model.",
        "sources": [
            {
                "arxiv_id": "2112.02026",
                "role": "actual_method",
                "placement": "Data/Selection: public SDSS DR17 provenance for the observed target vector.",
                "relevance": "Anchors the observed SDSS release before any future mock comparison.",
                "support": "supports actual method",
            },
            {
                "arxiv_id": "1812.05609",
                "role": "future_model",
                "placement": "Discussion/Future mock infrastructure: IllustrisTNG public data release.",
                "relevance": "Identifies a public simulation suite that could be forward-modelled through matching selection.",
                "support": "motivates future model comparison only",
            },
            {
                "arxiv_id": "1407.7040",
                "role": "future_model",
                "placement": "Discussion/Future mock infrastructure: EAGLE galaxy-formation/feedback suite.",
                "relevance": "Provides a second feedback-model family for future survey-matched comparisons.",
                "support": "motivates future model comparison only",
            },
            {
                "arxiv_id": "1901.10203",
                "role": "future_model",
                "placement": "Discussion/Future mock infrastructure: SIMBA black-hole growth and feedback prescriptions.",
                "relevance": "Defines another model family whose outputs would require forward modelling before comparison.",
                "support": "motivates future model comparison only",
            },
            {
                "arxiv_id": "2203.11575",
                "role": "future_model",
                "placement": "Methods/Future work: iMaNGA-style mock IFU construction and survey realism.",
                "relevance": "Closest source for the required synthetic-observation step before using observed target vectors to test models.",
                "support": "motivates future model comparison only",
            },
            {
                "arxiv_id": "2008.00004",
                "role": "scoped_interpretation",
                "placement": "Discussion/Future comparison: quenched-fraction comparisons with observations.",
                "relevance": "Shows the kind of quenching comparison a real model-validation paper would need, after applying matching selections.",
                "support": "status/method motivation only",
            },
            {
                "arxiv_id": "1606.03086",
                "role": "future_model",
                "placement": "Discussion/Future observables: morphology as a model output, not a current SDSS-vector result.",
                "relevance": "Motivates adding morphology to future validation; it is not measured in the current target vector.",
                "support": "motivates future model comparison only",
            },
            {
                "arxiv_id": "1301.3092",
                "role": "future_model",
                "placement": "Discussion/Future observables: AGN-driven quenching simulation implications.",
                "relevance": "Useful background for simulation-predicted signatures, with the guard that the current pilot has not tested them.",
                "support": "motivates future model comparison only",
            },
        ],
    },
]


def normalize_arxiv_id(s: str) -> str:
    s = s.strip()
    s = re.sub(r"^https?://arxiv\.org/abs/", "", s)
    return re.sub(r"v\d+$", "", s)


def arxiv_exact_url(versioned_or_base: str) -> str:
    return "https://arxiv.org/abs/" + versioned_or_base


def fetch_url(url: str, method: str = "GET", body: bytes | None = None, headers: dict | None = None, timeout: int = 60):
    h = {"User-Agent": UA}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, dict(resp.headers), resp.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read()


def fetch_arxiv_for_paper(paper: dict) -> tuple[str, dict]:
    ids = [s["arxiv_id"] for s in paper["sources"]]
    url = ARXIV_API + "?" + urllib.parse.urlencode({"id_list": ",".join(ids), "max_results": str(len(ids))})
    status, headers, payload = fetch_url(url)
    xml_path = RAW / f"{paper['slug']}_arxiv_id_list.xml"
    xml_path.write_bytes(payload)
    return url, {"status": status, "headers": headers, "path": str(xml_path), "bytes": len(payload)}


def parse_arxiv_xml(path: Path) -> dict:
    ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.parse(path).getroot()
    out = {}
    for entry in root.findall("a:entry", ns):
        id_url = (entry.findtext("a:id", default="", namespaces=ns) or "").strip()
        versioned = id_url.rsplit("/abs/", 1)[-1]
        base = normalize_arxiv_id(versioned)
        title = " ".join((entry.findtext("a:title", default="", namespaces=ns) or "").split())
        summary = " ".join((entry.findtext("a:summary", default="", namespaces=ns) or "").split())
        published = (entry.findtext("a:published", default="", namespaces=ns) or "").strip()
        updated = (entry.findtext("a:updated", default="", namespaces=ns) or "").strip()
        authors = []
        for a in entry.findall("a:author", ns):
            name = a.findtext("a:name", default="", namespaces=ns)
            if name:
                authors.append(" ".join(name.split()))
        cats = [c.attrib.get("term", "") for c in entry.findall("a:category", ns) if c.attrib.get("term")]
        doi = entry.findtext("arxiv:doi", default="", namespaces=ns) or ""
        primary = entry.find("arxiv:primary_category", ns)
        primary_cat = primary.attrib.get("term", "") if primary is not None else ""
        links = [l.attrib for l in entry.findall("a:link", ns)]
        rec = {
            "arxiv_id_base": base,
            "arxiv_id_versioned": versioned,
            "exact_url": arxiv_exact_url(versioned),
            "title": title,
            "year": published[:4] if published else "",
            "published": published,
            "updated": updated,
            "authors": authors,
            "authors_display": authors_display(authors),
            "categories": cats,
            "primary_category": primary_cat,
            "doi": doi,
            "summary": summary,
            "links": links,
        }
        out[base] = rec
        out[versioned] = rec
    return out


def authors_display(authors: list[str], n: int = 6) -> str:
    if not authors:
        return "unknown authors"
    if len(authors) <= n:
        return ", ".join(authors)
    return ", ".join(authors[:n]) + f", et al. ({len(authors)} authors)"


def fetch_semantic_scholar(unique_ids: list[str]) -> dict:
    ids = ["ARXIV:" + normalize_arxiv_id(x) for x in unique_ids]
    fields = "title,authors,year,citationCount,referenceCount,influentialCitationCount,externalIds,publicationVenue,abstract,url"
    url = S2_BATCH + "?" + urllib.parse.urlencode({"fields": fields})
    body = json.dumps({"ids": ids}).encode("utf-8")
    status, headers, payload = fetch_url(url, method="POST", body=body, headers={"Content-Type": "application/json"}, timeout=60)
    raw_path = RAW / "semantic_scholar_batch_raw.json"
    raw_path.write_bytes(payload)
    try:
        parsed = json.loads(payload.decode("utf-8")) if payload else None
    except Exception as exc:
        parsed = {"parse_error": repr(exc), "raw_prefix": payload[:500].decode("utf-8", "replace")}
    status_obj = {
        "url": url,
        "requested_ids": ids,
        "http_status": status,
        "response_headers_subset": {k: headers.get(k) for k in ["content-type", "retry-after", "x-ratelimit-limit", "x-ratelimit-remaining"] if headers.get(k) is not None},
        "raw_path": str(raw_path),
        "raw_bytes": len(payload),
        "parsed_kind": type(parsed).__name__,
    }
    (RAW / "semantic_scholar_batch_status.json").write_text(json.dumps(status_obj, indent=2, sort_keys=True) + "\n")
    return {"status": status_obj, "parsed": parsed}


def main() -> None:
    # Fetch arXiv per paper with a polite pause.
    arxiv_fetches = {}
    arxiv_records = {}
    for i, paper in enumerate(PAPERS):
        if i:
            time.sleep(3.2)
        url, meta = fetch_arxiv_for_paper(paper)
        meta["query_url"] = url
        arxiv_fetches[paper["slug"]] = meta
        arxiv_records.update(parse_arxiv_xml(Path(meta["path"])))

    unique_ids = []
    seen = set()
    for p in PAPERS:
        for s in p["sources"]:
            base = normalize_arxiv_id(s["arxiv_id"])
            if base not in seen:
                seen.add(base)
                unique_ids.append(base)

    s2 = fetch_semantic_scholar(unique_ids)
    s2_by_arxiv = {}
    if isinstance(s2["parsed"], list):
        for rec in s2["parsed"]:
            if not isinstance(rec, dict) or not rec:
                continue
            ext = rec.get("externalIds") or {}
            aid = ext.get("ArXiv") or ext.get("Arxiv") or ext.get("arXiv")
            if aid:
                s2_by_arxiv[normalize_arxiv_id(aid)] = rec

    rows = []
    missing_arxiv = []
    record_keys = []
    for paper in PAPERS:
        for idx, source in enumerate(paper["sources"], start=1):
            base = normalize_arxiv_id(source["arxiv_id"])
            meta = arxiv_records.get(base)
            if not meta:
                missing_arxiv.append({"paper_slug": paper["slug"], "arxiv_id": source["arxiv_id"]})
                meta = {
                    "arxiv_id_base": base,
                    "arxiv_id_versioned": base,
                    "exact_url": arxiv_exact_url(base),
                    "title": "ARXIV_METADATA_NOT_FOUND",
                    "year": "",
                    "authors": [],
                    "authors_display": "unknown authors",
                    "doi": "",
                    "summary": "",
                    "categories": [],
                    "primary_category": "",
                }
            s2rec = s2_by_arxiv.get(base, {}) if isinstance(s2_by_arxiv, dict) else {}
            record_key = f"{paper['slug']}|{base}"
            record_keys.append(record_key)
            rows.append({
                "record_key": record_key,
                "paper_slug": paper["slug"],
                "paper_title": paper["title"],
                "priority": idx,
                "arxiv_id_requested": source["arxiv_id"],
                "arxiv_id_base": meta["arxiv_id_base"],
                "arxiv_id_versioned": meta["arxiv_id_versioned"],
                "exact_url": meta["exact_url"],
                "title": meta["title"],
                "year": meta["year"],
                "authors": meta["authors"],
                "authors_display": meta["authors_display"],
                "doi": meta.get("doi", ""),
                "role": source["role"],
                "placement": source["placement"],
                "relevance": source["relevance"],
                "support_class": source["support"],
                "supports_actual_result": source["support"] in {"supports actual method", "supports scoped target stratification"},
                "semantic_scholar_found": bool(s2rec),
                "semantic_scholar_citationCount": s2rec.get("citationCount") if isinstance(s2rec, dict) else None,
                "semantic_scholar_year": s2rec.get("year") if isinstance(s2rec, dict) else None,
                "semantic_scholar_url": s2rec.get("url") if isinstance(s2rec, dict) else None,
                "abstract_available_arxiv": bool(meta.get("summary")),
            })

    dup_keys = sorted([k for k, c in Counter(record_keys).items() if c > 1])
    jsonl_path = LANE / f"literature_sources_wave2_citation_placement_{TS}.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")

    by_paper = {}
    for paper in PAPERS:
        prs = [r for r in rows if r["paper_slug"] == paper["slug"]]
        by_paper[paper["slug"]] = {
            "records": len(prs),
            "unique_source_bases": len({r["arxiv_id_base"] for r in prs}),
            "actual_method_or_scoped": sum(1 for r in prs if r["supports_actual_result"]),
            "future_or_status_only": sum(1 for r in prs if not r["supports_actual_result"]),
            "abstract_available": sum(1 for r in prs if r["abstract_available_arxiv"]),
            "doi_available": sum(1 for r in prs if r.get("doi")),
            "semantic_scholar_found": sum(1 for r in prs if r["semantic_scholar_found"]),
            "roles": dict(Counter(r["role"] for r in prs)),
        }

    summary = {
        "marker": f"LITERATURE_WAVE2_CITATION_PLACEMENT_{TS}",
        "utc": UTC_ISO,
        "local": LOCAL,
        "scope": "Wave-2 citation-placement/source-grounding for M2 P2, M3 P2, and M3 P3.",
        "records": len(rows),
        "unique_sources": len({r["arxiv_id_base"] for r in rows}),
        "papers": [p["slug"] for p in PAPERS],
        "by_paper": by_paper,
        "duplicate_record_keys": dup_keys,
        "missing_arxiv_records": missing_arxiv,
        "arxiv_fetches": arxiv_fetches,
        "semantic_scholar_status": s2["status"],
        "semantic_scholar_found_records": sum(1 for r in rows if r["semantic_scholar_found"]),
        "jsonl_path": str(jsonl_path),
        "raw_dir": str(RAW),
        "safety": "No credentials; no public/live/product DB/API/page_versions/trust/deploy/restart/git/billing/OAuth/cron/external-submission changes.",
    }
    summary_path = LANE / f"literature_summary_wave2_citation_placement_{TS}.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")

    md = build_markdown(rows, summary)
    md_path = LANE / f"literature_citation_placement_wave2_{TS}.md"
    md_path.write_text(md, encoding="utf-8")

    print(json.dumps({"md": str(md_path), "jsonl": str(jsonl_path), "summary": str(summary_path), "records": len(rows), "unique_sources": summary["unique_sources"], "duplicates": dup_keys, "semantic_scholar_http_status": s2["status"]["http_status"]}, indent=2, sort_keys=True))


def build_markdown(rows: list[dict], summary: dict) -> str:
    lines = []
    lines.append("# Literature/source grounding — Wave-2 citation placement review")
    lines.append("")
    lines.append(f"Marker: `LITERATURE_WAVE2_CITATION_PLACEMENT_{TS}`")
    lines.append("")
    lines.append(f"UTC: {UTC_ISO}  ")
    lines.append(f"Local: {LOCAL}")
    lines.append("")
    lines.append("## Scope and inputs read")
    lines.append("")
    lines.append("Focused on three Wave-2 high-risk papers after Lana's selection-disclosure revisions: **M2 P2**, **M3 P2**, and **M3 P3**. Read the overnight brief, swarm board, ledger, current run-root manuscripts, Lana lane-local revised manuscripts, current topic pages and pre-proposal backups, the prior Wave-2 source packet, and Hwao's latest director priorities. This is a source-grounding/citation-placement packet only: no manuscript, PDF, public page, product DB/API, deploy, git, billing/OAuth, cron, or external submission change is authorized or performed.")
    lines.append("")
    lines.append("## Acquisition and mechanical checks")
    lines.append("")
    lines.append("- Public arXiv export API only for primary metadata; raw XML was preserved by paper under `raw_payloads/{}/`.".format(TS))
    lines.append(f"- Unauthenticated Semantic Scholar batch enrichment attempted once; HTTP status: `{summary['semantic_scholar_status']['http_status']}`; matched records: {summary['semantic_scholar_found_records']}/{summary['records']}. It is enrichment only and not needed for the placement verdict.")
    lines.append(f"- Association records: **{summary['records']}** across **{summary['unique_sources']}** unique arXiv sources; duplicate record keys: `{summary['duplicate_record_keys']}`; arXiv metadata missing: `{summary['missing_arxiv_records']}`.")
    lines.append("- Every row below is classified as actual-method/scoped-result support versus future-data/model motivation. No citation is treated as support for unmeasured radio power, gas masses, depletion times, coupling efficiency, or simulation validation.")
    lines.append("")
    lines.append("## Paper-specific placement rules")
    for paper in PAPERS:
        prs = [r for r in rows if r["paper_slug"] == paper["slug"]]
        lines.append("")
        lines.append(f"### {paper['title']}")
        lines.append("")
        lines.append(f"Boundary: {paper['boundary']}")
        lines.append("")
        lines.append("| Priority | Source | Exact URL | Year / authors | Placement / relevance | Supports actual result, or only future data? |")
        lines.append("|---:|---|---|---|---|---|")
        for r in prs:
            year_auth = f"{r['year']} — {r['authors_display']}"
            placement = f"{r['placement']} {r['relevance']}"
            lines.append("| {priority} | {title} | {url} | {year_auth} | {placement} | {support} |".format(
                priority=r["priority"],
                title=escape_md(r["title"]),
                url=r["exact_url"],
                year_auth=escape_md(year_auth),
                placement=escape_md(placement),
                support=escape_md(r["support_class"]),
            ))
        lines.append("")
        lines.append(f"Integration guard: {paper['integration_guard']}")
    lines.append("")
    lines.append("## Later manuscript-integration checklist")
    lines.append("")
    lines.append("1. **M2 P2:** Add DR17/Kewley as method anchors; Best et al. can support massive-host/radio-mode target stratification; Santoro, McNamara--Nulsen, and Eckert belong only in the missing radio/X-ray/group-observable paragraph.")
    lines.append("2. **M3 P2:** Add DR17/Brinchmann around the optical denominator and catalog-property caveat; place COLD GASS/xCOLD GASS/xGASS only where the manuscript says CO/HI/dust gas data are required before gas-fraction/depletion-time/SFE claims.")
    lines.append("3. **M3 P3:** Add SDSS DR17 for the observed vector; simulation-suite citations belong in the future forward-modelling paragraph and must be paired with the statement that no mock catalogue has been run.")
    lines.append("4. Preserve the shared selection-function disclosure before citation expansion: 249,917 strict four-line S/N>=3 public rows, 60,000 cached rows, 24.0% coverage, SpecObjID row-cap caveat, and sSFR-dependent retention.")
    lines.append("")
    lines.append("## Artifact manifest")
    lines.append("")
    lines.append(f"- Markdown packet: `{LANE / f'literature_citation_placement_wave2_{TS}.md'}`")
    lines.append(f"- JSONL source/placement ledger: `{LANE / f'literature_sources_wave2_citation_placement_{TS}.jsonl'}`")
    lines.append(f"- Summary JSON: `{LANE / f'literature_summary_wave2_citation_placement_{TS}.json'}`")
    for paper in PAPERS:
        raw_xml = RAW / (paper["slug"] + "_arxiv_id_list.xml")
        lines.append(f"- Raw arXiv XML for {paper['slug']}: `{raw_xml}`")
    lines.append(f"- Semantic Scholar batch status/raw response: `{RAW / 'semantic_scholar_batch_status.json'}` and `{RAW / 'semantic_scholar_batch_raw.json'}`")
    lines.append("")
    lines.append("## Safety ledger")
    lines.append("")
    lines.append("- No credentials used; no ADS token/API-key access attempted.")
    lines.append("- No manuscript/PDF/public page/live root/product DB/API/page_versions/trust/deploy/restart/git/billing/OAuth/cron/external-submission changes.")
    lines.append("- This packet supports later local citation-integration review only; it does not authorize prose publication or public-linked PDF replacement.")
    lines.append("- No active execution phrase.")
    lines.append("")
    return "\n".join(lines)


def escape_md(s: str) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


if __name__ == "__main__":
    main()
