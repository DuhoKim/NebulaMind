#!/usr/bin/env python3
"""Write a markdown report for the arXiv -> wiki evidence feed dry run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from arxiv_wiki_feed_common import REPORT_PATH, latest_artifact, read_jsonl


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path)
    parser.add_argument("--output", type=Path, default=REPORT_PATH)
    args = parser.parse_args()

    if args.run_dir:
        run_dir = args.run_dir
    else:
        run_dir = latest_artifact("promotion_manifest.json").parent

    build_meta = load_json(run_dir / "build_candidates_meta.json")
    validate_summary = load_json(run_dir / "validate_summary.json") if (run_dir / "validate_summary.json").exists() else {}
    manifest = load_json(run_dir / "promotion_manifest.json") if (run_dir / "promotion_manifest.json").exists() else {}
    candidates = read_jsonl(run_dir / "candidates.jsonl") if (run_dir / "candidates.jsonl").exists() else []
    validations = read_jsonl(run_dir / "validator.jsonl") if (run_dir / "validator.jsonl").exists() else []

    lines = [
        "# Arxiv Wiki Evidence Feed v1 — galaxy-evolution dry run",
        "",
        f"- Run key: `{build_meta.get('run_key')}`",
        f"- Page: `{build_meta.get('page', {}).get('slug')}` (id {build_meta.get('page', {}).get('id')})",
        f"- Artifact directory: `{run_dir}`",
        f"- Candidate JSONL: `{run_dir / 'candidates.jsonl'}`",
        f"- Validator JSONL: `{run_dir / 'validator.jsonl'}`",
        f"- Promotion manifest: `{run_dir / 'promotion_manifest.json'}`",
        "",
        "## Candidate Build",
        "",
        f"- Page claims: {build_meta.get('counts', {}).get('page_claims', 0)}",
        f"- Eligible arXiv papers: {build_meta.get('counts', {}).get('eligible_papers', 0)}",
        f"- Candidate pairs: {build_meta.get('counts', {}).get('candidate_pairs', len(candidates))}",
        f"- Distinct claims covered by candidates: {build_meta.get('counts', {}).get('distinct_claims', 0)}",
        f"- Existing production duplicates excluded/flagged: {build_meta.get('counts', {}).get('duplicate_existing', 0)}",
        "",
        "## Validation",
        "",
        f"- Validated candidates: {validate_summary.get('validated_count', len(validations))}",
        f"- Final status counts: `{json.dumps(validate_summary.get('final_status_counts', {}), sort_keys=True)}`",
        f"- Final label counts: `{json.dumps(validate_summary.get('final_label_counts', {}), sort_keys=True)}`",
        f"- Atom label counts: `{json.dumps(validate_summary.get('atom_label_counts', {}), sort_keys=True)}`",
        f"- AstroSage label counts: `{json.dumps(validate_summary.get('astrosage_label_counts', {}), sort_keys=True)}`",
        f"- Atom/AstroSage agreement rate: {validate_summary.get('atom_astrosage_agreement_rate', 0.0)}",
        "",
        "## Promotion Manifest",
        "",
        f"- Dry run: {manifest.get('dry_run', True)}",
        f"- Validated-ready rows: {manifest.get('validated_ready_count', 0)}",
        f"- Distinct claims covered by validated-ready rows: {manifest.get('validated_ready_distinct_claim_count', 0)}",
        f"- Count gate passes: {manifest.get('gate_passes_counts', False)}",
        f"- Sign-off required: {manifest.get('manual_signoff_required_before_apply', True)}",
        "",
        "## V1 Policy Notes",
        "",
        "- Strict support only is eligible in v1.",
        "- Strict challenge is annotate-only/deferred to v1.1.",
        "- Rakon adjudication is annotation-only; no solo-Rakon promotion.",
        "- No production evidence rows are written by this dry run.",
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"report_path": str(args.output), "run_dir": str(run_dir)}, indent=2))


if __name__ == "__main__":
    main()
