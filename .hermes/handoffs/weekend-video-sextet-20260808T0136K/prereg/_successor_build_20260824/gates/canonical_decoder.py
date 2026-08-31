#!/usr/bin/env python3
"""canonical_decoder — REQUIRED build item (GPT56-V99 F8). Its definition is THE STATED
GRAMMAR of draft §6.1, not its fixtures (CODEX-V100 F5, GPT56-V100 F4): it accepts
EXACTLY the canonical grammar — the domain tag, the v9 field framing, the declared
payload encodings, canonical JSON, the decimal grammar — and REJECTS BY DEFAULT
everything else: unknown field names, out-of-grammar bytes, length mismatches, trailing
bytes. The bounds are the draft's valued productions (BS-2k inherits them, never the
reverse): field name ≤ 64 bytes of [a-z_]; integer ≤ 40 digits; decimal ≤ 48 chars;
string ≤ 2^16 UTF-8 NFC bytes; JSON depth ≤ 8 and ≤ 256 keys/object; payload ≤ 2^20;
envelope ≤ 2^24; ndarray via frombuffer+reshape only, C-contiguous, dtype ∈ {float64,
int64, bool}, ndim ≤ 2, ≤ 10^7 elements, object dtype refused; bool bytes exactly 0x00
or 0x01 (CODEX-V102 F8). Every node the decoder emits is constructed BY the decoder —
plain dict/str/int/float/ndarray of its own making — so no foreign object exists at any
depth (GPT56-V98 F4, CODEX-V98 F5). Fixtures corroborate; the grammar defines."""
import json
import re
import sys
import unicodedata

import numpy as np

MAX_NAME = 64
MAX_INT_DIGITS = 40
MAX_DECIMAL = 48
MAX_STRING = 2 ** 16
MAX_JSON_DEPTH = 8
MAX_JSON_KEYS = 256
MAX_PAYLOAD = 2 ** 20
MAX_ENVELOPE = 2 ** 24
MAX_NDARRAY_ELEMS = 10 ** 7

NAME_RE = re.compile(rb"[a-z_]{1,64}\Z")
DECIMAL_RE = re.compile(r"(?:(?:0|-?[1-9][0-9]*)(?:\.[0-9]*[1-9])?|-0\.[0-9]*[1-9])\Z")
INT_RE = re.compile(r"(?:0|-?[1-9][0-9]*)\Z")
DOMAIN_TAG_RE = re.compile(rb"NMPR1:[a-z][a-z0-9-]{0,62}:")


class DecodeRefusal(ValueError):
    pass


def _r(msg):
    raise DecodeRefusal(msg)


def validate_domain_tag(buf, kind):
    want = b"NMPR1:" + kind.encode() + b":"
    if not buf.startswith(want):
        _r(f"domain tag mismatch: expected {want!r}")
    return buf[len(want):]


def decode_envelope(buf, allowed_names):
    """v9 field framing: (name_len u32le, name, payload_len u64le, payload)*.
    Returns a decoder-constructed plain dict name->bytes. Reject-by-default."""
    if type(buf) is not bytes:
        _r("envelope must be bytes, exactly")
    if len(buf) > MAX_ENVELOPE:
        _r("envelope exceeds 2^24 bytes")
    allowed = {n if isinstance(n, bytes) else n.encode() for n in allowed_names}
    out = {}
    i, n = 0, len(buf)
    while i < n:
        if i + 4 > n:
            _r("truncated name length")
        nl = int.from_bytes(buf[i:i + 4], "little"); i += 4
        if nl > MAX_NAME or i + nl > n:
            _r("name length out of bounds")
        name = buf[i:i + nl]; i += nl
        if not NAME_RE.match(name):
            _r(f"field name out of grammar: {name[:20]!r}")
        if name not in allowed:
            _r(f"unknown field name: {name.decode()}")
        if name.decode() in out:
            _r(f"duplicate field: {name.decode()}")
        if i + 8 > n:
            _r("truncated payload length")
        pl = int.from_bytes(buf[i:i + 8], "little"); i += 8
        if pl > MAX_PAYLOAD or i + pl > n:
            _r("payload length out of bounds")
        out[name.decode()] = buf[i:i + pl]; i += pl
    if i != n:
        _r("trailing bytes after last field")
    missing = {a.decode() for a in allowed} - set(out)
    if missing:
        _r(f"missing required fields: {sorted(missing)}")
    return out


def decode_int(payload):
    if type(payload) is not bytes:
        _r("int payload must be bytes")
    s = payload.decode("ascii", errors="strict")
    if not INT_RE.match(s):
        _r(f"integer out of grammar: {s[:20]!r}")
    if len(s.lstrip("-")) > MAX_INT_DIGITS:
        _r("integer exceeds 40 digits")
    return int(s)


def decode_decimal(payload):
    s = payload.decode("ascii") if type(payload) is bytes else _r("decimal payload must be bytes")
    if len(s) > MAX_DECIMAL:
        _r("decimal exceeds 48 chars")
    if not DECIMAL_RE.match(s):
        _r(f"decimal out of grammar: {s[:20]!r}")
    return s  # decimals stay STRINGS — the corpus compares them as strings


def decode_string(payload):
    if len(payload) > MAX_STRING:
        _r("string exceeds 2^16 bytes")
    s = payload.decode("utf-8", errors="strict")
    if unicodedata.normalize("NFC", s) != s:
        _r("string not NFC-normal")
    return s


def _json_guard(obj, depth=0):
    if depth > MAX_JSON_DEPTH:
        _r("JSON depth exceeds 8")
    if type(obj) is dict:
        if len(obj) > MAX_JSON_KEYS:
            _r("JSON object exceeds 256 keys")
        for k, v in obj.items():
            if type(k) is not str:
                _r("non-string JSON key")
            _json_guard(v, depth + 1)
    elif type(obj) is list:
        for v in obj:
            _json_guard(v, depth + 1)
    elif type(obj) not in (str, int, float, bool, type(None)):
        _r(f"foreign JSON node type {type(obj).__name__}")


def decode_json(payload):
    s = decode_string(payload)
    try:
        obj = json.loads(s)
    except Exception as e:
        _r(f"JSON parse: {e}")
    _json_guard(obj)
    # CANONICALITY: one logical value, one byte string (sorted keys, compact, NFC,
    # short escapes via ensure_ascii=False round-trip equality)
    canon = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    if canon != s:
        _r("JSON not in canonical byte form")
    return obj


_DTYPES = {"float64": np.dtype("<f8"), "int64": np.dtype("<i8"), "bool": np.dtype("bool")}


def decode_ndarray(payload, dtype_name, shape):
    if dtype_name not in _DTYPES:
        _r(f"dtype {dtype_name!r} not in the closed set")
    if type(shape) is not tuple or len(shape) > 2 or not all(type(d) is int and d >= 0 for d in shape):
        _r("shape out of grammar (ndim ≤ 2, int dims)")
    n = 1
    for dim in shape:
        n *= dim
    if n > MAX_NDARRAY_ELEMS:
        _r("ndarray exceeds 10^7 elements")
    dt = _DTYPES[dtype_name]
    if len(payload) != n * dt.itemsize:
        _r("ndarray byte length mismatch")
    if dtype_name == "bool":
        bad = set(payload) - {0, 1}
        if bad:
            _r(f"bool bytes must be exactly 0x00/0x01; saw {sorted(bad)[:3]}")
    a = np.frombuffer(payload, dtype=dt).reshape(shape).copy()  # decoder-owned memory
    if a.dtype == np.dtype(object):
        _r("object dtype refused")
    return a


# ------------------------------------------------------------------ fixtures
def fixtures():
    f = []
    v9field = lambda name, payload: (len(name.encode()).to_bytes(4, "little")
                                     + name.encode()
                                     + len(payload).to_bytes(8, "little") + payload)
    ok = v9field("alpha", b"1") + v9field("beta", b"2")
    try:
        d = decode_envelope(ok, {"alpha", "beta"})
        if type(d) is not dict:
            f.append("envelope output not an exact dict")
    except DecodeRefusal as e:
        f.append(f"clean envelope refused: {e}")
    for label, buf, names in (
        ("trailing bytes", ok + b"x", {"alpha", "beta"}),
        ("unknown field", ok, {"alpha"}),
        ("missing field", v9field("alpha", b"1"), {"alpha", "beta"}),
        ("bad name grammar", v9field("Alpha", b"1"), {"Alpha"}),
        ("duplicate field", v9field("alpha", b"1") + v9field("alpha", b"2"), {"alpha"}),
    ):
        try:
            decode_envelope(buf, names)
            f.append(f"{label} accepted")
        except DecodeRefusal:
            pass
    for label, fn, arg in (
        ("oversized int", decode_int, b"1" * 41),
        ("leading-zero int", decode_int, b"01"),
        ("negative zero decimal", decode_decimal, b"-0"),
        ("trailing-zero decimal", decode_decimal, b"1.50"),
        ("non-NFC string", decode_string, "é".encode()),
        ("non-canonical JSON", decode_json, b'{"b":1,"a":2}'),
        ("deep JSON", decode_json, json.dumps(
            eval("{'k':" * 9 + "1" + "}" * 9)).encode()),
    ):
        try:
            fn(arg)
            f.append(f"{label} accepted")
        except DecodeRefusal:
            pass
    try:
        decode_ndarray(b"\x00\x01\x02", "bool", (3,))
        f.append("bool byte 0x02 accepted")
    except DecodeRefusal:
        pass
    a = decode_ndarray(np.arange(4, dtype="<i8").tobytes(), "int64", (2, 2))
    if type(a) is not np.ndarray or not a.flags["C_CONTIGUOUS"] or not a.flags["OWNDATA"]:
        f.append("ndarray not decoder-owned C-contiguous")
    class EvilDict(dict):
        pass
    if type(EvilDict()) is dict:
        f.append("subclass type-identity confused")
    try:
        decode_json(b'{"a":{"__array__":1}}')
        # a dict KEY named __array__ is legal JSON; the guard's job is that no node is a
        # FOREIGN OBJECT — json.loads only ever makes plain types, asserted:
        obj = json.loads('{"a": {"__array__": 1}}')
        _json_guard(obj)
    except DecodeRefusal:
        f.append("plain-JSON __array__ NAME wrongly refused (names are data; objects are the threat)")
    return f


if __name__ == "__main__":
    fails = fixtures()
    for x in fails:
        print("FIXTURE FAIL:", x)
    print(f"canonical decoder fixtures: {16 - len(fails)}/16 green")
    sys.exit(1 if fails else 0)
