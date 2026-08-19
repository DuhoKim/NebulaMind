#!/usr/bin/env python3
"""Forced-align a reading to its transcript; write per-sentence boundary times.

Why this exists: the archive highlights the sentence being spoken. Estimating that
from text was measured at ~11 wrong-sentence seconds per 60s — the character model
is already at its tuning ceiling (K=15 vs the live K=14 changed nothing), and a
syllable model scored worse. Real alignment is the only thing that clears the bar.

Runs at BUILD time only. archive.html never makes a network call. If this fails for
a reading, no .times.json is written and the index silently falls back to estimating.
Alignment must never block archiving.

  nm_audio_align.py            # align anything not already done
  nm_audio_align.py --all      # redo everything
  nm_audio_align.py FILE.mp3   # one reading
"""
import sys, re, json, difflib, pathlib

R = pathlib.Path("/Users/duhokim/HermesOps/reports/status-audio")
MODEL = "base.en"

def norm(t):
    return re.findall(r"[a-z0-9]+", t.lower())

def sentences(t):
    parts = re.split(r"((?<=[.!?])\s+)", t)
    return [p for i, p in enumerate(parts) if i % 2 == 0 and p.strip()]

def align(stem, model):
    txt = R / f"{stem}.txt"
    aud = R / f"{stem}.mp3"
    if not (txt.exists() and aud.exists()):
        return None
    text = txt.read_text().strip()
    sents = sentences(text)
    if not sents:
        return None
    segs, info = model.transcribe(str(aud), word_timestamps=True, language="en")
    words = [(w.word, w.start) for s in segs for w in (s.words or [])]
    if not words:
        return None

    ref, owner = [], []
    for i, s in enumerate(sents):
        for tok in norm(s):
            ref.append(tok); owner.append(i)
    hyp, htime = [], []
    for w, st in words:
        for tok in norm(w):
            hyp.append(tok); htime.append(st)

    sm = difflib.SequenceMatcher(a=hyp, b=ref, autojunk=False)
    first, matched = {}, 0
    for ai, bi, size in sm.get_matching_blocks():
        for k in range(size):
            matched += 1
            si, t = owner[bi + k], htime[ai + k]
            if si not in first or t < first[si]:
                first[si] = t
    cov = matched / max(len(ref), 1)
    # Coverage is the honest quality signal: whisper writes digits where the script
    # spelled them out, so some tokens never match. Too few anchors and the
    # interpolation below is doing the work, not the alignment.
    if cov < 0.5:
        return None

    dur = float(info.duration)
    starts = [first.get(i) for i in range(len(sents))]
    starts[0] = 0.0
    for i in range(1, len(starts)):
        if starts[i] is None:
            nxt = next((starts[j] for j in range(i + 1, len(starts)) if starts[j] is not None), dur)
            starts[i] = (starts[i - 1] + nxt) / 2
        starts[i] = max(starts[i], starts[i - 1] + 0.05)
    ends = starts[1:] + [dur]
    return {"mode": "aligned", "coverage": round(cov, 4), "duration": dur,
            "n": len(sents), "ends": [round(x, 3) for x in ends]}

def main():
    args = [a for a in sys.argv[1:]]
    redo = "--all" in args
    named = [a for a in args if not a.startswith("--")]
    if named:
        stems = [pathlib.Path(n).stem for n in named]
    else:
        stems = sorted(p.stem for p in R.glob("*.txt")
                       if not p.stem.startswith("latest") and (R / (p.stem + ".mp3")).exists())
    todo = [s for s in stems if redo or not (R / f"{s}.times.json").exists()]
    if not todo:
        print("nothing to align"); return
    from faster_whisper import WhisperModel
    model = WhisperModel(MODEL, device="cpu", compute_type="int8")
    ok = 0
    for s in todo:
        try:
            r = align(s, model)
        except Exception as e:
            print(f"  {s}: FAILED ({e.__class__.__name__}) — will fall back to estimate"); continue
        if not r:
            print(f"  {s}: no usable alignment — will fall back to estimate"); continue
        (R / f"{s}.times.json").write_text(json.dumps(r))
        ok += 1
        print(f"  {s}: {r['n']} sentences, coverage {r['coverage']:.0%}")
    print(f"aligned {ok}/{len(todo)}")

if __name__ == "__main__":
    main()
