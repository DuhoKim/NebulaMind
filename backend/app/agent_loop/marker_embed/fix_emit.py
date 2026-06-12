import re
file_path = "tasks.py"
with open(file_path, "r") as f:
    content = f.read()

content = content.replace("def claim_marker_embed_page(self, page_id: int) -> dict:", "def claim_marker_embed_page(self, page_id: int, section_key: str = None, expected_source_version: int = None) -> dict:")
with open(file_path, "w") as f:
    f.write(content)
print("Fixed claim_marker_embed_page bound method signature")
