#!/usr/bin/env python3
"""Shared animated renderer for all four source-specific sibling method canaries."""
from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

import PIL
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H, FPS = 1920, 1080, 30
BG = (8, 14, 27); PANEL = (18, 31, 52); PANEL2 = (24, 40, 65); GRID = (49, 70, 96)
WHITE = (239, 244, 251); MUTED = (163, 179, 201); BLUE = (85, 142, 255); CYAN = (56, 210, 232)
PURPLE = (169, 111, 238); GREEN = (67, 209, 158); AMBER = (245, 181, 62); RED = (243, 91, 91)
FONT_PATH = "/System/Library/Fonts/Avenir Next.ttc"; MONO_PATH = "/System/Library/Fonts/Menlo.ttc"
SERIF_PATH = "/System/Library/Fonts/Supplemental/STIXTwoText.ttf"
NUMERIC = re.compile(r"(?<![A-Za-z0-9_])(\d[\d,]*\.?\d*)(?![A-Za-z0-9_])")


@functools.lru_cache(maxsize=None)
def font(size: int, mono: bool = False, bold: bool = False, serif: bool = False) -> ImageFont.FreeTypeFont:
    if serif:
        return ImageFont.truetype(SERIF_PATH, size)
    idx = 0 if mono else 7 if bold else 0
    return ImageFont.truetype(MONO_PATH if mono else FONT_PATH, size, index=idx)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ease(x: float) -> float:
    x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)


def seg(p: float, a: float, b: float) -> float:
    return ease((p - a) / max(1e-6, b - a))


def mix(a, b, q: float):
    return tuple(round(a[i] + (b[i] - a[i]) * max(0, min(1, q))) for i in range(3))


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def center_text(draw, text: str, xy, size: int, color=WHITE, mono=False, bold=False):
    f = font(size, mono, bold); box = draw.textbbox((0, 0), text, font=f)
    draw.text((xy[0] - (box[2] - box[0]) / 2, xy[1] - (box[3] - box[1]) / 2), text, font=f, fill=color)


def wrap_lines(draw, text: str, fnt, width: float) -> list[str]:
    words = text.split(); lines = []; current = ""
    for word in words:
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            if current: lines.append(current)
            current = word
    if current: lines.append(current)
    return lines


def wrapped(draw, text: str, box, size: int, color=WHITE, mono=False, bold=False, align="center", max_lines=None, serif=False):
    f = font(size, mono, bold, serif); lines = wrap_lines(draw, text, f, box[2] - box[0])
    if max_lines and len(lines) > max_lines:
        raise RuntimeError(f"text exceeds {max_lines} lines: {text}")
    step = size + 9; total = len(lines) * step - 9; y = box[1] + max(0, (box[3] - box[1] - total) / 2)
    for line in lines:
        tw = draw.textlength(line, font=f)
        x = box[0] if align == "left" else box[2] - tw if align == "right" else box[0] + (box[2] - box[0] - tw) / 2
        draw.text((x, y), line, font=f, fill=color); y += step
    return len(lines)


def badge(draw, box, text, color, size=24):
    rounded(draw, box, 15, mix(BG, color, 0.10), color, 2); center_text(draw, text, ((box[0]+box[2])/2,(box[1]+box[3])/2), size, color, bold=True)


def arrow(draw, start, end, color, progress=1.0, width=4):
    q=max(0,min(1,progress)); x=start[0]+(end[0]-start[0])*q; y=start[1]+(end[1]-start[1])*q
    draw.line((start[0],start[1],x,y),fill=color,width=width)
    if q>0.92:
        ang=math.atan2(end[1]-start[1],end[0]-start[0]); l=15
        for d in (2.55,-2.55):
            draw.line((end[0],end[1],end[0]+l*math.cos(ang+d),end[1]+l*math.sin(ang+d)),fill=color,width=width)


def flow_dots(draw,start,end,t,color,count=4):
    for i in range(count):
        q=(t*0.32+i/count)%1.0; x=start[0]+(end[0]-start[0])*q; y=start[1]+(end[1]-start[1])*q
        draw.ellipse((x-5,y-5,x+5,y+5),fill=color)


def flatten_strings(value: Any) -> list[str]:
    if isinstance(value,str): return [value]
    if isinstance(value,dict):
        out=[]
        for v in value.values(): out+=flatten_strings(v)
        return out
    if isinstance(value,list):
        out=[]
        for v in value: out+=flatten_strings(v)
        return out
    return []


def resolve_source(candidate: Path, source: str) -> Path:
    p=Path(source); return p if p.is_absolute() else candidate/p


def numeric_guard(candidate: Path, spec: dict) -> dict:
    evidence=[]; problems=[]
    for item in spec["sentences"]:
        claims=" ".join([item["text"]]+flatten_strings(item.get("params",{})))
        nums=sorted({n.replace(",","") for n in NUMERIC.findall(claims)})
        if not nums: continue
        source=item.get("source")
        if not source:
            problems.append(f"{item['id']} has {nums} without a numeric source"); continue
        path=resolve_source(candidate,source)
        if not path.is_file():
            problems.append(f"{item['id']} source missing: {source}"); continue
        text=path.read_text(errors="replace"); lines=text.splitlines(); flat=text.replace(",","")
        for n in nums:
            if n not in flat:
                problems.append(f"{item['id']} number {n} absent from {source}")
            else:
                hits=[{"line":i+1,"context":line.strip()[:180]} for i,line in enumerate(lines) if n in line.replace(",","")]
                evidence.append({"id":item["id"],"number":n,"source":source,"hits":hits[:5],"hit_count":len(hits)})
    report={"status":"PASS" if not problems else "HOLD","problems":problems,"evidence":evidence}
    (candidate/"numeric_guard.json").write_text(json.dumps(report,indent=2)+"\n")
    if problems: raise RuntimeError("numeric guard HOLD: "+"; ".join(problems))
    return report


class Renderer:
    def __init__(self,candidate:Path):
        self.root=candidate; self.spec=json.loads((candidate/"spec.json").read_text()); self.timeline=json.loads((candidate/"audio/timeline.json").read_text())
        self.records=self.timeline["records"]; self.duration=float(self.timeline["master_duration_seconds"]); self.output=candidate/self.spec["candidate_filename"]
        self.qa_frames=candidate/"qa_frames"; self.preview=candidate/"final-timing-contact-sheet.jpg"
        numeric_guard(candidate,self.spec); self.validate()

    def validate(self):
        ids=[r["id"] for r in self.records]
        if len(ids)!=len(set(ids)): raise RuntimeError("duplicate ids")
        opening=self.records[:4]
        if [r["section"] for r in opening] != ["motivation"]*4: raise RuntimeError("motivation is not first")
        joined=" ".join(r["text"].lower() for r in opening)
        if not all(x in opening[1]["text"].lower() for x in ("if","would")): raise RuntimeError("opening stakes clause is not conditional")
        if "could" not in opening[2]["text"].lower(): raise RuntimeError("opening alternative is not conditional")
        if any(x in joined for x in ("not reportable","value withheld","method only","no result")): raise RuntimeError("opening begins with a disclaimer")
        corpus=" ".join(r["text"]+" "+" ".join(flatten_strings(r.get("params",{}))) for r in self.records).lower()
        hits=[x for x in self.spec.get("forbidden_terms",[]) if re.search(rf"(?<![a-z0-9]){re.escape(x.lower())}(?![a-z0-9])",corpus)]
        if hits: raise RuntimeError(f"forbidden terms: {hits}")
        if self.spec.get("video_reportable_now") is not False: raise RuntimeError("video_reportable_now must be false")
        if self.spec.get("source_freeze_status") != "ABSENT_FAIL_CLOSED": raise RuntimeError("SOURCE_FREEZE state must remain absent and fail-closed")
        forbidden_icons=set(self.spec.get("forbidden_icon_primitives",[]))
        if "curve" not in forbidden_icons: raise RuntimeError("curve must remain a forbidden icon primitive")
        for r in self.records:
            source=r.get("grounding")
            if not source or not resolve_source(self.root,source).is_file(): raise RuntimeError(f"ungrounded record {r['id']}")
            icon=r.get("params",{}).get("icon")
            if icon in forbidden_icons: raise RuntimeError(f"forbidden icon primitive {icon} in {r['id']}")
            if r.get("visual")=="peak" and r.get("params",{}).get("mode") in forbidden_icons: raise RuntimeError(f"forbidden peak primitive in {r['id']}")
        d=ImageDraw.Draw(Image.new("RGB",(W,H)))
        def caption_font(record):
            if record["section"] != "literature": return font(31,bold=True)
            return font(18 if len(record["text"])>190 else 24,serif=True)
        over={r["id"]:len(wrap_lines(d,r["text"],caption_font(r),W-410)) for r in self.records}
        if max(over.values())>2: raise RuntimeError(f"caption exceeds two lines: {over}")

    def active(self,t):
        for i,r in enumerate(self.records):
            end=self.records[i+1]["audio_start_seconds"] if i+1<len(self.records) else self.duration
            if t<end:
                start=r["audio_start_seconds"]; return r,max(0,min(1,(t-start)/max(0.001,end-start)))
        return self.records[-1],1.0

    def background(self,draw,t):
        for x in range(0,W+1,96): draw.line((x,80,x,H),fill=(20,35,55),width=1)
        for y in range(96,H,96): draw.line((0,y,W,y),fill=(20,35,55),width=1)
        for i in range(48):
            x=(i*211+37)%W; y=90+((i*97+int(t*7))%(H-190)); r=1 if i%4 else 2
            draw.ellipse((x-r,y-r,x+r,y+r),fill=(38,68,96))

    def chrome(self,draw,t,section):
        draw.text((70,31),self.spec["series_label"],font=font(22,bold=True),fill=MUTED)
        text="LITERATURE CONTEXT · NO ANSWER SELECTED" if section=="literature" else "METHOD DESIGN · NO MEASURED VALUE"; f=font(22,bold=True); draw.text((W-70-draw.textlength(text,font=f),31),text,font=f,fill=AMBER)
        draw.line((70,80,W-70,80),fill=GRID,width=2)
        stages=[("WHY IT MATTERS",{"motivation","literature","difficulty"}),("DISCRIMINANT",{"peak"}),("SOURCE",{"sample"}),("ESTIMATOR",{"estimator"}),("CONTROLS",{"controls","discipline"}),("SCIENCE",{"boundary","payoff"})]
        y=888; xs=[110,450,790,1130,1470,1810]
        draw.line((xs[0],y,xs[-1],y),fill=GRID,width=3)
        for x,(label,sections) in zip(xs,stages):
            on=section in sections; c=CYAN if on else MUTED
            if on:
                rounded(draw,(max(20,x-145),y+17,min(W-20,x+145),y+51),12,mix(BG,CYAN,.27))
            draw.ellipse((x-8,y-8,x+8,y+8),fill=c); center_text(draw,label,(x,y+34),18,c,bold=True)

    def title(self,draw,subtitle=None):
        center_text(draw,self.spec["short_title"],(W/2,137),48,WHITE,bold=True)
        if subtitle: center_text(draw,subtitle,(W/2,182),25,AMBER,bold=True)

    def icon(self,draw,kind,x,y,color,q=1.0,scale=1.0):
        c=mix(BG,color,q)
        if kind=="archive":
            for k in range(3): rounded(draw,(x-85+k*10,y-60+k*10,x+65+k*10,y+45+k*10),12,PANEL,c,3)
            for yy in (-25,5): draw.line((x-55,y+yy,x+55,y+yy),fill=c,width=3)
        elif kind=="galaxy":
            for a in range(0,420,7):
                th=a*0.22; r=0.33*a*scale; xx=x+r*math.cos(th); yy=y+0.55*r*math.sin(th)
                draw.ellipse((xx-3,yy-3,xx+3,yy+3),fill=c)
        elif kind=="curve":
            raise RuntimeError("forbidden icon primitive: curve")
        elif kind=="plane":
            draw.line((x-100,y+60,x-100,y-65,x+110,y+60),fill=c,width=3)
            draw.line((x+15,y-60,x+15,y+55),fill=c,width=3); draw.line((x-95,y+5,x+105,y+5),fill=c,width=3)
        elif kind=="anchor":
            draw.line((x,y-75,x,y+55),fill=c,width=8); draw.arc((x-80,y-25,x+80,y+85),0,180,fill=c,width=8)
            draw.line((x-80,y+30,x-35,y+70,x,y+45,x+35,y+70,x+80,y+30),fill=c,width=8)

    def intro(self,draw,r,p,t):
        P=r["params"]; self.title(draw,P["subtitle"])
        self.icon(draw,P["icon"],520,375,BLUE,1,1.0); self.icon(draw,P["icon"],1400,375,PURPLE,1,-1.0)
        center_text(draw,P["left_title"],(520,545),30,BLUE,bold=True); center_text(draw,P["right_title"],(1400,545),30,PURPLE,bold=True)
        lq=r["id"] in ("i01","i02","i04"); rq=r["id"] in ("i01","i03","i04")
        lb=(90,625,750,835); rb=(1170,625,1830,835)
        rounded(draw,lb,25,PANEL,BLUE if lq else GRID,4); rounded(draw,rb,25,PANEL,PURPLE if rq else GRID,4)
        center_text(draw,P["left_if"],(420,675),24,AMBER if lq else mix(BG,AMBER,.55),bold=True)
        wrapped(draw,P["left_body"],(130,700,710,815),29,WHITE if lq else mix(BG,WHITE,.55),bold=True,max_lines=3)
        center_text(draw,P["right_if"],(1500,675),24,AMBER if rq else mix(BG,AMBER,.55),bold=True)
        wrapped(draw,P["right_body"],(1210,700,1790,815),29,WHITE if rq else mix(BG,WHITE,.55),bold=True,max_lines=3)
        if r["id"]=="i01": badge(draw,(720,285,1200,360),P["pair_label"],CYAN,29)
        if r["id"]=="i04":
            arrow(draw,(750,735),(815,735),BLUE,1); arrow(draw,(1170,735),(1105,735),PURPLE,1)
            rounded(draw,(805,645,1115,825),25,PANEL2,CYAN,4); wrapped(draw,P["question"],(835,670,1085,800),28,WHITE,bold=True,max_lines=4)

    def literature(self,draw,r,p,t):
        P=r["params"]; color={"blue":BLUE,"cyan":CYAN,"purple":PURPLE}[P.get("color","blue")]
        center_text(draw,P["heading"],(W/2,160),32,AMBER,bold=True)
        if P.get("closing"):
            card=P["summary_cards"][0]; q=seg(p,.03,.72)
            rounded(draw,(350,255,1570,545),28,PANEL,mix(GRID,color,q),4)
            center_text(draw,card["author"],(960,335),33,color,bold=True)
            wrapped(draw,card["report"],(455,390,1465,485),29,WHITE,bold=True,max_lines=2)
            arrow(draw,(960,555),(960,640),color,q,4)
            rounded(draw,(430,625,1490,805),28,PANEL2,AMBER,4)
            center_text(draw,"CLAIMED · DISPUTED · UNSETTLED",(960,685),35,WHITE,bold=True)
            badge(draw,(665,725,1255,790),"NO ANSWER SELECTED",AMBER,29)
            return
        q=seg(p,.02,.72)
        rounded(draw,(245,235,1675,775),30,PANEL,mix(GRID,color,q),4)
        badge(draw,(390,280,1530,355),P["study_header"],color,27)
        rounded(draw,(335,395,1585,650),22,(10,18,31),GRID,2)
        wrapped(draw,r["text"],(385,420,1535,625),P.get("quote_font_size",32),WHITE,max_lines=6,serif=True)
        center_text(draw,"ATTRIBUTED TO ANOTHER STUDY · NOT THIS VIDEO'S FINDING",(960,705),22,AMBER,bold=True)
        center_text(draw,P["source_line"],(960,820),20,MUTED)

    def difficulty(self,draw,r,p,t):
        P=r["params"]; self.title(draw,P["heading"])
        rounded(draw,(690,290,1230,690),30,PANEL2,AMBER,4); self.icon(draw,P["icon"],960,420,AMBER,1)
        center_text(draw,P["object_label"],(960,595),31,AMBER,bold=True)
        left=(90,350,560,735); right=(1360,350,1830,735)
        rounded(draw,left,26,PANEL,BLUE,4); rounded(draw,right,26,PANEL,PURPLE,4)
        wrapped(draw,P["left"],(130,390,520,700),31,BLUE,bold=True,max_lines=5); wrapped(draw,P["right"],(1400,390,1790,700),31,PURPLE,bold=True,max_lines=5)
        arrow(draw,(560,540),(690,500),BLUE,1); arrow(draw,(1360,540),(1230,500),PURPLE,1)
        badge(draw,(690,730,1230,805),P["bottom"],AMBER,27)

    def peak_semantic(self,draw,r,p,t):
        P=r["params"]; self.title(draw,P["heading"])
        rounded(draw,(70,270,490,785),26,PANEL,BLUE,4); center_text(draw,"ONE ARCHIVE TABLE",(280,315),27,BLUE,bold=True)
        rows=P["rows"]
        for i,label in enumerate(rows):
            y=375+i*105; rounded(draw,(115,y,445,y+68),13,PANEL2,GRID,2); center_text(draw,label,(280,y+34),25,WHITE,bold=True)
        cards=[("COLUMN NAME",CYAN),("UCD QUALIFIER",GREEN),("DESCRIPTION",PURPLE)]
        for i,(label,c) in enumerate(cards):
            y=300+i*145; q=seg(p,i*.12,i*.12+.45); rounded(draw,(650,y,1080,y+100),17,PANEL2,mix(GRID,c,q),3); center_text(draw,label,(865,y+36),24,mix(BG,c,q),bold=True); flow_dots(draw,(500,520),(645,y+50),t+i,c,3)
        rounded(draw,(1240,275,1845,790),26,PANEL,AMBER,4); center_text(draw,"PREDECLARED CLAUSES",(1542,320),27,AMBER,bold=True)
        for i,label in enumerate(P["clauses"]):
            q=seg(p,.22+i*.1,.55+i*.1); badge(draw,(1290,370+i*105,1795,438+i*105),label,mix(GRID,GREEN,q),22)
        arrow(draw,(1090,520),(1230,520),CYAN,1); badge(draw,(630,730,1080,800),"EVIDENCE, NOT TAG ALONE",CYAN,24)

    def peak_curve(self,draw,r,p,t):
        P=r["params"]; self.title(draw,P["heading"])
        badge(draw,(540,195,1380,255),"MATCHED SWEEP DESIGN · NO RESULT GEOMETRY",AMBER,24)
        cards=[(120,315,770,570,P["curve_a"],BLUE),(1150,315,1800,570,P["curve_b"],PURPLE)]
        for x0,y0,x1,y1,label,c in cards:
            pulse=.55+.45*(.5+.5*math.sin(t*2.1))
            rounded(draw,(x0,y0,x1,y1),26,PANEL2,mix(GRID,c,pulse),4)
            center_text(draw,"DECLARED CALCULATION ARM",((x0+x1)/2,y0+58),21,MUTED,bold=True)
            wrapped(draw,label,(x0+55,y0+90,x1-55,y1-45),31,c,bold=True,max_lines=3)
        arrow(draw,(780,445),(920,445),CYAN,1); arrow(draw,(1140,445),(1000,445),CYAN,1)
        rounded(draw,(880,355,1060,535),24,PANEL,CYAN,4); wrapped(draw,"SAME GRID\nSAME PRIORS",(905,385,1035,505),24,WHITE,bold=True,max_lines=3)
        steps=["DECLARE","PROPAGATE","PAIR","CHALLENGE","COMPARE"]
        active=int((t*.72)%len(steps))
        for i,label in enumerate(steps):
            x=250+i*355; c=CYAN if i==active else MUTED
            rounded(draw,(x-130,650,x+130,720),15,PANEL2,c,3)
            center_text(draw,label,(x,685),21,c,bold=True)
            if i<len(steps)-1: arrow(draw,(x+135,685),(x+220,685),GRID,1,3)
        badge(draw,(430,755,1490,825),P["outcome"],AMBER,22)

    def peak_plane(self,draw,r,p,t):
        P=r["params"]; self.title(draw,P["heading"])
        for i,(label,c) in enumerate(((P["channel_a"],BLUE),(P["channel_b"],PURPLE))):
            y=310+i*180; rounded(draw,(70,y,470,y+120),20,PANEL,c,3); center_text(draw,label,(270,y+60),25,c,bold=True)
            arrow(draw,(480,y+60),(700,500),c,1); flow_dots(draw,(490,y+60),(690,500),t+i,c,4)
        rounded(draw,(700,390,1120,610),25,PANEL2,AMBER,4); wrapped(draw,P["same_table"],(745,420,1075,580),29,WHITE,bold=True,max_lines=4)
        arrow(draw,(1130,500),(1260,500),CYAN,1)
        x0,y0,x1,y1=1260,735,1840,275; pulse=.55+.45*(.5+.5*math.sin(t*2.0)); draw.line((x0,y0,x0,y1,x1,y1),fill=mix(GRID,MUTED,pulse),width=4)
        cutx=1510; cuty=520; draw.line((cutx,y1,cutx,y0),fill=BLUE,width=4); draw.line((x0,cuty,x1,cuty),fill=PURPLE,width=4)
        center_text(draw,P["x_label"],((x0+x1)/2,785),23,MUTED,bold=True); center_text(draw,P["y_label"],(1205,470),23,MUTED,bold=True)
        badge(draw,(1300,195,1800,255),"EMPTY PLANE · NO DATA POINTS",AMBER,22)
        center_text(draw,"NO OBJECT POSITION SHOWN",((x0+x1)/2,(y0+y1)/2),22,MUTED,bold=True)
        flow_dots(draw,(1135,500),(1240,500),t,CYAN,3)

    def peak_anchor(self,draw,r,p,t):
        P=r["params"]; self.title(draw,P["heading"])
        labels=P.get("chain", P.get("stages")); xs=[170,520,870,1220,1570]
        if not labels or len(labels) != len(xs):
            raise RuntimeError("anchor peak requires five chain stages")
        for i,(x,label) in enumerate(zip(xs,labels)):
            q=.4+.6*seg(p,i*.08,i*.08+.38); rounded(draw,(x-125,360,x+125,590),24,PANEL2,mix(GRID,[BLUE,CYAN,GREEN,PURPLE,AMBER][i],q),4)
            self.icon(draw,"anchor" if i==0 else "archive",x,435,[BLUE,CYAN,GREEN,PURPLE,AMBER][i],q,.45)
            wrapped(draw,label,(x-105,505,x+105,570),22,WHITE,bold=True,max_lines=3)
            if i<len(xs)-1: arrow(draw,(x+130,475),(xs[i+1]-130,475),CYAN,1); flow_dots(draw,(x+140,475),(xs[i+1]-140,475),t+i,CYAN,3)
        badge(draw,(530,665,1390,745),P.get("bottom", "EXPLANATIONS KEPT SEPARATE · VALUE WITHHELD"),AMBER,27)

    def peak(self,draw,r,p,t):
        mode=r["params"]["mode"]
        if mode=="semantic": self.peak_semantic(draw,r,p,t)
        elif mode=="curve": self.peak_curve(draw,r,p,t)
        elif mode=="plane": self.peak_plane(draw,r,p,t)
        elif mode=="anchor": self.peak_anchor(draw,r,p,t)
        else: raise RuntimeError(f"unknown peak mode {mode}")

    def funnel(self,draw,r,p,t):
        P=r["params"]; self.title(draw,P["heading"])
        stages=P["stages"]; n=len(stages); margin=80; gap=28; bw=(W-2*margin-gap*(n-1))/n
        for i,s in enumerate(stages):
            x=margin+i*(bw+gap); q=seg(p,i*.08,i*.08+.35); c=[BLUE,CYAN,GREEN,PURPLE,AMBER][i%5]
            rounded(draw,(x,320,x+bw,700),24,PANEL,mix(GRID,c,q),4)
            wrapped(draw,s["label"],(x+20,350,x+bw-20,470),25,mix(BG,c,q),bold=True,max_lines=4)
            if s.get("count"): center_text(draw,s["count"],(x+bw/2,555),48,mix(BG,WHITE,q),mono=True,bold=True)
            wrapped(draw,s.get("unit",""),(x+20,610,x+bw-20,665),20,MUTED,bold=True,max_lines=2)
            if i<n-1: arrow(draw,(x+bw+4,510),(x+bw+gap-4,510),CYAN,q,4)
        badge(draw,(590,745,1330,815),P["banner"],AMBER,24)

    def estimator(self,draw,r,p,t):
        P=r["params"]; self.title(draw,P["heading"])
        rounded(draw,(190,260,1730,700),30,PANEL,GRID,4)
        center_text(draw,P["symbol"],(430,480),58,WHITE,mono=True,bold=True); center_text(draw,"=",(575,480),58,WHITE,mono=True)
        q1=seg(p,.05,.45); q2=seg(p,.25,.70)
        if P.get("layout")=="expression":
            wrapped(draw,P["expression"],(690,350,1570,585),42,mix(PANEL,CYAN,q1),mono=True,bold=True,max_lines=3)
        else:
            center_text(draw,P["numerator"],(1120,405),43,mix(PANEL,CYAN,q1),mono=True,bold=True); draw.line((720,480,1515,480),fill=WHITE,width=5)
            center_text(draw,P["denominator"],(1120,555),39,mix(PANEL,GREEN,q2),mono=True,bold=True)
        badge(draw,(700,625,1240,700),"VALUE WITHHELD",AMBER,29)
        signs=P.get("signs",[])
        if signs:
            w=420; x0=(W-(w*len(signs)+35*(len(signs)-1)))/2
            for i,s in enumerate(signs): rounded(draw,(x0+i*(w+35),735,x0+i*(w+35)+w,810),16,PANEL2,GRID,2); center_text(draw,s,(x0+i*(w+35)+w/2,773),23,MUTED,mono=True)
            center_text(draw,"NO SIGN SELECTED",(W/2,845),20,MUTED,bold=True)

    def controls(self,draw,r,p,t):
        P=r["params"]; self.title(draw,P["heading"])
        x0,x1=110,1810; y0=275; rounded(draw,(x0,y0,x1,790),22,PANEL,GRID,3)
        draw.rectangle((x0,y0,x1,y0+70),fill=(31,52,82)); draw.text((145,y0+22),"CONTROL",font=font(22,bold=True),fill=CYAN); draw.text((760,y0+22),"FAILURE MODE TESTED",font=font(22,bold=True),fill=AMBER)
        for i,row in enumerate(P["rows"]):
            y=y0+90+i*125; q=seg(p,i*.1,i*.1+.35); c=[BLUE,GREEN,PURPLE][i%3]
            draw.text((145,y),row[0],font=font(25,bold=True),fill=mix(PANEL,c,q)); arrow(draw,(570,y+16),(690,y+16),mix(PANEL,c,q),q,3); draw.text((750,y),row[1],font=font(24),fill=mix(PANEL,WHITE,q))
        badge(draw,(680,805,1240,865),"DESIGN ONLY · NO OUTCOMES",AMBER,23)

    def discipline(self,draw,r,p,t):
        P=r["params"]; self.title(draw,"WE TIED OUR OWN HANDS")
        center_text(draw,"so the answer cannot be shaped after seeing it",(W/2,195),25,MUTED,bold=True)
        xs=[400,760,1120,1480]
        for i,(x,label) in enumerate(zip(xs,P["locks"])):
            q=seg(p,i*.09,i*.09+.35); rounded(draw,(x-145,340,x+145,535),23,PANEL2,mix(GRID,[BLUE,CYAN,GREEN,PURPLE][i],q),4); wrapped(draw,label,(x-120,375,x+120,505),25,mix(BG,WHITE,q),bold=True,max_lines=3)
            draw.arc((x-28,285,x+28,365),180,360,fill=mix(BG,AMBER,q),width=7); draw.rectangle((x-36,320,x+36,380),fill=mix(BG,AMBER,q))
        draw.line((250,670,1670,670),fill=RED,width=5); center_text(draw,"LATER CHOICE",(330,625),22,RED,bold=True); center_text(draw,"LATER CHOICE",(1590,625),22,RED,bold=True)
        badge(draw,(580,725,1340,810),P["bottom"],AMBER,25)

    def boundary(self,draw,r,p,t):
        P=r["params"]; self.title(draw,"SCIENTIFIC BOUNDARY")
        columns=[("KNOWN NOW",P["known"],GREEN),("NOT REPORTABLE",P["held"],RED),("NEXT SCIENTIFIC GATE",P["next"],AMBER)]
        for i,(head,items,c) in enumerate(columns):
            x=70+i*615; rounded(draw,(x,270,x+560,790),24,PANEL,mix(GRID,c,.75),4); center_text(draw,head,(x+280,320),25,c,bold=True)
            for j,item in enumerate(items): draw.ellipse((x+45,395+j*90,x+55,405+j*90),fill=c); wrapped(draw,item,(x+75,365+j*90,x+520,435+j*90),22,WHITE,align="left",max_lines=2)
        center_text(draw,"VALUE · DIRECTION · INTERPRETATION",(W/2,840),20,RED,bold=True)

    def payoff(self,draw,r,p,t):
        P=r["params"]; self.title(draw,P["heading"])
        left=(75,300,570,735); right=(1350,300,1845,735); middle=(690,330,1230,705)
        rounded(draw,left,28,PANEL,BLUE,4); rounded(draw,right,28,PANEL,PURPLE,4); rounded(draw,middle,28,PANEL2,CYAN,4)
        self.icon(draw,P["icon"],322,430,BLUE,1,.75); self.icon(draw,P["icon"],1598,430,PURPLE,1,.75)
        wrapped(draw,P["left"],(125,540,520,700),27,BLUE,bold=True,max_lines=4); wrapped(draw,P["right"],(1400,540,1795,700),27,PURPLE,bold=True,max_lines=4)
        wrapped(draw,P["discriminant"],(740,390,1180,645),31,WHITE,bold=True,max_lines=5)
        arrow(draw,(575,515),(680,515),BLUE,1); arrow(draw,(1345,515),(1240,515),PURPLE,1); badge(draw,(630,760,1290,830),P["banner"],AMBER,24)

    def frame(self,t):
        img=Image.new("RGB",(W,H),BG); draw=ImageDraw.Draw(img); self.background(draw,t); r,p=self.active(t); self.chrome(draw,t,r["section"])
        visual=r["visual"]
        if visual=="intro": self.intro(draw,r,p,t)
        elif visual=="literature": self.literature(draw,r,p,t)
        elif visual=="difficulty": self.difficulty(draw,r,p,t)
        elif visual=="peak": self.peak(draw,r,p,t)
        elif visual=="funnel": self.funnel(draw,r,p,t)
        elif visual=="estimator": self.estimator(draw,r,p,t)
        elif visual=="controls": self.controls(draw,r,p,t)
        elif visual=="discipline": self.discipline(draw,r,p,t)
        elif visual=="boundary": self.boundary(draw,r,p,t)
        elif visual=="payoff": self.payoff(draw,r,p,t)
        else: raise RuntimeError(f"unknown visual {visual}")
        if r.get("display_citation") and visual!="literature": draw.text((90,852),r["display_citation"],font=font(18),fill=MUTED)
        caption_size=18 if visual=="literature" and len(r["text"])>190 else 24 if visual=="literature" else 31
        rounded(draw,(170,940,1750,1054),22,(5,12,23),GRID,2); wrapped(draw,r["text"],(205,958,1715,1038),caption_size,WHITE,bold=visual!="literature",max_lines=2,serif=visual=="literature")
        return img

    def preview_frames(self):
        self.qa_frames.mkdir(parents=True,exist_ok=True); items=[]
        for r in self.records:
            t=(r["audio_start_seconds"]+r["audio_end_seconds"])/2; p=self.qa_frames/f"{r['id']}-{t:07.3f}.png"; self.frame(t).save(p); items.append((r["id"],t,p))
        peak=[r for r in self.records if r["section"]==self.spec["peak_section"]]; center=peak[len(peak)//2]
        for i,q in enumerate((.05,.25,.5,.75,.95),1):
            t=center["audio_start_seconds"]+(center["audio_end_seconds"]-center["audio_start_seconds"])*q; p=self.qa_frames/f"peak-{i}-{t:07.3f}.png"; self.frame(t).save(p); items.append((f"peak-{i}",t,p))
        cols=4; tw,th,lh=480,270,36; rows=math.ceil(len(items)/cols); sheet=Image.new("RGB",(cols*tw,rows*(th+lh)),(4,7,13)); d=ImageDraw.Draw(sheet); f=font(20,bold=True)
        for i,(label,t,p) in enumerate(items):
            x=(i%cols)*tw; y=(i//cols)*(th+lh); im=ImageOps.fit(Image.open(p).convert("RGB"),(tw,th),Image.Resampling.LANCZOS); sheet.paste(im,(x,y)); center_text(d,f"{label} · {t:06.2f}s",(x+tw/2,y+th+18),20,WHITE,bold=True)
        sheet.save(self.preview,quality=94,subsampling=0); print(self.preview)

    def render(self):
        count=math.ceil(self.duration*FPS); audio=self.root/"audio/narration_master.wav"
        cmd=["ffmpeg","-y","-hide_banner","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-i",str(audio),"-map","0:v:0","-map","1:a:0","-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-movflags","+faststart","-shortest",str(self.output)]
        provenance=self.root/"provenance"; provenance.mkdir(parents=True,exist_ok=True)
        renderer_snapshot=provenance/"render.py"; shutil.copy2(Path(__file__).resolve(),renderer_snapshot)
        ffmpeg_version=subprocess.run(["ffmpeg","-version"],check=True,capture_output=True,text=True).stdout.splitlines()[:4]
        environment={"python":sys.version,"platform":platform.platform(),"pillow":PIL.__version__,"ffmpeg":ffmpeg_version,"font_paths":{"sans":FONT_PATH,"mono":MONO_PATH,"serif":SERIF_PATH},"font_sha256":{"sans":sha256(Path(FONT_PATH)),"mono":sha256(Path(MONO_PATH)),"serif":sha256(Path(SERIF_PATH))},"build_command":cmd[:-1]+[self.output.name]}
        environment_path=provenance/"render_environment.json"; environment_path.write_text(json.dumps(environment,indent=2)+"\n")
        proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
        assert proc.stdin is not None
        try:
            for i in range(count):
                proc.stdin.write(self.frame(i/FPS).tobytes())
                if i%300==0: print(f"frame {i}/{count}")
        finally: proc.stdin.close()
        if proc.wait()!=0: raise RuntimeError("ffmpeg encode failed")
        grounded=0.0
        for i,r in enumerate(self.records):
            end=self.records[i+1]["audio_start_seconds"] if i+1<len(self.records) else self.duration; grounded+=max(0,end-r["audio_start_seconds"])
        probe=json.loads(subprocess.run(["ffprobe","-v","error","-count_frames","-show_entries","stream=codec_type,nb_read_frames,duration:format=duration","-of","json",str(self.output)],check=True,capture_output=True,text=True).stdout)
        video_stream=next(s for s in probe["streams"] if s["codec_type"]=="video")
        receipt={"candidate":self.root.name,"output":self.output.name,"output_sha256":sha256(self.output),"output_bytes":self.output.stat().st_size,"renderer":"shared sibling renderer","renderer_path":str(renderer_snapshot.relative_to(self.root)),"renderer_sha256":sha256(renderer_snapshot),"render_environment_path":str(environment_path.relative_to(self.root)),"render_environment_sha256":sha256(environment_path),"spec_sha256":sha256(self.root/"spec.json"),"timeline_sha256":sha256(self.root/"audio/timeline.json"),"audio_master_sha256":sha256(audio),"duration_seconds":self.duration,"fps":FPS,"resolution":[W,H],"raw_frames_submitted":count,"encoded_video_frames":int(video_stream["nb_read_frames"]),"frame_count_semantics":"raw submitted and encoded decoded are separate receipts","source_grounded_runtime_percent":100*grounded/max(self.duration,1),"video_reportable_now":False}
        (self.root/"build_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n"); print(self.output); print(receipt["output_sha256"])


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("candidate_dir"); ap.add_argument("--preview",action="store_true"); ap.add_argument("--render",action="store_true"); a=ap.parse_args()
    if not a.preview and not a.render: raise SystemExit("choose --preview or --render")
    r=Renderer(Path(a.candidate_dir).resolve())
    if a.preview: r.preview_frames()
    if a.render: r.render()
    return 0


if __name__=="__main__": raise SystemExit(main())
