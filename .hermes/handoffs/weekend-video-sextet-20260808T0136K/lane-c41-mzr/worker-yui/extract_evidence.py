#!/usr/bin/env python3
"""Extract a read-only C41 MZR video evidence freeze into this worker-Yui lane."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind")
SOURCE = ROOT / ".hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K"
PLOTS = Path("/Users/duhokim/HermesOps/cockpit/videos/plots")
LANE = ROOT / ".hermes/handoffs/weekend-video-sextet-20260808T0136K/lane-c41-mzr/worker-yui"

PATHS = {
    "current_public_video": ROOT / "frontend/public/videos/c41-highz-mzr-calibration-anchored.mp4",
    "source_storyboard": SOURCE / "storyboard_c41_anchor_gap.json",
    "shared_renderer": ROOT / "tools/nm_paper_video.py",
    "shared_plotter": ROOT / "tools/nm_paper_plot.py",
    "source_bins_figure": PLOTS / "c41-highz-mzr-calibration-anchored_bins.png",
    "source_literature_figure": PLOTS / "lit_metallicity.png",
    "paper_figure": SOURCE / "ANCHOR_GAP_FIGURE.png",
    "results": SOURCE / "T3_REAL_RESULTS.json",
    "sample": SOURCE / "T3_REAL_SAMPLE.jsonl",
    "run_log": SOURCE / "T3_REAL_LOG.txt",
    "paper_tex": SOURCE / "ANCHOR_GAP_PAPER.tex",
    "paper_pdf": SOURCE / "ANCHOR_GAP_PAPER.pdf",
    "public_paper_pdf": ROOT / "frontend/public/studies/c41-highz-mzr-calibration-anchored.pdf",
    "t5_receipt": SOURCE / "T5_RECEIPTS.md",
    "paper_history": ROOT / "frontend/public/studies/c41-highz-mzr-calibration-anchored_history.json",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def catalog_key(table_id: str) -> str:
    parts = table_id.split("/")
    if table_id.startswith("V/"):
        return "/".join(parts[:2])
    return "/".join(parts[:-1])


def classify_exclusion(value: str | None) -> str:
    if value is None:
        return "contract_grade_anchor"
    if value.startswith("S/N(4363)"):
        return "sn4363_below_floor"
    if value == "no Hbeta -> abundance undefined under A' spec":
        return "no_hbeta"
    if value == "missing 4363/5007 flux":
        return "missing_flux"
    if value == "Te out of range: nan":
        return "te_failure"
    raise ValueError(f"unrecognized exclusion: {value}")


def required_int(pattern: str, text: str, label: str) -> int:
    match = re.search(pattern, text)
    if match is None:
        raise ValueError(f"missing {label} in final run block")
    return int(match.group(1))


def main() -> None:
    for path in PATHS.values():
        if not path.exists():
            raise FileNotFoundError(path)

    storyboard = json.loads(PATHS["source_storyboard"].read_text())
    results = json.loads(PATHS["results"].read_text())
    rows = [json.loads(line) for line in PATHS["sample"].read_text().splitlines() if line.strip()]
    log_text = PATHS["run_log"].read_text()
    last_start = log_text.rfind("=== t3_real.py START")
    if last_start < 0:
        raise ValueError("final run block not found")
    block = log_text[last_start:]

    global_tables = required_int(r"S1-global v4: (\d+) 4363-tables", block, "global table count")
    join_candidates = required_int(r"S1 done: (\d+) candidates", block, "join candidate count")
    skipped_tables = re.findall(r"\] S2 SKIP ([^:]+):", block)
    fetched_tables = re.findall(
        r"\] S2 (?!SKIP |mass-sibling |done:)([^:]+): \d+ rows with 4363 measured",
        block,
    )
    raw_rows = required_int(r"S2 done: (\d+) z>3 rows", block, "raw row count")
    derived_rows = required_int(
        r"S3 done: (\d+) rows with A' direct O/H", block, "derived anchor count"
    )

    exclusion_counts: dict[str, int] = {}
    for row in rows:
        key = classify_exclusion(row.get("exclusion"))
        exclusion_counts[key] = exclusion_counts.get(key, 0) + 1

    if len(rows) != raw_rows:
        raise ValueError(f"sample/log mismatch: {len(rows)} != {raw_rows}")
    if exclusion_counts.get("contract_grade_anchor") != derived_rows:
        raise ValueError("anchor count mismatch")
    if sum(exclusion_counts.values()) != raw_rows:
        raise ValueError("exclusion accounting does not close")
    if len(fetched_tables) + len(skipped_tables) != join_candidates:
        raise ValueError("table fetch accounting does not close")

    bins = {
        "8_le_logM_lt_9": results["bins"]["M_star_bin_8_9"]["N"],
        "9_le_logM_lt_10": results["bins"]["M_star_bin_9_10"]["N"],
        "logM_ge_10": results["bins"]["M_star_bin_gt_10"]["N"],
    }
    below_floor = results["per_class_counts"]["below_bin_floor"]
    if sum(bins.values()) + below_floor != derived_rows:
        raise ValueError("mass-bin accounting does not close")

    probe = json.loads(
        subprocess.check_output(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration,size,bit_rate:stream=index,codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,sample_rate,channels",
                "-of",
                "json",
                str(PATHS["current_public_video"]),
            ],
            text=True,
        )
    )

    hashes = {name: sha256(path) for name, path in PATHS.items()}
    source_duration = sum(float(card.get("seconds", 5)) for card in storyboard["cards"])

    freeze = {
        "generated_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "lane": "lane-c41-mzr/worker-yui",
        "authority": "HWAO_WEEKEND_ORDER.md + COORDINATION_UPDATE.md",
        "video_reportable_now": {
            "decision": True,
            "verdict": "PASS_WITH_STRICT_ARCHIVE_CENSUS_BOUNDARY",
            "basis": [
                "T3_REAL_RESULTS.status is REAL_COMPLETED",
                "T5 receipt records PASS — SHAPE-2 MEASUREMENT RECEIPTED",
                "source and public paper PDF hashes are identical",
                "paper history records Duho's direction to land the paper on the Lab",
            ],
            "allowed": [
                "public-archive table/redshift/fetch/row/anchor funnel",
                "mass-bin counts 2/1/0 and two anchors below the frozen lower bin edge",
                "no mass bin reaches the pre-committed three-anchor minimum",
                "no deficit verdict is possible at contract-grade public statistics",
                "five is a public-archive floor because twelve candidate tables were unreachable and only the lambda-4363 channel was enumerated",
            ],
            "forbidden": [
                "a calibrated high-redshift mass-metallicity relation",
                "a metallicity deficit of any size or direction",
                "local diagnostics validated or invalidated at high redshift",
                "anchors absent from the sky",
                "FMR result; A4 remains not-computable-v1",
            ],
        },
        "artifact_hashes_sha256": hashes,
        "artifact_paths_verification_only": {name: str(path) for name, path in PATHS.items()},
        "current_video": {
            "probe": probe,
            "source_storyboard_card_count": len(storyboard["cards"]),
            "source_storyboard_duration_seconds": source_duration,
        },
        "funnel": {
            "stages": [
                {"count": global_tables, "unit": "archive tables", "condition": "carry a lambda-4363-class column"},
                {"count": join_candidates, "unit": "candidate tables", "condition": "redshift available in-table or by sibling join"},
                {"count": len(fetched_tables), "unit": "tables", "condition": "fetched at run time", "catalogs": len({catalog_key(item) for item in fetched_tables})},
                {"count": raw_rows, "unit": "z>3 rows", "condition": "tabulated lambda-4363 flux"},
                {"count": derived_rows, "unit": "contract-grade anchors", "condition": "direct-Te abundance plus linked stellar mass"},
            ],
            "unreachable_candidate_tables": len(skipped_tables),
            "fetched_table_ids_verification_only": fetched_tables,
            "skipped_table_ids_verification_only": skipped_tables,
        },
        "exclusion_accounting": exclusion_counts,
        "mass_bin_null": {
            "actual_anchor_counts": bins,
            "below_frozen_logM_8_floor": below_floor,
            "shared_minimum_per_bin": 3,
            "verdicts": {key: "no-verdict-possible (too few anchors)" for key in bins},
        },
        "display_citations": [
            "NebulaMind Autonomous Research Crew (2026), The Public-Archive Direct-Te Anchor Gap at z>3: A Contract-Grade Census, §§3–4, nebulamind.net/studies/c41-highz-mzr-calibration-anchored.pdf",
            "Andrews & Martini (2013), ApJ 765, 140",
            "Izotov et al. (2006), A&A 448, 955",
            "Luridiana et al. (2015), A&A 573, A42",
        ],
        "safety": {
            "shared_tools_modified": False,
            "tts_invoked": False,
            "candidate_bundle_written": False,
            "public_artifact_modified": False,
        },
    }

    output = LANE / "EVIDENCE_FREEZE.json"
    output.write_text(json.dumps(freeze, indent=2) + "\n")
    print(output)


if __name__ == "__main__":
    main()
