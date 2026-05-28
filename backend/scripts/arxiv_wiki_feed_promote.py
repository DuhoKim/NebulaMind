#!/usr/bin/env python3
"""Create promotion manifests and, only with explicit approval, promote evidence."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import random
from pathlib import Path

from sqlalchemy import text

from arxiv_wiki_feed_common import code_version, db_engine, latest_artifact, read_jsonl, write_json


TIER_B_AUDIT_SAMPLE_SIZE = 20
TIER_B_AUDIT_SAMPLE_SEED = 20260524
V1_1_SAMPLE_SIZE = 20
V1_1_SAMPLE_SEED = 20260524


def parse_force_rows(value: str | None) -> set[tuple[int, str]]:
    if not value:
        return set()
    rows = set()
    for item in value.split(","):
        item = item.strip()
        if not item:
            continue
        claim_id, sep, arxiv_id = item.partition(":")
        if not sep:
            raise SystemExit(f"Invalid --force-rows item {item!r}; expected claim_id:arxiv_id")
        rows.add((int(claim_id), arxiv_id.strip()))
    return rows


def build_manifest(rows: list[dict], args: argparse.Namespace, validator_path: Path) -> dict:
    ready = [row for row in rows if row.get("status") == "validated_ready"]
    force_rows = parse_force_rows(args.force_rows)
    if force_rows:
        ready = [row for row in ready if (int(row["claim_id"]), row["arxiv_id"]) in force_rows]
        found = {(int(row["claim_id"]), row["arxiv_id"]) for row in ready}
        missing = sorted(force_rows - found)
        if missing:
            raise SystemExit(f"--force-rows requested rows not found as validated_ready: {missing}")
    if args.limit:
        ready = ready[: args.limit]
    distinct_claims = sorted({row["claim_id"] for row in ready})
    gate = {
        "first_batch_min_ready": 30,
        "first_batch_min_distinct_claims": 15,
        "first_batch_requires_full_manual_audit_precision": 0.95,
        "second_promotion_min_ready": 100,
        "second_promotion_min_distinct_claims": 40,
        "strict_support_only": True,
        "first_batch_signoff": "HwaO + Papa",
    }
    gate_passes_counts = len(ready) >= gate["first_batch_min_ready"] and len(distinct_claims) >= gate["first_batch_min_distinct_claims"]
    return {
        "manifest_version": "arxiv_wiki_feed_v1_20260524",
        "created_at": dt.datetime.now().isoformat(timespec="seconds"),
        "source_validator_path": str(validator_path),
        "dry_run": not args.apply,
        "apply_requested": args.apply,
        "approved_by": args.approved_by,
        "promotion_gate": gate,
        "gate_passes_counts": gate_passes_counts,
        "count_gate_override": bool(force_rows),
        "override_reason": args.override_reason if force_rows else None,
        "forced_rows": sorted([{"claim_id": claim_id, "arxiv_id": arxiv_id} for claim_id, arxiv_id in force_rows], key=lambda r: (r["claim_id"], r["arxiv_id"])),
        "manual_signoff_required_before_apply": True,
        "validated_ready_count": len(ready),
        "validated_ready_distinct_claim_count": len(distinct_claims),
        "candidate_ids": [row.get("id") for row in ready if row.get("id")],
        "rows": [
            {
                "claim_id": row["claim_id"],
                "arxiv_id": row["arxiv_id"],
                "title": row["paper_title_snapshot"],
                "quality": row.get("quality"),
                "validator_score": row.get("validator_score"),
                "validator_agreement": row.get("validator_agreement"),
                "summary": row.get("evidence_summary"),
                "candidate": row,
            }
            for row in ready
        ],
        "promoted_evidence_ids": [],
    }


def validation_label(row: dict, key: str) -> str | None:
    validation = row.get(key) or {}
    return validation.get("label")


def validation_stance(row: dict, key: str) -> str | None:
    validation = row.get(key) or {}
    return validation.get("stance")


def tier_ab_for_row(row: dict) -> tuple[str, str] | None:
    atom_label = validation_label(row, "atom_validation")
    astrosage_label = validation_label(row, "astrosage_validation")
    atom_stance = validation_stance(row, "atom_validation")
    astrosage_stance = validation_stance(row, "astrosage_validation")
    if atom_stance != "supports" or astrosage_stance != "supports":
        return None
    labels = {atom_label, astrosage_label}
    if labels == {"strict_support"}:
        return ("A", "high")
    if labels == {"strict_support", "adjacent_support"}:
        return ("B", "medium_needs_audit")
    return None


def build_tier_ab_manifest(rows: list[dict], args: argparse.Namespace, validator_path: Path) -> dict:
    tiered = []
    for row in rows:
        tier = tier_ab_for_row(row)
        if not tier:
            continue
        confidence_tier, confidence = tier
        row_copy = dict(row)
        row_copy["status"] = "validated_ready"
        row_copy["confidence_tier"] = confidence_tier
        row_copy["confidence"] = confidence
        row_copy["quality"] = {
            **(row.get("quality") if isinstance(row.get("quality"), dict) else {}),
            "confidence": confidence,
            "confidence_tier": confidence_tier,
        }
        tiered.append(row_copy)

    force_rows = parse_force_rows(args.force_rows)
    if force_rows:
        tiered = [row for row in tiered if (int(row["claim_id"]), row["arxiv_id"]) in force_rows]
        found = {(int(row["claim_id"]), row["arxiv_id"]) for row in tiered}
        missing = sorted(force_rows - found)
        if missing:
            raise SystemExit(f"--force-rows requested rows not found in Tier A/B validated_ready: {missing}")
    if args.limit:
        tiered = tiered[: args.limit]

    tier_a = [row for row in tiered if row["confidence_tier"] == "A"]
    tier_b = [row for row in tiered if row["confidence_tier"] == "B"]
    distinct_claims = sorted({row["claim_id"] for row in tiered})
    tier_a_distinct_claims = sorted({row["claim_id"] for row in tier_a})
    gate = {
        "first_batch_min_ready": 30,
        "first_batch_min_distinct_claims": 15,
        "first_batch_requires_full_manual_audit_precision": 0.95,
        "second_promotion_min_ready": 100,
        "second_promotion_min_distinct_claims": 40,
        "strict_support_only": False,
        "tier_ab_dry_run_only": True,
        "tier_a": "both raters strict_support with stance=supports; confidence=high",
        "tier_b": "one rater strict_support and one adjacent_support, both stance=supports; confidence=medium_needs_audit",
        "first_batch_signoff": "HwaO + Papa",
    }
    gate_passes_counts = len(tiered) >= gate["first_batch_min_ready"] and len(distinct_claims) >= gate["first_batch_min_distinct_claims"]
    return {
        "manifest_version": "arxiv_wiki_feed_v1_20260524_tier_ab_dry_run",
        "created_at": dt.datetime.now().isoformat(timespec="seconds"),
        "source_validator_path": str(validator_path),
        "dry_run": True,
        "apply_requested": False,
        "approved_by": args.approved_by,
        "promotion_gate": gate,
        "gate_passes_counts": gate_passes_counts,
        "count_gate_override": bool(force_rows),
        "override_reason": args.override_reason if force_rows else None,
        "forced_rows": sorted([{"claim_id": claim_id, "arxiv_id": arxiv_id} for claim_id, arxiv_id in force_rows], key=lambda r: (r["claim_id"], r["arxiv_id"])),
        "manual_signoff_required_before_apply": True,
        "validated_ready_count": len(tiered),
        "validated_ready_distinct_claim_count": len(distinct_claims),
        "tier_a_count": len(tier_a),
        "tier_b_count": len(tier_b),
        "tier_a_distinct_claim_count": len(tier_a_distinct_claims),
        "combined_distinct_claim_count": len(distinct_claims),
        "candidate_ids": [row.get("id") for row in tiered if row.get("id")],
        "rows": [
            {
                "claim_id": row["claim_id"],
                "arxiv_id": row["arxiv_id"],
                "title": row["paper_title_snapshot"],
                "confidence_tier": row["confidence_tier"],
                "confidence": row["confidence"],
                "quality": row.get("quality"),
                "validator_score": row.get("validator_score"),
                "validator_agreement": row.get("validator_agreement"),
                "summary": row.get("evidence_summary"),
                "candidate": row,
            }
            for row in tiered
        ],
        "promoted_evidence_ids": [],
    }


def build_v1_1_manifest(rows: list[dict], args: argparse.Namespace, validator_path: Path) -> dict:
    validated = []
    human_review = []
    drop_bucket = []
    cell_counts: dict[str, int] = {}
    for row in rows:
        atom = row.get("atom_validation") or {}
        astrosage = row.get("astrosage_validation") or {}
        atom_label = atom.get("label")
        astrosage_label = astrosage.get("label")
        atom_stance = atom.get("stance")
        astrosage_stance = astrosage.get("stance")
        cell_key = f"atom={atom_label}|astrosage={astrosage_label}"
        cell_counts[cell_key] = cell_counts.get(cell_key, 0) + 1

        if (
            (atom_label == "strict_support" and astrosage_label == "needs_human")
            or (atom_label == "needs_human" and astrosage_label == "strict_support")
        ):
            human_review.append(row)
            continue
        if atom_label == "strict_challenge" and astrosage_label == "adjacent_support":
            drop_bucket.append(row)
            continue
        labels = {atom_label, astrosage_label}
        if labels <= {"strict_support", "adjacent_support"} and "strict_support" in labels:
            if atom_stance != "challenges" and astrosage_stance != "challenges":
                row_copy = dict(row)
                row_copy["status"] = "validated_ready"
                row_copy["promotion_policy"] = "v1.1"
                row_copy["confidence"] = "medium_needs_audit" if labels == {"strict_support", "adjacent_support"} else "high"
                row_copy["confidence_tier"] = "B" if labels == {"strict_support", "adjacent_support"} else "A"
                validated.append(row_copy)

    force_rows = parse_force_rows(args.force_rows)
    if force_rows:
        validated = [row for row in validated if (int(row["claim_id"]), row["arxiv_id"]) in force_rows]
        found = {(int(row["claim_id"]), row["arxiv_id"]) for row in validated}
        missing = sorted(force_rows - found)
        if missing:
            raise SystemExit(f"--force-rows requested rows not found in v1.1 validated_ready: {missing}")
    if args.limit:
        validated = validated[: args.limit]

    distinct_claims = sorted({row["claim_id"] for row in validated})
    gate = {
        "first_batch_min_ready": 30,
        "first_batch_min_distinct_claims": 15,
        "first_batch_requires_full_manual_audit_precision": 0.95,
        "second_promotion_min_ready": 100,
        "second_promotion_min_distinct_claims": 40,
        "policy": "v1.1",
        "rule": "Both raters in {strict_support, adjacent_support}; at least one strict_support; no challenge stance.",
        "human_review": "strict_support paired with needs_human",
        "drop_bucket": "Atom strict_challenge paired with AstroSage adjacent_support",
        "first_batch_signoff": "HwaO + Papa",
    }
    gate_passes_counts = len(validated) >= gate["first_batch_min_ready"] and len(distinct_claims) >= gate["first_batch_min_distinct_claims"]
    return {
        "manifest_version": "arxiv_wiki_feed_v1_1_20260524_dry_run",
        "created_at": dt.datetime.now().isoformat(timespec="seconds"),
        "source_validator_path": str(validator_path),
        "dry_run": True,
        "apply_requested": False,
        "approved_by": args.approved_by,
        "promotion_gate": gate,
        "gate_passes_counts": gate_passes_counts,
        "count_gate_override": bool(force_rows),
        "override_reason": args.override_reason if force_rows else None,
        "forced_rows": sorted([{"claim_id": claim_id, "arxiv_id": arxiv_id} for claim_id, arxiv_id in force_rows], key=lambda r: (r["claim_id"], r["arxiv_id"])),
        "manual_signoff_required_before_apply": True,
        "validated_ready_count": len(validated),
        "validated_ready_distinct_claim_count": len(distinct_claims),
        "human_review_count": len(human_review),
        "drop_bucket_count": len(drop_bucket),
        "cell_counts": dict(sorted(cell_counts.items())),
        "unlock_counts": {
            "both_strict": sum(1 for row in validated if validation_label(row, "atom_validation") == "strict_support" and validation_label(row, "astrosage_validation") == "strict_support"),
            "atom_strict_astrosage_adjacent": sum(1 for row in validated if validation_label(row, "atom_validation") == "strict_support" and validation_label(row, "astrosage_validation") == "adjacent_support"),
            "atom_adjacent_astrosage_strict": sum(1 for row in validated if validation_label(row, "atom_validation") == "adjacent_support" and validation_label(row, "astrosage_validation") == "strict_support"),
        },
        "candidate_ids": [row.get("id") for row in validated if row.get("id")],
        "human_review_rows": [manifest_row(row, policy="v1.1_human_review") for row in human_review],
        "drop_bucket_rows": [manifest_row(row, policy="v1.1_drop") for row in drop_bucket],
        "rows": [manifest_row(row, policy="v1.1") for row in validated],
        "promoted_evidence_ids": [],
    }


def manifest_row(row: dict, policy: str) -> dict:
    return {
        "claim_id": row["claim_id"],
        "arxiv_id": row["arxiv_id"],
        "title": row["paper_title_snapshot"],
        "policy": policy,
        "confidence_tier": row.get("confidence_tier"),
        "confidence": row.get("confidence"),
        "quality": row.get("quality"),
        "validator_score": row.get("validator_score"),
        "validator_agreement": row.get("validator_agreement"),
        "summary": row.get("evidence_summary"),
        "atom_label": validation_label(row, "atom_validation"),
        "atom_stance": validation_stance(row, "atom_validation"),
        "astrosage_label": validation_label(row, "astrosage_validation"),
        "astrosage_stance": validation_stance(row, "astrosage_validation"),
        "candidate": row,
    }


def write_tier_b_audit_sample(manifest: dict, output_path: Path, sample_size: int = TIER_B_AUDIT_SAMPLE_SIZE) -> list[dict]:
    tier_b_rows = [item["candidate"] for item in manifest["rows"] if item.get("confidence_tier") == "B"]
    rng = random.Random(TIER_B_AUDIT_SAMPLE_SEED)
    sample = rng.sample(tier_b_rows, min(sample_size, len(tier_b_rows)))
    records = []
    for row in sample:
        atom = row.get("atom_validation") or {}
        astrosage = row.get("astrosage_validation") or {}
        records.append(
            {
                "claim_id": row["claim_id"],
                "arxiv_id": row["arxiv_id"],
                "confidence_tier": "B",
                "confidence": "medium_needs_audit",
                "claim_text": row.get("claim_text_snapshot"),
                "claim_section": row.get("claim_section_snapshot"),
                "paper_title": row.get("paper_title_snapshot"),
                "paper_abstract": row.get("paper_abstract_snapshot"),
                "paper_url": row.get("paper_url"),
                "atom_label": atom.get("label"),
                "atom_stance": atom.get("stance"),
                "atom_score": atom.get("score"),
                "atom_rationale": atom.get("rationale"),
                "atom_quoted_evidence_span": atom.get("quoted_evidence_span"),
                "astrosage_label": astrosage.get("label"),
                "astrosage_stance": astrosage.get("stance"),
                "astrosage_score": astrosage.get("score"),
                "astrosage_rationale": astrosage.get("rationale"),
                "astrosage_quoted_evidence_span": astrosage.get("quoted_evidence_span"),
            }
        )
    with output_path.open("w") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
    return records


def write_v1_1_sample(manifest: dict, output_path: Path, sample_size: int = V1_1_SAMPLE_SIZE) -> list[dict]:
    rows = [item["candidate"] for item in manifest["rows"]]
    rng = random.Random(V1_1_SAMPLE_SEED)
    sample = rng.sample(rows, min(sample_size, len(rows)))
    records = []
    for row in sample:
        atom = row.get("atom_validation") or {}
        astrosage = row.get("astrosage_validation") or {}
        records.append(
            {
                "claim_id": row["claim_id"],
                "arxiv_id": row["arxiv_id"],
                "confidence_tier": row.get("confidence_tier"),
                "confidence": row.get("confidence"),
                "claim_text": row.get("claim_text_snapshot"),
                "claim_section": row.get("claim_section_snapshot"),
                "paper_title": row.get("paper_title_snapshot"),
                "paper_abstract": row.get("paper_abstract_snapshot"),
                "paper_url": row.get("paper_url"),
                "atom_label": atom.get("label"),
                "atom_stance": atom.get("stance"),
                "atom_score": atom.get("score"),
                "atom_rationale": atom.get("rationale"),
                "atom_quoted_evidence_span": atom.get("quoted_evidence_span"),
                "astrosage_label": astrosage.get("label"),
                "astrosage_stance": astrosage.get("stance"),
                "astrosage_score": astrosage.get("score"),
                "astrosage_rationale": astrosage.get("rationale"),
                "astrosage_quoted_evidence_span": astrosage.get("quoted_evidence_span"),
            }
        )
    with output_path.open("w") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
    return records


def create_promotion_run(conn, first_row: dict, manifest: dict) -> tuple[int, str]:
    run_key = f"{Path(manifest['source_validator_path']).parent.name}_promotion_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    run_id = conn.execute(
        text(
            """
            INSERT INTO arxiv_wiki_feed_runs
                (run_key, page_id, page_slug, run_scope, paper_query, candidate_params,
                 validator_params, status, created_by, code_version, notes)
            VALUES
                (:run_key, :page_id, :page_slug, 'single_page_promotion_override',
                 CAST(:paper_query AS jsonb), CAST(:candidate_params AS jsonb),
                 CAST(:validator_params AS jsonb), 'promotion_started', 'tori', :code_version, :notes)
            RETURNING id
            """
        ),
        {
            "run_key": run_key,
            "page_id": first_row["page_id"],
            "page_slug": first_row["page_slug"],
            "paper_query": json.dumps({"source_validator_path": manifest["source_validator_path"]}),
            "candidate_params": json.dumps({"forced_rows": manifest.get("forced_rows", [])}),
            "validator_params": json.dumps({"validator_model_set": first_row.get("validator_model_set", [])}),
            "code_version": code_version(),
            "notes": "Manual HwaO+Papa count-gate override for arxiv wiki feed smoke test",
        },
    ).scalar_one()
    return int(run_id), run_key


def ensure_shadow_row(conn, row: dict, manifest: dict, run_id: int, run_key: str) -> int:
    candidate_id = conn.execute(
        text(
            """
            INSERT INTO arxiv_wiki_evidence_candidates
                (run_id, page_id, page_slug, claim_id, claim_text_snapshot,
                 claim_section_snapshot, arxiv_paper_id, arxiv_id, paper_title_snapshot,
                 paper_abstract_snapshot, paper_authors_snapshot, paper_year, paper_url,
                 candidate_rank, bm25_score, tfidf_score, claim_key_overlap,
                 matched_terms, candidate_source, status, validator_label, validator_score,
                 validator_agreement, validator_model_set, evidence_stance, evidence_summary,
                 quality, duplicate_evidence_id, promotion_batch_id, promotion_gate)
            VALUES
                (:run_id, :page_id, :page_slug, :claim_id, :claim_text_snapshot,
                 :claim_section_snapshot, :arxiv_paper_id, :arxiv_id, :paper_title_snapshot,
                 :paper_abstract_snapshot, :paper_authors_snapshot, :paper_year, :paper_url,
                 :candidate_rank, :bm25_score, :tfidf_score, :claim_key_overlap,
                 CAST(:matched_terms AS jsonb), :candidate_source, 'validated_ready',
                 :validator_label, :validator_score, :validator_agreement,
                 CAST(:validator_model_set AS jsonb), :evidence_stance, :evidence_summary,
                 :quality, :duplicate_evidence_id, :promotion_batch_id, 'hwao_papa_count_gate_override')
            RETURNING id
            """
        ),
        {
            **row,
            "run_id": run_id,
            "matched_terms": json.dumps(row.get("matched_terms", [])),
            "validator_model_set": json.dumps(row.get("validator_model_set", [])),
            "promotion_batch_id": run_key,
        },
    ).scalar_one()
    for key in ("atom_validation", "astrosage_validation"):
        validation = row.get(key) or {}
        if not validation:
            continue
        conn.execute(
            text(
                """
                INSERT INTO arxiv_wiki_evidence_validations
                    (candidate_id, run_id, model_name, host, prompt_version, label, stance,
                     score, claim_key_overlap_seen, rationale, quoted_evidence_span, failure_mode)
                VALUES
                    (:candidate_id, :run_id, :model_name, :host, :prompt_version, :label, :stance,
                     :score, :claim_key_overlap_seen, :rationale, :quoted_evidence_span, :failure_mode)
                """
            ),
            {
                "candidate_id": candidate_id,
                "run_id": run_id,
                "model_name": validation.get("model_name"),
                "host": validation.get("host"),
                "prompt_version": validation.get("prompt_version"),
                "label": validation.get("label"),
                "stance": validation.get("stance"),
                "score": validation.get("score") or 0.0,
                "claim_key_overlap_seen": row.get("claim_key_overlap"),
                "rationale": validation.get("rationale"),
                "quoted_evidence_span": validation.get("quoted_evidence_span"),
                "failure_mode": validation.get("failure_mode"),
            },
        )
    return int(candidate_id)


def promote(manifest: dict) -> list[int]:
    if not manifest.get("apply_requested") or not manifest.get("approved_by"):
        raise SystemExit("Production promotion requires --apply and --approved-by.")
    engine = db_engine()
    promoted = []
    with engine.begin() as conn:
        if not manifest["rows"]:
            return promoted
        run_id, run_key = create_promotion_run(conn, manifest["rows"][0]["candidate"], manifest)
        for item in manifest["rows"]:
            row = item["candidate"]
            duplicate = conn.execute(
                text("SELECT id FROM evidence WHERE claim_id=:claim_id AND arxiv_id=:arxiv_id LIMIT 1"),
                {"claim_id": row["claim_id"], "arxiv_id": row["arxiv_id"]},
            ).scalar()
            if duplicate:
                raise SystemExit(f"Duplicate evidence already exists for claim_id={row['claim_id']} arxiv_id={row['arxiv_id']}: evidence_id={duplicate}")
            candidate_id = ensure_shadow_row(conn, row, manifest, run_id, run_key)
            evidence_id = conn.execute(
                text(
                    """
                    INSERT INTO evidence
                        (claim_id, arxiv_id, url, title, authors, year, summary, stance,
                         quality, abstract, verified_at, source_channel, arxiv_verified,
                         arxiv_wiki_candidate_id, evidence_status, provenance)
                    VALUES
                        (:claim_id, :arxiv_id, :url, :title, :authors, :year, :summary, 'supports',
                         :quality, :abstract, now(), 'arxiv_wiki_feed_v1', true,
                         :candidate_id, 'production_active', CAST(:provenance AS jsonb))
                    RETURNING id
                    """
                ),
                {
                    "claim_id": row["claim_id"],
                    "arxiv_id": row["arxiv_id"],
                    "url": row.get("paper_url"),
                    "title": row["paper_title_snapshot"],
                    "authors": row.get("paper_authors_snapshot"),
                    "year": row.get("paper_year"),
                    "summary": row.get("evidence_summary"),
                    "quality": row.get("quality") or 0.8,
                    "abstract": row.get("paper_abstract_snapshot"),
                    "candidate_id": candidate_id,
                    "provenance": json.dumps(
                        {
                            "manifest_version": manifest["manifest_version"],
                            "source": "arxiv_wiki_feed_v1",
                            "approved_by": manifest["approved_by"],
                            "count_gate_override": manifest.get("count_gate_override", False),
                            "override_reason": manifest.get("override_reason"),
                            "source_validator_path": manifest["source_validator_path"],
                        }
                    ),
                },
            ).scalar_one()
            conn.execute(
                text(
                    """
                    UPDATE arxiv_wiki_evidence_candidates
                    SET status='promoted', promoted_evidence_id=:evidence_id, promoted_at=now(), updated_at=now()
                    WHERE id=:candidate_id
                    """
                ),
                {"evidence_id": evidence_id, "candidate_id": candidate_id},
            )
            promoted.append(int(evidence_id))
        conn.execute(
            text("UPDATE arxiv_wiki_feed_runs SET status='promoted', finished_at=now() WHERE id=:run_id"),
            {"run_id": run_id},
        )
    return promoted


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validator", type=Path)
    parser.add_argument("--dry-run", action="store_true", default=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--approved-by", help="Required for --apply; e.g. 'HwaO+Papa manifest <id>'")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--force-rows", help="Count-gate override, comma-separated claim_id:arxiv_id rows. Does not lower default gates.")
    parser.add_argument("--override-reason", help="Required explanation for --force-rows production override.")
    parser.add_argument("--policy", choices=["v1.0", "v1.1", "tier_ab"], default="v1.0", help="Promotion aggregation policy. Non-v1.0 policies are dry-run only.")
    parser.add_argument("--manifest-output", type=Path, help="Optional dry-run manifest output path.")
    args = parser.parse_args()
    if args.force_rows and not args.override_reason:
        raise SystemExit("--force-rows requires --override-reason.")
    if args.apply and args.policy != "v1.0":
        raise SystemExit("--apply is only supported for policy v1.0.")

    validator_path = args.validator or latest_artifact("validator.jsonl")
    rows = read_jsonl(validator_path)
    if args.apply:
        manifest = build_manifest(rows, args, validator_path)
        manifest_path = validator_path.parent / "promotion_manifest.json"
    elif args.policy == "v1.1":
        manifest = build_v1_1_manifest(rows, args, validator_path)
        manifest_path = validator_path.parent / "promotion_manifest_v1_1.json"
        sample_path = validator_path.parent / "promotion_manifest_v1_1_sample_20.jsonl"
        sample = write_v1_1_sample(manifest, sample_path)
        manifest["sample_path"] = str(sample_path)
        manifest["sample_count"] = len(sample)
    elif args.policy == "tier_ab":
        manifest = build_tier_ab_manifest(rows, args, validator_path)
        manifest_path = validator_path.parent / "promotion_manifest_tier_ab.json"
        sample_path = validator_path.parent / "tier_b_audit_sample_20.jsonl"
        sample = write_tier_b_audit_sample(manifest, sample_path)
        manifest["tier_b_audit_sample_path"] = str(sample_path)
        manifest["tier_b_audit_sample_count"] = len(sample)
    else:
        manifest = build_manifest(rows, args, validator_path)
        manifest_path = validator_path.parent / "promotion_manifest.json"
    if args.manifest_output:
        if args.apply:
            raise SystemExit("--manifest-output is only supported for dry-run manifests.")
        manifest_path = args.manifest_output

    if args.apply:
        promoted = promote(manifest)
        manifest["promoted_evidence_ids"] = promoted
        manifest["dry_run"] = False

    write_json(manifest_path, manifest)
    print(
        json.dumps(
            {
                "manifest_path": str(manifest_path),
                "validated_ready_count": manifest["validated_ready_count"],
                "distinct_claims": manifest["validated_ready_distinct_claim_count"],
                "tier_a_count": manifest.get("tier_a_count"),
                "tier_b_count": manifest.get("tier_b_count"),
                "human_review_count": manifest.get("human_review_count"),
                "drop_bucket_count": manifest.get("drop_bucket_count"),
                "tier_b_audit_sample_path": manifest.get("tier_b_audit_sample_path"),
                "sample_path": manifest.get("sample_path"),
                "applied": args.apply,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
