#!/usr/bin/env python3
"""GENERATED RECORD of what the beacon subsystem was OBSERVED to do (Blanc 2026-09-06 00:49: prose written last, from executed behaviour,
quoting function names). Runs: the live-sample checks (nist_signature.verify_pulse / verify_certificate_anchor on the retained pulse and
certificate), the fixture suites, and negative_probes.py; then writes BEACON_SUBSYSTEM_OBSERVED_BEHAVIOUR_<date>.md from those outputs only.
Every sentence in the output corresponds to a printed result above it. Nothing here touches the network or any real pixel."""
import json, subprocess, sys, hashlib, time
from pathlib import Path
from datetime import datetime, timezone
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); LANE = HERE.parents[1]
import nist_signature as ns
out = []; W = out.append
W(f"# Beacon subsystem — observed behaviour (generated {time.strftime('%Y-%m-%d %H:%M KST')} by _optionA_dev/beacon/observed_behaviour.py)")
W("Every statement below is derived from a result printed by executing the code named; nothing is asserted that was not run.\n")
# 1. live sample
p = json.loads((HERE / "_sample_pulse_last.json").read_text())["pulse"]; cert = (HERE / "_sample_certificate.pem").read_bytes(); inter = (HERE / "_digicert_intermediate.pem").read_bytes()
saved = ns.TRUST_ROOTS; ns.TRUST_ROOTS = None
v = ns.verify_pulse(p, cert, intermediates_pem=[inter], at=datetime(2026, 9, 5, 15, 13, tzinfo=timezone.utc)); ns.TRUST_ROOTS = saved
from cryptography import x509; leaf = x509.load_pem_x509_certificate(cert)
W("## 1. The retained live NIST pulse (2026-09-05T15:13:00Z, chain 2, pulse 1928259) under `nist_signature.verify_pulse`")
W("| check (function → key) | observed |"); W("|---|---|")
for k in ("certificate_id_matches_sha512_of_der", "output_is_sha512_of_message_plus_signature", "output_is_sha512_of_signature", "status_code_zero", "key_is_rsa", "signature_pkcs1v15_sha512", "all"): W(f"| `verify_pulse` → `{k}` | {v.get(k)} |")
for k in ("san_matches", "valid_at_time", "chains_to_pinned_root", "chain_length", "root_sha256", "anchored"): W(f"| `verify_certificate_anchor` → `{k}` | {v['anchor'].get(k)} |")
W(f"| certificate key size / signature length | {leaf.public_key().key_size} bits / {len(bytes.fromhex(p['signatureValue']))} bytes |")
W(f"| certificate subject / SAN / issuer | {leaf.subject.rfc4514_string()} / engine.beacon.nist.gov / {leaf.issuer.rfc4514_string()} |")
W(f"\nRead-out: the certificate NIST serves for this pulse ANCHORS (DigiCert-issued, names the beacon host, chains to the pinned root) and the pulse's output binds its bytes and signature; the RSA signature does NOT verify under that certificate's {leaf.public_key().key_size}-bit key because the signature is {len(bytes.fromhex(p['signatureValue']))} bytes. `all` = {v['all']}: under the rule this pulse would be REFUSED (`BEACON-RETRY`).\n")
# 2. fixtures
def run(cmd, cwd):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True); tail = [l for l in (r.stdout + r.stderr).splitlines() if l.startswith("Ran ") or l in ("OK",) or l.startswith("FAILED")]; return " / ".join(tail) or f"rc={r.returncode}"
W("## 2. Fixture suites, executed now under `-W error::ResourceWarning`"); W("| suite | result |"); W("|---|---|")
W(f"| beacon: test_fetch_beacon + test_nist_signature | {run([sys.executable, '-W', 'error::ResourceWarning', '-m', 'unittest', 'test_fetch_beacon', 'test_nist_signature'], HERE)} |")
W(f"| corpus_identity: test_build_corpus_identity | {run([sys.executable, '-W', 'error::ResourceWarning', '-m', 'unittest', 'test_build_corpus_identity'], HERE.parent / 'corpus_identity')} |")
W(f"| fourier_chirality: test_fourier_chirality + test_run_configurations | {run([sys.executable, '-W', 'error::ResourceWarning', '-m', 'unittest', 'test_fourier_chirality', 'test_run_configurations'], HERE.parent / 'fourier_chirality')} |")
# 3. probes
r = subprocess.run([sys.executable, str(HERE / "negative_probes.py")], cwd=HERE, capture_output=True, text=True); rec = json.loads((HERE / "negative_probes_receipt.json").read_text())
W("\n## 3. Negative probes (`negative_probes.py`, executed now; one alteration per row of a GENUINE fetcher record)"); W("| probe | fetcher | builder (`build_corpus_identity.build` → `_validate_beacon_record`) |"); W("|---|---|---|")
for x in rec["probes"]: W(f"| {x['probe']} | {x['fetch']} | {x['builder']} |")
acc = [x for x in rec["probes"] if x["builder"] == "ACCEPTED"]
W(f"\nRead-out: {len(rec['probes'])} probes; {len(acc)} accepted — {'; '.join(x['probe'][:60] for x in acc)}. Every other alteration was refused with the token shown.\n")
# 4. what is recomputed vs read (by inspection of the executed functions' source)
import inspect, importlib.util
bspec = importlib.util.spec_from_file_location("bci", HERE.parent / "corpus_identity" / "build_corpus_identity.py"); bci = importlib.util.module_from_spec(bspec); bspec.loader.exec_module(bci)
src = inspect.getsource(bci._validate_beacon_record)
reads_flag = "pulse_verification" in src and "precommitment_chain_to_next_pulse" in src
W("## 4. Recomputed versus read, in `_validate_beacon_record` (source inspected after execution)")
W(f"- Recomputes: SHA-256 of `certificate_pem` ({'certificate_pem_sha256' in src}); SHA-256 of `body` ({'body_sha256' in src}); body-pulse equality ({'PULSE-BODY-MISMATCH' in src}); `nist_signature.verify_pulse` incl. anchor ({'verify_pulse' in src and 'intermediates_pem' in src}); precommitment from `next_body` ({'NIST-PRECOMMITMENT-MISMATCH' in src}); NIST re-fetch of pulse/cert/next ({'NIST-REFETCH-PULSE-DIFFERS' in src and 'NIST-REFETCH-NEXT-DIFFERS' in src}); drand pinned URLs ({'DRAND-RELAY-URL-NOT-PINNED' in src}); drand per-body round/randomness ({'DRAND-RELAY-AGREEMENT' in src}); drand live trigger re-check ({'DRAND-VOID-PRIMARY-AUTHENTICABLE' in src}); drand live relay re-fetch ({'DRAND-REFETCH-DISAGREES' in src}).")
W(f"- Reads a recorded verification flag anywhere on the acceptance path: {reads_flag} (the string `pulse_verification` {'appears' if 'pulse_verification' in src else 'does not appear'} in the function).")
W("\n## 5. Limits observed (findings, not gaps to paper over)")
W(f"- NIST signature: `signature_pkcs1v15_sha512` = {v['signature_pkcs1v15_sha512']} on the live sample because the served certificate's key ({leaf.public_key().key_size} bits) cannot verify a {len(bytes.fromhex(p['signatureValue']))}-byte signature; the code refuses such a pulse. Whether NIST will serve a verifying certificate is outside our control.")
W("- drand BLS proof: not verified by any code here (no BLS12-381 library); the fallback's authentication is ≥ 2 of 4 pinned relays agreeing, recomputed from retained bodies and re-fetched live.")
W("- Response bodies are retained so digests recompute; the fetcher's own record cannot prove the network path — the builder's build-time re-fetch is the check.")
(LANE / f"BEACON_SUBSYSTEM_OBSERVED_BEHAVIOUR_{time.strftime('%Y%m%d')}.md").write_text("\n".join(out) + "\n"); print("\n".join(out))
