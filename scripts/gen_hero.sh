#!/bin/bash
cd /Users/duhokim/NebulaMind/NebulaMind/backend
source .venv/bin/activate
python3 -u /tmp/gen_hero.py >> /Users/duhokim/NebulaMind/logs/gen_hero.log 2>&1
