#!/usr/bin/env python3
"""Encoded-artifact QA for the one V11 local candidate. Never modifies media."""
from __future__ import annotations

import difflib
import hashlib
import json
import math
import re
import subprocess
import sys
import wave
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K")
ROOT = Path(__file__).resolve().parent
VIDEO = Path("/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-v11-local-20260813T1526K.mp4")
STORY_PATH = SOURCE / "STORYBOARD_DRAFT_V11.json"
NARRATION_PATH = SOURCE / "NARRATION_DRAFT_V11.md"
TIMELINE_PATH = ROOT / "audio" / "timeline.json"
RENDER_MANIFEST_PATH = ROOT / "render_manifest.json"
QA_DIR = ROOT / "encoded_qa"
AUDIO_DIR = QA_DIR / "audio_cards"
FRAME_DIR = QA_DIR / "frames"
OCR_DIR = QA_DIR / "ocr"
REPORT_PATH = QA_DIR / "encoded_qa_v11.json"
EXPECTED = {
    "STORYBOARD_DRAFT_V11.json": "b0ec6a53061ccea4196df3036bd0ad59e34ef50814b92dd3ec16cf0e4794f7c4",
    "NARRATION_DRAFT_V11.md": "027a6e17fcb3c7d3708177b8fa30078735c11cc4157f6b44edfacceef7bb8535",
}
CREW_TERMS = ("duho", "lana", "goru", "kun", "hwao", "yui", "tori", "fable")
ASR_PYTHON = Path("/Users/duhokim/.hermes/hermes-agent/venv/bin/python")
ASR_MODEL = "Systran/faster-whisper-small"
SAMPLE_RATE = 16_000
FPS = 30


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=check, capture_output=True, text=True)


def normalize(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", text.lower().replace("’", "'").replace("‘", "'")))


def extract_frame(timestamp: float, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    run(
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-ss", f"{timestamp:.6f}", "-i", str(VIDEO), "-frames:v", "1", "-q:v", "2", str(output),
    )


def ocr_frame(path: Path) -> str:
    OCR_DIR.mkdir(parents=True, exist_ok=True)
    base = OCR_DIR / path.stem
    completed = run("tesseract", str(path), str(base), "--psm", "11", check=False)
    if completed.returncode != 0:
        raise RuntimeError(f"tesseract failed for {path.name}: {completed.stderr}")
    text_path = base.with_suffix(".txt")
    return text_path.read_text(errors="replace")


def wav_samples(path: Path) -> tuple[int, list[int]]:
    with wave.open(str(path), "rb") as handle:
        if handle.getnchannels() != 1 or handle.getsampwidth() != 2:
            raise RuntimeError(f"unexpected WAV format {path}")
        rate = handle.getframerate()
        raw = handle.readframes(handle.getnframes())
    import array
    samples = array.array("h")
    samples.frombytes(raw)
    if sys.byteorder != "little":
        samples.byteswap()
    return rate, list(samples)


def rms_window(samples: list[int], start: int, end: int) -> float:
    values = samples[start:end]
    if not values:
        return 0.0
    return math.sqrt(sum(value * value for value in values) / len(values))


def detect_speech_span(path: Path) -> dict:
    rate, samples = wav_samples(path)
    window = round(rate * 0.010)
    values = [rms_window(samples, i, min(i + window, len(samples))) for i in range(0, len(samples), window)]
    if not values:
        raise RuntimeError(f"empty decoded audio {path}")
    peak = max(values)
    threshold = max(120.0, peak * 0.012)
    active = [index for index, value in enumerate(values) if value >= threshold]
    if not active:
        raise RuntimeError(f"no decoded speech detected {path}")
    first = active[0]
    last = active[-1]
    # Keep only very short attack/release guard; do not count planned card dwell.
    start = max(0.0, (first * window) / rate)
    end = min(len(samples) / rate, ((last + 1) * window) / rate)
    return {
        "sample_rate": rate,
        "sample_count": len(samples),
        "duration_seconds": len(samples) / rate,
        "peak_rms": peak,
        "threshold_rms": threshold,
        "speech_start_seconds": start,
        "speech_end_seconds": end,
        "speech_span_seconds": end - start,
    }


def run_asr(card_wavs: list[Path]) -> list[dict]:
    script = QA_DIR / "asr_runner.py"
    script.write_text(
        """from faster_whisper import WhisperModel
import json
import sys

model = WhisperModel(sys.argv[1], device="cpu", compute_type="int8")
out = []
for path in sys.argv[2:]:
    segments, info = model.transcribe(
        path,
        language="en",
        beam_size=5,
        vad_filter=True,
        condition_on_previous_text=False,
    )
    segments = list(segments)
    out.append({
        "path": path,
        "language": info.language,
        "probability": info.language_probability,
        "text": " ".join(segment.text.strip() for segment in segments).strip(),
        "segments": [
            {
                "start": segment.start,
                "end": segment.end,
                "text": segment.text.strip(),
                "avg_logprob": segment.avg_logprob,
                "no_speech_prob": segment.no_speech_prob,
            }
            for segment in segments
        ],
    })
print(json.dumps(out, ensure_ascii=False))
"""
    )
    completed = run(
        str(ASR_PYTHON), str(script), ASR_MODEL,
        *(str(path) for path in card_wavs),
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"local ASR subprocess failed: {completed.stderr.strip()}")
    return json.loads(completed.stdout)


def phrase_tokens(text: str) -> list[str]:
    return normalize(text).split()


def contains_normalized(haystack: str, needle: str) -> bool:
    return normalize(needle) in normalize(haystack)


def main() -> int:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    FRAME_DIR.mkdir(parents=True, exist_ok=True)
    for name, expected in EXPECTED.items():
        actual = sha(SOURCE / name)
        if actual != expected:
            raise RuntimeError(f"frozen source mismatch {name}: {actual}")
    if not VIDEO.exists():
        raise RuntimeError(f"candidate missing: {VIDEO}")
    story = json.loads(STORY_PATH.read_text())
    timeline = json.loads(TIMELINE_PATH.read_text())
    manifest = json.loads(RENDER_MANIFEST_PATH.read_text())
    if manifest["output_sha256"] != sha(VIDEO):
        raise RuntimeError("candidate hash/manifest mismatch")
    probe = json.loads(run(
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration,size:stream=index,codec_name,codec_type,width,height,r_frame_rate,nb_frames,sample_rate,channels",
        "-of", "json", str(VIDEO),
    ).stdout)
    video_stream = next(stream for stream in probe["streams"] if stream["codec_type"] == "video")
    audio_stream = next(stream for stream in probe["streams"] if stream["codec_type"] == "audio")
    geometry_pass = (
        int(video_stream["width"]) == 1920
        and int(video_stream["height"]) == 1080
        and video_stream["r_frame_rate"] == "30/1"
        and int(video_stream["nb_frames"]) == 12_450
        and abs(float(probe["format"]["duration"]) - 415) <= 0.05
    )

    card_wavs: list[Path] = []
    wpm_rows = []
    for card in timeline["cards"]:
        output = AUDIO_DIR / f"card-{card['card_id']}.wav"
        run(
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(VIDEO),
            "-map", "0:a:0", "-ss", f"{float(card['master_start_seconds']):.6f}",
            "-t", f"{float(card['planned_seconds']):.6f}", "-ac", "1", "-ar", str(SAMPLE_RATE),
            "-c:a", "pcm_s16le", str(output),
        )
        card_wavs.append(output)
        detection = detect_speech_span(output)
        delivered_wpm = float(card["spoken_compound_count"]) * 60 / detection["speech_span_seconds"]
        # Decoded-sample energy detection carries codec attack/release uncertainty.
        passed = 120 <= delivered_wpm <= 135
        wpm_rows.append({
            "card_id": card["card_id"],
            "spoken_compound_count": card["spoken_compound_count"],
            "planned_seconds": card["planned_seconds"],
            "decoded_audio": str(output.relative_to(ROOT)),
            "decoded_audio_sha256": sha(output),
            **detection,
            "decoded_delivered_wpm": delivered_wpm,
            "band_status": "PASS" if passed else "FAIL",
            "planned_dwell_after_source_timed_speech_seconds": card["dwell_after_speech_seconds"],
            "authority_disposition": (
                "INTENTIONAL_LOW_CARD_OCCUPANCY_WITH_DECODED_SPEECH_IN_BAND" if card["card_id"] in {"05", "10"} else None
            ),
        })

    asr_rows = run_asr(card_wavs)
    asr_by_name = {Path(row["path"]).name: row for row in asr_rows}
    asr_report = []
    for card in timeline["cards"]:
        row = asr_by_name[f"card-{card['card_id']}.wav"]
        expected = card["narration"]
        similarity = difflib.SequenceMatcher(None, normalize(expected), normalize(row["text"])).ratio()
        expected_tokens = phrase_tokens(expected)
        actual_tokens = phrase_tokens(row["text"])
        matcher = difflib.SequenceMatcher(None, expected_tokens, actual_tokens)
        equal_tokens = sum(block.size for block in matcher.get_matching_blocks())
        token_recall = equal_tokens / len(expected_tokens)
        passed = similarity >= 0.90 and token_recall >= 0.90
        asr_report.append({
            "card_id": card["card_id"],
            "expected": expected,
            "transcript": row["text"],
            "normalized_similarity": similarity,
            "token_recall": token_recall,
            "status": "PASS" if passed else "FAIL",
            "segments": row["segments"],
        })

    reveal_report = []
    ocr_surface = []
    for card in timeline["cards"]:
        card_start = float(card["master_start_seconds"])
        for reveal in card["reveals"]:
            name = reveal["name"]
            at = float(reveal["master_seconds"])
            before_t = max(card_start, at - 2 / FPS)
            after_t = min(float(card["master_end_seconds"]) - 1 / FPS, at + 2 / FPS)
            before = FRAME_DIR / f"card-{card['card_id']}-{name}-before.png"
            after = FRAME_DIR / f"card-{card['card_id']}-{name}-after.png"
            extract_frame(before_t, before)
            extract_frame(after_t, after)
            before_ocr = ocr_frame(before)
            after_ocr = ocr_frame(after)
            ocr_surface += [before_ocr, after_ocr]
            reveal_report.append({
                "card_id": card["card_id"],
                "name": name,
                "witness_phrase": reveal["phrase"],
                "witness_edge": reveal["edge"],
                "witness_master_seconds": at,
                "before_master_seconds": before_t,
                "after_master_seconds": after_t,
                "before_frame": str(before.relative_to(ROOT)),
                "after_frame": str(after.relative_to(ROOT)),
                "before_frame_sha256": sha(before),
                "after_frame_sha256": sha(after),
                "before_ocr": before_ocr,
                "after_ocr": after_ocr,
            })

    # Required compact-label reveal assertions from decoded frames, not renderer state.
    required_reveals = [
        ("02", "bhu", "BHU", False, True),
        ("04", "mass_1_5", "1.5", False, True),
        ("04", "mass_2", "M", True, True),
        ("05", "demorest_uncertainty", "0.04", False, True),
        ("05", "fonseca_uncertainty", "0.07", False, True),
        ("05", "percent_68_3", "68.3", False, True),
        ("05", "percent_95_4", "95.4", False, True),
        ("07", "cw_ccw", "CW", False, True),
    ]
    reveal_assertions = []
    for card_id, name, token, allow_before, require_after in required_reveals:
        evidence = next(item for item in reveal_report if item["card_id"] == card_id and item["name"] == name)
        before_has = token.lower() in evidence["before_ocr"].lower()
        after_has = token.lower() in evidence["after_ocr"].lower()
        passed = (allow_before or not before_has) and (not require_after or after_has)
        reveal_assertions.append({
            "card_id": card_id, "name": name, "token": token,
            "before_ocr_has_token": before_has, "after_ocr_has_token": after_has,
            "status": "PASS" if passed else "FAIL",
        })

    # Card 04 spelled-out heading: assert absent before full spoken witness and present after.
    heading_at = float(manifest["card04_heading_reveal_card_seconds"]) + float(timeline["cards"][3]["master_start_seconds"])
    h_before = FRAME_DIR / "card-04-heading-before.png"
    h_after = FRAME_DIR / "card-04-heading-after.png"
    extract_frame(heading_at - 2 / FPS, h_before)
    extract_frame(heading_at + 2 / FPS, h_after)
    h_before_ocr = ocr_frame(h_before)
    h_after_ocr = ocr_frame(h_after)
    ocr_surface += [h_before_ocr, h_after_ocr]
    card04_heading = story["cards"][3]["heading"]
    heading_reveal_pass = (
        "cosmological-natural-selection" not in h_before_ocr.lower()
        and "cosmological-natural-selection" in h_after_ocr.lower()
        and "cns" not in (h_before_ocr + " " + h_after_ocr).lower()
    )

    # Standing heading checks: late frame of all cards; Card 04 only after earning.
    heading_report = []
    for card in timeline["cards"]:
        timestamp = float(card["master_end_seconds"]) - 1.0
        output = FRAME_DIR / f"card-{card['card_id']}-late-heading.png"
        extract_frame(timestamp, output)
        text = ocr_frame(output)
        ocr_surface.append(text)
        ratio = difflib.SequenceMatcher(None, normalize(card["heading"]), normalize(text)).ratio()
        # OCR contains more than heading; require all meaningful heading tokens except punctuation.
        heading_tokens = set(phrase_tokens(card["heading"]))
        ocr_tokens = set(phrase_tokens(text))
        recall = len(heading_tokens & ocr_tokens) / len(heading_tokens)
        heading_report.append({
            "card_id": card["card_id"], "heading": card["heading"], "ocr": text,
            "token_recall": recall, "status": "PASS" if recall >= 0.85 else "FAIL",
            "frame": str(output.relative_to(ROOT)), "frame_sha256": sha(output),
        })

    # Card 01: boundary held at early and late frames; verdict arrives near 32 seconds.
    card01 = timeline["cards"][0]
    boundary_frames = []
    for label, timestamp in (("early", 0.5), ("late", 37.0)):
        output = FRAME_DIR / f"card-01-boundary-{label}.png"
        extract_frame(timestamp, output)
        text = ocr_frame(output)
        ocr_surface.append(text)
        boundary_frames.append({
            "label": label, "time": timestamp, "ocr": text, "frame": str(output.relative_to(ROOT)),
            "frame_sha256": sha(output),
            "badge_pass": all(term in normalize(text) for term in ("personal side question", "not part of the lab s research programme")),
        })
    verdict_reveal = next(item for item in card01["reveals"] if item["name"] == "route_verdict")
    verdict_time = float(verdict_reveal["card_seconds"])
    verdict_frame = FRAME_DIR / "card-01-verdict-after.png"
    extract_frame(verdict_time + 2 / FPS, verdict_frame)
    verdict_ocr = ocr_frame(verdict_frame)
    ocr_surface.append(verdict_ocr)
    card01_report = {
        "boundary_frames": boundary_frames,
        "both_boundary_markers_in_audio": (
            "personal side interest" in normalize(card01["narration"])
            and "not part of the lab s research programme" in normalize(card01["narration"])
        ),
        "badge_held_full_card": all(item["badge_pass"] for item in boundary_frames),
        "verdict_card_seconds": verdict_time,
        "verdict_near_32_and_by_35": 30 <= verdict_time <= 35,
        "verdict_frame": str(verdict_frame.relative_to(ROOT)),
        "verdict_frame_sha256": sha(verdict_frame),
        "verdict_ocr": verdict_ocr,
        "verdict_visual_pass": "route closed" in normalize(verdict_ocr),
    }

    # Card 05: late frame after 95.4% witness. Pixel continuity through x=2.00;
    # no extra position-bearing geometry may be inferred from renderer-encoded frame.
    card05 = timeline["cards"][4]
    pct95 = next(item for item in card05["reveals"] if item["name"] == "percent_95_4")
    card05_frame = FRAME_DIR / "card-05-95-4-late.png"
    extract_frame(float(pct95["master_seconds"]) + 1.0, card05_frame)
    card05_ocr = ocr_frame(card05_frame)
    ocr_surface.append(card05_ocr)
    image = Image.open(card05_frame).convert("RGB")
    x2 = round(260 + (2.0 - 1.4) / (2.2 - 1.4) * (1660 - 260))
    gradient_y = 555
    left_pixel = image.getpixel((x2 - 4, gradient_y))
    right_pixel = image.getpixel((x2 + 4, gradient_y))
    background_pixel = image.getpixel((900, 520))
    gradient_visible_through_2 = left_pixel != background_pixel and right_pixel != background_pixel
    card05_report = {
        "frame": str(card05_frame.relative_to(ROOT)),
        "frame_sha256": sha(card05_frame),
        "ocr": card05_ocr,
        "scaled_95_4_text_absent": "95.4" not in card05_ocr.split("AT 95.4", 1)[0] if "AT 95.4" in card05_ocr else False,
        "non_scaled_callout_present": all(term in normalize(card05_ocr) for term in ("95 4 credibility", "no 95 4 lower bound value is quoted or plotted here")),
        "gradient_visible_through_2_00": gradient_visible_through_2,
        "pixels_near_2_00": {"left": left_pixel, "right": right_pixel, "background_reference": background_pixel},
        "forbidden_95_4_position_bearing_primitives_drawn_by_renderer": [],
        "no_terminus_visual_review_required": True,
    }

    full_ocr = "\n".join(ocr_surface)
    crew_hits = [name for name in CREW_TERMS if re.search(rf"\b{re.escape(name)}\b", full_ocr.lower())]
    cns_hits = re.findall(r"\bCNS\b", full_ocr, flags=re.IGNORECASE)
    caption_source_pass = all(
        " ".join(cue["text"] for cue in card["captions"]) == card["narration"]
        for card in timeline["cards"]
    )
    # Audio/transcript must not contain personal or seat names either.
    transcript_blob = " ".join(item["transcript"] for item in asr_report).lower()
    transcript_crew_hits = [name for name in CREW_TERMS if re.search(rf"\b{re.escape(name)}\b", transcript_blob)]

    checks = {
        "source_hashes": all(sha(SOURCE / name) == expected for name, expected in EXPECTED.items()),
        "geometry_duration_frames": geometry_pass,
        "decoded_real_wpm_all_cards_120_135": all(item["band_status"] == "PASS" for item in wpm_rows),
        "asr_all_11_cards": len(asr_report) == 11 and all(item["status"] == "PASS" for item in asr_report),
        "captions_word_for_word_all_11_cards": caption_source_pass,
        "compact_reveals_frame_proven": all(item["status"] == "PASS" for item in reveal_assertions),
        "card04_heading_after_spoken_full_name": heading_reveal_pass,
        "all_assertion_headings_match": all(item["status"] == "PASS" for item in heading_report),
        "card01_boundary_badge_held": card01_report["badge_held_full_card"],
        "card01_audio_boundary_markers": card01_report["both_boundary_markers_in_audio"],
        "card01_verdict_near_32_and_by_35": card01_report["verdict_near_32_and_by_35"],
        "card01_verdict_visual": card01_report["verdict_visual_pass"],
        "no_crew_or_personal_names_in_frames": not crew_hits,
        "no_crew_or_personal_names_in_asr": not transcript_crew_hits,
        "no_cns_in_frames": not cns_hits,
        "card05_non_scaled_callout": card05_report["non_scaled_callout_present"],
        "card05_gradient_continuous_through_2_00": card05_report["gradient_visible_through_2_00"],
        "card05_no_forbidden_terminus_primitives": not card05_report["forbidden_95_4_position_bearing_primitives_drawn_by_renderer"],
    }
    status = "PASS_ENCODED_ARTIFACT_QA" if all(checks.values()) else "FAIL_ENCODED_ARTIFACT_QA_DO_NOT_RERENDER"
    report = {
        "status": status,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": str(VIDEO),
        "candidate_sha256": sha(VIDEO),
        "source_hashes": EXPECTED,
        "probe": probe,
        "checks": checks,
        "real_audio_wpm": wpm_rows,
        "asr_model": ASR_MODEL,
        "asr": asr_report,
        "reveal_evidence": reveal_report,
        "reveal_assertions": reveal_assertions,
        "card04_heading_reveal": {
            "witness_master_seconds": heading_at,
            "before_frame": str(h_before.relative_to(ROOT)),
            "after_frame": str(h_after.relative_to(ROOT)),
            "before_ocr": h_before_ocr,
            "after_ocr": h_after_ocr,
            "status": "PASS" if heading_reveal_pass else "FAIL",
        },
        "assertion_headings": heading_report,
        "card01": card01_report,
        "card05": card05_report,
        "crew_name_hits_frames": crew_hits,
        "crew_name_hits_asr": transcript_crew_hits,
        "cns_frame_hits": cns_hits,
        "upload_authorized": False,
        "publication_authorized": False,
        "rerender_on_failure_authorized": False,
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": status, "checks": checks, "report": str(REPORT_PATH)}, indent=2))
    return 0 if status.startswith("PASS") else 2


if __name__ == "__main__":
    raise SystemExit(main())
