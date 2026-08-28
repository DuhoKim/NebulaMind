#!/usr/bin/env python3
"""Generate exact per-panel narration with the prior Hermes gateway voice."""
from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
import time
import urllib.request
import wave
from pathlib import Path
from typing import Any

import pipeline

RATE = 48000
CHANNELS = 1
SAMPLE_WIDTH = 2
MODEL = "gpt-4o-mini-tts"
VOICE = "alloy"
SPEED = 1.14
PANEL_SPEEDS = {"02": 1.06, "08": 1.04}
CONTRACT_TAIL_BOOSTS = {"02": {"seconds": 1.8, "gain_db": 12.0}}
FPS = 30
LEAD_SECONDS = 0.45
TAIL_SECONDS = 0.85
HERMES_CHECKOUT = Path("/Users/duhokim/.hermes/hermes-agent")
BASE_INSTRUCTIONS = (
    "Read the input exactly as written in a calm, measured public-science voice. "
    "Do not add, omit, summarize, or rewrite any word. Speak every digit, number, quoted phrase, negation, caveat, and verdict carefully. "
    "Keep the pace steady and clinical, with brief natural sentence pauses. Pronounce NebulaMind as Nebula Mind."
)


def instruction_policy(panel_id: str) -> str:
    additions = {
        "01": " Clearly enunciate 4; 10,000 to 100,000; no observable signature survives; and the route stays closed.",
        "02": " Say SPACETIME as one word. Clearly say negative 1 shifted 70 places. Preserve the no-plots sentence exactly. Do not stop early after the words decimal point. The final clause A WHISPER must be fully audible at the same normal speaking volume as the rest. Do not literally whisper those two words. Emphasize both final words and complete the terminal sentence.",
        "03": " Clearly say 6 neutrino types, exactly 6 times smaller, lined-up edge, unread behind a paywall, and quarantined. Do not stop early. Finish the final sentence exactly: The spring-like picture survives as a proposal; its exact strength is not unique.",
        "04": " Clearly say fermion fields, scale factor, sharp bottom, cusp, and only chain paper with plots.",
        "05": " Say NEARS the Planck scale with a clear N sound; never say mirrors. Preserve both quoted phrases exactly: not self-consistent; violates the cosmological principle. Clearly say about 730 and prescribed to jump outward.",
        "06": " Clearly say fixed compactness, the 1 inheritance channel, and preserve the no-plots sentence exactly.",
        "07": " Clearly say conjecture, horizon matching, one-way boundary, and 1 meter.",
        "08": " Say seed POD, with pod rhyming with nod and a clear final D. Give the repaired two-clause sentence extra care. Say exactly: Across all 4 papers, no equation carries the parent's spin through the bounce; the collapse papers mention it in exactly 1 sentence. Say the base form COLLAPSE PAPERS with a crisp S sound and a brief pause before papers; never add a D sound and never say collapsed papers. Then read the quoted sentence exactly. Preserve every no equation, no rotating model, and no calculation clause.",
        "09": " Clearly say 10-solar-mass; 6.6 times 10 to the power 26; 1 part in 10 to the power 27; roughly 1 order of magnitude. Preserve exactly: And if a spinning parent can't make their bounce at all, there is even less to see.",
        "10": " Clearly say helium, deuterium, lithium, 30 times radiation at 10 megaelectronvolts, and 45 orders of magnitude. Preserve the positive-versus-negative sign caveat.",
        "11": " Clearly say 1 part in 10,000 to 100,000; all 2 trillion observable galaxies; theoretical best, not an instrument. Preserve the entire One honest caveat sentence exactly, including Planck regime treated classically and awaits external theorist review.",
        "12": " Preserve all four numbered paper clauses, 1 unsupported sentence, 10,000 to 100,000 times, and the final verdict exactly. Pronounce both instances of ROUTE as ROWT with a crisp final T, never as root. Finish distinctly on: the ceiling says the route stays closed.",
    }
    return BASE_INSTRUCTIONS + additions.get(panel_id, "")


def gateway() -> Any:
    sys.path.insert(0, str(HERMES_CHECKOUT))
    from tools.managed_tool_gateway import resolve_managed_tool_gateway  # type: ignore[import-not-found]
    return resolve_managed_tool_gateway("openai-audio")


def synthesize(text: str, instructions: str, speed: float, output: Path, failure_log: Path) -> None:
    route = gateway()
    body = json.dumps({
        "model": MODEL,
        "voice": VOICE,
        "input": text,
        "speed": speed,
        "response_format": "wav",
        "instructions": instructions,
    }, ensure_ascii=False).encode("utf-8")
    url = route.gateway_origin.rstrip("/") + "/v1/audio/speech"
    for attempt in range(1, 4):
        request = urllib.request.Request(url, data=body, method="POST")
        request.add_header("Authorization", "Bearer " + route.nous_user_token)
        request.add_header("Content-Type", "application/json")
        try:
            payload = urllib.request.urlopen(request, timeout=300).read()
            if not payload:
                raise RuntimeError("empty TTS response")
            output.write_bytes(payload)
            return
        except Exception as exc:
            with failure_log.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps({"panel_text_sha256": pipeline.text_sha256(text), "attempt": attempt, "error_type": type(exc).__name__, "error": str(exc)[:500]}) + "\n")
            if attempt == 3:
                raise
            time.sleep(2 * attempt)


def convert_pcm(source: Path, destination: Path) -> None:
    subprocess.run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(source),
        "-ac", str(CHANNELS), "-ar", str(RATE), "-c:a", "pcm_s16le", str(destination),
    ], check=True)


def apply_contract_tail_boost(path: Path, seconds: float, gain_db: float) -> None:
    _, frames = wav_frames(path)
    start = max(0.0, frames / RATE - seconds)
    temporary = pipeline.BUILD / f"_tmp_boost-{path.name}"
    gain = 10 ** (gain_db / 20.0)
    subprocess.run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(path),
        "-af", f"volume='if(gte(t,{start:.6f}),{gain:.8f},1.0)':eval=frame",
        "-ac", str(CHANNELS), "-ar", str(RATE), "-c:a", "pcm_s16le", str(temporary),
    ], check=True)
    temporary.replace(path)


def wav_frames(path: Path) -> tuple[bytes, int]:
    with wave.open(str(path), "rb") as source:
        shape = (source.getnchannels(), source.getsampwidth(), source.getframerate())
        if shape != (CHANNELS, SAMPLE_WIDTH, RATE):
            raise RuntimeError(f"unexpected WAV shape for {path}: {shape}")
        return source.readframes(source.getnframes()), source.getnframes()


def timestamp(seconds: float, comma: bool) -> str:
    milliseconds = round(seconds * 1000)
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    secs, milliseconds = divmod(milliseconds, 1000)
    separator = "," if comma else "."
    return f"{hours:02d}:{minutes:02d}:{secs:02d}{separator}{milliseconds:03d}"


def plan_timeline(panels: list[dict[str, Any]], durations: dict[str, float]) -> dict[str, Any]:
    cursor = 0
    cards: list[dict[str, Any]] = []
    for panel in panels:
        planned_frames = round(float(panel["planned_seconds"]) * FPS)
        needed_samples = round((LEAD_SECONDS + durations[panel["id"]] + TAIL_SECONDS) * RATE)
        needed_frames = math.ceil(needed_samples * FPS / RATE)
        frame_count = max(planned_frames, needed_frames)
        card_samples = frame_count * RATE // FPS
        start = cursor
        speech_start = start + round(LEAD_SECONDS * RATE)
        speech_end = speech_start + round(durations[panel["id"]] * RATE)
        end = start + card_samples
        cards.append({
            "card_id": panel["id"],
            "heading": panel["assertion_heading"],
            "narration": panel["narration"],
            "narration_sha256": pipeline.text_sha256(panel["narration"]),
            "start_sample": start,
            "speech_start_sample": speech_start,
            "speech_end_sample": speech_end,
            "end_sample": end,
            "start_seconds": start / RATE,
            "speech_start_seconds": speech_start / RATE,
            "speech_end_seconds": speech_end / RATE,
            "end_seconds": end / RATE,
            "frame_count": frame_count,
            "effective_seconds": card_samples / RATE,
            "planned_seconds": float(panel["planned_seconds"]),
            "timing_extension_seconds": card_samples / RATE - float(panel["planned_seconds"]),
            "tail_dwell_seconds": (end - speech_end) / RATE,
        })
        cursor = end
    duration = cursor / RATE
    if not 390.0 <= duration <= 480.0:
        raise RuntimeError(f"audio-first master outside 6.5–8 minute contract: {duration:.3f}s")
    if cards[0]["end_seconds"] > 35.0:
        raise RuntimeError(f"opening panel misses 35-second contract: {cards[0]['end_seconds']:.3f}s")
    return {"sample_rate_hz": RATE, "master_sample_count": cursor, "master_duration_seconds": duration, "cards": cards}


def write_captions(timeline: dict[str, Any], audio_dir: Path) -> tuple[Path, Path]:
    srt: list[str] = []
    vtt: list[str] = ["WEBVTT", ""]
    for index, card in enumerate(timeline["cards"], 1):
        srt.extend([str(index), f"{timestamp(card['speech_start_seconds'], True)} --> {timestamp(card['speech_end_seconds'], True)}", card["narration"], ""])
        vtt.extend([str(index), f"{timestamp(card['speech_start_seconds'], False)} --> {timestamp(card['speech_end_seconds'], False)}", card["narration"], ""])
    srt_path, vtt_path = audio_dir / "narration.srt", audio_dir / "narration.vtt"
    srt_path.write_text("\n".join(srt), encoding="utf-8")
    vtt_path.write_text("\n".join(vtt), encoding="utf-8")
    return srt_path, vtt_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--regenerate", action="append", default=[], help="panel id to resynthesize; repeatable")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    regenerate = {str(value).zfill(2) for value in args.regenerate}
    frozen = pipeline.load_frozen_inputs()
    valid_ids = {panel["id"] for panel in frozen["panels"]}
    if not regenerate.issubset(valid_ids):
        raise RuntimeError(f"unknown regenerate panel ids: {sorted(regenerate - valid_ids)}")
    audio_dir = pipeline.BUILD / "audio"
    receipt_dir = audio_dir / "receipts"
    audio_dir.mkdir(parents=True, exist_ok=True)
    receipt_dir.mkdir(parents=True, exist_ok=True)
    failures = audio_dir / "tts_failures.jsonl"
    durations: dict[str, float] = {}
    assets: dict[str, dict[str, Any]] = {}

    for panel in frozen["panels"]:
        panel_id = panel["id"]
        final = audio_dir / f"narration-{panel_id}.wav"
        receipt_path = receipt_dir / f"narration-{panel_id}.json"
        instructions = instruction_policy(panel_id)
        speed = PANEL_SPEEDS.get(panel_id, SPEED)
        text_hash = pipeline.text_sha256(panel["narration"])
        instruction_hash = pipeline.text_sha256(instructions)
        must_generate = panel_id in regenerate or not final.exists()
        if not must_generate:
            if not receipt_path.exists():
                raise RuntimeError(f"refusing filename-only TTS cache: {final}")
            cached = json.loads(receipt_path.read_text(encoding="utf-8"))
            if cached["text_sha256"] != text_hash or cached["model"] != MODEL or cached["voice"] != VOICE or cached["speed"] != speed or cached["instructions_sha256"] != instruction_hash or cached["audio_sha256"] != pipeline.sha256(final):
                raise RuntimeError(f"TTS cache contract mismatch for panel {panel_id}")
        else:
            temporary = pipeline.BUILD / f"_tmp_tts-{panel_id}.wav"
            synthesize(panel["narration"], instructions, speed, temporary, failures)
            convert_pcm(temporary, final)
            temporary.unlink(missing_ok=True)
            if panel_id in CONTRACT_TAIL_BOOSTS:
                apply_contract_tail_boost(final, **CONTRACT_TAIL_BOOSTS[panel_id])
        _, frames = wav_frames(final)
        duration = frames / RATE
        durations[panel_id] = duration
        record = {
            "panel_id": panel_id,
            "input_text": panel["narration"],
            "text_sha256": text_hash,
            "storyboard_narration_sha256": panel["narration_sha256"],
            "input_byte_identical_to_storyboard": text_hash == panel["narration_sha256"],
            "model": MODEL,
            "voice": VOICE,
            "speed": speed,
            "postprocess": {"contract_tail_boost": CONTRACT_TAIL_BOOSTS.get(panel_id)},
            "instructions_sha256": instruction_hash,
            "provider_route": "Hermes managed OpenAI audio gateway",
            "audio": str(final.relative_to(pipeline.BUILD)),
            "audio_sha256": pipeline.sha256(final),
            "frames": frames,
            "duration_seconds": duration,
        }
        receipt_path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        assets[panel_id] = record
        print(f"panel {panel_id}: {duration:.3f}s")

    timeline = plan_timeline(frozen["panels"], durations)
    master = bytearray(timeline["master_sample_count"] * SAMPLE_WIDTH)
    for card in timeline["cards"]:
        asset = assets[card["card_id"]]
        frames, frame_count = wav_frames(pipeline.BUILD / asset["audio"])
        offset = card["speech_start_sample"] * SAMPLE_WIDTH
        master[offset:offset + len(frames)] = frames
        card["audio"] = asset["audio"]
        card["audio_sha256"] = asset["audio_sha256"]
        card["audio_frames"] = frame_count
    master_path = audio_dir / "narration_master.wav"
    with wave.open(str(master_path), "wb") as output:
        output.setnchannels(CHANNELS)
        output.setsampwidth(SAMPLE_WIDTH)
        output.setframerate(RATE)
        output.writeframes(master)
    srt_path, vtt_path = write_captions(timeline, audio_dir)
    timeline.update({
        "status": "PASS_EXACT_PANEL_TTS_INPUT_AND_FIXED_TIMELINE_PENDING_FULL_ASR",
        "model": MODEL,
        "voice": VOICE,
        "speed": {"default": SPEED, "panel_overrides": PANEL_SPEEDS},
        "provider_route": "Hermes managed OpenAI audio gateway",
        "gated_storyboard_sha256": pipeline.sha256(pipeline.STORYBOARD),
        "gated_script_sha256": pipeline.sha256(pipeline.SCRIPT),
        "master_audio": str(master_path.relative_to(pipeline.BUILD)),
        "master_audio_sha256": pipeline.sha256(master_path),
        "srt": str(srt_path.relative_to(pipeline.BUILD)),
        "srt_sha256": pipeline.sha256(srt_path),
        "vtt": str(vtt_path.relative_to(pipeline.BUILD)),
        "vtt_sha256": pipeline.sha256(vtt_path),
        "panel_wavs": [assets[panel["id"]] for panel in frozen["panels"]],
        "all_tts_inputs_byte_identical_to_storyboard_narration": all(asset["input_byte_identical_to_storyboard"] for asset in assets.values()),
    })
    (audio_dir / "timeline.json").write_text(json.dumps(timeline, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": timeline["status"], "duration_seconds": timeline["master_duration_seconds"], "panel_wavs": len(timeline["panel_wavs"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
