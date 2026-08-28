#!/usr/bin/env python3
"""Instrument all V13 text-drawing calls against Lana's closed-world keep lists."""
from __future__ import annotations

import importlib.util
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
RENDERER_PATH = ROOT / "render_v13.py"
OUTPUT = ROOT / "V13_RENDERED_TEXT_PROJECTION_AUDIT.json"


def load_renderer():
    spec = importlib.util.spec_from_file_location("render_v13_for_text_audit", RENDERER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load V13 renderer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    renderer_module = load_renderer()
    renderer = renderer_module.Renderer()
    contract = json.loads(renderer_module.TEXT_CONTRACT_PATH.read_text())
    current_card = [""]
    current_counter: Counter[str] = Counter()
    union_by_card = {f"{index:02d}": set() for index in range(1, 12)}
    max_counts_by_card = {f"{index:02d}": Counter() for index in range(1, 12)}

    def record(_draw, value, *args, **kwargs):
        current_counter[str(value)] += 1

    setattr(renderer_module, "center", record)
    setattr(renderer_module, "wrap", record)
    setattr(renderer_module, "text_plate", record)

    for card in renderer.cards:
        card_id = card["card_id"]
        current_card[0] = card_id
        times = renderer_module.reveal_map(card)
        duration = float(card["planned_seconds"])
        samples = {0.0, max(0.0, duration - 0.001)}
        for value in times.values():
            samples |= {max(0.0, value - 0.001), value, min(duration - 0.001, value + 0.25)}
        for timestamp in sorted(samples):
            current_counter.clear()
            image = Image.new("RGB", (renderer_module.W, renderer_module.H), renderer_module.BG)
            draw = ImageDraw.Draw(image)
            renderer_module.DRAWERS[card_id](image, draw, timestamp, times, False)
            union_by_card[card_id].update(current_counter)
            for text, count in current_counter.items():
                max_counts_by_card[card_id][text] = max(max_counts_by_card[card_id][text], count)

    card_rows = {}
    passed = True
    for card_id, card_contract in contract["cards"].items():
        expected_counts = Counter()
        for row in card_contract["permitted"]:
            expected_counts[row["text"]] = max(expected_counts[row["text"]], int(row.get("repeat", 1)))
        actual_union = union_by_card[card_id]
        actual_counts = max_counts_by_card[card_id]
        unexpected = sorted(actual_union - set(expected_counts))
        missing = sorted(set(expected_counts) - actual_union)
        repetition_mismatches = {
            text: {"expected_max_simultaneous": expected, "actual_max_simultaneous": actual_counts.get(text, 0)}
            for text, expected in expected_counts.items()
            if actual_counts.get(text, 0) != expected
        }
        card_pass = not unexpected and not missing and not repetition_mismatches
        passed = passed and card_pass
        card_rows[card_id] = {
            "status": "PASS" if card_pass else "FAIL",
            "actual_union": sorted(actual_union),
            "expected_union": sorted(expected_counts),
            "actual_max_simultaneous_counts": dict(sorted(actual_counts.items())),
            "expected_max_simultaneous_counts": dict(sorted(expected_counts.items())),
            "unexpected": unexpected,
            "missing": missing,
            "repetition_mismatches": repetition_mismatches,
        }
    result = {
        "status": "PASS_EXACT_CLOSED_WORLD_RENDERED_TEXT_PROJECTION" if passed else "HOLD_RENDERED_TEXT_PROJECTION",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "renderer": str(RENDERER_PATH),
        "renderer_sha256": renderer_module.sha(RENDERER_PATH),
        "text_contract": str(renderer_module.TEXT_CONTRACT_PATH),
        "text_contract_sha256": renderer_module.sha(renderer_module.TEXT_CONTRACT_PATH),
        "method": "Instrument center/wrap/text_plate calls at frame zero, immediately before/at/after every reveal witness, and final card state; compare string union and maximum simultaneous repetitions to each exhaustive keep list.",
        "cards": card_rows,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": result["status"], "output": str(OUTPUT), "output_sha256": renderer_module.sha(OUTPUT)}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
