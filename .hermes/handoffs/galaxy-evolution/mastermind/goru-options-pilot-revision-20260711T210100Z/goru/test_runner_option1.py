import os
import subprocess
import json
import http.server
import socketserver
import threading
import urllib.parse
import hashlib
import time
from datetime import datetime

ALLOWED_FIXTURES = [
    "fx_composer_idle.html", "fx_composer_dr_active.html", "fx_plan_ready.html",
    "fx_running.html", "fx_ack_no_control.html", "fx_complete_ok.html",
    "fx_complete_marker_missing.html", "fx_complete_marker_dup.html",
    "fx_verification_wall.html", "fx_billing_upsell.html", "fx_login_wall.html",
    "fx_stale_dom.html"
]

class MockHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/get_state":
            qs = urllib.parse.parse_qs(parsed.query)
            fixture_path = qs.get('fixture', [''])[0]
            canonical = os.path.realpath(fixture_path)
            
            root_dir = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/goru-options-pilot-20260711T102412Z"
            fixtures_dir = os.path.realpath(os.path.join(root_dir, "tests/fixtures"))
            
            if os.path.dirname(canonical) != fixtures_dir:
                self.send_response(403)
                self.end_headers()
                return
                
            if os.path.basename(canonical) not in ALLOWED_FIXTURES:
                self.send_response(403)
                self.end_headers()
                return

            if not os.path.exists(canonical):
                self.send_response(404)
                self.end_headers()
                return
                
            with open(canonical, 'rb') as f:
                content = f.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_response(404)
            self.end_headers()

def main():
    httpd = socketserver.TCPServer(("127.0.0.1", 0), MockHandler)
    port = httpd.server_address[1]
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    
    os.environ["MOCK_BASE_URL"] = f"http://127.0.0.1:{port}"
    print(f"Mock server running on {os.environ['MOCK_BASE_URL']}")
    
    root_dir = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/goru-options-pilot-20260711T102412Z"
    fixtures_dir = os.path.join(root_dir, "tests/fixtures")
    results_dir = os.path.join(root_dir, "tests/results/OPTION-1")
    
    with open(os.path.join(fixtures_dir, "EXPECTED_VERDICTS.json")) as f:
        expected_json = json.load(f)
        expected = expected_json["fixtures"]
        marker_string = expected_json["marker_string"]
        
    with open(os.path.join(fixtures_dir, "targets.json")) as f:
        targets = json.load(f)["targets"]
        
    verdicts = {}
    
    def run_shim(fixture_name, target, out_dir):
        fixture_path = os.path.join(fixtures_dir, fixture_name)
        subprocess.run(["python3", os.path.join(root_dir, "goru/option1_shim.py"), "--dry-run", "--fixture", fixture_path, "--target", target, "--out", out_dir], check=True, timeout=300)
        with open(os.path.join(out_dir, "verdict.json")) as f:
            return json.load(f)

    # T1
    print("Running T1...")
    start_t1 = time.time()
    t1_pass = True
    for fix, exp in expected.items():
        out = os.path.join(results_dir, "T1", fix.replace('.html', ''))
        res = run_shim(fix, "conv-alpha", out)
        if res["state"] != exp["state"]: t1_pass = False
        if not set(exp["required_actions"]).issubset(set(res["planned_actions"])): t1_pass = False
        if not set(res["planned_actions"]).issubset(set(exp["allowed_actions"])): t1_pass = False
    verdicts["T1"] = "PASS" if t1_pass else "FAIL"
    dur_t1 = time.time() - start_t1

    # T2
    print("Running T2...")
    start_t2 = time.time()
    t2_pass = True
    t2_count = 0
    for t in targets:
        for i in range(3):
            out = os.path.join(results_dir, "T2", f"{t['conversation_id']}_{i}")
            res = run_shim(t['fixture'], t['conversation_id'], out)
            if res["target_id"] != t['conversation_id']: t2_pass = False
            t2_count += 1
    if t2_count != 9: t2_pass = False
    verdicts["T2"] = "PASS" if t2_pass else "FAIL"
    dur_t2 = time.time() - start_t2
    
    # T3
    print("Running T3...")
    start_t3 = time.time()
    t3_pass = True
    walls = ["fx_verification_wall.html", "fx_billing_upsell.html", "fx_login_wall.html"]
    for w in walls:
        out = os.path.join(results_dir, "T3", w.replace('.html', ''))
        res = run_shim(w, "conv-alpha", out)
        if res["planned_actions"] != ["HARD_STOP"]: t3_pass = False
        if res["state"] != expected[w]["state"]: t3_pass = False
    verdicts["T3"] = "PASS" if t3_pass else "FAIL"
    dur_t3 = time.time() - start_t3
    
    # T4
    print("Running T4...")
    start_t4 = time.time()
    t4_pass = True
    caps = ["fx_complete_ok.html", "fx_complete_marker_missing.html", "fx_complete_marker_dup.html"]
    hashes = []
    for c in caps:
        c_hashes = []
        for i in range(2):
            out = os.path.join(results_dir, "T4", f"{c.replace('.html', '')}_{i}")
            res = run_shim(c, "conv-alpha", out)
            body_path = os.path.join(out, res["extracted_body"])
            with open(body_path, "rb") as bf:
                b = bf.read()
                h = hashlib.sha256(b).hexdigest()
                c_hashes.append(h)
                hashes.append(h)
            
            text_lines = b.decode('utf-8').strip().split('\n')
            text_lines = [l for l in text_lines if l.strip()]
            actual_count = sum(1 for l in text_lines if l == marker_string)
            final_line_is_marker = (len(text_lines) > 0 and text_lines[-1] == marker_string)
            
            exp_cap = expected[c]["capture"]
            if actual_count != exp_cap["marker_count"]:
                t4_pass = False
            if final_line_is_marker != exp_cap["marker_is_final_nonblank_line"]:
                t4_pass = False
                
        if c_hashes[0] != c_hashes[1]: t4_pass = False
    
    if len(set(hashes)) != len(caps): t4_pass = False
    verdicts["T4"] = "PASS" if t4_pass else "FAIL"
    dur_t4 = time.time() - start_t4

    # T5
    print("Running T5...")
    start_t5 = time.time()
    out1 = os.path.join(results_dir, "T5", "run1")
    res1 = run_shim("fx_plan_ready.html", "conv-t5", out1)
    out2 = os.path.join(results_dir, "T5", "run2")
    res2 = run_shim("fx_plan_ready.html", "conv-t5", out2)
    t5_pass = True
    
    if res2["planned_actions"] != ["HARD_STOP"]: t5_pass = False
    if res2["state"] != "UNKNOWN": t5_pass = False
    
    # Negative guard tests
    guard_results = {}
    bad_urls = [
        "http://localhost:9",
        "http://127.0.0.1:80@localhost:9"
    ]
    
    for bad_url in bad_urls:
        env = os.environ.copy()
        env["MOCK_BASE_URL"] = bad_url
        fixture_path = os.path.join(fixtures_dir, "fx_composer_idle.html")
        out_dir = os.path.join(results_dir, "T5", "guard")
        try:
            # timeout=10 and require nonzero exit
            subprocess.run(
                ["python3", os.path.join(root_dir, "goru/option1_shim.py"), "--dry-run", "--fixture", fixture_path, "--target", "conv-t5", "--out", out_dir],
                check=True, timeout=10, env=env
            )
            # If we succeed, the guard failed
            guard_results[bad_url] = "FAIL (shim accepted bad URL)"
            t5_pass = False
        except subprocess.CalledProcessError:
            # Nonzero exit means guard successfully rejected the bad URL
            guard_results[bad_url] = "PASS (rejected as expected)"
        except subprocess.TimeoutExpired:
            guard_results[bad_url] = "FAIL (timeout, did not exit cleanly)"
            t5_pass = False

    os.makedirs(os.path.join(results_dir, "T5"), exist_ok=True)
    summary_path = os.path.join(results_dir, "T5", "summary.json")
    with open(summary_path, "w") as f:
        json.dump({
            "configured_subprocess_timeout": 300,
            "guard_results": guard_results
        }, f, indent=2)

    dur_t5 = time.time() - start_t5
    
    import glob
    receipt_path = os.path.join(results_dir, "RECEIPT.md")
    total_bytes = 0
    files = glob.glob(os.path.join(results_dir, "**/*"), recursive=True) + [os.path.join(root_dir, "goru/option1_shim.py"), __file__]
    for path in files:
        if os.path.isfile(path) and path != receipt_path:
            total_bytes += os.path.getsize(path)
            
    bound_status = "PASS"
    if total_bytes > 20 * 1024 * 1024:
        print("FAIL: Total bytes exceed 20MB bound limit.")
        t5_pass = False
        bound_status = "FAIL (exceeds 20MB)"
        
    verdicts["T5"] = "PASS" if t5_pass else "FAIL"
    print(json.dumps(verdicts, indent=2))
    
    with open(receipt_path, "w") as f:
        f.write("# RECEIPT OPTION-1\n")
        f.write("Network: 127.0.0.1 loopback only; zero external network\n")
        f.write(f"Durations: T1={dur_t1:.2f}s, T2={dur_t2:.2f}s, T3={dur_t3:.2f}s, T4={dur_t4:.2f}s, T5={dur_t5:.2f}s\n")
        f.write(f"Total Bytes: {total_bytes} (Limit 20MB)\n")
        f.write(f"Bound Status: {bound_status}\n")
        
        for path in files:
            if os.path.isfile(path) and path != receipt_path:
                sz = os.path.getsize(path)
                with open(path, "rb") as pf:
                    h = hashlib.sha256(pf.read()).hexdigest()
                f.write(f"{h} {sz} {path}\n")
                
    ledger = os.path.join(root_dir, "WAVE_LEDGER.md")
    dt = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(ledger, "a") as f:
        for t, v in verdicts.items():
            f.write(f"| {dt} | {t} | OPTION-1 | tests/results/OPTION-1/{t}/ | — | {v} |\n")
        with open(receipt_path, "rb") as rf:
            rb = rf.read()
            rh = hashlib.sha256(rb).hexdigest()
        f.write(f"| {dt} | RECEIPT | OPTION-1 | tests/results/OPTION-1/RECEIPT.md | {rh} | 127.0.0.1 loopback only; {total_bytes} bytes; Bound={bound_status} |\n")
        
    print(f"Receipt Hash: {rh}")
    print(f"Receipt Bytes: {len(rb)}")
    print(f"Total Output Bytes: {total_bytes}")
    
if __name__ == "__main__":
    main()
