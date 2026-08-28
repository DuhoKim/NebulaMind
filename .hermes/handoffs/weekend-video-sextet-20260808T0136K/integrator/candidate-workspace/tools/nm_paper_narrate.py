#!/usr/bin/env python3
"""nm_paper_narrate.py — mux a paper's per-card narration onto its cards.

Duho, 2026-08-06: "i don't want low quality tts let Yuis add proper audio on top of it." So the
VOICE is not made here — Yui synthesises one track per card and this only places them. Keeping
the two apart is what let the narrated cuts survive a session dying mid-run: synthesis is
expensive and resumable, muxing is cheap and repeatable.

Two things it gets right that the earlier ad-hoc ffmpeg lines did not:

1. **A card is never shorter than its narration.** The card's on-screen time is the LARGER of the
   storyboard's `seconds` and the track's real duration plus a tail. The first cuts had lines
   still speaking as the card changed, and a pile of `*_overflow.mp3` retries trying to talk
   faster instead of holding the card longer.
2. **It renders through nm_paper_video.py rather than around it**, so the numeric-source guard
   still runs. A narration pass must not be a way to ship a card the guard would have refused.

Audio layout: <videos>/_audio_<slug>/NN.mp3 or card_NN.mp3, one per card, 1-indexed.

Usage:  nm_paper_narrate.py <storyboard.json> [--slug S] [--dry-run]
"""
import argparse, json, os, shutil, subprocess, sys, tempfile, time

ROOT = "/Users/duhokim/NebulaMind/NebulaMind"
VID = "/Users/duhokim/HermesOps/cockpit/videos"
TAIL = 1.2          # breath after a line before the card turns


def dur(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def track_for(adir, i):
    """FOUR naming conventions are in use across the five lanes — NN, card_NN, cardNN, card-NN —
    because each was narrated in a separate session. Accept all of them rather than renaming files
    Yui already produced; a rename would break whichever lane was not looked at."""
    for name in (f"{i:02d}.mp3", f"card_{i:02d}.mp3", f"card{i:02d}.mp3", f"card-{i:02d}.mp3"):
        p = os.path.join(adir, name)
        if os.path.exists(p):
            return p
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("storyboard")
    ap.add_argument("--slug")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    sb = json.load(open(a.storyboard))
    slug = a.slug or sb["slug"]
    cards = sb["cards"]
    adir = os.path.join(VID, f"_audio_{slug}")

    tracks, missing = [], []
    for i, c in enumerate(cards, 1):
        t = track_for(adir, i)
        tracks.append(t)
        # section dividers are deliberately silent: the section name and the progress rail say
        # what the chapter is, and a spoken gloss on top of that is filler.
        if not t and c.get("kind") != "section":
            missing.append(i)
    if missing:
        print(f"MISSING narration for card(s) {missing} in {adir}")
        print("  Yui synthesises these; this tool only places them. Nothing rendered.")
        for i in missing:
            c = cards[i - 1]
            line = f"{c['heading']}. {c['body']}"
            print(f"\n  --- line for card {i:02d} ---\n  {' '.join(line.split())}")
        return 2

    # timeline: each card holds for at least as long as it is spoken
    secs, offs, t = [], [], 0.0
    for c, tr in zip(cards, tracks):
        d = float(c.get("seconds", 5)) if tr is None else max(float(c.get("seconds", 5)),
                                                              dur(tr) + TAIL)
        offs.append(t)
        secs.append(d)
        t += d
    print(f"{slug}: {len(cards)} cards, {t:.1f}s total")
    for i, (c, d, o) in enumerate(zip(cards, secs, offs), 1):
        grew = "" if d <= float(c.get("seconds", 5)) + 0.01 else \
               f"  (held {d - float(c.get('seconds', 5)):.1f}s longer for the line)"
        print(f"  {i:02d} @{o:6.1f}s  {d:4.1f}s  {c['heading'][:40]}{grew}")
    if a.dry_run:
        return 0

    # ONE encode, not two. Cards, backdrop and narration are combined in a single ffmpeg pass:
    # the previous shape encoded the cards to h264, then re-encoded that h264 to blend the
    # backdrop, so every frame of text and every plot went through two lossy generations. The
    # visible softening was that, not the footage.
    frames = tempfile.mkdtemp(prefix="nm_frames_")
    try:
        stretched = os.path.join(frames, "storyboard_stretched.json")
        with open(stretched, "w") as sf:
            json.dump({**sb, "cards": [{**c, "seconds": v} for c, v in zip(cards, secs)]}, sf)
        # the renderer resolves relative `source` paths against the storyboard's directory, so the
        # stretched copy must sit where the original did or every citation breaks
        stretched2 = os.path.join(os.path.dirname(os.path.abspath(a.storyboard)),
                                  "_tmp_stretched_storyboard.json")
        shutil.copy(stretched, stretched2)
        r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "nm_paper_video.py"),
                            stretched2, "--frames-only", frames], capture_output=True, text=True)
        os.unlink(stretched2)
        print("  " + (r.stdout.strip() or r.stderr.strip()))
        if r.returncode:
            return r.returncode
        # the renderer quantised each card to the frame grid; re-place the audio on THOSE values
        # so slide and voice share one timeline by construction
        exact = json.load(open(os.path.join(frames, "durations.json")))["seconds"]
        offs, t = [], 0.0
        for d in exact:
            offs.append(t); t += d
        drift = sum(secs) - sum(exact)
        if abs(drift) > 0.001:
            print(f"  card timeline snapped to the {30}fps grid ({drift:+.3f}s vs the storyboard); "
                  f"audio placed on the snapped grid, so no drift accumulates")

        # VERSIONED FILENAME. A rebuild that reuses the same name is invisible to a browser —
        # three times running, Duho was shown a "not updated" video that was in fact current, and
        # the only thing wrong was the cache. A new cut gets a new URL, so it cannot be cached
        # away. The unversioned name is kept as a copy for anything that hardcodes it.
        stamp = time.strftime("%Y%m%dT%H%M")
        out = os.path.join(VID, f"{slug}-narrated-{stamp}.mp4")
        stable = os.path.join(VID, f"{slug}-narrated.mp4")
        bd = os.path.join(VID, f"_backdrop_{slug}.mp4")
        cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
               "-f", "concat", "-safe", "0", "-i", os.path.join(frames, "list.txt")]
        filt = []
        vlabel = "[0:v]"
        nin = 1
        if os.path.exists(bd):
            cmd += ["-stream_loop", "-1", "-i", bd]
            spans = [f"between(t,{o:.3f},{o + d:.3f})"
                     for c, d, o in zip(cards, exact, offs) if c.get("kind") != "figure"]
            filt.append("[1:v]scale=1920:1080,fps=30,setsar=1,"
                        "colorchannelmixer=rr=0.5:gg=0.5:bb=0.5[bg]")
            filt.append(f"[0:v]fps=30[cards]")
            filt.append(f"[cards][bg]blend=all_mode=lighten:shortest=1:enable='{'+'.join(spans)}'[v]")
            vlabel = "[v]"
            nin = 2
        else:
            filt.append("[0:v]fps=30[v]")
            vlabel = "[v]"
        voiced = [(tr, o) for tr, o in zip(tracks, offs) if tr]
        for i, (tr, o) in enumerate(voiced):
            cmd += ["-i", tr]
            ms = int(round(o * 1000))
            filt.append(f"[{nin + i}:a]adelay={ms}|{ms}[a{i}]")
        mix = "".join(f"[a{i}]" for i in range(len(voiced)))
        filt.append(f"{mix}amix=inputs={len(voiced)}:normalize=0:dropout_transition=0[vo]")
        filt.append(f"{vlabel}format=yuv420p[vout]")
        cmd += ["-filter_complex", ";".join(filt), "-map", "[vout]", "-map", "[vo]",
                "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-maxrate", "6M", "-bufsize", "12M",
                "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
                "-t", f"{sum(exact):.3f}", out + ".new.mp4"]
        rr = subprocess.run(cmd, capture_output=True, text=True)
        if rr.returncode:
            print("  ENCODE FAILED:", (rr.stderr or "").strip()[:200])
            if os.path.exists(out + ".new.mp4"):
                os.unlink(out + ".new.mp4")
            return rr.returncode
        # a file is only allowed to replace a working video once it demonstrably decodes
        probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                                "-show_entries", "stream=duration", "-of", "csv=p=0",
                                out + ".new.mp4"], capture_output=True, text=True)
        if probe.returncode or not probe.stdout.strip():
            print("  ENCODE PRODUCED AN UNREADABLE FILE — keeping the previous video")
            os.unlink(out + ".new.mp4"); return 4
        os.replace(out + ".new.mp4", out)
        shutil.copy2(out, stable)          # stable alias for anything that hardcodes the name
        # keep the three most recent versions; a lane rebuilt often should not fill the disk
        vers = sorted(f for f in os.listdir(VID)
                      if f.startswith(f"{slug}-narrated-") and f.endswith(".mp4"))
        for old in vers[:-3]:
            os.unlink(os.path.join(VID, old))
        if len(vers) > 3:
            print(f"  pruned {len(vers) - 3} old version(s), kept the newest 3")
        if os.path.exists(bd):
            print(f"  single pass: {len(spans)} text card(s) over backdrop, "
                  f"{len(cards) - len(spans)} figure card(s) masked")
    finally:
        shutil.rmtree(frames, ignore_errors=True)

    # verify there is actually sound in it — a silent "narrated" cut shipped once already
    lvl = subprocess.run(["ffmpeg", "-i", out, "-af", "volumedetect", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    mean = next((l.split("mean_volume:")[1].strip() for l in lvl.splitlines()
                 if "mean_volume:" in l), "unknown")
    print(f"wrote {out} ({os.path.getsize(out)} bytes) · mean volume {mean}")
    print("NOT uploaded. Publishing is a separate, explicitly-approved step.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
