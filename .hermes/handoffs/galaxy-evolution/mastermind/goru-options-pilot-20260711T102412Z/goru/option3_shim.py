import argparse
import os
import sys
import json
from bs4 import BeautifulSoup

ALLOWED_FIXTURES = [
    "fx_composer_idle.html", "fx_composer_dr_active.html", "fx_plan_ready.html",
    "fx_running.html", "fx_ack_no_control.html", "fx_complete_ok.html",
    "fx_complete_marker_missing.html", "fx_complete_marker_dup.html",
    "fx_verification_wall.html", "fx_billing_upsell.html", "fx_login_wall.html",
    "fx_stale_dom.html"
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", required=True)
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    canonical = os.path.realpath(args.fixture)
    root_dir = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/goru-options-pilot-20260711T102412Z"
    fixtures_dir = os.path.realpath(os.path.join(root_dir, "tests/fixtures"))
    
    if os.path.dirname(canonical) != fixtures_dir:
        print("FAIL: Fixture must be in tests/fixtures/")
        sys.exit(1)
    if os.path.basename(canonical) not in ALLOWED_FIXTURES:
        print("FAIL: Fixture must be one of the pinned 12 files")
        sys.exit(1)
        
    canonical_out = os.path.realpath(args.out)
    results_dir = os.path.realpath(os.path.join(root_dir, "tests/results/OPTION-3"))
    if os.path.commonpath([results_dir, canonical_out]) != results_dir or results_dir == canonical_out:
        print("FAIL: Out dir must be a strict descendant of tests/results/OPTION-3")
        sys.exit(1)
        
    with open(canonical, "r") as f:
        html = f.read()
        
    soup = BeautifulSoup(html, "html.parser")
    
    state = "UNKNOWN"
    planned_actions = ["HARD_STOP"]
    extracted_body = None
    
    body = soup.find("body")
    if body and "data-testid" in body.attrs:
        testid = body["data-testid"]
        if testid == "composer-idle":
            state = "COMPOSER_IDLE"
            planned_actions = ["SELECT_DEEP_RESEARCH"]
        elif testid == "composer-dr-active":
            state = "DR_ACTIVE"
            planned_actions = ["SUBMIT_PROMPT"]
        elif testid == "plan-ready":
            state = "PLAN_READY"
            planned_actions = ["SNAPSHOT_PLAN", "START_RESEARCH"]
        elif testid == "running":
            state = "RUNNING"
            planned_actions = ["WAIT"]
        elif testid == "ack-no-control":
            state = "ACK_NO_CONTROL"
            planned_actions = ["HARD_STOP"]
        elif testid == "complete-ok":
            state = "COMPLETE"
            planned_actions = ["CAPTURE_BODY"]
            extracted_body = "body.txt"
        elif testid == "complete-marker-missing":
            state = "MARKER_MISSING"
            planned_actions = ["CAPTURE_BODY"]
            extracted_body = "body.txt"
        elif testid == "complete-marker-dup":
            state = "MARKER_DUPLICATE"
            planned_actions = ["CAPTURE_BODY"]
            extracted_body = "body.txt"
        elif testid == "verification-wall":
            state = "VERIFICATION_WALL"
            planned_actions = ["HARD_STOP"]
        elif testid == "billing-upsell":
            state = "BILLING_WALL"
            planned_actions = ["HARD_STOP"]
        elif testid == "login-wall":
            state = "LOGIN_WALL"
            planned_actions = ["HARD_STOP"]
        elif testid == "stale-dom":
            state = "STALE_DOM"
            planned_actions = ["RELOAD_SAME_TARGET"]

    session_file = os.path.join(os.path.dirname(canonical_out), "session_state.json")
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
                
    os.makedirs(canonical_out, exist_ok=True)
    
    if extracted_body:
        article = soup.find("article", class_="report-body")
        if article:
            content = article.get_text(separator="\n", strip=True)
        else:
            content = ""
            
        with open(os.path.join(canonical_out, extracted_body), "w") as f:
            f.write(content + "\n")

    verdict = {
        "option": "OPTION-3",
        "fixture": os.path.basename(args.fixture),
        "target_id": args.target,
        "state": state,
        "planned_actions": planned_actions,
        "extracted_body": extracted_body
    }
    
    with open(os.path.join(canonical_out, "verdict.json"), "w") as f:
        json.dump(verdict, f)

if __name__ == "__main__":
    main()
