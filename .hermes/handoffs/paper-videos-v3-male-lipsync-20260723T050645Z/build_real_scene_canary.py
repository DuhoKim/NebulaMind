#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import random
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BASE = Path(__file__).resolve().parent
ISO_DIR = BASE / 'lipsync/isolated_512_michael_presenter_c'
NORM = BASE / 'lipsync/presenter_c_michael_isolated_512_cfr30.mp4'
STILL = BASE / 'lipsync/v3_real_scene_base.png'
MASK = BASE / 'lipsync/presenter_mask_430x560.png'
OUT = BASE / 'lipsync/NEBULAMIND_V3_PRESENTER_C_MICHAEL_REAL_SCENE_CANARY.mp4'
DRIVER = BASE / 'lipsync/michael_exact_excerpt_20_5s.wav'
SHEET = BASE / 'lipsync/V3_PRESENTER_C_MICHAEL_TEMPORAL_QA.png'
RECEIPT = BASE / 'lipsync/michael_presenter_c_canary_receipt.json'
W, H, FPS, DURATION = 2560, 1440, 30, 20.5
FONT_PATH = Path('/System/Library/Fonts/SFNSMono.ttf')
BG_TOP, BG_BOTTOM = '#07101F', '#0B1630'
CYAN, MAGENTA, GREEN, YELLOW = '#35D9F2', '#D95CFF', '#4EE09A', '#F2C14E'
BODY, MUTED, PANEL, OUTLINE = '#EAF2FF', '#91A4C4', '#101E39', '#29466E'


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def font(size: int):
    return ImageFont.truetype(str(FONT_PATH), size=size)


def rgb(v: str):
    v = v.lstrip('#')
    return tuple(int(v[i:i+2], 16) for i in (0, 2, 4))


def rgba(v: str, a: int = 255):
    return (*rgb(v), a)


def wrap(draw, text, fnt, width):
    lines, cur = [], ''
    for word in text.split():
        cand = word if not cur else f'{cur} {word}'
        if draw.textlength(cand, font=fnt) <= width:
            cur = cand
        else:
            if cur: lines.append(cur)
            cur = word
    if cur: lines.append(cur)
    return lines


def wrapped(draw, xy, text, fnt, fill, width, gap=10):
    x, y = xy
    box = draw.textbbox((0, 0), 'Ag', font=fnt)
    step = box[3] - box[1] + gap
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


def panel(draw, box, outline=OUTLINE, fill=PANEL, width=4, radius=30):
    draw.rounded_rectangle(box, radius=radius, fill=rgba(fill, 238), outline=outline, width=width)


def build_base() -> None:
    top, bottom = rgb(BG_TOP), rgb(BG_BOTTOM)
    im = Image.new('RGBA', (W, H), (*top, 255))
    d = ImageDraw.Draw(im)
    for y in range(H):
        t = y / (H - 1)
        c = tuple(round(top[i]*(1-t)+bottom[i]*t) for i in range(3))
        d.line((0, y, W, y), fill=c)
    rng = random.Random(20260723)
    for _ in range(150):
        x, y = rng.randrange(W), rng.randrange(H-160)
        r = rng.choice((1,1,2,2,3))
        d.ellipse((x-r,y-r,x+r,y+r), fill=rgb(rng.choice((CYAN,MAGENTA,BODY,MUTED))))
    glow = Image.new('RGBA', (W,H), (0,0,0,0)); g=ImageDraw.Draw(glow)
    g.ellipse((1500,-240,2950,1360), fill=rgba(CYAN,28))
    g.ellipse((-380,420,900,1760), fill=rgba(MAGENTA,18))
    im = Image.alpha_composite(im, glow.filter(ImageFilter.GaussianBlur(180)))
    d = ImageDraw.Draw(im)
    d.text((110,54),'NebulaMind',font=font(38),fill=BODY)
    d.text((420,60),'PAPER EXPLAINER · MALE PRESENTER V3 CANARY',font=font(25),fill=CYAN)
    d.text((2180,60),'LOCAL REVIEW',font=font(25),fill=MUTED)
    d.line((110,122,2450,122),fill=OUTLINE,width=2)
    d.text((110,166),'FROM CORE SAMPLE TO RESULT',font=font(26),fill=CYAN)
    d.text((110,225),'Five unlensed galaxies show a large shortfall',font=font(54),fill=BODY)

    x0, x1 = 110, 1640
    cards = [
        ('5 GALAXIES','core Pollock sample',CYAN),
        ('REDSHIFT 9.3–9.9','strictly unlensed field sample',MAGENTA),
        ('DIRECT TEMPERATURES','auroral-line oxygen abundance',GREEN),
    ]
    y = 365
    for value,label,accent in cards:
        panel(d,(x0,y,x1,y+190),outline=accent)
        d.text((x0+42,y+36),value,font=font(48),fill=BODY)
        wrapped(d,(x0+760,y+44),label,font(27),accent,690,gap=8)
        y += 218
    panel(d,(x0,1040,x1,1210),outline=YELLOW,fill='#0D1A31',width=3)
    d.text((x0+42,1073),'WHY THIS MATTERS',font=font(23),fill=YELLOW)
    wrapped(d,(x0+42,1120),'Direct measurements anchor the later comparison: about one fifth the nearby oxygen abundance.',font(31),BODY,1440,gap=10)

    panel(d,(1700,250,2485,1245),outline='#193653',fill='#07101F',width=2,radius=38)
    d.text((1760,350),'PRESENTER C · MICHAEL',font=font(32),fill=BODY)
    d.text((1760,405),'Local PCM · stable pace · 134.4 WPM',font=font(20),fill=CYAN)
    d.text((1760,450),'Exact-audio lip-sync · no generated dialogue',font=font(18),fill=MUTED)
    d.line((110,1285,2450,1285),fill=OUTLINE,width=2)
    d.text((110,1320),'FLAGSHIP · HAND-GUIDED',font=font(23),fill=MUTED)
    d.text((1850,1320),'V1/V2/site unchanged during review',font=font(21),fill=MUTED)
    im.convert('RGB').save(STILL, quality=95)


def build_mask() -> None:
    w,h=430,560
    mask=Image.new('L',(w,h),0); d=ImageDraw.Draw(mask)
    d.rounded_rectangle((24,10,w-24,h-10),radius=72,fill=248)
    mask=mask.filter(ImageFilter.GaussianBlur(30))
    px=mask.load()
    assert px is not None
    for y in range(h):
        bottom=max(0.0,min(1.0,(h-y)/95.0))
        for x in range(w):
            edge=min(1.0,x/50.0,(w-1-x)/50.0)
            px[x,y]=int(px[x,y]*bottom*edge)
    mask.save(MASK)


def latest_source() -> Path:
    files=sorted(ISO_DIR.glob('*.mp4'),key=lambda p:p.stat().st_mtime)
    if not files: raise RuntimeError(f'No SadTalker output in {ISO_DIR}')
    return files[-1]


def make_sheet() -> list[dict]:
    times=[0.6,2.2,4.0,6.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0]
    frames=[]; rows=[]
    frame_dir=BASE/'lipsync/qa_frames'; frame_dir.mkdir(parents=True,exist_ok=True)
    for i,t in enumerate(times):
        p=frame_dir/f'frame_{i:02d}_{t:04.1f}.png'
        run(['ffmpeg','-y','-v','error','-ss',str(t),'-i',str(OUT),'-frames:v','1',str(p)])
        im=Image.open(p).convert('RGB')
        full=im.resize((640,360),Image.Resampling.LANCZOS)
        crop=im.crop((1700,250,2485,1245)).resize((305,360),Image.Resampling.LANCZOS)
        tile=Image.new('RGB',(965,400),rgb(BG_TOP)); tile.paste(full,(0,40)); tile.paste(crop,(660,40))
        td=ImageDraw.Draw(tile); td.text((12,8),f'{t:04.1f}s · full layout + presenter closeup',font=font(18),fill=BODY)
        frames.append(tile); rows.append({'time_seconds':t,'frame':str(p)})
    sheet=Image.new('RGB',(965,400*len(frames)),rgb(BG_TOP))
    for i,tile in enumerate(frames): sheet.paste(tile,(0,i*400))
    sheet.save(SHEET,quality=92)
    return rows


def sha(path: Path): return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    source=latest_source(); build_base(); build_mask()
    run(['ffmpeg','-y','-v','error','-i',str(source),'-vf',f'fps={FPS},tpad=stop_mode=clone:stop_duration=0.2,trim=duration={DURATION},setpts=PTS-STARTPTS','-an','-frames:v',str(round(DURATION*FPS)),'-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-r',str(FPS),'-movflags','+faststart',str(NORM)])
    filt=(
        '[0:v]format=rgba[bg];'
        '[1:v]scale=430:560:force_original_aspect_ratio=increase,crop=430:560,fps=30,format=rgba[face];'
        '[2:v]format=gray,scale=430:560[mask];[face][mask]alphamerge[presenter];'
        '[bg][presenter]overlay=1980:610:format=auto[v];'
        '[3:a]apad,atrim=duration=20.5,loudnorm=I=-16:TP=-2:LRA=7[a]'
    )
    run(['ffmpeg','-y','-v','error','-loop','1','-i',str(STILL),'-i',str(NORM),'-loop','1','-i',str(MASK),'-i',str(DRIVER),'-filter_complex',filt,'-map','[v]','-map','[a]','-t',str(DURATION),'-frames:v',str(round(DURATION*FPS)),'-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-r',str(FPS),'-c:a','aac','-b:a','256k','-ar','48000','-movflags','+faststart',str(OUT)])
    run(['ffmpeg','-v','error','-xerror','-i',str(OUT),'-f','null','-'])
    rows=make_sheet()
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size:stream=codec_name,width,height,r_frame_rate,sample_rate,channels','-of','json',str(OUT)],text=True))
    receipt={'marker':'NEBULAMIND_V3_PRESENTER_C_MICHAEL_REAL_SCENE_CANARY_COMPLETE','identity_source':str(BASE/'identity/candidate_c_young_black_male.png'),'driver':str(DRIVER),'driver_sha256':sha(DRIVER),'sadtalker_source':str(source),'normalized_head':str(NORM),'final_canary':str(OUT),'final_sha256':sha(OUT),'temporal_sheet':str(SHEET),'sampled_frames':rows,'probe':probe,'facial_animation':'local SadTalker 512 crop mode, exact Michael driver, composited at 430x560','compositor':'Pillow + ffmpeg','fresh_generative_video_calls':'none','youtube_mutation':False,'website_mutation':False}
    RECEIPT.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__': main()
