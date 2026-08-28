#!/usr/bin/env python3
"""nm_paper_video.py — render an INFORMATIVE paper video from recorded artifacts.

Duho's bar for these videos: convey the goal and how it works via on-screen text and
infographics. Cosmic footage is a dim backdrop at most, never the whole video. So this renders
text/data cards locally rather than generating footage — which also means it needs no browser
(Flow/Veo is browser-driven and macOS TCC blocks Apple Events from cron) and no API key (the
Gemini key is deliberately disabled). PIL draws the frames; ffmpeg stitches them.

The rule that matters: **a number may not appear on a card unless it appears in the artifact the
card cites.** Every card carries a `source` (a file in the lane or the repo); before rendering,
each numeric token in the card's text is checked against that file, and an unverifiable number is
a hard failure, not a warning. Cards that make no numeric claim need no source. This is the same
discipline the lanes run on: nothing is typed, everything is read.

Storyboard JSON:
  {"title": "...", "slug": "...",
   "cards": [{"kind": "title|point|data|limit|close",
              "heading": "...", "body": "...",
              "source": "relative/path/to/artifact.json",   # required if body has numbers
              "seconds": 5}]}

Usage:
  nm_paper_video.py storyboard.json --out video.mp4        # render
  nm_paper_video.py storyboard.json --check                # verify sources only, render nothing

Writes a local .mp4. Uploads nothing, publishes nothing, touches no network.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile

from PIL import Image, ImageDraw, ImageFont

ROOT = "/Users/duhokim/NebulaMind/NebulaMind"
W, H = 1920, 1080
BG = (11, 15, 26)
FG = (233, 238, 247)
DIM = (150, 163, 186)
ACCENT = (122, 178, 255)
FONTS = ["/System/Library/Fonts/Supplemental/Arial Bold.ttf",
         "/System/Library/Fonts/Supplemental/Arial.ttf",
         "/System/Library/Fonts/SFCompact.ttf"]
# tokens that look numeric but are not claims about the world
NUMERIC = re.compile(r"(?<![\w/])(\d[\d,]*\.?\d*)(?![\w/])")
IGNORE = {"1", "2", "3", "4", "5", "0"}          # ordinals/enumerations, not measurements


def font(size, bold=False):
    for p in ([FONTS[0]] if bold else FONTS[1:]) + FONTS:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except OSError:
                continue
    return ImageFont.load_default()


def numbers_in(text):
    return {n.replace(",", "") for n in NUMERIC.findall(text or "") if n.replace(",", "") not in IGNORE}


def verify_card(card, base, evidence=None):
    """Every numeric claim must be findable in the cited artifact. Returns list of problems.

    KNOWN LIMIT, made visible rather than papered over: this is a SUBSTRING check. It proves a
    number occurs in the cited file; it cannot prove the number means what the card says. On
    2026-08-06 it passed "z~7" on a study titled "...at z>3" because a stray 7 sat elsewhere in
    the file. So when `evidence` is supplied, each verified number records the line it was found
    on — turning a blind pass into an auditable one. A reader can then see the difference between
    `157` matched on "candidates carrying all three axes: 157" and `7` matched on a timestamp.
    """
    nums = numbers_in(card.get("body", "")) | numbers_in(card.get("heading", ""))
    if not nums:
        return []
    src = card.get("source")
    if not src:
        return [f"card '{card.get('heading','')[:40]}' states {sorted(nums)} with no source"]
    path = src if os.path.isabs(src) else os.path.join(base, src)
    if not os.path.exists(path):
        return [f"source missing: {src}"]
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        blob = f.read()
    flat = blob.replace(",", "")
    missing = [n for n in nums if n not in flat and n not in blob]
    if evidence is not None:
        lines = blob.splitlines()
        flines = [l.replace(",", "") for l in lines]
        for n in sorted(nums - set(missing)):
            hits = [lines[i].strip() for i, l in enumerate(flines) if n in l or n in lines[i]]
            evidence.append({"card": card.get("heading", "")[:44], "number": n,
                             "source": src, "hits": len(hits),
                             "context": (hits[0][:110] if hits else "(matched only across a line break)")})
    return [f"card '{card.get('heading','')[:40]}': {m} not found in {src}" for m in missing]


def wrap(draw, text, fnt, width):
    words, lines, cur = (text or "").split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines


def render_figure(card, idx, outdir):
    """A card whose subject is a PLOT.

    The figure is drawn by nm_paper_plot.py from a recorded artifact — never generated — so this
    only places it. The card still carries a `source`, and the plot carries its own provenance
    caption, so the claim and the file it came from stay attached through the cut.
    """
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 14, H], fill=ACCENT)

    fig_path = card["figure"]
    if not os.path.isabs(fig_path):
        fig_path = os.path.join("/Users/duhokim/HermesOps/cockpit/videos/plots", fig_path)
    plot = Image.open(fig_path).convert("RGB")

    f1, f2 = font(52, True), font(32)
    y = 70
    # keep the heading clear of the top-right status badge when one is requested
    head_w = (W - 560) if card.get("status_badge") else (W - 300)
    for line in wrap(d, card.get("heading", ""), f1, head_w):
        d.text((150, y), line, font=f1, fill=FG)
        y += f1.size + 12
    body_lines = wrap(d, card.get("body", ""), f2, W - 320)
    room = H - y - 60 - (len(body_lines) * (f2.size + 10)) - 40
    scale = min((W - 300) / plot.width, room / plot.height)
    plot = plot.resize((max(1, int(plot.width * scale)), max(1, int(plot.height * scale))),
                       Image.LANCZOS)
    img.paste(plot, ((W - plot.width) // 2, y + 20))
    y += 20 + plot.height + 26
    for line in body_lines:
        d.text((150, y), line, font=f2, fill=DIM)
        y += f2.size + 10

    if card.get("status_badge"):
        img = paste_status_badge(img, card["status_badge"])
    p = os.path.join(outdir, f"card_{idx:03d}.png")
    img.save(p)
    return p


def paste_status_badge(img, text):
    """Persistent per-frame status badge (e.g. RESULT HELD), top-right.

    Sealed-v8 standard: a held result's status must be structural — visible on every frame,
    never delegated to a subordinate caveat. WORKSPACE COPY ONLY; repo renderer untouched.
    """
    d = ImageDraw.Draw(img)
    f = font(30, True)
    tw = int(d.textlength(text, font=f))
    # spin pass-9 safe-area guard: the complete capsule (border included) must sit inside the
    # inner-5% rectangle (x 96..1824, y 54..1026 at 1920x1080); outer band is decorative-only
    x1, y1 = W - tw - 160, 58
    x2, y2 = W - 100, 58 + f.size + 26
    d.rounded_rectangle([x1, y1, x2, y2], radius=(y2 - y1) // 2,
                        outline=(214, 154, 102), width=3, fill=(26, 21, 16))
    d.text(((x1 + x2 - tw) // 2, y1 + 13), text, font=f, fill=(214, 154, 102))
    return img


CHARACTER = "/Users/duhokim/HermesOps/cockpit/videos/_character_ref.jpg"


def paste_character(img):
    """Composite the series' recurring character into the right of the frame.

    One locked reference image, reused across all five videos — the same discipline as the locked
    narration voice. It is DECORATION: it carries no information, states no result, and the frame
    is faded toward the background so it never competes with the text that does the work.

    Deliberately composited rather than generated per-video: a second generation would be a second
    character, and the point is that it is the same one each time.
    """
    if not os.path.exists(CHARACTER):
        return img
    ch = Image.open(CHARACTER).convert("RGB")
    target_h = int(H * 0.62)
    scale = target_h / ch.height
    ch = ch.resize((int(ch.width * scale), target_h), Image.LANCZOS)
    ch = ch.crop((max(0, ch.width - int(W * 0.34)), 0, ch.width, ch.height))
    # fade toward the page background so it reads as a backdrop element, not a subject
    ch = Image.blend(ch, Image.new("RGB", ch.size, BG), 0.42)
    x, y = W - ch.width - 60, (H - ch.height) // 2 + 40
    img.paste(ch, (x, y))
    # soft left edge: a hard vertical seam would look like a pasted rectangle, which it is
    grad = Image.new("L", (140, ch.height))
    for gx in range(140):
        for_col = int(255 * (gx / 140))
        grad.paste(for_col, (gx, 0, gx + 1, ch.height))
    img.paste(Image.new("RGB", (140, ch.height), BG), (x, y),
              Image.eval(grad, lambda v: 255 - v))
    return img


SECTIONS = ["Introduction", "Data", "Analysis", "Discussion", "Summary"]


def render_section(card, idx, outdir):
    """A journal-style section divider: Introduction / Data / Analysis / Discussion / Summary.

    Duho, 2026-08-06, asked for the videos to be laid out like a paper. The divider carries a
    progress rail so a viewer always knows where in the argument they are — the Discussion card
    landing before the Summary is the point, not an afterthought.
    """
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 14, H], fill=ACCENT)

    here = card.get("section", card.get("heading", ""))
    f1, f2, f3 = font(96, True), font(38), font(26)
    d.text((150, 400), here, font=f1, fill=FG)
    y = 400 + f1.size + 34
    for line in wrap(d, card.get("body", ""), f2, int(W * 0.62)):
        d.text((150, y), line, font=f2, fill=DIM)
        y += f2.size + 12

    # the rail: every section named, the current one lit
    x = 150
    for s in SECTIONS:
        on = (s == here)
        w = int(d.textlength(s, font=f3))
        d.rectangle([x, H - 190, x + w, H - 186], fill=ACCENT if on else (42, 51, 70))
        d.text((x, H - 175), s, font=f3, fill=FG if on else (96, 108, 128))
        x += w + 46
    p = os.path.join(outdir, f"card_{idx:03d}.png")
    img.save(p)
    return p


def render_card(card, idx, outdir):
    if card.get("kind") == "section":
        return render_section(card, idx, outdir)
    if card.get("kind") == "figure" and card.get("figure"):
        return render_figure(card, idx, outdir)
    img = Image.new("RGB", (W, H), BG)
    if card.get("character"):
        img = paste_character(img)
    d = ImageDraw.Draw(img)
    kind = card.get("kind", "point")

    # a restrained accent bar: identity without decoration competing with the text
    d.rectangle([0, 0, 14, H], fill=ACCENT if kind != "limit" else (214, 154, 102))

    hx, y = 150, 250
    # the character occupies the right third; text must not run under her face, so the measure
    # narrows rather than the portrait shrinking — the words are what carry the meaning
    tw = int(W * 0.58) if card.get("character") else W - 300
    if kind == "title":
        f1, f2 = font(88, True), font(40)
        y = 380
    elif kind == "data":
        f1, f2 = font(150, True), font(42)
    else:
        f1, f2 = font(62, True), font(40)

    for line in wrap(d, card.get("heading", ""), f1, tw):
        d.text((hx, y), line, font=f1, fill=FG if kind != "data" else ACCENT)
        y += f1.size + 18
    y += 30
    for line in wrap(d, card.get("body", ""), f2, tw - 20):
        d.text((hx, y), line, font=f2, fill=DIM)
        y += f2.size + 16

    # Audience frames carry a human-readable citation; the `source` path keeps feeding the
    # numeric guard and the receipts. Standard upheld by the sealed spin v8 audit (no internal
    # paths/identifiers on screen) and requested identically by the fesc and c41 lanes.
    # WORKSPACE COPY ONLY — the repo's shared renderer is untouched (Git gate closed).
    if card.get("display_citation"):
        fs = font(26)
        d.text((hx, H - 90), card["display_citation"], font=fs, fill=(96, 108, 128))
    elif card.get("source"):
        fs = font(26)
        d.text((hx, H - 90), f"source: {card['source']}", font=fs, fill=(96, 108, 128))

    if card.get("status_badge"):
        img = paste_status_badge(img, card["status_badge"])

    p = os.path.join(outdir, f"card_{idx:03d}.png")
    img.save(p)
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("storyboard")
    ap.add_argument("--out")
    ap.add_argument("--check", action="store_true", help="verify sources; render nothing")
    ap.add_argument("--frames-only", metavar="DIR",
                    help="render the card PNGs and a concat list into DIR and stop. Lets the "
                         "caller do backdrop + audio + encode in ONE pass, instead of encoding "
                         "here and re-encoding later — which cost a visible generation of "
                         "quality on text and plots.")
    ap.add_argument("--fps", type=int, default=30)
    a = ap.parse_args()

    sb = json.load(open(a.storyboard))
    base = os.path.dirname(os.path.abspath(a.storyboard))
    cards = sb.get("cards", [])

    problems, evidence = [], ([] if a.check else None)
    for c in cards:
        problems += verify_card(c, base, evidence)
        # A figure card that points at a missing PNG must fail here, not render a blank frame
        # where a chart was promised.
        if c.get("kind") == "figure":
            fp = c.get("figure", "")
            if not os.path.isabs(fp):
                fp = os.path.join("/Users/duhokim/HermesOps/cockpit/videos/plots", fp)
            if not fp or not os.path.exists(fp):
                problems.append(f"card '{c.get('heading','')[:40]}': figure missing: "
                                f"{c.get('figure','(none)')}")
    if problems:
        print("UNVERIFIED NUMERIC CLAIMS — refusing to render:")
        for p in problems:
            print("  -", p)
        return 2
    print(f"all {len(cards)} cards verified against their sources")
    if a.check:
        # Show WHERE each number was found. The substring check cannot judge meaning; a human
        # reading these lines can. Numbers matching in many places, or in a line that has
        # nothing to do with the claim, are the ones to look at.
        print("\n--- evidence audit (read the context, not just the match) ---")
        for e in evidence or []:
            flag = "  <-- CHECK" if e["hits"] > 6 or e["hits"] == 0 else ""
            print(f"  [{e['number']:>10}] x{e['hits']:<3} {e['card'][:34]:<36} {e['context'][:70]}{flag}")
        return 0

    if not shutil.which("ffmpeg"):
        print("ffmpeg not found"); return 3
    out = a.out or os.path.join(ROOT, "frontend", "public", "videos", f"{sb['slug']}.mp4")
    os.makedirs(os.path.dirname(out), exist_ok=True)

    def write_frames(dirpath):
        """Render the cards and a concat list whose durations land EXACTLY on frame boundaries.

        The old list wrote raw float seconds. The concat demuxer then quantised each card to the
        frame grid and the remainders were lost: a 99.2s storyboard came out as a 97.4s video,
        1.8s short. That is invisible on its own — but the narration is placed at the storyboard's
        offsets, so every card drifted ~0.18s further out of sync than the last, and by the close
        card the voice was talking over the wrong slide.

        Rounding here, and returning the rounded values so the caller places audio on the SAME
        grid, is what makes the two agree by construction rather than by luck.
        """
        listing = os.path.join(dirpath, "list.txt")
        frame = 1.0 / a.fps
        exact = []
        with open(listing, "w") as lf:
            for i, c in enumerate(cards):
                p = render_card(c, i, dirpath)
                d = max(1, round(float(c.get("seconds", 5)) / frame)) * frame
                exact.append(d)
                lf.write(f"file '{p}'\nduration {d:.6f}\n")
            lf.write(f"file '{p}'\n")          # concat demuxer needs the last frame repeated
        with open(os.path.join(dirpath, "durations.json"), "w") as f:
            json.dump({"fps": a.fps, "seconds": exact, "total": sum(exact)}, f)
        return listing, exact

    if a.frames_only:
        os.makedirs(a.frames_only, exist_ok=True)
        listing, exact = write_frames(a.frames_only)
        print(f"frames: {len(cards)} cards -> {a.frames_only} "
              f"(total {sum(exact):.3f}s, frame-aligned at {a.fps}fps)")
        return 0

    tmp = tempfile.mkdtemp(prefix="nm_video_")
    try:
        listing, _ = write_frames(tmp)
        cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
               "-f", "concat", "-safe", "0", "-i", listing,
               "-vf", f"fps={a.fps},format=yuv420p", "-c:v", "libx264", "-preset", "medium",
               "-crf", "20", out]
        subprocess.run(cmd, check=True)
        print(f"wrote {out} ({os.path.getsize(out)} bytes, {len(cards)} cards)")
        print("NOT uploaded. Publishing is a separate, explicitly-approved step.")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
