import json
import urllib.request
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:19223"
TARGET_ID = "C92443095EE9116210C178D855DF3329"

with urllib.request.urlopen(f"{BASE}/json/list", timeout=3) as response:
    targets = json.load(response)
exact = [x for x in targets if x.get("id") == TARGET_ID and x.get("type") == "page"]
if len(exact) != 1:
    raise SystemExit(f"exact_target_count={len(exact)}")
parsed = urlparse(exact[0]["url"])
if parsed.scheme != "https" or parsed.netloc != "gemini.google.com" or not parsed.path.startswith("/app/"):
    raise SystemExit("target_drift")

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(BASE)
    pages = [pg for ctx in browser.contexts for pg in ctx.pages if pg.url == exact[0]["url"]]
    if len(pages) != 1:
        raise SystemExit(f"page_count={len(pages)}")
    page = pages[0]
    state = page.evaluate("""() => {
      const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};
      const label=e=>(e.getAttribute('aria-label')||e.getAttribute('title')||e.innerText||'').trim().replace(/\\s+/g,' ').slice(0,200);
      const dialogs=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(label);
      const challenge=location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||dialogs.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t));
      const controls=[...document.querySelectorAll('button,[role=button]')].filter(v).map(e=>({label:label(e),disabled:!!e.disabled})).filter(x=>/research|start|stop|cancel|good response|send|submit|retry|continue/i.test(x.label)).slice(0,40);
      const statusTexts=[...document.querySelectorAll('div,span,p')].filter(v).map(label).filter(x=>x&&x.length<220&&/researching|creating.*plan|research plan|start research|completed|sources/i.test(x)).slice(0,40);
      const messages=[...document.querySelectorAll('message-content')].filter(v).map(e=>({chars:(e.innerText||'').length,links:e.querySelectorAll('a[href]').length}));
      return {challenge,dialogs:dialogs.filter(x=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(x)),controls,statusTexts:[...new Set(statusTexts)],messages};
    }""")
    print(json.dumps({"target_id": TARGET_ID, "path": parsed.path, "state": state}, sort_keys=True))
