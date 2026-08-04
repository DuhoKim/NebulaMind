import sys
import json
import time
import datetime
import hashlib
from pathlib import Path
import urllib.request

sys.path.append("broker")
from transport import UDSClient
import ledger

UDS_PATH = "/tmp/nmbrk-live-20260714/b.sock"
CDP_URL = "http://127.0.0.1:19223"
TARGET_ID = "C92443095EE9116210C178D855DF3329"

def verify_target():
    req = urllib.request.Request(f"{CDP_URL}/json/list")
    try:
        with urllib.request.urlopen(req) as resp:
            targets = json.loads(resp.read().decode())
    except Exception as e:
        print("Failed to fetch /json/list:", e)
        sys.exit(1)
        
    for t in targets:
        if t["id"] == TARGET_ID:
            if "gemini.google.com" not in t["url"]:
                print("Target drift! URL is", t["url"])
                sys.exit(1)
            return t
    print("Exact target ID not found")
    sys.exit(1)

def check_challenge(page, client):
    # A real page-content challenge, CAPTCHA, sign-in wall, 2FA, permission prompt, accounts redirect
    if "accounts.google.com" in page.url or "signin" in page.url.lower():
        client.op({"op": "freeze", "declared_by": "goru", "reason": "sign-in wall detected"})
        print("Sign-in wall detected, broker frozen.")
        sys.exit(1)
    if page.locator("text=Verify it's you").is_visible() or page.locator("text=reCAPTCHA").is_visible() or page.locator("text=Robot").is_visible():
        client.op({"op": "freeze", "declared_by": "goru", "reason": "challenge detected"})
        print("Challenge detected, broker frozen.")
        sys.exit(1)

def main():
    client = UDSClient(UDS_PATH)
    t = verify_target()
    
    resp = client.op({
        "op": "acquire",
        "holder": "goru",
        "kind": "target",
        "scope": {
            "host_id": "pro",
            "bundle": "com.google.Chrome",
            "user_data_dir": "dr-live-cdp-20260714",
            "window_id": "pid-65195",
            "target_id": TARGET_ID
        }
    })
    if not resp.get("ok"):
        print("Failed to acquire target lease:", resp)
        sys.exit(1)
    
    target_lease = resp["lease"]["lease_id"]
    target_epoch = resp["lease"]["epoch"]
    
    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        req_ver = urllib.request.Request(f"{CDP_URL}/json/version")
        with urllib.request.urlopen(req_ver) as resp_ver:
            ver_info = json.loads(resp_ver.read().decode())
            browser_ws = ver_info["webSocketDebuggerUrl"].replace(":9223", ":19223")
            
        browser = p.chromium.connect_over_cdp(browser_ws)
        
        page = None
        for ctx in browser.contexts:
            for pg in ctx.pages:
                if "gemini.google.com" in pg.url:
                    page = pg
                    break
            if page: break
            
        if not page:
            client.op({"op": "release", "lease_id": target_lease})
            print("Failed to find Gemini page in contexts.")
            sys.exit(1)
        
        try:
            check_challenge(page, client)
            
            client.op({"op": "check", "lease_id": target_lease, "epoch": target_epoch, "action": "check_page"})
            
            upload_tools = page.locator("[aria-label='Upload & tools']").first
            if not upload_tools.is_visible(timeout=5000):
                print("Upload & tools not visible")
                sys.exit(1)
                
            verify_target()
            check_challenge(page, client)
            client.op({"op": "check", "lease_id": target_lease, "epoch": target_epoch, "action": "click_upload_tools"})
            upload_tools.click()
            
            time.sleep(1)
            deep_research_opt = page.locator("text=Deep Research").first
            if not deep_research_opt.is_visible(timeout=5000):
                print("Deep Research option not visible or ambiguous")
                sys.exit(1)
                
            verify_target()
            check_challenge(page, client)
            client.op({"op": "check", "lease_id": target_lease, "epoch": target_epoch, "action": "click_deep_research"})
            deep_research_opt.click()
            
            time.sleep(1)
            
            if not page.locator("text=Deep Research").first.is_visible():
                print("UI does not indicate Deep Research mode.")
                sys.exit(1)
            
            prompt = "Using official Apple and Google Chrome documentation, explain in no more than eight bullets how a direct Thunderbolt Bridge between two Macs can support isolated browser automation. Include two limitations and source links."
            
            textbox = page.get_by_role("textbox", name="Enter a prompt for Gemini")
            if not textbox.is_visible():
                print("Textbox not visible.")
                sys.exit(1)
            
            verify_target()
            check_challenge(page, client)
            client.op({"op": "check", "lease_id": target_lease, "epoch": target_epoch, "action": "fill_prompt"})
            textbox.fill(prompt)
            
            sub_resp = client.op({
                "op": "acquire",
                "holder": "goru",
                "kind": "account-submission"
            })
            if not sub_resp.get("ok"):
                print("Failed to acquire account-submission lease:", sub_resp)
                sys.exit(1)
            sub_lease = sub_resp["lease"]["lease_id"]
            sub_epoch = sub_resp["lease"]["epoch"]
            
            try:
                verify_target()
                check_challenge(page, client)
                client.op({"op": "check", "lease_id": sub_lease, "epoch": sub_epoch, "action": "submit"})
                
                submit_btn = page.locator("[aria-label='Submit']").first
                if submit_btn.is_visible():
                    submit_btn.click()
                else:
                    textbox.press("Enter")
                    
                submit_utc = datetime.datetime.utcnow().isoformat() + "Z"
            finally:
                client.op({"op": "release", "lease_id": sub_lease})
            
            page.wait_for_url(lambda u: "/app/" in u and len(u.split("/")[-1]) > 5, timeout=10000)
            
            conv_url = page.url
            conv_id = conv_url.split("/")[-1]
            
            time.sleep(5)
            conv_title = page.title()
            
            print(f"Conversation ID: {conv_id}")
            print(f"Conversation Title: {conv_title}")
            print(f"Submit UTC: {submit_utc}")
            
            print("Waiting for completion...")
            completed = False
            for _ in range(60):
                client.op({"op": "heartbeat", "lease_id": target_lease})
                check_challenge(page, client)
                if page.locator("[aria-label='Good response']").first.is_visible():
                    completed = True
                    break
                time.sleep(10)
                
            if not completed:
                print("Timeout waiting for completion.")
                sys.exit(1)
                
            client.op({"op": "heartbeat", "lease_id": target_lease})
            
            result_text = page.locator("message-content").last.inner_text()
            
            receipt = {
                "conversation_id": conv_id,
                "conversation_title": conv_title,
                "submit_utc": submit_utc,
                "result_text": result_text,
                "url": conv_url
            }
            
            receipt_path = Path("receipts/GORU_DR_RESULT.json")
            receipt_path.write_text(json.dumps(receipt, indent=2))
            
            sha256 = hashlib.sha256(receipt_path.read_bytes()).hexdigest()
            
            ledger.append("ledger/RUN_LEDGER.jsonl", "goru", "result_save", {"receipt_file": "receipts/GORU_DR_RESULT.json", "sha256": sha256})
            
            ok, msg = ledger.verify("ledger/RUN_LEDGER.jsonl")
            if not ok:
                print("Ledger verification failed:", msg)
                sys.exit(1)
                
            print(f"Done! SHA-256: {sha256}")
            print("Ledger VERIFY_OK.")
            
        finally:
            client.op({"op": "release", "lease_id": target_lease})

if __name__ == "__main__":
    main()
