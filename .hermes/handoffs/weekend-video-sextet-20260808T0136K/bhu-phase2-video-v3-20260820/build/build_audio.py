#!/usr/bin/env python3
"""Generate byte-identical v3 panel narration through the Hermes gateway."""
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
VOICE = "alloy"  # same voice as v2
SPEED = 0.88     # deliberately slower than default; never speed the voice up
FPS = 30
LEAD_SECONDS = 0.55
MIN_PANEL_TURN_SILENCE = 1.75
FRAGMENT_BOUNDARY_SILENCE = 0.28
HERMES_CHECKOUT = Path("/Users/duhokim/.hermes/hermes-agent")
BASE_INSTRUCTIONS = (
    "Read the input exactly as written in a calm, measured public-science voice at about 130 words per minute. "
    "Do not add, omit, summarize, paraphrase, or rewrite any word. Do not literally whisper any phrase. "
    "Speak every digit, number, quotation, negation, caveat, comparison, and verdict distinctly. "
    "Use brief natural sentence pauses and finish the final sentence at normal volume. "
    "Pronounce NebulaMind as Nebula Mind."
)
PANEL_INSTRUCTIONS = {
    "01": " Clearly preserve 4; 10,000 to 100,000; no observable signature survives; and the route stays closed. Do not stop after route stays closed. Finish exactly and audibly: Here's how we got there.",
    "04": " Clearly complete the phrase negative 1 sitting 70 places after the decimal point.",
    "05": " Clearly say 6 neutrino species, exactly 6 times smaller, lined-up edge, and carry both.",
    "06": " Clearly distinguish the correction notice exists from its words remain paywalled and unread.",
    "07": " Clearly say fermion fields, scale factor, sharp bottom, cusp, and smooth U-turn.",
    "08": " Preserve both quoted phrases, cosmological principle, about 730 times, and written in by hand.",
    "09": " Clearly say fixed compactness, parent mass, starting size and heat, no plots, and rotation stays outside the map.",
    "10": " Clearly preserve exactly 1 meter wide, about a doorway, and the paper never states that choice.",
    "11": " Preserve the entire two-clause sentence and quotation exactly. Say collapse papers, not collapsed papers. Finish the full rotating-fluid quotation before continuing.",
    "12": " Clearly say 10-solar-mass, spin-0.7, 6.6 times 10 to the power 26, 1 part in 10 to the power 27, roughly 1 order of magnitude, the full grain comparison, and the full conditional sentence beginning And if a spinning parent.",
    "13": " Clearly distinguish torsion and shear; finish This is a condition, not a signal size.",
    "14": " Clearly say 10 megaelectronvolts, up to 30 times radiation, about 45 orders of magnitude, and the full ocean-molecule comparison.",
    "15": " Clearly say all 2 trillion observable galaxies, not an instrument, 10,000 to 100,000 times, and the entire One honest caveat sentence.",
    "16": " Preserve each paper verdict, 10,000 to 100,000 times, and finish distinctly on The ceiling says the route stays closed.",
}


def gateway() -> Any:
    sys.path.insert(0, str(HERMES_CHECKOUT))
    from tools.managed_tool_gateway import resolve_managed_tool_gateway  # type: ignore[import-not-found]
    return resolve_managed_tool_gateway("openai-audio")


def synthesize(text: str, instructions: str, output: Path, failure_log: Path) -> None:
    route = gateway()
    body = json.dumps({
        "model": MODEL,
        "voice": VOICE,
        "input": text,
        "speed": SPEED,
        "response_format": "wav",
        "instructions": instructions,
    }, ensure_ascii=False).encode("utf-8")
    url = route.gateway_origin.rstrip("/") + "/v1/audio/speech"
    for attempt in range(1, 4):
        req = urllib.request.Request(url, data=body, method="POST")
        req.add_header("Authorization", "Bearer " + route.nous_user_token)
        req.add_header("Content-Type", "application/json")
        try:
            payload = urllib.request.urlopen(req, timeout=300).read()
            if not payload:
                raise RuntimeError("empty TTS response")
            output.write_bytes(payload)
            return
        except Exception as exc:
            with failure_log.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps({"text_sha256": pipeline.text_sha256(text), "attempt": attempt, "error_type": type(exc).__name__, "error": str(exc)[:500]}) + "\n")
            if attempt == 3:
                raise
            time.sleep(2 * attempt)


def convert_pcm(source: Path, destination: Path) -> None:
    subprocess.run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(source),
        # The TTS endpoint adds variable dead air around short exact-text
        # fragments. Trim only those outer silences; do not tempo-shift speech.
        "-af", "areverse,silenceremove=start_periods=1:start_duration=0.08:start_threshold=-55dB,areverse,loudnorm=I=-18:TP=-2:LRA=7",
        "-ac", str(CHANNELS), "-ar", str(RATE),
        "-c:a", "pcm_s16le", str(destination),
    ], check=True)


def wav_frames(path: Path) -> tuple[bytes, int]:
    with wave.open(str(path), "rb") as source:
        shape = (source.getnchannels(), source.getsampwidth(), source.getframerate())
        if shape != (CHANNELS, SAMPLE_WIDTH, RATE):
            raise RuntimeError(f"unexpected WAV shape for {path}: {shape}")
        frames = source.getnframes()
        return source.readframes(frames), frames


def tts_fragments(panel: dict[str, Any]) -> list[str]:
    """Exact ordered slices whose single-space join is the narration."""
    text = panel["narration"]
    split_starts = {
        "01": ["Here's how we got there."],
        "10": ["none is provided.", "The showcase numbers need a starting ball", "Where, then, is the spin bridge?"],
        "12": ["Requiring the paper's uniform bounce", "Would the bounce smooth lopsidedness?"],
        "13": ["The bounce neither smooths nor creates lopsidedness.", "Any lasting memory depends on particle production"],
        "14": ["The ceiling allows up to 30 times radiation", "Could perfect galaxy counting do better?"],
        "16": [
            "The spring paper proposes a bounce", "The sharp-corner paper replaces that engine",
            "The mass-map paper passes starting size and heat", "The collapse paper offers a lone unsupported line",
            "Helium hears no whisper.",
        ],
    }
    starts = split_starts.get(panel["id"], [])
    if not starts:
        return [text]
    positions = [0]
    for start in starts:
        index = text.find(start)
        if index <= 0:
            raise RuntimeError(f"panel {panel['id']} fragment marker changed: {start}")
        positions.append(index)
    positions.append(len(text))
    if positions != sorted(set(positions)):
        raise RuntimeError(f"panel {panel['id']} fragment markers are not ordered")
    fragments = [text[positions[i]:positions[i+1]].strip() for i in range(len(positions)-1)]
    if " ".join(fragments).encode("utf-8") != text.encode("utf-8"):
        raise RuntimeError("fragment join is not byte-identical to storyboard narration")
    return fragments


def synthesize_panel(panel: dict[str, Any], instructions: str, destination: Path, failures: Path) -> list[str]:
    """Synthesize exact text slices and join them without changing text order."""
    fragments = tts_fragments(panel)
    fragment_hints = {
        "10": "Begin the showcase sentence with the written article The. Pronounce need with a clear final D, and paper as that exact noun, never papering.",
        "12": "Start the first fragment with the article A pronounced uh, never The. Enunciate past with an audible final T. Say bounce, not balance; Requiring with initial R; inherited as one word ending in ED, never inherit its; Picture with initial P; and Would to rhyme with could, never With.",
        "13": "Enunciate smooths with its final S, and preserve the written articles exactly: a signal size, not the signal size.",
        "16": "Say mass-map as the two nouns mass map, never matte or mapped. Say collapse as a noun with no D ending, never collapsed. Pronounce every occurrence of route to rhyme with out, never root.",
    }
    pcm_parts: list[Path] = []
    for index, fragment in enumerate(fragments):
        raw = pipeline.BUILD / f"_tmp_tts-{panel['id']}-{index:02d}-raw.wav"
        pcm = pipeline.BUILD / f"_tmp_tts-{panel['id']}-{index:02d}-pcm.wav"
        if len(fragments) > 1:
            fragment_instructions = BASE_INSTRUCTIONS + " Speak only the supplied text fragment completely. " + fragment_hints.get(panel["id"], "")
        else:
            fragment_instructions = instructions
        synthesize(fragment, fragment_instructions, raw, failures)
        convert_pcm(raw, pcm)
        raw.unlink(missing_ok=True)
        pcm_parts.append(pcm)
    if len(pcm_parts) == 1:
        pcm_parts[0].replace(destination)
    else:
        joined = bytearray()
        for index, pcm in enumerate(pcm_parts):
            frames, _ = wav_frames(pcm)
            if index:
                joined.extend(b"\0" * (round(FRAGMENT_BOUNDARY_SILENCE * RATE) * SAMPLE_WIDTH))
            joined.extend(frames)
        with wave.open(str(destination), "wb") as output:
            output.setnchannels(CHANNELS)
            output.setsampwidth(SAMPLE_WIDTH)
            output.setframerate(RATE)
            output.writeframes(joined)
    for pcm in pcm_parts:
        pcm.unlink(missing_ok=True)
    return fragments


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
        needed_samples = round((LEAD_SECONDS + durations[panel["id"]] + MIN_PANEL_TURN_SILENCE) * RATE)
        needed_frames = math.ceil(needed_samples * FPS / RATE)
        frame_count = max(planned_frames, needed_frames)
        card_samples = frame_count * RATE // FPS
        start = cursor
        speech_start = start + round(LEAD_SECONDS * RATE)
        speech_end = speech_start + round(durations[panel["id"]] * RATE)
        end = start + card_samples
        turn_silence = (end - speech_end) / RATE
        if turn_silence < MIN_PANEL_TURN_SILENCE - 1 / RATE:
            raise RuntimeError(f"panel {panel['id']} breathing gap too short: {turn_silence}")
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
            "lead_silence_seconds": LEAD_SECONDS,
            "panel_turn_silence_seconds": turn_silence,
        })
        cursor = end
    duration = cursor / RATE
    if not 600.0 <= duration <= 720.0:
        raise RuntimeError(f"master outside 10–12 minute contract: {duration:.3f}s")
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
    parser.add_argument("--probe", help="synthesize one panel to _tmp and report measured WPM")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    frozen = pipeline.load_frozen_inputs()
    panels = frozen["panels"]
    failures = pipeline.BUILD / "_tmp_tts_failures.jsonl"
    if args.probe:
        panel_id = str(args.probe).zfill(2)
        panel = next((p for p in panels if p["id"] == panel_id), None)
        if panel is None:
            raise RuntimeError(f"unknown probe panel {panel_id}")
        raw = pipeline.BUILD / f"_tmp_probe-{panel_id}-raw.wav"
        pcm = pipeline.BUILD / f"_tmp_probe-{panel_id}.wav"
        synthesize(panel["narration"], BASE_INSTRUCTIONS + PANEL_INSTRUCTIONS.get(panel_id, ""), raw, failures)
        convert_pcm(raw, pcm)
        _, frames = wav_frames(pcm)
        duration = frames / RATE
        wpm = int(panel["word_count"]) / duration * 60
        print(json.dumps({"panel": panel_id, "words": panel["word_count"], "duration_seconds": duration, "measured_wpm": wpm, "speed": SPEED}))
        return 0

    regenerate = {str(value).zfill(2) for value in args.regenerate}
    valid_ids = {panel["id"] for panel in panels}
    if not regenerate.issubset(valid_ids):
        raise RuntimeError(f"unknown regenerate panel ids: {sorted(regenerate-valid_ids)}")
    audio_dir = pipeline.BUILD / "audio"
    receipts = audio_dir / "receipts"
    audio_dir.mkdir(parents=True, exist_ok=True)
    receipts.mkdir(parents=True, exist_ok=True)
    durations: dict[str, float] = {}
    assets: dict[str, dict[str, Any]] = {}

    for panel in panels:
        panel_id = panel["id"]
        final = audio_dir / f"narration-{panel_id}.wav"
        receipt_path = receipts / f"narration-{panel_id}.json"
        instructions = BASE_INSTRUCTIONS + PANEL_INSTRUCTIONS.get(panel_id, "")
        fragments = tts_fragments(panel)
        text_hash = pipeline.text_sha256(panel["narration"])
        instruction_hash = pipeline.text_sha256(instructions)
        must_generate = panel_id in regenerate or not final.exists()
        if not must_generate:
            if not receipt_path.exists():
                raise RuntimeError(f"refusing filename-only TTS cache: {final}")
            cached = json.loads(receipt_path.read_text(encoding="utf-8"))
            if any([
                cached["text_sha256"] != text_hash,
                cached["model"] != MODEL,
                cached["voice"] != VOICE,
                cached["speed"] != SPEED,
                cached["instructions_sha256"] != instruction_hash,
                cached["audio_sha256"] != pipeline.sha256(final),
                cached.get("input_fragments", [cached.get("input_text", "")]) != fragments,
            ]):
                raise RuntimeError(f"TTS cache contract mismatch for panel {panel_id}")
        else:
            fragments = synthesize_panel(panel, instructions, final, failures)
        _, frames = wav_frames(final)
        duration = frames / RATE
        durations[panel_id] = duration
        record = {
            "panel_id": panel_id,
            "input_text": panel["narration"],
            "input_fragments": fragments,
            "concatenated_fragments_byte_identical_to_storyboard": " ".join(fragments).encode("utf-8") == panel["narration"].encode("utf-8"),
            "fragment_boundary_silence_seconds": FRAGMENT_BOUNDARY_SILENCE if len(fragments) > 1 else 0.0,
            "text_sha256": text_hash,
            "storyboard_narration_sha256": panel["narration_sha256"],
            "input_byte_identical_to_storyboard": text_hash == panel["narration_sha256"],
            "model": MODEL,
            "voice": VOICE,
            "speed": SPEED,
            "voice_was_sped_up": False,
            "measured_wpm": int(panel["word_count"]) / duration * 60,
            "instructions_sha256": instruction_hash,
            "provider_route": "Hermes managed OpenAI audio gateway",
            "audio": str(final.relative_to(pipeline.BUILD)),
            "audio_sha256": pipeline.sha256(final),
            "frames": frames,
            "duration_seconds": duration,
        }
        receipt_path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        assets[panel_id] = record
        print(f"panel {panel_id}: {duration:.3f}s, {record['measured_wpm']:.1f} wpm")

    narration_seconds = sum(durations.values())
    overall_wpm = sum(int(p["word_count"]) for p in panels) / narration_seconds * 60
    # The brief's pace is approximate. Keep a half-word rounding tolerance;
    # the exact measured value is preserved in every receipt and freeze file.
    if not 124.5 <= overall_wpm <= 135.5:
        raise RuntimeError(f"measured narration pace outside approximate 125–135 wpm: {overall_wpm:.2f}")
    timeline = plan_timeline(panels, durations)
    master = bytearray(timeline["master_sample_count"] * SAMPLE_WIDTH)
    for card in timeline["cards"]:
        asset = assets[card["card_id"]]
        frames, frame_count = wav_frames(pipeline.BUILD / asset["audio"])
        offset = card["speech_start_sample"] * SAMPLE_WIDTH
        master[offset:offset+len(frames)] = frames
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
        "status": "PASS_BYTE_IDENTICAL_TTS_MEASURED_APPROX_125_TO_135_WPM_WITH_EXPLICIT_PANEL_TURN_SILENCE",
        "model": MODEL, "voice": VOICE, "speed": SPEED, "voice_was_sped_up": False,
        "provider_route": "Hermes managed OpenAI audio gateway",
        "measured_narration_wpm": overall_wpm,
        "narration_only_seconds": narration_seconds,
        "gated_storyboard_sha256": pipeline.sha256(pipeline.STORYBOARD),
        "gated_script_sha256": pipeline.sha256(pipeline.SCRIPT),
        "master_audio": str(master_path.relative_to(pipeline.BUILD)),
        "master_audio_sha256": pipeline.sha256(master_path),
        "srt": str(srt_path.relative_to(pipeline.BUILD)), "srt_sha256": pipeline.sha256(srt_path),
        "vtt": str(vtt_path.relative_to(pipeline.BUILD)), "vtt_sha256": pipeline.sha256(vtt_path),
        "panel_wavs": [assets[p["id"]] for p in panels],
        "all_tts_inputs_byte_identical_to_storyboard_narration": all(a["input_byte_identical_to_storyboard"] for a in assets.values()),
        "all_panel_turn_gaps_at_least_seconds": MIN_PANEL_TURN_SILENCE,
    })
    (audio_dir / "timeline.json").write_text(json.dumps(timeline, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": timeline["status"], "duration_seconds": timeline["master_duration_seconds"], "measured_wpm": overall_wpm, "panel_wavs": len(timeline["panel_wavs"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
