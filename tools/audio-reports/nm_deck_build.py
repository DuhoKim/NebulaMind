#!/usr/bin/env python3
"""nm_deck_build.py — turn an AUTHORED deck into a rendered deck.

Duho, 2026-08-20: "each Fable, now Opus should make it not you, since they know
better than you." So the speaker writes the deck for their own report; this only
resolves graphic directives into real assets and enforces the honesty rules.

Usage:  nm_deck_build.py <reading.mp3> <authored_deck.json>

Authored slide schema (Tori's podcast DECK format plus a `g` directive):
  {"t": 7.6, "k": "kicker", "h": "headline", "b": ["bullet", ...],
   "g": {"kind": "cutgrid", "n": 12},        # optional real graphic
   "img": "graphics/foo.png", "attr": "credit"}   # or supply your own

Graphic kinds (rendered from REAL data, never decoration):
  {"kind":"cutgrid","n":12}                  grid of real galaxy cutouts
  {"kind":"cutout"}                          one real cutout, enlarged
  {"kind":"progress","done":5300,"total":60308,"label":"bricks","unit":""}
  {"kind":"badges","items":[["receipts pass",true],["invalid pixels",false]]}

Enforced (a slide is a claim):
  - every slide time must be a real sentence start from the alignment;
  - every number in text OR in a progress/badge graphic must already appear in
    the transcript — invented numbers are rejected;
  - a graphic whose source data is missing is dropped, not faked.
"""
from __future__ import annotations
import json, pathlib, re, sys

sys.path.insert(0, "/Users/duhokim/HermesOps/scripts")
import nm_deck_derive as derive_mod


def numbers(text: str) -> set[str]:
    return {n.replace(",", "") for n in re.findall(r"\d[\d,]*\.?\d*", str(text))}


def build(mp3: pathlib.Path, authored: pathlib.Path) -> int:
    stem = mp3.with_suffix("")
    deck_in = json.loads(authored.read_text())
    slides_in = deck_in.get("slides") if isinstance(deck_in, dict) else deck_in
    if not isinstance(slides_in, list) or not slides_in:
        print("authored deck has no slides", file=sys.stderr)
        return 1

    sents, starts, mode, cov = derive_mod.sentences_with_times(stem)
    src_nums = numbers(" ".join(sents))

    graphics = None
    out_slides, notes = [], []
    for s in slides_in:
        t = float(s.get("t", 0))
        near = min(starts, key=lambda x: abs(x - t)) if starts else t
        if starts and abs(near - t) > 1.5:
            notes.append(f"slide time {t}s snapped to sentence start {near}s")
        t = near if starts else t
        body = " ".join([str(s.get("k", "")), str(s.get("h", ""))] + list(s.get("b") or []))
        invented = numbers(body) - src_nums
        if invented:
            notes.append(f"REJECTED slide at t={t}: number(s) {sorted(invented)} not in the audio")
            continue
        slide = {"t": t, "k": s.get("k", ""), "h": s.get("h", ""), "b": list(s.get("b") or [])[:3]}

        g = s.get("g")
        if isinstance(g, dict):
            if graphics is None:
                import importlib
                graphics = importlib.import_module("nm_report_graphics")
            kind = g.get("kind")
            try:
                if kind == "cutgrid":
                    r = graphics.cutout_grid(int(g.get("n", 12)), int(g.get("cols", 6)), f"{stem.name}:{t}")
                elif kind == "cutout":
                    r = graphics.single_cutout(f"{stem.name}:{t}")
                elif kind == "progress":  # numbers come from the SPEAKER, so they are checked
                    gn = numbers(f"{g.get('done')} {g.get('total')}") - src_nums
                    if gn:
                        notes.append(f"graphic at t={t} dropped: number(s) {sorted(gn)} not in the audio")
                        r = None
                    else:
                        r = graphics.progress_svg(float(g["done"]), float(g["total"]),
                                                  str(g.get("label", "")), str(g.get("unit", "")))
                elif kind == "skymap":
                    r = graphics.sky_map(f"{stem.name}:{t}")
                elif kind == "failstrip":
                    r = graphics.failure_strip()
                elif kind == "throughput":
                    r = graphics.throughput(int(g.get("hours", 24)))
                elif kind == "badges":
                    r = graphics.badge_svg([(str(a), bool(b)) for a, b in g.get("items", [])])
                else:
                    r = None
                    notes.append(f"unknown graphic kind '{kind}' at t={t}")
            except Exception as exc:
                r = None
                notes.append(f"graphic at t={t} failed ({type(exc).__name__}); slide kept text-only")
            if r:
                slide.update(r)
            elif kind in ("cutgrid", "cutout"):
                notes.append(f"graphic at t={t} dropped: source data unavailable (no placeholder drawn)")
        elif s.get("img"):
            slide["img"] = s["img"]
            slide["attr"] = s.get("attr", "")
        out_slides.append(slide)

    if not out_slides:
        print(f"no slides survived validation: {notes}", file=sys.stderr)
        return 1
    payload = {"marker": "NM_REPORT_DECK_V1", "timing": mode, "coverage": cov,
               "authored": True, "slides": sorted(out_slides, key=lambda x: x["t"]),
               "notes": notes}
    out = stem.with_suffix(".deck.json")
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n")
    print(f"{out.name}: {len(out_slides)} authored slide(s)"
          + (f"; {len(notes)} note(s): {notes}" if notes else ""))
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("usage: nm_deck_build.py <reading.mp3> <authored_deck.json>")
    raise SystemExit(build(pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])))
