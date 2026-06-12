import re
file_path = "injector.py"
with open(file_path, "r") as f:
    content = f.read()

# Remove the internal strip_markers call from inject_markers because pipeline.py already passed `clean_content`!
content = content.replace("    content = strip_markers(content)\n", "    # content = strip_markers(content) # Removed: caller handles stripping\n")

with open(file_path, "w") as f:
    f.write(content)
