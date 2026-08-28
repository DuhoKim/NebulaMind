#!/usr/bin/env python3
"""Verify pass-15 geometry evidence, guard, blockers, custody, and handoff."""

from __future__ import annotations

import hashlib
import json
import math
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
EXPECTED_CANDIDATE = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
EXPECTED_CUTS = [12.133333, 26.366667, 47.266667, 60.466667, 74.666667, 88.066667, 102.333333, 116.333333, 131.033333, 148.033333, 162.033333, 179.733333, 196.8, 213.433333, 233.866667]
VARIANTS = {
    "clean": (1.0, 1.0), "squeeze_x90": (0.9, 1.0), "squeeze_y90": (1.0, 0.9),
    "squeeze_x80": (0.8, 1.0), "squeeze_y80": (1.0, 0.8),
}
PINNED = {
    "SOURCE_STATUS_FREEZE.json": "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1",
    "STORYBOARD_PROPOSAL.json": "80c91bc5513ac6268501c02cac2e8354388e43bf0094569804e4bbf54f293bce",
    "proposal_frames/v8/render_receipt.json": "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3",
    "proposal_frames/v8/contact_sheet.png": "5889dfcbcb7f24afe989411b127a5c30adb9e4685513058eca9d51cc0cf32056",
    "SHARPNESS_RESILIENCE_STORYBOARD_CORRECTION_PASS12.json": "1312ea54aa860473ff57e3c47e8305ecca8630ba1f6a998a6e02d9aea9999422",
    "qa/pass12_sharpness_safe_mockup/receipt.json": "35f526a60b053f8c203278b3c205c1e0145f9a6dcd6da309541eb57b6399e92c",
    "qa/pass14_review_snapshot_v1.json": "3edbfe6a46c18821f388c0556131c05bc97f4334fc99dcd55cec64062da0b63f",
    "qa/extract_pass15_geometry_frames.py": "219c74e68249259b852481e4032b4f8947d1d2568b91f1040f359139d4cbf46a",
    "qa/pass15_geometry_audit/extraction_receipt.json": "358630f299fbb985273f4ecfd77bb2a8783fa341716be3a97d53edba12e4bb39",
    "qa/build_pass15_v8_geometry.py": "d7798af275492da421ffab92c8c03b554b19020cf8877c5166d1b1a12d86de00",
    "qa/pass15_v8_geometry/receipt.json": "6cba852331bb78caeb043176e2795637eb55cfcf9366fe18614fd9ca73577ffc",
    "qa/audit_pass15_geometry.py": "f5d1f2a1b70d7317b5cca26e5430e47290f8a6c9944d731f53b24913dfd0d5fb",
    "qa/pass15_geometry_quantitative_audit.json": "ed0637fc1e262bfebad89efc36178f6f9e2c5d51c774f2bd745d4052edabf621",
    "GEOMETRY_RESILIENCE_GUARD_PASS15.json": "65e99cc8b1b3bffdefb9b8136211645a9d3cbc3a3a818c29dff52c3723ed1d36",
    "PASS15_ENCODED_FRAME_AUDIT.md": "06785441e11a96a67b524c9a2153921e8d72b8f1be525c4e753e2b081b206992",
    "BLOCKER_PACKET_PASS15.json": "25f6d98c0b76b49804ebbec200632bb766347538eb254f9f313975b3740e618b",
    "qa/pass15_review_snapshot_v1.json": "8d911cc0d6abbf12e95be30420fd33018e18668ba5907edd990bc1f34e599428",
}


def require(condition: bool, label: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {label}")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(rel: str):
    return json.loads((ROOT / rel).read_text())


def squeeze(image: Image.Image, sx: float, sy: float) -> Image.Image:
    w, h = image.size; nw, nh = round(w * sx), round(h * sy)
    resized = image.resize((nw, nh), Image.Resampling.LANCZOS)
    out = Image.new("RGB", (w, h), (0, 0, 0)); out.paste(resized, ((w - nw) // 2, (h - nh) // 2)); return out


def image_equal(a: Image.Image, b: Image.Image) -> bool:
    return ImageChops.difference(a.convert("RGB"), b.convert("RGB")).getbbox() is None


def check_pins() -> None:
    require(sha(CANDIDATE) == EXPECTED_CANDIDATE, "candidate custody")
    for rel, expected in PINNED.items():
        require((ROOT / rel).is_file(), f"missing {rel}")
        require(sha(ROOT / rel) == expected, f"hash {rel}")


def check_extraction() -> None:
    receipt = load("qa/pass15_geometry_audit/extraction_receipt.json")
    require(receipt["candidate_sha256"] == EXPECTED_CANDIDATE, "extraction candidate")
    require(receipt["cut_detection"]["cuts"] == EXPECTED_CUTS, "fresh cuts")
    require(receipt["scene_count"] == 16 and receipt["variant_count"] == 5 and receipt["frame_count"] == 80, "candidate census")
    require(receipt["fresh_clean_match"] == "16/16_BYTE_IDENTICAL_TO_PASS14", "clean reproduction marker")
    require(receipt["operational_variants"] == ["squeeze_x90", "squeeze_y90"], "operational pair")
    require(receipt["characterization_variants"] == ["squeeze_x80", "squeeze_y80"], "characterization pair")
    require(len(receipt["records"]) == 16, "record count")
    for record in receipt["records"]:
        scene = record["scene"]; samples = {s["variant"]: s for s in record["samples"]}
        require(set(samples) == set(VARIANTS), f"candidate variants scene {scene}")
        clean_path = ROOT / "qa/pass15_geometry_audit" / samples["clean"]["frame"]
        prior = ROOT / f"qa/pass14_shadow_floor_audit/frames/clean/scene_{scene:02d}.png"
        require(sha(clean_path) == sha(prior) == record["prior_pass14_clean_sha256"], f"candidate clean scene {scene}")
        with Image.open(clean_path).convert("RGB") as clean:
            for variant, (sx, sy) in VARIANTS.items():
                path = ROOT / "qa/pass15_geometry_audit" / samples[variant]["frame"]
                require(sha(path) == samples[variant]["sha256"], f"candidate frame hash {scene}/{variant}")
                with Image.open(path).convert("RGB") as observed:
                    require(observed.size == (1920, 1080), f"candidate dimensions {scene}/{variant}")
                    expected = clean if variant == "clean" else squeeze(clean, sx, sy)
                    require(image_equal(expected, observed), f"candidate transform {scene}/{variant}")
    for variant, sheet in receipt["contact_sheets"].items():
        path = ROOT / "qa/pass15_geometry_audit" / sheet["path"]
        require(sha(path) == sheet["sha256"], f"candidate contact sheet {variant}")
        with Image.open(path) as image:
            require(image.size == (1892, 1276), f"candidate contact dimensions {variant}")


def check_method() -> None:
    receipt = load("qa/pass15_v8_geometry/receipt.json")
    require(receipt["group_count"] == 3 and receipt["scene_count"] == 21 and receipt["frame_count"] == 105, "method census")
    require(set(receipt["groups"]) == {"sealed_v8", "pass7_caption_safe", "pass12_sharpness_safe"}, "method groups")
    for group_name, group in receipt["groups"].items():
        require(group["scene_count"] == 7 and group["frame_count"] == 35, f"group census {group_name}")
        for row in group["scenes"]:
            scene = row["scene"]; source = ROOT / row["source"]
            require(sha(source) == row["source_sha256"], f"method source {group_name}/{scene}")
            with Image.open(source).convert("RGB") as clean:
                for sample in row["samples"]:
                    variant = sample["variant"]; path = ROOT / "qa/pass15_v8_geometry" / group_name / sample["frame"]
                    require(sha(path) == sample["frame_sha256"], f"method hash {group_name}/{scene}/{variant}")
                    with Image.open(path).convert("RGB") as observed:
                        expected = clean if variant == "clean" else squeeze(clean, *VARIANTS[variant])
                        require(image_equal(expected, observed), f"method transform {group_name}/{scene}/{variant}")
        for variant, sheet in group["contact_sheets"].items():
            path = ROOT / "qa/pass15_v8_geometry" / group_name / sheet["path"]
            require(sha(path) == sheet["sha256"], f"method sheet {group_name}/{variant}")
            with Image.open(path) as image:
                require(image.size == (1180, 1528), f"method sheet dimensions {group_name}/{variant}")


def near(actual, expected, label):
    require(math.isclose(float(actual), expected, abs_tol=1e-6), label)


def check_audit_and_packets() -> None:
    audit = load("qa/pass15_geometry_quantitative_audit.json")
    require(audit["deepening_pass"] == 15 and audit["raw_ocr_text_stored"] is False, "audit contract")
    c = audit["candidate"]["aggregates"]
    near(c["squeeze_x90"]["mean_headline_token_recall_vs_clean"], 0.993606, "candidate x90 headline")
    near(c["squeeze_y90"]["mean_headline_token_recall_vs_clean"], 0.940701, "candidate y90 headline")
    near(c["squeeze_x90"]["mean_full_token_recall_vs_clean"], 0.974214, "candidate x90 full")
    near(c["squeeze_y90"]["mean_full_token_recall_vs_clean"], 0.974387, "candidate y90 full")
    require(c["squeeze_x90"]["structural_gate_scene_count"] == 0 and c["squeeze_y90"]["structural_gate_scene_count"] == 0, "candidate operational gates")
    proof = audit["method_groups"]["pass12_sharpness_safe"]["aggregates"]
    for variant in ("squeeze_x90", "squeeze_y90", "squeeze_x80", "squeeze_y80"):
        require(proof[variant]["scene_specific_gate_count"] == 7, f"proof gates {variant}")
        near(proof[variant]["mean_gate_character_similarity_best_of_psm_6_7_11_13"], 1.0, f"proof similarity {variant}")
    visual = audit["human_visual_review"]
    require(visual["candidate_structural_gate_scenes"]["squeeze_x90"] == "0/16", "visual candidate gates")
    require(visual["pass12_no_overlap_clipping_or_semantic_ambiguity"] is True, "proof visual ambiguity")
    guard = load("GEOMETRY_RESILIENCE_GUARD_PASS15.json")
    require(guard["guard_id"] == "spin-worker-yui-pass15-geometry-20260808T100524K", "guard id")
    require(guard["disposition"]["non_pixel_integration_guard_added"] is True, "guard action")
    require(guard["disposition"]["new_pixel_change_requested"] is False and guard["disposition"]["new_copy_change_requested"] is False, "no correction")
    require(guard["science_boundary"]["video_reportable_now"] is False, "guard science")
    blocker = load("BLOCKER_PACKET_PASS15.json")
    require(blocker["packet_id"] == "spin-worker-yui-pass15-blockers-20260808T100524K", "blocker id")
    require(len(blocker["exact_blockers"]) == 2 and all(b["state"] == "BLOCKED" for b in blocker["exact_blockers"]), "exact blockers")
    require(blocker["video_reportable_now"] is False, "blocker reportability")
    snapshot = load("qa/pass15_review_snapshot_v1.json")
    require(snapshot["snapshot_id"] == "spin-worker-yui-pass15-review-v1-20260808T100618K", "snapshot id")
    require(snapshot["science_blockers"]["video_reportable_now"] is False, "snapshot science")
    require(all(v is False for v in snapshot["negative_actions"].values()), "snapshot negative actions")


def check_representation_and_handoff() -> None:
    freeze = load("SOURCE_STATUS_FREEZE.json"); require(freeze["video_reportable_now"] is False, "freeze reportability")
    story = load("STORYBOARD_PROPOSAL.json"); require(story["status"] == "PROPOSAL_ONLY_NOT_A_CANDIDATE" and story["video_reportable_now"] is False, "story status")
    static = load("qa/static_proposal_validation.json"); require(static.get("verdict") == "PASS", "static validation")
    for scene in range(1, 8):
        for variant in ("squeeze_x90", "squeeze_y90"):
            path = ROOT / f"qa/pass15_v8_geometry/pass12_sharpness_safe/frames/scene_{scene:02d}_{variant}.png"
            text = subprocess.run(["tesseract", str(path), "stdout", "--psm", "11"], check=True, capture_output=True, text=True).stdout.casefold()
            require("galaxy spin" in text, f"GALAXY SPIN header {scene}/{variant}")
            for forbidden in ("cosmolog", "dipole", "parity", "h0", "black hole"):
                require(forbidden not in text, f"forbidden {forbidden} {scene}/{variant}")
    status = load("STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS15_GEOMETRY_RESILIENCE_GUARD_V1", "status phase")
    require(status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS15_COMPLETE", "status marker")
    require(status["video_reportable_now"] is False, "status reportability")
    require(status["pass15_geometry_guard_added"] is True and status["pass15_new_pixel_or_copy_correction_requested"] is False, "status action")
    lane = (ROOT / "LANE_RECEIPT.md").read_text(); require("PASS15_DEEPENING_MARKER_V1" in lane, "lane marker")
    request = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text(); require("Pass 15 adds the anisotropic-geometry integration guard" in request, "integrator request")
    qa = (ROOT / "STATIC_PROPOSAL_QA.md").read_text(); require("Pass-15 anisotropic-geometry stress QA" in qa, "static QA")
    media = [p for p in ROOT.rglob("*") if p.is_file() and p.suffix.casefold() in {".mp4", ".mp3", ".wav", ".aac", ".m4a"}]
    require(not media, "no encoded media in lane")


def main() -> None:
    check_pins(); check_extraction(); check_method(); check_audit_and_packets(); check_representation_and_handoff()
    print("PASS pass15 snapshot/candidate/80-geometry-frames/hierarchy/105-method-derivatives/geometry-guard/source-blockers/status/no-media")


if __name__ == "__main__":
    main()
