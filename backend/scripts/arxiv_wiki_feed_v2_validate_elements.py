#!/usr/bin/env python3
"""Track B Phase 2 element-level validator for the arXiv wiki feed.

Default mode is artifact-only and safe for shadow runs. Model vote phases are
restart-safe and keyed by candidate_key + element_id + model + prompt_version.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import time
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ARTIFACT_ROOT = Path("/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2")
DEFAULT_PHASE1 = ARTIFACT_ROOT / "atomize_galaxy_evolution_20260524T174549Z" / "elements.jsonl"
DEFAULT_PHASE15 = ARTIFACT_ROOT / "atomize_galaxy_evolution_20260524T174549Z_phase15_retry_20260524T235035Z" / "elements.jsonl"
DEFAULT_CANDIDATES = (
    Path("/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed")
    / "arxiv_wiki_feed_v1_galaxy_evolution_20260524_120421"
    / "candidates.jsonl"
)
ATOM_MODEL = os.getenv("ARXIV_WIKI_ATOM_MODEL", "vanta-research/atom-astronomy-7b:latest")
ASTROSAGE_MODEL = os.getenv("ARXIV_WIKI_ASTROSAGE_MODEL", "astrosage-70b:latest")
OLLAMA_BASE = os.getenv("ARXIV_WIKI_OLLAMA_BASE", "http://localhost:11434")
PROMPT_VERSION = "arxiv_wiki_feed_v2_element_validator_phase2_20260525"
RECOVERED_IDS = {1641, 1682, 1686, 1735, 1742, 1784, 1787, 1822}
PERMANENT_FAILURE_IDS = {1653}

STOPWORDS = {
    "the", "and", "or", "of", "in", "to", "a", "an", "for", "with", "by", "at", "as",
    "is", "are", "was", "were", "that", "this", "these", "those", "from", "on", "into",
    "galaxy", "galaxies", "stellar", "star", "stars", "formation", "evolution", "redshift",
}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")


def sha_key(*parts: Any) -> str:
    normalized = "||".join(str(p or "").strip().lower() for p in parts)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def sha_text(value: Any) -> str:
    if value is None:
        value = ""
    if not isinstance(value, str):
        value = json.dumps(value, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def hydration_missing_error(row: dict[str, Any], missing: list[str], source: Path) -> ValueError:
    return ValueError(
        "HYDRATION_ARTIFACT_MISSING_TEXT: regenerate coverage artifact first; "
        f"missing={missing}; "
        f"tuple=({row.get('claim_id')}, {row.get('element_id')}, {row.get('arxiv_id')}); "
        f"source={source}"
    )


def tokenize(text: str | None) -> set[str]:
    if not isinstance(text, str):
        text = json.dumps(text, ensure_ascii=False) if text is not None else ""
    tokens = re.findall(r"[a-z][a-z0-9\-]{2,}", (text or "").lower())
    return {tok for tok in tokens if tok not in STOPWORDS and not tok.isdigit()}


def extract_json_object(text_value: str) -> dict[str, Any]:
    text_value = (text_value or "").strip()
    if not text_value:
        raise ValueError("empty model response")
    decoder = json.JSONDecoder()
    try:
        parsed, _end = decoder.raw_decode(text_value)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        start = text_value.find("{")
        end = text_value.rfind("}")
        if start < 0 or end <= start:
            raise
        return json.loads(text_value[start : end + 1])
    raise ValueError("model response did not start with a JSON object")


def normalize_vote(payload: dict[str, Any]) -> dict[str, Any]:
    label = str(payload.get("label") or "needs_human").strip().lower()
    if label not in {"supported", "partial", "missing", "contradicted", "needs_human"}:
        label = "needs_human"
    stance = str(payload.get("stance") or "none").strip().lower()
    if stance not in {"supports", "challenges", "none"}:
        stance = "none"
    try:
        score = max(0.0, min(1.0, float(payload.get("score", 0.0))))
    except Exception:
        score = 0.0
    return {
        "label": label,
        "stance": stance,
        "score": round(score, 4),
        "quoted_evidence_span": payload.get("quoted_evidence_span"),
        "matched_subject": payload.get("matched_subject"),
        "matched_mechanism": payload.get("matched_mechanism"),
        "matched_regime": payload.get("matched_regime"),
        "rationale": str(payload.get("rationale") or "")[:1200],
        "failure_mode": payload.get("failure_mode"),
    }


def ollama_chat(model: str, prompt: str, timeout: int) -> tuple[str, float]:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": 0.0, "num_ctx": 4096, "num_predict": 360},
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        f"{OLLAMA_BASE}/api/chat",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    started = time.time()
    with urllib.request.urlopen(request, timeout=timeout) as response:
        raw = response.read().decode("utf-8", errors="replace")
    parsed = json.loads(raw)
    return ((parsed.get("message") or {}).get("content") or "").strip(), round(time.time() - started, 3)


def element_prompt(pair: dict[str, Any], role: str) -> str:
    return f"""You are an astronomy element-level evidence validator ({role}).

Label whether the paper abstract supports this single required claim element.
Use only the abstract text. Quote only exact words from the abstract.

Labels:
- supported: abstract directly supports the element as written.
- partial: abstract supports a weaker, broader, nearby, or scope-shifted version.
- missing: abstract does not address the element.
- contradicted: abstract directly conflicts with the element.
- needs_human: ambiguous, malformed, or requires full text.

Respond with JSON only:
{{"label":"supported|partial|missing|contradicted|needs_human","stance":"supports|challenges|none","score":0.0,"quoted_evidence_span":null,"matched_subject":null,"matched_mechanism":null,"matched_regime":null,"rationale":"...","failure_mode":null}}

Claim:
{pair.get("claim_text_snapshot")}

Element:
- id: {pair.get("element_id")}
- type: {pair.get("element_type")}
- required: {pair.get("required")}
- text: {pair.get("element_text")}
- normalized_subject: {pair.get("normalized_subject")}
- normalized_mechanism: {pair.get("normalized_mechanism")}
- quantity_or_range: {json.dumps(pair.get("quantity_or_range"), ensure_ascii=False)}
- redshift_or_environment: {json.dumps(pair.get("redshift_or_environment"), ensure_ascii=False)}

Paper:
- arXiv: {pair.get("arxiv_id")}
- title: {pair.get("paper_title_snapshot")}
- abstract: {pair.get("paper_abstract_snapshot")}
"""


def merge_elements(phase1_path: Path, phase15_path: Path, out_dir: Path) -> list[dict[str, Any]]:
    phase1 = read_jsonl(phase1_path)
    phase15 = read_jsonl(phase15_path)
    merged = [
        row for row in phase1
        if int(row.get("claim_id")) not in RECOVERED_IDS and int(row.get("claim_id")) not in PERMANENT_FAILURE_IDS
    ]
    merged.extend(row for row in phase15 if int(row.get("claim_id")) not in PERMANENT_FAILURE_IDS)
    merged.sort(key=lambda r: (int(r["claim_id"]), int(r.get("element_index") or 0)))

    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for row in merged:
        claim_id = int(row["claim_id"])
        element_index = int(row.get("element_index") or len(out) + 1)
        element_id = row.get("element_id") or f"claim-{claim_id}-e{element_index:02d}"
        if element_id in seen:
            raise SystemExit(f"Duplicate element_id: {element_id}")
        seen.add(element_id)
        out.append(
            {
                **row,
                "run_key": out_dir.name,
                "element_id": element_id,
                "claim_id": claim_id,
                "element_index": element_index,
                "required": bool(row.get("required")),
                "source_artifact": str(phase15_path if claim_id in RECOVERED_IDS else phase1_path),
                "phase2_merge_rule": "phase15_overlay" if claim_id in RECOVERED_IDS else "phase1_primary",
            }
        )
    write_jsonl(out_dir / "element_claims_merged.jsonl", out)
    return out


def build_pairs(elements: list[dict[str, Any]], candidates_path: Path, out_dir: Path) -> list[dict[str, Any]]:
    candidates = read_jsonl(candidates_path)
    by_claim: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for element in elements:
        by_claim[int(element["claim_id"])].append(element)

    rows: list[dict[str, Any]] = []
    for candidate in candidates:
        claim_id = int(candidate["claim_id"])
        claim_elements = by_claim.get(claim_id, [])
        if not claim_elements:
            continue
        candidate_key = sha_key(
            candidate.get("page_id"),
            claim_id,
            candidate.get("arxiv_id"),
            candidate.get("paper_title_snapshot"),
            candidate.get("candidate_source"),
        )
        abstract_tokens = tokenize(" ".join([candidate.get("paper_title_snapshot") or "", candidate.get("paper_abstract_snapshot") or ""]))
        for element in claim_elements:
            element_tokens = tokenize(" ".join([
                str(element.get("text") or ""),
                json.dumps(element.get("normalized_subject"), ensure_ascii=False) if element.get("normalized_subject") is not None else "",
                json.dumps(element.get("normalized_mechanism"), ensure_ascii=False) if element.get("normalized_mechanism") is not None else "",
            ]))
            overlap = sorted(element_tokens & abstract_tokens)
            precheck_label = None
            precheck_reason = None
            if element_tokens and not overlap:
                precheck_label = "missing"
                precheck_reason = "no lexical overlap between element terms and title/abstract"
            rows.append(
                {
                    "run_key": out_dir.name,
                    "candidate_key": candidate_key,
                    "claim_id": claim_id,
                    "element_id": element["element_id"],
                    "element_index": element["element_index"],
                    "element_type": element.get("element_type"),
                    "element_text": element.get("text"),
                    "required": bool(element.get("required")),
                    "normalized_subject": element.get("normalized_subject"),
                    "normalized_mechanism": element.get("normalized_mechanism"),
                    "quantity_or_range": element.get("quantity_or_range"),
                    "redshift_or_environment": element.get("redshift_or_environment"),
                    "claim_text_snapshot": candidate.get("claim_text_snapshot") or element.get("parent_claim_text"),
                    "arxiv_id": candidate.get("arxiv_id"),
                    "paper_title_snapshot": candidate.get("paper_title_snapshot"),
                    "paper_abstract_snapshot": candidate.get("paper_abstract_snapshot"),
                    "paper_year": candidate.get("paper_year"),
                    "candidate_source": candidate.get("candidate_source"),
                    "candidate_status": candidate.get("status"),
                    "duplicate_evidence_id": candidate.get("duplicate_evidence_id"),
                    "claim_key_overlap": candidate.get("claim_key_overlap"),
                    "matched_terms": candidate.get("matched_terms"),
                    "element_matched_terms": overlap[:20],
                    "precheck_label": precheck_label,
                    "precheck_reason": precheck_reason,
                    "source_candidate_artifact": str(candidates_path),
                    "source_element_artifact": element.get("source_artifact"),
                }
            )
    write_jsonl(out_dir / "element_candidate_pairs.jsonl", rows)
    return rows



def row_is_coverage_ready(row: dict[str, Any], allow_incomplete_coverage: bool = False) -> bool:
    if allow_incomplete_coverage:
        return True
    status = str(row.get("coverage_status") or "").strip().lower()
    return status == "coverage_ready"


def build_targeted_pairs_from_coverage_ready(
    coverage_rows_path: Path,
    source_dir: Path | None,
    out_dir: Path,
    require_hydrated: bool = False,
    db_reads_used: list[bool] | None = None,
    allow_incomplete_coverage: bool = False,
) -> list[dict[str, Any]]:
    # Targeted mode is a pure artifact consumer. coverage_rows_path is authoritative.
    if db_reads_used is not None:
        db_reads_used.append(False)
    rows = read_jsonl(coverage_rows_path)

    targeted_pairs = []
    seen = set()

    coverage_backlog = [row for row in rows if not row_is_coverage_ready(row, allow_incomplete_coverage)]
    rows_for_validator = [row for row in rows if row_is_coverage_ready(row, allow_incomplete_coverage)]
    write_jsonl(out_dir / "coverage_backlog_rows.jsonl", coverage_backlog)

    for row in rows_for_validator:
        claim_id = int(row.get("claim_id"))
        element_id = row.get("element_id")
        arxiv_id = row.get("arxiv_id")

        tuple_key = (claim_id, element_id, arxiv_id)
        if tuple_key in seen:
            raise ValueError(f"DUPLICATE_TARGET_TUPLE: {tuple_key}")
        seen.add(tuple_key)

        required_fields = ["claim_text_snapshot", "element_text", "paper_title_snapshot", "paper_abstract_snapshot"]
        missing = [field for field in required_fields if not str(row.get(field) or "").strip()]
        if not isinstance(row.get("required"), bool):
            missing.append("required")
        if row.get("hydration_db_reads_used") is not False:
            missing.append("hydration_db_reads_used")
        if row.get("hydration_policy") not in (None, "artifact_only_fail_closed"):
            missing.append("hydration_policy")
        if missing:
            raise hydration_missing_error(row, missing, coverage_rows_path)

        source_hashes = row.get("source_hashes") or {}
        expected_hashes = {
            "claim_text_hash": sha_text(row.get("claim_text_snapshot")),
            "element_text_hash": sha_text(row.get("element_text")),
            "paper_title_hash": sha_text(row.get("paper_title_snapshot")),
            "paper_abstract_hash": sha_text(row.get("paper_abstract_snapshot")),
        }
        mismatched = [key for key, expected in expected_hashes.items() if source_hashes.get(key) != expected]
        if mismatched:
            raise ValueError(
                "HYDRATION_ARTIFACT_HASH_MISMATCH: "
                f"fields={mismatched}; tuple={tuple_key}; source={coverage_rows_path}"
            )

        pair = {
            "run_key": out_dir.name,
            "claim_id": claim_id,
            "element_id": element_id,
            "arxiv_id": arxiv_id,
            "claim_text_snapshot": row.get("claim_text_snapshot"),
            "element_text": row.get("element_text"),
            "element_type": row.get("element_type"),
            "required": row.get("required"),
            "normalized_subject": row.get("normalized_subject"),
            "normalized_mechanism": row.get("normalized_mechanism"),
            "quantity_or_range": row.get("quantity_or_range"),
            "redshift_or_environment": row.get("redshift_or_environment"),
            "candidate_key": sha_key("targeted", row.get("candidate_key"), claim_id, arxiv_id, element_id),
            "source_candidate_key": row.get("candidate_key"),
            "candidate_source": "coverage_ready_targeted",
            "candidate_atom_coverage_status": row.get("candidate_atom_coverage_status"),
            "coverage_status": row.get("coverage_status") or "coverage_ready",
            "coverage_required_stages": row.get("coverage_required_stages"),
            "coverage_missing_stages": row.get("coverage_missing_stages") or [],
            "coverage_artifact_refs": row.get("coverage_artifact_refs") or {},
            "section": row.get("section"),
            "retrieval_filter_decision": row.get("retrieval_filter_decision"),
            "paper_title_snapshot": row.get("paper_title_snapshot"),
            "paper_abstract_snapshot": row.get("paper_abstract_snapshot"),
            "matched_terms": row.get("matched_terms"),
            "element_matched_terms": row.get("element_matched_terms"),
            "source_hashes": source_hashes,
            "hydration_sources": row.get("hydration_sources"),
            "hydration_db_reads_used": False,
            "hydration_policy": "artifact_only_fail_closed",
            "coverage_ready_targeted_run": True,
            "targeted_coverage_mode": True,
            "promotion_eligible": False,
        }

        targeted_pairs.append(pair)

    write_jsonl(out_dir / "element_candidate_pairs.jsonl", targeted_pairs)

    write_json(out_dir / "targeted_metrics.json", {
        "coverage_ready_input_rows": len(rows),
        "targeted_pair_rows": len(targeted_pairs),
        "coverage_backlog_rows": len(coverage_backlog),
        "allow_incomplete_coverage": allow_incomplete_coverage,
        "hydration_missing_rows": 0,
        "db_reads_used": False,
        "hydration_policy": "artifact_only_fail_closed",
        "precheck_empty_text_failures": 0,
        "coverage_ready_targeted_run": True,
        "targeted_coverage_mode": True,
        "promotion_eligible": False,
    })

    return targeted_pairs

def completed_vote_keys(path: Path) -> set[tuple[str, str, str, str]]:
    if not path.exists():
        return set()
    return {
        (row.get("candidate_key"), row.get("element_id"), row.get("model_name"), row.get("prompt_version"))
        for row in read_jsonl(path)
    }


def vote_pairs(
    pairs: list[dict[str, Any]],
    out_dir: Path,
    model: str,
    output_name: str,
    role: str,
    timeout: int,
    max_votes: int,
    include_pair,
) -> int:
    out_path = out_dir / output_name
    done = completed_vote_keys(out_path)
    count = 0
    for pair in pairs:
        if pair.get("precheck_label"):
            continue
        if not include_pair(pair):
            continue
        key = (pair["candidate_key"], pair["element_id"], model, PROMPT_VERSION)
        if key in done:
            continue
        if max_votes and count >= max_votes:
            break
        started = time.time()
        try:
            raw, latency = ollama_chat(model, element_prompt(pair, role), timeout)
            vote = normalize_vote(extract_json_object(raw))
            failure = vote.get("failure_mode")
        except Exception as exc:
            raw = locals().get("raw")
            latency = round(time.time() - started, 3)
            vote = {
                "label": "needs_human",
                "stance": "none",
                "score": 0.0,
                "quoted_evidence_span": None,
                "matched_subject": None,
                "matched_mechanism": None,
                "matched_regime": None,
                "rationale": "Model call or parse failed.",
                "failure_mode": str(exc)[:300],
            }
            failure = vote["failure_mode"]
        append_jsonl(
            out_path,
            {
                **{k: pair.get(k) for k in ["run_key", "candidate_key", "claim_id", "element_id", "element_type", "required", "arxiv_id", "paper_title_snapshot", "paper_abstract_snapshot"]},
                "model_name": model,
                "prompt_version": PROMPT_VERSION,
                **vote,
                "raw_response": raw,
                "latency_seconds": latency,
                "failure_mode": failure,
                "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            },
        )
        count += 1
    return count


def aggregate(out_dir: Path) -> list[dict[str, Any]]:
    pairs = read_jsonl(out_dir / "element_candidate_pairs.jsonl")
    atom_votes = read_jsonl(out_dir / "element_votes_atom.jsonl") if (out_dir / "element_votes_atom.jsonl").exists() else []
    astrosage_votes = read_jsonl(out_dir / "element_votes_astrosage.jsonl") if (out_dir / "element_votes_astrosage.jsonl").exists() else []
    atom_by_key = {(v["candidate_key"], v["element_id"]): v for v in atom_votes}
    astro_by_key = {(v["candidate_key"], v["element_id"]): v for v in astrosage_votes}

    summary_rows: list[dict[str, Any]] = []
    by_candidate: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for pair in pairs:
        key = (pair["candidate_key"], pair["element_id"])
        atom = atom_by_key.get(key)
        astro = astro_by_key.get(key)
        final_label = pair.get("precheck_label") or (astro or atom or {}).get("label") or "needs_human"
        final_score = (astro or atom or {}).get("score", 0.0)
        if pair.get("precheck_label"):
            final_score = 0.0
        row = {
            **{k: pair.get(k) for k in ["run_key", "candidate_key", "claim_id", "element_id", "element_type", "required", "arxiv_id"]},
            "final_label": final_label,
            "final_score": final_score,
            "atom_label": atom.get("label") if atom else None,
            "astrosage_label": astro.get("label") if astro else None,
            "precheck_label": pair.get("precheck_label"),
            "precheck_reason": pair.get("precheck_reason"),
        }
        summary_rows.append(row)
        by_candidate[pair["candidate_key"]].append(row)
    write_jsonl(out_dir / "element_vote_summary.jsonl", summary_rows)

    aggregates: list[dict[str, Any]] = []
    targeted_mode = (out_dir / "targeted_metrics.json").exists()
    for candidate_key, rows in by_candidate.items():
        required = [r for r in rows if r.get("required")]
        labels = [r.get("final_label") for r in required]
        first_pair = next(p for p in pairs if p["candidate_key"] == candidate_key)
        targeted_status = str(first_pair.get("candidate_atom_coverage_status") or "").strip().lower()
        if targeted_mode and targeted_status == "ready":
            claim_label = "coverage_ready"
            status = "validated_ready"
        elif targeted_mode and targeted_status in {"missing", "error_terminal"}:
            claim_label = "coverage_missing"
            status = "validator_rejected"
        elif targeted_mode and targeted_status in {"needs_human", "error_retryable"}:
            claim_label = "coverage_needs_human"
            status = "needs_human"
        elif required and all(label == "supported" for label in labels):
            claim_label = "strict_support"
            status = "validated_ready"
        elif "contradicted" in labels:
            claim_label = "strict_challenge"
            status = "needs_human"
        elif any(label == "supported" for label in labels) and any(label in {"partial", "missing"} for label in labels):
            claim_label = "adjacent_support"
            status = "validator_rejected"
        elif any(label == "needs_human" for label in labels):
            claim_label = "needs_human"
            status = "needs_human"
        else:
            claim_label = "neutral_or_unclear"
            status = "validator_rejected"
        aggregates.append(
            {
                "run_key": out_dir.name,
                "candidate_key": candidate_key,
                "claim_id": first_pair["claim_id"],
                "element_id": first_pair.get("element_id"),
                "arxiv_id": first_pair["arxiv_id"],
                "source_candidate_key": first_pair.get("source_candidate_key"),
                "candidate_atom_coverage_status": first_pair.get("candidate_atom_coverage_status"),
                "paper_title_snapshot": first_pair["paper_title_snapshot"],
                "claim_level_label": claim_label,
                "status": status,
                "required_element_count": len(required),
                "supported_required_count": sum(1 for label in labels if label == "supported"),
                "missing_required_count": sum(1 for label in labels if label == "missing"),
                "partial_required_count": sum(1 for label in labels if label == "partial"),
                "needs_human_required_count": sum(1 for label in labels if label == "needs_human"),
                "contradicted_required_count": sum(1 for label in labels if label == "contradicted"),
                "promotion_blockers": [] if status == "validated_ready" else sorted({label for label in labels if label != "supported"}),
                "targeted_coverage_mode": targeted_mode,
                "coverage_ready_targeted_run": targeted_mode,
                "promotion_eligible": False if targeted_mode else status == "validated_ready",
            }
        )
    aggregates.sort(key=lambda r: (r["status"] != "validated_ready", r["claim_id"], r["arxiv_id"]))
    write_jsonl(out_dir / "claim_candidate_aggregate.jsonl", aggregates)
    manifest_rows = [r for r in aggregates if r["status"] == "validated_ready"]
    write_json(
        out_dir / "promotion_manifest_phase2_shadow.json",
        {
            "run_key": out_dir.name,
            "executable": False,
            "targeted_coverage_mode": targeted_mode,
            "coverage_ready_targeted_run": targeted_mode,
            "promotion_eligible": False if targeted_mode else bool(manifest_rows),
            "validated_ready": [] if targeted_mode else manifest_rows,
        },
    )
    return aggregates


def write_report(out_dir: Path, args: argparse.Namespace) -> None:
    metrics = build_metrics(out_dir, args)
    write_json(out_dir / "phase2_metrics.json", metrics)
    report = [
        "# Track B Phase 2 Element Validator Shadow Report",
        "",
        f"- Run key: `{out_dir.name}`",
        f"- No DB write: `{args.no_db_write}`",
        f"- Candidate source: `{args.candidates}`",
        f"- Final denominator: 320 parseable claims; permanent atomizer failure excluded: `1653`.",
        f"- Merged elements: {metrics['counts'].get('merged_elements', 0)}",
        f"- Candidate-element pairs: {metrics['counts'].get('candidate_element_pairs', 0)}",
        f"- Atom votes: {metrics['counts'].get('atom_votes', 0)}",
        f"- AstroSage votes: {metrics['counts'].get('astrosage_votes', 0)}",
        f"- Shadow validated_ready rows: {metrics['counts'].get('validated_ready', 0)}",
        f"- Shadow validated_ready distinct claims: {metrics['counts'].get('validated_ready_distinct_claims', 0)}",
        "",
        "Stop point: Phase 2 shadow artifacts only; no production evidence apply.",
    ]
    (out_dir / "phase2_validator_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")


def build_metrics(out_dir: Path, args: argparse.Namespace) -> dict[str, Any]:
    def count(path: str) -> int:
        f = out_dir / path
        return len(read_jsonl(f)) if f.exists() else 0
    aggregates = read_jsonl(out_dir / "claim_candidate_aggregate.jsonl") if (out_dir / "claim_candidate_aggregate.jsonl").exists() else []
    targeted_metrics_path = out_dir / "targeted_metrics.json"
    targeted_metrics = json.loads(targeted_metrics_path.read_text(encoding="utf-8")) if targeted_metrics_path.exists() else {}
    targeted_mode = bool(targeted_metrics)
    return {
        "run_key": out_dir.name,
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "no_db_write": args.no_db_write,
        "db_reads_used": bool(targeted_metrics.get("db_reads_used", False)),
        "hydration_policy": targeted_metrics.get("hydration_policy"),
        "targeted_coverage_mode": targeted_mode,
        "coverage_ready_targeted_run": targeted_mode,
        "promotion_eligible": False if targeted_mode else any(r.get("status") == "validated_ready" for r in aggregates),
        "next_step": "expand_coverage_first" if targeted_mode else None,
        "prompt_version": PROMPT_VERSION,
        "models": {"atom": ATOM_MODEL, "astrosage": ASTROSAGE_MODEL},
        "inputs": {
            "phase1_elements": str(args.phase1_elements),
            "phase15_elements": str(args.phase15_elements),
            "candidates": str(args.candidates),
        },
        "counts": {
            "merged_elements": count("element_claims_merged.jsonl"),
            "candidate_element_pairs": count("element_candidate_pairs.jsonl"),
            "atom_votes": count("element_votes_atom.jsonl"),
            "astrosage_votes": count("element_votes_astrosage.jsonl"),
            "element_vote_summary": count("element_vote_summary.jsonl"),
            "claim_candidate_aggregate": len(aggregates),
            "validated_ready": sum(1 for r in aggregates if r.get("status") == "validated_ready"),
            "validated_ready_distinct_claims": len({r["claim_id"] for r in aggregates if r.get("status") == "validated_ready"}),
        },
        "targeted_metrics": targeted_metrics,
        "permanent_atomizer_failures": sorted(PERMANENT_FAILURE_IDS),
        "recovered_phase15_claims": sorted(RECOVERED_IDS),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--page-slug", default="galaxy-evolution")
    parser.add_argument("--phase1-elements", type=Path, default=DEFAULT_PHASE1)
    parser.add_argument("--phase15-elements", type=Path, default=DEFAULT_PHASE15)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--coverage-ready-rows", type=Path)
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--targeted-coverage-mode", action="store_true")
    parser.add_argument("--require-hydrated-text", action="store_true")
    parser.add_argument("--allow-incomplete-coverage", action="store_true", help="Diagnostic override; do not use for production promotion.")
    parser.add_argument("--out-dir", type=Path)
    parser.add_argument("--no-db-write", action="store_true", required=True)
    parser.add_argument("--phases", nargs="+", default=["merge-elements", "build-pairs", "aggregate", "report"])
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--max-atom-votes", type=int, default=0)
    parser.add_argument("--max-astrosage-votes", type=int, default=0)
    args = parser.parse_args()

    if not args.no_db_write:
        raise SystemExit("Phase 2 validator must run with --no-db-write")

    out_dir = args.out_dir or ARTIFACT_ROOT / f"arxiv_wiki_feed_v2_phase2_element_validator_{dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    out_dir.mkdir(parents=True, exist_ok=True)

    elements: list[dict[str, Any]]
    pairs: list[dict[str, Any]]
    
    if args.targeted_coverage_mode:
        if not args.coverage_ready_rows:
            raise SystemExit("BLOCKED_VALIDATOR_TARGETED_INPUT_SOURCE_ARTIFACT_MISSING: --coverage-ready-rows required")
        if "build-pairs" in args.phases:
            pairs = build_targeted_pairs_from_coverage_ready(
                args.coverage_ready_rows,
                args.source_dir,
                out_dir,
                args.require_hydrated_text,
                allow_incomplete_coverage=args.allow_incomplete_coverage,
            )
    else:
        if "merge-elements" in args.phases:
            elements = merge_elements(args.phase1_elements, args.phase15_elements, out_dir)
        else:
            elements = read_jsonl(out_dir / "merged_elements.jsonl")

        if "build-pairs" in args.phases:
            build_pairs(elements, args.candidates, out_dir)

    if "build-pairs" not in args.phases:
        pairs = read_jsonl(out_dir / "element_candidate_pairs.jsonl")

    if "atom-vote" in args.phases:
        vote_pairs(
            pairs, out_dir, ATOM_MODEL, "element_votes_atom.jsonl", "Atom-7B bulk vote",
            args.timeout, args.max_atom_votes, lambda _pair: True,
        )

    if "astrosage-review" in args.phases:
        atom_votes = read_jsonl(out_dir / "element_votes_atom.jsonl") if (out_dir / "element_votes_atom.jsonl").exists() else []
        atom_by_key = {(v["candidate_key"], v["element_id"]): v for v in atom_votes}

        def needs_review(pair: dict[str, Any]) -> bool:
            vote = atom_by_key.get((pair["candidate_key"], pair["element_id"]))
            if not vote:
                return False
            return (
                vote.get("label") == "supported"
                or (vote.get("label") == "partial" and pair.get("required"))
                or pair.get("element_type") == "redshift_or_environment"
                or (
                    pair.get("element_type") == "quantity_or_threshold"
                    and float(vote.get("score") or 0.0) >= 0.50
                )
            )

        vote_pairs(
            pairs, out_dir, ASTROSAGE_MODEL, "element_votes_astrosage.jsonl", "AstroSage-70B promotion review",
            args.timeout, args.max_astrosage_votes, needs_review,
        )

    if "aggregate" in args.phases:
        aggregate(out_dir)

    (out_dir / "element_votes_rakon_audit.jsonl").touch(exist_ok=True)
    if not (out_dir / "rakon_deferred_audit_replacement.md").exists():
        (out_dir / "rakon_deferred_audit_replacement.md").write_text(
            "Rakon audit deferred in this shadow script run; no production apply is allowed in Phase 2.\n",
            encoding="utf-8",
        )
    write_report(out_dir, args)
    print(json.dumps(build_metrics(out_dir, args), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
