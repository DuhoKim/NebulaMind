import os
import hashlib
import json
import argparse
from bs4 import BeautifulSoup

STATE_MAP = {
    "billing-upsell": ("BILLING_WALL", ["HARD_STOP"]),
    "running": ("RUNNING", ["WAIT"]),
    "ack-no-control": ("ACK_NO_CONTROL", ["HARD_STOP"]),
    "login-wall": ("LOGIN_WALL", ["HARD_STOP"]),
    "stale-dom": ("STALE_DOM", ["RELOAD_SAME_TARGET"]),
    "composer-idle": ("COMPOSER_IDLE", ["SELECT_DEEP_RESEARCH"]),
    "verification-wall": ("VERIFICATION_WALL", ["HARD_STOP"]),
    "composer-dr-active": ("DR_ACTIVE", ["SUBMIT_PROMPT"]),
    "plan-ready": ("PLAN_READY", ["SNAPSHOT_PLAN", "START_RESEARCH"]),
    "complete-ok": ("COMPLETE", ["CAPTURE_BODY"]),
    "complete-marker-missing": ("MARKER_MISSING", ["CAPTURE_BODY"]),
    "complete-marker-dup": ("MARKER_DUPLICATE", ["CAPTURE_BODY"])
}

def parse_dom_fixture(html_path, target_id, expected_marker):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, "html.parser")
    body = soup.body
    test_id = body.get("data-testid") if body else None
    
    if test_id in STATE_MAP:
        state, actions = STATE_MAP[test_id]
    else:
        state, actions = "UNKNOWN", ["HARD_STOP"]

    verdict = {
        "state": state,
        "target_id": target_id,
        "planned_actions": actions,
        "marker_count": 0,
        "marker_is_final_nonblank_line": False,
        "extracted_body_sha256": None,
        "extracted_body_path": None
    }
    
    body_text = None
    if state in ["COMPLETE", "MARKER_MISSING", "MARKER_DUPLICATE"]:
        article = soup.find("article", class_="report-body")
        if article:
            # Join paragraphs with newline
            lines = [p.get_text() for p in article.find_all("p")]
            body_text = "\n".join(lines)
            
            verdict["extracted_body_sha256"] = hashlib.sha256(body_text.encode('utf-8')).hexdigest()
            verdict["marker_count"] = body_text.count(expected_marker)
            
            nonblank = [line.strip() for line in lines if line.strip()]
            if nonblank and nonblank[-1] == expected_marker:
                verdict["marker_is_final_nonblank_line"] = True
            
            if verdict["marker_count"] == 1 and verdict["marker_is_final_nonblank_line"]:
                verdict["verdict_class"] = "CAPTURED_OK"
            else:
                verdict["verdict_class"] = "VOID"
                
            # Stash body_text temporarily for main()
            verdict["_body_text"] = body_text
                
    return verdict

def _hash_and_size(path):
    with open(path, 'rb') as f:
        content = f.read()
    return {"sha256": hashlib.sha256(content).hexdigest(), "bytes": len(content)}

def write_capture_receipt(body_path):
    # This is retained for the old test backward compatibility if needed,
    # but the full receipt now handles verdict.json too in main()
    r = _hash_and_size(body_path)
    os.chmod(body_path, 0o444)
    return r

def save_body(body_text, out_path):
    if os.path.exists(out_path):
        raise Exception("File exists, overwrite refused.")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(body_text)

def live_capture_boundary():
    raise Exception("HELD: Live boundary invoked in dev lane.")

def main(argv=None):
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--dry-run", action="store_true", required=True)
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--marker", required=True)
    parser.add_argument("--out", required=True)
    
    args = parser.parse_args(argv)
    
    verdict = parse_dom_fixture(args.fixture, args.target, args.marker)
    body_text = verdict.pop("_body_text", None)
    
    # 1. Atomically create output dir before branching
    os.mkdir(args.out)
    verdict_path = os.path.join(args.out, "verdict.json")
    
    if verdict["state"] in ["COMPLETE", "MARKER_MISSING", "MARKER_DUPLICATE"] and body_text is not None:
        body_path = os.path.join(args.out, "body.md")
        receipt_path = os.path.join(args.out, "CAPTURE_RECEIPT.json")
        
        verdict["extracted_body_path"] = "body.md"
        
        with open(body_path, 'x', encoding='utf-8') as f:
            f.write(body_text)
            
        with open(verdict_path, 'x', encoding='utf-8') as f:
            json.dump(verdict, f, indent=2)
            
        receipt = {
            "schema": "NM_DEEP_RESEARCH_CAPTURE_RECEIPT_V1",
            "files": {
                "body.md": _hash_and_size(body_path),
                "verdict.json": _hash_and_size(verdict_path)
            }
        }
        
        with open(receipt_path, 'x', encoding='utf-8') as f:
            json.dump(receipt, f, indent=2)
            
        os.chmod(body_path, 0o444)
        os.chmod(verdict_path, 0o444)
        os.chmod(receipt_path, 0o444)
    else:
        # Non-capture states write ONLY verdict.json with exclusive create
        with open(verdict_path, 'x', encoding='utf-8') as f:
            json.dump(verdict, f, indent=2)
        os.chmod(verdict_path, 0o444)
        
    print(json.dumps(verdict))
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv[1:]))
