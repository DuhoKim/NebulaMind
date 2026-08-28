#!/usr/bin/env python3
"""Pre-encode ASR guard for exact mathematical-symbol pronunciation in literature quotes."""
from __future__ import annotations

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
RECEIPT = ROOT / "audio_v5/synthesis_receipt.json"
OUT_DIR = ROOT / "preencode_symbol_qa"
WAV = OUT_DIR / "literature-symbols.wav"
REPORT = OUT_DIR / "PREENCODE_SYMBOL_ASR.json"


def normalize(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def main() -> int:
    receipt = json.loads(RECEIPT.read_text())
    by_id = {item["id"]: item for item in receipt["records"]}
    longo = ROOT / by_id["i05l"]["file"]
    shamir = ROOT / by_id["i05s"]["file"]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-i", str(longo), "-i", str(shamir),
            "-filter_complex", "[0:a]aresample=16000[a0];[1:a]aresample=16000[a1];[a0][a1]concat=n=2:v=0:a=1[out]",
            "-map", "[out]", "-ac", "1", "-ar", "16000", str(WAV),
        ],
        check=True,
    )
    gateway = resolve_managed_tool_gateway("openai-audio")
    if gateway is None:
        raise RuntimeError("managed openai-audio gateway unavailable")
    client = OpenAI(
        api_key=gateway.nous_user_token,
        base_url=gateway.gateway_origin.rstrip("/") + "/v1",
        timeout=180,
    )
    with WAV.open("rb") as handle:
        transcript = client.audio.transcriptions.create(model="whisper-1", file=handle).text
    normalized = normalize(transcript)
    checks = {
        "longo_minus": "minus 0 0408" in normalized,
        "longo_plus_or_minus": "plus or minus 0 011" in normalized or "plus minus 0 011" in normalized,
        "longo_times_ten_minus_fourth": "times 10 to the minus fourth" in normalized,
        "shamir_z_less_than": "z less than 0 3" in normalized or "z is less than 0 3" in normalized,
        "shamir_p_less_than": "p less than 5 8" in normalized or "p is less than 5 8" in normalized,
        "shamir_times_ten_minus_sixth": "times 10 to the minus sixth" in normalized,
        "no_equality_substitution": "p equals 5 8" not in normalized and "p equal to 5 8" not in normalized,
    }
    report = {
        "status": "PASS" if all(checks.values()) else "HOLD",
        "model": "whisper-1 via Hermes managed openai-audio gateway",
        "source_ids": ["i05l", "i05s"],
        "exact_tts_inputs_preserved": [by_id["i05l"]["text"], by_id["i05s"]["text"]],
        "transcript": transcript,
        "normalized_transcript": normalized,
        "checks": checks,
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
