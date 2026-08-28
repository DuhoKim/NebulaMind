#!/usr/bin/env python3
"""Synthesize narrative v4 one exact sentence per managed OpenAI TTS call.

This why-study lineage never reads or reuses predecessor audio.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERMES_SOURCE = Path("/Users/duhokim/.hermes/hermes-agent")
if str(HERMES_SOURCE) not in sys.path:
    sys.path.insert(0, str(HERMES_SOURCE))

from tools.managed_tool_gateway import resolve_managed_tool_gateway  # noqa: E402

ROOT = Path(__file__).resolve().parent
SCRIPT_PATH = ROOT / "narration_script_v4.json"
RAW_DIR = ROOT / "audio_v4" / "raw"
RECEIPT_PATH = ROOT / "audio_v4" / "synthesis_receipt.json"
MODEL = "gpt-4o-mini-tts"
VOICE = "alloy"
SPEED = 1.18
INSTRUCTIONS = (
    "Measured scientific-conference narration. Calm, precise, and authoritative. "
    "Give the six-sentence why-study opening warmth, clarity, and deliberate pacing. "
    "Keep isotropy, tidal-torque expectation, conditional stakes, the unsettled question, "
    "and sorting bias logically separate. Preserve the exact wording of the Longo sentence. "
    "Let the mirror-test sentences carry intellectual emphasis without sounding dramatic. "
    "Do not imply that a result has been revealed."
)


def probe(path: Path) -> dict:
    run = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration,size:stream=codec_name,codec_type,sample_rate,channels,bit_rate",
            "-of",
            "json",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(run.stdout)
    duration = float(data["format"]["duration"])
    if duration <= 0 or int(data["format"]["size"]) <= 0:
        raise RuntimeError(f"invalid audio returned for {path.name}")
    return data


def synthesize(text: str, output: Path) -> None:
    gateway = resolve_managed_tool_gateway("openai-audio")
    if gateway is None:
        raise RuntimeError(
            "BLOCKED_OPENAI_AUDIO_GATEWAY: managed openai-audio gateway is unavailable; "
            "do not fall back to another voice"
        )
    body = json.dumps(
        {
            "model": MODEL,
            "voice": VOICE,
            "input": text,
            "speed": SPEED,
            "response_format": "mp3",
            "instructions": INSTRUCTIONS,
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        gateway.gateway_origin.rstrip("/") + "/v1/audio/speech",
        data=body,
        method="POST",
    )
    request.add_header("Authorization", "Bearer " + gateway.nous_user_token)
    request.add_header("Content-Type", "application/json")
    payload = urllib.request.urlopen(request, timeout=180).read()
    if not payload:
        raise RuntimeError("managed TTS returned an empty body")
    output.write_bytes(payload)


def main() -> int:
    spec = json.loads(SCRIPT_PATH.read_text())
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    records = []
    for item in spec["sentences"]:
        text = item["text"]
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        output = RAW_DIR / f"{item['id']}-{text_hash[:12]}.mp3"
        if not output.exists():
            last_error = None
            for attempt in (1, 2):
                try:
                    synthesize(text, output)
                    probe(output)
                    last_error = None
                    break
                except Exception as exc:
                    last_error = exc
                    output.unlink(missing_ok=True)
                    if attempt == 1:
                        time.sleep(2)
            if last_error is not None:
                raise RuntimeError(f"{item['id']} synthesis failed: {last_error}")
        facts = probe(output)
        records.append(
            {
                "id": item["id"],
                "section": item["section"],
                "text": text,
                "text_sha256": text_hash,
                "file": str(output.relative_to(ROOT)),
                "file_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
                "probe": facts,
            }
        )
        print(f"{item['id']} {float(facts['format']['duration']):.3f}s {output.name}")

    receipt = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "revision": "v4-duho-why-study-introduction",
        "predecessor_audio_not_reused": "spin-method-overhaul-canary-20260808T1959K/audio_v3/",
        "provider_route": "Hermes managed OpenAI audio gateway",
        "model": MODEL,
        "voice": VOICE,
        "speed": SPEED,
        "instructions": INSTRUCTIONS,
        "synthesis_unit": "one exact sentence per call",
        "music": False,
        "narration_script": str(SCRIPT_PATH.relative_to(ROOT)),
        "narration_script_sha256": hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest(),
        "sentence_count": len(records),
        "records": records,
    }
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"receipt {RECEIPT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
