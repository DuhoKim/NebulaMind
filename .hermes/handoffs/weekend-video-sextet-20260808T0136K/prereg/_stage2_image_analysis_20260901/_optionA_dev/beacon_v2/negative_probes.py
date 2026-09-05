#!/usr/bin/env python3
"""NEGATIVE PROBES for beacon_v2 — alter one thing at a time in a GENUINE record (produced by beacon_record.collect over the three-tier test
network) and record the shared verdict's outcome AND the identity builder's response (the builder calls the same verdict). Also probes the
builder's own boundary (hand-made record; bare seed). Output: negative_probes_receipt.json + a Markdown table. Offline; mocked network."""
import json, sys, tempfile, hashlib, importlib.util
from pathlib import Path
from datetime import datetime, timezone, timedelta
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import beacon_record as br, drand_round, test_pki as pki, nist_pulse
bspec = importlib.util.spec_from_file_location("bci", HERE.parent / "corpus_identity" / "build_corpus_identity.py"); bci = importlib.util.module_from_spec(bspec); bspec.loader.exec_module(bci)
bci.nist_pulse.pinned_roots = lambda: pki.roots()
EXCL = HERE.parent / "corpus_identity" / "dryrun_identities_to_exclude_20260905.txt"
T_SIGN = datetime(2026, 9, 6, 0, 0, tzinfo=timezone.utc); TP = br.pulse_time(T_SIGN); D = "a" * 64; STMT = f"signed {D} at {br.fmt(T_SIGN)}".encode(); RND = drand_round.round_for(TP)
rows = []
def build(rec_dict, net, now, rule=D, stmt=STMT):
    d = Path(tempfile.mkdtemp()); rp = d / "r.json"; rp.write_text(json.dumps(rec_dict)); sp = d / "s.txt"; sp.write_bytes(stmt)
    try: bci.build(out_dir=d / "out", beacon_record_path=rp, exclude_path=EXCL, rule_sha256=rule, signature_statement=sp, fetch=net, now=now); return "BUILT"
    except SystemExit as e: return str(e).split(":")[0] + (" (" + str(e).split("verdict ")[1].split(":")[0] + ")" if "verdict " in str(e) else "")
def probe(name, rec, net, now, **kw):
    v = br.verdict(rec, now, pki.roots(), fetch=net, rule_sha256=kw.get("rule", D), statement_bytes=kw.get("stmt", STMT)); rows.append((name, v["outcome"], build(rec, net, now, kw.get("rule", D), kw.get("stmt", STMT))))
net = pki.network(TP); now1 = TP + timedelta(hours=1); base = br.collect(net, br.fmt(T_SIGN), D, STMT, now=now1)
probe("genuine NIST record (three-tier chain, signed pulse)", base, net, now1)
def mut(fn): R = json.loads(json.dumps(base)); fn(R); return R
def repulse(R, edit):
    pb = json.loads(br.unb64(R["nist"]["pulse_body_b64"])); edit(pb["pulse"]); R["nist"]["pulse_body_b64"] = br.b64(json.dumps(pb).encode())
probe("schema field changed", mut(lambda R: R.__setitem__("schema", "X")), net, now1)
probe("T_pulse not derived from T_sign", mut(lambda R: R.__setitem__("T_pulse", br.fmt(TP + timedelta(minutes=1)))), net, now1)
probe("rule digest supplied differs from the record's", base, net, now1, rule="b" * 64)
probe("statement supplied differs from the record's", base, net, now1, stmt=b"other")
probe("statement lacks the binding", mut(lambda R: R.__setitem__("statement_b64", br.b64(b"no binding"))), net, now1, stmt=b"no binding")
probe("pulse outputValue replaced (seed of choice)", mut(lambda R: repulse(R, lambda p: p.__setitem__("outputValue", "E" * 128))), net, now1)
probe("pulse timeStamp shifted one minute", mut(lambda R: repulse(R, lambda p: p.__setitem__("timeStamp", (TP + timedelta(minutes=1)).strftime("%Y-%m-%dT%H:%M:%S.000Z")))), net, now1)
probe("pulse statusCode 1", mut(lambda R: repulse(R, lambda p: p.__setitem__("statusCode", 1))), net, now1)
probe("intermediate certificates removed (chain cannot anchor)", mut(lambda R: R["nist"].__setitem__("intermediate_pems_b64", [])), net, now1)
def selfsigned(R):
    lc, k = pki.leaf(signed_by="self"); R["nist"]["leaf_pem_b64"] = br.b64(pki.pem(lc)); R["nist"]["pulse_body_b64"] = br.b64(pki.pulse_body(TP, lc, k))
probe("self-signed leaf with a pulse signed under it (internally consistent)", mut(selfsigned), pki.network(TP, leaf_cert=pki.leaf(signed_by="self")[0], key=pki.leaf(signed_by="self")[1]), now1)
probe("retained intermediate certificate replaced (live issuer chain differs)", mut(lambda R: R["nist"].__setitem__("intermediate_pems_b64", [br.b64(pki.pem(pki.ROOT))])), net, now1)
probe("next pulse altered (precommitment link broken)", mut(lambda R: R["nist"].__setitem__("next_body_b64", br.b64(json.dumps({"pulse": {"localRandomValue": "99" * 64}}).encode()))), net, now1)
probe("retained record genuine, but NIST now serves an unsigned pulse (live differs)", base, pki.network(TP, sign=False), now1)
probe("unsigned pulse before 24 h", br.collect(pki.network(TP, sign=False), br.fmt(T_SIGN), D, STMT, now=now1), pki.network(TP, sign=False), now1)
now25 = TP + timedelta(hours=25); netf = pki.network(TP, nist_404=True, drand=(RND, "f" * 64)); fb = br.collect(netf, br.fmt(T_SIGN), D, STMT, now=now25)
probe("genuine drand fallback (NIST 404 for 25 h; four pinned relays agree)", fb, netf, now25)
probe("fallback record, but NIST serves an AUTHENTICABLE pulse now (two-link chain)", fb, pki.network(TP, drand=(RND, "f" * 64)), now25)
probe("fallback record, live relays report a different randomness", fb, pki.network(TP, nist_404=True, drand=(RND, "0" * 64)), now25)
def invent(R):
    b = json.dumps({"round": RND, "randomness": "e" * 64}).encode(); R["drand"]["relays"] = {"https://attacker-one.invalid/public/%d" % RND: {"body_b64": br.b64(b)}, "https://attacker-two.invalid/public/%d" % RND: {"body_b64": br.b64(b)}}
fb2 = json.loads(json.dumps(fb)); invent(fb2); probe("fallback record with two invented relay hosts and a chosen seed", fb2, netf, now25)
def wrong_round(R):
    for u, r in R["drand"]["relays"].items(): r["body_b64"] = br.b64(json.dumps({"round": RND + 1, "randomness": "f" * 64}).encode())
fb3 = json.loads(json.dumps(fb)); wrong_round(fb3); probe("fallback record whose relay bodies carry the wrong round", fb3, netf, now25)
probe("fallback attempted before 24 h (relays present)", br.collect(pki.network(TP, nist_404=True, drand=(RND, "f" * 64)), br.fmt(T_SIGN), D, STMT, now=now1), pki.network(TP, nist_404=True, drand=(RND, "f" * 64)), now1)
rows.append(("builder: hand-made two-field record", "—", build({"source": "NIST-beacon-2.0", "seed_hex": "e" * 128}, net, now1)))
try: bci.build(out_dir=Path(tempfile.mkdtemp()), seed_hex="e" * 128, exclude_path=EXCL); rows.append(("builder: bare seed without test flag", "—", "BUILT"))
except SystemExit as e: rows.append(("builder: bare seed without test flag", "—", str(e).split(":")[0]))
rec = {"deterministic": True, "probes": [{"probe": a, "verdict": b, "builder": c} for a, b, c in rows], "files": {f: hashlib.sha256((HERE / f).read_bytes()).hexdigest() for f in ("beacon_record.py", "nist_pulse.py", "drand_round.py", "test_pki.py")} | {"build_corpus_identity.py": hashlib.sha256((HERE.parent / "corpus_identity" / "build_corpus_identity.py").read_bytes()).hexdigest()}}
(HERE / "negative_probes_receipt.json").write_text(json.dumps(rec, indent=1)); print("| probe | verdict | builder |\n|---|---|---|"); [print(f"| {a} | {b} | {c} |") for a, b, c in rows]
