#!/usr/bin/env python3
"""Transcribe the encoded four-sentence introduction through the managed audio gateway."""
from __future__ import annotations

import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

HERMES_SOURCE = Path("/Users/duhokim/.hermes/hermes-agent")
if str(HERMES_SOURCE) not in sys.path:
    sys.path.insert(0, str(HERMES_SOURCE))

from openai import OpenAI  # noqa: E402
from tools.managed_tool_gateway import resolve_managed_tool_gateway  # noqa: E402

ROOT = Path(__file__).resolve().parent
VIDEO = ROOT / "spin-method-overhaul-canary-20260808T1959K.mp4"
TIMELINE = ROOT / "audio_v3" / "timeline.json"
SCRIPT = ROOT / "narration_script_v3.json"
OUT_DIR = ROOT / "encoded_qa"
INTRO_WAV = OUT_DIR / "encoded-introduction.wav"
REPORT = OUT_DIR / "encoded-introduction-transcription.json"


def normalize(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def main() -> int:
    timeline = json.loads(TIMELINE.read_text())
    script = json.loads(SCRIPT.read_text())
    opening = script["sentences"][:4]
    if [item["id"] for item in opening] != ["i01", "i02", "i03", "i04"]:
        raise RuntimeError("introduction is not first")
    next_state = next(item for item in timeline["records"] if item["id"] == "s02")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(VIDEO),
            "-map",
            "0:a:0",
            "-t",
            f"{next_state['audio_start_seconds']:.6f}",
            "-ac",
            "1",
            "-ar",
            "16000",
            str(INTRO_WAV),
        ],
        check=True,
    )
    gateway = resolve_managed_tool_gateway("openai-audio")
    if gateway is None:
        raise RuntimeError("managed openai-audio gateway unavailable during encoded narration QA")
    client = OpenAI(
        api_key=gateway.nous_user_token,
        base_url=gateway.gateway_origin.rstrip("/") + "/v1",
        timeout=180,
    )
    with INTRO_WAV.open("rb") as handle:
        response = client.audio.transcriptions.create(model="whisper-1", file=handle)
    transcript = response.text
    expected = " ".join(item["text"] for item in opening)
    expected_norm = normalize(expected)
    transcript_norm = normalize(transcript)
    similarity = difflib.SequenceMatcher(None, expected_norm, transcript_norm).ratio()
    required = {
        "two_handednesses": "two handednesses" in transcript_norm,
        "conditional_universe_clause": all(term in transcript_norm for term in ("if one were", "sky", "fact about the universe")),
        "conditional_sorters_clause": all(term in transcript_norm for term in ("humans sorted", "apparent excess", "could instead", "fact about the sorters")),
        "question_not_clipped": "how do we tell the two apart" in transcript_norm,
    }
    passed = similarity >= 0.90 and all(required.values())
    report = {
        "status": "PASS" if passed else "HOLD",
        "source": str(VIDEO.relative_to(ROOT)),
        "segment_end_seconds": next_state["audio_start_seconds"],
        "model": "whisper-1 via Hermes managed openai-audio gateway",
        "expected": expected,
        "transcript": transcript,
        "normalized_similarity": similarity,
        "checks": required,
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
