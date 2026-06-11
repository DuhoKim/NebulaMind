#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import logging
import sys
from pathlib import Path

from sqlalchemy import text

sys.path.insert(0, str(Path(__file__).resolve().parent))
from arxiv_wiki_feed_common import code_version, db_engine, read_jsonl

logger = logging.getLogger(__name__)
MANIFEST_VERSION = "arxiv_wiki_feed_v2_phase3_promoter_v1"
DEFAULT_SOURCE_CHANNEL = "arxiv_wiki_feed_v2_element"


def clean_arxiv_id(value):
    return str(value or "").strip()


def enrich_labels(labels, *, page, claims, papers, source_run_key, approved_by, source_channel):
    rows = []
    schema_drift = []
    for label in labels:
        claim_id = int(label["claim_id"])
        arxiv_id = clean_arxiv_id(label.get("paper_id") or label.get("arxiv_id"))
        claim = claims.get(claim_id)
        paper = papers.get(arxiv_id)
        if not claim or not paper:
            schema_drift.append({"claim_id": claim_id, "arxiv_id": arxiv_id, "reason": "missing_claim_or_paper"})
            continue
        rows.append(
            {
                **label,
                "claim_id": claim_id,
                "arxiv_id": arxiv_id,
                "page_id": page["id"],
                "page_slug": page["slug"],
                "claim_text_snapshot": claim.get("text"),
                "paper_title": paper.get("title"),
                "paper_abstract": paper.get("abstract"),
                "paper_authors": paper.get("authors"),
                "paper_submitted": paper.get("submitted"),
                "source_run_key": source_run_key,
                "approved_by": approved_by,
                "source_channel": source_channel,
            }
        )
    return rows, schema_drift


def collapse_promotion_units(enriched_rows, existing_evidence):
    grouped = {}
    for row in enriched_rows:
        grouped.setdefault((row["claim_id"], row["arxiv_id"]), []).append(row)

    rows = []
    held_back = []
    for key in sorted(grouped):
        claim_id, arxiv_id = key
        elements = sorted(grouped[key], key=lambda r: str(r.get("element_id") or ""))
        first = elements[0]
        element_support = [
            {
                "element_id": row.get("element_id"),
                "element_label": row.get("label"),
                "element_reason": row.get("reason"),
                "prompt_version": row.get("prompt_version"),
            }
            for row in elements
        ]
        row = {
            "claim_id": claim_id,
            "arxiv_id": arxiv_id,
            "label": "citable",
            "source_section": first.get("section"),
            "target_section": first.get("target_section"),
            "target_section_title": first.get("target_section_title"),
            "element_ids": [item["element_id"] for item in element_support],
            "claim_text_snapshot": first.get("claim_text_snapshot"),
            "paper_title": first.get("paper_title"),
            "paper_abstract": first.get("paper_abstract"),
            "paper_authors": first.get("paper_authors"),
            "proposed_source_channel": first.get("source_channel", DEFAULT_SOURCE_CHANNEL),
            "provenance": {
                "source": "arxiv_wiki_feed_v2_phase3",
                "source_run_key": first.get("source_run_key"),
                "target_section": first.get("target_section"),
                "element_ids": [item["element_id"] for item in element_support],
                "element_support": element_support,
                "approved_by": first.get("approved_by"),
                "manifest_version": MANIFEST_VERSION,
            },
        }
        existing = existing_evidence.get(key)
        if existing:
            held_back.append(
                {
                    **row,
                    "existing_evidence_id": existing.get("id"),
                    "existing_source_channel": existing.get("source_channel"),
                    "held_back_reason": "existing_evidence_for_claim_arxiv",
                }
            )
        else:
            rows.append(row)
    return rows, held_back


def build_manifest(
    *,
    page_slug,
    section,
    labels_path,
    source_run_key,
    apply_requested,
    approved_by,
    min_rows,
    min_distinct_claims,
    min_rows_override,
    source_channel,
    rows,
    held_back_rows,
    schema_drift,
    rollback_manifest_path,
    audited_strict_precision=1.0,
    off_domain_promoted_count=0,
):
    distinct_claims = len({row["claim_id"] for row in rows})
    count_gate = len(rows) >= min_rows and distinct_claims >= min_distinct_claims
    if min_rows_override:
        count_gate = True
    precision_gate = float(audited_strict_precision) >= 0.95
    off_domain_gate = int(off_domain_promoted_count) == 0
    return {
        "manifest_version": MANIFEST_VERSION,
        "page_slug": page_slug,
        "target_section": section,
        "source_run_key": source_run_key,
        "source_labels_path": str(labels_path),
        "dry_run": not apply_requested,
        "apply_requested": apply_requested,
        "approved_by": approved_by,
        "promotion_gate": {
            "min_rows": min_rows,
            "min_distinct_claims": min_distinct_claims,
            "min_audited_strict_precision": 0.95,
            "off_domain_promoted_max": 0,
        },
        "gate_passes_counts": count_gate,
        "gate_passes_precision": precision_gate,
        "gate_passes_off_domain": off_domain_gate,
        "gate_passes": count_gate and precision_gate and off_domain_gate,
        "force_gate_override": min_rows_override,
        "audited_strict_precision": audited_strict_precision,
        "off_domain_promoted_count": off_domain_promoted_count,
        "raw_element_pair_count": sum(len(row.get("element_ids") or []) for row in rows) + len(held_back_rows),
        "validated_element_pair_count": len(rows),
        "distinct_claim_count": distinct_claims,
        "duplicate_existing_count": len(held_back_rows),
        "schema_drift": schema_drift,
        "rows": rows,
        "held_back_rows": held_back_rows,
        "rollback_manifest_path": str(rollback_manifest_path),
        "source_channel": source_channel,
    }


def require_apply_allowed(manifest):
    if not manifest.get("apply_requested"):
        return
    if not manifest.get("approved_by"):
        raise SystemExit("apply requires approved_by")
    if not manifest.get("gate_passes_counts"):
        raise SystemExit("count gate failed")
    if not manifest.get("gate_passes_precision", True):
        raise SystemExit("audited precision gate failed")
    if not manifest.get("gate_passes_off_domain", True):
        raise SystemExit("off-domain gate failed")


def apply_manifest(manifest, *, source_channel, rollback_path, engine=None):
    require_apply_allowed(manifest)
    engine = engine or db_engine()
    rollback = {
        "status": "prepared_before_db_inserts",
        "inserted_evidence_ids": [],
        "inserted_candidate_ids": [],
        "feed_run_id": None,
    }
    rollback_path.parent.mkdir(parents=True, exist_ok=True)
    rollback_path.write_text(json.dumps(rollback, indent=2, sort_keys=True), encoding="utf-8")
    with engine.begin() as conn:
        run_id = conn.execute(
            text(
                """
                INSERT INTO arxiv_wiki_feed_runs
                    (run_key, page_slug, run_scope, paper_query, candidate_params,
                     validator_params, status, created_by, code_version, notes)
                VALUES
                    (:run_key, :page_slug, 'v2_phase3_element_promotion',
                     '{}', '{}', '{}', 'applied', :created_by, :code_version, :notes)
                RETURNING id
                """
            ),
            {
                "run_key": f"{manifest['source_run_key']}_phase3_apply_{dt.datetime.utcnow().timestamp()}",
                "page_slug": manifest["page_slug"],
                "created_by": manifest.get("approved_by"),
                "code_version": code_version(),
                "notes": manifest.get("force_gate_override") or "",
            },
        ).scalar_one()
        rollback["feed_run_id"] = run_id
        for row in manifest["rows"]:
            candidate_id = conn.execute(
                text(
                    """
                    INSERT INTO arxiv_wiki_evidence_candidates
                        (run_id, page_slug, claim_id, claim_text_snapshot,
                         arxiv_id, paper_title_snapshot, status)
                    VALUES
                        (:run_id, :page_slug, :claim_id, :claim_text_snapshot,
                         :arxiv_id, :paper_title_snapshot, 'promoted')
                    RETURNING id
                    """
                ),
                {
                    "run_id": run_id,
                    "page_slug": manifest["page_slug"],
                    "claim_id": row["claim_id"],
                    "claim_text_snapshot": row.get("claim_text_snapshot"),
                    "arxiv_id": row["arxiv_id"],
                    "paper_title_snapshot": row.get("paper_title"),
                },
            ).scalar_one()
            rollback["inserted_candidate_ids"].append(candidate_id)
            evidence_id = conn.execute(
                text(
                    """
                    INSERT INTO evidence
                        (claim_id, arxiv_id, url, title, authors, summary, stance,
                         quality, abstract, verified_at, source_channel,
                         arxiv_wiki_candidate_id, evidence_status, provenance)
                    VALUES
                        (:claim_id, :arxiv_id, :url, :title, :authors, '', 'supports',
                         1.0, :abstract, NOW(), :source_channel,
                         :candidate_id, 'active', :provenance)
                    RETURNING id
                    """
                ),
                {
                    "claim_id": row["claim_id"],
                    "arxiv_id": row["arxiv_id"],
                    "url": f"https://arxiv.org/abs/{row['arxiv_id']}",
                    "title": row.get("paper_title") or "",
                    "authors": row.get("paper_authors") or "",
                    "abstract": row.get("paper_abstract") or "",
                    "source_channel": source_channel,
                    "candidate_id": candidate_id,
                    "provenance": json.dumps(row.get("provenance") or {}),
                },
            ).scalar_one()
            rollback["inserted_evidence_ids"].append(evidence_id)
        conn.execute(
            text("UPDATE arxiv_wiki_evidence_candidates SET promotion_batch_id=:batch WHERE run_id=:run_id"),
            {"batch": manifest["source_run_key"], "run_id": run_id},
        )
    rollback["status"] = "applied"
    rollback_path.write_text(json.dumps(rollback, indent=2, sort_keys=True), encoding="utf-8")
    return rollback

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--page-slug", required=True)
    parser.add_argument("--section", required=True)
    parser.add_argument("--labels", required=True, type=Path)
    parser.add_argument("--source-run-key", required=True)
    parser.add_argument("--manifest-output", required=True, type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--approved-by", help="Required if --apply is set")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--force-element-rows")
    parser.add_argument("--min-rows", type=int, default=30)
    parser.add_argument("--min-distinct-claims", type=int, default=15)
    parser.add_argument("--source-channel", default="arxiv_wiki_feed_v2_element")
    parser.add_argument("--force-gate-override", help="Reason for overriding count gate")
    return parser.parse_args()

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    args = parse_args()
    
    if args.apply and not args.approved_by:
        raise SystemExit("Error: --approved-by is required when --apply is set.")
    
    # Load labels
    labels = read_jsonl(args.labels)
    citable_labels = [L for L in labels if L.get("label") == "citable" and L.get("target_section") == args.section]
    
    # Connect DB
    engine = db_engine()
    
    # 1. Enrich labels and dedup
    # We need claim snapshot and paper details.
    # Actually, the paper details come from `arxiv_papers` table.
    
    # Query all claims
    claim_ids = list({L["claim_id"] for L in citable_labels})
    paper_ids = list({L["paper_id"] for L in citable_labels})
    
    claims_map = {}
    papers_map = {}
    existing_evidence = {}
    
    with engine.begin() as conn:
        if claim_ids:
            claim_rows = conn.execute(
                text("SELECT id, text FROM claims WHERE id IN :ids"),
                {"ids": tuple(claim_ids)}
            ).fetchall()
            for r in claim_rows:
                claims_map[r.id] = r.text
        
        if paper_ids:
            paper_rows = conn.execute(
                text("SELECT arxiv_id, title, abstract, authors, submitted FROM arxiv_papers WHERE arxiv_id IN :ids"),
                {"ids": tuple(paper_ids)}
            ).fetchall()
            for r in paper_rows:
                papers_map[r.arxiv_id] = {
                    "title": r.title,
                    "abstract": r.abstract,
                    "authors": r.authors,
                    "submitted": r.submitted
                }
        
        # Check existing evidence
        if claim_ids and paper_ids:
            existing_ev_rows = conn.execute(
                text("SELECT id, claim_id, arxiv_id, source_channel FROM evidence WHERE claim_id IN :cids AND arxiv_id IN :pids"),
                {"cids": tuple(claim_ids), "pids": tuple(paper_ids)}
            ).fetchall()
            for r in existing_ev_rows:
                existing_evidence[(r.claim_id, r.arxiv_id)] = {
                    "id": r.id,
                    "source_channel": r.source_channel
                }
                
        # Get page id
        page_res = conn.execute(
            text("SELECT id FROM wiki_pages WHERE slug = :slug"),
            {"slug": args.page_slug}
        ).fetchone()
        page_id = page_res.id if page_res else None

    # Group by (claim_id, arxiv_id)
    grouped = {}
    for L in citable_labels:
        key = (L["claim_id"], L["paper_id"])
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(L)
        
    force_pairs = set()
    if args.force_element_rows:
        for item in args.force_element_rows.split(","):
            if not item.strip(): continue
            parts = item.split(":")
            if len(parts) == 3:
                # claim_id:element_id:paper_id
                force_pairs.add((int(parts[0]), parts[2]))
            
    # Prepare rows
    manifest_rows = []
    held_back_rows = []
    raw_element_pair_count = len(citable_labels)
    duplicate_existing_count = 0
    
    # Sort keys for deterministic output
    for key in sorted(grouped.keys()):
        claim_id, arxiv_id = key
        elements = grouped[key]
        
        if force_pairs and key not in force_pairs:
            continue
            
        paper_info = papers_map.get(arxiv_id, {})
        claim_text = claims_map.get(claim_id, "")
        
        # Provenance payload
        element_ids = [e["element_id"] for e in elements]
        element_support = [
            {
                "element_id": e["element_id"],
                "element_label": e["label"],
                "element_reason": e.get("reason"),
                "prompt_version": e.get("prompt_version")
            } for e in elements
        ]
        
        provenance = {
            "source": "arxiv_wiki_feed_v2_phase3",
            "source_run_key": args.source_run_key,
            "target_section": args.section,
            "element_ids": element_ids,
            "element_support": element_support,
            "approved_by": args.approved_by,
            "manifest_version": "arxiv_wiki_feed_v2_phase3_promoter_v1"
        }
        
        row_dict = {
            "claim_id": claim_id,
            "arxiv_id": arxiv_id,
            "label": "citable", # aggregated
            "source_section": elements[0].get("section"),
            "target_section": args.section,
            "target_section_title": elements[0].get("target_section_title"),
            "astrosage_reason": elements[0].get("reason"),
            "claim_text_snapshot": claim_text,
            "element_text": "", # or combine?
            "paper_title": paper_info.get("title"),
            "paper_abstract": paper_info.get("abstract"),
            "proposed_source_channel": args.source_channel,
            "provenance": provenance
        }
        
        if key in existing_evidence:
            duplicate_existing_count += 1
            row_dict["existing_evidence_id"] = existing_evidence[key]["id"]
            held_back_rows.append(row_dict)
        else:
            manifest_rows.append(row_dict)

    if args.limit:
        manifest_rows = manifest_rows[:args.limit]

    distinct_claims = len(set(r["claim_id"] for r in manifest_rows))
    validated_element_pair_count = len(manifest_rows)

    gate_passes = (validated_element_pair_count >= args.min_rows and distinct_claims >= args.min_distinct_claims)
    
    if args.force_gate_override:
        gate_passes = True

    gate = {
        "min_rows": args.min_rows,
        "min_distinct_claims": args.min_distinct_claims,
    }

    manifest = {
        "manifest_version": "arxiv_wiki_feed_v2_phase3_promoter_v1",
        "page_slug": args.page_slug,
        "target_section": args.section,
        "source_run_key": args.source_run_key,
        "source_labels_path": str(args.labels),
        "dry_run": not args.apply,
        "apply_requested": args.apply,
        "approved_by": args.approved_by,
        "promotion_gate": gate,
        "gate_passes_counts": gate_passes,
        "force_gate_override": args.force_gate_override,
        "raw_element_pair_count": raw_element_pair_count,
        "validated_element_pair_count": validated_element_pair_count,
        "distinct_claim_count": distinct_claims,
        "duplicate_existing_count": duplicate_existing_count,
        "rows": manifest_rows,
        "held_back_rows": held_back_rows,
        "rollback_manifest_path": str(args.manifest_output.with_name(args.manifest_output.stem + "_rollback.json")) if args.apply else None
    }
    
    with open(args.manifest_output, "w") as f:
        json.dump(manifest, f, indent=2)

    logger.info(f"Manifest written to {args.manifest_output}")
    logger.info(f"Raw citable element pairs: {raw_element_pair_count}")
    logger.info(f"Deduped claim-paper promotion count: {validated_element_pair_count}")
    logger.info(f"Distinct claims: {distinct_claims}")
    logger.info(f"Duplicate/Held back: {duplicate_existing_count}")
    logger.info(f"Gate passes: {gate_passes}")

    if not args.apply:
        return
        
    if not gate_passes:
        raise SystemExit("Gate failed, and no override provided. Aborting apply.")

    # APPLY
    rollback_manifest = {"inserted_evidence_ids": [], "inserted_candidate_ids": [], "run_id": None}
    
    with engine.begin() as conn:
        # Insert run
        run_res = conn.execute(
            text("""
            INSERT INTO arxiv_wiki_feed_runs
                (run_key, page_id, page_slug, run_scope, paper_query, candidate_params,
                 validator_params, status, created_by, code_version, notes)
            VALUES
                (:run_key, :page_id, :page_slug, 'v2_phase3_section_promotion', '{}', '{}',
                 '{}', 'applied', :created_by, :code_version, :notes)
            RETURNING id
            """),
            {
                "run_key": args.source_run_key + f"_phase3_apply_{dt.datetime.utcnow().timestamp()}",
                "page_id": page_id,
                "page_slug": args.page_slug,
                "created_by": args.approved_by,
                "code_version": code_version(),
                "notes": args.force_gate_override or ""
            }
        )
        run_id = run_res.fetchone()[0]
        rollback_manifest["run_id"] = run_id
        
        for r in manifest_rows:
            # Insert candidate shadow row
            cand_res = conn.execute(
                text("""
                INSERT INTO arxiv_wiki_evidence_candidates
                    (run_id, page_id, page_slug, claim_id, claim_text_snapshot,
                     claim_section_snapshot, arxiv_paper_id, arxiv_id, paper_title_snapshot,
                     status, confidence_tier, evidence_summary, created_at, updated_at)
                VALUES
                    (:run_id, :page_id, :page_slug, :claim_id, :claim_text,
                     :claim_section, :arxiv_paper_id, :arxiv_id, :paper_title,
                     'promoted', 'A', '', NOW(), NOW())
                RETURNING id
                """),
                {
                    "run_id": run_id,
                    "page_id": page_id,
                    "page_slug": args.page_slug,
                    "claim_id": r["claim_id"],
                    "claim_text": r["claim_text_snapshot"],
                    "claim_section": r["source_section"],
                    "arxiv_paper_id": None, # or look up ID in arxiv_papers
                    "arxiv_id": r["arxiv_id"],
                    "paper_title": r["paper_title"]
                }
            )
            cand_id = cand_res.fetchone()[0]
            rollback_manifest["inserted_candidate_ids"].append(cand_id)
            
            paper_info = papers_map.get(r["arxiv_id"], {})
            year = None
            if paper_info.get("submitted"):
                year = paper_info["submitted"].year
            
            # Insert evidence
            ev_res = conn.execute(
                text("""
                INSERT INTO evidence
                    (claim_id, arxiv_id, url, title, authors, year, summary, stance,
                     quality, abstract, verified_at, source_channel, arxiv_verified,
                     arxiv_wiki_candidate_id, evidence_status, provenance)
                VALUES
                    (:claim_id, :arxiv_id, :url, :title, :authors, :year, '', 'supports',
                     1.0, :abstract, NOW(), :source_channel, true,
                     :cand_id, 'production_active', :provenance)
                RETURNING id
                """),
                {
                    "claim_id": r["claim_id"],
                    "arxiv_id": r["arxiv_id"],
                    "url": f"https://arxiv.org/abs/{r['arxiv_id']}",
                    "title": paper_info.get("title", ""),
                    "authors": paper_info.get("authors", ""),
                    "year": year,
                    "abstract": paper_info.get("abstract", ""),
                    "source_channel": args.source_channel,
                    "cand_id": cand_id,
                    "provenance": json.dumps(r["provenance"])
                }
            )
            ev_id = ev_res.fetchone()[0]
            rollback_manifest["inserted_evidence_ids"].append(ev_id)
            
    with open(manifest["rollback_manifest_path"], "w") as f:
        json.dump(rollback_manifest, f, indent=2)
    logger.info(f"Apply complete. Rollback manifest: {manifest['rollback_manifest_path']}")

if __name__ == "__main__":
    main()
