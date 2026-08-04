import argparse
import os
import sys
import json
import re
import requests
import urllib.parse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", required=True)
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    base_url = os.environ.get("MOCK_BASE_URL")
    if not base_url:
        print("FAIL: MOCK_BASE_URL not set")
        sys.exit(1)
        
    parsed = urllib.parse.urlparse(base_url)
    if parsed.scheme != "http":
        print("FAIL: Base URL scheme must be http")
        sys.exit(1)
    if parsed.hostname != "127.0.0.1":
        print("FAIL: Base URL hostname must be 127.0.0.1")
        sys.exit(1)
    if not parsed.port:
        print("FAIL: Base URL must have an explicit port")
        sys.exit(1)
    if parsed.username or parsed.password:
        print("FAIL: Base URL must not have credentials")
        sys.exit(1)
    if parsed.query or parsed.fragment:
        print("FAIL: Base URL must not have query or fragment")
        sys.exit(1)
    if parsed.path not in ("", "/"):
        print("FAIL: Base URL path must be empty or /")
        sys.exit(1)

    url = f"{parsed.scheme}://{parsed.netloc}/get_state?fixture={urllib.parse.quote(args.fixture)}&target={urllib.parse.quote(args.target)}"
    
    session = requests.Session()
    session.trust_env = False
    
    try:
        resp = session.get(
            url,
            headers={"X-Synthetic-Auth": "DUMMY_1PSID_DO_NOT_USE"},
            timeout=5,
            allow_redirects=False
        )
        if resp.is_redirect or resp.status_code != 200:
            print(f"FAIL: Network error to loopback (redirect or non-200): {resp.status_code}")
            sys.exit(1)
        html = resp.text
    except Exception as e:
        print(f"FAIL: Network error to loopback: {e}")
        sys.exit(1)
        
    state = "UNKNOWN"
    planned_actions = ["HARD_STOP"]
    extracted_body = None

    if 'data-testid="composer-idle"' in html:
        state = "COMPOSER_IDLE"
        planned_actions = ["SELECT_DEEP_RESEARCH"]
    elif 'data-testid="composer-dr-active"' in html:
        state = "DR_ACTIVE"
        planned_actions = ["SUBMIT_PROMPT"]
    elif 'data-testid="plan-ready"' in html:
        state = "PLAN_READY"
        planned_actions = ["SNAPSHOT_PLAN", "START_RESEARCH"]
    elif 'data-testid="running"' in html:
        state = "RUNNING"
        planned_actions = ["WAIT"]
    elif 'data-testid="ack-no-control"' in html:
        state = "ACK_NO_CONTROL"
        planned_actions = ["HARD_STOP"]
    elif 'data-testid="complete-ok"' in html:
        state = "COMPLETE"
        planned_actions = ["CAPTURE_BODY"]
        extracted_body = "body.txt"
    elif 'data-testid="complete-marker-missing"' in html:
        state = "MARKER_MISSING"
        planned_actions = ["CAPTURE_BODY"]
        extracted_body = "body.txt"
    elif 'data-testid="complete-marker-dup"' in html:
        state = "MARKER_DUPLICATE"
        planned_actions = ["CAPTURE_BODY"]
        extracted_body = "body.txt"
    elif 'data-testid="verification-wall"' in html:
        state = "VERIFICATION_WALL"
        planned_actions = ["HARD_STOP"]
    elif 'data-testid="billing-upsell"' in html:
        state = "BILLING_WALL"
        planned_actions = ["HARD_STOP"]
    elif 'data-testid="login-wall"' in html:
        state = "LOGIN_WALL"
        planned_actions = ["HARD_STOP"]
    elif 'data-testid="stale-dom"' in html:
        state = "STALE_DOM"
        planned_actions = ["RELOAD_SAME_TARGET"]
    
    session_file = os.path.join(os.path.dirname(args.out), "session_state.json")
    os.makedirs(os.path.dirname(session_file), exist_ok=True)
    session_state = {}
    if os.path.exists(session_file):
        with open(session_file, "r") as f:
            session_state = json.load(f)
            
    if state == "PLAN_READY":
        if session_state.get(args.target) == "started":
            state = "UNKNOWN"
            planned_actions = ["HARD_STOP"]
        else:
            session_state[args.target] = "started"
            with open(session_file, "w") as f:
                json.dump(session_state, f)

    target_id = args.target
    
    os.makedirs(args.out, exist_ok=True)
    
    if extracted_body:
        m = re.search(r'<article class="report-body">(.*?)</article>', html, re.DOTALL)
        content = m.group(1).strip() if m else ""
        content = re.sub(r'<[^>]+>', '\n', content)
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        body_path = os.path.join(args.out, extracted_body)
        with open(body_path, "w") as f:
            f.write("\n".join(lines) + "\n")
            
    verdict = {
        "option": "OPTION-1",
        "fixture": os.path.basename(args.fixture),
        "target_id": target_id,
        "state": state,
        "planned_actions": planned_actions,
        "extracted_body": extracted_body
    }
    
    with open(os.path.join(args.out, "verdict.json"), "w") as f:
        json.dump(verdict, f)

if __name__ == "__main__":
    main()
