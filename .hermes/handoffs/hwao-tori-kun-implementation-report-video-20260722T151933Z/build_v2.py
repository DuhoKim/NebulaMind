#!/usr/bin/env python3
"""Build the evidence-bounded Hwao + Tori + Kun implementation report video V2."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import importlib.util
import json
import sys

V1_BUILDER = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "kun-tori-progress-video-20260722T105357Z/build.py"
)
BASE = Path(__file__).resolve().parent

spec = importlib.util.spec_from_file_location("kun_tori_video_v1", V1_BUILDER)
if spec is None or spec.loader is None:
    raise RuntimeError(f"unable to import validated V1 renderer: {V1_BUILDER}")
v1: Any = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = v1
spec.loader.exec_module(v1)

TMP = BASE / "build"
SCENES_DIR = TMP / "scenes"
AUDIO_DIR = TMP / "audio"
RAW_AUDIO_DIR = AUDIO_DIR / "raw"
for directory in (TMP, SCENES_DIR, AUDIO_DIR, RAW_AUDIO_DIR):
    directory.mkdir(parents=True, exist_ok=True)

v1.BASE = BASE
v1.TMP = TMP
v1.SCENES_DIR = SCENES_DIR
v1.AUDIO_DIR = AUDIO_DIR
v1.RAW_AUDIO_DIR = RAW_AUDIO_DIR
v1.FREEZE = BASE / "source_freeze.json"
v1.FINAL = BASE / "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_V2.mp4"
v1.SRT = BASE / "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_V2.srt"
v1.NARRATION_WAV = BASE / "hwao_tori_kun_implementation_female_narration.wav"
v1.CONTACT_SHEET = BASE / "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_SCENE_SHEET.png"
v1.BUILD_RECEIPT = BASE / "build_receipt.json"

Scene = v1.Scene
SCENES = (
    Scene(0, "open", 3.0, "", ()),
    Scene(
        1,
        "hwao",
        13.0,
        "Hwao turned Kun's oversight into a preservation-first implementation plan. Completed evidence stayed intact, and each new action remained separately gated. That decision prevented a valid Claim Ledger contract from being rebuilt or silently overwritten.",
        (
            "Hwao turned Kun's oversight into a preservation-first implementation plan.",
            "Completed evidence stayed intact, and each new action remained separately gated.",
            "A valid Claim Ledger contract was not rebuilt or silently overwritten.",
        ),
    ),
    Scene(
        2,
        "tori",
        15.0,
        "Tori tracked custody through the Surveys rework. Three fail-closed reviews recorded two failures before an unconditional pass across all ten acceptance items. Hwao closed the unit verified-PASS. The seven-file V2 remains frozen and uncommitted; landing it still needs separate approval.",
        (
            "Tori tracked custody through the Surveys rework.",
            "Three fail-closed reviews recorded two failures before an unconditional pass across all 10 acceptance items.",
            "Hwao closed the unit verified-PASS.",
            "The seven-file V2 remains frozen and uncommitted; landing still needs separate approval.",
        ),
    ),
    Scene(
        3,
        "execution",
        18.0,
        "With explicit authorization, guarded deletion executed: eighteen quarantined debris files, eighteen regenerable test databases, and two primary pytest caches were removed. Eight protected caches and the secret-adjacent environment file stayed retained. No tracked file changed; the regeneration check passed four tests.",
        (
            "With explicit authorization, guarded deletion executed.",
            "18 quarantined debris files, 18 regenerable test databases, and 2 primary pytest caches were removed.",
            "Eight protected caches and the secret-adjacent environment file were retained.",
            "No tracked file changed; the regeneration check passed four tests.",
        ),
    ),
    Scene(
        4,
        "map",
        16.0,
        "Kun's docs-only implementation also built status and debate map version one from the frozen sixteen-entry claim ledger. Four axes preserve twenty-eight counterevidence items and four epistemic caps. The validator resolved every entry and returned PASS, with no database, Git, runtime, or publication action.",
        (
            "Kun's docs-only implementation built status and debate map version one from the frozen 16-entry claim ledger.",
            "Four axes preserve 28 counterevidence items and four epistemic caps.",
            "The validator resolved every entry and returned PASS.",
            "No database, Git, runtime, or publication action occurred.",
        ),
    ),
    Scene(
        5,
        "artifact",
        17.0,
        "Hwao reviewed the implementation boundary and created a private, captioned capture of the rendered four-axis map: mechanism, prevalence, dominance debate, and simulation support. Manual sharing is still pending. The artifact reports the implementation; it does not prove that map wiring is live in the product.",
        (
            "Hwao created a private, captioned capture of the rendered four-axis map.",
            "Mechanism, prevalence, dominance debate, and simulation support are visible.",
            "Manual sharing is still pending.",
            "The artifact reports implementation; it does not prove live product wiring.",
        ),
    ),
    Scene(
        6,
        "boundary",
        15.0,
        "This is real implementation progress, not a full release. Surveys landing, map wiring, reader-facing prose, database changes, runtime deployment, and public publication remain separate gates. The verified outputs are preserved; no additional action is implied by this report video.",
        (
            "This is real implementation progress, not a full release.",
            "Surveys landing, map wiring, reader-facing prose, database changes, runtime deployment, and public publication remain separate gates.",
            "No additional action is implied by this report video.",
        ),
    ),
    Scene(7, "close", 3.0, "", ()),
)
v1.SCENES = SCENES


def centered(draw, box, text, text_font, fill):
    x0, y0, x1, y1 = box
    bounds = draw.textbbox((0, 0), text, font=text_font)
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    draw.text(((x0 + x1 - width) / 2, (y0 + y1 - height) / 2 - bounds[1]), text, font=text_font, fill=fill)


def caption_panel(draw, text):
    if not text:
        return
    v1.panel(draw, (52, 604, 1228, 704), outline="#29466E", fill="#07101F", width=1, radius=18)
    draw.text((75, 621), "NARRATION", font=v1.font(13), fill=v1.CYAN)
    caption_font = v1.font(14)
    lines = v1.wrap_text(draw, text, caption_font, 1040)
    if len(lines) > 3:
        raise RuntimeError(f"burned-in narration exceeds three lines at 14pt: {text}")
    y = 620
    for line in lines:
        draw.text((170, y), line, font=caption_font, fill=v1.BODY)
        y += 24


v1.caption_panel = caption_panel


def scene_open(scene):
    image = v1.gradient_background(scene.index)
    v1.paste_portrait(image, (755, 64, 1195, 650))
    draw = v1.ImageDraw.Draw(image)
    draw.text((64, 42), "NebulaMind", font=v1.font(23), fill=v1.BODY)
    draw.text((64, 148), "IMPLEMENTATION REPORT", font=v1.font(18), fill=v1.CYAN)
    draw.text((64, 200), "Hwao · Tori · Kun", font=v1.font(46), fill=v1.BODY)
    draw.text((64, 262), "Verified progress · retained gates", font=v1.font(24), fill=v1.WARNING)
    draw.line((64, 325, 650, 325), fill=v1.CYAN, width=3)
    draw.text((64, 365), "22 July 2026 · V2 local review", font=v1.font(18), fill=v1.MUTED)
    v1.panel(draw, (64, 485, 650, 570), outline=v1.SUCCESS, fill="#0D2730", width=2, radius=17)
    draw.text((90, 507), "STATUS FREEZE", font=v1.font(14), fill=v1.SUCCESS)
    draw.text((90, 540), "execution receipts + map validation locked", font=v1.font(15), fill=v1.BODY)
    return image


def scene_hwao(scene):
    image = v1.gradient_background(scene.index)
    draw = v1.ImageDraw.Draw(image)
    v1.header(draw, scene, "Hwao coordination", "Preserve verified truth before new execution")
    cards = (
        (64, "KUN OVERSIGHT", "HEALTHY WITH RISKS", v1.WARNING),
        (448, "HWAO RULING", "PRESERVE + RECONCILE", v1.CYAN),
        (832, "ACTION MODEL", "SEPARATE GATES", v1.SUCCESS),
    )
    for x, kicker, value, accent in cards:
        v1.panel(draw, (x, 195, x + 340, 355), outline=accent)
        draw.text((x + 22, 220), kicker, font=v1.font(14), fill=accent)
        draw.text((x + 22, 272), value, font=v1.font(19), fill=v1.BODY)
    draw.line((235, 405, 1025, 405), fill="#29466E", width=3)
    steps = ((235, "VALID CONTRACT", v1.SUCCESS), (630, "NO REBUILD", v1.CYAN), (1025, "NO SILENT OVERWRITE", v1.WARNING))
    for x, label, accent in steps:
        draw.ellipse((x - 30, 430, x + 30, 490), fill=v1.rgba(v1.PANEL_2), outline=accent, width=3)
        centered(draw, (x - 30, 430, x + 30, 490), "✓", v1.font(22), accent)
        centered(draw, (x - 160, 505, x + 160, 548), label, v1.font(14), v1.MUTED)
    v1.caption_panel(draw, scene.narration)
    return image


def scene_tori(scene):
    return v1.scene_tori(scene)


def scene_execution(scene):
    image = v1.gradient_background(scene.index)
    draw = v1.ImageDraw.Draw(image)
    v1.header(draw, scene, "Authorized execution", "Guarded deletion completed without widening scope")
    metrics = (
        ("18", "quarantined debris", v1.MAGENTA),
        ("18", "regenerable test DBs", v1.CYAN),
        ("2", "primary pytest caches", v1.WARNING),
        ("0", "tracked deletions", v1.SUCCESS),
    )
    for i, (value, label, accent) in enumerate(metrics):
        x0 = 64 + i * 288
        v1.panel(draw, (x0, 190, x0 + 260, 310), outline=accent)
        draw.text((x0 + 18, 208), value, font=v1.font(32), fill=v1.BODY)
        draw.text((x0 + 18, 264), label, font=v1.font(13), fill=accent)
    v1.panel(draw, (64, 345, 760, 570), outline=v1.SUCCESS, fill="#0D2730")
    draw.text((90, 370), "RETAINED BY RULE", font=v1.font(17), fill=v1.SUCCESS)
    retained = ("8 protected/worktree caches", "secret-adjacent environment file", "tracked source and HEAD")
    for i, item in enumerate(retained):
        draw.text((90, 420 + i * 42), f"✓  {item}", font=v1.font(16), fill=v1.BODY)
    v1.panel(draw, (800, 345, 1216, 570), outline=v1.CYAN, fill="#0E2135")
    draw.text((826, 370), "REGENERATION CHECK", font=v1.font(16), fill=v1.CYAN)
    draw.text((826, 425), "4 PASSED", font=v1.font(40), fill=v1.SUCCESS)
    draw.text((826, 493), "test fixture recreated cleanly", font=v1.font(14), fill=v1.MUTED)
    v1.caption_panel(draw, scene.narration)
    return image


def scene_map(scene):
    image = v1.gradient_background(scene.index)
    draw = v1.ImageDraw.Draw(image)
    v1.header(draw, scene, "Kun docs-only implementation", "Four-axis status / debate map — validator PASS")
    axes = (
        ("MECHANISM", "widely supported", v1.SUCCESS),
        ("PREVALENCE", "sample-limited", v1.CYAN),
        ("DOMINANCE DEBATE", "actively debated", v1.MAGENTA),
        ("SIMULATION SUPPORT", "model-dependent", v1.WARNING),
    )
    for i, (name, status, accent) in enumerate(axes):
        col, row = i % 2, i // 2
        x0 = 64 + col * 576
        y0 = 188 + row * 140
        v1.panel(draw, (x0, y0, x0 + 540, y0 + 112), outline=accent)
        draw.text((x0 + 22, y0 + 18), name, font=v1.font(15), fill=v1.BODY)
        draw.text((x0 + 22, y0 + 64), status, font=v1.font(14), fill=accent)
    v1.panel(draw, (64, 485, 1216, 575), outline=v1.SUCCESS, fill="#0D2730", width=2, radius=17)
    facts = (("16 / 16", "entries"), ("28", "counterevidence"), ("4", "epistemic caps"), ("0", "errors"))
    for i, (value, label) in enumerate(facts):
        x = 100 + i * 285
        draw.text((x, 505), value, font=v1.font(23), fill=v1.SUCCESS)
        draw.text((x, 540), label, font=v1.font(13), fill=v1.MUTED)
    v1.caption_panel(draw, scene.narration)
    return image


def scene_artifact(scene):
    image = v1.gradient_background(scene.index)
    draw = v1.ImageDraw.Draw(image)
    v1.header(draw, scene, "Hwao review layer", "Private map artifact — manual Share still pending")
    v1.panel(draw, (64, 180, 900, 570), outline=v1.CYAN, fill="#0A172A", width=2, radius=22)
    draw.rectangle((64, 180, 900, 225), fill=v1.rgba("#142544"))
    draw.ellipse((86, 195, 98, 207), fill=v1.FAIL)
    draw.ellipse((108, 195, 120, 207), fill=v1.WARNING)
    draw.ellipse((130, 195, 142, 207), fill=v1.SUCCESS)
    draw.text((168, 192), "AGN DEBATE MAP · CAPTIONED CAPTURE", font=v1.font(13), fill=v1.MUTED)
    mini = (
        (94, 255, "MECHANISM", v1.SUCCESS),
        (482, 255, "PREVALENCE", v1.CYAN),
        (94, 385, "DOMINANCE", v1.MAGENTA),
        (482, 385, "SIMULATION", v1.WARNING),
    )
    for x, y, label, accent in mini:
        v1.panel(draw, (x, y, x + 330, y + 95), outline=accent, fill="#101E39", width=2, radius=14)
        draw.text((x + 18, y + 18), label, font=v1.font(14), fill=v1.BODY)
        draw.text((x + 18, y + 58), "claims + counter-evidence", font=v1.font(12), fill=accent)
    v1.panel(draw, (940, 180, 1216, 350), outline=v1.WARNING, fill="#2A2318")
    draw.text((966, 210), "VISIBILITY", font=v1.font(14), fill=v1.WARNING)
    draw.text((966, 258), "PRIVATE", font=v1.font(28), fill=v1.BODY)
    draw.text((966, 306), "Share pending", font=v1.font(14), fill=v1.WARNING)
    v1.panel(draw, (940, 385, 1216, 570), outline=v1.FAIL, fill="#2A1822")
    draw.text((966, 412), "DOES NOT PROVE", font=v1.font(14), fill=v1.FAIL)
    for i, item in enumerate(("product wiring", "runtime release", "public publish")):
        draw.text((966, 457 + i * 31), f"— {item}", font=v1.font(13), fill=v1.BODY)
    v1.caption_panel(draw, scene.narration)
    return image


def scene_boundary(scene):
    image = v1.gradient_background(scene.index)
    draw = v1.ImageDraw.Draw(image)
    v1.header(draw, scene, "Release boundary", "Implementation verified — release gates retained")
    v1.panel(draw, (64, 190, 580, 570), outline=v1.SUCCESS, fill="#0D2730")
    draw.text((92, 218), "VERIFIED OUTPUTS", font=v1.font(17), fill=v1.SUCCESS)
    complete = ("Surveys unit closed", "guarded deletion executed", "map built + PASS", "private report artifact")
    for i, item in enumerate(complete):
        draw.text((92, 275 + i * 55), f"✓  {item}", font=v1.font(16), fill=v1.BODY)
    v1.panel(draw, (620, 190, 1216, 570), outline=v1.WARNING, fill="#2A2318")
    draw.text((648, 218), "SEPARATE FUTURE GATES", font=v1.font(17), fill=v1.WARNING)
    held = ("Surveys landing", "map wiring + reader prose", "database + runtime", "public sharing / publication")
    for i, item in enumerate(held):
        draw.text((648, 275 + i * 55), f"—  {item}", font=v1.font(16), fill=v1.BODY)
    v1.caption_panel(draw, scene.narration)
    return image


def scene_close(scene):
    image = v1.gradient_background(scene.index)
    v1.paste_portrait(image, (70, 68, 510, 654))
    draw = v1.ImageDraw.Draw(image)
    draw.text((600, 155), "IMPLEMENTATION VERIFIED.", font=v1.font(31), fill=v1.SUCCESS)
    draw.text((600, 215), "RELEASE GATES RETAINED.", font=v1.font(31), fill=v1.WARNING)
    draw.line((600, 282, 1180, 282), fill=v1.CYAN, width=3)
    draw.text((600, 335), "HWAO", font=v1.font(15), fill=v1.CYAN)
    draw.text((720, 335), "coordination + boundary", font=v1.font(16), fill=v1.BODY)
    draw.text((600, 390), "TORI", font=v1.font(15), fill=v1.CYAN)
    draw.text((720, 390), "custody + verification", font=v1.font(16), fill=v1.BODY)
    draw.text((600, 445), "KUN", font=v1.font(15), fill=v1.CYAN)
    draw.text((720, 445), "implementation + reproducibility", font=v1.font(16), fill=v1.BODY)
    draw.text((600, 590), "LOCAL REVIEW · NO FURTHER ACTION AUTHORIZED", font=v1.font(13), fill=v1.MUTED)
    return image


v1.SCENE_RENDERERS = {
    "open": scene_open,
    "hwao": scene_hwao,
    "tori": scene_tori,
    "execution": scene_execution,
    "map": scene_map,
    "artifact": scene_artifact,
    "boundary": scene_boundary,
    "close": scene_close,
}


def mux_final(silent_video: Path) -> None:
    v1.verify_source_freeze()
    expected_duration = sum(scene.duration for scene in SCENES)
    audio_filter = (
        f"loudnorm=I=-16:LRA=7:TP=-1.5,apad=pad_dur={expected_duration:.6f},"
        f"atrim=duration={expected_duration:.6f}"
    )
    v1.run([
        "ffmpeg", "-y", "-v", "error",
        "-i", str(silent_video),
        "-i", str(v1.NARRATION_WAV),
        "-map", "0:v:0", "-map", "1:a:0",
        "-af", audio_filter,
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", str(v1.FPS),
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-movflags", "+faststart",
        "-metadata", "title=Hwao Tori Kun implementation report V2",
        "-metadata", "comment=Evidence-bounded local review; no further action authorized",
        "-t", f"{expected_duration:.6f}", str(v1.FINAL),
    ])


def main() -> None:
    v1.verify_source_freeze()
    scene_paths = v1.render_scene_images()
    v1.make_contact_sheet(scene_paths)
    v1.write_srt()
    audio_rows = v1.render_audio()
    scene_videos = v1.render_scene_videos(scene_paths)
    silent = v1.concatenate_video(scene_videos)
    mux_final(silent)
    final_duration = v1.probe_duration(v1.FINAL)
    expected_duration = sum(scene.duration for scene in SCENES)
    if abs(final_duration - expected_duration) > 0.08:
        raise RuntimeError(f"final duration {final_duration} != expected {expected_duration}")
    receipt = {
        "marker": "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_VIDEO_BUILD_COMPLETE_V2",
        "completed_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "supersedes_status_only": str(V1_BUILDER.parent / "KUN_REPORT_TORI_PROGRESS_REVIEW_V1.mp4"),
        "source_freeze_verified_before_build": True,
        "source_freeze_verified_before_final_mux": True,
        "renderer": "Pillow + ffmpeg through validated V1 adapter",
        "new_generative_video_calls": "none",
        "voice": v1.VOICE,
        "voice_gender": "Female",
        "presenter_policy": "approved synthetic Flow astronomer portrait appears only during silent opening/outro; no visible narration or false lip-sync",
        "music": "none",
        "expected_duration": expected_duration,
        "observed_duration": final_duration,
        "artifact": str(v1.FINAL),
        "artifact_sha256": v1.sha256(v1.FINAL),
        "artifact_bytes": v1.FINAL.stat().st_size,
        "srt": str(v1.SRT),
        "srt_sha256": v1.sha256(v1.SRT),
        "narration": str(v1.NARRATION_WAV),
        "narration_sha256": v1.sha256(v1.NARRATION_WAV),
        "contact_sheet": str(v1.CONTACT_SHEET),
        "contact_sheet_sha256": v1.sha256(v1.CONTACT_SHEET),
        "scenes": audio_rows,
        "publication_state": "local review only; not uploaded, shared, or published",
    }
    v1.BUILD_RECEIPT.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(receipt, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
