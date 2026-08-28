#!/usr/bin/env python3
"""Extract encoded-output frame, audio, and caption QA artifacts."""
from __future__ import annotations
import json
import math
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

BUILD=Path(__file__).resolve().parent
VIDEO=Path('/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-narrated-20260813T0030K.mp4')
T=json.loads((BUILD/'audio/timeline.json').read_text())
OUT=BUILD/'final_qa'; FRAMES=OUT/'frames'; CARDS=OUT/'cards'
FRAMES.mkdir(parents=True,exist_ok=True); CARDS.mkdir(parents=True,exist_ok=True)
items=[]
for c in T['cards']:
    for tag,q in (('early',.2),('mid',.55),('late',.86)):
        t=c['start_seconds']+(c['end_seconds']-c['start_seconds'])*q
        p=FRAMES/f"card-{c['card_id']}-{tag}-{t:07.3f}.png"
        subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-ss',f'{t:.6f}','-i',str(VIDEO),'-frames:v','1','-vsync','0',str(p)],check=True)
        items.append((c['card_id']+' '+tag,t,p))
# Contact sheet is built only from frames decoded from the final MP4.
tw,th,lh,cols=640,360,36,3; rows=math.ceil(len(items)/cols)
sheet=Image.new('RGB',(cols*tw,rows*(th+lh)),(2,5,10)); d=ImageDraw.Draw(sheet); f=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',20,index=1)
for i,(label,t,p) in enumerate(items):
    x=(i%cols)*tw; y=(i//cols)*(th+lh); im=ImageOps.fit(Image.open(p).convert('RGB'),(tw,th),Image.Resampling.LANCZOS); sheet.paste(im,(x,y))
    text=f'{label} · {t:.2f}s'; b=d.textbbox((0,0),text,font=f); d.text((x+(tw-(b[2]-b[0]))/2,y+th+5),text,font=f,fill=(240,244,250))
sheet.save(OUT/'encoded-contact-sheet.jpg',quality=95,subsampling=0)
# Decode final AAC and split by exact card boundaries.
master=OUT/'encoded_audio.wav'
subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',str(VIDEO),'-map','0:a:0','-c:a','pcm_s16le','-ar','48000','-ac','1',str(master)],check=True)
for c in T['cards']:
    p=CARDS/f"card-{c['card_id']}.wav"
    subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',str(master),'-ss',str(c['start_seconds']),'-to',str(c['speech_end_seconds']),'-c:a','pcm_s16le',str(p)],check=True)
# Decode embedded subtitles to SRT.
subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',str(VIDEO),'-map','0:s:0',str(OUT/'encoded_captions.srt')],check=True)
print(json.dumps({'video':str(VIDEO),'contact_sheet':str(OUT/'encoded-contact-sheet.jpg'),'decoded_audio':str(master),'decoded_captions':str(OUT/'encoded_captions.srt'),'sampled_frames':len(items),'card_audio_segments':len(T['cards'])},indent=2))
