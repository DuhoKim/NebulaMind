#!/usr/bin/env python3
import json
import subprocess
import time
from pathlib import Path
import sys

JS_PATH = "/tmp/gemini_web_capture_state.js"
CONVERSATION_PREFIX = "https://gemini.google.com/app"

def capture_state() -> dict:
    script = f'''set jsCode to (read (POSIX file "{JS_PATH}") as «class utf8»)
tell application "Google Chrome"
  repeat with w in windows
    repeat with t in tabs of w
      if (URL of t) starts with "{CONVERSATION_PREFIX}" then return execute t javascript jsCode
    end repeat
  end repeat
  return "NO_CONVERSATION_TAB"
end tell'''
    cp = subprocess.run(["osascript", "-e", script], text=True, capture_output=True, timeout=30)
    if cp.returncode != 0:
        raise RuntimeError(cp.stderr.strip() or f"osascript exit {cp.returncode}")
    raw = cp.stdout.strip()
    if raw == "NO_CONVERSATION_TAB":
        raise RuntimeError(raw)
    return json.loads(raw)

def wait_and_capture(output_path: Path):
    print(f"Waiting for Gemini generation to finish... saving to {output_path.name}")
    deadline = time.time() + 1800 # 30 mins max wait
    while time.time() < deadline:
        try:
            state = capture_state()
            if not state.get("generating"):
                # Check if it has responses
                responses = state.get("responses", [])
                report = state.get("reportText", "").strip()
                if not report and responses:
                    report = responses[-1]
                
                if report and len(report) > 100:
                    text = report + ("\n" if not report.endswith("\n") else "")
                    output_path.write_text(text, encoding="utf-8")
                    print(f"SUCCESS: Captured {len(text)} bytes to {output_path}")
                    return True
        except Exception as e:
            print(f"Error capturing state: {e}")
        
        time.sleep(10)
    print("TIMEOUT")
    return False

if __name__ == "__main__":
    out_file = Path(sys.argv[1])
    out_file.parent.mkdir(parents=True, exist_ok=True)
    wait_and_capture(out_file)
