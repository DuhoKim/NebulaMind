#!/usr/bin/env python3
"""Artifact-only retrieval filter calibration helpers.

This module intentionally performs no database access and no model calls.  It
works from labeled candidate artifacts and derives section-local thresholds.
"""

from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


STOPWORDS = frozenset(
    """
    a about above after against all also am an and any are as at be because been before
    being below between both but by can cannot could did do does doing down during each
    few for from further had has have having he her here hers him his how i if in into
    is it its itself may more most must my no nor not of off on once only or other our
    out over own same she should so some such than that the their them then there these
    they this those through to too under until up very was we were what when where which
    while who whom why will with would you your
    galaxy galaxies galactic evolution formation stellar star stars redshift cosmic
    universe astronomical astrophysical observations observed using based study studies
    model models simulation simulations data analysis results show shows suggest suggests
    paper papers research system systems object objects source sources sample samples
    """.split()
)

SECTION_SLUG_TO_LEGACY_SECTION = {
    "high_z_sf": "Physical Mechanisms",
    "shmr_halo_quenching": "Dark Matter, Halos & Structure Formation",
    "env_quenching": "Environmental Effects",
    "feedback_outflows": "AGN Feedback & Quenching Debates",
    "size_evolution": "Galaxy Scaling Relations & Size Evolution",
}

NEIGHBORING_DOMAIN_TAGS = {
    "single_object_agn",
    "stellar_object",
    "milky_way_local",
    "molecular_cloud",
    "instrumentation",
    "compact_object_transient",
}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")


def normalize_arxiv_id(value: Any) -> str:
    return str(value or "").strip().replace("arXiv:", "").replace("oai:arXiv.org:", "")


def tokenize(value: Any) -> list[str]:
    if value is None:
        text = ""
    elif isinstance(value, str):
        text = value
    else:
        text = json.dumps(value, ensure_ascii=False)
    tokens = re.findall(r"[a-z][a-z0-9\-]{2,}", text.lower())
    return [token for token in tokens if token not in STOPWORDS and not token.isdigit()]


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    pos = (len(ordered) - 1) * q
    lower = math.floor(pos)
    upper = math.ceil(pos)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] * (upper - pos) + ordered[upper] * (pos - lower)


def safe_div(num: float, den: float) -> float:
    return num / den if den else 0.0


def lexical_metadata_tags(title: str | None, abstract: str | None) -> list[str]:
    text = f"{title or ''}\n{abstract or ''}".lower()
    tags: set[str] = set()

    if re.search(r"\b(ngc|mrk|ark|eso|qso|bl\s*lac|seyfert|agn)\s*[- ]?\d+", text) and re.search(
        r"\b(reverberation|continuum lag|lag|accretion disk|broad-line|blr)\b", text
    ):
        tags.add("single_object_agn")
    if re.search(r"\b(pulsar|globular cluster|white dwarf|neutron star|x-ray binary|stellar wind|massive star)\b", text):
        tags.add("stellar_object")
    if re.search(r"\b(milky way|galactic center|galactic centre|local group|magellanic|nearby dwarf)\b", text):
        tags.add("milky_way_local")
    if re.search(r"\b(molecular cloud|dark cloud|filament|protostar|star-forming region|interstellar cloud)\b", text):
        tags.add("molecular_cloud")
    if re.search(r"\b(instrument|detector|pipeline|calibration|spectrograph|telescope performance|survey strategy)\b", text):
        tags.add("instrumentation")
    if re.search(r"\b(transient|fast radio burst|grb|supernova|tidal disruption|compact object)\b", text):
        tags.add("compact_object_transient")
    if re.search(r"\b(population|mass function|scaling relation|main sequence|quiescent|star-forming galaxies)\b", text):
        tags.add("galaxy_population")
    if re.search(r"\b(cosmological simulation|hydrodynamic simulation|n-body|illustris|eagle|tng|simba|zoom-in)\b", text):
        tags.add("cosmological_simulation")
    if re.search(r"\b(size|effective radius|half-light|morpholog|compact|disk|bulge|surface brightness)\b", text):
        tags.add("morphology_size")
    if re.search(r"\b(quench|feedback|outflow|agn feedback|suppression|green valley|red sequence)\b", text):
        tags.add("quenching")

    return sorted(tags)


@dataclass(frozen=True)
class FilteredRow:
    row: dict[str, Any]
    label: str
    section: str
    paper_id: str
    tags: list[str]
    context_score: float
    positive_score: float
    combined_score: float
    final_score: float
    dropped: bool
    drop_reasons: list[str]


def attach_candidate_metadata(
    labels: list[dict[str, Any]],
    element_pairs: list[dict[str, Any]],
    candidates: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    by_claim_paper: dict[tuple[int | None, str], dict[str, Any]] = {}
    by_element_paper: dict[tuple[str, str], dict[str, Any]] = {}

    for row in candidates:
        key = (row.get("claim_id"), normalize_arxiv_id(row.get("arxiv_id")))
        by_claim_paper[key] = row
    for row in element_pairs:
        paper_id = normalize_arxiv_id(row.get("arxiv_id"))
        by_element_paper[(str(row.get("element_id") or ""), paper_id)] = row
        by_claim_paper.setdefault((row.get("claim_id"), paper_id), row)

    enriched: list[dict[str, Any]] = []
    for label in labels:
        paper_id = normalize_arxiv_id(label.get("paper_id") or label.get("arxiv_id"))
        element_key = (str(label.get("element_id") or ""), paper_id)
        claim_key = (label.get("claim_id"), paper_id)
        metadata = by_element_paper.get(element_key) or by_claim_paper.get(claim_key) or {}
        merged = {**metadata, **label}
        merged["paper_id"] = paper_id
        merged["target_section"] = label.get("target_section") or label.get("section") or "unknown"
        merged["target_section_title"] = label.get("target_section_title") or merged.get("claim_section_snapshot") or ""
        enriched.append(merged)
    return enriched


def derive_positive_terms(rows: list[dict[str, Any]]) -> dict[str, float]:
    citable_docs: list[set[str]] = []
    off_docs: list[set[str]] = []
    for row in rows:
        text = " ".join(
            str(row.get(key) or "")
            for key in (
                "target_section_title",
                "claim_text_snapshot",
                "element_text",
                "paper_title_snapshot",
                "paper_abstract_snapshot",
            )
        )
        tokens = set(tokenize(text))
        if row.get("label") == "citable":
            citable_docs.append(tokens)
        elif row.get("label") == "off_domain":
            off_docs.append(tokens)

    citable_df = Counter(term for doc in citable_docs for term in doc)
    off_df = Counter(term for doc in off_docs for term in doc)
    terms: dict[str, float] = {}
    for term, c_count in citable_df.items():
        if c_count < 2 and len(citable_docs) >= 8:
            continue
        off_count = off_df.get(term, 0)
        c_rate = (c_count + 0.5) / (len(citable_docs) + 1.0)
        off_rate = (off_count + 0.5) / (len(off_docs) + 1.0)
        lift = math.log(c_rate / off_rate)
        if lift > 0:
            terms[term] = lift
    return dict(sorted(terms.items(), key=lambda item: (-item[1], item[0]))[:50])


def tag_lift(rows: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    counts: dict[str, Counter[str]] = defaultdict(Counter)
    totals = Counter()
    for row in rows:
        label = row.get("label") or "unknown"
        totals[label] += 1
        for tag in row.get("tags", []):
            counts[tag][label] += 1
    lifts: dict[str, dict[str, float]] = {}
    for tag, label_counts in counts.items():
        off_rate = (label_counts.get("off_domain", 0) + 0.5) / (totals.get("off_domain", 0) + 1.0)
        cit_rate = (label_counts.get("citable", 0) + 0.5) / (totals.get("citable", 0) + 1.0)
        lifts[tag] = {
            "off_domain_count": label_counts.get("off_domain", 0),
            "citable_count": label_counts.get("citable", 0),
            "off_domain_lift_vs_citable": round(off_rate / cit_rate, 4),
        }
    return lifts


def score_row(row: dict[str, Any], positive_terms: dict[str, float]) -> tuple[float, float, float]:
    context_tokens = set(
        tokenize(
            " ".join(
                str(row.get(key) or "")
                for key in ("target_section_title", "claim_text_snapshot", "element_text", "normalized_subject", "normalized_mechanism")
            )
        )
    )
    paper_tokens = set(tokenize(f"{row.get('paper_title_snapshot') or ''}\n{row.get('paper_abstract_snapshot') or ''}"))
    overlap = context_tokens & paper_tokens
    lexical_score = safe_div(len(overlap), len(context_tokens))

    positive_den = sum(weight for term, weight in positive_terms.items() if term in context_tokens) or sum(positive_terms.values())
    positive_num = sum(weight for term, weight in positive_terms.items() if term in overlap)
    positive_score = safe_div(positive_num, positive_den)
    combined_score = (0.55 * lexical_score) + (0.45 * positive_score)
    return lexical_score, positive_score, combined_score


def calibrate_section(rows: list[dict[str, Any]], section: str) -> dict[str, Any]:
    for row in rows:
        row["tags"] = lexical_metadata_tags(row.get("paper_title_snapshot"), row.get("paper_abstract_snapshot"))

    positive_terms = derive_positive_terms(rows)
    lifts = tag_lift(rows)
    enriched_tags = {
        tag
        for tag, metrics in lifts.items()
        if metrics["off_domain_count"] >= 2
        and metrics["citable_count"] == 0
        and metrics["off_domain_lift_vs_citable"] >= 2.0
    }

    paper_labels: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        paper_id = normalize_arxiv_id(row.get("paper_id"))
        if paper_id:
            paper_labels[paper_id][row.get("label") or "unknown"] += 1
    suppressed_papers = {
        paper_id
        for paper_id, counts in paper_labels.items()
        if counts.get("off_domain", 0) >= 3 and counts.get("citable", 0) == 0
    }

    scored: list[dict[str, Any]] = []
    for row in rows:
        lexical_score, positive_score, combined_score = score_row(row, positive_terms)
        scored.append(
            {
                **row,
                "context_score": lexical_score,
                "positive_score": positive_score,
                "combined_score": combined_score,
            }
        )

    citable_scores = [row["combined_score"] for row in scored if row.get("label") == "citable"]
    off_scores = [row["combined_score"] for row in scored if row.get("label") == "off_domain"]
    citable_floor = percentile(citable_scores, 0.20)
    off_domain_high = percentile(off_scores, 0.80)

    filtered: list[FilteredRow] = []
    for row in scored:
        final_score = row["combined_score"]
        reasons: list[str] = []
        row_tags = set(row.get("tags", []))
        enriched_tag_gate = False
        paper_suppression_gate = False
        if row_tags & enriched_tags:
            final_score *= 0.68
            reasons.append("off_domain_enriched_tag_downweight")
            if row["combined_score"] < off_domain_high:
                enriched_tag_gate = True
                reasons.append("off_domain_enriched_tag_gate")
        if row_tags & NEIGHBORING_DOMAIN_TAGS and row["combined_score"] < off_domain_high:
            final_score *= 0.82
            reasons.append("neighboring_domain_tag_downweight")
        if normalize_arxiv_id(row.get("paper_id")) in suppressed_papers:
            final_score *= 0.15
            reasons.append("page_local_paper_suppression")
            paper_suppression_gate = True

        score_gate = final_score < citable_floor
        dropped = score_gate or enriched_tag_gate or paper_suppression_gate
        if score_gate:
            reasons.append("derived_score_gate")
        filtered.append(
            FilteredRow(
                row=row,
                label=str(row.get("label") or "unknown"),
                section=section,
                paper_id=normalize_arxiv_id(row.get("paper_id")),
                tags=sorted(row_tags),
                context_score=round(row["context_score"], 6),
                positive_score=round(row["positive_score"], 6),
                combined_score=round(row["combined_score"], 6),
                final_score=round(final_score, 6),
                dropped=dropped,
                drop_reasons=reasons,
            )
        )

    return {
        "section": section,
        "positive_terms": positive_terms,
        "tag_lift": lifts,
        "off_domain_enriched_tags": sorted(enriched_tags),
        "suppressed_papers": sorted(suppressed_papers),
        "thresholds": {
            "citable_combined_score_p20": round(citable_floor, 6),
            "off_domain_combined_score_p80": round(off_domain_high, 6),
        },
        "rows": filtered,
    }


def summarize_rows(rows: list[FilteredRow]) -> dict[str, Any]:
    before = Counter(row.label for row in rows)
    after = Counter(row.label for row in rows if not row.dropped)
    dropped = Counter(row.label for row in rows if row.dropped)
    total_before = sum(before.values())
    total_after = sum(after.values())
    return {
        "before_total": total_before,
        "after_total": total_after,
        "before_labels": dict(sorted(before.items())),
        "after_labels": dict(sorted(after.items())),
        "dropped_labels": dict(sorted(dropped.items())),
        "before_off_domain_share": round(safe_div(before.get("off_domain", 0), total_before), 6),
        "after_off_domain_share": round(safe_div(after.get("off_domain", 0), total_after), 6),
        "citable_retention": round(safe_div(after.get("citable", 0), before.get("citable", 0)), 6),
        "off_domain_reduction": round(safe_div(dropped.get("off_domain", 0), before.get("off_domain", 0)), 6),
    }


def filtered_row_to_dict(row: FilteredRow) -> dict[str, Any]:
    return {
        "section": row.section,
        "claim_id": row.row.get("claim_id"),
        "element_id": row.row.get("element_id"),
        "paper_id": row.paper_id,
        "label": row.label,
        "tags": row.tags,
        "context_score": row.context_score,
        "positive_score": row.positive_score,
        "combined_score": row.combined_score,
        "final_score": row.final_score,
        "dropped": row.dropped,
        "drop_reasons": row.drop_reasons,
    }
