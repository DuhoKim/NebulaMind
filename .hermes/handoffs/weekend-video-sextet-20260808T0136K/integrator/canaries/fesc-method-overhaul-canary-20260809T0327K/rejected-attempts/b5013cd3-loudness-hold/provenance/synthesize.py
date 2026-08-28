#!/usr/bin/env python3
"""Fresh sentence-aligned Alloy synthesis for one sibling lane at a time."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
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
MODEL = "gpt-4o-mini-tts"
VOICE = "alloy"
SPEED = 1.18


def probe(path: Path) -> dict:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration,size:stream=codec_name,codec_type,sample_rate,channels", "-of", "json", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(out.stdout)
    if float(data["format"]["duration"]) <= 0 or int(data["format"]["size"]) <= 0:
        raise RuntimeError(f"invalid audio returned for {path.name}")
    return data


def synthesize(text: str, instructions: str, output: Path) -> None:
    gateway = resolve_managed_tool_gateway("openai-audio")
    if gateway is None:
        raise RuntimeError("BLOCKED_OPENAI_AUDIO_GATEWAY: do not substitute another voice")
    body = json.dumps(
        {
            "model": MODEL,
            "voice": VOICE,
            "input": text,
            "speed": SPEED,
            "response_format": "mp3",
            "instructions": instructions,
        }
    ).encode()
    req = urllib.request.Request(gateway.gateway_origin.rstrip("/") + "/v1/audio/speech", data=body, method="POST")
    req.add_header("Authorization", "Bearer " + gateway.nous_user_token)
    req.add_header("Content-Type", "application/json")
    payload = urllib.request.urlopen(req, timeout=180).read()
    if not payload:
        raise RuntimeError("managed TTS returned no bytes")
    output.write_bytes(payload)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate_dir")
    args = ap.parse_args()
    candidate = Path(args.candidate_dir).resolve()
    provenance = candidate / "provenance"
    provenance.mkdir(parents=True, exist_ok=True)
    synthesizer_snapshot = provenance / "synthesize.py"
    shutil.copy2(Path(__file__).resolve(), synthesizer_snapshot)
    spec_path = candidate / "spec.json"
    spec = json.loads(spec_path.read_text())
    slug = spec["slug"]
    audio = ROOT / "audio" / slug
    if audio.exists():
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        archive = ROOT / "audio_archive" / f"{slug}-{stamp}"
        archive.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(audio), str(archive))
    raw = audio / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    instructions = spec.get(
        "tts_instructions",
        "Measured scientific-conference narration. Calm, precise, and authoritative. Warmly motivate the opening without implying a result. Give the discriminating method the strongest intellectual emphasis. Never sound as if a value has been revealed.",
    )
    records = []
    for item in spec["sentences"]:
        text = item["text"]
        text_hash = hashlib.sha256(text.encode()).hexdigest()
        output = raw / f"{item['id']}-{text_hash[:12]}.mp3"
        last_error = None
        facts = None
        for attempt in (1, 2):
            try:
                synthesize(text, instructions, output)
                facts = probe(output)
                last_error = None
                break
            except Exception as exc:
                last_error = exc
                output.unlink(missing_ok=True)
                if attempt == 1:
                    time.sleep(2)
        if last_error is not None:
            raise RuntimeError(f"{item['id']} synthesis failed: {last_error}")
        if facts is None:
            raise RuntimeError(f"{item['id']} synthesis returned no probe facts")
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
        print(f"{item['id']} {float(facts['format']['duration']):.3f}s")
    receipt = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": candidate.name,
        "slug": slug,
        "provider_route": "Hermes managed OpenAI audio gateway",
        "model": MODEL,
        "voice": VOICE,
        "speed": SPEED,
        "music": False,
        "synthesis_unit": "one exact sentence per call",
        "instructions": instructions,
        "spec_sha256": hashlib.sha256(spec_path.read_bytes()).hexdigest(),
        "synthesizer_path": str(synthesizer_snapshot.relative_to(candidate)),
        "synthesizer_sha256": hashlib.sha256(synthesizer_snapshot.read_bytes()).hexdigest(),
        "sentence_count": len(records),
        "records": records,
    }
    (audio / "synthesis_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(audio / "synthesis_receipt.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
