#!/usr/bin/env python3
"""Shadow retrieval filter for arXiv -> Wiki Feed v2 candidates.

This script is deliberately artifact-only: it writes a shadow A/B report and
candidate JSONL files, but never writes to production tables.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import requests
import yaml


ATOM_MODEL = "vanta-research/atom-astronomy-7b:latest"
OLLAMA_URL = "http://localhost:11434"
SECTION_ALLOWLIST = {
    "shmr_halo_quenching",
    "env_quenching",
    "size_evolution",
    "high_z_sf",
    "feedback_outflows",
}
SIZE_EVOLUTION_NEGATIVE_LIFT_TAGS = [
    "single_object_agn",
    "instrumentation",
    "reverberation_mapping",
    "blazar",
    "stellar_wind",
]
NEGATIVE_LIFT_BASE_SUBDOMAINS = {"agn", "stellar", "instrumentation"}
STOPWORDS = {
    "the", "and", "for", "with", "from", "that", "this", "are", "was", "were", "into",
    "using", "use", "used", "between", "across", "through", "their", "than", "such",
    "when", "where", "which", "while", "about", "over", "under", "also", "show",
    "shows", "showing", "paper", "candidate", "claim", "galaxy", "galaxies",
}
NUMBER_RE = re.compile(r"(?<![a-z0-9])(?:[<>~=]*\s*)?\d+(?:\.\d+)?(?:\s*[x]\s*10\^?-?\d+)?", re.I)
EMBED_MODEL = "nomic-embed-text:v1.5"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def norm(text: Any) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def tokens(text: str) -> list[str]:
    out = []
    for token in re.findall(r"[a-zA-Z][a-zA-Z0-9_-]{2,}", text.lower()):
        if token not in STOPWORDS:
            out.append(token)
    return out


def numeric_literals(text: str) -> set[str]:
    return {re.sub(r"\s+", "", value.lower()) for value in NUMBER_RE.findall(text or "")}


def element_support_features(element_text: str, paper_text: str) -> dict[str, Any]:
    element_tokens = set(tokens(element_text))
    paper_tokens = set(tokens(paper_text))
    element_numbers = numeric_literals(element_text)
    paper_numbers = numeric_literals(paper_text)
    term_overlap = sorted(element_tokens & paper_tokens)
    number_overlap = sorted(element_numbers & paper_numbers)
    proxy = len(term_overlap) / max(1, len(element_tokens))
    return {
        "element_support_terms": term_overlap,
        "element_support_numbers": number_overlap,
        "element_support_proxy": round(proxy, 4),
        "element_support_gate": bool(term_overlap or number_overlap),
        "element_support_threshold": ">=1_content_token_or_>=1_numeric_literal",
    }


def get_embedding(text: str, model: str = EMBED_MODEL, host: str = OLLAMA_URL) -> list[float]:
    response = requests.post(
        f"{host.rstrip('/')}/api/embeddings",
        json={"model": model, "prompt": text or ""},
        timeout=30,
    )
    response.raise_for_status()
    embedding = response.json().get("embedding")
    if not isinstance(embedding, list):
        raise ValueError("embedding response missing list")
    return [float(value) for value in embedding]


def cosine_similarity(left: list[float], right: list[float]) -> float:
    dot = sum(a * b for a, b in zip(left, right))
    left_mag = math.sqrt(sum(a * a for a in left))
    right_mag = math.sqrt(sum(b * b for b in right))
    if not left_mag or not right_mag:
        return 0.0
    return dot / (left_mag * right_mag)


def semantic_support_features(
    element_text: str,
    paper_abstract: str,
    min_semantic_similarity: float = 0.50,
    ollama_host: str = OLLAMA_URL,
) -> dict[str, Any]:
    try:
        similarity = cosine_similarity(
            get_embedding(element_text, host=ollama_host),
            get_embedding(paper_abstract, host=ollama_host),
        )
    except Exception as exc:
        return {
            "coverage_candidate": False,
            "semantic_similarity": None,
            "semantic_similarity_threshold": min_semantic_similarity,
            "semantic_support_status": "embedding_failed",
            "semantic_support_error": str(exc)[:220],
        }
    return {
        "coverage_candidate": similarity >= min_semantic_similarity,
        "semantic_similarity": round(similarity, 6),
        "semantic_similarity_threshold": min_semantic_similarity,
        "semantic_support_status": "semantic_supported" if similarity >= min_semantic_similarity else "semantic_unsupported",
        "semantic_support_error": None,
    }


def load_taxonomy(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        import json
        taxonomy = json.load(fh)
    if "subdomains" not in taxonomy:
        # Wrap it if it's missing the key
        taxonomy = {"version": taxonomy.get("version", "v1"), "subdomains": taxonomy.get("tags", {}), "scoring": {"same_subdomain_bonus": 0.5, "compatible_subdomain_bonus": 0.2, "allow_hard_drop_when": {"section_rerank_percentile_max": 0.2}}, "compatibility": {}}
        # Or just format it right based on the JSON
        if isinstance(taxonomy["subdomains"], list):
            taxonomy["subdomains"] = {t["name"]: t for t in taxonomy["subdomains"]}
    return taxonomy


def semantic_threshold_from_calibration(path: Path | None, fallback: float) -> float:
    if not path:
        return fallback
    with path.open(encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)
    if not isinstance(loaded, dict):
        raise ValueError(f"Invalid page calibration config: {path}")
    semantic_band = loaded.get("semantic_band") or {}
    if not isinstance(semantic_band, dict):
        raise ValueError("semantic_band must be a mapping when present")
    value = semantic_band.get("min_semantic_similarity", fallback)
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("semantic_band.min_semantic_similarity must be numeric") from exc


def label_key(row: dict[str, Any]) -> tuple[str, str]:
    return (norm(row.get("element_id")), norm(row.get("paper_id") or row.get("arxiv_id")))


def build_candidate_rows(
    candidates_path: Path,
    labels_path: Path,
    min_semantic_similarity: float = 0.50,
    ollama_host: str = OLLAMA_URL,
) -> list[dict[str, Any]]:
    labels = {label_key(row): row for row in read_jsonl(labels_path)}
    pair_rows: dict[tuple[str, str], dict[str, Any]] = {}
    for row in read_jsonl(candidates_path):
        key = (norm(row.get("element_id")), norm(row.get("arxiv_id") or row.get("paper_id")))
        if key in labels and key not in pair_rows:
            pair_rows[key] = row

    candidates = []
    for key, label in labels.items():
        pair = pair_rows.get(key, {})
        section = label.get("target_section") or label.get("section")
        if section not in SECTION_ALLOWLIST:
            continue
        arxiv_id = key[1]
        element_text = pair.get("element_text") or pair.get("claim_text_snapshot") or ""
        paper_title = pair.get("paper_title_snapshot") or ""
        paper_abstract = pair.get("paper_abstract_snapshot") or ""
        support = element_support_features(element_text, " ".join([paper_title, paper_abstract]))
        semantic_support = semantic_support_features(element_text, paper_abstract, min_semantic_similarity, ollama_host)
        candidates.append(
            {
                "candidate_key": pair.get("candidate_key") or f"{key[0]}::{arxiv_id}",
                "claim_id": label.get("claim_id") or pair.get("claim_id"),
                "element_id": key[0],
                "arxiv_id": arxiv_id,
                "target_section": section,
                "target_section_title": label.get("target_section_title") or section,
                "label": label.get("label") or label.get("final_label") or "unclear",
                "astrosage_reason": label.get("reason") or "",
                "claim_text_snapshot": pair.get("claim_text_snapshot") or "",
                "element_text": element_text,
                "paper_title": paper_title,
                "paper_abstract": paper_abstract,
                "primary_category": pair.get("primary_category") or pair.get("paper_primary_category") or "",
                "candidate_source": pair.get("candidate_source") or "post_retry_label_projection",
                "claim_key_overlap": float(pair.get("claim_key_overlap") or 0.0),
                "matched_terms": pair.get("matched_terms") or [],
                "element_matched_terms": pair.get("element_matched_terms") or [],
                **support,
                **semantic_support,
            }
        )
    return candidates


def derive_section_profiles(candidates: list[dict[str, Any]], taxonomy: dict[str, Any]) -> dict[str, Any]:
    section_terms: dict[str, Counter[str]] = defaultdict(Counter)
    page_terms: Counter[str] = Counter()
    for row in candidates:
        if row["label"] != "citable":
            continue
        text = " ".join([row["target_section_title"], row["claim_text_snapshot"], row["element_text"], row["paper_title"]])
        section_terms[row["target_section"]].update(tokens(text))
        page_terms.update(tokens(text))

    # Page target is derived from citable text against taxonomy lexical hints.
    page_scores = {}
    page_text = " ".join(page_terms.elements())
    for subdomain, spec in taxonomy["subdomains"].items():
        score = 0.0
        for hint in spec.get("positive_lexical_hints", []):
            if hint.lower() in page_text:
                score += 0.08
        for hint in spec.get("negative_lexical_hints", []):
            if hint.lower() in page_text:
                score -= 0.06
        page_scores[subdomain] = round(max(0.0, min(1.0, score)), 4)
    if page_scores:
        best = max(page_scores, key=page_scores.get)
        page_scores[best] = max(page_scores[best], 0.90)

    sections: dict[str, Any] = {}
    for section in sorted(SECTION_ALLOWLIST):
        common = [term for term, _count in section_terms[section].most_common(28)]
        sections[section] = {
            "target_subdomain_scores": page_scores,
            "positive_terms": common,
            "negative_lift_tags": SIZE_EVOLUTION_NEGATIVE_LIFT_TAGS if section == "size_evolution" else [],
            "rerank_centroid_source": "section_claims_plus_citable_rows",
            "profile_confidence": "medium" if common else "low",
        }
    return {
        "taxonomy_version": taxonomy["version"],
        "page_subdomain_scores": page_scores,
        "target_subdomain": max(page_scores, key=page_scores.get) if page_scores else "other",
        "sections": sections,
    }


def category_score(primary_category: str, priors: dict[str, float]) -> float:
    if primary_category in priors:
        return float(priors[primary_category])
    return 0.0


def deterministic_tag(paper: dict[str, Any], taxonomy: dict[str, Any]) -> dict[str, Any]:
    text = " ".join([paper.get("title", ""), paper.get("abstract", "")]).lower()
    primary_category = paper.get("primary_category") or ""
    scores: dict[str, float] = {}
    matched_rules: list[str] = []
    for subdomain, spec in taxonomy["subdomains"].items():
        score = category_score(primary_category, spec.get("arxiv_category_priors", {}))
        if score:
            matched_rules.append(f"{subdomain}:{primary_category}_prior")
        for hint in spec.get("positive_lexical_hints", []):
            if hint.lower() in text:
                score += 0.18
                matched_rules.append(f"{subdomain}:positive:{hint}")
        for hint in spec.get("negative_lexical_hints", []):
            if hint.lower() in text:
                score -= 0.12
                matched_rules.append(f"{subdomain}:negative:{hint}")
        scores[subdomain] = round(max(0.0, min(1.0, score)), 4)
    primary = max(scores, key=scores.get) if scores else "other"
    ordered = sorted(scores.values(), reverse=True)
    confidence = ordered[0] if ordered else 0.0
    margin = ordered[0] - ordered[1] if len(ordered) > 1 else ordered[0] if ordered else 0.0
    return {
        "arxiv_id": paper["arxiv_id"],
        "taxonomy_version": taxonomy["version"],
        "primary_subdomain": primary,
        "subdomain_scores": scores,
        "confidence": round(confidence, 4),
        "score_margin": round(margin, 4),
        "tag_source": "category_lexical_v1",
        "matched_rules": matched_rules[:20],
    }


def extract_json(text: str) -> dict[str, Any]:
    value = norm(text)
    if value.startswith("```"):
        value = re.sub(r"^```(?:json)?\s*", "", value)
        value = re.sub(r"\s*```$", "", value)
    try:
        parsed = json.loads(value)
        return parsed if isinstance(parsed, dict) else {}
    except Exception:
        match = re.search(r"\{.*\}", value, re.S)
        return json.loads(match.group(0)) if match else {}


def atom_tag(paper: dict[str, Any], taxonomy: dict[str, Any], timeout: int = 120) -> tuple[dict[str, Any] | None, bool]:
    prompt = f"""Classify this astronomy paper into one primary subdomain.
Allowed subdomains: {', '.join(taxonomy['subdomains'].keys())}, other.
Return ONLY JSON:
{{"primary_subdomain":"...","secondary_subdomains":[],"confidence":0.0,"reason":"short"}}

Title: {paper.get('title', '')}
Abstract: {paper.get('abstract', '')[:2200]}
"""
    payload = {
        "model": ATOM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "format": "json",
        "options": {"temperature": 0, "num_ctx": 4096, "num_predict": 320},
    }
    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = json.loads(resp.read().decode("utf-8", errors="replace"))
        content = ((raw.get("message") or {}).get("content") or "").strip()
        parsed = extract_json(content)
        primary = parsed.get("primary_subdomain")
        if primary not in taxonomy["subdomains"]:
            return None, True
        scores = {name: 0.0 for name in taxonomy["subdomains"].keys()}
        scores[primary] = float(parsed.get("confidence") or 0.0)
        for secondary in parsed.get("secondary_subdomains") or []:
            if secondary in scores:
                scores[secondary] = max(scores[secondary], 0.35)
        return {
            "arxiv_id": paper["arxiv_id"],
            "taxonomy_version": taxonomy["version"],
            "primary_subdomain": primary,
            "subdomain_scores": scores,
            "confidence": round(float(parsed.get("confidence") or 0.0), 4),
            "score_margin": 0.0,
            "tag_source": "atom_ambiguity_v1",
            "matched_rules": [f"atom_reason:{norm(parsed.get('reason'))[:180]}"],
        }, False
    except Exception:
        return None, True


def derive_tags(candidates: list[dict[str, Any]], taxonomy: dict[str, Any], max_atom_calls: int) -> tuple[dict[str, dict[str, Any]], int, int]:
    papers: dict[str, dict[str, Any]] = {}
    for row in candidates:
        papers.setdefault(
            row["arxiv_id"],
            {
                "arxiv_id": row["arxiv_id"],
                "title": row["paper_title"],
                "abstract": row["paper_abstract"],
                "primary_category": row["primary_category"],
            },
        )
    tags = {}
    atom_calls = 0
    atom_failures = 0
    for arxiv_id, paper in papers.items():
        tag = deterministic_tag(paper, taxonomy)
        use_atom = (tag["confidence"] < 0.70 or tag["score_margin"] < 0.18) and atom_calls < max_atom_calls
        if use_atom:
            atom_calls += 1
            atom_result, failed = atom_tag(paper, taxonomy)
            if failed:
                atom_failures += 1
            if atom_result:
                tag = atom_result
            elif failed:
                tag["tag_source"] = "failed_model_fallback"
                tag["matched_rules"].append("atom_failed_keep_candidate")
        tags[arxiv_id] = tag
    return tags, atom_calls, atom_failures


def section_score(row: dict[str, Any], profile: dict[str, Any]) -> float:
    terms = set(profile["sections"][row["target_section"]].get("positive_terms") or [])
    if not terms:
        return 0.5
    doc_tokens = set(tokens(" ".join([row["paper_title"], row["paper_abstract"]])))
    claim_tokens = set(tokens(" ".join([row["claim_text_snapshot"], row["element_text"], row["target_section_title"]])))
    query_terms = terms | {t for t in claim_tokens if len(t) > 4}
    if not query_terms:
        return 0.5
    overlap = len(query_terms & doc_tokens) / max(1, len(query_terms))
    return round(min(1.0, overlap * 3.0), 4)


def negative_lift_tags(row: dict[str, Any], tag: dict[str, Any]) -> list[str]:
    text = " ".join([row.get("paper_title", ""), row.get("paper_abstract", "")]).lower()
    matched = " ".join(tag.get("matched_rules") or []).lower()
    combined = f"{text} {matched}"
    tags: set[str] = set()
    if tag.get("primary_subdomain") == "instrumentation":
        tags.add("instrumentation")
    if "blazar" in combined:
        tags.add("blazar")
    if "reverberation" in combined or "broad-line region" in combined or "broad line region" in combined:
        tags.add("reverberation_mapping")
    if "stellar wind" in combined or "stellar winds" in combined:
        tags.add("stellar_wind")
    if tag.get("primary_subdomain") == "agn" and any(
        marker in combined
        for marker in [
            "single object",
            "individual object",
            "ngc ",
            "m87",
            "mrk ",
            "3c ",
            "ton ",
            "bl lac",
        ]
    ):
        tags.add("single_object_agn")
    return sorted(tags)


def subdomain_adjustment(page_target: str, tag: dict[str, Any], taxonomy: dict[str, Any]) -> tuple[float, str]:
    scoring = taxonomy["scoring"]
    primary = tag["primary_subdomain"]
    if primary == page_target:
        return float(scoring["same_subdomain_bonus"]), "same"
    comp = taxonomy.get("compatibility", {}).get(page_target, {})
    if primary in comp.get("compatible", []):
        return float(scoring["compatible_subdomain_bonus"]), "compatible"
    if primary in comp.get("severe_mismatch", []):
        return float(scoring["severe_mismatch_penalty"]), "severe_mismatch"
    return float(scoring["mismatch_penalty"]), "mismatch"


def percentile(values: list[float], p: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, math.floor((len(ordered) - 1) * p)))
    return ordered[idx]


def score_candidates(candidates: list[dict[str, Any]], tags: dict[str, dict[str, Any]], profile: dict[str, Any], taxonomy: dict[str, Any]) -> list[dict[str, Any]]:
    scored = []
    page_target = profile["target_subdomain"]
    for row in candidates:
        tag = tags[row["arxiv_id"]]
        sec_score = section_score(row, profile)
        lift_tags = negative_lift_tags(row, tag)
        section_profile = profile["sections"].get(row["target_section"], {})
        section_negative_tags = set(section_profile.get("negative_lift_tags") or [])
        negative_lift_applied = (
            bool(section_negative_tags.intersection(lift_tags))
            and tag["primary_subdomain"] in NEGATIVE_LIFT_BASE_SUBDOMAINS
        )
        if negative_lift_applied:
            sec_score = round(max(0.0, sec_score - 0.10), 4)
        base_score = float(row.get("claim_key_overlap") or 0.0)
        adj, relation = subdomain_adjustment(page_target, tag, taxonomy)
        final = base_score + adj + float(taxonomy["scoring"].get("section_score_weight", 0.20)) * sec_score
        scored.append(
            {
                **row,
                "paper_subdomain": tag["primary_subdomain"],
                "subdomain_confidence": tag["confidence"],
                "tag_source": tag["tag_source"],
                "subdomain_relation": relation,
                "negative_lift_tags": lift_tags,
                "negative_lift_applied": negative_lift_applied,
                "base_score": round(base_score, 4),
                "subdomain_adjustment": round(adj, 4),
                "section_rerank_score": sec_score,
                "final_retrieval_score": round(final, 4),
            }
        )
    hard = taxonomy["scoring"]["allow_hard_drop_when"]
    section_percentile = float(hard.get("section_rerank_percentile_max", 0.20))
    section_cutoff = {
        section: percentile([r["section_rerank_score"] for r in scored if r["target_section"] == section], section_percentile)
        for section in SECTION_ALLOWLIST
    }
    for row in scored:
        weak_section = row["section_rerank_score"] <= max(section_cutoff[row["target_section"]], 0.18)
        if not row.get("coverage_candidate"):
            decision = "semantic_unsupported"
        elif row["tag_source"] == "failed_model_fallback":
            decision = "ambiguous_keep"
        elif (
            row["subdomain_relation"] == "severe_mismatch"
            and row["subdomain_confidence"] >= float(hard["subdomain_confidence_min"])
            and weak_section
        ):
            decision = "drop"
        elif row["subdomain_relation"] == "severe_mismatch" and row["subdomain_confidence"] >= 0.70:
            decision = "holdout_drop"
        elif row["subdomain_relation"] == "mismatch":
            decision = "downrank"
        else:
            decision = "keep"
        row["filter_decision"] = decision
    return scored


def evaluate(scored: list[dict[str, Any]]) -> dict[str, Any]:
    kept = [r for r in scored if r["filter_decision"] not in {"drop", "holdout_drop"}]
    dropped = [r for r in scored if r["filter_decision"] in {"drop", "holdout_drop"}]
    before = Counter(r["label"] for r in scored)
    after = Counter(r["label"] for r in kept)
    citable_recall = after["citable"] / before["citable"] if before["citable"] else 1.0
    by_section = {}
    for section in sorted(SECTION_ALLOWLIST):
        rows = [r for r in scored if r["target_section"] == section]
        kept_rows = [r for r in kept if r["target_section"] == section]
        before_c = sum(1 for r in rows if r["label"] == "citable")
        after_c = sum(1 for r in kept_rows if r["label"] == "citable")
        by_section[section] = {
            "before": len(rows),
            "after": len(kept_rows),
            "citable_before": before_c,
            "citable_after": after_c,
            "citable_recall": round(after_c / before_c, 4) if before_c else 1.0,
            "off_domain_after": sum(1 for r in kept_rows if r["label"] == "off_domain"),
            "off_domain_share_after": round(sum(1 for r in kept_rows if r["label"] == "off_domain") / len(kept_rows), 4) if kept_rows else 0.0,
        }
    off_after = after["off_domain"] / len(kept) if kept else 0.0
    load_reduction = len(dropped) / len(scored) if scored else 0.0
    wrong_off = [r for r in kept if r["label"] == "off_domain" and r["subdomain_relation"] == "severe_mismatch"]
    off_kept = [r for r in kept if r["label"] == "off_domain"]
    wrong_share_after = len(wrong_off) / len(off_kept) if off_kept else 0.0
    baseline_wrong_share = 0.533
    relative_drop = (baseline_wrong_share - wrong_share_after) / baseline_wrong_share if baseline_wrong_share else 0.0
    return {
        "rows_before": len(scored),
        "rows_after": len(kept),
        "rows_dropped": len(dropped),
        "load_reduction": round(load_reduction, 4),
        "label_counts_before": dict(before),
        "label_counts_after": dict(after),
        "citable_recall": round(citable_recall, 4),
        "off_domain_share_after": round(off_after, 4),
        "wrong_subdomain_share_after": round(wrong_share_after, 4),
        "wrong_subdomain_share_relative_drop": round(relative_drop, 4),
        "by_section": by_section,
    }


def gates(metrics: dict[str, Any], atom_calls: int, atom_failures: int) -> tuple[bool, list[str]]:
    failures = []
    if metrics["citable_recall"] < 0.90:
        failures.append("citable_recall_below_90")
    if metrics["wrong_subdomain_share_relative_drop"] < 0.25:
        failures.append("wrong_subdomain_relative_drop_below_25")
    if metrics["off_domain_share_after"] > 0.16:
        failures.append("overall_off_domain_above_16")
    for section, data in metrics["by_section"].items():
        if data["off_domain_share_after"] > 0.25:
            failures.append(f"{section}_off_domain_above_25")
        if data["citable_recall"] < 0.85:
            failures.append(f"{section}_citable_loss_above_15")
    failure_rate = atom_failures / atom_calls if atom_calls else 0.0
    if failure_rate >= 0.05:
        failures.append("atom_json_failure_rate_above_5")
    if not (0.15 <= metrics["load_reduction"] <= 0.30):
        failures.append("validator_load_reduction_outside_15_30")
    return not failures, failures


def render_report(run_key: str, metrics: dict[str, Any], failures: list[str], scored: list[dict[str, Any]], report_path: Path) -> None:
    dropped = [r for r in scored if r["filter_decision"] in {"drop", "holdout_drop"}]
    wrong_sample = [r for r in dropped if r["label"] == "off_domain"][:12]
    dropped_citable = [r for r in dropped if r["label"] == "citable"][:12]
    lines = [
        "# arXiv Wiki Feed v2 Retrieval Filter Shadow A/B",
        "",
        f"- Run key: `{run_key}`",
        "- Mode: shadow only; no DB writes; no production route changes",
        f"- Retrospective status: {'passes gates' if not failures else 'gates failed'}",
        "",
        "## Before/After",
        "",
        "| Metric | A lane before | B lane projected |",
        "|---|---:|---:|",
        f"| Validator rows | {metrics['rows_before']} | {metrics['rows_after']} |",
        f"| Validator load reduction | 0.0% | {metrics['load_reduction']*100:.1f}% |",
        f"| Citable rows | {metrics['label_counts_before'].get('citable', 0)} | {metrics['label_counts_after'].get('citable', 0)} |",
        f"| Citable recall | 100.0% | {metrics['citable_recall']*100:.1f}% |",
        f"| Off-domain rows | {metrics['label_counts_before'].get('off_domain', 0)} | {metrics['label_counts_after'].get('off_domain', 0)} |",
        f"| Off-domain share | 21.4% | {metrics['off_domain_share_after']*100:.1f}% |",
        f"| Wrong-subdomain relative drop | baseline 53.3% | {metrics['wrong_subdomain_share_relative_drop']*100:.1f}% |",
        "",
        "## Section Gates",
        "",
        "| Section | Rows before | Rows after | Citable recall | Off-domain after |",
        "|---|---:|---:|---:|---:|",
    ]
    for section, data in metrics["by_section"].items():
        lines.append(
            f"| `{section}` | {data['before']} | {data['after']} | {data['citable_recall']*100:.1f}% | {data['off_domain_share_after']*100:.1f}% |"
        )
    lines += ["", "## Gate Failures", ""]
    if failures:
        lines.extend(f"- `{f}`" for f in failures)
    else:
        lines.append("- none")
    lines += ["", "## Wrong-Subdomain Dropped Sample", ""]
    for row in wrong_sample:
        lines.append(
            f"- `{row['target_section']}` `{row['element_id']}` `{row['arxiv_id']}` "
            f"{row['paper_subdomain']} conf={row['subdomain_confidence']}: {row['paper_title'][:160]}"
        )
    lines += ["", "## Failure Examples: Dropped Citable Rows", ""]
    if dropped_citable:
        for row in dropped_citable:
            lines.append(
                f"- `{row['target_section']}` `{row['element_id']}` `{row['arxiv_id']}` "
                f"decision={row['filter_decision']} subdomain={row['paper_subdomain']} title={row['paper_title'][:160]}"
            )
    else:
        lines.append("- none in retrospective projection")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True)
    parser.add_argument("--labels", required=True)
    parser.add_argument("--taxonomy", required=True)
    parser.add_argument("--run-key", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-atom-calls", type=int, default=50)
    parser.add_argument("--report-path", required=True)
    parser.add_argument("--calibration", type=Path, help="Per-page retrieval calibration YAML.")
    parser.add_argument("--min-semantic-similarity", type=float, default=None, help="Diagnostic override for semantic_band.min_semantic_similarity.")
    parser.add_argument("--ollama-host", default=OLLAMA_URL)
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    taxonomy = load_taxonomy(Path(args.taxonomy))
    min_semantic_similarity = args.min_semantic_similarity
    if min_semantic_similarity is None:
        min_semantic_similarity = semantic_threshold_from_calibration(args.calibration, 0.50)
    candidates = build_candidate_rows(Path(args.candidates), Path(args.labels), min_semantic_similarity, args.ollama_host)
    profile = derive_section_profiles(candidates, taxonomy)
    tags, atom_calls, atom_failures = derive_tags(candidates, taxonomy, args.max_atom_calls)
    scored = score_candidates(candidates, tags, profile, taxonomy)
    kept = [r for r in scored if r["filter_decision"] not in {"drop", "holdout_drop"}]
    metrics = evaluate(scored)
    passed, failures = gates(metrics, atom_calls, atom_failures)
    status = "complete" if passed else "gates_failed"

    write_jsonl(out_dir / "unfiltered_candidates.jsonl", candidates)
    write_jsonl(out_dir / "filtered_candidates.jsonl", kept)
    write_jsonl(out_dir / "retrieval_filter_scores.jsonl", scored)
    write_jsonl(out_dir / "paper_subdomain_tags.jsonl", list(tags.values()))
    write_json(out_dir / "page_retrieval_profile.json", profile)
    render_report(args.run_key, metrics, failures, scored, out_dir / "RETRIEVAL_FILTER_REPORT.md")
    render_report(args.run_key, metrics, failures, scored, Path(args.report_path))

    summary = {
        "run_key": args.run_key,
        "artifact_dir": str(out_dir),
        "status": status,
        "no_db_writes": True,
        "taxonomy_version": taxonomy["version"],
        "semantic_band": {
            "min_semantic_similarity": min_semantic_similarity,
            "source": "cli_override" if args.min_semantic_similarity is not None else ("calibration" if args.calibration else "default"),
            "calibration_path": str(args.calibration) if args.calibration else None,
        },
        "papers_tagged": len(tags),
        "atom_fallback_calls": atom_calls,
        "atom_json_failures": atom_failures,
        "retrospective_gates": {
            "citable_recall": metrics["citable_recall"],
            "wrong_subdomain_share_relative_drop": metrics["wrong_subdomain_share_relative_drop"],
            "off_domain_share": metrics["off_domain_share_after"],
            "by_section_off_domain": {
                section: data["off_domain_share_after"] for section, data in metrics["by_section"].items()
            },
            "failures": failures,
        },
        "validator_rerun": {
            "attempted": False,
            "new_citable": 0,
            "new_off_domain": 0,
            "validator_rows_before": metrics["rows_before"],
            "validator_rows_after": metrics["rows_after"],
        },
        "metrics": metrics,
        "report_path": args.report_path,
    }
    write_json(out_dir / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
