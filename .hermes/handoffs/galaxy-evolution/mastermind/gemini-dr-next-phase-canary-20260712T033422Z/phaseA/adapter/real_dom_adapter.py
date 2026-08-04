import json

SELECTORS = {
    "running_stop": "button[aria-label='Stop research'],button[aria-label='Stop response'],[data-test-id='stop-response-button'],[data-testid='running']",
    "verification": "iframe[src*='recaptcha' i],[data-sitekey],textarea[name='g-recaptcha-response'],[data-testid='verification-wall']",
    "billing_candidates": "dialog, button, a, [role='dialog'], [data-testid='billing-upsell']",
    "login": "input[type='password'],[data-testid='login-wall']",
    "composer": "[role='textbox'][aria-label='Enter a prompt for Gemini']",
    "pro_mode": "[data-test-id='bard-mode-menu-button'][aria-label^='Open mode picker, currently Pro']",
    "deep_research_active": "[aria-label='Deselect Deep research'],[data-test-id='deselect-drawer-item-gem-button']",
    "plan": "[data-test-id='research-steps'],[aria-label='More research plan details']",
    "start_control": "button[aria-label='Start research'],[data-test-id='confirm-button']",
    "complete": ".response-footer.complete,[data-test-id='gem-processing-card'].completed,[data-testid^='complete']",
    "answer_body": "#extended-response-markdown-content,.report-body",
    "links": "[data-test-id='browse-web-item-link']"
}

def build_js_probe():
    return f"""(function() {{
        var counts = {{}};
        
        var countMatches = function(sel) {{
            return document.querySelectorAll(sel).length;
        }};
        
        counts['composer'] = countMatches("{SELECTORS['composer']}");
        counts['pro_mode'] = countMatches("{SELECTORS['pro_mode']}");
        counts['deep_research_active'] = countMatches("{SELECTORS['deep_research_active']}");
        counts['plan'] = countMatches("{SELECTORS['plan']}");
        counts['start_control'] = countMatches("{SELECTORS['start_control']}");
        counts['running_stop'] = countMatches("{SELECTORS['running_stop']}");
        counts['complete'] = countMatches("{SELECTORS['complete']}");
        counts['answer_body'] = countMatches("{SELECTORS['answer_body']}");
        counts['links'] = countMatches("{SELECTORS['links']}");
        counts['verification_iframe'] = countMatches("{SELECTORS['verification']}");
        counts['login_node'] = countMatches("{SELECTORS['login']}");
        
        var billingNodes = Array.from(document.querySelectorAll("{SELECTORS['billing_candidates']}")).filter(function(e) {{
            var txt = (e.textContent || '').trim();
            return e.closest("[data-testid='billing-upsell']") !== null || (/^(Upgrade|Subscribe|Purchase|Buy)$/i.test(txt) && e.offsetParent !== null);
        }});
        counts['billing_upgrade'] = billingNodes.length;
        
        return JSON.stringify({{
            url: document.location.href,
            title: document.title,
            counts: counts
        }});
    }})();"""

def classify_signal(signal, expected_url=None):
    url = signal.get("url", "")
    counts = signal.get("counts", {})
    
    if expected_url and url != expected_url:
        return "TARGET_MISMATCH"
        
    if "/challenge" in url or "/sorry" in url:
        return "VERIFICATION_WALL"
        
    if "accounts.google.com" in url or "ServiceLogin" in url or counts.get("login_node", 0) > 0:
        return "LOGIN_WALL"
        
    if counts.get("verification_iframe", 0) > 0:
        return "VERIFICATION_WALL"
        
    if counts.get("billing_upgrade", 0) > 0:
        return "BILLING_WALL"
        
    if counts.get("running_stop", 0) > 0:
        return "RUNNING"
        
    if counts.get("complete", 0) > 0 and counts.get("answer_body", 0) > 0:
        return "COMPLETE"
        
    if counts.get("plan", 0) > 0 and counts.get("start_control", 0) > 0:
        return "PLAN_READY"
        
    if counts.get("composer", 0) > 0 and counts.get("pro_mode", 0) > 0 and counts.get("deep_research_active", 0) > 0:
        return "DR_ACTIVE"
        
    return "UNKNOWN"

def build_capture_js(expected_url, marker):
    expected_js = json.dumps(expected_url)
    marker_js = json.dumps(marker)
    return f"""(function() {{
        if (document.location.href !== {expected_js}) {{
            return "TARGET_MISMATCH";
        }}
        var bodyNode = document.querySelector("{SELECTORS['answer_body']}");
        var completeNode = document.querySelector("{SELECTORS['complete']}");
        
        if (!bodyNode || !completeNode) {{
            return "NOT_COMPLETE";
        }}
        
        var text = bodyNode.innerText;
        var hasMarker = text.includes({marker_js});
        var linksList = Array.from(document.querySelectorAll("{SELECTORS['links']}")).map(function(a) {{ return a.href; }});
        return JSON.stringify({{
            body: text,
            links: linksList,
            marker: hasMarker
        }});
    }})();"""
