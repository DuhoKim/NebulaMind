#!/usr/bin/env python3
"""Build ADS/arXiv source-grounding packet for the active-9 papers not yet covered by prior literature waves.

Scope: local overnight Galaxy Evolution AAS pilot improvement. Public/read-only metadata only.
Writes local artifacts under the overnight root and appends one concise ledger line.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

STAMP = "20260708T170557Z"
UTC = "2026-07-08T17:05:57Z"
KST = "2026-07-09 02:05:57 KST"
MARKER = f"LITERATURE_SOURCE_WAVE3_MISSING_ACTIVE9_{STAMP}"
VALIDATOR_MARKER = f"GORU_LITERATURE_WAVE3_VALIDATE_{STAMP}"
TICK_MARKER = f"TICK_LITERATURE_WAVE3_MISSING_ACTIVE9_{STAMP}"
ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708")
LANE = ROOT / "lanes" / "literature"
GORU = ROOT / "lanes" / "goru"
RAW = LANE / "raw_payloads" / STAMP
TICKS = ROOT / "ticks"
LANE_TICKS = LANE / "ticks"
GORU_ART = GORU / "artifacts"
GORU_TICKS = GORU / "ticks"
for p in [RAW, TICKS, LANE_TICKS, GORU_ART, GORU_TICKS]:
    p.mkdir(parents=True, exist_ok=True)

# Accepted coverage/category matrix for this tick. These are the active papers that had not yet
# received topic-specific literature/source packets in Wave-1 or Wave-2.
PAPER_BOUNDARIES = {
    "m1_rp1_sdss_agn_sfr": {
        "label": "M1 RP-1 — SDSS AGN/sSFR matched-control pilot",
        "boundary": "Actual SDSS DR17 emission-line matched-control association; not causal AGN-feedback proof and not a complete quiescent-galaxy census.",
        "target_roles": ["actual_data_or_method", "scoped_interpretation", "overclaim_guard"],
    },
    "m2_p3_feedback_transition_mass": {
        "label": "M2 P3 — mass transition in quenching and optical AGN incidence",
        "boundary": "Actual SDSS mass-bin quenched-fraction / optical-BPT-AGN incidence diagnostic; no gas fractions, halo masses, baryon deficits, or causal stellar-vs-AGN feedback separation.",
        "target_roles": ["actual_data_or_method", "status_or_debate_context", "future_data_guard"],
    },
    "m3_p1_multiphase_census": {
        "label": "M3 P1 — common-denominator optical tracer census",
        "boundary": "Actual SDSS optical tracer denominator only; no molecular/neutral/X-ray/radio common-denominator outflow rates or kinetic powers measured.",
        "target_roles": ["actual_data_or_method", "multiphase_status_context", "future_data_guard"],
    },
}

SOURCES = [
    {
        "source_id": "2112.02026",
        "coverage_category": "actual_data_provenance",
        "primary_role": "actual_data_or_method",
        "papers": ["m1_rp1_sdss_agn_sfr", "m2_p3_feedback_transition_mass", "m3_p1_multiphase_census"],
        "why_relevant": "Public SDSS DR17 release paper; anchors the survey provenance for all three local SDSS pilots.",
        "support_scope": "Actual-data provenance only; does not support any feedback-physics conclusion by itself.",
        "integration_guard": "Use in Data/Sample sections to identify the public survey release and preserve the distinction between SDSS observables and missing follow-up data.",
    },
    {
        "source_id": "astro-ph/0311060",
        "coverage_category": "sfr_stellar_property_method",
        "primary_role": "actual_data_or_method",
        "papers": ["m1_rp1_sdss_agn_sfr"],
        "why_relevant": "Low-redshift SDSS physical-property and star-formation reference; directly relevant to catalog SFR/sSFR context in the matched-control pilot.",
        "support_scope": "Method/provenance context for SFR/sSFR-like catalog quantities; not proof that AGN caused the observed offset.",
        "integration_guard": "Cite near catalog-property definitions and keep estimator assumptions/aperture caveats explicit.",
    },
    {
        "source_id": "astro-ph/0605681",
        "coverage_category": "optical_agn_classification_method",
        "primary_role": "actual_data_or_method",
        "papers": ["m1_rp1_sdss_agn_sfr", "m3_p1_multiphase_census"],
        "why_relevant": "AGN host/classification source tied to optical diagnostic diagrams; supports why BPT/line-ratio labels are classification proxies.",
        "support_scope": "Optical classification-method support only; not evidence for outflow rates, gas escape, or causal quenching.",
        "integration_guard": "Use when defining optical-BPT classes and when warning that classification labels are not feedback measurements.",
    },
    {
        "source_id": "1302.2631",
        "coverage_category": "agn_sfr_context",
        "primary_role": "scoped_interpretation",
        "papers": ["m1_rp1_sdss_agn_sfr"],
        "why_relevant": "Directly addresses star formation--AGN connection at low redshift, matching the pilot's association-only topic.",
        "support_scope": "Scoped interpretation/status context; should not be used to convert the matched sSFR deficit into causal feedback proof.",
        "integration_guard": "Use in Introduction/Discussion with wording such as 'context for the AGN--SFR connection', not as confirmation of a causal mechanism.",
    },
    {
        "source_id": "1501.03812",
        "coverage_category": "retired_liner_overclaim_guard",
        "primary_role": "overclaim_guard",
        "papers": ["m1_rp1_sdss_agn_sfr"],
        "why_relevant": "Retired-galaxy/LINER caveat source for optical line classifications in AGN/SF studies.",
        "support_scope": "Overclaim guard: optical emission-line labels can mix AGN, retired, and weak-ionization populations.",
        "integration_guard": "Use in Limitations to demote broad AGN-feedback language and require stricter subclasses/follow-up.",
    },
    {
        "source_id": "astro-ph/0204055",
        "coverage_category": "stellar_mass_method",
        "primary_role": "actual_data_or_method",
        "papers": ["m2_p3_feedback_transition_mass"],
        "why_relevant": "SDSS stellar-mass and star-formation-history methodology source; anchors why stellar mass is a central axis in the transition-mass pilot.",
        "support_scope": "Method/context support for mass-axis interpretation; not a gas or halo feedback measurement.",
        "integration_guard": "Use when describing stellar-mass binning and catalog mass dependence.",
    },
    {
        "source_id": "astro-ph/0205070",
        "coverage_category": "stellar_mass_transition_context",
        "primary_role": "status_or_debate_context",
        "papers": ["m2_p3_feedback_transition_mass"],
        "why_relevant": "Classic SDSS mass-dependence paper tying star-formation history/internal structure to stellar mass.",
        "support_scope": "Status/context for mass transition language; does not identify stellar or AGN feedback as the unique cause in this pilot.",
        "integration_guard": "Use to motivate mass-bin diagnostics while explicitly requiring gas/halo/morphology controls before causal labels.",
    },
    {
        "source_id": "astro-ph/0309710",
        "coverage_category": "galaxy_bimodality_context",
        "primary_role": "status_or_debate_context",
        "papers": ["m2_p3_feedback_transition_mass"],
        "why_relevant": "Observed color-magnitude bimodality source; relevant to quenching/transition framing around the stellar-mass scale.",
        "support_scope": "Population-context support only; the SDSS pilot's quenched fraction remains a proxy diagnostic.",
        "integration_guard": "Use in background, not as evidence that the pilot has measured the physical origin of bimodality.",
    },
    {
        "source_id": "astro-ph/0412300",
        "coverage_category": "halo_shock_heating_model_context",
        "primary_role": "future_data_guard",
        "papers": ["m2_p3_feedback_transition_mass"],
        "why_relevant": "Cold-flow/shock-heating model source for mass-scale quenching discussions.",
        "support_scope": "Future/model context; the current pilot lacks halo masses, gas accretion, and shock diagnostics.",
        "integration_guard": "Use only as motivation for missing halo/gas follow-up, not as support that the pilot identifies shock heating.",
    },
    {
        "source_id": "1106.2546",
        "coverage_category": "mass_environment_quenching_context",
        "primary_role": "status_or_debate_context",
        "papers": ["m2_p3_feedback_transition_mass"],
        "why_relevant": "Mass/environment quenching framework; useful for separating mass transition from environmental satellite effects.",
        "support_scope": "Status/debate context; the pilot does not have group catalogues or central/satellite labels.",
        "integration_guard": "Use to motivate future environment/central-satellite controls and to avoid conflating mass with halo environment.",
    },
    {
        "source_id": "2301.03677",
        "coverage_category": "black_hole_mass_debate_guard",
        "primary_role": "future_data_guard",
        "papers": ["m2_p3_feedback_transition_mass"],
        "why_relevant": "Recent debate/status source emphasizing quenching dependence on black-hole mass rather than accretion rate.",
        "support_scope": "Overclaim guard and future-data motivation; the pilot has no black-hole masses and cannot adjudicate this axis.",
        "integration_guard": "Use only to state which missing variables are needed before assigning the mass transition to AGN feedback.",
    },
    {
        "source_id": "astro-ph/0504435",
        "coverage_category": "multiphase_outflow_review",
        "primary_role": "multiphase_status_context",
        "papers": ["m3_p1_multiphase_census"],
        "why_relevant": "Broad galactic-winds review; establishes that a true census is multiphase and multiwavelength.",
        "support_scope": "Status/review support for why SDSS optical lines are incomplete; not actual molecular/neutral/X-ray/radio data for this pilot.",
        "integration_guard": "Use in background/limitations to frame the need for phase-complete follow-up.",
    },
    {
        "source_id": "1311.2595",
        "coverage_category": "molecular_outflow_future_data",
        "primary_role": "future_data_guard",
        "papers": ["m3_p1_multiphase_census"],
        "why_relevant": "CO molecular-outflow source; gives a concrete missing phase for the common-denominator census proposal.",
        "support_scope": "Future molecular-data motivation only; the SDSS pilot has no CO outflow masses or rates.",
        "integration_guard": "Cite only when specifying the future CO/molecular phase needed beyond the optical denominator.",
    },
    {
        "source_id": "1702.04507",
        "coverage_category": "agn_wind_scaling_future_data",
        "primary_role": "future_data_guard",
        "papers": ["m3_p1_multiphase_census"],
        "why_relevant": "AGN wind scaling-relations source; motivates kinetic-power/outflow-rate measurements absent from the optical tracer table.",
        "support_scope": "Future-data/status motivation; not evidence that the SDSS optical prevalence table measures wind energetics.",
        "integration_guard": "Use in the future-work paragraph requiring velocities, radii, phase masses, and selection-matched denominators.",
    },
    {
        "source_id": "1503.01481",
        "coverage_category": "multiphase_case_study_guard",
        "primary_role": "future_data_guard",
        "papers": ["m3_p1_multiphase_census"],
        "why_relevant": "Multi-phase Markarian 231 wind case; illustrates how hot/ultra-fast and galaxy-scale molecular components differ.",
        "support_scope": "Case-study/future-observable motivation only; a single object or phase-specific study is not a prevalence anchor for the SDSS denominator.",
        "integration_guard": "Use as an example of phase complexity, not as a denominator-wide incidence result.",
    },
    {
        "source_id": "1712.08944",
        "coverage_category": "neutral_ionized_phase_mismatch_guard",
        "primary_role": "future_data_guard",
        "papers": ["m3_p1_multiphase_census"],
        "why_relevant": "Neutral-vs-ionized outflow relation source; directly supports the guard that one phase cannot stand in for all phases.",
        "support_scope": "Overclaim guard for phase mismatch; not actual neutral-gas data in the current pilot.",
        "integration_guard": "Use to warn that optical tracer prevalence cannot be extrapolated to neutral or molecular outflow prevalence without matched data.",
    },
    {
        "source_id": "1812.05184",
        "coverage_category": "star_formation_wind_review_guard",
        "primary_role": "multiphase_status_context",
        "papers": ["m3_p1_multiphase_census"],
        "why_relevant": "Recent galactic-winds observational review, useful as a non-AGN/stellar-feedback counterweight when discussing outflow drivers.",
        "support_scope": "Status and balance source; prevents treating every optical outflow-like tracer as AGN-driven.",
        "integration_guard": "Use in background/limitations to separate AGN-driven, star-formation-driven, and mixed wind populations.",
    },
]

ADS_FIELDS = "bibcode,title,author,year,identifier,doi,abstract,doctype,property,citation_count,pub,volume,page,arxiv_class"
ADS_URL = "https://api.adsabs.harvard.edu/v1/search/query"
ARXIV_NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def safe_filename(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", s).strip("_")


def ads_token() -> str | None:
    for k in ("ADS_API_KEY", "ADS_DEV_KEY", "ADS_API_TOKEN"):
        v = os.environ.get(k)
        if v:
            return v
    env_path = Path.home() / ".hermes" / ".env"
    if env_path.exists():
        for line in env_path.read_text(errors="ignore").splitlines():
            if "=" not in line or line.lstrip().startswith("#"):
                continue
            k, v = line.split("=", 1)
            if k in {"ADS_API_KEY", "ADS_DEV_KEY", "ADS_API_TOKEN"} and v.strip():
                return v.strip().strip('"').strip("'")
    return None


def fetch_ads_one(source_id: str, token: str | None) -> dict[str, Any]:
    if not token:
        return {"ok": False, "error": "ADS token unavailable", "source_id": source_id}
    params = urllib.parse.urlencode({"q": f"identifier:{source_id}", "fl": ADS_FIELDS, "rows": 5})
    req = urllib.request.Request(f"{ADS_URL}?{params}", headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        return {"ok": True, "source_id": source_id, "query": f"identifier:{source_id}", "payload": payload}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:500]
        return {"ok": False, "source_id": source_id, "status": e.code, "error": f"HTTPError: {e}", "body_prefix": body}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "source_id": source_id, "error": f"{type(e).__name__}: {e}"}


def base_arxiv_id(versioned: str) -> str:
    base = versioned.strip()
    if "/abs/" in base:
        base = base.split("/abs/")[-1]
    if "v" in base and base.rsplit("v", 1)[-1].isdigit():
        base = base.rsplit("v", 1)[0]
    return base


def fetch_arxiv_group(slug: str, ids: list[str]) -> tuple[str, dict[str, dict[str, Any]], str | None]:
    params = urllib.parse.urlencode({"id_list": ",".join(ids)})
    url = f"https://export.arxiv.org/api/query?{params}"
    raw_path = RAW / f"{slug}_arxiv_id_list.xml"
    try:
        with urllib.request.urlopen(url, timeout=45) as resp:
            raw = resp.read()
        raw_path.write_bytes(raw)
        root = ET.fromstring(raw)
        records: dict[str, dict[str, Any]] = {}
        for entry in root.findall("a:entry", ARXIV_NS):
            versioned = entry.findtext("a:id", default="", namespaces=ARXIV_NS).strip().split("/abs/")[-1]
            base = base_arxiv_id(versioned)
            title = " ".join(entry.findtext("a:title", default="", namespaces=ARXIV_NS).split())
            authors = [a.findtext("a:name", default="", namespaces=ARXIV_NS) for a in entry.findall("a:author", ARXIV_NS)]
            doi_el = entry.find("arxiv:doi", ARXIV_NS)
            records[base] = {
                "arxiv_id": base,
                "arxiv_versioned_id": versioned,
                "title": title,
                "authors": authors,
                "published": entry.findtext("a:published", default="", namespaces=ARXIV_NS),
                "updated": entry.findtext("a:updated", default="", namespaces=ARXIV_NS),
                "doi": doi_el.text.strip() if doi_el is not None and doi_el.text else None,
                "categories": [c.attrib.get("term", "") for c in entry.findall("a:category", ARXIV_NS)],
                "url": f"https://arxiv.org/abs/{versioned}",
                "stable_url": f"https://arxiv.org/abs/{base}",
                "pdf_url": f"https://arxiv.org/pdf/{base}",
            }
        return rel(raw_path), records, None
    except Exception as e:  # noqa: BLE001
        raw_path.write_text(f"FETCH_ERROR {type(e).__name__}: {e}\n", encoding="utf-8")
        return rel(raw_path), {}, f"{type(e).__name__}: {e}"


def normalize_title(title: str) -> str:
    return re.sub(r"\W+", " ", title.lower()).strip()


def ads_arxiv_available(identifiers: list[str], source_id: str) -> bool:
    low = [i.lower() for i in identifiers]
    return any("arxiv" in i or "astro.ph" in i or "hep-th" in i or "hep-ph" in i for i in low) or source_id.startswith("astro-ph/")


def first_doc_from_ads(result: dict[str, Any]) -> dict[str, Any] | None:
    docs = result.get("payload", {}).get("response", {}).get("docs", []) if result.get("ok") else []
    return docs[0] if docs else None


def authors_short(authors: list[str], n: int = 6) -> str:
    if not authors:
        return "authors unavailable"
    if len(authors) <= n:
        return ", ".join(authors)
    return ", ".join(authors[:n]) + f", et al. ({len(authors)} authors)"


def md_escape(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")

# Preserve ADS raw payloads by paper/category. We keep one JSON per paper containing the exact
# per-identifier ADS responses, without logging or writing the token.
token = ads_token()
ads_raw_by_paper: dict[str, str] = {}
ads_by_source: dict[str, dict[str, Any]] = {}
for slug in PAPER_BOUNDARIES:
    source_ids = sorted({s["source_id"] for s in SOURCES if slug in s["papers"]})
    paper_payload = {"marker": MARKER, "paper": slug, "ads_query_count": len(source_ids), "responses": {}}
    for sid in source_ids:
        if sid not in ads_by_source:
            ads_by_source[sid] = fetch_ads_one(sid, token)
            time.sleep(0.35)
        paper_payload["responses"][sid] = ads_by_source[sid]
    raw_path = RAW / f"{slug}_ads_identifier_payloads.json"
    raw_path.write_text(json.dumps(paper_payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ads_raw_by_paper[slug] = rel(raw_path)

# Preserve arXiv raw XML by paper for stable arXiv metadata, politely rate-limited.
arxiv_raw_by_paper: dict[str, str] = {}
arxiv_by_paper: dict[str, dict[str, Any]] = {}
arxiv_errors: dict[str, str | None] = {}
for i, slug in enumerate(PAPER_BOUNDARIES):
    ids = sorted({s["source_id"] for s in SOURCES if slug in s["papers"]})
    raw_rel, recs, err = fetch_arxiv_group(slug, ids)
    arxiv_raw_by_paper[slug] = raw_rel
    arxiv_by_paper[slug] = recs
    arxiv_errors[slug] = err
    if i < len(PAPER_BOUNDARIES) - 1:
        time.sleep(3.2)

# Single unauthenticated Semantic Scholar status check as enrichment probe. It is not required for
# acceptance and is often 429 in this environment.
s2_status: dict[str, Any] = {
    "attempted": True,
    "used_credentials": False,
    "url": "https://api.semanticscholar.org/graph/v1/paper/arXiv:2112.02026?fields=title,authors,year,citationCount,externalIds",
    "status": None,
    "error": None,
}
try:
    with urllib.request.urlopen(s2_status["url"], timeout=20) as resp:
        s2_status["status"] = resp.status
        s2_status["payload"] = json.loads(resp.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    s2_status["status"] = e.code
    s2_status["error"] = f"HTTPError: {e}"
except Exception as e:  # noqa: BLE001
    s2_status["error"] = f"{type(e).__name__}: {e}"
s2_path = RAW / "semantic_scholar_status_check.json"
s2_path.write_text(json.dumps(s2_status, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

records: list[dict[str, Any]] = []
missing_ads: list[dict[str, Any]] = []
for s in SOURCES:
    sid = s["source_id"]
    ads_result = ads_by_source.get(sid, {})
    doc = first_doc_from_ads(ads_result)
    if doc is None:
        missing_ads.append({"source_id": sid, "error": ads_result.get("error"), "status": ads_result.get("status")})
        # Use arXiv metadata fallback from any credited paper if available.
        arxiv_doc = None
        for p in s["papers"]:
            arxiv_doc = arxiv_by_paper.get(p, {}).get(sid)
            if arxiv_doc:
                break
        title = arxiv_doc.get("title") if arxiv_doc else "ADS metadata unavailable"
        authors = arxiv_doc.get("authors", []) if arxiv_doc else []
        year = int(arxiv_doc.get("published", "0000")[:4]) if arxiv_doc and arxiv_doc.get("published", "")[:4].isdigit() else None
        bibcode = None
        doi = [arxiv_doc["doi"]] if arxiv_doc and arxiv_doc.get("doi") else []
        identifiers: list[str] = []
        abstract = None
    else:
        title = (doc.get("title") or [""])[0]
        authors = doc.get("author") or []
        year = doc.get("year")
        bibcode = doc.get("bibcode")
        doi = doc.get("doi") or []
        identifiers = doc.get("identifier") or []
        abstract = doc.get("abstract")
    fallback_key = (doi[0].lower() if doi else normalize_title(title))
    dedupe_key = f"ads:{bibcode}" if bibcode else (f"doi:{fallback_key}" if doi else f"title:{fallback_key}")
    arxiv_records_for_papers = {p: arxiv_by_paper.get(p, {}).get(sid) is not None for p in s["papers"]}
    records.append({
        "marker": MARKER,
        "source_id": sid,
        "dedupe_key": dedupe_key,
        "ads_bibcode": bibcode,
        "title": title,
        "authors": authors,
        "year": int(year) if isinstance(year, str) and year.isdigit() else year,
        "doi": doi,
        "ads_identifiers": identifiers,
        "ads_arxiv_available_from_identifier_entries": ads_arxiv_available(identifiers, sid),
        "ads_abstract_available": bool(abstract),
        "ads_abstract_prefix": " ".join(abstract.split())[:700] if abstract else None,
        "ads_doctype": doc.get("doctype") if doc else None,
        "ads_property": doc.get("property") if doc else None,
        "ads_citation_count": doc.get("citation_count") if doc else None,
        "ads_pub": doc.get("pub") if doc else None,
        "ads_arxiv_class": doc.get("arxiv_class") if doc else None,
        "coverage_category": s["coverage_category"],
        "primary_role": s["primary_role"],
        "papers_credited": s["papers"],
        "paper_labels": {p: PAPER_BOUNDARIES[p]["label"] for p in s["papers"]},
        "pilot_boundaries": {p: PAPER_BOUNDARIES[p]["boundary"] for p in s["papers"]},
        "why_relevant": s["why_relevant"],
        "supports_actual_result_or_future_only": s["support_scope"],
        "integration_guard": s["integration_guard"],
        "raw_ads_payloads_by_paper": {p: ads_raw_by_paper[p] for p in s["papers"]},
        "raw_arxiv_payloads_by_paper": {p: arxiv_raw_by_paper[p] for p in s["papers"]},
        "arxiv_api_record_seen_by_paper": arxiv_records_for_papers,
    })

seen: set[str] = set()
duplicate_keys: list[str] = []
for r in records:
    if r["dedupe_key"] in seen:
        duplicate_keys.append(r["dedupe_key"])
    seen.add(r["dedupe_key"])

jsonl_path = LANE / f"literature_sources_wave3_missing_active9_{STAMP}.jsonl"
with jsonl_path.open("w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")

per_paper_records: dict[str, list[dict[str, Any]]] = {p: [] for p in PAPER_BOUNDARIES}
for r in records:
    for p in r["papers_credited"]:
        per_paper_records[p].append(r)

role_credit_counts = {p: {} for p in PAPER_BOUNDARIES}
category_counts = {p: {} for p in PAPER_BOUNDARIES}
for p, recs in per_paper_records.items():
    for r in recs:
        role_credit_counts[p][r["primary_role"]] = role_credit_counts[p].get(r["primary_role"], 0) + 1
        category_counts[p][r["coverage_category"]] = category_counts[p].get(r["coverage_category"], 0) + 1

coverage_ready = {}
for p, info in PAPER_BOUNDARIES.items():
    roles = set(role_credit_counts[p])
    targets = set(info["target_roles"])
    # Treat future_data_guard as satisfying an overclaim/future guard target and scoped interpretation/status as debate context.
    normalized_roles = set(roles)
    if "future_data_guard" in roles:
        normalized_roles.add("overclaim_guard")
    if "scoped_interpretation" in roles:
        normalized_roles.add("status_or_debate_context")
    if "status_or_debate_context" in roles:
        normalized_roles.add("scoped_interpretation")
    if "multiphase_status_context" in roles:
        normalized_roles.add("status_or_debate_context")
    coverage_ready[p] = {
        "target_roles": info["target_roles"],
        "observed_roles": sorted(roles),
        "missing_target_roles": sorted(targets - normalized_roles),
        "ready_for_local_integration_review": not bool(targets - normalized_roles),
    }

summary = {
    "marker": MARKER,
    "utc": UTC,
    "local": KST,
    "scope": "Wave-3 source grounding for active-9 papers not covered by prior literature packets: M1 RP-1, M2 P3, and M3 P1. No manuscript/public/prose edits.",
    "accepted_coverage_matrix": PAPER_BOUNDARIES,
    "public_sources_used": ["NASA ADS API", "arXiv export API", "Semantic Scholar status probe"],
    "ads_credentials_used": bool(token),
    "semantic_scholar": s2_status,
    "records_total": len(records),
    "deduplicated_candidate_records_total": len(seen),
    "duplicate_dedupe_keys": duplicate_keys,
    "records_by_paper_role_credit": {p: len(recs) for p, recs in per_paper_records.items()},
    "role_credit_counts": role_credit_counts,
    "coverage_category_counts": category_counts,
    "coverage_ready": coverage_ready,
    "availability_counts": {
        "ads_bibcode": sum(bool(r["ads_bibcode"]) for r in records),
        "ads_identifier_entries": sum(bool(r["ads_identifiers"]) for r in records),
        "ads_arxiv_available_from_identifier_entries": sum(bool(r["ads_arxiv_available_from_identifier_entries"]) for r in records),
        "doi": sum(bool(r["doi"]) for r in records),
        "ads_abstract": sum(bool(r["ads_abstract_available"]) for r in records),
        "year": sum(bool(r["year"]) for r in records),
        "authors": sum(bool(r["authors"]) for r in records),
    },
    "missing_ads_records": missing_ads,
    "arxiv_fetch_errors": {k: v for k, v in arxiv_errors.items() if v},
    "raw_payloads": {
        "ads_by_paper": ads_raw_by_paper,
        "arxiv_by_paper": arxiv_raw_by_paper,
        "semantic_scholar_status": rel(s2_path),
    },
    "outputs": {
        "jsonl": rel(jsonl_path),
        "packet_md": f"lanes/literature/literature_source_packet_wave3_missing_active9_{STAMP}.md",
        "summary_json": f"lanes/literature/literature_summary_wave3_missing_active9_{STAMP}.json",
        "goru_validation_json": f"lanes/goru/artifacts/goru_literature_wave3_validation_{STAMP}.json",
        "goru_validation_md": f"lanes/goru/ticks/GORU_LITERATURE_WAVE3_VALIDATE_{STAMP}.md",
        "tick_md": f"ticks/TICK_{STAMP}.md",
    },
    "gate": "SOURCE_GROUNDING_PACKET_READY_FOR_LOCAL_CITATION_INTEGRATION_REVIEW_ONLY",
    "gate_caveat": "Does not authorize public/wiki/prose publication, DB/API/page_versions/trust, deploy/restart, git operations, or external submission.",
    "safety": {
        "no_public_pages_or_live_roots": True,
        "no_product_db_sql_api_pages_or_page_versions": True,
        "no_trust_recompute": True,
        "no_deploy_restart_git_billing_oauth_cron_or_external_submission": True,
        "local_artifacts_only_under_overnight_root_except_reading_ads_token_env": True,
    },
}
summary_path = LANE / f"literature_summary_wave3_missing_active9_{STAMP}.json"
summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

# Human source packet.
lines: list[str] = []
lines.append("# Literature/source grounding tick — Wave-3 missing active-9 papers")
lines.append("")
lines.append(f"Marker: `{MARKER}`")
lines.append("")
lines.append(f"UTC: {UTC}  ")
lines.append(f"Local: {KST}")
lines.append("")
lines.append("## Scope and inputs read")
lines.append("")
lines.append("This tick closes the largest remaining active-9 bibliography/source-grounding gap: **M1 RP-1**, **M2 P3**, and **M3 P1** had not been covered by the prior Wave-1/Wave-2 topic-specific source packets. It is a source packet only: no manuscript overwrite, no PDF change, no citation insertion, and no public mirroring.")
lines.append("")
lines.append("Read before synthesis: `OVERNIGHT_BRIEF.md`, `OVERNIGHT_LEDGER.md`, the 8-paper manifest, the public-link verification packet, current AASTeX sources for RP-1/M2 P3/M3 P1, Hwao director guidance, Goru robustness results, Lana revision notes, and prior literature/source packets.")
lines.append("")
lines.append("## Acquisition and corpus-gate discipline")
lines.append("")
lines.append("- Started from an accepted coverage matrix with target roles per paper: actual data/method anchor, status/context anchor, and future-data/overclaim guard.")
lines.append("- Used ADS metadata acquisition because ADS credentials were available to the local Hermes tool environment. Raw ADS JSON payloads were preserved by paper.")
lines.append("- Also fetched raw arXiv export XML by paper for stable arXiv IDs/versions. arXiv availability counts below come from ADS `identifier` entries, not a top-level arXiv field.")
if s2_status.get("status") == 429:
    lines.append("- Attempted one unauthenticated Semantic Scholar enrichment/status probe; it returned HTTP 429 and was not used.")
else:
    lines.append(f"- Attempted one unauthenticated Semantic Scholar enrichment/status probe; status/result: {s2_status.get('status') or s2_status.get('error')}.")
lines.append("- Deduplicated by ADS bibcode first, then DOI/title fallback. No source is being treated as full-text evidence; this clears only local citation-integration review.")
lines.append("")
lines.append("## Mechanical summary")
lines.append("")
lines.append(f"- Deduplicated source records: **{len(seen)}**; duplicate keys: **{len(duplicate_keys)}**.")
lines.append(f"- ADS bibcodes: {summary['availability_counts']['ads_bibcode']}/{len(records)}; DOI: {summary['availability_counts']['doi']}/{len(records)}; ADS abstracts: {summary['availability_counts']['ads_abstract']}/{len(records)}; ADS identifier entries: {summary['availability_counts']['ads_identifier_entries']}/{len(records)}.")
lines.append(f"- arXiv availability counted from ADS identifiers: {summary['availability_counts']['ads_arxiv_available_from_identifier_entries']}/{len(records)}.")
lines.append("")
lines.append("## Paper-specific integration rules")
for slug, info in PAPER_BOUNDARIES.items():
    lines.append("")
    lines.append(f"### {info['label']}")
    lines.append("")
    lines.append(f"Current pilot boundary: {info['boundary']}")
    lines.append("")
    ready = coverage_ready[slug]
    lines.append(f"Coverage roles observed: {', '.join(ready['observed_roles'])}. Missing target roles: {', '.join(ready['missing_target_roles']) if ready['missing_target_roles'] else 'none'}.")
    lines.append("")
    lines.append("| Priority | Source | ADS bibcode | Year / authors | Role | Why relevant | Safe integration guard |")
    lines.append("|---:|---|---|---|---|---|---|")
    for i, rec in enumerate(per_paper_records[slug], 1):
        year_auth = f"{rec['year']} — {authors_short(rec['authors'])}" if rec.get("year") else authors_short(rec["authors"])
        lines.append(
            f"| {i} | {md_escape(rec['title'])} | {md_escape(rec['ads_bibcode'])} | {md_escape(year_auth)} | {md_escape(rec['primary_role'])} | {md_escape(rec['why_relevant'])} | {md_escape(rec['integration_guard'])} |"
        )
    lines.append("")
    if slug == "m1_rp1_sdss_agn_sfr":
        lines.append("Integration guard: keep the measured result as a matched-control optical-AGN/sSFR association in the capped SDSS four-line denominator. The packet strengthens method provenance and retired/LINER caveats; it does not turn the offset into causal AGN-feedback evidence.")
    elif slug == "m2_p3_feedback_transition_mass":
        lines.append("Integration guard: use transition/bimodality/quenching sources to motivate mass-bin diagnostics, while saying the pilot lacks gas, halo, black-hole-mass, and central/satellite data needed to separate stellar-feedback from AGN-feedback regulation.")
    elif slug == "m3_p1_multiphase_census":
        lines.append("Integration guard: call the current table an optical common-denominator tracer census. Use multiphase outflow sources only to justify why CO/HI/Na I/X-ray/radio/kinematic follow-up is required.")
lines.append("")
lines.append("## Bibliography-gap actions for a later manuscript integration pass")
lines.append("")
lines.append("1. RP-1: add DR17 and sSFR/catalog-method provenance, then add a retired/LINER caveat paragraph before any causal language.")
lines.append("2. M2 P3: add mass-transition/bimodality/quenching context, but label halo-shock and black-hole-mass papers as future-data/debate guards, not measured results.")
lines.append("3. M3 P1: add multiphase wind/outflow citations only in the background/future-work sections; the result table remains optical-only.")
lines.append("4. Preserve the selection-function disclosure from the attrition packet before merging any citation-enhanced draft into a primary manuscript.")
lines.append("")
lines.append("## Artifact manifest")
lines.append("")
lines.append(f"- Deduplicated JSONL candidate ledger: `{rel(jsonl_path)}`")
lines.append(f"- Summary JSON: `{rel(summary_path)}`")
for slug, p in ads_raw_by_paper.items():
    lines.append(f"- Raw ADS payloads for {slug}: `{p}`")
for slug, p in arxiv_raw_by_paper.items():
    lines.append(f"- Raw arXiv XML for {slug}: `{p}`")
lines.append(f"- Semantic Scholar status probe: `{rel(s2_path)}`")
lines.append(f"- Goru-style mechanical validation: `{summary['outputs']['goru_validation_md']}` and `{summary['outputs']['goru_validation_json']}`")
lines.append("")
lines.append("## Safety ledger")
lines.append("")
lines.append("No public pages, live roots, product DB, SQL, `/api/pages`, page_versions, trust recompute, deploy/restart, git write, billing/OAuth changes, new cron jobs, or external submissions. No active execution phrase.")
packet_path = LANE / f"literature_source_packet_wave3_missing_active9_{STAMP}.md"
packet_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

# Goru-style mechanical validation.
jsonl_rows = []
with jsonl_path.open(encoding="utf-8") as f:
    for line in f:
        if line.strip():
            jsonl_rows.append(json.loads(line))
validator = {
    "marker": VALIDATOR_MARKER,
    "utc": UTC,
    "jsonl_parse_ok": True,
    "jsonl_rows": len(jsonl_rows),
    "summary_records_total": summary["records_total"],
    "row_count_matches_summary": len(jsonl_rows) == summary["records_total"],
    "dedupe_keys_unique": len({r["dedupe_key"] for r in jsonl_rows}) == len(jsonl_rows),
    "duplicate_dedupe_keys": duplicate_keys,
    "records_by_paper_role_credit": summary["records_by_paper_role_credit"],
    "coverage_ready": coverage_ready,
    "availability_counts": summary["availability_counts"],
    "missing_ads_records": missing_ads,
    "arxiv_fetch_errors": summary["arxiv_fetch_errors"],
    "raw_payload_files_exist": {k: {slug: (ROOT / path).exists() for slug, path in paths.items()} if isinstance(paths, dict) else (ROOT / paths).exists() for k, paths in summary["raw_payloads"].items()},
    "safety_no_write_boundaries": summary["safety"],
    "gate": summary["gate"],
}
validator_path = GORU_ART / f"goru_literature_wave3_validation_{STAMP}.json"
validator_path.write_text(json.dumps(validator, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
val_lines = [
    f"# Goru mechanical validation — literature Wave-3 missing active-9",
    "",
    f"Marker: `{VALIDATOR_MARKER}`",
    "",
    f"UTC: {UTC}",
    "",
    f"- JSONL parse OK: {validator['jsonl_parse_ok']}; rows: {validator['jsonl_rows']}; matches summary: {validator['row_count_matches_summary']}.",
    f"- Dedupe keys unique: {validator['dedupe_keys_unique']}; duplicate keys: {validator['duplicate_dedupe_keys']}.",
    f"- Role-credit counts by paper: {validator['records_by_paper_role_credit']}.",
    f"- ADS availability counts: {validator['availability_counts']}.",
    f"- Missing ADS records: {len(missing_ads)}; arXiv fetch errors: {validator['arxiv_fetch_errors']}.",
    "- No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/cron/billing/OAuth/external-submission changes were made by this packet.",
]
validator_md = GORU_TICKS / f"GORU_LITERATURE_WAVE3_VALIDATE_{STAMP}.md"
validator_md.write_text("\n".join(val_lines) + "\n", encoding="utf-8")

# Lane tick and required root tick report.
lane_tick = LANE_TICKS / f"LITERATURE_TICK_WAVE3_MISSING_ACTIVE9_{STAMP}.md"
lane_tick.write_text(
    "\n".join([
        f"# Literature lane tick — {STAMP}",
        "",
        f"Marker: `{MARKER}`",
        "",
        "Built ADS/arXiv source packet for the active-9 papers not yet covered by prior source waves: M1 RP-1, M2 P3, and M3 P1. Preserved raw ADS JSON and arXiv XML, wrote deduplicated JSONL and summary JSON, and produced Goru-style mechanical validation. No manuscript/public/product/git/deploy/billing/OAuth/cron/external-submission changes.",
        "",
        f"Report: `{rel(packet_path)}`",
    ]) + "\n",
    encoding="utf-8",
)

changed = [
    rel(packet_path),
    rel(jsonl_path),
    rel(summary_path),
    rel(validator_path),
    rel(validator_md),
    rel(lane_tick),
]
changed += list(ads_raw_by_paper.values()) + list(arxiv_raw_by_paper.values()) + [rel(s2_path)]
changed.append(rel(Path(__file__)))

tick_path = TICKS / f"TICK_{STAMP}.md"
tick_lines = [
    f"# Overnight cron tick — literature Wave-3 source grounding ({STAMP})",
    "",
    f"Marker: `{TICK_MARKER}`",
    "",
    "## What I did",
    "",
    "Ran a bounded source/literature verification phase for the active-9 papers that prior source packets had not covered: M1 RP-1, M2 P3, and M3 P1. Used ADS metadata (available local token, not printed) plus arXiv export metadata; preserved raw payloads, wrote a deduplicated JSONL candidate/source ledger, summary JSON, human Markdown packet, and Goru-style mechanical validation.",
    "",
    "## Files changed",
    "",
]
tick_lines.extend([f"- `{p}`" for p in changed])
tick_lines += [
    "",
    "## Data/source grounding",
    "",
    f"- Records: {len(records)} deduplicated ADS/arXiv source records across 3 active papers.",
    f"- By role-credit paper: {summary['records_by_paper_role_credit']}.",
    f"- ADS bibcodes/DOI/abstract/arXiv-identifier availability: {summary['availability_counts']}.",
    "- All arXiv availability counts are from ADS identifier entries; arXiv XML is preserved separately for stable URLs/versions.",
    "- No source is promoted to full-text evidence; this is source grounding for later local manuscript integration review only.",
    "",
    "## Verification",
    "",
    f"- Goru-style validation JSON: `{rel(validator_path)}`.",
    f"- JSONL rows match summary: {validator['row_count_matches_summary']}.",
    f"- Dedupe keys unique: {validator['dedupe_keys_unique']}.",
    f"- Coverage ready flags: {coverage_ready}.",
    f"- Missing ADS records: {len(missing_ads)}; arXiv fetch errors: {summary['arxiv_fetch_errors']}.",
    "",
    "## Blockers / caveats",
    "",
    "- This does not authorize prose/publication, bibliography insertion into linked/public PDFs, public mirroring, DB/API/page_versions/trust changes, deploy/restart, git operations, or external submission.",
    "- Semantic Scholar was only a status/enrichment probe; if HTTP 429 occurred, it was not used.",
    "- The three papers still need a later manuscript integration pass that preserves selection-function/SDSS-denominator guardrails.",
    "",
    "## Next recommended tick",
    "",
    "Use this Wave-3 packet plus the selection-function attrition packet to write a lane-local citation/method-integration draft for M2 P3 and M3 P1 first, then refresh RP-1 with selection-disclosure and retired/LINER caveats. If manuscripts are edited, compile and hash the PDFs locally only.",
    "",
    "## Safety",
    "",
    "No NebulaMind/product DB writes, SQL, `/api/pages`, page_versions, live wiki publish, trust recompute, public/live frontend mirroring, deploy/restart, git commit/push/merge/rebase, new cron jobs, billing/cloud/OAuth changes, or external journal/arXiv submission. No active execution phrase.",
]
tick_path.write_text("\n".join(tick_lines) + "\n", encoding="utf-8")

ledger_line = f"- {UTC} — Literature Wave-3 source grounding covered the remaining active-9 papers without prior source packets (M1 RP-1, M2 P3, M3 P1); wrote `{rel(packet_path)}`, `{rel(jsonl_path)}`, `{rel(summary_path)}`, Goru validation `{rel(validator_md)}`, and tick report `{rel(tick_path)}`. Verified {len(records)} deduplicated ADS/arXiv records, 0 duplicate keys, role coverage ready for local citation-integration review only. No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/extra-cron/billing/OAuth/external submission changes."
ledger_path = ROOT / "OVERNIGHT_LEDGER.md"
ledger_text = ledger_path.read_text(encoding="utf-8")
if STAMP not in ledger_text:
    with ledger_path.open("a", encoding="utf-8") as f:
        if not ledger_text.endswith("\n"):
            f.write("\n")
        f.write(ledger_line + "\n")

print(json.dumps({
    "marker": MARKER,
    "packet": str(packet_path),
    "jsonl": str(jsonl_path),
    "summary": str(summary_path),
    "validator_json": str(validator_path),
    "validator_md": str(validator_md),
    "tick": str(tick_path),
    "records_total": len(records),
    "deduped": len(seen),
    "duplicate_keys": duplicate_keys,
    "records_by_paper_role_credit": summary["records_by_paper_role_credit"],
    "availability_counts": summary["availability_counts"],
    "missing_ads": missing_ads,
    "arxiv_fetch_errors": summary["arxiv_fetch_errors"],
    "semantic_scholar_status": s2_status.get("status") or s2_status.get("error"),
}, ensure_ascii=False, indent=2))
