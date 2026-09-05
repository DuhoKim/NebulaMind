#!/usr/bin/env python3
"""NEGATIVE PROBES for the beacon-record path (selection rule §3b) — a receipt a referee reads instead of constructing tampered inputs
itself. Each probe takes a GENUINE fetcher record (produced by fetch_beacon.main under a mocked network with a test-signed pulse),
alters ONE thing, and records the builder's refusal token. Also probes the fetcher directly (unsigned pulse; single relay).
Output: negative_probes_receipt.json + a Markdown table on stdout. Nothing here touches the network or any real pixel."""
import json, sys, tempfile, hashlib, importlib.util
from pathlib import Path
from datetime import datetime, timezone, timedelta
from unittest import mock
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import fetch_beacon as fb, test_support as ts
ts.install_test_root()
bspec = importlib.util.spec_from_file_location("bci", HERE.parent / "corpus_identity" / "build_corpus_identity.py"); bci = importlib.util.module_from_spec(bspec); bspec.loader.exec_module(bci)
EXCL = HERE.parent / "corpus_identity" / "dryrun_identities_to_exclude_20260905.txt"

def genuine(source="nist", hours=2):
    d = Path(tempfile.mkdtemp()); rec = d / "record.json"; stmt = d / "statement.txt"; D = "a" * 64
    t_sign = (datetime.now(timezone.utc) - timedelta(hours=hours)).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ"); tp = fb.pulse_time(fb.parse_utc(t_sign)); stmt.write_text(f"signed {D} at {t_sign}")
    if source == "nist": body, pem = ts.make_nist(tp); side = ts.nist_side(body, pem, tp=tp)
    else: side = ts.drand_side(fb.drand_round(tp))
    CURRENT["side"] = side
    with mock.patch.object(fb, "fetch", side_effect=side): rc = fb.main(["--t-sign", t_sign, "--out", str(rec), "--rule-sha256", D, "--signature-statement", str(stmt)])
    return rc, rec, stmt, D, d

CURRENT = {"side": None}
def build(rec, stmt, D):
    """The builder RE-FETCHES the public sources at build time; the same mocked source that produced the genuine record answers."""
    try:
        with mock.patch.object(fb, "fetch", side_effect=CURRENT["side"]): bci.build(out_dir=Path(tempfile.mkdtemp()), beacon_record=rec, exclude_path=EXCL, rule_sha256=D, signature_statement=stmt)
        return "ACCEPTED"
    except SystemExit as e: return str(e).split(":")[0]

rows = []
rc, rec, stmt, D, d = genuine("nist"); base = json.loads(rec.read_text()); rows.append(("genuine NIST record from the fetcher (test-signed pulse)", f"fetch rc={rc}", build(rec, stmt, D)))
def variant(name, mutate):
    R = json.loads(json.dumps(base)); mutate(R); p = d / (name.replace(" ", "_")[:40] + ".json"); p.write_text(json.dumps(R)); rows.append((name, "record altered", build(p, stmt, D)))
variant("verification booleans set true, everything else genuine but pulse output replaced", lambda R: (R.__setitem__("seed_hex", "e" * 128), R["pulse"].__setitem__("outputValue", "E" * 128), R.__setitem__("pulse_verification", {"certificate_id_matches_sha512_of_der": True, "output_is_sha512_of_message_plus_signature": True, "status_code_zero": True, "precommitment_chain_to_next_pulse": True, "all": True})))
variant("certificate_pem replaced by another self-signed certificate (digest updated)", lambda R: (R.__setitem__("certificate_pem", ts.test_certificate.__wrapped__()[0].decode() if hasattr(ts.test_certificate, "__wrapped__") else __import__("cryptography").x509.CertificateBuilder and R["certificate_pem"].replace("A", "B", 1)), R.__setitem__("certificate_pem_sha256", hashlib.sha256(R["certificate_pem"].encode()).hexdigest())))
def _selfsigned(R):
    cert = ts.test_certificate(signed_by_root=False); tp = fb.parse_utc(R["T_pulse"]); nb, npem = ts.make_nist(tp, cert=cert); np_ = json.loads(nb)["pulse"]
    R["pulse"] = np_; R["seed_hex"] = np_["outputValue"].lower(); R["body"] = nb.decode(); R["body_sha256"] = hashlib.sha256(nb).hexdigest(); R["certificate_pem"] = npem.decode(); R["certificate_pem_sha256"] = hashlib.sha256(npem).hexdigest()
variant("self-signed certificate + pulse signed under it (everything internally consistent)", _selfsigned)
variant("body replaced by a body whose pulse differs from record.pulse (digest updated)", lambda R: (R.__setitem__("body", json.dumps({"pulse": dict(R["pulse"], statusCode=1)})), R.__setitem__("body_sha256", hashlib.sha256(R["body"].encode()).hexdigest())))
variant("signatureValue altered in both record.pulse and body (digests updated)", lambda R: (R["pulse"].__setitem__("signatureValue", "AB" * 256), R.__setitem__("body", json.dumps({"pulse": R["pulse"]})), R.__setitem__("body_sha256", hashlib.sha256(R["body"].encode()).hexdigest())))
variant("pulse timeStamp moved one minute (in record and body)", lambda R: (R["pulse"].__setitem__("timeStamp", (fb.parse_utc(R["T_pulse"]) + timedelta(minutes=1)).strftime("%Y-%m-%dT%H:%M:%S.000Z")), R.__setitem__("body", json.dumps({"pulse": R["pulse"]})), R.__setitem__("body_sha256", hashlib.sha256(R["body"].encode()).hexdigest())))
variant("rule_sha256 in the record changed", lambda R: R.__setitem__("rule_sha256", "b" * 64))
variant("recorded precommitment FLAG removed — irrelevant: the link is recomputed from the retained next pulse, so ACCEPTED is the correct outcome", lambda R: R["pulse_verification"].__setitem__("precommitment_chain_to_next_pulse", None))
# fetcher-level probes
d2 = Path(tempfile.mkdtemp()); out = d2 / "r.json"; st = d2 / "s.txt"; t_sign = (datetime.now(timezone.utc) - timedelta(hours=2)).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ"); tp = fb.pulse_time(fb.parse_utc(t_sign)); st.write_text(f"signed {'a'*64} at {t_sign}")
body, pem = ts.make_nist(tp, sign=False)
with mock.patch.object(fb, "fetch", side_effect=ts.nist_side(body, pem, tp=tp)): rc1 = fb.main(["--t-sign", t_sign, "--out", str(out), "--rule-sha256", "a" * 64, "--signature-statement", str(st)])
rows.append(("fetcher: pulse whose signature does not verify under the served certificate", f"fetch rc={rc1} ({json.loads(out.read_text()).get('verdict','')[:60]})", "no record produced" if rc1 != 0 else build(out, st, "a" * 64)))
t30 = (datetime.now(timezone.utc) - timedelta(hours=30)).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ"); st.write_text(f"signed {'a'*64} at {t30}"); rnd = fb.drand_round(fb.pulse_time(fb.parse_utc(t30)))
import urllib.error, urllib.parse
def one_relay(url, timeout=30):
    if "nist.gov" in url: raise urllib.error.HTTPError(url, 404, "Not Found", None, None)
    if "api.drand.sh" in url: return json.dumps({"round": rnd, "randomness": "f" * 64}).encode()
    raise OSError("relay down")
with mock.patch.object(fb, "fetch", side_effect=one_relay): rc2 = fb.main(["--t-sign", t30, "--out", str(out), "--rule-sha256", "a" * 64, "--signature-statement", str(st)])
rows.append(("fetcher: fallback with only ONE relay answering", f"fetch rc={rc2} ({json.loads(out.read_text()).get('verdict','')[:40]})", "no record produced" if rc2 != 0 else "ACCEPTED"))
variant("next_body altered so the precommitment link no longer holds (digest updated)", lambda R: (R.__setitem__("next_body", json.dumps({"pulse": dict(json.loads(R["next_body"])["pulse"], localRandomValue="99" * 64)})), R.__setitem__("next_body_sha256", hashlib.sha256(R["next_body"].encode()).hexdigest())))
# genuine drand path, then drand-record adversarial variants (the mocked source keeps answering as the genuine relays)
rc3, rec3, stmt3, D3, d3 = genuine("drand", hours=30); rows.append(("genuine drand fallback record (four relays agree)", f"fetch rc={rc3}", build(rec3, stmt3, D3)))
dbase = json.loads(rec3.read_text())
def dvariant(name, mutate):
    R = json.loads(json.dumps(dbase)); mutate(R); p = d3 / (name.replace(" ", "_")[:40] + ".json"); p.write_text(json.dumps(R)); rows.append((name, "drand record altered", build(p, stmt3, D3)))
def _invent_hosts(R):
    R["seed_hex"] = "e" * 64; R["pulse"]["randomness"] = "e" * 64; R["body"] = json.dumps(R["pulse"]); R["body_sha256"] = hashlib.sha256(R["body"].encode()).hexdigest()
    rr = {}
    for h in ("https://attacker-one.invalid/public/%d" % R["round"], "https://attacker-two.invalid/public/%d" % R["round"]):
        b = json.dumps({"round": R["round"], "randomness": "e" * 64}); rr[h] = {"ok": True, "body": b, "body_sha256": hashlib.sha256(b.encode()).hexdigest()}
    R["relay_responses"] = rr; R["relays_agreeing"] = list(rr); R["uri"] = list(rr)[0]
dvariant("drand: chosen seed with two invented relay hosts (all digests consistent)", _invent_hosts)
def _wrong_round_bodies(R):
    for u, r in R["relay_responses"].items():
        if r.get("ok"): b = json.dumps({"round": R["round"] + 1, "randomness": R["seed_hex"]}); r["body"] = b; r["body_sha256"] = hashlib.sha256(b.encode()).hexdigest()
dvariant("drand: retained relay bodies carry the wrong round (digests updated)", _wrong_round_bodies)
dvariant("drand: fetched_utc earlier than T_pulse + 24 h", lambda R: R.__setitem__("fetched_utc", R["T_pulse"]))
# VOID probe: a genuine drand record, but at build time NIST serves an authenticable T_pulse pulse
tpv = fb.pulse_time(fb.parse_utc(dbase["T_sign"])); CURRENT["side"] = ts.drand_side_with_authenticable_nist(dbase["round"], tpv, randomness=dbase["seed_hex"])
rows.append(("drand: genuine record, but NIST serves an authenticable pulse at build time", "primary authenticable now", build(rec3, stmt3, D3))); CURRENT["side"] = ts.drand_side(dbase["round"])
rec_out = {"utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "probes": [{"probe": a, "fetch": b, "builder": c} for a, b, c in rows],
           "files": {f: hashlib.sha256((HERE / f).read_bytes()).hexdigest() for f in ("fetch_beacon.py", "nist_signature.py", "test_support.py")} | {"build_corpus_identity.py": hashlib.sha256((HERE.parent / "corpus_identity" / "build_corpus_identity.py").read_bytes()).hexdigest()}}
(HERE / "negative_probes_receipt.json").write_text(json.dumps(rec_out, indent=1))
print("| probe | fetcher | builder outcome |\n|---|---|---|"); [print(f"| {a} | {b} | {c} |") for a, b, c in rows]
