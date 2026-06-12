file_path = "pipeline.py"
with open(file_path, "r") as f:
    content = f.read()

import re

old_def = """def run_pipeline(
    page_id: int,
    content: str,
    claims: list[dict],
    source_version: Optional[int] = None,
    dry_run: bool = False,
    enable_topical_anchors: bool = False,
) -> tuple[Optional[str], RunStats]:"""

new_def = """def run_pipeline(
    page_id: int,
    content: str,
    claims: list[dict],
    source_version: Optional[int] = None,
    dry_run: bool = False,
    enable_topical_anchors: bool = False,
    section_key: Optional[str] = None
) -> tuple[Optional[str], RunStats]:"""

content = content.replace(old_def, new_def)
with open(file_path, "w") as f:
    f.write(content)
