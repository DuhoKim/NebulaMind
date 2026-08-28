#!/usr/bin/env python3
"""Synthesize exact V7 narration sentence-by-sentence via Hermes OpenAI TTS.

The storyboard narration strings are the sole spoken source. Headings remain visual.
Every TTS input and output is hash-receipted. Audio is normalized to mono 48 kHz
PCM before deterministic concatenation with fixed pauses.
"""
from __future__ import annotations
import hashlib
import json
import re
import subprocess
import sys
import time
import urllib.request
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = Path(__file__).resolve().parent
STORY = ROOT / "STORYBOARD_DRAFT_V7.json"
NARR = ROOT / "NARRATION_DRAFT_V7.md"
EXPECTED_STORY_SHA = "3077f0636385487bb4092d2032c18bbedaedb647780bbfc581e59027c87a8d2b"
EXPECTED_NARR_SHA = "3380497f0514e906db8463d0fdd2ffd1f0b02b37ac6825e3bfdec86011c2edc0"
MODEL = "gpt-4o-mini-tts"
VOICE = "alloy"
SPEED = 1.0
SENTENCE_PAUSE = 0.26
CARD_PAUSE = 0.72
RATE = 48000

sys.path.insert(0, "/Users/duhokim/.hermes/hermes-agent")
from tools.managed_tool_gateway import resolve_managed_tool_gateway


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def split_sentences(text: str) -> list[str]:
    # Decimal points are not followed by whitespace and therefore remain intact.
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z“‘])", text.strip())
    if " ".join(parts) != text.strip():
        raise RuntimeError("sentence split failed exact reconstruction")
    return parts


def synth(text: str, out: Path) -> None:
    gateway = resolve_managed_tool_gateway("openai-audio")
    body = json.dumps({
        "model": MODEL,
        "voice": VOICE,
        "input": text,
        "speed": SPEED,
        "response_format": "wav",
        "instructions": (
            "Read the input exactly as written in a calm, clear public-science voice. "
            "Do not add, omit, summarize, or rewrite words. Give numbers and scientific names careful diction."
        ),
    }).encode()
    req = urllib.request.Request(gateway.gateway_origin.rstrip("/") + "/v1/audio/speech", data=body, method="POST")
    req.add_header("Authorization", "Bearer " + gateway.nous_user_token)
    req.add_header("Content-Type", "application/json")
    for attempt in (1, 2, 3):
        try:
            data = urllib.request.urlopen(req, timeout=180).read()
            if not data:
                raise RuntimeError("empty TTS response")
            out.write_bytes(data)
            probe = subprocess.run([
                "ffprobe", "-v", "error", "-show_entries", "format=duration",
                "-of", "csv=p=0", str(out),
            ], capture_output=True, text=True)
            if probe.returncode == 0 and float(probe.stdout.strip()) > 0:
                return
            raise RuntimeError("invalid TTS audio")
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 * attempt)


def convert(src: Path, dst: Path) -> None:
    subprocess.run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(src),
        "-ac", "1", "-ar", str(RATE), "-c:a", "pcm_s16le", str(dst),
    ], check=True)


def wav_data(path: Path) -> tuple[bytes, int]:
    with wave.open(str(path), "rb") as w:
        if (w.getnchannels(), w.getsampwidth(), w.getframerate()) != (1, 2, RATE):
            raise RuntimeError(f"unexpected normalized WAV format: {path}")
        frames = w.readframes(w.getnframes())
        return frames, w.getnframes()


def main() -> int:
    if sha(STORY) != EXPECTED_STORY_SHA or sha(NARR) != EXPECTED_NARR_SHA:
        raise RuntimeError("gated source hash mismatch")
    data = json.loads(STORY.read_text())
    raw_dir = BUILD / "audio" / "raw"
    pcm_dir = BUILD / "audio" / "pcm"
    raw_dir.mkdir(parents=True, exist_ok=True)
    pcm_dir.mkdir(parents=True, exist_ok=True)
    records = []
    all_inputs = []
    for ci, card in enumerate(data["cards"], 1):
        sentences = split_sentences(card["narration"])
        if " ".join(sentences) != card["narration"]:
            raise RuntimeError(f"card {ci}: split no longer reconstructs gated narration")
        for si, text in enumerate(sentences, 1):
            ident = f"c{ci:02d}s{si:02d}"
            raw = raw_dir / f"{ident}.wav"
            pcm = pcm_dir / f"{ident}.wav"
            if not raw.exists():
                synth(text, raw)
            convert(raw, pcm)
            frames, nframes = wav_data(pcm)
            records.append({
                "id": ident,
                "card_id": card["id"],
                "sentence_index": si,
                "text": text,
                "text_sha256": sha_bytes(text.encode()),
                "raw_audio": str(raw.relative_to(BUILD)),
                "raw_audio_sha256": sha(raw),
                "pcm_audio": str(pcm.relative_to(BUILD)),
                "pcm_audio_sha256": sha(pcm),
                "audio_frames": nframes,
                "audio_duration_seconds": nframes / RATE,
            })
            all_inputs.append(text)
            print(ident, f"{nframes/RATE:.3f}s", text[:80])
    # Prove the exact card-level inputs, not only individual fragments.
    for card in data["cards"]:
        rebuilt = " ".join(r["text"] for r in records if r["card_id"] == card["id"])
        if rebuilt != card["narration"]:
            raise RuntimeError(f"TTS input mismatch card {card['id']}")

    master = BUILD / "audio" / "narration_master.wav"
    timeline = []
    cursor = 0
    silence_sentence = b"\x00\x00" * round(SENTENCE_PAUSE * RATE)
    silence_card = b"\x00\x00" * round(CARD_PAUSE * RATE)
    with wave.open(str(master), "wb") as out:
        out.setnchannels(1); out.setsampwidth(2); out.setframerate(RATE)
        for i, rec in enumerate(records):
            frames, nframes = wav_data(BUILD / rec["pcm_audio"])
            start = cursor / RATE
            out.writeframes(frames); cursor += nframes
            end = cursor / RATE
            timeline.append({**rec, "start_seconds": start, "end_seconds": end})
            last_in_card = i == len(records)-1 or records[i+1]["card_id"] != rec["card_id"]
            pause = silence_card if last_in_card else silence_sentence
            out.writeframes(pause); cursor += len(pause)//2

    cards = []
    for card_index, card in enumerate(data["cards"]):
        rr = [r for r in timeline if r["card_id"] == card["id"]]
        next_card_id = data["cards"][card_index + 1]["id"] if card_index + 1 < len(data["cards"]) else None
        next_card_start = next(
            (r["start_seconds"] for r in timeline if next_card_id and r["card_id"] == next_card_id),
            cursor / RATE,
        )
        cards.append({
            "card_id": card["id"],
            "heading": card["heading"],
            "narration": card["narration"],
            "start_seconds": rr[0]["start_seconds"],
            "speech_end_seconds": rr[-1]["end_seconds"],
            "end_seconds": next_card_start,
            "sentence_ids": [r["id"] for r in rr],
        })
    receipt = {
        "status": "SYNTHESIZED_EXACT_INPUT_PENDING_ASR_AND_LISTEN",
        "model": MODEL,
        "voice": VOICE,
        "speed": SPEED,
        "provider_route": "Hermes managed OpenAI audio gateway",
        "sentence_pause_seconds": SENTENCE_PAUSE,
        "card_pause_seconds": CARD_PAUSE,
        "sample_rate_hz": RATE,
        "gated_narration_sha256": sha(NARR),
        "gated_storyboard_sha256": sha(STORY),
        "master_audio": str(master.relative_to(BUILD)),
        "master_audio_sha256": sha(master),
        "master_duration_seconds": cursor / RATE,
        "sentence_count": len(records),
        "tts_inputs_reconstruct_all_card_narration_exactly": True,
        "records": timeline,
        "cards": cards,
    }
    (BUILD / "audio" / "timeline.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({k: receipt[k] for k in ("master_audio_sha256", "master_duration_seconds", "sentence_count")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
