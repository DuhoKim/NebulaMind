#!/usr/bin/env python3
"""Validate arXiv -> claim candidates with Atom and AstroSage."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from arxiv_wiki_feed_common import (
    ASTROSAGE_MODEL,
    ATOM_MODEL,
    OLLAMA_BASE,
    PROMPT_VERSION,
    artifact_dir,
    extract_json_object,
    http_error_text,
    latest_artifact,
    normalize_validation,
    ollama_chat,
    quality_score,
    read_jsonl,
    summarize_counts,
    validator_prompt,
    write_json,
)


def validate_one(candidate: dict, timeout: int) -> dict:
    result = {**candidate}
    validations = []

    atom = call_validator(candidate, ATOM_MODEL, "Atom-7B full scoring", timeout)
    validations.append(atom)
    result["atom_validation"] = atom

    review_labels = {"strict_support", "strict_challenge", "adjacent_support", "needs_human"}
    should_review = atom["label"] in review_labels or atom["score"] >= 0.55
    if should_review:
        astrosage = call_validator(candidate, ASTROSAGE_MODEL, "AstroSage-70B positive/ambiguous review", timeout)
    else:
        astrosage = {
            "model_name": ASTROSAGE_MODEL,
            "host": OLLAMA_BASE,
            "prompt_version": PROMPT_VERSION,
            "label": "not_reviewed",
            "stance": "none",
            "score": 0.0,
            "rationale": "Atom did not mark this candidate as positive or ambiguous.",
            "quoted_evidence_span": None,
            "failure_mode": None,
            "raw_response": None,
            "latency_seconds": 0.0,
        }
    validations.append(astrosage)
    result["astrosage_validation"] = astrosage

    final = aggregate(candidate, atom, astrosage)
    result.update(final)
    result["validations"] = validations
    return result


def call_validator(candidate: dict, model: str, role: str, timeout: int) -> dict:
    prompt = validator_prompt(candidate, role)
    started = time.time()
    try:
        raw_text, meta = ollama_chat(model, prompt, timeout=timeout)
        parsed = normalize_validation(extract_json_object(raw_text))
        return {
            "model_name": model,
            "host": OLLAMA_BASE,
            "prompt_version": PROMPT_VERSION,
            **parsed,
            "raw_response": raw_text,
            "latency_seconds": meta.get("duration_seconds", round(time.time() - started, 3)),
        }
    except Exception as exc:
        return {
            "model_name": model,
            "host": OLLAMA_BASE,
            "prompt_version": PROMPT_VERSION,
            "label": "needs_human",
            "stance": "none",
            "score": 0.0,
            "rationale": "Validator failed; requires human review.",
            "quoted_evidence_span": None,
            "failure_mode": http_error_text(exc)[:300],
            "raw_response": None,
            "latency_seconds": round(time.time() - started, 3),
        }


def aggregate(candidate: dict, atom: dict, astrosage: dict) -> dict:
    duplicate = candidate.get("duplicate_evidence_id")
    if duplicate:
        return {
            "status": "duplicate_existing",
            "validator_label": "duplicate_existing",
            "validator_score": 0.0,
            "validator_agreement": 0.0,
            "label_agreement": 0.0,
            "validator_model_set": [ATOM_MODEL, ASTROSAGE_MODEL],
            "evidence_stance": None,
            "evidence_summary": None,
            "quality": None,
            "promotion_blockers": ["production duplicate exists"],
        }

    blockers = []
    overlap = float(candidate.get("claim_key_overlap") or 0.0)
    if overlap < 0.20:
        blockers.append("claim_key_overlap < 0.20")
    if atom.get("label") != "strict_support":
        blockers.append("Atom label is not strict_support")
    if atom.get("score", 0.0) < 0.90:
        blockers.append("Atom score < 0.90")
    if astrosage.get("label") != "strict_support":
        blockers.append("AstroSage label is not strict_support")
    if astrosage.get("score", 0.0) < 0.80:
        blockers.append("AstroSage score < 0.80")
    if atom.get("stance") != astrosage.get("stance") or atom.get("stance") != "supports":
        blockers.append("Atom/AstroSage stance disagreement or non-support stance")

    label_agreement = 1.0 if atom.get("label") == astrosage.get("label") and atom.get("stance") == astrosage.get("stance") else 0.0
    agreement = 1.0 if not blockers and label_agreement == 1.0 else 0.0
    quality = quality_score(float(atom.get("score") or 0.0), float(astrosage.get("score") or 0.0), 0)
    if agreement < 0.80:
        blockers.append("validator_agreement < 0.80")
    if quality < 0.80:
        blockers.append("quality < 0.80")

    if not blockers:
        status = "validated_ready"
        label = "strict_support"
        stance = "supports"
    elif atom.get("label") == "strict_challenge" or astrosage.get("label") == "strict_challenge":
        status = "needs_human"
        label = "strict_challenge_annotate_only"
        stance = "challenges"
        blockers.append("strict_challenge deferred to v1.1")
    elif atom.get("failure_mode") or astrosage.get("failure_mode"):
        status = "needs_human"
        label = "needs_human"
        stance = None
    elif atom.get("label") != astrosage.get("label") and astrosage.get("label") != "not_reviewed":
        status = "needs_human"
        label = "needs_human"
        stance = None
        blockers.append("Atom/AstroSage label disagreement")
    else:
        status = "validator_rejected"
        label = atom.get("label") or "neutral_or_unclear"
        stance = None

    rationale_parts = [v.get("rationale") for v in (atom, astrosage) if v.get("rationale")]
    return {
        "status": status,
        "validator_label": label,
        "validator_score": round(min(float(atom.get("score") or 0.0), float(astrosage.get("score") or 0.0)), 4),
        "validator_agreement": agreement,
        "label_agreement": label_agreement,
        "validator_model_set": [ATOM_MODEL, ASTROSAGE_MODEL],
        "evidence_stance": stance,
        "evidence_summary": " / ".join(rationale_parts)[:1200] if status == "validated_ready" else None,
        "quality": round(quality, 4),
        "promotion_blockers": sorted(set(blockers)),
        "rakon_annotation": "required_for_dispute" if status == "needs_human" else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", type=Path)
    parser.add_argument("--page-slug", default="galaxy-evolution")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--sleep", type=float, default=0.1)
    parser.add_argument("--output-name", default="validator.jsonl")
    parser.add_argument("--summary-name", default="validate_summary.json")
    args = parser.parse_args()

    candidates_path = args.candidates or latest_artifact("candidates.jsonl")
    candidates = read_jsonl(candidates_path)
    candidates = [row for row in candidates if row.get("status") == "shadow_proposed"]
    if args.limit:
        candidates = candidates[: args.limit]

    run_dir = candidates_path.parent
    validator_path = run_dir / args.output_name
    completed_keys = set()
    rows = []
    if validator_path.exists():
        rows = read_jsonl(validator_path)
        completed_keys = {(row.get("claim_id"), row.get("arxiv_id")) for row in rows}
        print(f"Resuming with {len(completed_keys)} completed validations from {validator_path}", flush=True)

    remaining = [
        row
        for row in candidates
        if (row.get("claim_id"), row.get("arxiv_id")) not in completed_keys
    ]

    with validator_path.open("a", encoding="utf-8") as fh:
        for offset, candidate in enumerate(remaining, start=1):
            idx = len(completed_keys) + offset
            print(f"[{idx}/{len(candidates)}] claim={candidate['claim_id']} arxiv={candidate['arxiv_id']}", flush=True)
            row = validate_one(candidate, args.timeout)
            rows.append(row)
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
            fh.flush()
            if args.sleep:
                time.sleep(args.sleep)

    summary_path = run_dir / args.summary_name
    rows = read_jsonl(validator_path)

    strict_rows = [r for r in rows if r.get("astrosage_validation", {}).get("label") != "not_reviewed"]
    agreement_denom = len(strict_rows)
    agreement_count = sum(
        1
        for r in strict_rows
        if r.get("atom_validation", {}).get("label") == r.get("astrosage_validation", {}).get("label")
        and r.get("atom_validation", {}).get("stance") == r.get("astrosage_validation", {}).get("stance")
    )
    summary = {
        "candidates_path": str(candidates_path),
        "validator_path": str(validator_path),
        "dry_run": args.dry_run,
        "validated_count": len(rows),
        "final_status_counts": summarize_counts(rows, "status"),
        "final_label_counts": summarize_counts(rows, "validator_label"),
        "atom_label_counts": summarize_counts([r["atom_validation"] for r in rows], "label"),
        "astrosage_label_counts": summarize_counts([r["astrosage_validation"] for r in rows], "label"),
        "atom_astrosage_agreement_rate": round(agreement_count / agreement_denom, 4) if agreement_denom else 0.0,
        "validated_ready": sum(1 for r in rows if r.get("status") == "validated_ready"),
        "validated_ready_distinct_claims": len({r["claim_id"] for r in rows if r.get("status") == "validated_ready"}),
    }
    write_json(summary_path, summary)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
