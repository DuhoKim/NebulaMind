#!/usr/bin/env python3
"""Transcribe the encoded nine-sentence why-study introduction through the managed audio gateway."""
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
VIDEO = ROOT / "spin-literature-intro-canary-20260810T1434K.mp4"
TIMELINE = ROOT / "audio_v5" / "timeline.json"
SCRIPT = ROOT / "narration_script_v5.json"
OUT_DIR = ROOT / "encoded_qa"
INTRO_WAV = OUT_DIR / "encoded-why-study-introduction-v5.wav"
REPORT = OUT_DIR / "encoded-why-study-introduction-transcription-v5.json"


def normalize(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def main() -> int:
    timeline = json.loads(TIMELINE.read_text())
    script = json.loads(SCRIPT.read_text())
    opening = script["sentences"][:9]
    if [item["id"] for item in opening] != ["i01", "i02", "i03", "i04", "i05l", "i05s", "i05d", "i05u", "i06"]:
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
        "isotropy_expectation": all(term in transcript_norm for term in ("same in every direction", "no built in preference")),
        "angular_momentum_origin": all(term in transcript_norm for term in ("angular momentum", "balance is the prediction")),
        "conditional_stakes": all(term in transcript_norm for term in ("would indicate", "preferred axis")),
        "longos_attributed_report": all(term in transcript_norm for term in ("longo reported", "unbinned analysis", "dipole asymmetry")),
        "shamirs_attributed_report": all(term in transcript_norm for term in ("shamir reported", "local universe", "galaxy spin")),
        "lands_attributed_report": all(term in transcript_norm for term in ("land and colleagues reported", "correcting", "statistical isotropy")),
        "open_question": all(term in transcript_norm for term in ("literature remains disputed", "adopts none")),
        "sorting_bias_handoff": all(term in transcript_norm for term in ("sorting bias", "mirror control")),
    }
    passed = similarity >= 0.84 and all(required.values())
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
