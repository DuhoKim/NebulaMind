#!/usr/bin/env python3
"""Second-model ASR adjudication for decoded V11 Cards 05 and 06."""
from __future__ import annotations
import json
from pathlib import Path
from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parent
MODEL = "Systran/faster-whisper-medium"
model = WhisperModel(MODEL, device="cpu", compute_type="int8")
rows = []
for card_id in ("05", "06"):
    path = ROOT / "audio_cards" / f"card-{card_id}.wav"
    segments, info = model.transcribe(
        str(path), language="en", beam_size=5, vad_filter=True,
        condition_on_previous_text=False,
    )
    segments = list(segments)
    rows.append({
        "card_id": card_id,
        "model": MODEL,
        "language": info.language,
        "language_probability": info.language_probability,
        "transcript": " ".join(segment.text.strip() for segment in segments).strip(),
        "segments": [
            {
                "start": segment.start,
                "end": segment.end,
                "text": segment.text.strip(),
                "avg_logprob": segment.avg_logprob,
                "no_speech_prob": segment.no_speech_prob,
            }
            for segment in segments
        ],
    })
output = ROOT / "asr_medium_cards_05_06.json"
output.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(rows, indent=2, ensure_ascii=False))
