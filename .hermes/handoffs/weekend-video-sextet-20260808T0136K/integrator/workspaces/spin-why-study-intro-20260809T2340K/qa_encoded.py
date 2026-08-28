#!/usr/bin/env python3
"""Run post-encode media, motion, OCR, frame, and lineage QA on the local canary."""
from __future__ import annotations

import hashlib
import json
import math
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageStat

ROOT = Path(__file__).resolve().parent
VIDEO = ROOT / "spin-method-overhaul-canary-20260809T2340K.mp4"
PREDECESSOR = ROOT.parents[1] / "canaries/spin-method-overhaul-canary-20260808T1959K"
TIMELINE_PATH = ROOT / "audio_v4" / "timeline.json"
SCRIPT_PATH = ROOT / "narration_script_v4.json"
BUILD_RECEIPT = ROOT / "build_receipt.json"
OUT = ROOT / "encoded_qa"
FRAMES = OUT / "frames"
CONTACT = ROOT / "encoded-contact-sheet-v4.jpg"
REPORT = ROOT / "encoded_qa.json"
OCR_PATH = OUT / "ocr.txt"
ASR_REPORT = OUT / "encoded-why-study-introduction-transcription-v4.json"
FONT_PATH = "/System/Library/Fonts/Avenir Next.ttc"


def run(command: list[str], check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(command, check=check, capture_output=True)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_frame(time_seconds: float, output: Path) -> None:
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-ss",
            f"{time_seconds:.6f}",
            "-i",
            str(VIDEO),
            "-frames:v",
            "1",
            "-q:v",
            "1",
            str(output),
        ]
    )


def make_contact_sheet(items: list[tuple[str, float, Path]]) -> None:
    cols = 6
    thumb_w, thumb_h, label_h = 320, 180, 30
    rows = math.ceil(len(items) / cols)
    sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), (5, 8, 14))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.truetype(FONT_PATH, 16)
    for index, (label, time_seconds, path) in enumerate(items):
        x = (index % cols) * thumb_w
        y = (index // cols) * (thumb_h + label_h)
        with Image.open(path) as image:
            thumb = ImageOps.fit(image.convert("RGB"), (thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(thumb, (x, y))
        line = f"{label} · {time_seconds:06.2f}s"
        box = draw.textbbox((0, 0), line, font=font)
        draw.text((x + (thumb_w - (box[2] - box[0])) / 2, y + thumb_h + 5), line, font=font, fill=(240, 245, 250))
    sheet.save(CONTACT, quality=94, subsampling=0)


def motion_metrics() -> dict:
    width, height = 160, 90
    frame_bytes = width * height
    process = subprocess.Popen(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(VIDEO),
            "-vf",
            f"fps=2,scale={width}:{height},format=gray",
            "-f",
            "rawvideo",
            "pipe:1",
        ],
        stdout=subprocess.PIPE,
    )
    assert process.stdout is not None
    previous = None
    differences: list[float] = []
    while True:
        payload = process.stdout.read(frame_bytes)
        if not payload:
            break
        if len(payload) != frame_bytes:
            raise RuntimeError("partial raw frame in motion QA")
        if previous is not None:
            differences.append(sum(abs(a - b) for a, b in zip(previous, payload)) / frame_bytes)
        previous = payload
    if process.wait() != 0:
        raise RuntimeError("motion decode failed")
    near_threshold = 0.08
    longest = current = 0
    for value in differences:
        if value < near_threshold:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    ordered = sorted(differences)
    return {
        "sample_rate_fps": 2,
        "sample_count": len(differences) + 1,
        "mean_abs_luma_difference": sum(differences) / len(differences),
        "minimum_abs_luma_difference": min(differences),
        "p05_abs_luma_difference": ordered[max(0, round(0.05 * (len(ordered) - 1)))],
        "median_abs_luma_difference": ordered[len(ordered) // 2],
        "maximum_abs_luma_difference": max(differences),
        "near_unchanged_threshold": near_threshold,
        "longest_near_unchanged_seconds": longest / 2,
    }


def parse_loudness() -> dict:
    measured = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostats",
            "-i",
            str(VIDEO),
            "-map",
            "0:a:0",
            "-af",
            "loudnorm=I=-16:LRA=7:TP=-2.3:print_format=json",
            "-f",
            "null",
            "-",
        ]
    )
    stderr = measured.stderr.decode("utf-8", "replace")
    match = re.search(r"\{\s*\"input_i\".*?\}", stderr, re.S)
    if not match:
        raise RuntimeError("could not parse encoded loudness")
    return json.loads(match.group(0))


def freeze_and_silence() -> dict:
    freeze = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-i",
            str(VIDEO),
            "-vf",
            "freezedetect=n=0.001:d=8",
            "-an",
            "-f",
            "null",
            "-",
        ]
    ).stderr.decode("utf-8", "replace")
    silence = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-i",
            str(VIDEO),
            "-map",
            "0:a:0",
            "-af",
            "silencedetect=n=-45dB:d=2",
            "-f",
            "null",
            "-",
        ]
    ).stderr.decode("utf-8", "replace")
    return {
        "freeze_events_at_least_8_seconds": re.findall(r"freeze_duration:\s*([0-9.]+)", freeze),
        "silence_starts": [float(x) for x in re.findall(r"silence_start:\s*([0-9.]+)", silence)],
        "silence_ends": [float(x) for x in re.findall(r"silence_end:\s*([0-9.]+)", silence)],
        "silence_durations": [float(x) for x in re.findall(r"silence_duration:\s*([0-9.]+)", silence)],
    }


def ocr_frames(items: list[tuple[str, float, Path]]) -> dict:
    blocks = []
    for label, time_seconds, path in items:
        result = run(["tesseract", str(path), "stdout", "--psm", "6"], check=False)
        text = result.stdout.decode("utf-8", "replace")
        blocks.append(f"### {label} {time_seconds:.3f}s\n{text.strip()}\n")
    joined = "\n".join(blocks)
    OCR_PATH.write_text(joined)
    lower = joined.lower()
    forbidden_words = ["grb", "quasar", "desi", "ganalyzer"]
    forbidden_phrases = [
        "sn ia",
        "dark energy",
        "black hole",
        "observed asymmetry",
        "statistically significant",
        "the universe is anisotropic",
        "parity is violated",
    ]
    internal_markers = ["frontend/public", "/users/", ".json", ".md"]
    word_hits = [
        term
        for term in forbidden_words
        if re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", lower)
    ]
    phrase_hits = [
        term
        for term in forbidden_phrases
        if re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", lower)
    ]
    return {
        "text_path": str(OCR_PATH.relative_to(ROOT)),
        "forbidden_hits": word_hits + phrase_hits + [term for term in internal_markers if term in lower],
        "characters": len(joined),
    }


def main() -> int:
    if not VIDEO.is_file() or not BUILD_RECEIPT.is_file():
        raise FileNotFoundError("render or build receipt is missing")
    OUT.mkdir(parents=True, exist_ok=True)
    FRAMES.mkdir(parents=True, exist_ok=True)
    timeline = json.loads(TIMELINE_PATH.read_text())
    script = json.loads(SCRIPT_PATH.read_text())
    build = json.loads(BUILD_RECEIPT.read_text())
    asr = json.loads(ASR_REPORT.read_text())
    probe = json.loads(
        run(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration,size,bit_rate:stream=index,codec_name,codec_type,width,height,r_frame_rate,avg_frame_rate,sample_rate,channels,bit_rate",
                "-of",
                "json",
                str(VIDEO),
            ]
        ).stdout.decode()
    )
    items: list[tuple[str, float, Path]] = []
    for record in timeline["records"]:
        time_seconds = (record["audio_start_seconds"] + record["audio_end_seconds"]) / 2
        path = FRAMES / f"{record['id']}-{time_seconds:07.3f}.jpg"
        exact_frame(time_seconds, path)
        items.append((record["id"], time_seconds, path))
    mirror = next(record for record in timeline["records"] if record["id"] == "s07")
    mirror_paths = []
    for index, q in enumerate((0.05, 0.25, 0.50, 0.75, 0.95), 1):
        time_seconds = mirror["audio_start_seconds"] + (mirror["audio_end_seconds"] - mirror["audio_start_seconds"]) * q
        path = FRAMES / f"mirror-{index}-{time_seconds:07.3f}.jpg"
        exact_frame(time_seconds, path)
        items.append((f"mirror-{index}", time_seconds, path))
        mirror_paths.append(path)
    make_contact_sheet(items)

    video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
    audio_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "audio"]
    duration = float(probe["format"]["duration"])
    frame_stats = []
    for label, time_seconds, path in items:
        with Image.open(path) as image:
            stat = ImageStat.Stat(image.convert("L"))
            frame_stats.append({"label": label, "time": time_seconds, "mean_luma": stat.mean[0], "sha256": sha256(path)})
    mirror_unique = len({sha256(path) for path in mirror_paths})
    loudness = parse_loudness()
    stability = freeze_and_silence()
    motion = motion_metrics()
    ocr = ocr_frames(items)

    narration = " ".join(item["text"] for item in script["sentences"]).lower()
    semantic_assertions = [
        "we find an asymmetry",
        "we found an asymmetry",
        "this study finds an asymmetry",
        "there is a preferred direction",
        "the universe is anisotropic",
        "parity is violated",
        "observed asymmetry",
        "statistically significant",
        "black hole",
    ]
    semantic_hits = [term for term in semantic_assertions if term in narration]
    opening = script["sentences"][:6]
    opening_text = " ".join(item["text"] for item in opening).lower()
    longo = (
        "A preference for spiral galaxies in one sector of the sky to be left-handed or right-handed spirals "
        "would indicate a parity violating asymmetry in the overall universe and a preferred axis."
    )
    renderer_source = (ROOT / "build.py").read_text()
    section_intervals = {}
    for section in {item["section"] for item in timeline["records"]}:
        records = [item for item in timeline["records"] if item["section"] == section]
        section_intervals[section] = max(item["audio_end_seconds"] for item in records) - min(
            item["audio_start_seconds"] for item in records
        )
    mirror_interval = section_intervals["mirror-climax"]
    checks = {
        "exactly_one_video_stream": len(video_streams) == 1,
        "exactly_one_audio_stream": len(audio_streams) == 1,
        "h264_video": len(video_streams) == 1 and video_streams[0]["codec_name"] == "h264",
        "aac_audio": len(audio_streams) == 1 and audio_streams[0]["codec_name"] == "aac",
        "resolution_1920x1080": len(video_streams) == 1 and video_streams[0].get("width") == 1920 and video_streams[0].get("height") == 1080,
        "fps_30": len(video_streams) == 1 and video_streams[0].get("avg_frame_rate") == "30/1",
        "duration_matches_audio_within_one_frame": abs(duration - timeline["master_duration_seconds"]) <= 1 / 30 + 0.002,
        "delivered_wpm_105_to_125": 105 <= timeline["delivered_wpm"] <= 125,
        "audio_visual_action_delta_within_0_3s": timeline["max_abs_audio_visual_start_delta_seconds"] <= 0.3,
        "all_29_sentence_frames_nonblack": len(frame_stats) >= 29 and all(item["mean_luma"] > 8 for item in frame_stats[:29]),
        "five_beat_introduction_is_first": [item["id"] for item in opening] == ["i01", "i02", "i03", "i04", "i05", "i06"],
        "opening_required_terms_present": all(
            term in opening_text
            for term in (
                "same in every direction",
                "no built-in preference",
                "angular momentum",
                "balance is the prediction",
                "would indicate",
                "preferred axis",
                "left unsettled",
                "sorting bias",
                "mirror control",
            )
        ),
        "opening_beats_remain_separate": [item.get("beat") for item in opening]
        == ["expectation", "expectation", "tidal-torque", "conditional-stakes", "open-question", "catch-and-handoff"],
        "long_source_directional_sentence_is_verbatim": opening[3]["text"] == longo,
        "long_source_stakes_remain_conditional": "would indicate" in opening[3]["text"].lower(),
        "open_question_adopts_no_answer": "left unsettled" in opening[4]["text"].lower() and "adopts no answer" in opening[4]["text"].lower(),
        "broad_reason_precedes_sorting_method": opening[0]["beat"] == "expectation" and opening[5]["beat"] == "catch-and-handoff",
        "five_unique_encoded_mirror_positions": mirror_unique == 5,
        "no_freeze_event_8s": not stability["freeze_events_at_least_8_seconds"],
        "motion_near_unchanged_run_under_8s": motion["longest_near_unchanged_seconds"] < 8,
        "encoded_integrated_loudness_in_governing_band": -21.8 <= float(loudness["input_i"]) <= -19.0,
        "encoded_true_peak_no_clipping": float(loudness["input_tp"]) <= -1.0,
        "no_forbidden_narration_terms": not semantic_hits,
        "no_forbidden_or_internal_filename_ocr_hits": not ocr["forbidden_hits"],
        "forbidden_icon_primitives_contract_present": script.get("forbidden_icon_primitives") == ["curve"],
        "generic_curve_dispatch_absent": re.search(r"elif\s+kind\s*==\s*['\"]curve['\"]\s*:", renderer_source) is None,
        "local_breathing_rail_focus_present": all(token in renderer_source for token in ("focus_left", "focus_right", "glow =", "9 + int(round(math.sin(math.pi * t)))")),
        "encoded_why_study_intro_asr_exact": asr["status"] == "PASS" and asr["normalized_similarity"] >= 0.99 and all(asr["checks"].values()),
        "build_receipt_hash_matches_video": build["output_sha256"] == sha256(VIDEO),
        "build_receipt_audio_matches_timeline": build["audio_master_sha256"] == timeline["master_sha256"],
        "predecessor_mp4_preserved": sha256(PREDECESSOR / "spin-method-overhaul-canary-20260808T1959K.mp4") == "c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240",
        "predecessor_script_v3_preserved": sha256(PREDECESSOR / "narration_script_v3.json") == "1865f96b334a44499c58b6fdf545e140110bde2680ed202593dda2bd3a121f8b",
    }
    report = {
        "candidate": ROOT.name,
        "status": "PENDING_TORI_EXACT_HASH_REGATE" if all(checks.values()) else "MACHINE_QA_HOLD",
        "video": str(VIDEO.relative_to(ROOT)),
        "video_sha256": sha256(VIDEO),
        "probe": probe,
        "timeline": {
            "sentence_count": timeline["sentence_count"],
            "word_count": timeline["word_count"],
            "delivered_wpm": timeline["delivered_wpm"],
            "master_duration_seconds": timeline["master_duration_seconds"],
            "max_alignment_delta_seconds": timeline["max_abs_audio_visual_start_delta_seconds"],
        },
        "loudness": loudness,
        "stability": stability,
        "motion": motion,
        "frame_stats": frame_stats,
        "mirror_unique_frame_hashes": mirror_unique,
        "ocr": ocr,
        "semantic_narration_hits": semantic_hits,
        "encoded_why_study_intro_asr": asr,
        "section_intervals_seconds": section_intervals,
        "checks": checks,
        "contact_sheet": str(CONTACT.relative_to(ROOT)),
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "checks": checks, "video_sha256": report["video_sha256"], "contact_sheet": str(CONTACT)}, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
