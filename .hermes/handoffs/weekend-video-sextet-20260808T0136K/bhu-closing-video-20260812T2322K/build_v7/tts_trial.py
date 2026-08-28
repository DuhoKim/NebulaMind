#!/usr/bin/env python3
"""One-sentence OpenAI TTS calibration using the Hermes managed gateway."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import urllib.request

sys.path.insert(0, "/Users/duhokim/.hermes/hermes-agent")
from tools.managed_tool_gateway import resolve_managed_tool_gateway


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--speed", type=float, required=True)
    a = ap.parse_args()
    gateway = resolve_managed_tool_gateway("openai-audio")
    body = json.dumps({
        "model": "gpt-4o-mini-tts",
        "voice": "alloy",
        "input": a.text,
        "speed": a.speed,
        "response_format": "wav",
        "instructions": "Read the input exactly as written in a calm, clear public-science voice. Do not add, omit, or rewrite words.",
    }).encode()
    req = urllib.request.Request(
        gateway.gateway_origin.rstrip("/") + "/v1/audio/speech",
        data=body,
        method="POST",
    )
    req.add_header("Authorization", "Bearer " + gateway.nous_user_token)
    req.add_header("Content-Type", "application/json")
    data = urllib.request.urlopen(req, timeout=180).read()
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    print(json.dumps({"output": str(out), "bytes": len(data), "model": "gpt-4o-mini-tts", "voice": "alloy", "speed": a.speed}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
