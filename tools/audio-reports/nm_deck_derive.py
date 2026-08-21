#!/usr/bin/env python3
"""nm_deck_derive.py — derive a slide deck for one audio report.

Per FEATURE_SPEC_AUDIO_SLIDES_20260820 (Duho: slides are a DEFAULT part of every
audio report). Inputs beside the mp3: <stem>.txt (sentences) and <stem>.times.json
(forced alignment). Output: <stem>.deck.json in Tori's proven DECK schema.

Two hard rules, enforced mechanically rather than trusted:
  1. A slide may only RESTATE the audio — so every number appearing in the deck
     must already appear in the transcript. Invented numbers are rejected.
  2. Every slide time must equal a real sentence start time.
A deck that fails validation is discarded: the report archives audio-only.
Slides must never block archiving.

Cached: an existing .deck.json is never re-rolled (no re-billing, no drift).
"""
from __future__ import annotations
import json, pathlib, re, subprocess, sys

HERMES = "/Users/duhokim/.local/bin/hermes"
# Direct Moonshot key, not the Nous route: the Nous PLAN pool is $0.10/month and
# exhausts instantly, so "free" Nous calls actually bill purchased top-up — 102M
# kimi tokens burned ~$35 of it in two days while the direct wallet sat untouched
# at $199.73 (found 2026-08-21). Nous keeps TTS and gateway tools.
PROVIDER = "moonshot"
MODEL = "kimi-k3"
SENT_SPLIT = re.compile(r'(?<=[.!?])\s+')


def sentences_with_times(stem: pathlib.Path):
    text = stem.with_suffix(".txt").read_text().strip()
    sents = [s.strip() for s in SENT_SPLIT.split(text) if s.strip()]
    tj = stem.with_suffix(".times.json")
    if tj.exists():
        d = json.loads(tj.read_text())
        ends = d.get("ends") or []
        mode, cov = d.get("mode"), d.get("coverage", 0)
        if mode == "aligned" and cov >= 0.8 and len(ends) == len(sents):
            starts = [0.0] + ends[:-1]
            return sents, [round(s, 2) for s in starts], "aligned", cov
    # proportional fallback — declared, never passed off as precision
    total = 0
    try:
        total = float(json.loads(tj.read_text()).get("duration") or 0)
    except Exception:
        pass
    if not total:
        total = max(8.0, len(text) / 15.0)
    chars = [len(s) for s in sents] or [1]
    acc, starts = 0, []
    for c in chars:
        starts.append(round(total * acc / sum(chars), 2))
        acc += c
    return sents, starts, "estimated", 0.0


# Only take a decimal point when digits follow, so a sentence-final number does
# not swallow its full stop and fail to match the slide that quotes it.
def numbers_in(text: str) -> set[str]:
    return {n.replace(",", "") for n in re.findall(r"\d[\d,]*(?:\.\d+)?", text)}


def derive(stem: pathlib.Path) -> int:
    out = stem.with_suffix(".deck.json")
    if out.exists():
        print(f"deck cached: {out.name}")
        return 0
    if not stem.with_suffix(".txt").exists():
        print("no transcript; skipping deck", file=sys.stderr)
        return 1
    sents, starts, mode, cov = sentences_with_times(stem)
    if len(sents) < 2:
        print("too short for a deck", file=sys.stderr)
        return 1
    numbered = "\n".join(f"[t={t}] {s}" for t, s in zip(starts, sents))
    allowed = {str(t) for t in starts}
    src_nums = numbers_in(" ".join(sents))

    prompt = f"""Turn this spoken status report into a slide deck. Reply with ONLY a JSON array, no prose, no code fence.

RULES (violating any one voids the deck):
- A slide may ONLY restate what the report says. No new facts, no interpretation.
- NEVER introduce a number that is not already in the text. If a sentence has no number, its slide has no number.
- Produce 4 to 8 slides.
- Each slide's "t" MUST be exactly one of the [t=...] values shown below.
- "k" = kicker, 1-3 words. "h" = headline, max 9 words. "b" = 1-3 bullets, each max 22 words.
- Wrap numbers in <span class="num">, failures in <span class="bad">, successes in <span class="ok">.
- Schema per slide: {{"t": <number>, "k": "...", "h": "...", "b": ["...", "..."]}}

REPORT (each line prefixed with its start time in seconds):
{numbered}
"""
    r = subprocess.run([HERMES, "-z", prompt, "--provider", PROVIDER, "-m", MODEL],
                       capture_output=True, text=True, timeout=600)
    raw = r.stdout.strip()
    m = re.search(r"\[\s*{.*}\s*\]", raw, re.S)
    if not m:
        print(f"no JSON array in model reply; no deck written", file=sys.stderr)
        return 1
    try:
        deck = json.loads(m.group(0))
    except Exception as exc:
        print(f"deck JSON invalid ({exc}); no deck written", file=sys.stderr)
        return 1

    # --- enforcement: restate-only ---
    clean, rejected = [], []
    for s in deck:
        if not isinstance(s, dict) or "t" not in s or "h" not in s:
            rejected.append("malformed slide"); continue
        t = s.get("t")
        if str(round(float(t), 2)) not in allowed and str(float(t)) not in allowed:
            near = min(starts, key=lambda x: abs(x - float(t)))
            if abs(near - float(t)) > 0.6:
                rejected.append(f"invented time {t}"); continue
            s["t"] = near
        body = " ".join([str(s.get("k", "")), str(s.get("h", ""))] + list(s.get("b") or []))
        invented = numbers_in(body) - src_nums
        if invented:
            rejected.append(f"invented number(s) {sorted(invented)} in slide at t={s['t']}")
            continue
        clean.append({"t": s["t"], "k": s.get("k", ""), "h": s["h"], "b": list(s.get("b") or [])[:3]})
    if len(clean) < 3:
        print(f"deck rejected: only {len(clean)} valid slide(s); {rejected}", file=sys.stderr)
        return 1
    payload = {"marker": "NM_REPORT_DECK_V1", "timing": mode, "coverage": cov,
               "slides": sorted(clean, key=lambda x: x["t"]),
               "rejected": rejected, "model": MODEL}
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n")
    print(f"{out.name}: {len(clean)} slides ({mode}); rejected {len(rejected)}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: nm_deck_derive.py <reading.mp3>")
    p = pathlib.Path(sys.argv[1])
    raise SystemExit(derive(p.with_suffix("")))
