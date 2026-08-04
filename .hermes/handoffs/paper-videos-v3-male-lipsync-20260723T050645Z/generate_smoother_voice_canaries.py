#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import uuid
from pathlib import Path

HERMES_ROOT = Path('/Users/duhokim/.hermes/hermes-agent')
sys.path.insert(0, str(HERMES_ROOT))
from tools.tts_tool import _import_openai_client, _resolve_openai_audio_client_config

BASE = Path(__file__).resolve().parent
OUT = BASE / 'voice_canaries_v2_smooth'
OUT.mkdir(parents=True, exist_ok=True)
TEXT = (
    'The core evidence is five strictly unlensed Pollock galaxies from redshift nine point three to nine point nine. '
    'Their oxygen abundances use direct electron-temperature measurements, which infer gas temperature from an auroral line. '
    'Against the Curti comparison, the five galaxies average zero point six nine dex lower in oxygen abundance—about one fifth the nearby level. '
    'Replacing the local comparison with the Andrews and Martini relation changes the result only slightly. '
    'The deficit remains, while its exact size is limited by systematic uncertainty.'
)
VOICES = ('echo', 'verse', 'ballad')
MODEL = 'gpt-4o-mini-tts'
SPEED = 0.92
INSTRUCTIONS = (
    'Speak as a polished male science documentary host. Use a smooth, warm timbre and clean consonants. '
    'Use connected, conversational phrasing at a moderately energetic pace. Avoid gravelly texture, an announcer growl, '
    'exaggerated dramatic pauses, and ponderous number delivery. Explain rather than declaim. Keep technical terms clear.'
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def probe(path: Path) -> dict:
    return json.loads(subprocess.check_output([
        'ffprobe','-v','error','-show_entries','format=duration,size:stream=codec_name,sample_rate,channels','-of','json',str(path)
    ], text=True))


def main() -> None:
    api_key, base_url, _managed = _resolve_openai_audio_client_config()
    Client = _import_openai_client()
    client = Client(api_key=api_key, base_url=base_url)
    words = len(re.findall(r"\b[\w'-]+\b", TEXT))
    items = []
    try:
        for voice in VOICES:
            raw = OUT / f'{voice}_smooth_raw.wav'
            review = OUT / f'{voice}_smooth_review_16lufs.wav'
            response = client.audio.speech.create(
                model=MODEL,
                voice=voice,
                input=TEXT,
                instructions=INSTRUCTIONS,
                response_format='wav',
                speed=SPEED,
                extra_headers={'x-idempotency-key': str(uuid.uuid4())},
            )
            response.stream_to_file(raw)
            subprocess.run([
                'ffmpeg','-y','-v','error','-i',str(raw),'-af','loudnorm=I=-16:TP=-2:LRA=7',
                '-ar','48000','-ac','1','-c:a','pcm_s16le',str(review)
            ], check=True)
            p=probe(review); duration=float(p['format']['duration'])
            item={
                'voice':voice,'model':MODEL,'provider':'OpenAI via Nous managed audio gateway','speed':SPEED,
                'instructions':INSTRUCTIONS,'word_count':words,'duration_seconds':round(duration,3),
                'words_per_minute':round(words/duration*60,1),'raw_path':str(raw),'review_path':str(review),
                'raw_sha256':sha(raw),'review_sha256':sha(review),'probe':p,
            }
            items.append(item); print(json.dumps(item),flush=True)
    finally:
        client.close()
    receipt={'marker':'NEBULAMIND_V3_SMOOTHER_MALE_VOICE_CANARIES_COMPLETE','supersedes':'Onyx coarse/slow canary','text':TEXT,'items':items,'global_config_changed':False}
    (OUT/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')

if __name__=='__main__': main()
