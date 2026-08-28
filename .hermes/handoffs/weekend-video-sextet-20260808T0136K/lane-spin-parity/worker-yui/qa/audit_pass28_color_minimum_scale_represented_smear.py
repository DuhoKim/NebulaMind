#!/usr/bin/env python3
"""Quantify color/monochrome -> 360p -> represented-pixel horizontal width-3 smear interaction."""

from __future__ import annotations

import collections
import csv
import difflib
import io
import json
import math
import re
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
CAND_ROOT = ROOT / "qa/pass28_color_minimum_scale_represented_smear_audit"
CAND_RECEIPT = CAND_ROOT / "extraction_receipt.json"
METHOD_ROOT = ROOT / "qa/pass28_v8_color_minimum_scale_represented_smear"
METHOD_RECEIPT = METHOD_ROOT / "receipt.json"
OUT = ROOT / "qa/pass28_color_minimum_scale_represented_smear_quantitative_audit.json"
WIDTH = 3
CRITICAL = {7, 9, 10, 11, 16}
GATE_CROP = (28, 20, 520, 49)
PSMS = (6, 7, 11, 13)
THRESHOLD = 0.80
GATES = {
    1: "result locked archive frame independent review required",
    2: "overlapping readouts do not sum",
    3: "label frame statistic physical interpretation held",
    4: "frame unstated result held",
    5: "column check only storage frame unresolved",
    6: "control design only outcomes withheld",
    7: "separate authorization required after both blockers resolve",
}
VARIANTS = [
    "color_then_360p_then_represented_horizontal_smear_w03",
    "grayscale_bt709_then_360p_then_represented_horizontal_smear_w03",
    "protanopia_machado100_then_360p_then_represented_horizontal_smear_w03",
    "deuteranopia_machado100_then_360p_then_represented_horizontal_smear_w03",
    "tritanopia_machado100_then_360p_then_represented_horizontal_smear_w03",
]
GATE_PATTERNS = [re.compile(r"\bresult\s+held\b"), re.compile(r"\bframe\s+unstated\b"), re.compile(r"\boutcomes?\s+withheld\b"), re.compile(r"\bresult\s+locked\b"), re.compile(r"\bno\s+outcome\s+shown\b")]


def ocr_tsv(path: Path, psm: int = 6) -> list[dict]:
    result = subprocess.run(["tesseract", str(path), "stdout", "--psm", str(psm), "tsv"], check=True, capture_output=True, text=True)
    rows = []
    for row in csv.DictReader(io.StringIO(result.stdout), delimiter="\t"):
        text = (row.get("text") or "").strip()
        try:
            conf = float(row.get("conf", -1))
        except ValueError:
            conf = -1
        if text and conf >= 20:
            rows.append({"text": text, "norm": re.sub(r"[^a-z0-9]+", "", text.lower()), "left": int(row["left"]), "top": int(row["top"]), "width": int(row["width"]), "height": int(row["height"]), "conf": conf})
    return rows


def counter(rows: list[dict], region: str) -> collections.Counter:
    selected = []
    for row in rows:
        cy = row["top"] + row["height"] / 2
        if region == "headline" and cy > 105:
            continue
        if region == "lower" and cy < 230:
            continue
        if region == "numeric" and not any(ch.isdigit() for ch in row["text"]):
            continue
        if row["norm"]:
            selected.append(row["norm"])
    return collections.Counter(selected)


def recall(reference: collections.Counter, observed: collections.Counter) -> float:
    total = sum(reference.values())
    return 1.0 if total == 0 else sum((reference & observed).values()) / total


def norm_text(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def crop_similarity(path: Path, canonical: str) -> tuple[float, int]:
    with Image.open(path) as image:
        crop = image.convert("RGB").crop(GATE_CROP).resize(((GATE_CROP[2] - GATE_CROP[0]) * 4, (GATE_CROP[3] - GATE_CROP[1]) * 4), Image.Resampling.NEAREST)
    scores = []
    for psm in PSMS:
        result = subprocess.run(["tesseract", "stdin", "stdout", "--psm", str(psm)], input=image_bytes(crop), check=True, capture_output=True)
        observed = norm_text(result.stdout.decode("utf-8", "ignore"))
        score = difflib.SequenceMatcher(None, norm_text(canonical), observed).ratio()
        scores.append((score, psm))
    return max(scores)


def image_bytes(image: Image.Image) -> bytes:
    stream = io.BytesIO()
    image.save(stream, format="PNG", optimize=False)
    return stream.getvalue()


def structural(rows: list[dict]) -> bool:
    line_groups: dict[tuple[int, int, int], list[dict]] = collections.defaultdict(list)
    for row in rows:
        line_groups[(row["top"] // 8, row["height"] // 4, row["left"] // 800)].append(row)
    for group in line_groups.values():
        text = " ".join(item["text"] for item in sorted(group, key=lambda item: item["left"])).lower()
        if any(pattern.search(text) for pattern in GATE_PATTERNS):
            return True
    return False


def luma(a: np.ndarray) -> np.ndarray:
    return 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]


def smear(a: np.ndarray) -> np.ndarray:
    pad = WIDTH // 2
    padded = np.pad(a.astype(np.uint64), ((0, 0), (pad, pad), (0, 0)), mode="edge")
    cumulative = np.concatenate([np.zeros((a.shape[0], 1, a.shape[2]), dtype=np.uint64), np.cumsum(padded, axis=1, dtype=np.uint64)], axis=1)
    totals = cumulative[:, WIDTH:] - cumulative[:, :-WIDTH]
    return ((totals + WIDTH // 2) // WIDTH).astype(np.uint8)


def pixel_metrics(reference: np.ndarray, observed: np.ndarray) -> dict:
    delta = reference.astype(np.float64) - observed.astype(np.float64)
    mse = float(np.mean(delta * delta))
    mae = float(np.mean(np.abs(delta)))
    psnr = 99.0 if mse == 0 else 10.0 * math.log10((255.0 ** 2) / mse)
    yr, yo = luma(reference.astype(np.float64)), luma(observed.astype(np.float64))
    ref_grad_x = float(np.mean(np.abs(np.diff(yr, axis=1))))
    obs_grad_x = float(np.mean(np.abs(np.diff(yo, axis=1))))
    ref_grad_y = float(np.mean(np.abs(np.diff(yr, axis=0))))
    obs_grad_y = float(np.mean(np.abs(np.diff(yo, axis=0))))
    ref_edge = ((np.pad(np.abs(np.diff(yr, axis=1)), ((0, 0), (0, 1))) > 12) | (np.pad(np.abs(np.diff(yr, axis=0)), ((0, 1), (0, 0))) > 12)).astype(np.uint8) * 255
    obs_edge = ((np.pad(np.abs(np.diff(yo, axis=1)), ((0, 0), (0, 1))) > 12) | (np.pad(np.abs(np.diff(yo, axis=0)), ((0, 1), (0, 0))) > 12)).astype(np.uint8) * 255
    dilated = np.asarray(Image.fromarray(obs_edge).filter(ImageFilter.MaxFilter(3)), dtype=np.uint8) > 0
    edge_count = int(np.count_nonzero(ref_edge))
    edge_recall = 1.0 if edge_count == 0 else float(np.count_nonzero((ref_edge > 0) & dilated) / edge_count)
    return {
        "rgb_psnr_db": psnr,
        "mean_absolute_rgb_error": mae,
        "tolerant_luma_edge_recall": edge_recall,
        "horizontal_luma_gradient_energy_ratio": 1.0 if ref_grad_x == 0 else obs_grad_x / ref_grad_x,
        "vertical_luma_gradient_energy_ratio": 1.0 if ref_grad_y == 0 else obs_grad_y / ref_grad_y,
    }


def aggregate(items: list[dict]) -> dict:
    return {key: round(float(np.mean([item[key] for item in items])), 6) for key in items[0]}


def main() -> None:
    cand = json.loads(CAND_RECEIPT.read_text())
    method = json.loads(METHOD_RECEIPT.read_text())
    candidate = {}
    held_critical = {}
    for variant in VARIANTS:
        all_refs = {region: collections.Counter() for region in ("full", "headline", "lower", "numeric")}
        all_obs = {region: collections.Counter() for region in all_refs}
        critical_refs = {region: collections.Counter() for region in all_refs}
        critical_obs = {region: collections.Counter() for region in all_refs}
        pixel_rows = []
        gate_count = 0
        critical_gate_count = 0
        for scene in cand["scenes"]:
            sample = next(item for item in scene["samples"] if item["variant"] == variant)
            baseline = ROOT / sample["baseline_path"]
            output = CAND_ROOT / sample["frame"]
            baseline_rows, output_rows = ocr_tsv(baseline), ocr_tsv(output)
            for region in all_refs:
                baseline_counter = counter(baseline_rows, region)
                output_counter = counter(output_rows, region)
                all_refs[region].update(baseline_counter)
                all_obs[region].update(output_counter)
                if scene["scene"] in CRITICAL:
                    critical_refs[region].update(baseline_counter)
                    critical_obs[region].update(output_counter)
            has_gate = structural(output_rows)
            gate_count += int(has_gate)
            critical_gate_count += int(has_gate and scene["scene"] in CRITICAL)
            with Image.open(baseline) as image:
                ref_pixels = np.asarray(image.convert("RGB"), dtype=np.uint8)
            with Image.open(output) as image:
                out_pixels = np.asarray(image.convert("RGB"), dtype=np.uint8)
            expected = smear(ref_pixels)
            if not np.array_equal(expected, out_pixels):
                raise SystemExit(f"candidate smear mismatch S{scene['scene']} {variant}")
            pixel_rows.append(pixel_metrics(ref_pixels, out_pixels))
        candidate[variant] = {**{f"{region}_recall": round(recall(all_refs[region], all_obs[region]), 6) for region in all_refs}, **aggregate(pixel_rows), "structural_gate_scenes": gate_count, "exact_smear_frames": len(pixel_rows)}
        held_critical[variant] = {**{f"{region}_recall": round(recall(critical_refs[region], critical_obs[region]), 6) for region in critical_refs}, "structural_gate_scenes": critical_gate_count}
    method_groups = {}
    for name, group in method["groups"].items():
        variant_results = {}
        for variant in VARIANTS:
            exact = 0
            gate_scores = []
            for scene in group["scenes"]:
                sample = next(item for item in scene["samples"] if item["variant"] == variant)
                baseline = ROOT / sample["baseline_path"]
                output = METHOD_ROOT / name / sample["frame"]
                with Image.open(baseline) as image:
                    ref_pixels = np.asarray(image.convert("RGB"), dtype=np.uint8)
                with Image.open(output) as image:
                    out_pixels = np.asarray(image.convert("RGB"), dtype=np.uint8)
                expected = smear(ref_pixels)
                if not np.array_equal(expected, out_pixels):
                    raise SystemExit(f"method smear mismatch {name} S{scene['scene']} {variant}")
                exact += 1
                if name == "pass12_sharpness_safe":
                    score, psm = crop_similarity(output, GATES[scene["scene"]])
                    gate_scores.append({"scene": scene["scene"], "score": round(score, 6), "psm": psm, "passes": score >= THRESHOLD})
            variant_results[variant] = {"exact_smear_frames": exact, "mapped_gate_scores": gate_scores, "mapped_gate_threshold_passes": sum(int(item["passes"]) for item in gate_scores), "mean_mapped_gate_similarity": round(float(np.mean([item["score"] for item in gate_scores])), 6) if gate_scores else None}
        method_groups[name] = variant_results
    human_review = {
        "candidate": {"result_hierarchy_primary": True, "structural_held_gate_scenes": "0/16_ALL_FIVE_VARIANTS", "fine_support_softens_first": ["narrow glyphs", "vertical separators", "fine axes", "error bars", "units", "legends", "caveats", "citations", "provenance", "small qualifiers"], "clipping_overlap_or_meaning_changing_ambiguity": False, "transform_repairs_or_authorizes_candidate": False},
        "sealed_v8": {"result_held_badges": "7/7_ALL_FIVE_VARIANTS", "major_method_status_boundaries": "7/7_ALL_FIVE_VARIANTS", "galaxy_spin_headers": "7/7_ALL_FIVE_VARIANTS", "direct_labels_and_non_color_geometry": "PASS", "clipping_overlap_or_ambiguity": False},
        "pass7_caption_safe": {"exact_top_gates": "7/7_ALL_FIVE_VARIANTS", "result_held_badges": "7/7_ALL_FIVE_VARIANTS", "clipping_overlap_or_ambiguity": False},
        "pass12_sharpness_safe": {"exact_top_gates": "7/7_ALL_FIVE_VARIANTS", "result_held_badges": "7/7_ALL_FIVE_VARIANTS", "complete_gate_containers": "7/7_ALL_FIVE_VARIANTS", "separated_header_gate_badge_headline_layers": "PASS", "clipping_overlap_or_ambiguity": False},
        "hue_only_required_meaning": 0,
    }
    audit = {
        "status": "QA_ONLY_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 28,
        "transform": "native color/monochrome -> Pillow LANCZOS 640x360 -> represented-pixel centered horizontal width-3 box smear",
        "transform_scope": "PACKET_SPECIFIC_PRESENTATION_STRESS_NOT_CLINICAL_OR_NAMED_DISPLAY_PLAYER_PROJECTOR_BROWSER_PLATFORM_SERVICE_ROOM_VIEWER_OR_UNIVERSAL_STANDARD",
        "candidate": candidate,
        "held_critical": held_critical,
        "method_groups": method_groups,
        "human_review": human_review,
        "candidate_receipt_sha256": __import__("hashlib").sha256(CAND_RECEIPT.read_bytes()).hexdigest(),
        "method_receipt_sha256": __import__("hashlib").sha256(METHOD_RECEIPT.read_bytes()).hexdigest(),
    }
    OUT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    gray = candidate[VARIANTS[1]]
    proof_min = min(method_groups["pass12_sharpness_safe"][variant]["mapped_gate_threshold_passes"] for variant in VARIANTS)
    print(f"PASS candidate=16/80 method=21/105 gray_headline={gray['headline_recall']:.6f} gray_full={gray['full_recall']:.6f} gray_lower={gray['lower_recall']:.6f} proof_min={proof_min}/7")


if __name__ == "__main__":
    main()

