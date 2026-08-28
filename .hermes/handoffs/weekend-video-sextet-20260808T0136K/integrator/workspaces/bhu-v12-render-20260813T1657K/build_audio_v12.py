#!/usr/bin/env python3
"""Build exact-source V12 audio at 142 WPM from V11's custodied raw Edge-TTS inputs."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import wave
from datetime import datetime, timezone
from pathlib import Path

SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K")
ROOT = Path(__file__).resolve().parent
V11_ROOT = ROOT.parent / "bhu-v11-render-20260813T1526K"
STORY = SOURCE / "STORYBOARD_DRAFT_V12.json"
NARRATION = SOURCE / "NARRATION_DRAFT_V12.md"
SPEC = SOURCE / "LANA_VISUAL_REDESIGN_SPEC.md"
EXPECTED = {
    "STORYBOARD_DRAFT_V12.json": "9d55257fe62c7a82d2fe32f424e896ce079393219c08aed6663b6c90c3539399",
    "NARRATION_DRAFT_V12.md": "178ffe4ada125668c8ff84bc156adee7820954591f9781adb7101aac562d80da",
    "LANA_VISUAL_REDESIGN_SPEC.md": "cf9cefe8a0c07f8cc960388004a20d4518a7cf7fbcea5ff688825ffdc47bfd22",
}
V11_TIMELINE_SHA = "0fdcc404e4b4e5886f82f776cc239e494d7c9f8d60a62773ab5628f003981048"
TARGET_WPM = 142.0
WPM_BAND = (135.0, 150.0)
SAMPLE_RATE = 48_000
LEAD_SECONDS = 0.06
TAIL_SECONDS = 0.08
AUDIO_DIR = ROOT / "audio"
CARD_DIR = AUDIO_DIR / "cards"
MASTER = AUDIO_DIR / "narration_master.wav"
TIMELINE = AUDIO_DIR / "timeline.json"
SRT = ROOT / "captions_v12.srt"
VTT = ROOT / "captions_v12.vtt"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, capture_output=True, text=True)


def duration(path: Path) -> float:
    return float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)).stdout.strip())


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower().replace("’", "'").replace("‘", "'"))


def word_count(text: str) -> int:
    return len(re.findall(r"[^\W_]+(?:[’'][^\W_]+)?", re.sub(r"[—–-]", " ", text), flags=re.UNICODE))


def split_sentences(text: str) -> list[str]:
    return re.split(r"(?<=[.!?])\s+(?=[A-Z“‘])", text)


def cue_fragments(card_id: str, narration: str) -> list[str]:
    result = split_sentences(narration)
    if card_id == "02":
        expected = "We found at least five different proposals under this label — black-hole universe, or BHU for short."
        if result[1] != expected:
            raise RuntimeError("Card 02 earning sentence drift")
        result[1:2] = ["We found at least five different proposals under this label —", "black-hole universe, or", "BHU for short."]
    if card_id == "04":
        expected = "One proposal — called cosmological natural selection — says universes have children: every black hole buds off a new universe with slightly different physics."
        if result[0] != expected:
            raise RuntimeError("Card 04 earning sentence drift")
        result[0:1] = ["One proposal — called", "cosmological", "natural", "selection —", "says universes have children: every black hole buds off a new universe with slightly different physics."]
    if tokens(" ".join(result)) != tokens(narration):
        raise RuntimeError(f"caption token reconstruction failed Card {card_id}")
    return result


def flatten_events(text: str, events: list[dict]) -> list[dict]:
    flat = []
    for event in events:
        parts = tokens(str(event["text"]))
        if not parts:
            continue
        start = float(event["offset_seconds"])
        span = float(event["duration_seconds"])
        for index, token in enumerate(parts):
            flat.append({
                "token": token,
                "raw_start_seconds": start + span * index / len(parts),
                "raw_end_seconds": start + span * (index + 1) / len(parts),
            })
    if [item["token"] for item in flat] != tokens(text):
        raise RuntimeError("custodied raw word boundaries no longer match exact narration")
    return flat


def locate(stream: list[dict], phrase: str, start: int = 0) -> tuple[int, int]:
    needle = tokens(phrase)
    haystack = [item["token"] for item in stream]
    for index in range(start, len(haystack) - len(needle) + 1):
        if haystack[index:index + len(needle)] == needle:
            return index, index + len(needle) - 1
    raise RuntimeError(f"phrase not found: {phrase}")


def stamp(seconds: float, decimal: str) -> str:
    milliseconds = round(seconds * 1000)
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    seconds, milliseconds = divmod(milliseconds, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}{decimal}{milliseconds:03d}"


def render_sidecar(cues: list[dict], vtt: bool) -> str:
    lines = ["WEBVTT", ""] if vtt else []
    decimal = "." if vtt else ","
    for index, cue in enumerate(cues, 1):
        lines += [str(index), f"{stamp(cue['master_start_seconds'], decimal)} --> {stamp(cue['master_end_seconds'], decimal)}", cue["text"], ""]
    return "\n".join(lines)


def make_reveals(card_id: str, stream: list[dict], master_start: float) -> list[dict]:
    def witness(name: str, phrase: str, edge: str = "end") -> dict:
        first, last = locate(stream, phrase)
        at = stream[first]["card_start_seconds"] if edge == "start" else stream[last]["card_end_seconds"]
        return {"name": name, "phrase": phrase, "edge": edge, "card_seconds": at, "master_seconds": master_start + at}

    definitions = {
        "01": [("primary_sources", "We read the original papers", "start"), ("number_we_can_check", "One idea gives us a number", "start"), ("galaxy_spin_limits", "For galaxy spin", "start"), ("route_verdict", "So this route closes", "start"), ("true_false_boundary", "The idea is not declared true or false", "start")],
        "02": [("bhu", "black-hole universe, or BHU for short", "end"), ("proposal_1", "A closed universe inside a black hole", "start"), ("proposal_2", "A collapse that bounces", "start"), ("proposal_3", "A universe that inherits its parent's spin", "start"), ("proposal_4", "Universes that reproduce", "start"), ("proposal_5", "And baby universes", "start"), ("no_shared_forecast", "Five ideas", "start"), ("closing_record", "We wrote what we found into a closing record", "start")],
        "03": [("target", "It needs a number", "start"), ("identify", "And if you find it", "start"), ("neutron_stars", "It uses neutron stars", "start"), ("pulsars", "The ones we can time as they spin", "start")],
        "04": [("family_tree", "One proposal", "start"), ("mass_1_5", "one point five solar masses", "end"), ("mass_2", "approximately two solar masses or above", "end"), ("source_quote", "serious doubt or simply falsify", "end")],
        "05": [("demorest_uncertainty", "give or take point zero four", "end"), ("fonseca_uncertainty", "give or take point zero seven", "end"), ("percent_68_3", "sixty-eight point three percent", "end"), ("percent_95_4", "ninety-five point four percent", "end")],
        "06": [("source_disjunction", "serious doubt, or simply falsify", "end"), ("not_adjudicated", "does not decide which side applies", "end"), ("named_regime", "entered the regime named by the source", "end")],
        "07": [("inherited_axis", "inherits its axis", "end"), ("cw_ccw", "clockwise- and counterclockwise-spinning galaxy counts should be different", "end"), ("no_amplitude", "What's missing is any number", "start")],
        "08": [("timeline", "after the galaxy studies", "end"), ("post_data", "not a prediction made before the data", "end"), ("forecast_blanks", "not a numerical forecast", "end")],
        "09": [("observed_difference", "spin-handedness difference", "end"), ("not_identify", "would not identify BHU by itself", "end"), ("other_causes", "several different causes", "end"), ("measurement_not_identification", "not automatically a successful test", "end")],
        "10": [("no_range", "no pass-or-fail range", "end"), ("no_signature", "without a unique signature", "end"), ("trustworthy_measurement", "trustworthy measurement", "end"), ("closing_line", "The hunt had a source", "start")],
        "11": [("target_gate", "a published calculation", "start"), ("signature_gate", "a fingerprint only a black-hole birth would leave", "start"), ("asymmetry_alone", "A confirmed spin asymmetry alone", "start"), ("reopen", "This route reopens only", "start")],
    }
    return [witness(*row) for row in definitions[card_id]]


def main() -> int:
    for name, expected in EXPECTED.items():
        if sha(SOURCE / name) != expected:
            raise RuntimeError(f"V12 source drift: {name}")
    v11_timeline_path = V11_ROOT / "audio" / "timeline.json"
    if sha(v11_timeline_path) != V11_TIMELINE_SHA:
        raise RuntimeError("V11 custodied audio timeline drift")
    story = json.loads(STORY.read_text())
    v11_timeline = json.loads(v11_timeline_path.read_text())
    v11_cards = {card["card_id"]: card for card in v11_timeline["cards"]}
    narration_document = NARRATION.read_text()
    if story["estimated_duration_seconds"] != 402:
        raise RuntimeError("V12 runtime contract drift")
    if [float(x) for x in story["render_contract"]["allowed_wpm_band"]] != list(WPM_BAND):
        raise RuntimeError("WPM band drift")

    CARD_DIR.mkdir(parents=True, exist_ok=True)
    timeline_cards = []
    all_fragments = []
    source_sentence_cues = []
    master_start = 0.0
    for card in story["cards"]:
        card_id = card["id"]
        narration = card["narration"]
        if narration_document.count(narration) != 1:
            raise RuntimeError(f"Card {card_id} narration not unique in V12 narration authority")
        old = v11_cards[card_id]
        if old["narration"] != narration:
            raise RuntimeError(f"Card {card_id} narration differs from custodied raw input")
        raw = V11_ROOT / old["raw_audio"]
        boundary = raw.with_name(raw.stem + "-boundaries.json")
        if not raw.exists() or not boundary.exists():
            raise RuntimeError(f"custodied raw input missing Card {card_id}")
        raw_tokens = flatten_events(narration, json.loads(boundary.read_text()))
        raw_start = raw_tokens[0]["raw_start_seconds"]
        raw_end = raw_tokens[-1]["raw_end_seconds"]
        raw_span = raw_end - raw_start
        count = word_count(narration)
        target_span = count * 60 / TARGET_WPM
        atempo = raw_span / target_span
        crop_start = max(0.0, raw_start - LEAD_SECONDS)
        crop_end = raw_end + TAIL_SECONDS
        planned = float(card["planned_seconds"])
        delivered = CARD_DIR / f"card-{card_id}.wav"
        chain = (
            f"atrim=start={crop_start:.9f}:end={crop_end:.9f},asetpts=PTS-STARTPTS,"
            f"atempo={atempo:.9f},aresample={SAMPLE_RATE},aformat=sample_fmts=s16:channel_layouts=mono,"
            f"apad=whole_dur={planned:.9f},atrim=duration={planned:.9f}"
        )
        run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw), "-af", chain, "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", "pcm_s16le", str(delivered))
        if abs(duration(delivered) - planned) > 0.002:
            raise RuntimeError(f"Card {card_id} duration drift")
        transformed = [
            {
                "index": index,
                "token": item["token"],
                "card_start_seconds": max(0.0, (item["raw_start_seconds"] - crop_start) / atempo),
                "card_end_seconds": max(0.0, (item["raw_end_seconds"] - crop_start) / atempo),
            }
            for index, item in enumerate(raw_tokens)
        ]
        speech_start = transformed[0]["card_start_seconds"]
        speech_end = transformed[-1]["card_end_seconds"]
        speech_span = speech_end - speech_start
        delivered_wpm = count * 60 / speech_span
        if not WPM_BAND[0] <= delivered_wpm <= WPM_BAND[1] or abs(delivered_wpm - TARGET_WPM) > 0.02:
            raise RuntimeError(f"Card {card_id} WPM drift: {delivered_wpm}")
        if speech_end > planned:
            raise RuntimeError(f"Card {card_id} speech overrun")

        fragments = []
        cursor = 0
        for cue_index, payload in enumerate(cue_fragments(card_id, narration), 1):
            first, last = locate(transformed, payload, cursor)
            cursor = last + 1
            cue = {
                "id": f"c{card_id}-{cue_index:02d}", "card_id": card_id, "text": payload,
                "card_start_seconds": transformed[first]["card_start_seconds"],
                "card_end_seconds": transformed[last]["card_end_seconds"],
                "master_start_seconds": master_start + transformed[first]["card_start_seconds"],
                "master_end_seconds": master_start + transformed[last]["card_end_seconds"],
                "first_token_index": first, "last_token_index": last,
            }
            fragments.append(cue)
            all_fragments.append(cue)
        if cursor != len(transformed) or tokens(" ".join(x["text"] for x in fragments)) != tokens(narration):
            raise RuntimeError(f"Card {card_id} fragment consumption failed")

        fragment_cursor = 0
        for sentence in split_sentences(narration):
            wanted = tokens(sentence)
            accumulated = []
            first_fragment = fragment_cursor
            while fragment_cursor < len(fragments) and len(accumulated) < len(wanted):
                accumulated += tokens(fragments[fragment_cursor]["text"])
                fragment_cursor += 1
            if accumulated != wanted:
                raise RuntimeError(f"Card {card_id} source sentence mapping failed")
            selected = fragments[first_fragment:fragment_cursor]
            source_sentence_cues.append({
                "card_id": card_id,
                "text": sentence,
                "master_start_seconds": selected[0]["master_start_seconds"],
                "master_end_seconds": selected[-1]["master_end_seconds"],
                "source_fragment_ids": [item["id"] for item in selected],
            })
        if fragment_cursor != len(fragments):
            raise RuntimeError(f"Card {card_id} leftover fragments")

        reveals = make_reveals(card_id, transformed, master_start)
        timeline_cards.append({
            "card_id": card_id, "narration": narration, "text_sha256": hashlib.sha256(narration.encode()).hexdigest(),
            "planned_seconds": planned, "master_start_seconds": master_start, "master_end_seconds": master_start + planned,
            "raw_audio": str(raw), "raw_audio_sha256": sha(raw), "raw_boundaries": str(boundary), "raw_boundaries_sha256": sha(boundary),
            "delivered_audio": str(delivered.relative_to(ROOT)), "delivered_audio_sha256": sha(delivered),
            "spoken_compound_count": count, "target_wpm": TARGET_WPM, "atempo_factor": atempo,
            "speech_start_seconds": speech_start, "speech_end_seconds": speech_end, "speech_span_seconds": speech_span,
            "delivered_wpm": delivered_wpm, "dwell_after_speech_seconds": planned - speech_end,
            "tokens": transformed, "caption_fragments": fragments, "reveals": reveals,
        })
        master_start += planned
        print(f"Card {card_id}: {count} words / {speech_span:.3f}s = {delivered_wpm:.2f} WPM; dwell {planned - speech_end:.3f}s")

    if abs(master_start - 402) > 0.001:
        raise RuntimeError(f"master timeline drift: {master_start}")
    with wave.open(str(MASTER), "wb") as output:
        output.setnchannels(1); output.setsampwidth(2); output.setframerate(SAMPLE_RATE)
        for card in timeline_cards:
            with wave.open(str(ROOT / card["delivered_audio"]), "rb") as source:
                if (source.getnchannels(), source.getsampwidth(), source.getframerate()) != (1, 2, SAMPLE_RATE):
                    raise RuntimeError("card WAV format drift")
                output.writeframes(source.readframes(source.getnframes()))
    if abs(duration(MASTER) - 402) > 0.002:
        raise RuntimeError("master duration drift")
    if len(source_sentence_cues) != 64:
        raise RuntimeError(f"expected 64 source sentence cues, got {len(source_sentence_cues)}")
    if any(round(a["master_end_seconds"] * 1000) > round(b["master_start_seconds"] * 1000) for a, b in zip(source_sentence_cues, source_sentence_cues[1:])):
        raise RuntimeError("source sentence cues overlap")
    SRT.write_text(render_sidecar(source_sentence_cues, False))
    VTT.write_text(render_sidecar(source_sentence_cues, True))
    timeline = {
        "status": "PASS_EXACT_V12_AUDIO_BUILT_AT_142_WPM_WITH_64_SOURCE_SENTENCE_CAPTIONS",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_hashes": EXPECTED,
        "base_raw_audio_timeline_sha256": V11_TIMELINE_SHA,
        "provider": "Microsoft Edge TTS raw inputs already synthesized and custodied in V11; deterministic local retiming only",
        "new_tts_requests": 0, "paid_generation": False, "voice": v11_timeline["voice"],
        "target_wpm": TARGET_WPM, "allowed_wpm_band": list(WPM_BAND), "sample_rate": SAMPLE_RATE, "music": False,
        "master_audio": str(MASTER.relative_to(ROOT)), "master_audio_sha256": sha(MASTER), "master_duration_seconds": duration(MASTER),
        "srt": str(SRT.relative_to(ROOT)), "srt_sha256": sha(SRT), "vtt": str(VTT.relative_to(ROOT)), "vtt_sha256": sha(VTT),
        "source_sentence_cue_count": len(source_sentence_cues), "source_sentence_cues": source_sentence_cues,
        "cards": timeline_cards,
    }
    TIMELINE.write_text(json.dumps(timeline, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": timeline["status"], "timeline": str(TIMELINE), "timeline_sha256": sha(TIMELINE), "master_sha256": sha(MASTER), "srt_sha256": sha(SRT), "vtt_sha256": sha(VTT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
