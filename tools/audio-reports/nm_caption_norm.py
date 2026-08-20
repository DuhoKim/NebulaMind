#!/usr/bin/env python3
"""nm_caption_norm.py — captions carry digits, not spelled-out numbers.

Duho's standing rule (2026-08-12, restated 2026-08-20): "numbers stay — they
are the content". Spelling them out for the voice ("three hundred forty six")
leaks straight into the caption, because the caption IS the spoken text. This
normalizes the DISPLAY copy only; the audio already spoke whatever it spoke.

Also collapses letter-spacing pronunciation hacks ("S E O" -> "SEO") for the
same reason: they are speech aids, not reading text.
"""
from __future__ import annotations
import re

UNITS = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,
         "eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,
         "fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,
         "nineteen":19}
TENS = {"twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,
        "eighty":80,"ninety":90}
SCALES = {"hundred":100,"thousand":1000,"million":1_000_000,"billion":1_000_000_000}
WORDS = set(UNITS) | set(TENS) | set(SCALES)
# "one" and "a" as articles are left alone; only run-forming words convert.
KEEP_AS_WORD = {"one"}


def _value(tokens: list[str]) -> int:
    total = current = 0
    for t in tokens:
        if t in UNITS:
            current += UNITS[t]
        elif t in TENS:
            current += TENS[t]
        elif t == "hundred":
            current = (current or 1) * 100
        else:
            current = (current or 1) * SCALES[t]
            total += current
            current = 0
    return total + current


def spelled_to_digits(text: str) -> tuple[str, int]:
    """Return (normalized, replacements). Converts every spelled-out numeral
    except a bare 'one' (which is as often an article as a count)."""
    out, n = [], 0
    tokens = re.split(r"(\W+)", text)
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        low = tok.lower().strip("-")
        if low in WORDS:
            run, j = [], i
            last_word = i          # index of the last NUMBER token consumed
            while j < len(tokens):
                w = tokens[j].lower().strip("-")
                if w in WORDS:
                    run.append(w)
                    last_word = j
                    j += 1
                elif w == "and" and any(r in SCALES for r in run):
                    # "two thousand AND forty seven" is ONE number in ordinary
                    # speech. Splitting it wrote "2,000 and 47" into the caption,
                    # so slides legitimately claiming 2,047 were refused (Hwao
                    # lost 4 of 6 slides to this, 2026-08-20). Absorb the
                    # connector only where a scale word precedes it — "3 machines
                    # and 2 repairs" must stay two separate numbers.
                    k = j + 1
                    while k < len(tokens) and not tokens[k].strip():
                        k += 1
                    if k < len(tokens) and tokens[k].lower().strip("-") in WORDS:
                        j = k
                        continue
                    break
                elif not tokens[j].strip() or tokens[j].strip() == "-":
                    nxt = j + 1
                    if nxt < len(tokens) and (tokens[nxt].lower().strip("-") in WORDS
                                              or tokens[nxt].lower().strip("-") == "and"):
                        j += 1
                    else:
                        break
                else:
                    break
            j = last_word + 1      # never swallow the separator after the number
            words_only = [t for t in run]
            if words_only and not (len(words_only) == 1 and words_only[0] in KEEP_AS_WORD):
                val = _value(words_only)
                # Duho, 2026-08-20: digits, not words — all counts, not just
                # the big ones. Only bare "one" stays a word (it reads as an
                # article as often as a count: "one of the lanes").
                if len(words_only) > 1 or val >= 2:
                    out.append(f"{val:,}")
                    n += 1
                    i = j
                    continue
        out.append(tok)
        i += 1
    return "".join(out), n


def collapse_letter_spacing(text: str) -> tuple[str, int]:
    """'S E O' -> 'SEO' (pronunciation aid, not reading text)."""
    pattern = re.compile(r"\b(?:[A-Z] ){1,5}[A-Z]\b")
    n = 0
    def sub(m):
        nonlocal n
        n += 1
        return m.group(0).replace(" ", "")
    return pattern.sub(sub, text), n


def normalize(text: str) -> tuple[str, int]:
    t, a = spelled_to_digits(text)
    t, b = collapse_letter_spacing(t)
    return t, a + b


if __name__ == "__main__":
    import sys
    src = sys.stdin.read() if len(sys.argv) < 2 else sys.argv[1]
    norm, n = normalize(src)
    print(norm)
    if n:
        print(f"[{n} caption normalization(s)]", file=sys.stderr)
