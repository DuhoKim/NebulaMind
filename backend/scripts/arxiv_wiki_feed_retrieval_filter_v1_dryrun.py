#!/usr/bin/env python3
"""Run retrieval filter v1 calibration as an artifact-only dry-run."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from retrieval_filter_v1 import (
    attach_candidate_metadata,
    calibrate_section,
    filtered_row_to_dict,
    load_taxonomy,
    read_jsonl,
    summarize_rows,
    write_json,
)


DEFAULT_SPEC = Path(
    "/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/"
    "arxiv_wiki_feed_v2_phase2_diagnostic_followups_20260526T063415Z/"
    "RETRIEVAL_FILTER_SPEC_size_evolution_v1.md"
)
DEFAULT_LABELS = Path(
    "/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/"
    "arxiv_wiki_feed_v2_phase2_unclear_retry_20260526T040155Z/"
    "LABELS_AFTER_RETRY.jsonl"
)
DEFAULT_ELEMENT_PAIRS = Path(
    "/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/"
    "arxiv_wiki_feed_v2_phase2_element_validator_20260525T005117Z/"
    "element_candidate_pairs.jsonl"
)
DEFAULT_CANDIDATES = Path(
    "/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed/"
    "arxiv_wiki_feed_v1_galaxy_evolution_20260524_120421/"
    "candidates.jsonl"
)
DEFAULT_TAXONOMY = Path(__file__).with_name("retrieval_filter_v1_taxonomy.json")
DEFAULT_OUTPUT_DIR = Path(
    "/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/"
    "arxiv_wiki_feed_v2_retrieval_filter_v1_dryrun_20260526T081400Z"
)


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(value) for value in row) + " |")
    return "\n".join(lines)


def pct(value: float) -> str:
    return f"{value * 100:.1f}%"


def label_counts_text(counts: dict[str, int]) -> str:
    return ", ".join(f"{key}={value}" for key, value in sorted(counts.items())) or "-"


def build_reports(
    output_dir: Path,
    spec_path: Path,
    labels_path: Path,
    element_pairs_path: Path,
    candidates_path: Path,
    taxonomy_path: Path,
    section_results: dict[str, dict[str, Any]],
    summary: dict[str, Any],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    before_after_rows = []
    dropped_rows = []
    report_rows = []
    for section, result in section_results.items():
        section_summary = summary["sections"][section]
        projected_pp_reduction = (
            section_summary["before_off_domain_share"] - section_summary["after_off_domain_share"]
        ) * 100.0
        before_after_rows.append(
            [
                section,
                section_summary["before_total"],
                section_summary["after_total"],
                f"{section_summary['before_total'] - section_summary['after_total']} ({pct(section_summary['candidate_drop_rate'])})",
                pct(section_summary["before_off_domain_share"]),
                pct(section_summary["after_off_domain_share"]),
                f"{projected_pp_reduction:.1f} pp",
                pct(section_summary["citable_retention"]),
                pct(section_summary["off_domain_reduction"]),
            ]
        )
        for row in result["rows"]:
            if not row.dropped:
                continue
            dropped_rows.append(
                [
                    section,
                    row.row.get("claim_id"),
                    row.row.get("element_id"),
                    row.paper_id,
                    row.label,
                    ", ".join(row.tags) or "-",
                    row.combined_score,
                    row.final_score,
                    ", ".join(row.drop_reasons),
                ]
            )
        report_rows.append(
            [
                section,
                label_counts_text(section_summary["before_labels"]),
                label_counts_text(section_summary["after_labels"]),
                ", ".join(result["off_domain_enriched_tags"]) or "-",
                ", ".join(result["suppressed_papers"][:8]) or "-",
                json.dumps(result["thresholds"], sort_keys=True),
            ]
        )

    impl_notes = f"""# Retrieval Filter v1 Implementation Notes

Source spec: `{spec_path}`

This dry-run is artifact-only. It reads labeled rows and candidate metadata from JSONL files, performs no DB writes, and makes no model calls.

## Inputs

- Labels: `{labels_path}`
- Element candidate metadata: `{element_pairs_path}`
- Existing candidate metadata: `{candidates_path}`
- Taxonomy config: `{taxonomy_path}`

## Mechanical Stages

1. Lexical candidate metadata tagger: tags are extracted from paper title and abstract using the config-driven taxonomy in `{taxonomy_path}`. The code path does not carry a hardcoded section or page enum.
2. Derived positive section terms: each section derives positive terms from currently `citable` rows against `off_domain` rows. Terms are not hardcoded per section.
3. Off-domain enriched tag downweight and page-local paper suppression: tags with section-local off-domain enrichment and zero citable support are downweighted. Papers recurring at least three times as off-domain with zero citable rows in that section are suppressed for this calibration run only.
4. Score gate: lexical/context overlap and citable-term support are combined. The keep floor is the section-local minimum citable combined score, chosen to preserve recall in a pre-AstroSage gate; off-domain 80th percentile is used only to moderate neighboring-domain downweights.

## Page-Agnostic Enforcement

- The dry-run groups by `target_section` from the input artifact and never branches on a specific section slug.
- Section terms, tag enrichment, score thresholds, and paper suppression are all derived from page-local labeled rows.
- Paper suppression is section/page-local calibration state, not a global blacklist.

## Non-goals

- No production retrieval code is changed.
- No database tables are read or mutated.
- No AstroSage, Ollama, or API model calls are made.
"""

    before_after = "# Retrieval Filter v1 Before/After Table\n\n" + md_table(
        [
            "Section",
            "Before rows",
            "After rows",
            "Dropped rows",
            "Before off-domain",
            "After off-domain",
            "Projected off-domain reduction",
            "Citable retention",
            "Off-domain dropped",
        ],
        before_after_rows,
    )
    before_after += "\n\n## Dropped Candidate Rows\n\n"
    before_after += md_table(
        [
            "Section",
            "Claim",
            "Element",
            "Paper",
            "Label",
            "Tags",
            "Combined score",
            "Final score",
            "Drop reasons",
        ],
        dropped_rows,
    )

    dry_run_report = "# Retrieval Filter v1 Dry-Run Report\n\n"
    dry_run_report += md_table(
        [
            "Section",
            "Before labels",
            "After labels",
            "Off-domain enriched tags",
            "Suppressed papers",
            "Thresholds",
        ],
        report_rows,
    )
    dry_run_report += "\n\n## Size Evolution Acceptance Check\n\n"
    size = summary["sections"].get("size_evolution", {})
    dry_run_report += "\n".join(
        [
            f"- Off-domain share: {pct(size.get('before_off_domain_share', 0.0))} -> {pct(size.get('after_off_domain_share', 0.0))}",
            f"- Citable retention: {pct(size.get('citable_retention', 0.0))}",
            f"- `2512.18276v1` suppressed: {summary['checks']['size_evolution_2512_18276v1_suppressed']}",
        ]
    )

    (output_dir / "RETRIEVAL_FILTER_V1_IMPL_NOTES.md").write_text(impl_notes, encoding="utf-8")
    (output_dir / "BEFORE_AFTER_TABLE.md").write_text(before_after + "\n", encoding="utf-8")
    (output_dir / "DRY_RUN_REPORT.md").write_text(dry_run_report + "\n", encoding="utf-8")
    write_json(output_dir / "summary.json", summary)
    with (output_dir / "FILTERED_ROWS.jsonl").open("w", encoding="utf-8") as handle:
        for result in section_results.values():
            for row in result["rows"]:
                handle.write(json.dumps(filtered_row_to_dict(row), ensure_ascii=False, sort_keys=True) + "\n")


def run(args: argparse.Namespace) -> dict[str, Any]:
    labels = read_jsonl(args.labels)
    element_pairs = read_jsonl(args.element_pairs)
    candidates = read_jsonl(args.candidates)
    taxonomy = load_taxonomy(args.taxonomy)
    enriched = attach_candidate_metadata(labels, element_pairs, candidates)

    by_section: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in enriched:
        by_section[str(row.get("target_section") or "unknown")].append(row)

    section_results: dict[str, dict[str, Any]] = {}
    all_filtered = []
    for section in sorted(by_section):
        result = calibrate_section(by_section[section], section, taxonomy=taxonomy)
        section_results[section] = result
        all_filtered.extend(result["rows"])

    sections_summary = {
        section: summarize_rows(result["rows"])
        for section, result in section_results.items()
    }
    overall = summarize_rows(all_filtered)
    size_rows = section_results.get("size_evolution", {}).get("rows", [])
    target_rows = [
        row
        for row in size_rows
        if row.paper_id == "2512.18276v1"
    ]
    target_suppressed = bool(target_rows) and all(row.dropped for row in target_rows)

    summary = {
        "run_key": args.output_dir.name,
        "no_db_writes": True,
        "model_calls": 0,
        "inputs": {
            "spec": str(args.spec),
            "labels": str(args.labels),
            "element_pairs": str(args.element_pairs),
            "candidates": str(args.candidates),
            "taxonomy": str(args.taxonomy),
        },
        "overall": overall,
        "sections": sections_summary,
        "calibration": {
            section: {
                "positive_terms_top20": list(result["positive_terms"].items())[:20],
                "off_domain_enriched_tags": result["off_domain_enriched_tags"],
                "suppressed_papers": result["suppressed_papers"],
                "thresholds": result["thresholds"],
                "tag_lift": result["tag_lift"],
            }
            for section, result in section_results.items()
        },
        "checks": {
            "size_evolution_acceptance_off_domain_below_20pct": sections_summary.get("size_evolution", {}).get(
                "after_off_domain_share", 1.0
            )
            < 0.20,
            "size_evolution_acceptance_citable_retention_at_least_90pct": sections_summary.get("size_evolution", {}).get(
                "citable_retention", 0.0
            )
            >= 0.90,
            "size_evolution_2512_18276v1_rows": [filtered_row_to_dict(row) for row in target_rows],
            "size_evolution_2512_18276v1_suppressed": target_suppressed,
        },
        "filtered_rows_sample": [filtered_row_to_dict(row) for row in all_filtered[:50]],
    }

    build_reports(
        args.output_dir,
        args.spec,
        args.labels,
        args.element_pairs,
        args.candidates,
        args.taxonomy,
        section_results,
        summary,
    )
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", type=Path, default=DEFAULT_SPEC)
    parser.add_argument("--labels", type=Path, default=DEFAULT_LABELS)
    parser.add_argument("--element-pairs", type=Path, default=DEFAULT_ELEMENT_PAIRS)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--taxonomy", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def main() -> None:
    summary = run(parse_args())
    print(json.dumps({"output_dir": summary["run_key"], "overall": summary["overall"]}, sort_keys=True))


if __name__ == "__main__":
    main()
