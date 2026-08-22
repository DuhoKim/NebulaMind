#!/usr/bin/env python3
"""Timestamped transcript of a podcast episode via the Hermes managed OpenAI audio gateway.

Usage: transcribe.py <audio.m4a> <out.json>
The gateway rejects multi-MB uploads, so the episode is split into fixed-length chunks,
each transcribed separately, and segment times are shifted back by the chunk offset.
"""
import json, subprocess, sys, urllib.request, uuid, time
from pathlib import Path

HERMES = Path("/Users/duhokim/.hermes/hermes-agent")
MODEL = "whisper-1"
# Vocabulary hint. Whisper biases toward terms it sees here, so the crew's names belong in it:
# a 2026-08-22 sweep found 29 captions carrying non-word garbles that no numeric check could see,
# and swapping base.en for whisper-1 fixed the physics words while leaving the PROPER NOUNS intact
# — "longdo" for Longo in a caption about his own dipole, "kuhn" for Kun, "goroo"/"guru's" for Goru.
# A better general model does not know who these people are. This list is the actual lever.
NAMES = ("Longo, Kun, Goru, Lana, Miru, Tori, Hwao, Blanc, Yui, Duho, "
         "Poplawski, Smolin, Brown, Rho, Bethe, Ferdman, Tauris, Mittal, Shamir, Kramer, Freire")
TERMS = ("NebulaMind, spacetime, Einstein-Cartan, torsion, spin fluid, fermion fields, Planck scale, "
         "cosmological principle, bounce, scale factor, nucleosynthesis, arXiv, "
         "dipole, anisotropy, chirality, kaon condensation, resampling, pre-registration, "
         "de-mirrored, spin parity, neutron star, DESI, Zenodo")
PROMPT = NAMES + ". " + TERMS + "."
CHUNK = 180  # seconds

src, out = Path(sys.argv[1]), Path(sys.argv[2])
work = src.parent / ("_chunks_" + src.stem)
work.mkdir(exist_ok=True)

dur = float(subprocess.run(["/opt/homebrew/bin/ffprobe", "-v", "error", "-show_entries",
                            "format=duration", "-of", "csv=p=0", str(src)],
                           capture_output=True, text=True).stdout.strip())

sys.path.insert(0, str(HERMES))
from tools.managed_tool_gateway import resolve_managed_tool_gateway
route = resolve_managed_tool_gateway("openai-audio")
url = route.gateway_origin.rstrip("/") + "/v1/audio/transcriptions"


def send(path: Path) -> dict:
    boundary = uuid.uuid4().hex
    fields = [("model", MODEL), ("response_format", "verbose_json"), ("language", "en"), ("prompt", PROMPT)]
    chunks = []
    for name, value in fields:
        chunks += [f"--{boundary}\r\n".encode(),
                   f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
                   value.encode() + b"\r\n"]
    chunks += [f"--{boundary}\r\n".encode(),
               f'Content-Disposition: form-data; name="file"; filename="{path.name}"\r\n'.encode(),
               b"Content-Type: audio/mpeg\r\n\r\n", path.read_bytes(), b"\r\n",
               f"--{boundary}--\r\n".encode()]
    body = b"".join(chunks)
    for attempt in range(1, 4):
        req = urllib.request.Request(url, data=body, method="POST")
        req.add_header("Authorization", "Bearer " + route.nous_user_token)
        req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
        try:
            return json.loads(urllib.request.urlopen(req, timeout=600).read())
        except Exception as e:
            if attempt == 3:
                raise
            time.sleep(3 * attempt)


all_segs = []
offset = 0.0
idx = 0
while offset < dur:
    piece = work / f"c{idx:02d}.mp3"
    if not piece.exists():
        subprocess.run(["/opt/homebrew/bin/ffmpeg", "-y", "-loglevel", "error", "-ss", str(offset),
                        "-t", str(CHUNK), "-i", str(src), "-ac", "1", "-ar", "16000",
                        "-b:a", "24k", str(piece)], check=True)
    mb = piece.stat().st_size / 1048576
    parsed = send(piece)
    n = 0
    for s in parsed.get("segments", []):
        all_segs.append({"start": round(s["start"] + offset, 2),
                         "end": round(s["end"] + offset, 2),
                         "text": s["text"].strip()})
        n += 1
    print(f"  chunk {idx} @{int(offset)}s ({mb:.2f}MB) -> {n} segments", flush=True)
    offset += CHUNK
    idx += 1

out.write_text(json.dumps({"duration": dur, "segments": all_segs}, indent=1, ensure_ascii=False),
               encoding="utf-8")
print(f"OK total_segments={len(all_segs)} duration={dur:.1f}")
