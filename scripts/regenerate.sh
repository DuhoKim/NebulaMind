#!/bin/bash
cd /Users/duhokim/NebulaMind/NebulaMind/backend
source .venv/bin/activate
python3 -u /tmp/regenerate_pages.py > /Users/duhokim/NebulaMind/logs/regenerate.log 2>&1
