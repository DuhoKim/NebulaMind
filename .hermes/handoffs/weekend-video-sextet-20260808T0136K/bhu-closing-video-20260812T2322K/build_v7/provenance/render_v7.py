#!/usr/bin/env python3
"""Render the exact V7 BHU explainer with deterministic Pillow diagrams.

The gated storyboard supplies every viewer-facing heading, narration string, and
support label. This renderer does not modify source bytes. Card 05 deliberately
contains no 95.4% position-bearing primitive on its mass axis.
"""
from __future__ import annotations
import functools
import hashlib
import json
import math
import platform
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Callable

import PIL
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
BUILD = Path(__file__).resolve().parent
STORY = ROOT / "STORYBOARD_DRAFT_V7.json"
NARR = ROOT / "NARRATION_DRAFT_V7.md"
TIMELINE = BUILD / "audio" / "timeline.json"
EXPECTED_STORY_SHA = "3077f0636385487bb4092d2032c18bbedaedb647780bbfc581e59027c87a8d2b"
EXPECTED_NARR_SHA = "3380497f0514e906db8463d0fdd2ffd1f0b02b37ac6825e3bfdec86011c2edc0"
W, H, FPS = 1920, 1080, 30
BG = (9, 14, 24); PANEL = (18, 29, 47); PANEL2 = (25, 40, 62); GRID = (54, 73, 99)
WHITE = (237, 242, 248); MUTED = (154, 168, 188); BLUE = (118, 182, 255); AMBER = (240, 179, 107)
RED = (217, 123, 123); GREEN = (121, 198, 163); CYAN = (89, 213, 220); PURPLE = (171, 135, 231)
FONT_PATH = "/System/Library/Fonts/Helvetica.ttc"
SERIF_PATH = "/System/Library/Fonts/Supplemental/STIXTwoText.ttf"
MONO_PATH = "/System/Library/Fonts/Menlo.ttc"
OUTPUT = BUILD / "bhu-closing-record-narrated-20260813T0030K-base.mp4"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@functools.lru_cache(maxsize=None)
def font(size: int, bold: bool = False, serif: bool = False, mono: bool = False):
    path = SERIF_PATH if serif else MONO_PATH if mono else FONT_PATH
    index = 1 if bold and path == FONT_PATH else 0
    return ImageFont.truetype(path, size, index=index)


def rounded(d, box, r=18, fill=PANEL, outline=GRID, width=2):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def wrap(d, text, box, size, color=WHITE, bold=False, align="center", max_lines=None, serif=False, mono=False):
    f = font(size, bold, serif, mono); words=text.split(); lines=[]; cur=""; width=box[2]-box[0]
    for w in words:
        trial=(cur+" "+w).strip()
        if d.textlength(trial,font=f)<=width: cur=trial
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    if max_lines and len(lines)>max_lines: raise RuntimeError(f"text exceeds {max_lines} lines: {text}")
    step=size+8; total=len(lines)*step-8; y=box[1]+max(0,(box[3]-box[1]-total)/2)
    for line in lines:
        tw=d.textlength(line,font=f); x=box[0] if align=="left" else box[2]-tw if align=="right" else box[0]+(width-tw)/2
        d.text((x,y),line,font=f,fill=color); y+=step
    return len(lines)


def center(d,text,xy,size,color=WHITE,bold=False,serif=False,mono=False):
    f=font(size,bold,serif,mono); b=d.textbbox((0,0),text,font=f); d.text((xy[0]-(b[2]-b[0])/2,xy[1]-(b[3]-b[1])/2),text,font=f,fill=color)


def arrow(d,a,b,color=CYAN,width=4,head=True):
    d.line((a[0],a[1],b[0],b[1]),fill=color,width=width)
    if head:
        ang=math.atan2(b[1]-a[1],b[0]-a[0]); L=16
        for q in (2.55,-2.55): d.line((b[0],b[1],b[0]+L*math.cos(ang+q),b[1]+L*math.sin(ang+q)),fill=color,width=width)


def badge(d,box,text,color,size=24):
    rounded(d,box,15,tuple(round(BG[i]*.84+color[i]*.16) for i in range(3)),color,2); center(d,text,((box[0]+box[2])/2,(box[1]+box[3])/2),size,color,True)


def galaxy(d,x,y,color,flip=1,scale=1.0):
    for i in range(260):
        th=i*.28; r=i*.48*scale; xx=x+flip*r*math.cos(th); yy=y+.48*r*math.sin(th)
        d.ellipse((xx-2,yy-2,xx+2,yy+2),fill=color)
    d.ellipse((x-9,y-9,x+9,y+9),fill=WHITE)


def mass_axis(d,y=650):
    x0,x1=260,1660; lo,hi=1.4,2.2
    d.line((x0,y,x1,y),fill=WHITE,width=4)
    def X(v): return x0+(v-lo)/(hi-lo)*(x1-x0)
    # Only ordinary axis ticks and source-supported values. No 95.4% position-bearing primitive.
    for v in (1.4,1.6,1.8,2.0,2.2):
        x=X(v); d.line((x,y-12,x,y+12),fill=MUTED,width=3); center(d,f"{v:.1f}",(x,y+48),24,MUTED,mono=True)
    center(d,"NEUTRON-STAR MASS (M☉)",((x0+x1)/2,y+92),25,MUTED,True,serif=True)
    return X


def card01(d,p):
    galaxy(d,305,470,BLUE,1,.55); badge(d,(105,650,555,715),"DUHO'S PERSONAL INTEREST",BLUE,23); wrap(d,"NOT PART OF THE LAB'S RESEARCH PROGRAMME",(115,725,545,805),24,WHITE,True,max_lines=2)
    rounded(d,(700,320,1120,565),25,PANEL2,CYAN,4); center(d,"PRIMARY SOURCES",(910,390),29,CYAN,True); wrap(d,"WE READ THE PRIMARY SOURCES",(750,430,1070,525),25,WHITE,True,max_lines=2)
    arrow(d,(1125,405),(1290,305),BLUE); arrow(d,(1125,485),(1290,650),AMBER)
    rounded(d,(1285,190,1815,435),24,PANEL,BLUE,4); wrap(d,"NEUTRON STARS\nA NUMBER TO CHECK",(1330,245,1770,390),31,BLUE,True,max_lines=3)
    rounded(d,(1235,510,1845,820),24,PANEL,AMBER,4); wrap(d,"GALAXY SPIN",(1300,545,1780,600),28,AMBER,True); wrap(d,"THE SOURCES GIVE NO EXPECTED SIZE FOR THE EFFECT",(1290,605,1790,690),24,WHITE,True,max_lines=2); wrap(d,"NOT IDENTIFYING BY ITSELF",(1300,710,1780,770),24,RED,True)
    badge(d,(630,835,1290,900),"ROUTE CLOSED · IDEA NOT DECLARED TRUE OR FALSE",RED,23)


def card02(d,p):
    badge(d,(100,315,390,385),"ONE LABEL",BLUE,27)
    labels=["CLOSED-UNIVERSE\nIDENTIFICATION","COLLAPSE\nBOUNCE","INHERITED\nROTATION","COSMOLOGICAL\nNATURAL SELECTION","OTHER BABY-\nUNIVERSE WORK"]
    boxes=[(560,235,930,405),(1010,235,1380,405),(1455,235,1825,405),(790,545,1160,715),(1260,545,1630,715)]
    colors=[BLUE,AMBER,PURPLE,GREEN,CYAN]
    # One label fans to five proposals; their short output arrows remain separate.
    for b in boxes: arrow(d,(395,350),(b[0]-12,(b[1]+b[3])//2),CYAN,3)
    for b,l,c in zip(boxes,labels,colors):
        rounded(d,b,22,PANEL2,c,3); wrap(d,l,(b[0]+25,b[1]+25,b[2]-25,b[3]-25),25,c,True,max_lines=3)
        arrow(d,(b[2]+8,(b[1]+b[3])//2),(min(W-55,b[2]+75),(b[1]+b[3])//2),c,3)
    badge(d,(550,810,1370,880),"AT LEAST FIVE PROPOSALS · NO SINGLE SHARED FORECAST",RED,24)


def card03(d,p):
    nodes=[(180,390,490,555,"MODEL",BLUE),(720,350,1170,595,"TARGET BAND",GREEN),(1430,390,1740,555,"MEASUREMENT",AMBER)]
    for x0,y0,x1,y1,l,c in nodes: rounded(d,(x0,y0,x1,y1),24,PANEL2,c,4); center(d,l,((x0+x1)/2,(y0+y1)/2),30,c,True)
    arrow(d,(495,472),(710,472),CYAN); arrow(d,(1180,472),(1420,472),CYAN)
    d.ellipse((1300,440,1328,468),fill=RED); arrow(d,(1314,454),(1165,375),RED); center(d,"CAN BE WRONG",(1315,345),24,RED,True)
    arrow(d,(1580,565),(1350,720),AMBER); arrow(d,(1580,565),(1725,720),AMBER); badge(d,(1200,700,1490,770),"POSSIBLE CAUSE A",MUTED,20); badge(d,(1550,700,1840,770),"POSSIBLE CAUSE B",MUTED,20)
    badge(d,(280,790,870,855),"1 · A TARGET THAT CAN BE MISSED",GREEN,23); badge(d,(1030,790,1660,855),"2 · A RESULT THAT IDENTIFIES THE IDEA",BLUE,23)


def card04(d,p):
    center(d,"UNIVERSE",(270,340),28,BLUE,True); arrow(d,(390,340),(590,340),CYAN); center(d,"BLACK HOLES",(750,340),28,CYAN,True); arrow(d,(910,340),(1110,340),CYAN); center(d,"CHILD UNIVERSES",(1350,340),28,GREEN,True)
    X=mass_axis(d,660); x15=X(1.5); x2=X(2.0)
    d.line((x15,530,x15,680),fill=BLUE,width=5); center(d,"BROWN–BETHE MAXIMUM ~1.5 M☉",(x15,490),24,BLUE,True,serif=True)
    d.rectangle((x2,570,X(2.2),650),fill=(80,54,44)); d.line((x2,540,x2,680),fill=AMBER,width=5); center(d,"M ≳ 2 M☉",(x2,505),26,AMBER,True,serif=True)
    badge(d,(510,805,1410,875),'“SERIOUS DOUBT OR SIMPLY FALSIFY” — BROWN, LEE & RHO',RED,23)


def card05(d,p):
    X=mass_axis(d,660); center(d,"EVERY DISTANT-STAR MASS HAS AN UNCERTAINTY RANGE",(960,260),27,AMBER,True)
    # Source-defined comparison structure: ~1.5 marker and approximate >=2 regime.
    d.rectangle((X(2.0),405,X(2.2),645),fill=(49,38,37)); d.line((X(1.5),400,X(1.5),685),fill=BLUE,width=3)
    center(d,"BROWN–BETHE MAXIMUM ~1.5 M☉",(X(1.5),380),18,BLUE,True,serif=True); center(d,"M ≳ 2 M☉",((X(2.0)+X(2.2))/2,430),20,AMBER,True,serif=True)
    rows=[("DEMOREST: 1.97 ± 0.04 M☉",1.97,.04,470,BLUE),("FONSECA: 2.08 ± 0.07 M☉ · 68.3%",2.08,.07,555,GREEN)]
    for label,mu,e,y,c in rows:
        center(d,label,(275,y),22,c,True,serif=True); d.line((X(mu-e),y,X(mu+e),y),fill=c,width=8); d.line((X(mu-e),y-13,X(mu-e),y+13),fill=c,width=4); d.line((X(mu+e),y-13,X(mu+e),y+13),fill=c,width=4); d.ellipse((X(mu)-9,y-9,X(mu)+9,y+9),fill=WHITE)
    d.line((X(2.0),400,X(2.0),690),fill=AMBER,width=3); center(d,"2.00",(X(2.0),382),22,AMBER,True,mono=True)
    # The 95.4% statement is NON-SCALED: separate panel, no connector, endpoint, arrow, tick, bracket, marker, whisker, shaded edge, or axis-aligned glyph.
    rounded(d,(245,765,1675,900),24,PANEL2,RED,3); wrap(d,"AT 95.4% CREDIBILITY, THE CLOSING RECORD STATES ONLY THAT THE RESULT DOES NOT CLEAR 2.00",(300,785,1620,835),22,WHITE,True,max_lines=2); wrap(d,"NO 95.4% LOWER-BOUND VALUE IS QUOTED OR PLOTTED HERE",(330,845,1590,885),21,RED,True,max_lines=1)


def card06(d,p):
    # Dimmed mass-plot context carried from Card 05; no 95.4% position exists.
    d.line((260,290,1660,290),fill=GRID,width=3)
    for x in (435,785,1135,1485): d.line((x,282,x,298),fill=GRID,width=2)

    rounded(d,(220,330,750,600),24,PANEL2,AMBER,4); wrap(d,"SERIOUS DOUBT",(270,395,700,530),34,AMBER,True,max_lines=2)
    center(d,"OR",(960,465),46,WHITE,True)
    rounded(d,(1170,330,1700,600),24,PANEL2,RED,4); wrap(d,"SIMPLY FALSIFY",(1220,395,1650,530),34,RED,True,max_lines=2)
    arrow(d,(960,730),(960,605),MUTED); d.line((905,650,1015,650),fill=MUTED,width=7)
    badge(d,(525,690,1395,760),"CLOSING RECORD DOES NOT ADJUDICATE",BLUE,26); badge(d,(560,800,1360,870),"OBSERVATIONS ENTER THE SOURCE-NAMED REGIME",GREEN,24)


def card07(d,p):
    d.ellipse((135,305,615,785),outline=BLUE,width=6); center(d,"PARENT ROTATION AXIS",(375,280),24,BLUE,True); d.line((375,300,1170,700),fill=CYAN,width=5); arrow(d,(615,490),(970,610),CYAN)
    d.ellipse((840,305,1460,825),outline=PURPLE,width=5); center(d,"CHILD UNIVERSE",(1150,280),24,PURPLE,True)
    for i in range(10): galaxy(d,1000+(i%5)*90,390+(i//5)*180,[BLUE,PURPLE][i%2],-1 if i%2 else 1,.16)
    badge(d,(1500,360,1810,455),"CW COUNTS",BLUE,23); center(d,"≠",(1655,535),48,AMBER,True); badge(d,(1500,615,1810,710),"CCW COUNTS",PURPLE,23); center(d,"QUALITATIVE SOURCE CLAIM · NO AMPLITUDE SHOWN",(960,865),22,MUTED,True)


def card08(d,p):
    d.line((180,360,1740,360),fill=GRID,width=5); d.ellipse((390,343,424,377),fill=BLUE); d.ellipse((1200,343,1234,377),fill=AMBER); center(d,"CITED GALAXY STUDIES",(405,300),24,BLUE,True); center(d,"HANDEDNESS CLAIM ADDED IN 2025",(1217,300),24,AMBER,True)
    rounded(d,(190,500,1730,800),26,PANEL,GRID,3); center(d,"FORECAST CONTRACT",(960,550),28,WHITE,True)
    items=[("EQUATIONS PRESENT",GREEN,True),("EXPECTED SIZE",RED,False),("SCALE / REDSHIFT RULE",RED,False),("INDEPENDENT DIRECTION",RED,False),("PASS-OR-FAIL RANGE",RED,False)]
    x=260
    for label,c,ok in items:
        w=270; rounded(d,(x,610,x+w,720),16,PANEL2,c,3); wrap(d,label,(x+25,625,x+w-25,705),20,c,True,max_lines=2); x+=295
    badge(d,(500,835,1420,895),"NOT A PREDICTION MADE BEFORE THE DATA",RED,24)


def card09(d,p):
    rounded(d,(675,360,1245,550),26,PANEL2,AMBER,4); wrap(d,"OBSERVED CW/CCW DIFFERENCE",(735,405,1185,505),29,AMBER,True,max_lines=2)
    arrow(d,(860,555),(560,720),MUTED); arrow(d,(1060,555),(1380,720),MUTED)
    badge(d,(340,700,710,790),"BHU?",BLUE,32); badge(d,(1210,700,1660,790),"OTHER POSSIBLE CAUSES",PURPLE,25)
    badge(d,(540,835,1380,905),"MEASUREMENT ≠ IDENTIFICATION",RED,28)


def card10(d,p):
    rounded(d,(110,285,900,755),28,PANEL,BLUE,4); wrap(d,"1 · NO SOURCE-DEFINED PASS-OR-FAIL RANGE",(180,315,830,385),24,BLUE,True,max_lines=2); wrap(d,"FINITE-PRECISION RESULT",(180,410,830,470),27,WHITE,True); d.line((250,545,760,545),fill=MUTED,width=5); center(d,"BLANK SCORING RULER",(505,600),22,MUTED,True); badge(d,(250,650,760,715),"NO PREDICTED SIZE",RED,24)
    rounded(d,(1020,285,1810,755),28,PANEL,PURPLE,4); center(d,"2 · NO UNIQUE SIGNATURE",(1415,345),27,PURPLE,True); rounded(d,(1260,420,1570,515),18,PANEL2,AMBER,3); center(d,"POSITIVE RESULT",(1415,467),23,AMBER,True); arrow(d,(1340,525),(1190,630),MUTED); arrow(d,(1490,525),(1640,630),MUTED); wrap(d,"A POSITIVE RESULT DOES NOT IDENTIFY BHU",(1080,620,1750,710),23,WHITE,True,max_lines=2)
    center(d,"MEASUREMENT MAY STILL BE TRUSTWORTHY",(960,780),21,MUTED,True)
    badge(d,(355,800,1565,850),"ROUTE CLOSED FOR THIS CAMPAIGN'S SKY-STATISTICS LINE",RED,21)
    badge(d,(460,862,1460,912),"THE HUNT HAD A SOURCE · IT DID NOT HAVE A TARGET",RED,22)


def card11(d,p):
    badge(d,(535,255,765,315),"MODEL",BLUE,22); arrow(d,(775,285),(845,285),CYAN,3); badge(d,(855,255,1085,315),"TARGET",GREEN,22); arrow(d,(1095,285),(1165,285),CYAN,3); badge(d,(1175,255,1455,315),"MEASUREMENT",AMBER,22)
    rounded(d,(160,340,650,620),28,PANEL2,BLUE,4); wrap(d,"CALIBRATED TARGET",(215,405,595,535),32,BLUE,True,max_lines=2)
    rounded(d,(1270,340,1760,620),28,PANEL2,GREEN,4); wrap(d,"UNIQUE SIGNATURE",(1325,405,1705,535),32,GREEN,True,max_lines=2)
    rounded(d,(720,390,1200,555),23,PANEL,AMBER,3); wrap(d,"CONFIRMED SPIN ASYMMETRY ALONE",(770,425,1150,520),25,AMBER,True,max_lines=3)
    arrow(d,(720,470),(665,470),MUTED); arrow(d,(1200,470),(1255,470),MUTED); center(d,"LOCKED",(635,665),24,RED,True); center(d,"LOCKED",(1285,665),24,RED,True)
    badge(d,(385,780,1535,860),"REOPEN ONLY FOR A CALIBRATED TARGET OR A UNIQUE SIGNATURE",GREEN,27)


DRAWERS: dict[str,Callable] = {f"{i:02d}":f for i,f in enumerate([card01,card02,card03,card04,card05,card06,card07,card08,card09,card10,card11],1)}


class Renderer:
    def __init__(self):
        if sha(STORY)!=EXPECTED_STORY_SHA or sha(NARR)!=EXPECTED_NARR_SHA: raise RuntimeError("gated source hash mismatch")
        self.story=json.loads(STORY.read_text()); self.timeline=json.loads(TIMELINE.read_text()); self.cards=self.timeline["cards"]
        self.duration=self.timeline["master_duration_seconds"]
        for card in self.story["cards"]:
            tc=next(x for x in self.cards if x["card_id"]==card["id"])
            if tc["narration"]!=card["narration"] or tc["heading"]!=card["heading"]: raise RuntimeError(f"timeline source mismatch card {card['id']}")
        self.validate_public_surface()

    def validate_public_surface(self):
        surface=[]
        for c in self.story["cards"]: surface += [c["heading"],c["narration"],c["diagram"],*c["on_screen_support"]]
        blob=" ".join(surface).lower()
        for term in ("the packet","packet does not","the ledger","the receipt","1.95","near-certainty"):
            if term in blob: raise RuntimeError(f"forbidden public term {term}")
        c5=self.story["cards"][4]
        required="Do not draw a 95.4% endpoint, arrow, tick, bracket, or marker on the mass axis."
        if required not in c5["diagram"]: raise RuntimeError("Card 05 negative visual constraint absent")

    def active(self,t):
        for c in self.cards:
            if t<c["end_seconds"]: return c,max(0,min(1,(t-c["start_seconds"])/max(.001,c["end_seconds"]-c["start_seconds"])))
        return self.cards[-1],1.0

    def frame(self,t):
        img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
        for x in range(0,W+1,96): d.line((x,0,x,H),fill=(19,31,48),width=1)
        for y in range(0,H+1,96): d.line((0,y,W,y),fill=(19,31,48),width=1)
        c,p=self.active(t); spec=next(x for x in self.story["cards"] if x["id"]==c["card_id"])
        d.text((72,36),"NEBULAMIND · CLOSING RECORD",font=font(21,True),fill=MUTED); right=f"{int(c['card_id'])} / 11"; f=font(21,True); d.text((W-72-d.textlength(right,font=f),36),right,font=f,fill=MUTED)
        d.line((72,82,W-72,82),fill=GRID,width=2)
        wrap(d,spec["heading"],(125,105,1795,240),47,WHITE,True,max_lines=2)
        # Deterministic state transition: diagram first, then support. The
        # assertion heading is stable from frame one; no decorative motion.
        layer=Image.new("RGBA",(W,H),(0,0,0,0)); ld=ImageDraw.Draw(layer)
        DRAWERS[c["card_id"]](ld,p)
        q=max(0.0,min(1.0,p/0.14)); q=q*q*(3-2*q)
        layer.putalpha(layer.getchannel("A").point([round(a*q) for a in range(256)]))
        img=Image.alpha_composite(img.convert("RGBA"),layer).convert("RGB"); d=ImageDraw.Draw(img)
        # Visual support strip selected from gated strings, never metadata.
        support=spec["on_screen_support"][-1]
        support_layer=Image.new("RGBA",(W,H),(0,0,0,0)); sd=ImageDraw.Draw(support_layer)
        rounded(sd,(135,920,1785,985),17,(7,12,21),GRID,2); wrap(sd,support,(175,930,1745,975),20,MUTED,True,max_lines=2)
        s=max(0.0,min(1.0,(p-0.10)/0.10)); s=s*s*(3-2*s)
        support_layer.putalpha(support_layer.getchannel("A").point([round(a*s) for a in range(256)]))
        img=Image.alpha_composite(img.convert("RGBA"),support_layer).convert("RGB")
        return img

    def preview(self):
        out=BUILD/"qa_frames_pre"; out.mkdir(parents=True,exist_ok=True); items=[]
        for c in self.cards:
            for tag,q in (("early",.2),("mid",.55),("late",.86)):
                t=c["start_seconds"]+(c["end_seconds"]-c["start_seconds"])*q; p=out/f"card-{c['card_id']}-{tag}-{t:07.3f}.png"; self.frame(t).save(p); items.append((c["card_id"]+" "+tag,t,p))
        cols=3; tw,th,lh=640,360,36; rows=math.ceil(len(items)/cols); sheet=Image.new("RGB",(cols*tw,rows*(th+lh)),(2,5,10)); d=ImageDraw.Draw(sheet)
        for i,(label,t,p) in enumerate(items):
            x=(i%cols)*tw; y=(i//cols)*(th+lh); im=ImageOps.fit(Image.open(p),(tw,th),Image.Resampling.LANCZOS); sheet.paste(im,(x,y)); center(d,f"{label} · {t:.2f}s",(x+tw/2,y+th+18),20,WHITE,True)
        sheet.save(BUILD/"pre-render-contact-sheet.jpg",quality=95,subsampling=0)
        print(BUILD/"pre-render-contact-sheet.jpg")

    def render(self):
        OUTPUT.parent.mkdir(parents=True,exist_ok=True); audio=BUILD/"audio/narration_master.wav"; count=math.ceil(self.duration*FPS)
        cmd=["ffmpeg","-y","-hide_banner","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-i",str(audio),"-map","0:v:0","-map","1:a:0","-c:v","libx264","-preset","medium","-crf","19","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-movflags","+faststart","-shortest",str(OUTPUT)]
        p=subprocess.Popen(cmd,stdin=subprocess.PIPE); assert p.stdin
        try:
            for i in range(count):
                p.stdin.write(self.frame(i/FPS).tobytes())
                if i%600==0: print(f"frame {i}/{count}")
        finally: p.stdin.close()
        if p.wait()!=0: raise RuntimeError("encode failed")
        prov=BUILD/"provenance"; prov.mkdir(exist_ok=True); shutil.copy2(__file__,prov/"render_v7.py")
        env={"python":sys.version,"platform":platform.platform(),"pillow":PIL.__version__,"ffmpeg":subprocess.run(["ffmpeg","-version"],capture_output=True,text=True).stdout.splitlines()[:4],"fonts":{p:sha(Path(p)) for p in (FONT_PATH,SERIF_PATH,MONO_PATH)},"output":str(OUTPUT),"raw_frames_submitted":count}
        (prov/"environment.json").write_text(json.dumps(env,indent=2)+"\n")
        print(OUTPUT); print(sha(OUTPUT))


def main():
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument("--preview",action="store_true"); ap.add_argument("--render",action="store_true"); a=ap.parse_args(); r=Renderer()
    if a.preview: r.preview()
    if a.render: r.render()
    if not a.preview and not a.render: raise SystemExit("choose --preview or --render")


if __name__=="__main__": main()
