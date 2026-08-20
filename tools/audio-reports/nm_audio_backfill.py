#!/usr/bin/env python3
"""nm_audio_backfill.py — recover captions for readings whose text was never saved.

MUST run under /Users/duhokim/.hermes/hermes-agent/venv/bin/python (system
python3 has no faster_whisper).

Honesty rule: these captions are MACHINE TRANSCRIPTIONS of the audio, not the
original written text — that text is gone for pre-2026-08-20 readings. Each one
gets a <stem>.asr.json marker so pages can label it "auto-transcribed" and no
one mistakes a guess for a receipt. Verbatim captions written by the publisher
are never touched.
"""
from __future__ import annotations
import json, pathlib, sys, time

R = pathlib.Path("/Users/duhokim/HermesOps/reports/status-audio")
MODEL = "base.en"


def main() -> int:
    stems = []
    for mp3 in sorted(R.glob("*.mp3")):
        if mp3.stem.startswith("latest"):
            continue
        if not mp3.with_suffix(".txt").exists():
            stems.append(mp3)
    print(f"{len(stems)} reading(s) need a caption", flush=True)
    if not stems:
        return 0
    from faster_whisper import WhisperModel
    model = WhisperModel(MODEL, device="cpu", compute_type="int8")
    done = failed = 0
    for i, mp3 in enumerate(stems, 1):
        t0 = time.time()
        try:
            segments, info = model.transcribe(str(mp3), beam_size=1)
            text = " ".join(s.text.strip() for s in segments).strip()
            if not text:
                raise ValueError("empty transcription")
            # normalize the caption the same way live ones are
            sys.path.insert(0, str(R.parent.parent / "scripts"))
            try:
                import nm_caption_norm
                text, _ = nm_caption_norm.normalize(text)
            except Exception:
                pass
            mp3.with_suffix(".txt").write_text(text + "\n")
            mp3.with_suffix(".asr.json").write_text(json.dumps({
                "source": "asr-backfill", "model": MODEL,
                "language": getattr(info, "language", None),
                "duration_s": round(getattr(info, "duration", 0.0), 2),
                "note": "machine transcription of the audio; the original written text was not saved",
            }) + "\n")
            done += 1
        except Exception as exc:
            failed += 1
            print(f"  FAIL {mp3.name}: {type(exc).__name__}: {exc}", flush=True)
        if i % 10 == 0 or i == len(stems):
            print(f"  {i}/{len(stems)} ({done} ok, {failed} failed, {time.time()-t0:.1f}s last)", flush=True)
    print(f"backfilled {done}, failed {failed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
