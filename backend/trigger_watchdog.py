import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.agent_loop.tasks import sync_verbatim_markers_nightly

# Test the watchdog locally
sync_verbatim_markers_nightly(page_id=57)
