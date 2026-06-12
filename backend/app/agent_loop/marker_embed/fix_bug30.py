import re
file_path = "tasks.py"
with open(file_path, "r") as f:
    content = f.read()

# Fix the note logging
old_notes_bind = """:notes": stats.notes if not section_key else f"Section repair: {section_key}. " + stats.notes,"""
new_notes_bind = """:notes": stats.notes if not section_key else f"Section repair: {section_key}. " + (stats.notes or ''),"""
content = content.replace(old_notes_bind, new_notes_bind)

with open(file_path, "w") as f:
    f.write(content)
