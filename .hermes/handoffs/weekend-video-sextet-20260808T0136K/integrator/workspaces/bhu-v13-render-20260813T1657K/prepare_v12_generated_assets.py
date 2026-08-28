#!/usr/bin/env python3
"""Prepare only audited-safe generated regions and freeze the V12 generation-spend ledger."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "generated_assets"
PREPARED = ROOT / "assets" / "generated_prepared"
LEDGER = ROOT / "V12_GENERATION_SPEND_LEDGER.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


CALLS = [
    {
        "id": "g01", "purpose": "Card 01 book/roads/gate world, first attempt",
        "file": "card01-road-gate-raw.png", "url": "https://v3b.fal.media/files/b/0aa625d9/PaJQvfYW4TjK3B0Rwn2ng_R8py5njU.png",
        "prompt": "Stylized painterly open book, two diverging roads, checkable star, galaxy fog, intact gate; no people, facilities, observation-like imagery, charts, axes, scales, numbers, letters, words, labels, logos, or watermark.",
        "disposition": "REJECTED_FULL_FRAME", "reason": "Safe illustration boundary, but the book did not visibly produce two roads; blur-test claim failed.",
    },
    {
        "id": "g02", "purpose": "Card 02 five-proposal icon sheet, first attempt",
        "file": "card02-five-ideas-raw.png", "url": "https://v3b.fal.media/files/b/0aa625d9/3VT4y4tuWYU1rQMvNPQ04_U4ei785X.png",
        "prompt": "Five isolated painterly metaphors: nested universe, collapse bounce, handed-down spin, universe family tree, unlike fingerprints; no text, data, facilities, observations, or quantitative geometry.",
        "disposition": "PARTIAL_ACCEPT_CROPS_ONLY", "reason": "Nested universe, family tree, and fingerprint regions passed; bounce resembled a meteor and single top failed inheritance.",
    },
    {
        "id": "g03", "purpose": "Card 03 dartboard/orb prop tableau",
        "file": "card03-dartboard-raw.png", "url": "https://v3b.fal.media/files/b/0aa625d9/faV4286NJvPMOVTv2SkqK_BBdZG5YU.png",
        "prompt": "Painterly dartboard, darts, two glowing orbs with negative space; no humans, text, numbers, labels, charts, scales, data, facilities, or observations.",
        "disposition": "REJECTED_FULL_FRAME", "reason": "Model invented a visible M on the dartboard. V12 dartboard and orbs are rebuilt locally.",
    },
    {
        "id": "g04", "purpose": "Card 01 book/two-road/gate world, replacement",
        "file": "card01-road-gate-r2-raw.png", "url": "https://v3b.fal.media/files/b/0aa625e1/bE-bez_gGUZHU4UlnRyfX_asv7K1oM.png",
        "prompt": "Open book as common origin of exactly two Y-forking roads: open star road and galaxy-fog road spanned by intact gate; no people, facilities, observations, charts, numbers, letters, text, labels, or watermark.",
        "disposition": "RETAINED_NOT_USED_IN_FINAL", "reason": "The still passed the static boundary, but its already-closed gate conflicted with verdict-time reveal chronology. A local mask produced visible blobs, so the final Card 01 is entirely local deterministic art.",
    },
    {
        "id": "g05", "purpose": "Card 02 bounce and inherited-spin replacement props",
        "file": "card02-bounce-spin-r2-raw.png", "url": "https://v3b.fal.media/files/b/0aa625e1/cxrH936FOedOjofkx1d5t_QqISe48G.png",
        "prompt": "Two isolated painterly icons: squash-and-rebound ball; parent and child spinning tops; no humans, text, numbers, data, facilities, observations, or charts.",
        "disposition": "PARTIAL_ACCEPT_CROPS_ONLY", "reason": "Bounce and both top props passed. Painted handoff arrow is excluded; handoff motion is drawn locally.",
    },
    {
        "id": "g06", "purpose": "Card 06 fork-road atmosphere",
        "file": "card06-fork-raw.png", "url": "https://v3b.fal.media/files/b/0aa62636/UcmvhGBTIV_SIK9meQoxQ_3G9YUrmP.png",
        "prompt": "Illustrative fork road, blank signpost, stopped abstract marker; no person, text, numbers, data, axes, facilities, observations, or watermark.",
        "disposition": "PARTIAL_ACCEPT_BACKGROUND_ONLY", "reason": "Road fork and atmosphere passed. Generated rectangular sign is covered; local two-arm sign and quotations carry semantics.",
    },
    {
        "id": "g07", "purpose": "Cards 07/08 galaxy and empty-prop sheet",
        "file": "card07-08-props-raw.png", "url": "https://v3b.fal.media/files/b/0aa62648/SzyWaMKQjebIy9pz-ZmKl_H4V9cBca.png",
        "prompt": "Six stylized galaxy icons and blank ruler/map/needleless compass/needleless meter props; no text, numbers, marks, observations, or facilities.",
        "disposition": "PARTIAL_ACCEPT_GALAXIES_ONLY", "reason": "Six galaxy icons passed. Ruler ticks, compass letters/needle, meter ticks/needle and PASS text violated prompt and are excluded.",
    },
    {
        "id": "g08", "purpose": "Card 09 footprint and three possible makers",
        "file": "card09-footprint-raw.png", "url": "https://v3b.fal.media/files/b/0aa62636/_Ljt0QU1WKqTi3Ox-AN6L_bOWBCEha.png",
        "prompt": "One footprint with exactly three different unlabeled fictional animal silhouettes; no text, numbers, charts, facilities, observations, or watermark.",
        "disposition": "ACCEPTED_WHOLE", "reason": "Exactly one trace and three visibly distinct possible makers; sound-off underdetermination reads without text.",
    },
    {
        "id": "g09", "purpose": "Card 11 keys and unequal-stack token",
        "file": "card11-keys-raw.png", "url": "https://v3b.fal.media/files/b/0aa62636/vZcyF0YO4Eo7qRLluQPCD_r9fiR6EV.png",
        "prompt": "Ruler-range key without ticks, fingerprint key, unequal galaxy-stack token; no text, numbers, scales, data, facilities, observations, or watermark.",
        "disposition": "REJECTED_FULL_FRAME", "reason": "Ruler received generated ticks and was not a key; stack did not encode the intended unequal callback. Card 11 is local deterministic art.",
    },
    {
        "id": "g10", "purpose": "Card 08 timeline and empty-slot props",
        "file": "card08-timeline-props-raw.png", "url": "https://v3b.fal.media/files/b/0aa62649/7YOs4UrvwXDhjpb8v6DIM_hRpaAWny.png",
        "prompt": "Blank photo-frame icons, later paper/speech bubble, four empty props; no text, numbers, ticks, needles, facilities, observations, or watermark.",
        "disposition": "PARTIAL_ACCEPT_TOP_PROPS_ONLY", "reason": "Blank photo icons and speech bubble passed. Bottom ruler/map/compass/meter contain marks, needles, letters, PASS, and Local Year text; all excluded.",
    },
]

CROPS = [
    ("card01_final.png", "card01-road-gate-r2-raw.png", (0, 0, 1024, 576)),
    ("card02_nested.png", "card02-five-ideas-raw.png", (35, 20, 350, 300)),
    ("card02_family.png", "card02-five-ideas-raw.png", (25, 260, 395, 576)),
    ("card02_fingerprints.png", "card02-five-ideas-raw.png", (500, 270, 1024, 576)),
    ("card02_bounce.png", "card02-bounce-spin-r2-raw.png", (0, 35, 500, 560)),
    ("card02_parent_top.png", "card02-bounce-spin-r2-raw.png", (520, 140, 810, 480)),
    ("card02_child_top.png", "card02-bounce-spin-r2-raw.png", (800, 215, 1024, 465)),
    ("card06_fork_background.png", "card06-fork-raw.png", (0, 0, 1024, 576)),
    ("card07_galaxies.png", "card07-08-props-raw.png", (0, 0, 520, 576)),
    ("card08_photos.png", "card08-timeline-props-raw.png", (0, 0, 520, 325)),
    ("card08_bubble.png", "card08-timeline-props-raw.png", (520, 0, 1024, 325)),
    ("card09_final.png", "card09-footprint-raw.png", (0, 0, 1024, 576)),
]


def main() -> int:
    PREPARED.mkdir(parents=True, exist_ok=True)
    raw_rows = []
    for call in CALLS:
        path = RAW / call["file"]
        if not path.exists():
            raise RuntimeError(f"missing generated raw asset {path}")
        with Image.open(path) as image:
            size = list(image.size)
        raw_rows.append({**call, "path": str(path), "sha256": sha(path), "bytes": path.stat().st_size, "pixel_size": size})
    prepared_rows = []
    for output_name, input_name, box in CROPS:
        input_path = RAW / input_name
        output_path = PREPARED / output_name
        with Image.open(input_path) as image:
            crop = image.crop(box).convert("RGB")
            crop.save(output_path, optimize=True)
        prepared_rows.append({
            "path": str(output_path), "sha256": sha(output_path), "bytes": output_path.stat().st_size,
            "source_raw": input_name, "source_raw_sha256": sha(input_path), "crop_box": list(box), "pixel_size": list(crop.size),
            "semantic_motion_or_text_authority": False,
        })
    ledger = {
        "status": "V12_GENERATION_CLOSED_TEN_STILL_CALLS_AUDITED_FAIL_CLOSED",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "provider_route": "Nous-managed image_generate; active model reported by tool surface as FLUX 2 Klein 9B",
        "generation_call_count": len(CALLS),
        "generated_video_call_count": 0,
        "monetary_cost": {"amount": None, "currency": None, "status": "NOT_REPORTED_BY_TOOL_DO_NOT_INVENT"},
        "new_calls_permitted_after_ledger": False,
        "boundary": {
            "generated_quantitative_pixels": False,
            "generated_on_screen_text": False,
            "real_people_or_facilities": False,
            "observation_or_survey_like_images": False,
            "all_semantic_motion_local": True,
            "cards_04_05_generated_pixels": False,
        },
        "calls": raw_rows,
        "prepared_assets": prepared_rows,
        "excluded_raw_files_retained_for_audit": True,
    }
    LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": ledger["status"], "calls": len(CALLS), "prepared": len(prepared_rows), "ledger": str(LEDGER), "ledger_sha256": sha(LEDGER)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
