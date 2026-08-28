#!/usr/bin/env python3
"""Synthesize narrative v5 one exact sentence per managed OpenAI TTS call.

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
SCRIPT_PATH = ROOT / "narration_script_v5.json"
RAW_DIR = ROOT / "audio_v5" / "raw"
RECEIPT_PATH = ROOT / "audio_v5" / "synthesis_receipt.json"
MODEL = "gpt-4o-mini-tts"
VOICE = "alloy"
SPEED = 1.18
INSTRUCTIONS = (
    "Measured scientific-conference narration. Calm, precise, and authoritative. "
    "Give the nine-sentence why-study opening warmth, clarity, and deliberate pacing. "
    "Keep isotropy, tidal-torque expectation, conditional stakes, the unsettled question, "
    "and sorting bias logically separate. Preserve every exact primary-abstract sentence. "
    "Clearly voice Longo, Shamir, and Land as attributions to other studies, not our findings. "
    "Let the mirror-test sentences carry intellectual emphasis without sounding dramatic. "
    "Do not imply that a result has been revealed."
)
SYMBOL_INSTRUCTIONS = {
    "i05l": (
        " Pronounce every mathematical symbol literally: the minus sign as 'minus', ± as 'plus or minus', "
        "× as 'times', and 10⁻⁴ as 'ten to the minus fourth'. Do not omit or change any symbol."
    ),
    "i05s": (
        " Pronounce every mathematical symbol literally: z<0.3 as 'z less than zero point three', and "
        "P<5.8×10⁻⁶ as 'P less than five point eight times ten to the minus sixth'. "
        "The less-than signs must be spoken as 'less than', never as equality and never omitted."
    ),
}


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


def synthesize(text: str, output: Path, instructions: str) -> None:
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
            "instructions": instructions,
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
        instructions = INSTRUCTIONS + SYMBOL_INSTRUCTIONS.get(item["id"], "")
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        output = RAW_DIR / f"{item['id']}-{text_hash[:12]}.mp3"
        if not output.exists():
            last_error = None
            for attempt in (1, 2):
                try:
                    synthesize(text, output, instructions)
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
                "instructions": instructions,
                "file": str(output.relative_to(ROOT)),
                "file_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
                "probe": facts,
            }
        )
        print(f"{item['id']} {float(facts['format']['duration']):.3f}s {output.name}")

    receipt = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "revision": "v5-duho-literature-beat-only",
        "predecessor_audio_not_reused": "spin-why-study-intro-20260809T2340K/audio_v4/",
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
