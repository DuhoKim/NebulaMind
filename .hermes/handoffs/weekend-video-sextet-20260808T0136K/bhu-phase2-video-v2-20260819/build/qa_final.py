#!/usr/bin/env python3
"""Full final-MP4 ASR, visual, caption, plot, and media QA for v2."""
from __future__ import annotations

import difflib
import json
import math
import mimetypes
import re
import secrets
import subprocess
import sys
import time
import unicodedata
import urllib.request
from pathlib import Path
from typing import Any

from PIL import Image, ImageChops, ImageOps, ImageStat

import assemble
import pipeline

HERMES_CHECKOUT = Path("/Users/duhokim/.hermes/hermes-agent")
ASR_MODEL = "whisper-1"

CONTRACT_PHRASES = {
    "01": [
        "Even the most generous signal is about 10,000 to 100,000 times below the best possible galaxy-counting test.",
        "The inheritance route now exists as a ceiling, and the route stays closed.",
    ],
    "03": ["The printed value sits near the lined-up edge, so we carry both."],
    "08": [
        "Across all 4 papers, no equation carries the parent's spin through the bounce; the collapse papers mention it in exactly 1 sentence: “It would still be valid for a more realistic gravitational collapse of an inhomogeneous and rotating fluid.”",
    ],
    "09": ["And if a spinning parent can't make their bounce at all, there is even less to see."],
    "11": ["One honest caveat: both bounces sit in the Planck regime treated classically, and the strict chain awaits external theorist review."],
    "12": ["The strongest inheritance route now exists on the record as a ceiling, and the ceiling says the route stays closed."],
}

NUMBER_PHRASES = [
    ("one hundred thousand", "100000"), ("a hundred thousand", "100000"),
    ("ten thousand", "10000"), ("seven hundred and thirty", "730"), ("seven hundred thirty", "730"),
    ("forty five", "45"), ("twenty seven", "27"), ("twenty six", "26"),
    ("six point six", "6.6"), ("two trillion", "2 trillion"), ("one order", "1 order"),
    ("twenty ten", "2010"), ("two thousand and ten", "2010"), ("two thousand ten", "2010"),
    ("twenty twelve", "2012"), ("two thousand and twelve", "2012"), ("two thousand twelve", "2012"),
    ("twenty twenty five", "2025"), ("two thousand and twenty five", "2025"), ("two thousand twenty five", "2025"),
    ("ten mega electron volts", "10 megaelectronvolts"), ("mega electron volts", "megaelectronvolts"),
]
NUMBER_WORDS = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
}
FORBIDDEN_PHRASES = ["bhu is false", "bhu is impossible", "proved wrong", "refuted"]
COSMETIC_WORDS = {"a", "an", "the"}
PROPER_NAME_VARIANTS = {
    ("dutta", "data"), ("scherrer", "sherer"), ("scherrer", "scherer"), ("scherrer", "sharer"),
    ("cartan", "carton"),
}


def normalize_words(text: str) -> list[str]:
    normalized = unicodedata.normalize("NFKD", text).lower()
    normalized = "".join(char for char in normalized if not unicodedata.combining(char))
    normalized = normalized.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    normalized = re.sub(r"(?<=\d),(?=\d)", "", normalized)
    normalized = normalized.replace("×", " times ").replace("−", "-")
    normalized = re.sub(r"\bto the power of\b", "to the power", normalized)
    normalized = re.sub(r"\b(\d+) to the (\d+)(?:st|nd|rd|th) power\b", r"\1 to the power \2", normalized)
    normalized = re.sub(r"\b([a-z]+) to the ([a-z]+)(?:st|nd|rd|th) power\b", r"\1 to the power \2", normalized)
    normalized = re.sub(r"'s\b", "", normalized)
    normalized = re.sub(r"[–—-]", " ", normalized)
    normalized = re.sub(r"\bnebula\s+mind\b", "nebulamind", normalized)
    normalized = re.sub(r"\bbig\s+bang\b", "bigbang", normalized)
    normalized = re.sub(r"\bspace\s+time\b", "spacetime", normalized)
    normalized = re.sub(r"\bparents\b", "parent", normalized)
    normalized = re.sub(r"\bmega\s+electron\s+volts?\b", "megaelectronvolts", normalized)
    for phrase, replacement in NUMBER_PHRASES:
        normalized = re.sub(rf"\b{re.escape(phrase)}\b", replacement, normalized)
    for word, digit in NUMBER_WORDS.items():
        normalized = re.sub(rf"\b{word}\b", digit, normalized)
    return re.findall(r"[a-z0-9]+(?:\.[0-9]+)?", normalized)


def alignment(expected: str, transcript: str) -> list[dict[str, Any]]:
    expected_words = normalize_words(expected)
    transcript_words = normalize_words(transcript)
    matcher = difflib.SequenceMatcher(None, expected_words, transcript_words, autojunk=False)
    return [
        {"tag": tag, "expected_index": [i1, i2], "transcript_index": [j1, j2], "expected": expected_words[i1:i2], "transcript": transcript_words[j1:j2]}
        for tag, i1, i2, j1, j2 in matcher.get_opcodes()
        if tag != "equal"
    ]


def edit_distance(expected: list[str], transcript: list[str]) -> int:
    previous = list(range(len(transcript) + 1))
    for word in expected:
        current = [previous[0] + 1]
        for index, other in enumerate(transcript, 1):
            current.append(min(current[-1] + 1, previous[index] + 1, previous[index - 1] + (word != other)))
        previous = current
    return previous[-1]


def find_subsequence(haystack: list[str], needle: list[str]) -> int | None:
    if not needle:
        return 0
    for index in range(len(haystack) - len(needle) + 1):
        if haystack[index:index + len(needle)] == needle:
            return index
    return None


def contract_positions(panel_id: str, expected: str) -> set[int]:
    words = normalize_words(expected)
    positions = {index for index, word in enumerate(words) if re.fullmatch(r"\d+(?:\.\d+)?", word)}
    for phrase in CONTRACT_PHRASES.get(panel_id, []):
        phrase_words = normalize_words(phrase)
        start = find_subsequence(words, phrase_words)
        if start is None:
            raise RuntimeError(f"contract phrase not found in panel {panel_id}: {phrase}")
        positions.update(range(start, start + len(phrase_words)))
    return positions


def is_cosmetic_tokens(expected: list[str], transcript: list[str]) -> bool:
    if set(expected + transcript).issubset(COSMETIC_WORDS):
        return True
    return len(expected) == len(transcript) == 1 and (expected[0], transcript[0]) in PROPER_NAME_VARIANTS


def judge_mismatches(panel_id: str, expected: str, differences: list[dict[str, Any]]) -> list[dict[str, Any]]:
    protected = contract_positions(panel_id, expected)
    judged = []
    for difference in differences:
        i1, i2 = difference["expected_index"]
        check_indices = set(range(i1, max(i1 + 1, i2)))
        if i1 == i2:
            check_indices.update({max(0, i1 - 1), i1})
        touches_contract = bool(check_indices & protected)
        cosmetic = not touches_contract and is_cosmetic_tokens(difference["expected"], difference["transcript"])
        if cosmetic and len(difference["expected"]) == len(difference["transcript"]) == 1 and (difference["expected"][0], difference["transcript"][0]) in PROPER_NAME_VARIANTS:
            reason = "phonetic ASR rendering of a cited proper name outside protected claims"
        elif cosmetic:
            reason = "minor function-word ASR variance outside every protected phrase and number"
        else:
            reason = "number, protected caveat/Reading/F-B/verdict phrase, or substantive narration word"
        judged.append({**difference, "judgment": "cosmetic" if cosmetic else "contract-bearing", "reason": reason})
    return judged


def multipart(audio: Path) -> tuple[bytes, str]:
    boundary = "----HermesBHUPhase2V2" + secrets.token_hex(12)
    mime = mimetypes.guess_type(audio.name)[0] or "audio/wav"
    chunks = [
        f"--{boundary}\r\n".encode(), b'Content-Disposition: form-data; name="model"\r\n\r\n', ASR_MODEL.encode() + b"\r\n",
        f"--{boundary}\r\n".encode(), b'Content-Disposition: form-data; name="response_format"\r\n\r\n', b"json\r\n",
        f"--{boundary}\r\n".encode(), b'Content-Disposition: form-data; name="language"\r\n\r\n', b"en\r\n",
        f"--{boundary}\r\n".encode(), f'Content-Disposition: form-data; name="file"; filename="{audio.name}"\r\n'.encode(), f"Content-Type: {mime}\r\n\r\n".encode(), audio.read_bytes(), b"\r\n",
        f"--{boundary}--\r\n".encode(),
    ]
    return b"".join(chunks), boundary


def transcribe(audio: Path, output: Path) -> dict[str, Any]:
    audio_hash = pipeline.sha256(audio)
    if output.exists():
        cached = json.loads(output.read_text(encoding="utf-8"))
        if cached.get("candidate_audio_sha256") == audio_hash:
            return cached
    sys.path.insert(0, str(HERMES_CHECKOUT))
    from tools.managed_tool_gateway import resolve_managed_tool_gateway  # type: ignore[import-not-found]
    route = resolve_managed_tool_gateway("openai-audio")
    body, boundary = multipart(audio)
    url = route.gateway_origin.rstrip("/") + "/v1/audio/transcriptions"
    for attempt in range(1, 4):
        request = urllib.request.Request(url, data=body, method="POST")
        request.add_header("Authorization", "Bearer " + route.nous_user_token)
        request.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
        try:
            parsed = json.loads(urllib.request.urlopen(request, timeout=300).read())
            parsed.update({"candidate_audio_sha256": audio_hash, "model_requested": ASR_MODEL})
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(json.dumps(parsed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            return parsed
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 * attempt)
    raise RuntimeError("unreachable ASR retry state")


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def parse_caption_payloads(path: Path) -> list[str]:
    blocks = re.split(r"\n\s*\n", path.read_text(encoding="utf-8-sig").strip())
    payloads: list[str] = []
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines or lines[0] == "WEBVTT":
            continue
        if lines[0].isdigit():
            lines = lines[1:]
        if lines and "-->" in lines[0]:
            lines = lines[1:]
        if lines:
            payloads.append("\n".join(lines))
    return payloads


def decoded_heading_rms(source: Path, decoded: Path) -> float:
    left = Image.open(source).convert("RGB").crop((80, 35, 1840, 220))
    right = Image.open(decoded).convert("RGB").crop((80, 35, 1840, 220))
    values = ImageStat.Stat(ImageChops.difference(left, right)).rms
    return math.sqrt(sum(value * value for value in values) / len(values))


def main() -> int:
    frozen = pipeline.load_frozen_inputs()
    timeline = json.loads((pipeline.BUILD / "audio/timeline.json").read_text(encoding="utf-8"))
    assembly = json.loads((pipeline.BUILD / "qa/assembly-receipt.json").read_text(encoding="utf-8"))
    card_audit = json.loads((pipeline.BUILD / "qa/card-text-and-geometry-audit.json").read_text(encoding="utf-8"))
    candidate = pipeline.BUILD / assembly["output"]
    candidate_hash = pipeline.sha256(candidate)
    if candidate_hash != assembly["output_sha256"]:
        raise RuntimeError("candidate changed after assembly")

    decoded_audio = pipeline.BUILD / "_tmp_final-decoded.wav"
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(candidate), "-map", "0:a:0", "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", str(decoded_audio)])
    records: list[dict[str, Any]] = []
    all_contract_residuals: list[dict[str, Any]] = []
    all_cosmetic_residuals: list[dict[str, Any]] = []
    for panel, card in zip(frozen["panels"], timeline["cards"]):
        segment = pipeline.BUILD / f"_tmp_asr-panel-{panel['id']}.wav"
        asr_start = max(card["start_seconds"], card["speech_start_seconds"] - 0.10)
        asr_end = min(card["end_seconds"], card["speech_end_seconds"] + 0.20)
        run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(decoded_audio), "-ss", f"{asr_start:.6f}", "-t", f"{asr_end - asr_start:.6f}", "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", str(segment)])
        raw = transcribe(segment, pipeline.BUILD / "qa" / f"asr-panel-{panel['id']}.json")
        transcript = raw.get("text", "").strip()
        expected_words = normalize_words(panel["narration"])
        transcript_words = normalize_words(transcript)
        differences = alignment(panel["narration"], transcript)
        judged = judge_mismatches(panel["id"], panel["narration"], differences)
        contract_residuals = [item for item in judged if item["judgment"] == "contract-bearing"]
        cosmetic_residuals = [item for item in judged if item["judgment"] == "cosmetic"]
        phrase_checks = []
        for phrase in CONTRACT_PHRASES.get(panel["id"], []):
            passed = find_subsequence(transcript_words, normalize_words(phrase)) is not None
            phrase_checks.append({"phrase": phrase, "status": "PASS" if passed else "HOLD"})
            if not passed and not contract_residuals:
                contract_residuals.append({"tag": "protected_phrase_not_contiguous", "expected": normalize_words(phrase), "transcript": [], "judgment": "contract-bearing", "reason": "protected phrase did not survive final rendered-audio ASR contiguously"})
        errors = edit_distance(expected_words, transcript_words)
        record = {
            "panel_id": panel["id"],
            "expected": panel["narration"],
            "expected_text_sha256": pipeline.text_sha256(panel["narration"]),
            "transcript": transcript,
            "normalized_expected_words": expected_words,
            "normalized_transcript_words": transcript_words,
            "word_errors": errors,
            "word_error_rate": errors / max(1, len(expected_words)),
            "alignment": judged,
            "protected_phrase_checks": phrase_checks,
            "contract_bearing_residuals": contract_residuals,
            "cosmetic_residuals": cosmetic_residuals,
            "status": "PASS_NO_RESIDUAL" if not judged else "PASS_COSMETIC_RESIDUAL_ONLY" if not contract_residuals else "HOLD_CONTRACT_BEARING_RESIDUAL",
            "decoded_panel_audio_sha256": pipeline.sha256(segment),
        }
        records.append(record)
        all_contract_residuals.extend({"panel_id": panel["id"], **item} for item in contract_residuals)
        all_cosmetic_residuals.extend({"panel_id": panel["id"], **item} for item in cosmetic_residuals)
        segment.unlink(missing_ok=True)

    transcript_blob = " ".join(record["transcript"] for record in records).lower()
    forbidden_hits = [phrase for phrase in FORBIDDEN_PHRASES if phrase in transcript_blob]
    asr_status = "PASS_FULL_RENDERED_AUDIO_ASR_NO_CONTRACT_RESIDUALS" if not all_contract_residuals and not forbidden_hits else "HOLD_FULL_ASR_CONTRACT_RESIDUAL"
    asr_report = {
        "status": asr_status,
        "candidate_sha256": candidate_hash,
        "model": ASR_MODEL,
        "route": "Hermes managed OpenAI audio gateway",
        "scope": "Every panel was cut from audio decoded from the exact final MP4 and transcribed in full.",
        "normalization_policy": ["case/punctuation", "curly/straight quotes", "hyphen tokenization", "digit/spoken-number forms", "common year forms", "NebulaMind token boundary", "big-bang token boundary", "megaelectronvolt token boundary", "possessive ASR tokenization"],
        "aggregate_expected_words": sum(len(record["normalized_expected_words"]) for record in records),
        "aggregate_word_errors": sum(record["word_errors"] for record in records),
        "aggregate_word_error_rate": sum(record["word_errors"] for record in records) / max(1, sum(len(record["normalized_expected_words"]) for record in records)),
        "contract_bearing_residuals": all_contract_residuals,
        "cosmetic_residuals": all_cosmetic_residuals,
        "forbidden_hits": forbidden_hits,
        "records": records,
    }
    asr_json = pipeline.BUILD / "qa/full-asr-qa.json"
    asr_json.write_text(json.dumps(asr_report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    markdown = [
        "# ASR QA — BHU Phase 2 explainer v2", "",
        f"Status: `{asr_status}`", f"Final MP4 SHA-256: `{candidate_hash}`", f"Gateway ASR model: `{ASR_MODEL}`", "",
        "Every panel below was transcribed from audio decoded from the exact final MP4. Word errors use only the declared representational normalization. Numbers, the caveat sentence, the Reading-1 clause, the repaired Panel-08 two-clause sentence, verdict language, and all other substantive changes are contract-bearing. Contract-bearing residuals are not accepted.", "",
        f"Final residual summary: {len(all_cosmetic_residuals)} cosmetic; {len(all_contract_residuals)} contract-bearing.", "",
    ]
    for record in records:
        markdown.extend([
            f"## Panel {record['panel_id']} — {record['status']}", "",
            f"Word errors: {record['word_errors']} / {len(record['normalized_expected_words'])} (WER {record['word_error_rate']:.4f})", "",
            f"Expected: {record['expected']}", "", f"ASR: {record['transcript']}", "",
            "Per-panel word-error alignment:", "",
        ])
        if not record["alignment"]:
            markdown.append("- none — exact after declared normalization")
        else:
            for item in record["alignment"]:
                markdown.append(f"- `{item['tag']}` expected `{item['expected']}` → ASR `{item['transcript']}` — **{item['judgment']}**: {item['reason']}")
        markdown.extend(["", "Protected phrase checks:", ""])
        if not record["protected_phrase_checks"]:
            markdown.append("- no additional exact protected phrase beyond numeric/substantive alignment checks")
        else:
            for check in record["protected_phrase_checks"]:
                markdown.append(f"- `{check['status']}` — {check['phrase']}")
        markdown.append("")
    markdown.extend([
        "## Final judgment", "",
        f"Cosmetic residual mismatches: {json.dumps(all_cosmetic_residuals, ensure_ascii=False) if all_cosmetic_residuals else 'none'}", "",
        f"Contract-bearing residual mismatches: {json.dumps(all_contract_residuals, ensure_ascii=False) if all_contract_residuals else 'none — acceptable for freeze'}", "",
    ])
    pipeline.ASR_QA.write_text("\n".join(markdown), encoding="utf-8")

    # Decode every state midpoint and compare the assertion-heading crop to its source state.
    frame_records = []
    contact_images = []
    state_cursor = 0.0
    for panel_record, panel_audit in zip(assembly["panels"], card_audit["panels"]):
        for state_record, state_audit in zip(panel_record["states"], panel_audit["states"]):
            midpoint = state_cursor + state_record["duration_seconds"] / 2
            frame = pipeline.BUILD / f"_tmp_frame-{panel_record['panel_id']}-{state_record['name']}.png"
            run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-ss", f"{midpoint:.6f}", "-i", str(candidate), "-frames:v", "1", str(frame)])
            rms = decoded_heading_rms(pipeline.BUILD / state_audit["path"], frame)
            exact_heading = state_audit["heading"] == frozen["panels"][int(panel_record["panel_id"]) - 1]["assertion_heading"]
            frame_records.append({"panel_id": panel_record["panel_id"], "state": state_record["name"], "heading_exact": exact_heading, "heading_crop_rms": rms, "decoded_pixels_match": rms < 20.0, "status": "PASS" if exact_heading and rms < 20.0 else "HOLD"})
            contact_images.append(Image.open(frame).convert("RGB").copy())
            frame.unlink(missing_ok=True)
            state_cursor += state_record["duration_seconds"]
    columns = 4
    rows = math.ceil(len(contact_images) / columns)
    sheet = Image.new("RGB", (1920, rows * 270), (7, 13, 25))
    for index, image in enumerate(contact_images):
        sheet.paste(ImageOps.fit(image, (480, 270), Image.Resampling.LANCZOS), ((index % columns) * 480, (index // columns) * 270))
    contact = pipeline.BUILD / "qa/decoded-state-contact-sheet.png"
    sheet.save(contact, format="PNG", optimize=False, compress_level=9)
    heading_status = "PASS_ASSERTION_HEADING_EVERY_DECODED_STATE" if all(record["status"] == "PASS" for record in frame_records) else "HOLD_DECODED_STATE_QA"

    encoded_srt = pipeline.BUILD / "_tmp_encoded-captions.srt"
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(candidate), "-map", "0:s:0", str(encoded_srt)])
    expected_payloads = [panel["narration"] for panel in frozen["panels"]]
    caption_status = "PASS_EXACT_ENCODED_CAPTION_PAYLOADS" if parse_caption_payloads(encoded_srt) == expected_payloads else "HOLD_CAPTION_PAYLOAD"
    encoded_srt.unlink(missing_ok=True)

    decode = subprocess.run(["ffmpeg", "-v", "error", "-i", str(candidate), "-f", "null", "-"], capture_output=True, text=True)
    volume = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(candidate), "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True)
    mean_match = re.search(r"mean_volume:\s*(-?[0-9.]+) dB", volume.stderr)
    max_match = re.search(r"max_volume:\s*(-?[0-9.]+) dB", volume.stderr)
    if not mean_match or not max_match:
        raise RuntimeError("volume metrics missing")
    probe = assemble.ffprobe(candidate)
    expected_frames = sum(int(card["frame_count"]) for card in timeline["cards"])
    assemble.validate_media_contract(probe, expected_frames, timeline["master_duration_seconds"])

    geometry = card_audit["quantitative_geometry"]
    equation_status = "PASS_EXACTLY_THREE_PERMITTED_EQUATIONS" if card_audit["equations_projected_exactly"] == pipeline.EXPECTED_EQUATIONS and not card_audit["other_equations_projected"] else "HOLD_EQUATION_PROJECTION"
    no_plots_status = "PASS_HONEST_NO_PLOTS_CARDS_EXACTLY_02_06_08" if card_audit["no_plots_panels"] == ["02", "06", "08"] else "HOLD_NO_PLOTS_CARDS"
    plot_assets = [
        state["geometry"].get("paper_asset")
        for panel in card_audit["panels"]
        for state in panel["states"]
        if state["geometry"].get("paper_asset")
    ]
    plot_status = "PASS_FOUR_PINNED_PAPER_FIGURES_LARGE_ATTRIBUTED_AND_ANIMATED" if (
        plot_assets == ["prd_1111.4595_fig1_scale.jpg", "prd_1111.4595_fig2_temp.jpg", "ds_1006.4166_comparison.png", "ds_1006.4166_prefac_Yp.png"] and
        assembly["animated_plot_walkthrough_states"] == ["04/plot", "05/plot", "10/figure1", "10/figure2"] and
        card_audit["paper_assets_verified_before_embedding"]
    ) else "HOLD_PAPER_FIGURE_EXECUTION"
    geometry_status = "PASS_LABELED_BANDS_LADDERS_AND_PLANCK_MARKERS" if (
        geometry["panel_05"]["audit"]["linear_ladder_rungs"] == 730 and
        geometry["panel_05"]["plot"]["planck_marker_outside_paper_pixels"] and
        geometry["panel_09"]["ceiling"]["causality_order_steps"] == 27 and
        geometry["panel_09"]["ceiling"]["treatment_band_edges"] == 2 and
        geometry["panel_11"]["main"]["signal_range_band_edges"] == 2 and
        geometry["panel_11"]["main"]["planck_regime_chip"] and
        not geometry["panel_11"]["main"]["unlabeled_log_compression"]
    ) else "HOLD_MAGNITUDE_GEOMETRY"
    overall = "PASS_LOCAL_RENDER_QA_READY_FOR_KIMI_REVIEW" if all([
        asr_status.startswith("PASS"), heading_status.startswith("PASS"), caption_status.startswith("PASS"),
        equation_status.startswith("PASS"), no_plots_status.startswith("PASS"), plot_status.startswith("PASS"),
        geometry_status.startswith("PASS"), decode.returncode == 0,
    ]) else "HOLD_LOCAL_RENDER_QA"
    report = {
        "status": overall,
        "candidate": assembly["output"],
        "candidate_sha256": candidate_hash,
        "candidate_bytes": candidate.stat().st_size,
        "duration_seconds": float(probe["format"]["duration"]),
        "asr_status": asr_status,
        "asr_report": str(asr_json.relative_to(pipeline.BUILD)),
        "asr_report_sha256": pipeline.sha256(asr_json),
        "asr_qa_markdown": str(pipeline.ASR_QA.relative_to(pipeline.ROOT)),
        "asr_qa_markdown_sha256": pipeline.sha256(pipeline.ASR_QA),
        "contract_bearing_residual_count": len(all_contract_residuals),
        "cosmetic_residual_count": len(all_cosmetic_residuals),
        "heading_status": heading_status,
        "heading_records": frame_records,
        "caption_status": caption_status,
        "equation_status": equation_status,
        "no_plots_status": no_plots_status,
        "plot_status": plot_status,
        "geometry_status": geometry_status,
        "decoded_contact_sheet": str(contact.relative_to(pipeline.BUILD)),
        "decoded_contact_sheet_sha256": pipeline.sha256(contact),
        "full_decode_status": "PASS" if decode.returncode == 0 else "HOLD",
        "mean_volume_db": float(mean_match.group(1)),
        "max_volume_db": float(max_match.group(1)),
        "publication_state": "LOCAL_ONLY_NOT_UPLOADED",
        "credits_spent": 0,
    }
    (pipeline.BUILD / "qa/final-qa-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    decoded_audio.unlink(missing_ok=True)
    print(json.dumps({key: report[key] for key in ("status", "candidate_sha256", "duration_seconds", "asr_status", "contract_bearing_residual_count", "cosmetic_residual_count", "heading_status", "caption_status", "equation_status", "no_plots_status", "plot_status", "geometry_status")}, ensure_ascii=False))
    return 0 if overall.startswith("PASS") else 2


if __name__ == "__main__":
    raise SystemExit(main())
