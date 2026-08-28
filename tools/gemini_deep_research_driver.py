#!/usr/bin/env python3
import subprocess
import time
import json
import sys

def run_applescript(script: str, args: list = None):
    cmd = ['osascript', '-']
    if args:
        cmd.extend(args)
    
    result = subprocess.run(cmd, input=script, text=True, capture_output=True)
    if result.returncode != 0:
        raise Exception(f"AppleScript Error: {result.stderr}")
    return result.stdout.strip()

def run_js_in_gemini(js_code: str):
    """Executes JS in the active Gemini tab and returns the result."""
    applescript = """
    on run argv
        set jsCode to item 1 of argv
        tell application "Google Chrome"
            set target to missing value
            repeat with w in windows
                repeat with t in tabs of w
                    if (URL of t) starts with "https://gemini.google.com/app" then
                        set target to t
                        exit repeat
                    end if
                end repeat
                if target is not missing value then exit repeat
            end repeat
            if target is missing value then
                return "ERROR_NO_TAB"
            end if
            return execute target javascript jsCode
        end tell
    end run
    """
    res = run_applescript(applescript, [js_code])
    if res == "ERROR_NO_TAB":
        raise Exception("Could not find a Gemini tab in Chrome.")
    return res

def is_deep_research_enabled():
    """Reads the DOM to check if the Deep Research toggle is active."""
    # TODO: We need the actual CSS selector for the Deep Research toggle.
    js_check = """
    (function() {
        const toggle = document.querySelector('button[aria-label*="Deep Research"]');
        if (!toggle) return false;
        return toggle.getAttribute('aria-checked') === 'true' || toggle.classList.contains('active');
    })();
    """
    result = run_js_in_gemini(js_check)
    return result.lower() == 'true'

def enable_deep_research():
    """Finds the Deep Research toggle and clicks it using native System Events or JS."""
    print("Enabling Deep Research...")
    
    # 1. Click 'Upload & tools'
    js_step1 = """
    (function() {
        let btn = document.querySelector("button[aria-label='Upload & tools']");
        if(btn) { btn.click(); return "OK"; }
        return "ERROR";
    })();
    """
    res = run_js_in_gemini(js_step1)
    if res == "ERROR":
        print("WARNING: Could not find 'Upload & tools' button!")
        return
        
    time.sleep(0.5)
    
    # 2. Click 'More tools'
    js_step2 = """
    (function() {
        let els = Array.from(document.querySelectorAll("div, span, button, li"));
        for (let el of els) {
            if (el.textContent && el.textContent.trim() === "More tools" && el.children.length === 0) {
                el.click();
                return "OK";
            }
        }
        return "ERROR";
    })();
    """
    run_js_in_gemini(js_step2)
    time.sleep(0.5)
    
    # 3. Click 'Deep research'
    js_step3 = """
    (function() {
        let els = Array.from(document.querySelectorAll("div, span, button, li"));
        for (let el of els) {
            if (el.textContent && el.textContent.trim() === "Deep research" && el.children.length === 0) {
                el.click();
                return "OK";
            }
        }
        return "ERROR";
    })();
    """
    run_js_in_gemini(js_step3)
    time.sleep(0.5)
    print("Deep Research activated via UI menu!")

def submit_prompt(prompt: str):
    """Uses System Events to natively paste and submit the prompt."""
    print("Injecting prompt via native Cmd+V paste...")
    
    # 1. Put prompt into clipboard securely using osascript (bypasses tmux pbcopy bugs)
    applescript_clipboard = """
    on run argv
        set the clipboard to (item 1 of argv)
    end run
    """
    run_applescript(applescript_clipboard, [prompt])
    
    # 1.5 Explicitly click the rich-textarea <p> element so Chrome focuses the composer
    js_focus = """
    (function() {
        let p = document.querySelector('rich-textarea p');
        if(p) { p.focus(); p.click(); return "OK"; }
        return "ERROR";
    })();
    """
    run_js_in_gemini(js_focus)
    time.sleep(1)
    
    # 2. Command+V and Return via AppleScript
    applescript_submit = """
    on run
        tell application "Google Chrome" to activate
        tell application "System Events"
            tell process "Google Chrome"
                set frontmost to true
                delay 1
                keystroke "v" using {command down}
                delay 1
                keystroke return
            end tell
        end tell
    end run
    """
    run_applescript(applescript_submit)

def wait_for_completion():
    """Polls the DOM until the Deep Research stream completes."""
    print("Waiting for response to complete (this may take a while for Deep Research)...")
    js_check_status = """
    (function() {
        // Look for the loading indicator or the stop generating button
        const isGenerating = document.querySelector('button[aria-label="Stop generating"]') !== null;
        return isGenerating.toString();
    })();
    """
    
    # Wait for generating to start
    time.sleep(3)
    
    # Poll until generating stops
    while True:
        is_gen = run_js_in_gemini(js_check_status)
        if is_gen.lower() != 'true':
            break
        print(".", end="", flush=True)
        time.sleep(5)
    
    print("\\nResponse completed!")

def extract_response():
    """Extracts the final markdown text from the DOM."""
    js_extract = """
    (function() {
        // Find the last message response block
        const responses = document.querySelectorAll('.message-content');
        if (responses.length === 0) return "";
        return responses[responses.length - 1].innerText;
    })();
    """
    return run_js_in_gemini(js_extract)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 gemini_deep_research_driver.py 'Your complex prompt here'")
        sys.exit(1)
        
    prompt = sys.argv[1]
    
    try:
        # 1. Ensure Deep Research is active
        if not is_deep_research_enabled():
            enable_deep_research()
        else:
            print("Deep Research is already enabled.")
            
        # 2. Submit the query
        submit_prompt(prompt)
        
        # 3. Wait for the generation
        wait_for_completion()
        
        # 4. Extract and print the final result
        result = extract_response()
        print("\\n=== FINAL RESULT ===\\n")
        print(result)
        
    except Exception as e:
        print(f"\\nFATAL ERROR: {e}")

if __name__ == "__main__":
    main()
