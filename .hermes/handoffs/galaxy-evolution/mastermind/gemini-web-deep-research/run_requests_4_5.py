#!/usr/bin/env python3
import subprocess
import time
from pathlib import Path
import sys

REQUESTS = [
    ("REQ_004_P1_LEGACY_OVERCLAIMS_PROMPT.md", "REQ_004_P1_LEGACY_OVERCLAIMS_OUTPUT.md"),
    ("REQ_005_P3_PRIMACY_RECAST_PROMPT.md", "REQ_005_P3_PRIMACY_RECAST_OUTPUT.md")
]

BASE_DIR = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-deep-research")
REQUESTS_DIR = BASE_DIR / "requests"
OUTPUTS_DIR = BASE_DIR / "outputs"
CAPTURE_SCRIPT = BASE_DIR / "capture_current.py"

def run_apple_script(script: str):
    subprocess.run(["osascript", "-e", script], check=True)

def copy_to_clipboard(text: str):
    subprocess.run("pbcopy", universal_newlines=True, input=text, check=True)

for prompt_file, output_file in REQUESTS:
    prompt_path = REQUESTS_DIR / prompt_file
    output_path = OUTPUTS_DIR / output_file
    
    if output_path.exists():
        print(f"Skipping {prompt_file}, output already exists.")
        continue
        
    print(f"--- Processing {prompt_file} ---")
    prompt_content = prompt_path.read_text(encoding="utf-8")
    copy_to_clipboard(prompt_content)
    
    # Open tab and paste
    run_apple_script('tell application "Google Chrome" to activate')
    run_apple_script('tell application "Google Chrome" to tell window 1 to make new tab with properties {URL:"https://gemini.google.com/app"}')
    time.sleep(5)
    run_apple_script('tell application "System Events" to keystroke "v" using {command down}')
    time.sleep(1)
    run_apple_script('tell application "System Events" to key code 36')
    
    # Wait for capture
    print("Waiting for generation...")
    subprocess.run(["python3", str(CAPTURE_SCRIPT), str(output_path)], check=True)
    print(f"Completed {prompt_file}\n")
    time.sleep(2)
