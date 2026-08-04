#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERMES_ROOT = Path('/Users/duhokim/.hermes/hermes-agent')
if str(HERMES_ROOT) not in sys.path:
    sys.path.insert(0, str(HERMES_ROOT))
from tools.tts_tool import _generate_openai_tts

BASE = Path(__file__).resolve().parent
TEXT = (BASE / 'canary_passage.txt').read_text(encoding='utf-8').strip()
VOICES = ('onyx', 'echo', 'ash')
SPEED = 0.85
MODEL = 'gpt-4o-mini-tts'
OUT = BASE / 'voice_canaries'
OUT.mkdir(parents=True, exist_ok=True)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def probe(path: Path) -> dict:
    raw = subprocess.check_output([
        'ffprobe', '-v', 'error', '-show_entries',
        'format=duration,size:stream=codec_name,sample_rate,channels',
        '-of', 'json', str(path),
    ], text=True)
    return json.loads(raw)


def loudness(path: Path) -> dict:
    proc = subprocess.run([
        'ffmpeg', '-nostats', '-hide_banner', '-i', str(path),
        '-af', 'ebur128=peak=true', '-f', 'null', '-'
    ], text=True, capture_output=True, check=True)
    text = proc.stderr
    def last(pattern: str):
        vals = re.findall(pattern, text)
        return float(vals[-1]) if vals else None
    return {
        'integrated_lufs': last(r'I:\s*(-?\d+(?:\.\d+)?) LUFS'),
        'true_peak_dbtp': last(r'Peak:\s*(-?\d+(?:\.\d+)?) dBFS'),
    }


def main() -> None:
    word_count = len(re.findall(r"\b[\w'-]+\b", TEXT))
    items = []
    for voice in VOICES:
        raw = OUT / f'{voice}_raw.wav'
        review = OUT / f'{voice}_review_16lufs.wav'
        _generate_openai_tts(
            TEXT, str(raw), {}, model=MODEL, voice=voice, speed=SPEED
        )
        subprocess.run([
            'ffmpeg', '-y', '-v', 'error', '-i', str(raw),
            '-af', 'loudnorm=I=-16:TP=-2:LRA=7',
            '-ar', '48000', '-ac', '1', '-c:a', 'pcm_s16le', str(review)
        ], check=True)
        p = probe(review)
        duration = float(p['format']['duration'])
        items.append({
            'voice': voice,
            'presentation': 'male-coded OpenAI voice candidate',
            'model': MODEL,
            'provider': 'OpenAI via Nous managed audio gateway',
            'speed': SPEED,
            'word_count': word_count,
            'duration_seconds': round(duration, 3),
            'words_per_minute': round(word_count / duration * 60, 1),
            'raw_path': str(raw),
            'review_path': str(review),
            'raw_sha256': sha256(raw),
            'review_sha256': sha256(review),
            'probe': p,
            'loudness': loudness(review),
        })
        print(json.dumps(items[-1]), flush=True)
    receipt = {
        'marker': 'NEBULAMIND_V3_MALE_VOICE_CANARIES_COMPLETE',
        'text': TEXT,
        'items': items,
        'global_config_changed': False,
    }
    (OUT / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
