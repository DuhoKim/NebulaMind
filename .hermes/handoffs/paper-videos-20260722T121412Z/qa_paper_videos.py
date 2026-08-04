#!/usr/bin/env python3
"""Deterministic media and semantic QA for the five-paper batch."""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re
import subprocess

from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
SPEC = json.loads((BASE / "paper_video_specs.json").read_text())
BATCH = json.loads((BASE / "batch_build_receipt.json").read_text())
QA = BASE / "qa"
FRAMES = QA / "encoded_frames"
QA.mkdir(exist_ok=True)
FRAMES.mkdir(exist_ok=True)
FONT = ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", 14)
TIMES = [1.2, 7.5, 18.0, 29.5, 41.5, 53.5, 66.0, 73.2]


def capture(command: list[str], *, stderr: bool = False) -> str:
    p = subprocess.run(command, text=True, capture_output=True, check=True)
    return p.stderr if stderr else p.stdout


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def parse_srt(path: Path) -> list[dict]:
    blocks=re.split(r"\n\s*\n",path.read_text().strip())
    rows=[]
    for block in blocks:
        lines=block.splitlines()
        if len(lines)<3: raise RuntimeError(f"malformed SRT block: {block}")
        m=re.fullmatch(r"(\d\d):(\d\d):(\d\d),(\d\d\d) --> (\d\d):(\d\d):(\d\d),(\d\d\d)",lines[1])
        if not m: raise RuntimeError(f"bad SRT timing: {lines[1]}")
        vals=[int(x) for x in m.groups()]
        start=vals[0]*3600+vals[1]*60+vals[2]+vals[3]/1000
        end=vals[4]*3600+vals[5]*60+vals[6]+vals[7]/1000
        rows.append({"index":int(lines[0]),"start":start,"end":end,"text":" ".join(lines[2:])})
    return rows


def loudness(path: Path) -> dict:
    err=capture(["ffmpeg","-hide_banner","-nostats","-i",str(path),"-af","loudnorm=I=-16:LRA=7:TP=-1.5:print_format=json","-f","null","-"],stderr=True)
    m=re.search(r"\{\s*\"input_i\".*?\}",err,re.S)
    if not m: raise RuntimeError(f"no loudnorm JSON for {path}")
    return json.loads(m.group(0))


def scan(path: Path, kind: str) -> list[str]:
    if kind=="black":
        flt="blackdetect=d=0.5:pix_th=0.02"
        pattern=r"black_start:[^\n]+"
    else:
        flt="silencedetect=n=-50dB:d=0.7"
        pattern=r"silence_(?:start|end):[^\n]+"
    err=capture(["ffmpeg","-hide_banner","-nostats","-i",str(path),"-af" if kind=="silence" else "-vf",flt,"-f","null","-"],stderr=True)
    return re.findall(pattern,err)


def extract_frame(video: Path, out: Path, t: float) -> None:
    subprocess.run(["ffmpeg","-y","-v","error","-ss",f"{t:.3f}","-i",str(video),"-frames:v","1",str(out)],check=True)


def make_sheet(paths: list[Path], out: Path, labels: list[str]) -> None:
    sheet=Image.new("RGB",(1280,360),(7,16,31)); d=ImageDraw.Draw(sheet)
    for i,p in enumerate(paths):
        im=Image.open(p).convert("RGB").resize((320,180),Image.Resampling.LANCZOS)
        x,y=(i%4)*320,(i//4)*180
        sheet.paste(im,(x,y)); d.rectangle((x,y,x+319,y+179),outline=(41,70,110),width=2)
        d.rectangle((x+8,y+8,x+100,y+30),fill=(7,16,31)); d.text((x+13,y+10),labels[i],font=FONT,fill=(234,242,255))
    sheet.save(out)


def main() -> None:
    if BATCH.get("marker")!="NEBULAMIND_FIVE_PAPER_VIDEO_BATCH_BUILD_COMPLETE_V1": raise RuntimeError("batch receipt missing")
    papers={p["key"]:p for p in SPEC["papers"]}
    rows=[]; sheets=[]
    for artifact in BATCH["artifacts"]:
        key=artifact["key"]; paper=papers[key]
        video=Path(artifact["path"]); srt=Path(artifact["srt"])
        receipt=json.loads((video.parent/"build_receipt.json").read_text())
        if sha256(video)!=artifact["sha256"] or sha256(video)!=receipt["artifact_sha256"]: raise RuntimeError(f"{key}: video hash mismatch")
        if sha256(srt)!=artifact["srt_sha256"] or sha256(srt)!=receipt["srt_sha256"]: raise RuntimeError(f"{key}: SRT hash mismatch")
        cues=parse_srt(srt)
        if any(c["end"]<=c["start"] for c in cues) or any(b["start"]<a["end"]-0.002 for a,b in zip(cues,cues[1:])): raise RuntimeError(f"{key}: overlapping or invalid cues")
        expected=normalize(" ".join(s["narration"] for s in paper["scenes"]))
        observed=normalize(" ".join(c["text"] for c in cues))
        if observed!=expected: raise RuntimeError(f"{key}: SRT narration mismatch")
        if cues[0]["start"]<2.84 or cues[-1]["end"]>72.31: raise RuntimeError(f"{key}: SRT outside narrated region")
        probe=json.loads(capture(["ffprobe","-v","error","-count_frames","-show_entries","format=duration:stream=index,codec_type,codec_name,profile,width,height,pix_fmt,avg_frame_rate,nb_read_frames,sample_rate,channels","-of","json",str(video)]))
        v=next(s for s in probe["streams"] if s["codec_type"]=="video"); a=next(s for s in probe["streams"] if s["codec_type"]=="audio")
        media_ok=(v["codec_name"]=="h264" and v.get("profile")=="High" and v["width"]==1280 and v["height"]==720 and v["pix_fmt"]=="yuv420p" and v["avg_frame_rate"]=="30/1" and int(v["nb_read_frames"])==2220 and a["codec_name"]=="aac" and a["sample_rate"]=="48000" and a["channels"]==2 and abs(float(probe["format"]["duration"])-74.0)<=0.08)
        if not media_ok: raise RuntimeError(f"{key}: media contract failed: {probe}")
        subprocess.run(["ffmpeg","-v","error","-i",str(video),"-map","0:v:0","-map","0:a:0","-f","null","-"],check=True)
        loud=loudness(video)
        if not (-16.7<=float(loud["input_i"])<=-15.3 and float(loud["input_tp"])<=-1.3): raise RuntimeError(f"{key}: loudness outside target: {loud}")
        blacks=scan(video,"black"); silences=scan(video,"silence")
        frame_paths=[]
        for i,t in enumerate(TIMES):
            p=FRAMES/f"{key}_{i:02d}.png"; extract_frame(video,p,t); frame_paths.append(p)
        sheet=QA/f"{key}_ENCODED_TEMPORAL_SHEET.png"; make_sheet(frame_paths,sheet,[f"{t:.1f}s" for t in TIMES]); sheets.append(sheet)
        extract_frame(video,QA/f"{key}_SCENE1_FULL.png",7.5)
        extract_frame(video,QA/f"{key}_STATUS_FULL.png",66.0)
        rows.append({"key":key,"video":str(video),"sha256":artifact["sha256"],"bytes":video.stat().st_size,"duration":float(probe["format"]["duration"]),"frames":int(v["nb_read_frames"]),"srt_cues":len(cues),"first_cue":cues[0]["start"],"last_cue":cues[-1]["end"],"loudness":loud,"black_events":blacks,"silence_events":silences,"full_decode":"PASS","semantic_srt":"PASS","media_contract":"PASS","encoded_sheet":str(sheet)})
    aggregate=Image.new("RGB",(1280,360*len(sheets)),(7,16,31))
    for i,p in enumerate(sheets): aggregate.paste(Image.open(p).convert("RGB").resize((1280,360),Image.Resampling.LANCZOS),(0,i*360))
    aggregate.save(QA/"FIVE_PAPER_ENCODED_SHEETS.png")
    result={"marker":"NEBULAMIND_FIVE_PAPER_DETERMINISTIC_QA_PASS_V1","paper_count":len(rows),"rows":rows,"aggregate_sheet":str(QA/"FIVE_PAPER_ENCODED_SHEETS.png"),"visual_qa":"pending","asr_qa":"pending","publication_state":"local QA only"}
    (QA/"deterministic_qa.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps(result,indent=2,ensure_ascii=False))


if __name__=="__main__": main()
