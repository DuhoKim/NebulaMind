#!/usr/bin/env python3
"""nm_say.py — speak arbitrary text in the channel's `alloy` voice.

nm_paper_tts.py can only cut a storyboard, so status readouts had no way to reach the same voice
the videos use. This is that gap filled: plain text in, mono MP3 out, identical engine and voice.

The gateway resolver lives in the Hermes tree and needs Python 3.10+ (`str | object`), while this
repo runs system 3.9 — so we shell out to the Hermes venv, which also keeps the credential inside
that process. No token is ever read here.

Speed is 1.0, not nm_paper_tts's 1.18: that 1.18 exists to match the pacing of already-shipped
video tracks, and a spoken status update has no such constraint.

  nm_say.py "text"  [--voice alloy] [--speed 1.0] [-o out.mp3]
"""
import argparse, json, os, subprocess, sys

HERMES_PY = "/Users/duhokim/.hermes/hermes-agent/venv/bin/python"

p = argparse.ArgumentParser()
p.add_argument("text")
p.add_argument("--voice", default="alloy")
p.add_argument("--speed", type=float, default=1.0)
p.add_argument("--model", default="gpt-4o-mini-tts")
p.add_argument("-o", "--out", default="/tmp/nm_say.mp3")
a = p.parse_args()

if not os.path.exists(HERMES_PY):
    sys.exit(f"hermes venv python not found at {HERMES_PY}")

code = (
    "import sys,json,urllib.request\n"
    "sys.path.insert(0,'/Users/duhokim/.hermes/hermes-agent')\n"
    "from tools.managed_tool_gateway import resolve_managed_tool_gateway\n"
    "g=resolve_managed_tool_gateway('openai-audio')\n"
    "text=json.load(sys.stdin)['text']\n"
    f"body=json.dumps({{'model':{a.model!r},'voice':{a.voice!r},'input':text,"
    f"'speed':{a.speed!r}}}).encode()\n"
    "r=urllib.request.Request(g.gateway_origin.rstrip('/')+'/v1/audio/speech',"
    "data=body,method='POST')\n"
    "r.add_header('Authorization','Bearer '+g.nous_user_token)\n"
    "r.add_header('Content-Type','application/json')\n"
    "d=urllib.request.urlopen(r,timeout=120).read()\n"
    f"open({a.out!r},'wb').write(d)\n"
    "print(len(d))\n"
)
# edge-tts fallback (2026-08-20): when the Nous balance hit $0 the whole audio
# report system went hard-mute while the video path (which carries an edge
# engine) kept working. Voice-gender mapping keeps the Fables recognizable.
EDGE_VOICES = {
    "onyx": "en-US-AndrewMultilingualNeural",     # Blanc (M)
    "shimmer": "en-US-AvaMultilingualNeural",     # Hwao (F)
    "nova": "en-US-EmmaMultilingualNeural",       # Tori (F)
    "coral": "en-US-AvaMultilingualNeural",
}
EDGE_DEFAULT = "en-US-AndrewMultilingualNeural"


def edge_fallback(reason: str) -> None:
    try:
        import asyncio, edge_tts
    except ImportError:
        sys.exit(f"{reason}; and edge_tts is not installed for the fallback")
    voice = EDGE_VOICES.get(a.voice, EDGE_DEFAULT)
    asyncio.run(edge_tts.Communicate(a.text, voice, rate="+20%").save(a.out))
    n2 = os.path.getsize(a.out)
    if n2 < 2000:
        sys.exit(f"{reason}; edge fallback also produced only {n2} bytes")
    print(f"{a.out}  {n2} bytes (edge-tts fallback: {reason})")


r = subprocess.run([HERMES_PY, "-c", code], input=json.dumps({"text": a.text}),
                   text=True, capture_output=True)
if r.returncode != 0:
    edge_fallback(f"gateway tts failed: {r.stderr.strip()[-200:]}")
    sys.exit(0)
n = int(r.stdout.strip() or 0)
# A 200 with an empty body has happened before and surfaced only as an opaque ffmpeg error later.
if n < 2000:
    edge_fallback(f"gateway returned {n} bytes — too small to be audio")
    sys.exit(0)
print(f"{a.out}  {n} bytes")
