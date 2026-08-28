import re

with open("PREREG_SUCCESSOR_DRAFT_V25_20260827.md", "r") as f:
    text = f.read()

with open("GENERATED_TRACE.md", "r") as f:
    trace_text = f.read()

# Find Section 10
start_idx = text.find("## §10 Gate plan and repair trace")
end_idx = text.find("Next: both referee seats on this text", start_idx)

if start_idx != -1 and end_idx != -1:
    old_section_10 = text[start_idx:end_idx]
    
    new_section_10 = "## §10 Gate plan and repair trace\n\n" + trace_text + "\n\n"
    text = text.replace(old_section_10, new_section_10)
    
    with open("PREREG_SUCCESSOR_DRAFT_V25_20260827.md", "w") as f:
        f.write(text)
    print("Patched section 10")
else:
    print("Could not find section boundaries")
