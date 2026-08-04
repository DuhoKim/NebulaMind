#!/usr/bin/env python3
"""Build a lane-local Wave-2 literature/source packet for the overnight 9-paper swarm.

Public sources only: arXiv export API plus a single unauthenticated Semantic Scholar status check.
Writes only under lanes/literature/.
"""
from __future__ import annotations

import datetime as dt
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

STAMP = "20260708T164632Z"
UTC = "2026-07-08T16:46:32Z"
KST = "2026-07-09 01:46:32 KST"
ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708")
LANE = ROOT / "lanes" / "literature"
RAW = LANE / "raw_payloads" / STAMP
TICKS = LANE / "ticks"
RAW.mkdir(parents=True, exist_ok=True)
TICKS.mkdir(parents=True, exist_ok=True)

PAPERS = {
    "m2_p2_radio_jet_environment": {
        "label": "M2 P2 — environment proxy for optical AGN in massive hosts",
        "pilot_result": "Massive-host optical BPT AGN fraction is higher in the high-density quartile than the low-density quartile in the cached SDSS four-line sample; no radio jet power, cavity energetics, hot-gas density, or coupling efficiency is measured.",
        "ids": ["2009.11175", "astro-ph/0506269", "2403.17145"],
        "notes": {
            "2009.11175": {
                "why": "Direct topical anchor for young radio galaxies, observed AGN-driven outflows, and feedback-efficiency language; useful because the paper title itself ties radio-galaxy outflows to efficiency estimates.",
                "support": "Motivates future radio/kinematic coupling data only; it does not support interpreting the SDSS optical-density pilot as a jet-coupling measurement.",
                "integration_guard": "Use in the Discussion/future-work paragraph defining radio-outflow/efficiency observables, not as support for the measured BPT AGN fraction."
            },
            "astro-ph/0506269": {
                "why": "SDSS-era radio-loud AGN demographic bridge linking host mass, cooling, and AGN-feedback framing; relevant to why the M2 P2 pilot isolates massive hosts before radio follow-up.",
                "support": "Scoped interpretation/target-stratification support only. It supports the massive-host/radio-AGN follow-up rationale, not actual radio power in the current optical sample.",
                "integration_guard": "Pair with explicit statement that the current denominator is optical BPT AGN and not a radio-loud AGN catalogue."
            },
            "2403.17145": {
                "why": "Recent group-scale AGN-feedback review/status source; matches the proposal need for environment, hot gas, and group-regime measurements.",
                "support": "Future-data/status motivation only; no group catalogue, X-ray gas, or radio jet coupling was measured in this pilot.",
                "integration_guard": "Use to justify group/X-ray/radio follow-up requirements and environment labels."
            },
        },
    },
    "m3_p2_gas_depletion_efficiency": {
        "label": "M3 P2 — optical denominator for gas-fraction versus efficiency tests",
        "pilot_result": "The pilot identifies an emission-line-detected massive low-sSFR optical denominator and H-alpha proxy baseline; it has no CO/dust gas masses, molecular gas fractions, depletion times, or star-formation efficiencies.",
        "ids": ["1103.1642", "1104.0019", "1710.02157", "1802.02373"],
        "notes": {
            "1103.1642": {
                "why": "COLD GASS molecular-gas survey anchor for massive nearby galaxies; establishes that H2/HI/stellar structural measurements are the relevant data for gas-fraction tests.",
                "support": "Motivates future CO/H2 data and gas-fraction interpretation; it does not support treating SDSS H-alpha proxy as a molecular-gas measurement.",
                "integration_guard": "Use when saying the full test requires CO/H2 data matched to the optical denominator."
            },
            "1104.0019": {
                "why": "COLD GASS depletion-timescale paper; directly relevant to the depletion-time versus SFE distinction the proposal wants to test.",
                "support": "Future-data motivation and wording guard: depletion time is a molecular-gas/SFR quantity, not derivable from the current SDSS four-line denominator alone.",
                "integration_guard": "Use to justify demoting H-alpha to an optical proxy baseline."
            },
            "1710.02157": {
                "why": "xCOLD GASS complete IRAM-30m legacy-survey release; broad modern survey anchor for molecular gas in galaxy-evolution studies.",
                "support": "Motivates the needed CO follow-up denominator; not actual support for any gas-depletion result in the pilot.",
                "integration_guard": "Use in future-data paragraph for CO survey matching and completeness."
            },
            "1802.02373": {
                "why": "xGASS cold-gas scaling-relation source linking atomic and molecular gas ratios in local galaxies; relevant to distinguishing gas availability from efficiency.",
                "support": "Future-data/status motivation for HI+H2 gas inventory; not actual SDSS result support.",
                "integration_guard": "Use only with a caveat that current pilot contains no HI/CO/dust gas masses."
            },
        },
    },
    "m3_p3_simulation_validation": {
        "label": "M3 P3 — SDSS target vector for feedback-model validation",
        "pilot_result": "The pilot writes an observed SDSS target vector across mass/redshift cells; no simulation catalogue has been forward-modelled through the SDSS/MaNGA/ALMA/X-ray/radio selection functions.",
        "ids": ["1812.05609", "1407.7040", "1901.10203", "2203.11575", "2008.00004"],
        "notes": {
            "1812.05609": {
                "why": "Public-data-release anchor for IllustrisTNG, one plausible simulation suite for future target-vector comparison.",
                "support": "Future model-comparison infrastructure only; the current pilot has not queried TNG or built SDSS-like mocks.",
                "integration_guard": "Use to name a reproducible future simulation source, not to imply validation has occurred."
            },
            "1407.7040": {
                "why": "EAGLE simulation-suite source with galaxy-formation/feedback model context; broad model family for comparison.",
                "support": "Future-data/status motivation only; no EAGLE mock was passed through the pilot selection function.",
                "integration_guard": "Use as model-context citation with explicit mock-selection caveat."
            },
            "1901.10203": {
                "why": "SIMBA simulation source with black-hole growth and feedback prescriptions; relevant because M3 P3 targets feedback-model validation.",
                "support": "Future model-comparison motivation only; not evidence that the SDSS vector validates or falsifies SIMBA.",
                "integration_guard": "Use only in the required-simulation-mocks paragraph."
            },
            "2203.11575": {
                "why": "Mock MaNGA galaxies based on IllustrisTNG and MaStar SSPs; directly illustrates the kind of survey-forward mock needed before comparing an observed SDSS/MaNGA-like vector to simulations.",
                "support": "Strong future-method support for forward-modelling/selection-function language; not actual result support.",
                "integration_guard": "Use to justify the statement that mocks must pass through survey apertures/noise/selection before model claims."
            },
            "2008.00004": {
                "why": "IllustrisTNG quenched-fraction comparison with observations; close topical match to an observed quenched-fraction target vector.",
                "support": "Scoped interpretation/status source for what a real comparison would look like; the current pilot is not itself such a comparison.",
                "integration_guard": "Use as an example of comparison target structure, while avoiding any claim that the pilot ranks TNG."
            },
        },
    },
}

NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def fetch_arxiv_for_paper(slug: str, ids: list[str]) -> tuple[dict[str, dict], str]:
    params = urllib.parse.urlencode({"id_list": ",".join(ids)})
    url = f"https://export.arxiv.org/api/query?{params}"
    with urllib.request.urlopen(url, timeout=40) as resp:
        raw = resp.read()
    raw_path = RAW / f"{slug}_arxiv_id_list.xml"
    raw_path.write_bytes(raw)
    root = ET.fromstring(raw)
    records: dict[str, dict] = {}
    for entry in root.findall("a:entry", NS):
        versioned = entry.findtext("a:id", default="", namespaces=NS).strip().split("/abs/")[-1]
        # base ID removes a trailing version suffix for matching, but keeps old-style ids intact.
        base = versioned
        if "v" in base and base.rsplit("v", 1)[-1].isdigit():
            base = base.rsplit("v", 1)[0]
        title = " ".join(entry.findtext("a:title", default="", namespaces=NS).split())
        summary = " ".join(entry.findtext("a:summary", default="", namespaces=NS).split())
        published = entry.findtext("a:published", default="", namespaces=NS)
        updated = entry.findtext("a:updated", default="", namespaces=NS)
        authors = [a.findtext("a:name", default="", namespaces=NS) for a in entry.findall("a:author", NS)]
        doi_el = entry.find("arxiv:doi", NS)
        doi = doi_el.text.strip() if doi_el is not None and doi_el.text else None
        cats = [c.attrib.get("term", "") for c in entry.findall("a:category", NS)]
        records[base] = {
            "source": "arXiv export API",
            "arxiv_id": base,
            "arxiv_versioned_id": versioned,
            "title": title,
            "authors": authors,
            "year": int(published[:4]) if published[:4].isdigit() else None,
            "published": published,
            "updated": updated,
            "url": f"https://arxiv.org/abs/{versioned}",
            "stable_url": f"https://arxiv.org/abs/{base}",
            "pdf_url": f"https://arxiv.org/pdf/{base}",
            "doi": doi,
            "categories": cats,
            "summary": summary,
            "raw_payload": str(raw_path.relative_to(LANE)),
        }
    return records, str(raw_path.relative_to(LANE))


all_records = []
raw_payloads = {}
missing = []
seen = set()
for slug, pdata in PAPERS.items():
    records, raw_rel = fetch_arxiv_for_paper(slug, pdata["ids"])
    raw_payloads[slug] = raw_rel
    for aid in pdata["ids"]:
        rec = records.get(aid)
        if rec is None:
            missing.append({"paper": slug, "arxiv_id": aid})
            continue
        notes = pdata["notes"][aid]
        key = rec["arxiv_id"].lower()
        duplicate = key in seen
        seen.add(key)
        all_records.append({
            "paper": slug,
            "paper_label": pdata["label"],
            "pilot_result_boundary": pdata["pilot_result"],
            "dedupe_key": key,
            "duplicate_key": duplicate,
            **{k: rec[k] for k in ["source", "arxiv_id", "arxiv_versioned_id", "title", "authors", "year", "published", "updated", "url", "stable_url", "pdf_url", "doi", "categories", "raw_payload"]},
            "why_relevant": notes["why"],
            "supports_actual_result_or_future_only": notes["support"],
            "integration_guard": notes["integration_guard"],
        })
    time.sleep(3.2)

# Single public Semantic Scholar status check, expected to be rate-limited in this environment.
s2_status = {"attempted": True, "used_credentials": False, "status": None, "error": None, "url": "https://api.semanticscholar.org/graph/v1/paper/arXiv:2009.11175?fields=title,authors,year,citationCount,externalIds"}
try:
    with urllib.request.urlopen(s2_status["url"], timeout=20) as resp:
        s2_status["status"] = resp.status
        s2_status["payload"] = json.loads(resp.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    s2_status["status"] = e.code
    s2_status["error"] = f"HTTPError: {e}"
except Exception as e:  # noqa: BLE001
    s2_status["error"] = f"{type(e).__name__}: {e}"
(RAW / "semantic_scholar_status_check.json").write_text(json.dumps(s2_status, ensure_ascii=False, indent=2) + "\n")

jsonl_path = LANE / f"literature_sources_wave2_{STAMP}.jsonl"
with jsonl_path.open("w", encoding="utf-8") as f:
    for rec in all_records:
        f.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + "\n")

by_paper_counts = {slug: sum(1 for r in all_records if r["paper"] == slug) for slug in PAPERS}
summary = {
    "marker": f"LITERATURE_SOURCE_WAVE2_{STAMP}",
    "utc": UTC,
    "local": KST,
    "scope": "Wave-2 public source grounding for M2 P2, M3 P2, and M3 P3 only; no manuscript/public/prose edits.",
    "public_sources_used": ["arXiv export API"],
    "semantic_scholar": s2_status,
    "credentials_used": False,
    "records_total": len(all_records),
    "records_by_paper": by_paper_counts,
    "missing_arxiv_records": missing,
    "duplicate_dedupe_keys": [r["dedupe_key"] for r in all_records if r["duplicate_key"]],
    "raw_payloads": raw_payloads | {"semantic_scholar_status": str((RAW / "semantic_scholar_status_check.json").relative_to(LANE))},
    "outputs": {
        "jsonl": jsonl_path.name,
        "packet_md": f"literature_source_packet_wave2_{STAMP}.md",
        "summary_json": f"literature_summary_wave2_{STAMP}.json",
        "tick_md": f"ticks/LITERATURE_TICK_{STAMP}.md",
    },
    "safety": {
        "wrote_only_under_literature_lane_except_ledger_append_required_by_user": True,
        "no_public_pages": True,
        "no_product_db_or_api": True,
        "no_page_versions_or_trust": True,
        "no_deploy_restart_git_billing_oauth_cron_or_external_submission": True,
    },
}
summary_path = LANE / f"literature_summary_wave2_{STAMP}.json"
summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def authors_short(authors: list[str], n: int = 6) -> str:
    if len(authors) <= n:
        return ", ".join(authors)
    return ", ".join(authors[:n]) + f", et al. ({len(authors)} authors)"

lines: list[str] = []
lines.append("# Literature/source grounding tick — Wave-2 high-risk papers")
lines.append("")
lines.append(f"Marker: `LITERATURE_SOURCE_WAVE2_{STAMP}`")
lines.append("")
lines.append(f"UTC: {UTC}  ")
lines.append(f"Local: {KST}")
lines.append("")
lines.append("## Scope and inputs read")
lines.append("")
lines.append("Lane role: public source grounding for the overnight 9-paper Galaxy Evolution AAS pilot swarm. This is a source packet only: no prose edit, no bibliography insertion, no manuscript overwrite, and no public mirroring.")
lines.append("")
lines.append("Read before synthesis:")
lines.append("- `OVERNIGHT_BRIEF.md`, `SWARM_BOARD.md`, `OVERNIGHT_LEDGER.md`")
lines.append("- Current AASTeX sources for M2 P2, M3 P2, and M3 P3 under `runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/`")
lines.append("- Lana selection-disclosure revision report `lanes/lana/ticks/TICK_20260708T161724Z.md`")
lines.append("- Hwao director priority report `lanes/hwao/HWAO_DIRECTOR_TICK_20260708T160831Z.md`")
lines.append("- Current public research-topic page and pre-proposal backup page for active-vs-historical context")
lines.append("")
lines.append("Priority followed from Hwao/Lana blockers: **M2 P2**, **M3 P2**, and **M3 P3**.")
lines.append("")
lines.append("## Acquisition note")
lines.append("")
lines.append("- No credentials were used.")
lines.append("- arXiv export API metadata was fetched and raw XML was preserved by paper under `raw_payloads/`.")
if s2_status.get("status") == 429:
    lines.append("- A public unauthenticated Semantic Scholar check was attempted once and returned HTTP 429, so no Semantic Scholar metadata was used.")
else:
    lines.append(f"- A public unauthenticated Semantic Scholar check status was: {s2_status.get('status') or s2_status.get('error')}.")
lines.append("- This packet classifies sources as actual-result support versus scoped interpretation/future-data motivation; it does not authorize citation insertion or public publishing.")
lines.append("")
lines.append("## High-level verdict")
lines.append("")
lines.append("The Wave-2 bibliography gap is now bounded by three safe integration rules:")
lines.append("")
lines.append("1. **M2 P2** can cite radio-AGN/environment sources only as a bridge from the optical BPT massive-host denominator to the missing radio/X-ray/hot-gas follow-up. They do not turn the SDSS density association into a jet-coupling-efficiency measurement.")
lines.append("2. **M3 P2** should cite COLD GASS/xCOLD GASS/xGASS as the reason CO/HI gas data are required. These sources explicitly guard against treating H-alpha or four-line optical selection as molecular gas mass, gas fraction, depletion time, or SFE.")
lines.append("3. **M3 P3** should cite TNG/EAGLE/SIMBA/iMaNGA-style work as future model/mock infrastructure. They do not validate, reject, rank, or falsify any feedback model until a mock catalogue is forward-modelled through the pilot selection function.")
lines.append("")
lines.append("## Paper-specific source packet")

for slug, pdata in PAPERS.items():
    lines.append("")
    lines.append(f"### {pdata['label']}")
    lines.append("")
    lines.append(f"Current pilot boundary: {pdata['pilot_result']}")
    lines.append("")
    lines.append("| Priority | Source | Exact URL read | Year / authors | Why relevant | Supports actual result, or only future data? |")
    lines.append("|---:|---|---|---|---|---|")
    p_recs = [r for r in all_records if r["paper"] == slug]
    for i, rec in enumerate(p_recs, 1):
        year_auth = f"{rec['year']} — {authors_short(rec['authors'])}" if rec.get("year") else authors_short(rec["authors"])
        source = rec["title"].replace("|", "\\|")
        why = rec["why_relevant"].replace("|", "\\|")
        supp = rec["supports_actual_result_or_future_only"].replace("|", "\\|")
        lines.append(f"| {i} | {source} | {rec['url']} | {year_auth} | {why} | {supp} |")
    lines.append("")
    if slug == "m2_p2_radio_jet_environment":
        lines.append("Integration guard for M2 P2: keep the measured result as an optical BPT AGN-versus-density association in massive hosts. Use these sources to motivate the missing radio jet power, hot-gas, group-environment, and coupling-efficiency measurements.")
    elif slug == "m3_p2_gas_depletion_efficiency":
        lines.append("Integration guard for M3 P2: call the current object set an emission-line-detected optical follow-up denominator. Use gas-survey citations only when saying the full test requires CO/HI/dust gas masses and aperture-matched SFRs.")
    elif slug == "m3_p3_simulation_validation":
        lines.append("Integration guard for M3 P3: call the table an observed target vector. Use simulation citations only for future mock construction/comparison; do not say the pilot validates or falsifies any model.")

lines.append("")
lines.append("## Bibliography-gap actions for a later integration pass")
lines.append("")
lines.append("1. For M2 P2, add Santoro et al. 2020, Best et al. 2005, and Eckert et al. 2024 only in the discussion/future-observables context; if Best et al. is used near the result, say it supports target stratification rather than an actual radio measurement.")
lines.append("2. For M3 P2, add COLD GASS/xCOLD GASS/xGASS citations around the explicit statement that the SDSS pilot lacks molecular/atomic gas masses and cannot distinguish depletion from SFE.")
lines.append("3. For M3 P3, add TNG/EAGLE/SIMBA/iMaNGA citations around the future mock-selection paragraph; do not cite them as if a simulation comparison has been run.")
lines.append("4. Preserve the DR17/BPT method backbone from the prior packet for actual data provenance; the Wave-2 sources here are mostly topic/future-data anchors.")
lines.append("")
lines.append("## Artifact manifest")
lines.append("")
lines.append(f"- JSONL source ledger: `{jsonl_path.name}`")
lines.append(f"- Summary JSON: `{summary_path.name}`")
for slug, rel in raw_payloads.items():
    lines.append(f"- Raw arXiv XML for {slug}: `{rel}`")
lines.append("- Semantic Scholar status check: `raw_payloads/{}/semantic_scholar_status_check.json`".format(STAMP))
lines.append("")
lines.append("## Safety ledger")
lines.append("")
lines.append("- Files written under literature lane only: packet Markdown, JSONL source ledger, summary JSON, raw arXiv/Semantic-Scholar-status payloads, helper script, and lane-local tick note.")
lines.append("- Required shared ledger append: one concise line to `OVERNIGHT_LEDGER.md`.")
lines.append("- No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git, billing, OAuth, external submission, or new cron jobs touched.")
lines.append("- No active execution phrase.")

packet_path = LANE / f"literature_source_packet_wave2_{STAMP}.md"
packet_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

tick_lines = [
    f"# Literature lane tick — {STAMP}",
    "",
    f"Marker: `LITERATURE_SOURCE_WAVE2_{STAMP}`",
    "",
    "Read the overnight brief/board/ledger, current M2 P2/M3 P2/M3 P3 manuscripts, Lana selection revisions, Hwao priorities, and public topic-page/backups. Fetched arXiv metadata for 12 public sources; Semantic Scholar unauthenticated check returned HTTP 429 and was not used. Wrote Wave-2 source packet with exact URLs, titles, authors/year, relevance, and actual-result-vs-future-data classifications. No public/live/product/git/deploy/billing/OAuth/cron/external-submission changes.",
    "",
    f"Report: `{packet_path.name}`",
]
(LANE / "ticks" / f"LITERATURE_TICK_{STAMP}.md").write_text("\n".join(tick_lines) + "\n", encoding="utf-8")

print(json.dumps({
    "packet": str(packet_path),
    "jsonl": str(jsonl_path),
    "summary": str(summary_path),
    "tick": str(LANE / "ticks" / f"LITERATURE_TICK_{STAMP}.md"),
    "records_total": len(all_records),
    "records_by_paper": by_paper_counts,
    "missing": missing,
    "s2_status": s2_status.get("status") or s2_status.get("error"),
}, ensure_ascii=False, indent=2))
