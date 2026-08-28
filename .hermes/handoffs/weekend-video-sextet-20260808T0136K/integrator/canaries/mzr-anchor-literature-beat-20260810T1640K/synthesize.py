#!/usr/bin/env python3
"""Synthesize every sentence afresh, one exact sentence per managed OpenAI TTS call."""
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
SPEC_PATH = ROOT / "spec.json"
RAW_DIR = ROOT / "audio" / "raw"
RECEIPT_PATH = ROOT / "audio" / "synthesis_receipt.json"
MODEL = "gpt-4o-mini-tts"
VOICE = "alloy"
SPEED = 1.18
SYMBOL_INSTRUCTIONS = {
    "i05q": " Pronounce '(y-int)' as 'y intercept'. Pronounce 0.7 dex as 'zero point seven dex', with dex spoken as one word rhyming with decks; never spell D or X as letters. Do not omit or change the number or unit.",
}


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def probe(path: Path) -> dict:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration,size:stream=codec_name,codec_type,sample_rate,channels", "-of", "json", str(path)],
        check=True, capture_output=True, text=True,
    )
    data = json.loads(result.stdout)
    if float(data["format"]["duration"]) <= 0 or int(data["format"]["size"]) <= 0:
        raise RuntimeError(f"invalid audio returned for {path.name}")
    return data


def synthesize(text: str, output: Path, instructions: str) -> None:
    gateway = resolve_managed_tool_gateway("openai-audio")
    if gateway is None:
        raise RuntimeError("BLOCKED_OPENAI_AUDIO_GATEWAY: do not fall back to another voice")
    body = json.dumps({"model": MODEL, "voice": VOICE, "input": text, "speed": SPEED, "response_format": "mp3", "instructions": instructions}).encode()
    request = urllib.request.Request(gateway.gateway_origin.rstrip("/") + "/v1/audio/speech", data=body, method="POST")
    request.add_header("Authorization", "Bearer " + gateway.nous_user_token)
    request.add_header("Content-Type", "application/json")
    payload = urllib.request.urlopen(request, timeout=180).read()
    if not payload:
        raise RuntimeError("managed TTS returned an empty body")
    output.write_bytes(payload)


def main() -> int:
    spec = json.loads(SPEC_PATH.read_text())
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    records = []
    for item in spec["sentences"]:
        text = item["text"]
        text_hash = sha256_bytes(text.encode())
        output = RAW_DIR / f"{item['id']}-{text_hash[:12]}.mp3"
        instructions = spec["tts_instructions"] + SYMBOL_INSTRUCTIONS.get(item["id"], "")
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
        records.append({"id": item["id"], "section": item["section"], "text": text, "text_sha256": text_hash, "instructions": instructions, "file": str(output.relative_to(ROOT)), "file_sha256": sha256(output), "probe": facts})
        print(f"{item['id']} {float(facts['format']['duration']):.3f}s {output.name}")
    receipt = {"created_at_utc": datetime.now(timezone.utc).isoformat(), "revision": spec["revision"], "predecessor_audio_reused": False, "provider_route": "Hermes managed OpenAI audio gateway", "model": MODEL, "voice": VOICE, "speed": SPEED, "synthesis_unit": "one exact sentence per call", "music": False, "spec_sha256": sha256(SPEC_PATH), "sentence_count": len(records), "records": records}
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"receipt {RECEIPT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
