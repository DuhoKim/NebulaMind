#!/usr/bin/env python3
import hashlib, json, pathlib, re, subprocess
from PIL import Image, ImageDraw, ImageFont

HANDOFF=pathlib.Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K')
OUT=HANDOFF/'integrator/tori-hwao-fix-review-20260809T1337K'
CASES={
 'mzr-census':('integrator/canaries/mzr-census-method-overhaul-canary-20260809T0320K/mzr-census-method-overhaul-canary-20260809T0320K.mp4','d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b',109.0,130.0),
 'fesc':('integrator/canaries/fesc-method-overhaul-canary-20260809T0327K/fesc-method-overhaul-canary-20260809T0327K.mp4','47eb0d0b151b51667a4b29a39da74b947086c925dda7ce7e819240ffde25e42d',60.0,109.0),
 'brightend':('integrator/canaries/brightend-method-overhaul-canary-20260809T0337K/brightend-method-overhaul-canary-20260809T0337K.mp4','6e0f4b098d6c5386d08ab7fb670b8b6564e257edeac5dc1c6fec2cc6b97bc7b4',59.0,107.0),
}
FONT='/System/Library/Fonts/Menlo.ttc'

def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()

def sheet(paths,out,prefix):
 font=ImageFont.truetype(FONT,22)
 pages=[]
 for page_start in range(0,len(paths),20):
  batch=paths[page_start:page_start+20]
  canvas=Image.new('RGB',(2400,1160),(0,0,0)); d=ImageDraw.Draw(canvas)
  for j,(path,t) in enumerate(batch):
   im=Image.open(path).convert('RGB'); im.thumbnail((472,266),Image.Resampling.LANCZOS)
   x=(j%5)*480+4; y=(j//5)*290+4
   canvas.paste(im,(x,y)); d.text((x+8,y+268),f'{t:07.2f}s',font=font,fill=(255,255,255))
  dest=out/f'{prefix}-{page_start//20+1:02d}.jpg'; canvas.save(dest,quality=94,subsampling=0); pages.append(dest)
 return pages

def cyan_blob_scan(path):
 im=Image.open(path).convert('RGB')
 # Strict interior of the bright-end evidence plane; excludes external provenance flow and axes labels.
 x0,y0,x1,y1=1290,335,1880,690
 pix=im.load()
 if pix is None: raise RuntimeError(f'cannot access pixels: {path}')
 mask=set()
 for y in range(y0,y1):
  for x in range(x0,x1):
   r,g,b=pix[x,y]
   if r<105 and g>175 and b>190: mask.add((x,y))
 comps=[]
 while mask:
  seed=mask.pop(); stack=[seed]; pts=[seed]
  while stack:
   x,y=stack.pop()
   for q in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
    if q in mask: mask.remove(q);stack.append(q);pts.append(q)
  xs=[p[0] for p in pts];ys=[p[1] for p in pts]
  w=max(xs)-min(xs)+1;h=max(ys)-min(ys)+1
  if len(pts)>=30 and 5<=w<=35 and 5<=h<=35: comps.append({'area':len(pts),'bbox':[min(xs),min(ys),max(xs),max(ys)]})
 return comps

def main():
 OUT.mkdir(parents=True,exist_ok=True); report={'sampling_fps':2,'cases':{}}
 for lane,(rel,expected,start,end) in CASES.items():
  video=HANDOFF/rel; actual=sha(video)
  if actual!=expected: raise RuntimeError(f'{lane} hash drift {actual}')
  frame_dir=OUT/'frames'/lane; frame_dir.mkdir(parents=True,exist_ok=True)
  subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(video),'-vf','fps=2','-q:v','2',str(frame_dir/'frame-%06d.jpg')],check=True)
  frames=sorted(frame_dir.glob('frame-*.jpg'))
  timed=[(p,(int(p.stem.split('-')[1])-1)/2.0) for p in frames]
  risk=[x for x in timed if start<=x[1]<=end]
  full=[x for i,x in enumerate(timed) if i%10==0]
  lane_out=OUT/'sheets'/lane;lane_out.mkdir(parents=True,exist_ok=True)
  risk_pages=sheet(risk,lane_out,'risk-2fps')
  full_pages=sheet(full,lane_out,'full-sweep-5s')
  findings={'video_sha256':actual,'decoded_2fps_frames':len(frames),'risk_interval_seconds':[start,end],'risk_frames':len(risk),'risk_pages':[str(p.relative_to(OUT)) for p in risk_pages],'full_pages':[str(p.relative_to(OUT)) for p in full_pages]}
  if lane=='mzr-census':
   hits={term:[] for term in ('178','21','157')}
   for p,t in risk:
    text=subprocess.run(['tesseract',str(p),'stdout'],capture_output=True,text=True).stdout
    norm=' '.join(text.split())
    for term in hits:
     if re.search(rf'(?<!\d){re.escape(term)}(?!\d)',norm): hits[term].append({'time':t,'text':norm})
   findings['forbidden_count_ocr_hits']=hits
  if lane=='brightend':
   blobs=[]
   for p,t in risk:
    comps=cyan_blob_scan(p)
    if comps:blobs.append({'time':t,'components':comps})
   findings['in_plane_cyan_point_like_components']=blobs
  report['cases'][lane]=findings
 (OUT/'FRAME_INDEX.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'out':str(OUT),'index_sha256':sha(OUT/'FRAME_INDEX.json'),'counts':{k:v['decoded_2fps_frames'] for k,v in report['cases'].items()},'risk_counts':{k:v['risk_frames'] for k,v in report['cases'].items()},'mzr_ocr_hits':report['cases']['mzr-census']['forbidden_count_ocr_hits'],'bright_point_like_hits':len(report['cases']['brightend']['in_plane_cyan_point_like_components'])},indent=2))

if __name__=='__main__':main()
