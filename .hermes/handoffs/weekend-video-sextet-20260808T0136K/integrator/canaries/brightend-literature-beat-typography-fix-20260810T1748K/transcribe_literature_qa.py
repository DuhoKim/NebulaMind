#!/usr/bin/env python3
"""Transcribe freshly synthesized literature sentences and fail closed on semantic drift."""
from __future__ import annotations

import difflib
import json
import re
import sys
from pathlib import Path

HERMES_SOURCE = Path("/Users/duhokim/.hermes/hermes-agent")
if str(HERMES_SOURCE) not in sys.path:
    sys.path.insert(0, str(HERMES_SOURCE))
from tools.managed_tool_gateway import resolve_managed_tool_gateway  # noqa: E402
from openai import OpenAI  # noqa: E402

ROOT = Path(__file__).resolve().parent


def normalize(text: str) -> str:
    text = text.lower()
    replacements = {
        "(y-int)": "y intercept", "y-int": "y intercept", "y int": "y intercept",
        "0.7": "zero point seven", "∼": " approximately ", "~": " approximately ",
        "λcdm": "lambda c d m", "lambda-cdm": "lambda c d m", "lambda cdm": "lambda c d m",
        "7-10": "seven to ten", "7–10": "seven to ten", "7−10": "seven to ten", "7 to 10": "seven to ten",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", text).split())


def main() -> int:
    spec = json.loads((ROOT / "spec.json").read_text())
    synthesis = json.loads((ROOT / "audio/synthesis_receipt.json").read_text())
    by_id = {record["id"]: record for record in synthesis["records"]}
    ids = [record["id"] for record in spec["sentences"] if record["section"] == "literature"]
    gateway = resolve_managed_tool_gateway("openai-audio")
    if gateway is None:
        raise RuntimeError("managed audio gateway unavailable; no fallback authorized")
    client = OpenAI(api_key=gateway.nous_user_token, base_url=gateway.gateway_origin.rstrip("/") + "/v1")
    results = []
    for sentence_id in ids:
        record = by_id[sentence_id]
        path = ROOT / record["file"]
        with path.open("rb") as stream:
            transcript = client.audio.transcriptions.create(model="whisper-1", file=stream).text.strip()
        expected_norm = normalize(record["text"])
        actual_norm = normalize(transcript)
        similarity = difflib.SequenceMatcher(None, expected_norm, actual_norm).ratio()
        semantic = True
        if sentence_id == "i05q":
            semantic = "zero point seven dex" in actual_norm and "calibration" in actual_norm
        if sentence_id == "i05b":
            semantic = all(token in actual_norm for token in ("approximately seven to ten", "unresolved", "properties", "observations", "lambda c d m"))
        threshold = 0.86 if sentence_id in {"i05q", "i05b"} else 0.90
        status = "PASS" if similarity >= threshold and semantic else "HOLD"
        results.append({"id": sentence_id, "expected": record["text"], "transcript": transcript, "normalized_expected": expected_norm, "normalized_transcript": actual_norm, "similarity": similarity, "threshold": threshold, "semantic_guard": semantic, "status": status})
        print(sentence_id, status, f"{similarity:.4f}", transcript)
    report = {"status": "PASS" if all(r["status"] == "PASS" for r in results) else "HOLD", "provider_route": "Hermes managed OpenAI audio gateway", "model": "whisper-1", "records": results}
    path = ROOT / "audio/literature_asr.json"
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(path)
    if report["status"] != "PASS":
        raise RuntimeError("literature ASR HOLD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
