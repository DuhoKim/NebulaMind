#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parent
SPEC = ROOT / "V5_G1_VOICE_CANARY_SPEC.json"
BUILD = ROOT / "V5_G1_AUDIO_RECEIPT.json"
OUTPUT = ROOT / "V5_G1_AUDIO_QA.json"
TRANSCRIPT = ROOT / "V5_G1_Z9_MICHAEL_ASR.txt"
ALIASES = {
    "decks": "dex",
    "un-lensed": "unlensed",
    "un lensed": "unlensed",
    "electron temperature": "electron-temperature",
}
NUMBER_UNITS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19,
}
NUMBER_TENS = {
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
}
NUMBER_SCALES = {"hundred": 100, "thousand": 1000, "million": 1000000, "billion": 1000000000}
NUMBER_WORDS = set(NUMBER_UNITS) | set(NUMBER_TENS) | set(NUMBER_SCALES) | {"point"}


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_number(value: str) -> str:
    try:
        number = Decimal(value.replace(",", ""))
    except InvalidOperation:
        return value
    if number == number.to_integral():
        return str(int(number))
    return format(number.normalize(), "f")


def parse_number_words(values: list[str]) -> str:
    if "point" in values:
        split = values.index("point")
        whole = parse_number_words(values[:split]) if split else "0"
        digits = "".join(str(NUMBER_UNITS[value]) for value in values[split + 1:] if value in NUMBER_UNITS)
        return canonical_number(f"{whole}.{digits or '0'}")
    total = 0
    current = 0
    for value in values:
        if value in NUMBER_UNITS:
            current += NUMBER_UNITS[value]
        elif value in NUMBER_TENS:
            current += NUMBER_TENS[value]
        elif value == "hundred":
            current = max(1, current) * 100
        elif value in {"thousand", "million", "billion"}:
            total += max(1, current) * NUMBER_SCALES[value]
            current = 0
    return str(total + current)


def raw_tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower().replace("’", "'"))


def semantic_tokens(text: str) -> list[str]:
    value = text.lower().replace("’", "'")
    for source, target in ALIASES.items():
        value = value.replace(source, target)
    values = re.findall(r"[a-z]+|[-+]?\d[\d,]*(?:\.\d+)?", value)
    output: list[str] = []
    index = 0
    while index < len(values):
        token = values[index]
        if re.fullmatch(r"[-+]?\d[\d,]*(?:\.\d+)?", token):
            output.append(canonical_number(token))
            index += 1
            continue
        if token in NUMBER_WORDS:
            end = index + 1
            while end < len(values) and values[end] in NUMBER_WORDS:
                end += 1
            output.append(parse_number_words(values[index:end]))
            index = end
            continue
        output.append(token)
        index += 1
    return output


def edit_distance(left: list[str], right: list[str]) -> int:
    previous = list(range(len(right) + 1))
    for i, a in enumerate(left, 1):
        current = [i]
        for j, b in enumerate(right, 1):
            current.append(min(current[-1] + 1, previous[j] + 1, previous[j - 1] + (a != b)))
        previous = current
    return previous[-1]


def probe(path: Path) -> dict[str, Any]:
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration,size:stream=codec_name,codec_type,sample_fmt,sample_rate,channels,bits_per_sample",
        "-of", "json", str(path),
    ], text=True))


def main() -> None:
    spec = json.loads(SPEC.read_text())
    build = json.loads(BUILD.read_text())
    if build.get("marker") != "NEBULAMIND_V5_G1_AUDIO_BUILD_PASS":
        raise RuntimeError("audio build receipt does not pass")
    master = Path(build["listening_master"])
    if sha256(master) != build["listening_master_sha256"]:
        raise RuntimeError("listening master hash drift")
    if sha256(SPEC) != build["spec_sha256"]:
        raise RuntimeError("spec lineage drift")
    subprocess.run(["ffmpeg", "-v", "error", "-xerror", "-i", str(master), "-f", "null", "-"], check=True)
    media = probe(master)
    stream = next(row for row in media["streams"] if row["codec_type"] == "audio")
    if stream["codec_name"] != "pcm_s24le" or stream["sample_rate"] != "48000" or stream["channels"] != 1:
        raise RuntimeError(f"lossless review format drift: {stream}")

    expected = " ".join(row["text"] for row in spec["sentences"])
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    segments, info = model.transcribe(str(master), language="en", beam_size=5, vad_filter=True, condition_on_previous_text=True)
    transcript = " ".join(segment.text.strip() for segment in segments).strip()
    TRANSCRIPT.write_text(transcript + "\n", encoding="utf-8")
    reference_raw = raw_tokens(expected)
    observed_raw = raw_tokens(transcript)
    reference_semantic = semantic_tokens(expected)
    observed_semantic = semantic_tokens(transcript)
    raw_wer = 100.0 * edit_distance(reference_raw, observed_raw) / len(reference_raw)
    semantic_wer = 100.0 * edit_distance(reference_semantic, observed_semantic) / len(reference_semantic)
    critical = ["oxygen", "redshift", "lensing", "benchmark", "unlensed", "electron", "fifth", "dex", "uncertain", "detection"]
    observed_set = set(observed_semantic)
    missing = [word for word in critical if word not in observed_set]
    if semantic_wer > 8.0:
        raise RuntimeError(f"semantic WER exceeds 8%: {semantic_wer:.3f}")
    if missing:
        raise RuntimeError(f"ASR missing spoken critical terms: {missing}; transcript={transcript}")
    if info.language != "en" or info.language_probability < 0.95:
        raise RuntimeError(f"language confidence failed: {info.language} {info.language_probability}")

    result = {
        "marker": "NEBULAMIND_V5_G1_AUDIO_QA_PASS",
        "completed_at_utc": now(),
        "gate": "V5-G1 voice canary only",
        "master": str(master),
        "master_sha256": sha256(master),
        "media": media,
        "duration_seconds": build["total_duration_seconds"],
        "delivered_wpm": build["delivered_wpm"],
        "loudness": build["loudness"],
        "language": info.language,
        "language_probability": info.language_probability,
        "raw_wer_percent_diagnostic": round(raw_wer, 3),
        "semantic_wer_percent": round(semantic_wer, 3),
        "critical_terms": critical,
        "critical_terms_status": "PASS",
        "transcript": transcript,
        "transcript_path": str(TRANSCRIPT),
        "transcript_sha256": sha256(TRANSCRIPT),
        "checks": {
            "full_decode": "PASS",
            "lossless_pcm_24bit_48khz_mono": "PASS",
            "spec_and_master_hash_lineage": "PASS",
            "english_language_confidence": "PASS",
            "semantic_wer_at_most_8_percent": "PASS",
            "spoken_critical_terms": "PASS",
        },
        "human_listening_gate": "PENDING_DUHO_EAR_CHECK",
        "note": "Metrics do not certify naturalness or coherence; Duho must review the exact WAV before V5-G2 or any animation.",
        "video_created": False,
        "animation_created": False,
        "youtube_mutation": False,
        "visibility_mutation": False,
        "website_mutation": False,
        "git_mutation": False,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "PASS",
        "master": str(master),
        "duration": result["duration_seconds"],
        "wpm": result["delivered_wpm"],
        "raw_wer": result["raw_wer_percent_diagnostic"],
        "semantic_wer": result["semantic_wer_percent"],
        "critical_terms": result["critical_terms_status"],
        "human_gate": result["human_listening_gate"],
    }, indent=2))


if __name__ == "__main__":
    main()
