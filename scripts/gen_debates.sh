#!/bin/bash
cd /Users/duhokim/NebulaMind/NebulaMind/backend
source .venv/bin/activate
python3 -u /tmp/gen_debates.py >> /Users/duhokim/NebulaMind/logs/gen_debates.log 2>&1
