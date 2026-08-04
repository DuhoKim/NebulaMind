#!/usr/bin/env python3
"""Deterministic C41 Step-1 corpus filter (stdlib only, no network, no DB).

Rules are frozen in STEP1_CORPUS_PROTOCOL.md. The 420 MB base JSONL is streamed.
Outputs are written atomically beside this script.
"""

from __future__ import annotations

import collections
import hashlib
import json
import math
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Iterable

PROTOCOL_VERSION = "C41_STEP1_V1"
CLUSTER = 41
CEILING = 180
REVIEW_CAP = 24
CALIBRATION_ANCHOR_CAP = 8
CORPUS_MIN_YEAR = 2009
CORPUS_MAX_YEAR = 2026
FROZEN_QUESTION_SHA256 = "9ac5ca1f6321e2808eec3b9c2d38b8e616e0a9d774f4f277469c38fadbf789e1"

LANE_DIR = Path(__file__).resolve().parent
REPO_ROOT = Path(__file__).resolve().parents[3]
ENGINE_DIR = (
    REPO_ROOT
    / ".hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718"
)

PATHS = {
    "frozen_question": LANE_DIR / "STEP0_FROZEN_QUESTION.md",
    "protocol": LANE_DIR / "STEP1_CORPUS_PROTOCOL.md",
    "filter": Path(__file__).resolve(),
    "plan": REPO_ROOT / ".hermes/plans/2026-08-04_0040-c41-jwst-highz-baseline-restart.md",
    "base_labels": ENGINE_DIR / "cluster_labels_v2.json",
    "base_corpus": ENGINE_DIR / "corpus_ga_co_2009_2026.jsonl",
    "delta_labels": ENGINE_DIR / "delta/new_labels.json",
    "delta_corpus": ENGINE_DIR / "delta/new_papers.jsonl",
    "dispersion": ENGINE_DIR / "dispersion_v2.json",
    "strict_lexicon_source": ENGINE_DIR / "rank_frontiers_v3.py",
    "dispersion_lexicon_source": REPO_ROOT / "tools/nm_dispersion_v2.py",
}

OUTPUT_INCLUDED = LANE_DIR / "SELECTION_INCLUDED.json"
OUTPUT_EXCLUDED = LANE_DIR / "SELECTION_EXCLUDED.json"
OUTPUT_SHAS = LANE_DIR / "SELECTION_SHAS.txt"

RULE_TEXT = collections.OrderedDict(
    [
        (
            "DUPLICATE_IDENTITY",
            "Later occurrence of a normalized identity already seen in fixed base-then-delta source order.",
        ),
        (
            "MALFORMED_REQUIRED_METADATA",
            "Normalized identity, title, or abstract required by the protocol is missing.",
        ),
        (
            "UNSUPPORTED_SOURCE_CLASS",
            "Record is neither a REFEREED base article nor an identified delta arXiv preprint.",
        ),
        (
            "LRD_AGN_OUTSIDE_THREE_AXES",
            "LRD/high-z AGN record lacks a strong formation-efficiency, chemical-enrichment, or ionizing-output hit.",
        ),
        (
            "INSTRUMENT_OUTSIDE_SELECTION_LIMITS",
            "Instrument design/performance/commissioning record lacks a completeness or selection-limit exception tied to an axis.",
        ),
        (
            "NAMED_TOPIC_OUTSIDE_THREE_AXES",
            "Cosmic-noon quenching, environment, or mergers-as-topic record lacks a strong three-axis hit.",
        ),
        (
            "NO_THREE_AXIS_SIGNAL",
            "Metadata has no hit on formation efficiency, chemical enrichment, or ionizing output.",
        ),
        (
            "NO_HIGH_Z_SIGNAL",
            "Axis-bearing record has no z>=6/early-epoch marker and is not an explicit chemical-calibration anchor.",
        ),
        (
            "REVIEW_CLASS_CAP",
            f"Review candidate exceeds the deterministic cap of {REVIEW_CAP} among the {CEILING} included records.",
        ),
        (
            "CALIBRATION_ANCHOR_CAP",
            f"Non-high-z chemical-calibration anchor exceeds the deterministic cap of {CALIBRATION_ANCHOR_CAP}.",
        ),
        (
            "CAPACITY_BELOW_TOP_180",
            f"Otherwise eligible record falls below the deterministic {CEILING}-record ceiling.",
        ),
    ]
)


def _compile(patterns: Iterable[str]) -> list[re.Pattern[str]]:
    return [re.compile(pattern, re.IGNORECASE) for pattern in patterns]


AXIS_PATTERNS = {
    "formation_efficiency": _compile(
        [
            r"\bstar[-\s]?formation\b",
            r"\bstar[-\s]?forming\b",
            r"\bSFR\b",
            r"\bsSFR\b",
            r"formation efficien",
            r"feedback[-\s]?free",
            r"\bfeedback\b",
            r"\bbursty\b",
            r"\bburst(?:s|iness)?\b",
            r"non[-\s]?thermal",
            r"initial mass function",
            r"\bIMF\b",
            r"UV luminosity function",
            r"\bUVLF\b",
            r"bright[-\s]?end",
            r"stellar mass function",
        ]
    ),
    "chemical_enrichment": _compile(
        [
            r"\bmetallicit",
            r"chemical enrich",
            r"chemical evolution",
            r"metal enrich",
            r"oxygen abundance",
            r"12\s*\+\s*log",
            r"\bO\s*/\s*H\b",
            r"\bC\s*/\s*O\b",
            r"\bN\s*/\s*O\b",
            r"\[Fe/H\]",
            r"\[alpha/Fe\]",
            r"abundance pattern",
        ]
    ),
    "ionizing_output": _compile(
        [
            r"ioni[sz]",
            r"\bxi[_\s-]*ion\b",
            r"ξ[_\s-]*ion",
            r"escape fraction",
            r"\bf[_\s-]*esc\b",
            r"\bLyC\b",
            r"Lyman continuum",
            r"reioni[sz]",
            r"ionizing (?:photon|budget|emissiv|production|output)",
        ]
    ),
}

STRONG_FORMATION_PATTERNS = _compile(
    [
        r"formation efficien",
        r"feedback[-\s]?free",
        r"\bfeedback\b",
        r"\bbursty\b",
        r"\bburst(?:s|iness)?\b",
        r"non[-\s]?thermal",
        r"initial mass function",
        r"\bIMF\b",
        r"UV luminosity function",
        r"\bUVLF\b",
        r"bright[-\s]?end",
    ]
)

HIGH_Z_PATTERNS = _compile(
    [
        r"\bz\s*(?:[=~≈><]|>=|<=|≤|≥|\\gtrsim|\\geq?)?\s*(?:6(?:\.\d+)?|[7-9](?:\.\d+)?|1[0-9](?:\.\d+)?)\b",
        r"\bredshift(?:s| range)?\s*(?:[=~≈><]|of|>=|<=|≤|≥|from|at)?\s*(?:6(?:\.\d+)?|[7-9](?:\.\d+)?|1[0-9](?:\.\d+)?)\b",
        r"high[-\s]?redshift",
        r"\bhigh[-\s]?z\b",
        r"cosmic dawn",
        r"epoch of reioni[sz]ation",
        r"\bEoR\b",
        r"first galaxies",
        r"earliest galaxies",
        r"reioni[sz]ation",
    ]
)

CALIBRATION_PATTERNS = _compile(
    [
        r"calibrat",
        r"direct[-\s]?T[_e]?",
        r"electron temperature",
        r"auroral",
        r"strong[-\s]?line",
        r"photoioni[sz]ation model",
    ]
)

REVIEW_PATTERNS = _compile(
    [
        r"\bthis review\b",
        r"\bwe review\b",
        r"\breview article\b",
        r"\ba review of\b",
        r"\bwe provide an overview\b",
    ]
)
REVIEW_VENUE_TERMS = (
    "annual review",
    "astronomy and astrophysics review",
    "physics reports",
    "nature reviews physics",
)

LRD_AGN_PATTERNS = _compile(
    [
        r"little red dot",
        r"\bLRDs?\b",
        r"active galactic nuclei?",
        r"\bAGN\b",
        r"black[-\s]?hole accretion",
    ]
)

INSTRUMENT_CORE_PATTERNS = _compile(
    [
        r"instrument design",
        r"instrument performance",
        r"commissioning",
        r"detector performance",
        r"spectrograph design",
        r"telescope performance",
    ]
)

SELECTION_LIMIT_PATTERNS = _compile(
    [
        r"completeness",
        r"selection function",
        r"selection bias",
        r"detection limit",
        r"flux limit",
        r"sensitivity",
        r"contamination",
        r"photometric[-\s]?redshift",
    ]
)

NAMED_OUT_TOPIC_PATTERNS = _compile(
    [
        r"cosmic noon",
        r"\bquench",
        r"environmental dependence",
        r"galaxy environment",
        r"galaxy merger",
        r"mergers? as",
    ]
)

# Exact strict terms and physics-tension exception from the verified rank_frontiers_v3.py.
STRICT_TERMS = (
    "tension",
    "discrepan",
    "contradict",
    "inconsisten",
    "cannot explain",
    "fail to reproduce",
    "overpredict",
    "underpredict",
)
STRICT_RE = {
    term: re.compile(r"(?<![a-z])" + re.escape(term), re.IGNORECASE)
    for term in STRICT_TERMS
}
PHYS_TENSION_RE = re.compile(
    r"(?<![a-z])(?:strings?|branes?|surface|domain[-\s]?walls?)\s+tension",
    re.IGNORECASE,
)

# Relevant subset copied as a frozen v2.2 lexicon snapshot from tools/nm_dispersion_v2.py.
DISPERSION_PATTERNS = {
    "metallicity": _compile(
        [r"12\s*\+\s*log", r"log\s*\(?\s*O\s*/\s*H", r"oxygen abundance", r"metallicit"]
    ),
    "ms_slope": _compile(
        [r"main[-\s]?sequence", r"star[-\s]?forming sequence", r"\bSFR\b.{0,25}\bM", r"sSFR"]
    ),
    "fesc": _compile([r"escape fraction", r"f_?\s*esc", r"\bLyC\b", r"Lyman continuum"]),
    "sfrd": _compile([r"star formation rate density", r"\bSFRD\b", r"cosmic star formation"]),
    "uvlf_alpha": _compile([r"luminosity function", r"faint[-\s]?end slope", r"\balpha\b"]),
    "stellar_feh": _compile([r"\[Fe/H\]", r"metallicit", r"iron abundance"]),
    "alpha_fe": _compile(
        [r"\[alpha/Fe\]", r"\[α/Fe\]", r"\[[A-Za-z]{1,2}/Fe\]", r"alpha[-\s]?enhanc", r"abundance ratio"]
    ),
    "imf_slope": _compile(
        [r"initial mass function", r"\bIMF\b", r"IMF slope", r"high-mass slope", r"mass function slope"]
    ),
    "metal_gradient": _compile(
        [r"metallicity gradient", r"abundance gradient", r"dex/kpc", r"radial gradient", r"radial metallicity"]
    ),
}

QUANTITY_AXIS = {
    "metallicity": "chemical_enrichment",
    "stellar_feh": "chemical_enrichment",
    "alpha_fe": "chemical_enrichment",
    "metal_gradient": "chemical_enrichment",
    "ms_slope": "formation_efficiency",
    "sfrd": "formation_efficiency",
    "uvlf_alpha": "formation_efficiency",
    "imf_slope": "formation_efficiency",
    "fesc": "ionizing_output",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_write(path: Path, content: str) -> None:
    tmp = path.with_name(f"_tmp_{path.name}.{os.getpid()}")
    try:
        with tmp.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            tmp.unlink()


def atomic_json(path: Path, payload: Any) -> None:
    atomic_write(
        path,
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def normalized_text(record: dict[str, Any]) -> tuple[str, str, str]:
    raw_title = record.get("title")
    if isinstance(raw_title, list):
        title = " ".join(str(item) for item in raw_title if item is not None).strip()
    else:
        title = str(raw_title or "").strip()
    abstract = str(record.get("abstract") or "").strip()
    return title, abstract, f"{title} {abstract}".strip()


def normalized_identity(record: dict[str, Any], origin: str) -> tuple[str | None, str | None, str | None]:
    if origin == "base":
        bibcode = str(record.get("bibcode") or "").strip()
        return (f"bibcode:{bibcode}" if bibcode else None, bibcode or None, None)
    arxiv_id = str(record.get("arxiv_id") or "").strip()
    arxiv_id = re.sub(r"^arXiv:", "", arxiv_id, flags=re.IGNORECASE)
    arxiv_id = re.sub(r"v\d+$", "", arxiv_id)
    return (f"arxiv:{arxiv_id}" if arxiv_id else None, None, arxiv_id or None)


def matches_any(patterns: Iterable[re.Pattern[str]], text: str) -> bool:
    return any(pattern.search(text) for pattern in patterns)


def strict_hits(text: str) -> list[str]:
    cleaned = PHYS_TENSION_RE.sub(" ", text)
    hits = []
    for term in STRICT_TERMS:
        haystack = cleaned if term == "tension" else text
        if STRICT_RE[term].search(haystack):
            hits.append(term)
    return hits


def axis_hits(text: str) -> list[str]:
    return [axis for axis, patterns in AXIS_PATTERNS.items() if matches_any(patterns, text)]


def strong_axis_hits(text: str) -> list[str]:
    hits = []
    if matches_any(STRONG_FORMATION_PATTERNS, text):
        hits.append("formation_efficiency")
    for axis in ("chemical_enrichment", "ionizing_output"):
        if matches_any(AXIS_PATTERNS[axis], text):
            hits.append(axis)
    return hits


def dispersion_lexicon_hits(text: str, eligible_quantities: set[str]) -> list[str]:
    return sorted(
        quantity
        for quantity, patterns in DISPERSION_PATTERNS.items()
        if quantity in eligible_quantities and matches_any(patterns, text)
    )


def source_class(record: dict[str, Any], origin: str, is_review: bool) -> str | None:
    if is_review:
        if origin == "base" and "REFEREED" in (record.get("property") or []):
            return "review"
        if origin == "delta" and record.get("arxiv_id"):
            return "review"
    if origin == "base":
        properties = record.get("property") or []
        if "REFEREED" in properties and "ARTICLE" in properties:
            return "peer_reviewed_primary"
        return None
    if origin == "delta" and record.get("arxiv_id"):
        return "arxiv_preprint"
    return None


def parse_year(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def parse_citations(value: Any) -> int:
    try:
        return max(0, int(value))
    except (TypeError, ValueError):
        return 0


def rank_score(year: int, citations: int, is_review: bool) -> float:
    recency = min(1.0, max(0.0, (year - CORPUS_MIN_YEAR) / (CORPUS_MAX_YEAR - CORPUS_MIN_YEAR)))
    citation = min(1.0, max(0.0, math.log1p(citations) / math.log1p(1000)))
    return 0.75 * recency + 0.23 * citation + 0.02 * int(is_review)


def direct_measurement_priority(
    bibcode: str | None,
    direct_measurements: dict[str, list[tuple[str, int]]],
) -> tuple[int, list[str]]:
    if not bibcode:
        return 0, []
    rows = direct_measurements.get(bibcode, [])
    if not rows:
        return 0, []
    priority = max(tier for _, tier in rows)
    quantities = sorted({quantity for quantity, tier in rows if tier == priority})
    return priority, quantities


def classify_candidate(
    record: dict[str, Any],
    origin: str,
    direct_measurements: dict[str, list[tuple[str, int]]],
    eligible_quantities: set[str],
) -> dict[str, Any]:
    """Classify one record from metadata classes only; usable by Kun for synthetic decoy tests."""

    identity, bibcode, arxiv_id = normalized_identity(record, origin)
    title, abstract, text = normalized_text(record)
    axes = axis_hits(text)
    strong_axes = strong_axis_hits(text)
    high_z = matches_any(HIGH_Z_PATTERNS, text)
    calibration = matches_any(CALIBRATION_PATTERNS, text)
    calibration_anchor = (not high_z) and calibration and "chemical_enrichment" in axes
    review = matches_any(REVIEW_PATTERNS, text) or any(
        venue in str(record.get("pub") or "").lower() for venue in REVIEW_VENUE_TERMS
    )
    boundary = matches_any(LRD_AGN_PATTERNS, text)
    instrument_core = matches_any(INSTRUMENT_CORE_PATTERNS, text)
    selection_limit = matches_any(SELECTION_LIMIT_PATTERNS, text)
    named_out_topic = matches_any(NAMED_OUT_TOPIC_PATTERNS, text)
    strict = strict_hits(text)
    dispersion_hits = dispersion_lexicon_hits(text, eligible_quantities)
    direct_tier, direct_quantities = direct_measurement_priority(bibcode, direct_measurements)
    if direct_tier:
        priority = direct_tier
        priority_basis = "direct_dispersion_measurement"
    elif strict:
        priority = 2
        priority_basis = "strict_tension_lexicon"
    elif dispersion_hits:
        priority = 1
        priority_basis = "dispersion_quantity_lexicon"
    else:
        priority = 0
        priority_basis = "none"

    src_class = source_class(record, origin, review)
    year = parse_year(record.get("year"))
    citations = parse_citations(record.get("citation_count"))

    exclusion = None
    if not identity or not title or not abstract:
        exclusion = "MALFORMED_REQUIRED_METADATA"
    elif src_class is None:
        exclusion = "UNSUPPORTED_SOURCE_CLASS"
    elif boundary and not strong_axes:
        exclusion = "LRD_AGN_OUTSIDE_THREE_AXES"
    elif instrument_core and not (selection_limit and axes):
        exclusion = "INSTRUMENT_OUTSIDE_SELECTION_LIMITS"
    elif named_out_topic and not strong_axes:
        exclusion = "NAMED_TOPIC_OUTSIDE_THREE_AXES"
    elif not axes:
        exclusion = "NO_THREE_AXIS_SIGNAL"
    elif not high_z and not calibration_anchor:
        exclusion = "NO_HIGH_Z_SIGNAL"

    return {
        "key": identity,
        "bibcode": bibcode,
        "arxiv_id": arxiv_id,
        "origin": origin,
        "title": title,
        "year": year,
        "citation_count": record.get("citation_count") if origin == "base" else None,
        "publication": str(record.get("pub") or "") or None,
        "doi": sorted(str(item) for item in (record.get("doi") or []) if item),
        "identifiers": sorted(str(item) for item in (record.get("identifier") or []) if item),
        "source_class": src_class,
        "scope_class": "calibration_anchor" if calibration_anchor else "high_z_axis" if high_z else None,
        "axis_hits": axes,
        "strong_axis_hits": strong_axes,
        "high_z_signal": high_z,
        "calibration_anchor": calibration_anchor,
        "review": review,
        "lrd_agn_boundary": boundary,
        "instrument_core": instrument_core,
        "selection_limit_signal": selection_limit,
        "named_out_topic_signal": named_out_topic,
        "strict_tension_hits": strict,
        "dispersion_lexicon_hits": dispersion_hits,
        "direct_dispersion_quantities": direct_quantities,
        "contested_priority": priority,
        "contested_priority_basis": priority_basis,
        "rank_score": round(rank_score(year, citations, review), 10),
        "exclusion_rule": exclusion,
    }


def stream_jsonl(path: Path) -> Iterable[tuple[int, dict[str, Any]]]:
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"malformed JSON at {path}:{line_number}: {exc}") from exc
            if not isinstance(row, dict):
                raise RuntimeError(f"non-object JSON at {path}:{line_number}")
            yield line_number, row


def load_direct_measurements() -> tuple[dict[str, list[tuple[str, int]]], set[str], dict[str, str]]:
    payload = load_json(PATHS["dispersion"])
    if not isinstance(payload, dict) or not isinstance(payload.get("dispersion"), list):
        raise RuntimeError("dispersion_v2.json has malformed dispersion structure")
    verdicts: dict[str, str] = {}
    for row in payload["dispersion"]:
        quantity = str(row.get("quantity") or "")
        if quantity in QUANTITY_AXIS:
            verdicts[quantity] = str(row.get("verdict") or "")
    missing = sorted(set(QUANTITY_AXIS) - set(verdicts))
    if missing:
        raise RuntimeError(f"dispersion verdicts missing relevant quantities: {missing}")

    eligible_quantities = {
        quantity
        for quantity, verdict in verdicts.items()
        if "contested" in verdict.lower() or "mild" in verdict.lower()
    }
    direct: dict[str, list[tuple[str, int]]] = collections.defaultdict(list)
    measurements = payload.get("measurements")
    if not isinstance(measurements, list):
        raise RuntimeError("dispersion_v2.json has malformed measurements structure")
    for row in measurements:
        if row.get("cluster") != CLUSTER:
            continue
        bibcode = str(row.get("bibcode") or "").strip()
        quantity = str(row.get("quantity") or "")
        if not bibcode or quantity not in eligible_quantities:
            continue
        verdict = verdicts[quantity].lower()
        tier = 4 if "contested" in verdict else 3
        direct[bibcode].append((quantity, tier))
    return dict(direct), eligible_quantities, verdicts


def input_manifest() -> dict[str, dict[str, Any]]:
    manifest = {}
    for name, path in PATHS.items():
        if not path.is_file():
            raise RuntimeError(f"required input missing: {path}")
        manifest[name] = {
            "path": str(path.relative_to(REPO_ROOT)) if path.is_relative_to(REPO_ROOT) else str(path),
            "sha256": sha256_file(path),
            "bytes": path.stat().st_size,
        }
    if manifest["frozen_question"]["sha256"] != FROZEN_QUESTION_SHA256:
        raise RuntimeError("frozen question SHA-256 mismatch; stop rather than improvise")
    return manifest


def count_nested(records: list[dict[str, Any]], field: str) -> dict[str, int]:
    counts: collections.Counter[str] = collections.Counter()
    for record in records:
        value = record.get(field)
        if isinstance(value, list):
            counts.update(str(item) for item in value)
        elif value is not None:
            counts[str(value)] += 1
    return dict(sorted(counts.items()))


def concise_record(record: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in record.items() if key != "exclusion_rule"}


def main() -> int:
    started = time.monotonic()
    manifest = input_manifest()
    base_labels = load_json(PATHS["base_labels"])
    delta_labels = load_json(PATHS["delta_labels"])
    if not isinstance(base_labels, dict) or not isinstance(delta_labels, dict):
        raise RuntimeError("label inputs must be JSON objects")
    base_members = {str(key) for key, value in base_labels.items() if value == CLUSTER}
    delta_members = {str(key) for key, value in delta_labels.items() if value == CLUSTER}
    if not base_members or not delta_members:
        raise RuntimeError("C41 base or delta membership is empty")

    direct_measurements, eligible_quantities, verdicts = load_direct_measurements()
    candidates: list[dict[str, Any]] = []
    base_seen: set[str] = set()
    for _, row in stream_jsonl(PATHS["base_corpus"]):
        bibcode = str(row.get("bibcode") or "")
        if bibcode not in base_members:
            continue
        base_seen.add(bibcode)
        candidates.append(
            classify_candidate(row, "base", direct_measurements, eligible_quantities)
        )
    missing_base = sorted(base_members - base_seen)
    if missing_base:
        raise RuntimeError(
            f"base C41 label/metadata mismatch: {len(missing_base)} labeled members missing metadata"
        )

    delta_seen: set[str] = set()
    for _, row in stream_jsonl(PATHS["delta_corpus"]):
        arxiv_id = str(row.get("arxiv_id") or "")
        if arxiv_id not in delta_members:
            continue
        delta_seen.add(arxiv_id)
        candidates.append(
            classify_candidate(row, "delta", direct_measurements, eligible_quantities)
        )
    missing_delta = sorted(delta_members - delta_seen)
    if missing_delta:
        raise RuntimeError(
            f"delta C41 label/metadata mismatch: {len(missing_delta)} labeled members missing metadata"
        )

    excluded: dict[str, list[dict[str, Any]]] = {
        rule: [] for rule in RULE_TEXT
    }
    identities: set[str] = set()
    eligible: list[dict[str, Any]] = []
    for record in candidates:
        key = record.get("key")
        if key and key in identities:
            record["exclusion_rule"] = "DUPLICATE_IDENTITY"
        elif key:
            identities.add(key)
        rule = record.get("exclusion_rule")
        if rule:
            excluded[rule].append(record)
        else:
            eligible.append(record)

    eligible.sort(
        key=lambda row: (
            -int(row["contested_priority"]),
            -float(row["rank_score"]),
            -int(row["year"]),
            -parse_citations(row.get("citation_count")),
            str(row["key"]),
        )
    )

    included: list[dict[str, Any]] = []
    review_count = 0
    calibration_anchor_count = 0
    for record in eligible:
        if record["review"] and review_count >= REVIEW_CAP:
            record["exclusion_rule"] = "REVIEW_CLASS_CAP"
            excluded["REVIEW_CLASS_CAP"].append(record)
            continue
        if record["calibration_anchor"] and calibration_anchor_count >= CALIBRATION_ANCHOR_CAP:
            record["exclusion_rule"] = "CALIBRATION_ANCHOR_CAP"
            excluded["CALIBRATION_ANCHOR_CAP"].append(record)
            continue
        if len(included) >= CEILING:
            record["exclusion_rule"] = "CAPACITY_BELOW_TOP_180"
            excluded["CAPACITY_BELOW_TOP_180"].append(record)
            continue
        included.append(record)
        if record["review"]:
            review_count += 1
        if record["calibration_anchor"]:
            calibration_anchor_count += 1

    for rank, record in enumerate(included, 1):
        record["rank"] = rank

    universe_count = len(candidates)
    excluded_count = sum(len(records) for records in excluded.values())
    if len(included) > CEILING:
        raise RuntimeError("selection ceiling violated")
    if len(included) + excluded_count != universe_count:
        raise RuntimeError("included/excluded partition does not cover the universe exactly")
    included_keys = [record["key"] for record in included]
    if len(included_keys) != len(set(included_keys)):
        raise RuntimeError("normalized identity appears more than once in the included set")
    nonduplicate_keys = [
        record["key"]
        for rule, records in excluded.items()
        if rule != "DUPLICATE_IDENTITY"
        for record in records
        if record["key"]
    ]
    if len(nonduplicate_keys) != len(set(nonduplicate_keys)):
        raise RuntimeError("non-duplicate exclusion contains a repeated normalized identity")

    rule_counts = {rule: len(excluded[rule]) for rule in RULE_TEXT}
    source_counts = count_nested(included, "source_class")
    axis_counts = count_nested(included, "axis_hits")
    priority_counts = count_nested(included, "contested_priority")
    origin_counts = count_nested(included, "origin")
    year_counts = count_nested(included, "year")

    common = {
        "protocol_version": PROTOCOL_VERSION,
        "cluster": CLUSTER,
        "ceiling": CEILING,
        "review_cap": REVIEW_CAP,
        "calibration_anchor_cap": CALIBRATION_ANCHOR_CAP,
        "input_manifest": manifest,
        "ranking": {
            "priority_order": {
                "4": "direct relevant dispersion measurement; quantity verdict contains contested",
                "3": "direct relevant dispersion measurement; quantity verdict contains mild",
                "2": "strict disagreement lexicon hit",
                "1": "relevant contested/mild dispersion quantity lexicon hit",
                "0": "no contested-measurement signal",
            },
            "within_priority_score": "0.75*recency + 0.23*log_citation + 0.02*review_flag",
            "recency": "clamp((year-2009)/17,0,1)",
            "log_citation": "clamp(log1p(citation_count)/log1p(1000),0,1); missing=0",
            "tie_breakers": ["year_desc", "citation_count_desc", "normalized_identity_asc"],
        },
        "dispersion_relevant_verdicts": {
            quantity: verdicts[quantity] for quantity in sorted(verdicts)
        },
        "safety_ledger": {
            "network": False,
            "database_or_sql": False,
            "model_calls_or_deep_research": False,
            "product_wiki_live_or_deploy": False,
            "git_writes": False,
            "writes_outside_lane": False,
        },
    }

    included_payload = {
        **common,
        "summary": {
            "universe": universe_count,
            "eligible_before_caps": len(eligible),
            "included": len(included),
            "excluded": excluded_count,
            "included_by_source_class": source_counts,
            "included_by_axis_overlapping": axis_counts,
            "included_by_contested_priority": priority_counts,
            "included_by_origin": origin_counts,
            "included_by_year": year_counts,
            "included_reviews": review_count,
            "included_calibration_anchors": calibration_anchor_count,
        },
        "records": [concise_record(record) for record in included],
    }
    excluded_payload = {
        **common,
        "summary": {
            "universe": universe_count,
            "included": len(included),
            "excluded": excluded_count,
            "excluded_by_rule": rule_counts,
        },
        "rule_classes": [
            {
                "rule_id": rule,
                "rule_text": text,
                "count": len(excluded[rule]),
                "records": [concise_record(record) for record in excluded[rule]],
            }
            for rule, text in RULE_TEXT.items()
        ],
    }

    atomic_json(OUTPUT_INCLUDED, included_payload)
    atomic_json(OUTPUT_EXCLUDED, excluded_payload)
    sha_lines = [
        f"{sha256_file(OUTPUT_INCLUDED)}  {OUTPUT_INCLUDED.name}",
        f"{sha256_file(OUTPUT_EXCLUDED)}  {OUTPUT_EXCLUDED.name}",
    ]
    atomic_write(OUTPUT_SHAS, "\n".join(sha_lines) + "\n")

    elapsed = time.monotonic() - started
    print(
        json.dumps(
            {
                "protocol_version": PROTOCOL_VERSION,
                "universe": universe_count,
                "eligible_before_caps": len(eligible),
                "included": len(included),
                "excluded": excluded_count,
                "excluded_by_rule": rule_counts,
                "included_by_axis_overlapping": axis_counts,
                "included_by_source_class": source_counts,
                "included_by_contested_priority": priority_counts,
                "included_by_origin": origin_counts,
                "included_reviews": review_count,
                "included_calibration_anchors": calibration_anchor_count,
                "runtime_seconds": round(elapsed, 6),
                "outputs": [
                    OUTPUT_INCLUDED.name,
                    OUTPUT_EXCLUDED.name,
                    OUTPUT_SHAS.name,
                ],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"STEP1_FILTER_BLOCKED: {exc}", file=sys.stderr)
        raise
