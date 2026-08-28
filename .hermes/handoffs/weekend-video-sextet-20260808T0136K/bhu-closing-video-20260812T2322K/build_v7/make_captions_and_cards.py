#!/usr/bin/env python3
"""Generate exact sentence captions and per-card WAV extracts from the V7 audio receipt."""
from pathlib import Path
import json
import subprocess

BUILD=Path(__file__).resolve().parent
T=json.loads((BUILD/'audio/timeline.json').read_text())


def stamp(t):
    ms=round(t*1000); h,ms=divmod(ms,3600000); m,ms=divmod(ms,60000); s,ms=divmod(ms,1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

srt=[]
for i,r in enumerate(T['records'],1):
    # Hold through the deterministic pause, but never overlap the next sentence.
    end=T['records'][i]['start_seconds'] if i<len(T['records']) else T['master_duration_seconds']
    srt += [str(i),f"{stamp(r['start_seconds'])} --> {stamp(end)}",r['text'],""]
(BUILD/'audio/narration_v7.srt').write_text("\n".join(srt))

cards=BUILD/'audio/cards'; cards.mkdir(exist_ok=True)
master=BUILD/'audio/narration_master.wav'
for c in T['cards']:
    out=cards/f"card-{c['card_id']}.wav"
    subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',str(master),'-ss',str(c['start_seconds']),'-to',str(c['speech_end_seconds']),'-c:a','pcm_s16le',str(out)],check=True)
print(json.dumps({'srt':str(BUILD/'audio/narration_v7.srt'),'captions':len(T['records']),'cards':len(T['cards'])}))
