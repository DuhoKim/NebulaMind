#!/usr/bin/env python3
"""Verify pass-21 native-directional-smear/minimum-scale evidence and handoff."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import cast

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
CAND_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
SOURCE_SHA = "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1"
SNAPSHOT_SHA = "f2cb324f1d55a1710b9debd865d73ab02c10735076f040c2dee22ee0b2af81c5"
EXPECTED_CUTS = [12.133333, 26.366667, 47.266667, 60.466667, 74.666667, 88.066667, 102.333333, 116.333333, 131.033333, 148.033333, 162.033333, 179.733333, 196.8, 213.433333, 233.866667]
CAND_DIR = ROOT / "qa/pass21_minimum_scale_directional_smear_audit"
METHOD_DIR = ROOT / "qa/pass21_v8_minimum_scale_directional_smear"
VARIANTS = ["clean", "downscale_360p", "smear_w07_then_360p", "smear_w13_then_360p", "smear_w21_then_360p"]
SMEAR = {"smear_w07_then_360p": 7, "smear_w13_then_360p": 13, "smear_w21_then_360p": 21}
PINS = {
    "SOURCE_STATUS_FREEZE.json": SOURCE_SHA,
    "STORYBOARD_PROPOSAL.json": "80c91bc5513ac6268501c02cac2e8354388e43bf0094569804e4bbf54f293bce",
    "proposal_frames/v8/render_receipt.json": "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3",
    "qa/pass20_review_snapshot_v1.json": "63ff67da70a52b3175bb8ddb5803c07c2121d5b9a5e5bfeb247a5f03518fddea",
    "qa/extract_pass21_minimum_scale_directional_smear_frames.py": "31ba12ba16307beb3caf562de10b81adde2295769f6bc042fc3fc750e370170b",
    "qa/pass21_minimum_scale_directional_smear_audit/extraction_receipt.json": "f3ff4685628992ab053b77da384e5745a2b3145c53831bba40bf9c92c2d0bd0b",
    "qa/build_pass21_v8_minimum_scale_directional_smear.py": "34ae1b1d9f21864ad756f76da5d638e46564c5e023d8cdcea2973165a4f3e129",
    "qa/pass21_v8_minimum_scale_directional_smear/receipt.json": "17ea19ddbfe73c124c7cf986defafd2279862e002f6d8305914be055f3a5d067",
    "qa/audit_pass21_minimum_scale_directional_smear.py": "a3c03d6ef7fc3de95b933e9ec61e2b46ec34bc6c9cc70f599271070db899cef9",
    "qa/pass21_minimum_scale_directional_smear_quantitative_audit.json": "bcb93036c352ed316a53b85151f161ad976a8bfed25f42cf9a7708d7bc4c162d",
    "MINIMUM_SCALE_DIRECTIONAL_SMEAR_GUARD_PASS21.json": "b783db9895c548539cde4209048253f39bb8363b7f35f90415dd6746b9e80543",
    "PASS21_ENCODED_FRAME_AUDIT.md": "37b2317c53effab7a6b7bbdbebd9f00162f12efb5b65b4bbb4d09d2cd10f4dba",
    "BLOCKER_PACKET_PASS21.json": "c4b6ef2e36e7192c4cfc71cc779c9508dae29403966cc3fa0df1574726a0156d",
    "qa/pass21_review_snapshot_v1.json": SNAPSHOT_SHA,
}


def sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text())
    if not isinstance(value, dict):
        raise AssertionError(f"object required: {path}")
    return value


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(value: object, expected: float) -> bool:
    return math.isclose(float(cast(float | int | str, value)), expected, abs_tol=0.0000005)


def horizontal_smear(image: Image.Image, width: int) -> np.ndarray:
    values = np.asarray(image.convert("RGB"), dtype=np.uint8)
    radius = width // 2
    padded = np.pad(values, ((0, 0), (radius, radius), (0, 0)), mode="edge")
    cumulative = np.cumsum(padded, axis=1, dtype=np.uint64)
    cumulative = np.concatenate([np.zeros((values.shape[0], 1, 3), dtype=np.uint64), cumulative], axis=1)
    sums = cumulative[:, width:, :] - cumulative[:, :-width, :]
    smeared = ((sums + width // 2) // width).astype(np.uint8)
    return np.asarray(Image.fromarray(smeared, mode="RGB").resize((640, 360), Image.Resampling.LANCZOS), dtype=np.uint8)


def verify_pins() -> None:
    require(sha(CANDIDATE) == CAND_SHA, "candidate hash drift")
    for relative, expected in PINS.items():
        require(sha(ROOT / relative) == expected, f"hash drift: {relative}")


def verify_candidate() -> None:
    receipt = load(CAND_DIR / "extraction_receipt.json")
    require(receipt["candidate_sha256"] == CAND_SHA, "candidate receipt hash")
    require(receipt["cut_times_seconds"] == EXPECTED_CUTS, "cut list")
    require(receipt["fresh_clean_match"] == "16/16_BYTE_IDENTICAL_TO_PASS20", "clean lineage")
    require(receipt["variant_order"] == VARIANTS and receipt["frame_count"] == 80, "candidate dimensions")
    records = cast(list[dict[str, object]], receipt["records"])
    require(len(records) == 16, "candidate scene count")
    for record in records:
        samples = cast(list[dict[str, object]], record["samples"])
        require([sample["variant"] for sample in samples] == VARIANTS, "candidate variants")
        paths = {str(sample["variant"]): CAND_DIR / str(sample["frame"]) for sample in samples}
        prior = ROOT / str(record["prior_pass20_clean_path"])
        require(sha(paths["clean"]) == sha(prior), "clean byte custody")
        with Image.open(paths["clean"]) as native_open:
            native = native_open.convert("RGB")
        require(native.size == (1920, 1080), "native dimensions")
        for variant, width in SMEAR.items():
            with Image.open(paths[variant]) as observed_open:
                observed = np.asarray(observed_open.convert("RGB"), dtype=np.uint8)
            require(observed.shape == (360, 640, 3), "represented dimensions")
            require(np.array_equal(horizontal_smear(native, width), observed), f"candidate transform {variant}")
        for sample in samples:
            require(sha(CAND_DIR / str(sample["frame"])) == sample["sha256"], "candidate frame hash")


def verify_methods() -> None:
    receipt = load(METHOD_DIR / "receipt.json")
    require(receipt["frame_count"] == 105 and receipt["scene_count"] == 21, "method counts")
    require(receipt["variant_order"] == VARIANTS, "method variants")
    groups = cast(dict[str, dict[str, object]], receipt["groups"])
    require(set(groups) == {"sealed_v8", "pass7_caption_safe", "pass12_sharpness_safe"}, "method groups")
    for group_name, group in groups.items():
        scenes = cast(list[dict[str, object]], group["scenes"])
        require(len(scenes) == 7, f"method scenes {group_name}")
        for record in scenes:
            source = ROOT / str(record["source"])
            require(sha(source) == record["source_sha256"], "method source custody")
            samples = cast(list[dict[str, object]], record["samples"])
            paths = {str(sample["variant"]): METHOD_DIR / group_name / str(sample["frame"]) for sample in samples}
            require(sha(paths["clean"]) == sha(source), "method clean custody")
            with Image.open(source) as native_open:
                native = native_open.convert("RGB")
            for variant, width in SMEAR.items():
                with Image.open(paths[variant]) as observed_open:
                    observed = np.asarray(observed_open.convert("RGB"), dtype=np.uint8)
                require(np.array_equal(horizontal_smear(native, width), observed), f"method transform {group_name} {variant}")


def verify_metrics_and_boundary() -> None:
    audit = load(ROOT / "qa/pass21_minimum_scale_directional_smear_quantitative_audit.json")
    candidate = cast(dict[str, object], audit["candidate"])
    aggregates = cast(dict[str, dict[str, object]], candidate["aggregate"])
    operational = aggregates["smear_w07_then_360p"]
    require(close(operational["headline_recall"], 0.85), "headline metric")
    require(close(operational["full_recall"], 0.620722), "full metric")
    require(close(operational["lower_recall"], 0.265169), "lower metric")
    require(close(operational["numeric_recall"], 0.122222), "numeric metric")
    require(operational["structural_gate_scene_count"] == 0, "candidate structural gate")
    require(operational["exact_transform_recomputed_scenes"] == 16, "candidate exact transform")
    method = cast(dict[str, object], audit["method"])
    proof_group = cast(dict[str, object], method["pass12_sharpness_safe"])
    proof_variants = cast(dict[str, dict[str, object]], proof_group["variants"])
    proof = proof_variants["smear_w07_then_360p"]
    require(proof["gate_count_passing_threshold"] == 6, "mapped OCR aid count")
    require(close(proof["mean_best_similarity"], 0.945953), "mapped OCR aid mean")
    rows = cast(list[dict[str, object]], proof["gate_rows"])
    scene4 = next(row for row in rows if row["scene"] == 4)
    require(close(scene4["best_similarity"], 0.780488) and not scene4["passes_threshold"], "scene4 disclosure")
    human = cast(dict[str, object], method["human_review"])
    require(human["pass12_smear_w07_then_360p_exact_top_gates"] == "7/7", "visual proof gates")
    require(human["pass12_smear_w07_then_360p_result_held_badges"] == "7/7", "visual proof badges")
    snapshot = load(ROOT / "qa/pass21_review_snapshot_v1.json")
    require(cast(dict[str, object], snapshot["representation_boundary"])["method_only"] is True, "method boundary")
    require(cast(dict[str, object], snapshot["representation_boundary"])["science_adjudicated"] is False, "science boundary")
    blocker = load(ROOT / "BLOCKER_PACKET_PASS21.json")
    require(blocker["video_reportable_now"] is False, "reportable state")
    require(all(item["state"] in {"OPEN", "PRESERVED_EVIDENCE"} for item in cast(list[dict[str, object]], blocker["exact_science_blockers"])), "blocker states")


def verify_no_media() -> None:
    forbidden = {".mp4", ".mp3", ".wav", ".aac", ".m4a"}
    hits = [path for path in ROOT.rglob("*pass21*") if path.is_file() and path.suffix.lower() in forbidden]
    require(not hits, f"pass21 media outputs: {hits}")
    require(not (ROOT / "proposal_frames/v9").exists(), "v9 exists")


def verify_handoff() -> None:
    status = load(ROOT / "STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS21_MINIMUM_SCALE_DIRECTIONAL_SMEAR_GUARD_V1", "status phase")
    require(status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS21_COMPLETE", "status receipt")
    require(status["video_reportable_now"] is False, "status reportable")
    receipt = (ROOT / "LANE_RECEIPT.md").read_text()
    require("# PASS21_DEEPENING_MARKER_V1" in receipt and "Exact Hwao action requested after pass 21" in receipt, "lane receipt")
    require("PASS21_ENCODED_FRAME_AUDIT.md" in (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text(), "integrator handoff")
    require("Pass-21 compound native-directional-smear/minimum-scale stress QA" in (ROOT / "STATIC_PROPOSAL_QA.md").read_text(), "static QA handoff")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence-only", action="store_true")
    arguments = parser.parse_args()
    verify_pins()
    verify_candidate()
    verify_methods()
    verify_metrics_and_boundary()
    verify_no_media()
    if not arguments.evidence_only:
        verify_handoff()
    suffix = "evidence-only" if arguments.evidence_only else "status-handoff"
    print(f"PASS pass21 snapshot/candidate/80-compound-frames/hierarchy/105-method-derivatives/minimum-scale-directional-smear-guard/source-blockers/{suffix}/no-media")


if __name__ == "__main__":
    main()
