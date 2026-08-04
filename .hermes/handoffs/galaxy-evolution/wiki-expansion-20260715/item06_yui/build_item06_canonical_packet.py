#!/usr/bin/env python3
"""Build the bounded Yui canonical advisory packet for review-base item 06."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CANONICAL_CLAIM_SECTIONS = (
    (
        "Established findings",
        (
            {"key": "REV06-E01", "body": "For massive main-sequence galaxies at z≈1–3, CO and dust surveys report molecular-gas mass fractions of order 0.3–0.5, substantially above local analogs. [REV06-P001] [REV06-P004] [REV06-P014]"},
            {"key": "REV06-E02", "body": "Integrated molecular-gas depletion time varies with redshift and displacement from the star-forming main sequence; starbursts consume gas faster than main-sequence systems. [REV06-P015] [REV06-P021]"},
            {"key": "REV06-E03", "body": "Cold-accretion and gas-regulator models link cosmological inflow to the evolution of cold-gas content and star-formation rates. [REV06-P028] [REV06-P031] [REV06-P035]"},
            {"key": "REV06-E04", "body": "The CO-to-H₂ conversion factor rises toward low metallicity as an increasing fraction of molecular gas becomes CO-dark. [REV06-P006] [REV06-P008]"},
            {"key": "REV06-E05", "body": "For integrated molecular gas, the global star-formation relation is close to linear for main-sequence systems, while mixing disks and starbursts introduces offsets and slope changes. [REV06-P003] [REV06-P017]"},
            {"key": "REV06-E06", "body": "Massive star-forming disks at z≈1–3 show turbulent ionized-gas kinematics with intrinsic dispersions of order 40–80 km s⁻¹. [REV06-P018] [REV06-P019]"},
            {"key": "REV06-E08", "body": "Long-wavelength Rayleigh–Jeans dust continuum can serve as an ISM-mass proxy within calibrated dust-temperature and metallicity regimes. [REV06-P009] [REV06-P024] [REV06-P025]"},
            {"key": "REV06-E09", "body": "Star-formation-law models calibrated across galactic environments place the efficiency per free-fall time at order one percent. [REV06-P034]"},
            {"key": "REV06-E10", "body": "Gas-rich disk-instability simulations connect radial inflow and compaction to central mass growth and subsequent quenching pathways. [REV06-P030] [REV06-P033] [REV06-P039]"},
            {"key": "REV06-E11", "body": "The star-forming main sequence remains relatively tight, with scatter of order 0.3 dex, across a broad redshift range. [REV06-P010] [REV06-P011] [REV06-P012]"},
            {"key": "REV06-E12", "body": "Nearby resolved maps show H I surface-density saturation and an H₂-dominated star-formation relation in denser regions. [REV06-P007] [REV06-P016]"},
        ),
    ),
    (
        "Open debates and tensions",
        (
            {"key": "REV06-D01", "body": "The exact dependence of the CO-to-H₂ conversion factor on shielding, metallicity, and radiation field remained uncertain, especially for low-metallicity high-redshift systems. [REV06-P006]"},
            {"key": "REV06-D02", "body": "Whether the dust-to-gas ratio stays approximately linear with metallicity or steepens in low-metallicity and high-redshift regimes remained an important calibration uncertainty. [REV06-P009] [REV06-P024]"},
            {"key": "REV06-D03", "body": "The literature still allowed both a disk–starburst bimodality and a smoother continuous sequence of star-formation efficiencies. [REV06-P015] [REV06-P023] [REV06-P027]"},
            {"key": "REV06-D04", "body": "Available scaling data did not cleanly distinguish a depletion-time dependence on redshift from one tied to Hubble or internal dynamical times. [REV06-P001]"},
            {"key": "REV06-D06", "body": "The survival of giant high-redshift clumps versus rapid disruption by feedback remained unsettled. [REV06-P022]"},
            {"key": "REV06-D07", "body": "Variation in integrated depletion time could reflect true local efficiency changes, changing structure, or both. [REV06-P003]"},
            {"key": "REV06-D08", "body": "Gas-regulator models were not unique because mass loading, inflow metallicity, and equilibration times remained degenerate. [REV06-P028] [REV06-P031]"},
        ),
    ),
    (
        "Measurements, model benchmarks, and calibrations",
        (
            {"key": "REV06-N01", "body": "A Milky-Way-like conversion factor αCO≈4.36 M☉ (K km s⁻¹ pc²)⁻¹, including helium, is the baseline for near-solar-metallicity main-sequence disks. [REV06-P006]"},
            {"key": "REV06-N02", "body": "The deferred packet adopts a low-metallicity correction approximately αCO∝(Z/Z☉)⁻¹·⁵ to (Z/Z☉)⁻² within its stated regime. [REV06-P006] [REV06-P008]"},
            {"key": "REV06-N03", "body": "The retained main-sequence-offset fit uses μgas∝(sSFR/sSFRMS)^0.53. [REV06-P001]"},
            {"key": "REV06-N04", "body": "The retained main-sequence-offset fit uses tdep∝(sSFR/sSFRMS)^−0.44. [REV06-P001]"},
            {"key": "REV06-N07", "body": "A representative intrinsic velocity-dispersion range for z≈1–3 star-forming disks is σ₀≈40–80 km s⁻¹, subject to beam-smearing corrections. [REV06-P018] [REV06-P019]"},
            {"key": "REV06-N08", "body": "A solar-metallicity baseline dust-to-gas ratio of order 100 underlies common dust-continuum gas-mass conversions, with strong caveats away from the calibrated regime. [REV06-P009] [REV06-P024]"},
        ),
    ),
    (
        "Unknowns and uncertainties as of 2020",
        (
            {"key": "REV06-U01", "body": "Direct 21-cm constraints on the cosmic evolution of atomic gas remained limited well below cosmic noon, leaving the H I replenishment pathway weakly constrained. [REV06-P016]"},
            {"key": "REV06-U03", "body": "CO and dust become difficult total-gas tracers in low-metallicity high-redshift dwarfs, leaving their molecular reservoirs uncertain. [REV06-P006]"},
            {"key": "REV06-U05", "body": "Uncertain multi-phase outflow mass-loading factors prevented a unique observational test of feedback prescriptions in gas-regulator models. [REV06-P028] [REV06-P031]"},
        ),
    ),
)

EXCLUDED_CLAIMS = {
    "REV06-E07",
    "REV06-D05",
    "REV06-N05",
    "REV06-N06",
    "REV06-U02",
    "REV06-U04",
    "REV06-U06",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    without_tags = re.sub(r"<[^>]+>", "", value)
    return re.sub(r"\s+", " ", html.unescape(without_tags)).strip()


def source_line(result: dict[str, Any], classification: dict[str, Any]) -> str:
    raw = result["raw_identity"]
    public = result["semantic_scholar_identity"] or {}
    title = clean_text(public.get("title")) or clean_text(raw["title"])
    topics = ", ".join(classification["topic_scope"])
    membership_entry = clean_text(result["exact_bibliography_entries"][0])
    return (
        f"- [{result['key']}] {clean_text(raw['author'])} ({raw['year']}, "
        f"{clean_text(raw['journal'])}). \"{title}.\" "
        f"DOI `{result['canonical_doi']}`; arXiv `{result['canonical_arxiv']}`; "
        f"ADS `{raw['ads']}`. Role: `{classification['canonical_role']}`. "
        f"Topic scope: {topics}. Review-bibliography identity: {membership_entry}"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", type=Path, required=True)
    parser.add_argument("--identity", type=Path, required=True)
    parser.add_argument("--classification", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--bibliography-receipt", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    raw_text = args.raw.read_text(encoding="utf-8")
    identity = json.loads(args.identity.read_text(encoding="utf-8"))
    classifications = json.loads(args.classification.read_text(encoding="utf-8"))["entries"]
    results = identity["results"]
    result_by_key = {result["key"]: result for result in results}
    usable = [
        result
        for result in results
        if result["disposition"] == "USABLE_COMPOSITE_VERIFIED"
    ]
    quarantined = [
        result
        for result in results
        if result["disposition"].startswith("QUARANTINE")
    ]
    usable_keys = {result["key"] for result in usable}
    quarantined_keys = {result["key"] for result in quarantined}

    if len(usable) != 35 or len(quarantined) != 10:
        raise ValueError("Expected 35 usable and 10 quarantined source rows")
    if set(classifications) != set(result_by_key):
        raise ValueError("Classification and identity key sets differ")

    extracted = CANONICAL_CLAIM_SECTIONS
    retained_claim_keys = [
        claim["key"] for _, claims in extracted for claim in claims
    ]
    if len(retained_claim_keys) != 27 or len(set(retained_claim_keys)) != 27:
        raise ValueError("Expected 27 unique retained claim keys")
    if set(retained_claim_keys) & EXCLUDED_CLAIMS:
        raise ValueError("A quarantined claim key remains in the canonical sections")

    retained_claim_text = "\n".join(
        claim["body"] for _, claims in extracted for claim in claims
    )
    retained_references = set(re.findall(r"\[(REV06-P\d{3})\]", retained_claim_text))
    contaminated_references = sorted(retained_references & quarantined_keys)
    if contaminated_references:
        raise ValueError(f"Quarantined references remain in claims: {contaminated_references}")
    unknown_references = sorted(retained_references - usable_keys)
    if unknown_references:
        raise ValueError(f"Unknown references remain in claims: {unknown_references}")

    primary = sorted(
        (
            result
            for result in usable
            if classifications[result["key"]]["canonical_role"].startswith("primary_")
        ),
        key=lambda result: result["key"],
    )
    supporting_reviews = sorted(
        (
            result
            for result in usable
            if classifications[result["key"]]["canonical_role"] == "supporting_review"
        ),
        key=lambda result: result["key"],
    )
    if len(primary) != 33 or len(supporting_reviews) != 2:
        raise ValueError("Expected 33 primary sources and 2 supporting reviews")

    created_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        "# Tacconi, Genzel & Sternberg (2020) — Yui Canonical Advisory Packet",
        "",
        f"Generated: `{created_at}`",
        "",
        "Status: `IDENTITY_RECONCILED_ADVISORY_ONLY`",
        "",
        "This packet supersedes the deferred raw packet for item 06 at the advisory-file layer only. It does not mutate the live wiki, database, trust state, runtime, deployment, Git history, or public site.",
        "",
        "## Scope and evidence boundary",
        "",
        "- Authoritative review membership is established from the pinned `Literature Cited` section of arXiv:2003.06245 (pages 43–52 in the pinned 58-page PDF).",
        "- Composite identifiers are accepted only when DOI/arXiv/ADS metadata resolves to one physical paper and the review-bibliography identity matches.",
        "- The retained claims are bounded restatements of the deferred packet after identity and topic-scope filtering; primary-paper claim text was not re-extracted in this reconciliation pass.",
        "- Polluted raw identity anchors were not copied as claim-level evidence excerpts.",
        "- Ten non-member or mismatched source rows are quarantined. Seven raw claim rows are excluded: four because their usable support disappeared after source quarantine and three because the surviving source topic did not support the raw claim.",
        "",
        "## Claim sections",
        "",
    ]
    for output_heading, claims in extracted:
        lines.extend([f"### {output_heading}", ""])
        lines.extend(f"- [{claim['key']}] {claim['body']}" for claim in claims)
        lines.append("")

    lines.extend(
        [
            "## Canonical source ledger",
            "",
            f"Primary sources: **{len(primary)}**. Supporting reviews: **{len(supporting_reviews)}**. Supporting reviews are not counted as primary citations.",
            "",
            "### Primary empirical/model/simulation sources",
            "",
        ]
    )
    lines.extend(
        source_line(result, classifications[result["key"]]) for result in primary
    )
    lines.extend(["", "### Supporting reviews", ""])
    lines.extend(
        source_line(result, classifications[result["key"]])
        for result in supporting_reviews
    )

    lines.extend(["", "## Quarantine ledger", ""])
    for result in sorted(quarantined, key=lambda item: item["key"]):
        raw = result["raw_identity"]
        classification = classifications[result["key"]]
        candidate_text = "; ".join(
            clean_text(entry) for entry in result.get("exact_bibliography_entries") or []
        ) or "none"
        lines.append(
            f"- [{result['key']}] {clean_text(raw['author'])} ({raw['year']}), "
            f"raw title \"{clean_text(raw['title'])}\" — `{result['disposition']}`. "
            f"Reason: {classification['reason']} Exact bibliography match: {candidate_text}"
        )

    lines.extend(
        [
            "",
            "### Quarantined claim keys",
            "",
            "- " + ", ".join(sorted(EXCLUDED_CLAIMS)),
            "",
            "## Custody ledger",
            "",
            f"- Raw packet SHA-256: `{sha256(args.raw)}`",
            f"- Raw inventory SHA-256: `{sha256(args.inventory)}`",
            f"- Authoritative bibliography receipt SHA-256: `{sha256(args.bibliography_receipt)}`",
            f"- Composite identity reconciliation SHA-256: `{sha256(args.identity)}`",
            f"- Role/topic classification SHA-256: `{sha256(args.classification)}`",
            "",
            "## Safety receipt",
            "",
            "- Browser/account action: none.",
            "- Live wiki/DB/trust mutation: none.",
            "- Deploy/restart: none.",
            "- Git write/publication: none.",
            "- Hwao/DESI crew interruption after redirect: none.",
            "- Owner: Yui; local advisory artifacts only.",
            "",
        ]
    )
    args.output.write_text("\n".join(lines), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
