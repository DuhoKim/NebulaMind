#!/usr/bin/env python3
# C1 helper: print repr() head/tail and byte count for entry 18 (PDF-extracted source).
path = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt"
with open(path, "rb") as f:
    data = f.read()
text = data.decode("utf-8", errors="replace")
print("byte_count:", len(data))
print("char_count:", len(text))
print("repr_first_200:")
print(repr(text[:200]))
print("repr_last_200:")
print(repr(text[-200:]))
print("NOTE: the full repr is reproducible from the raw bytes of the file pinned by sha256 "
      "2f3ca3e10ec016eed83104750d11d2428d5523c712814f68d559724d8b2c6b6f")
